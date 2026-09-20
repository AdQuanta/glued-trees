# Childs2003 — Exponential Algorithmic Speedup by a Quantum Walk

> Sources: Andrew M Childs; Richard Cleve; Enrico Deotto; Edward Farhi; Sam Gutmann; Daniel A Spielman (2003)
> Raw: [Full-text source record](../../../raw/literature/exponential-algorithmic-speedup-by-a-quantum-walk-full-text.md)
> Updated: 2026-09-20

## Bibliographic identity

- Zotero parent key: `C3URD9FR`
- Zotero standardized note title: `Childs2003`
- Strategic topic: [Quantum walks and graph engineering](../organized-literature-map.md#quantum-walks-and-graph-engineering)
- Original scientific grouping: Glued-tree traversal and physical realizations

## Scope and technical content

Constructs the random glued-trees black-box traversal problem, gives an efficient circuit simulation of the continuous-time walk, and proves rapid entrance-to-exit traversal. Its classical lower bound rules out subexponential black-box algorithms, turning the earlier propagation contrast into an exponential algorithmic separation.

## Main derivation or method

Constructs the random glued-trees black-box traversal problem, gives an efficient circuit simulation of the continuous-time walk, and proves rapid entrance-to-exit traversal.

## Main result

Its classical lower bound rules out subexponential black-box algorithms, turning the earlier propagation contrast into an exponential algorithmic separation.

## Mathematical core

The oracle problem is traversed with the same continuous-time generator $H=-\gamma A$ used for the glued-tree walk, but the random gluing is exposed only through local black-box queries. In the clean column-symmetric sector,

$$
\langle S_{\ell+1}|A|S_\ell\rangle
=\frac{m_\ell}{\sqrt{n_\ell n_{\ell+1}}},
$$

so the quantum evolution can be simulated efficiently as a sparse Hamiltonian. The exponential separation comes from pairing this algorithm with a classical query lower bound for the random oracle construction; it does not follow from ballistic propagation alone.

## Relevance to the glued-trees paper

Use this work to define the clean benchmark and identify competing graph-transport mechanisms. A favorable finite-size trend is not evidence for the project’s target until it survives the asymptotic and accessibility checks.

## Related concepts and work

- [Glued-Trees Walk and Problem Formulation](../../concepts/glued-trees-walk-and-problem-formulation.md)
- [Disorder, Localization, and Evidence](../../concepts/disorder-localization-and-asymptotic-evidence.md)
- [Protected Layer-Manifold Theory](../../theory/protected-layer-manifold-theory.md)
- [Paper-Readiness Criteria](../../project/paper-readiness-criteria.md)
- [Törmä2002 — Localization and diffusion in Ising-type quantum networks](torma2002-bbn4unyd.md)
- [Mülken2007 — Quantum transport on small-world networks: A continuous-time quantum walk approach](mulken2007-k2539m6f.md)
