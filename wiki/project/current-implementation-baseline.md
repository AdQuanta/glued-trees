# Current Implementation Baseline

> Sources: implementation and SPEC.md, 2026-09-20
> Updated: 2026-09-20

## Overview

The codebase is an exploratory numerical baseline. It constructs canonical glued-tree backbones, samples quenched onsite disorder, supports dense all-to-all and independently sampled intra-layer controls, propagates states with QuTiP, and computes layer and exit distributions. This is a source-code inventory, not verifier-certified model compliance.

## Implemented model classes

`GluedTrees` constructs two depth-$L$ binary trees and glues their leaf sets with two shuffled perfect matchings while rejecting duplicate assignments. It assigns every backbone edge weight $J_{\rm GT}$. `DisorderedGluedTrees` samples the canonical disorder array, $\epsilon_i\overset{\rm iid}{\sim}U[-W,W]$. `AllToAllGluedTrees` adds weighted complete graphs within layers, while `IndependentEdgeGluedTrees` optionally adds consecutive-index path edges and independently samples remaining intra-layer candidate edges with probability $p$. Every added intra-layer edge has weight $J_{\rm LR}$.

All models require keyword arguments and expose `graph`, `left_tree`, `right_tree`, and, for protected variants, `protected_graph`. The selected `hamiltonian_convention` is either `"adjacency"`, implementing $-A_J+\operatorname{diag}(\epsilon)$, or `"laplacian"`, implementing $D_J-A_J+\operatorname{diag}(\epsilon)$. The infinite-time layer distribution uses spectral projectors over eigenvalue groups identified by a documented absolute tolerance, avoiding arbitrary-basis dependence in degenerate eigenspaces.

## Gap to the governing specification

The implementation does not establish the complete model and verifier program required by the specification. In particular, it does not provide bounded-degree network families, converged disorder/network/gluing ensembles, rigorous asymptotic model comparison, mechanism diagnostics, evidence bundles, or frozen verifiers.

The independent-edge construction tests every possible intra-layer pair independently and therefore does not enforce the specification's hard maximum-added-degree condition. The all-to-all class is explicitly a dense control. These are implementation facts and scope gaps, not scientific conclusions.

## See also

- [Research Program](research-program.md)
- [Disorder, Localization, and Asymptotic Evidence](../concepts/disorder-localization-and-asymptotic-evidence.md)
