# Interaction quench in the Hubbard model: Relaxation of the spectral function and the optical conductivity - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevB.81.115131
> Collected: 2026-09-20
> Published: 2010-03-22
> Zotero parent key: Y5N3NE3E
> Evidence: Zotero indexed PDF text

arXiv:0910.5674v1 [cond-mat.str-el] 29 Oct 2009
Interaction quench in the Hubbard model: Relaxation of the spectral function and the optical conductivity
Martin Eckstein,1 Marcus Kollar,2 and Philipp Werner1
1Theoretical Physics, ETH Zurich, 8093 Zurich, Switzerland 2Theoretical Physics III, Center for Electronic Correlations and Magnetism, Institute for Physics, University of Augsburg, 86135 Augsburg, Germany (Dated: August 10, 2018)
We use non-equilibrium dynamical mean-field theory in combination with a recently developed Quantum Monte Carlo impurity solver to study the real-time dynamics of a Hubbard model which is driven out of equilibrium by a sudden increase in the on-site repulsion U . We discuss the implementation of the self-consistency procedure and some important technical improvements of the QMC method. The exact numerical solution is compared to iterated perturbation theory, which is found to produce accurate results only for weak interaction or short times. Furthermore we calculate the spectral functions and the optical conductivity from a Fourier transform on the finite Keldysh contour, for which the numerically accessible timescales allow to resolve the formation of Hubbard bands and a gap in the strongly interacting regime. The spectral function, and all one-particle quantities that can be calculated from it, thermalize rapidly at the transition between qualitatively different weak- and strong-coupling relaxation regimes.
PACS numbers: 67.40.Fd, 71.10.Fd, 05.10.Ln
I. INTRODUCTION
The recent realization of a Mott insulating state of repulsively interacting fermions in trapped ultracold atoms1,2 opens the door to controlled studies of the nonequilibrium properties of fermionic lattice models. At the same time, the relaxation dynamics of strongly correlated electron systems is starting to be explored experimentally through femtosecond spectroscopy.3,4,5,6 Dynamical mean-field theory7 (DMFT) is a promising tool to approach these challenging issues from the theoretical side. The DMFT formalism is based on the mapping of a lattice model to a quantum impurity model. This approximation is based on a purely spatial argument which becomes exact in the limit of infinite dimensions.8 On the one hand this fact makes DMFT a nonperturbative method which can capture, e.g., the local Mott physics of the Hubbard model. On the other hand, it implies that DMFT can be formulated equally well in imaginary and real time, and hence the method can be applied to both equilibrium and nonequilibrium situations.9 A number of authors have employed the nonequilibrium DMFT framework to study dynamical properties of the Falicov-Kimball model, which is a variant of the Hubbard model in which only one spin species can hop between lattice sites. Despite this simplification, the Falicov-Kimball model exhibits a relatively rich phase diagram with metallic, Mott-insulating, and charge-ordered phases.10 Its most attractive feature in the present context is that the associated quantum impurity model in DMFT can be solved analytically or numerically by simple means,11 which provides reliable access to the long-time dynamics. Both the transient dynamics after the sudden switching-on of a static electric field12,13,14 and, using a combined Floquet and DMFT formalism, the non-equilibrium steady state in the pres
ence of an alternating or constant field15,16,17 were calculated. The evolution of the momentum distribution and double occupation after an interaction quench, i.e., a sudden change in the interaction parameter, was studied in Ref. 18, where it was also shown that for the FalicovKimball model these quantities do not thermalize. This is a consequence of the immobility of one spin species and the resulting quadratic form of the Hamiltonian for the mobile other spin species. A more realistic model for the description of correlated electron systems and interacting fermions in optical lattices is the Hubbard model,
H(t) = ∑
ijσ
Vij c†
iσcjσ + U (t) ∑
i
(ni↑ − 1
2
)(ni↓ − 1
2
), (1)
which describes fermions of spin one half which hop on a lattice with hopping amplitude Vij and interact on each site with a repulsion energy U . An interaction quench has so far been experimentally realized in the bosonic version of the Hubbard model.19 To describe the corresponding situation in the fermionic model, we allow for a timedependent interaction U (t) in Eq. (1). Even after the mapping to a single-site model, the solution of the Hubbard model within nonequilibrium DMFT requires the calculation of the time evolution of an interacting many-body system. In a previous publication20 we employed a recently developed diagrammatic impurity solver21 to compute the time evolution after an interaction quench over a wide parameter regime within DMFT. The numerical simulations confirmed an analytical flow equation analysis for quenches to small U ,22 which showed that in the limit U → 0 the system is trapped in a nonthermal metastable intermediate state, a phenomenon known as prethermalization.23 We identified a similar trapping phenomenon for quenches to very large interactions. Most interestingly, these two prether


 2
malization regimes are separated by a well-defined “critical” interaction Udyn, where instead of a trapping in either of the nonthermal states a fast thermalization is observed. In Ref. 20 these qualitatively different regimes were demonstrated on the basis of an analysis of the momentum distribution and the double occupancy. Relaxation to a thermal state is often difficult to establish numerically because the time evolution must be studied on long timescales. In general thermalization is expected for interacting systems (in the weak sense that the expectation value of a large class of observables approaches the thermal expectation value in the longtime limit). In exactly solvable systems, however, thermalization is often prevented by integrability,18,24,25,26 while its mechanism for nonintegrable systems is currently under debate.27,28,29,30,31,32 The existence of two separate relaxation regimes is similar to what was found for Heisenberg spin chains33 and the one-dimensional Bose-Hubbard model.34 The purpose of the present work is twofold: First, we want to explain in some detail the machinery behind our Quantum Monte Carlo (QMC) calculation of the Hubbard model in nonequilibrium DMFT. We will briefly review the DMFT formalism (Sec. II) and the diagrammatic Monte Carlo method (Sec. III), discuss some important tricks which improve the efficiency of the Monte Carlo sampling, and then present in detail the solution of the DMFT self-consistency equations based on the exact equation of motion approach (Sec. IV). The QMC solution of DMFT is finally used to discuss the validity of the nonequilibrium generalization of the iterated perturbation theory (Sec. V). The second purpose of this paper is to further analyze the main finding of Ref. 20, namely a fast thermalization after a quench from U = 0 to Udyn, with additional data for the momentum distribution, the spectral function, and the optical conductivity (Sec. VI). In particular we find that at Udyn the retarded non-equilibrium Green function relaxes to the appropriate equilibrium Green function within the numerical accuracy, establishing thermalization of all oneparticle quantities that can be calculated from it.
II. NONEQUILIBRIUM DMFT
A. Contour-ordered Green functions
In the following section we set up the framework for the investigation of a rather general class of nonequilibrium situations. We assume that the system of interest is initially prepared in thermal equilibrium. For times t > 0 it is then acted on by some perturbation, but there is no coupling to external heat or particle reservoirs. Technically, this setup implies that the time evolution is unitary and captured by a time-dependent Hamiltonian, but all results must be averaged over initial states according to the grand-canonical density matrix ρ0 =
e−βH(0)/Tr[e−βH(0)] at temperature T = 1/β. The con
max
s
2 s3
t
t3
t2
t1 s1
t
5 s5 t4 s4
ts
ts
66
77
0
−iβ
FIG. 1: The L-shaped contour C for the description of transient nonequilibrium states with initial state density matrix
∝ e−βH(0). Arrows show a possible Monte Carlo configuration corresponding to perturbation order n = 7 and n+ = 3, n
− = 2, nβ = 2 (cf. Sec. III).
ventional approach to this kind of nonequilibrium situation within many-body theory is based on the use of contour-ordered Keldysh Green functions,35
Gαα′ (t, t′) = −i〈TC cˆα(t)cˆ†
α′ (t′)〉 , (2)
where the time arguments t and t′ lie on the L-shaped contour C that runs from 0 to some time tmax (i.e., the largest time of interest) on the real time axis, back to 0, and finally to −iβ along the imaginary time axis (Fig. 1). Here and in the following, operators with hat are in Heisenberg notation with respect to the time-dependent Hamiltonian [on the imaginary branch, H = H(0), and cˆ(−iτ ) = eτH(0)ce−τH(0)], and 〈·〉 = Tr[ρ0·] is the expectation value taken in the initial equilibrium state. The contour-ordering TC exchanges the order of two operators A(t1) and B(t2) in a product A(t1)B(t2) if and only if t2 appears later on the contour than t1, with an additional minus sign if the exchange involves an odd number of Fermi operators. The order of time arguments along C is indicated by the arrow in Fig. 1, which points from “earlier” to “later” times. Contour-ordered Green functions were first introduced by Keldysh36 in order to generalize Wick’s theorem and diagrammatic perturbation theory to nonequilibrium physics. The extension of the original Keldysh formalism to the L-shaped contour C, which has numerous applications in nonequilibrium many-body theory,37 becomes important whenever correlations between the initial state at t = 0 and time t > 0 cannot be neglected.38,39 The contour-ordered Green function (2) is related to a number of real and imaginary-time Green functions, which we list in the following paragraph for later reference. When both time arguments are on the imaginary branch, Eq. (2) reduces to the Matsubara Green function of the initial equilibrium state,
G
M
αα′ (τ, τ ′) = Gαα′ (−iτ, −iτ ′). (3)
Because the Hamiltonian is constant on the vertical branch of C and commutes with the initial state density


 3
matrix, GM
αα′ (τ, τ ′) is translationally invariant in imagi
nary time, such that we can introduce the usual Matsubara frequency representation,
G
M(τ, τ ′) = i
β
∑
n
eiωn(τ ′−τ )gM(iωn), (4a)
g
M(iωn) = −i
β
∫
0
dτ eiωnτ GM(τ, 0). (4b)
On the other hand, when both time arguments are real, one obtains the lesser, retarded, and advanced Green functions,
Gα<α′ (t, t′) ≡ Gαα′ (t+, t′−) = i〈cˆ†
α′ (t′)cˆα(t)〉0 (5)
GαRα′ (t, t′) ≡ Θ(t − t′)[Gαα′ (t−, t′+) − Gαα′ (t+, t′−)]
= −iΘ(t − t′)〈{cˆ†
α′ (t′), cˆα(t)}〉, (6)
GαAα′ (t, t′) ≡ Θ(t′ − t)[Gαα′ (t+, t′−) − Gαα′ (t−, t′+)]
= iΘ(t′ − t)〈{cˆ†
α′ (t′), cˆα(t)}〉. (7)
The subscript of each real time-argument indicates whether it is on the upper (+) or lower (−) real-time branch of C. The lesser Green function is related to the occupation of states α, to which its imaginary part reduces for t = t′ and α = α′. On the other hand, the retarded and advanced Green function are related to the spectral function, which will be discussed in more detail in Sec. VI. In addition to the real and imaginary time Green functions, the Green functions
Gα¬α′ (t, τ ) ≡ Gαα′ (t±, −iτ ), (8a)
G
¬
αα′ (τ, t) ≡ Gαα′ (−iτ, t±). (8b)
with mixed time arguments encode the correlations between the initial state and times t > 0. It follows from the cyclic property of the trace and the definition of the contour-ordering that the Green function (2) satisfies an antiperiodic boundary condition on C in both time-arguments,
Gαα′ (0+, t′) = −Gαα′ (−iβ, t′), (9a) Gαα′ (t, 0+) = −Gαα′ (t, −iβ). (9b)
This boundary condition holds for all contour functions in this text, including those which have no simple definition in terms of Heisenberg operators. Furthermore, the Green function (2) satisfies the hermitian symmetry
GαRα′ (t, t′) = GαA′α(t′, t)∗ (10a)
Gα<α′ (t, t′) = −Gα<′α(t′, t)∗ (10b)
Gα¬α′ (t, τ ) = G
¬
α′α(β − τ, t)∗, (10c)
which will be used frequently in the following.
B. Dynamical mean-field theory
In equilibrium DMFT local correlation functions are obtained from a single-site impurity model subject to
a self-consistency condition.7 The mapping of the lattice problem (1) onto the single-site problem is formally achieved by integrating out all lattice sites apart from one. A straightforward reformulation of this mapping for Green functions on the Keldysh contour9,12 makes DMFT applicable to nonequilibrium problems. The single-site action is then given by
S = S0 +
∫
C
dt hloc(t), (11a)
S0 = ∑
σ=↑,↓
∫
C
dt dt′ c†σ(t)Λσ(t, t′)cσ(t′), (11b)
where ∫
C dt = ∫ tmax
0 dt+−∫ tmax
0 dt−− i ∫ β
0 dτ is the integral
along C,
hloc(t) = U (t)(n↑ − 1
2
)(n↓ − 1
2
) (12)
is the local interaction of the Hamiltonian, and S0 describes the hybridization of the site with an environment that is determined self-consistently by the DMFT procedure. In the following we consider only homogeneous paramagnetic phases, such that Λσ does not depend on the lattice site or spin σ. The local Green function for action (11) is given by
Gσ(t, t′) = −i〈cσ(t)c†σ(t′)〉S , (13)
where operators without a hat are in the interaction picture with respect to μ(n↑ + n↓), and the notation
〈 · · · 〉S = Tr[e−βμ(n↑+n↓)TC exp(−iS) · · · ]
Tr[e−βμ(n↑+n↓)TC exp(−iS)] (14)
is used. In general, the computation of Gσ(t, t′) is a complicated nonequilibrium many-body problem. For this reason, nonequilibrium DMFT has so far been applied mostly to the Falicov-Kimball model, where the single-site problem can be reduced to a quadratic one and thus becomes exactly solvable either numerically12,14 or analytically.18 In the present paper, just as in Ref. 20, we investigate the Hubbard model and solve the singlesite problem using the weak-coupling continuous time Monte Carlo algorithm,21 which will be described below (Sec. III). The local self-energy is then defined by the Dyson equation
[(G0−,1σ − Σσ) ∗ Gσ](t, t′) = δC(t, t′), (15)
where the noninteracting (U = 0) single-site Green function and its inverse are given by
G0,σ(t, t′) = −i〈cσ(t)c†σ(t′)〉S0 , (16a)
G0−,1σ(t, t′) = δC(t, t′)(i∂t + μ) − Λσ(t, t′), (16b)
respectively. Here we introduced the notation [a ∗ b](t, t′) =
∫
C dt ̄a(t, t ̄) b(t ̄, t′) for the convolution of two contour


 4
functions, and the contour-delta function δC(t, t′) is defined such that
∫
C
dt ̄f (t ̄)δC(t ̄, t) = f (t) (17)
for any contour function f , i.e., δC(t, t′) = ±δ(t − t′) if
t and t′ both on the upper or lower real branch of C, and δC(−iτ, −iτ ′) = iδ(τ − τ ′) for time arguments on the vertical branch. Both the Dyson equation (15) and the corresponding equation
[G0−,1σ ∗ G0,σ](t, t′) = δC(t, t′), (18)
for G0,σ are inhomogeneous integro-differential equations on the contour C when Eq. (16a) is inserted. They have a unique solution because G0,σ and G satisfy the boundary condition (9). The solution of such integral equations on C is discussed in detail in Sec. IV. In order to determine the hybridization function Λσ(t, t′) one must equate the self-energy Σσ(t, t′) and the
Green function Gσ(t, t′) of the single-site problem with
the local self-energy Σjjσ(t, t′) and the local Green func
tion Gjjσ (t, t′) of the lattice problem at the given site j, respectively,
Gjjσ (t, t′) = Gσ(t, t′), Σijσ(t, t′) = δij Σσ(t, t′). (19)
The latter two are related by the lattice Dyson equation,
(i∂t + μ − ǫk)Gkσ(t, t′) − [Σσ ∗ Gkσ](t, t′) = δC(t, t′), (20)
which is stated here for the homogeneous case after Fourier transform with respect to lattice sites. In Eq. (20),
G
kσ(t, t′) = −i〈TCcˆkσ(t)cˆ†
kσ(t′)〉 (21)
is the momentum-resolved lattice Green function. (For a Bravais lattice, k are quasimomenta and ǫk are band energies, but more generally, 〈i|k〉 and ǫk are eigenvectors and eigenvalues of the hopping matrix Vij , respectively.) The local Green function is given by the momentum sum
Gσ(t, t′) = ∑
k
|〈j|kσ〉|2Gkσ(t, t′), (22)
which closes the self-consistency. In the present paper we consider the case of a timedependent interaction but no external fields. The hopping matrix elements are then independent of time, and the k-summation in Eq. (22) can be reduced to an integral over a single energy variable
Gσ(t, t′) =
∫
dǫ ρ(ǫ)Gǫσ(t, t′), (23)
involving the Green function Gǫσ(t, t′) = Gkσ(t, t′)|ǫkσ=ǫ and the local density of states ρ(ǫ) = ∑
k |〈j|k〉|2δ(ǫ −
ǫ
k) at an arbitrary site j. For the case of a semielliptic density of states,
ρ(ǫ) =
√4V 2 − ǫ2
2πV , (24)
with quarter bandwidth V , which corresponds to nearestneighbor hopping on the Bethe lattice7,40 or a particular kind of long-range hopping on the hypercubic lattice,41 one obtains a closed form expression for the Weiss field,18
Λσ(t, t′) = V 2Gσ(t, t′). (25)
We will use this self-consistency equation for all results of this work, so that the solution of the DMFT equations is achieved by iteration of Eqs. (13) and (25).
III. REAL-TIME MONTE CARLO METHOD
The real-time evolution of the impurity model can be computed using the weak-coupling diagrammatic Monte Carlo method. More specifically, we employed the realtime version of the continuous-time auxiliary field algorithm (CTAUX)42 which was discussed in detail in Ref. 21. In the following section we present the implementation of this algorithm on the L-shaped contour (Fig. 1) and then discuss some technical aspects which improve the efficiency of the method to the point where relevant timescales even in the strong-coupling regime become accessible. We start by expressing the partition function of the initial state as
Z = Tr[e−βμ(n↑+n↓)TCe−iS ]
= e−βU/4−i R
C dtk(t)Tr[e−βμ(n↑+n↓)TCe−iSk ] (26)
with Sk = S − ∫
C dt(k(t) + U/4) and k(t) 6= 0. This (pos
sibly time-dependent) shift in the action is introduced so that the interaction term can be decoupled using auxiliary Ising spin variables according to43
− hloc(t) + k(t) + U/4 = k(t) − U (n↑n↓ − (n↑ + n↓)/2))
= k(t)/2 ∑
s=−1,1
eγ (t)s(n↑ −n↓ ) ,
cosh(γ(t)) = 1 + U/(2k(t)). (27)
Expansion of e−iSk in powers of (hloc(t) − k(t) − U/4) and subsequent auxiliary field decomposition leads to an expression of the partition function as a sum over all possible Ising spin configurations on the contour C. The weight of the Monte Carlo configurations {(t1, s1), (t2, s2), . . . (tn, sn)} (see illustration in Fig. 1) is obtained by evaluating the trace of the remaining noninteracting problem,


 5
w({(t1, s1), . . . (tn, sn)}) = (ik(t1)dt/2) . . . (ik(tn+ )dt/2)(−ik(tn++1)dt/2) . . . (−ik(tn++n− )dt/2)
×(k(tn++n−+1)dτ /2) . . . (k(tn++n−+nβ )dτ /2) ∏
σ
det Nσ−1, (28)
Nσ−1 = eΓσ − iG0,σ(eΓσ − I). (29)
Here n± and nβ denotes the number of Ising spins on the three branches of C, G0,σ is the (n++n−+nβ)×(n++n−+ nβ) matrix of bath Green functions (16a) evaluated at the
time arguments defined by the Ising spins, and eΓσ = diag(eγ(t1)s1σ, . . . , eγ(tn)snσ). A Monte Carlo sampling of all possible spin configurations can then be implemented based on the absolute value of these weights. The contribution of a specific configuration c to the Green function is given by
Gcσ(t, t′) = G0,σ(t, t′)
+i
n
∑
i,j=1
G0,σ(t, ti)[(eΓσ − 1)Nσ]i,j G0,σ(tj , t′),
(30)
so the Green function G is obtained as the Monte Carlo average of Gc. The sign problem in this method grows exponentially with the average perturbation order on the real-time portion of C. To reach long times or strong interactions, it is therefore important to reduce this perturbation order as much as possible. In the particle-hole symmetric case, i.e., at half-filling and for a symmetric density of states, the parameter k(t) of the algorithm can be chosen such that only even perturbation orders appear in the expansion. In fact, for
k(t) = −U/4 (31)
we have γ(t) = iπ, eγ(t)sσ = −1 and hence the spin degree of freedom effectively disappears. The algorithm then becomes the real-time version of Rubtsov’s weakcoupling method44 for the particle-hole symmetric inter
action term hloc(t) = U (n↑ − 1
2 )(n↓ − 1
2 ) with weight
weven(t1, . . . , tn) = (−iU dt)n+ (iU dt)n− (−U dτ )nβ
×
∏
σ
det
(
iG0,σ − 1
2I
)
. (32)
(For a detailed discussion of the equivalence between the Rubtsov and CTAUX methods for the Anderson impurity model, see Ref. 45). The above choice of k(t) requires the implementation of Monte Carlo updates which change the perturbation order from n to n ± 2. We found, however, that the odd perturbation orders are continuously suppressed as k(t) approaches −U/4, so one may as well choose k(t) = −U/4 + δ (with small δ) in combination with rank one updates. The efficiency of the Green function measurement can be improved dramatically by the following simple tricks. First, we rewrite Eq. (30) as
Gcσ(t, t′) = G0,σ(t, t′) +
∫
C
ds1
∫
C
ds2G0,σ(t, s1)
〈
i
n
∑
i,j=1
δC(s1, ti)[(eΓσ − 1)Nσ]i,j δC(s2, tj )
〉
mcG0,σ(s2, t′), (33)
where the variables s1 and s2 run over the contour C, and 〈·〉mc denotes the Monte Carlo averaging. It is therefore sufficient to accumulate the impurity system T -matrix
Xσ(s1, s2) =
〈
i
n
∑
i,j=1
δC(s1, ti)[(eΓσ −1)Nσ]i,j δC(s2, tj )
〉
mc,
(34) as mentioned in Ref. 42. While the measurement of X on some fine grid introduces discretization errors, these can be made negligibly small at essentially no computational
cost. Furthermore, comparison of Eq. (33) to the Dyson equation (15) shows that X is related to the self-energy by
X ∗ G0 = Σ ∗ G, (35)
so the measurement of X allows to extract Σ as explained in Section IV C. Further improvements are possible. Assuming that the perturbation order on the real-time branch is non-zero, it follows from Eq. (28) that the weight of the Monte Carlo


 6
configuration changes sign if the last spin (corresponding to the largest time argument) is shifted from the forward contour to the backward contour or vice versa. Since the absolute value of the weight does not change, these two configurations will be generated with equal probability. As a result, all terms in Eq. (34) which do not involve the last operator on the contour will cancel on average. It is therefore more efficient to accumulate only the contributions to Eq. (34) from those pairs (i, j) in which either i or j corresponds to the last operator on the real-time branch. (If all spins sit on the imaginary-time branch, no such simplification is possible.) We also note that the error bars on measurements can be substantially reduced by appropriate symmetrizations of the real and imaginary parts of X (symmetry lines s1 = tmax, s2 = tmax, s1 = s2).
IV. WEAK-COUPLING CTQMC + DMFT
To use the weak-coupling CTQMC as an impurity solver within DMFT, we iterate the following two steps until convergence: (i) The local Green function Gσ(t, t′) is determined in CTQMC [Eq. (33)], using the noninteracting bath Green function G0,σ(t, t′) as input, and (ii),
G0,σ(t, t′) is determined from its inverse (16b), using the
QMC output Gσ(t, t′) and the self-consistency Eq. (25).
We start the iteration from an initial guess for G0,σ(t, t′), for which we usually take the noninteracting equilibrium Green function,
Geσq(t, t′) = i
∫
dǫ ρ(ǫ)eiǫ(t′−t)[f (ǫ) − ΘC(t, t′)], (36)
where ΘC(t, t′) = 1 if t is later on the contour than t′ and otherwise zero. In this section we describe in detail how G0,σ is determined from Λσ (Sec. IV A), how the self-energy is calculated from the impurity correlation function Xσ after convergence of the DMFT iteration (Sec. IV B), and how one finally obtains expectation values of various observables of the lattice system (Sec. IV C). Furthermore, we introduce a real frequency representation which is needed to efficiently treat the case of zero temperature on the Lshaped contour (Sec. IV D), and combine this with the weak-coupling impurity solver for the case of a noninteracting initial state.
A. Integral equations on the contour C
Within nonequilibrium DMFT one must frequently solve equations on C of the type
[i∂t − h(t)]Y (t, t′) − [K ∗ Y ](t, t′) = δC(t, t′) (37)
with a known integral kernel K(t, t′). The solution Y (t, t′) is unique when the antiperiodic boundary condition (9) is imposed on Y (t, t′). For example, both
Eq. (18) for the noninteracting bath Green function G0,σ(t, t′) and Eq. (20) for the momentum-resolved Green function have this form. By choosing a suitable discretization of the contour C, Eq. (37) can in principle be reduced to the inversion of a matrix whose dimension is given by the number of mesh points along C.13 In the following we pursue a different approach, where both Y and K in Eq. (37) are first represented in terms of their respective real and imaginary time components (3)-(8), and separate integral equations (which are similar to the Kadanoff-Baym equations35) are solved for each component. Although this procedure may seem rather cumbersome compared to direct contour discretization, it has several advantages: (i) It is straightforward to incorporate the hermitian symmetry (10) which is satisfied by both the local self-energy and the hybridization function Λσ. (ii) The resulting equations are Volterra type integro-differential equations, for which highly stable and accurate algorithms can be found in the literature,46 and which remain causal even when they are approximated numerically. Finally, (iii), the real-frequency representation which we introduce in Sec. IV D to handle initial states at zero temperature is based on this approach. In the following we assume that Y and K satisfy the hermitian symmetry (10), such that it is sufficient to determine the Matsubara, retarded, mixed “¬”, and lesser components of Y . Corresponding components of the convolution K ∗Y in Eq. (37) are obtained from the Langreth rules,35 which follow directly from the definitions (3)-(8) and the definition of the contour integral. By taking the Matsubara component (3) of Eq. (37) we obtain
(−∂τ − h)Y M(τ, τ ′) + i
β
∫
0
dτ ̄KM(τ, τ ̄)Y M(τ ̄, τ ′) =
iδ(τ − τ ′), (38)
where h = h(0) is constant on the imaginary branch. This equation must be augmented with an antiperiodic boundary condition Y M(0, τ ′) = −Y M(β, τ ′) which follows from Eq. (9). When we assume that the kernel KM has the Matsubara frequency representation (4), it follows that the solution Y M(τ, τ ′) is of the same form, with
y
M(iωn) = [iωn − h − kM(iω)]−1. (39)
As required by causality, Y M thus turns out to depend only on the initial equilibrium state, independent of the subsequent perturbation of the system. In a similar fashion, the retarded component (6) of Eq. (37) is given by
[i∂t − h(t)]Y R(t, t′) −
t
∫
t′
dt ̄KR(t, t ̄)Y R(t ̄, t′) = δ(t − t′).
(40)


 7
Because Y R(t, t′) vanishes for t < t′ by definition [cf. Eq. (6)], integration over the δ-function yields
Y R(t, t) = −i. (41)
One can thus restrict the solution of Eq. (40) to t > t′, drop the δ-function on the right-hand side and instead impose (41) as an initial condition. The limits of the integral in (40) take into account that retarded functions vanish for t > t′. This fact turns Eq. (40) into a Volterra equation of second kind,46 i.e., the derivative at time t is determined by the kernel and the function at earlier times only. The numerical solution of this type of equations is analogous to the solution of ordinary differential equations.46 For the Green functions (8) with mixed time arguments, Eq. (37) reads
[i∂t − h(t)]Y ¬(t, τ ) −
t
∫
0
dt ̄KR(t, t ̄)Y ¬(t ̄, τ )
= −i
β
∫
0
dτ ̄ K¬(t, τ ̄)Y M(τ ̄, τ ) . (42)
We assume that Y is continuous on C (which is true if neither K(t, t′) nor h(t) are singular at t = 0), such that Eq. (42) must be solved with the initial condition
Y ¬(0, τ ) = Y M(0, τ ). For given τ , Eq. (42) is an inhomogeneous Volterra integro-differential equation, for which only known functions [cf. Eq. (39)] enter the source term on the right-hand side. A third and last Volterra integral equation can be derived for the lesser component (5),
[i∂t − h(t)]Y <(t, t′) −
t
∫
0
dt ̄KR(t, t ̄)Y <(t ̄, t′) =
−i
β
∫
0
dτ ̄K¬(t, τ ̄)Y
¬
(τ ̄, t′) +
t′
∫
0
dt ̄K<(t, t ̄)Y A(t ̄, t′). (43)
Due to the symmetry (10) it is sufficient to solve this equation for t < t′, with the initial condition Y <(0, t′) = −Y
¬
(β, t′). The latter follows from Eq. (9) and the continuity of Y along C. The functions Y A and Y
¬
which enter the source term of Eq. (43) on the right-hand side can be obtained from the previous solution of Eqs. (40) and (42), and the symmetry (10). The successive solution of Eqs. (38), (40), (42), and (43) completes the determination of the contour function Y .
B. Determination of the self-energy
The impurity self-energy can be obtained from the correlation function Xσ via Eq. (35). By comparison of
the Dyson equation (15) in integral form, Gσ = G0,σ + Gσ ∗ Σσ ∗ G0,σ, with Eq. (33), i.e., Gσ = G0,σ + G0,σ ∗ Xσ ∗ G0,σ, we find the relation
(1 + Xσ ∗ G0,σ) ∗ Σσ = Xσ. (44)
This equation is very similar to Eq. (37), with unknown Y = Σ, kernel K = Xσ ∗ G0,σ, h = 1, and without the differential term. The solution of (44) is thus analogous to Eq. (37), using a decomposition in terms of the components (3)-(5). The final equations read
Σ
M(tωn) = xM(iωn)
1 + kM(iωn) , (45a)
ΣR(t, t′) +
t
∫
t′
dt ̄KR(t, t ̄)ΣR(t ̄, t′) = XR(t, t′), (45b)
Σ¬(t, τ ) +
t
∫
0
dt ̄KR(t, t ̄)Σ¬(t ̄, τ ) = X¬(t, τ )+
i
β
∫
0
dτ ̄ K¬(t, τ ̄)ΣM(τ ̄, τ ) (45c)
Σ<(t, t′) +
t
∫
0
dt ̄KR(t, t ̄)Σ<(t ̄, t′) = Xσ<(t, t′)+
i
β
∫
0
dτ ̄K¬(t, τ ̄)Σ
¬
(τ ̄, t′)−
t′
∫
0
dt ̄K<(t, t ̄)ΣA(t ̄, t′). (45d)
Note that the kernel K = Xσ ∗ G0,σ does not satisfy the hermitian symmetry (10), i.e., Xσ ∗ G0,σ 6= G0,σ ∗ Xσ. We would like to remark that the self-energy can equally well be determined from the linear equation
Xσ ∗ Gσ0 = Σσ ∗ Gσ. (46)
However, Eqs. (45) are essentially Volterra integral equations of the second kind, while Eq. (46) leads to Volterra equations of the first kind, i.e., only the integral-term is present on the left-hand side. Because the numerical solution of Volterra equations of the first kind tends to be unstable46 we prefer the solution of Eq. (44) over Eq. (46).
C. Expectation values of observables
From the self-energy Σ one can directly compute the expectation values of observables of the lattice Hamiltonian. In this section we let 〈· · ·〉 denote the initial state expectation value at temperature T = 1/β, and operators with hat are in Heisenberg representation with respect to the Hubbard Hamiltonian (1) with time-dependent interaction. The number of lattice sites will be denoted by L.


 8
The particle number per site for spin σ is given by the local Green function Gσ(t, t′)
nσ(t) = 1
L
∑
j
〈cˆ†
jσ(t)cˆjσ(t)〉 = −iGσ<(t, t), (47)
provided that the state is homogeneous. Because nσ(t)
is conserved, the condition Gσ<(t, t) = const provides a
first test of the numerical accuracy. The occupation of the momentum states
n(ǫk, t) ≡ 〈cˆ†
kσ(t)cˆkσ(t)〉 = −iG<
kσ(t, t), (48)
is obtained from the momentum-resolved Green function G
kσ(t, t′) = −i〈TCcˆkσ(t)c†
kσ(t′)〉. For a momentum in
dependent Σσ, n(ǫk, t) depends on momentum k only
via the band-energy ǫk. The Green function Gkσ(t, t′) is determined from the lattice Dyson equation (20), whose solution is analogous to that of Eq. (37). The kinetic energy per lattice site
Ekin(t) = 1
L
∑
kσ
ǫ
k〈cˆ†
kσ(t)cˆk(t)〉, (49a)
is obtained from n(ǫ, t) by replacing the k-sum with an integral over the local density of states [Eq. (24)],
Ekin(t) =
∫
dǫ ρ(ǫ) ǫ n(ǫ, t). (49b)
Furthermore we are interested in the double occupation per lattice site
d(t) = 1
L
∑
i
〈ˆni↑(t)ˆni↓(t)〉, (50)
and the interaction energy
Epot ≡ U (t) ∑
i
〈(ˆni↑(t) − 1
2
)(ˆni↓(t) − 1
2
)〉 (51)
= U (t)[d(t) − 1
2 (n↑(t) + n↓(t)) + 1
4
]. (52)
To calculate this quantity we consider the equation of motion for the local lattice Green function Gjjσ , which reads
[(Gσ−1)jl ∗ Gljσ](t, t′) = δC(t, t′) + U (t)Γjσ(t, t′), (53)
(Gσ−1)jl(t, t′) = δC(t, t′)[δjl(i∂t + μ) − tjl], (54)
Γjσ(t, t′) = −i〈TCcˆiσ(t)(ˆniσ ̄ (t) − 1
2 )cˆ†
iσ(t′)〉. (55)
Comparison with the lattice Dyson equation in real space yields
U (t)Γjσ(t, t′) = [Σσ ∗ Gjjσ](t, t′), (56)
because the self-energy is local and site-independent. Hence Γσ ≡ Γjσ can be determined from quantities measured in the single-site problem [cf. Eq. (46)], and Eq. (55) implies
d(t) = −iΓi<σ(t, t) + 1
2 nσ(t) (57)
for a homogeneous state. Finally we can compute the total energy from Eqs. (49) and (51),
Etot(t) = Ekin(t) + Epot(t). (58)
This quantity must be constant when the Hamiltonian is time-independent, which provides a second test for the accuracy of the numerical solution.
D. Real-frequency representation
In this subsection we introduce a partial Fourier transform of the mixed components “¬” and “
¬
”, which will allow us to handle contour equations such as Eqs. (37) and (44) in the limit of zero temperature without dealing explicitly with a contour of infinite length. We start from the Fourier series in the interval 0 ≤ τ ≤ β,
Y
¬
(iωn, t) =
β
∫
0
dτ Y
¬
(τ, t)eiωnτ , (59a)
Y
¬
(τ, t) = 1
β
∑
n
Y
¬
(iωn, t)e−iωnτ , (59b)
in terms of fermionic Matsubara frequencies iωn. This representation is now used within the solution of Eq. (37). In contrast to Eq. (42), the corresponding equation for the mixed “
¬
” component
(−∂τ − h)Y
¬
(τ, t) + i
β
∫
0
dτ ̄ KM(τ, τ ̄)Y
¬
(τ ̄, t)
=
t
∫
0
dt ̄K
¬
(τ, t ̄)Y A(t ̄, t) (60)
is not an initial value problem, but rather a boundary value problem on C: The boundary condition Y
¬
(β, t) = −Y
¬
(0, t) − Y A(0, t) follows from Eqs. (9) and (7) and the continuity of the contour functions along C. Using the transformation (59) and Eq. (39) for the Matsubara component, Eq. (60) becomes an explicit integral expression for Y
¬
(iωn, t),
Y
¬
(iωn, t) =
y
M(iωn)
[
Y A(0, t) +
t
∫
0
dt ̄K
¬
(iωn, t ̄)Y A(t ̄, t)
]
. (61)
In the following we assume that K
¬
(iωn, t) can be continued to complex frequencies z, such that K
¬
(z, t) is analytic in the upper and lower complex half plane, respectively, and has a branch cut along the real frequency axis. For the Green function (2) this property follows


 9
from a Lehmann representation in terms of an eigenbasis {|n〉} of H(0),
G
¬
αα′ (z, t) = i ∑
nm
(wn +wm)〈n|cα|m〉〈m|c†
α′ (t)|n〉 z + En − Em
, (62)
which has poles on the real axis only (wn = e−βEn). When Eq. (61) is continued to the real axis, we obtain two functions Y
¬
(ω±, t), where ω± = ω ± iη for η → 0+. In contrast to the equilibrium functions yM(ω±), the two functions Y
¬
(ω±, t) are not simply related by complex conjugation. Matsubara summations are then transformed into integrals along the branch cut of Y
¬
(z, t) in the usual way. For example, the backtransformation (59b) is given by
Y
¬
(τ, t) =
∫ dω
2πi f (ω)eωτ [Y
¬
(ω−, t) − Y
¬
(ω+, t)], (63)
where f (ω) = 1/(e−βω + 1) is the Fermi function. Using the real frequency representation for the mixed components, the first source term on the right hand side of Eq. (43) can be rewritten in terms of the previously determined functions Y
¬
(ω±, t)
β
∫
0
dτ ̄ K¬(t, τ ̄)Y
¬
(τ ̄, t) =
∫ dω
2πi f (ω) ×
[K¬(t, ω+)Y
¬
(ω+, t′) − K¬(t, ω−)Y
¬
(ω−, t′)]. (64)
Here the Fourier transformation (59a) with opposite sign for iωn is used in the second time argument for the ¬ Green functions (8a), such that
Y
¬
(z, t) = −Y ¬(t, z∗)∗ (65)
follows by symmetry (10c). The above real-frequency representation can be used within DMFT whenever the impurity problem is solvable at zero temperature. This is the case for approximate analytical methods (Sec. V). It might also be of advantage for arbitrary initial states in the Falicov-Kimball model,13,18 where the solution of the impurity is based on the solution of equations of motion which have exactly the structure of Eq. (37). In the following section we present another application, namely nonequilibrium DMFT for the Hubbard model with a noninteracting initial state.
E. CTQMC and DMFT for noninteracting initial states
The computational scheme for the solution of the nonequilibrium DMFT equations is represented in Fig. 2 for a semielliptic density of states (24) and a noninteracting initial state. Green functions Gσ, Gσ0, and Λσ satisfy the symmetry (10), such that they are represented
.
.
i)
iv)
ii)
Λ
<
Λ
ret
Λ
¬
iii)
G<
0 Gret
0
G
¬
0
G< Gret
G
¬
FIG. 2: Computational scheme for the nonequilibrium DMFT using the self-consistency (25) and noninteracting initial states. Steps (i)-(iv) are explained in the text.
by their Matsubara, retarded, “
¬
” and lesser component. The Matsubara Green functions are given by the equilibrium (noninteracting) Green function
g
M
σ (iωn) = gM
0,σ(iωn) =
∫
dǫ ρ(ǫ)
iωn + μ − ǫ (66)
= V −2λM
σ (iωn), (67)
where ρ(ǫ) is given by Eq. (24), and the last equality holds due to the self-consistency (25). The mixed components G
¬
σ, G
¬
σ0, and Λ
¬
σ are represented after the par
tial Fourier transform (59) and analytical continuation by their value along the branch cut, i.e., for each Green function Y we keep two functions Y
¬
(ω±, t) on a fixed frequency mesh. The DMFT iteration is started from an initial guess (36). In step (i) [cf. Fig. 2], the Weiss field Λ(t, t′) is computed from the closed self-consistency equation (25). This is then used to determine the noninteracting bath Green function Gσ0 from its inverse (16b), as explained in the previous subsection [step (ii) in Fig. 2]. The function Gσ0 is the input for the calculation of the interacting bath Green function (13) using CTQMC [step (iii) in Fig. 2]. Because the initial state is noninteracting, the Monte Carlo simulation is restricted to the real-time branch of the contour, and only the real-time components GσR
and Gσ< are obtained. However, the mixed component
G
¬
σ (ω±, t) can be reconstructed from these functions and
the previous Weiss field Λ [step (iv)]: For this purpose consider the Dyson equation (15), which has the form of Eq. (37) after the replacement K = Λσ + Σσ, Y = Gσ, and h(t) = μ. Hence G
¬
(z, t) can be obtained from the integral (61), making the same replacements. Because Σσ(t, t′) is proportional to the interaction strengths U (t)
and U (t′), we have Σ
¬
σ (τ, t) = 0 for a noninteracting ini
tial state, with U (−iτ ) = U (0) = 0. Hence G
¬
(ω±, t) is given by
G
¬
σ (ω±, t)
= gM
σ (ω±)
[
GσA(0, t) +
t
∫
0
dt ̄Λ
¬
σ (ω±, t ̄)GσA(t ̄, t)
]
, (68)
where gM
σ (ω±) = ∓πiρ(ω) [Eq. (66)]. Steps (i) through


 10
-0.8
-0.6
-0.4
-0.2
0
0.2
012345
Energy
t
a) U=2
Epot
EEktiont
-1
-0.5
0
0.5
1
0 0.5 1 1.5 2 2.5 3
Energy
t
b) U=5 Epot
EEktiont
FIG. 3: Potential energy Epot(t) [Eq. (51)], kinetic energy Ekin(t) [Eq. (49)], and total energy Etot = Epot + Ekin in the half-filled Hubbard model after an interaction quench from U = 0 to U = 2 (a) and U = 5 (b). The initial state temperature is given by T = 0. The results were obtained with nonequilibrium DMFT for a semielliptic density of states (24), using either CTQMC (symbols), IPT (dashed lines) or SPT (solid lines) to solve the single-site problem. The inset in the upper panel shows the second-oder diagram for Σσ. Lines represent G0,σ for IPT [Eq. (69)], and Gσ for SPT [Eq. (70)].
(iv) are repeated until convergence, which is usually reached after not more that 15 iterations.
V. COMPARISON TO ITERATED PERTURBATION THEORY
In equilibrium DMFT, the so-called iterated perturbation theory (IPT),7,47 is frequently used as an approximate but efficient method to solve the single-site problem. Within IPT, the self-energy Σσ is expanded up to second order in the interaction U . Although this is a weak-coupling expansion by construction, it is accidentally correct for the atomic limit of the half-filled Hubbard model in equilibrium. In many aspects, IPT thus
provides a reasonable interpolation between the two exact limits U = 0 and V = 0. In particular, it qualitatively reproduces the DMFT phase diagram and the Mott transition in the paramagnetic phase, although there are quantitative differences to numerically exact QMC results. It is therefore interesting to see whether this approximation performs similarly well when used to solve the single-site problem in nonequilibrium DMFT. In the following we restrict ourselves to the half-filled Hubbard model with time-dependent interaction U (t). The Hartree contribution to the self-energy (first-order diagram), which gives a shift of the chemical potential with respect to μ = 0, then vanishes, and the secondorder contribution to the self-energy is given by a single diagram (inset in Fig. 3a),
Σiσpt(t, t′) = −U (t)U (t′)G0,σ(t, t′)G0,σ ̄ (t′, t)G0,σ ̄ (t, t′).
(69)
This equation is easily incorporated into the DMFT selfconsistency iteration by replacing step (iii) and (iv) in Fig. 2 with a solution of the Dyson equation (15) for Gσ, where Σσ is given by Eq. (69). Equation (15) is solved numerically, as described in Sec. IV A. In Fig. 3 we plot the potential energy Epot(t) [Eq. (51)], the kinetic energy Ekin(t) [Eq. (49)], and total energy Etot = Epot + Ekin of the half-filled Hubbard model after an interaction quench from the noninteracting initial state at temperature T = 0. The hopping matrix elements correspond to a semielliptic density of states Eq. (24) with quarter bandwidth V = 1, and time is measured in units of ħ/V = 1. The numerically exact CTQMC results show a rapid relaxation of these quantities, which is discussed in detail below. As required by energy conservation, Etot is constant within the numerical accuracy. IPT can reproduce these results rather accurately for small values of U (Fig. 3a). Already at intermediate coupling, however, the results of CTQMC and IPT strongly deviate from each other (Fig. 3b). In particular, the total energy Etot is generally not conserved within IPT, such that the use of IPT as an approximation for the intermediate- and strong-coupling regime becomes highly questionable. In contrast to equilibrium DMFT, IPT does not provide a reasonable interpolation between weak- and strong-coupling regimes. This violation of energy conservation is cured by a simple procedure. An expansion of Σσ up to finite order in terms of the noninteracting Green function is not a conserving approximation in the sense of Kadanoff and Baym.48,49 However, the approximation becomes conserving when G0,σ in Eq. (69) is replaced by the full interacting Green function,
Σsσpt(t, t′) = −U (t)U (t′)Gσ(t, t′)Gσ ̄ (t′, t)Gσ ̄ (t, t′). (70)
The resulting self-consistent perturbation theory (SPT) is a truncation of the skeleton expansion for the selfenergy, which can be derived from an approximation to


 11
the Luttinger Ward-functional and is therefore conserving. SPT is incorporated into the DMFT iteration by replacing step (ii)-(iv) in Fig. 2 with a solution of the Dyson equation (15) for Gσ, where Σσ is given by Eq. (69). Note that in this implementation Gσ is the SPT solution of the single-site problem for given Λ only after the DMFT iteration is converged. When SPT is used instead of IPT as an approximate impurity solver, we find that Etot is indeed constant with time (solid lines in Fig. 3). However, SPT is not reliable at intermediate interaction strength either. For U = 5 (Fig. 3b), SPT predicts a monotonous relaxation of Epot and Ekin, while the numerically exact QMC yields oscillations which are an important feature of the dynamics in the Hubbard model at strong coupling. For weak interactions, SPT performs slightly better, but in this parameter regime it is worse that the IPT solution (Fig. 3a). The fact that IPT approximates the exact numerical solution better than SPT is already known from equilibrium DMFT.
VI. RESULTS
In the remainder of this paper we present additional numerical results for the interaction quench in the Hubbard model in nonequilibrium DMFT, building on our previous work (Ref. 20). The system is assumed to be in the noninteracting ground state before time t = 0, when the interaction is abruptly switched to a positive value U . We consider only homogeneous nonmagnetic states
at half-filling (n↑ = n↓ = 1
2 ). Hopping matrix elements
are chosen such that the density of states is of semielliptic shape Eq. (24), and the quarter bandwidth V = 1 is set as energy unit, so that time is measured in units of ħ/V = 1.
The time evolution of various thermodynamic quantities after this interaction quench was already discussed in Ref. 20. After some preliminary remarks on the effective temperature after a quench (Sec. VI A) we will briefly restate the basic conclusions of the latter publication and substantiate them with additional data (Sec. VI B). We then turn to a characterization of the relaxing state in terms of dynamical quantities, i.e., the spectral function (Sec. VI C), and the optical conductivity (Sec. VI D).
A. Excitation after an interaction quench
An important information on the state of the system after the interaction quench is its excitation energy with respect to the ground state. Because the system is assumed to be isolated from the environment, the total energy is conserved after the quench and its value follows from the expectation values of the Hamiltonian in the initial state immediately before the quench. The energy corresponds to an effective temperature Teff, i.e., the temperature of the unique thermal equilibrium state which
0
0.5
1
n(ε,t)
a) U=2
12345
-2
-1
0
1
2
ε t
n(ε,t)
0
0.5
1
n(ε,t)
b) U=3.3
12345
-2
-1
0
1
2
ε t
n(ε,t)
0
0.5
1
n(ε,t)
c) U=5
0.5 1 1.5 2 2.5 3
-2
-1
0
1
2
ε t
n(ε,t)
FIG. 4: Momentum distribution n(ǫ, t) after an interaction quench in the Hubbard model from the noninteracting ground state to interaction U = 2 (a), U = 3.3 (b), and U = 5 (c).
has the same total energy [Eq. (58)],
Etot(t) = Etot(0+) = Tr H e−H/Teff
Tr e−H/Teff . (71)
(An analogously defined effective chemical potential is fixed to μeff = 0 by particle-hole symmetry.) For the quench in the Hubbard model we compute Teff by a numerical solution of Eq. (71). Thermal equilibrium expectation values of static quantities are obtained from equilibrium DMFT, using QMC as impurity solver. For the quenches discussed below, Teff is of the same order as the hopping strength, which is far above the Mott transition endpoint in thermal equilibrium. If the system reaches a thermal equilibrium state a sufficiently long time after the quench, the temperature


 12
of this state is given by Teff. Below we thus compare expectation values of observables after the quench with thermal equilibrium expectation values at T = Teff. All static quantities in thermal equilibrium are directly computed within equilibrium DMFT. The computation of dynamical quantities such as the spectral function and the optical conductivity, however, would require an analytical continuation from Matsubara frequencies to real frequencies, which is not accurate enough at large frequencies and high temperature to allow for a quantitative comparison. We therefore use nonequilibrium DMFT to obtain real-time Green functions and the real-time optical conductivity in thermal equilibrium directly in the time domain. This calculation is equivalent to an “interaction quench” in which the value of U is not changed and the initial state is at finite temperature T = Teff. In contrast to the quench from the noninteracting state, it is done on the L-shaped contour, and we do not use the tricks which are discussed in Sec. IV E. The maximum times that are accessible in this way are comparable to the times which are accessible an the interaction quench from the noninteracting initial state.
B. Relaxation after an interaction quench
The time evolution after an interaction quench in the Hubbard model depends on the parameter U in a very sensitive manner. To illustrate the qualitatively different relaxation behavior in the weak, strong, and intermediate-coupling regime we plot the momentum distribution n(ǫ, t) [Eq. (48)] for three values of U (Fig. 4). In all three cases the magnitude of the discontinuity ∆n(t) = limη→0+ [n(−η, t) − n(η, t)] at the Fermi energy decreases with time. Note that ∆n(t) remains finite for a finite time after the quench; for the present case of a local self-energy this is due to the fact that ∆n(t) is directly related to the retarded Green function at ǫ = 0.20 Because a discontinuity in the momentum distribution of a Fermi liquid in thermal equilibrium can exist only at zero temperature, while on the other hand, a quenched system is always excited with respect to the ground state, the existence of a finite jump ∆n(t) clearly indicates that the system is not yet fully thermalized. The size of the discontinuity is thus well suited to characterize the relaxation after the quench. In the weak-coupling regime (Fig. 4a), n(ǫ, t) rapidly evolves towards a distribution (t . 2 in Fig. 4a) which is not yet thermalized, but changes only slowly in time. This emergence of long-lived nonthermal states is an example of prethermalization,22 which is observed in a wide range of classical and quantum systems.23 As shown by Moeckel and Kehrein,22 the nonthermal state remains stable for all times within second order unitary perturbation theory in U/V , i.e., higher-order corrections become effective only on the long timescale V 3/U 4. In the limit of infinite dimensions their weak-coupling result for the transient behavior towards the prethermalization plateau
0.2
0.4
0.6
0.8
1
n(ε,t)
a) U=2
t = 3.0 t = 4.0 Teff = 0.31
0.2
0.4
0.6
0.8
1
n(ε,t)
b) U=3.3
t = 1.575 Teff = 0.84
0.2
0.4
0.6
0.8
1
-2 -1.5 -1 -0.5 0 0.5 1 1.5 2
n(ε,t)
ε
c) U=5
t = 2.175 t = 2.925 Teff = 2.0
FIG. 5: Comparison of the momentum distribution n(ǫ, t) for fixed time t after the quench (symbols) to the momentum distribution in thermal equilibrium at the effective temperature Teff [cf. Eq. (71)] (solid lines). Interaction parameters are U = 2 (a), U = 3.3 (b), and U = 5 (c).
has the form
npert(ǫ, t) = n(ǫ) − 4U 2F (ǫ, t) , (72)
F (ǫ, t) =
∞
∫
−∞
dE sin2(E − ǫ)t/2
(E − ǫ)2 Jǫ(E), (73)
Jǫ(E) =
∫
dǫ′1
∫
dǫ′2
∫
dǫ1 δ(ǫ′1 + ǫ′2 − ǫ1 − E) ×
ρ(ǫ′1)ρ(ǫ′2)ρ(ǫ1) [n(ǫ)n(ǫ1)(1 − n(ǫ′1))(1 − n(ǫ′2)) − (1 − n(ǫ))(1 − n(ǫ1))n(ǫ′1)n(ǫ′2)]. (74)
For a half-filled band and a symmetric density of states, ρ(ǫ) = ρ(−ǫ), we obtain
F (ǫ, t) = − sgn(ǫ)
2
t
∫
0
ds (t − s) Re[R(s)3 eis|ǫ|], (75)
where R(s) = ∫ dǫ Θ(−ǫ) ρ(ǫ) eisǫ. This yields ∆n(t) and also d(t) by using the energy conservation after the


 13
-0.2
0
0.2
0.4
0.6
0.8
1
012345
∆n(t)
t
a)
U=0.5
UU==11.5
UU==22.5
0.09
0.13
0.17
0.21
0.25
012345
d(t)
t
b)
U=0.5
UU==11.5
U=2 U=2.5
FIG. 6: Approach of the prethermalized state at weakcoupling and subsequent relaxation towards the thermal state. (a) Discontinuity at the Fermi surface. (b) Double occupation. Solid lines: weak-coupling results [Eq. (76)-(77)].
quench,
∆npert(t) = 1 − 4U 2
t
∫
0
ds (t − s) Re[R(s)3], (76)
dpert(t) = 1
4 − 2U
t
∫
0
ds Im[R(s)4]. (77)
Numerical evaluations of these functions are plotted and compared to our DMFT results in Fig. 6 for the semielliptic density of states (24) with V = 1. Regarding the transient behavior and the prethermalization plateau we find very good agreement for U . 1. Interestingly the prethermalization plateau of ∆n(t) is almost correctly predicted by the weak-coupling results even for U . 2. For larger times the system relaxes further towards the thermal value. In the strong-coupling regime (Fig. 4c), the relaxation is dominated by damped collapse and revival oscillations of approximate periodicity 2π/U . The decay of these
oscillations is not fully accessible within CTQMC due to the dynamical sign problem. However, our results show that n(ǫ, t) oscillates around a nonthermal distribution (Fig. 5c). This behavior, which is analogous to prethermalization at weak-coupling, is similar to what was found for the double occupation d(t),20 i.e., a decay on the timescale 1/V to oscillations around a nonthermal value which does not change on much longer timescales. The interaction quench to U = 3.3V is characterized by a rapid thermalization of the momentum distribution (Figs. 4b and 5b), without signatures of either collapse and revival oscillations or a prethermalization plateau in n(ǫ, t). Numerically we cannot detect a finite width to the crossover regime between the weak- and strongcoupling behavior, which indicates that there is a single point U = Udyn ≈ 3.2V which marks a dynamical transi
tion in the Hubbard model.20 A further investigation of this phenomenon and its relation to the Mott transition in equilibrium will require a systematic analysis of interaction quenches which start from a wide range of initial states other than the noninteracting ground state. This is left to a future publication. In the following we turn to a different question and investigate to what extent the rapid thermalization close to U = Udyn, the oscillations at U > Udyn, and the prethermalization at U < Udyn show up in various dynamical quantities of the Hubbard model.
C. Spectral function
Important information about a correlated system out of equilibrium cannot only be obtained from thermodynamic quantities, but also from the dynamical response of the system to certain external perturbations, which can be computed from various real-time correlation functions. In the following subsection we discuss the time evolution of the local Green function Gσ(t, t′) ≡ G(t, t′) in the paramagnetic phase of the Hubbard model after a quench from the noninteracting ground state to finite interaction U . For this purpose we introduce the partial Fourier transform
GR,<(ω, t) =
∫
ds eiωsGR,<(t + s, t) (78)
of the retarded and lesser Green function, and the spectral function A(ω, t) = −(1/π) Im GR(ω + i0, t). The spectrum turns out to be a useful representation of the nonequilibrium Green function, although it lacks a direct relation to the “distribution function” G<(ω, t) and thus does not have the same significance as in the equilibrium case. [In equilibrium one has G<(ω) = 2πiA(ω)f (ω).] Before discussing the results we have to mention a technicality, which arises from the restriction of the Monte Carlo simulations to relatively small times t < tmax. In practice, the integration range in Eq. (78) must be cut off at smax ≡ tmax − t, leading to artificial oscillations at frequency 1/smax. To reduce this effect in a controlled way


 14
-0.2
0
0.2
0.4
0.6
0.8
1
012345
iGret(t+s,t)
s
a)
U=0 t = 0.0 t = 0.2 t = 0.4 t = 1.0 Teff=0.84
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
-4 -2 0 2 4 6
A(ω,t)
ω
b) t = 0.0 t = 0.2 t = 0.4 t = 1.0 Teff=0.84
FIG. 7: (a) Local Green function GR(t + s, t) for an interaction quench in the Hubbard model to U = 3.3 (slightly above Udyn). The function is purely imaginary due to particle-hole symmetry. The solid black line is the Green function in the thermal equilibrium state (U = 3.3, Teff = 1/β = 0.84). The dotted line (U = 0) is the retarded Green function in the noninteracting initial state. (b) Spectral function A(ω, t) =
−(1/π)ImGR(ω, t) for the same parameters as in the upper panel. The dotted line and the line labelled Teff = 0.84 are the semielliptic density of states (24) of the initial state and the thermal equilibrium spectrum at temperature Teff = 0.84, respectively. Spectra are obtained from Fourier transformation of real-time quantities, and the Fourier integral (78) is cut off at smax = 3.5 with an additional Gaussian factor (see text). The corresponding kernel [Eq. (79), κ = 0.1] is shown as thin solid line.
we introduce an additional Gaussian factor exp(−s2κ) in the integral (78). The resulting expression amounts to a convolution of the true Fourier transform (tmax = ∞) with the kernel
k(ω; κ, smax) = 1
2π
smax
∫
−smax
ds exp(iωs − s2κ). (79)
A suitable choice of the parameter κ can in some cases suppress the oscillations without washing out important
spectral features, and a comparison with a known equilibrium spectrum is always possible without loss of information after convolution of the latter with the same kernel.
In Fig. 7 we plot GR(t + s, t) and A(ω, t) for a quench to interaction U = 3. The spectrum A(ω, t) differs from the initial semielliptic density of states for all times t ≥ 0, because the choice of the Fourier transform in Eq. (78) implies that the initial equilibrium Green function does not enter the definition of A(ω, t) for t > 0. Note that this would be different for the common definition of the Fourier transform at constant average time (t + t′)/2.50 Within numerical accuracy, both GR(t + s, t) and A(ω, t) become time-(t)-independent for t > 1/V . This timescale is comparable to the relaxation time of the double occupation and the momentum distribution at U ≈ 3.3 (Fig. 4b).
An important interpretation of the finite relaxation time in A(ω, t) can be inferred directly from the definition of the Green function. According to Eq. (6), GR(t + s, t) is related to the survival amplitude of local single-particle excitations which are created at time t and destroyed at later time t + s. The decay of such an excitation depends on both the Hamiltonian, which defines the possible scattering mechanisms, and the quantum state of those particles which act as scatterers. While the Hamiltonian changes abruptly at t = 0, the latter evolves with time, leading to the finite relaxation time of A(ω, t). In contrast, A(ω, t) would be constant immediately after a quench in a noninteracting system, because the anticommutator in Eq. (6) is a c-number for a quadratic Hamiltonian. We can thus conclude that the finite relaxation time observed in Fig. 7 is a true many-body effect, in analogy to the well-known fact that equilibrium spectra depend on temperature only for interacting systems.
To characterize the final state after the relaxation, its spectrum should be compared to the equilibrium spectrum of a correlated metal at rather high temperature. In fact, A(ω, t) is strongly modified with respect to the semielliptic density of states, with precursors of the Hubbard bands around ω = ±2. The fact that the spectrum is not pinned at ω = 0 can be attributed to the strong excitation of the system with respect to the ground state. A quantitative analysis of the spectrum requires the knowledge of the equilibrium spectrum at the effective temperature Teff [cf. Eq. (71), Teff = 0.84 for U = 3.3]. Equilibrium spectra are usually computed from imaginary-time correlation functions using (maximum entropy) analytical continuation, which is not accurate enough at high frequencies to allow for a comparison of two rather similar spectra. Using nonequilibrium DMFT, however, we can avoid this complication and compute real-time equilibrium Green function GeRq(t, t′) ≡ gR(t − t′) without
analytical continuation (cf. Sec. VI A). Within numerical accuracy, the resulting equilibrium function indeed agrees with the retarded Green function GR(t, t′) after relaxation (Fig. 7a), which proves that the rapid thermalization at U ≈ 3.3 can also be seen in the spectral


 15
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
0.8
1
0 0.5 1 1.5 2 2.5 3
iGret(t+s,t)
s
a)
U=0 t = 0.0 t = 0.6 t = 1.2 Teff=2
0
0.05
0.1
0.15
0.2
0.25
0.3
-8 -6 -4 -2 0 2 4 6 8
A(ω,t)
ω
b) U = 0
Teff=2 t = 0.0
FIG. 8: Same as Fig. 7, but for the interaction quench to U = 5. Spectra (b) are obtained from Fourier transformation of real-time quantities, and the Fourier integral (78) is cut off at smax = 2.5 with an additional Gaussian factor (see text). The corresponding kernel [Eq. (79), κ = 0.4] is shown as thin solid line.
function. The analysis of the spectrum can now be repeated for quenches to the weak- and strong-coupling regime. For U ≪ V , however, the spectrum remains close to the semielliptic density of states for all times, such that rather high numerical accuracy would be needed for a systematic investigation of the small differences. In the strong-coupling regime, on the other hand, the restriction to small times t < tmax turns out to be more limiting for an investigation of the retarded Green function than for static quantities, simply because GR(t + s, t) is known only for t < tmax − s and not for t < tmax. Nevertheless, one can see that the relaxation of the Green function after a quench to U = 5 (Fig. 8a) roughly follows the oscillatory behavior of the momentum distribution (Fig. 4c): Close coincidence with the thermal function is reached around the time when the jump of the momentum occupation has its first minimum (t = 0.6), after which the deviations to the thermal Green function slightly increase
again. Similar behavior was found for the double occupation, which comes closest to the thermal value at its first minimum around t = 0.6.20 In spite of the large effective temperature (Teff = 2V ), the spectral function has a clear minimum at ω = 0, and well-pronounced Hubbard bands at ω ≈ ±U/2 (Fig. 8b). However, the absolute changes with time are small in the strong-coupling regime. This behavior is expected because it can be shown that the spectrum is independent of time t after a quench to the atomic limit.
D. Optical conductivity
The two-time optical conductivity σ(t, t′) describes the linear response of the electrical current in a nonequilibrium state to a time-dependent electrical field δE(t) (which we call the probe field),
δ〈j(t)〉 =
t
∫
−∞
dt ̄σ(t, t ̄)δE(t ̄). (80)
(Tensor notation of σ(t, t′) is suppressed.) In solids, optical spectroscopy on nonequilibrium states is usually performed within the pump-probe setup, where the system is driven out of equilibrium by a strong laser pulse (the pump). In the following we calculate σ(t, t′) after the interaction quench to see how the electrical response becomes stationary while the system relaxes towards its thermal equilibrium state. Microscopically, the optical conductivity is related to the current-current correlation function, which can be computed from two diagrammatic contributions: (i) The bubble diagram of two Green functions Gk and the current vertex vk = ∂ǫk/∂k, and (ii) diagrams containing the vertex corrections of the current vertex.51 Within equilibrium DMFT, vertex corrections are local and thus do not contribute to the conductivity because vk is antisymmetric under inversion of k, and Gk is symmetric.52 In a nonequilibrium situation these conditions can be violated, e.g., due to an electrical pump field, in which case the conductivity depends on the relative polarization of pump and probe, so that vertex corrections do contribute.17,53 However, for the interaction quench the inversion symmetry of the state is preserved, and σ(t, t′) can be calculated from the bubble diagram alone.53 The microscopic derivation of σ(t, t′) within nonequilibrium DMFT was discussed in detail in Ref. 53. In the following we thus only state the results for σ(t, t′) after an interaction quench in the Hubbard model on the hypercubic lattice in d = ∞, with hopping amplitudes that yield a semielliptic density of states41 (Eq. (24) with V = 1, as above). The band dispersion ǫk enters the expression via the current vertex vk = ∂ǫ(k)/∂k; this is where the hopping amplitudes enter in addition to the density of states. Conductivity is measured in units of σ0 = 2ρa2e2V /ħ2, where a is the lattice constant, and ρ is the number of lattice sites per volume.


 16
0.1
0.2
0.3
0.4
0.5
012345
σ(t+s,t)/σ0
s
a) U=2
t=0 t=0.5 t=1 t=2 t=3
0.4
0.5
012345
σ/σ0
t
σ(t,t)
0
0.1
0.2
0.3
0.4
0.5
0 0.5 1 1.5 2 2.5
σ(t+s,t)/σ0
s
b) U=3.3
t=0 t=0.3 t=0.6 t=0.9 t=2.0 0.2
0.4
012
σ/σ0
t
σ(t,t)
0
0.1
0.2
0.3
0.4
0.5
0 0.5 1 1.5 2 2.5
σ(t+s,t)/σ0
s
c) U=5
tt==00.5
tt==11.5
t=2
0.2
0.4
012
σ/σ0
t
σ(t,t)
FIG. 9: Optical conductivity σ(t + s, t) [Eq. (80)] after quenches to U = 2 (a), U = 3.3 (b), and U = 5 (c). The inset shows σ(t, t), and black solid lines correspond to the optical conductivity in thermal equilibrium at Teff = 0.37 (a), Teff = 0.84 (b), and Teff = 2 (c).
In Fig. 9, σ(t + s, t) is plotted as a function of timedifference s. This parametrization is most convenient for analyzing how the electrical response of the system becomes stationary (i.e., independent of t) during the relaxation. The results are compared to the optical conductivity σeq(s) in thermal equilibrium, which is obtained directly from nonequilibrium DMFT without analytical continuation (cf. Sec. VI A). The more familiar frequency-dependent optical conductivity
σeq(ω) = Re
∞
∫
0
ds eiωsσeq(s) (81)
is plotted in Fig. 10. After quenches to weak-coupling (U = 2, Fig. 9a), σ(t, t′) undergoes a rapid initial relaxation, but it does not approach the thermal value within the accessible times. This behavior reflects the prethermalization that is observed in the momentum occupation. The conductivity at the corresponding effective temperature (Teff = 0.37) consists of a Drude peak at ω = 0 (Fig. 10), which is only slightly broadened due to temperature and interaction. Because a narrow Drude peak implies a slow decay of σeq(s) with time difference, we cannot resolve the true width of the peak from data which are restricted to small times. For a quench to U = 3.3 (Fig. 9b), we observe a rapid relaxation of the optical response. The optical conductivity depends only on time difference for t & 1/V and coincides with σeq(s) for the effective temperature Teff = 0.67. The latter falls off rather quickly with time differences s, indicating that the Drude peak is strongly broadened because of the large temperature and the relatively strong interaction (Fig. 10). Finally, for the quench to U = 5 (Fig. 9c) relaxation to the thermal state becomes again slower than at U = 3.3. We observe the characteristic collapse and revival oscillations when σ(t + s, t) is plotted at fixed time difference s (inset in Fig. 9c). Due to the large effective temperature (Teff = 2) the conductivity of the corresponding equilibrium state is rather a bad metal than an insulator, but nevertheless the Hubbard band at ω = U is clearly separated from the broad feature at ω = 0 (Fig. 10).
VII. CONCLUSION
In this paper we described in detail how weak-coupling continuous-time quantum Monte Carlo (QMC) can be used as an impurity solver within nonequilibrium DMFT. The formalism, which was used in Ref. 20 to investigate the interaction quench in the Hubbard model, was extended to the case when the initial state is a finite temperature equilibrium state at nonzero interaction U . Because nonequilibrium experiments in interacting systems often start from correlated initial states rather than the noninteracting ground state, this extension is a prerequisite to apply DMFT within a variety of experimental sit


 17
0
0.1
0.2
0.3
0.4
0.5
0 2 4 6 8 10
σ(ω) [σ0/V]
ω
U=2 U=3.3 (x4) U=5 (x8)
FIG. 10: Frequency-dependent optical conductivity in thermal equilibrium at the temperature Teff = 0.37 (U = 2), Teff = 0.84 (U = 3.3), and Teff = 2 (U = 5). The latter two curves are scaled by a factor 4 and 8, respectively. All curves were obtained by Fourier transformation (81) of realtime data. In the case of U = 2, the Fourier integral is cut off at smax = 5 with an additional Gaussian factor, as explained for the spectral function. The corresponding kernel [Eq. (79), κ = 0.2] is shown as dotted line.
uations in the field of cold atomic gases and time-resolved spectroscopy on correlated solids. We used the numerically exact QMC solution of the DMFT equations to benchmark the generalization of the iterated perturbation theory (IPT) to the Keldysh contour. We find that IPT is remarkably good at weak interactions. However, in contrast to the equilibrium case it yields unphysical results in the intermediate-coupling regime and thus cannot provide a reasonable interpolation between the weak- and strong-coupling regime. The reason is that IPT is not a conserving approximation, which can lead to an explicit violation of the energy conservation as a function of time in some parameter regime. Furthermore, we used the nonequilibrium formalism to solve a system in thermal equilibrium. In this way one can avoid analytical continuation and obtain dynamical quantities in real time instead of imaginary time. We used this approach to compute the spectral func
tion and the optical conductivity of the single-band Hubbard model. Due to the dynamical sign problem of QMC one is restricted to relatively short times, such that frequency-dependent quantities, which are obtained from real-time functions by Fourier transformation, are considerably broadened. The real-time formalism can thus not directly replace the conventional analytical continuation from Matsubara to real frequencies. However, since the kernel which mediates the broadening of the spectra is explicitly known, it may be useful either to judge the accuracy of analytically continued spectra, or improve the analytical continuation in some frequency range.
In the last part of this paper we presented further results for the interaction quench in the Hubbard model. In particular, we investigated the time evolution of the real-time Green functions. It was shown that the different relaxation behavior at weak, strong and intermediate coupling, which was characterized by the time evolution of the double occupation and the momentum distribution in Ref. 20, is also reflected in the nonequilibrium spectral function: In the weak- and strong-coupling regime a thermal state cannot be reached within the accessible times, whereas the spectrum (as well all quantities that can be obtained from it) rapidly relaxes to the thermal equilibrium at intermediate coupling (U = Udyn).
The fact that the very sensitive U -dependence of the relaxation behavior is manifest also in the spectral function suggests that the phenomenon of fast electronic thermalization near Udyn may also be observed with pumpprobe spectroscopy on correlated systems. Further details of this transition-like phenomenon will hopefully soon be clarified by means of the DMFT+QMC formalism presented in this work.
Acknowledgements
M.E. acknowledges support by Studienstiftung des deutschen Volkes. This work was supported in part by the SFB 484 of the Deutsche Forschungsgemeinschaft (DFG) and the Swiss National Science Foundation (PP002-118866). CTQMC calculations were run on the Brutus cluster at ETH Zurich, using the ALPS library.54
1 R. J ̈ordens, N. Strohmaier, K. Gu ̈nter, H. Moritz, and T. Esslinger, Nature 455, 204 (2008).
2 U. Schneider, L. Hackermu ̈ller, S. Will, T. Best, I. Bloch, T. A. Costi, R. W. Helmes, D. Rasch, and A. Rosch, Science 322, 1520 (2008).
3 S. Iwai, M. Ono, A. Maeda, H. Matsuzaki, H. Kishida, H. Okamoto, and Y. Tokura, Phys. Rev. Lett. 91, 057401 (2003).
4 L. Perfetti, P. A. Loukakos, M. Lisowski, U. Bovensiepen, H. Berger, S. Biermann, P. S. Cornaglia, A. Georges, and
M. Wolf, Phys. Rev. Lett. 97, 067402 (2006); L. Perfetti, P. A. Loukakos, M. Lisowski, U. Bovensiepen, M. Wolf, H. Berger, S. Biermann, and A. Georges, New J. of Phys. 10, 053019 (2008).
5 Y. Kawakami, S. Iwai, T. Fukatsu, M. Miura, N. Yoneyama, T. Sasaki, and N. Kobayashi, Phys. Rev. Lett. 103, 066403 (2009).
6 S. Wall, D. Brida, S. R. Clark, H.P. Ehrke, D. Jaksch, A. Ardavan, S. Bonora, H. Uemura, Y. Takahashi, T. Hasegawa, H. Okamoto, G. Cerullo, and A. Cavalleri


 18
arXiv:0910.3808 (unpublished).
7 A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg, Rev. Mod. Phys. 68, 13 (1996).
8 W. Metzner and D. Vollhardt, Phys. Rev. Lett. 62, 324 (1989).
9 P. Schmidt and H. Monien, arXiv:cond-mat/0202046 (unpublished); P. Schmidt, Diploma thesis, University of Bonn (1999).
10 J. K. Freericks and V. Zlatic ́, Rev. Mod. Phys. 75, 1333 (2003).
11 U. Brandt and C. Mielsch, Z. Phys. B 75,365 (1989).
12 J. K. Freericks, V. M. Turkowski, and V. Zlatic ́, Phys. Rev. Lett. 97, 266408 (2006).
13 J. K. Freericks, Phys. Rev. B 77, 075109 (2008).
14 M.-T. Tran, Phys. Rev. B 78, 125103 (2008).
15 A. V. Joura, J. K. Freericks, and T. Pruschke, Phys. Rev. Lett. 101, 196401 (2008).
16 N. Tsuji, T. Oka, and H. Aoki, Phys. Rev. B 78, 235124 (2008).
17 N. Tsuji, T. Oka, and H. Aoki, Phys. Rev. Lett. 103, 047403 (2009).
18 M. Eckstein and M. Kollar, Phys. Rev. Lett. 100, 120404 (2008).
19 M. Greiner, O. Mandel, T. W. H ̈ansch, and I. Bloch, Nature 419, 51 (2002).
20 M. Eckstein, M. Kollar, and P. Werner, Phys. Rev. Lett. 103, 056403 (2009).
21 P. Werner, T. Oka and A. J. Millis, Rev. B 79, 035320 (2009).
22 M. M ̈ockel and S. Kehrein, Phys. Rev. Lett. 100, 175702 (2008); Ann. Phys. 324, 2146 (2009).
23 J. Berges, S. Borsa ́nyi, and C. Wetterich, Phys. Rev. Lett. 93, 142002 (2004).
24 M. Rigol, V. Dunjko, V. Yurovsky, and M. Olshanii, Phys. Rev. Lett. 98, 050405 (2007); M. Rigol, A. Muramatsu, and M. Olshanii, Phys. Rev. A, 74, 053616 (2006).
25 M. A. Cazalilla, Phys. Rev. Lett. 97, 156403 (2006).
26 M. Kollar and M. Eckstein, Phys. Rev. A 78, 013626 (2008).
27 S. R. Manmana, S. Wessel, R. M. Noack, and A. Muramatsu, Phys. Rev. Lett. 98, 210405 (2007).
28 M. Rigol, V. Dunjko, and M. Olshanii, Nature 452, 854 (2008).
29 G. Roux, Phys. Rev. A 79, 021608 (2009).
30 G. Biroli, C. Kollath, A. L ̈auchli, arXiv:0907.3731 (unpublished).
31 M. Rigol, Phys. Rev. Lett. 103, 100403 (2009); arXiv:0908.3188 (unpublished); arXiv:0909.4556 (unpublished).
32 L. F. Santos and M. Rigol, arXiv:0910.2985.
33 P. Barmettler, M. Punk, V. Gritsev, E. Demler, and E. Altman, Phys. Rev. Lett. 102, 130603 (2009).
34 C. Kollath, A. L ̈auchli, and E. Altman, Phys. Rev. Lett. 98, 180601 (2007).
35 For an introduction into the Keldysh formalism, see R. van Leeuwen, N. E. Dahlen, G. Stefanucci, C.O. Almbladh and U. von Barth, arXiv:cond-mat/0506130 (published in: Time-dependent density functional theory, M. A. L. Marques, C. A. Ullrich, F. Nogueira, A. Rubio, K. Burke, and E. K .U. Gross (eds.), Lecture Notes in Physics 706, Springer, Berlin 2006).
36 L. V. Keldysh, J. Exptl. Theoret. Phys. 47, 1515 (1964) [Sov. Phys. JETP 20, 1018 (1965)].
37 M. Bonitz and D. Semkat (eds.), Progress in Nonequilibrium Green’s Functions II, World Scientific, Singapore, 2003.
38 P. Danielewicz, Ann. Physics 152, 239 (1984).
39 M. Wagner, Phys. Rev. B 44, 6104 (1991).
40 E. N. Economou, Green’s Functions in Quantum Physics, Springer, Berlin, 1979.
41 N. Blu ̈mer and P. G. J. van Dongen, arXiv:cond-mat/0303204 (published in: Concepts in Electron Correlation, edited by A. C. Hewson and V. Zlatic ́, NATO Science Series, Kluwer, 2003).
42 E. Gull, P. Werner, O. Parcollet, and M. Troyer, Europhys. Lett. 82, 57003 (2008).
43 S. M. A. Rombouts, K. Heyde, and N. Jachowicz, Phys. Rev. Lett. 82, 4155 (1999).
44 A. N. Rubtsov, V. V. Savkin and A. I. Lichtenstein, Phys. Rev. B 72, 035122 (2005).
45 K. Mikelsons, A. Macridin, and M. Jarrell, arXiv:0903.0559 (unpublished).
46 H. Brunner and P. J. van der Houwen, The numerical solution of Volterra equations, North-Holland, Amsterdam, 1986.
47 X. Y. Zhang, M. J. Rozenberg, and G. Kotliar, Phys. Rev. Lett. 70, 1666 (1993).
48 G. Baym and L. P. Kadanoff, Phys. Rev. 124, 287 (1961).
49 G. Baym, Phys. Rev. 127, 1391 (1962).
50 V. Turkowski and J. K. Freericks, Phys. Rev. B 71, 085104 (2005).
51 T. Pruschke, D. L. Cox, and M. Jarrell, Phys. Rev. B 47, 3553 (1993).
52 A. Khurana, Phys. Rev. Lett. 64, 1990 (1990).
53 M. Eckstein and M. Kollar, Phys. Rev. B 78, 205119 (2008).
54 A. F. Albuquerque et al., Journal of Magnetism and Magnetic Materials 310, 1187 (2007).
