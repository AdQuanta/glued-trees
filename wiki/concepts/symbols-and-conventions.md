# Symbols and Conventions

> Sources: Project specification, 2026-09-20
> Raw: [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## Purpose

This page fixes the notation used throughout the wiki. It distinguishes the specified model from a verified result: symbols define the research program; they do not imply that its North-Star scaling change has been observed.

## Graph and layer notation

The canonical backbone contains two depth-$L$ binary trees. The source-to-target layers are indexed by

$$
\ell=0,1,\ldots,2L+1,
$$

with $\ell=0$ the entrance $|\mathrm{IN}\rangle$, $\ell=2L+1$ the exit $|\mathrm{OUT}\rangle$, and $V_\ell$ the set of vertices in layer $\ell$. Its size is $n_\ell=|V_\ell|$, and the layer projector is

$$
\Pi_\ell=\sum_{i\in V_\ell}|i\rangle\langle i|.
$$

The normalized layer-symmetric state and its projector are

$$
|S_\ell\rangle=\frac{1}{\sqrt{n_\ell}}\sum_{i\in V_\ell}|i\rangle,
\qquad
P=\sum_\ell |S_\ell\rangle\langle S_\ell|,
\qquad Q=I-P.
$$

Here $P$ is the clean transport manifold and $Q$ its nonsymmetric complement.

## Couplings, disorder, and biases

$J_{\rm GT}$ denotes the backbone coupling, $J_{\rm LR}$ the added intra-layer coupling, and $k$ the maximum added intra-layer degree. The sparse-resource condition is $k=O(1)$ and $J_{\rm LR}/J_{\rm GT}=O(1)$ as $L$ and total graph size grow.

Static onsite disorder is quenched and independent:

$$
\epsilon_i\overset{\rm iid}{\sim}U[-W,W],
\qquad
V_{\rm dis}=\sum_i\epsilon_i|i\rangle\langle i|.
$$

$W$ is the disorder half-width. A uniform layer bias is $H_{\rm bias}=\sum_\ell b_\ell\Pi_\ell$; it may compensate a layer mean but cannot by itself remove disorder coupling from $P$ to $Q$.

## Hamiltonian conventions

For real symmetric edge weights $J_{ij}$, the weighted adjacency is

$$
A_J=\sum_{\{i,j\}\in E}J_{ij}(|i\rangle\langle j|+|j\rangle\langle i|).
$$

The adjacency CTQW uses $H_A=-A_J+V_{\rm dis}+H_{\rm bias}$. The Laplacian CTQW uses $H_L=L_J+V_{\rm dis}+H_{\rm bias}$ with $L_J=D_J-A_J$ and $D_J$ the weighted-strength diagonal. They must be analyzed separately unless an invariant-subspace equivalence has been proved for the chosen graph, initial state, and disorder realization.

## Observable notation

The primary observable is the disorder-ensemble average of the infinite-time exit occupation, $\langle\overline P_{\rm exit}^{(\infty)}(L)\rangle$. It is not a first-passage probability. $P_{\rm sym}(t)=\langle\psi(t)|P|\psi(t)\rangle$ measures occupation of the symmetric manifold, and $C_\ell(t)$ denotes an intralayer coherence diagnostic. A finite-time accessibility test uses a polynomial window $T(L)$ and must be reported separately from the infinite-time result.

## See Also

- [Glued-Trees Walk and Problem Formulation](glued-trees-walk-and-problem-formulation.md)
- [Protected Layer-Manifold Theory](../theory/protected-layer-manifold-theory.md)
- [Paper-Readiness Criteria](../project/paper-readiness-criteria.md)
