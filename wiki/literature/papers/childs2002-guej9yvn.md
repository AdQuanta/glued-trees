# Childs2002 — An Example of the Difference Between Quantum and Classical Random Walks

> Sources: Andrew M Childs; Edward Farhi; Sam Gutmann (2002)
> Raw: [Full-text source record](../../../raw/literature/an-example-of-the-difference-between-quantum-and-classical-r-full-text.md)
> Updated: 2026-09-20

## Bibliographic identity

- Zotero parent key: `GUEJ9YVN`
- Zotero standardized note title: `Childs2002`
- Strategic topic: [Quantum walks and graph engineering](../organized-literature-map.md#quantum-walks-and-graph-engineering)
- Original scientific grouping: Glued-tree traversal and physical realizations

## Scope and technical content

Defines a continuous-time graph walk and studies a two-tree graph whose column-symmetric sector reduces to a one-dimensional chain. Quantum propagation reaches the opposite root in linear time and the infinite-time probability there is at least 1/(2n+1), whereas the classical limiting probability is exponentially small; this is a dynamical separation, not yet an oracle-algorithm lower bound.

## Main derivation or method

Defines a continuous-time graph walk and studies a two-tree graph whose column-symmetric sector reduces to a one-dimensional chain.

## Main result

Quantum propagation reaches the opposite root in linear time and the infinite-time probability there is at least $1/(2n+1)$, whereas the classical limiting probability is exponentially small; this is a dynamical separation, not yet an oracle-algorithm lower bound.

## Mathematical core

The continuous-time walk uses $H=-\gamma A$ and $|\psi(t)\rangle=e^{-iHt}|\mathrm{IN}\rangle$. Permutation symmetry reduces the glued graph to column states $|S_j\rangle$. Between adjacent columns with $m_j$ edges and sizes $n_j,n_{j+1}$,

$$
\langle S_{j+1}|A|S_j\rangle=\frac{m_j}{\sqrt{n_jn_{j+1}}}.
$$

The resulting one-dimensional chain supports the rapid quantum propagation. The stated lower bound is for the infinite-time average and is not a finite-time success probability.

## Relevance to the glued-trees paper

Use this work to define the clean benchmark and identify competing graph-transport mechanisms. A favorable finite-size trend is not evidence for the project’s target until it survives the asymptotic and accessibility checks.

## Related concepts and work

- [Glued-Trees Walk and Problem Formulation](../../concepts/glued-trees-walk-and-problem-formulation.md)
- [Disorder, Localization, and Evidence](../../concepts/disorder-localization-and-asymptotic-evidence.md)
- [Protected Layer-Manifold Theory](../../theory/protected-layer-manifold-theory.md)
- [Paper-Readiness Criteria](../../project/paper-readiness-criteria.md)
- [Wong2021 — Equivalent Laplacian and adjacency quantum walks on irregular graphs](wong2021-i9nh4awn.md)
- [Törmä2002 — Localization and diffusion in Ising-type quantum networks](torma2002-bbn4unyd.md)
