# Manipulating the dipolar interactions and cooperative effects in confined geometries - Full Text

> Source: https://iopscience.iop.org/article/10.1088/1367-2630/ad42c7
> Collected: 2026-09-20
> Published: 2024-05-01
> Zotero parent key: KIZYV9NW
> Evidence: Zotero indexed PDF text

PAPER • OPEN ACCESS
Manipulating the dipolar interactions and cooperative effects in confined geometries
To cite this article: Hadiseh Alaeian etal 2024 NewJ.Phys. 26 055001
View the article online for updates and enhancements.
You may also like
The SPECTRAL Ice Chamber: Application to Titan’s Stratospheric Ice Clouds C. M. Anderson, D. Nna-Mvondo, R. E. Samuelson et al.

Titania Nanotube Array Sensor for Electrochemical Detection of Four Predominate Tuberculosis Volatile Biomarkers Dhiman Bhattacharyya, York R. Smith, Swomitra K. Mohanty et al.

Copper Corrosion Initiated by Butyric Acid Vapors E. Cano, E. M. Mora, H. Azcaray et al.

This content was downloaded from IP address 192.114.105.254 on 16/10/2024 at 10:14


 New J. Phys. 26 (2024) 055001 https://doi.org/10.1088/1367-2630/ad42c7
OPEN ACCESS
RECEIVED
9 January 2024
REVISED
12 April 2024
ACCEPTED FOR PUBLICATION 24 April 2024
PUBLISHED 7 May 2024
Original Content from this work may be used under the terms of the Creative Commons Attribution 4.0 licence.
Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
PAPER
Manipulating the dipolar interactions and cooperative effects in confined geometries
Hadiseh Alaeian1,∗, Artur Skljarow2, Stefan Scheel3, Tilman Pfau2 and Robert Löw2,∗
1 Elmore Family School of Electrical and Computer Engineering, Department of Physics and Astronomy, Purdue Quantum Science and Engineering Institute, Purdue University, West Lafayette, IN 47907, United States of America 2 5 Physikalisches Institut, Center for Integrated Quantum Science and Technology (IQST), Universität Stuttgart, Pfaffenwaldring 57, 70569 Stuttgart, Germany 3 Institut für Physik, Universität Rostock, Albert-Einstein-Straße 23-24, 18059 Rostock, Germany
∗ Authors to whom any correspondence should be addressed.
E-mail: halaeian@purdue.edu and r.loew@physik.uni-stuttgart.de
Keywords: dipole–dipole interaction, cooperative effects, spin model, mean-field theory, nonlinear optics
Abstract
To facilitate the transition of quantum effects from the controlled laboratory environment to practical real-world applications, there is a pressing need for scalable platforms. One promising strategy involves integrating thermal vapors with nanostructures designed to manipulate atomic interactions. In this tutorial, we aim to gain deeper insights into this by examining the behavior of thermal vapors that are confined within nanocavities or waveguides and exposed to near-resonant light. We explore the interactions between atoms in confined dense thermal vapors. Our investigation reveals deviations from the predictions of continuous electrodynamics models, including density-dependent line shifts and broadening effects. In particular, our results demonstrate that by carefully controlling the saturation of single atoms and the interactions among multiple atoms using nanostructures, along with controlling the geometry of the atomic cloud, it becomes possible to manipulate the effective optical nonlinearity of the entire atomic ensemble. This capability renders the hybrid thermal atom-nanophotonic platform a distinctive and valuable one for manipulating the collective effect and achieving substantial optical nonlinearities.
1. Introduction
Atoms represent ideal systems for investigating cooperative quantum phenomena due to their narrow radiative linewidth and consistent reproducibility. When photons are emitted by two distinct atoms, they often exhibit remarkable similarity, setting atoms apart from artificial light emitters such as quantum dots, vacancy centers, or rare-earth ions. Unlike these artificial emitters, atoms cannot be customized to user specifications but offer predictable properties with additional interactions involving their environment, like phonons or nuclear spins. In certain situations, cold and thermal atomic clouds can be confined very close to macroscopic surfaces, such as wedged vapor cells [1, 2], nano-fibers [3, 4], or atom-cladded nanophotonic devices [5–13]. In these cases, the electromagnetic characteristics of the macroscopic surroundings influence the interactions between the atomic dipoles. These effects can be analyzed within the framework of macroscopic quantum electrodynamics (mQED) [14, 15], which describes the quantized electromagnetic field in various absorptive and dispersive linear media using the classical electromagnetic Green’s tensor. This can be seen as a generalized mode expansion where photons occupy the same modes as classical wave counterparts. The theory accounts for quantum fluctuations in matter and fields, which can spontaneously polarize neutral atoms, leading to effective interactions with the surrounding macroscopic objects. This interaction with surfaces results in an additional radiative line shift, known as the Casimir–Polder shift [16]. It is one of several electromagnetic dispersion interactions caused by quantum vacuum fluctuations, depending on variations in atom and body properties with frequency.
© 2024 The Author(s). Published by IOP Publishing Ltd on behalf of the Institute of Physics and Deutsche Physikalische Gesellschaft


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Furthermore, in an ensemble of atoms where many dipoles interact simultaneously, new properties can emerge. Notable examples are altered spontaneous emission rates, referred to as sub- or superradiance, initially predicted by Dicke in 1954 [17] and elaborated on by Lehmberg [18, 19]. Resonant atom–atom interactions can have both positive and negative effects. For instance, in an array of atomic clocks, undesired interactions reduce coherence and precision. Conversely, they can be harnessed to engineer light-matter interactions, creating a perfect mirror using a single atomic or excitonic layer [20–24]. In a continuous medium, a polarized atom alters its local environment, affecting the local field at the position of other atoms, known as the local field correction. This is described by the density-dependent Lorentz–Lorenz shift. In a discrete medium of closely spaced individual atoms, superradiance results in a dispersive effective interaction, sometimes referred to as the cooperative Lamb shift [25], observed in thin atomic layers [26–28]. Various theoretical approaches have been proposed [29–33] to explain some but not all observed features. In systems with numerous interacting atoms in a disordered ensemble, the resulting inhomogeneous broadening of atomic resonance frequencies leads to saturation of the optical response, resulting in an effective refractive index of the atomic medium that reaches approximately n ≈ 1.7 [34]. This work employs a first-principle approach to unify interpretations and treatments of dipole–dipole interactions (DDIs) and cooperative effects in the literature. While the primary focus is on thermal atomic ensembles experiencing motional dephasing, the theoretical framework is broadly applicable. The paper’s structure is as follows: section 2 uses the most general formalism of mQED to derive the DDI, starting from the general quantum master equation. It discusses the impact of resonant and virtual photon transitions on cooperative shifts and interactions, shedding light on different approximations commonly used in literature to describe cooperative effects in various physical platforms across different limits. To the best of our knowledge, the approach presented here represents the first comprehensive quantum treatment of this problem. The section concludes by deriving the well-known spin model often used to describe cooperative effects in atomic systems. In section 3, the spin model is employed to calculate the evolution of the joint density matrix of the atomic ensemble in free space. For the two-atom case, the effective non-Hermitian Hamiltonian is directly diagonalized to determine the energies and decay rates of hybridized states, illustrating their sub(super)-radiant characteristics. The study is then extended to larger ensembles with more than two atoms, with a focus on thermal atoms subject to transit and Doppler broadening and dephasing. While exact diagonalization of the ensemble effective Hamiltonian becomes impractical in this limit due to the rapid dephasing of thermal atoms, rendering the mean-field (MF) approximation a valid approach. A Monte–Carlo approach is used to account for all motional effects, examining dipolar interactions in various dimensions, from 1D to 3D clouds, emphasizing the crucial role of geometry and dimensionality in emerging dipolar effects. Section 4 summarizes recent experiments that utilize thermal atoms to investigate and manipulate dipolar interactions. Finally, section 5 provides a summary of the results and suggests intriguing directions for exploring dipolar atomic ensembles at various dimensions.
2. Atom–atom interactions from first principles
The interaction of an atomic ensemble with a common light field leads to an effective light- induced DDI as well as cooperative effects [35, 36]. To derive the simplest case of light-induced dipolar interaction from first principles, we consider N atoms interacting with the electromagnetic field in free space. After tracing over the electromagnetic degrees of freedom, one obtains an effective DDI between the atoms. In what follows, we will start from the most general description of an atomic ensemble interacting with quantized electromagnetic fields to derive a quantum master equation that describes the evolution of the reduced atomic density matrix. Then, we show how, by employing several approximations such as the rotating wave, Born-Markov, and mean-field approximations, one obtains various descriptions of the interacting emitter ensemble including the well-known classical coupled dipole model. This pedagogical approach presented here clarifies the range of validity of each approximation and delimits their applicability in modeling the experimental scenarios and describing their results as summarized in section 4. In the most general form, and when expanded in Fourier space, the electric field operator reads [15]
Eˆ (R) =
ˆ∞
0
dω
(Eˆ(R, ω) + Eˆ† (R, ω)
)
, (1)
2


 New J. Phys. 26 (2024) 055001 H Alaeian et al
where Eˆ(R, ω) is related to ˆf(R, ω), the annihilation operator of the medium-assisted field excitation at position R and frequency ω, as [15, 37]
Eˆ(R, ω) = i
(ω
c
)2
√
 ̄h π ε0
ˆ
dR ′√Im (ε (R ′, ω)) G (R, R ′, ω) ˆf (R ′, ω) , (2)
where ε(R, ω) is the permittivity of the medium and G(R, R ′, ω) is the classical electromagnetic Green’s tensor determined via the Helmholtz equation [38] [
∇×∇×−
(ω
c
)2
ε (R, ω)
]
G (R, R ′, ω) = δ (R − R ′) I . (3)
For an ensemble of N multi-level atoms with transition frequencies ωn interacting with the continuum modes of the electromagnetic field, the total Hamiltonian reads as [39]
Hˆ = Hˆ A + Hˆ F + Hˆ AF =  ̄h ∑
A,n
ωA,nσˆA,nn +  ̄h
ˆ
dR
ˆ∞
0
dω ωˆf†ˆf −
∑
A
ˆdA · Eˆ (RA) , (4)
where the first and second terms correspond to the free atom and the electromagnetic field energies, respectively, and the last term describes the atom–field interaction to the leading order, i.e. in electric-dipole approximation. Further, σˆA,mn = |mA⟩⟨nA| are the spin transition operators between electronic levels n, m of the Ath atom, and dˆA is the transition dipole moment operator of the Ath atom as,
dˆA = −q ∑
m,n
⟨mA|rA|nA⟩σˆA,mn = dA,mnσˆA,mn . (5)
Note that, for a two-level atom, the above dipole operator simplifies to d (σˆ+
A + σˆ−
A
) in terms of the well-known raising and lowering spin operators σˆ±
A . Although a real atom is not a simple two-level system, later it will become evident under which circumstances this is a sensible approximation. The joint atom–field density operator evolves according to the von Neumann equation as
ρˆ ̇ (t) = − i
 ̄h
[Hˆ A + Hˆ F + Hˆ AF, ρˆ(t)] , (6)
with the formal solution, valid for a time-independent Hamiltonian,
ρˆ(t) = Uˆ (t) ρˆ(0) Uˆ † (t) , Uˆ (t) = e−itHˆ/ ̄h . (7)
To determine the atom–atom interaction, the electromagnetic degrees of freedom have to be integrated out to obtain the dynamics in terms of atomic quantities, only. This will become clearer in the interaction picture after rotating the joint atom–field density operator to the frame of the free atoms and photons given by Hˆ0 = Hˆ A + Hˆ F via a unitary transformation Uˆ 0(t) = e−itHˆ0/ ̄h
OˆI (t) = Uˆ †
0 (t) Oˆ (t) Uˆ 0 (t) . (8)
It is straightforward to show that the time evolution of the rotated joint density matrix in the interaction picture is given by
ρˆ ̇I (t) = − i
 ̄h
[Hˆ AFI (t) , ρˆI (t)] . (9)
The reduced atomic density matrix can be obtained by taking the partial trace over the electromagnetic field degrees of freedom as
ρˆIA (t) = TrF (ρˆI (t)) . (10)
As the goal is to derive an explicit equation of motion for the reduced atomic density matrix, we can directly use equation (10) in equation (9) to find the time evolution of ρˆIA(t). At this point, it is helpful to separate the interaction of the atom with the electromagnetic field into two parts; (1) the interaction with the driving field which is typically in a coherent state, and (2) the interaction
3


 New J. Phys. 26 (2024) 055001 H Alaeian et al
with other allowed modes, e.g. via the incoherent spontaneous emission into other electromagnetic modes in free space. Here the subscripts L and V refer to the first and the second case, respectively. We formally write the time evolution of the reduced atomic density matrix as
ρˆ ̇IA (t) = − i
 ̄h TrL
[Hˆ AFI (t) , ρˆI (t)] − i
 ̄h TrV
[Hˆ AFI (t) , ρˆI (t)] . (11)
The incoherently populated fluctuating electromagnetic modes can be described as spatially and spectrally uncorrelated fields with the following properties [40]:
⟨Eˆ (R, ω)⟩V = 0 ,
⟨Eˆ (R, ω) ⊗ Eˆ (R ′, ω ′)⟩V = 0 ,
⟨Eˆ† (R, ω) ⊗ Eˆ (R ′, ω ′)⟩V =  ̄hμ0ω2
π nT (ω) Im (G (R, R ′, ω)) δ (ω − ω ′) ,
⟨Eˆ (R, ω) ⊗ Eˆ† (R ′, ω ′)⟩V =  ̄hμ0ω2
π (1 + nT (ω)) Im (G (R, R ′, ω)) δ (ω − ω ′) ,
(12)
where nT(ω) is the mean number of thermal photons at temperature T and frequency ω determined via the Bose–Einstein distribution as
nT (ω) = 1
e
h ̄ω
kBT − 1
. (13)
As can be seen, the electric field vanishes on average, consistent with the assumption about their population via fluctuations, but the field intensity does not. Later, it will become clear that these contributions lead to stimulated emission (∝ nT(ω)) and absorption (∝ 1 + nT(ω)) triggered by thermal photons and the vacuum. The latter case is better known as spontaneous emission. Equation (9) can be formally solved for the interacting density matrix as
ρˆI (t) = ρˆI (0) − i
 ̄h
ˆt
0
dt ′ [Hˆ AFI (t ′) , ρˆI (t ′)] . (14)
As can be seen from equation (12), the non-driven, spontaneously occupied modes are described via their correlations, which implies that the formal solution equation (14) should be re-inserted into the second term of equation (11), i.e. fluctuating field contributions, leading to the equation of motion for the reduced atomic density matrix as
ρˆ ̇IA (t) = − i
 ̄h TrL
[Hˆ AFI (t) , ρˆI (t)] − i
 ̄h TrV
[Hˆ AFI (t) , ρˆI (0)] − 1
 ̄h2 TrV
ˆt
0
dt ′ [Hˆ AFI (t) , [Hˆ AFI (t ′) , ρˆI (t ′)]] .
(15) We assume that, at t = 0, atoms and fields are not correlated, and hence ρˆI(0) = ρˆA(0) ⊗ ρˆF 4. Under this condition the second term in equation (15) vanishes. Under the weak atom–field couplings, the field remains unchanged, i.e. ρˆ ̇F(t) = 0. This limit, known as Born approximation allows one to write the joint density matrix as a direct product of atoms and photon density matrices at all times, i.e. ρˆI(t) ≈ ρˆIA(t) ⊗ ρˆF [41]. In particular, this means that the joint evolution does not correlate or entangle atoms and light at any time step. Furthermore, if the atomic states change slowly enough compared to all other timescales, their time evolution is a Markovian process implying that ρˆIA(t ′) ≈ ρˆIA(t) 5. With these assumptions, equation (15) can be simplified to [42]
ρˆ ̇IA (t) = − i
 ̄h TrL
[Hˆ AFI (t) , ρˆIA (t) ⊗ ρˆF
]− 1
 ̄h2 TrV
ˆ∞
0
dt ′ [ ˆHAFI (t) , [Hˆ AFI (t − t ′) , ρˆIA (t) ⊗ ρˆF
]] , (16)
where in the last integral the limit is extended to ∞, justified by the finite correlation times of the field.
4 This is a strong assumption that has to be checked in each scenario. 5 This approximation is justified since the reduced density is already in the rotated frame and hence the fast-varying part has been already extracted.
4


 New J. Phys. 26 (2024) 055001 H Alaeian et al
2.1. Quantum master equation for the reduced atomic density matrix
Starting from equation (16), we first calculate the rotated interacting Hamiltonian Hˆ AFI as
Hˆ AFI (t) = −
∑
B
(
eit ˆHA / ̄h dˆB e−itHˆ A / ̄h )
·
(
eitHˆF/ ̄hEˆ (RB) e−itˆHF/ ̄h)
, (17)
where we used [Hˆ A, Hˆ F
] = 0, to separate the unitary rotation Uˆ 0(t) into atom and field parts. Using the explicit form of the atom–field interaction in the electric-dipole approximation limit, the Hamiltonian in the interaction picture reads as
Hˆ AFI = −
∑
B
∑
m,n
dB,mneiωB,mntσˆB,mn
} {{ }
dˆBI (t)
·
ˆ∞
0
dω
(
eiωtEˆ† (RB, ω) + e−iωtEˆ(RB, ω)
)
} {{ }
ˆHFI (t)
. (18)
Since the interaction Hamiltonian can be decomposed as Hˆ AFI = Hˆ AI ⊗ Hˆ FI , one can directly calculate the contribution of the driving field in equation (16) as [43]
TL = − i
 ̄h TrL
[Hˆ AFI (t), ρˆIA(t) ⊗ ρˆF
]
=− i
2 ̄h TrL
( [Hˆ AI (t), ρˆIA(t)] ⊗ {Hˆ FI , ρˆF
} + {Hˆ AI (t), ρˆIA(t)} ⊗ [Hˆ FI , ρˆF
])
=−i
 ̄h TrL
(Hˆ FI ρˆF
) [Hˆ AI (t), ρˆIA(t)] ,
(19)
where we used TrL[Hˆ FI , ρˆF] = 0 and TrL{Hˆ FI , ρˆF} = 2TrL(Hˆ FI ρˆF). Assuming the typical spectroscopy scenario using a coherent field |Er,ω⟩, the field density operator can be written as ρˆF = |Er,ω⟩⟨Er,ω| and hence the partial trace TrL over the field can be simplified as
TrL
(Hˆ FI ρˆF
) = TrL
ˆ∞
0
dω
(
eiωtEˆ† (RB, ω) + e−iωtEˆ(RB, ω)
)
|Er,ω ⟩⟨Er,ω |
=
ˆ∞
0
dω (eiωtEr∗,ω + e−iωtEr,ω
) = E (r, t) , (20)
where in the last line we employed the unity trace property of the density matrix ρˆF followed by the inverse Fourier transform to re-constitute the driving field in the time domain from its frequency components. This simplifies the driving field contribution to the evolution of the reduced atomic density matrix to
TL = i
 ̄h
[∑
B
dˆBI (t) · E (RB, t) , ρˆIA (t)
]
. (21)
The final equation is the Rabi Hamiltonian describing the dynamics of atoms driven by the classical field E(RB, t). As can be seen, the coupling of each atom to the driving field is independent of other atoms in the ensemble which is consistent with the aforementioned Born approximation. On the other hand, there will be effective atom–atom interactions that arise from the second term in equation (16). Those modes are not externally driven and are solely populated by photons emitted by the atoms, whose contributions can be determined as
TV = − 1
 ̄h2 TrV
ˆ∞
0
dt ′ [Hˆ AFI (t) , [Hˆ AFI (t − t ′) , ρˆIA (t) ⊗ ρˆF
]]
=− 1
 ̄h2
∑
C,D
ˆ∞
0
dt ′ dˆCI (t) · TrV
{EˆI (RC, t) ⊗ EˆI (RD, t − t ′) ρˆFI
} dˆDI (t − t ′) ρˆIA (t)
+1
 ̄h2
∑
C,D
ˆ∞
0
dt ′ dˆCI (t) ρˆIA (t) · TrV
{EˆI (RC, t) ⊗ EˆI (RD, t − t ′) ρˆFI
} dˆDI (t − t ′)
+1
 ̄h2
∑
C,D
ˆ∞
0
dt ′ dˆDI (t − t ′) · TrV
{EˆI (RD, t − t ′) ⊗ EˆI (RC, t) ρˆFI
} ρˆIA (t) dˆCI (t)
−1
 ̄h2
∑
C,D
ˆ∞
0
dt ′ρˆIA (t) dˆDI (t − t ′) · TrV
{EˆI (RD, t − t ′) ⊗ EˆI (RC, t) ρˆFI
} dˆCI (t) , (22)
5


 New J. Phys. 26 (2024) 055001 H Alaeian et al
where we used the identity
(v1 · v2) (v3 · v4) = v1 · (v2 ⊗ v3) v4 (23)
to re-write the integral kernels as tensor products. The correlation properties of these fluctuation fields summarized in equation (12) should be used to simplify the integral kernels, after employing the Fourier transformation, as
TrV
{EˆI (RC, t) ⊗ EˆI (RD, t − t ′) ρˆFI
}
=
ˆ∞
0
dωdω ′⟨E (RC, ω) E† (RD, ω ′)⟩Ve−i(ω−ω ′)t−i ω ′t ′
+
ˆ∞
0
dωdω ′⟨E† (RC, ω) E (RD, ω ′)⟩Vei(ω−ω ′)t+i ω ′t ′
=  ̄hμ0
π
ˆ∞
0
dω
(
(1 + n (ω)) e−iωt ′ + n (ω) eiωt ′ )
ω2Im (G (RC, RD, ω)) . (24)
Other terms of equation (22) can be calculated similarly and expressed in terms of photon density and Green’s tensor. Combining the results with equation (21) and inserting the final expression into equation (16), we obtain the quantum master equation for the reduced atomic density matrix ρˆIA(t) in the interaction picture. The atomic density operator in the original frame can be obtained using the unitary transformation ρˆA(t) = e−itˆHA/ ̄hρˆIA(t)eitˆHA/ ̄h. Using the explicit form of the dipole operator dC,D in terms of the dipole-allowed transitions as in equation (5), the evolution of the reduced atomic density matrix is given by
d
dt ρˆA (t) = − i
 ̄h
[
Hˆ A −
∑
B,m,n
dB,mn · E (RB, t) σˆB,mn, ρˆA (t)
]
+
∑
C,D,m,n,i,j
dC,mn · Hji (RC, RD) · dD,ij
(σˆC,mnσˆD,ijρˆA (t) − σˆD,ijρˆA (t) σˆC,mn
)
−
∑
C,D,m,n,i,j
dC,mn · Hj∗i (RC, RD) · dD,ij
(σˆC,mnρˆA (t) σˆD,ij − ρˆA (t) σˆD,ijσˆC,mn
) , (25)
where Hij(RC, RD) are the Green’s function-dependent coefficients for two atoms located at RC,D for jith transition, as detailed in [44]. As can be inferred from equation (25), the first line corresponds to the single-atom dynamics due to the free atom and the driving field. The second and the third lines, on the other hand, describe the light-induced atom–atom interaction, in the forms of spin exchange as σˆC,mnσˆD,ij. In the next subsection, we show how this general form can be used to derive the commonly-used simplified spin model master equation [45–50] as well as the well-known classical coupled dipole model in some specific limits.
2.2. The coupled-spin master equation and classical coupled-dipole limit
Using the Heisenberg equation of motion obtained from equation (25), one can study the atomic polarization generated by the atom-light interactions as well as the light-induced DDI within the ensemble. Let us assume that the driving field is a monochromatic coherent field as E0(r)e−iωLt + c.c., and it is near-resonant with only one of the electronic transitions at ω0, such that ωL − ω0 ≪ ωL − ωmn for ωmn being the transition frequency of other allowed transitions as (m ←→ n). This allows one to simplify the equations of motion noticeably, since such near-resonant exciting laser couples only those state pairs efficiently, while the far-detuned levels remained almost unperturbed and hence can be dropped from equation (25). Further, we assume a small detuning as ωL − ω0 ≪ ωL + ω0 which allows one to employ the rotating-wave approximation to further ignore fast-rotating, i.e. energy non-conserving, terms in the Rabi Hamiltonian, and only retain excitation-conserving terms. Using common notations of g, e for the states of this two-level atom with transition frequency ω0 and
with sub-levels of μ, ν, respectively, and in the rotated the frame of the laser σˆ ̃ge
Bμν (t) = σˆge
Bμν (t)eiωLt, the dipole moment of the Ath atom will be given as
⟨dˆA,ge⟩ = Σμ,ν ⟨σˆge
Bμν ⟩dge
Aμν . (26)
6


 New J. Phys. 26 (2024) 055001 H Alaeian et al
The time evolution of the spin operator is given via
d
dt ⟨σˆ ̃ge
Aμν (t)⟩ = i (ωL − ω0) ⟨σˆ ̃ge
Aμν (t)⟩ − i
 ̄h
∑
κ
(
⟨σˆ ̃eAeκν (t)⟩deg
Aκμ − ⟨σˆ ̃gg
Aμκ (t)⟩deg
Aνκ
)
· E0 (RA)
− i μ0ω02
 ̄h
∑
B̸=A
∑
δεκ
deg
Aκμ · G (RA, RB, ω0) · dge
Bδε ⟨σˆ ̃eAeκν (t) σˆ ̃ge
Bδε (t)⟩
+ i μ0ω02
 ̄h
∑
B̸=A
∑
δεκ
deg
Aνκ · G (RA, RB, ω0) · dge
Bδε ⟨σˆ ̃gg
Aμκ (t) σˆ ̃ge
Bδε (t)⟩
+i∑
ε
(
−ωeCP
Aνε + i ΓeAνε
2
)
⟨σˆ ̃ge
Aμε (t)⟩ +
(
ωgCP
Aμε + i Γg
Aμε
2
)
⟨σˆ ̃ge
Bεν (t)⟩ . (27)
This is the coupled-spin model, whose first line describes the dynamics of a coherently-driven atom, while the second line is the light-induced DDI due to the exchange of a real photon, i.e. a resonant photon that swaps the spins of the two atoms. In the last line ωCP, Γ corresponds to the collective phase shift and dissipation due to the other off-resonant electronic states of the atom [44]. Such a shift was first studied by Casimir and Polder and hence it is preferred to as Casimir–Polder (CP) shift [16], whose detailed form can be found in appendix. This treatment also takes into account the modifications of the local density of the optical states in any environment if the proper Green’s function is used. Physically, this leads to a modified decay rate, an effect first predicted and studied by Purcell [51, 52]. In general, the coupled-spin master equation of equation (27) leads to an infinite hierarchy of moments for the spins due to the spin correlation terms in the resonant DDI. However, if such correlations are ignored, the mean-field approximation can be employed to simplify them as ⟨σˆC,mn(t)σˆD,ij(t)⟩ ≈ ⟨σˆC,mn(t)⟩⟨σˆD,ij(t)⟩. This approximation converts the equations of motion to a closed system of coupled nonlinear equations.
Finally, in a weakly-driven limit, where the atoms are not strongly polarized, i.e. ⟨σˆeAe(t) − σˆgg
A (t)⟩ ≈ −1, the mean-field version of equation (27) simplifies to the familiar classical coupled-dipole model. In the next section, we start from the quantum master equation (27) to study the canonical problem of light-induced DDI between two atoms.
3. An interacting ensemble of atoms
Ignoring the fluctuation effects on the lineshift and broadening, and considering a near-resonant monochromatic coherent drive in the form of E0(R)e−iωLt (cf section 2.2), equation (25) for the reduced atomic ensemble density operator ρˆA(t) can be simplified to the following master equation
d dt
ρˆ ̃A (t) = − i

∑
B
∆Bσˆ+
B σˆ−
B−
( dB · E0 (RB)
 ̄h σˆ+
B + H.c.
) −
∑
C̸=B
εBCσˆ+
B σˆ−
C , ρˆ ̃A (t)


+
∑
B,C
κBC
(
σˆ−
B ρˆ ̃A (t) σˆ+
C −1
2
{
σˆ+
B σˆ−
C , ρˆ ̃A (t)
})
, (28)
where ∆B = ω0 − ωL is the detuning of the Bth atom from the excitation laser, εBC = 3π Γ0dB· Re(G(RB, RC, ω0)) · dC and κBC = 3π Γ0dB · Im(G(RB, RC, ω0)) · dC correspond to the dispersive and dissipative DDIs, respectively. Further, Γ0 is the decay rate of a two-level atom in free space and is related to the transition frequency ω0 and dipole matrix element d as
Γ0 = ω03
3π  ̄hε0c3 |d|2 . (29)
The dyadic Green’s function G(r, r ′, ω) depends on the geometry as well as the optical properties of the environment, and has a closed-form solution in only a few limited cases. In this section, we focus on the physics of such dipolar interactions by limiting ourselves to the simplest case, i.e. an atomic ensemble in free space, where a closed-form Green’s tensor with the following form is available [53]
G=
(
I+ 1
k20
∇∇
) eik0R
4π k0R , (30)
where R = |R2 − R1| and k0 = ω0/c.
7


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Using this Green’s function, the atom–field interaction energy is given by
G = k30eik0R
4π ε0k0R
[
(r × d1) × r + [3r (r · d1) − d1]
( 1
(k0R)2 − i
k0R
)]
· d2 , (31)
where r = (R2 − R1)/R is the unit vector between the two emitters. The dispersive and dissipative interaction effects are related to G via ε12 = Re(G) and κ12 = Im(G).
3.1. Canonical problem: two interacting atoms
To develop a better understanding of the DDI, we approximate the master equation (28) with a non-Hermitian Hamiltonian as
d dt
ρˆ ̃A (t) = −iHˆeffρˆ ̃A (t) + i ρˆ ̃A (t) Hˆ†
eff , (32)
where the effective non-Hermitian operator is
Hˆeff = Hˆ − i
( Γ0 2
(σˆ+
1 σˆ−
1 + σˆ+
2 σˆ−
2
) + κ12
(σˆ+
1 σˆ−
2 + σˆ+
2 σˆ−
1
))
. (33)
We start by writing Hˆeff in the two-spin basis of |1⟩ = |g1g2⟩, |2⟩ = |e1g2⟩, |3⟩ = |g1e2⟩, |4⟩ = |e1e2⟩ as
Heff =


0 −Ω1 −Ω2 0 −Ω1∗
(∆ − i Γ0
2
) − (ε12 + iκ12) −Ω2
−Ω2∗ − (ε12 + iκ12) (∆ − i Γ0
2
) −Ω1
0 −Ω2∗ −Ω1∗ (2∆ − i Γ0)

 . (34)
The effect of DDI can be clarified in the weak-probe limit, i.e. Ω1,2 ≈ 0, where the following new states can be determined
ω1 = 0 −→ |1⟩,
ω2 = (∆ − ε12) − i
2 (Γ0 + 2κ12) −→ |+⟩ = |2⟩ + |3⟩
√2
ω3 = (∆ + ε12) − i
2 (Γ0 − 2κ12) −→ |−⟩ = |2⟩ − |3⟩
√2
ω4 = 2∆ − iΓ0 −→ |4⟩, (35)
where the real and imaginary parts of ωi are the frequency of the normal mode and its corresponding decoherence rate, respectively. As can be seen, the interaction removes the degeneracy of the two entangled states |±⟩, splitting them to ∆ ∓ ε12 decaying at Γ0 ± 2κ12, respectively. Typically, the mode with the faster (slower) decay rate compared to an isolated atom is called the super (sub)-radiant state. In general, G describes a non-local and retarded interaction however by limiting oneself to the near-field only, i.e. k0R ≪ 1, G simplifies to
G ≈ 3r (r · d1) − d1
4π ε0R3 · d2 . (36)
This limit is typically referred to as the coherent interaction, where the interaction has a dispersive-only contribution (ε12 ̸= 0) without any dissipative part (κ12 = 0). It is straightforward to expand Green’s function for small inter-atomic separations k0R to find
d1 · Im(G)d2 ≃ k0
6π d1 · d2 − k30R2
60π [2d1 · d2 − (d1 · r) (d2 · r)] , (37)
where the first term is responsible for the decay rate Γ0, and the second term accounts for a finite propagation time between the two emitters. From the near-field form of equation (36) it is evident that in an atomic ensemble, the strongest interaction arises from two dominant arrangements of the atoms being arranged either side-by-side (blue-colored spheres) or head-to-tail (red-colored spheres). In the first case, r · d1 = 0, the interaction energy is positive and hence repulsive which leads to an increase in the energy and a blue-shift of the two-atom spectrum. On the other hand, for the head-to-tail configuration, the interaction energy is negative,
8


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Figure 1. Free-space dipole–dipole interaction of two polarized atoms. (a) The DDI-induced energy shift, vs. the distance between
two emitters r in units of the reduced wavelength λ ̄. (b) The DDI-induced broadening, for the same dipole orientations as in (a). (c) The energy of the two-atom case for two different orientations. In each case, configurations are depicted with arrows and higher levels indicate larger energies.
meaning an attractive potential and hence a red-shifted two-atom spectrum. Besides, as the near-field interaction scales as 1/R3 (cf equation (36)), the energy shift ε12 becomes proportional to the ensemble density. Beyond the near-field regime, however, Green’s function oscillates with distance R as a result of the retardation, hence the DDI-induced energy shift and the decay rates become strongly distance-dependent. In the rest of the text when needed for numerical calculations, we considered the 5S1/2 → 5P3/2 transition in rubidium. Figures 1(a) and (b) shows the real and imaginary parts of the light-induced interaction between two atoms as a function of their separation, respectively. In each panel, the side-by-side configuration case is shown in blue while the orange line shows the behavior of the head-to-tail configuration. Figure 1(c) summarizes the energies of the two interacting atoms when arranged head-to-tail or side-by-side compared to the individual atom energy. Figures 2(a)–(d) shows the excited state population of the two fixed atoms ⟨σˆee⟩ vs. detuning at different normalized inter-atomic spacing r, and four possible dipole orientations shown with black arrows. The corresponding lineshift, shown in figures 2(e)–(h), is extracted by fitting a Lorentzian to each spectrum, and the resonance is plotted as a function of the normalized inter-atomic spacing (kr)−3. As one can see, the induced lineshift scales linearly with the density (in 3D) due to the near-field R−3 scaling in equation (36). As discussed before, an attractive interaction leads to a negative shift, and a repulsive interaction to a positive one. Further, it is straightforward to check that for parallel spins, i.e. d1 · d2 ⩾ 0, the DDI in the side-by-side arrangement increases the energy by 3/4Γ0, while the head-to-tail configuration reduces the energy by 3/2Γ0. The estimated lineshift from the near-field approximation is plotted as a dashed line in figures 2(e)–(h), which is close to the exact solution obtained from the full Green’s function, shown in circles. In both cases, the attractive shift of the head-to-tail configuration is twice as strong as the repulsive shift of the side-by-side one. This simple near-field interaction picture will be useful when we investigate dipolar interactions in different dimensions in the next section. Figures 2(i)–(l) illustrates the dissipative effect of the DDI in modifying the decay rates of the collective states. For both optically-active cases in figures 2(i) and (j), the effective decay rate of the entangled states Γ′ is larger than the free space lifetime, hence it is a super-radiant mode. On the other hand, for the optically dark states shown in figures 2(k) and (l), the effective decay rates of the entangled states are smaller than the isolated atom implying a longer-lived and hence a sub-radiant state.
3.2. DDI in a thermal cloud in lower dimensions
To model the experiments involving thermal atoms subject to motional dephasing and the Doppler effect, as well as studies on cooperative effects in solid-state systems with spectral wandering, a detailed investigation of the inhomogeneous effects is required. In such cases, it is no longer sufficient to consider the fixed atoms as done so far. Instead, one has to take into account the random velocities and trajectories of individual atoms as well as a time- varying mutual interaction. The resulting Doppler and transit time effects play crucial roles in the optical properties of the ensemble and in modifying the static picture. To that end, we developed a Monte–Carlo algorithm to evolve the density matrix of the atomic ensemble in time, using the equations of motion derived in equation (27). Given that we are examining thermal atoms whose kinetic energies exceed that of photon recoil, a classical treatment suffices for the atom’s motion. In the 3D ensemble, we initialize the atoms with velocities in x, y, and z directions sampled randomly from a normal distribution with a mean determined by the cloud temperature. The atom follows a classical trajectory, evolving its state in each time step according to the generalized Bloch equations derived from the mean-field
9


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Figure 2. DDI vs. detuning and inter-atomic separation. (a)–(d) Waterfall plot of the excited state population ⟨σˆee⟩ of two stationary atoms as a function of probe detuning ∆ at different inter-atomic spacings. (e)–(h) The lineshift s and (i)–(l) linewidth Γ ′ of the spectrum vs. normalized distance (kr)−3 extracted from the corresponding spectrum in (a)–(d). All plots are color-coded with the colormap in the top left corner of the panel (a) that shows the inter-atomic distance r in units of the reduced
wavelength λ ̄. The rows are separated in head-to-tail (a), (e), (i), parallel side-by-side (b), (f), (j), anti-parallel side-by-side (c), (g), (k), and anti-parallel head-to-tail (d), (h), (l) configurations as depicted with arrows in each row at the right edge. Dashed lines in (e)–(h) mark simplified linear predictions ∝ r−3 for the lineshift. The driving field strength is Ω = 0.01Γ within the weak-probe limit.
approximation of equation (27). Upon collision with another atom or a wall, the atom undergoes quenching and returns to the ground state. Its emission during quenching is recorded and it resumes dynamics after velocity re-initialization. Using this stochastic approach we fully capture the motional effects such as Doppler and finite-time atom–field interactions. Figure 3 shows some important possible dipolar collisions with moving atoms in a typical thermal cloud. In all panels, we plot the difference in the excited state population between the interacting atoms ⟨σˆieent⟩ and
the non-interacting case ⟨σˆe0e⟩ with ∆σ = ⟨σˆieent⟩ − ⟨σˆe0e⟩. This way, we isolate the dynamics of the atomic states in the driving field from the interaction effects. In figure 3(a), two atoms start at t = 0 at a distance R and fly towards each other with identical velocities v1 = −v2. The atoms are shown as orange and purple circles, while the direction of motion of the atoms and the laser direction are depicted as black and red arrows, respectively. At t ≈ 2.2 μs, the atoms meet, an event that leads to a change in ∆σ as a result of the interaction. Further, as the dipolar forces are weak, they have negligible effects on the velocity of the fast-moving thermal atoms and hence the motion of atoms can be treated classically. The resulting oscillations of the excited state population quickly vanish as the distance between both atoms increases after the collision. Note that, the evolution is not identical for both atoms as they experience different Doppler shifts concerning the probe laser. When the probe direction is perpendicular to the atoms’ trajectories as shown in figure 3(b), the scenario for both atoms is symmetric, and hence both atoms evolve equally due to the driving laser as well as the mutual dipolar interactions. Unlike case (a) here, as soon as both atoms interact, they become detuned to the probe laser which leads to an overall smaller effect.
10


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Figure 3. DDI between two flying atoms. Dynamic dipole–dipole interaction of two flying atoms. The difference in the excited state population ∆σ between two interacting atoms and two non-interacting ones is plotted as a function of time-of-flight. The orange and purple curves correspond to individual atoms’ quantities. Four different probe laser (red arrow) configurations are considered: (a) counter-propagating atoms with (anti-) parallel probe, (b) counter-propagating atoms and orthogonal probe, (c) co-propagating atoms with a parallel probe, and (d) co-propagating atoms with an anti-parallel probe. The laser is linearly polarized with an out-of-plane field. The absolute velocities of all atoms are equal in each scenario. The driving field is weak Ω = 0.01Γ and the probe is resonant, i.e. ∆ = 0.
In figure 3(c) both atoms move in the side-by-side configuration and start at a distance of R = λ/20 with the same velocity v1 = v2. Due to their initial configuration, they interact from the start t = 0 and evolve towards a new steady state based on their identical detuning relative to the probe. As both atoms are in the near-field of one another at all times, they experience a strong repulsive interaction and hence a dipolar-induced blueshift. However, due to the relative motion of the atoms and the laser propagation, the driving field is Doppler shifted to lower energies, i.e. red-shifted. As a result, both atoms are shifted out of resonance which reduces their interaction. This is observable as a reduced oscillation. As their interaction decreases, the interaction-induced blueshift is reduced as well and hence their detuning decreases which consequently leads to their stronger polarization. This behavior is noticeable as a revived population in figure 3(c) at t ≈ 0.35. A similar scenario is depicted in figure 3(d), however, as both atoms travel toward the laser, the blue-detuned laser will be in resonance with the blueshifted atoms. Due to this resonant driving field and hence increased polarization, both atoms interact strongly with one another as can be seen in the amplitude of the oscillations compared to figure 3(c). All other interactions in an ensemble resulting from arbitrary trajectories of two atoms can be thought of in these four cases summarized in figure 3 with the only differences being the randomized orientations of the atoms and a larger coordination number. The previous results imply that the effect of dipolar interactions can be modified noticeably by changing the atomic orientations or the coordination numbers, so it is interesting to explore if the well-known cooperative effects can be modified via the ensemble geometry or dimensionality. From the two-atom discussions, it is evident that the ensemble can be confined such that certain dipole configurations are favored, e.g. the head-to-tail configuration dominates the ensemble when confined to 2D. To study this more
11


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Figure 4. Tunability of DDI with the ensemble dimensionality. Continuous transition of dipolar interactions from 2D to 1D without Purcell enhancement. (a) Waterfall plot of the excited state spectrum for different aspect ratios between transversal and longitudinal dimensions. The ratio Lz/Lx = Lz/Ly increases from bottom to top. Dashed lines show Voigt fits into the spectrum. (b) Lineshift and linewidth extracted from the Voigt fit as a function of transverse to longitudinal aspect ratio. Region I and Region II mark the regime where attractive and repulsive interactions dominate the spectrum, respectively. The density is kept constant for each aspect ratio. The transversal dimensions are Lx = Ly = 0.3λ. (c) Lineshift as a function of density for a 2D (I) and a 1D (II) probe volume referring to the markers in (b). Points represent simulated lineshifts, dashed lines are linear fits and solid lines show the expected lineshift for a simple picture of a static dipole ensemble in the near field with the associated dipole orientation. The driving field strength is Ω = 0.01Γ.
systematically, we start with a 2D ensemble with Lx = Ly = 0.3λ and Lz = 0.05λ and continuously increase the volume by increasing Lz such that the initial 2D geometry is changed to a pseudo-1D rectangular ‘tube’. The corresponding excited state population vs. detuning for various lengths and the energy shift extracted from these spectra as a function of the tube length transitioning from 2D to 1D is depicted in figures 4(a) and (b), respectively. Note that the linewidth is a result of the Doppler and transit time broadening, due to the small transversal dimensions Lx,y, as well as the frequent boundary collisions. The Doppler detuning emerges from the velocity component along the z-axis (parallel to the laser) which did not exist in the pure 2D case. The Doppler broadening continuously vanishes with decreasing Lz. The atoms with a large vz along the laser immediately collide with the wall and only scatter a small amount of the probe light, while atoms with small vz interact longer with the probe field and hence contribute to the signal more. This gradual contribution of the dephasing with increasing Lz leads to the broadening depicted in figure 4(b). For Lz ⩾ λ the broadening remains almost unchanged as the volume is large enough to fully resolve the dephasing along the z-axis and an equilibrium condition for the transversal collisions, along the x- and y-axis, is reached. The lineshift depicted in panel (b) is extracted from a Voigt fit to the simulated data in figure 4(a), shown as dashed lines in the same panel. One can see from the orange line in figure 4(b) that the interaction varies from an attractive to a repulsive corresponding to red and blue shifts, for Lz ⩽ Lx and Lz ⩾ Lx, respectively. The former is a quasi-2D scenario
12


 New J. Phys. 26 (2024) 055001 H Alaeian et al
where the head-to-tail configurations of the dipoles are dominant which leads to a redshift of the averaged spectrum. In contrast, the latter corresponds to an elongated pseudo-1D cloud and accommodates more side-by-side atom pairs with repulsive interactions which leads to a blueshift, ultimately. At Lx = Ly = Lz, denoted by a vertical dashed line in figure 4(b), the near-field dipole interactions from various arrangements cancel out each other and the collective shift vanishes. Hence, a rearrangement of dipoles using different confinements can switch the collective behavior from attractive to repulsive without manipulating each atom. Note that both, red-shift as well as blue-shift, saturate at Lz/Lx ⩽ 0.1 and Lx/Lz ⩾ 10, respectively, implying that at least an aspect ratio of ≈10 between transversal and longitudinal confinement is required to render the system to 2D or 1D. Figures 4(c) and (d) show the lineshift for different densities at simulation conditions marked with ‘I’ and ‘II’ in panel (b). Both shifts scale linearly with the normalized density (k0R)−3 as shown with linear fits (dashed line) to the simulated data (points). However, when compared to the near-field approximations (solid lines in figures 4(c) and (d)), the collective effect is noticeably weaker. This can be attributed to the perturbed repulsive interactions resulting in a blueshift in (II) by attractive interactions as the transversal dimensions are still finite such that occasionally atom pairs can be found in the head-to-tail configuration. After averaging, the excited state population over all atoms and time steps the effect of confinements along the x- and y-axis are noticeable as a reduction of the expected blueshift in a 1D ensemble. The same is true for the attractive interactions in (I). Overall, figure 4 shows that moving atoms confined in different free-space geometries do not behave similarly to the simple static two-atom cases explained in the previous section and one cannot extend the simple near-field interpretation as described with equation (36) to the free-space ensemble behavior. Also, the aspect ratio regarding transversal and longitudinal components plays a crucial role in the energy shift of the spectrum.
4. Experiments
Although collective light shifts caused by light-induced DDI were predicted 50 years ago in a seminal paper by Friedberg et al [25], it took a long time until the first experimental evidence of such a shift was provided. The actual shift depends on various parameters including the shape of the sample, the density, the level structures, the type of quantum emitters, and whether hot or ultracold atoms are used. As a side remark, the dipole–dipole shift is often termed the cooperative Lamb shift. However, this effect is not related to the fluctuations of the electromagnetic field, i.e. the origin of the Lamb shift derives from QED (cf appendix). Although Friedberg and Manassah, who initially coined this term, revisited their wording later [54], the term ‘Lamb shift’ is still meaningful in a historical context [55]. The first attempt to measure the collective response was conducted in an optically-excited thermal xenon gas in 1990 [56]. There, a three-photon excitation scheme in a macroscopic cell filled with xenon at high densities and large laser beams compared to wavelengths were used. The excitation scheme was chosen to avoid radiation trapping and incoherent multiple scattering, which can also lead to line broadenings and shifts [57, 58]. Further, laser beams were aligned at multiple angles to create 3D excitation volumes. Predominantly, the Lorentz–Lorenz shift, aka the Clausius–Mossotti shift, is anticipated to be the primary contributor to the observed line shift, typically manifesting as a redshift. Additionally, there are minor corrections attributable to collective effects, which are highly sensitive to the geometry of the excitation volume. However, these corrections are presumed to be minimal in a 3D sample, as the net effect of all DDIs is expected to average out to zero. Nonetheless, the obtained data shows an overall blueshift for most of the configurations. Compared to later experiments carried out in rubidium vapors as will be discussed in what follows, the shifts in xenon are roughly an order of magnitude larger. In [59], the authors have analyzed the shifts in various geometrical arrangements, including 3D configurations, identifying three key components of the lineshift: (1) the Coulomb term, (2) the cooperative Lamb shift (CLS), and (3) the resonant collision shift. For larger volumes, the Coulomb term also referred to as the Lorentz–Lorenz shift, is quantified as ∆LL = − Nd2
3ε0 ̄h , where N represents the ensemble density and d the transition dipole moment. The CLS
conceptualized as a virtual photon exchange between two atoms, introduces a correction in 3D, expressed as ∆CLS = ∆LL
4 . The final component, the resonant collision shift, arises from transient correlations in dipole orientations during close encounters between atoms, involving a permanent exchange of excitation. From the available information, it is hard to delimit the effect of multiple scattering. Even if such parasitic effects can be neglected, other effects such as excitation above saturation, transient interaction, Doppler selection, optical pumping, polarization, and laser linewidth may have influenced the experimental outcomes. Therefore, a re-investigation of these measurements in a more controlled experiment using today’s technology and modern narrow-band CW lasers will be beneficial.
13


 New J. Phys. 26 (2024) 055001 H Alaeian et al
It is worth emphasizing that, our approach and the numerical results incorporate all these factors, with the limitation that correlations beyond two-body interactions were not considered. Our simulations also indicate a shift towards 3D characteristics (cf figure 4). However, due to the limited size of the systems that we can simulate, it remains unclear how significant the impact of finite-size effects is in this context. In another experiment, x-rays were used to excite a solid iron sample inside a low-Q cavity [60]. They use a 14.4 keV excitation source, i.e. a wavelength of 86 pm, which is smaller than the iron lattice constant of 287 pm. The advantage of this experiment is the absence of atom–atom interactions, which simplifies the description. The collective response of the system was studied in terms of Dicke superradiance accompanied by a collective shift [61] and measured in the spectra of the superradiant burst. Further, the fluorescence lineshift showed a scaling with the number of iron atoms. This is not the typical density scaling as the density of the iron samples is constant. The larger number of atoms in a bigger iron sample N increased the number of atoms participating in a Dicke state, leading to an N-dependent lineshift and the superradiant time scale. The observed shifts are about 5 orders of magnitude smaller than those observed in rubidium (when compared via particle density), but of course, the x-ray wavelength is about 4 orders of magnitude smaller. This experiment is also hard to compare to Friedberg’s original proposal [25] since the collective effects are not due to light-induced DDIs. The distance between the quantum emitters is larger than the involved wavelength, a situation closer to the canonical Dicke model. Besides this, the experiment has been carried out in a cavity and in a transient regime, both of which are not present in the original Friedberg paper, either. Nonetheless, the theoretical model applied by the authors describes the observations rather well. As geometry plays a crucial role in modifying the collective effects, it is desirable to obtain good control over the actual arrangement of the quantum emitters and the excitation volume. The emitters should be as simple as possible, ideally, two-level systems, to simplify the description of the excitation dynamics and to reduce the complexity of any theoretical or numerical simulation. Alkali atoms with their lowest lying S to P transitions in the VIS/NIR domain are ideal candidates for this. The strength of the light-induced DDI becomes significant when the distance between the atoms gets smaller than the involved wavelengths. This can easily be achieved with thermal gases of alkali atoms, e.g. potassium, rubidium, and cesium, by heating the metal to 500–700 K. The drawback of such dense gases is their large optical depth and hence the very low signal-to-noise ratio. To study light-induced dipole- dipole interactions it is necessary to stay below the saturation intensity, i.e. a few mW cm−2. With densities similar to a BEC (e.g. at around 150 Celsius in a rubidium vapor) one obtains optical depths above 1 at a 1 μm thickness [62]. The solution is to use vapor cells with an extremely narrow spacing, ideally with a wedge-shaped spacing to adjust the thickness of the sample to thicknesses below 1 μm. With such wedged cells, two experiments have been performed in rubidium [26] and potassium [27]. The atoms have been excited in cell lengths ranging from (10 nm–μm) with laser beam diameters larger than the cell thickness and the excitation wavelength. The result is a 2D pancake-shaped atomic cloud where the expected cooperative collective shift is [25]
∆CLS = ∆LL − 3
4 ∆LL
(
1 − sin 2kL
2kL
)
, (38)
where L is the length of the vapor cell. For a very short vapor slab, the system is effectively two-dimensional. For high enough densities, the interaction is dominated by the non-retarded light-induced DDI in a plane, where the polarization lies in the plane of the atoms, and the attractive head-to-tail contribution of the DDI dominates over the repulsive side-by-side contribution resulting in a net red-shift (cf section 3 for detailed discussions). When extending the sample to L = λ/4, the retardation of the propagating laser leads to a π phase shift. The dipoles are now oriented in the opposite direction and the interaction results in a blueshift. Therefore, one expects an oscillation of ∆CLS as a function of the cell thickness which is consistent with the experimental observations. Further, the theory developed in [25] matches well with the experimental data although it does not consider the full quantum correlations between the atoms. A remaining oscillation of the data as a function of cell length can be explained by the effective refractive index of the atomic slab itself. In addition, there is a cavity effect induced by the cell walls as theoretically described in [33]. To avoid the undesired cavity effect of the wedged cells, one could employ the light-induced atomic desorption (LIAD) effect to desorb atoms from the cell surface via a pulsed laser. Using a short pulse, compared to the motion of the released atoms, for a very short time a 2D ensemble of atoms can be created. At high laser intensities, the density of this 2D sample can be large and the light-induced DDI effects can be studied. This has been recently observed in [2], where the scaling with the transition strength has been studied, by confirming the quadratic scaling of the lineshift between the D1 (795 nm) and D2 (780 nm) transitions in rubidium.
14


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Another potential candidate to measure collective lamb shifts in a 2D geometry is based on the total reflection of light from the glass wall of a vapor cell, where a very short-range evanescent field can be established inside the atomic vapor. This technique was used in a pioneering experiment in 1991 to observe the Lorentz–Lorenz shift in potassium vapor [63]. However, a clear signature of cooperative Lamb shifts has not been reported in similar experiments, so far. Finally, there exists one experimental result on a cooperative line shift in a 1D atomic ensemble [13]. The geometry, in this case, is set by the light mode confined in a slot waveguide. Since the slot is only 50 nm which is much smaller compared to the 1529 nm, the wavelength of the 5P-4D transition in rubidium used in that work, the atoms entering the light mode inside the waveguide are effectively arranged in one dimension. The polarization is perpendicular to the atomic chain, and hence the induced dipoles are parallel to each other. For close-by atoms, the DDI is repulsive and the line shift goes predominantly to the blue. An interesting aspect of having an optical structure close to the atoms is an enhanced Purcell factor favoring scattering into the waveguide mode [64]. This not only enhances the DDI along the waveguide but also changes the 1/r3 scaling in free space to an all-to-all interaction. To describe the observed line shift, the states of the atoms in a non-uniform field were determined using Bloch equations while the full motion of the atoms was included. In addition, the Casimir–Polder shifts of the atomic resonances due to the waveguide as well as a pairwise light-induced DDI have been included. This method, as detailed in section 3, led to an excellent agreement with the experimental data [13]. Over the last 33 years, there have been so far only 5 experimental results on the light-induced cooperative phenomenon in atoms. The sixth result is the thin iron foil experiment in a low-Q cavity, as described above. In thermal gases, the short coherence time allows a simplified theoretical treatment that neglects all higher-order quantum correlations, except the pair correlations between two atoms. For ultracold atoms, however, the behavior cannot be fully captured unless higher-order correlations are included. First experiments have been carried out in one-dimensional systems [65, 66], but more experiments are on the way. The potential to arrange ultracold atoms in optical tweezers in arbitrary configurations has inspired a lot of theoretical studies during the last five years. One candidate to implement many of these ideas relies on the low-lying clock transitions in the alkaline earth elements [67]. They are especially suited to study coherent collective and cooperative effects in ultracold atoms due to their long wavelength and the possibility of their side-band cooling to the ground state inside the tweezers. In parallel, there are attempts to use ensembles of solid-state quantum emitters to study collective effects [68, 69]. Solid-state emitters have several advantages compared to atoms as they are fixed in space, they can be closely packed to high densities, their excitation and emission wavelength are flexible, and they can be easily integrated with nano-photonic structures. Their main drawback is the dispersion of absorption/emission wavelengths among identical emitters, which makes it hard to observe collective effects. Also, the coupling to the environment, e.g. phonons, spin noise, and charge noise, leads to additional dephasing and shorter coherence times. We are not aware of any experiment observing light-induced interactions with many solid-state emitters thus far, except for a work observing a large collective Lamb shift of two coupled superconducting ‘atoms’ [70]. The key is the tunability of the emitters by external electric fields or via local strain of the supporting solid-state matrix. This has been achieved for optically active molecules frozen onto a surface at liquid helium temperature. Here two molecules were brought into resonance by electric field tuning [71]. Also, three strain-tuned quantum dots coupled via a photonic waveguide have been enabled to superradiate collectively [72]. How these methods can lead to a scalable approach has to be investigated in the future. What are the open questions an experiment can address? There is still only limited knowledge regarding the influence of geometry and dimensionality on the collective line shifts. Also, absorption and fluorescence have different properties, and the connection between super-/subradiance with the various sources of line shifts is not entirely understood. The role of coherence and quantum correlations is not very significant in thermal gases, but with longer coherence times in ultracold atoms, and ensembles of fixed solid-state emitters they become more relevant. Finally, one has to distinguish between the steady-state features and the transient responses. Both regimes are relevant to exploit dense ensembles of quantum emitters for quantum technologies, e.g. quantum sensors, single-photon storage, or light-driven quantum computers and simulators.
5. Conclusion
Our theoretical framework for examining thermal vapors within macroscopic environments marks an initial step towards exploiting the considerable adjustability afforded by this platform. However, it raises several pressing queries that require further exploration.
15


 New J. Phys. 26 (2024) 055001 H Alaeian et al
Firstly, there is a need to extend our coupled dipole model to accommodate large atomic densities analogous to those encountered in experimental setups. Moreover, it is imperative to include the temporal dynamics, accounting for atomic motion. This temporal consideration becomes pivotal in addressing nonlocal effects, variations in Doppler shifts, atomic collisions, and other dynamic phenomena. However, the principal impediment to this endeavor is the substantial numerical complexity involved in seeking exact solutions to the coupled dipole model. Recent advances, exemplified by the renormalization group approach, offer auspicious avenues to approximate solutions and potentially alleviate the computational demands [73]. This becomes particularly relevant if avenues for deriving (semi-)analytical solutions can be explored. An initial step entails investigating the feasibility of extending this approach to encompass the precise three-dimensional Green’s tensor associated with macroscopic geometries and stochastically include the Doppler effects. Secondly, our developed coupled-dipole model, originally applied to thermal, exhibits potential for broader applicability. It can be extended to scrutinize atom–atom interactions across a wider spectrum of macroscopic geometries. While extensive investigations into atom–atom interactions have occurred in oneand two-dimensional photonic crystals, the interaction between hot or cold atoms and diverse structures, such as microresonators, nanofibers, hollow-core fibers, superconducting chips, and atomic cladding waveguides, remain unexplored. Lastly, it is important to extend the analysis to Rydberg atoms. In numerous experiments, atom–atom interactions were of minimal concern due to low atomic densities. However, this scenario undergoes a transformation when atoms are excited to higher energy levels, particularly in Rydberg states. Transitions between Rydberg levels feature significantly smaller wavenumbers, necessitating fewer atoms to reach the critical density of 1/k3. Consequently, the coupled-dipole model needs to be extended in two critical aspects. Firstly, it should account for coherences between multiple atomic levels, given that Rydberg atoms are typically produced through a two-step excitation process. Secondly, the treatment of atom-wall and atom–atom interactions should adopt a self-consistent approach. Rydberg atoms are characterized by potent interactions and minute energy gaps between adjacent states, suggesting that the impact of interactions may no longer be perturbatively small. While many existing studies have addressed these aspects separately, a unified model capable of addressing dense thermal vapors within arbitrary geometries remains elusive. Ultimately, once we have comprehensively described all pertinent aspects of a system, the mQED formalism can showcase its full potential. A macroscopic environment, represented by the Green’s tensor, can be tailored to induce specific system behaviors. Over the long term, this inverse design approach holds the potential to enhance existing applications, including vapor-based single-photon sources and quantum memories, while also opening the door to entirely novel yet-to-come applications.
Data availability statement
The data that support the findings of this study are available from the corresponding authors upon reasonable request.
Acknowledgments
The authors would like to acknowledge stimulating and insightful discussions with H Dobbertin and C S Adams. H A acknowledges financial support from the Eliteprogramm of Baden-Württemberg Stiftung, DFG (GRK2642 ‘Photonic Quantum Engineers’) through the Mercator Fellowship, the Purdue University Startup fund, the financial support from the Industry-University Cooperative Research Center Program at the US National Science Foundation under Grant No. 2224960, and the Air Force Office of Scientific Research under Award Number FA9550-23-1-0489. We gratefully acknowledge Deutsche Forschungsgemeinschaft (DFG) through the Priority Programme 1929 ‘Giant Interaction in Rydberg systems (GiRyd)’ and Grant LO 1657/7-1 under DFG SPP 1929 GiRyd. We also gratefullyacknowledge the financial support by the Baden-WürttembergStiftung via Grant No. BWST-ISF2019-017 under theprogram Internationale Spitzenforschung.
Appendix. Casimir–Polder and Lamb Shift
In equation (27) of the main text we showed how one can obtain the well-known interacting spin model after several assumptions about the relative frequencies including the coherent drive frequency as well as the resonance frequency of the emitters. In particular, when the two-level approximation is valid the coupling of far-detuned transitions to the laser can be ignored in the DDI. However, the presence of these off-resonant
16


 New J. Phys. 26 (2024) 055001 H Alaeian et al
excitations and the photon exchange leads to additional collective corrections in terms of a frequency shift and a broadening. In this appendix, we present the detailed expressions for the collective off-resonant frequency shift, i.e.
ωmCP , and the collective decay due to the off-resonant transitions, i.e. Γm. Following the general expression of the atomic reduced density matrix and summing over all other transitions, we will get a state-dependent frequency shift as
ωmCP
Aνδ = − μ0ω2
 ̄h
∑
k,κ
dAmνkκ · {[Θ(ωA,mk) (n(ωA,mk) + 1)) − Θ(ωA,km)n(ωA,km)]
× Re(G(RA, RA, ωA,mk)) − 2kBT
 ̄h
∑ ∞
j =0
ωA,mkG(RA, RA, iξj)
ξj2 + ω2A,mk
} · dkAmκδ , (A.1)
as well as an additional broadening as
ΓAmνδ = 2μ0ω2
 ̄h
∑
k,κ
dAmνkκ · {[Θ(ωA,mk) (n(ωA,mk) + 1)) + Θ(ωA,km)n(ωA,km)]
× Im(G(RA, RA, ωA,mk))} · dkAmκδ . (A.2)
Here, ξj = 2π kBT
 ̄h j denotes the Matsubara frequencies, originating from the poles of the Bose–Einstein distribution on the imaginary axis [15]. Remarkably, the finite temperature only changes the shift and broadening through the density of the fluctuating photons, but does not contribute to the resonant DDI. As a limiting case, the broadening contains the free-space contribution at zero temperature. Furthermore, it includes the modifications of the local density of states due to the presence of any objects through the corresponding Green’s function G. This consequently leads to a modified decay rate as predicted by Purcell [51, 52]. To interpret the results of the collective shift and decay let us focus on the energy levels m, k. The expression dAnk · Re(G(RA, RA, ωA,mk) · dAnk describes the following phenomenon: atom A undergoes the m → k transition using a photon with frequency ωAmk that travels from the atoms to the environment and comes back to the atom where it is reabsorbed. The transitions are either triggered by the stimulated emission and absorption of a thermal photon (n(ωAmk )) or by the stimulated emission due to vacuum fluctuations (term 1). The free-space part of Green’s tensor formally gives an infinite result. But it can be renormalized and then gives the Lamb shift [40], which is complemented by an AC-Stark shift at the finite temperature. Such a shift in the presence of some macroscopic objects and not in the free space is the so-called Casimir–Polder shift. The free space Lamb shift is naturally independent of the macroscopic environment and the position of the atoms.
References
[1] Ripka F, Kübler H, Löw R and Pfau T 2018 Science 362 446–9 [2] Christaller F, Mäusezahl M, Moumtsilis F, Belz A, Kübler H, Alaeian H, Adams C S, Löw R and Pfau T 2022 Phys. Rev. Lett. 128 173401 [3] Mitsch R, Sayrin C, Albrecht B, Schneeweiss P and Rauschenbeutel A 2014 Nat. Commun. 5 446–9 [4] Le Kien F and Rauschenbeutel A 2017 Phys. Rev. A 95 023838 [5] Thompson J D, Tiecke T G, de Leon N P, Feist J, Akimov A V, Gullans M, Zibrov A S, Vuletic ́ V and Lukin M D 2013 Science 340 1202–5 [6] Stern L, Desiatov B, Goykhman I and Levy U 2013 Nat. Commun. 4 1548 [7] Goban A, Hung C L, Hood J D, Yu S P, Muniz J A, Painter O and Kimble H J 2015 Phys. Rev. Lett. 115 063601 [8] Ritter R, Gruhler N, Pernice W H P, Kübler H, Pfau T and Löw R 2015 Appl. Phys. Lett. 107 041101 [9] Ritter R, Gruhler N, Pernice W H P, Kübler H, Pfau T and Löw R 2016 New J. Phys. 18 103031 [10] Stern L, Desiatov B, Mazurski N and Levy U 2017 Nat. Commun. 8 14461 [11] Ritter R, Gruhler N, Dobbertin H, Kübler H, Scheel S, Pernice W, Pfau T and Löw R 2018 Phys. Rev. X 8 021032 [12] Skljarow A, Gruhler N, Pernice W, Kübler H, Pfau T, Löw R and Alaeian H 2020 Opt. Express 28 19593–607 [13] Skljarow A, Kübler H, Adams C S, Pfau T, Löw R and Alaeian H 2022 Phys. Rev. Res. 4 023073 [14] Sandoghdar V, Sukenik C I, Hinds E A and Haroche S 1992 Phys. Rev. Lett. 68 3432–5 [15] Scheel S and Buhmann S Y 2008 Acta Phys Slovaca 58 675–809 [16] Casimir H B G and Polder D 1948 Phys. Rev. 73 360 [17] Dicke R H 1954 Phys. Rev. 93 99 [18] Lehmberg R H 1970 Phys. Rev. A 2 883 [19] Lehmberg R H 1970 Phys. Rev. A 2 889 [20] Bettles R J, Gardiner S A and Adams C S 2016 Phys. Rev. Lett. 116 103602 [21] Shahmoon E, Wild D S, Lukin M D and Yelin S F 2017 Phys. Rev. Lett. 118 113601 [22] Zeytinogˇlu S, Roth C, Huber S and I ̇mamog ̆lu A 2017 Phys. Rev. A 96 031801
17


 New J. Phys. 26 (2024) 055001 H Alaeian et al
[23] Back P, Zeytinoglu S, Ijaz A, Kroner M and Imamog ̆lu A 2018 Phys. Rev. Lett. 120 037401 [24] Rui J, Wei D, Rubio-Abadal A, Hollerith S, Zeiher J, Stamper-Kurn D A, Gross C and Bloch J 2020 Nature 583 389 [25] Friedberg R, Hartmann S R and Manassah J T 1973 Phys. Rep. 3 101–79 [26] Keaveney J, Sargsyan A, Krohn U, Hughes I G, Sarkisyan D and Adams C S 2012 Phys. Rev. Lett. 108 173601 [27] Peyrot T, Sortais Y R P, Browaeys A, Sargsyan A, Sarkisyan D, Keaveney J, Hughes I G and Adams C S 2018 Phys. Rev. Lett. 120 243401 [28] Peyrot T, Sortais Y R P, Greffet J J, Browaeys A, Sargsyan A, Keaveney J, Hughes I G and Adams C S 2019 Phys. Rev. Lett. 122 113401 [29] Rzaz ̇ewski K and  ̇Zakowicz W 1980 J. Math. Phys. 21 378–88 [30] Lewenstein M and Rzazewski K 1980 J. Phys. A: Math. Gen. 13 743 [31] Ruostekoski J and Javanainen J 1997 Phys. Rev. A 55 513–26 [32] Javanainen J, Ruostekoski J, Li Y and Yoo S M 2014 Phys. Rev. Lett. 112 113603 [33] Dobbertin H, Löw R and Scheel S 2020 Phys. Rev. A 102 031701 [34] Andreoli F, Gullans M J, High A A, Browaeys A and Chang D E 2021 Phys. Rev. X 11 011026 [35] Passante R 2018 Symmetry 10 735 [36] Reitz M, Sommer C and Genes C 2022 PRX Quantum 3 010201 [37] Knöll L, Scheel S and Welsch D G 2001 QED in dispersing and absorbing dielectric media Coherence and Statistics of Photons and Atoms 1st edn, ed J Perˇina (Wiley-VCH) [38] Jackson J D 1999 Classical Electrodynamics 3rd edn (Wiley) [39] Cohen-Tannoudji C, Diu B and Laloe ̈ F 1977 Quantum Mechanics 1st edn (Wiley) [40] Buhmann S Y, Tarbutt M R, Scheel S and Hinds E A 2008 Phys. Rev. A 78 052901 [41] Breuer H P and Petruccione F 2002 The Theory of Open Quantum Systems (Oxford University Press)
[42] Gardiner C W and Zoller P 2004 Quantum Noise: a Handbook of Markovian and Non-Markovian Quantum Stochastic Methods With Applications to Quantum Optics (Springer) [43] Altafini C 2004 Phys. Rev. A 70 032331 [44] Dobbertin H 2021 Dipole-dipole interactions in confined planar geometries PhD Thesis University of Rostock [45] Manzoni M T, Mathey L and Chang D E 2017 Nat. Commun. 8 14696 [46] Chang D E, Douglas J S, González-Tudela A, Hung C L and Kimble H J 2018 Rev. Mod. Phys. 90 031002 [47] Albrecht A, Henriet L, Asenjo-Garcia A, Dieterle P B, Painter O and Chang D E 2019 New J. Phys. 21 025003 [48] Mahmoodian S, Calajó G, Chang D E, Hammerer K and Sørensen A S 2020 Phys. Rev. X 10 031011 [49] He Y, Ji L, Wang Y, Qiu L, Zhao J, Ma Y, Huang X, Wu S and Chang D E 2020 Phys. Rev. Lett. 125 213602 [50] Moreno-Cardoner M, Goncalves D and Chang D E 2021 Phys. Rev. Lett. 127 263602 [51] Purcell E M, Torrey H C and Pound R V 1946 Phys. Rev. 69 37–38
[52] Purcell E M 1995 Spontaneous Emission Probabilities at Radio Frequencies (Springer) p 839
[53] Novotny L and Hecht B 2012 Principles of Nano-Optics 2nd edn (Cambridge University Press) [54] Friedberg R and Manassah J T 2022 Atoms 10 49 [55] Scully M O and Svidzinsky A A 2010 Science 328 1239–41 [56] Garrett W R, Hart R C, Wray J E, Datskou I and Payne M G 1990 Phys. Rev. Lett. 64 1717–20 [57] Chevrollier M 2012 Contemp. Phys. 53 227–39 [58] Molisch A and Oehry B 1998 Radiation Trapping in Atomic Vapours (Oxford Science Publications) [59] Friedberg R, Hartmann S R and Manassah J T 1989 Phys. Rev. A 39 93–94 [60] Röhlsberger R, Schlage K, Sahoo B, Couet S and Rüffer R 2010 Science 328 1248–51 [61] Gross M and Haroche S 1982 Phys. Rep. 93 301–96 [62] Baluktsian T, Urban C, Bublat T, Giessen H, Löw R and Pfau T 2010 Opt. Lett. 35 1950–2 [63] Maki J J, Malcuit M S, Sipe J E and Boyd R W 1991 Phys. Rev. Lett. 67 972–5 [64] Asenjo-Garcia A, Hood J D, Chang D E and Kimble H J 2017 Phys. Rev. A 95 033818 [65] Glicenstein A, Ferioli G, Sˇibalic ́ N, Brossard L, Ferrier-Barbut I and Browaeys A 2020 Phys. Rev. Lett. 124 253602 [66] Maiwöger M, Sonnleitner M, Zhang T, Mazets I, Mallweger M, Rätzel D, Borselli F, Erne S, Schmiedmayer J and Haslinger P 2022 Phys. Rev. X 12 031018
[67] Olmos B, Yu D, Singh Y, Schreck F, Bongs K and Lesanovsky I 2013 Phys. Rev. Lett. 110 143602 [68] Pak D, Nandi A, Titze M, Bielejec E S, Alaeian H and Hosseini M 2022 Commun. Phys. 5 89 [69] Davis E J et al 2023 Nat. Phys. 19 836–44 [70] Wen P Y et al 2019 Phys. Rev. Lett. 123 233602 [71] Hettich C, Schmitt C, Zitzmann J, Kühn S, Gerhardt I and Sandoghdar V 2002 Science 298 385–9 [72] Grim J Q et al 2019 Nat. Mater. 18 963 [73] Grava S, He Y, Wu S and Chang D E 2022 New J. Phys. 24 013031
18
