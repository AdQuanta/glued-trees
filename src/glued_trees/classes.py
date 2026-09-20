"""Canonical glued-trees graph models and continuous-time walk Hamiltonians.

Degenerate eigenspaces in ``infinite_time_average_layer_distribution`` are
identified with an absolute eigenvalue tolerance of ``1e-10``.
"""

from functools import cached_property
from numbers import Integral, Real
from typing import Any, Literal
import itertools

import networkx as nx
import numpy as np
from scipy.sparse import csr_array, diags

from qutip import Qobj, Result, basis, sesolve


HamiltonianConvention = Literal["adjacency", "laplacian"]
DEGENERACY_ABSOLUTE_TOLERANCE = 1e-10


class GluedTrees:
    def __init__(
        self,
        *,
        L: int,
        J_GT: float,
        hamiltonian_convention: HamiltonianConvention = "laplacian",
        rng: np.random.Generator | int = 0,
    ):
        self.L = _validate_depth(L)
        self.J_GT = _validate_nonnegative_real(J_GT, "J_GT")
        self.hamiltonian_convention = _validate_hamiltonian_convention(
            hamiltonian_convention
        )
        self.rng = _parse_rng(rng)
        self.graph, self.left_tree, self.right_tree = self.construct_glued_trees_graph()
        self.N = len(self.graph)

    @property
    def num_layers(self) -> int:
        return 2 * (self.L + 1)

    @cached_property
    def node_positions(self) -> dict[int, tuple[float, float]]:
        """Lay out the two glued trees with Graphviz once and reuse it."""
        left_positions = nx.nx_agraph.graphviz_layout(self.left_tree, prog="dot")
        right_positions = {
            self.N - node - 1: (x, -y - 100)
            for node, (x, y) in left_positions.items()
        }
        return {**left_positions, **right_positions}

    def construct_glued_trees_graph(self) -> tuple[nx.Graph, nx.Graph, nx.Graph]:
        """Construct the two-tree backbone with two distinct edges per leaf."""
        left_tree = nx.balanced_tree(2, self.L)
        tree_size = len(left_tree)
        right_tree = nx.Graph()
        right_tree.add_nodes_from(sorted(left_tree.nodes, reverse=True))
        right_tree.add_edges_from(left_tree.edges)
        graph = nx.disjoint_union(left_tree, right_tree)

        left_leaves = list(range(tree_size - 2**self.L, tree_size))
        right_leaves = list(range(tree_size, tree_size + 2**self.L))
        first_matching = right_leaves.copy()
        second_matching = right_leaves.copy()
        self.rng.shuffle(first_matching)
        self.rng.shuffle(second_matching)
        while not all(first != second for first, second in zip(first_matching, second_matching)):
            self.rng.shuffle(second_matching)

        graph.add_edges_from(
            list(zip(left_leaves, first_matching))
            + list(zip(left_leaves, second_matching))
        )
        nx.set_edge_attributes(graph, self.J_GT, "weight")
        return graph, left_tree, right_tree

    def _hamiltonian_graph(self) -> nx.Graph:
        return self.graph

    def get_hamiltonian(self, sparse: bool = False) -> np.ndarray | csr_array:
        """Return ``-A_J + V_dis`` or ``D_J - A_J + V_dis`` as configured."""
        adjacency = nx.to_scipy_sparse_array(
            self._hamiltonian_graph(),
            nodelist=range(self.N),
            weight="weight",
            dtype=float,
            format="csr",
        )
        if self.hamiltonian_convention == "adjacency":
            hamiltonian = -adjacency
        else:
            strengths = np.asarray(adjacency.sum(axis=1)).ravel()
            hamiltonian = diags(strengths, format="csr") - adjacency

        epsilon = self._disorder_energies()
        if np.any(epsilon):
            hamiltonian = hamiltonian + diags(epsilon, format="csr")
        return hamiltonian if sparse else hamiltonian.toarray()

    def _disorder_energies(self) -> np.ndarray:
        return np.zeros(self.N)

    def compute_spectrum(self) -> tuple[np.ndarray, np.ndarray]:
        return np.linalg.eigh(self.get_hamiltonian())

    def _layer_indices(self, layer_idx: int) -> tuple[int, int]:
        if layer_idx <= self.L:
            return 2**layer_idx - 1, 2 ** (layer_idx + 1) - 1
        if layer_idx <= 2 * self.L + 1:
            inverse_layer_idx = 2 * self.L + 1 - layer_idx
            return (
                self.N - 2 ** (inverse_layer_idx + 1) + 1,
                self.N - 2**inverse_layer_idx + 1,
            )
        raise ValueError("Invalid layer index.")

    def get_layer_distribution(self, psi: Qobj) -> np.ndarray:
        psi_vector = psi.full()[:, 0]
        layer_distribution = np.zeros(self.num_layers)
        for layer_idx in range(self.num_layers):
            start_idx, end_idx = self._layer_indices(layer_idx)
            layer_distribution[layer_idx] = np.sum(
                np.abs(psi_vector[start_idx:end_idx]) ** 2
            )
        return layer_distribution

    def infinite_time_average_layer_distribution(self) -> np.ndarray:
        """Return the entrance-state infinite-time layer distribution.

        For every eigenvalue group within ``DEGENERACY_ABSOLUTE_TOLERANCE``,
        this evaluates ``<IN| P_g Pi_layer P_g |IN>`` using the full spectral
        projector. This is independent of the arbitrary basis returned for a
        degenerate eigenspace.
        """
        eigenvalues, eigenvectors = self.compute_spectrum()
        return self._infinite_time_distribution_from_eigensystem(
            eigenvalues,
            eigenvectors,
            degeneracy_tolerance=DEGENERACY_ABSOLUTE_TOLERANCE,
        )

    def _infinite_time_distribution_from_eigensystem(
        self,
        eigenvalues: np.ndarray,
        eigenvectors: np.ndarray,
        *,
        degeneracy_tolerance: float,
    ) -> np.ndarray:
        layer_distribution = np.zeros(self.num_layers)
        for group_start, group_end in _degenerate_eigenvalue_groups(
            eigenvalues, degeneracy_tolerance
        ):
            eigenvectors_group = eigenvectors[:, group_start:group_end]
            projected_entrance = eigenvectors_group @ np.conj(eigenvectors_group[0, :])
            for layer_idx in range(self.num_layers):
                start_idx, end_idx = self._layer_indices(layer_idx)
                layer_distribution[layer_idx] += np.sum(
                    np.abs(projected_entrance[start_idx:end_idx]) ** 2
                )
        return layer_distribution

    def get_layer_state(self, layer_idx: int) -> np.ndarray:
        psi = np.zeros(self.N)
        start_idx, end_idx = self._layer_indices(layer_idx)
        psi[start_idx:end_idx] = 1 / np.sqrt(end_idx - start_idx)
        return psi

    def time_evolution(
        self,
        tmax: float,
        dt: float,
        psi0: np.ndarray | None = None,
        prog_bar: bool = True,
    ) -> Result:
        psi0_qt = basis(self.N, 0) if psi0 is None else Qobj(psi0)
        options = {"progress_bar": "tqdm"} if prog_bar else {}
        return sesolve(
            Qobj(self.get_hamiltonian()),
            psi0_qt,
            tlist=np.arange(0, tmax, dt),
            options=options,
        )

    def plot_graph_on_ax(self, ax, node_vals: np.ndarray | None = None):
        pos = self.node_positions
        nx.draw_networkx_edges(self.graph, pos, ax=ax, alpha=0.2)
        nx.draw_networkx_nodes(
            self.graph,
            pos,
            ax=ax,
            node_size=1,
            node_color="black",
            edgecolors="black",
            alpha=0.2,
        )

    def plot_spectrum(self):
        from matplotlib import pyplot as plt

        _, eigenvectors = self.compute_spectrum()
        fig, axes = plt.subplots(1, 2, figsize=(12, 8), dpi=100)
        self.plot_graph_on_ax(axes[0], node_vals=eigenvectors[:, 0])
        self.plot_graph_on_ax(axes[1], node_vals=eigenvectors[:, -1])
        plt.tight_layout()
        plt.show()

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "L": self.L,
            "J_GT": self.J_GT,
            "hamiltonian_convention": self.hamiltonian_convention,
            "graph": self.graph,
            "left_tree": self.left_tree,
            "right_tree": self.right_tree,
            "N": self.N,
        }


class DisorderedGluedTrees(GluedTrees):
    def __init__(
        self,
        *,
        L: int,
        J_GT: float,
        W: float,
        hamiltonian_convention: HamiltonianConvention = "laplacian",
        rng: np.random.Generator | int = 0,
    ):
        super().__init__(
            L=L,
            J_GT=J_GT,
            hamiltonian_convention=hamiltonian_convention,
            rng=rng,
        )
        self.W = _validate_nonnegative_real(W, "W")
        self.epsilon = self.rng.uniform(-self.W, self.W, self.N)

    def _disorder_energies(self) -> np.ndarray:
        return self.epsilon

    @property
    def parameters(self) -> dict[str, Any]:
        return {**super().parameters, "W": self.W, "epsilon": self.epsilon}


class AllToAllGluedTrees(DisorderedGluedTrees):
    def __init__(
        self,
        *,
        L: int,
        J_GT: float,
        J_LR: float,
        W: float,
        hamiltonian_convention: HamiltonianConvention = "laplacian",
        rng: np.random.Generator | int = 0,
    ):
        super().__init__(
            L=L,
            J_GT=J_GT,
            W=W,
            hamiltonian_convention=hamiltonian_convention,
            rng=rng,
        )
        self.J_LR = _validate_nonnegative_real(J_LR, "J_LR")
        self.protected_graph = self.construct_all_to_all_graph()

    def construct_all_to_all_graph(self) -> nx.Graph:
        protected_graph = self.graph.copy()
        for layer_idx in range(self.num_layers):
            start_idx, end_idx = self._layer_indices(layer_idx)
            for node_u, node_v in itertools.combinations(range(start_idx, end_idx), 2):
                protected_graph.add_edge(node_u, node_v, weight=self.J_LR)
        return protected_graph

    def _hamiltonian_graph(self) -> nx.Graph:
        return self.protected_graph

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            **super().parameters,
            "J_LR": self.J_LR,
            "protected_graph": self.protected_graph,
        }


class IndependentEdgeGluedTrees(DisorderedGluedTrees):
    def __init__(
        self,
        *,
        L: int,
        J_GT: float,
        J_LR: float,
        p: float,
        add_path_edges: bool,
        W: float,
        hamiltonian_convention: HamiltonianConvention = "laplacian",
        rng: np.random.Generator | int = 0,
    ):
        super().__init__(
            L=L,
            J_GT=J_GT,
            W=W,
            hamiltonian_convention=hamiltonian_convention,
            rng=rng,
        )
        self.J_LR = _validate_nonnegative_real(J_LR, "J_LR")
        self.p = _validate_probability(p)
        if not isinstance(add_path_edges, bool):
            raise TypeError("add_path_edges must be a bool.")
        self.add_path_edges = add_path_edges
        self.protected_graph = self.construct_independent_edge_graph()

    def construct_independent_edge_graph(self) -> nx.Graph:
        protected_graph = self.graph.copy()
        for layer_idx in range(1, self.num_layers - 1):
            start_idx, end_idx = self._layer_indices(layer_idx)
            if self.add_path_edges:
                for node in range(start_idx, end_idx - 1):
                    protected_graph.add_edge(node, node + 1, weight=self.J_LR)

            layer_edges = np.array(list(itertools.combinations(range(start_idx, end_idx), 2)))
            if len(layer_edges):
                edges_to_add = layer_edges[self.rng.random(len(layer_edges)) < self.p]
                protected_graph.add_edges_from(edges_to_add, weight=self.J_LR)
        return protected_graph

    def _hamiltonian_graph(self) -> nx.Graph:
        return self.protected_graph

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            **super().parameters,
            "J_LR": self.J_LR,
            "p": self.p,
            "add_path_edges": self.add_path_edges,
            "protected_graph": self.protected_graph,
        }


def _degenerate_eigenvalue_groups(
    eigenvalues: np.ndarray, tolerance: float
) -> list[tuple[int, int]]:
    """Return consecutive groups whose values differ by an absolute tolerance."""
    if tolerance < 0:
        raise ValueError("degeneracy tolerance must be nonnegative.")
    groups = []
    group_start = 0
    for index in range(1, len(eigenvalues)):
        if abs(eigenvalues[index] - eigenvalues[group_start]) > tolerance:
            groups.append((group_start, index))
            group_start = index
    groups.append((group_start, len(eigenvalues)))
    return groups


def _validate_depth(L: int) -> int:
    if not isinstance(L, Integral) or isinstance(L, bool):
        raise TypeError("L must be an integer.")
    if L < 1:
        raise ValueError("L must be at least 1 so every leaf can have two distinct gluing edges.")
    return int(L)


def _validate_nonnegative_real(value: float, name: str) -> float:
    if not isinstance(value, Real) or isinstance(value, bool):
        raise TypeError(f"{name} must be a real number.")
    if not np.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative.")
    return float(value)


def _validate_probability(p: float) -> float:
    p = _validate_nonnegative_real(p, "p")
    if p > 1:
        raise ValueError("p must be between 0 and 1.")
    return p


def _validate_hamiltonian_convention(
    hamiltonian_convention: str,
) -> HamiltonianConvention:
    if hamiltonian_convention not in {"adjacency", "laplacian"}:
        raise ValueError("hamiltonian_convention must be 'adjacency' or 'laplacian'.")
    return hamiltonian_convention


def _parse_rng(rng: np.random.Generator | int) -> np.random.Generator:
    if isinstance(rng, Integral) and not isinstance(rng, bool):
        return np.random.default_rng(rng)
    if isinstance(rng, np.random.Generator):
        return rng
    raise TypeError("rng must be an int or a numpy random Generator.")
