# Glued-Trees Quantum Walks

Python tools for continuous-time quantum walks on disordered glued-trees graphs and exploratory intra-layer protection controls.

The canonical backbone contains two depth-$L$ binary trees. Their leaves are joined by two random perfect matchings, so every leaf has two distinct cross-tree edges. The graph contains

$$
N=2(2^{L+1}-1)
$$

vertices arranged into $2L+2$ source-to-target layers.

## Model

Backbone edges have weight $J_{\rm GT}$ and added intra-layer edges have weight $J_{\rm LR}$. Static onsite disorder is sampled once per model instance:

$$
\epsilon_i\overset{\rm iid}{\sim} U[-W,W].
$$

Choose one Hamiltonian convention explicitly:

$$
H_A=-A_J+\operatorname{diag}(\epsilon),
\qquad
H_L=D_J-A_J+\operatorname{diag}(\epsilon).
$$

The models are `GluedTrees`, `DisorderedGluedTrees`, `AllToAllGluedTrees`, and `IndependentEdgeGluedTrees`. The independent-edge construction samples each possible intra-layer edge with probability `p`; it is not a Watts–Strogatz model and does not itself enforce bounded added degree.

All model constructors are keyword-only. The infinite-time layer observable is `infinite_time_average_layer_distribution()`. It groups eigenvalues with an absolute tolerance of `1e-10` and uses spectral projectors, making the result invariant under a change of basis inside degenerate eigenspaces.

## Quick start

```python
from src.glued_trees import DisorderedGluedTrees
from src.glued_trees.analyze import full_analysis

graph = DisorderedGluedTrees(
    L=4,
    J_GT=1.0,
    W=0.5,
    hamiltonian_convention="laplacian",
    rng=0,
)
results = full_analysis(graph, max_t=20.0, dt=0.1, prog_bar=False)

print(f"vertices: {graph.N}")
print(f"maximum exit probability: {results.exit_probabilities.max():.6f}")
```

To add independently sampled intra-layer couplings:

```python
from src.glued_trees import IndependentEdgeGluedTrees

graph = IndependentEdgeGluedTrees(
    L=4,
    J_GT=1.0,
    J_LR=1.0,
    p=0.1,
    add_path_edges=True,
    W=0.5,
    hamiltonian_convention="adjacency",
    rng=0,
)
```

## Parameters

| Name | Meaning |
|---|---|
| `L` | Depth of each binary tree |
| `N` | Total vertices, $2(2^{L+1}-1)$ |
| `J_GT` | Glued-trees backbone edge weight |
| `J_LR` | Added intra-layer edge weight |
| `p` | Independent inclusion probability for candidate intra-layer edges |
| `add_path_edges` | Add consecutive-index intra-layer path edges |
| `W` | Uniform disorder half-width |
| `epsilon` | Quenched onsite energy array |
| `hamiltonian_convention` | Either `"adjacency"` or `"laplacian"` |

## Development

Create the required Python 3.13 virtual environment and install pinned dependencies:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

Run the deterministic checks from the repository root:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m compileall src scripts
```

The scripts in `scripts/` are exploratory and write generated artifacts under `outputs/`, which is not tracked. The code supports small-system numerical studies; this implementation refactor alone does not verify the research program or establish paper readiness. See [SPEC.md](SPEC.md) and [the implementation baseline](wiki/project/current-implementation-baseline.md) for scope.
