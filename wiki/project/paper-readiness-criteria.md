# Paper-Readiness Criteria

> Sources: SPEC.md, collected 2026-09-20
> Raw: [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## Overview

`paper_ready = true` is the specification's positive-story gate, not a synonym for scientific completion. It may be declared only when every applicable frozen paper-readiness criterion is satisfied and every required verifier passes. A rigorous negative result can still complete the research program without meeting this gate, and manuscript writing begins only after the gate rather than being part of it.

## Declaration rule

The research agent may declare `paper_ready = true` without a separate human approval gate once the frozen criteria and required verifiers pass. The project owner retains authority to reject the declaration, reopen the research, change the specification, or request more evidence. The final assessment must be performed by the frozen, fresh-context `paper_readiness_verifier` using the evidence bundles and outputs of the lower-level verifiers; it may not reinterpret a failed lower-level verifier into a pass.

## Required evidence

### Core scaling result

At least one genuinely sparse intra-layer family must show verifier-supported recovery of the ensemble-averaged infinite-time exit probability from exponential to power-law scaling,

$$
\left\langle\overline P_{\rm exit}\right\rangle:
e^{-L/\xi}\rightarrow L^{-\alpha},
$$

within the available asymptotic finite-size evidence. The candidate must keep both $k=O(1)$ and $J_{\rm LR}/J_{\rm GT}=O(1)$ independent of $L$ and $N$. The all-to-all control is ineligible.

### No fine-tuned protection strength

The successful sparse scheme must operate across a non-fine-tuned $J_{\rm LR}$ regime. At the ensemble and scaling level, increasing the coupling should improve protection or lead to saturation rather than produce only a narrow isolated optimum.

### Rigorous numerics and statistics

The `numerics_verifier`, `ensemble_verifier`, and `scaling_verifier` must pass. The result must survive solver- and ensemble-convergence studies, changes to the fit window, inclusion of the largest accessible systems, and comparison against competing asymptotic models.

### Analytic physical mechanism

The `mechanism_verifier` must pass. The evidence must include an analytic theory of the protected manifold, disorder-induced leakage, connectivity and bias effects, and the relevant scales in $W$, $J_{\rm LR}$, $k$, and measurable graph properties. Numerical agreement must support the mechanism rather than merely assume it.

### Disorder-strength characterization

The evidence must either support protection across the tested range in a manner consistent with the hypothesis that every finite $W$ can be protected by sufficiently strong, size-independent $J_{\rm LR}$, or characterize the threshold/crossover structure if that hypothesis fails. The latter must distinguish an asymptotic transition from a crossover or a mere increase in localization length. A finite numerical scan cannot establish protection for all finite $W$.

### Mandatory finite-time accessibility diagnostic

The `accessibility_verifier` must pass by confirming that the finite-polynomial-time diagnostic was completed rigorously. Polynomial accessibility strengthens the result but is required for `paper_ready` only if the final central claim invokes operational or algorithmic quantum advantage. A negative or inconclusive outcome must narrow the manuscript's claims.

### Both CTQW formulations

Weighted-adjacency and weighted-Laplacian CTQWs must both be investigated, and their relationship must be understood. They need not agree, but neither formulation may be omitted because its outcome is inconvenient.

### Classical sanity check

The classical source-to-target comparison on the protected graph family must be sufficient to support any quantum-advantage language.

### Glued-tree ensemble robustness

The central result must survive averaging over independent glued-tree leaf-gluing realizations rather than only one fixed backbone.

### Generalization beyond glued trees

At least one genuinely distinct non-glued-tree graph or task must successfully extend the protection principle. An extension with algorithmic utility is preferred; otherwise, its broader significance must be strong enough to support the high-impact claim.

### Reproducibility and knowledge capture

Every manuscript-critical result must have a reproducible evidence bundle, pass its relevant frozen verifiers, and be promoted to the research wiki with provenance. The final evidence, research ledger, and wiki must contain no unresolved contradictions.

### Fresh-context final assessment

The frozen `paper_readiness_verifier` must pass in fresh context using the submitted evidence bundles and lower-level verifier outputs, without access to the persuasive exploratory history of the result.

## Claim boundary

Passing the gate supports manuscript preparation; it does not itself prove stronger phrases such as “phase transition,” “arbitrary disorder,” “spectral-gap protection,” or “quantum advantage restored.” Each such claim still requires its own specified evidence. If finite-time accessibility or the classical comparison is negative or unresolved, the paper must restrict its claims even when the infinite-time protection result remains scientifically valid.

## See Also

- [Research Program](research-program.md)
- [Current Implementation Baseline](current-implementation-baseline.md)

