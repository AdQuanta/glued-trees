import inspect
from pathlib import Path
import re
import unittest

import networkx as nx
import numpy as np

from src.glued_trees import (
    AllToAllGluedTrees,
    DisorderedGluedTrees,
    GluedTrees,
    IndependentEdgeGluedTrees,
)
from src.glued_trees.analyze import compute_infinite_time_layer_distribution, full_analysis
from src.glued_trees.classes import _degenerate_eigenvalue_groups
from src.glued_trees.visualize import _parameters_str


class GluedTreesTest(unittest.TestCase):
    def test_constructors_are_keyword_only_and_validate_inputs(self) -> None:
        for model in (
            GluedTrees,
            DisorderedGluedTrees,
            AllToAllGluedTrees,
            IndependentEdgeGluedTrees,
        ):
            parameters = list(inspect.signature(model).parameters.values())
            self.assertTrue(
                all(parameter.kind is parameter.KEYWORD_ONLY for parameter in parameters)
            )

        with self.assertRaises(TypeError):
            GluedTrees(1, 1.0)
        with self.assertRaises(ValueError):
            GluedTrees(L=0, J_GT=1.0)
        with self.assertRaises(ValueError):
            GluedTrees(L=1, J_GT=-1.0)
        with self.assertRaises(ValueError):
            GluedTrees(L=1, J_GT=1.0, hamiltonian_convention="invalid")
        with self.assertRaises(ValueError):
            IndependentEdgeGluedTrees(
                L=1,
                J_GT=1.0,
                J_LR=1.0,
                p=1.1,
                add_path_edges=False,
                W=0.0,
            )

    def test_vertex_and_layer_counts(self) -> None:
        for L in (1, 2, 4):
            graph = GluedTrees(L=L, J_GT=1.0)
            self.assertEqual(graph.N, 2 * (2 ** (L + 1) - 1))
            self.assertEqual(graph.num_layers, 2 * L + 2)

    def test_layer_ranges_partition_vertices(self) -> None:
        for L in (1, 2, 3):
            graph = GluedTrees(L=L, J_GT=1.0)
            vertices = []
            for layer_idx in range(graph.num_layers):
                start_idx, end_idx = graph._layer_indices(layer_idx)
                vertices.extend(range(start_idx, end_idx))
            self.assertEqual(vertices, list(range(graph.N)))

    def test_every_leaf_has_two_distinct_cross_tree_edges(self) -> None:
        graph = GluedTrees(L=4, J_GT=1.0, rng=7)
        tree_size = 2 ** (graph.L + 1) - 1
        left_leaves = range(tree_size - 2**graph.L, tree_size)
        right_leaves = range(tree_size, tree_size + 2**graph.L)
        for leaf in (*left_leaves, *right_leaves):
            cross_neighbors = [
                neighbor
                for neighbor in graph.graph.neighbors(leaf)
                if (leaf < tree_size) != (neighbor < tree_size)
            ]
            self.assertEqual(len(cross_neighbors), 2)
            self.assertEqual(len(set(cross_neighbors)), 2)

    def test_fixed_seed_is_reproducible(self) -> None:
        kwargs = dict(
            L=3,
            J_GT=1.0,
            J_LR=0.25,
            p=0.3,
            add_path_edges=True,
            W=0.7,
            rng=42,
        )
        first = IndependentEdgeGluedTrees(**kwargs)
        second = IndependentEdgeGluedTrees(**kwargs)
        self.assertEqual(
            sorted(first.protected_graph.edges(data="weight")),
            sorted(second.protected_graph.edges(data="weight")),
        )
        np.testing.assert_array_equal(first.epsilon, second.epsilon)

    def test_uniform_disorder_shape_and_bounds(self) -> None:
        graph = DisorderedGluedTrees(L=3, J_GT=1.0, W=0.7, rng=3)
        self.assertEqual(graph.epsilon.shape, (graph.N,))
        self.assertTrue(np.all(graph.epsilon >= -graph.W))
        self.assertTrue(np.all(graph.epsilon <= graph.W))

    def test_backbone_and_intralayer_edge_weights(self) -> None:
        graph = IndependentEdgeGluedTrees(
            L=3,
            J_GT=2.0,
            J_LR=0.5,
            p=0.0,
            add_path_edges=True,
            W=0.0,
        )
        self.assertTrue(
            all(data["weight"] == graph.J_GT for _, _, data in graph.graph.edges(data=True))
        )
        added_edges = set(graph.protected_graph.edges()) - set(graph.graph.edges())
        self.assertTrue(added_edges)
        self.assertTrue(
            all(graph.protected_graph.edges[edge]["weight"] == graph.J_LR for edge in added_edges)
        )

    def test_adjacency_hamiltonian_formula(self) -> None:
        graph = DisorderedGluedTrees(
            L=2,
            J_GT=1.5,
            W=0.4,
            hamiltonian_convention="adjacency",
            rng=1,
        )
        adjacency = nx.to_numpy_array(graph.graph, nodelist=range(graph.N), weight="weight")
        expected = -adjacency + np.diag(graph.epsilon)
        np.testing.assert_allclose(graph.get_hamiltonian(), expected)

    def test_laplacian_hamiltonian_formula(self) -> None:
        graph = AllToAllGluedTrees(
            L=2,
            J_GT=1.5,
            J_LR=0.25,
            W=0.4,
            hamiltonian_convention="laplacian",
            rng=1,
        )
        adjacency = nx.to_numpy_array(
            graph.protected_graph, nodelist=range(graph.N), weight="weight"
        )
        expected = np.diag(adjacency.sum(axis=1)) - adjacency + np.diag(graph.epsilon)
        np.testing.assert_allclose(graph.get_hamiltonian(), expected)

    def test_dense_and_sparse_hamiltonians_agree(self) -> None:
        for convention in ("adjacency", "laplacian"):
            graph = IndependentEdgeGluedTrees(
                L=2,
                J_GT=1.0,
                J_LR=0.5,
                p=0.4,
                add_path_edges=True,
                W=0.3,
                hamiltonian_convention=convention,
                rng=5,
            )
            np.testing.assert_allclose(
                graph.get_hamiltonian(), graph.get_hamiltonian(sparse=True).toarray()
            )

    def test_infinite_time_distribution_is_normalized_and_regresses_clean_case(self) -> None:
        graph = GluedTrees(
            L=1, J_GT=1.0, hamiltonian_convention="laplacian", rng=0
        )
        distribution = graph.infinite_time_average_layer_distribution()
        self.assertTrue(np.all(distribution >= -1e-14))
        self.assertAlmostEqual(float(distribution.sum()), 1.0, places=12)
        self.assertAlmostEqual(float(distribution[-1]), 0.3300653595, places=9)

    def test_degenerate_projector_average_is_basis_invariant(self) -> None:
        graph = GluedTrees(
            L=1, J_GT=1.0, hamiltonian_convention="laplacian", rng=0
        )
        eigenvalues, eigenvectors = graph.compute_spectrum()
        original = graph._infinite_time_distribution_from_eigensystem(
            eigenvalues, eigenvectors, degeneracy_tolerance=1e-10
        )
        group_start, group_end = next(
            group
            for group in _degenerate_eigenvalue_groups(eigenvalues, 1e-10)
            if group[1] - group[0] > 1
        )
        rotation, _ = np.linalg.qr(
            np.array(
                [
                    [1.0, 2.0, 3.0],
                    [4.0, 5.0, 6.0],
                    [7.0, 8.0, 10.0],
                ]
            )
        )
        rotated_eigenvectors = eigenvectors.copy()
        rotated_eigenvectors[:, group_start:group_end] = (
            eigenvectors[:, group_start:group_end] @ rotation
        )
        rotated = graph._infinite_time_distribution_from_eigensystem(
            eigenvalues, rotated_eigenvectors, degeneracy_tolerance=1e-10
        )
        np.testing.assert_allclose(original, rotated, atol=1e-12)

    def test_analysis_and_visualization_use_canonical_parameters(self) -> None:
        graph = DisorderedGluedTrees(L=1, J_GT=1.0, W=0.2, rng=0)
        results = full_analysis(graph, max_t=0.1, dt=0.1, prog_bar=False)
        self.assertEqual(results.parameters, graph.parameters)
        self.assertEqual(_parameters_str(graph.parameters), "L: 1, J_GT: 1.0, W: 0.2")
        np.testing.assert_allclose(
            compute_infinite_time_layer_distribution(graph),
            graph.infinite_time_average_layer_distribution(),
        )

    def test_old_public_names_are_absent_from_migrated_surfaces(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        paths = [
            *sorted((repository_root / "src" / "glued_trees").glob("*.py")),
            *sorted((repository_root / "scripts").glob("*.py")),
            repository_root / "README.md",
        ]
        deprecated_names = (
            "h",
            "J",
            "J2",
            "sigma",
            "omegas",
            "T",
            "T1",
            "T2",
            "GluedTreesDisorder",
            "GluedTreesSmallWorld",
            "average_layer_distribution",
            "Taa",
            "Tsw",
            "nn",
        )
        for path in paths:
            contents = path.read_text()
            for deprecated_name in deprecated_names:
                self.assertIsNone(
                    re.search(rf"(?<![A-Za-z0-9_]){deprecated_name}(?![A-Za-z0-9_])", contents),
                    path,
                )


if __name__ == "__main__":
    unittest.main()
