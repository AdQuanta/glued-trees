# Dynamics of Interacting Fermions in Spin-Dependent Potentials - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevLett.117.195302
> Collected: 2026-09-20
> Published: 2016-11-04
> Zotero parent key: XHLTVMEA
> Evidence: Zotero indexed PDF text

This is the accepted manuscript made available via CHORUS. The article has been published as:
Dynamics of Interacting Fermions in Spin-Dependent Potentials
Andrew P. Koller, Michael L. Wall, Josh Mundinger, and Ana Maria Rey
Phys. Rev. Lett. 117, 195302 — Published 4 November 2016
DOI: 10.1103/PhysRevLett.117.195302


 Dynamics of interacting fermions in spin-dependent potentials
Andrew P. Koller,1, 2, ∗ Michael L. Wall,2, ∗ Josh Mundinger,3 and Ana Maria Rey1, 2
1Department of Physics, University of Colorado, Boulder, CO 80309 2JILA, NIST, Center for Theory of Quantum Matter, University of Colorado, Boulder, CO 80309 3Department of Mathematics and Statistics, Swarthmore College, 500 College Avenue, Swarthmore, PA 19081
Recent experiments with dilute trapped Fermi gases observed that weak interactions can drastically modify spin transport dynamics and give rise to robust collective effects including global demagnetization, macroscopic spin waves, spin segregation, and spin self-rephasing. In this work we develop a framework for studying the dynamics of weakly interacting fermionic gases following a spin-dependent change of the trapping potential which illuminates the interplay between spin, motion, Fermi statistics, and interactions. The key idea is the projection of the state of the system onto a set of lattice spin models defined on the single-particle mode space. Collective phenomena, including the global spreading of quantum correlations in real space, arise as a consequence of the long-ranged character of the spin model couplings. This approach achieves good agreement with prior measurements and suggests a number of directions for future experiments.
The interplay between spin and motional degrees of freedom in interacting electron systems has been a longstanding research topic in condensed matter physics. Interactions can modify the behavior of individual electrons and give rise to emergent collective phenomena such as superconductivity and colossal magnetoresistance [1]. Theoretical understanding of non-equilibrium dynamics in interacting fermionic matter is limited, however, and many open questions remain. Ultracold atomic Fermi gases, with precisely controllable parameters, offer an outstanding opportunity to investigate the emergence of collective behavior in out-of-equilibrium settings.
Progress in this direction has been made in recent experiments with ultracold spin-1/2 fermionic vapors, where initially spin-polarized gases were subjected to a spin-dependent trapping potential (Fig. 1) implemented by a magnetic field gradient [2–4], or a spin-dependent harmonic trapping frequency [5–8] – equivalent to a spatially-varying gradient. Even in the weakly interacting regime, drastic modifications of the single-particle dynamics were reported. Moreover, despite the local character of the interactions, collective phenomena were observed, including demagnetization and transverse spinwaves in the former, and a time-dependent separation (segregation) of the spin densities and spin self-rephasing in the latter. Although mean-field and kinetic theory formulations have explained some of these phenomena [818], a theory capable of describing all the time scales and the interplay between spin, motion, and interactions has not been developed.
In this work, we develop a framework that accounts for the coupling of spin and motion in weakly interacting Fermi gases. We qualitatively reproduce and explain all phenomena of the aforementioned experiments and obtain quantitative agreement with the results of Ref. [7]. In this formulation the state of the system is represented as a superposition of spin configurations which live on lattices whose sites correspond to modes of the underlying single-particle system. Within each configuration,
a V "(x) V #(x)
mode number
n=0
n=1
n=2
...
V "(x) = V #(x)
Quench
b | i(t) = ...i+ ...i+ ...
n=0 n=1 n=2 n=0 n=1 n=2 n=3
Hˆns0m Hˆns1m
d1|
d0|
FIG. 1. (Color online) (a) Atoms spin-polarized along X occupy single-particle eigenstates, labeled by mode number n. The potential is quenched to a spin-dependent form, and dynamics result from a spin model with long ranged interactions (green wavy lines) in energy space. (b) The state |ψ〉 is a coherent superposition of spins in many mode configurations (unoccupied modes are represented by open circles). In each configuration particles are localized in mode space, with spin model Hamiltonian Hˆ sm
i . Coherences between the configurations capture motional effects.
the dynamics is described by a spin model with longranged couplings which generates collective quantum correlations and entanglement. Each sector evolves independently and the accumulated phase differences between sectors capture the interplay of spin and motion (Fig. 1 b). Using this formulation, we gain a great deal of insight about the dynamics, and can extract analytic solutions for spin observables and correlations in several limits. Although spin models in energy space [19–25] have been used before and agreed well with experiments [5, 23, 2630], their use was limited to pure spin dynamics (no motion). Our formulation allows us to track motional degrees of freedom, compute local observables, and determine how correlations spread in real space. This opens a route for investigations of generic interacting spin-motion coupled systems beyond current capabilities. Our predictions also suggest directions for future experiments in the


 2
weakly interacting regime, which might, for instance, investigate the collective rise of quantum correlations. In contrast to strongly coupled ultracold gases, where motion is quickly suppressed and features of the dynamics tend to be universal [2, 31, 32], in the weakly-interacting regime spin, motion, and interactions are all important and must be treated on the same level. A wide variety of analytical and numerical tools have been developed for lattice quantum spin models [3340], making a spin model description of fermions potentially very useful. To demonstrate the capabilities of this approach, we use time-dependent matrix product state methods which are efficient in one-dimension [41]. Setup– We consider N identical fermionic atoms of mass ma with a spin-1/2 degree of freedom α ∈ {↑, ↓} trapped in a one dimensional harmonic oscillator of frequency ω, V 0(x) = 1
2 maω2x2. The gas begins spin
polarized in the ↓ state and atoms populate distinct trap
modes. The initial Hamiltonian is Hˆ = Hˆ sp
0 +Hˆ int where
Hˆ sp
0 =∑
α
∫
dxψˆ†α(x)
(
−1
2ma
∂2
∂x2 + V 0(x)
)
ψˆα(x),
Hˆ int = 2as
maa2⊥
∫
dxρˆ↑(x)ρˆ↓(x).
ψˆα(x) is the fermionic field operator for spin α at point x,
as is the s-wave scattering length, ρˆα(x) = ψˆ†α(x)ψˆα(x), ħ = 1, and we have integrated over two transverse directions with small confinement length a⊥ aH , with
aH = (maω)− 1
2 . Note that the initial spin-polarized sample will not experience interactions. A resonant π/2 pulse collectively rotates the spin to the X-axis, and a magnetic field gradient is suddenly turned on. This introduces a sudden change (quench) in the single-particle Hamilto
nian Hˆ sp
0 , which becomes spin-dependent, Hˆ sp, where
Hˆ sp = ∑
α
∫
dxψˆ†α(x)
(
−1
2ma
∂2
∂x2 + V α(x)
)
ψˆα(x).
This quench protocol is illustrated in Fig. 1(a). The spin-dependence of the trapping potential V α=↑,↓(x) creates an inhomogeneity between the spin species, allowing contact s-wave collisions to occur. Expanding the field operators in the basis of single-particle eigenstates φnα(x) with associated creation operator cˆ†nα and defin
ing the interaction parameter u↑↓ = 2as/(maaH a2⊥),
Hˆ int becomes u↑↓
∑
nmpq Anmpqcˆ†
n↑cˆm↑cˆ†
p↓cˆq↓, where
Anmpq = aH
∫ dxφ↑n(x)φ↑m(x)φ↓p(x)φq↓(x).
To model two classes of experiments [2–4] and [58], we consider spin-dependent potentials of the form V α=↑,↓(x) = V 0(x) + ∆V α(x), with ∆V α(x) generated by a magnetic field with a constant gradient, ∆V α(x) = ±Bx, or a linear gradient, ∆V α(x) = ±maω2Bx2/2. In
both cases Hˆ sp can be written as:
Hˆ sp = ∑
n
[
ω ̄(n + 1/2)Nˆn + ∆ω (n + 1/2) σˆnZ
]
,
with Nˆn = cˆ†
n↑cˆn↑ + cˆ†
n↓cˆn↓, and {σˆnX , σˆnY , σˆnZ } ≡
∑
α,β cˆ†nα~σαβcˆnβ where ~σ is a vector of Pauli matrices.
The constant gradient shifts the trap for spin up (down) by x0 (−x0), with x0 = B
maω2 , but does not change the
frequency; ω ̄ = ω and ∆ω = 0. In a noninteracting gas the ↓ and ↑ densities and the magnetization oscillate at frequency ω due to this motion [16, 42]. A linear gradient adds an additional harmonic potential term resulting in different trap frequencies for the two spins: ω ̄ = (ω↑ + ω↓)/2 and ∆ω = (ω↑ − ω↓)/2. The noninteracting spin densities undergo a breathing motion in their respective traps, leading to oscillations in the total magnetization [42]. A finite ∆ω causes dephasing through rotations of the magnetization in the XY plane with mode-dependent rates.
The generalized spin model approximation– The quench of the trapping potential to a spin-dependent form projects the initially polarized state, which we take to be the ground state in this work, onto the eigenmode
basis of Hˆ sp[43]. The resulting state |ψ〉t=0 is a coherent superposition of many product states, each characterized by a set of populated modes ni = {ni1, ni2, . . . , niN }:
|ψ〉t=0 = ∑
i di
⊗N
j=1
(
cˆ†
ni
j↑ + cˆ†
ni
j↓
)
|0〉. The coefficients
di are determined by the change of basis associated with
the eigenstates of V 0(x) and V α=↑,↓(x). Our key approximation is that single particle modes either remain the same or are exchanged between two colliding atoms. Exact numerical calculations confirm the validity of this approximation in the weakly interacting regime [44]. For each set ni the resulting total Hamiltonian takes the form of an XXZ spin model,
Hˆnsim = Hˆ sp
ni − u↑↓
4
∑
n6=m∈ni
∑
ν=X,Y,Z Jnνmσˆνnσˆνm , (1)
plus additional small density-σˆZ couplings [44]. Here, the Ising, JnZm ≡ Annmm, and exchange, JnXm = JnYm =
Jn⊥m ≡ Anmmn, couplings result from the overlap between the ↑ and ↓ single-particle eigenstates and are longranged (∼ 1/√|n − m|) in each direction (x, y, z) [44]. In this approximation, each sector ni evolves independently, but with ni-dependent parameters, under Eq. 1. When computing observables, we account for both the interaction-driven spin dynamics within each ni sector, as well as the single particle dynamics determined from the coherences between sectors. Spin observables– The local and collec
tive magnetizations are given by S~ˆ(x) =
1 2
∑
nm,α,β φnα(x)φβm(x) (cˆ†nα~σαβ cˆβm
) and S~ˆ = ∫ dxS~ˆ(x). Fig. 2 summarizes the results for a constant gradient with N = 10 [45]. At short times the collective mag
netization 〈SˆX 〉 ((a) and (e)) exhibits characteristic single-particle oscillations at frequency ω; these quickly dephase and are modulated by a global envelope with a longer time scale. Similar behavior is observed for the
local magnetizations 〈SˆX,Y,Z (x)〉 (b-d, f-h). Although


 3
0 20 40 60 80 100
0.05 0.15 0.25 0.35 0.45
1
2
3
4
5
!t u"#/!
0 20 40 60 80 100
0.05 0.15 0.25 0.35 0.45
0
1
2
3
4
5
u"#/!
!t
bc d
a
f gh
e
!t !t !t
!t !t !t
hSˆX (x)i
hSˆX i hSˆY (x)i hSˆZ (x)i
x/aH
x/aH
hSˆX i
x/aH x/aH
hSˆX (x)i hSˆY (x)i x/aH hSˆZ (x)i x/aH
FIG. 2. (Color online) Magnetization dynamics for a constant gradient. Collective 〈SˆX 〉 for a x0 = 0.1aH (a) (and x0 = 0.3aH (e)) displays global interaction-induced demagnetization, which damps single-particle oscillations. Collective (generic) Ising solutions, black lines, give the demagnetization envelopes. Local magnetizations 〈SˆX,Y,Z (x)〉 with x0 = 0.1aH (b-d) (and x0 = 0.3aH f-h) reflect similar behavior, both shown with u↑↓ = 0.35ω.
the total 〈SˆY,Z 〉 magnetizations are zero at all times,
the local quantities 〈SˆY,Z (x)〉 evolve due to coherences between mode configurations. Their dynamics, however, are damped by interactions. The dynamics can be understood as follows. For spin independent potentials, JnZm = Jn⊥m and ∆ω = 0. The
Hamiltonian Hˆnsim is SU(2) symmetric and commutes
with S~ˆ2, where S~ˆ ≡ 1
2
∑
n ~σˆn, and so its eigenstates
can be labelled by the total spin S. When a gradient is applied, the SU(2) symmetry is broken by terms ∆nm = JnZm −Jn⊥m (∆ω = 0 for a constant gradient), and
the Hamiltonian can be rewritten as HˆnSi + Hˆnδi , where
HˆnSi = Eni − u↑↓
4
∑
n6=m∈ni
[Jn⊥m~σn · ~σm +  ̄∆σˆnZ σˆZm
],
Hˆnδi = − u↑↓
4
∑
n6=m∈ni
δnmσˆnZ σˆZm, (2)
Eni = ω ̄ ∑
n∈ni (n + 1/2) is a constant, ∆ ̄ is the aver
age value of ∆nm, and δnm = ∆nm −  ̄∆. HˆnSi commutes
with S~ˆ2 so only Hˆnδi induces transitions between man
ifolds of different S. For a sufficiently weak gradient, and δnm Jn⊥m, a large energy gap G, which we call the Dicke gap, opens between the S = N/2 “Dicke” manifold and the S = (N/2 − 1) “spin-wave” manifold [44]. The state of the system begins in the Dicke manifold, and it
remains there when terms in Hˆnδi are small compared to
this gap [46]. Dynamics resulting from the collective Ising
term in HˆnSi is given by 〈SˆX 〉ni = N
2 cosN−1 (u↑↓  ̄∆t) , and
〈SˆY,Z 〉ni = 0. Since the interaction parameters JnZm and
Jn⊥m vary slowly with parameter index, the dynamics of
〈SˆX 〉ni is approximately the same for all i, and a single
configuration n0 ≡ {0, 1, · · · N − 1} well reproduces the demagnetization envelope (Fig. 2(a)).
For strong gradients, exchange processes are suppressed and the effective interaction Hamil
tonian becomes a generic Ising model Hˆ Ising
ni =
− u↑↓
4
∑
n6=m∈ni JnZmσˆnZ σˆZm, which also admits a simple
expression for the spin magnetization dynamics [37–40]
〈SˆX 〉ni = ∑
n∈ni
∏
m6=n∈ni cos (u↑↓JnZmt). In this limit
the demagnetization envelope can be captured by the n0 realization of the generic Ising solution (Fig. 2(e)).
Short time dynamics of an XXZ Hamiltonian [47] is
given by 〈SˆX 〉 = 〈SˆX 〉t=0
(1 − (t/τM )2) + O(t3), where we define τM as the demagnetization time. By analyzing the scaling of the interaction parameters we find that τM ∼ (N u↑↓x20
)−1 , which agrees well the numerical scaling ∼ u−1
↑↓ x0−2N −0.823 [44]. Similar behavior was re
ported in Ref. [2] in the weakly-interacting regime [48].
Fig. 3 (a) shows the numerically-obtained total magnetization vs. interactions for a weak linear gradient. The magnetization remains nearly constant for sufficiently strong interactions, and the collective spin dynamics is a global precession in the XY plane (inset). This self-rephasing effect was experimentally reported in Ref. [5], and the spin model provides a simple interpretation. For a system in a weak gradient, the single-particle term ∝ ∆ω is the largest inhomogeneity. In this limit the Hamiltonian simplifies
to − u↑↓
4
∑
n6=m Jn⊥m~σn · ~σm + ∑
n ∆ω(n + 1
2 )σˆnZ . When
∆ωNnaive G, where G is the Dicke gap and Nnaive is
the average mode occupation, most of the population
remains in the Dicke manifold. After projecting Hˆ sp onto the Dicke states, the dynamics is a collective precession in the XY plane of the generalized Bloch vector, i.e
〈Sˆ±(t)〉 = 〈Sˆ±(0)〉e±2it(Nave
ni + 1
2 )∆ω, with Sˆ± = SˆX ±iSˆY . Demagnetization is suppressed when interactions (∝ G)


 4
c
bd
0.05 0.15 0.25 0.35 0.45
0 20 40 60 80 100
-1
0
1
2
3
4
5
!t u"#/!
a
|hS~ˆi|
<Sx>
<Sy>
0 20 40 60 80 100
--42024
ωt
hhSSYXii
!t
Simulation 55ms Analytic 55ms Simulation 110ms Analytic 110 ms
FIG. 3. (Color online) Dynamics for a linear gradient. (a) Spin self-rephasing for ωB = 0.1ω: as interactions increase,
demagnetization is suppressed and 〈S~ˆ〉 precesses collectively in the XY plane (inset). (b) Simulation of a one dimensional gas at zero temperature with parameters from Ref. [7], showing (n↑ − n↓)/n0 at the cloud center (blue solid line) with analytic prediction (red dashed line), and (c) segregated spin density profiles. (d) Data from Ref. [7], and prediction (red dashed line) based on a thermal average of Rabi oscillations between the Dicke and spin-wave manifolds.
-0.4
-0.2
0
0.2
-0.4
-0.2
0
0.2
0.4
b
a
FIG. 4. (Color online) (a) Real part of the connected correlation function Re [G++(x, 0; t)] for a weak gradient (x0 = 0.1aH , u↑,↓ = 0.35ω). Correlations grow collectively due to the long-ranged nature of the interactions in energy space, and peak when the gas is demagnetized. (b) For a linear gradient in the self-rephasing regime (ωB = 0.1ω, u↑↓ = 0.45ω), the connected correlator Re [G++(x, 0; t)] rotates collectively in the XY plane.
dominate over the dephasing introduced by ∆ω. Under this condition, a large fraction of the population stays in the Dicke manifold. Spin segregation in fermionic gases – a clear, spatial separation of the spin densities, first reported in Ref. [7] – occurs at timescales set by the mean interaction energy, and reverses sign when interactions are switched from attractive to repulsive. When ∆ωN G, this effect can be understood as the result of off-resonant Rabi oscillations between the S = N/2 Dicke states and the S = (N/2−1) spin-wave states, which are coupled by the gradient and whose energies are separated by the Dicke gap G. If the gradient is weak, one can ignore coherences developed between mode sectors, and approximate φ↑n(x) ≈ φ↓n(x) = φn(x). In this limit the dynamics of
the population difference ∆n = n↑(x) − n↓(x) is approximately [44]
〈∆n〉 = 2∆ω
G
∑
n∈ni
φn(x)2 (n − Nnaive) (cos (Gt) − 1) .(3)
The spin density changes sign when n > Nnaive. Spin
segregation occurs as a result since high energy modes
on average occupy positions further from the origin than low energy modes.
We now proceed to use the spin model framework to model the segregation observed in Ref. [7]. Although the measurements were done in the high temperature regime, we first determine the role of single particle motion by modeling a simpler 1D case at zero temperature with the same effective parameters. This case can be exactly solved with t-DMRG [44] and Figs. 3(b,c) show the dynamics of (n↑(x) − n↓(x))/n0, where n0 =
(n↑(0) + n↓(0))/2. Single particle motion is negligible, and the dynamics is closely approximated by Eq. 3. This information allows us to model the actual experiment with a pure spin model. At the high temperature of the experiment, the Dicke gap significantly decreases, however, Eqn. 3 remains valid at short times when the majority of the population is in the Dicke manifold. The segregation obtained from a thermal average of Eqn. 3 [44] well reproduces the experiment as shown in Fig. 3d. For this calculation the only free parameter is the asymptotic value of the density imbalance [49]. The population difference saturates due to dephasing associated with the thermal spread of the G values.
Correlations– Our approach can be used to compute higher-order correlations, such as the G++(x, x′) =
〈Sˆ+(x)Sˆ+(x′)〉 − 〈Sˆ+(x)〉〈Sˆ+(x′)〉 correlator shown in Fig. 4. Although the system is initially non-interacting, G++(t = 0) shows finite anti-bunching correlations near x ∼ x′ arising from Fermi statistics (mode entanglement) [50, 51]. At later times, correlations behave collectively, a distinct consequence of the long-range character of the spin coupling parameters [52–56].
For a weak constant gradient, the collective Ising model provides a good characterization of the correlation
dynamics. For each spin configuration G++
ni (x, x′; t) =
f1i(x, x′) cosN−2 (2u↑↓  ̄∆t) − f2i(x, x′) cos2N−2 (u↑↓∆ ̄ t),
where the functions f1i,2(x, x′) depend on the set of
populated modes [44]. G++ peaks at the time when the system has completely demagnetized (Fig. 4(a)). For a pure spin system with a collective Ising Hamiltonian, the state at this time is a Schro ̈dinger-cat state [57, 58].


 5
For the linear gradient in the self-rephasing regime, we observe collective precession of G++ (Fig. 4(b)). As interactions decrease or the inhomogeneity increases, correlations are strongly affected by the interplay between single-particle dynamics and interactions. Mode entanglement tends to cause an almost linear spreading of the correlations with time [59–61], while interactions tend to globally distribute and damp those correlations [44]. Current experiments are in position to confirm these predictions. Outlook– We have discussed an approach to model the interplay of motional and spin degrees of freedom in weakly interacting fermionic systems in spin-dependent potentials. Simulations reproduce several collective dynamical phenomena that were recently observed in cold gas experiments, and we can understand the physics behind these effects with simple considerations. For larger systems and in higher dimensions, methods such as the discrete truncated Wigner approximation could be utilized [34–36, 62]. Our formulation may also be useful for modeling other spin transport experiments [31, 63].
ACKNOWLEDGEMENTS
We thank J. E. Thomas, K. R. A. Hazzard, A. Pikovski, and J. Schachenmayer for useful discussions, and P. Romatschke, J. Bohnet, and M. G ̈arttner for comments on the manuscript. This work was supported by JILA-NSF-PFC-1125844, NSF-PIF- 1211914, ARO, AFOSR, and AFOSR-MURI. AK was supported by the Department of Defense through the NDSEG program. MLW thanks the NRC postdoctoral fellowship program for support.
∗ A.P.K. and M.L.W. contributed equally to this work. [1] A. P. Ramirez, Journal of Physics: Condensed Matter 9, 8171 (1997). [2] M. Koschorreck, D. Pertot, E. Vogt, and M. Kohl, Nature Physics 9, 405 (2013). [3] A. B. Bardon, S. Beattie, C. Luciuk, W. Cairncross, D. Fine, N. S. Cheng, G. J. A. Edge, E. Taylor, S. Zhang, S. Trotzky, and J. H. Thywissen, Science 344, 722 (2014). [4] S. Trotzky, S. Beattie, C. Luciuk, S. Smale, B. Bardon, A. T. Enss, E. Taylor, S. Zhang, and H. Thywissen, J. Phys. Rev. Lett. 114, 015301 (2015). [5] C. Deutsch, F. Ramirez-Martinez, C. Lacrouˆte, F. Reinhard, T. Schneider, J. N. Fuchs, F. Pi ́echon, F. Laloe ̈, J. Reichel, and P. Rosenbusch, Phys. Rev. Lett. 105, 020401 (2010). [6] H. J. Lewandowski, D. M. Harber, D. L. Whitaker, and E. A. Cornell, Phys. Rev. Lett. 88, 070403 (2002). [7] X. Du, L. Luo, B. Clancy, and J. E. Thomas, Phys. Rev. Lett. 101, 150401 (2008). [8] X. Du, Y. Zhang, J. Petricka, and J. E. Thomas, Phys. Rev. Lett. 103, 010401 (2009).
[9] J. N. Fuchs, D. M. Gangardt, and F. Laloe ̈, Phys. Rev. Lett. 88, 230404 (2002). [10] J. E. Williams, T. Nikuni, and C. W. Clark, Phys. Rev. Lett. 88, 230405 (2002). [11] A. S. Bradley and C. W. Gardiner, Journal of Physics B: Atomic, Molecular and Optical Physics 35, 4299 (2002). [12] S. S. Natu and E. J. Mueller, Phys. Rev. A 79, 051601 (2009). [13] U. Ebling, A. Eckardt, and M. Lewenstein, Phys. Rev. A 84, 063607 (2011). [14] G. M. Bruun, New Journal of Physics 13, 035005 (2011). [15] F. Pie ́chon, J. N. Fuchs, and F. Laloe ̈, Phys. Rev. Lett. 102, 215301 (2009). [16] J. Xu, Q. Gu, and E. J. Mueller, Phys. Rev. A 91, 043613 (2015). [17] O. Goulko, F. Chevy, and C. Lobo, Phys. Rev. Lett. 111, 190402 (2013). [18] T. Enss, Phys. Rev. A 91, 023614 (2015). [19] M. O. Oktel and L. S. Levitov, Phys. Rev. Lett. 88, 230403 (2002). [20] K. Gibble, Physical Review Letters 103, 113202 (2009). [21] A. M. Rey and A. V. Gorshkov and C. Rubbo, Phys. Rev. Lett. 103, 260402 (2009). [22] Z. H. Yu and C. J. Pethick, Phys. Rev. Lett. 104, 010801 (2010). [23] E. Hazlett, Y. Zhang, R. Stites, K. Gibble, and K. M. O’Hara, Phys. Rev. Lett. 110, 160801 (2013). [24] A. P. Koller, M. Beverland, A. V. Gorshkov, and A. M. Rey, Phys. Rev. Lett. 112, 123001 (2014). [25] M. E. Beverland, G. Alagic, M. J. Martin, A. P. Koller, A. M. Rey, and A. V. Gorshkov, arXiv:1409.3234 (20014). [26] M. D. Swallows, M. Bishof, Y. G. Lin, S. Blatt, M. J. Martin, A. M. Rey, and J. Ye, Science 331, 1043 (2011). [27] W. Maineult, C. Deutsch, K. Gibble, J. Reichel, and P. Rosenbusch, Phys. Rev. Lett. 109, 020407 (2012). [28] M. J. Martin, M. Bishof, M. D. Swallows, X. Zhang, C. Benko, J. von Stecher, A. V. Gorshkov, A. M. Rey, and J. Ye, Science 341, 632 (2013). [29] H. Pechkis, J. Wrubel, A. Schwettmann, P. Griffin, R. Barnett, E. Tiesinga, and P. Lett, Phys. Rev. Lett. 111, 025301 (2013). [30] B. Yan, S. A. Moses, B. Gadway, J. P. Covey, K. R. A. Hazzard, A. M. Rey, D. S. Jin, and J. Ye, Nature 501, 521 (2013). [31] A. Sommer, M. Ku, G. Roati, and M. W. Zwierlein, Nature 472, 201 (2011). [32] P. Makotyn, C. E. Klauss, D. L. Goldberger, E. Cornell, and D. S. Jin, Nature Physics 10, 116 (2014). [33] U. Schollwo ̈ck, Annals of Physics 326, 96 (2011), january 2011 Special Issue. [34] A. Polkovnikov, Annals of Physics 325, 1790 (2010). [35] J. Schachenmayer, A. Pikovski, and A. M. Rey, Phys. Rev. X 5, 011022 (2015). [36] L. Pucci, A. Roy, and M. Kastner, arXiv:1510.03768 (20015). [37] G. G. Emch, Journal of Mathematical Physics 7, (1966). [38] C. Radin, Journal of Mathematical Physics 11, (1970). [39] M. Kastner, Phys. Rev. Lett. 106, 130601 (2011). [40] M. Foss-Feig, K. R. A. Hazzard, J. J. Bollinger, and A. M. Rey, Phys. Rev. A 87, 042101 (2013). [41] The matrix product state studies of the main text were performed using extensions of the open source MPS library [64, 65], and are described further in the supplement [44].


 6
[42] A. P. Koller, J. Mundinger, M. L. Wall, and A. M. Rey, Phys. Rev. A 92, 033608 (2015). [43] The initial 2N spin-independent populated modes (0, ..., N − 1 for both spin-up and spin-down) are projected onto 2N ̃ modes, where the N ̃ modes for spin up are different than the N ̃ for spin down, and N ̃ is chosen such that the initial state is reproduced to an error of 10−16 in the norm. [44] See supplemental material for “Dynamics of interacting fermions in spin-dependent potentials,” which includes Refs. [64-69]. [45] All simulations displayed in figures in the main text are for N = 10 except for those in Fig. 3(b-d). [46] A. M. Rey, L. Jiang, M. Fleischhauer, E. Demler, and M. D. Lukin, Phys. Rev. A 77, 052305 (2008). [47] K. R. A. Hazzard, M. van den Worm, M. Foss-Feig, S. R. Manmana, E. G. Dalla Torre, T. Pfau, M. Kastner, and A. M. Rey, Phys. Rev. A 90, 063622 (2014). [48] We note that the spin echo pulse applied in Refs. [2, 3] modifies the single-particle physics [42], but does not affect the interaction-induced collective demagnetization. [49] The asymptotic value of the spin density imbalance is chosen to be 0.4, which matches the experimental values from 500-1000ms. Relaxation due to other decoherence mechanisms occurs at ∼2s. [50] V. Vedral, Open Physics 1, 289 (2003). [51] S. Clark, C. M. Alves, and D. Jaksch, New Journal of Physics 7, 124 (2005). [52] P. Hauke and L. Tagliacozzo, Physical review letters 111, 207202 (2013). [53] J. Schachenmayer, B. Lanyon, C. Roos, and A. Daley, Physical Review X 3, 031015 (2013).
[54] J. Eisert, M. van den Worm, S. R. Manmana, and M. Kastner, Physical review letters 111, 260401 (2013). [55] Z.-X. Gong, M. Foss-Feig, S. Michalakis, and A. V. Gorshkov, Physical review letters 113, 030602 (2014). [56] P. Richerme, Z.-X. Gong, A. Lee, C. Senko, J. Smith, M. Foss-Feig, S. Michalakis, A. V. Gorshkov, and C. Monroe, Nature 511, 198 (2014). [57] M. Kitagawa and M. Ueda, Physical Review A 47, 5138 (1993). [58] T. Opatrn`y and K. Mølmer, Physical Review A 86, 023845 (2012). [59] E. Lieb and R. D., Commun. Math. Phys. 28, 251 (1972). [60] B. Nachtergaele, Y. Ogata, and R. Sims, Journal of statistical physics 124, 1 (2006). [61] M. Cheneau, P. Barmettler, D. Poletti, M. Endres, P. Schauß, T. Fukuhara, C. Gross, I. Bloch, C. Kollath, and S. Kuhr, Nature 481, 484 (2012). [62] J. Schachenmayer, A. Pikovski, and A. M. Rey, New Journal of Physics 17, 065009 (2015). [63] D. Niroomand, S. D. Graham, and J. M. McGuirk, Phys. Rev. Lett. 115, 075302 (2015). [64] Open Source MPS, http://sourceforge.net/projects/openmps/. [65] M. L. Wall and L. D. Carr, New Journal of Physics 14, 125015 (2012). [66] J. S. Krauser, U. Ebling, N. Flschner, J. Heinze, K. Sengstock, M. Lewenstein, A. Eckardt, and C. Becker, Science 343, 157 (2014). [67] M. P. Zaletel, R. S. K. Mong, C. Karrasch, J. E. Moore, and F. Pollmann, Phys. Rev. B 91, 165112 (2015). [68] G. M. Crosswhite, A. C. Doherty, and G. Vidal, Phys. Rev. B 78, 035116 (2008). [69] B. Pirvu, V. Murg, J. I. Cirac, and F. Verstraete, New Journal of Physics 12, 025012 (2010).
