# Protected Layer-Manifold Theory

> Sources: project specification, 2026-09-20; full-text literature synthesis, 2026-09-20
> Raw: [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## Status and claim boundary

This page derives the mechanism proposed in `SPEC.md`. It is a **working analytic hypothesis**, not a verified result. In particular, the bounds below explain what would make sparse intra-layer connectivity protective; they do not establish that any tested graph family changes the asymptotic exit scaling. That claim still requires the frozen numerical, ensemble, scaling, mechanism, and accessibility verifiers.

The central question is whether fixed added degree $k=O(1)$ and fixed coupling ratio $J_{
m LR}/J_{
m GT}=O(1)$ can change

$$
\left\langle \overline P_{\rm exit}^{(\infty)}(L)\right\rangle
\sim e^{-L/\xi}
\quad\text{to}\quad
\left\langle \overline P_{\rm exit}^{(\infty)}(L)\right\rangle
\sim L^{-\alpha}.
$$

An increase of localization length, a favorable finite-$L$ crossover, or a narrow resonance in $J_{\rm LR}$ is not sufficient.

## Symmetric transport channel

For layer $V_\ell$ of size $n_\ell$, define

$$
|S_\ell\rangle=\frac{1}{\sqrt{n_\ell}}\sum_{i\in V_\ell}|i\rangle,
\qquad
P=\sum_{\ell=0}^{2L+1}|S_\ell\rangle\langle S_\ell|,
\qquad Q=I-P.
$$

The clean glued-tree backbone preserves $P\mathcal H$. If $m_\ell$ is the number of backbone edges between adjacent layers, then

$$
\langle S_{\ell+1}|A_{\rm GT}|S_\ell\rangle
=\frac{m_\ell}{\sqrt{n_\ell n_{\ell+1}}}.
$$

For each binary-tree step, $m_\ell=2n_\ell$ and $n_{\ell+1}=2n_\ell$, so the reduced hopping is $\sqrt{2}J_{\rm GT}$. Across the two leaf layers, both have size $2^L$ and the 2-regular bipartite gluing contains $2^{L+1}$ edges, so the reduced hopping is $2J_{\rm GT}$. Thus the clean exponentially large graph contains an exact $(2L+2)$-dimensional transport chain:

$$
PH_{\rm GT}P
=-J_{\rm GT}\!\left[
\sqrt{2}\!\sum_{\ell\ne L}
(|S_{\ell+1}\rangle\langle S_\ell|+\text{h.c.})
+2(|S_{L+1}\rangle\langle S_L|+\text{h.c.})
\right]
$$

for the adjacency convention, with the corresponding backbone-strength diagonal added for the Laplacian convention.

This reduction explains the clean ballistic channel. Static site disorder breaks the layer permutation symmetry and couples it to the exponentially larger $Q$ sector.

## What regular intra-layer graphs do

Let a protected layer have a $k$-regular unweighted adjacency matrix $A_\ell$. Then

$$
A_\ell|S_\ell\rangle=k|S_\ell\rangle.
$$

For the adjacency CTQW, the symmetric mode receives the energy shift

$$
\langle S_\ell|(-J_{\rm LR}A_\ell)|S_\ell\rangle=-kJ_{\rm LR},
$$

and its separation from the nearest nonsymmetric adjacency eigenmode is the candidate scale

$$
\Delta_\ell^{(A)}
=J_{\rm LR}\bigl(k-\lambda_{2,\ell}^{(A)}\bigr).
$$

For the Laplacian CTQW, $L_\ell=kI-A_\ell$ annihilates the symmetric state while nonsymmetric modes begin at the algebraic connectivity:

$$
L_\ell|S_\ell\rangle=0,
\qquad
\Delta_\ell^{(L)}=J_{\rm LR}\lambda_2(L_\ell).
$$

The two conventions therefore implement protection differently. Laplacian coupling leaves the symmetric layer energy unchanged and raises transverse modes. Adjacency coupling lowers the symmetric mode relative to them, but it also shifts all protected layers relative to the unprotected entrance and exit. Endpoint or layer bias may be needed to distinguish genuine leakage suppression from simple detuning.

Fixed degree alone is not enough. A cycle has

$$
\lambda_2(L_{C_n})=2-2\cos(2\pi/n)\sim 4\pi^2/n^2,
$$

so its transverse protection scale closes with layer size. Fixed-degree expander-like families can instead retain a nonzero asymptotic gap. Random regular, circulant, and capped small-world graphs must be judged by their measured spectra; expansion cannot be inferred from their names.

## Disorder projection and leakage

Write the disorder in layer $\ell$ as

$$
\epsilon_i=\bar\epsilon_\ell+\delta\epsilon_i,
\qquad
\bar\epsilon_\ell=\frac1{n_\ell}\sum_{i\in V_\ell}\epsilon_i,
\qquad
\sum_i\delta\epsilon_i=0.
$$

The direct projection is purely longitudinal:

$$
PV_{\rm dis}P
=\sum_\ell\bar\epsilon_\ell|S_\ell\rangle\langle S_\ell|.
$$

For iid $\epsilon_i\sim U[-W,W]$, with variance $\sigma^2=W^2/3$,

$$
\operatorname{Var}(\bar\epsilon_\ell)=\frac{W^2}{3n_\ell}.
$$

The off-manifold coupling vector is

$$
QV_{\rm dis}|S_\ell\rangle
=\frac1{\sqrt{n_\ell}}\sum_{i\in V_\ell}\delta\epsilon_i|i\rangle,
$$

with expected squared norm

$$
\mathbb E\left\|QV_{\rm dis}|S_\ell\rangle\right\|^2
=\frac{W^2}{3}\left(1-\frac1{n_\ell}\right).
$$

This distinction is essential: the first-order layer mean self-averages as $n_\ell^{-1/2}$, but the **total** coupling from one symmetric layer state into all nonsymmetric modes remains $O(W)$. Protection cannot rely on layer averaging alone; it needs spectral denominators, selection structure, or a different demonstrated mechanism.

A uniform bias $b_\ell=-\bar\epsilon_\ell$ cancels $PV_{\rm dis}P$ exactly, including on the entrance and exit singleton layers. It does not remove $QV_{\rm dis}P$, nor does it cancel the self-energy generated by virtual excursions through $Q$.

## Feshbach effective Hamiltonian

Block the full Hamiltonian as

$$
H=
\begin{pmatrix}
PHP & PHQ\\
QHP & QHQ
\end{pmatrix}.
$$

Eliminating the $Q$-component of an eigenstate at energy $E$ gives

$$
H_{\rm eff}(E)
=PHP+\Sigma(E),
\qquad
\Sigma(E)=PHQ(E-QHQ)^{-1}QHP.
$$

For a clean regular construction, backbone and intra-layer terms preserve $P$, so the leading $PHQ$ is generated by residual onsite disorder. If the relevant transport energy is separated from the $Q$-sector spectrum by

$$
\delta(E)=\operatorname{dist}\bigl(E,\operatorname{spec}(QHQ)\bigr)>0,
$$

then

$$
\|\Sigma(E)\|
\le \frac{\|PHQ\|^2}{\delta(E)},
\qquad
\|Q|\psi\rangle\|
\lesssim \frac{\|QHP\|}{\delta(E)}\|P|\psi\rangle\|.
$$

The perturbative leakage probability is therefore expected to scale as

$$
p_{\rm leak}=O\!\left(\frac{W^2}{\delta^2}\right),
$$

while the induced longitudinal energy correction is generically

$$
\delta H_{\rm long}=O\!\left(\frac{W^2}{\delta}\right).
$$

For a genuinely gapped transverse family, $\delta\propto J_{\rm LR}g_\mathcal G$, where $g_\mathcal G$ is an appropriate measured adjacency or Laplacian separation. This gives the testable strong-coupling prediction

$$
p_{\rm leak}\propto \frac{W^2}{J_{\rm LR}^2g_\mathcal G^2},
\qquad
\delta H_{\rm long}\propto \frac{W^2}{J_{\rm LR}g_\mathcal G},
$$

until the result saturates at the clean projected dynamics. It explains why a true passive mechanism should improve or saturate with $J_{\rm LR}$, not exist only at a narrow resonance.

These expressions are controlled only when the resolvent distance stays open over the transport band. A nominal layer gap is insufficient if nonsymmetric bands from different layers overlap the longitudinal energies, if irregular degrees introduce additional $P$–$Q$ coupling, or if disorder closes the separation.

## Candidate threshold and competing mechanisms

A useful dimensionless leakage parameter is

$$
\eta(E)=\max_\ell
\frac{\|QV_{\rm dis}|S_\ell\rangle\|}{
\operatorname{dist}(E,\operatorname{spec}QHQ)}.
$$

The projected theory predicts a crossover when $\eta$ becomes $O(1)$. A stronger transport criterion also asks that the induced longitudinal disorder remain below the clean channel scale:

$$
\frac{W^2}{J_{\rm LR}g_\mathcal G}\ll J_{\rm GT}.
$$

These estimates suggest, but do not prove, thresholds of order

$$
J_{\rm LR}g_\mathcal G\gtrsim W
\quad\text{and possibly}\quad
J_{\rm LR}g_\mathcal G\gg \frac{W^2}{J_{\rm GT}}.
$$

Numerics must decide which scale is relevant. They must also distinguish spectral protection from alternatives: increased bandwidth, changed density of states, a longer but finite localization length, rare high-transmission samples, endpoint detuning, or bias-driven cancellation.

## Mechanism observables

The minimum direct diagnostics are

$$
P_{\rm sym}(t)=\langle\psi(t)|P|\psi(t)\rangle
$$

and, for an occupied layer,

$$
C_\ell(t)=
\frac{|\sum_{i\in V_\ell}\psi_i(t)|^2}
{n_\ell\sum_{i\in V_\ell}|\psi_i(t)|^2}.
$$

A spectral-gap mechanism should jointly predict:

1. decreasing $1-P_{\rm sym}$ as $J_{\rm LR}g_\mathcal G/W$ grows;
2. increasing intralayer coherence $C_\ell$;
3. a self-energy or leakage rate consistent with measured $QHQ$ spectra;
4. stronger protection for graph families with larger measured transverse separation at the same degree and coupling;
5. monotonic improvement or saturation rather than a narrow optimum;
6. a corresponding, verifier-supported change in the large-$L$ exit scaling.

The first five without the sixth establish a mechanism for finite-size protection, not the North-Star asymptotic claim.

## Observable and operational boundary

The primary observable remains

$$
\overline P_{\rm exit}^{(\infty)}
=\sum_{E_a=E_b}
\langle OUT|E_a\rangle\langle E_a|IN\rangle
\langle IN|E_b\rangle\langle E_b|OUT\rangle,
$$

with exact handling of degeneracies. It is a long-time occupation, not a first-passage probability. Any claim of recovered operational or algorithmic advantage also needs a polynomial-time window $T(L)$ for which

$$
\overline P_{\rm exit}(T(L),L)\ge 1/\operatorname{poly}(L).
$$

The literature supplies close analogies—cavity bright/dark protection, interaction-gapped magnetization, exchange narrowing, and manifold-protected squeezing—but none proves the glued-tree scaling result. Their value is to sharpen the denominators, observables, and falsification tests used here.

## See Also

- [Research Program](../project/research-program.md)
- [Paper-Readiness Criteria](../project/paper-readiness-criteria.md)
- [Organized Literature Map](../literature/organized-literature-map.md)
- [Disorder, Localization, and Asymptotic Evidence](../concepts/disorder-localization-and-asymptotic-evidence.md)
- [Coherence Protection Mechanisms](../concepts/coherence-protection-mechanisms.md)
