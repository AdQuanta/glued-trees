# Foundations and Claim Architecture

> Sources: Farhi and Gutmann, 1998; Aharonov et al., 2001; Kempe, 2003; Childs and Goldstone, 2004
> Raw: [Decision-tree CTQW](../../raw/literature/1998-08-01-quantum-computation-and-decision-trees-full-text.md); [Quantum walks on graphs](../../raw/literature/2001-07-06-quantum-walks-on-graphs-full-text.md); [Quantum-walk overview](../../raw/literature/quantum-random-walks-an-introductory-overview-full-text.md); [Spatial search](../../raw/literature/2004-08-23-spatial-search-by-quantum-walk-full-text.md)
> Updated: 2026-09-20

## Papers in this route

| Paper | Year |
|---|---:|
| [Farhi1998 — Quantum computation and decision trees](papers/farhi1998-pun6tiuf.md) | 1998 |
| [Aharonov2001 — Quantum walks on graphs](papers/aharonov2001-q6axaxzq.md) | 2001 |
| [Kempe2003 — Quantum random walks - an introductory overview](papers/kempe2003-aueijzej.md) | 2003 |
| [Childs2004 — Spatial search by quantum walk](papers/childs2004-97wb8nvd.md) | 2004 |
| [Babbush2023 — Exponential Quantum Speedup in Simulating Coupled Classical Oscillators](papers/babbush2023-fnyhlmcu.md) | 2023 |

## Role in the paper

This route fixes what is meant by a quantum walk, an observable, and an advantage claim. Its main service is negative: it prevents a long-time occupation, a hitting probability, a mixing diagnostic, and an oracle-query separation from being treated as interchangeable.

## Mathematical core

A continuous-time walk evolves according to

$$
i\frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle,
\qquad
|\psi(t)\rangle=e^{-iHt}|\psi(0)\rangle.
$$

For a graph with adjacency $A$ and degree matrix $D$, common choices are $H=-\gamma A$ and $H=\gamma(D-A)$. The two agree up to a scalar only on regular graphs or on a specifically proved invariant subspace. Discrete-time walks instead introduce a coin and step operator; their mixing and hitting definitions cannot be transplanted unaltered into the CTQW project.

Spatial search illustrates the spectral viewpoint. A marked vertex enters through an oracle term, and success depends on avoided crossings and spectral dimension rather than graph size alone. This motivates reporting the relevant energy scales and state overlaps for glued trees rather than giving a purely graph-theoretic description.

## Paper-writing consequence

The current project may call its primary quantity an ensemble-averaged infinite-time exit occupation. It may not call it a hitting time, mixing probability, or recovered oracle advantage without the separately specified finite-time and classical evidence. The exact definitions are collected in [Symbols and Conventions](../concepts/symbols-and-conventions.md).

## See Also

- [Strategic Literature Map](organized-literature-map.md#foundations-and-research-claims)
- [Glued-Trees Walk and Problem Formulation](../concepts/glued-trees-walk-and-problem-formulation.md)
- [Farhi1998](papers/farhi1998-pun6tiuf.md)
- [Aharonov2001](papers/aharonov2001-q6axaxzq.md)
- [Childs2004](papers/childs2004-97wb8nvd.md)
