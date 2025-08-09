from typing import Any
import itertools
from functools import cached_property
import logging


import networkx as nx
import numpy as np
from tqdm import tqdm

from qutip import basis, Qobj, sesolve, Result


class GluedTrees:
    def __init__(self, h: int, J: float, rng:np.random.Generator|int=0):
        self.rng : np.random.Generator = _parse_rng(rng)
        self.h = h  # Tree height
        self.J = J  # Interaction strength
        self.T, self.T1, self.T2 = self.construct_glued_trees_graph()
        self.N = len(self.T)

    @property
    def num_layers(self) -> int:
        return 2 * (self.h + 1)
    
    @cached_property
    def node_positions(self) -> dict[int, tuple[float, float]]:
        """
        Lay out the two glued trees with Graphviz *once* and reuse it.

        Returns
        -------
        dict[int, tuple[float, float]]
            Mapping  node_id → (x, y)  coordinates for *both* trees.
        """
        # --- First tree ---------------------------------------------------
        pos_T1 = nx.nx_agraph.graphviz_layout(self.T1, prog="dot")

        # --- Mirror it to obtain the second tree -------------------------
        pos_T2 = {
            self.N - k - 1: (x, -y - 100)     # drop 100 px in the y-direction
            for k, (x, y) in pos_T1.items()
        }

        # --- Merge and return -------------------------------------------
        return {**pos_T1, **pos_T2}

    def construct_glued_trees_graph(self) -> tuple[nx.Graph, nx.Graph, nx.Graph]:
        rng = self.rng

        # Create a union of two binary trees
        T1 = nx.balanced_tree(2, self.h)
        N_tree = len(T1)
        T2 = nx.Graph()
        T2.add_nodes_from(sorted(T1.nodes, reverse=True))
        T2.add_edges_from(T1.edges)
        T = nx.disjoint_union(T1, T2)

        # "Glue" the trees together by adding random connections between the leaves
        T1_leaf_nodes = list(range(N_tree - 2 ** self.h, N_tree))
        T2_leaf_nodes = list(range(N_tree, N_tree + 2 ** self.h))
        T2_mix_1 = T2_leaf_nodes.copy()
        rng.shuffle(T2_mix_1)
        T2_mix_2 = T2_leaf_nodes.copy()
        rng.shuffle(T2_mix_2)
        if self.h > 0:
            while not all(u != v for u, v in zip(T2_mix_1, T2_mix_2)):
                rng.shuffle(T2_mix_2)
        T.add_edges_from(list(zip(T1_leaf_nodes, T2_mix_1)) + list(zip(T1_leaf_nodes, T2_mix_2)))

        return T, T1, T2

    def get_hamiltonian(self) -> np.ndarray:
        return self.J * nx.adjacency_matrix(self.T).toarray()

    def compute_spectrum(self) -> tuple[np.ndarray, np.ndarray]:
        [E, v] = np.linalg.eigh(self.get_hamiltonian())
        return E, v

    def _layer_indices(self, layer_idx: int) -> tuple[int, int]:
        # Layer before gluing
        if layer_idx <= self.h:
            return 2 ** layer_idx - 1, 2 ** (layer_idx + 1) - 1

        # Layer after gluing
        elif layer_idx <= 2 * self.h + 1:
            inv_layer_idx = 2 * self.h + 1 - layer_idx
            return self.N - 2 ** (inv_layer_idx + 1) + 1, self.N - 2 ** inv_layer_idx + 1

        else:
            raise ValueError("Invalid layer index.")

    def get_layer_distribution(self, psi: Qobj) -> np.ndarray:
        psi_vec = psi.full()[:, 0]
        layer_distribution = np.zeros(2 * (self.h + 1))
        for layer_idx in range(2 * (self.h + 1)):
            start_idx, end_idx = self._layer_indices(layer_idx)
            layer_distribution[layer_idx] = np.sum(np.abs(psi_vec[start_idx:end_idx]) ** 2)
        return layer_distribution

    def average_layer_distribution(self) -> np.ndarray:
        layer_distribution = np.zeros(2 * (self.h + 1))
        _, v = self.compute_spectrum()

        # For a single layer
        np.sum(np.abs(v[0, :]) ** 2 * np.abs(v[-1, :]) ** 2)

        for layer_idx in range(2 * (self.h + 1)):
            start_idx, end_idx = self._layer_indices(layer_idx)
            layer_distribution[layer_idx] = np.sum(np.abs(v[0, :]) ** 2 * np.abs(v[start_idx:end_idx, :]) ** 2)

        return layer_distribution

    def get_layer_state(self, layer_idx: int) -> np.ndarray:
        psi = np.zeros(self.N)
        start_idx, end_idx = self._layer_indices(layer_idx)
        psi[start_idx:end_idx] = 1 / np.sqrt(end_idx - start_idx)
        return psi

    def time_evolution(self, tmax: float, dt: float, psi0: np.ndarray|None = None, prog_bar:bool=True) -> Result:
        if psi0 is None:
            # Single-excitation at the entrance root node
            psi0_qt = basis(self.N, 0)
        else:
            psi0_qt = Qobj(psi0)
        H_qt = Qobj(self.get_hamiltonian())

        if prog_bar:
            options={"progress_bar": "tqdm"}
        else:
            options={}

        res = sesolve(H_qt, psi0_qt, tlist=np.arange(0, tmax, dt), options=options)
        return res

    def plot_graph_on_ax(self, ax, node_vals: np.ndarray|None = None):
        # Get positions (cached property):
        pos = self.node_positions  # first access computes, then cached
        # Draw the basics:
        nx.draw_networkx_edges(self.T, pos, ax=ax, alpha=0.2)
        nx.draw_networkx_nodes(self.T, pos, ax=ax, node_size=1, node_color="black", edgecolors="black", alpha=0.2)


    def plot_spectrum(self):
        # in-fucntion import. no need for speed, but we don't want to require matplotlib if no-one uses it
        from matplotlib import pyplot as plt

        E, v = self.compute_spectrum()

        # Plot most interesting eigenvectors
        fig, ax = plt.subplots(1, 2, figsize=(12, 8), dpi=100)
        self.plot_graph_on_ax(ax[0], node_vals=v[:, 0])
        self.plot_graph_on_ax(ax[1], node_vals=v[:, -1])
        plt.tight_layout()
        plt.show()

    @property
    def parameters(self) -> dict[str, Any]:
        """
        Get the parameters of the model.
        """
        d : dict= {
            'h': self.h,
            'J': self.J,
            'T': self.T,
            'T1': self.T1,
            'T2': self.T2,
            'N': self.N
        }
        return d


class GluedTreesDisorder(GluedTrees):
    def __init__(self, h: int, J: float, sigma: float, distribution: str, rng: np.random.Generator|int=0):
        super().__init__(h, J, rng=rng)
        self.sigma = sigma
        self.distribution = distribution
        self.omegas = self._generate_disorder(sigma, distribution)

    def _generate_disorder(self, sigma: float, distribution: str) -> np.ndarray:
        rng = self.rng
        if distribution == "uniform":
            bw = np.sqrt(3) * sigma
            omegas = rng.uniform(-bw, bw, self.N)
        elif distribution == "gaussian":
            omegas = sigma * rng.standard_normal(self.N)
        elif distribution == "lorentzian":
            omegas = rng.standard_cauchy(self.N)  # TODO add FWHM
        else:
            raise ValueError("Invalid distribution type.")

        return omegas

    def get_hamiltonian(self) -> np.ndarray:
        return self.J * nx.adjacency_matrix(self.T).toarray() + np.diag(self.omegas)
    
    @property
    def parameters(self) -> dict[str, Any]:
        """
        Get the parameters of the model.
        """
        d : dict= super().parameters
        d['sigma'] = self.sigma
        d['distribution'] = self.distribution
        d['omegas'] = self.omegas
        return d


class GluedTreesAllToAll(GluedTreesDisorder):
    def __init__(self, h: int, J: float, J2: float, sigma: float, distribution: str):
        super().__init__(h, J, sigma, distribution)
        self.J2 = J2
        self.Taa = self.construct_all_to_all_graph()

    def construct_all_to_all_graph(self) -> nx.Graph:
        Taa = self.T.copy()
        nx.set_edge_attributes(Taa, self.J, "weight")

        # Add all-to-all connections between nodes in the same layer
        for layer_idx in range(2 * (self.h + 1)):
            start_idx, end_idx = self._layer_indices(layer_idx)
            w = self.J2
            if 0 < layer_idx <= self.h:
                w /= 2 ** layer_idx - 1
            elif self.h < layer_idx < 2 * self.h + 1:
                w /= 2 ** (2 * self.h + 1 - layer_idx) - 1
            for u, v in itertools.combinations(range(start_idx, end_idx), 2):
                Taa.add_edge(u, v, weight=w)

        # Add self edges at the boundaries
        Taa.add_edge(0, 0, weight=self.J2)
        Taa.add_edge(self.N - 1, self.N - 1, weight=self.J2)

        return Taa

    def get_hamiltonian(self) -> np.ndarray:
        return nx.adjacency_matrix(self.Taa).toarray() + np.diag(self.omegas)


class GluedTreesSmallWorld(GluedTreesDisorder):
    def __init__(
        self, 
        h: int,    # Tree height
        J: float,  # Interaction strength
        p: float,  #
        nn: bool, 
        sigma: float, 
        distribution: str,
        rng: np.random.Generator|int=0,
    ):
        super().__init__(h, J, sigma, distribution, rng=rng)
        self.p = p
        self.nn = nn
        self.Tsw = self.construct_small_world_graph()

    def construct_small_world_graph(self) -> nx.Graph:
        rng = self.rng

        Tsw = self.T.copy()
        nx.set_edge_attributes(Tsw, self.J, "weight")
        
        layers_without_entrance_and_exit = range(1, self.num_layers-1)
        for layer_idx in layers_without_entrance_and_exit:
            start_idx, end_idx = self._layer_indices(layer_idx)

            # Add nearest-neighbor connections
            if self.nn:
                for u in range(start_idx, end_idx - 1):
                    Tsw.add_edge(u, u + 1, weight=self.J)

            # Add small-world connections w. probability p
            layer_edges = np.array(list(itertools.combinations(range(start_idx, end_idx), 2)))
            connection_probs = rng.random(len(layer_edges))
            edges_to_add = layer_edges[connection_probs < self.p]
            Tsw.add_edges_from(edges_to_add, weight=self.J)

        return Tsw

    def get_hamiltonian(self) -> np.ndarray:
        return nx.laplacian_matrix(self.Tsw).toarray() + np.diag(self.omegas)
    
    @property
    def parameters(self) -> dict[str, Any]:
        """
        Get the parameters of the model.
        """
        d : dict= super().parameters
        d['p'] = self.p
        d['nn'] = self.nn
        d['Tsw'] = self.Tsw
        return d



def _parse_rng(rng: np.random.Generator|int) -> np.random.Generator:
    if isinstance(rng, int):
        return np.random.default_rng(rng)
    elif isinstance(rng, np.random.Generator):
        return rng
    else:
        raise TypeError("rng must be an int or a numpy random Generator.")