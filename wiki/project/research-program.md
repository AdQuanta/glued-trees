# Research Program

> Sources: Project README, SPEC.md, and implementation snapshot, 2026-09-20
> Raw: [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## Overview

The project studies passive protection of a disordered continuous-time quantum walk on glued trees using sparse, long-range, intra-layer connectivity. Its central target is an asymptotic change in the ensemble-averaged infinite-time exit probability from exponential decay in tree depth to power-law decay while both the maximum added degree and the ratio of protection to backbone coupling remain size-independent. This page records the governing specification, not an established scientific result.

## Canonical model

The specified backbone is two depth-$L$ binary trees whose leaf sets are joined by a random 2-regular bipartite graph. Layers run from the entrance at $\ell=0$ to the exit at $\ell=2L+1$. Every non-singleton layer may receive independently sampled intra-layer edges from one fixed network family per experiment.

Both weighted-adjacency and weighted-Laplacian walks are first-class cases. The disorder is static and independent,

$$
\epsilon_i\overset{\rm iid}{\sim}U[-W,W].
$$

The intended sparse resource obeys a hard maximum-added-degree bound independent of $L$ and $N$, and $J_{\rm LR}/J_{\rm GT}$ must remain $O(1)$. Dense all-to-all coupling is a mechanism/control case, not a successful sparse construction.

## Observable and mechanism program

The primary observable is the ensemble-averaged infinite-time occupation of the exit, not first-passage probability. The headline ensemble mean is accompanied by the distribution, median, and typical value to expose rare-event domination. Finite-time polynomial accessibility is mandatory as a secondary diagnostic.

The working mechanism is leakage suppression from the layer-symmetric transport manifold into nonsymmetric intra-layer modes. This is explicitly a hypothesis. The program must compare spectral separation, algebraic connectivity, leakage matrix elements, nearby nonsymmetric-state density, self-energy, localization, participation, and generic bandwidth explanations. Symmetric-manifold occupation and an operational intra-layer coherence measure are mandatory diagnostics.

## Evidence ladder

Positive numerics alone are insufficient. The specification requires model, numerical, ensemble, scaling, mechanism, accessibility, generality, and paper-readiness verifiers. Scaling must compare exponential, stretched-exponential, and power-law models with uncertainty and fit-window checks. Both Hamiltonian conventions, independent glued-tree realizations, a classical sanity check, and a distinct non-glued-tree generalization are required before `paper_ready = true`.

## Governance

The project owner approves what each scientific check tests; the research agent controls how an approved check is executed. Verifiers are frozen after approval and cannot be weakened following an unfavorable result. Negative outcomes are valid. No experiment is authorized merely by this specification: every hypothesis check requires an approved contract first.

Only verified project results may be promoted to this wiki as established knowledge. Literature synthesis and implementation descriptions must remain visibly distinct from verified scientific results.

## See Also

- [Paper-Readiness Criteria](paper-readiness-criteria.md)
- [Current Implementation Baseline](current-implementation-baseline.md)
- [Symbols and Conventions](../concepts/symbols-and-conventions.md)
- [Glued-Trees Walk and Problem Formulation](../concepts/glued-trees-walk-and-problem-formulation.md)
- [Strategic Literature Map](../literature/organized-literature-map.md)
