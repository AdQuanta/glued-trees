# Solution for the dynamics of the BCS and central spin problems - Full Text

> Source: https://iopscience.iop.org/article/10.1088/0305-4470/38/36/003
> Collected: 2026-09-20
> Published: 2005-09-09
> Zotero parent key: 7VI2MRKK
> Evidence: Zotero indexed PDF text

Journal of Physics A: Mathematical and General
Solution for the dynamics of the BCS and central spin problems
To cite this article: Emil A Yuzbashyan etal 2005 J.Phys.A:Math.Gen. 38 7831
View the article online for updates and enhancements.
You may also like
The two-gap BCS model in the large-N approximation within a field-theory approach Leandro O. Nascimento

Pairing in excited nuclei: a review N Quang Hung, N Dinh Dang and L G Moretto

A study of self-consistent Hartree–Fock plus Bardeen–Cooper–Schrieffer calculations with finite-range interactions M Anguiano, A M Lallena, G Co’ et al.

This content was downloaded from IP address 77.137.64.243 on 08/11/2024 at 10:28


 INSTITUTE OF PHYSICS PUBLISHING JOURNAL OF PHYSICS A: MATHEMATICAL AND GENERAL
J. Phys. A: Math. Gen. 38 (2005) 7831–7849 doi:10.1088/0305-4470/38/36/003
Solution for the dynamics of the BCS and central spin problems
Emil A Yuzbashyan1, Boris L Altshuler1,2, Vadim B Kuznetsov3 and Victor Z Enolskii4
1 Physics Department, Princeton University, Princeton, NJ 08544, USA 2 NEC Research Institute, Princeton, NJ 08540, USA 3 Department of Applied Mathematics, University of Leeds, Leeds, LS2 9JT, UK 4 Department of Mathematics, Heriot-Watt University, Edinburgh, EH14 4AS, UK
Received 30 June 2005, in final form 4 July 2005 Published 23 August 2005 Online at stacks.iop.org/JPhysA/38/7831
Abstract
We develop an explicit description of a time-dependent response of fermionic condensates to perturbations. The dynamics of Cooper pairs at times shorter than the energy relaxation time can be described by the BCS model. We obtain a general explicit solution for the dynamics of the BCS model. We also solve a closely related dynamical problem—the central spin model, which describes a localized spin coupled to a ‘spin bath’. Here, we focus on presenting the solution and describing its general properties, but also mention some applications, e.g. to nonstationary pairing in cold Fermi gases and to the issue of electron spin decoherence in quantum dots. A typical dynamics of the BCS and central spin models is quasi-periodic with a large number of frequencies and stable under small perturbations. We show that for certain special initial conditions the number of frequencies decreases and the solution simplifies. In particular, periodic solutions correspond to the ground state and excitations of the BCS model.
PACS numbers: 05.70.Ln, 74.20.De
1. Introduction
Recent experiments [1] on cold fermion pairing in the vicinity of a Feshbach resonance offer a unique opportunity to control the strength of pairing interactions between fermions by a magnetic field. This opens up an exciting possibility of exploring fundamentally new aspects of the nonequilibrium pairing following an abrupt change of the coupling strength. Interestingly, the dynamical pairing in this regime can be linked to a seemingly unrelated spin model. The latter describes the interaction of a localized (central) spin with a ‘spin bath’ of environmental spins. The central spin model has re-emerged recently in the context of experiments [2, 3] on electron spin dynamics due to the hyperfine interaction with nuclei in
0305-4470/05/367831+19$30.00 © 2005 IOP Publishing Ltd Printed in the UK 7831


 7832 E A Yuzbashyan et al
GaAs quantum dots. Since single electron quantum dots are now experimentally accessible [3], and are considered one of the most promising candidates for solid state qubits, it is also important to understand the effect of this interaction on the coherence of the electron spin. In this paper, we present a theory that provides an accurate description for a range of phenomena in the dynamical pairing and central spin problems. As we will see below, there is an intimate connection between these two problems that will enable us to treat them on an equal footing. The study of the dynamics of the superconducting state in metals founded on microscopic principles has begun during the decade following the advent [4] of the BCS theory (see [5] for a review). The simplest theory for nonstationary processes in superconductors is based on the time-dependent Ginzburg–Landau (TDGL) equation [6–8] for the order parameter (t). The TDGL approach is valid when quasiparticles are able to reach a local equilibrium quickly on the characteristic time scale of the order parameter variation τ ( −1 at zero temperature). This requirement usually limits the applicability of the TDGL theory to situations where mechanisms destroying Cooper pairs are effective, such as a narrow vicinity of Tc or a large concentration of magnetic impurities. An alternative theory [9, 10] is the Boltzmann kinetic approach, which describes the dynamics in terms of a kinetic equation for the quasiparticle distribution function coupled to a self-consistent equation for (t). However, this scheme is justified only when external parameters change slowly on the τ time scale. As pointed out in [11], cold fermionic gases can be in a regime where the notion of the excitation spectrum is irrelevant and neither TDGL nor the Boltzmann kinetic equations are valid. Indeed, in these systems external parameters such as the detuning from a Feshbach resonance can change on a time scale τ0 τ , τ , where τ is the quasiparticle energy relaxation time. On the other hand, the energy relaxation is slow, while the lifetime of the samples is limited. It is therefore desirable to develop a theory that describes nonstationary pairing effects in this regime. The nonequilibrium Cooper pairing at times t τ is non-dissipative and in a translationally invariant system can be described by the reduced BCS model
Hˆ BCS = ∑
p,σ
p cˆ †
pσ cˆpσ − g
∑
p,k
cˆ †
p↑ cˆ †
−p↓cˆ−k↓cˆk↑. (1.1)
It is interesting to note that the use of this model for describing the dynamics of a homogeneous superconducting state in metals in the non-dissipative regime, t τ , has been justified [12] quite generally starting from nonstationary Eliashberg equations. Here, we are interested in a situation when a system at zero temperature is out of an equilibrium at t = 0. The goal is to determine the subsequent evolution of the initial state. In particular, this includes the case when at t = 0 the coupling constant has been abruptly changed from g′ to g. In the absence of translational invariance, e.g. in a dirty superconductor or in a finite system, Hamiltonian (1.1) has to be appropriately generalized [13]. First, let us discuss the familiar case of electron–electron interactions. If there are no spatial symmetries, but the timereversal invariance is preserved, single-particle orbitals j are degenerate only with respect to spin. For each orbital j there is a pair of states, |j ↑〉 and |j ↓〉, related by time reversal symmetry. The pairing occurs between time reversed states, i.e.
Hˆ BCS = ∑
j,σ
j cˆ†
jσ cˆjσ − g
∑
j,q
cˆ †
j ↑ cˆ †
j↓cˆq↓cˆq↑. (1.2)
Deviations of the coupling strength g from a constant in q and j are small and sample-dependent [13, 14].


 Solution for the dynamics of the BCS and central spin problems 7833
For a two-species Fermi system, such as a two-component mixture of fermionic atoms in a trap, spin up and down states in (1.2) have to be identified with the two species of fermions. With this replacement, arguments [13, 14]5 leading to Hamiltonian (1.2) are valid in the weak coupling regime. Hamiltonian (1.1) is obtained from (1.2) by specializing to a translationally invariant situation. In this case, time reversed states are |p ↑〉 and |−p ↓〉. One can also take a thermodynamic limit by taking the number of orbital levels to infinity. However, in view of applications where the effective number of levels is finite and even small (see below), we deal with the general Hamiltonian (1.2) here. Remarkably, the BCS model turns out to be closely related to a model describing the Heisenberg exchange interaction of a single localized spin (the central spin) with a number of environmental spins. The Hamiltonian reads
Hˆ 0 =
n∑−1
j =1
γj ˆK0 · Kˆ j − BKˆ z
0 (1.3)
where Kˆ 0 is the central spin, Kˆ j are environmental spins, γj are (nonuniform) coupling constants, and B represents the magnetic field6. The central spin model has an interesting history of its own. For example, it emerged in the studies of electron spin dynamics in disordered insulators [15] and of coherent spin tunnelling in ferromagnetic grains [16]. More recently, it attracted considerable attention as a model for decoherence of qubits [17–20]. In particular, it can be used to model [17, 18] the hyperfine interaction of a localized electron spin with nuclear spins and the spin-dependent transport [21] in GaAs quantum dots. In these cases, it provides an adequate description of spin dynamics at times shorter than the nuclear spin relaxation time in the regime where the orbital level spacing in the dot is much larger than the temperature and typical interaction energies. The main result of this paper is an explicit general solution for the dynamics of the BCS and central spin models. In particular, we determine as functions of time the order parameter (t) and the expectation value of the central spin (equations (3.22) and (3.24)) as well as the dynamics of the remaining degrees of freedom for arbitrary initial conditions. Here, we concentrate on presenting the solution and describing its general properties. We also mention several applications to specific issues such as nonequilibrium pairing and that of decoherence due to the hyperfine interaction, but leave a detailed discussion for the future. The solution is based on the integrability [22–24] of the BCS and central spin models. This important property has been largely underestimated in part because it was discovered outside the main physical context of these models. Besides, due to the infinite range of interactions in Hamiltonians (1.2) and (1.3), the mean field approximation is exact [25, 26] for these models in the limit of large number of particles. In this approximation, the BCS and central spin models can be mapped onto a classical nonlinear system (see below). However, while the mean field simplifies the description of equilibrium properties to an extent where no advanced techniques are required, it is the integrability of the resulting classical system that enables us to solve dynamical problems. The BCS solution [4] for the ground state and excitations of the BCS model is recovered as a periodic case of the general solution (see the discussion following (2.6) and section 4). It is also interesting to note that, as we will see,
5 If the trap has certain spatial symmetries, the coupling g in (1.2) can depend on j and q. Hamiltonians (1.2) and (1.1) neglect any such effects, which are usually not important (see also the discussion of stability against perturbations later in the paper). 6 Since the component of the total spin along the magnetic field is conserved, including a uniform magnetic field acting on environmental spins is equivalent to adding a constant to the Hamiltonian.


 7834 E A Yuzbashyan et al
models (1.2) and (1.3), being in many respects classical, have distinct robust features that are preserved when the integrability is destroyed. The general nonstationary solution of the BCS and central spin models is in terms of hyperelliptic functions—multiple variable generalizations of ordinary elliptic functions. These functions frequently arise as solutions of integrable equations and have well-known analytical properties [27]. We show that for most initial conditions the dynamics is quasi-periodic with a number of independent frequencies equal to the number of degrees of freedom, n, and evaluate the frequencies in terms of the integrals of motion. The typical motion uniformly explores an invariant torus—an n-dimensional subspace of the 2n-dimensional phase space allowed by the conservation laws. These features of the typical motion are stable against small perturbations that destroy integrability. Further, we identify certain special values of integrals of motion for which the number of independent frequencies, m, becomes less than the number of degrees of freedom. For these degenerate cases, we were able to explicitly reduce the motion of the BCS and central spin models with n degrees of freedom to that of same systems with only m degrees of freedom. The solution progressively simplifies as the number of independent frequencies decreases. For example, solutions characterized by a single frequency (m = 1), i.e. periodic trajectories, are given by trigonometric functions; degenerate solutions with two independent frequencies (m = 2) are given by a combination of trigonometric and elliptic functions (see also [11] and the end of section 4), etc. Periodic solutions (m = 1) occupy a special place among degenerate solutions. As we show in section 4, they reproduce the BCS solution for the ground state and excitations of the BCS model. The paper is organized as follows. In section 2, we use a mean field approximation to map the BCS and central spin models onto equivalent classical models. Section 3 contains an explicit general solution for the dynamics of both problems. In section 4, we consider degenerate solutions. Section 5 discusses some open problems and possible applications of our results.
2. Mean field approximation
Our starting point is the mean field approximation, which enables the mapping of the BCS and central spin models onto equivalent classical nonlinear systems. We also derive the equations of motion and describe the relationship between the BCS and central spin models. The discussion of the mean field is facilitated by representing BCS Hamiltonian (1.2) in terms of Anderson pseudospin-1/2 operators [25].
Hˆ BCS =
n∑−1
j =0
2 j Kˆ z
j − gLˆ +Lˆ − ˆL =
n∑−1
q=0
ˆKq (2.1)
where n is the number of single-particle orbitals. Pseudospin operators are related to fermion creation and annihilation operators via
Kˆ z
j = c†
j↑cˆj↑ + cˆ†
j↓cˆj↓ − 1
2
Kˆ −
j = cˆj↓cˆj↑ Kˆ +
j = cˆ†
j ↑ cˆ †
j↓. (2.2)
Pseudospins are defined on unoccupied and doubly occupied pairs of states |j ↑〉 and |j ↓〉, where they have all properties of spin-1/2. Singly occupied pairs of states, on the other hand, do not participate in pair scattering and are decoupled from the dynamics.


 Solution for the dynamics of the BCS and central spin problems 7835
Our goal is to determine the time evolution according to Hamiltonian (2.1) of an arbitrary initial distribution of pseudospins. The mean field approximation consists of the replacement of the effective field seen by each pseudospin in BCS Hamiltonian (2.1) with its quantummechanical average, bj (t) = (−2 x(t), −2 y(t), 2 j ), where (t) is the BCS gap function
(t) ≡ x(t) − i y(t) ≡ g
∑
p
〈Kˆ −
j (t)〉. (2.3)
In this approximation, each spin evolves in the self-consistent field created by other spins
 ̇ˆKj = i[Hˆ BCS, Kˆ j ] = bj × ˆKj . (2.4)
Since equations (2.4) are linear in Kˆ j , we can take their quantum mechanical average with respect to the time-dependent state of the system to obtain
s ̇j = bj × sj bj = (−gJx , −gJy , 2 j ) J =
n∑−1
q=0
sq (2.5)
where sj (t) = 2〈Kˆ j (t)〉. Evolution equations (2.5) conserve the square of the average for each spin, i.e. s2
j = const. If spins initially were in a product state7, s2
j = 1.
Note from equation (2.2) the following correspondence between components of sj (t) and the normal and anomalous (Keldysh) Green functions at coinciding times:
Gj (t) = −i〈[cj↑(t), cˆ†
j↑(t)]〉 = isz
j (t)
Fj (t) = −i〈[cj↑(t), cˆj↓(t)]〉 = is−
j (t).
Equations (2.5) were derived [12] for phonon superconductors within the general framework of nonstationary Eliashberg theory in the collisionless regime t τ . A linearized version of these equations was considered in [12, 25, 28, 29]. Due to the infinite range of interactions between spins in (2.1), the mean field approximation is exact in the thermodynamic limit. For a system with a finite number, N, of particles (spins) we expect, based on an analysis of leading finite size corrections [30] to the mean field, equations (2.5) to be accurate for large N at times t < t∗N η, where t∗ and η > 0 do not depend on N. We see that sj = 2〈Kˆ j 〉 have all properties of classical spins governed by a Hamiltonian
HBCS =
n∑−1
j =0
2 jsz
j−g
2 J+J− (2.6)
and usual angular momentum Poisson brackets. Thus, the problem reduces to determining the time evolution of n classical spins according to Hamiltonian (2.6). The BCS solution for the ground state corresponds to the minimum of (2.6) and is obtained by aligning each spin in (2.6) antiparallel to the field acting upon it. A pair excitation8 (excitation of the condensate) of energy 2
√
( j − μ)2 + 2
0, where μ and 0 are the chemical potential and the equilibrium gap respectively, is obtained by flipping the spin sj . The U (1) symmetry of the BCS order parameter is equivalent to the symmetry of (2.6) with respect to uniform rotations of all spins around the z-axis. Due to this symmetry, spin configurations that determine the ground state and excitations can rotate around the z-axis with a frequency 2μ at no energy cost. In the presence of a particle–hole symmetry μ = 0 and these configurations
7 Within the mean field approximation, this is always true in equilibrium with any value of the coupling constant. 8 These are excitations that conserve the number of Cooper pairs, see [4, 25].


 7836 E A Yuzbashyan et al
are stationary with respect to Hamiltonian (2.6) (see section 4 where we recover the BCS solution as a periodic case of the general time-dependent solution). Next, we turn to the central spin model and its relationship to the BCS model. The central spin Hamiltonian (1.3) turns out to be a member of an integrable family of Gaudin magnets [23]—n Hamiltonians of the form:
Hˆ q = 2
n∑−1
j =0
′ ˆKq · ˆKj
q− j
− αKˆ z
q q = 0, . . . , n − 1 (2.7)
where j and α are arbitrary parameters. All Hamiltonians Hˆ q commute with each other and
with the z-component of the total spin, Lˆ z ∝ ∑
q Hˆ q , for arbitrary j and α. The central spin
model (1.3) coincides with Hˆ 0 in equation (2.7) if we choose 0 − j = 2/γj and α = B. Note that if a number of orbitals j in (2.1) are degenerate, the magnitude of their
total spin ∑
j =const ˆKj is conserved by Hamiltonian (2.1). In this case one can replace
Kˆ j → ∑
j =const Kˆ j in Hamiltonians (2.1) and (2.7) and sum over nondegenerate orbitals only. Now consider the following linear combination of Hˆ q:
n∑−1
q=0
q Hˆ q = − α
2


n∑−1
q=0
2 q Kˆ z
q− 2
α
ˆL+ ˆL−

 + const.
We see that for α = 2/g the expression in the square brackets coincides with BCS Hamiltonian (2.1). Therefore, for α = 2/g, the BCS Hamiltonian commutes with all Hˆ q and thus belongs to the same class of integrable models [23, 24]. In the same way as we did for the BCS model, we employ the mean field approximation to derive classical Hamiltonians that govern the evolution of sj (t) = 2〈Kˆ j (t)〉 for Hamiltonians (2.7):


Hq =
n∑−1
j =0
′ sq · sj
q− j
− αsz
q
HBCS =
n∑−1
j =0
2 jsz
j − J+J−
α.
(2.8)
In particular, the classical counterpart of central spin Hamiltonian (1.3) is
H0 =
n∑−1
j =0
γj
2 s0 · sj − Bsz
0. (2.9)
The validity of the mean field approximation for central spin model (1.3) is subject to similar considerations as for the BCS model (see the second paragraph following equation (2.5) and also [18]). Thus, the problem of determining the dynamics of the BCS and central spin models reduces to solving equations of motion for Hamiltonians H0 and HBCS in system (2.8). To obtain solutions for BCS (1.2) and central spin (1.3) models, one has to choose
α= 2
g BCS
2
0− j
= γj α = B central spin.
(2.10)


 Solution for the dynamics of the BCS and central spin problems 7837
Hamiltonians (2.8) Poisson commute with each other and with the z-component of the
total spin Jz ∝ ∑
q Hq. Each Hamiltonian in system (2.8) describes an evolution of n spins in an 2n-dimensional phase space (two angles for each spin) and has n integrals of motion (the energy and the remaining Hamiltonians from system (2.8)). Therefore, all Hamiltonians (2.8) are classical integrable models.
3. The solution
In the previous section we mapped the BCS and central spin models onto a classical integrable system (2.8). Nevertheless, even though Liouville’s theorem [31] guarantees a formal integrability in quadratures of classical integrable models, an explicit solution for the evolution of the original dynamical variables is not always possible. Fortunately, this turns out to be not the case for the BCS and central spin problems. For these models, as detailed below, we were able to obtain an explicit general solution of equations of motion. Before we proceed, let us discuss generic features [31] expected of the dynamics of a classical integrable model with n degrees of freedom. The motion is confined by conservation laws to an n-dimensional subspace of the 2n-dimensional phase space. This subspace (invariant torus) is determined by initial values of integrals of motion and is topologically equivalent to an n-dimensional torus. The motion on the invariant torus is characterized by n angle variables, φk and the corresponding angular frequencies, φk(t) = kt + φk(0). The frequencies depend only on integrals of motion, while constants φk(0) are determined by initial values of remaining degrees of freedom. Since for most initial conditions all frequencies k are independent9, typical trajectories uniformly explore the entire torus. All these properties are not affected by small perturbations destroying integrability (Kolmogorov–Arnold–Moser theorem). Now we turn to the solution for the dynamics of the BCS and central spin models. The solution consists of two main steps. The first one is a change of variables that casts equations of motion into the form of a known mathematical problem. In the second step, we use the solution of this problem to obtain dynamical variables sj (t) = 2〈Kˆ j (t)〉 as explicit functions of time. The change of variables is facilitated by defining a 2 × 2 matrix10 that depends on dynamical variables sj and also on an auxiliary parameter u
L=
( A(u) B(u)
B∗(u) −A(u)
)
(3.1)
where matrix elements of L are
A(u) = α −
n∑−1
j =0
sz
j
u− j
B(u) =
n∑−1
j =0
s−
j
u− j
. (3.2)
The eigenvalues of this matrix, ±v(u), depend on dynamical variables only through integrals of motion – Hj and s2
j
v2(u) = α2 +
n∑−1
j =0
(
2Hj
u− j
+ s2
j
(u − j )2
)
≡ α2Q2n(u)
Pn2(u) (3.3)
where we defined two polynomials, Q2n(u) and Pn(u) that will be frequently used in subsequent calculations
9 Frequencies k are independent if m = 0 is the only vector with integer components such that Ω · m = 0. 10 Matrix L is called the Lax matrix of integrable system (2.8).


 7838 E A Yuzbashyan et al
Q2n(u) ≡
2n−1
∏
j =0
(u − Ej ) ≡
2∑n
k=0
αkuk α2n = 1 (3.4)
Pn(u) ≡
n∏−1
q=0
(u − q ). (3.5)
Note that because L is Hermitian for real u, its eigenvalues are real and therefore the polynomial Q2n(u) is positive definite on the real axis. We will often refer to the polynomial Q2n(u) as the spectral polynomial. Following an algebraic version of the variable separation method [32, 33], we introduce n − 1 variables, uj , as zeros of B(u)—one of the off-diagonal matrix elements of L. Variables vj , canonically conjugate to uj , are given by one of the eigenvalues of matrix L at u = uj .
B(uj ) = 0 vj = −A(uj ) j = 1, . . . , n − 1. (3.6)
Although we will not use the Hamilton–Jacobi method, we remark that variables (uj , vj ) separate [33] Hamilton–Jacobi equations for Hamiltonians (2.8). Since uj are zeros of B(u), we can rewrite the matrix element B(u) as
B(u) = J−
∏n−1
j=1(u − uj )
∏n−1
j=0(u − j ) ≡ J−
Rn−1(u)
Pn(u) . (3.7)
This equation is useful for expressing original dynamical variables—components of spins sj —through separation variables uj and J−. For example, using equations (3.2) and (3.7), we have
s−
j = ur=esj
B(u) = J−
Rn−1( j )
Pn′ ( j ) (3.8)
where the prime denotes a derivative with respect to u. Equations of motion for central spin Hamiltonian (2.9) in terms of new variables uj and J− can be derived by using equation (3.3). We have
u ̇ j = iB√Q2n(uj )
uj
∏
m=j (uj − um)
s−
0 J−
J ̇− = iBs−
0 = iλJ−Rn−1(0) λ = B
2n
n ∏
j =1
γj .
(3.9)
Similarly, one obtains equations of motion for BCS Hamiltonian (2.6)
u ̇ j = 2i√Q2n(uj )
∏
m=j (uj − um)
J ̇− = −2iJ−


n∑−1
j =0
j + gJz
2−
n∑−1
j =1
uj

.
(3.10)
In equations (3.9) and (3.10) as well as in the rest of the paper, with no loss of generality, we shifted parameters j in the BCS and central spin Hamiltonians by a constant so that 0 = 0. In the reminder of this section we obtain an explicit general solution for the expectation value of each (pseudo)spin, sj (t) = 2〈Kˆ j (t)〉, as a function of time. In particular, this includes the expectation value of the central spin, s0(t), and the BCS gap function, (t) = gJ−(t).


 Solution for the dynamics of the BCS and central spin problems 7839
The solution is based on the observation that, with the help of elementary algebra, equations of motion (3.9) and (3.10) can be cast into a form of a known mathematical problem. Specifically, one can rewrite equations (3.9) and (3.10) for variables uj as
n∑−1
j =1
ul−1
j duj
√Q2n(uj ) = dxl l = 1, . . . , n − 1 (3.11)
where the polynomial Q2n(u) is defined in equation (3.3). To obtain equations of motion (3.10) for the BCS Hamiltonian one has to choose
xT = i(c1, . . . , cn−2, 2t + cn−1) (3.12)
while for the central spin model one has
xT = −iλ(t + c1, . . . , cn−2, cn−1) (3.13)
where c1, . . . , cn−1 are arbitrary constants. Differential equations (3.11) constitute a well-known mathematical problem called Jacobi’s inversion problem (see, for example, [27] and references therein). The solution of equations (3.11) can be expressed [34] through hyperelliptic Abelian functions—multiple variable generalizations of ordinary elliptic functions. These functions are often encountered as solutions of integrable equations and have well-known analytical properties. They are also implemented in standard mathematical software packages [35]. The Riemann theta function of genus g (in our case g = n − 1) is defined as the following sum over all g-dimensional integer vectors
θ (x|τ ) = ∑
m∈Zg
exp[iπ(mT τ m + 2xT m)] (3.14)
where τ = ω′ω−1, and ω and ω′ are g × g matrices to be specified below. Klenian σ - and ζ -functions of genus g are defined through the Riemann theta function as11
σ (x) = C exp[xT η(2ω)−1x]θ ((2ω)−1x|τ )
ζl(x) = ∂ ln σ (x)
∂ xl
. (3.15)
In our case, the g × g matrices ω and η (matrices of periods) that appear in the definition of hyperelliptic functions (3.14) and (3.15) are
2ωkl =
∮
bk
ul−1 du
√Q2n(u)
2ηkl = −
∮
bk
du
4√Q2n(u)
2n−l
∑
k=l+1
(k − l)αk+luk−1
(3.16)
where contours of integration bk go around branch cuts of a hyperelliptic curve z(u) =
√Q2n(u) as shown in figure 1. Matrices ω′ and η′ are also defined by equations (3.16) with the replacement of the contours of integration bk → hk (see figure 1). The solution [34] of differential equations (3.11) for arbitrary initial conditions states that functions up(x) are zeros of the following polynomial of a degree g = n − 1:
Rn−1(u, t ) = un−1 −
n∑−1
k=1
fk(x)uk−1 (3.17)
11 A more conventional definition of the σ -function is σ (x) = C exp[xT η(2ω)−1x]θ ((2ω)−1x − rτ ), where r is a vector of (Riemann) constants. In our case, this makes no difference since the vector r affects only constants ck in equations (3.12) and (3.13).


 7840 E A Yuzbashyan et al
E2g+1
E1
E2g
E2g-2
E2g-1
E2
E3
E0
b2
bg
hg
h2
h1
b1
Figure 1. Riemann surface of a hyperelliptic curve z(u) = √Q2n(u) of genus12 g = n−1 showing contours of integration bk and hk with k = 1, . . . , g. These contours appear in the definition of matrices of periods (3.16) of hyperelliptic functions. Contours bk go around g = n − 1 branch cuts connecting first 2g = 2n − 2 roots Ek of the spectral polynomial Q2n(u). Integration along the contours is clockwise. Note that since the spectral polynomial is positively defined the branch cuts are parallel to the imaginary axis.
where coefficients of Rn−1(u, t) are
fk(x) = ζk(x + d) − ζk(x − d) + ak. (3.18)
Here vector x is defined by equations (3.12) and (3.13) for the BCS and central spin problems, respectively. The argument of ζ -functions in equations (3.18) is shifted by a vector of constants d that has the following components:
dl =
∫∞
E0
ul−1 du
√Q2n(u) l = 1, . . . , n − 1 (3.19)
where E0 is one of the roots of the spectral polynomial Q2n(u) (see figure 1 and equation (3.4)). Note that, according to its definition (3.3), the spectral polynomial Q2n(u) depends only on integrals of motion and on parameters j and α. Finally, constants ak in equations (3.18) are obtained from the expansion
√√√√ 2∑n
k=0
αk
zk = 1
zn + a1
zn−1 + · · · + an−1
z + O(1) (3.20)
where αk are the coefficients of the spectral polynomial Q2n(u) defined by equation (3.4). For example, an−1 = α2n−1/2, an−2 = α2n−2/2 − α2
2n−1
/8, etc. To obtain quantum mechanical expectation values of original spins sj (t) = 2〈Kˆ j (t)〉 for central spin model (1.3) and pseudospins (2.2) for BCS model (1.2), we observe that, according to equation (3.8), they can be expressed through the polynomial Rn−1(u, t) given by expression (3.17). We have
s−
j (t ) = J−(t ) Rn−1( j , t )
Pn′ ( j ) . (3.21)
12 The genus is the number of handles on the Riemann surface of z(u) = √Q2n(u). The latter consists of two branches glued along n cuts (see figure 1). Each branch is a complex plane that is equivalent to a sphere. Because the two spheres are glued along n cuts, there are g = n − 1 handles.


 Solution for the dynamics of the BCS and central spin problems 7841
Recall that coefficients of the polynomial Pn(u), defined by equation (3.5), depend only on parameters j . Similarly, one can use an expression for the matrix element A(u) defined in equation (3.2) in terms of variables uj to obtain z-components of (pseudo)spins as functions of time. However, these components are not independent and can also be obtained from the equation
(sz
j
)2 + |s−
j |2 = s2
j = 1, where the sign of sz
j is determined by initial conditions. Integrating equations (3.9) and (3.10) for the evolution of x and y components of the total (pseudo)spin with the help of equation (3.18), we obtain
J−(t ) = cn e−iβt σ (x + d)
σ (x − d) (t) = gJ−(t) (3.22)
where the vector x is defined by equations ((3.12)) and ((3.13)). The frequency β is different for the BCS (βBCS) and central spin (β0) models
βBCS = gJz
2+
n∑−1
j =0
j β0 = a1λ, (3.23)
where λ and a1 are defined in equations (3.9) and (3.20) respectively. Average components of the electron (central) spin, s0(t) = 2〈Kˆ 0(t)〉 are obtained from equation (3.21) (recall that 0 = 0)
s−
0 (t) = c′
n[ζ1(x − d) − ζ1(x + d) − a1] σ (x + d)
σ (x − d) (3.24)
where c′n = (λcn)/B.
To summarize, quantum-mechanical averages of (pseudo)spins for the BCS and central spin models, including the electron (central) spin and the BCS gap function (t) are hyperelliptic functions (equations (3.14) and (3.15)) of the time variable and n − 1 constants ck (equations (3.21), (3.22) and (3.24)). These functions are specified by their matrices of periods ω, ω′ and η. The latter depend only on integrals of motion according to equations (3.3) and (3.16). The remaining n out of 2n initial conditions fix constants ck in equations (3.12) and (3.13). An important characteristic of a quasi-periodic motion is its (Fourier) frequencies. To determine the frequencies for the BCS and central spin models, we observe from equation (3.15) that the time variable enters the solution through combinations of ei kt , where
k = iπ ω−1
kg BCS
k = −iπ ω−1
k1 central spin
(3.25)
k = 1, . . . , g, and g = n−1. Note that, since the spectral polynomial Q2n(u) in equation (3.16) is positively defined, the matrix ω is pure imaginary and, therefore, frequencies k are real13 (see figure 1).
4. Degenerate solutions
Here we identify a class of ‘resonant’ nonstationary solutions for the BCS and central spin models with n degrees of freedom (n spins or pseudospins) but only m < n independent frequencies. While a typical dynamics of the BCS and central spin models with n (pseudo)spins is quasi-periodic with n independent frequencies, it is clear already on physical grounds that there
13 In addition to n − 1 frequencies k there is one more frequency that comes from the exponential prefactor in the σ -function (3.15). We were not able to find a simple expression for this frequency.


 7842 E A Yuzbashyan et al
must be solutions with fewer frequencies. For example, the only ‘spatial’ symmetry of the BCS ground state is the U (1) symmetry of the order parameter that translates into rotations of all pseudospins in Hamiltonians (2.1) and (2.6) around the z-axis. The corresponding trajectory in the phase space is a circle and, therefore, the motion is periodic with a single frequency (see also the discussion following equation (2.6) and below in this section). Generally, one can show [31] that there are (resonant) tori with an arbitrary number m < n of independent frequencies in a vicinity of any point in the phase space. It should be noted though that the set of points for which m < n has a zero measure in the phase space just like the set of rational numbers on the real axis. Moreover, such points are typically unstable [31] and provide seeds of chaotic behaviour in integrable systems. This occurs because small perturbations can destroy resonant tori and let the corresponding trajectories escape to other regions of the energy shell. In contrast, the majority of invariant tori with n independent frequencies are only slightly deformed by perturbations. Interestingly, for the resonant (degenerate) cases considered here we were able to reduce the BCS and central spin models with n spins to same models with only m spins. For example, solutions with m = 2 frequencies can be obtained from the BCS and central spin models for only two spins, etc. Further, we will see that one spin solutions (periodic trajectories) are special among degenerate solutions in that they correspond to the BCS energy spectrum. We start by determining conditions under which the number of independent frequencies is reduced. Since the frequencies are fixed by initial values of integrals of motion, degeneracies occur only for special values of the integrals. On the other hand, a complete information about integrals of motion is encoded in the spectral polynomial Q2n(u) defined in equations (3.3) and (3.4). Specifically, we have seen in the previous section that the number of frequencies
k is equal to the number of branch cuts of the hyperelliptic curve z(u) = √Q2n(u). Evidently, the latter decreases by one when two roots of the polynomial Q2n(u) coincide. Thus, as detailed below, merging 2(n − m) roots of Q2n(u) we obtain solutions with m < n frequencies. Indeed, consider a situation when 2(n − m) roots coincide, i.e. the spectral polynomial Q2n(u) in equation (3.3) has the following special form:
Q2n(u) = Q ̃2m(u)
n∏−1
k=m
(u − Ek)2 = Q ̃2m(u)W 2
n−m(u). (4.1)
We assume that double roots in equation (4.1) are complex conjugate to each other so that coefficients of polynomials Q ̃2m(u) and Wn−m(u) are real. Note that, since the polynomial Q2n(u) is positively defined (see the remark following equation (3.5)), so is the polynomial
Q ̃2m(u). We will see below that degenerate solutions are completely determined by the
‘residual’ spectral polynomial Q ̃2m(u). Now let us choose m − n separation variables uj to coincide with double roots of the polynomial Q2n(u), i.e.
uj = Ej j = m, . . . , n − 1
Wn−m(u) =
n∏−1
k=m
(u − Ek) =
n∏−1
j =m
(u − uj ). (4.2)
We observe that equations of motion for these variables are automatically satisfied because both sides of equations (3.9) and (3.10) vanish.


 Solution for the dynamics of the BCS and central spin problems 7843
Next, we use equations (4.1) and (3.3) to express eigenvalues of matrix L in terms of the residual spectral polynomial Q ̃2m(u) as follows,
v2(u) = α2


n∑−1
q=0
Cq u− q


2
Q ̃2m(u) (4.3)
where we expanded the ratio of polynomials Wn−m(u) and Pn(u) into elementary fractions
Wn−m(u)
Pn(u) =
n∑−1
q=0
Cq u− q
. (4.4)
Since the degrees of polynomials Wn−m(u) and Pn(u) differ by m, there are m constraints on the values of Cq, which can be derived by expanding equation (4.4) in 1/u. We have
n∑−1
q=0
Cq k−1
q = δkm k = 1, . . . , m. (4.5)
Values of Cq can be expressed through coefficients of Q ̃2m(u) by comparing residues at double poles at u = q in equations (3.3) and (4.3),
Cq = eq α
√Q ̃2m( q )
where eq = ±1. (4.6)
Note that equations (4.5) provide the following m constraints,
n∑−1
q=0
eq k−1
q
√Q ̃2m( q )
= αδkm k = 1, . . . , m (4.7)
on 2m coefficients of a positively defined polynomial Q ̃2m(u). Values of integrals of motion Hq for which degeneracies occur can be determined in terms
of coefficients of the residual spectral polynomial Q ̃2m(u) by comparing residues at simple poles at u = q in equations (3.3) and (4.3).
Hq = α2
n∑−1
j =0
′ Cq Cj Q ̃2m( q )
q− j
+ α2
2 C2
q Q ̃′
2m( q ). (4.8)
In particular, the value of H0—twice the energy14 of the central spin model on degenerate solutions is
E0 = h√α ̃0e0
n∑−1
q=1
Cj γj
4 + α ̃1
2α ̃0
(4.9)
where α ̃k are coefficients of Q ̃2m(u) defined as
Q ̃2m(u) ≡
2∑m
k=0
α ̃kuk α ̃2m = 1. (4.10)
The BCS energy EBCS ∝ ∑
q q Hq + const and the value of Jz ∝ ∑
q Hq can be obtained from the knowledge of Hq. However, a more convenient derivation is to compare expansions of equations (3.3) and (4.3) in powers of 1/u. We have
14 The factor of two arises because with the choice sp = 2〈 ˆKp〉 the value of classical Hamiltonians (2.6) and (2.9) is twice the value of their quantum counterparts (2.1) and (1.3).


 7844 E A Yuzbashyan et al
Jz + α
n∑−1
q=0
Cq m
q = − αα ̃2m−1
2 (4.11)
gEBCS = −
m−1
∑
q=0
Cq
(2 m+1
q + α ̃2m−1 m
q
) − α ̃2
2m−1
4 + α ̃2m−2. (4.12)
So far, we determined initial conditions for which the number of independent frequencies for a system with n (pseudo)spins drops from n to m. We saw that these conditions are fixed by the residual spectral polynomial Q ̃2m(u). Note that separation variables uj with j m are also fixed by this polynomial because they are zeros of equation (4.4). Thus, we are left with m dynamical variables—uj with j = 1, . . . , m − 1 and J−. Equations of motion (3.9) and (3.10) for these uj can be cast into a standard form (3.11) where n is now replaced with m and the original spectral polynomial Q2n(u) is replaced with
the residual polynomial Q ̃2m(u). On the other hand, it is clear that we would obtain similar equations of motion for m spins s ̃j governed by the BCS or central spin Hamiltonians. This
analogy can be made precise if we identify the residual polynomial Q ̃2m(u) with the spectral polynomial of a system of m spins (cf equation (3.3)), i.e.
v ̃2 = α2 +
m−1
∑
j =0
(
2H ̃j u −  ̃j
+ s ̃2
j
(u −  ̃j )2
)
= α2Q ̃2m(u)
P ̃2m(u) (4.13)
where we replaced parameters j with new ones
P ̃m(u) =
m−1
∏
q=0
(u − ̃q ) (4.14)
and chose  ̃0 = 0, consistent with the choice 0 = 0 (see below equation (3.10)). The rest of  ̃j are arbitrary real numbers. BCS (2.6) and central spin (2.9) Hamiltonians for new classical spins ̃sj are
H ̃BCS =
m−1
∑
j =0
2 ̃j s ̃z
j −g
2
J ̃+J ̃−  ̃J =
m−1
∑
q=0
s ̃q
H ̃0 =
m−1
∑
j =0
γ ̃j
2 s ̃0 · s ̃j − Bs ̃z
0 γ ̃j = 2
 ̃0 −  ̃j
.
(4.15)
Now, comparing equations of motion (3.9) and (3.10) for m separation variables u ̃j for new spins with those for the remaining variables uj for j = 1, . . . , m − 1 in the original problem with n spins, we see that they coincide if we re-scale the time variable for the central spin problem as follows:
t ̃= (−1)ne0
∏m−1
k=1  ̃m
B √α ̃0
t central spin
t ̃= t BCS.
(4.16)
No re-scaling is necessary for the BCS model. Further, analysing equations of motion for x and y components of the total spin (3.9) and (3.10), we conclude that they coincide for original and new spins, i.e.
J ̃− = J−.


 Solution for the dynamics of the BCS and central spin problems 7845
To express original n (pseudo)spins sj (t) = 2〈Kˆ j (t)〉 in terms of m new spins s ̃j (t ̃), we use equations (4.4) and (4.2) to rewrite the matrix element B(u) given by equation (3.7) as
B(u) = J−
m−1
∏
j =1
(u − uj )
n∑−1
q=0
Cq u− q
= B ̃(u)P ̃m(u)
n∑−1
q=0
Cq u− q
. (4.17)
Evaluating residues at u = j in equation (4.17), we obtain according to equation (3.8)
s−
j (t) = Cj P ̃m( j )
m−1
∑
q=0
s ̃−
j (t ̃)
j −  ̃q
(4.18)
where constants Cj are given by equation (4.6). Similarly, one can relate z-components of original spins to new ones
sz
j (t) = Cj P ̃m( j )

−α +
m−1
∑
q=0
s ̃z
q (t ̃)
j −  ̃q

 . (4.19)
The solution for new spins s ̃j (t ̃) as functions of time can be read off directly from the general solution—equations (3.21), (3.22) and (3.24) of the previous section. We only need to replace n with m, re-scale the time variable for the central spin model according to equation (4.16), and replace the spectral polynomial Q2n(u) with its reduced counterpart Q ̃2m(u) in the definition of matrices of periods (3.16) of hyperelliptic functions. For future reference, let us also write equations for components of original spins sj (t) = 2〈Kˆ j (t)〉 and evolution of J−(t) for degenerate solutions in terms of m variables u ̃j = uj . Evaluating residues at u = j in equation (4.17) and using equation (3.8), we find
s−
j = Cj J−
m−1
∏
j =1
( j − uj ). (4.20)
With the help of equations (4.1) and (4.20), evolution equations (3.9) and (3.10) for J− become
d ln J−
dt = (−1)mie0
√α ̃0
m−1
∏
j =1
uj central spin
d ln J−
dt = i

α ̃2m−1 + 2
m−1
∑
j =1
uj

 BCS.
(4.21)
We see that degenerate solutions with m < n frequencies can be parametrized by m auxiliary spins both for the BCS and central spin model. Therefore, corresponding trajectories live on an m-dimensional torus. By symmetry, for the same initial conditions, trajectories of all Hamiltonians Hq in system (2.8) live on the same torus. This implies, for example, that a slight change of initial values of integrals of motion (4.8) will induce small oscillations along the remaining n − m directions. Let us consider several examples of degenerate solutions.
One-spin solutions, m = 1. These solutions reproduce the BCS solution for the ground state and excitations of the BCS model (see also the discussion following equation (2.6)).


 7846 E A Yuzbashyan et al
Since the residual spectral polynomial is positively defined, we can parametrize it as Q ̃2(u) = (u − μ)2 + 2
0. For m = 1, there is only one condition in equation (4.7)
n∑−1
q=0
eq
√
( q − μ)2 + 2
0
= α eq = ±1. (4.22)
For the BCS model α = 2/g and we recognize equation (4.22) as the BCS gap equation. Similarly, equation (4.11) becomes the BCS equation for the chemical potential. The energy of BCS model (4.12) for m = 1 is
EBCS =
2 0
g − μJz −
n∑−1
j =0
ej
√
( j − μ)2 + 2
0. (4.23)
We see that a choice of signs ej = 1 for all j yields the BCS ground state energy, while if we choose one of ej to be negative, eq = −1 and ej = 1 for j = q, the solution corresponds to
a pair excitation of energy 2√( q−μ)2+ 2
0. Similarly, one obtains solutions with two and more excitations by choosing several signs ej to be negative. According to equations (4.15), the BCS and central spin models for m = 1 reduce to the following single spin models:
H ̃0 = −Bs ̃z
0 H ̃BCS = − g
2 s ̃+
0 s ̃−
0 . (4.24)
Then, equation (4.13) provides an alternative parametrization of the residual spectral polynomial Q ̃2(u)
Q ̃2(u) = u2 − 2s ̃z
0
α u + s ̃2
0
α2 . (4.25)
The solution of equations of motion is
J−(t) = s ̃−
0 (t ̃) = α 0 e−iβt+iφ (4.26)
where the frequency β is different for BCS (βBCS) and central spin (β0) models
βBCS = 2μ β0 = −e0
√
μ2 + 2
0
e0 = ±1.
Components of original spins sj (t) = 2〈Kˆ j (t)〉 are given by equations (4.18) and (4.19). We have
s−
j (t) = ej J−(t)
α
√
( j − μ)2 + 2
0
sz
j = − ej ( j − μ)
√
( j − μ)2 + 2
0
. (4.27)
Note that one-spin solutions constructed above do not minimize central spin Hamiltonian (2.9). Instead, we observe that in this case the configuration of spins with minimum energy is sz
j = −sgn γj . Similarly, we see from equations (2.8) that configurations that minimize
Hamiltonians Hq are sz
j = −sgn( q − j ). Interestingly, according to the definition of pseudospins (2.2), one of these configurations is the unperturbed Fermi ground state. Since


 Solution for the dynamics of the BCS and central spin problems 7847
all spins in these configurations are oriented along the z-axis, they are also stationary with respect to BCS Hamiltonian (2.6).
Two-spin solutions, m = 2. In this case there are two constraints (4.7) on four coefficients of
a positively defined polynomial Q ̃4(u).
n∑−1
q=0
eq
√Q ̃4( q )
=0
n∑−1
q=0
eq q
√Q ̃4( q )
= α eq = ±1
Q ̃4(u) =
4 ∑
k=0
α ̃kuk α ̃4 = 1.
Equations (4.9) and (4.12) show that the energy of these solutions can take arbitrary values in the range of energies allowed for the BCS and central spin models. The equivalent two-spin problems (4.15) are
H ̃BCS = 2 ̃1s ̃z
1 −g
2
J ̃+J ̃− H ̃0 = γ ̃0
2 s ̃0 · s ̃1 − Bs ̃z
0 . (4.28)
We are left with only one separation variable u1 =  ̃u1 and equations (3.11) now read
u ̇ 2
1 + 4Q ̃4(u1) = 0 BCS
α ̃0u ̇ 2
1 + Q ̃4(u1) = 0 central spin (4.29)
while for the total (pseudo)spin, using equation (4.21), we obtain
d ln J−
dt = ± √iα ̃0
u1 central spin
d ln J−
dt = iα ̃3 + 2iu1 BCS.
(4.30)
Components of individual spins can be expressed either through u1 and J− or in terms of new spins using equations (4.20) and (4.18)
s−
j = Cj J−( j − u1) = Cj ( j −  ̃1)s ̃−
0 ( t ̃) + Cj j s ̃−
1 ( t ̃). (4.31)
A special case of two-spin solutions when the four coefficients of a positively defined
polynomial Q ̃4(u) can be parametrized by three numbers, Q ̃4(u) = ((u − ω)2 + 2− + 2
+
)2 −
4 2− 2
+, has been previously discovered in [11]. The general two-spin solution is obtained from equations (4.29)–(4.31), which are solved by setting n = 2 (g = 1) in equations (3.17), (3.21) and (3.22) where hyperelliptic functions now become ordinary elliptic functions. Similarly, one can obtain three, four etc spin solutions (degenerate solutions with m = 3, 4 etc frequencies) in terms of hyperelliptic functions of genus g = 2, 3, etc. Degenerate solutions derived here are not all solutions with m < n independent frequencies. Indeed, it is clear that for a generic point in the phase space all roots of the spectral polynomial Q2n(u) are distinct and, by continuity, the distance to the closest point where two roots coincide is finite. On the other hand, there are points with any number of frequencies arbitrarily close to any point in the phase space. Other solutions with m < n frequencies can be constructed using the reduction theory for hyperelliptic functions [36]. Note also that degenerate solutions with m frequencies contain ones with fewer frequencies and can be further reduced to m − 1, m − 2, etc. Geometrically, they live on a 2m-dimensional surface in the 2n-dimensional phase space (see the remark below equation (4.21)). Surfaces with smaller m are embedded into ones with larger m. Interestingly, periodic trajectories that correspond to the BCS energy spectrum (m = 1) belong to all these surfaces.


 7848 E A Yuzbashyan et al
5. Applications and open problems
Our results can be applied to the problem of decoherence within the central spin model. In this case, we believe, a complete exact answer can be obtained. Another possible application is to experiments [2] on electron transport in spin blockaded semiconductor double dots. In this connection, it might be useful to analyse first a simpler setup of a single dot connected to two polarized leads. This setup leads [37] to an integrable model very similar to the central spin model. Further, it might be possible to use the BCS model (2.6) with few classical spins to describe a number of grains connected to each other by Josephson junctions. Other interesting applications include pairing phenomena in cold fermion gases [1] and in superconducting metals (see, e.g., the discussion in [29]). In these cases, a careful identification of observable robust features of the solution is needed. An interesting open problem is the evaluation of leading finite size (quantum) corrections to the general solution obtained in this paper.
Acknowledgments
We thank L Glazman and L Levitov for drawing our attention to the problem of determining the dynamics of the central spin and BCS models and for pointing out a number of relevant references. We are also grateful to them and to A Lamacraft, A Polyakov, N Saulina and P Wiegmann for interesting discussions.
References
[1] Zwierlein M W et al 2004 Phys. Rev. Lett. 92 120403 Regal C A, Greiner M and Jin D S 2004 Phys. Rev. Lett. 92 040403 [2] Ono K and Tarucha S 2003 Preprint cond-mat/0309062 [3] Fujisawa T et al 2002 Phys. Rev. Lett. 88 236802 Hanson R et al 2003 Phys. Rev. Lett. 91 196802
[4] Bardeen J, Cooper L N and Schriefer J R 1957 Phys. Rev. 108 1175
[5] Kopnin N B 2001 Theory of Nonequilibrium Superconductivity (Oxford: Clarendon) [6] Abrahams E and Tsuneto T 1966 Phys. Rev. 152 416 [7] Schmid A 1966 Phys. Kond. Mat. 5 302 [8] Gor’kov L P and Eliashberg G M 1968 Sov. Phys.—JETP 27 328 [9] Betbeder-Matibet O and Nozieres P 1969 Ann. Phys. 51 392 [10] Aronov A G et al 1981 Adv. Phys. 30 539 Aronov A G et al 1986 Nonequilibrium Superconductivity ed D N Landenberg and A I Larkin (Amsterdam: Elsevier) [11] Barankov R A, Levitov L S and Spivak B Z 2004 Phys. Rev. Lett. 93 160401 [12] Volkov A F and Kogan Sh M 1974 Sov. Phys.—JETP 38 1018 [13] Anderson P W 1959 J. Phys. Chem. Solids 11 26 [14] Kurland I L, Aleiner I L and Altshuler B L 2000 Phys. Rev. B 62 14886 [15] Sachdev S and Bhatt R N 1987 J. Appl. Phys. 61 4366 [16] Prokof’ev N V and Stamp P C E 1993 J. Phys.: Condens. Matter 5 L663 Prokof’ev N V and Stamp P C E 1995 Quantum Tunneling of Magnetization ed L Gunther and B Barbara (Dordrecht: Kluwer) [17] Khaetskii A V, Loss D and Glazman L 2002 Phys. Rev. Lett. 88 186802 Schliemann J, Khaetskii A and Loss D 2003 J. Phys.: Condens. Matter 15 R1809 [18] Erlingsson S I and Nazarov Yu V 2004 Preprint cond-mat/0405318 [19] Melikidze A, Dobrovitski V V, De Raedt H A, Katsnelson M I and Harmon B N 2004 Phys. Rev. B 70 14435 [20] Taylor J M, Imamoglu A and Lukin M D 2003 Phys. Rev. Lett. 91 246802 [21] Erlingsson S I, Jouravlev O N and Nazarov Yu V 2003 Preprint cond-mat/0309069


 Solution for the dynamics of the BCS and central spin problems 7849
[22] Richardson R W and Sherman N 1964 Nucl. Phys. 52 221 Richardson R W and Sherman N 1964 Nucl. Phys. 52 253 [23] Gaudin M 1972 Note CEA 1559 1 Gaudin M 1976 J. Phys. (Paris) 37 1087 Gaudin M 1983 La fonction d’onde de Bethe (Paris: Masson) [24] Cambiaggio M C, Rivas A M F and Saraceno M 1997 Nucl. Phys. A 424 157 [25] Anderson P W 1958 Phys. Rev. 112 1900 [26] Richardson R W 1977 J. Math. Phys. 18 1802
[27] Belokolos E D et al 1994 Algebro-geometric Approach to Nonlinear-integrable Equations (Berlin: Springer) Mumford D 1983, 1984 Tata Lectures on Theta vols 1–2 (Basle: Birkhauser) [28] Galaiko V P 1972 Sov. Phys.—JETP 34 203 [29] Gal’perin Yu M, Kozub V I and Spivak B Z 1981 Sov. Phys.—JETP 54 1126 [30] Yuzbashyan E A, Baytin A A and Altshuler B L 2005 Phys. Rev. B 71 094505
[31] Arnold V I 1978 Mathematical Methods of Classical Mechanics (New York: Springer) Tabor M 1989 Chaos and Integrability in Nonlinear Dynamics (New York: Wiley) [32] Sklyanin E K 1989 J. Sov. Math. 47 2473
Sklyanin E K 1995 Prog. Theor. Phys. Suppl. 118 35 [33] Kuznetsov V B 1992 J. Math. Phys. 33 3240 [34] Eilbeck J C, Enolskii V Z and Holden H 2003 Proc. R. Soc. A 459 1581 Abenda S and Fedorov Ju 2000 Acta. Appl. Math. 60 137 [35] See, e.g., Maple v. 8 and higher and B. Deconinck et al 2002 Preprint nlin.SI/0206009 [36] Belokolos E and Enolskii V Z 2001 J. Math. Sci. 106 3395 Belokolos E and Enolskii V Z 2002 J. Math. Sci. 108 295 [37] Altshuler B L, Glazman L and Yuzbashyan E A unpublished
