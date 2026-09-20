# Consequences of integrability breaking in quench dynamics of pairing Hamiltonians - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevB.99.054520
> Collected: 2026-09-20
> Published: 2019-02-28
> Zotero parent key: IHDCTTUA
> Evidence: Zotero indexed PDF text

This is the accepted manuscript made available via CHORUS. The article has been published as:
Consequences of integrability breaking in quench dynamics of pairing Hamiltonians
Jasen A. Scaramazza, Pietro Smacchia, and Emil A. Yuzbashyan
Phys. Rev. B 99, 054520 — Published 28 February 2019
DOI: 10.1103/PhysRevB.99.054520


 Consequences of integrability breaking in quench dynamics of pairing Hamiltonians
Jasen A. Scaramazza, Pietro Smacchia and Emil A. Yuzbashyan
Department of Physics and Astronomy, Rutgers University, Piscataway, New Jersey 08854, USA (Dated: February 14, 2019)
We study the collisionless dynamics of two classes of nonintegrable pairing models. One is a BCS model with separable energy-dependent interactions, the other – a 2D topological superconductor with spin-orbit coupling and a band-splitting external field. The long-time quantum quench dynamics at integrable points of these models are well understood. Namely, the squared magnitude of the time-dependent order parameter ∆(t) can either vanish (Phase I), reach a nonzero constant (Phase II), or periodically oscillate as an elliptic function (Phase III). We demonstrate that nonintegrable models too exhibit some or all of these nonequilibrium phases. Remarkably, elliptic periodic oscillations persist, even though both their amplitude and functional form change drastically with integrability breaking. Striking new phenomena accompany loss of integrability. First, an extremely long time scale emerges in the relaxation to Phase III, such that short-time numerical simulations risk erroneously classifying the asymptotic state. This time scale diverges near integrable points. Second, an entirely new Phase IV of quasiperiodic oscillations of |∆| emerges in the quantum quench phase diagrams of nonintegrable pairing models. As integrability techniques do not apply for the models we study, we develop the concept of asymptotic self-consistency and a linear stability analysis of the asymptotic phases. With the help of these new tools, we determine the phase boundaries, characterize the asymptotic state, and clarify the physical meaning of the quantum quench phase diagrams of BCS superconductors. We also propose an explanation of these diagrams in terms of bifurcation theory.
CONTENTS
I. Introduction 2
II. Models and pseudospin representation 4
III. Main results 5
IV. Ground state and quench protocol 6
V. Simulations of nonequilibrium phases and stability analysis 7 A. Phases I and II 8 B. Stability analysis 10 C. Phase III 11 1. Universality of elliptic oscillations 11 2. Relaxation time 12
VI. Phase III asymptotic solution 13 A. External driving 13 B. Phase III spin solution in the separable BCS model 16 C. Asymptotic self-consistency 18 D. Self-consistent solutions in the separable BCS model 18
VII. Quasiperiodic Phase IV 20
VIII. Conclusion 20
Acknowledgments 21
A. Mean-field equations of motion 21
B. Integrable limit of spin-orbit quenches 22
C. Integrability breaking forbids asymptotic reduction 24 1. Existence of reduced solutions implies integrability and vice versa 24 2. Asymptotic ∆(t) does not match the 2-spin solution in nonintegrable cases 25
D. The link between Lax constructions and the stability analysis 26 1. Lax norms 26 2. Phase I-II transition 27 3. Phase II-III transition 27 4. Real parts of Lax roots at the transitions 28 a. s-wave, II-III 28 b. p + ip, II-III 28
References 29


 2
I. INTRODUCTION
The past fifteen years have borne witness to impressive advances in the ability to experimentally control manybody systems where dissipative and decoherence effects are strongly suppressed. Studies of cold atomic gases1–10, solid state pump-probe experiments11–15 and quantum information processing16–23 can now explore coherent many-body dynamics for long time scales, paving the way for the characterization of new phenomena. In particular, cold atomic gases with tunable interactions24–29 are an instrumental experimental tool in the quest to understand previously inaccessible aspects of far from equilibrium many-body dynamics.
A major focus of recent theory and experiment has been the unitary time evolution of a system, initially in the ground state, subject to a sudden perturbation30–32. This experimental protocol, known as a quantum quench, can induce long-lived states with properties strikingly different from those of equilibrium states at similar energy scales. In this work, we focus on the quench dynamics of various superconducting models, which is a modern reformulation of the longstanding problem of nonequilibrium superconductivity in the collisionless regime33–36. A canonical result is that the infinitesimal perturbation of a Bardeen-Cooper-Schrieffer (BCS) s-wave superconductor leads to power law oscillatory relaxation of the order parameter amplitude |∆| to a constant value35.
Decades later, it was discovered that larger deviations could give rise to different dynamical phases identified by the asymptotic behavior of the amplitude of the order parameter37–44. Consider the dynamics of ∆ after quenches of the coupling g in various superconducting models. When the final coupling gf is small enough, ∆ vanishes rapidly in time; this behavior characterizes what we call Phase I. For intermediate gf , |∆| exhibits oscillatory power law decay to a nonzero constant (Phase II). For larger gf , |∆| exhibits persistent periodic oscillations (Phase III) – a nonlinear manifestation of what is known in the literature as the Higgs or amplitude mode45–52.
The exact quantum quench phase diagrams of the s-wave superconductor were eventually constructed using a sophisticated analytical method that relies on the model’s integrability53. It turns out that the integrable p+ip topological superconductor exhibits the same three phases, and similar analytical tools lead to the construction of its phase diagrams54. Thus, there may appear to be some profound connection between integrability and these three dynamical phases, but nonintegrable models also have Phases I and II40,45,55–57 and Phase III-like behavior is thought to persist in some nonintegrable models as well. On the other hand, the existence of Phase III in such models has not been convincingly established beyond the linear regime and aspects of quench dynamics unique to the nonintegrable case have not been explored.
Overall, the description of these nonequilibrium dynamical phases lacks a unifying mechanism applicable to finite quenches of nonintegrable pairing models. Here we present an in-depth study of the nonequilibrium phases of various nonintegrable superconducting models with and without spin-orbit coupling. A common feature of models we consider is that the order parameter takes the form of a single complex number. We establish that Phase III persists when integrability is broken58 and give strong numerical evidence that the persistent oscillations are always elliptic, which generalizes the known behavior of integrable models37,53,54.
Although the integrable and nonintegrable phenomenology are similar, we find that integrability breaking has profound consequences. Unique to nonintegrable models is an extremely long relaxation time scale τ which diverges as one approaches integrable points and is most prominent in quenches to Phase III. One must analyze dynamics beyond τ to truly observe Phase III, which has not been done in other studies. As illustrated in Fig. 1, for t < τ , |∆| may oscillate with several frequencies and a slowly evolving amplitude, both of which undermine naive analyses restricted to t < τ . One may incorrectly conclude from the transient dynamics that the asymptotic nonequilibrium phase has several undamped frequencies, or that |∆| is oscillating periodically while in fact the amplitude is still changing. Nonintegrable Phase III oscillations further require comparatively more elaborate elliptic functions to describe the oscillations.
To complicate the picture even further, certain quantum quenches of nonintegrable pairing models genuinely do not fit into any of the Phases I, II and III. Here the asymptotic |∆| is truly quasiperiodic, leading us to conclude that there are regions of quasiperiodicity – a new Phase IV – in the quantum quench phase diagrams of these models.
Another consequence of integrability breaking arises in the analytical description of the three nonequilibrium phases. In the integrable case, there is a dynamical reduction in the number of degrees of freedom of the system53,54 such that Phases I, II and III correspond to an effective classical spin Hamiltonian with 0, 1 and 2 spins, respectively. Phase III in the general case, however, does not admit such a 2-spin representation. As a surrogate to this analytical method, we propose a stability analysis of Phases I and II that applies generally to finite quenches. The stability analysis is based on linearizing around the asymptotic solutions to the equations of motion in each of the phases. We can then nonperturbatively determine the phase I-II boundary as well as the phase II-III boundary in nonintegrable pairing models. Finally, we return to Phase III and argue that the selfconsistency condition (gap equation) is responsible not only for the existence of persistent periodic oscillations of |∆|, but also for selecting elliptic functions amongst all possible periodic functions.


 3
(a) (b)
(c) (d)
(e) (f)
FIG. 1. Illustration of the large time scale τ that emerges in Phase III quenches gi → gf of nonintegrable pairing models. In all plots, the equilibrium gap corresponding to the initial coupling gi is ∆0i = 1.33 × 10−3W, while that for the final coupling gf is ∆0f = 0.4W, and we took N = 2 × 105 equally spaced single-particle energy levels on the interval [−W/2, W/2]. The lines in the plots on the right are the local minima and maxima of the oscillations. In terms of the single-particle level spacing δ, the evolution in the right column goes out to tmax = 0.94δ−1. In (a) and (b), we see that the persistent elliptic oscillations in the integrable s-wave case stabilize after a small number of oscillations. In (c) and (d), the amplitude of the oscillations takes roughly a thousand times longer to stop changing. In (e) and (f), integrability is strongly broken and it is not even clear whether the oscillations stabilize to a constant amplitude. The nonintegrable model used was the separable BCS model (2.9) with f (ε) from Eq. (5.1). The nearly integrable version uses γ = W, while the far from integrable one has γ = 1.33 × 10−2W.


 4
II. MODELS AND PSEUDOSPIN REPRESENTATION
In this paper, we consider quantum quenches in two types of nonintegrable pairing models
Hˆf =
∑
jλ
εj cˆ†
jλcˆjλ − 1
g
ˆ∆†∆ˆ , ˆ∆ ≡ g
∑
j
fj cˆj↓cˆj↑,
Hˆso =
∑
kab
[
(εkδab − hσz
ab) + α(kyσx
ab − kxσy
ab)
]
cˆ†
kacˆkb−
−1
g
ˆ∆†∆ˆ , ˆ∆ ≡ g
∑
k
cˆ−k↓cˆk↑.
(2.1)
The Hamiltonian Hˆf is a separable BCS Hamiltonian where the εj are N single-particle energy levels, cˆ†
jλ (cˆjλ) is a fermion creation (annihilation) operator for an electron with energy εj and spin index λ, g > 0 is the pairing interaction strength and fj ≡ f (εj) is a generic function of εj. The Hamiltonian Hˆso describes a 2D topological spin-orbit coupled superconductor with s-wave interactions59,60. Here k = (kx, ky) is a two-dimensional momentum vector, σj are Pauli matrices, h is a Zeeman field and α is the Rashba spin-orbit coupling. We will take the density of states to be constant for both models, which is the case in 2D or at weak coupling, so that the single-particle energy levels are distributed uniformly on an interval of length W , called the bandwidth. Apart from certain choices of f (x), the separable BCS Hamiltonian Hˆf is a toy model for breaking integrability. The choice of f 2(x) = C1 + C2x produces a quantum integrable Hamiltonian61,62; for example, f (x) = 1 and
f (x) = √x correspond to the s-wave39 and p + ip63,64 BCS models, respectively. A notable nonintegrable case is the d + id model65, where f (x) = x. The spin-orbit Hamiltonian Hˆso, on the other hand, can be realized with cold Fermi gases66–75. As both Hamiltonians in Eq. (2.1) have infinite range interactions, the mean-field approximation is expected to be exact in the thermodynamic (N → ∞) limit. We therefore replace 2-body operators as follows cˆ†cˆ†cˆcˆ ≈ 〈cˆ†cˆ†〉cˆcˆ + cˆ†cˆ†〈cˆcˆ〉 − 〈cˆ†cˆ†〉〈cˆcˆ〉 in the equations of motion. We also diagonalize the noninteracting part of Hˆso through a unitary transformation Uk which is detailed in Appendix A. Up to additive constants, the effective mean-field Hamiltonians of Eq. (2.1) are
Hˆf =
∑
jλ=↑↓
εj cˆ†
jλcˆjλ −
∑
j
fj
[
∆∗cˆj↓cˆj↑ + h.c.
]
,
Hˆso =
∑
kλ=±
εkλaˆ†
kλaˆkλ −
(∆
2
∑
kλ
e−iθk
[
λ sin φkaˆ†
kλaˆ†
−kλ+
+ cos φkˆa†
−kλ ˆa†
kλ ̄
]
+ h.c.
)
(2.2)
The new parameters in Hˆso are
cos φk = h
Rk
, sin φk = αk
Rk
,
Rk =
√
h2 + α2k2,
εkλ = εk − λRk, λ = ±, λ ̄ = −λ,
k = kx + i ky = kei θk .
(2.3)
Note that both α = 0 and h = 0 correspond to integrable points of the spin-orbit model; in both cases, Hˆso becomes a Hamiltonian for two bands of independent swave BCS models. Most importantly, the mean-field order parameters ∆ ≡ ∆(t) are defined in terms of expectation values
∆=g
∑
j
fj 〈cˆj↓cˆj↑〉,
∆= g
2
∑
kλ=±
ei θk
[
λ sin φk〈ˆa−kλaˆkλ〉 + cos φk〈aˆkλaˆ−kλ ̄〉
]
,
(2.4)
for their respective models. We will discuss the mean-field dynamics generated by Hamiltonians (2.2) in terms of Anderson pseudospins ˆsj = (sˆx
j , sˆy
j , sˆz
j ) which will allow for intuitive visualizations of the dynamics of different nonequilibrium phases. The transformation from fermions to pseudospins is given by
sˆ−
j = sˆx
j − i sˆy
j = cˆj↓cˆj↑, sˆz
j=1
2 (cˆ†
j↑cˆj↑ + cˆ†
j↓cˆj↓ − 1).
(2.5) In the spin-orbit case the pseudospin representation requires an additional set of auxiliary variables. For the sake of brevity, we relegate the derivations of the pseudospin equations of motion to Appendix A and simply state them here. In the mean-field equations of motion that follow, s = 〈ˆs〉 are to be understood as classical variables satisfying the angular momentum Poisson brackets {sa
j , sb
k} =
−δjk abcsc
j. In the separable BCS model, we have
s ̇j = bj × sj, bj = (−2fj∆x, −2fj∆y, 2εj), (2.6)
where self-consistency requires
∆=g
∑
j
fj s−
j = ∆x − i∆y. (2.7)
The spin-length sj = 1/2 is conserved by Eqs. (2.6), which together with Eq. (2.7) are the equations of motion of the following classical spin Hamiltonian:
Hf =
∑
j
2εj sz
j −g
∑
j,k
fj fks+
j s−
k
=
∑
j
2εj sz
j − |∆|2/g.
(2.8)


 5
Note that without loss of generality, we can choose fj to be real and nonnegative as we have done above. Indeed, let fj = |fj|e−iθj be general complex numbers and
Hf =
∑
j
2εj sz
j −g
∑
j,k
fj f ∗
k s+
j s−
k . (2.9)
We redefine the spins by making local rotations around the z-axis, s−
j → s−
j e−iθj . In terms of the new spins the Hamiltonian becomes
Hf =
∑
j
2εj sz
j −g
∑
j,k
|fj ||fk |s+
j s−
k , (2.10)
and the order parameter is ∆ = ∑
j |fj |s−
j . This transformation does not affect spin (angular momentum) Poisson brackets and therefore the equations of motion retain their form. We thus arrive at the same problem only with fj → |fj|.
We use capital letters Skλ to denote the classical pseudospins in the spin-orbit model and must introduce (see Appendix A) a set of auxiliary variables: the scalars Tk and vectors Lk±, where Lk+ and Lk− differ only in sign of the z-component. The equations of motion are
S ̇ kλ = Bkλ × Skλ + mk × Lkλ − mkTk,
L ̇ x
kλ = −2εkLy
kλ + my
k
2
[Sz
k+ + Sz
k−
] + Bx
kλTk,
L ̇ y
kλ = 2εkLx
kλ − mx
k
2
[Sz
k+ + Sz
k−
] + By
kλTk,
L ̇ z
kλ = −2RkλTk + mx
k
2
[Sy
kλ − Sy
kλ ̄
] − my
k
2
[Sx
kλ − Sx
kλ ̄
],
T ̇k = 2RkLz
k+ − Bx
k+Lx
k+ − By
k+Ly
k++
+1
2 mk · [Sk+ + Sk−
],
(2.11)
where the momentum dependent fields Bkλ and mk are defined in terms of the order parameter ∆
∆= g
2
∑
kλ
[ sin φkS−
kλ + cos φkL−
kλ
]
= ∆x − i∆y,
Bkλ = (−2 sin φk∆x, −2 sin φk∆y, 2εkλ),
mk = (−2 cos φk∆x, −2 cos φk∆y, 0).
(2.12)
The first of these equations is the self-consistency relationship for the spin-orbit model. The equation for  ̇Skλ in Eq. (2.11) corrects an error in a previous paper56, which is missing the last term. For each k, there is a conserved quantity analogous to pseudospin length
N2
k = 2T 2
k+
∑
λ
[S2
kλ + L2
kλ
]= 1
4 . (2.13)
Similar to Eq. (2.8), the classical spin-orbit Hamiltonian in pseudospin notation has a simple and compact expression
Hso =
∑
kλ
2εkλSz
kλ − 2|∆|2/g. (2.14)
Because of the simple relationship connecting Lk+ to Lk−, each momentum vector k corresponds to ten dynamical variables (Sk+, Sk−, Lk+, Tk) constrained by Eq. (2.13). Note that Tk and Lz
kλ do not appear in (2.14), but as discussed in Appendix A, they are necessary for the closure of the equations of motion. From now on we simplify notation to Lk ≡ Lk+ and define the 10-dimensional vector Γk ≡ (Sk+, Sk−, Lk, Tk). Finally, the conservation of the total number of fermions Nf in each model corresponds to the conservation of total z-component in the pseudospin language
Nf =
∑
j
(2sz
j + 1), (2.15)
for the separable BCS model and
Nf =
∑
kλ
(
Sz
kλ + 1
2
)
, (2.16)
for the spin-orbit model.
III. MAIN RESULTS
The main purpose of this work is to compare the nonequilibrium phases of quenches from the ground state of nonintegrable pairing Hamiltonians, such as those in Eq. (2.1), to those of the integrable s-wave53 and pwave54 models. Some qualitative aspects of the primary phases are independent of integrability insofar as the squared modulus of the order parameter ∆ may exhibit any of three distinct asymptotic behaviors in the continuum limit: it can relax to zero (Phase I), relax to a nonzero constant value (Phase II), or display persistent periodic elliptic oscillations (Phase III). We first show the existence of these three phases in Sects. V A-V C through direct numerical simulation of the dynamics. In Sect. V B we present a stability analysis of the phases of the separable BCS models which leads to conditions for nonequilibrium phase transitions. The stability analysis applied to integrable cases reduces to the known results that relied on exact solvability53,54. Our analysis provides a physical explanation for the transitions in terms of the frequencies of linearized perturbations δ∆(t) of the asymptotic ∆. The transition from Phase I to Phase II occurs through an exponential instability characterized by a pair of conjugate imaginary frequencies in the linearization spectrum, while that of Phase II to III occurs either when small harmonic oscillations fail to dephase or when an exponential instability occurs. The appearance of some or all of Phases I-III in nonintegrable models suggests an underlying universality to quench dynamics, but we show that the story is less straightforward. One the one hand, these phases are understood in the integrable cases53,54. There is a dynamical reduction of the number of effective degrees of freedom, so that at large times the dynamics are governed


 6
by a Hamiltonian of the same form, but which has just a few collective degrees of freedom. The three phases correspond to 0, 1 or 2 effective spins for each phase, respectively. On the other hand, the nonintegrable dynamics admit no known analogous reduction because the 2-spin solutions to the equations of motion do not reproduce the observed asymptotic behavior of ∆ in Phase III. If such a reducing “flow” in time of the Hamiltonian occurs in the nonintegrable case, then the form of the Hamiltonian itself must change. For specifics on this latter point, see Appendix C. Importantly, nonintegrable pairing models also display dynamics markedly different from those in the main three phases. We illustrate this behavior with two examples in Sect. VII – one for the spin-orbit Hamiltonian and one for a particle-hole symmetric separable BCS Hamiltonian – where the magnitude of the order parameter oscillates quasiperiodically. We interpret this observation as an indication of a new quasiperiodic phase (Phase IV) unique to quantum quench phase diagrams of these models. More subtle details of the dynamics in the main three phases change drastically once integrability is broken. We show in Sect. V C 2 that nonintegrable models take an extremely long time to relax to Phase III. This time scale is absent in the integrable case, yet it diverges when one approaches the integrable limit. One must take this time scale into account when studying Phase III on the basis of numerical simulation alone. For example, in the weak coupling regime, the nonintegrable d + id model may appear to quickly enter Phase III76 while in fact the minima of |∆| oscillations have not converged to a fixed value. The further into the weak coupling regime one explores, the longer the relaxation time. Quenches outside of weak coupling have faster dynamics, but exhibit behavior that markedly contrasts with Phase III, and above a certain energy threshold the asymptotic state collapses rapidly to Phase II. This long relaxation time is typical in the nonintegrable case. Despite these consequences of breaking integrability, our mixed strategy of simulation and stability analysis applies to the two rather different classes of nonintegrable pairing models found in Eq. (2.1). The separable BCS permits a standard Anderson pseudospin representation and is a single band model, while the spin-orbit model requires an expanded pseudospin representation, has multiple bands and a topological quantum phase transition. Yet both models have a single complex order parameter, which we believe is the essential characteristic that leads to the three phases. The self-consistency relationship (2.7) for the order parameter is central to both our stability analysis of Phases I and II in Sect. V B and our investigations of Phase III in Sect. VI. In the former case, the frequencies of harmonic perturbations of a given nonequilibrium phase are constrained by the self-consistency requirement. As for Phase III, we show in Sect. VI that there is always a periodic solution to the spin equations of motion when ∆(t) is periodic, and that the general
spin solution precesses around the periodic one. We then argue through numerical examples that further imposing the self-consistency requirement on ∆(t) selects elliptic functions amongst all possible periodic ∆(t).
IV. GROUND STATE AND QUENCH PROTOCOL
In a quantum quench, we prepare the system in the ground state with an initial order parameter ∆ = ∆0e−2iμt, which corresponds to system parameters such as the interaction strength g, the equilibrium chemical potential μ, the magnetic field h and the spin-orbit strength α. The amplitude ∆0 is constant in the ground state. At time t = 0, we suddenly change one of these parameters, which throws the system out of equilibrium. In the separable BCS model we will consider quenches gi → gf , but we will label the initial and final states by the coordinates ∆0i ≡ ∆0(gi) and ∆0f ≡ ∆0(gf ). In the spin-orbit model, we will consider quenches of the magnetic field hi → hf . The fermion number Nf is fixed across the quench in both cases, which implies that the equilibrium chemical potential μ changes with h. For a given ∆0 and μ, we express the ground state configuration of the separable BCS model in a frame that rotates around the z-axis with frequency 2μ. We then orient each sj against the magnetic bj, the z-component of which is shifted by 2μ,
s−
j0 = fj ∆0
2Ej
, sz
j0 = − εj − μ
2Ej
,
Ej(∆) ≡
√
(εj − μ)2 + f 2(εj)|∆|2.
(4.1)
The relationship between ∆0, g, Nf and μ obtains from the application of the definition of ∆ in (2.7) to (2.15) and the configuration in (4.1),
1
g=
∑
j
f2
j
2Ej
, Nf =
∑
j
(
1 − εj − μ
Ej
)
(4.2)
We will assert without loss of generality that ∆0i is real in both models, which can always be achieved by a time-independent rotation in the xy-plane in pseudospin space. Unless otherwise stated, we will simplify the analysis of the separable BCS model by restricting ourselves to cases where the order parameter ∆ remains real for all time, i.e., ∆y(t) = 0. To achieve this, we will consider the particle-hole symmetric case where the energies εj are symmetrically distributed around the chemical potential μ, which is set to zero without loss of generality. We will also only consider even functions f (x) = f (−x). Under these conditions, any initial spin configuration that satisfies the symmetry conditions sz(εj) = −sz(−εj), s+(εj) = s−(−εj), as does the ground state (4.1), will do so for all time. This fact can be verified with the


 7
equations of motion (2.6) by considering time derivatives of quantities such as sz(εj) + sz(−εj), which vanish under the aforementioned assumptions. We will not use particle-hole symmetry in the d + id model, where f (x) = x and εj will be distributed on a positive interval. Further, Eqs. (2.6) and (2.7) are invariant under the time-reversal transformation
sz
j (t) → sz
j (−t), s±
j (t) → s∓
j (−t),
∆(t) → ∆∗(−t). (4.3)
Since the initial conditions (4.1) at t = 0 also have this property, it holds at all times. The ground state of the spin-orbit model is less obvious56
Sx
kλ0 = ∆0 sin φk
Dk
[
∆2
0 + ξ2
kλ ̄ + Ek+Ek−
]
,
Sz
kλ0 = − 1
Dk
[
ξkλ(Ek+Ek− + ξ2
kλ ̄ + ∆2
0 sin2 φk)+
+ ∆2
0 cos2 φkξkλ ̄
]
,
Lx
k0 = ∆0 cos φk
Dk
[
∆2
0 + ξk+ξk− + Ek+Ek−
]
,
Lz
k0 = 1
Dk
[
2Rk ∆2
0 cos φk sin φk
]
,
ξk(λ) ≡ εk(λ) − μ,
Ekλ(∆) ≡
[
ξ2
k + ∆2 + R2
k − 2Rkλ
√
ξ2
k + cos2 φk∆2
]1/2
,
Dk ≡ 2Ek+Ek−(Ek+ + Ek−),
(4.4)
while Sy
kλ0 = Ly
k0 = Tk0 = 0. The corresponding selfconsistent equation relating ∆0 to g is
2
g=
∑
kλ
Ek+Ek− + ∆20 + sin2 φkξ2
kλ + cos2 φkξkλξkλ ̄
2Ek+Ek−(Ek+ + Ek−) .
(4.5)
The quantities 2Ej(∆) and 2Ekλ(∆) in (4.1) and (4.4) are the excitation energies obtained by diagonalization of the quadratic mean-field Hamiltonians in Eqs. (2.2) at a given ∆. For given values of g, Nf , α and h, one can simultaneously solve Eq. (2.16) and Eq. (4.5) using the ground state configurations to obtain the corresponding chemical potential μ and ground state gap ∆0. As the ground state is rotationally symmetric in k, and the equations of motion preserve this symmetry, in our numerics we always replace sums over momenta with sums over energies with a flat density of states ∑
k→∑
ε. The level spacing δ is related to the number of spins N and the bandwidth W through
δ= W
N − 1 . (4.6)
FIG. 2. Ground state order parameter ∆0, chemical potential μ and Egap = Ek=0,+ = (√∆2
0 + μ2 − h)2 as functions of the external field h in the spin-orbit model. One simultaneously solves the fermion number equation (2.16) and the selfconsistency relationship Eq. (4.5) with the ground state configuration (4.4). The vanishing of Egap corresponds to a topological quantum phase transition. The number of fermions is Nf = 0.65N , where N is the number of spins. We express energies in units of the bandwidth W , including the spin-orbit coupling α2 = 0.1W , the level spacing δ = W/(N − 1), and the BCS coupling g = 0.9δ. The Fermi energy in these units is εF = W
2N Nf = 0.325W . These spin-orbit model parameters remain the same for the remainder of this work, up to adjusting the value of N . We do not consider a similar plot for the separable BCS model because in the particle-hole symmetric case considered, the fermion number Nf = N and thus μ = 0.
Formally, in 2D this means N − 1 = W
2π A, where A is
the physical area of the system. Fig. 2 shows an example of the relationship between different parameters for the spin-orbit model.
V. SIMULATIONS OF NONEQUILIBRIUM PHASES AND STABILITY ANALYSIS
Now we numerically simulate the equations of motion (2.6) and (2.11) and plot the behavior of ∆(t) for each of the three phases in Sects. V A and V C. In Sect. V C, we also characterize the long time scale of nonintegrable models in Phase III. In Sect. V B, we introduce a stability analysis for the Phases I and II that gives the conditions under which a nonequilibrium phase transition occurs. We will consider several integrability-breaking functions for f (ε), which appears in the separable BCS equations of motion Eq. (2.6). All f (ε) considered here will be even functions, and as we discuss in Sect. V B, the particular form of f (ε) affects which phases occur. With this in mind, we consider the “Lorentzian” coupling45
flor(ε, γ) = γ
√γ2 + ε2 , (5.1)


 8
the “sine” coupling,
fsin(ε, γ) = 1 + sin2(ε/γ), (5.2)
and the “cube root” coupling,
fcub(ε, γ) = (γ3 + |ε|3)1/3
γ . (5.3)
The parameter γ is fixed for any particular Hamiltonian, and it characterizes how strongly integrability is broken. For γ & W , we have f (ε, γ) ∼ 1 in all three cases, which we consider to be “nearly integrable”. For γ W , integrability is strongly broken. We control for finite size effects in our simulations by increasing N until ∆(t) in the time window of interest no longer changes when N is doubled. In practice, we find that finite size effects become significant at times t > tfs, where
tfs ≈ 1
δ = N −1
W , (5.4)
is the inverse single-particle level spacing, see also Ref. 53. To observe the asymptotic dynamics, N has to be sufficiently large, so that the relaxation time τ < tfs.
A. Phases I and II
Figs. 3-5 contain examples of Phase I and Phase II quenches in both the separable BCS and spin-orbit models. To heuristically understand the emergence of these two phases, one can insert the prescribed behavior of ∆ into the equations of motion (2.6) and (2.11). This examination of the asymptotic solutions to the equations of motion in each phase will be important for the stability analyses of Sect. V B. The following applies to the separable BCS models in the particle-hole symmetric limit, but the analysis is analogous when this symmetry is broken and in the spinorbit case. In Phase I, we set ∆ to zero
s ̇z
j = 0,
s ̇x
j = −2εj sy
j,
s ̇y
j = 2εj sx
j.
(5.5)
The most general solution that conserves both s2
j = 1/4 and the time-reversal symmetry (4.3) is
sz
j = zj ,
sx
j = xj cos(2εjt),
sy
j = xj sin(2εjt),
z2
j = 1/4 − x2
j.
(5.6)
where zj is the Phase I steady state spin-profile. In order for (5.6) to make sense as a solution to the actual equations of motion, Eq. (2.7) must hold, i.e., we must
(a)
(b)
FIG. 3. Examples of Phase I quenches for separable BCS models. The equilibrium gaps ∆0i, ∆0f and integrability breaking parameter γ are given in units of the bandwidth W , and there are N = 5 × 104 (a) and N = 2 × 105 (b) spins. The initial rapid decay of ∆ is shown, but out of caution one must simulate to longer times (still smaller than the inverse level spacing) in order to verify that the phase is indeed stable.
have that ∆ = gf
∑
j fj s−
j equals zero, which is called the self-consistency condition. Strictly speaking, the solution (5.6) violates the self-consistency condition
∆ = gf
∑
j
fjxj cos(2εjt) 6= 0, (5.7)
but as the number of single-particle energies N goes to infinity, i.e., in the continuum limit when the sum in Eq. (5.7) turns into an integral, ∆ from Eq. (5.7) vanishes through dephasing for 1 t 1/δ = (N − 1)/W . This description is invalid for t ∼ N/W . In this sense, we refer to the solution (5.6) as asymptotically self-consistent, which is a concept we will often use in the remainder of this paper.
Let us now replace ∆ with ∆∞ 6= 0 in Eq. (2.6) to ex


 9
(a)
(b)
FIG. 4. Quenches in the spin-orbit model that lead to (a) Phase I and (b) Phase II. Here the number of single-particle energies is N = 104, and all other parameters are the same as given in the caption of Fig. 2.
amine the asymptotic solutions corresponding to Phase II
s ̇z
j = −2fj sy
j ∆∞,
s ̇x
j = −2εj sy
j,
s ̇y
j = 2εj sx
j + 2fj sz
j ∆∞.
(5.8)
The solution which preserves spin length and the timereversal symmetry is then
sz
j = Zj + ζj cos(bjt),
sx
j = − fj ∆∞
εj
Zj + εj
fj ∆∞
ζj cos(bjt),
sy
j = bj
2fj ∆∞
ζj sin(bjt),
(5.9)
where Zj is the Phase II steady state spin profile, which,
(a)
(b)
FIG. 5. Examples of Phase II quenches for separable BCS models. In (a) N = 2 × 105 spins, and the quench from ∆0i = 0.15W is close to the Phase I-II boundary. In (b), N = 5×104. The oscillatory power law decay to a constant value takes a rather long time, and we have verified out to tδ = 2 in (a) and tδ = 0.5 in (b) that the amplitude of the oscillations is indeed decreasing to zero with power-law decay. In both plots, ∆0 and γ are expressed in units of the bandwidth.
along with ∆∞, determines the other constants
bj = 2
√
ε2
j + f2
j ∆2∞,
ζ2
j = f2
j ∆2∞
b2
j
− f2
j ∆2∞
ε2
j
Z2
j.
(5.10)
The solution (5.9) must be asymptotically self-consistent, i.e., for N → ∞, limt→∞ ∆ = ∆∞, which implies
1 = −gf
∑
j
f2
j Zj
εj
, (5.11)
which is the nonequilibrium analogue of the ground state self-consistency requirement (4.2).


 10
B. Stability analysis
Now we consider the stability of Phases I and II for the separable BCS model by linearizing the equations of motion (5.5) and (5.8) about the asymptotic states given in (5.6) and (5.9), respectively. The main result is Eq. (5.20), which is the equation for frequencies of linearized perturbations to the asymptotic ∆(t) of either Phase I or Phase II. For Phase I, the appearance of a complex conjugate pair of imaginary frequencies signals an exponential instability. For Phase II, a solution ω0 to Eq. (5.20) may enter the band gap, or a complex conjugate pair of frequencies may appear. The former case, which occurs in the integrable s-wave and p + ip models, signifies a transition to Phase III because the linearized gap δ∆(t) oscillates persistently, i.e., it does not dephase. In Appendix D, we show that the nonequilibrium phase transitions predicted by this stability analysis both match and give a physical interpretation to the results obtained in integrable models53,54 using tools inextricably linked to exact solvability. Although the final result (5.20) applies generally, we limit the discussion to the particle-hole symmetric case to simplify the presentation. Let sj = sj0 + δsj, where sj0 is the Phase I asymptotic solution from Eq. (5.6). Neglecting second and higher order terms, the linearized equations for the spin components are
δs ̇z
j = −2fj sy
j0δ∆
δs ̇x
j = −2εj δsy
j,
δs ̇y
j = 2εj δsx
j + 2fjzjδ∆,
δ∆ ≡ gf
∑
j
fj δsx
j.
(5.12)
Expanding sj(t) in Fourier components
δsj(t) =
∑
ω
δ
s ̃j (ω)e−iωt,
δ∆ =
∑
ω
δ
 ̃∆(ω)e−iωt,
(5.13)
and using the Fourier space version of the self-consistency relation in Eq. (5.12), we find the following equation for the allowable frequencies ω
1 = 4gf
∑
j
f2
j εj zj
ω2 − 4ε2
j
. (5.14)
The following discussion uses particle-hole symmetry along with the empirical fact that for quenches from the ground state, zjεj < 0 in Phase I. Upon inspecting Eq. (5.14), one determines that there are N/2 unique ω2
j , of which all but one lie between consecutive 4ε2
j . The remaining ω02 is less than the smallest 4ε2
j , and can therefore be negative. A negative ω02 corresponds to a pair of conjugate imaginary frequencies, and therefore an exponential instability in δsj. We thus determine the Phase I
boundary in (∆0i, ∆0f ) space to be those values for which ω02 passes through zero. The stability analysis for Phase II follows a similar logic. Consider the linearized equations of motion
δs ̇z
j = −2fj sy
j0δ∆ − 2fj ∆∞δsy
j,
δs ̇x
j = −2εj δsy
j,
δs ̇y
j = 2εj δsx
j + 2fj sz
j0δ∆ + 2fj ∆∞δsz
j,
(5.15)
where now sj0 is the Phase II asymptotic solution from Eq. (5.9). Again changing to the Fourier basis, we solve for δs ̃x
j (ω) and apply the self-consistency condition for
δ
 ̃∆(ω), which reads
δ
∆ ̃ (ω)
(
1 − 4gf
∑
j
εj f 2
j Zj
ω2 − b2
j
)
=
= 2gf
ω
∑
j
εj f 2
j ζj
( δ  ̃∆(ω + bj) ω + bj
+ δ  ̃∆(ω − bj)
ω − bj
)
.
(5.16)
Although in principle Eq. (5.16) can be solved numerically with Zj and ∆∞ as input, such an approach is needlessly complex and obscures the mechanism by which Phase II gives way to Phase III. The difficulty presented by Eq. (5.16) stems from the fact that we required exact self-consistency. It turns out that relaxing this requirement to asymptotic self-consistency, defined in Sect. V A, suffices to understand the Phase II-III transition. We return to Eq. (5.15) and solve it in the time domain under the assumption δ∆(t) = δ+e−iω0t + δ−eiω0t. We neglect higher order harmonics because the Phase III oscillations near the II-III boundary are small. Under this ansatz, δsx
j (t) has six frequencies: ±ω0 and ±ω0 ± bj. If ω0 is a real frequency isolated from the continuum of bj defined in Eq. (5.10), then the constant ∆∞ of Phase II is “unstable” in the sense that oscillatory perturbations do not dephase. The self-consistent equation for this harmonic δ∆(t) is
1 = 4gf
∑
j
f2
j εj Zj
ω02 − b2
j
+
+ 2gf
ω0
∑
j
( eibj tf 2
j εj ζj
ω0 − bj
+ [bj → −bj]
)
.
(5.17)
This relation cannot hold for arbitrary t, but it will in the continuum limit if we require ω02 < b2
min and t → ∞, which allows the harmonic ansatz to be asymptotically self-consistent due to dephasing. Thus the equation for ω0, the frequency of a harmonic perturbation to ∆∞ in Phase II, is
1 = 4gf
∑
j
f2
j εj Zj
ω02 − b2
j
. (5.18)
Eq. (5.18) generalizes the small quench linearization method developed in Ref. 45, which we recover by replacing Zj of Eq. (5.18) with the z-component spin profile of the gi ground state. For the Lorentzian coupling,


 11
ω0 is in the band gap for infinitesimal quenches, so that linearized Phase III oscillations do not decay45. In order to understand whether the finite quench dynamics admit such an isolated ω0, consider the implications of (5.18) combined with (5.11) for the ∆∞ of Phase II. We find
ω02 4∆2∞
= I1(ω02)
I2(ω02) ,
I1(ω2
0) ≡ gf
∑
j
f4
j Zj
εj (ω02 − b2
j),
I2(ω2
0) ≡ gf
∑
j
f2
j Zj
εj (ω02 − b2
j).
(5.19)
It helps to analyze (5.19) under the simplifying assumption that Zj/εj < 0, which holds exactly for the integrable s-wave model, and is therefore applicable in the weak-coupling regime (∆0i, ∆0f W ) of the general separable case53. With this restriction, Eq. (5.18) implies ω02 is real, while Eq. (5.19) requires ω02 > 0, i.e., the allowed frequencies ω0 are purely real. We now examine the effect of the function fj in determining whether solutions ω02 to Eq. (5.19) are isolated from the b2
j continuum. If fj < f (0) for all j and b2
min = 4∆2∞, then Eq. (5.19)
has a solution 0 < ω02 < b2
min, and oscillations of δ∆(t) do not dephase. In this scenario, Phase III is the asymptotic state due the presence of persistent periodic oscillations about the Phase II solution. If fj < f (0) for all j and b2
min < 4∆2∞, then the relationship between ω02 and b2
min is
not immediately obvious from Eq. (5.19). The Lorentzian coupling, where fj = γ(γ2 + ε2
j )−1/2, allows for both possibilities: If ∆∞ ≤ γ, then b2
min = 4∆2∞ and Phase II
is not the asymptotic state. If ∆∞ > γ, then b2
min =
4γ(2∆∞ − γ), and we cannot characterize solutions to Eq. (5.19) without detailed knowledge of Zj and ∆∞. If fj ≥ f (0) for all j, then b2
min = 4∆2∞ and we find
that solutions ω02 to Eq. (5.19) are not isolated from the b2
j
continuum. In this case, the harmonic ansatz for δ∆(t) is not asymptotically self-consistent, and there are no persistent small oscillations about Phase II. The integrable s-wave model is defined by fj = f (0) = 1, in which case ω02 = 4∆2∞ is the only solution to Eq. (5.19), which is not isolated. On the other hand, Phase III exists in the s-wave case53. Therefore, fj ≥ f (0) does not imply that such models will always reach Phase II. Indeed, the relaxation to Phase II is always accompanied by nonperturbative oscillations which persist in the case of Phase III. Thus, even under the simplifying assumptions of particle-hole symmetry and Zj/εj < 0, the stability analysis of Phase II reveals a variety of possible behaviors in the separable BCS models. The nature of f (ε) near ε = 0 (the Fermi surface) is especially crucial to determining whether oscillations fully dephase to Phase II – a statement which extends to the non-particle-hole symmetric case in the weak coupling regime. Upon relaxing the restriction Zj/εj < 0, isolated solutions to Eq. (5.19) can have nonzero imaginary part,
thereby allowing for the possibility of exponential instabilities to Phase II solutions (see Fig. 10). In the non-particle-hole symmetric case, ∆(t) = ∆∞e−2iμ∞t in Phase II, and the equation for the frequencies of harmonic δ∆(t) can be expressed in the form
S2
2 (ω0) = (S1(ω0) − 1)2 + (S1(ω0) − 1)S3(ω0),
S1(ω0) ≡ 4gf
∑
j
ε ̃j f 2
j Zj
ω02 −  ̃b2
j
,
S2(ω0) ≡ 2gf ω0
∑
j
f2
j Zj
ω02 − b ̃2
j
,
S3(ω0) ≡ 4gf ∆2
∞
∑
j
f4
j Zj
ε ̃j (ω02 − b ̃2
j),
(5.20)
where
ε ̃j ≡ εj − μ∞,  ̃bj ≡ 2
√
ε ̃2
j + f2
j ∆2∞. (5.21)
The self-consistency equation for ∆(t) in Phase II has the same form as Eq. (5.11), with the substitution εj → ε ̃j. In the particle-hole symmetric limit, S2(ω0) = 0 and the correct solution to Eq. (5.20) solves Eq. (5.18). In the limit ∆∞ → 0, (5.20) is also the stability equation for Phase I. In Appendix D, we show that the Phase I-II and Phase II-III transitions given by (5.20) are identical to those obtained using exact solvability in the integrable s-wave and p + ip models.
C. Phase III
1. Universality of elliptic oscillations
The asymptotic Phase III solution is significantly more complicated than its Phase I and Phase II counterparts (5.6) and (5.9). We derive this solution in Sect. VI. Presently we provide evidence that the asymptotic behavior of ∆(t) can always be described by Jacobi elliptic functions. Consider first the particle-hole symmetric limit, for which we find
∆ ̇ 2(t) = P4[∆(t)], as t → ∞, (5.22)
where P4[∆(t)] is a generic fourth-order polynomial in ∆(t). Now parametrize P4[∆(t)] as
P4[∆(t)] = −a2(∆(t) − ∆+)(∆(t) − ∆−)×
×(∆(t) + ∆ ̃ +)(∆(t) + ∆ ̃ −), (5.23)
where the real coefficients ∆± are the maximum and minimum values of ∆(t), while  ̃∆± are either complex conjugate or independent real numbers. This parametrization


 12
FIG. 6. The quench in the Lorentzian separable BCS model (blue dots) from Fig. 1 (c) and (d) [γ = W ] and the corresponding elliptic function fit (solid red) from Eq. (5.24) with a ≈ 0.868205, ∆+ ≈ 0.941415, ∆− ≈ 0.501511,  ̃∆+ = ∆ ̃ ∗
−≈ 0.915740 + 0.002407i and t0 = 2.801929. To obtain these
parameters, we fit ∆ ̇ to Eq. (5.22) and then shift by the appropriate t0. If a fifth order polynomial is used instead of P4[∆(t)], the coefficient of the ∆5 term is −6.08 × 10−5, providing further evidence that this asymptotic ∆(t) is indeed an elliptic function. Although only a short time frame is shown, this fit works well for the entire time interval from t∆0f = 104, which is the time scale after which the oscillation amplitude stabilizes, to the times shown. In this fitting procedure, ∆ is given in units of ∆0f = 0.4W and time is measured in units of
∆−1
0f as pictured. In terms of the level spacing δ = 5×10−6W , the time domain pictured is 0.73125 < tδ < 0.731688.
leads to the following solution for ∆(t)
∆(t) =  ̃∆+(∆+ + ∆ ̃ −)dn2[ab(t − t0), m] − ∆ ̃ −(∆+ +  ̃∆+)
∆+ + ∆ ̃ + − (∆+ + ∆ ̃ −)dn2[ab(t − t0), m] ,
m ≡ (∆+ − ∆−)(  ̃∆+ − ∆ ̃ −)
(∆+ +  ̃∆−)(∆− + ∆ ̃ +) ,
b≡ 1
2
√
(∆+ + ∆ ̃ −)(∆− + ∆ ̃ +),
(5.24)
where dn[t, m] is the Jacobi-dn function. When particlehole symmetry does not hold, then one replaces ∆(t) with |∆(t)|2 in Eqs. (5.22)-(5.24). In Figs. 6 and 7 we show that Phase III oscillations in separable BCS models satisfy Eq. (5.22) and Eq. (5.24), while Fig. 8 shows the same for the spin-orbit model. As a general rule of thumb, most spin-orbit quenches that superficially appear to relax to Phase III really have not. Fig. 8 is the result of a thorough search of the parameter space in order to find a true Phase III quench within a computationally achievable time. On the one hand, the final field hf has to be large enough so as to nonperturbatively break integrability, for small perturbations lead to long relaxation times. On the other hand, the fields cannot be so large as to suppress the equilibrium gap ∆0 scale, which is the scale of the oscillation
FIG. 7. A Phase III quench in a f (ε) = exp[−|ε|/γ] separable BCS model (blue dots), where γ = 0.5W , N = 2 × 105, ∆0i = 0.04W , ∆0f = 0.8W . The corresponding elliptic function fit (solid red) from Eq. (5.24) has a ≈ 0.821896, ∆+ ≈ 1.075648, ∆− ≈ 0.566069, ∆ ̃ + = ∆ ̃ ∗
− ≈ 0.010686 + 1.327633i and t0 = 2.131916. To obtain these parameters, we fit ∆ ̇ to Eq. (5.22) and then shift by the appropriate t0. If a fifth order polynomial is used instead of P4[∆], the coefficient of the ∆5 term is 4.22 × 10−9. In this fitting procedure, ∆ is given in units of ∆0f and time is measured in units of ∆−1
0f
as pictured. In terms of the level spacing δ, the time domain pictured is 0.405 < tδ < 0.40525.
frequency. The value of α must also break integrability nonperturbatively, but a larger α also requires a larger number of spins to reach the thermodynamic limit. Finally, it turns out that a smaller Fermi energy relative to the bandwidth promotes a faster relaxation time. We discuss this Phase III relaxation time further in Sect. V C 2 in the context of the separable BCS models. For the integrable s-wave case it can be shown analytically53 that  ̃∆± = ∆± and a = 1, which greatly
simplifies P4[∆(t)] and ∆(t) → ∆+dn[∆+(t−t0), 1− ∆2
−
∆2
+
].
The mechanism behind the emergence of the three phases in the s-wave Hamiltonian is a dynamical reduction in the number of degrees of freedom. The Phase III asymptotic solution for ∆(t) is identical with that of a 2-spin s-wave Hamiltonian, while Phases II and I correspond to 1-spin and 0-spin solutions, respectively. In Phase III, this technique does not work for the separable BCS models. In Appendix C, we show that the 2-spin solution for these nonintegrable models is identical to that of the integrable case, up to a rescaling of time, while the general asymptotic solution that we observe is Eq. (5.24). Thus, if a reduction mechanism exists in the nonintegrable cases, the form of the m-spin Hamiltonian must also change.
2. Relaxation time
In Sect. V B we saw that there are examples of nonintegrable separable BCS models where the constant ∆∞ of Phase II is unstable to harmonic perturbations, and in


 13
FIG. 8. A Phase III quench in the spin-orbit model (blue dots), where in units of the bandwidth W : εF = 0.1, α2 = 0.9, gN = 2.315999, hi = 1.998980, hf = 0.801020. These parameters uniquely determine the initial and final equilibrium gaps and chemical potentials through the use of Eq. (2.16) and Eq. (4.5). The energies εj are uniformly distributed in the interval [0, W ], and the number of pseudospins is N = 8 × 104. As particle-hole symmetry does not hold, we fit Ω ≡ |∆|2 to the elliptic function definition in Eq. (5.24). The fit is a ≈ 0.776633, ∆+ ≈ 0.096608, ∆− ≈ 0.080316, ∆ ̃ + =  ̃∆∗
− ≈ 0.873604 + 0.883872i and t0 = 3.033272. The fit (solid red) is good for all t > τ , where τ is the relaxation time defined in Sect. V C 2. Here τ ∆0f ≈ 3050. In the fitting procedure, ∆ is given in units of ∆0f and time is measured in units of ∆−1
0f as pictured. In terms of the level spacing δ, the time domain pictured is 1.472 < tδ < 1.473, shortly after which finite size effects take over.
Sect. V C 1 we gave evidence that the Phase III oscillations of these models are elliptic functions. This behavior is typical of integrable models as well, although the form of the elliptic functions changes once integrability is broken. A more important difference, however, is that a long relaxation time scale τ emerges before the system truly reaches Phase III. Fig. 9 gives an example of the long relaxation time in the d + id model, which is the separable BCS model with f (ε) = ε. The initial dynamics at weak coupling seem to indicate76 that |∆(t)| oscillates with a single frequency reminiscent of Phase III. Upon closer inspection, however, the amplitude of the oscillations slowly changes with no indication of stabilizing. In Fig. 10, quenches at higher energies provide further evidence that the longtime asymptotic state is difficult to determine based on the short-time dynamics. Let us now explore the dependence of the relaxation time τ on ∆0i, ∆0f and γ in the Lorentzian separable BCS model defined in Eq. (5.1). We define τ as the minimum time after which the minimum of |∆(t)| oscillations stays within η = 10−4 of its asymptotic value. This definition of τ and the precise value of η are somewhat arbitrary, but empirically we find that the minima of |∆(t)| take longer to relax to the stationary value than the maxima. Typically, the minimum will increase for a time until it begins to oscillate with decreasing amplitude
about a final value. Most importantly, this definition of τ delineates clearly the difference between integrable and nonintegrable behavior. Fig. 11 shows the dependence of τ on the values of ∆0i and ∆0f , with one or the other fixed. Generally speaking, we find that quenches at lower energy scales increase τ . More interesting is the dependence of τ on γ, the integrability-breaking parameter, at fixed (∆0i, ∆0f ). First, let us examine quenches that lead to Phase III in both the Lorentzian and integrable s-wave models. Fig. 12 shows that τ has single minimum for γ ∼ 0.4W and increases away from this point both as γ → 0 and as γ → ∞. In all cases, the relaxation time of quenches in the integrable s-wave model, which is the γ → ∞ limit of our separable BCS Hamiltonians, is far smaller. We believe that the increase of τ as γ → ∞ is indicative of nonperturbative behavior of the dynamics in the vicinity of the integrable limit, see Sect. VIII. The behavior of f (ε) as γ → 0 is model dependent; in the case of the Lorentzian model, the stability analysis of Sect. V B indicates that Phase II is unstable to harmonic perturbations if γ > ∆∞; otherwise, Phase II could be stable. We observe in Fig. 12 large oscillations in the evolution of the minimum of ∆(t) at γ = 0.2W , behavior which occurs in the range 0.13W . γ . 0.26W For γ . 0.13W , the minima oscillations disappear and τ begins to dramatically increase. Despite this qualitative change in the evolution of |∆(t)|, down to at least γ = 0.11W we still find that the system eventually enters Phase III with a reduced amplitude of oscillation. Fig. 13 is similar to Fig. 12, except we now choose ∆0i and ∆0f such that the (integrable) s-wave model enters Phase II. The behavior of τ with respect to γ is qualitatively similar, except there is no regime where the minimum of ∆(t) undergoes large oscillations. The spin-orbit model also has a very long relaxation time to Phase III. In order to observe this asymptotic state, as is shown in Fig. 8, one must carefully choose model and quench parameters, otherwise τ is simply too large for our present numerical study.
VI. PHASE III ASYMPTOTIC SOLUTION
We now explore the structure of the Phase III asymptotic state. First, we treat ∆(t) as a periodic external driving and show that there is always a periodic solution for the classical pseudospins (and auxiliary functions in the spin-orbit model), and then we provide evidence that the class of periodic ∆(t) that are also self-consistent are elliptic functions.
A. External driving
In the separable BCS model, the mean-field dynamics can be described alternatively by a Gaussian wave func


 14
(a) (b)
FIG. 9. Example of a deceitful quench in the f (ε) = ε (d + id) separable BCS model, which at short times seems to enter Phase III on a similar time scale as the corresponding integrable s-wave quench with the same parameters. Part (b) shows that minimum of the d + id |∆(t)| is actually evolving over the entire time scale considered, and it is not clear what the asymptotic phase is. For both models, we used 4 × 104 single-particle energies εj uniformly distributed on the interval [0, W ], ∆0f = 0.00625W , ∆0i = 0.05∆0f , εF = 0.25W 77. In Fig. 10, we explore similar quenches in the d + id model at larger energy scales, where the dynamics are faster.
(a) (b)
FIG. 10. Study of the long time dynamics of d + id model quenches, continued from Fig. 9. We keep the same parameters and the same ratio ∆0i/∆0f = 0.05 while varying ∆0f . Pictured are the maxima and minima of oscillations of |∆|. Part (a) shows that below a certain critical ∆0f ∼ 0.0845W , the amplitude of |∆| oscillations evolves over an extremely long time scale. When ∆0f = 0.05W , there are also multiple incommensurate frequencies, and it is unclear whether the asymptotic state is Phase II, III, or something else entirely. When ∆0f = 0.075W , the decay in amplitude of |∆| resembles typical decays to Phase II seen in other models (see Fig. 5). At ∆0f = 0.1W , the system rapidly enters Phase II at a smaller ∆∞ than would be inferred from the other two cases, indicating that we have crossed a transition point. Part (b) shows a quench at this transition point, where the Phase II state seen for ∆0f = 0.1W exhibits an exponential instability and moves to an oscillatory state with unknown asymptotic behavior. The integrable s-wave BCS model, f (ε) = 1, is deep in Phase III for all these values of ∆0f and ∆0i.
tion with complex Bogoliubov amplitudes uj(t) and vj(t)
|ψ〉 =
∏
j
[u∗
j (t) + v∗
j (t)cˆ†
j↑cˆ†
j↓]|0〉, (6.1)
where normalization requires |vj|2 + |uj|2 = 1. The equations of motion for u(t) and v(t) follow from the timedependent Schr ̈odinger equation i ∂
∂t |ψ〉 = Hˆ |ψ〉 applied
to (6.1) with the mean-field Hamiltonian from (2.2),
id
dt
( uj(t) vj (t)
)
=
( εj fj ∆ fj ∆∗ −εj
) ( uj(t) vj (t)
)
, (6.2)
where we shifted the Hamiltonian by a constant Hˆ = Hˆf − ∑
j εj in order to make it traceless. The mapping


 15
(a) (b)
(c) (d)
FIG. 11. Nonintegrable pairing models exhibit an extremely long relaxation time τ when the asymptotic state is Phase III, which is most prominent in the evolution of the minima of the oscillations of ∆(t). Pictured is a study of τ as a function of ∆0f , at fixed ∆0i = 10−3W (a,b), and τ as a function of ∆0i at fixed ∆0f = 0.4W (c,d) in the Lorentzian model at γ = 0.8W in the particle-hole symmetric case. The time τ is not monotonic in either case, but it is generally a decreasing function of the initial and final coupling strengths gi and gf . In all plots, ∆0i and ∆0f are given in units of the bandwidth W. In (a,b) 2.4 × 104 > N > 1.2 × 104 and in (c,d) N = 8400.
to the classical pseudospins is
s−
j = uj v∗
j , sz
j = |vj |2 − |uj |2
2 . (6.3)
We shall discuss the nature of the asymptotic Phase III ∆(t) in terms of v(t) and u(t). To do so, consider first Eq. (6.2) with a periodic ∆(t) = ∆(t + T ) that is not necessarily self-consistent, which decouples each pair of (uj, vj) from all the others. The abstract form of Eq. (6.2) is
id
dt
(u
v
)
= h(t)
(u
v
)
(6.4)
with
h(t) =
( A B(t) B†(t) −A
)
, (6.5)
where u and v are m-dimensional vectors, A is a constant real symmetric m × m matrix, B(t) is a complex m × m
matrix periodic in t with period T , and we dropped the index j for simplicity. The forthcoming discussion is valid for all systems of this form, see also Ref. 53. For example, the spin-orbit dynamics admit such a representation with m = 4, while m = 1 in the separable BCS model. As h(t) is periodic by assumption, the Floquet theorem applies. There are thus 2m independent solutions ψi(t) to Eq. (6.4) of the form
ψi(t) = eδit
( Ui(t) Vi(t)
)
, i = 1 . . . 2m, (6.6)
where the Ui(t) and Vi(t) are periodic with the same period as h(t) and the δi are complex numbers known as Floquet exponents. The solutions ψi(t) therefore have the property
ψi(t + T ) = ρiψi(t), ρi ≡ eδiT , (6.7)
where the ρi are known as Floquet multipliers. Because h(t) is Hermitian, Eq. (6.4) conserves the norm of the


 16
(a) (b)
(c) (d)
FIG. 12. Study of the relaxation time τ , see Fig. 11, in the Lorentzian model as a function of the integrability breaking parameter γ at fixed ∆0i = .005W and ∆0f = 0.6W , where γ = ∞ is the integrable s-wave model. For these quench parameters, both the Lorentzian and s-wave models enter Phase III. Parts (a)-(c) show how the minimum of ∆(t) slowly evolves and reaches an asymptote, while part (d) gives τ near γ = 0.4W , where the minimum satisfies τmin∆0f ≈ 89. This minimum is still greater than the relaxation time of the s-wave case, where τ ∆0f ≈ 65. The relaxation time increases sharply away from γ = 0.4W , especially in the direction of decreasing gamma, where τ ∆0f ≈ 64500 at γ = 0.11W . In all plots, γ is given in units of the bandwidth W and N = 5500.
solutions ψi(t), which implies |ρi| = 1 and δi = iνi for νi real. Furthermore, the particular form of h(t) implies that if ψ = (u, v)T is a solution then so is ψ ̃ = (v∗, −u∗)T . This pairing of solutions implies that if δi is a Floquet exponent, then so is −δi. In Sect. VI B, we will use this latter fact to prove that there is always a periodic spin solution to Eq. (2.6) for a given periodic ∆(t).
Before continuing, we note that the Phase III asymptotic ∆(t) is only periodic in the particle-hole limit of the separable BCS model. In the general case, ∆(t) = F (t)e−2iμ∞t, where F (t) is periodic. Nonetheless, we can still reduce this problem, where h(t) is not periodic, to the periodic case by absorbing the phase 2μ∞t in the
following manner:
v′ = v e−iμ∞t,
u′ = u eiμ∞t,
A′ = A − μ∞1,
(6.8)
so that the time evolution of (u′, v′)T is described by Eq. (6.4) with periodic h(t) of the form given in Eq. (6.5) where A is replaced by A′. In terms of the pseudospin representation of the dynamics, this transformation amounts to an overall time-dependent rotation about the z-axis with frequency 2μ∞.
B. Phase III spin solution in the separable BCS model
Now we draw our attention to the behavior of the spin solutions to the separable BCS model for the periodic


 17
(a)
(b)
FIG. 13. Study of the relaxation time τ in the Lorentzian model as a function of the integrability breaking parameter γ at fixed ∆0i = 0.2W and ∆0f = 0.6W . For these quench parameters, the s-wave model enters Phase II, while the Lorentzian enters Phase III. Part (a) shows how the minimum of ∆(t) slowly evolves and reaches an asymptote, while part (b) gives τ near γ = 0.6W , where τmin∆0f ≈ 175. The relaxation time increases away from γ = 0.6W in both directions. In all plots, γ is given in units of the bandwidth W and N = 2800.
external ∆(t) considered in the previous section. The dimension of the matrix h(t) is now 2m = 2 and there are two independent solutions to the Floquet problem
ψ1j (t) = eiνjt
( Uj(t) Vj (t)
)
, ψ2j (t) = e−iνjt
( V∗
j (t)
−U ∗
j (t)
)
,
where Uj(t) and Vj(t) are periodic and we restored the index j. Using ψ1j(t) and Eq. (6.3), we can construct a periodic spin solution σj(t) [i.e., a periodic solution of Eq. (2.6) for the given external ∆(t) that does not necessarily satisfy Eq. (2.7)],
σ−
j (t) = Uj(t)V ∗
j (t),
σz
j (t) = |Vj(t)|2 − |Uj(t)|2
2.
(6.9)
We will now show that the most general spin solution sj(t) precesses about the periodic solution σj(t) with a variable angular velocity. First we write the general solution Ψj(t) as a linear combination of ψ1j(t) and ψ2j(t)
Ψj(t) = cos θj
2 ψ1j(t) + sin θj
2 ψ2j(t). (6.10)
Although the coefficients of linear combination are in principle complex, we can drop the constant overall phase of Ψj(t) as well as absorb 1
2 ×the remaining constant rel
ative phase into the definitions of Uj(t) and Vj(t). Once again using (6.3), we now write Ψj(t) in terms of spin variables. It is helpful to first parametrize Uj(t) and Vj(t) as
Uj(t) = |Uj(t)|e i
2 [αj (t)−2νj t−βj (t)],
Vj(t) = |Vj(t)|e i
2 [αj (t)−2νj t+βj (t)],
(6.11)
whence
s−
j = cos θj σ−
j + sin θj
σ−
j
|σ−
j|
(
σz
j cos αj − i
2 sin αj
)
,
sz
j = cos θj σz
j − sin θj |σ−
j | cos αj. (6.12)
Note that θj is the only time-independent quantity in Eq. (6.12). A geometric interpretation of the motion of the general solution sj(t) with respect to the periodic solution σj(t) becomes clear once we use Eq. (6.12) to express sj(t) in the body coordinate system of σj(t). Let ˆz′
j = σˆ j, while xˆ′
j lies along the line defined by the in
tersection of the plane spanned by {zˆ′
j, ˆzj} and that per
pendicular to ˆz′
j. Finally, yˆ′
j satisfies yˆ′
j · xˆ′
j = yˆ′
j · ˆz′
j =0
and ˆx′
j × yˆ′
j = ˆz′
j. These definitions lead to
ˆx′
j= 2
|σ−
j|
(
σz
j σx
j ˆxj + σz
j σy
j yˆj − |σ−
j |2ˆzj
)
,
yˆ′
j = − σy
j
|σ−
j | xˆj + σx
j
|σ−
j | yˆj .
(6.13)
The general spin solution sj(t) in this new coordinate system is then
sj(t) = cos θjσj(t) + sin θjσj⊥(t),
σj⊥(t) ≡ cos αj(t)
2 ˆx′
j + sin αj(t)
2 yˆ′
j,
(6.14)
where σj · σj⊥ = 0 and σj⊥ is not periodic. We see from Eq. (6.14) that sj(t) makes a constant angle θj with the periodic solution and rotates about it with a variable angular frequency α ̇ j(t). From Eq. (6.11) and the periodicity of Uj(t) and Vj(t), we conclude that αj(t) − 2νjt is also periodic with the same period as the external ∆(t) driving the system.


 18
C. Asymptotic self-consistency
Thus far, we have considered ∆(t) to be an external periodic driving that is not necessarily self-consistent. We showed for any such external driving, there is a corresponding periodic spin solution σj(t) with the same period as ∆(t). Furthermore, we derived in Eq. (6.14) that the general spin solution sj(t) precesses in a simple manner about σj(t). In the true quench dynamics, however, ∆(t) must be self-consistent, and we now show that this requirement implies that there always exists a set of constants θj, such that the following integral equation holds for the asymptotic periodic ∆(t):
∆(t) = gf
∑
j
fj σ−
j [∆(t)] cos θj, (6.15)
The notation σj = σj[∆] emphasizes that the periodic spin solution is some complicated nonlocal function of ∆(t). An analogous expression to Eq. (6.15) exists for the spin-orbit model. Eq. (6.15) is simply asymptotic self-consistency, as introduced in Sect. V, applied to the Floquet problem studied in Sects. VI A and VI B. To see this, suppose that we observe some Phase III asymptotic periodic ∆(t) after a quench from the ground state of the separable BCS model, as discussed in Sect. V C. This ∆(t) is selfconsistent by definition, i.e.,
∆(t) = gf
∑
j
fj s−
j (t), (6.16)
which we write in terms of the underlying periodic spin solution σj by using Eq. (6.12)
∆ = gf
∑
j
fj
(
σ−
j [∆] cos θj + σ−
j⊥[∆] sin θj
)
,
σj⊥ ≡ σ−
j
|σ−
j|
(
σz
j cos αj − i
2 sin αj
)
,
αj(t) = Aj(t) + 2νjt, Aj(t + T ) = Aj(t),
(6.17)
where νj is the imaginary part of the Floquet exponent as introduced in Eq. (6.6). As in our analysis of selfconsistency in Phases I and II, Eq. (6.17) cannot hold exactly, this time because the sum over σ−
j⊥[∆] is the only non-periodic term. Nonetheless, under the reasonable assumption that νj+1 − νj ∼ δ, where δ is the level
spacing, the sum over σ−
j⊥[∆] dephases in N → ∞ limit as t → ∞ (the N → ∞ limit comes first), leading to Eq. (6.15).
D. Self-consistent solutions in the separable BCS model
We have seen that an asymptotically self-consistent periodic ∆(t) satisfies the functional equation (6.15) in the
(a)
(b)
FIG. 14. (a) Examples of exactly self-consistent, periodic ∆(t)’s for the Lorentzian separable BCS equations of motion for different values of γ at fixed ∆0f = 0.5W , period T = 225/W , and N = 500. For these fixed parameters, below γmin ∼ 0.172W the only exactly self-consistent, periodic ∆(t) is a constant in time equal to the equilibrium value. (b) Convergence of γmin as a function N . In both plots, ∆0f and γ are given in units of W and T in units of W −1.
separable BCS model. We now will give evidence that solutions to Eq. (6.15) are elliptic functions. In order to generate such solutions, fix a period T and write ∆(t) as a Fourier series
∆(t) =
∞
∑
n=−∞
cne2πin t
T , (6.18)
which we truncate to some nmax, such that cn = 0 if |n| > nmax. In the particle-hole symmetric limit, ∆(t) is a real quantity that satisfies ∆(t) = ∆(−t) [see Eq. (4.3)], so that cn is real and equals c−n.
For a fixed set of coefficients cn, we determine σx
j [∆(t)] by solving the equations of motion (2.6) from t = 0 to t = T with ∆(t) given by (6.18). If the choice of cn produces a self-consistent ∆(t), then it will be equal to


 19
FIG. 15. Evidence that the self-consistent periodic ∆(t) from Fig. 14 are elliptic functions. Squared time derivatives ∆ ̇ (t) as a function of ∆(t) are given by solid blue lines. These lines overlap strongly with the dashed lines, which are the fits to the defining differential equation for elliptic functions Eq. (5.22). If a ∆5 coefficient is included in the fits, it is several orders of magnitude smaller than those for the 4th order fit shown here, providing strong evidence that ∆ ̇ 2(t) is indeed a 4th order polynomial in ∆(t). In this plot, γ is given in units of W and ∆ in units of ∆0f
the quantity ∆comp(t) defined as
∆comp(t) = gf
∑
j
fj σx
j [∆(t)] cos θj, (6.19)
for some set of θj. For most choices of cn, however, Eq. (6.19) will not hold. As both ∆(t) and ∆comp(t) are periodic functions of time with the same period, we define a distance r({cn}) as
r2({cn}) =
∫T
0
(
∆comp(t) − ∆(t)
)2
dt. (6.20)
A given ∆(t) is asymptotically self-consistent if and only if r({cn}) = 0. We now explore the results of this procedure for the Lorentzian coupling of the separable BCS model for various values of the integrability breaking parameter γ. It turns out that this procedure works when we fix cos θj = 1, i.e., we find exactly (and not just asymptotically) self-consistent solutions. In order to find such solutions, we start from the known values of the Fourier coefficients of the s-wave (γ = ∞) solution, which are close to the Fourier coefficients of the γ 1 solutions. We then progressively lower γ while finding Fourier coefficients that minimize r({cn}). Typically we obtain values of r ∼ 10−12 − 10−11 before declaring the solution self-consistent. Fig. 14 gives of examples of such solutions at fixed ∆0f and period T . Notably, there is a minimum γ =
γmin below which the amplitude of oscillation vanishes. As γ is increased from this minimum, the amplitude of oscillations increases to a maximum and then decreases to a nonzero limiting value as γ → ∞. Fig. 14 also shows the fast convergence of γmin as a function of N for two examples of this procedure. In Sect. V C, we argued through example quenches that the ∆(t) of Phase III are always elliptic functions, i.e., they satisfy Eq. (5.22). We show in Fig. 15 that the exactly self-consistent ∆(t) from Fig. 14 also satisfy Eq. (5.22) to a high degree of accuracy. The Floquet analysis of the equations of motion from Sect. VI A applies to any periodic ∆(t). From Fig. 15, we conclude that the self-consistency requirement (6.15) is essential to selecting elliptic functions amongst all possible periodic functions.
(a)
(b)
FIG. 16. Quenches of nonintegrable separable BCS and spinorbit models that do not conform to Phases I, II or III. This quasiperiodic dynamics of the order parameter emerge early and persist for the entire time of the simulation, see also Fig. 17. Plot (a) is the particle-hole symmetric separable BCS model with sine coupling from Eq. (5.2) and N = 4×105 spins. In units of the bandwidth, the integrability breaking parameter is γ = 0.075, while ∆0i = 0.05 and ∆0f = 0.5. Part (b) is the spin-orbit model with N = 2 × 105 spins. In units of the bandwidth: εF = 0.4, α2 = 0.4, gN = 2, hi = 2, and hf = 0.514256.


 20
(a)
(b)
FIG. 17. Darker blue points are local minima and maxima of the oscillations for the quenches from Fig. 16 for the entire time of the simulations. These plots suggest that there are regions of quasiperiodicity (Phase IV) in the quantum quench phase diagrams of nonintegrable pairing models. Part (a) is the same quench as in Fig. 16a, part (b) corresponds to Fig. 16b. In terms of the inverse level spacing, the time evolution goes out to tmax = 0.625δ−1 in plot (a) and to tmax = δ−1 in plot (b).
VII. QUASIPERIODIC PHASE IV
Quenches that do not conform to Phases I-III are another intriguing consequence of integrability breaking. We present two such examples in Figs. 16 and 17. Figs. 16a and 17a show a particle-hole symmetric quench of the separable BCS Hamiltonian with sine coupling from Eq. (5.2). Figs. 16b and 17b depict a quench of the Zeeman field in the spin-orbit model (2.14). The quasiperiodic behavior of ∆(t) in Fig. 16a sets in very early on, as corroborated by Fig. 17a, and persists with no appreciable changes at least until the times shown in the figure. Similarly, Fig. 16b is representative of the long-time spin-orbit |∆(t)|2 as evidenced by Fig. 17b. Based on our preliminary analysis of the Fourier spectrum of |∆(t)|2 for this quench and of the maximal Lyapunov exponent with the method of local divergence
rates78, we believe that it too is quasiperiodic. However, a more careful study is needed to unambigously distinguish between quasiperiodicity and chaos in this case. Such a study is beyond the scope of the present paper, where we mainly focus on the properties of Phases I-III. Note that the simulation times in Figs. 16 and 17 are enormous compared to the characteristic time of a single oscillation and even to typical Phase III relaxation times τ ∆0f ∼ 103 we observed in Sect. V C 2, cf. Fig. 12 and the caption to Fig. 8. Thus, both of these examples do not belong to Phases I, II, or III. We therefore conclude that there are regions of quasiperiodicity in the quantum quench phase diagrams of nonintegrable pairing models, which we call Phase IV.
VIII. CONCLUSION
The far-from-equilibrium steady states reached by nonintegrable pairing models after a quantum quench admit a similar taxonomy as do the integrable cases. We have shown that some or all of Phases I-III may occur in the separable BCS models and spin-orbit model defined in Eq. (2.1). The persistent periodic oscillations characterizing Phase III are always elliptic functions, regardless of whether the model is integrable. Moreover, we have developed a stability analysis of the three phases, summarized in Eq. (5.20), which generalizes known results in the integrable cases and elucidates the mechanism of nonequilibrium phase transitions using the language of linear analysis. Despite these striking similarities, important consequences accompany integrability breaking. As argued in Sect. V B, some nonintegrable models may not exhibit all three phases. At the same time, an entirely new quasiperiodic Phase IV emerges in certain models. Another key byproduct of integrability breaking is the emergence of a new, extremely long relaxation time scale τ when the asymptotic state either is or appears to be Phase III. For t < τ , ∆ can oscillate with more than one fundamental frequency and a slowly varying amplitude. This time scale is a generic feature of nonintegrable models, and its existence renders short-time analyses inadequate for determining the long-time dynamics. Moreover, τ diverges as we approach integrable points (e.g., as γ−1 → 0 in the separable pairing models of Sect. V), and it is often too large for the practical determination of the true asymptotic state. While the squared modulus of ∆(t) [and ∆(t) itself in the particle-hole symmetric case] is always an elliptic function in Phase III, its parametrization is more complicated in nonintegrable models. As a result, the reduction mechanism discussed in Appendix C, which explains how Phase III manifests itself in the integrable models, does not apply to nonintegrable models. Nonetheless, we demonstrated in Sect. VI that the common structure of the nonintegrable models implies the existence of a periodic solution to the classical pseudospin equations of


 21
motion if ∆(t) is taken to be a generic periodic external driving. Using numerical examples, we argued that further requiring ∆(t) to be self-consistent selects elliptic functions amongst all possible periodic functions. It is instructive to discuss the BCS quench dynamics in terms of bifurcation theory79–81. For example, consider the particle-hole symmetric separable BCS models with real ∆. For fixed initial conditions (4.1) and any function ∆(t) with fixed ∆(0), the equations of motion (2.6) have a unique solution sj[∆(t)] ≡ s[εj, ∆(t)]. Eq. (2.7) then provides a closed nonlinear integral equation for ∆(t) [cf. Eq. (6.15)],
∆(t) = gf
∫
dε sx[ε, ∆(t)]. (8.1)
Phase I is a fixed point, ∆ = 0, of this equation82, while Phase II corresponds to two fixed points ∆∞ and eiπ∆∞ = −∆∞. In Phase III we end up on one of two limit cycles related to each other by a rotation by π around the z-axis [change of sign of ∆(t)]. The Phase I to II and II to III transitions correspond to supercritical pitchfork and Hopf bifurcations, respectively, in this language83. The same results apply to the spin-orbit model (2.14). We also note that this quantum quench phase diagram is surprisingly similar to the nonequilibrium phase diagram of two atomic condensates coupled to a heavily damped cavity mode84,85. The meanfield dynamics of the latter system are described by the driven-dissipative variant of the Bloch equations (2.6) for two classical spins representing individual condensates. Moreover, there are islands of quasiperiodicity in the phase diagram of the two coupled condensates, where the dynamics are very similar to that shown in Figs. 16 and 17. Bifurcation theory also offers a plausible explanation for the divergence of the relaxation time τ near integrable points. Consider Phase III for an integrable pairing Hamiltonian, such as the particle-hole symmetric swave BCS model. Suppose the corresponding limit cycle loses stability as soon as integrability is broken and another limit cycle emerges as an attractor. An example of such behavior is the transcritical bifurcation79–81. Because the instability is weak for weak integrability breaking and because the evolution starts near the unstable limit cycle, the system takes a very long time τ to reach the attractor. The weaker the integrability breaking, the closer we are to the bifurcation and the longer the time τ . An interesting open problem is to explore the newly discovered quasiperiodic Phase IV. In particular, one needs to investigate the possibility that asymptotic oscillations of |∆(t)| for certain quenches may be chaotic, rather than quasiperiodic, i.e., the potential existence of a chaotic phase in addition to the quasiperiodic one. Let us also mention that quasiperiodic |∆(t)| also occurs in integrable models, but only when the initial (pre-quench) state is a highly excited state instead of the ground state86.
In this paper, we employed reduced BCS Hamiltonians (2.1) to model pairing dynamics. This description is valid only at times t Γ−1, where Γ is the highest among the rates of processes such Hamiltonians neglect. These processes include pair-breaking collisions35–37,53, threebody losses in ultracold gases87, thermal fluctuations88, etc. Thus, to reach the asymptotic state before these effects influence the dynamics, we need Γ−1 τ . In Phases II and III, this requirement is much more stringent than Γ−1 T∆ typically quoted in the literature on collisionless pairing dynamics. Here T∆ is the characteristic period of ∆(t) oscillations (T∆ is of the order of the inverse equilibrium gap ∆0f in our separable BCS models). Another limitation is the parametric instability of Phase III with respect to spontaneous eruptions of spatial inhomogeneities89–92. To avoid this instability, the system size has to be smaller than the superconducting coherence length, but not too small, so that the dephasing effect of quantum fluctuations on the mean-field Phase III oscillations88,93,94 is still negligible.
ACKNOWLEDGMENTS
We thank M. Dzero, A. J. Millis and A. Patra for helpful discussions. This work was supported by the National Science Foundation Grant DMR-1609829. J.A.S. was supported by a Rutgers University Louis Bevier Dissertation Completion Fellowship.
Appendix A: Mean-field equations of motion
The pseudospin equations of motion for the separable BCS model (2.6) obtain simply from the Heisenberg equations of motion d
dt Aˆ = i [Hˆ , Aˆ] applied to the mean
field Hˆf in Eq. (2.2) and the pseudospin operators sˆ defined in Eq. (2.5). The classical spin variables s are the expectation values of the pseudospin operators s = 〈sˆ〉, and the time-dependent order parameter ∆ is determined self-consistently according to Eq. (2.7). The generalized pseudospin representation of the spinorbit Hamiltonian Hˆso from Eq. (2.1) requires more work56. First, we diagonalize the kinetic part of Hˆso through the following unitary transformation to new fermionic operators aˆk±
Uk
( cˆk↑ cˆk↓
)
=
( aˆk+ ˆak−
)
Uk =
( cos φk
2 −i e−iθk sin φk
2
sin φk
2 i e−iθk cos φk
2
)
,
(A1)
where k = keiθk and φk is defined in terms of the model parameters in Eq. (2.3). One can check that the new elementary excitation energies are εk± ≡ εk ∓ Rk. Eq. (A1)


 22
implies
cˆ−k↓cˆk↑ = −i eiθk
2
(
sin φk(ˆa−k+aˆk+ − aˆ−k−aˆk−)+
+ cos φk(ˆak−aˆ−k+ + ˆak+ˆa−k−)+
+ aˆk+ˆa−k− + aˆ−k+aˆk−
)
.
(A2)
Upon summing over k, the last two terms in parentheses cancel with momenta of opposite sign. Therefore, the interaction term of (2.1) in this new basis becomes
g
∑
kk′
cˆ†
k↑cˆ†
−k↓cˆ−k′↓cˆk′↑ = 1
g
∆ˆ † ˆ∆,
∆ˆ ≡ g
2
∑
kλ
eiθk
(
λ sin φkaˆ−kλˆakλ + cos φkaˆkλaˆ−kλ ̄
)
,
(A3)
and upon taking the mean-field approximation cˆ†cˆ†cˆcˆ ≈ 〈cˆ†cˆ†〉cˆcˆ + cˆ†cˆ†〈cˆcˆ〉 − 〈cˆ†cˆ†〉〈cˆcˆ〉, the interaction term becomes
ˆ∆† ˆ∆ ≈ ∆∗ ˆ∆ + ∆ ˆ∆† − ∆∗∆,
∆ ≡ 〈 ˆ∆〉.
(A4)
Neglecting the constant term ∆∗∆/g, we arrive at the mean-field spin-orbit Hamiltonian Hˆso in the ˆa basis found in (2.2). Similar to the separable BCS model, we now search for a set of quadratic fermionic operators whose equations of motion are closed. Define the following operators
Sˆz
kλ = 1
2
(ˆa†
kλˆakλ + aˆ†
−kλˆa−kλ − 1),
Sˆ−
kλ = ληkˆa−kλaˆkλ,
Lˆz
kλ = − λ
4
(ˆa†
k+aˆk− + aˆ†
−k+aˆ−k−+
+ aˆ†
k−aˆk+ + ˆa†
−k−aˆ−k+
),
Lˆ−
kλ = ηk
2
(aˆk+ˆa−k− + ˆak−ˆa−k+
),
Tˆk = i
4
( − ˆa†
k+ˆak− − aˆ†
−k+ ˆa−k− +
+ ˆa†
k−aˆk+ + ˆa†
−k−aˆ−k+
),
(A5)
where ηk = ei θk = −η−k and, as usual, Sˆ− = Sˆx − i Sˆy and Lˆ− = Lˆx − i Lˆy. One can check that Sˆkλ, Lˆkλ and Tˆk are Hermitian operators. There is reflection symmetry in k-space: Aˆ−kλ = Aˆkλ for all operators Aˆkλ in (A5), as well as the following band symmetry for Lˆkλ: Lˆ−
k+ = Lˆ−
k− and Lˆz
k+ = −Lˆz
k−.
We apply the Heisenberg equations of motion to (A5) and Hˆso from (2.2) and then take expectation values to arrive at the generalized pseudospin equations of motion (2.11). The time-dependent order parameter ∆ =
〈∆ˆ 〉 as a function of the new variables can be found in Eq. (2.12). The factor ηk does not appear in Eq. (2.11), implying that the dynamics preserve any radial symmetry found in the initial state. As all initial states considered in this work are radially symmetric, one can opt to label the generalized pseudospin variables by their singleparticle energies rather than their momentum vector.
Appendix B: Integrable limit of spin-orbit quenches
The authors of Ref. 55 created a full nonequilibrium phase diagram of the spin-orbit model for quenches of the magnetic field hi → hf as a function of hi and hf . However, this phase diagram needs to be revised by running simulations to much longer times t > τ , which, in particular, may modify the Phase II-III boundary95. The phase diagram of Ref. 55 is also missing the quasiperiodic Phase IV discovered in the present work. In Ref. 56, an attempt was made to analyze interaction and external field quenches to the integrable limit hf = 0, but mistakes led to an incorrect phase diagram for the interaction quenches. Here we correct those mistakes and generate a correct phase diagram. When the external field h is set to zero, Hso from (2.14) becomes equivalent to the integrable s-wave model with a dispersion relation εkλ = k2
2 − λαk. This becomes
clear in the equations of motion (2.11) with cos φk = 0 and sin φk = 1, where the spin degrees of freedom Skλ decouple from the others and ∆ depends only on Skλ. In what follows, the initial state of the system will be the ground state for some hi ≥ 0 given by (4.4), and the Hamiltonian for t ≥ 0 is
H=
∑
kλ
2εkλSz
kλ − 2|∆|2/gf ,
∆ = gf
2
∑
kλ
S−
kλ, εkλ = k2
2 − λαk.
(B1)
We use the integrability of H to construct the exact phase diagram using a technique imported from Refs. 53 which we now summarize briefly. The analysis centers around a quantity L(u) called the Lax vector (not to be confused with the variables Lkλ)
L(u) = − 2
gf
zˆ +
∑
kλ
Skλ
u − εkλ
. (B2)
The integrability of H follows from the fact that L2(u) is conserved by the time evolution for arbitrary u, which implies conservation of the 2N roots of L2(u), which we call uj. As demonstrated in Ref. 53, each of the asymptotic nonequilibrium phases corresponds a unique number of isolated complex pairs of uj in the continuum limit. Phase I corresponds to zero isolated uj, Phase II corresponds to one pair, and Phase III corresponds to two pairs. As the uj are constants of the motion, we can


 23
evaluate L2(u) at t = 0 to determine the number of isolated pairs of uj and thus generate the phase diagram for a given hi. Let us first start with the case when hi = 0 and we quench the interaction gi → gf . In this case the ground state self-consistency relationship is
2
gi,f
=
∑
kλ
1
2Ekλ
, Ekλ =
√
(εkλ − μi,f )2 + ∆2
0i,f .
(B3)
Using Eq. (B3) along with the initial state given by Eq. (4.1), we find that the initial Lax vector has the form
L(u) =
(
∆0iLx(u), 0, (μi − u)Lx(u) − β ̃
)
,
Lx(u) =
∑
kλ
1
2(u − εkλ)Ekλ
,
β ̃ ≡ 2
gf
−2
gi
.
(B4)
If gf = gi, i.e., the zero quench, then β ̃ = 0 and the only complex pair of roots is u± = ±i ∆0i + μ. This is the degenerate Phase II case, where ∆(t) = ∆0i identically. When gf 6= gi, L2(u) = 0 implies
∑
kλ
1
(u − εkλ)√(εkλ − μi)2 + ∆2
0i
= − 2β ̃
u − μi ± i ∆0i
.
(B5)
We now construct the phase diagram shown in Fig. 18 for the hi = hf = 0, gi → gf quenches in the spin-orbit model. As we will not utilize particle-hole symmetry, the chemical potential μ must be calculated from the fermion number Eq. (2.16), which in the present case reads
Nf =
∑
kλ
(
− εkλ − μ
2
√(εkλ − μ)2 + ∆2
0i
+1
2
)
. (B6)
In the continuum limit, we have the following translation from sums over kλ to integrals over the continuum for arbitrary functions F (εkλ)
∑
kλ
F (εkλ) = N
W
∫ W−
−εb
F (x)να(x)dx,
να(x) =

  
  
2
√
1+x/εb
, −εb ≤ x ≤ 0
2, 0 ≤ x ≤ W+
1− 1
√
1+x/εb
, W+ ≤ x ≤ W−
,
εb ≡ α2/2, Wλ ≡ W − 2λ√εbW .
(B7)
Thus, the spin-orbit coupling α at h = 0 has the simple effect of introducing a peculiar density of states να(x) to the s-wave problem. Let B ̃ = limN→∞ β ̃/N and n = limN→∞ Nf /N , the latter of which is fixed for the entire phase diagram. For a given pair (∆0f , ∆0i), we first solve for (μf , μi) and then for B ̃ through the following integral
equations:
2n =
∫
X
(
1 − x − μi,f
√
(x − μi,f )2 + ∆2
0i,f
)
,
2
B ̃ =
∫
X
(1
√
(x − μf )2 + ∆2
0f
−1
√(x − μi)2 + ∆2
0i
)
,
∫
X
(·) ≡ 1
W
∫ W−
−εb
(·)ν(x)dx.
(B8)
We then use B ̃ and μi as input for the following integral equation:
∫
X
1
(u − x)√(x − μi)2 + ∆2
0i
= − 2B ̃
u − μi ± i ∆0i
, (B9)
which we solve for u. The number of complex pairs of roots to Eq. (B9) determines which nonequilibrium phase the system enters.
FIG. 18. Phase diagram for interaction quenches gi → gf in the integrable limit hf = hi = 0 of the spin-orbit model. Apart from the varying coupling constant g, the model parameters are the same as found in Fig. 2. The black dotted lines ∆0i = e±π/2∆0f indicate the weak coupling limit (∆ W ) phase boundaries53. The thick blue lines mark the true phase boundaries, which are characterized by the appearance of a new pair of complex roots of Eq. (B9) when passing from Phase I to Phase II or Phase II to Phase III.
Quenches from hi 6= 0 to hf = 0 still undergo integrable dynamics, except now the initial state is no longer the s-wave ground state. We consider the behavior of the zeros of L2(u) with respect to hi in the continuum limit with the spin-orbit parameters given in Fig. 2. The Lax vector is still as defined in Eq. (B2), but we now enter the spin-orbit ground state (4.4) into the equation L2(uj) = 0, which implies Lx(uj) = ±i Lz(uj). The spin components of the hi 6= 0 ground state are functions of the form Fλ(εk) instead of F (εkλ); we therefore do not use (B7) for the continuum limit, but rather
∑
kλ
Fλ(εk) = N
W
∫W
0
(
F+(x) + F−(x)
)
dx. (B10)


 24
FIG. 19. Behavior of the roots of L2(u) for quenches from the ground state of hi 6= 0 to hf = 0 in the continuum limit with spin-orbit parameters as given in Fig. 2. Each solid line is the absolute value of the imaginary part of a pair of complex conjugate roots. Regions of hi with one such line indicate that the asymptotic state is Phase II, while the region where there are two separate lines indicate Phase III. The vertical dashed lines indicate various critical values of hi where the system undergoes a phase transition or crossover. From left to right, h1 = 0.7813εF is the topological transition of the ground state, h2 = 0.9938εF is a Phase II-III transition, h3 = 1.6625εF is the BCS-BEC crossover, and h4 = 2.2938εF is a Phase III-II transition which also appears to correspond to ∆0i = 0 being the only self-consistent initial equilibrium gap. These critical values of hi depend in general on the various spin-orbit model parameters.
The result of the root calculation is given in Fig. 19, where we plot the absolute value of the imaginary part of each root pair. For small hi, there is only one pair of complex roots, i.e., the asymptotic phase is Phase II. At a certain critical hi, a second pair of complex roots appears, and the system enters Phase III. For larger hi, the two pairs of roots merge into one and the system reenters Phase II. Phase I does not occur in hf = 0 quenches for the parameters we used.
Appendix C: Integrability breaking forbids asymptotic reduction
An important property of the quench dynamics of integrable s and (p + ip)-wave Hamiltonians is the dynamical reduction in the number of degrees of freedom at t → +∞ in the thermodynamic limit53,54. In particular, Phase III in these models corresponds to the motion of two collective classical spins S1 and S2 governed by a Hamiltonian of the same form. The asymptotic order parameter ∆(t) in Phase III coincides with that of the 2-spin problem. Further, there are special reduced solutions of equations of motion with the same ∆(t) that are of the form
sj = αjS1 + βjS2 + ηj ˆz, (C1)
where αj, βj and ηj are time-independent and zˆ is a unit vector along the z-axis. These observations lead to an
analytical expression for ∆(t) and, moreover, help to construct the full asymptotic spin configuration in Phase III. We note also that, as we will see below, for the s-wave BCS model in the particle-hole symmetric case, (C1) is equivalent to the ansatz of Ref. 37. We will now show that the above reduction mechanism relies on integrability and breaks down for nonintegrable separable BCS models. We will prove two independent statements: (i) reduced solutions exist only when f 2(x) = C1 + C2x, i.e. only when the Hamiltonian is integrable61,62 and (ii) ∆(t) for a 2-spin separable BCS Hamiltonian with an arbitrary choice of new ε1,2, f1,2 and g does not match the asymptotic ∆(t) we obtained in Sect. V C.
1. Existence of reduced solutions implies integrability and vice versa
We will follow the same steps as in the derivation of the 2-spin solutions in Ref. 53 and show that it only works for special choices of f (x). First, we treat the general non-particle-hole symmetric case. Let
∆ = Ωe−iΦ. (C2)
The 2-spin (reduced) Hamiltonian is
Hred =
2
∑
j=1
2
ε ̃j Sz
j − g ̃
∑
j,k
f ̃j f ̃kS−
j S+
k=
=
2
∑
j=1
2
ε ̃j Sz
j − |∆|2
g ̃ ,
(C3)
where ∆ = g ̃(f ̃1S−
1 + f ̃2S−
2 ). We take both f ̃k to be nonzero, because otherwise the two spins simply decouple and rotate uniformly around the z-axis. Energy and S1z + S2z are conserved. Since there are two conservation laws and two degrees of freedom, Hred is integrable. For more than two spins, integrability persists only for special choices of f ̃k. This fact alone already distinguishes the 2-spin problem from that of a generic N -spin separable BCS Hamiltonian. Conservation of energy and S1z + S2z read
2
ε ̃1Sz
1 + 2ε ̃2Sz
2 = E ̃ + Ω2
g ̃ , Sz
1 + Sz
2 = const,
(C4)
We need ε ̃1 6= ε ̃2 or |∆| will be constant. We use Eq. (C4) to express Sz
k in terms of Ω2,
Sz
k =  ̃akΩ2 +  ̃bk, k = 1, 2; (C5)
where  ̃ak and  ̃bk are time-independent and a ̃1 = −a ̃2 6= 0. Furthermore, Eq. (C1) implies a similar expression for sz
j
in terms of the order parameter amplitude,
sz
j = ajΩ2 + bj. (C6)


 25
Conservation of the energy
E=
∑
j
2εj sz
j − |∆|2
g , (C7)
and of Jz = ∑
j sz
j require
∑
j
aj = 0,
∑
j
2εjaj = 1
g . (C8)
We write the Bloch equations for the separable BCS Hamiltonian as
s ̇z
j = −ifj (s−
j ∆∗ − s+
j ∆), (C9)
s ̇−
j = −2ifj sz
j ∆ − 2iεj s−
j . (C10)
Since the equations of motion and Eqs. (C5) and (C6) for the reduced solution and the 2-spin problem have the same form, we can treat both of them simultaneously. Substituting Eq. (C6) into Eq. (C9), we find
s−
j eiΦ − s+
j e−iΦ = 2i aj
fj
Ω ̇ . (C11)
Next, we multiply Eq. (C10) by eiΦ and add the resulting equation to its complex conjugate,
d dt
(s−
j eiΦ + s+
j e−iΦ) = 4aj εj
fj
Ω ̇ − 2 aj
fj
Φ ̇ Ω ̇ , (C12)
where we made use of Eq. (C11). Integrating and adding the resulting equation and Eq. (C11), we obtain
s−
j eiΦ = 2aj εj
fj
Ω − aj
fj
A + i aj
fj
Ω ̇ + ajcj
fj
, (C13)
where ajcj
fj is the integration constant and A = ∫ dtΦ ̇ Ω ̇ .
The self-consistency condition ∆ = g ∑
j fj s−
j , combined with Eq. (C8), implies ∑
j aj cj = 0.
The analogous expressions for the 2-spin problem are
S−
k eiΦ = 2a ̃kε ̃k
f ̃k
Ω −  ̃ak
f ̃k
A + i a ̃k
f ̃k
Ω ̇ + a ̃kc ̃k
f ̃k
, (C14)
and a ̃1c ̃1 + a ̃2c ̃2 = a ̃1(c ̃1 − c ̃2) = 0. Therefore, c ̃1 = c ̃2 and the last term in Eq. (C14) can be absorbed into A, which is defined up to a constant anyway, i.e.,
S−
k eiΦ = 2a ̃kε ̃k
f ̃k
Ω − a ̃k
f ̃k
A + i a ̃k
f ̃k
Ω ̇ . (C15)
Since s−
j is related to S−
1 and S−
2 via Eq. (C1), this also eliminates the last term in Eq. (C13), i.e.,
s−
j eiΦ = 2aj εj
fj
Ω − aj
fj
A + i aj
fj
Ω ̇ . (C16)
Combining the conservation of the spin norm, s2
j= (sz
j )2 + |s−
j |2, with Eqs. (C6) and (C16), we derive the following differential equation for Ω:
(aj Ω2 + bj )2 + (2aj εj Ω − aj A)2 + a2
j Ω ̇ 2
f2
j
= s2
j , (C17)
or, equivalently,
Ω ̇ 2 + f 2
j Ω4 + Ω2
(
2 fj bj
aj
+ 4ε2
j
)
− 4εjAΩ
+A2 + f 2
j (b2
j − s2
j)
a2
j
= 0.
(C18)
This equation implies, among other things, that A is a function of Ω. Indeed, consider a set of numbers xj, such that ∑
j xj = 0. Multiplying Eq. (C18) by xj and summing over j, we find
AΩ = λΩ4 + 2μΩ2 + κ, (C19)
where λ, μ and κ are real constants. Substituting this back into Eq. (C18), we obtain
w ̇ 2
4 + λ2w4 + (f 2
j − 4λξj)w3 +
( 2fj bj
aj
+ 2λκ + 4ξ2
j
)
w2+
(f2
j (b2
j − s2
j)
a2
j
− 4κξj
)
w + κ2 = 0,
(C20)
where w = Ω2 and ξj = εj − μ. These equations are consistent only when the coefficients of powers of w are j-independent. In particular, we must have f 2
j = 4λξj + const., i.e.,
f2
j = C1 + C2εj, (C21)
where C1 and C2 are real constants. This is the most general form of fj for which the separable BCS Hamiltonian (2.8) is known to be integrable61,62. In particular, C2=0 corresponds to the s-wave and C1 = 0 to the (p + ip)-wave models. Conversely, when Eq. (C21) holds and the separable Hamiltonian is therefore integrable, the j-independence of coefficients at w2 and w determines aj and bj, and Eq. (C20) means that w = |∆|2 is a certain elliptic function of time.
2. Asymptotic ∆(t) does not match the 2-spin solution in nonintegrable cases
In Sect. V C we numerically determined ∆(t) in two nonintegrable separable BCS Hamiltonians, see Eq. (5.24). Here we show that ∆(t) for the most general separable 2-spin Hamiltonian (C3) cannot match Eq. (5.24). Since ∆(t) in Eq. (5.24) is real, we take ∆ in the 2-spin problem to be real as well, though we do not a priori assume particle-hole symmetry in the 2-spin problem. All we need is to specialize the derivation of the previous subsection to the case of real ∆. Then, the Bloch equations become
S ̇ z
j = −2f ̃j Sy
j ∆,
S ̇ x
j = −2ε ̃j Sy
j,
S ̇ y
j = 2ε ̃j Sx
j + 2f ̃j Sz
j ∆.
(C22)


 26
Substituting Eq. (C5) into the first two equations of motion, we obtain
Sy
k = −  ̃ak
f ̃k
∆ ̇ , (C23)
and
Sx
k = 2ε ̃ka ̃k
f ̃k
∆ +  ̃akc ̃k
f ̃k
, (C24)
where  ̃akc ̃k
f ̃k
is the integration constant. As before, the
self-consistency condition g ̃(f ̃1S−
1 + f ̃2S−
2 ) = ∆ together with  ̃a1 = −a ̃2 imply c ̃1 = c ̃2 ≡ c ̃, and the conservation of spin length (Sx
k )2 + (Sy
k )2 + (Sz
k )2 = S2
k yields
 ̇∆2 + (2ε ̃k∆ + c ̃)2 +
(
f ̃k∆2 +
 ̃bk f ̃k
a ̃k
)2
= S2
k
f ̃2
k
a ̃2
k
. (C25)
Equating the coefficients at different powers of ∆ for k = 1 and 2, we find c ̃(ε ̃1 − ε ̃2) = 0 ⇒ c ̃ = 0,
f ̃1 = f ̃2 ≡ f ̃, (C26)
and two more relationships that constrain  ̃ak and  ̃bk. The constraint (C26) is a consequence of the requirement that ∆ be real. Now Eq. (C25) is of the form
 ̇∆2 = −f ̃2(∆2 − ∆2
+)(∆2 − ∆2
−). (C27)
This is the same as the equation for the asymptotic ∆(t) for the integrable s-wave BCS Hamiltonian in the particle-hole symmetric case up to rescaling ∆new = f ̃∆. This is not surprising because f ̃1 = f ̃2 = f ̃ and the factor of f ̃2 in Eq. (C3) can be absorbed into the coupling constant, g ̃new = f ̃2
g ̃ resulting in an integrable s-wave BCS Hamiltonian for two spins with ∆new =
g ̃new (S −
1 + S−
2 ) = f ̃∆. The solution of Eq. (C27) is
∆(t) = ∆+dn[f ̃∆+(t − t0), 1 − ∆2
+
∆2
−
]. As we saw in
Sect. V C, in the nonintegrable case we find instead a more general differential equation Eq. (5.22) with the solution given by Eq. (5.24).
Appendix D: The link between Lax constructions and the stability analysis
As mentioned above, the separable BCS model is integrable when f 2
j = C1εj + C2. Two important cases are the s-wave model where fj = 1 and the p + ip model
where fj = √εj. In past work53,54, integrability has been exploited to determine the nonequilibrium asymptotic phases through the use of Lax constructions. These techniques are useful for constructing phase diagrams, but the physical interpretation of the phase transitions is obscured by the use of exact solvability. We demonstrate here that the stability equation Eq. (5.20), which applies
to the nonintegrable cases as well, both predicts the same transition points and clarifies the physical meaning of the Lax construction.
In the following, we will assume the quantities Zj, ∆∞ and μ∞ are given. They are functions of the quench parameters ∆0i, ∆0f , the particle number Nf , and the Fermi energy εF .
1. Lax norms
In the s-wave model, the Lax vector is53
Ls(u) = − zˆ
gf
+
∑
j
sj u − εj
, (D1)
while in the p + ip model its components are54
L+
p (u) =
∑
j
√εj s+
j
u − εj
,
L−
p (u) =
∑
j
√εj s−
j
u − εj
,
Lz
p(u) =
∑
j
εj s−
j
u − εj
−1
gf
,
(D2)
where u is a complex (spectral) parameter.
We focus on the norms of these quantities, defined as L2(u) = L2x(u) + L2y(u) + L2y(u) in the s-wave case and L2(u) = uL+(u)L−(u) + [Lz(u)]2 for p + ip. Integrability follows from the fact that the L2(u) and L2(u) are conserved by the time evolution for arbitrary u, which implies conservation of their roots uj. As demonstrated in Refs. 53 and 54 and discussed in Appendix B, each of the asymptotic nonequilibrium phases corresponds a unique number of isolated complex pairs of uj in the continuum limit. Phase I corresponds to zero isolated uj, Phase II corresponds to one pair, and Phase III corresponds to two pairs.
The main result of this Appendix is that the roots of the Lax norm u and the frequencies ω of δ∆(t) are related by u − ur = ± 1
2
√ω2 − b2
min, where ur is the real part of the root (cf. Refs. 42 and 53), and bmin is the band edge in the frequency spectrum (bmin = 0 in Phase I). Thus, the new pair of complex conjugate Lax roots appears at the same time that ω emerges into the band gap (i.e., ω2 < b2
min in Phase II and ω2 < 0 in Phase I). Here and below in this Appendix, we use the same notation u for the roots and for generic values of the spectral parameter.
One may plug into the Lax norms the asymptotic spin solution (5.9) for Phase II, but we shall use solutions that do not impose particle-hole symmetry. Letting ε ̃j = εj − μ∞, and noting that sums over the time-dependent


 27
terms dephase in the t → ∞ limit, we find
L2(u) =
(
−1
gf
+ σ1
)2
+ ∆2
∞σ2
2,
σ1 ≡
∑
j
Zj u − εj
, σ2 ≡
∑
j
Zj
ε ̃j(u − εj) ,
L2(u) =
(
−1
gf
+ p1
)2
+ u∆2
∞p2
2
p1 ≡
∑
j
εj Zj u − εj
, p2 ≡
∑
j
εj Zj
ε ̃j(u − εj) .
(D3)
Eq. (D3) reduces to the Phase I Lax norms when ∆∞ = 0 and by convention Zj → zj. In Phase II, Eq. (D3) is supplemented by the self-consistency relationship
1 = −gf
∑
j
f2
j Zj
ε ̃j
. (D4)
2. Phase I-II transition
In the s-wave case, and in Phase I, we compare the stability equation Eq. (5.20) to the vanishing of the Lax norm L2(u) = 0. After some algebra, Eqs. (5.20) and L2(u) = 0 become
1
gf
=
∑
j
zj ±1
2 ω0 + μ∞ − εj
, (D5a)
1
gf
=
∑
j
zj u − εj
, (D5b)
respectively. We argued in Sect. V B that the Phase I-II transition occurs when a purely imaginary pair of complex conjugate ω0 emerges as solutions to Eq. (D5a), implying an exponential instability to Phase I. The Lax construction stipulates that the same transition occurs when an isolated pair of complex conjugate u solve Eq. (D5b). In order for these two methods to match, we must make the identification u − μ∞ = ± 1
2 ω0, i.e., the real part of
the emergent Lax norm pair of roots must be μ∞. We prove this is the case in Sect. D 4. The corresponding equations for Phase I in the p + ip model are
1
gf
=
∑
j
εj zj ±1
2 ω0 + μ∞ − εj
, (D6a)
1
gf
=
∑
j
εj zj u − εj
, (D6b)
and the same identification reconciles the two approaches.
3. Phase II-III transition
In Phase II, one applies the self-consistency relationship (D4) to the Lax norms (D3). In the s-wave case,
L2(u) = 0 becomes
0 = [(u − μ∞)2 + ∆2
∞
]
( ∑
j
Zj ε ̃j(u − εj)
)2
, (D7)
and we see the single pair of isolated conjugate roots are u± = μ∞ ± i∆∞. The equation for the second pair of isolated roots that would signal a transition to Phase III is therefore
0=
∑
j
Zj
ε ̃j(u − εj) . (D8)
After applying Eq. (D4) to the quantities Sj(ω0) in the stability equation (5.20), we find for the s-wave model
S1(ω) − 1 =
( ω2
4∆2∞
−1
)
S3(ω). (D9)
This simplifies Eq. (5.20) to
0=
∑
j
Zj
ε ̃j(±y + μ∞ − εj) , y = 1
2
√ω2 − 4∆2∞.
(D10)
Matching (D10) to (D8), we make the correspondence u − μ∞ = ± 1
2
√ω02 − 4∆2∞. As we discussed in Sect. V B, an ω0 emerging out of the continuum and into the band gap signals the transition to Phase III. The band edge in the s-wave model is precisely 2∆∞. We show in Sect. D 4 that the new pair of conjugate Lax roots has real part μ∞. Therefore, the two approaches predict the same phase transition. In the p + ip case, L2(u) = 0 couples with (D4) to give
0 = [u∆2
∞ + (u − μ∞)2]
( ∑
j
εj Zj ε ̃j(u − εj)
)2
. (D11)
The single pair of isolated roots of Phase II is then
u± = uc ± i∆∞
√
μ∞ − ∆2∞
4 ; uc ≡ μ∞ − ∆2∞
2 , (D12)
and the emergent pair of conjugate roots solves
0=
∑
j
εj Zj
ε ̃j(u − εj) . (D13)
To show that the stability analysis reproduces Eq. (D13), we will need two relations. The first holds in general by applying the self-consistency relation (D4) to the sums in (5.20)
S1(ω) − 1 = ω2S4(ω) − S3(ω),
S4(ω) ≡ gf
∑
j
f2
j Zj
ε ̃j(ω2 −  ̃b2
j ) , (D14)


 28
while the second is specific to the p + ip model
S2(ω) = −2ωμ∞S4(ω) + ω
2∆2∞
S3(ω). (D15)
We substitute Eqs. (D14)-(D15) into Eq. (5.20), which becomes a quadratic function of S3 and S4. The solution is
0=
∑
j
Zj
ε ̃j(±y + uc − εj) , y = 1
2
√
ω2 − B12, (D16)
where B1 = √4μ∞∆2∞ − ∆4∞ is the band edge when uc ≥ 0. In this parameter range, we identity u − uc =
±1
2
√ω2 − B12. We show in Sect. D 4 that the real part of the emergent Lax roots is uc, and therefore the stability analysis and Lax constructions give the same Phase II-III transition. When uc < 0, the band edge is no longer B1, and we believe there to be no Phase II-III transition in that case.
4. Real parts of Lax roots at the transitions
The equivalence between the Lax construction and the stability analysis relies on the fact that the real parts of the emerging Lax roots are equal to μ∞ at the Phase I-II transition in both integrable models, μ∞ at the Phase II
III transition in the s-wave model, and μ∞ − ∆2
∞
2 at the
Phase II-III transition in the p+ip model. In other words, the emergent second pair of isolated roots has the same real part as the first pair of isolated roots. The Phase I-II transition real parts can be understood by a continuity argument. In the s-wave model, Eq. (D7) implies that the single pair of roots can be written as u± = μ∞ ± i∆∞. As we approach the I-II boundary, ∆∞ decreases continuously to zero, which implies the real part of both roots at the boundary is μ∞. In the p + ip case, a similar argument follows from Eq. (D12).
a. s-wave, II-III
We use results from the spin reduction mechanism, discussed in Appendix C, of the s-wave model to obtain the real parts of the Lax roots at the Phase II-III transition. This discussion quotes several results directly from Sect. II B 3 of Ref. 53. The isolated roots in Phase III of L2(u) are given by the roots of the 2-spin spectral polynomial53 Q4(u)
Q4(u) = [(u − μ)2 − ρ]2 − κ(u − μ) − χ. (D17)
We determine the real parameters μ, ρ, κ and χ at the transition, which will then give the roots of Q4(u). To do so, we use the differential equation and solution for the 2-spin ∆, which is identical to that of the Phase III asymptotic ∆ of the many-body problem, which we write
as ∆ = |∆|e−iΦ. Let w = |∆|2 = Λ2 + h1, where h1 is a constant. The differential equation for w is
0 = w ̇ 2 + 4w3 + 16ρw2 + 16χw + 4κ2, (D18)
while the equation for the phase Φ is
Φ ̇ = 2μ − κ
Λ2 + h1
. (D19)
Upon rewriting (D18) as an equation for Λ, we find
Λ ̇ 2 = −(Λ2
+ − Λ2)(Λ2
− − Λ2), (D20)
where the constants Λ± are the maximum and minimum of the Λ oscillations which are functions of the constants ρ, χ and κ. The solution of interest to Eq. (D20) is
Λ = Λ+dn
[
Λ+(t − t0), 1 − Λ2−
Λ2+
]
. (D21)
Near the II-III transition, the oscillations of Λ are small and it sufficient to keep only the first harmonic of Eq. (D21)
Λ ≈ Λ0 + δ cos [ω0(t − t0)],
δ Λ0, ω0 ≈ 2Λ0. (D22)
As we approach the II-III transition, ∆ → ∆∞e−2iμ∞t. Because |∆|2 = Λ2 + h1 has the same frequency as Λ2, and the frequency of small oscillations of |∆|2 at the IIIII transition is 2∆∞, we conclude Λ0 = ∆∞ and h1 = 0. Using Eq. (D19), we also find κ = 0 and μ = μ∞. It remains to determine the constants ρ and χ, which we do by plugging (D22) into (D18) and considering the
O(δ0) and O(δ) terms separately. The result is ρ = − ∆2
∞ 2
and χ = ∆4
∞
4 . The roots of the spectral polynomial Q4(u)
from Eq. (D17) at the Phase II-III transition therefore solve
0=
[
(u − μ∞)2 + ∆2∞
2
]2
− ∆4∞
4 . (D23)
One solution to (D23) is u± = μ∞ ± i∆∞, which is the single isolated pair characteristic of Phase II. The other solution is a double root at u = μ∞, i.e., the new pair of roots that emerges in Phase III has real part μ∞.
b. p + ip, II-III
In order to prove that the Lax construction and stability analysis predict the same p+ip Phase II-III transition, we needed to assume that the real part of the emerging second pair of roots equals that of the first pair of roots u± from (D12). Using results from Ref. 54, we now show that this is indeed the case. For brevity, our derivation will use the conventions of Ref. 54, where the definitions of some quantities differ


 29
by numerical factors. One redefines ε → 2ε, 2G → g,
√2∆ → ∆ and u → 2u in order to translate quantities from Ref. 54 to those in this work. While some details of the derivation depend on such conventions, the conclusion does not. We also assume uc ≡ Re[u±] ≥ 0, which is the parameter regime where we show the equivalence of the Lax construction and stability analysis for the p + ip model. Eq. (4.3) of Ref. 54 gives the isolated pair of roots in Phase II to be u± = uc ± 2iEmin, where Emin is the minimum of the asymptotic dispersion relation [see text below Eq. (5.29) in Ref. 54]. According to Eq. (4.39) in Ref. 54 the frequency of small oscillations in Phase III close to the Phase II-III boundary is
Ωc =
√
(ur − uc)2 + 4E2
min, (D24)
where ur is the real part of the pair of roots absent in Phase II. The frequency Ωc should match the frequency of dephasing oscillations in Phase II close to the boundary. The text below Eq. (3.53) in Ref. 54 says that the latter frequency is
Ω = 2Emin. (D25)
Setting Ωc = Ω, implies that on the Phase II-III boundary
ur = uc. (D26)
1 T. Kinoshita, T. Wenger, and D. S. Weiss, A quantum Newton’s cradle, Nature 440, 900 (2006). 2 H. Lignier, C. Sias, D. Ciampini, Y. Singh, A. Zenesini, O. Morsch, and E. Arimondo, Dynamical Control of MatterWave Tunneling in Periodic Potentials, Phys. Rev. Lett. 99, 220403 (2007). 3 S. Hofferberth, I. Lesanovsky, B. Fischer, T. Schumm, and J. Schmiedmayer, Non-equilibrium coherence dynamics in one-dimensional Bose gases, Nature 449 324 (2007). 4 C. N. Weiler, T. W. Neely, D. R. Scherer, A. S. Bradley, M. J. Davis, and B. P. Anderson, Spontaneous vortices in the formation of Bose-Einstein condensates, Nature 455, 948 (2008). 5 A. Widera, S. Trotzky, P. Cheinet, S. Fo ̈lling, F. Gerbier, I. Bloch, V. Gritsev, M. D. Lukin, and E. Demler, Quantum Spin Dynamics of Mode-Squeezed Luttinger Liquids in Two-Component Atomic Gases, Phys. Rev. Lett. 100, 140401 (2008). 6 M. Gring, M. Kuhnert, T. Langen, T. Kitagawa, B. Rauer, M. Schreitl, I. Mazets, D. Adu Smith, E. Demler, and J. Schmiedmayer, Relaxation and Prethermalization in an Isolated Quantum System, Science 337, 1318 (2012). 7 T. Langen, S. Erne, R. Geiger, B. Rauer, T. Schweigler, M. Kuhnert, W. Rohringer, I. E. Mazets, T. Gasenzer, and J. Schmiedmayer, Experimental observation of a generalized Gibbs ensemble, Science 348, 207 (2015). 8 Y. Tang, W. Kao, K.-Y. Li, S. Seo, K. Mallayya, M. Rigol, S. Gopalakrishnan, and B. L. Lev, Thermalization near Integrability in a Dipolar Quantum Newton’s Cradle, Phys. Rev. X 8, 021030 (2018). 9 M. A. Norcia, R. J. Lewis-Swan, J. R. K. Cline, B. Zhu, A. M. Rey, J. K. Thompson, Cavity-mediated collective spinexchange interactions in a strontium superradiant laser, Science 361, 259 (2018). 10 S. Smale, P. He, B. A. Olsen, K. G. Jackson, H. Sharum, S. Trotzky, J. Marino, A. M. Rey, J. H. Thywissen, Observation of a Dynamical Phase Transition in the Collective Heisenberg Model, arXiv:1806.11044 (2018). 11 T. Kampfrath, K. Tanaka, K. A. Nelson, Resonant and nonresonant control over matter and light by intense terahetz transients, Nat. Phot. 7, 680 (2013). 12 C. Giannetti, M. Capone, D. Fausti, M. Fabrizio, F. Parmi
giani and D. Mihailovic, Ultrafast optical spectroscopy of strongly correlated materials and high-temperature superconductors: a non-equilibrium approach, Adv. Phys. 65, 58 (2016). 13 D. Fausti, R. I. Tobey, N. Dean, S. Kaiser, A. Dienst, M. C. Hoffmann, S. Pyon, T. Takayama, H. Takagi and A. Cavalieri, Light-induced superconductivity in a stripeordered cuprate, Science 331, 189 (2011). 14 R. Matsunaga, Y. I. Hamada, K. Makise, Y. Uzawa, H. Terai, Z. Wang and R. Shimano, Higgs amplitude mode in the BCS superconductors Nb1−xTixN induced by terahertz pulse excitation, Phys. Rev. Lett. 111, 057002 (2013). 15 R. Matsunaga, N. Tsuji, H. Fujita, A. Sugioka, K. Makise, Y. Uzawa, H. Terai, Z. Wang, H. Aoki and R. Shimano, Light-induced collective pseudospin precession resonating with Higgs mode in a superconductor, Science 345, 1145 (2014). 16 H. Ribeiro, J. R. Petta, and G. Burkard, Interplay of charge and spin coherence in Landau-Zener-St ̈uckelbergMajorana interferometry, Phys. Rev. B 87, 235318 (2013). 17 P. Richerme, Z.-X. Gong, A. Lee, C. Senko, J. Smith, M. Foss-Feig, S. Michalakis, A. V. Gorshkov and C. Monroe, Non-local propagation of correlations in quantum systems with long-range interactions, Nature 511, 198 (2014). 18 L. Wang, C. Zhou, T. Tu, H.-W. Jiang, G.-P. Guo, and G.C. Guo, Quantum simulation of the Kibble-Zurek mechanism using a semiconductor electron charge qubit, Phys. Rev. A 89, 022337 (2014). 19 R. Barends, L. Lamata, J. Kelly, L. Garcı ́a-  ́Alvarez, A.G. Fowler, A. Megrant, E. Jeffrey, T. C. White, D. Sank, J.Y. Mutus et. al., Digital quantum simulation of fermionic models with a superconducting circuit, Nature Comm. 6, 7654 (2015). 20 J. M. Nichol, S. P. Harvey, M. D. Shulman, A. Pal, V. Umansky, E. I. Rashba, B. I. Halperin, and Amir Yacoby, Quenching of dynamic nuclear polarization by spin-orbit coupling in GaAs quantum dots, Nature Comm. 6, 7682 (2015). 21 C. Song, K. Xu, W. Liu, C. Yang, S.-B. Zheng, H. Deng, Q. Xie, K. Huang, Q. Guo, L. Zhang et. al., 10-Qubit Entanglement and Parallel Logic Operations with a Superconducting Circuit, Phys. Rev. Lett. 119, 180511 (2017).


 30
22 H. Bernien, S. Schwartz, A. Keesling, H. Levine, A. Omran, H. Pichler, S. Choi, A. S. Zibrov, M. Endres, M. Greiner, V. Vuletic ́ and M. D. Lukin, Probing many-body dynamics on a 51-atom quantum simulator, Nature 551, 579 (2017). 23 J. Zhang, G. Pagano, P. W. Hess, A. Kyprianidis, P. Becker, H. Kaplan, A. V. Gorshkov, Z.-X. Gong and C. Monroe, Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator, Nature 551, 601 (2017). 24 A. Regal, M. Greiner, and D. S. Jin, Observation of Resonance Condensation of Fermionic Atom Pairs, Phys. Rev. Lett. 92, 040403 (2004). 25 M. W. Zwierlein, C. A. Stan, C. H. Schunck, S. M. F. Raupach, A. J. Kerman, and W. Ketterle, Condensation of Pairs of Fermionic Atoms near a Feshbach Resonance, Phys. Rev. Lett. 92, 120403 (2004). 26 M. W. Zwierlein, J. R. Abo-Shaeer, A. Schirotyek, C. H. Schunck and W. Ketterle, Vortices and superfluidity in a strongly interacting Fermi gas, Nature 435, 1047 (2005). 27 I. Bloch, J. Dalibard and W. Zwerger, Many-body physics with ultracold gases, Rev. Mod. Phys. 80, 885 (2008). 28 S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of ultracold atomic Fermi gases, Rev. Mod. Phys. 80, 1215 (2008). 29 I. Bloch, J. Dalibard and S. Nascimbe`ne, Quantum simulations with ultracold quantum gases, Nature Phys. 8, 267 (2012). 30 A. Polkovnikov, K. Sengupta, A. Silva and M. Vengalattore, Colloquium: Nonequilibrium dynamics of closed interacting quantum systems. Rev. Mod. Phys. 83, 863 (2011). 31 J. Eisert, M. Friesdorf, C. Gogolin, Quantum many-body systems out of equilibrium, Nature Phys. 11, 124 (2015). 32 R. Vasseur and J. E. Moore, Nonequilibrium quantum dynamics and transport: from integrability to many-body localization, J. Stat. Mech. 064010 (2016). 33 P. W. Anderson, Random-Phase Approximation in the Theory of Superconductivity, Phys. Rev. 112, 1900 (1958). 34 V. P. Galaiko, Kinetic Equations for Relaxation Processes in Superconductors, Sov. Phys. JETP 34, 203 (1972). 35 A. F. Volkov and S. M. Kogan, Collisionless relaxation of the energy gap in superconductors, Sov. Phys. JETP 38, 1018 (1974). 36 Yu. M. Galperin, V. I. Kozub, and B. Z. Spivak, Stability of the nonequilibrium states of a superconductor with a finite difference between the populations of the electron and hole-like spectral branches, Sov. Phys. JETP 54, 1126 (1981). 37 R. A. Barankov, L. S. Levitov, and B. Z. Spivak, Collective Rabi Oscillations and Solitons in a Time-Dependent BCS Pairing Problem, Phys. Rev. Lett. 93, 160401 (2004). 38 M. Amin, E. Bezuglyi, A. Kijko, and A. Omelyanchouk, Wigner distribution function formalism for superconductors and collisionless dynamics of the superconducting order parameter, Low Temp. Phys. 30, 661 (2004). 39 E. A. Yuzbashyan, B. L. Altshuler, V. B. Kuznetsov, and V. Z. Enolskii, Solution for the dynamics of the BCS and central spin problems, J. Phys. A 38, 7831 (2005). 40 M. H. Szymanska, B. D. Simons, and K. Burnett, Dynamics of the BCS-BEC Crossover in a Degenerate Fermi Gas, Phys. Rev. Lett. 94, 170402 (2005). 41 E. A. Yuzbashyan, B. L. Altshuler, V. B. Kuznetsov, and V. Z. Enolskii, Nonequilibrium Cooper pairing in the nona
diabatic regime, Phys. Rev. B 72, 220503(R) (2005). 42 E. A. Yuzbashyan, O. Tsyplyatyev and B. Altshuler, Relaxation and persistent oscillations of the order parameter in fermionic condensates, Phys. Rev. Lett 96, 097005 (2006). 43 R. A. Barankov and L. S. Levitov, Synchronization in the BCS pairing dynamics as a critical phenomenon, Phys. Rev. Lett. 96, 230403 (2006). 44 E. A. Yuzbashyan and M. Dzero, Dynamical vanishing of the order parameter in a fermionic condensate, Phys. Rev. Lett. 96, 230404 (2006). 45 R. A. Barankov and L. S. Levitov, Excitation of the dissipationless Higgs mode in a fermionic condensate, arXiv:0704.1292 (2007). 46 D. Pekker and C. M. Varma, Amplitude/Higgs modes in condensed matter physics, Ann. Rev. Cond. Mat. Phys. 6, 269 (2015). 47 A. Pashkin and A. Leitenstorfer, Particle physics in a superconductor, Science 345, 1121 (2014). 48 Y. Barlas and C. M. Varma, Amplitude or Higgs modes in d-wave superconductors, Phys. Rev. B. 87, 054503 (2013). 49 B. Nosarzewski, B. Moritz, J. K. Freericks, A. F. Kempter and T. P. Devereaux, Amplitude mode oscillations in pump-probe photoemission spectra from a d-wave superconductor, Phys. Rev. B 96, 184518 (2017). 50 S. Hannibal, P. Kettmann, M. D. Croitoru, A. Vagov, V. M. Axt and T. Kuhn, Quench dynamics of an ultracold Fermi gas in the BCS regime: Spectral properties and confinement-induced breakdown of the Higgs mode, Phys. Rev. A 91, 043630 (2015). 51 H. Krull, N. Bittner, G. S. Uhrig, D. Manske and A. P. Schnyder, Coupling of Higgs and Leggett modes in nonequilibrium superconductors, Nat. Comm. 7, (2016). 52 A. Moor, A. F. Volkov and K. B. Efetov, Amplitude Higgs mode and admittance in superconductors with a moving condensate, Phys. Rev. Lett. 118, 047001 (2017). 53 E. A. Yuzbashyan, M. Dzero, V. Gurarie and M. S. Foster, Quantum quench phase diagrams of an s-wave BCS-BEC condensate, Phys. Rev. A 91, 033628 (2015). 54 M. S. Foster, M. Dzero, V. Gurarie and E. A. Yuzbashyan, Quantum quench in a p + ip superfluid: Winding numbers and topological states far from equilibrium, Phys. Rev. B 88, 104511 (2013). 55 Y. Dong, L. Dong, M. Gong and H. Pu, Dynamical phases in quenched spin-orbit-coupled degenerate Fermi gas, Nat. Comm. 6, 6103 (2015). 56 M. Dzero, A. A. Kirmani and E. A. Yuzbashyan, Nonadiabatic dynamics of superfluid spin-orbit-coupled degenerate Fermi gas, Phys. Rev. A 92, 053626 (2015). 57 F. Peronaci, M. Schiro ́ and M. Capone, Transient dynamics of d-wave superconductors after a sudden quench, Phys. Rev. Lett. 115, 257001 (2015). 58 Not all three phases are necessarily present in a given model, e.g., there are models where Phase II45 or Phase III57 are absent, see also the discussion in Sect. V B 59 M. Sato, Y. Takahashi, and S. Fujimoto, Non-Abelian topological order in s-wave superfluids of ultracold fermionic atoms, Phys. Rev. Lett. 103, 020401 (2009). 60 M. Sato, Y. Takahashi, and S. Fujimoto, Non-Abelian topological orders and Majorana fermions in spin-singlet superconductors, Phys. Rev. B 82, 134521 (2010). 61 R. W. Richardson, New Class of Solvable and Integrable Many-Body Models, arXiv:cond-mat/0203512 (2002). 62 G. Ortiz, R. Somma, J. Dukelsky, and S. Rombouts,


 31
Exactly-solvable models derived from a generalized Gaudin algebra, Nucl. Phys. B 707, 421 (2005). 63 C. Dunning, M. Ibanez, J. Links, G. Sierra, and S.-Y. Zhao, Exact solution of the p+ip pairing Hamiltonian and a hierarchy of integrable models, J. Stat. Mech. P08025 (2010). 64 M. A. Rombouts, J. Dukelsky, and G. Ortiz, Quantum phase diagram of the integrable px + ipy fermionic superfluid, Phys. Rev. B 82, 224510 (2010). 65 I. Marquette and J. Links, Integrability of an extended d + id-wave pairing Hamiltonian, Nucl. Phys. B 866, 378 (2013). 66 V. Makhalov, K. Martiyanov and A. Turlapov, Observation of two-dimensional Fermi gas of atoms, Phys. Rev. Lett 105, 030404 (2010). 67 B. Fro ̈hlich, M. Feld, E. Vogt, M. Koschorreck, W. Zwerger and M. Ko ̈hl, Radio-frequency spectroscopy of a strongly interacting two-dimensional Fermi gas, Phys. Rev. Lett. 106, 105301 (2011). 68 P. Dyke, E. D. Kuhnle, S. Whitlock, H. Hu, M. Mark, S. Hoinka, M. Lingham, P. Hannaford and C. J. Vale, Crossover from 2D to 3D in a weakly interacting Fermi gas, Phys. Rev. Lett. 106, 105304 (2011). 69 P. Wang, Z. Q. Yu, Z. Fu, J. Miao, L. Huang, S. Chai, H. Zhai and J. Zhang, Spin-orbit coupled degenerate Fermi gases, Phys. Rev. Lett. 109, 095301 (2012). 70 L. W. Cheuk, A. T. Sommer, Z. Hadzibabic, T. Yefsah, W. S. Bakr and M. W. Zwierlein, Spin-injection spectroscopy of a spin-orbit coupled Fermi gas, Phys. Rev. Lett. 109, 095302 (2012). 71 R. A. Williams, M. C. Beeler, L. J. LeBlanc, K. Jime ́nezGarcı ́a and I. B. Spielman, Raman-induced interactions in a single-component Fermi gas near an s-wave Feshbach resonance, Phys. Rev. Lett 111, 095301 (2013). 72 Z. Fu, L. Huang, Z. Meng, P. Wang, L. Zhang, S. Zhang, H. Zhai, P. Zhang and J. Zhang, Production of Feshbach molecules induced by spin-orbit coupling in Fermi gases, Nature Phys. 10, 110 (2014). 73 V. Makhalov, K. Martiyanov and A. Turlapov, Groundstate pressure of quasi-2D Fermi and Bose gases, Phys. Rev. Lett. 112, 045301 (2014). 74 L. Huang, Z. Meng, P. Wang, P. Peng, S. L. Zhang, L. Chen, D. Li, Q. Zhou and J. Zhang, Experimental realization of two-dimensional synthetic spin-orbit coupling in ultracold Fermi gases, Nature Phys. 12, 540 (2016). 75 H. Zhai, Degenerate quantum gases with spin-orbit coupling: a review, Rep. Prog. Phys. 78, 026001 (2015). 76 A. A. Kirmani and M. Dzero, Short-time order parameter dynamics in d + id-wave fermionic superfluids, arXiv:1804.11257 (2018). 77 One can choose the parameters differently in the two models, e.g., choose a different εF in the s-wave model, so that the first few oscillations almost coincide76. However, such fine-tuning seems unwarranted and, in any case, the longer-time dynamics will disagree. 78 H. Kantz, A robust method to estimate the maximal Lyapunov exponent of a time series, Phys. Lett. A 185, 77 (1994).
79 J. D. Crawford, Introduction to bifurcation theory, Rev. Mod. Phys. 63, 991 (1991).
80 Y. A. Kuznetsov, Elements of Applied Bifurcation Theory, Second Edition (Springer-Verlag, 1998).
81 R. C. Hilborn, Chaos and Nonlinear Dynamics, An Introduction for Scientists and Engineers, Second Edition (Oxford University Press, 2001). 82 In equilibrium, i.e., when gf = gi, Eq. (8.1) is simply the BCS gap equation with two fixed points ∆ = 0 and ∆ = ±∆0i corresponding to the normal and the BCS ground states, respectively. 83 In the absence of particle-hole symmetry, Phase II is a simple limit cycle ∆∞e−2iμ∞t (circle in the plane of complex ∆). Phase III is a 2D (two fundamental frequencies) torus (annulus in the plane of complex ∆). Phase I-II and II-III transitions are then analogous to supercritical Hopf and Neimark-Sacker (torus) bifurcations. 84 A. Patra, B. L. Altshuler and E. A. Yuzbashyan, DrivenDissipative Dynamics of Atomic Ensembles in a Resonant Cavity: Nonequilibrium Phase Diagram and Periodically Modulated Superradiance, arXiv:1811.01515 (2018). 85 A. Patra, B. L. Altshuler and E. A. Yuzbashyan, Chaotic Synchronization between Atomic Clocks, arXiv:1811.02148 (2018). 86 E. A. Yuzbashyan, Normal and anomalous solitons in the theory of dynamical Cooper pairing, Phys. Rev. B 78, 184507 (2008). 87 M. S. Foster, V. Gurarie, M. Dzero and E. A. Yuzbashyan, Quench-induced Floquet topological p-wave superfluids, Phys. Rev. Lett. 113, 076403 (2014). 88 E. A. Yuzbashyan and O. Tsyplyatyev, Dynamics of emergent Cooper pairing at finite temperatures, Phys. Rev. B 79, 132504 (2009). 89 M. Dzero, E. A. Yuzbashyan and B. L. Altshuler, Cooper pair turbulence in atomic Fermi gases, Eur. Phys. Lett. 85 20004 (2009). 90 M. S. Foster, E. A. Yuzbashyan and B. L. Altshuler, Quantum quench in 1D: Coherent inhomogeneity amplification and ‘supersolitons’, Phys. Rev. Lett. 105, 135701 (2010). 91 G.-W. Chern and K. Barros, Nonequilibrium dynamics of superconductivity in the attractive Hubbard model, arXiv:1803.04118 (2018). 92 M. Dzero, E. A. Yuzbashyan, B. L. Altshuler, Comment on “Nonequilibrium dynamics of superconductivity in the attractive Hubbard model”, arXiv:1806.03474 (2018). 93 A. Faribault, P. Calabrese, and J.-S. Caux, Bethe ansatz approach to quench dynamics in the Richardson model, J. Math. Phys. 50, 095212 (2009). 94 C. Stra ̈ter, O. Tsyplyatyev, and A. Faribault, “Nonequilibrum dynamics in the strongly excited inhomogeneous Dicke model”, Phys. Rev. B 86, 195101 (2012). 95 Note that Ref. 55 has a different convention of naming Phases I and III. The only example of Phase III |∆(t)| dynamics shown in Ref. 55 is for the integrable case hf = 0, when the long relaxation time τ is absent.
