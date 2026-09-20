# Spectroscopic properties of inhomogeneously broadened spin ensembles in a cavity - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.83.053852
> Collected: 2026-09-20
> Published: 2011-05-31
> Zotero parent key: 2IEWU8BU
> Evidence: Zotero indexed PDF text

PHYSICAL REVIEW A 83, 053852 (2011)
Spectroscopic properties of inhomogeneously broadened spin ensembles in a cavity
Z. Kurucz,1,* J. H. Wesenberg,2 and K. Mølmer1
1Lundbeck Foundation Theoretical Center for Quantum System Research, Department of Physics and Astronomy, University of Aarhus, DK-8000 A ̊rhus C, Denmark 2Centre for Quantum Technologies, National University of Singapore, Singapore 117543 (Received 26 January 2011; published 31 May 2011)
The enhanced collective coupling to weak quantum fields may turn atomic or spin ensembles into an important component in quantum information processing architectures. Inhomogeneous broadening can, however, significantly reduce the coupling and the lifetime of the collective excitation that represent the quantum information. In this paper we show that the width and shape of the inhomogeneous broadening have a striking influence on the dynamics of the cavity-ensemble system and may lead to narrowing of the linewidth of the collective states. We underpin our findings with the examples of a Gaussian and a Lorentzian profile of the inhomogeneity.
DOI: 10.1103/PhysRevA.83.053852 PACS number(s): 42.50.Ct, 42.50.Pq, 42.50.Gy
I. INTRODUCTION
In ensembles of a large number of identical atoms, the interaction with the electromagnetic radiation field concentrates in a few collective degrees of freedom. Typically, one identifies effective oscillator degrees of freedom, which represent the collective atomic population of different internal states. The strong effective coupling of these oscillators to incident quantum fields makes atomic ensembles a prospective component in light-matter interfaces [1], quantum memories [2], repeaters for long-range quantum communication [3], and many other applications in quantum information technology. The ensemble size, on the one hand, provides a large optical depth, and on the other hand, it provides phase-matching conditions to couple strongly to weak quantum fields. In a microscopic quantum formulation, an incident single photon couples to a single collective excitation, i.e., to a superposition state where all atoms have the same or similar excitation amplitude. The corresponding Rabi frequency is proportional to the square root of the number of atoms. While a single collective oscillator degree of freedom is coupled to the field, a stored field state can be transferred to another spatial mode of collective excitation by applying a controlled reversible inhomogeneous broadening (CRIB) to the atoms. In this way, a multimode optical interface and memory can be established [4]. Although optical transitions of rare-earth ion dopants in crystals are inhomogeneously broadened, narrow spectral features can still be defined with hole-burning techniques, and both CRIB schemes [5,6] and schemes based on atomicfrequency combs [7] have been used to demonstrate storage of up to 1060 pulses of light [8,9]. In this paper, we consider an ensemble of N effective spin-1/2 particles, coupled to a central quantum oscillator (cavity). A cavity can be used to significantly enhance the atom-light interaction, as demonstrated by experiments on ultracold rubidium atoms [10] and ion Coulomb crystals [11] in an optical cavity. Furthermore, a single quantized field mode can be used as an interface in hybrid proposals for
*Also, Research Institute for Solid State Physics and Optics, H.A.S., H-1525 Budapest, Hungary.
quantum computing, e.g., to couple polar molecules [12,13] or solid-state spin ensembles [14] to a superconducting qubit via a transmission-line resonator. Recent experimental breakthroughs have led to the observation of strong collective coupling between a superconducting transmission-line resonator and large ensembles (N > 1012) of electron spins of chromium ions in ruby [15], nitrogen-vacancy centers in diamond [16], and erbium ions in yttrium orthosilicate crystal [17], while iron nuclei embedded in a low-Q planar cavity have been resonantly excited by synchrotron radiation to a superradiant state with a large collective Lamb shift [18]. The multimode capacity of ensembles has also been observed with nitrogen electron spins in fullerene cages and the electron and nuclear spins of phosphorous in silicon [19]. The purpose of this paper is to investigate collective enhancement in the presence of inhomogeneous broadening, which is not controllable by the experimentalist. We study a system with a Hamiltonian,
Hˆ0 = ωcaˆ †
c aˆc + ∑
j
ωj σˆ j
z , (1)
where ωc is the angular frequency of the central oscillator, ωj is the time-independent transition frequency of the j th spin, and  ̄h = 1. The spins are noninteracting and the coupling to the central oscillator is described by a Jaynes–Cummings Hamiltonian,
Hˆ1 = ∑
j
gj σˆ j
+aˆc + H.c., (2)
with possibly different coupling constants gj . This model has fundamental importance and it appears with different variations in quantum physics: a single spin coupled to a bath of oscillators (the model explaining spontaneous emission of light from a single atom), a central spin coupled to a spin bath in a spin-star configuration [20], a single oscillator interacting with a spin ensemble, or a cloud of atoms in an optical or microwave cavity. Many of these models have been addressed in textbooks [21] with emphasis on the resulting dissipative dynamics of the central system. The mathematical difficulties arising when taking the limit of a continuously dense ensemble are also well known [22–24].
053852-1
1050-2947/2011/83(5)/053852(11) ©2011 American Physical Society


 Z. KURUCZ, J. H. WESENBERG, AND K. MØLMER PHYSICAL REVIEW A 83, 053852 (2011)
Here we revisit the problem with emphasis on the “spin bath” degrees of freedom. We show that the density of spin states plays an important role in the joint dynamics of the central oscillator and the collective spin-wave mode that is directly coupled to it. In certain cases, despite the inhomogeneity, all the other spin-wave modes are effectively decoupled. This fact manifests itself in reduced oscillator linewidths determined by the homogeneous linewidth of the individual spins [25,26]. For other configurations, however, the oscillator linewidths are dominated by the inhomogeneous broadening, and the “decoherence” of the superradiant mode is collectively enhanced. The paper is organized as follows. Section II derives some important properties of the model system, including the distribution of eigenenergies, the transmission spectrum through the cavity, and a formal solution for the dynamics of the system in the limit of high polarization. In Sec. III, we analyze in detail the cases where the effective density of spin states is Gaussian and Lorentzian, and compare the oscillator linewidths as well as the degree of Rabi splitting in both cases. In Sec. IV, we consider the regime of strong coupling and study the protective effects of the Rabi splitting in a perturbative manner. Section V summarizes our results.
II. THE CAVITY-ENSEMBLE SYSTEM
At low temperatures (high polarization), a collection of twolevel systems and a collection of oscillators behave identically. This fact is conveniently described in the Holstein–Primakoff approximation by introducing the bosonic operators aˆj for each spin-1/2 particle,
σˆ j
z ≡ −1
2 + aˆ †
j aˆj , σˆ j
+ ≡ aˆ †
j
√
1 − aˆ †
j aˆj ≈ aˆ †
j . (3)
The nonlinearity introduced by the square-root term in Eq. (3) ensures that no two excitations can take place at the same spin. If we consider delocalized spin waves involving a large number of spins compared to the number of excitations, the probability that a given spin is excited is inversely proportional to the number of spins N . Therefore, as long as only a few delocalized spin excitations are considered, it is reasonable to neglect the square-root term in Eq. (3). In this regime, the free and interaction Hamiltonian (1) and (2) become quadratic in the bosonic operators (apart from an omitted c number),
Hˆ0 = ωcaˆ †
c aˆc +
N ∑
j =1
ωj aˆ †
j aˆj , (4)
Hˆ1 =
N ∑
j =1
gj aˆ †
j aˆc + H.c. =  (bˆ†aˆc + aˆ †
cbˆ), (5)
where bˆ† ≡ ∑
j αj aˆ †
j , defined by the normalized vector αj =
gj /(∑
k |gk|2)1/2, is the creation operator of a delocalized spinwave mode, which is the superradiant mode. This is the concentrated degree of freedom which is coupled to the cavity with
the collective coupling strength   = (∑
k |gk|2)1/2 that scales
as √N . An important consequence of the Holstein–Primakoff approximation is that the excitations become independent (noninteracting) quasiparticles. Therefore, the dynamics of a single excitation provides the general solution, even if the total
number of excitations is actually much larger than unity (but still much smaller than N ; see [27] for the case when the number of excitations in the superradiant mode is comparable to the number of spins). In the following, our aim is to gain a detailed understanding of the spectroscopic signature of the bath, as observed through the cavity mode. In order to do so, in Sec. II A we will use the resolvent formalism [21] to calculate the Green’s functions of the system, then we will describe transmission spectroscopy in Sec. II B. We find that the Green’s functions, as well as the spectroscopic properties of the system, are closely linked to the level-shift function, and we devote Sec. II C to studying the analytic properties of this function.
A. Green’s functions
The Green’s functions, which we are going to derive first, provide a convenient description of the dynamics. We start from the Heisenberg–Langevin equation of motion for the oscillator operators in the Heisenberg picture,
d
dt aˆc = −iωcaˆc − i
∑
j
g∗
j aˆj + fˆc, (6)
d
dt aˆj = −iωj aˆj − igj aˆc + fˆj . (7)
To account for photons leaking out of the cavity at rate κ and spins decaying at rate γj , the cavity frequency and the spin transition frequencies are considered complex with negative or zero imaginary parts, Im ωc = −κ and Im ωj = − 1
2 γj . The
Langevin noise operators fˆc and fˆj satisfy 〈fˆc(t)fˆc†(t′)〉 = 2κδ(t − t′) and 〈fˆj (t)fˆ†
k (t′)〉 = γj δjkδ(t − t′). Equations (6) and (7) specify a set of inhomogeneous linear differential equations, whose Green’s functions can be calculated as
Gμν (t ) ≡ [e−iHt ]μν = 〈[aˆμ(t ),aˆ †
ν(0)]〉, (8)
where the matrix elements of the dynamic matrix H are Hcc =
ωc, Hjk = δjkωj , and Hjc = H ∗
cj = gj . (In what follows, Latin
indices j,k = 1, . . ., N enumerate spins only, whereas Greek letters μ, ν = c, 1, ..., N refer both to spins and to the cavity.) Calculating the matrix exponential directly in Eq. (8) can be rather appealing (see Sec. II D). Instead, here we derive the Green’s functions using the resolvent technique, which allows for taking the continuum limit. The Green’s function (8) also specifies the transition amplitude for an excitation created at t = 0 in the oscillator mode ν to end up in oscillator μ at a later time t and, thus, can be expressed as the given commutator expectation value. We use this formula to convert Eqs. (6) and (7) to a system of differential equations for the Green’s functions,
id
dt Gcν (t) = ωcGcν (t) + ∑
j
g∗
j Gjν (t), (9)
id
dt Gjν (t) = ωj Gjν (t) + gj Gcν (t), (10)
with the initial condition Gμν(0) = δμν. Substituting into Eq. (9) the formal solution
Gjc(t ) = Gjc(0)e−iωj t − igj
∫t
0
Gcc(τ )e−iωj (t−τ) dτ, (11)
053852-2


 SPECTROSCOPIC PROPERTIES OF INHOMOGENEOUSLY . . . PHYSICAL REVIEW A 83, 053852 (2011)
we get a closed integro-differential equation for Gcc(t),
id
dt Gcc(t) = ωcGcc(t) − i
∫t
0
Gcc(τ )K(t − τ ) dτ, (12)
where we have introduced the memory kernel function
K(t) ≡ ∑
j
|gj |2e−iωj t . (13)
Equation (12) can be solved in the Fourier domain by extending the integral to a proper convolution. For this, we introduce the advanced (+) and retarded (−) versions of the Green’s functions and the memory kernel function,
G±
μν(t) ≡ ∓i (±t)Gμν(t),
(14)
K±(t) ≡ ∓i (±t)K(t),
where (t) is the Heaviside step function. With these functions, we have a proper convolution,
id
dt G±
cc(t) = δ(t) + ωcG±
cc(t ) +
∫∞
−∞
G±
cc(τ )K±(t − τ ) dτ.
(15)
Now taking the Fourier transform of Eq. (15), we obtain
ωG ̃ ±
cc(ω) = 1 + ωcG ̃ ±
cc(ω) + G ̃ ±
cc(ω)K ̃ ±(ω), (16)
from which the explicit form of the reduced dynamics of the central oscillator follows by simple algebra,
G ̃ ±
cc(ω) = [ω − ωc − K ̃ ±(ω)]−1. (17)
The Fourier transforms G ̃ μ±ν(ω) = ∫ Gμ±ν(t)eiωt dt are conventionally called forward and backward propagators, while K ̃ ±(ω) is the level-shift function [21]. We note, however, that K ̃ −(ω), as well as the backward propagators G ̃ μ−ν(ω), are undefined if any of the spin-relaxation rates γj or the cavity κ is nonzero. The remaining propagator matrix elements can all be expressed in terms of G ̃ c±c(ω): Introducing kj (t) ≡ e−iωj t and
defining k±
j (t) similarly to Eq. (14), we find by Eq. (11) that
G ̃ ±
jc(ω) = gj k ̃±
j (ω)G ̃ c±c(ω), (18)
G ̃ ±
ck(ω) = g∗
k k ̃±
k (ω)G ̃ c±c(ω), (19) G ̃ ±
jk(ω) = δjkk ̃±
j (ω) + gj g∗
k k ̃±
j (ω)k ̃±
k (ω)G ̃ c±c(ω). (20)
Furthermore, for the amplitude of transiting from the cavity to the superradiant spin-wave mode, Gsc(t) ≡ 〈[bˆ(t),aˆc†(0)]〉, we have
G ̃ ±
sc(ω) = G ̃ ±
cs (ω) =  −1K ̃ ±(ω)G ̃ ±
cc(ω), (21)
G ̃ ±
ss(ω) = K ̃ ±(ω)[1 − K ̃ ±(ω)G ̃ ±
cc(ω)]/  2. (22)
B. Linear response and spectroscopic features
An efficient experimental tool for studying the coupled cavity-ensemble system is transmission spectroscopy. In this process, the (lossy) cavity is driven by an external classical field of frequency ω0 via the interaction Hamiltonian Vˆ (t) =
Ee−iω0t aˆc† + H.c. The transmitted field—which is proportional to the steady state of the field inside the cavity—reflects the linear response of the system to the driving field and
shows a resonance when the driving frequency is near an eigenfrequency. The linear susceptibility of the system is, therefore, what we are going to derive here. Let us consider a general external classical drive described
by Vˆ (t) = ∑
μ Eμe−iω0t aˆ †μ + H.c. For the transmission spec
troscopic setup above, Ej = 0 and Ec = E are proportional to the external field driving the cavity; but one could also consider, e.g., directly driving the spins via an external field that couples to the total spin, Ec = 0 and Ej = E. We assume that the driving field is weak, so that the total number of excitations is always small and the Holstein–Primakoff approximation remains valid. Then the Heisenberg–Langevin equation of motion for the annihilation operators can be obtained from Eqs. (6) and (7) by adding the source terms −iEce−iω0t and −iEj e−iω0t , respectively, to the right-hand sides. The formal solution of this set of inhomogeneous differential equations can be written in terms of the Green’s functions as
aˆμ(t) = ∑
ν
Gμν (t − t0)aˆν (t0)
+∑
ν
∫t
t0
Gμν (t − τ )[−iEν e−iω0τ + fˆν (τ )] dτ.
(23)
The first term vanishes when taking the limit t0 → −∞, for all eigenvalues of Hμν are assumed to have a negative imaginary part (even if infinitesimal). Since 〈fμ(t)〉 = 0, the expectation value of the oscillator operators in the steady state becomes
〈ass
μ (t )〉 = e−iω0t ∑
ν
χμν (ω0)Eν , (24)
where
χμν(ω) ≡ −i
∫∞
0
Gμν (τ )eiωτ dτ = G ̃ +
μν(ω) (25)
is the linear susceptibility (impedance) of the system, which has been calculated in Eqs. (17)–(22). In the transmission spectroscopic setup, the cavity field is 〈ass
c (t)〉 = Ee−iω0t χcc(ω0), so the transmissivity of the system
is proportional to |G ̃ c+c(ω0)|2, and the phase shift is φ(ω0) =
arg G ̃ c+c(ω0) [26,28]. The resonance peaks in the transmission
spectrum are characterized by the complex poles of G ̃ c+c(z), that is, the solutions for z of the implicit equation
[G ̃ +
cc(z)]−1 = z − ωc − K ̃ +(z) = 0. (26)
Finally, we mention that there is a direct way to extract information about the level-shift function—and thus about the structure of the spin bath—from the measured transmission spectrum. The level-shift function can be calculated by inverting Eq. (17): K ̃ +(ω) = ω − ωc − χ −1
cc (ω). Alternatively, if only the transmissivity is available experimentally, but not the phase of the susceptibility, then K ̃ +(ω) may be obtained by fitting a Lorentzian to the transmissivity |χcc(ω,ωc)|2 as a function of the cavity frequency ωc (with Im ωc = −iκ). Once
the values of the level-shift function K ̃ +(ω) are known for real frequencies, its analytic properties can be used to derive information about the shape of the inhomogeneous broadening of the spin ensemble.
053852-3


 Z. KURUCZ, J. H. WESENBERG, AND K. MØLMER PHYSICAL REVIEW A 83, 053852 (2011)
C. Analytic properties of the level-shift function
The complex analytic extension of the level-shift function K ̃ ±(ω) is of special importance, and here we summarize some of its properties [21]. First we note that the Fourier
Laplace transforms k ̃±
j (z) ≡ ∫ k±
j (t)eizt dt are defined on complementary halves of the complex plane,
k ̃±
j (z) =
{1
z−ωj if Im z ≷ Im ωj ,
undefined if Im z ≶ Im ωj , (27)
and when Im z approaches Im ωj = − 1
2 γj from above or
below, k ̃+
j (z) and k ̃−
j (z) tend to different distributions,
ηli→m0+
k ̃±
j
(
ω− i
2 γj ± iη
)
=P 1
ω − Re ωj
∓ iπ δ(ω − Re ωj ), (28)
where ω is real and P denotes the principal value. The whole ensemble may consist of discrete and continuous
sets of spins, and K ̃ +(z) = ∑
j |gj |2k ̃+
j (z) is defined for Im z >
supj Im ωj , while K ̃ −(z) is defined for Im z < infj Im ωj . For simplicity, we assume that the decay rate is the same for all spins, γj = γhom. A continuous spin ensemble can be described by its
coupling-density profile, ρ(ω) ≡ ∑
j |gj |2δ(ω − Re ωj ). If ρ(ω) is an analytic function of the real variable ω, then
K ̃ (z) =
∫ ρ(ω)
z−ω+ i
2 γhom
dω (29)
is a complex analytic extension of K ̃ ±(z) that has a branch-cut discontinuity along the line ω − i
2 γhom, such that it approaches
different values from above and from below,
ηli→m0+
K ̃
(
ω− i
2 γhom ± iη
)
= K ̃ ±
(
ω− i
2 γhom
)
, (30)
as illustrated in Fig. 1. The real and imaginary parts of K ̃ ±(z) =  c(z) ∓ i
2  c(z) on the branch-cut line z = ω − i
2 γhom follow
from Eqs. (28) and (29),
 c
(
ω− i
2 γhom
)
=P
∫ ρ(ω′)
ω − ω′ dω′, (31)
 c
(
ω− i
2 γhom
)
= 2πρ(ω). (32)
Re z
Im z
E− E+
ωc
K ̃ + (z)
K ̃ − (z) ω− γ
FIG. 1. The branch cut of the level-shift function K ̃ (z) displayed as the straight line ω − i
2 γhom (ω ∈ R) in the complex plane. K ̃ (z)
has a jump of K ̃ −(z) − K ̃ +(z) = i c(z) when passing through the cut from above. Depending on whether κ is smaller than, equal to, or larger than 1
2 γhom, the poles of the cavity-cavity propagator, i.e., the roots E± of Eq. (26), may lie above the cut, on the cut, or on the second Riemann sheet below the cut, respectively.
Thus the analytic continuation of K ̃ +(z) is given by Eq. (29) above the branch cut, while it explores the second Riemann sheet of K ̃ (z) below the cut,
K ̃ +(z) =
⎧⎪⎨
⎪⎩
K ̃ (z) if Im z > − 1
2 γhom,
 c(z) − i
2  c(z) if Im z = − 1
2 γhom,
K ̃ (z) − i c(z) if Im z < − 1
2 γhom.
(33)
The roots of Eq. (26), which give the position and width of the resonance peaks, may be located above the branch cut of
K ̃ (z), on the cut line, or below it depending on whether κ or
1
2 γhom is larger (see Fig. 1).
These considerations allow us to extract information about the structure of the inhomogeneity (the shape of the couplingdensity profile) from the transmission spectrum. We can revert Eq. (32) once the values of the level-shift function K ̃ +(ω) are evaluated on the real axis (see end of Sec. II B),
ρ(ω) = − 1
π Im K ̃ +
(
ω− i
2 γhom
)
≈ −1
π Im K ̃ +(ω) + 1
2π
∂Re K ̃ +(ω)
∂ω γhom, (34)
where we truncated the Taylor series of Im K ̃ +(z) at first order in γhom and obtained the derivative from the Cauchy–Riemann equations. Finally, we remark that we included γhom in Eq. (29) merely in order to separate the effects of homogeneous and inhomogeneous broadening. Alternatively, we could have assumed a coupling-density profile that already included homogeneous broadening via the convolution
ρ′(ω) ≡
∫ γhom/2π
(ω − ω′)2 + 1
4γ2
hom
ρ(ω′) dω′. (35)
The branch cut of the new level-shift function K ̃ ′(z) =
∫ ρ′(ω)/(z − ω) dω is then on the real axis. However, the analytic continuations of K ̃ ′±(z) are the same as those of K ̃ ±(z), and the two models lead to the same dynamics.
D. Normal modes of discrete systems
As an alternative to the Green’s functions, the dynamics of the oscillator operators can be given via the quasinormal modes of the system. The matrix exponential in Eq. (8) can, in principle, also be calculated by diagonalizing the
non-Hermitian matrix H: ∑
ν Hμν ηνq = Eq ημq . Provided that
the spin transition frequencies ωj are all different, the N + 1 eigenvalues are, as in Eq. (26), the solutions of the equation
Eq − ωc − ∑
j
|gj |2/(Eq − ωj ) = 0. (36)
The columns of the diagonalizing matrix η are the right eigenvectors of H, while the rows of η−1 are the left ones, and it is easy to see that, including normalization,
η−2
cq = [η−1]−2
qc = 1 + ∑
j
|gj |2
|Eq − ωj |2 , (37)
ηjq = gj ηcq
Eq − ωj
, [η−1]qj = g∗
j [η−1]qc
Eq − ωj
. (38)
053852-4


 SPECTROSCOPIC PROPERTIES OF INHOMOGENEOUSLY . . . PHYSICAL REVIEW A 83, 053852 (2011)
−4
−2
0
2
4
6
8
Re q
Ε /∆ ω
Ω = 4∆ ω
2∆ ω 2Ω
(a)
Ω=∆ω
2∆ ω
(b)
Ω = ∆ ω/4
2∆ ω
(c)
−4
−2
0
2
4
6
8
−6 −4 −2 0 2 4 6
ω0/∆ ω
δ/ ∆ ω
(d)
2∆ ω 2Ω
−6 −4 −2 0 2 4 6
δ/ ∆ ω
(e)
2∆ ω
−6 −4 −2 0 2 4 6
δ/ ∆ ω
(f)
2∆ ω
FIG. 2. (Color online) Numerical calculation for N = 25 spins with an inhomogeneous width of  ω, sampled from a Gaussian distribution. The individual spins decay at a rate γj = 0.1 ω and are uniformly coupled to the cavity. The cavity decay rate is κ = 0.05 ω. (a)–(c) The real part of the exact eigenenergies as a function of the cavity detuning. Color red (blue) indicates that the corresponding polariton is photon-like (spin-like). (d)–(f) Transmission spectrogram, the color hue (saturation) corresponds to the phase (logarithmic magnitude) of the susceptibility (25). (a), (d) In the strong-coupling regime   = 4 ω, only the two extremal eigenmodes have photonic attribute. (b), (e) In the intermediate-coupling regime   =  ω, a band of intermediate eigenmodes has significant cavity content, and the cavity can “decay” into any of these modes. (c), (f) In the weak-coupling regime   =  ω/4, there is no collective effect, and only a few resonant spins are dressed by the cavity.
Note that for lossless systems (κ = 0, γj = 0), the diagonal
izing matrix is unitary, so [η−1]qμ = η∗μq . The left and right eigenvectors form a complete set, and at any time, the oscillator operators can be expanded in the right eigenbasis as
aˆμ(t) = ∑
q
ημq ˆ q (t), (39)
where the expansion coefficient ˆ q is the annihilation operator of the quasinormal mode q and can be expressed using the left eigenvectors as
ˆ q (t) ≡ ∑
μ
[η−1]qcaˆμ. (40)
For atomic spins in an optical cavity, excitations of these quasinormal modes are called cavity polaritons. It is straightforward
to show that the Heisenberg–Langevin equation of motion for the operators of the quasinormal modes reads
d
dt
ˆ q = −iEq ˆ q + Fˆq , (41)
where Fˆq (t) ≡ ∑
μ[η−1]qμfˆμ(t) is the transformed noise operator. (Note that the transformed noise operators may not necessarily be independent of each other.) One can then formally integrate Eq. (41) and obtain the time evolution of the quasinormal modes,
ˆ q (t ) = e−iEqt ˆ q (0) +
∫t
0
e−iEq(t−τ)Fˆq (τ ) dτ. (42)
As an example, Fig. 2 shows the eigenenergies and transmission spectra for an ensemble of 25 spins in the regimes of strong, intermediate, and weak coupling.
053852-5


 Z. KURUCZ, J. H. WESENBERG, AND K. MØLMER PHYSICAL REVIEW A 83, 053852 (2011)
III. EXAMPLES OF SPECTROSCOPIC SIGNATURES
With the results of the previous section, we are equipped to predict the spectroscopic signature for a given system as observed by transmission spectroscopy. While the output signal could have been obtained more directly via classical input-output theory [26], we shall see that the framework developed in Sec. II provides additional insights into the physics by explicitly considering the state of the spin bath. We will first consider the limiting cases of infinitely narrow and infinitely wide coupling-density profiles, before studying the qualitative differences between the intermediate cases for Lorentzian and Gaussian coupling-density profiles.
A. Oscillation and decay
In certain situations, the detailed structure of the couplingdensity profile is not important. On time scales much smaller than the inverse inhomogeneous width of the ensemble, that is, when the inhomogeneous broadening cannot be resolved, the ensemble behaves as a single oscillator with a collectively enhanced coupling constant. In this case, the memory kernel function (13) can be approximated by K(t) ≈  2e−iωat , or equivalently, K ̃ ±(ω) =  c(ω) ∓ i
2  c(ω) with  c(ω) ≈
P 2/(ω − ωa) and  c(ω) ≈ 2π  2δ(ω − ωa), where the ensemble’s mean transition frequency ωa is assumed to be real. The inverse Fourier–Laplace transforms of Eqs. (17) and (21) show that the cavity and the superradiant mode undergo Rabi
oscillation at the Rabi frequency  R = √ 2 + δ2/4,
Gcc(t ) = e−i(ωa+δ/2)t (cos  Rt − i cos θ sin  Rt ), (43)
Gsc(t ) = −ie−i(ωa+δ/2)t sin θ sin  Rt, (44)
where the detuning of the cavity, δ = ωc − ωa, and the mixing angle, tan θ ≡ 2 /δ, are assumed to be real. In the opposite limit, when the inhomogeneous width is much larger than the collective coupling  , and the spin transition frequencies are sufficiently dense to form a continuum, we are in the Weisskopf–Wigner regime. In analogy with the spontaneous emission of an excited atom, the cavity excitation effectively decays into the continuum of spin waves in this regime [29]. The key assumption in the Weisskopf–Wigner approximation is that the kernel function K(t) decays fast compared to the slowly varying envelope Gcc(t)eiωct , and thus the frequency dependence of K ̃ ±(ω) can be neglected. The inverse Fourier–Laplace transform of Eq. (17) then gives an exponential decay,
Gcc(t ) = e−i[ωc+ c(ωc)− i
2  c(ωc)]t . (45)
Here we see that  c(ωc) is the shift of the cavity frequency and
1
2  c(ωc) is an additional cavity decay rate due to the coupling
to the dense spin reservoir. Finally, we consider the general case when an initially photonic excitation decays into the continuum of spin-wave modes, and we specify the asymptotic energy distribution of the excited spin. If Gcc(t) converges to zero, it is either because the initially photonic excitation leaks out of the cavity, or
because the photon is irreversibly converted into a spin-like excitation. From Eq. (11), we have
tli→m∞ Gjc(t )eiωj t = gj G ̃ +
cc(ωj ), (46)
so the asymptotic probability that the j th spin is excited equals limt→∞ |Gjc(t)|2 = |gj |2|G ̃ c+c(ωj )|2, assuming that γj = 0. Then the asymptotic energy distribution of the excited spin, i.e., the probability that the transition frequency of the excited spin is ω, reads
p(ω) ≡ ∑
j
δ(ω − ωj )|Gjc(∞)|2 = ρ(ω)|G ̃ +
cc (ω)|2
=1
2π
 c(ω)
[ω − Re ωc −  c(ω)]2 + [2κ +  c(ω)]2/4 . (47)
In particular, it is proportional to a Lorentzian in the Weisskopf–Wigner regime, in analogy to the energy distribution of a photon spontaneously emitted by an atom.
B. Lorentzian coupling-density profile
When the cavity is coupled to a single atomic oscillator (e.g., a degenerate ensemble of homogeneously broad but identical atoms), we recover the well-known problem of a driven two-level atom or that of two coupled oscillators. With an atomic transition frequency ωa, natural atomic linewidth γ , cavity detuning from the atomic transition δ, and cavity linewidth 2κ, we take the complex frequencies ω1 = ωa − i
2γ
and ωc = ωa + δ − iκ.
The memory kernel function defined in Eq. (13) is K(t) =  2e−iωat−γ t/2 for such a single collective spin excitation, which yields K ̃ +(z) =  2/(z − ωa + i
2 γ ). The same memory
kernel function is obtained for a large, inhomogeneously broadened ensemble with a Lorentzian coupling-density profile. This is the case, for example, when each spin in the ensemble is uniformly coupled to the cavity with the
same coupling constant g =  /√N , and the spin transition frequencies are distributed according to
D(ω) = 1
2π
Nγ
(ω − ωa)2 + γ 2/4 , (48)
where now γ is the ensemble’s inhomogeneous width (full width at half maximum) and the individual spins do not decay, and the coupling-density profile is ρ(ω) = g2D(ω). All the dynamical properties of both the cavity and the superradiant spin-wave mode are determined by K ̃ +(z) alone, and thus they are the same for a single (homogeneously broad) atomic oscillator and for an inhomogeneous ensemble with Lorentzian coupling density. Therefore, it cannot be determined from the linear response of the cavity whether the broadening is of homogeneous or inhomogeneous origin. The forward propagator (17) reads
G ̃ +
cc(ω) = ω − ωa + i
2γ
(ω − E+)(ω − E−) , (49)
with the two complex poles
E± = ωa − i
2 γ +  R cos θ ±  R, (50)
053852-6


 SPECTROSCOPIC PROPERTIES OF INHOMOGENEOUSLY . . . PHYSICAL REVIEW A 83, 053852 (2011)
where
 R ≡
√
 2 + [δ − i(κ − 1
2 γ )]2/4 (51)
is the (complex) Rabi frequency, and for the (complex) mixing angle, we have
cos θ ≡ δ − i(κ − 1
2γ)
2 R
, sin θ ≡  
 R
. (52)
The two poles correspond to two peaks in the transmission spectrum: The position and the width of the peaks are determined by the real and imaginary parts of E±, respectively. The system undergoes damped Rabi oscillations, as can be seen by taking the inverse Fourier transform of Eqs. (49) and (21),
Gcc(t ) = e−i(ωa+δ/2)t−(γ /2+κ)t/2
×
(
cos  Rt − i cos Re θ
cos Im θ sin  Rt
)
, (53)
Gsc(t ) = −ie−i(ωa+δ/2)t−(γ /2+κ)t/2
× (sin Re θ sin  Rt − tan Im θ cos  Rt). (54)
As an illustrative example, let us consider the resonant case δ = 0. Depending on the value of (γ − 2κ)/(4 ), we see a transition from (a) damped Rabi oscillations at a reduced effective Rabi frequency to (b) an overdamped situation [see also Figs. 3(a)–3(b)]. (a) Regime of oscillations. The Rabi frequency (51) is real when γ − 2κ < 4 , giving rise to a Rabi splitting of  R =
− 2 Im Ε ± /γ FWHM
Ω/γ FWHM
(b)
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.5
1.0
1.5
− 1.0
− 0.5
0.0
0.5
1.0
(Re Ε(±Re a
ω )/γ FWHM
(a)
Lorentzian
0.0 0.2 0.4 0.6 0.8 1.0
Ω/γ FWHM
(d)
(c)
Gaussian
FIG. 3. (a), (c) Real and (b), (d) imaginary parts of the poles of the susceptibility (17) as a function of the collective coupling strength for (a), (b) a Lorentzian and (c), (d) a Gaussian coupling density profile. The quantities are directly related to the position and width of the peaks in the transmission spectrum. The cavity is tuned at the center of the ensemble (ωc = ωa), and κ = γhom = 0 was assumed. The full width at half maximum of the coupling density is γFWHM =
γ for the Lorentzian and γFWHM = √8 ln 2 σ for the Gaussian. (a), (c) Dashed lines show the lowest order solutions of the asymptotic expansion given by Eq. (79), and correspond to the strong-coupling approximation described in Sec. III A. (c), (d) Dotted curves show the asymptotic solutions in the next orders as given by Eqs. (64) and (65). (c) Dash-dotted curve shows Eq. (60) corresponding to the Weisskopf–Wigner approximation in the weak-coupling regime.
√
 2 − ( 1
2 γ − κ)2/4 around the atomic transition frequency
ωa [Fig. 3(a)], and the width of the peaks in the transmission
spectrum is −2Im E± = 1
2 γ + κ [Fig. 3(b)]. Here we see two
important facts about a Lorentzian coupling-density profile: the resonant Rabi splitting is smaller than the actual collective coupling strength  , and the linewidth of the peaks is determined by the inhomogeneous width of the ensemble, independent of the coupling strength. As we shall see, the cavity does not provide protection for the superradiant mode in this case. (b) Overdamped regime. The Rabi frequency (51) is purely imaginary for γ − 2κ > 4 . There is no Rabi splitting at all, for we have two overlapping peaks at ωa
of width −2Im E± = (γ + 2κ)/2 ∓ √(γ − 2κ)2/4 − 4 2. In the Weisskopf–Wigner regime (γ  ,2κ), the dynamics reduces to the exponential decay given by Eq. (45), and the peaks in the spectrum become clearly distinguishable: On top of a wide background peak with γ+ ≈ γ , corresponding to the weakly perturbed superradiant mode, there is superimposed a narrow peak of the cavity, whose width γ− ≈ 2κ + 4 2/γ equals the overall decay rate of the cavity excitation as given in Eq. (45) with  c = 4 2/γ . Finally we note that the oscillating–decaying dynamics of our cavity photon interacting with an inhomogeneously broadened, highly polarized spin ensemble shows some similarity with the dynamics of a single atom in a damped, zero-temperature cavity [30]. In the latter case, the atom interacts with the lossy cavity, and the cavity itself is coupled to a collection of external radiation modes. In our case, the cavity interacts with the superradiant spin-wave mode, and the superradiant mode itself is coupled to a collection of subradiant spin-wave modes.
C. Gaussian coupling-density profile
We consider now a Gaussian coupling-density profile,
ρ(ω) = √12π
 2
σ exp
[
− (ω − ωa)2
2σ 2
]
, (55)
and show that the spectrum of an ensemble with such an inhomogeneity is qualitatively different from what we learned from the Lorentzian profile in the previous section. From the integral in Eq. (29), we obtain
K ̃ +(z) =
√π
2
 2
σ e−ξ2 [erfi(ξ ) − i], (56)
where we have introduced the dimensionless parameter ξ ≡ (z − ωa + i
2 γhom)/(√2σ ). Equation (56) is composed of
complex analytic functions with no branch-cut singularities, and Im K ̃ +(ω − i
2 γhom) = −πρ(ω). Therefore, Eq. (56) is
indeed the analytic continuation of K ̃ +(z) on the entire complex plane. To determine the position and width of the peaks in the transmission spectrum, we solve Eq. (26) numerically [Figs. 3(c)–3(d)]. Here we observe two regimes: an overdamped one without Rabi splitting ( /γFWHM   0.23) and another one with two Rabi-split peaks ( /γFWHM   0.23). The most important difference from the case with Lorentzian coupling density is that the width of the split peaks decreases with the coupling strength, and for strong coupling it is
053852-7


 Z. KURUCZ, J. H. WESENBERG, AND K. MØLMER PHYSICAL REVIEW A 83, 053852 (2011)
dominated by the ensemble’s homogeneous width or the cavity κ, as has been pointed out in Refs. [25,26]. To estimate the position and width of the resonances, let us first consider the overdamped regime,   σ . The Taylor series expansion of Eq. (56) around ξ = 0 reads
K ̃ +(z) =  2
√2σ
[
2ξ
∑ ∞
n=0
(−2ξ 2)n
(2n + 1)!! − i√π
∑ ∞
n=0
(−ξ 2)n
n!
]
.
(57)
A good approximation for the first peak, which corresponds to the dressed cavity mode, can be readily obtained by keeping only the first term in both sums,
Re (E+ − ωa) = δ/(1 −  2/σ 2), (58)
−2Im E+ = 2κ + 2κ − γhom + √2π σ
σ 2/  2 − 1 . (59)
For δ = κ = γhom = 0 [dash-dotted curve in Fig. 3(d)],
−2Im E+ = √2π  2/σ + O( 4) (60)
has quadratic dependence on the collective coupling  , which confirms the Weisskopf–Wigner approximation. Keeping the ξ 2 term in Eq. (57), we find a second root,
Re (E− − ωa) = −δ + O( 2), (61)
−2Im E− = 2γhom − 2κ + √82σπ
(σ2
 2 − 1
)
+ O( 2).
(62)
It is worth mentioning that we have not only two, but infinitely many roots with an increasingly large negative imaginary part (not shown in Fig. 3). This is a mathematical consequence of the dynamics of the subradiant modes and causes the cavity not to follow a simple exponential decay [31]. In the limit of weak coupling, however, the first root with a finite imaginary part yields exponential decay in accordance with the WeisskopfWigner approximation. We consider now the strong-coupling regime   σ . The asymptotic expansion of Eq. (56) reads
K ̃ +(z) ∼  2
√2σ
[
−i√π e−ξ2 + 1
ξ
∞ ∑
n=0
(2n − 1)!!
(2ξ 2)n
]
. (63)
Although the asymptotic power series does not converge, for any given ξ , we still get a good approximation if we truncate the series at n   |ξ |2. In fact, the strong coupling approximation in Sec. III A corresponds to keeping only the n = 0 term of the series, and it yields eigenenergies similar to Eq. (50) with γ = γhom, which are shown as dashed lines in Fig. 3(c). Focusing on the resonant case δ = 0 and κ = γhom = 0, we first neglect the imaginary part in Eq. (63) and truncate the series after the n = 1 term. This gives the position of the peaks in the next order [dotted curves in Fig. 3(c)],
Re (E(1)
± − ωa) = ±√
 2 + σ 2, (64)
or equivalently, ξ (1)
± = ±√( 2 + σ 2)/2σ 2. To obtain the imaginary part of the eigenenergies, we look for the solutions in the form ξ = ξ (1)
± +  . We write ξ (1)
± in place of ξ in the exponent in Eq. (63), and we use the facts that 1/ξ ≈
1/ξ (1)
± −  /ξ (1)2
± and 1/ξ 3 ≈ 1/ξ (1)3
± − 3 /ξ (1)4
± . With these approximations, we have, for the imaginary parts [dotted curve in Fig. 3(d)],
−2Im E(2)
±=
√ 2π
e e−  2
2σ 2
[  2 − σ 2
2σ + O( −2)
]
. (65)
We see that for large coupling strength, the width of the spectral peaks rapidly decreases. This is a manifestation of the gapping mechanism, which will be investigated in more details in the next section.
IV. PROTECTIVE ENERGY GAP IN THE STRONG-COUPLING REGIME
Ideally, when a spectrally narrow ensemble is strongly coupled to a cavity, excitations undergo coherent Rabi oscillation between the cavity and the superradiant spin-wave mode at a collectively enhanced Rabi frequency  , without involving the subradiant modes. In reality, however, the inhomogeneity in the spin transition frequencies will gradually mix in the subradiant modes, thus resulting in decoherence of the cavity-superradiant subspace [31]. The time scale for the latter process can vary, depending not only on the ensemble’s inhomogeneous width, but also on the structure of the inhomogeneity. For a Lorentzian coupling-density profile, e.g., it is always dominated by the inverse of the ensemble’s inhomogeneous width, as we have seen in Sec. III B. For other distributions, like the Gaussian, this “decoherence” time can be significantly longer—an effect conventionally explained by a gapping mechanism [31,32]. In this section, we investigate how the strong coupling to the cavity prevents the mixing of the superradiant and subradiant modes, thus leading to narrowing of the linewidth of the superradiant spin-wave mode. For the cavity to have an effect, we will assume that the cavity is not too far from resonance (δ  2/ ω).
A. Appearance of the energy gap
In the absence of inhomogeneity, the dressed polariton modes, which are defined as combinations of the superradiant spin-wave mode and the cavity mode,
ˆ (0)
+ = cos θ
2 aˆc + sin θ
2
bˆ, (66)
ˆ (0)
− = sin θ
2 aˆc − cos θ
2
bˆ, (67)
are quasinormal modes which are uncoupled to the subradiant spin-wave modes and form a closed subsystem. In the presence of inhomogeneity, however, these polariton modes are only approximate eigenmodes. Their equations of motion read
d
dt
ˆ (0)
+ = −iE(0)
+ ˆ (0)
+ − i ω sin θ
2 cˆ + · · · , (68)
d
dt
ˆ (0)
− = −iE(0)
− ˆ (0)
− + i ω cos θ
2 cˆ + · · · , (69)
where we omit the Langevin noise terms, and where E(0)
±= (ω + ωc)/2 ±  R are the (complex) eigenenergies of the
respective polariton modes, cˆ ≡  ω−1 ∑
j (ωj − ω)α∗
j aˆj is an annihilation operator corresponding to a subradiant mode orthogonal to both aˆc and bˆ, and the ensemble’s inhomogeneous
053852-8


 SPECTROSCOPIC PROPERTIES OF INHOMOGENEOUSLY . . . PHYSICAL REVIEW A 83, 053852 (2011)
width  ω is defined as the variance of the spin transition frequencies,
 ω2 ≡ ∑
j
|ωj − ω|2|αj |2 =
∫
(ω − Re ω)2 ρ(ω)
 2 dω,
(70)
ω≡∑
j
ωj |αj |2 =
∫(
ω− i
2 γhom
) ρ(ω)
 2 dω, (71)
where we assume Im ωj = Im ω = − 1
2 γhom for all spins.
For a cavity not too far from resonance (δ  2/ ω), the limit of strong coupling is identified by the condition    ω. If the tail of the coupling-density profile falls off sufficiently fast so that the Rabi-split eigenenergies E(0)
± lie far from all
the spin transition frequencies, then the operators ˆ (0)
± rotate fast with respect to cˆ, and the contribution of cˆ in Eqs. (68) and (69) can be neglected (rotating-wave approximation). In other words, the spin dephasing processes induced by the inhomogeneous broadening have to bridge the energy gap between the dressed modes and the subradiant modes, and if this energy gap is large enough, the dressed modes are efficiently protected from decoherence (see Fig. 4). Finally, we note that the gapping mechanism may be observed even when the cavity is out of resonance ( ω   δ  2/ ω). Provided that the tail of the couplingdensity profile falls off sufficiently fast, the cavity can be adiabatically eliminated in the Born–Markov approximation. In this case, the cavity only has a dispersive effect, and its presence results in an energy shift of the superradiant mode equivalent to the ac Stark shift in optics. Namely, Hˆ1 can be replaced by
Hˆgap =  gap bˆ†bˆ,  gap = −  2
δ , (72)
independent of the state of the cavity. The superradiant
mode, bˆ† ≡ ∑
j αj aˆ †
j , is an eigenmode of Hˆgap, but due to
the dephasing effects of the inhomogeneity in Hˆ0, it gets
Φ(+0)
Φ(−0)
2ΩR
ac
b
Ωδ
c
∆ω c
FIG. 4. (Color online) Level diagram showing the quasiclosed subspace consisting of the dressed polariton modes (superpositions of the cavity and the superradiant spin-wave mode) coupled to a chain of subradiant spin-wave modes. In the strong-coupling regime  R  ω, the coupling between the dressed modes  ± and the subradiant mode c is off-resonant, therefore, the inhomogeneity does not induce decoherence of the dressed modes: the dressed levels are not broadened.
mixed with the subradiant modes, as shown by the Heisenberg equation of motion
d
dt
bˆ† = i[Hˆ0 + Hˆgap,bˆ†] = i(ω +  gap)bˆ† + i ω cˆ†.
(73)
For a large gap ( gap  ω), and provided that the tail of the coupling-density profile falls off sufficiently fast, the superradiant mode is energetically separated from the subradiant modes. Therefore, the inhomogeneous broadening cannot induce real transitions involving the superradiant mode. This energy gap may efficiently protect the quantum information stored in the superradiant spin-wave mode from the dephasing effects of the inhomogeneous broadening or spin diffusion [32].
B. Corrections to the eigenenergies
In this section, we estimate how fast the tail of the couplingdensity distribution should fall off in order for the cavitysuperradiant subspace to become protected and for the line narrowing to manifest. In the strong-coupling limit, the eigenenergies E± lie far away from the typical spin transition frequencies, and in this region (|z − ω|  ω), we make an asymptotic power-series expansion of K ̃ +(z) in the form
K ̃ +(z) =
n ∑
k=0
 2Ak
(z − ω)k+1 + O
(1
(z − ω)n+2
)
. (74)
For the Lorentzian (48), An = (− i
2 γ )n, while A2n =
(2n − 1)!!σ 2n and A2n+1 = 0 for the Gaussian (55). In general, inserting the identity
P1
ω − ω′ ∼
∑ ∞
n=0
(ω′ − Re ω)n
(ω − Re ω)n+1 (75)
into (31) yields the asymptotic power-series expansion
 c
(
ω− i
2 γhom
) ∼
∑ ∞
n=0
 2Mn
(ω − Re ω)n+1 , (76)
as long as the statistical moments of the coupling density,
Mn ≡ 1
 2
∫
(ω − Re ω)nρ(ω) dω, (77)
are well defined. In what follows, we will assume that the coupling density also has an asymptotic power-series expansion,
ρ(ω) ∼
∑ ∞
n=1
 2Bn
(ω − Re ω)n+1 . (78)
Then Im Ak = −π Bk. However, if the nth moment (75) exists, we must have Bk = 0, and Ak = Mk for all k   n. Given the power-series expansion (74), we now look for the resonance peaks in an iterative way. Since M0 = 1, we start
with K ̃ +(0)(z) ≈  2/(z − ω) in the zeroth order. Equation (26) then yields two roots, the same as those given by Eqs. (50)–(52) with γ = γhom, namely,
E(0)
± − ω = ± 
(
cot θ
2
)±1
. (79)
053852-9


 Z. KURUCZ, J. H. WESENBERG, AND K. MØLMER PHYSICAL REVIEW A 83, 053852 (2011)
In the first order, we look for the solution in the form z = E(0) +   and write
K ̃ +(1)(z) =  2
E(0) − ω
[
1 + A1 −  
E(0) − ω
]
. (80)
Then we obtain the corrections to E(0)
+ and E(0)
−,
  (1)
+ = A1 sin2 θ
2 ,  (1)
− = A1 cos2 θ
2 . (81)
In the case of a Lorentzian coupling density, A1 = − i
2γ
immediately leads to wide resonance peaks dominated by the ensemble’s inhomogeneous width γ . In general, if the tail of the coupling-density profile falls off as (ω − ω)−2, then the imaginary part of the correction  (1) reads
−2Im  (1)
± = 2π B1
{
sin2 θ
2
cos2 θ
2
}
, (82)
and it is not reduced by a strong-coupling constant  . If, however, the first moment of ρ(ω) exists (and ω is such that M1 = 0) and ρ(ω) has the asymptotic power-series expansion (78), then B1 must be zero, and so A1 = 0. In this case, we have to proceed further in the expansion. In the second order, we assume that A1 = 0, so we look for the solution in the form z = E(0) +   and write
K ̃ +(2)(z) =  2
E(0) − ω
[
1−  
E(0) − ω +  2 + A2
(E(0) − ω)2
] .
(83)
To simplify the roots of the resulting quadratic equation, we assume that |A2|  2 and make a series expansion with respect to A2/  2. For the corrections, we obtain
  (2)
± = ± A2
 
{
sin2 θ
2 tan θ
2
cos2 θ
2 cot θ
2
}
+ O(A2
2
/ 4), (84)
and the resonance peaks are at
E(2)
+ ≈ ω + ωc
2 +  R
[
1+
(
2 sin4 θ
2
) A2  2
]
, (85)
E(2)
− ≈ ω + ωc
2 −  R
[
1+
(
2 cos4 θ
2
) A2  2
]
. (86)
We see that the contribution from A2 is suppressed for large  .
If the second moment of ρ(ω) exists, then A2 =  ω2 is purely real, and corrections to the resonance widths may only come from a complex mixing angle θ . As an example, let us consider the resonant case δ = 0. The Rabi frequency is reduced,  R =
[ 2 − ( 1
2 γhom − κ)2/4]1/2, and the mixing angle is θ ≈ π/2 −
i(1
2 γhom − κ)/2 R. The real and imaginary parts of the two
poles then read
Re (E(2)
± − ω) = ± R
(
1+ 1
2
 ω2  2
)
, (87)
−2Im E(2)
± =1
2 γhom + κ +
(1
2 γhom − κ
)  ω2
 2 . (88)
A small inhomogeneous broadening enhances the Rabi splitting, while the width of the peaks is predominantly determined by the homogeneous width, and not the inhomogeneous one. We mention that in contrast to Eq. (88), Eq. (65) was obtained
for κ = γhom = 0, and therefore we had to consider higher orders of ρ(ω) to estimate the peak widths.
C. Losses due to inhomogeneous broadening
Here we show that the inhomogeneity alone does not necessarily lead to a complete extinction of an excitation in the protected cavity-superradiant subspace. To estimate the magnitude of the leakage from the two-dimensional subspace of the dressed states due only to the inhomogeneous broadening, we consider an otherwise lossless system (κ = 0 and γj = 0) and examine an initial excitation in the mode (66). The exact time evolution of this mode in the Heisenberg picture follows from Eq. (42),
ˆ (0)
+ (t) = ∑
q
φq e−iEq t ˆ q , (89)
with real eigenenergies Eq and without noise operators. The coefficients are φq = cos θ
2 ηcq + sin θ
2  −1 ∑
j g∗
j ηjq , and we
will index the normal mode closest to (89) by q = +, so that φ+ is the largest coefficient. We expect that the transition amplitude between the original and the evolved modes, given by
G++(t ) ≡ 〈[ ˆ (0)
+ (t ), ˆ (0)†
+ (0)]〉 = ∑
q
|φq |2e−iEq t , (90)
rotates with an amplitude that is only slightly decreased compared to the homogeneous case. Indeed, we can place a lower bound on |G++(t)| using the triangle inequality,
|G++(t)|   |φ+|2 − ∑
q =+
|φq |2 = 2|φ+|2 − 1. (91)
Using the method of Sec. IV B, we obtain
ηc+ ≈ cos θ
2
[
1 − sin4 θ
2
(
2 + sec2 θ
2
)  ω2
2 2
]
, (92)
ηs+ ≈ sin θ
2
[
1 + tan2 θ
2 cos θ
(
1 + cos2 θ
2
)  ω2
2 2
]
, (93)
and the inequality (91) reads, to second order in  ω/  ,
|G++(t)|   2|φ+|2 − 1 ≈ 1 − 2Re
(
sin2 θ
2 tan2 θ
2
)  ω2
 2 ,
(94)
which yields |G++(t)|   1 −  ω2/ 2 for the resonant case
δ = 0, and |G++(t)|   1 − 4 ω2/ 2
gap for the off-resonant
gapping regime (δ  2/ ω, i.e.,  ω  gap). The leakage (1 − |G++(t)|) is thus bounded from above by
a quantity proportional to  ω2/  2. A similar bound can be derived for a  ˆ (0)
− excitation. The bound given by Eq. (91) is exact for a lossless system and valid for arbitrary coupling density. We emphasize, however, that these bounds are obtained by considering only the inhomogeneous distribution of the spin transition frequencies. Other relaxation mechanisms of the individual spins, such as spontaneous decay, dephasing, or spin diffusion, may still be significant sources of losses.
053852-10


 SPECTROSCOPIC PROPERTIES OF INHOMOGENEOUSLY . . . PHYSICAL REVIEW A 83, 053852 (2011)
V. CONCLUSION
We have studied highly polarized, inhomogeneously broad spin ensembles interacting with a single mode of a cavity. Using the resolvent formalism, we have shown how the transmission spectrum of the cavity depends on the density of spin states and the coupling-density profile, and how this coupling density can be obtained from the transmission spectrum. The strong superradiant coupling provides an energy gap for both the cavity and the superradiant spin-wave modes with respect to the subradiant modes. This gap may, in certain cases, efficiently protect the superradiant polariton and decrease its linewidth. We have investigated the criterion for the appearance of this gapping mechanism in the presence of
inhomogeneity, and provided corrections to the conventionally used picture of a driven two-level system. We have also considered two specific inhomogeneous coupling-density profiles: Lorentzian and Gaussian. We have shown that the gapping mechanism does not work for the former, and the polariton linewidth does not decrease with the collective coupling strength. For the latter, however, the gapping mechanism can efficiently reduce the polariton linewidth to a limit depending only on the cavity linewidth and the homogeneous linewidth of the individual spins. In general, we have found that the ensemble’s coupling density ρ(ω) should fall off as ω−3 or faster in order for the gapping mechanism to manifest itself as line narrowing.
[1] K. Hammerer, A. S. Sørensen, and E. S. Polzik, Rev. Mod. Phys. 82, 1041 (2010). [2] M. Fleischhauer and M. D. Lukin, Phys. Rev. Lett. 84, 5094 (2000). [3] L.-M. Duan, M. D. Lukin, J. I. Cirac, and P. Zoller, Nature (London) 414, 413 (2001). [4] N. W. Carlson, L. J. Rothberg, A. G. Yodh, W. R. Babbitt, and T. W. Mossberg, Opt. Lett. 8, 483 (1983). [5] M. Nilsson and S. Kr ̈oll, Opt. Commun. 247, 393 (2005). [6] B. Kraus, W. Tittel, N. Gisin, M. Nilsson, S. Kroll, and J. I. Cirac, Phys. Rev. A 73, 020302(R) (2006). [7] M. Afzelius, C. Simon, H. de Riedmatten, and N. Gisin, Phys. Rev. A 79, 052329 (2009). [8] M. Afzelius et al., Phys. Rev. Lett. 104, 040503 (2010). [9] M. Bonarota and T. C. J.-L. Le Gou ̈et, New J. Phys. 13, 013013 (2011). [10] F. Brennecke, T. Donner, S. Ritter, T. Bourdel, M. K ̈ohl, and T. Esslinger, Nature (London) 450, 268 (2007); Y. Colombe, T. Steinmetz, G. Dubois, F. Linke, D. Hunger, and J. Reichel, ibid. 450, 272 (2007). [11] P. F. Herskind, A. Dantan, J. P. Marler, M. Albert, and M. Drewsen, Nature Phys. 5, 494 (2009). [12] A. Andr ́e, D. DeMille, J. M. Doyle, M. D. Lukin, S. E. Maxwell, P. Rabl, R. J. Schoelkopf, and P. Zoller, Nature Phys. 2, 636 (2006). [13] K. Tordrup, A. Negretti, and K. Mølmer, Phys. Rev. Lett. 101, 040501 (2008). [14] J. H. Wesenberg, A. Ardavan, G. A. D. Briggs, J. J. L. Morton, R. J. Schoelkopf, D. I. Schuster, and K. Mølmer, Phys. Rev. Lett. 103, 070502 (2009). [15] D. I. Schuster et al., Phys. Rev. Lett. 105, 140501 (2010). [16] Y. Kubo et al., Phys. Rev. Lett. 105, 140502 (2010).
[17] P. Bushev, A. K. Feofanov, H. Rotzinger, I. Protopopov, J. H. Cole, G. Fischer, A. Lukashenko, and A. V. Ustinov, e-print arXiv:1102.3841. [18] R. Ro ̈hlsberger, K. Schlage, B. Sahoo, S. Couet, and R. R ̈uffer, Science 328, 1248 (2010). [19] H. Wu, R. E. George, J. H. Wesenberg, K. Mølmer, D. I. Schuster, R. J. Schoelkopf, K. M. Itoh, A. Ardavan, J. J. L. Morton, and G. A. D. Briggs, Phys. Rev. Lett. 105, 140503 (2010). [20] H.-P. Breuer, D. Burgarth, and F. Petruccione, Phys. Rev. B 70, 045323 (2004). [21] C. Cohen-Tannoudji, J. Dupont-Roc, and G. Grynberg, AtomPhoton Interactions: Basic Processes and Applications (Wiley, New York, 1992); M. E. Peskin and D. V. Schroeder, Introduction to Quantum Field Theory (Westview, Boulder, CO, 1995). [22] T. D. Lee, Phys. Rev. 95, 1329 (1954); K. O. Friedrichs, Commun. Pure Appl. Math. 1, 361 (1948).
[23] Lectures on Field Theory and the Many-Body Problem, edited by E. R. Caianiello (Academic, New York, 1961). [24] S. Stenholm, Opt. Commun. 179, 247 (2000). [25] R. Houdr ́e, R. P. Stanley, and M. Ilegems, Phys. Rev. A 53, 2711 (1996). [26] I. Diniz, S. Portolan, R. Ferreira, J. G ́erard, P. Bertet, and A. Auff`eves, e-print arXiv:1101.1842. [27] I. Chiorescu, N. Groll, S. Bertaina, T. Mori, and S. Myiashita, Phys. Rev. B 82, 024413 (2010). [28] A. Auff`eves, B. Besga, J.-M. G ́erard, and J.-P. Poizat, Phys. Rev. A 77, 063833 (2008). [29] G. Nikoghosyan and M. Fleischhauer, Phys. Rev. Lett. 103, 163603 (2009). [30] S. Sachdev, Phys. Rev. A 29, 2627 (1984). [31] J. H. Wesenberg, Z. Kurucz, and K. Mølmer, Phys. Rev. A 83, 023826 (2011). [32] Z. Kurucz, M. W. Sørensen, J. M. Taylor, M. D. Lukin, and M. Fleischhauer, Phys. Rev. Lett. 103, 010502 (2009).
053852-11
