# Current Implementation Baseline

> Sources: Project README, SPEC.md, and implementation snapshot, 2026-09-20
> Raw: [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## Overview

The current code is an exploratory numerical baseline. It constructs glued trees, adds static onsite disorder, supports dense all-to-all or probabilistic intra-layer couplings, propagates states with QuTiP, and computes layer and exit distributions. This is a source-code inventory, not verifier-certified model compliance.

## Implemented model classes

`GluedTrees` constructs two balanced binary trees and glues the leaf sets using two independently shuffled matchings while rejecting pairwise duplicate assignments. Its Hamiltonian is the NetworkX graph Laplacian multiplied by $J$. The analysis layer supports time evolution, layer populations, exit probability, and a Fourier transform of the exit signal.

`GluedTreesDisorder` adds diagonal disorder and currently accepts uniform, Gaussian, or Lorentzian sampling. `GluedTreesAllToAll` adds weighted complete graphs within layers. `GluedTreesSmallWorld` can add nearest-neighbor edges plus independently selected intra-layer pairs with probability $p$.

## Gap to the governing specification

The snapshot does not yet establish the complete model/verifier program required by the specification. In particular, the specification calls for adjacency and Laplacian formulations, the fixed uniform disorder convention, bounded-degree network families, exact or converged infinite-time averages, joint disorder/network ensembles, final gluing ensembles, rigorous asymptotic model comparison, mechanism diagnostics, evidence bundles, and frozen verifiers.

The present probabilistic small-world construction tests every possible intra-layer pair independently and therefore does not itself enforce the specification's hard maximum-added-degree condition. The all-to-all class is explicitly a dense control under the specification. These are implementation facts and scope gaps, not scientific conclusions.

## See Also

- [Research Program](research-program.md)
- [Disorder, Localization, and Asymptotic Evidence](../concepts/disorder-localization-and-asymptotic-evidence.md)
