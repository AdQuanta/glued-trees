# Quantum Walks and Graph Engineering

> Sources: Childs et al., 2002 and 2003; Jackson et al., 2012; Wong and Lockhart, 2021
> Raw: [Glued-tree propagation](../../raw/literature/an-example-of-the-difference-between-quantum-and-classical-r-full-text.md); [Oracle separation](../../raw/literature/exponential-algorithmic-speedup-by-a-quantum-walk-full-text.md); [Disordered trees](../../raw/literature/2012-08-27-quantum-walks-on-trees-with-disorder-decay-diffusion-and-loc-full-text.md); [Adjacency–Laplacian equivalence](../../raw/literature/2021-10-25-equivalent-laplacian-and-adjacency-quantum-walks-on-irregula-full-text.md)
> Updated: 2026-09-20

## Papers in this route

| Paper | Year |
|---|---:|
| [Childs2002 — An Example of the Difference Between Quantum and Classical Random Walks](papers/childs2002-guej9yvn.md) | 2002 |
| [Törmä2002 — Localization and diffusion in Ising-type quantum networks](papers/torma2002-bbn4unyd.md) | 2002 |
| [Childs2003 — Exponential Algorithmic Speedup by a Quantum Walk](papers/childs2003-c3urd9fr.md) | 2003 |
| [Mülken2007 — Quantum transport on small-world networks: A continuous-time quantum walk approach](papers/mulken2007-k2539m6f.md) | 2007 |
| [Mülken2011 — Continuous-time quantum walks: Models for coherent transport on complex networks](papers/mulken2011-ba8ikgfr.md) | 2011 |
| [Jackson2012 — Quantum walks on trees with disorder: Decay, diffusion, and localization](papers/jackson2012-dvzgdrqv.md) | 2012 |
| [Izaac2013 — Continuous-time quantum walks with defects and disorder](papers/izaac2013-7b8g38rk.md) | 2013 |
| [Wong2021 — Equivalent Laplacian and adjacency quantum walks on irregular graphs](papers/wong2021-i9nh4awn.md) | 2021 |

## Role in the paper

This route supplies the clean glued-tree benchmark, the disorder competitors, and the Hamiltonian-convention discipline needed to state a sparse graph-engineering result.

## Exact column reduction

For the uniform layer state $|S_\ell\rangle$ and $m_\ell$ edges between adjacent layers,

$$
\langle S_{\ell+1}|A_{\rm GT}|S_\ell\rangle=
\frac{m_\ell}{\sqrt{n_\ell n_{\ell+1}}}.
$$

Binary branching gives $\sqrt{2}J_{\rm GT}$, while the 2-regular leaf gluing gives $2J_{\rm GT}$. The exponentially large clean graph therefore has an exact $(2L+2)$-site column chain. Childs et al. use that structure first for a propagation contrast and then, with random black-box gluing, for an oracle separation.

## What disorder and extra edges test

Onsite disorder breaks layer permutation symmetry. Its layer mean perturbs the reduced chain, while the zero-mean component couples the column chain into nonsymmetric modes. Tree-localization and defect studies show why this cannot be summarized by one universal localization length. Shortcut edges, changed degrees, and endpoint shifts can also change transport without protecting the column manifold.

For an irregular graph, $H_L=\gamma(D-A)$ differs from $H_A=-\gamma A$ by a state-dependent diagonal. Wong and Lockhart identify conditions under which that diagonal acts as a scalar on the evolving subspace; those conditions, not graph appearance alone, establish equivalence.

## See Also

- [Strategic Literature Map](organized-literature-map.md#quantum-walks-and-graph-engineering)
- [Disorder, Localization, and Asymptotic Evidence](../concepts/disorder-localization-and-asymptotic-evidence.md)
- [Childs2002](papers/childs2002-guej9yvn.md)
- [Childs2003](papers/childs2003-c3urd9fr.md)
- [Wong2021](papers/wong2021-i9nh4awn.md)
