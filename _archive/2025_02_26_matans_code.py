import itertools
import logging

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from tqdm import tqdm

from qutip import *

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize RNG seed for reproducibility
rng = np.random.default_rng(0)

# Set default plot parameters
plt.rcParams["font.size"] = 12
plt.rcParams["font.sans-serif"] = "Arial"


class GluedTrees:
    def __init__(self, h: int, J: float):
        self.h = h  # Tree height
        self.J = J  # Interaction strength
        self.T, self.T1, self.T2 = self.construct_glued_trees_graph()
        self.N = len(self.T)

    def construct_glued_trees_graph(self) -> (nx.Graph, nx.Graph, nx.Graph):
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

    def get_hamiltonian(self) -> np.array:
        return self.J * nx.adjacency_matrix(self.T).toarray()

    def compute_spectrum(self) -> (np.array, np.array):
        [E, v] = np.linalg.eigh(self.get_hamiltonian())
        return E, v

    def _layer_indices(self, layer_idx: int) -> (int, int):
        # Layer before gluing
        if layer_idx <= self.h:
            return 2 ** layer_idx - 1, 2 ** (layer_idx + 1) - 1

        # Layer after gluing
        elif layer_idx <= 2 * self.h + 1:
            inv_layer_idx = 2 * self.h + 1 - layer_idx
            return self.N - 2 ** (inv_layer_idx + 1) + 1, self.N - 2 ** inv_layer_idx + 1

        else:
            raise ValueError("Invalid layer index.")

    def get_layer_distribution(self, psi: Qobj) -> np.array:
        psi_vec = psi.full()[:, 0]
        layer_distribution = np.zeros(2 * (self.h + 1))
        for layer_idx in range(2 * (self.h + 1)):
            start_idx, end_idx = self._layer_indices(layer_idx)
            layer_distribution[layer_idx] = np.sum(np.abs(psi_vec[start_idx:end_idx]) ** 2)
        return layer_distribution

    def average_layer_distribution(self) -> np.array:
        layer_distribution = np.zeros(2 * (self.h + 1))
        _, v = self.compute_spectrum()

        # For a single layer
        np.sum(np.abs(v[0, :]) ** 2 * np.abs(v[-1, :]) ** 2)

        for layer_idx in range(2 * (self.h + 1)):
            start_idx, end_idx = self._layer_indices(layer_idx)
            layer_distribution[layer_idx] = np.sum(np.abs(v[0, :]) ** 2 * np.abs(v[start_idx:end_idx, :]) ** 2)

        return layer_distribution

    def get_layer_state(self, layer_idx: int) -> np.array:
        psi = np.zeros(self.N)
        start_idx, end_idx = self._layer_indices(layer_idx)
        psi[start_idx:end_idx] = 1 / np.sqrt(end_idx - start_idx)
        return psi

    def time_evolution(self, tmax: float, dt: float, psi0: np.array = None) -> Result:
        if psi0 is None:
            # Single-excitation at the entrance root node
            psi0_qt = basis(self.N, 0)
        else:
            psi0_qt = Qobj(psi0)
        H_qt = Qobj(self.get_hamiltonian())
        res = sesolve(H_qt, psi0_qt, tlist=np.arange(0, tmax, dt), options={"progress_bar": "tqdm"})

        # Visualize state graphs
        for idx, t in enumerate(res.times):
            fig, ax = plt.subplots(1, 1, figsize=(8, 6), dpi=100)
            self.plot_graph_on_ax(ax, res.states[idx].full()[:, 0])
            ax.set_title(f"t = {t:.1f}")
            plt.tight_layout()
            plt.show()

        # Visualize layer distribution over time
        cmap = plt.get_cmap("rainbow")
        fig, ax = plt.subplots(1, 1, figsize=(8, 6), dpi=300)
        for idx, t in enumerate(res.times):
            layer_distribution = self.get_layer_distribution(res.states[idx])
            ax.stairs(layer_distribution, np.arange(2 * (self.h + 1) + 1), color=cmap(idx / len(res.times)), fill=True,
                      alpha=0.8)
        ax.set_xlabel("Layer index")
        ax.set_ylabel("Population")
        ax.tick_params(axis="both", which="major")
        plt.tight_layout()
        plt.show()

        return res

    def plot_graph_on_ax(self, ax, node_vals: np.array = None):
        pos_T1 = nx.nx_agraph.graphviz_layout(self.T1, prog="dot")
        pos_T2 = {self.N - k - 1: np.array([x, -y - 100]) for k, (x, y) in pos_T1.items()}
        pos = pos_T1.copy()
        pos.update(pos_T2)
        if node_vals is not None:
            nx.draw_networkx_nodes(self.T, pos, ax=ax, node_size=50,
                                   node_color=np.angle(node_vals / node_vals[0]), vmin=-np.pi, vmax=np.pi,
                                   alpha=np.minimum(1, 0.25 * np.abs(node_vals) ** 2 * self.N), edgecolors="black",
                                   cmap="hsv")
        else:
            nx.draw_networkx_nodes(self.T, pos, ax=ax, node_size=50, node_color="skyblue", edgecolors="black")
        nx.draw_networkx_edges(self.T, pos, ax=ax, alpha=0.2)

    def plot_spectrum(self):
        E, v = self.compute_spectrum()

        # Plot most interesting eigenvectors
        fig, ax = plt.subplots(1, 2, figsize=(12, 8), dpi=100)
        self.plot_graph_on_ax(ax[0], node_vals=v[:, 0])
        self.plot_graph_on_ax(ax[1], node_vals=v[:, -1])
        plt.tight_layout()
        plt.show()


class GluedTreesDisorder(GluedTrees):
    def __init__(self, h: int, J: float, sigma: float, distribution: str):
        super().__init__(h, J)
        self.sigma = sigma
        self.distribution = distribution
        self.omegas = self._generate_disorder(sigma, distribution)

    def _generate_disorder(self, sigma: float, distribution: str) -> np.array:
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

    def get_hamiltonian(self) -> np.array:
        return self.J * nx.adjacency_matrix(self.T).toarray() + np.diag(self.omegas)


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

    def get_hamiltonian(self) -> np.array:
        return nx.adjacency_matrix(self.Taa).toarray() + np.diag(self.omegas)


class GluedTreesSmallWorld(GluedTreesDisorder):
    def __init__(self, h: int, J: float, p: float, nn: bool, sigma: float, distribution: str):
        super().__init__(h, J, sigma, distribution)
        self.p = p
        self.nn = nn
        self.Tsw = self.construct_small_world_graph()

    def construct_small_world_graph(self) -> nx.Graph:
        Tsw = self.T.copy()
        nx.set_edge_attributes(Tsw, self.J, "weight")

        for layer_idx in range(1, 2 * self.h + 1):
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

    def get_hamiltonian(self) -> np.array:
        return nx.laplacian_matrix(self.Tsw).toarray() + np.diag(self.omegas)


# Test for myself
if __name__ == "__main__":
    J = -1.  # Coupling strength
    J2 = -1.  # All-to-all coupling strength
    p = 1.  # Small-world connection probability
    sigma = 1.  # Disorder strength

    gt = GluedTreesSmallWorld(4, J, p, False, sigma, distribution="gaussian")
    gt.time_evolution(40, 4)

    pass
