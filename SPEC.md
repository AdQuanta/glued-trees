# SPEC.md — Sparse Intra-Layer Protection of Disordered Continuous-Time Quantum Walks

## 0. Purpose and governance

This specification governs the **research program** for a theory project on passive protection of continuous-time quantum walks (CTQWs) against static on-site disorder using sparse intra-layer connectivity.

The intended scientific endpoint is a high-impact PRL / Nature Physics-level result. This specification owns the project **through `paper_ready`**, meaning that the scientific claims, analytic understanding, numerical evidence, robustness checks, reproducibility records, and required generalizations are complete enough to support manuscript writing. The manuscript itself is governed by a separate future workflow/specification.

This file is intended to be dropped into an **existing research codebase**. It must therefore be repository-adaptive:

- reuse the existing language(s), environment, tooling, scheduler, testing framework, and directory conventions where practical;
- add only the research-loop infrastructure needed to execute this spec;
- do not gratuitously restructure the repository;
- do not prescribe a new wiki structure at this stage.

### 0.1 Human/agent division of authority

The governing rule is:

> **The project owner controls WHAT is solved. The research agent controls HOW it is solved.**

For every scientific hypothesis check:

1. the hypothesis, scientific question, fixed model/regime, primary observable, required comparisons, success evidence, falsification evidence, and required verifiers must be planned jointly with the project owner;
2. the project owner must explicitly approve that hypothesis check **before execution**;
3. after approval, the agent may freely choose and adapt numerical methods, analytic techniques, solver implementations, parameter resolution, convergence settings, ensemble sizes, computational resources, and debugging strategy needed to answer the approved question rigorously;
4. the agent may not change the scientific question, primary observable, comparison being made, success/failure criteria, or scope of the approved check without returning to the project owner.

The agent may propose new hypotheses or branches, but **may not execute them before approval**.

### 0.2 Verifier governance

Verifiers are treated as frozen research infrastructure once approved.

- A verifier may not be weakened, bypassed, reinterpreted, or edited because a desired result failed.
- The agent may identify a scientific defect or omission in a verifier and propose a change.
- **No verifier change may occur without explicit approval from the project owner.**
- Every approved verifier revision must be versioned and logged.
- Results must record the exact verifier versions under which they were evaluated.

Judgment-heavy verifiers, especially scaling, mechanism, and paper-readiness verifiers, should be executed by a **fresh-context agent** that receives the frozen verifier criteria and submitted evidence bundle but not the persuasive exploratory history of the result.

### 0.3 Scientific completion versus `paper_ready`

A rigorous negative result is a valid completion state for a hypothesis or even for the central research program. The agent must never move goalposts, tune indefinitely, or selectively reinterpret evidence in order to obtain the desired positive story.

Possible top-level scientific outcomes include:

- `SUPPORTED`
- `FALSIFIED`
- `INCONCLUSIVE`
- `BLOCKED_BY_RESOURCES`
- `PAPER_READY`

A central hypothesis may be falsified while the research process is scientifically successful.

`paper_ready = true` is a stronger positive-story condition defined explicitly in Section 22.

---

# 1. North Star

The central question is:

> **Can bounded-degree, size-independent, long-range intra-layer connectivity passively protect a disordered CTQW on a glued-trees network strongly enough to change the asymptotic infinite-time-averaged exit probability from exponential decay in tree depth to power-law decay?**

The desired asymptotic change is

\[
\boxed{
\left\langle \overline P_{\rm exit}^{(\infty)}(L)\right\rangle
\sim e^{-L/\xi}
\quad\longrightarrow\quad
\left\langle \overline P_{\rm exit}^{(\infty)}(L)\right\rangle
\sim L^{-\alpha}
}
\]

under a protection scheme in which both

\[
k=O(1),
\qquad
J_{\rm LR}/J_{\rm GT}=O(1)
\]

remain independent of tree depth \(L\) and total graph size \(N\).

The research must determine **why** protection occurs. A preferred working hypothesis is given in Section 7, but the mechanism is not assumed and must be proved, falsified, or replaced by a better explanation.

---

# 2. Canonical glued-trees backbone

## 2.1 Geometry

The canonical graph consists of two depth-\(L\) binary trees:

- the root of the left tree is the entrance state \(|{\rm IN}\rangle\);
- the root of the right tree is the exit state \(|{\rm OUT}\rangle\);
- each tree has \(2^L\) leaves;
- every leaf of either tree has exactly **two** gluing edges to leaves of the opposite tree.

The leaf-to-leaf gluing is therefore a random **2-regular bipartite graph** between the two leaf sets. A valid implementation is the union of two random perfect matchings, with duplicate edges rejected/resampled if the graph is required to be simple.

Every leaf has:

- one parent edge inside its binary tree;
- two random cross-tree gluing edges;

and hence backbone degree three.

The nominal development workflow initially fixes one gluing realization. Final paper-level validation must additionally average over independent gluing realizations.

## 2.2 Layer convention

Use a source-to-target layer index

\[
\ell=0,1,\ldots,2L+1,
\]

where:

- \(\ell=0\): \(|{\rm IN}\rangle\);
- \(\ell=1,\ldots,L\): successive left-tree generations, with \(\ell=L\) the left leaf layer;
- \(\ell=L+1\): the right leaf layer;
- \(\ell=L+2,\ldots,2L+1\): successive generations toward the right-tree root;
- \(\ell=2L+1\): \(|{\rm OUT}\rangle\).

Let \(V_\ell\) be the vertex set of layer \(\ell\), \(n_\ell=|V_\ell|\), and

\[
\Pi_\ell=\sum_{i\in V_\ell}|i\rangle\langle i|.
\]

All nontrivial layers except the singleton entrance and exit layers may receive added intra-layer connectivity. **Every layer, including IN and OUT, may receive a uniform layer bias.**

---

# 3. Hamiltonians

The project must investigate both weighted-adjacency and weighted-Laplacian CTQWs as first-class cases.

Let the full graph after adding protection edges be \(G=(V,E)\). Let real symmetric couplings satisfy

\[
J_{ij}=J_{ji}.
\]

For the Laplacian convention, weights are assumed nonnegative unless an explicitly approved hypothesis check changes that assumption.

The disorder term is

\[
\boxed{
V_{\rm dis}
=
\sum_{i\in V}\epsilon_i |i\rangle\langle i|
}
\]

with static independent disorder

\[
\boxed{
\epsilon_i\overset{\rm iid}{\sim}U[-W,W].
}
\]

The disorder is quenched and time-independent. Time-dependent noise, dephasing baths, Lindblad dynamics, or correlated disorder are outside the present core scope.

## 3.1 Weighted-adjacency CTQW

Define the weighted adjacency operator

\[
A_J
=
\sum_{\{i,j\}\in E}
J_{ij}
\left(
|i\rangle\langle j|+|j\rangle\langle i|
\right).
\]

The adjacency walk Hamiltonian is

\[
\boxed{
H_A=-A_J+V_{\rm dis}+H_{\rm bias}.
}
\]

Explicitly,

\[
\boxed{
H_A
=
-\sum_{\{i,j\}\in E}
J_{ij}
\left(
|i\rangle\langle j|+|j\rangle\langle i|
\right)
+
\sum_i\epsilon_i|i\rangle\langle i|
+
\sum_\ell b_\ell\Pi_\ell .
}
\]

## 3.2 Weighted-Laplacian CTQW

Define the weighted strength of vertex \(i\),

\[
s_i=\sum_{j:\{i,j\}\in E}J_{ij},
\]

and

\[
D_J=\sum_i s_i|i\rangle\langle i|,
\qquad
L_J=D_J-A_J.
\]

The Laplacian walk Hamiltonian is

\[
\boxed{
H_L=L_J+V_{\rm dis}+H_{\rm bias}.
}
\]

Explicitly,

\[
\boxed{
H_L
=
-\sum_{\{i,j\}\in E}
J_{ij}
\left(
|i\rangle\langle j|+|j\rangle\langle i|
\right)
+
\sum_i
\left(
s_i+\epsilon_i
\right)|i\rangle\langle i|
+
\sum_\ell b_\ell\Pi_\ell.
}
\]

Thus, for the same off-diagonal hopping matrix,

\[
H_L-H_A=D_J.
\]

Adjacency and Laplacian dynamics may differ substantially on the protected graph because added intra-layer connectivity can make the graph irregular.

## 3.3 Nominal two-coupling specialization

Although the implementation may support irregular \(J_{ij}\), the nominal physical model uses two uniform coupling scales:

\[
J_{ij}
=
\begin{cases}
J_{\rm GT}, & \{i,j\}\in E_{\rm GT},\\[1mm]
J_{\rm LR}, & \{i,j\}\in E_{\rm intra}.
\end{cases}
\]

Use \(J_{\rm GT}\) as the energy unit when convenient.

The added intra-layer coupling must be uniform across protected layers in a given run:

\[
J_{\rm LR}^{(\ell)}=J_{\rm LR}.
\]

The key resource constraint is

\[
\boxed{
J_{\rm LR}/J_{\rm GT}=O(1)\quad \text{as }L,N\to\infty.
}
\]

A scheme does **not** count as successful if its required \(J_{\rm LR}\) must grow with \(L\), \(\log N\), \(N^\alpha\), or any other system-size-dependent scale.

For a fixed disorder strength \(W\), \(J_{\rm LR}\) may depend on \(W\), but not on \(L\) or \(N\).

---

# 4. Added intra-layer connectivity

## 4.1 Hard definition of sparse

For vertex \(i\), define the added intra-layer degree

\[
k_i^{\rm add}
=
\#\{
\text{added protection edges incident on }i
\}.
\]

A protection family is **sparse** only if there exists a finite constant \(K\), independent of both \(L\) and \(N\), such that

\[
\boxed{
k_i^{\rm add}\le K
\qquad
\forall i,L,N.
}
\]

Equivalently, every node receives only \(O(1)\) added edges, where \(O(1)\) explicitly means **does not scale with \(N\) or \(L\)**.

The total number of added edges may still scale as \(O(N)\).

Any graph family implementation used as a sparse candidate must respect this strict maximum-added-degree condition, not merely constant expected degree.

## 4.2 Which layers are protected

Every layer except the singleton entrance and exit layers receives intra-layer connectivity:

\[
\boxed{
E_{\rm intra}
=
\bigcup_{\ell=1}^{2L}
E_{\rm intra}^{(\ell)}.
}
\]

IN and OUT do not receive intra-layer edges.

## 4.3 Sampling rule across layers

Within a given experiment:

- all protected layers use the **same network family**;
- the family parameter \(k\), where applicable, is uniform across layers;
- \(J_{\rm LR}\) is uniform across layers;
- the actual graph realization in each layer is sampled **independently** from that family.

Thus topology is not replicated layer-to-layer unless a separately approved hypothesis check explicitly tests such correlations.

## 4.4 Required network families

The initial family set is:

1. **Nominal / no intra-layer coupling**
   \[
   E_{\rm intra}^{(\ell)}=\varnothing.
   \]

2. **Nearest-neighbor coupling only**
   - open boundary conditions: path graph within each layer;
   - periodic boundary conditions: cycle graph within each layer.

3. **\(k\)-circulant graphs**
   - fixed-size generator/offset set independent of \(L,N\);
   - exact generator convention must be recorded in the approved experiment contract.

4. **Random \(k\)-regular graphs**
   - fixed \(k=O(1)\);
   - independently sampled in every layer;
   - expected to be expander-like with high probability for suitable fixed \(k\), but expansion must be measured rather than assumed when used mechanistically.

5. **Watts-Strogatz small-world graphs**
   - implemented subject to the project's hard bounded-added-degree condition;
   - if a canonical rewiring realization violates the maximum-degree cap, use rejection/resampling or a degree-preserving/capped implementation;
   - exact convention and rewiring probability must be recorded.

6. **All-to-all intra-layer coupling**
   - included as an important dense limiting/control case;
   - explicitly **not sparse**;
   - it may illuminate mechanism or asymptotic limits but cannot by itself satisfy the sparse-protection claim.

The family set may be expanded only through an explicitly approved new hypothesis check.

---

# 5. Layer biasing

Uniform biasing within each layer is allowed:

\[
\boxed{
H_{\rm bias}
=
\sum_{\ell=0}^{2L+1} b_\ell\Pi_\ell.
}
\]

Biasing is allowed on **all** layers, including IN and OUT.

The bias may be:

- layer-dependent;
- disorder-realization-dependent;
- fine-tuned if useful.

A canonical allowed example is cancellation of the layer-mean onsite disorder:

\[
\bar\epsilon_\ell
=
\frac{1}{n_\ell}\sum_{i\in V_\ell}\epsilon_i,
\qquad
b_\ell=-\bar\epsilon_\ell.
\]

This removes the disorder component seen directly by the layer-symmetric state:

\[
\langle S_\ell|
(V_{\rm dis}+H_{\rm bias})
|S_\ell\rangle=0.
\]

The residual fluctuations

\[
\delta\epsilon_i=\epsilon_i-\bar\epsilon_\ell
\]

remain and may continue to couple symmetric and nonsymmetric modes.

Biasing is considered a **technical auxiliary control** that may mitigate residual Anderson localization in the effective one-dimensional layer dynamics. The central scientific resource is the sparse long-range intra-layer connectivity.

Therefore:

- power-law recovery is allowed to require layer biasing;
- unbiased results must still be computed as a diagnostic that separates the roles of connectivity and bias;
- every bias rule must be documented in the approved experiment contract and evidence bundle;
- site-resolved cancellation of individual \(\epsilon_i\) values is outside the current scope unless separately approved.

---

# 6. Primary observable: exit probability

Initialize the walker at the entrance:

\[
|\psi(0)\rangle=|{\rm IN}\rangle.
\]

The instantaneous exit probability is

\[
\boxed{
P_{\rm exit}(t;L)
=
\left|
\langle {\rm OUT}|e^{-iHt}|{\rm IN}\rangle
\right|^2.
}
\]

The primary scientific observable is the infinite-time average:

\[
\boxed{
\overline P_{\rm exit}^{(\infty)}(L)
=
\lim_{T\to\infty}
\frac{1}{T}
\int_0^T
P_{\rm exit}(t;L)\,dt.
}
\]

For an exact spectral decomposition, degeneracies must be handled correctly:

\[
\overline P_{\rm exit}^{(\infty)}
=
\sum_{\substack{a,b\\E_a=E_b}}
\langle {\rm OUT}|E_a\rangle
\langle E_a|{\rm IN}\rangle
\langle {\rm IN}|E_b\rangle
\langle E_b|{\rm OUT}\rangle.
\]

For a nondegenerate spectrum this reduces to

\[
\overline P_{\rm exit}^{(\infty)}
=
\sum_a
|\langle {\rm OUT}|E_a\rangle|^2
|\langle E_a|{\rm IN}\rangle|^2.
\]

This is a long-time occupation diagnostic, **not** a first-passage probability and not an absorbing-boundary hitting probability.

## 6.1 Ensemble average

During initial discovery, fix the random glued-tree leaf gluing and average over:

1. onsite disorder realizations;
2. independent intra-layer graph realizations.

The main development observable is therefore

\[
\boxed{
\left\langle
\overline P_{\rm exit}^{(\infty)}(L)
\right\rangle_{\epsilon,\mathcal G}.
}
\]

For final paper-level validation, additionally average over independent glued-tree gluing realizations:

\[
\boxed{
\left\langle
\overline P_{\rm exit}^{(\infty)}(L)
\right\rangle_{\epsilon,\mathcal G,{\rm GT}}.
}
\]

The arithmetic ensemble mean is the **headline scaling quantity**.

Because broad distributions may occur, the distribution, median, and typical value

\[
P_{\rm typ}
=
\exp\left[
\left\langle
\ln \overline P_{\rm exit}^{(\infty)}
\right\rangle
\right]
\]

should be retained as robustness diagnostics so that an apparent algebraic ensemble mean is not unknowingly dominated by rare high-transmission realizations.

---

# 7. Working physical mechanism — hypothesis, not assumption

For each layer define the normalized layer-symmetric state

\[
\boxed{
|S_\ell\rangle
=
\frac{1}{\sqrt{n_\ell}}
\sum_{i\in V_\ell}|i\rangle.
}
\]

Define the layer-symmetric transport manifold

\[
\boxed{
\mathcal H_{\rm sym}
=
{\rm span}\{
|S_0\rangle,\ldots,|S_{2L+1}\rangle
\},
}
\]

with projector

\[
P\equiv \Pi_{\rm sym}
=
\sum_\ell |S_\ell\rangle\langle S_\ell|,
\qquad
Q=I-P.
\]

The working physical picture is:

\[
\boxed{
\text{intra-layer connectivity}
\rightarrow
\text{full walk stays closer to }\mathcal H_{\rm sym}
\rightarrow
\text{intra-layer phase coherence is preserved}
\rightarrow
\text{coherent longitudinal propagation is restored}.
}
\]

A more precise candidate mechanism is **spectral suppression of disorder-induced leakage** from \(\mathcal H_{\rm sym}\) into nonsymmetric intra-layer modes.

For a \(k\)-regular adjacency layer,

\[
A_\ell|S_\ell\rangle=k|S_\ell\rangle.
\]

A candidate protection scale may involve separation of the symmetric eigenvalue from the nonsymmetric spectrum, for example

\[
\Delta_{\ell}^{(A)}
\sim
J_{\rm LR}
\left(
k-\lambda_{2,\ell}^{(A)}
\right),
\]

or, for a Laplacian layer,

\[
\Delta_{\ell}^{(L)}
\sim
J_{\rm LR}\lambda_{2,\ell}(L_\ell).
\]

This spectral-gap hypothesis is **not presumed true**.

The project must actively distinguish among possible mechanisms, including but not limited to:

- spectral separation of the symmetric state;
- algebraic connectivity / expansion;
- suppression of \(Q V_{\rm dis}P\)-induced leakage;
- density of nonsymmetric states near the transport band;
- effective self-energy of the symmetric sector;
- localization-length changes;
- participation properties / IPR;
- generic connectivity or bandwidth effects unrelated to a graph spectral gap.

The agent must be willing to replace the initial mechanism if evidence points elsewhere.

## 7.1 Mandatory mechanistic observables

At minimum, candidate protected regimes must permit evaluation of the symmetric-manifold occupation

\[
\boxed{
P_{\rm sym}(t)
=
\langle\psi(t)|P|\psi(t)\rangle.
}
\]

A useful intralayer coherence diagnostic is

\[
\boxed{
C_\ell(t)
=
\frac{
\left|\sum_{i\in V_\ell}\psi_i(t)\right|^2
}{
n_\ell
\sum_{i\in V_\ell}|\psi_i(t)|^2
},
\qquad
0\le C_\ell\le1,
}
\]

whenever the denominator is nonzero.

\(C_\ell=1\) corresponds to perfectly equal-phase amplitudes within that layer. The term “phase synchronization” should not be used as a manuscript-level explanation unless an operational diagnostic such as this, or a better justified one, actually supports it.

---

# 8. Mandatory analytic theory

A positive numerical observation is insufficient for `paper_ready`.

The project must derive an analytic or controlled approximate theory of the protection mechanism. At minimum, analyze:

\[
PHP,
\qquad
QHP,
\qquad
PHQ,
\qquad
QHQ.
\]

The theory must address:

1. the effective dynamics inside \(\mathcal H_{\rm sym}\);
2. the way onsite disorder couples \(\mathcal H_{\rm sym}\) to nonsymmetric modes;
3. how intra-layer connectivity modifies that coupling or the relevant energy denominators;
4. residual effective longitudinal disorder after projection;
5. the role of layer biasing;
6. the dependence of protection on
   \[
   W,\quad J_{\rm LR},\quad k,
   \]
   and measurable graph properties;
7. why stronger \(J_{\rm LR}\) should improve or saturate protection rather than require a narrow resonance, if that monotonic mechanism is correct;
8. a theoretically motivated threshold or crossover criterion whenever possible;
9. the relation between analytic predictions and numerical finite-size scaling.

Schrieffer-Wolff/Feshbach projection, resolvent/self-energy methods, perturbation theory, random-matrix arguments, localization theory, or other appropriate methods may be used. The spec fixes the scientific questions, not the analytic technique.

The theory must clearly state its regime of validity and must not be presented as exact outside that regime.

---

# 9. Protection-strength requirement: no fine-tuned \(J_{\rm LR}\)

A successful sparse protection scheme must not rely on a narrow resonance or a finely tuned coupling value.

For fixed \(W\), \(k\), and graph family, increasing \(J_{\rm LR}\) should, over the physically relevant strong-coupling regime,

- improve protection, or
- lead to saturation,

rather than produce a narrow isolated optimum beyond which protection disappears.

Finite-size fluctuations or small non-monotonic wiggles are acceptable. A scheme whose claimed restoration exists only near

\[
J_{\rm LR}\approx J_{\rm LR}^\star
\]

with substantial deterioration for modestly larger \(J_{\rm LR}\) does **not** satisfy the intended passive-protection criterion unless a new scientific interpretation is explicitly approved.

This monotonic/saturating behavior must be evaluated at the ensemble and scaling level, not demanded realization-by-realization.

---

# 10. Disorder-strength question and asymptotic transition

The strong working hypothesis is:

\[
\boxed{
\forall\, W<\infty,\quad
\exists\,J_{\rm LR}^\star(W)<\infty
}
\]

such that, at fixed

\[
J_{\rm LR}>J_{\rm LR}^\star(W),
\]

with \(J_{\rm LR}\) independent of \(L,N\), the asymptotic exit probability changes from exponential to algebraic scaling in \(L\).

This is a hypothesis to test, not an assumption.

If the strong hypothesis fails, the project must characterize the boundary

\[
W_c(J_{\rm LR},k,\mathcal G)
\]

or the appropriate replacement relation.

A central task is to determine whether the observed change is:

- a true asymptotic transition;
- a finite-size crossover;
- or merely a large enhancement of localization length without a change in asymptotic scaling class.

Any claim of a “phase transition” is fundamentally an \(L\to\infty\) claim. Finite-\(L\) curves may show only smooth crossover behavior and must not be called a phase transition without appropriate finite-size evidence.

If a threshold exists, the project should seek critical/scaling structure when justified, but should not force a phase-transition narrative onto crossover data.

---

# 11. Scaling and statistical rigor

The central scaling claim must never be established solely by visual straightness on a log plot or by a single \(R^2\).

At minimum, the scaling analysis must compare:

### Exponential

\[
P(L)=A e^{-L/\xi}.
\]

### Stretched exponential

\[
P(L)=A\exp\left[-(L/\xi)^\beta\right].
\]

### Power law

\[
P(L)=A L^{-\alpha}.
\]

Additional plausible forms may be included if scientifically justified and approved as part of the check.

## 11.1 Required robustness

The scaling verifier must require, at minimum:

- explicit uncertainty treatment;
- statistically justified model comparison, such as likelihood-based and/or information-criterion methods;
- residual diagnostics where appropriate;
- repeated fits over increasingly asymptotic \(L\)-windows;
- stability of inferred parameters, especially \(\alpha\), under removal of smaller-\(L\) points;
- rerunning the model comparison when larger \(L_{\max}\) becomes available;
- rejection of “power-law” claims that occur only over a narrow transient window;
- explicit documentation when accessible sizes cannot distinguish a power law from a stretched exponential.

No local effective exponent \(\alpha_{\rm eff}(L)\) is required by this specification.

## 11.2 Ensemble statistics

For every central parameter point, increase the number of joint disorder/network realizations until the relevant ensemble statistics converge.

Do not assume Gaussian sample statistics.

Use an uncertainty method appropriate to the observed distribution, for example bootstrap, batch means, or another justified robust method.

The verifier must check that:

- the estimated mean is stable as sample count increases;
- confidence intervals are stable;
- successive added batches do not show systematic drift;
- rare-event domination is diagnosed using the distribution/median/typical value where relevant.

The exact target sample count is not fixed by this spec; convergence is the criterion.

---

# 12. Numerical correctness and convergence

The agent is free to choose the numerical implementation, including exact diagonalization, sparse eigensolvers, Krylov propagation, shift-invert methods, stochastic methods, effective theories, tensor/network methods, or other techniques.

The agent must be honest about computational limitations.

A result is not verified until the relevant convergence tests pass.

## 12.1 Small-system exact cross-check

Whenever feasible, benchmark approximate/scalable methods against exact calculations at small \(L\).

Cross-check quantities such as:

\[
\overline P_{\rm exit}^{(\infty)},
\qquad
P_{\rm exit}(t),
\qquad
P_{\rm sym}(t),
\]

and any mechanism-specific quantity central to the claim.

## 12.2 Solver convergence

For the chosen algorithm, tighten the relevant numerical controls until the scientific observable is stable within a justified tolerance.

Examples include:

- eigensolver tolerance;
- number of eigenpairs;
- Krylov subspace dimension;
- time step;
- propagation tolerance;
- spectral cutoff;
- stochastic sample count;
- linear-solver tolerance.

The evidence bundle must contain an actual convergence record, not merely a statement that convergence was checked.

## 12.3 Infinite-time-average convergence

When computed spectrally, verify eigenvalue resolution and degeneracy handling.

When computed through finite-time integration,

\[
\overline P_{\rm exit}(T)
=
\frac1T\int_0^T P_{\rm exit}(t)\,dt,
\]

test increasing windows such as

\[
T,\;2T,\;4T
\]

until the estimate stabilizes.

Where practical, spectral and time-domain evaluations should cross-check each other on overlapping system sizes.

## 12.4 Finite-size convergence

The central scientific conclusion must be repeatedly reevaluated as larger \(L\) values are added.

If the accessible range is insufficient to distinguish asymptotic forms, record the result as `INCONCLUSIVE`; do not promote the desired model by preference.

---

# 13. Mandatory secondary diagnostic: finite-time accessibility

Infinite-time algebraic exit weight may be operationally misleading if it appears only after exponentially long evolution.

Therefore, finite-time accessibility is a **mandatory secondary diagnostic**.

Define

\[
\boxed{
\overline P_{\rm exit}(T,L)
=
\frac1T
\int_0^T
P_{\rm exit}(t;L)\,dt.
}
\]

The diagnostic asks whether there exists a polynomial time scale

\[
T(L)=\operatorname{poly}(L)
\]

for which

\[
\overline P_{\rm exit}(T(L),L)
\]

remains only polynomially small.

A useful target form is

\[
\exists\, T(L)=\operatorname{poly}(L):
\qquad
\overline P_{\rm exit}(T(L),L)
\ge
\frac{1}{\operatorname{poly}(L)}.
\]

This check is mandatory, but **a negative accessibility result does not automatically invalidate the primary infinite-time protection result**.

Interpretation:

- if accessibility is polynomial, language about recovered algorithmic/operational quantum advantage may be strengthened;
- if accessibility is exponential or unresolved, the infinite-time result may still be scientifically important, but claims must be restricted accordingly.

The accessibility verifier therefore verifies that the diagnostic was executed rigorously and classifies the outcome; `paper_ready` does not require a positive accessibility outcome unless the eventual headline claim explicitly depends on it.

---

# 14. Classical sanity check

The project is not primarily a study of classical random walks.

Nevertheless, because the paper may invoke “recovered quantum advantage,” perform a lightweight classical sanity check on the same protected graph family.

The purpose is only to verify that the added bounded-degree intra-layer connections do not trivially change the classical source-to-target scaling in a way that undermines the quantum-advantage narrative.

Do not turn this into a large optimization branch unless jointly approved.

---

# 15. Generalization beyond glued trees

Glued trees are the primary mechanism-discovery platform, but a high-impact paper must demonstrate that the protection principle is not merely a repair of one contrived graph.

`paper_ready` requires at least **one successful non-glued-tree generalization** that is genuinely distinct from the canonical glued-tree example.

Preference order:

1. an application or graph with **algorithmic utility**;
2. another meaningful quantum-information transport task;
3. a strong broader physical transport example if no convincing algorithmic extension survives.

Candidate utility classes may include, but are not fixed to:

- quantum search;
- traversal;
- routing;
- coherent state transfer;
- other CTQW algorithmic primitives.

The exact generalization is intentionally **not frozen now**. It must be proposed and approved through the normal hypothesis-check process.

The goal is to generalize the **principle** of passive protection of a low-dimensional coherent transport channel using bounded-degree transverse connectivity, not merely to repeat similar numerics on a cosmetic graph variant.

---

# 16. Hypothesis-check contract

No new scientific hypothesis check may be executed until the project owner approves an explicit contract.

Use at least the following fields:

```text
CHECK_ID:
TITLE:

HYPOTHESIS:
SCIENTIFIC_QUESTION:

FIXED_MODEL_AND_REGIME:
PRIMARY_OBSERVABLE:
SECONDARY_DIAGNOSTICS:
REQUIRED_COMPARISONS:

SUCCESS_EVIDENCE:
FALSIFICATION_EVIDENCE:
INCONCLUSIVE_CONDITIONS:

MANDATORY_VERIFIERS:
OUT_OF_SCOPE:

APPROVED_BY_PROJECT_OWNER:
APPROVAL_DATE_OR_COMMIT:
```

The contract fixes **WHAT** is being tested.

After approval, the agent controls **HOW**:

- numerical method;
- analytic method;
- parameter resolution;
- number of samples;
- solver tolerances;
- computational platform;
- convergence strategy;
- implementation details.

The agent may increase \(L\), increase ensemble size, tighten tolerances, or densify parameter sampling inside the approved scientific regime when needed for convergence, without seeking a new approval.

The agent may not silently change the question, observable, model comparison, or success/falsification criteria.

---

# 17. Research state, anti-divergence, and result lifecycle

Maintain a compact persistent research state/ledger that records active and completed hypothesis checks.

Recommended result statuses:

- `UNTESTED`
- `ACTIVE`
- `SUPPORTED`
- `FALSIFIED`
- `INCONCLUSIVE`
- `BLOCKED`
- `VERIFIED`

The exact file layout is repository-dependent.

Each branch must preserve:

- the approved contract;
- current evidence;
- verifier status;
- strongest supporting evidence;
- strongest counterevidence;
- known failure modes;
- next proposed scientific question.

The agent may recommend a next hypothesis check but may not launch it before project-owner approval.

A failed branch is not to be repeatedly resurrected with minor parameter changes unless a new scientific reason is documented and a new check is approved.

The agent is allowed to change its scientific beliefs. It is **not** allowed to change the success criteria without the approved process.

---

# 18. Modular verifier architecture

Implement narrow verifiers rather than one monolithic judge.

At minimum:

## 18.1 `model_verifier`

Checks:

- glued-tree construction;
- leaf gluing degree;
- layer indexing;
- Hamiltonian convention;
- disorder distribution;
- adjacency versus Laplacian implementation;
- intra-layer family construction;
- independence of layer graph samples;
- uniform \(k\) and \(J_{\rm LR}\) across layers;
- sparsity cap;
- \(J_{\rm LR}\) size-independence;
- bias convention;
- reproducibility metadata.

## 18.2 `numerics_verifier`

Checks:

- small-\(L\) exact reference comparisons where feasible;
- solver convergence;
- tolerance studies;
- infinite-time-average evaluation;
- degeneracy handling;
- cross-method agreement where available;
- honest reporting of unresolved numerical limitations.

## 18.3 `ensemble_verifier`

Checks:

- convergence in disorder realizations;
- convergence in intra-layer network realizations;
- uncertainty estimates;
- broad/rare-event behavior;
- final glued-tree-gluing ensemble averaging when required.

## 18.4 `scaling_verifier`

Fresh-context preferred.

Checks:

- exponential versus stretched-exponential versus power-law models;
- uncertainty;
- model comparison;
- fit-window robustness;
- stability under removal of small \(L\);
- stability when adding larger \(L\);
- whether available sizes genuinely support an asymptotic classification;
- whether claimed transition language is justified.

## 18.5 `mechanism_verifier`

Fresh-context preferred.

Checks:

- analytic projected theory;
- quantitative leakage/coherence diagnostics;
- consistency between analytic predictions and numerics;
- competing mechanism tests;
- whether the claimed mechanism is actually distinguished from generic connectivity effects;
- whether the role of bias is separated from the role of connectivity.

## 18.6 `accessibility_verifier`

Checks the mandatory finite-polynomial-time diagnostic and classifies the result as, for example:

- `POLYNOMIALLY_ACCESSIBLE`
- `NOT_POLYNOMIALLY_ACCESSIBLE`
- `INCONCLUSIVE`

The verifier passing means the diagnostic itself was correctly and rigorously completed, not necessarily that accessibility is positive.

## 18.7 `generality_verifier`

Checks:

- both adjacency and Laplacian CTQWs were investigated;
- classical sanity check completed;
- final robustness to random glued-tree gluing realizations;
- at least one successful non-glued-tree extension;
- whether the extension has algorithmic utility or, if not, how its significance is justified.

## 18.8 `paper_readiness_verifier`

Fresh-context required.

Consumes the outputs/evidence bundles of the other frozen verifiers.

It must not silently redo or reinterpret failed lower-level verifiers in order to produce a pass.

---

# 19. Wiki policy

The repository will maintain a Karpathy-style research wiki.

The wiki structure is intentionally **not specified yet**.

Promotion rule:

\[
\boxed{
\text{experiment}
\rightarrow
\text{research ledger}
\rightarrow
\text{relevant frozen verifiers}
\rightarrow
\text{VERIFIED}
\rightarrow
\text{wiki}.
}
\]

Only verified results are promoted into the wiki as established knowledge.

Candidate, exploratory, or inconclusive findings remain in the active research state/ledger.

Verified negative results may also be promoted to the wiki when they materially constrain future work.

Every wiki result must preserve provenance to the underlying evidence bundle and verifier versions.

---

# 20. Reproducibility and future APP publication

The project is intended to be published under Xiao-Liang Qi's Agentic Publication Protocol (APP) **only after the journal manuscript has been accepted**.

The research repository should nevertheless be developed in an APP-compatible spirit.

Every verified hypothesis check must leave an internally reproducible evidence record containing, as applicable:

- exact model definition;
- parameter values;
- graph-family settings;
- disorder and graph random seeds, or a deterministic seed-generation rule;
- code revision / commit identifier;
- environment information sufficient to reproduce the computation;
- raw or minimally processed outputs needed for the claim;
- analysis outputs;
- uncertainty/statistical outputs;
- convergence records;
- verifier reports and verifier versions;
- rerun instructions / commands;
- known limitations.

Final APP-specific packaging, publication-agent construction, and public release are **outside this research spec** and occur only after journal acceptance.

---

# 21. Strong protection hypothesis and decision logic

The preferred positive outcome is:

1. the unprotected disordered walk has
   \[
   \langle\overline P_{\rm exit}\rangle
   \sim e^{-L/\xi};
   \]

2. a sparse intra-layer family with fixed
   \[
   k=O(1)
   \]
   and fixed
   \[
   J_{\rm LR}/J_{\rm GT}=O(1)
   \]
   changes the asymptotic scaling to
   \[
   \langle\overline P_{\rm exit}\rangle
   \sim L^{-\alpha};
   \]

3. the effect does not require fine tuning of \(J_{\rm LR}\);

4. a physical mechanism is analytically and numerically established;

5. the role of optional layer biasing is clearly separated from the role of connectivity.

If instead protection only increases \(\xi\) but the asymptotic form remains exponential, record that outcome honestly.

If no tested sparse family changes the scaling class and the failure can be robustly established or explained, this is a valid negative scientific result.

---

# 22. `paper_ready` definition

The research agent may declare

```text
paper_ready = true
```

when **all frozen paper-readiness criteria apply and all required verifiers pass**.

A separate human approval gate is not required for the agent to make this declaration. The project owner retains ultimate authority to reject the declaration, reopen the research, change the spec, or demand further evidence.

For this project, `paper_ready = true` requires all of the following:

## 22.1 Core scaling result

At least one genuinely sparse intra-layer family exhibits verifier-supported recovery

\[
\boxed{
\left\langle\overline P_{\rm exit}\right\rangle
:
e^{-L/\xi}
\rightarrow
L^{-\alpha}
}
\]

in the asymptotic finite-size evidence available.

The sparse candidate must satisfy

\[
k=O(1),
\qquad
J_{\rm LR}/J_{\rm GT}=O(1),
\]

independent of \(L,N\).

The all-to-all control cannot satisfy this criterion.

## 22.2 No fine-tuned protection strength

The positive sparse scheme must work over a non-fine-tuned \(J_{\rm LR}\) regime in which stronger coupling improves or saturates protection at the scaling/ensemble level.

## 22.3 Rigorous numerics and statistics

`numerics_verifier`, `ensemble_verifier`, and `scaling_verifier` pass.

The evidence must survive:

- solver-convergence tests;
- ensemble-convergence tests;
- fit-window tests;
- addition of the largest accessible sizes;
- competing asymptotic models.

## 22.4 Analytic physical mechanism

`mechanism_verifier` passes.

The paper-ready evidence includes an analytic theory of the protected manifold, disorder-induced leakage, role of connectivity, role of bias, and the relevant \(W,J_{\rm LR},k\) / graph-property scales.

The mechanism must be supported rather than assumed.

## 22.5 Disorder-strength characterization

Either:

- strong evidence supports protection for the tested range consistent with the hypothesis that every finite \(W\) can be protected by sufficiently strong size-independent \(J_{\rm LR}\);

or, if this is false,

- the threshold/crossover structure is characterized, including whether the available evidence supports an asymptotic transition, a crossover, or only a localization-length enhancement.

Do not claim proof for “all finite \(W\)” from a finite numerical scan.

## 22.6 Mandatory finite-time accessibility diagnostic

`accessibility_verifier` passes in the sense that the finite-polynomial-time diagnostic has been completed rigorously.

A positive polynomial-accessibility outcome is scientifically stronger but is **not automatically required** for `paper_ready` unless the paper's final central claim explicitly invokes operational/algorithmic quantum advantage.

A negative or inconclusive accessibility result must constrain the manuscript claim accordingly.

## 22.7 Adjacency and Laplacian CTQWs

Both adjacency and Laplacian formulations have been investigated and their relation understood.

They are not required to produce identical outcomes, but a formulation may not be silently omitted because it is inconvenient.

## 22.8 Classical sanity check

The classical source-to-target comparison has been checked sufficiently to support any quantum-advantage language.

## 22.9 Final glued-tree ensemble robustness

The central result survives final averaging over independent glued-tree leaf-gluing realizations, not only a single fixed backbone.

## 22.10 Generalization

At least one genuinely distinct non-glued-tree graph/task shows a successful extension of the protection principle.

The extension should **preferably have algorithmic utility**. If the successful extension is not algorithmic, its broader significance must be strong enough to justify the high-impact claim.

## 22.11 Reproducibility and knowledge capture

All manuscript-critical results have:

- reproducible evidence bundles;
- passed the relevant frozen verifiers;
- been promoted to the research wiki with provenance;
- no unresolved contradiction between the wiki, ledger, and final evidence.

## 22.12 Fresh-context final assessment

The frozen fresh-context `paper_readiness_verifier` passes using the evidence bundles and outputs of the lower-level verifiers.

---

# 23. Claims that are forbidden without evidence

The agent must not use the following claims merely because they fit the preferred narrative:

- “phase synchronization” without a quantitative operational diagnostic;
- “spectral-gap protection” without evidence that gap/expansion actually controls the effect;
- “phase transition” from finite-size sharpness alone;
- “power law” from a visually straight log-log segment alone;
- “quantum advantage restored” if the finite-time or classical checks do not support the intended meaning;
- “works for arbitrary disorder” based on a finite range of \(W\);
- “sparse” for any candidate whose added maximum degree scales with \(L\) or \(N\);
- “robust” for a narrow tuned resonance in \(J_{\rm LR}\);
- “continuous-time quantum error correction” unless the formal criteria for QEC, rather than merely Hamiltonian error suppression/passive protection, are actually justified.

Until stronger criteria are established, the preferred language is:

> **passive Hamiltonian protection / passive protection of coherent quantum transport against static on-site disorder.**

---

# 24. Immediate execution rule

This spec does **not** authorize the agent to begin an arbitrary sequence of experiments autonomously.

The next step after adopting this spec is:

1. jointly select the first scientific hypothesis check;
2. write its experiment contract;
3. obtain explicit project-owner approval;
4. execute the approved check with agent freedom over implementation;
5. run the relevant frozen verifiers;
6. review the verified result with the project owner;
7. only then plan the next hypothesis check.

This human-in-the-loop cadence is an intentional anti-divergence mechanism and overrides any generic autonomous-research-loop behavior.

---

# 25. Compact invariant checklist

These invariants must remain true throughout the project unless the project owner explicitly changes this spec:

- [ ] static i.i.d. onsite disorder only: \(\epsilon_i\sim U[-W,W]\);
- [ ] two depth-\(L\) binary trees;
- [ ] every leaf has exactly two random cross-tree gluing edges;
- [ ] both adjacency and Laplacian CTQWs investigated;
- [ ] intra-layer graph independently sampled in each protected layer;
- [ ] same family, \(k\), and \(J_{\rm LR}\) across layers in a run;
- [ ] all layers except IN/OUT may receive intra-layer edges;
- [ ] all layers including IN/OUT may receive layer-uniform bias;
- [ ] sparse means bounded added degree per node independent of \(L,N\);
- [ ] \(J_{\rm LR}\) does not scale with \(L,N\);
- [ ] no narrow fine-tuned \(J_{\rm LR}\) protection accepted;
- [ ] primary observable is ensemble-averaged infinite-time exit probability;
- [ ] primary scaling variable is tree depth \(L\);
- [ ] finite-time accessibility always checked;
- [ ] physical mechanism must be derived/tested, not assumed;
- [ ] scaling classification is rigorous and asymptotic-minded;
- [ ] negative results are legitimate;
- [ ] project owner approves WHAT before execution;
- [ ] agent controls HOW after approval;
- [ ] verifier changes require explicit project-owner approval;
- [ ] only verified results enter the wiki;
- [ ] every verified check has a reproducible evidence bundle;
- [ ] at least one non-glued-tree generalization is required for `paper_ready`;
- [ ] research ends at `paper_ready`; manuscript writing is separate;
- [ ] APP packaging occurs only after journal acceptance.

