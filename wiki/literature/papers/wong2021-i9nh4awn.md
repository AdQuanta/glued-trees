# Wong2021 — Equivalent Laplacian and adjacency quantum walks on irregular graphs

> Sources: Thomas G. Wong; Joshua Lockhart (2021)
> Raw: [Full-text source record](../../../raw/literature/2021-10-25-equivalent-laplacian-and-adjacency-quantum-walks-on-irregula-full-text.md)
> Updated: 2026-09-20

## Bibliographic identity

- Zotero parent key: `I9NH4AWN`
- Zotero standardized note title: `Wong2021`
- Strategic topic: [Quantum walks and graph engineering](../organized-literature-map.md#quantum-walks-and-graph-engineering)
- Original scientific grouping: Graph Hamiltonians and experimental equivalence

## Scope and technical content

Shows that adjacency- and Laplacian-generated walks, though generally different on irregular graphs, can have identical vertex probabilities for special starting vertices. Exhaustive search through connected irregular graphs with at most eleven vertices finds 64 examples and eight infinite families, but the equivalence is rare, initial-state dependent, and does not make the amplitudes identical.

## Main derivation or method

Shows that adjacency- and Laplacian-generated walks, though generally different on irregular graphs, can have identical vertex probabilities for special starting vertices.

## Main result

Exhaustive search through connected irregular graphs with at most eleven vertices finds 64 examples and eight infinite families, but the equivalence is rare, initial-state dependent, and does not make the amplitudes identical.

## Mathematical core

With a common hopping scale $\gamma$,

$$
H_A=-\gamma A,
\qquad H_L=\gamma(D-A)=H_A+\gamma D.
$$

If the evolving state remains in a subspace on which $D=dI$, then $e^{-iH_Lt}=e^{-i\gamma dt}e^{-iH_At}$ on that subspace, differing only by a global phase. The paper identifies nontrivial irregular-graph cases where this condition holds; site disorder or nonregular added edges can invalidate it.

## Relevance to the glued-trees paper

Use this work to define the clean benchmark and identify competing graph-transport mechanisms. A favorable finite-size trend is not evidence for the project’s target until it survives the asymptotic and accessibility checks.

## Related concepts and work

- [Glued-Trees Walk and Problem Formulation](../../concepts/glued-trees-walk-and-problem-formulation.md)
- [Disorder, Localization, and Evidence](../../concepts/disorder-localization-and-asymptotic-evidence.md)
- [Protected Layer-Manifold Theory](../../theory/protected-layer-manifold-theory.md)
- [Paper-Readiness Criteria](../../project/paper-readiness-criteria.md)
- [Izaac2013 — Continuous-time quantum walks with defects and disorder](izaac2013-7b8g38rk.md)
- [Childs2002 — An Example of the Difference Between Quantum and Classical Random Walks](childs2002-guej9yvn.md)
