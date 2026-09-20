# Glued-Trees Walk and Problem Formulation

> Sources: Childs et al., 2002 and 2003; project specification, 2026-09-20
> Raw: [Childs 2002 full text](../../raw/literature/an-example-of-the-difference-between-quantum-and-classical-r-full-text.md); [Childs 2003 full text](../../raw/literature/exponential-algorithmic-speedup-by-a-quantum-walk-full-text.md); [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## The graph

The glued-trees benchmark joins two depth-$L$ binary trees at their leaves. The entrance and exit are the two roots. In the specified backbone, every left leaf connects to two right leaves and every right leaf connects to two left leaves, making the leaf-to-leaf gluing a random 2-regular bipartite graph. This choice preserves degree three at every leaf: one tree-parent edge and two gluing edges.

The graph is exponentially large in $L$, yet the clean walk started at the entrance is confined to a small permutation-symmetric sector. All vertices in a common layer have equal amplitude in that sector, so it is described by the $(2L+2)$ states $|S_\ell\rangle$ defined in [Symbols and Conventions](symbols-and-conventions.md).

## Exact clean reduction

For adjacent layers, let $m_\ell$ be the number of backbone edges. The symmetric-sector matrix element of the adjacency is

$$
\langle S_{\ell+1}|A_{\rm GT}|S_\ell\rangle=
\frac{m_\ell}{\sqrt{n_\ell n_{\ell+1}}}.
$$

For a binary branching step, $m_\ell=2n_\ell$ and $n_{\ell+1}=2n_\ell$, giving reduced hopping $\sqrt{2}J_{\rm GT}$. Across the two leaf layers, the 2-regular gluing gives $2J_{\rm GT}$. Thus the clean exponentially large graph reduces exactly to a short inhomogeneous chain. This reduction explains ballistic transport, but it is lost when independent onsite disorder distinguishes vertices within a layer.

## What the original results do—and do not—claim

Childs, Farhi, and Gutmann first established a propagation contrast: quantum amplitude crosses the clean glued structure in time linear in $L$, while the classical limiting probability at the exit is exponentially small. The subsequent black-box construction adds a random gluing and proves that no classical randomized oracle algorithm succeeds in subexponential queries, while an efficiently simulated continuous-time quantum walk does.

Those results are the benchmark, not the conclusion of this project. The present problem changes the Hamiltonian by adding static disorder and sparse intra-layer couplings. It must show whether protection changes the large-$L$ scaling of the specified exit occupation, rather than merely recovering a visible finite-depth transmission peak.

## The project question

The core question is whether bounded-degree, size-independent intra-layer connectivity can protect the disordered walk strongly enough to change

$$
\left\langle\overline P_{\rm exit}^{(\infty)}(L)\right\rangle
\sim e^{-L/\xi}
\quad\hbox{to}\quad
\left\langle\overline P_{\rm exit}^{(\infty)}(L)\right\rangle
\sim L^{-\alpha}.
$$

The requirement is deliberately stronger than improved transport: the construction must remain sparse, its improvement must not be a narrow coupling resonance, and any language about operational or algorithmic advantage additionally requires a finite polynomial-time accessibility analysis and a matching classical comparison.

## See Also

- [Symbols and Conventions](symbols-and-conventions.md)
- [Disorder, Localization, and Asymptotic Evidence](disorder-localization-and-asymptotic-evidence.md)
- [Protected Layer-Manifold Theory](../theory/protected-layer-manifold-theory.md)
- [Childs2002](../literature/papers/childs2002-guej9yvn.md)
- [Childs2003](../literature/papers/childs2003-c3urd9fr.md)
