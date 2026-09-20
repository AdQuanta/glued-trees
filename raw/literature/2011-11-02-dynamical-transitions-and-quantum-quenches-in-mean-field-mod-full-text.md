# Dynamical transitions and quantum quenches in mean-field models - Full Text

> Source: https://iopscience.iop.org/article/10.1088/1742-5468/2011/11/P11003
> Collected: 2026-09-20
> Published: 2011-11-02
> Zotero parent key: 2N8JBRJZ
> Evidence: Zotero indexed PDF text

Journal of Statistical Mechanics: Theory and Experiment
Dynamical transitions and quantum quenches in mean-field models
To cite this article: Bruno Sciolla and Giulio Biroli J.Stat.Mech. (2011) P11003
View the article online for updates and enhancements.
You may also like
Mean-field theory of meta-learning Dariusz Plewczynski

Exact thermodynamic theory of an ideal boson gas in a one-dimensional harmonic trap Ze Cheng

Inhomogeneous quantum quenches Spyros Sotiriadis and John Cardy

This content was downloaded from IP address 77.137.64.243 on 07/11/2024 at 21:23


 J.Stat.Mech. (2011) P11003
ournal of Statistical Mechanics:
J
Theory and Experiment
Dynamical transitions and quantum
quenches in mean-field models
Bruno Sciolla and Giulio Biroli
Institut de Physique The ́orique, CEA/DSM/IPhT-CNRS/URA 2306 CEA-Saclay, F-91191 Gif-sur-Yvette, France E-mail: bruno.sciolla@cea.fr and giulio.biroli@cea.fr
Received 25 August 2011 Accepted 15 October 2011 Published 2 November 2011
Online at stacks.iop.org/JSTAT/2011/P11003 doi:10.1088/1742-5468/2011/11/P11003
Abstract. We develop a generic method to compute the dynamics induced by quenches in completely connected quantum systems. These models are expected to provide a mean-field description at least of the short-time dynamics of finitedimensional systems. We apply our method to the Bose–Hubbard model, to a generalized Jaynes–Cummings model, and to the Ising model in a transverse field. We find that the quantum evolution can be mapped onto a classical effective dynamics, which involves only a few intensive observables. For some special parameters of the quench, peculiar dynamical transitions occur. They result from singularities of the classical effective dynamics and are reminiscent of the transition recently found in the fermionic Hubbard model. Finally, we discuss the generality of our results and possible extensions.
Keywords: quantum phase transitions (theory), stationary states, optical lattices
©c 2011 IOP Publishing Ltd and SISSA 1742-5468/11/P11003+29$33.00


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Contents
1. Introduction 3
2. Summary of the method and results 3
3. Definition of the models 5 3.1. Bose–Hubbard model and the Mott–superfluid transition . . . . . . . . . . 5 3.2. Generalized Jaynes–Cummings model and super-radiance transition . . . . 6 3.3. Ising model in a transverse field and the ferromagnetic transition . . . . . . 7
4. Quantum quenches in completely connected models: mapping to an effective classical dynamics 7 4.1. Site permutation symmetry and classical Hamiltonian dynamics . . . . . . 7
5. Effective classical Hamiltonian equations in the Bose–Hubbard model with truncation nmax
b =2 9
5.1. Schro ̈dinger equation in the site-permutation symmetric basis and effective Hamiltonian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 5.2. Nature of the ground state and quantum phase transition . . . . . . . . . . 10 5.3. Effective classical evolution of wavepackets . . . . . . . . . . . . . . . . . . 11 5.4. Different effective trajectories in the phase space . . . . . . . . . . . . . . . 13
6. Sudden quenches in the Bose–Hubbard model for nmax
b = 2 15
6.1. Mott to superfluid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 6.2. Superfluid to Mott . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 6.3. Superfluid to superfluid Ud < Uf < Uc . . . . . . . . . . . . . . . . . . . . . 16 6.4. Superfluid to superfluid Uf < Ud . . . . . . . . . . . . . . . . . . . . . . . . 17
7. Bose–Hubbard model with weaker truncation nmax
b ≥ 3 18
7.1. Hamiltonian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 7.2. Regularity of trajectories after a quench . . . . . . . . . . . . . . . . . . . 18 7.3. Dynamical transition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
8. Quenches in the generalized Jaynes–Cummings model for superradiance transition 20 8.1. Super-radiance quantum phase transition . . . . . . . . . . . . . . . . . . . 20 8.2. Sudden quenches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
9. Quenches in the Ising model in a transverse field 23
10.Discussion 24
11.Summary and outlook 25
Acknowledgments 26
Appendix A. Gutzwiller ansatz 26
Appendix B. Eigenstates in completely connected models 28
References 28
doi:10.1088/1742-5468/2011/11/P11003 2


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
1. Introduction
Thanks to the fast experimental progress on cold atoms [1]–[3], where direct control over the parameters of the effective Hamiltonian is available, many theoretical questions about out-of-equilibrium dynamics of quantum systems have been raised and started to be addressed. Among them, we cite the problem of thermalization for an isolated system (see, e.g., [4, 5]) the existence of long-lived out-of-equilibrium states (see, e.g., [6]–[9]), dynamical transitions out of equilibrium [10]–[13], etc. In this work we focus on the off-equilibrium dynamics induced by quantum quenches, i.e. the evolution of an isolated quantum system after a sudden change of a parameter of the Hamiltonian. This problem has been intensively studied these last few years. It provides an useful idealization of the protocols followed in experiments, where the change of parameters takes place instead at finite rates. The literature on quantum quenches is already quite broad, see, for example, the reviews [14]–[16]. One-dimensional systems have been intensively studied by exact analytical and numerical methods. Results for higher-dimensional systems are instead scarcer; the previous methods cannot be applied and one has to resort to approximations of some kind. The ones that have been more often used are the Bogoliubov method [17], path integral saddle point expansions [18, 19], the large-N limit [20] and mean-field (or large dimension) approximations [21], [10]–[12], [22]. Interestingly, mean-field approaches revealed that quantum quenches may lead to out-ofequilibrium dynamical transitions. This was first found in the analysis of the fermionic Hubbard model by time-dependent dynamical mean-field theory (t-DMFT) in [10]. Later, a confirmation and explanation of this result was found by using a Gutzwiller timedependent ansatz in [11]. In [12] we solved the Bose–Hubbard model on a completely connected lattice and found a very similar dynamical transition at integer fillings. This was also noticed in the hard-core Bose–Hubbard model in a superlattice potential [23]. Finally, clues to argue that these dynamical transitions are generic even beyond the mean field were recently presented in [13] by mapping the problem to the one of classical phase transitions in films. In this paper we first describe a generic approach to solve the dynamics of quenches in completely connected quantum models. Then, we apply our method to the Bose–Hubbard model, the generalized Jaynes–Cummings model and the Ising model in a transverse field. We find that the dynamical transition, discovered for the Hubbard model, is a systematic dynamical effect present in completely connected systems characterized by a quantum phase transition in equilibrium. A shorter version of this work, that focused only on the Bose–Hubbard model, appeared in [12].
2. Summary of the method and results
In this paper, we focus on the out-of-equilibrium dynamics in several completely connected models: the Bose–Hubbard model (BHM), the transverse field Ising model (IM) and the Jaynes–Cumming model (JCM). The reason for focusing on systems defined on completely connected graphs is that this allows one to study a well-defined model and—at the same time—to obtain an approximate solution for finite-dimensional lattices. Indeed, such models are related to several approximations used in the literature. Among the most well-known ones, we cite the limit of infinite dimensions for models defined on a hyper
doi:10.1088/1742-5468/2011/11/P11003 3


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
cubic d-dimensional lattice1 and the Gutzwiller ansatz, a widespread method to obtain mean-field equations. Actually, in the case of completely connected models, the Gutzwiller ansatz can be shown to be exact by using a Hubbard–Stratonovich transformation. We shall focus on out-of-equilibrium dynamics induced by a quantum quench. This procedure is defined as follows. Let Hˆ (λ) be the quantum Hamiltonian, which depends on a coupling λ. The system is prepared in its ground state |ψ(t < 0)〉 = |GS(λi)〉 at some coupling λi. At t ≥ 0, the system is driven out of equilibrium in a controlled fashion, tuning the coupling λ(t) in time according to a predefined procedure. Except for quasistatic procedures, often called ‘adiabatic’, the wavefunction becomes different from the ground state |ψ(t > 0)〉 = |GS(λ(t))〉. We call sudden quench the procedure in which the coupling is suddenly switched to a final value λf: λ(t) = (λf − λi) θ(t) + λi. As we shall show, the quantum dynamics in a completely connected system can be solved by mapping the unitary evolution onto an effective model undergoing Newtonian dynamics. This is a drastic simplification which is possible thanks to the symmetry of the completely connected Hamiltonian under any permutation of sites. We restrict our analysis to cases where |ψ(t = 0)〉 is the ground state at some coupling λi. Thus, |ψ(t = 0)〉 is also symmetric under permutation of sites and, since both the initial state and the Hamiltonian are symmetric, the generic unitary evolution takes place in the sector of symmetric states only. In this subspace, the states are parameterized using a few local macroscopic observables. The unitary evolution can then be written as a Schro ̈dinger equation in the symmetric space, which involve an effective ħ = V −1, where V is the number of sites of the system. Thanks to this property, at the thermodynamic limit, the entire dynamics of the system can be encoded in one of a few macroscopic variables, which undergo an effective classical Hamiltonian evolution. We first apply this approach to the Bose–Hubbard model, our main interest because of its applicability to cold atom experiments. In this case, it is the on-site repulsion U that plays the role of the coupling λ. In the first stage we make the additional assumption that the number of bosons per site is less than or equal to nmax
b = 2. The average
superfluid order after the quench is a non-monotonic function of |Uf − Ui|. Actually, it decays logarithmically to zero at some special values of Ui and Uf . For these special quenches, the superfluid order relaxes exponentially to zero. We call this peculiar feature a dynamical transition. Surprisingly, the microcanonical equilibrium characterized by the same energy, towards which the system would relax on large times if it were able to thermalize2, has non-zero superfluid order. Thus, this transition is a purely dynamical phenomenon, which has nothing to do with the fact that the superfluid order vanishes in the high temperature phase. We extend our analysis to nmax
b ≥ 3. In this case the
effective dynamics involves nmax
b − 1 degrees of freedom and the classical trajectories can be either regular or chaotic. Apart from this difference, the dynamical transition is found to be qualitatively unchanged and the quantitative differences with nmax
b = 2 are small. Finally, we focus on two other systems, for which some out-of-equilibrium properties have already been studied, a generalized Jaynes–Cummings model [25] and the Ising model
1 This consists in a technique similar to the ones developed in [24].
2 Thermalization is very likely to occur in finite dimensions for the Bose–Hubbard model, because the system is not integrable. Instead, for completely connected models we do not expect thermalization to the Gibbs ensemble, as we shall discuss later. This implies that in the large dimension limit the timescale for equilibration diverges as a function of d.
doi:10.1088/1742-5468/2011/11/P11003 4


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
in a transverse field [21]. We apply our formalism to both systems and show that also in these cases there is a dynamical transition for sudden quenches. This paper is organized as follows: in section 3, we briefly describe the three considered models. In section 4, we describe how the effective classical dynamics can be derived for an arbitrary Hamiltonian. Then in section 5 we derive the classical dynamics for the Bose–Hubbard model with truncation nmax
b = 2 and analyze quenches and the dynamical
transition in section 6. The general case nmax
b ≥ 3 is considered in section 7. The effective dynamics and quench properties of the generalized Jaynes–Cummings model are described in section 8 and in section 9 for the Ising model. Sections 10 and 11 contain discussions and possible extensions of our work. Appendix A is devoted to prove that the same effective dynamics is recovered with a Gutzwiller ansatz wavefunction and in appendix B the WKB eigenstates of the completely connected model are discussed.
3. Definition of the models
3.1. Bose–Hubbard model and the Mott–superfluid transition
The Bose–Hubbard lattice model has regained a lot of interest recently since it can be realized and studied in experiments on cold atoms [26]. The Hamiltonian of its completely connected version, suited to describe the limit d → ∞ of the lattice model, is
H=U
2
∑
i
ni(ni − 1) − J
V
∑
i=j
b†
jbi (1)
where b†
i , bi are the bosonic creation and annihilation operators, satisfying [bi, b†
j ] = δij
and ni = b†
i bi. The first term is an on-site repulsion between bosons, the second is a tunneling term, of amplitude J, and rescaled by the volume V (number of sites). This rescaling is needed to obtain a well-defined thermodynamic limit V → ∞. The limit of infinite dimensions that is equivalent to this model is obtained by taking a coupling J/2d for a BHM defined on a d-dimensional hyper-cubic lattice. This model undergoes a quantum phase transition at commensurate fillings: 〈nˆi〉 = n with n integer. See [27] for a detailed discussion of the phase diagram. Notice that, since we consider the dynamical behavior, the number of particles is fixed because it corresponds to a quantity conserved by the dynamics. In consequence we shall discuss the phase diagram in terms of the density and not the chemical potential, as it is instead done usually. Let us focus first on cases where the number of particles per site is an integer. To grasp why there is a quantum phase transition, it is helpful to compare the ground state in the two limits U → ∞ (or J = 0) and U → 0. In the first case, the ground state is diagonal in the occupation number |ψ〉 = ⊗i|ni = n〉. It remains the same for all U > Uc and is called a Mott insulator. It is incompressible because adding or removing a boson requires an energy of the order of U. In the second case, U = 0, the ground state is akin
to3 a product of coherent states |ψ〉 = C ∏
i e−αb†
i |0〉. For U = 0, and also moderate values
of U, the ground state is superfluid and compressible. The usual order parameter 〈ˆbi〉 is zero because the density is fixed, hence the appropriate parameter is the off-diagonal long
3 Formally, this state is the true ground state only in the grand canonical ensemble. However, the canonical and grand canonical ensemble are equivalent up to 1/V corrections.
doi:10.1088/1742-5468/2011/11/P11003 5


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
range order measured by |Ψ0|2 = limdij→∞〈ˆb†
jˆbi〉. In the completely connected model, all distances dij between two different sites are equal to 1. This is the largest distance in the
problem. As a consequence one can define4
|Ψ0|2 = 〈ˆb†
jbˆi〉 i = j. (2)
Because the system is completely connected, phonons are absent and the spectrum always has a gap. Beyond a critical coupling Uc, the order parameter |Ψ0|2 vanishes and the ground state becomes a Mott insulator. This is the Mott–superfluid quantum phase transition. For non-integer fillings, the system is instead always superfluid and compressible as it can be understood considering perturbation around the U → ∞ limit. At non-zero temperature, there is a second-order phase transition from the superfluid phase to a Bose gas at a critical temperature Tc(U).
3.2. Generalized Jaynes–Cummings model and super-radiance transition
The second model that we consider is the generalized Jaynes–Cummings model studied in [25], which describes N distinguishable two-level systems in interaction with a single quantized electromagnetic mode. It is useful in various contexts and has been suggested as a qualitative description of the BEC/BCS crossover in fermionic condensates, of molecular magnetism and of the formation of dimers by the pairing of two bosons. Recently, new experiments in the setting of cavity quantum electrodynamics [28] are realizations of the Dicke Hamiltonian [29], which can be mapped onto the Jaynes–Cummings Hamiltonian if the ‘rotating wave approximation’ is made. The dynamics of sweeps, starting from an empty bosonic mode, was studied in [25] using quasiclassical approximations and the truncated Wigner approximation. Here, we describe the dynamics of sudden quenches from the broken symmetry phase. The model is defined as follows. There is one bosonic [ˆb, ˆb†] = 1 degree of freedomthe electromagnetic mode—and one SU(2) spin S = N/2. The spin degree of freedom keeps track of the number of excited two-level systems, nexc = Sz + N/2. With ˆn = ˆb†ˆb, the Hamiltonian is
Hˆ = ω0Sˆz + ωˆn + √gN (ˆb†Sˆ− + ˆbSˆ+). (3)
It includes a potential energy for bosons (ω), for the spin (ω0), and a coupling g between the two. Each time a boson is lost, a two-level system is excited, and reciprocally: the quantity Qˆ = Sˆz+ˆb†bˆ is conserved by the dynamics. It is thus possible to define 2λ = ω0−ω such that up to a constant term one finds
Hˆ = −2λnˆ + √gN (ˆb†Sˆ− + ˆbSˆ+). (4)
In the following we take g = 1 and consider λ in units of g and the time in units of ħ/g. We consider the regime Q ≥ N/2 (which can be reduced to Q = N/2), for which there is a quantum phase transition. At T = 0, the system is in the normal ground state 〈nˆ〉 = 0 if λ < λc = −1 and is in the super-radiant ground state for λ > λc, where 〈nˆ〉 = 0. This is the super-radiance quantum phase transition. This transition is the
4 In equilibrium, it is easy to check that the definition below gives back the usual one used in the grand canonical ensemble, |Ψ0|2 = |〈b〉|2.
doi:10.1088/1742-5468/2011/11/P11003 6


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
consequence of the competition between the two terms in the Hamiltonian: the first one favors removing bosons (if λ < 0), whereas the second plays the role of a kinetic energy and it can lower the energy if the bosons modes are filled, see section 8. As for the BoseHubbard model, there is a finite-temperature phase transition at Tc(λ), above which the super-radiant phase disappears. Notice that this phase transition is usually studied in the canonical/microcanonical ensemble, whereas here it is more natural to focus on a given value of Q since this quantity conserved by the dynamics.
3.3. Ising model in a transverse field and the ferromagnetic transition
The Ising model in a transverse field is a paradigm of quantum phase transitions [30]. The Hamiltonian of its completely connected version is
Hˆ = − J
2N
∑
ij
SˆizSˆjz − Γ
∑
i
Sˆix (5)
where J is the ferromagnetic coupling and Γ the transverse field. For simplicity, we set J = 1, measure Γ in units of J and time in units of ħ/J. The Hamiltonian can be written
using a single spin Sˆ = ∑
i Sˆi and is
Hˆ = − 1
2N (Sz)2 − ΓSx (6)
The large N limit corresponds to the large spin S = N/2 limit, which is also the classical limit. The ground state is found, minimizing the corresponding classical Hamiltonian5
Sˆ → S = S{sin θ cos φ, sin θ sin φ, cos θ} [21]. The minimum is at φ = 0, and for Γ < 1/2, sin θ = 2Γ, which is a ferromagnetic ground state, in which the spins align towards the z axis. For Γ > 1/2, θ = π and the ground state is called a quantum paramagnet, because
it is unoriented in the z basis |±〉i, |ψ〉 = 1/√2V ⊗i (|+〉i + |−〉i). The quantum phase transition from z-ferromagnet to quantum paramagnet takes place at Γc = 1/2. Starting from the ferromagnetic ground state and increasing the temperature the system undergoes a second-order phase transition at a finite temperature Tc(Γ).
4. Quantum quenches in completely connected models: mapping to an effective classical dynamics
4.1. Site permutation symmetry and classical Hamiltonian dynamics
In the following, we show how the dynamics induced by quantum quenches, in arbitrary completely connected models, can be mapped onto an effective classical Hamiltonian dynamics. As already stated, any model defined on a completely connected lattice has a Hamiltonian which is symmetric under any permutation of sites. Thus, one expects that the ground state of the model is also site permutation symmetric6. We shall study quenches starting from the ground state of the system. Since the site permutation symmetry is conserved by the unitary evolution, the dynamics only takes place into the
5 The kinetic term of the classical limit is nontrivial to obtain, but we do not need it for the moment.
6 This symmetry may be spontaneously broken in systems with attractive interactions, which we do not consider here.
doi:10.1088/1742-5468/2011/11/P11003 7


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
subspace of symmetric wavefunctions. This is a drastic simplification, because symmetric states can be described using a few variables only. To clarify this point in a concrete but simple case, let us see what these variables are for the Bose–Hubbard model, with the additional constraint that there are nmax
b = 2 or
less bosons per site. First, remark that, given a particular Fock state |{ni}〉, the linear combination of every possible site-permuted Fock state is a site-permutation symmetric
state |S({ni})〉 ∼ ∑
P |{nP (i)}〉. This new state is completely characterized by the fraction x0, x1, x2 of sites with zero, one and two bosons, respectively, and we call it |x0, x1, x2〉 = |x〉, where x is a shorthand for all variables. Since the Fock states form a basis of generic states, the {|x〉} states form a basis of the symmetric sector. In order to express the Schro ̈dinger evolution in this basis, we have to compute the transitions elements 〈x′|Hˆ |x〉. Typically, only a few transitions Wm(x) = −(1/V )〈x + m/V |Hˆ |x〉 are
allowed7, with m = {m0, m1, . . .} a vector of integers. For example in the Bose–Hubbard model, the matrix elements of the Hamiltonian connect states that differs by one boson jump. Thus x0, x1 and x2 can only differ by 1/V or 2/V . For example, after a jump
|2i . . . 0j . . .〉 → |1i . . . 1j . . .〉, x′1 = x1 + 2/V , x′0 = x0 − 1/V and x′2 = x2 − 1/V . This transition is labeled m = {m0 = −1, m1 = 2, m2 = −1}. Moreover, the reverse move is a transition characterized by −m, with the same amplitude W−m(x) = Wm(x) at dominant order in V . Thanks to the ‘locality’ of transition elements between symmetric states, the
Schr ̈odinger equation in the symmetric basis |ψ〉 = ∑
x ψx(t)|x〉 takes a simple form.
The Schr ̈odinger equation projected on 〈x| is 〈x|i∂t|ψ〉 = 〈x|H|ψ〉. Denoting the diagonal transition element D(x) = (1/V )〈x|H|x〉, we get
i∂tψx = V D(x)ψx − V
∑
m
Wm(x)(ψx+m + ψx−m)
=V
(
D(x) − 2
∑
m
Wm(x) cosh(mi∂xi/V )
)
ψx (7)
where we made use of ψx+m/V = exp(mi∂xi/V )ψx with an implicit summation over the index i. Strikingly, the Schr ̈odinger equation (7) involves an effective ħ = 1/V ; thus the regime of interest V → ∞ corresponds to the classical regime. Furthermore, for
the ground state, the initial wavefunction is a narrow wavepacket of width 1/√V (this general property is discussed in more detail for the Bose–Hubbard model in section 5.2). Thus, by the Heisenberg uncertainty principle, we expect that momentum fluctuations
are proportional to √ħ ∝ √1/V . Therefore the evolution of the wavepacket can be fully described in the thermodynamic limit by its average (or center) x(t) = 〈xˆ〉 and average momentum p(t) = 〈pˆ〉. Both quantities evolve following a classical Hamiltonian dynamics obtained from the quantum one by replacing pˆ = (i/V )∂x → p(t) and xˆ → x(t):
i
V ∂tψx = (Dx − 2Wx cosh(2∂x/V ))ψx =
(
Dx − 2
∑
m
Wm(x) cos(mipˆi)
)
ψx = Hˆ ψx (8)
H[x, p] = D(x) − 2
∑
m
Wm(x) cos(mipi). (9)
7 The minus sign in this definition is for later convenience.
doi:10.1088/1742-5468/2011/11/P11003 8


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
The classical Hamiltonian evolution of the variables x ̇ i(t) = ∂H/∂pi and p ̇i(t) = −∂H/∂xi yields the evolution of the wavepacket after the quantum quench, and give access to all observables as a function of time. A more careful analysis is performed in section 5.3 and fully supports this picture. As a conclusion, the analysis of quench dynamics in connected models is tractable and takes the form of an effective classical Hamiltonian evolution. The initial condition is provided by the ground state values of xi, pi at the initial coupling Ui. The sudden quantum quench dynamics is then described by the classical dynamics of x(t), p(t) induced by the effective Hamiltonian H(Uf), with initial conditions xi, pi.
5. Effective classical Hamiltonian equations in the Bose–Hubbard model with truncation nmax
b =2
In the following, we study the Bose–Hubbard model with two or less bosons per site. We derive explicitly the effective classical Hamiltonian in section 5.1. The nature of the ground state, in particular the peaking of the wavepacket when V → ∞ and the quantum phase transition, are discussed in section 5.2. A more thorough derivation of the effective Hamiltonian dynamics is presented in section 5.3. Finally, we conclude by describing the phase space of effective trajectories in section 5.4.
5.1. Schr ̈odinger equation in the site-permutation symmetric basis and effective Hamiltonian
In this section, the method sketched above is applied to the Bose–Hubbard model with truncation nb ≤ nmax
b = 2. This restriction is well suited to derive analytical expressions and preserves the main features of the model, such as the Mott insulator to superfluid quantum phase transition. The case of a larger number of bosons per site is considered in section 7. The results remain qualitatively the same. The symmetric states are written in the form |x0, x1, x2〉. Since the total number of sites V = V (x0 + x1 + x2) is fixed, and the overall density of bosons n = N/V = x1 + 2x2 is conserved by the dynamics, the symmetric states can be labeled by one variable only. Choosing x1 as such a variable, the symmetric normalized wavefunctions are denoted
|x1〉 = (N0!N1!N2!/V !)1/2 ∑′
{ni} |n1, n2, . . . , nV 〉, where Ni = V xi and ∑′ means the sum
over Fock states of fixed fraction x1. In the following for simplicity of notation we drop the subindex 1 and use x instead of x1. Note that, contrary to the previous paragraph, x is now just a number and not a vector. To compute the transition rates, we proceed as follows. The repulsion term
1/2 ∑
i ni(ni − 1) is diagonal in the |x〉 basis. The tunneling term −1/V ∑
i=j b†
jbi allows transitions from |N0, N1, N2〉 to three states, |N0 −1, N1 +2, N2 −1〉, |N0 +1, N1 −2, N2 +1〉 and |N0, N1, N2〉. Using the previous notations, the only possible transitions correspond to m = 2, m = −2, m = 0 representing, respectively, 〈x + 2/V |Hˆ |x〉, 〈x − 2/V |Hˆ |x〉 and 〈x|Hˆ |x〉. The first amplitude is
〈x + 2/V |Hˆ |x〉 =
( (N0 − 1)!(N1 + 2)!(N2 − 1)!
V!
N0!N1!N2!
V!
)1/2 ′ ∑
{n′i}
〈{n′i}|Hˆ
∑′
{ni }
|{ni}〉.
(10)
doi:10.1088/1742-5468/2011/11/P11003 9


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
There are V !/(N0!N1!N2!) factors on the ket side. For each of these factors, there
are N0N2 transitions to a state with N1′ = N1 + 2. Therefore using that b†
i bj|0i〉|2j〉 =
√2|1i〉|1j〉, and after a partial cancellation of the normalization factors, we obtain
〈x + 2/V |Hˆ |x〉 = −√2
V [N0N2(N1 + 1)(N1 + 2)]1/2. (11)
In the following, only dominant contributions of order V are kept; the sub-leading ones are dropped since they do not matter for dynamics taking place on times not diverging with the system size. Rewriting x0 and x2 as functions of x, the transition rates are
〈x − 2/V |Hˆ |x〉 = −V x[(2 − x − n)(n − x)/2]1/2 ≡ −V Wˆ x
〈x|Hˆ |x〉 = V U(n − x)/2 − V x(2 + n − 3x)/2 ≡ V Dˆx
〈x + 2/V |Hˆ |x〉 = 〈x − 2/V |Hˆ |x〉.
(12)
The Schr ̈odinger evolution on ψx(t) in the site-permutation symmetrical basis is 〈x|i∂t|ψ〉 = 〈x|H|ψ〉:
i∂tψx = V Dˆ xψx − V Wˆ x(ψx+2/V + ψx−2/V )
= V (Dˆx − 2Wˆ x cosh(2∂x/V ))ψx
= (Dˆx − 2Wˆ x cos(2pˆ))ψx. (13)
Therefore we have obtained that the Hamiltonian in the subspace of symmetric states is
Hˆ = Dˆx − 2Wˆ x cos(2pˆ). (14)
Note that the dimension of the Hilbert space has been reduced from eV to V in this case. The case nmax
b = 2 is especially convenient because the effective classical motion takes place in one dimension; therefore the equation of motion are integrable and the evolution easy to understand and describe.
5.2. Nature of the ground state and quantum phase transition
As in section 4, the Schr ̈odinger equation (13) involves an effective ħ = 1/V and its classical limit is obtained through xˆ → x(t) and pˆ → p(t):
H[x, p] = D(x) − 2W (x) cos(2p). (15)
The possibility of describing the quantum dynamics after a quench in terms of classical dynamics relies on the fact that the initial wavefunction is initially of small
width (∼1/√V ). In order to check this, let us first expand the eigenvalue equation at lowest order in 1/V :
Eψx =
(
Dˆ x − 2Wˆ x − 4Wˆ x
V 2 ∂x2
)
ψx.
Since the kinetic term has a factor 1/V 2 in front, the ground state corresponds to the minimum of Dx − 2Wx and small quantum fluctuations around it. Indeed, around the minimum, xGS, a quadratic expansion of Wx and Dx maps this problem onto a quantum
harmonic oscillator with m = WxGS/8 and ω = √∂x2(D − 2W )|xGS/m. Thus, we find
doi:10.1088/1742-5468/2011/11/P11003 10


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
that the ground state wavefunction is centered around the absolute minimum xGS of the
potential D(x) − 2W (x) and has a width σ ∼ √ħ/mω, which is of the order of 1/√V . An appropriate expression for any eigenstate is provided by the WKB expansion given in appendix B. The quantum phase transition taking place as a function of U can be recovered within this formalism as we now show. We recall that, for the Bose–Hubbard model, the quantum phase transition and the Mott phase are present at commensurate fillings only, so we have to focus on n = 1 for nmax
b = 2. The ground state of the quantum Hamiltonian corresponds to the global minimum of the effective Hamiltonian (15), given by ∂H/∂x = ∂H/∂p = 0. These equations lead to p = 0 and x equal to the value xGS, which verifies ∂(D(x) − 2W (x))/∂x = 0. It is easy to check that
xGS =
⎧⎨
⎩
1 if U ≥ Uc, Mott insulator ground state
U/Uc + 1
2 < 1 if U < Uc, superfluid ground state (16)
where Uc = 3 + 2√2 5.828 43 (note that x ≤ 1). In the thermodynamic limit, the Mott insulator ground state is |n0 = 1, n1 = 1 · · ·〉 = |x = 1〉. Instead the superfluid ground state is |x = x0〉, with 1/2 < x0 < 1. Therefore, in the superfluid state, a
fraction of sites x2 = (1 − xGS)/2 > 0 contain two bosons. |Ψ0|2 = 1/V 2〈∑
ij b†
i bj 〉 is proportional to the intensive kinetic energy, and can be computed using the identity
|Ψ0|2 = −1/J(E − U/2〈∑
i ni(ni − 1)〉) = xGS(1 − xGS)Uc/2. It is the order parameter for the transition: it is positive in the superfluid phase and vanishes in the Mott insulating one.
5.3. Effective classical evolution of wavepackets
In the following we show in detail how the classical Hamiltonian dynamics emerges from the quantum evolution of symmetric states in the thermodynamic limit. For simplicity we consider the situation of section 5, where nmax
b ≤ 2, but the argument is more general. The Schr ̈odinger equation is
1
V i∂tψx = (Dx − 2Wx cosh(2∂x/V ))ψx. (17)
A ground state wavefunction is a wavepacket characterized by a small width of the order
of 1/√V , as shown in section 5.2. The width broadens after a long time, which diverges with V . On times that do not diverge in the thermodynamic limit, the ground state wavefunction and its subsequent evolution can be written as
ψ(x, t) = e−V f(x,t) (18)
with f (x, t) = g(x, t) − iθ(x, t), g and θ being respectively the envelope and the phase of the wavepacket. The envelope g(x, t) has a maximum at x(t), and expanding g(x, t)
around x(t) shows that indeed this wavefunction describes a packet of width 1/√V . After these preliminary considerations, we proceed and evaluate the evolution of the wavefunction, plugging the expression (18) of ψ(x, t) into (17):
−i∂tf (x, t) = Dx − 2Wx cosh(2∂xf ). (19)
doi:10.1088/1742-5468/2011/11/P11003 11


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
For the amplitude and the phase, this leads to
∂tg = −2Wx sin(2∂xθ) sinh(2∂xg) ∂tθ = −Dx + 2Wx cos(2∂xθ) cosh(2∂xg). (20)
The position of the peak x(t) corresponds to the maximum of the amplitude; thus it satisfies the implicit equation ∂xg|x(t) = 0. To obtain its evolution, we differentiate it with respect to time:
dx(t)
dt ∂x2g + ∂t∂xg = 0. (21)
The term ∂t∂xg above can be computed from (20). At the point where ∂xg|x(t) = 0, (21) becomes dx(t)
dt = 4Wx sin(2∂xθ)|x(t). (22)
This equation involves only one unknown quantity, ∂xθ|x(t), which, as we shall show, is akin to a momentum. A self-consistent equation for this quantity can be found by taking its derivative with respect to time:
d∂xθ|x(t)
dt = dx(t)
dt ∂x2θ
∣∣∣∣x(t)
+ ∂t∂xθ|x(t). (23)
In the previous expression, ∂t∂xθ|x(t) is the space derivative of (20). Using (22) the two
terms in ∂x2θ|x(t) cancel out and (23) is
d∂xθ|x(t)
dt = −∂xDx|x(t) + 2 cos(2∂xθ|x(t))∂xWx|x(t). (24)
This, together with equation (22), provides a set of closed differential equations for x(t) and ∂xθ|x(t). The last thing we have to show is that the quantity ∂xθ|x(t) is the average value of the momentum operator pˆ, which is
〈pˆ〉 = −
∫
x
i
V ψ†x∂xψx
=i
∫
x
|ψx2|∂xg(x, t) +
∫
x
|ψx2|∂xθ(x, t). (25)
Because of the form (18) of ψx(t) these integrals can be performed by the saddle point method (in the limit V → ∞). At the saddle point, ∂xg(x(t), t) = 0 and ∂xθ(x(t), t) has a non-zero value, thus 〈pˆ〉 = ∂xθ|x(t) + O(1/V ). The same is true for 〈xˆ〉 = x(t) + O(1/V ). Thus, rewriting (22) and (24), one finds that the phase p(t) and the position x(t) obey the equations
dx(t)
dt = 4Wx sin(p) = ∂p(Dx − 2Wx cos(2p)) dp(t)
dt = −∂x(Dx − 2Wx cos(2p)). (26)
As a conclusion, the average values x(t) and p(t) of the position and momentum operators, which describe the global behavior of the wavepacket, have the same time evolution as classical canonical variables with Hamiltonian H[x, p] = Dx − 2Wx cos(2p). This property fits into the general picture of the propagation of wavepackets in the semiclassical regime (see, for example, [31] for a mathematically oriented review) and, hence, was expected on general grounds as discussed previously. The generalization to more than one variable
doi:10.1088/1742-5468/2011/11/P11003 12


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 1. The trajectory x(t) for U = 3.33, with initial conditions x(0) = 0.26 of energy E = 0.2. The dots are obtained by numerical diagonalization of (13) for V = 5000 with a sharp Gaussian initial condition. The line is the evolution according to the classical Hamiltonian. The two are equivalent at short times. Similar results hold for any trajectory and initial condition.
is straightforward. The width of the packet can also be evaluated. It is related to the separation in time of two classical trajectories initially separated by the width of the packet. When the effective dynamics is one-dimensional, the classical Hamiltonian is integrable and periodic orbits separate linearly in time. In this case, since trajectories
start from an initial distance 1/√V , the typical time of separation is t ∼ √V . We check numerically that our analysis of the limit of large V is correct. In figure 1, the exact quantum evolution, obtained by diagonalization of the discrete equation (7), is compared to the classical evolution for short times. We find an excellent agreement.
5.4. Different effective trajectories in the phase space
We now study the effective classical dynamics by focusing on the phase space properties. Since the Hamiltonian (15) is one-dimensional and energy is conserved, there are lots of constraints on the motion. In particular, all the trajectories are integrable and can only be periodic in x(t) except for separatrix trajectories. We find that the phase space is divided into two regions by a separatrix. To see this, one can characterize trajectories in terms of their turning points, and considering whether the momentum p is bounded or not. There are three types of turning points: the derivative dx/dt = 4W (x) sin(2p) vanishes if either p = 0, p = π/2 or W (2x′) = 0. This last case is called ‘absorbing’ for a reason that will be explained later. Let us compare three trajectories at different energies for U < Uc, which are representative of all the cases encountered. For this purpose, two representations are shown: the evolution of x(t), p(t) in figure 2 and the phase space in figure 3 (right panel). The three types of trajectories are:
• (A) has two p = 0 turning points, and thus its momentum p is bounded.
• (B) is a separatrix trajectory in the classical mechanics sense. The left turning point is at p = 0 and the right turning point at x = 0 is ‘absorbing’; the time taken to reach
doi:10.1088/1742-5468/2011/11/P11003 13


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 2. The time evolution x(t) and 2p(t) modulo π for the three trajectories A, B and C. The scale is the same for all graphs.
Figure 3. (a) Three trajectories A, B and C for U = 3.33 < Uc. The energy of each trajectory, D + 2W and D − 2W as functions of x. (b) Trajectories in the phase space, momentum 2p versus x.
it (or escape from it) is infinite. In the equation of motion, at the point W (x) = 0, the effective mass tend to infinity.
• (C) has one turning point type at p = 0 and one at p = π/2. p is growing infinitely large with time, which is not pathological because only p modulo π enters the equations.
The diagram in figure 3 (left panel) is similar in spirit to the figures of effective potential shown to explain central motions in textbooks. It allows one to understand the dynamical evolution in a simple way. Actually, since the classical energy E = D(x) − 2W (x) cos(2p) is conserved, the values of x during the motion are restricted by the conditions D(x) − 2W (x) ≤ E ≤ D(x) + 2W (x) (note that W (x) = 0 for x = 1, 0). Except for the separatrix, all turning points correspond to either p = 0 at E = D − 2W ,
doi:10.1088/1742-5468/2011/11/P11003 14


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 4. D(x) ± 2W (x) versus x for the three regimes of couplings U in the Bose–Hubbard model nmax
b ≤ 2. Dark circles and squares are the superfluid and Mott insulator ground states, respectively. Dark dashed lines correspond to separatrix trajectories.
or p = π/2 at E = D + 2W . Thus, all trajectories are delimited by the two turning points xa and xb, which are at the intersection between E and D(x) + 2W (x), and E and D(x) − 2W (x). The evolution of the system then consists in a periodic motion oscillating between xa and xb. In the previous discussion we considered a specific form of the phase space and of D − 2W and D + 2W which are valid for certain values of U only. In the next section a careful investigation of the U dependence will be presented. However, before that, we want to stress that the effective potentials D − 2W , D + 2W can take three different qualitative forms, depending on the coupling U. These are shown in figure 4. The three regimes are separated by two special values of U: Ud and Uc, see figure 4. Uc is the critical coupling of the quantum phase transition and Ud = 1/Uc 0.1715. The special regime
U < Ud disappears when larger filling numbers nmax
b ≥ 3 are included, so it is a peculiarity
of the nmax
b = 2 case and, hence, not very relevant.
6. Sudden quenches in the Bose–Hubbard model for nmax
b =2
We now discuss the dynamical evolution following a quantum quench and its dependence on the final and initial values of U. At t < 0 the system is in the ground state at the coupling Ui. At t = 0 the coupling is switched to Uf and the quench dynamics is computed for t > 0. In the following we call a quench ‘from superfluid’ when Ui < Uc and ‘from Mott’ when Ui > Uc, and ‘to superfluid’ or ‘to Mott’ when Uf > Uc and Uf < Uc. The results of the following sections are summarized by the dynamical phase diagram shown in figure 6 (left panel).
6.1. Mott to superfluid
Starting from the Mott ground state x0 = 1, the trajectory is stuck at x(t) ∼ 1 even for large times. In order to check this, let us linearize the equation of motion around
doi:10.1088/1742-5468/2011/11/P11003 15


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 5. Quench trajectories for the three regimes of Uf with D(x)±2W (x), like in figure 4. Right panel (Uc < Uf ): in the quench Q1, at t = 0 the packet state is at x = x0, p = 0 (thus on the line D − 2W (Uf )), a position indicated by the arrow Q1. Then the trajectory of constant energy E is shown by the horizontal dark dashed–dotted line. Left and center panel (Uf < Ud and Ud < Uf < Uc): different initial conditions lead to qualitatively different quenches. The dark dashed lines are singular trajectories of infinite period. Quenches on these trajectories (Q3 and Q5) are at the dynamical transition.
x = 1. We use that x ̇ = ∂H/∂p = 4Wx sin(2p) and that sin(2p) can be extracted from
E = Dx − 2Wx cos(2p) to obtain x ̇ = −√4Wx2 − Dx2. Thus, at dominant order in we
obtain the equation for = 1 − x:
 ̇ = /τ, τ = 2/√(Uc − U )(U − Ud). (27)
The trajectory (t) = 0 is unstable, and since the wavefunction has a width 1/√V , its
typical evolution is given by (t) = 1/√V et/τ . Therefore, in the effective picture, the trajectory is stuck at the Mott ground state for times of the order of log(V ). This result is a peculiarity, actually a pathology, of mean-field models. Indeed, in a real finitedimensional system, spatial fluctuations drive the system away from the Mott state in a finite time.
6.2. Superfluid to Mott
In a superfluid to Mott quench, the initial condition is given by the ground state packet characterized by {x = (U/Uc + 1)/2, p = 0}. The trajectory after the quench is of
type (C), see quench Q1 of figure 5. The superfluid order parameter |Ψ20| (equation (2)) oscillates.
6.3. Superfluid to superfluid Ud < Uf < Uc
Depending on the value of Ui and Uf, there are three different types of dynamical evolutions in this case, that we call Q2, Q3 and Q4 in figure 5. Q2 is of type (C) and Q4 is of type (A). Q3, reached from a special Uid (dependent on Uf), corresponds to a singular separatrix of type (B) and of energy E = 0. In this case the packet relaxes exponentially to the Mott
doi:10.1088/1742-5468/2011/11/P11003 16


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 6. (a) Dynamical phase diagram for the Bose–Hubbard model with nmax
b = 2. In the M area, within mean field, the system remains stuck to the Mott insulator ground state after the quench. Quenches from the superfluid phase are oscillating and similar to (A) or (C). The dynamical transition (B) separating the two is displayed as a dashed line; it meets the Mott phase at Uf = Uc.
(b) Superfluid order 〈|Ψ0|2〉 as a function of Uf . Continuous line: time average after a quench. Dashed line: microcanonical average at the corresponding energy after the quench. The initial coupling is Ui = 0 but the evolution is qualitatively similar for all Ui with a dynamical transition.
insulator ground state |x = 1〉, and concomitantly the superfluid order |Ψ0|2 vanishes exponentially in time. This may be seen from the linearization (27), which becomes  ̇ = − /τ for a trajectory relaxing to x = 1. Approaching the transition oscillations take place on a timescale that diverges as −τ ln(|Ufd − Uf|). As a consequence we find that a
dynamical singularity, or transition, takes place at Ufd. The values of Ufd depend on Ui and
thus define a dynamical transition line Ufd = (Uc + Uid)/2, in the Ui, Uf plane. In figure 6
(right panel), as an example of singular behavior, we show the time average 〈|Ψ0|2〉 as a function of Uf for quenches starting from the noninteracting case Ui = 0. It is interesting to compare to 〈|Ψ0|2〉 its equilibrium counterpart obtained from the microcanonical average corresponding to the same energy. From this we clearly see that the system is not thermalized. Actually, large quenches (Q2) have nonvanishing oscillations of the superfluid order, contrary to the equilibrium value which is instead zero (because it corresponds to an effective high temperature). Moreover, we find that the dynamical transition takes place at an energy at which the system, if it were relaxed, would be superfluid. Thus, the exponential relaxation of the superfluid order is a purely dynamical effect.
6.4. Superfluid to superfluid Uf < Ud
In this regime, there is a qualitatively new family of quenches Q6 (comparable to Q2). There is also a new special quench Q5 to the modified separatrix state at energy Ed, which gives rise to another dynamical transition. However, unlike the other quench cases, these effects are artifacts of the truncation nmax
b = 2 and disappear for nmax
b ≥ 3. Therefore, they are not indicated in figure 6 (left panel), where the outcome of all possible sudden quenches is summarized.
doi:10.1088/1742-5468/2011/11/P11003 17


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
7. Bose–Hubbard model with weaker truncation nmax
b ≥3
7.1. Hamiltonian
The previous analysis focused on two bosons or less per site. This constraint can be relaxed to include up to nmax
b numbers of bosons per site. When nmax
b is sufficiently high
compared to the density, nmax
b n, one recovers the behavior of the Bose–Hubbard model with no constraints on the occupation number per site. For a given maximum number of bosons per site, nmax
b , any symmetric wavefunction
can be parameterized by the fractions xi of sites with i bosons per site, i ∈ [0, nmax
b ]. Since
the xi are fractions, they verify ∑
i xi = 1. Moreover the density n = ∑
i ixi is fixed; thus
there are only nmax
b − 1 free variables left. The wavefunction is expanded in the symmetric
basis like |ψ〉 = ∑
x ψx(t)|x〉. The transition elements D(x) and Wm(x) can be computed
as done previously. For instance, there are three different types of transitions m when
nmax
b = 3 and 6 when nmax
b = 4. Performing the classical equivalence for packet states, the resulting Hamiltonian can be put in the form (9)
H(x, p) = D(x) − 2
∑
m
Wm(x) cos(mipi). (28)
Specifically, when nmax
b = 3, if one chooses x1 and x2 as free variables, the Hamiltonian is
H(x1, x2, p1, p2) = D − 2W1 cos(p1 + p2) − 2W2 cos(2p1 − p2) − 2W3 cos(p1 − 2p2)
W1 = J (3x0x1x2x3)1/2 W2 = J x1(2x0x2)1/2 W3 = J x2(6x1x3)1/2
D = x2 + 3x3 − J (x0x1 + 2x1x2 + 3x2x3)
x0 = 1 − x1 − x2 − x3 x3 = 1
3 (n − x1 − 2x2).
(29)
Notice that, because 0 < xi < 1, there are constraints on the possible values of xi, such
as x2 < (n − x1)/2. For all nmax
b , there is a Mott insulator to superfluid quantum phase
transition at some coupling Uc if the density n is an integer (lower than nmax
b ). Above the critical coupling U > Uc the ground state is a Mott insulator xn = 1, xi=n = 0 (all sites have n bosons), and below U < Uc the ground state is superfluid with all xi = 0.
7.2. Regularity of trajectories after a quench
In the previous case nmax
b = 2, the effective dynamics was one-dimensional, and thus
integrable. For nmax
b > 2, the classical dynamics takes place in two or more dimensions and the trajectories may be either regular or chaotic. In order to characterize them we study their regularity properties. For chaotic trajectories, neighboring trajectories separate exponentially in time in the phase space y = {xi, pi}, like δy(t) ∼ exp(λt)δy(0). The
rate of separation λ is the largest Lyapunov exponent [32]. We computed λ for nmax
b =3 at density n = 1 for several trajectories, using a simplified version of the traditional GramSchmidt orthonormalization of the Lyapunov vectors. Roughly speaking, if we write the Hamiltonian evolution under the form y ̇i = fi(y), the deviation satisfies δ ̇yi = ∂jfi(y)δyj. This can be integrated numerically and normalized at each step to avoid an overflow (the orthogonalization step is dedicated to find all Lyapunov exponents, whereas here we only need the largest one). The Lyapunov exponents for trajectories with different initial conditions {xi1, xi2, p1 = p2 = 0} are plotted in figure 7 in the superfluid phase
doi:10.1088/1742-5468/2011/11/P11003 18


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 7. (a) Lyapunov exponents of the trajectories with initial conditions {x1, x2, p1 = p2 = 0}, for U = 2.86 plotted in levels of gray. The bright zone is regular (numerically λ 0.05) and the dark zones are chaotic. The Lyapunov exponents corresponding to initial conditions given by ground states obtained by varying Ui are indicated by a continuous line. The dashed line indicates initial conditions with zero energy. The dynamical transition corresponds to their intersection. (b) Dynamical phase diagram for nmax
b = 4. The dynamical
transition is at the dashed line. The dotted line is the dynamical transition when nmax
b = 2, for comparison.
U = 2.86 < Uc. Trajectories are regular in some regions of the space (periodic or quasiperiodic) with λ = 0 within the error bar, whereas some other regions are chaotic with λ > 0.1. The quench from E = 0 is exactly at the dynamical transition; the corresponding trajectory is chaotic. For U > Uc, when the ground state is a Mott insulator, all trajectories are regular. We notice that the regularity of a trajectory affects the time of spreading of the packet (determined by the time of separation of two neighboring trajectories). Actually, the time of separation is typically polynomial t ∼ V 1/α for a regular motion but only t ∼ ln V for a chaotic one.
7.3. Dynamical transition
In quenches from the superfluid phase Ui < Uc, like in the previous case nmax
b = 2, a
dynamical transition occurs at the special coupling Ufd, where the final energy equals the energy E = 0 of the unstable Mott trajectory xn = 1, xi=n = 0. Direct evidence of
this transition is given by the singularity of the time-averaged superfluid order |Ψ0|2 as
a function of Uf for a given Ui. In figure 8(b), we compare this singularity in |Ψ0|2 for
nmax
b = {2, 3, 4, 5} and find that the dependence in nmax
b of the divergence is very weak
beyond nmax
b = 4. The two curves nmax
b = 4 and nmax
b = 5 are not distinguishable, because they are identical up to 0.01%. We show the dynamical phase diagram in figure 7(b) for nmax
b = 4 and unit filling
factor. We observe that the transition line is near to the transition line for nmax
b = 2, and that they are asymptotically equal around Uc. Because the probability of having
more than four bosons on the same site is extremely small, of the order of 0.01% when
nmax
b 4, we can safely assume that this phase diagram is quantitatively representative of the phase diagram without truncation.
doi:10.1088/1742-5468/2011/11/P11003 19


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 8. (a) Evolution of x(t) and p(t) with time, nmax
b = 3, n = 1 and Ui = 1.
Left panel, Uf = 2.5 and right panel, Uf = 3.29. The dynamical transition is at
Ufd = 3.21. The left panel is before (E < 0) the dynamical transition, the right
one (E > 0) is after. (b) Superfluid order parameter 〈|Ψ0|2〉 as a function of Uf
for n = 1, Ui = 3, with nmax
b = 2, 3, 4 and 5. The curve nmax
b = 2 is shifted by
0.025 along the Uf axis for comparison.
Even though the existence of the dynamical transition for any nmax
b is beyond doubt, because the singularity is numerically manifest, more precise results on this transition, even for nmax
b = 3, are hard to provide. Some features of the case nmax
b = 2 persist; for
example, at the dynamical transition, the momentum 2p1 − p2 becomes unbounded, see figure 8(a). The fractions xi(t) are also oscillating, but without definite period. They are either quasi-periodic for low λ regions, or chaotic. Approaching the dynamical transition, the typical time of return to x1 ∼ 1 is increasing, possibly logarithmically divergent in
Uf −Ufd as suggested by the numerical divergence in figure 8(b). Unfortunately, the analysis
of the singularity for nmax
b ≥ 3 turns out to be out of reach. The numerical integration of classical equations of motions is exponentially sensible to numerical errors and thus not reliable. One could imagine that the trajectory at E = 0 is an unstable manifold, which would support the existence of a singularity for trajectories arbitrarily close to it. However, it is hard to decide whether the trajectory at the dynamical transition goes arbitrarily close to the point x1 = 1 (ground state of the Mott insulator), at which the trajectory is exponentially slowed down. A possible scenario, in which the surface E = 0 is ergodic, does not seem to be validated by the numerical integration of trajectories.
8. Quenches in the generalized Jaynes–Cummings model for super-radiance transition
8.1. Super-radiance quantum phase transition
We now consider the generalized Jaynes–Cummings model (4) and derive its quench dynamics. For simplicity and without loss of generality we focus on Qˆ = N/2. Thanks
doi:10.1088/1742-5468/2011/11/P11003 20


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
to the conservation of Qˆ = Sˆz + bˆ†bˆ, the spin degrees of freedom can be accounted for in terms of the bosonic ones. The states can be parameterized by the density of bosons n only, in the Fock basis |n〉bosons ⊗ |S; m〉spin:
|n〉 = |N n〉bosons ⊗ |N/2; N (1/2 − n)〉spin.
The action on |n〉 of some useful operators can be readily computed at the dominant order in N:
Sˆz|n〉 = N (1/2 − n)|n〉
ˆb†ˆb|n〉 = N n|n〉
Sˆ+ˆb|n〉 = √nN √N 2/4 − m2|n − 1/N 〉
= N 3/2n√1 − n|n − 1/N 〉.
From these equations, the transition elements Dn = 1/N〈n|Hˆ |n〉 and Wn = −1/N〈n ± 1/N|Hˆ |n〉 are easy to compute and yield an effective Hamiltonian on n and φ its conjugate momentum H[n, φ] = Dn − 2Wn cos(φ):
H[n, φ] = −2λn + 2n√1 − n cos(φ) (30)
which is the semiclassical approximation of the original Hamiltonian obtained in [25], up to a shift in the phase φ → φ + π. In [25], the authors studied sweeps from the empty state 〈nˆ〉 = 0 and the link to the Landau–Zener problem. Here, we focus on sudden quenches and the related dynamical transition. The ground state of this effective system is at φGS = π and
nGS =
⎧⎪⎨
⎪⎩
0 if λ ≤ −1, standard ground state
2
9 (3 − λ2 − √λ2(3 + λ2)) if −1 ≤ λ ≤ 0 super-radiant ground state
2
9 (3 − λ2 + √λ2(3 + λ2)) if λ ≥ 0 super-radiant ground state.
The super-radiance quantum phase transition is the result of a competition between the potential energy term and the kinetic energy term, which can be understood if the quantum Hamiltonian is written in the |n〉 basis:
Hˆ = −2λN nˆ + √gN N √nˆ(1 − nˆ)(ˆb† + ˆb).
Qualitatively, the potential term −2λˆb†ˆb encourages filling for λ ≥ 0 and discourages it
for λ ≤ 0. The ‘kinetic’ contribution ∼g(ˆb† + bˆ) can lower the energy. As a matter of fact, the sign of g is almost irrelevant. Changing the sign of g leads to Wn → −Wn. However, the new Hamiltonian can be mapped into the old one by the translation p → p + π. As a consequence, if the ground state of a given Hamiltonian is at p = 0,
ψn ∼ exp[−(n − nGS)/(σ/√N )2], then the ground state of the Hamiltonian with the
opposite sign of g is at p = π, ψn ∼ exp[−iN πn − (n − nGS)/(σ/√N )2], identical but with a staggered sign.
8.2. Sudden quenches
Previously, we have shown that the characterization of turning points plays an important role for understanding the dynamical behavior. In the generalized Jaynes–Cummings
doi:10.1088/1742-5468/2011/11/P11003 21


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
0
Figure 9. (a) Ground state nGS as a function of the parameter λ. The quantum phase transition takes place at λ = −1. (b) Quench diagram for all λi → λf . The quench trajectory is of bounded momentum φ (light gray) or unbounded φ (white). On the dashed line, the separatrix states are not singular (absorbing). The thick line is the dynamical transition, where the trajectories are singular. For λi < −1, in the dark gray region, trajectories are definitely stuck at n = 0. Otherwise, there is a slow relaxation at times of order log N .
model, there are two special turning points, nc = {0, 1}, identified by the equation dn/dt = Wn sin(φ) = 0. Like in the Bose–Hubbard model, only one gives rise to singular trajectories. This is readily seen, for example, computing the time taken to reach the singular point and having zero kinetic energy at this point:
T=
∫ nc
dn dt
dn =
∫ nc
dn (2Wn sin(φ))−1.
Using the conservation of energy E = Dn − 2Wn cos(φ), we can eliminate sin(φ) =
[1 − (E(nc) − Dn)2/(4Wn2)]1/2 and obtain
T=
∫ nc
dn [4Wn2 − (E(nc) − Dn)2]−1/2.
Around n = 1 − , the time is finite T ∼ ∫
0 d 1/√ , whereas around n = , the time
T ∼∫
0 d 1/√ 2 diverges. In other words, the trajectories touching the turning point
n = 1 have a finite period, whereas the trajectories touching n = 0 have an infinite period. The situation is analogous to the one already studied for the BHM: the absorbing state nc = 0 plays the same role of the Mott state and gives rise to the dynamical transition.
To identify the critical value λfd at which the transition takes place, one can compute the
energy after a quench λi → λf and compare it to the energy of the system at rest in n = 0. One can check that a trajectory n(t) starting with the same energy, actually energy zero, is indeed driven to the absorbing point nc = 0. This dynamical transition occurs on the
line λfd = −√1 − nGS(λi). A linearization similar to (27) shows that the relaxation is
exponential at the transition with a characteristic time τ −1 = 2√1 − λ2. Around the transition, the period of a trajectory diverges as τ ln(|λf − λfd|). The dynamical phase diagram is shown in figure 9(b). For λi > λc, the initial state is in the broken symmetry phase 〈nˆ(t = 0)〉 = 0. The situation is very similar to the BHM
doi:10.1088/1742-5468/2011/11/P11003 22


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
one: the filling number n(t) oscillates in time after the quench, and there is one region with bounded effective momentum φ, and two regions with unbounded φ. Notice that there are two separatrices between the three regions, and that one is not singular and does not give rise to a dynamical transition, whereas the other is. The singular one is the one for which the absorbing state n = 0 is met, corresponding to the restored symmetry state. For quenches with λi < λc, the initial state is empty 〈nˆ(t = 0)〉 = 0, and either drifts away from zero at large times (of the order of log N) if λf < 1, and otherwise, the state is definitely stuck at n = 0. The bounded or unbounded nature of the final state is also indicated.
Finally, we remark that eigenstates of the completely connected model can be written within a WKB expansion; this is done for completeness in appendix B.
9. Quenches in the Ising model in a transverse field
In our last example, let us consider the dynamics due to quantum quenches in the transverse field Ising model. To derive the classical effective dynamics, one can use the fact that the large spin limit is also the classical limit, see, e.g., [21]. To do so, one should
make the substitution Sˆ → S = S{sin θ cos φ, sin θ sin φ, cos θ}. The kinetic term (needed to describe classical dynamics) in the classical Hamiltonian of the large spin limit can be derived using a path integral for spins [33]. Here we instead use our generic method based on site-permutation symmetry. We denote spin-symmetric states of total momentum S = N/2 with the notation |s〉. They are such that Sˆz|s〉 = Ns|s〉 with s ∈ [−1/2, 1/2].
At dominant order in N , Sˆx|s〉 = N √1/4 − s2(|s + 1/N〉 + |s − 1/N〉)/2. One can proceed as usual to get the effective Hamiltonian:
Ds = 1
N 〈s|Hˆ |s〉 = −1
2 s2 Ws = − 1
N
〈
s+ 1
N
∣∣∣∣ Hˆ |s〉 = Γ
2
√1
4 − s2
H[s, φ] = Ds − 2Ws cos φ = − 1
2 s2 − Γ
√
1
4 − s2 cos φ.
As expected, the Hamiltonian is very reminiscent of the classical Hamiltonian for a single rotor once the change of variables s → cos θ is made. Indeed, the equations of motion obtained here are the same as in [21]. In this paper, the authors studied the quench from the paramagnetic phase to the ferromagnetic phase and AC dynamics.
Proceeding as for the BHM, we analyze the phase space of symmetric trajectories. This is different in the ferromagnetic and paramagnetic phases, see figure 10. In the latter, obtained for Γ < Γc, there is a separatrix. For sudden quenches from the ferromagnetic phase, where s = 0, to final values of the transverse field Γf < Γc, there is a dynamical
transition at Γfd = 1/2(1/2 + Γi). At the transition, the trajectory is a separatrix and s decreases exponentially in time to s = 0, which is the quantum paramagnetic ground state. The symmetry is dynamically restored at this point but also for larger quenches: contrary to the two previous examples, for quenches beyond the dynamical transition Γf > Γfd, the trajectories are symmetric in s → −s and the magnetization is oscillating
around zero. Averaging over time, the order parameter is zero: 〈Sˆz〉 = 0.
doi:10.1088/1742-5468/2011/11/P11003 23


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Figure 10. D(s) ± 2W (s) for Γ = 0.3 < Γc and Γ = 0.6 > Γc. The dark square is the quantum paramagnetic ground state and the dark circles are the ferromagnetic ground states. The dark dashed line is the separatrix; quenches on this trajectory are at the dynamical transition.
10. Discussion
Before concluding, two points need to be addressed further: (1) the possible link between dynamical transitions and equilibrium quantum phase transitions and (2) the pro and cons of our approach concerning the physics of finite-dimensional systems.
• In three examples, we found that dynamical transitions occur in systems characterized by a quantum equilibrium phase transition. Therefore, despite the fact that the dynamical transition is not directly related to the equilibrium one, as we stressed before, it is natural to wonder whether instead its existence is related to it. In support of this, if one studies the completely connected Bose–Hubbard model in a parameter regime (nonunitary fillings) where there is no equilibrium quantum phase transition then one finds that there is no dynamical transition either. Actually, we found the very same phenomenon in all models we studied, and this was also noticed for the fermionic Hubbard model [11]. We certainly cannot address this issue in general, also because it is still far from clear what ‘the dynamical transition’ is beyond mean-field theory. We shall instead endeavor to provide a partial answer at the mean-field level. Generically, we observe that, in all models we studied, there is a regime in which the symmetric state (the Mott insulator, the paramagnet, etc) is not the ground state but it plays the role of an excited metastable state that can trap the system for an infinite time. This gives rise to the dynamical transition. If the effective motion is one-dimensional, this state is absorbing and belongs to a separatrix. If the effective motion has two or more degrees of freedom, this state seems to belong to an unstable manifold. Thus, it appears that the singularity at the dynamical transition is a result of this singular trajectory, which in turn is a consequence of the existence of a quantum phase transition. A physical argument to support this idea is the following. For a quench from the unbroken symmetry phase to the broken symmetry phase
doi:10.1088/1742-5468/2011/11/P11003 24


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
in a completely connected model, the dynamical evolution is expected to be very slow. The reason is that the symmetry must break up and the order must develop starting from this point. This, however, is a local phenomenon, for example due to domain growth in finite dimensions, and therefore generically absent in completely connected models, except for times diverging with the system size: indeed, in our examples, we find that the typical timescale to depart from the initial value x(t = 0) is of the order of log V . The point is that this slow trajectory is precisely the time reversal of the singular trajectory that is responsible for the dynamical transition. To summarize, the existence of a quantum phase transition implies the existence of slow trajectories. They correspond to the escape from the symmetry unbroken state. Their time-reversed counterparts are the trajectories responsible for the dynamical transition. Thus, the existence of a phase transition indeed appears to be intertwined with the existence of a dynamical transition within the mean field.
• Let us now discuss the range of applicability of our results for finite-dimensional systems. First, our analysis can be put on the same footing as the Gutzwiller ansatz and functional integral saddle point approximations. Actually, the time-dependent Gutzwiller approximation applied to a finite-dimensional lattice leads to dynamical equations of motion that coincide with ours. This becomes manifest by deriving the Gutzwiller dynamical equations using the method presented in [11] (see appendix A and also [22]). Clearly, our mean-field approximation misses several essential physical effects. Relaxation and thermalization, for which spatial and temporal fluctuations must be taken into account, are not present. From this point of view, it is a more crude mean-field approximation than t-DMFT, which instead at least captures some dynamical fluctuations. Furthermore, the dynamics of a quench from the unbroken symmetry phase to the broken symmetry phase is not properly described for the reasons mentioned above. Inhomogeneities, topological defects and domain growth are out of reach. In contrast, our mean-field approximation is expected to capture well the evolution of local quantities at least on short times, as long as they are homogeneous across the system. Contrary to many other approaches, it is not perturbative in parameters (U, J, Γ etc) of the Hamiltonian. Unlike perturbative approaches, it can describe the existence of dynamical transitions and phenomena related to global observables.
11. Summary and outlook
The general purpose of this paper was twofold. First, we described a method to study the quantum quench dynamics of generic completely connected models, providing a mapping to effective classical dynamics. There are two reasons for considering completely connected models. In some cases, such as in the generalized Jaynes–Cummings model and the Dicke model, they provide the correct physical description. In others, such as the transverse field Ising model or the Bose–Hubbard model, they lead to an approximative treatment of finite-dimensional systems. In the latter case, the range of validity of the approximation is possibly limited to short times only. Our second aim was to study and to reveal the existence of out-of-equilibrium dynamical transitions induced by quantum quenches. In agreement with other works [11, 13] we showed that, within the mean-field approximation, dynamical transitions occur in quenches from the broken symmetry phase to other regions
doi:10.1088/1742-5468/2011/11/P11003 25


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
of the broken symmetry phase and that this is a quite generic phenomenon for systems that display a quantum phase transition at equilibrium. Clearly, a main and pressing question is to understand what this transition really is, beyond mean-field theory. Does it become a crossover in finite dimensions? If it remains a bona fide transition, what are its critical properties? Does the transition point correspond to a rapid thermalization, as suggested by t-DMFT [10], or instead to a singular behavior of the order parameter (the two things not necessarily being concomitant)? In the d = 1 BHM, a non-monotonic behavior of the propagation velocity as a function of Uf has been found in [34] by t-DMRG. This could well be a signature of a crossover related to the dynamical transition found in the mean field. An exact diagonalization study of hardcore bosons in d = 2 suggests the existence of a crossover or a singularity of the revival time after a quantum quench [23]. From the analytic point of view, going beyond the mean field is a difficult task. An argument for the occurrence of dynamical transitions beyond mean field is given in [13], within an imaginary time path integral formalism. Clearly, it is crucial to take into account fluctuations not captured by mean-field theory. This was started to be done in [35]. This work indeed suggests that these fluctuations could alter substantially the mean-field results. Promising ways to capture fluctuations are the projector operator formalism [36] and 1/z expansions [37] (z is the connectivity of the lattice). Field-theoretic methods are also being developed, as in [19] for the BoseHubbard model in the grand canonical ensemble; the use of two-particle irreducible actions also seems promising [38].
Acknowledgments
We thank C Kollath, M Schiro`, M Eckstein and J Keeling for interesting discussions on these topics. GB acknowledges partial financial support from ANR FAMOUS.
Appendix A. Gutzwiller ansatz
The previous analysis, based on the symmetry between sites, seems to be related to completely connected models only. Instead, it is completely equivalent to the dynamical Gutzwiller approximation applied to finite-dimensional lattices. In order to show this, we proceed in two steps. First, we recall that, within the Gutzwiller approximation, the only property of the lattice that matters is the local connectivity z. All lattices with the same value of Jz are characterized by the same dynamical equations. Thus, from this perspective, our completely connected model for which the value of the coupling and the connectivity are respectively J/V and V is equivalent to any finite-dimensional lattice with a coupling J′ and a connectivity z′ such that J′z′ = J. The second step consists in showing that the Gutzwiller ansatz applied to our model indeed leads to the dynamical equation we obtained. In order to do this, we follow the method presented in [11] where one introduces a trial wavefunction dependent on some physical parameters that are chosen through a maximization procedure. In its equilibrium version, the estimated ground state is simply found minimizing the energy. The dynamical formulation is a bit more elaborated. For clarity, we show here how to build it for the case nmax
b = 2 only. The following is an adapted version of the formulation developed in [11].
doi:10.1088/1742-5468/2011/11/P11003 26


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Let us define first the ‘full state’ |F 〉 = ⊗l(|0〉 + |1〉 + |2〉), and let Pˆjl be the projector
on site l on the state |j〉, where j ∈ {0, 1, 2}. The Gutzwiller ansatz wavefunction is a trial wavefunction with six real, time-dependent parameters xj(t), pj(t):
|ψGA〉 =
∏
sites
ei(p0Pˆ0+p1Pˆ1+p2Pˆ2)(√x0Pˆ0 + √x1Pˆ1 + √x2Pˆ2)|F 〉
=
∏
sites
(eip0√x0|0〉 + eip1√x1|1〉 + eip2√x2|2〉). (A.1)
Note that for simplicity we dropped the site index. The xn are the projector average:
xn = 〈ψ|Pˆn|ψ〉. As we shall see, they will turn out to coincide with the fraction of sites with n bosons. Obviously, because this is only a trial wavefunction, it cannot satisfy exactly the time evolution: i.e. iħ(d/dt)|ψGA〉 = Hˆ |ψGA〉. However, one can enforce it in an approximate way. This allows one to obtain the time evolution of xj(t) and pj(t). We impose the following constraints:
• The projectors in the Heisenberg representation PˆlH satisfy, on average, the Heisenberg
equation of evolution Pˆ ̇lH = i[Hˆ , PˆlH]. This amounts to computing the average of Pˆ
in the Schro ̈dinger picture xl(t) = 〈ψ|Pˆl|ψ〉 using
x ̇l = 〈  ̇ψ|Pˆl|ψ〉 + 〈ψ|Pˆl|ψ ̇ 〉
= −i〈ψ|[Pˆl, Hˆ ]|ψ〉. (A.2)
• The energy is conserved E = 〈ψ|Hˆ |ψ〉.
Let us call H[xl, pl] = 〈ψ|Hˆ |ψ〉 the energy as a function of the parameters. The evolution (A.2) can also be written, using the explicit form of |ψ〉 (A.1):
x ̇l = −i〈ψ|[Pˆl, Hˆ ]|ψ〉 = ∂
∂pl
〈ψ|Hˆ |ψ〉
= ∂H[xl, pl]
∂pl
. (A.3)
This evolution is very reminiscent of the first Hamilton equation of motion. Furthermore, the conservation of energy E ̇ = (∂H[xl, pl]/∂pl)p ̇l + (∂H[xl, pl]/∂xl)x ̇l = 0 leads to the second Hamilton equation:
p ̇l = − ∂H[xl, pl]
∂xl
. (A.4)
As a consequence, the Gutzwiller ansatz wavefunction is indeed equivalent to an effective classical Hamiltonian evolution of the variables xl and pl. The effective
Hamiltonian H[xl, pl] = 〈ψ|Hˆ |ψ〉[xl, pl] must be computed for the model at hand. For
the Bose–Hubbard model with a given truncation nmax
b (in particular nmax
b = 2) one recovers the dynamical equation (15) that we derived in the main text. This completes the proof of the equivalence of the Gutzwiller approximation for finite-dimensional lattices and the dynamics of completely connected models.
doi:10.1088/1742-5468/2011/11/P11003 27


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
Appendix B. Eigenstates in completely connected models
Using a Wentzel–Kramers–Brillouin (WKB) approximation [39], eigenstates of the Schr ̈odinger equation (13) can be found in the limit of large V . To do so, we write the eigenstates φE(x) within the WKB approximation. The derivation is standard: one
looks for stationary solutions of the form ψ(x) = A(x)eiV S(x) of the equation (13), at dominant order in V . One finds
φE(x) = C
2W (x)√sin(2p(x)) exp
(
±iV
∫x
x0
dx′ p(x′)
)
(B.1)
where C is a normalization constant, E is the energy, p(x) satisfies the implicit equation E = Dx − 2Wx cos(2p(x)) and x0 is the left turning point of the classical trajectory of energy E. Using this expression, we can draw a parallel between the eigenstate φE(x) and the effective classical trajectories of energy E. For an observable f (xˆ), the average is
〈φE|f (xˆ)|φE〉 = |C|2
∫
x
dx f (x)
4W (x) sin(2p(x))
= ∫ 1dt
∫
x
dx dt
dx f (x) = f (x). (B.2)
In the second line, we refer to the effective classical motion dx/dt = ∂H/∂p and the average f (x) is the average over the effective classical trajectory of f (x) over one period. In other words, we found that, in the semiclassical regime, the average over a quantum stationary state of energy E is given by the average over one period of the classical trajectory of the same energy E. Although this result is not often mentioned, this is a direct consequence of the WKB expression of the wavefunction.
References
[1] Greiner M et al , 2002 Nature 415 39 [2] Greiner M et al , 2002 Nature 419 51 [3] Greiner M, Regal C A and Jin D S, 2005 Phys. Rev. Lett. 94 070403 [4] Rigol M, Dunjko V and Olshanii M, 2008 Nature 452 854 [5] Biroli G, Kollath C and L ̈auchli A, 2010 Phys. Rev. Lett. 105 250401 [6] Kinoshita T, Wenger T and Weiss D S, 2006 Nature 440 900 [7] Kollath C, L ̈auchli A M and Altman E, 2007 Phys. Rev. Lett. 98 180601 [8] Roux G, 2010 Phys. Rev. A 81 053604 [9] Roux G, 2009 Phys. Rev. A 79 021608(R) [10] Eckstein M, Kollar M and Werner P, 2009 Phys. Rev. Lett. 103 056403 [11] Schir ́o M and Fabrizio M, 2010 Phys. Rev. Lett. 105 076401 [12] Sciolla B and Biroli G, 2010 Phys. Rev. Lett. 105 220401 [13] Gambassi A and Calabrese P, 2011 Europhys. Lett. 95 66007 [14] Eckstein M, Hackl A, Kehrein S, Kollar M, Moeckel M, Werner P and Wolf F A, 2009 Eur. Phys. J. Spec. Top. 180 217
[15] Barmettler P, Punk M, Gritsev V, Demler E and Altman E, 2010 New J. Phys. 12 055017 [16] Polkovnikov A, Sengupta K, Silva A and Vengalattore M, 2010 Rev. Mod. Phys. 83 863–83 [17] Cucchietti F M, Damski B, Dziarmaga J and Zurek W H, 2007 Phys. Rev. A 75 023603 [18] Altman E and Auerbach A, 2002 Phys. Rev. Lett. 89 250404 [19] Kennett M P and Dalidovich D, 2011 Phys. Rev. A 84 033620 [20] Schu ̈tzhold R, Uhlmann M, Xu Y and Fischer U R, 2006 Phys. Rev. Lett. 97 200601 [21] Das A, Sengupta K, Sen D and Chakrabarti B K, 2006 Phys. Rev. B 74 144423
doi:10.1088/1742-5468/2011/11/P11003 28


 J.Stat.Mech. (2011) P11003
Dynamical transitions and quantum quenches in mean-field models
[22] Snoek M, 2011 Europhys. Lett. 95 30006 [23] Wolf F, Hen I and Rigol M, 2010 Phys. Rev. A 82 043601 [24] Georges A and Yedidia J S, 1991 J. Phys. A: Math. Gen. 24 2173 [25] Altland A, Gurarie V, Kriecherbauer T and Polkovnikov A, 2009 Phys. Rev. A 79 042703 [26] Jaksch D and Zoller P, 2005 Ann. Phys., NY 315 52 [27] Fisher M P A, Weichman P B, Grinstein G and Fisher D S, 1989 Phys. Rev. B 40 546 [28] Baumann K, Guerlin C, Brennecke F and Esslinger T, 2010 Nature 464 1301 [29] Keeling J, Bhaseen M J and Simons B D, 2010 Phys. Rev. Lett. 105 043001 [30] Sachdev S, 1999 Quantum Phase Transitions (Cambridge: Cambridge University Press) [31] Littlejohn R, 1986 Phys. Rep. 138 193 [32] Gaspard P, 1998 Chaos, Scattering and Statistical Mechanics (Cambridge: Cambridge University Press) [33] Fradkin E, 1991 Field Theories of Condensed Matter Systems (Frontiers in Physics vol 82) (Reading, MA: Addison-Wesley) [34] L ̈auchli A and Kollath C, 2008 J. Stat. Mech. P05018 [35] Schir ́o M and Fabrizio M, 2011 Phys. Rev. B 83 165105 [36] Trefzger C and Sengupta K, 2011 Phys. Rev. Lett. 106 095702 [37] Navez P and Schu ̈tzhold R, 2010 Phys. Rev. A 82 063603 [38] Rey A M, Hu B L, Calzetta E, Roura1 A and Clark C W, 2004 Phys. Rev. A 69 033610 [39] Von Brack M and Bhaduri R K, 1996 Semiclassical Physics (Frontiers in Physics) (Reading, MA: Addison-Wesley)
doi:10.1088/1742-5468/2011/11/P11003 29
