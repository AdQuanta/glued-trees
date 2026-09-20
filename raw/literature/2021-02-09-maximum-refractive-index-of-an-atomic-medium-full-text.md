# Maximum Refractive Index of an Atomic Medium - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevX.11.011026
> Collected: 2026-09-20
> Published: 2021-02-09
> Zotero parent key: M52NG83I
> Evidence: Zotero indexed PDF text

Maximum Refractive Index of an Atomic Medium
Francesco Andreoli ,1 Michael J. Gullans ,2 Alexander A. High,3,4 Antoine Browaeys,5 and Darrick E. Chang 1,6 1ICFO—Institut de Cie`ncies Fotòniques, The Barcelona Institute of Science and Technology, 08860 Castelldefels, Spain 2Department of Physics, Princeton University, Princeton, New Jersey 08544, USA 3Pritzker School of Molecular Engineering, University of Chicago, Chicago, Illinois 60637, USA 4Center for Molecular Engineering and Materials Science Division, Argonne National Laboratory, Lemont, Illinois 60439, USA 5Universite ́ Paris-Saclay, Institut d’Optique Graduate School, CNRS, Laboratoire Charles Fabry, F-91127 Palaiseau, France 6ICREA—Institució Catalana de Recerca i Estudis Avançats, 08015 Barcelona, Spain
(Received 26 June 2020; revised 6 November 2020; accepted 18 December 2020; published 9 February 2021)
It is interesting to observe that all optical materials with a positive refractive index have a value of index that is of order unity. Surprisingly, though, a deep understanding of the mechanisms that lead to this universal behavior seems to be lacking. Moreover, this observation is difficult to reconcile with the fact that a single isolated atom is known to have a giant optical response, as characterized by a resonant scattering cross section that far exceeds its physical size. Here, we theoretically and numerically investigate the evolution of the optical properties of an ensemble of ideal atoms as a function of density, starting from the dilute gas limit, including the effects of multiple scattering and near-field interactions. Interestingly, despite the giant response of an isolated atom, we find that the maximum index does not indefinitely grow with increasing density but rather reaches a limiting value of n ≈ 1.7. This limit arises purely from electrodynamics, as it occurs at densities far below those where chemical processes become important. We propose an explanation based upon strong-disorder renormalization group theory, in which the nearfield interaction combined with random atomic positions results in an inhomogeneous broadening of atomic resonance frequencies. This mechanism ensures that, regardless of the physical atomic density, light at any given frequency only interacts with at most a few near-resonant atoms per cubic wavelength, thus limiting the maximum index attainable. Our work is a promising first step to understand the limits of the refractive index from a bottom-up, atomic physics perspective, and it also introduces the renormalization group as a powerful tool to understand the generally complex problem of multiple scattering of light overall.
DOI: 10.1103/PhysRevX.11.011026 Subject Areas: Atomic and Molecular Physics, Optics, Quantum Physics
I. INTRODUCTION
One interesting observation is that all the optical materials that we know of, with a positive index of refraction at visible wavelengths, universally have an index of order unity, n ∼ Oð1Þ. While we typically utilize materials far from their natural electronic resonances, this observation even holds true close to resonance [1–8]. Yet, despite the profound implications that an ultrahigh index material would have for optical technologies, a deep understanding of the origin of this apparently universal behavior seems to
be lacking. Furthermore, this property of real materials is not readily reconciled with the fact that a single isolated atom exhibits a giant scattering cross section σsc ∼ λ20 for photons resonant with an atomic transition of wavelength λ0 [Fig. 1(a)], which far exceeds both the physical size of the atom and the typical lattice constant of a solid (λ0 ∼ 1 μm for a typical optical transition, compared to the Bohr radius a0 ∼ 0.1 nm). In standard theories [9,10], the macroscopic index of an atomic medium [Fig. 1(b)] is constructed from the product of the single-atom polarizability and the atomic density,
and around resonance, its value n ∼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi Nλ30=V
q
extrapolates
to a maximum of about 105 at solid densities [Fig. 1(c)]. It is well known that this argument neglects multiple scattering of light and photon-mediated dipole-dipole interactions [11,12], and substantial work has been devoted to exploring
Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article’s title, journal citation, and DOI.
PHYSICAL REVIEW X 11, 011026 (2021)
Featured in Physics
2160-3308=21=11(1)=011026(17) 011026-1 Published by the American Physical Society


 their effects on various optical phenomena, such as collective resonance shifts [13–18], cooperative scattering properties [19–21], emergence of subradiance and superradiance [22–27], realization of atomic mirrors [28–30], and Anderson localization of light [31,32]. In particular, past work includes theoretical and experimental evidence that the optical response of dense gases can be much smaller than standard predictions [12,19,33–35] or even reach limiting values [36–42]. However, an underlying physical explanation is still missing, and our goal here is to
better understand the mechanisms that might limit the index even when operating close to resonance. Specifically, we investigate in detail the optical response of an ideal ensemble of identical, stationary atoms as a function of density starting from the dilute limit and well within the regime where the atoms do not interact chemically. In large-scale numerics (involving up to around 23 000 atoms, about an order of magnitude larger than comparable works [12,15,18–21,34,36–40]), we find that the maximum index does not indefinitely grow with density, and it saturates to a maximum value of n ≈ 1.7, when the typical distance between atoms becomes smaller than the length scale associated with the resonant cross section, i.e., d < λ0. Furthermore, we introduce an underlying theory based upon the strong-disorder renormalization group (RG), which has been a very successful technique to deal with highly varying interaction strengths in a wide variety of condensed matter systems [43–50]. In the context of our particular problem, the combination of strong near-field (∼1=r3) optical interactions and random atomic positions enables one to characterize the optical response of the system in terms of a hierarchy of strongly interacting, nearby atomic pairs. The shifts of the resonance frequencies arising from the near-field interactions then effectively yield an inhomogeneously broadened optical medium, where the amount of broadening linearly scales with density. This process implies that light of any given wavelength only interacts with at most around 1 nearresonant atom per reduced cubic wavelength λ30=ð2πÞ3, regardless of the physical atomic density, thus limiting the optical response [Fig. 1(d)]. Our results are potentially significant on a number of fronts. First, they provide a convincing picture of why typical theories for optical response, based upon a smooth density approximation, fail for dense, near-resonant atomic media, due to the important role of granularity and strong interactions of any given atom with a particularly close-by, single neighbor. Furthermore, our results show the promise of a bottom-up approach to understanding the physical limits of the refractive index, starting from objects (isolated atoms) whose optical responses are both huge and exquisitely understood. Separately, the existence of a fundamental mechanism that results in inhomogeneous broadening (i.e., dephasing) and saturation of optical properties at high densities, which occurs even for perfect, stationary atoms, should impose fundamental bounds on the maximum densities and minimum sizes of atom-light interfaces needed to realize high-fidelity quantum technologies. Finally, while we focus here on the linear optical response of a dense atomic medium, we believe that the validity of the RG is quite general and can constitute a versatile new tool for the generally challenging problem of multiple scattering in near-resonant disordered media [12,20,31, 34–37,40,51–53], including in the nonlinear and quantum regimes [54].
FIG. 1. Optical response of an atomic medium. (a) Illustration of a single atom with a dipole-allowed optical transition between ground and excited states, jgi and jei, characterized by a transition wavelength λ0 and spontaneous emission rate Γ0. Such an atom exhibits a scattering cross section (illustrated by the shaded region) of σsc ∼ λ20 for a single resonant photon (wavy green arrows). (b) In a dense ensemble with many atoms per cubic wavelength λ30, the scattering of an incident photon can involve multiple scattering and interference between atoms. (c) In conventional theories of macroscopic optical response, the atoms are approximated by a smooth medium, and the index is derived from the product of single-atom polarizability and density. The maximum index n near the atomic resonance
then scales with atomic density like n ∼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Nλ30=V
p . (d) In our renormalization group theory, we retain multiple scattering and granularity, showing that the optical properties of the ensemble are determined by a hierarchy of nearby atomic pairs that strongly interact via their near fields. These interactions effectively produce an inhomogeneously broadened ensemble, where the amount of broadening scales with density (with the different colors of atoms representing the different resonance frequencies in the figure). An incident photon of a given frequency thus sees only about 1 near-resonant atom per reduced cubic wavelength to interact with, regardless of atomic density, resulting in a maximum index of n ≈ 1.7.
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-2


 This paper is structured as follows. First, we briefly review the theoretical formulation of the multiple scattering problem of atoms or other pointlike dipoles and the standard atomic physics model of the refractive index, when atomic granularity and multiple scattering are ignored. We then formulate our large-scale numerical simulations, describing a few implementation details that allow the index to be efficiently calculated, and we show that the index eventually saturates with increasing density to a maximum value of n ≈ 1.7. We then introduce our RG theory, which highlights the importance of granularity and nearby atomic pairs on the macroscopic optical response, before concluding with an expanded discussion of future interesting directions to investigate.
II. FORMAL THEORY OF MULTIPLE SCATTERING
We consider a minimal system consisting of N identical, stationary two-level atoms. The atoms are assumed to have electronic ground and excited states, jgi and jei—with a frequency difference ω0 and an associated wavelength λ0 1⁄4 2πc=ω0—which have an electric-dipole transition
with a dipole matrix element along a fixed axis (say xˆ ), as depicted in Fig. 1(a). The excited states of the atoms decay purely radiatively, with a rate of Γ0 for a single isolated atom. As we are specifically interested in the linear refractive index, it is sufficient to treat atoms in the limit of classical, polarizable, radiating dipoles. In order to investigate the frequency-dependent index nðωÞ, we consider that the atoms are driven by a monochromatic, linearly polarized, input beam Einðr; ωÞ 1⁄4 Einðr; ωÞ ˆx, whose polarization aligns with the polarizability axis of the atoms. Each atom j acquires a dipole moment djðωÞ 1⁄4 djðωÞ ˆx, as a result of being driven by the total field, which consists of the sum of the incident field and fields rescattered from other atoms. Formally, the total field can be expressed as [55]
Eðr; ωÞ 1⁄4 Einðr; ωÞ þ μ0ω2 N X
j1⁄41
G ̄ ̄ ðr; rj; ωÞ · djðωÞ: ð1Þ
Here, the dyadic Green’s tensor  ̄ ̄Gðr; rj; ωÞ encodes the field at position r, produced by an oscillating dipole at rj, and in vacuum, it is given by [55]
G ̄ ̄ ðr; r0; ωÞ 1⁄4 k eiρ
4π
1
ρþ i
ρ2 − 1
ρ3 I
þ −1
ρ − 3i
ρ2 þ 3
ρ3
ρ⊗ρ
ρ2 ; ð2Þ
with the dimensionless distance defined as ρ ≡ jρj≡
kjðr − r0Þj and k 1⁄4 ω=c. Note that G ̄ ̄ ðr; r0; ωÞ contains both nonradiative, near-field (∼1=ρ3) and radiative, far-field (∼1=ρ) terms. Then, the induced dipole moment of atom i is given by
diðωÞ 1⁄4 α0ðωÞε0 Einðri; ωÞ
þ μ0ω2 NX−1
j≠i
ˆx ·  ̄ ̄Gðri; rj; ωÞ · ˆxdjðωÞ ; ð3Þ
where the parameter α0ðωÞ defines the polarizability of a single dipole. Although Eqs. (1) and (3) can describe any system of linearly polarizable, pointlike dipoles [55], e.g., dielectric nanoparticles [56], in our case we focus on the response of nonabsorbing, purely radiative atoms, whose resonant cross section σsc 1⁄4 3λ20=ð2πÞ is the maximum set by the unitarity limit [57]. In this context, the atomic polarizability reads α0ðωÞ 1⁄4 −3π=1⁄2ðΔ þ i=2Þk30 , where
k0 1⁄4 2π=λ0 denotes the resonant wave vector, while Δ ≡ ðω − ω0Þ=Γ0 represents the dimensionless detuning between the input beam frequency ω and the atomic resonance ω0. To relate to other work, we note that an equation identical to Eq. (3) can also be derived starting from a quantum mechanical formulation of atom-light interactions in the presence of multiple scattering, where the light-mediated interactions between atoms are encoded in a non-Hermitian Hamiltonian describing dipole-dipole interactions [23]. More precisely, one can focus on the regime where at most one atom is excited, which reflects the low-intensity limit of linear optics in which we are interested. Then, the steady-state wave-function amplitudes for atom i to be excited obey the same coupled equations of Eq. (3) [16,26,31,36,37]. While Eqs. (1) and (3) are formally exact, solving a number of equations that explicitly scale with the number of atoms and that depend on the details of atomic positions is not a particularly convenient way to calculate the index or other optical properties. Historically, this issue fostered the development of simplified theories for the macroscopic response, such as the Drude-Lorentz model [9] or, equivalently, the Maxwell-Bloch (MB) equations [10], where the discreteness of atoms is replaced by a smooth medium of density N=V [Fig. 1(c)]. The resulting index depends on the product of density and single-atom polarizability,
nMBðΔÞ 1⁄4
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1þN
V α0ðωÞ
r
1⁄4
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 þ 3πη
−Δ − i=2
s
; ð4Þ
where we defined the dimensionless density η ≡ N=ðVk30Þ. Notably, for an optimum detuning, the maximum real part
of the index scales like pffiηffiffi. While the MB equations ignore multiple scattering, the Lorentz-Lorenz (LL) or the equivalent Clausius-Mossotti model is one well-known approach to approximate its effects, still within the smooth density approximation. Given any atom located at r0, the model approximates the neighboring atoms as a smooth dielectric medium with a small spherical exclusion around r0 [9]. The resulting local field correction produced by the other atoms gives an
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-3


 index that satisfies the equation ðn2LL − 1Þ=ðn2LL þ 2Þ 1⁄4
ðN=VÞα0ðωÞ=3 [55]. Plugging in the atomic polarizability, one readily finds that
nLLðΔÞ 1⁄4 nMBðΔ þ πηÞ: ð5Þ
Importantly, while the spectrum is shifted with respect to the MB model, the LL model still produces a maximum
index that grows like pffiηffiffi.
III. COUPLED-DIPOLE SIMULATIONS
Equations (1) and (3) are ubiquitously used to model multiple scattering and interference effects involving a moderate number of pointlike scatterers. Here, we briefly introduce some key details of our implementation, which allows us to perform simulations on very high atom numbers and efficiently extract the index. First, one conceptually straightforward way to extract the complex refractive index of a material would be to take a slab of thickness d and large transverse extent and investigate the phase shift and attenuation of a quasiplane-wave incident field upon transmission. We approximately realize such a situation by taking atoms with a fixed density in a cylindrical volume centered around the origin, illuminated by a weakly focused, near-resonant Gaussian beam. Decomposing the position r 1⁄4 fr⊥; zg in terms of a transverse component r⊥ and axial component z, the beam amplitude within the paraxial approximation is given by Einðr; ω0Þ 1⁄4 E01⁄2w0=wðzÞ expf−1⁄2r⊥=wðzÞ 2 þ i1⁄2k0zþ φðr; w0Þ g, where wðzÞ 1⁄4 w0
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 þ ðz=zRÞ2
p describes the transverse extension of the beam while w0 1⁄4 wð0Þ is the beam waist at the focal plane and φðr; w0Þ accounts for the curvature of the wave front and for the Gouy phase [10] [see Fig. 2(a) for an illustration of the system]. This parameter is given by φðr; w0Þ 1⁄4 − arctanðz=zRÞ þ k0r2⊥=
f2z1⁄21 þ ðzR=zÞ2 g, with zR 1⁄4 k0w20=2. Given that the intensity of the beam drops off rapidly for transverse distances larger than wðzÞ, the parameters are chosen such that wðzÞ is small compared to the radius of the cylinder; thus, diffraction effects from the edges are negligible. Note that the cylindrical geometry has the nice feature that the furthest atoms are equidistant from the center of the beam, thus avoiding “wasting” computational resources, such as in a rectangular geometry, on atoms at the corners that hardly contribute to the optical response. Finally, we avoid very tight focusing, w0 ≲ λ0, where nonparaxial effects could emerge. We must also specify a practical definition of index for a granular system such as ours. In particular, since our atoms are purely scattering and have no absorption, it is well known [20,51,52,58] that for a fixed random spatial configuration, an input as in Fig. 2 produces a complex “speckle” pattern in the outgoing intensity when the system is optically dense, due to multiple scattering and
interference, as exemplified in Fig. 2(b). To isolate the part of the field that possesses a well-defined phase relationship with the incident field from realization to realization, we project Eq. (1) back into the same Gaussian mode as the input, as can be experimentally enforced by recollecting the transmitted light through a single mode fiber. This process results in a transmission coefficient tðΔÞ given by [36,59]
tðΔÞ 1⁄4 1 þ 3i
ðw0k0Þ2
N X
j1⁄41
Einðrj; ω0Þ
E0
cjðΔÞ; ð6Þ
where E0 is the input field amplitude at the beam focus. Here, for convenience, we have defined rescaled dipole
(a)
(b)
FIG. 2. Simulated physical system. (a) Cylindrical ensemble of randomly distributed atoms (green points) illuminated by a z-directed Gaussian beam, whose beam waist wðzÞ ≫ λ0 is represented in orange. The transverse radius of the cylinder is chosen to be much larger than the beam waist to avoid edge diffraction. (b) Color-coded 3D representation of the forward scattered intensity Iðr; ω0Þ 1⁄4 jEðr; ω0Þj2=ð2μ0cÞ (with the value indicated in the color bar) over a hemispherical surface far from the ensemble (the radius of this hemisphere is 35λ0), given an incident resonant Gaussian beam. The intensity is calculated for a single random atomic configuration. The system parameters used are as follows: beam waist w0 1⁄4 3λ0, cylinder radius lcyl 1⁄4 7λ0, and thickness d 1⁄4 2λ0.
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-4


 amplitudes cjðΔÞ 1⁄4 djðωÞk30=ð3πε0E0Þ, which satisfy the dimensionless coupled equations
−ΔciðΔÞ − N X
j1⁄41
GijcjðΔÞ 1⁄4 Einðri; ω0Þ
E0
: ð7Þ
In these equations, we define Gij ≡ ð3π=k0Þ ˆx ·  ̄ ̄Gðri;rj;ω0Þ · ˆx and Gjj 1⁄4 i=2, which coincides with the single-atom decay rate in units of Γ0, while regularizing the divergent
self-energy associated with the real part of  ̄ ̄G. Note that, for
simplicity, the Green’s function  ̄ ̄Gðri; rj; ω0Þ is only evaluated at the atomic resonance frequency, in order to ease the computational cost as the detuning is varied. Ignoring the
dispersion of  ̄ ̄G is an excellent approximation for nearresonant atoms, as the optical dispersion and delay of such a system is dominated by the atomic response itself rather than from the vacuum [60]. Similarly, we approximate the near-resonant input field as Einðri; ωÞ ≃ Einðri; ω0Þ. The expression in Eq. (6) represents a useful closed-form definition of the transmission coefficient tðΔÞ, which avoids a numerically expensive point-by-point evaluation of the scattered field Eðr; ωÞ, as nominally prescribed by Eq. (1). We can extrapolate the complex index of refraction nðΔÞ from the relation
htðΔÞi 1⁄4 exp fi1⁄2nðΔÞ − 1 k0dg; ð8Þ
where the averages are performed over about 103–104 sets of random positions, for each fixed density. Unlike in a smooth medium, we have that jhtðΔÞij2 ≠ hjtðΔÞj2i. Nevertheless, our definition of the index coincides with that often used within atomic physics (e.g., in phase contrast or absorption imaging of a Bose-Einstein condensate [61,62]). In the Appendix A, we demonstrate the
independence of the calculated index from the thickness d, which is implicitly assumed in Eq. (8). Alternatively, one might assume that the calculated htðΔÞi approximately coincides with the finite-slab Fresnel coefficients for a smooth material [63]. This assumption produces an alternative way to extrapolate the index, which we find yields quantitatively similar results to what we present below. In Fig. 3, we plot our numerical results for the real and imaginary parts of nðΔÞ, as a function of the input field detuning Δ, and for various densities. For comparison, we also plot the index as predicted by the MB equations, which starts to appreciably deviate from the full numerical results for dimensionless densities η ≳ 0.1. Interestingly, for sufficiently high densities, we observe that the computed spectra collapse onto the same curve when plotted as a function of the rescaled detuning Δ=η, as shown in the insets of Fig. 3, which include all plots in the range 2 ≲ η ≲ 3. The invariance of nðΔ=ηÞ for η ≳ 2 directly indicates that both the maximum real index and the attenuation per unit length acquire fixed values with increasing density and that density only determines a linear broadening in the spectra. Notably, the maximum real index saturates to a “real-life” value of around 1.7, in contrast to the indefinite growth predicted by both MB and LL. We note that a number of experiments involving dense cold atomic clouds have observed both a saturation of the index [38,40,41] and the emergence of an anomalous broadening of the linewidth [17,33,34,38,39], including a linear scaling with density [40,41]. A maximum index of n ≈ 1.26 has also been observed in experiments involving dense, hot atomic vapors [42], which has been attributed to atomic collisions. However, while complex collision dynamics necessitate semiphenomenological models [64], here, our mechanism for saturation is quite fundamental, and it occurs even for perfectly identical, stationary atoms.
30 20 10 0 10 20 30
0.0
0.5
1.0
1.5
2.0
Im(n)
30 20 10 0 10 20 30
0.5
1.0
1.5
Re (n)
0
1
2
3
(a) (b)
FIG. 3. Frequency-dependent refractive index for different atomic densities. The solid lines portray the imaginary (a) and real (b) parts of the refractive index versus dimensionless detuning Δ, obtained through Eq. (6), while the dotted lines show the MB predictions. The colors denote different atomic densities (color bar on the right), with the specific values indicated by the dotted white lines. The refractive index is inferred by averaging the complex transmission coefficient tðΔÞ over about 103–104 atomic configurations. Other system parameters are as follows: thickness d 1⁄4 0.4λ0, transverse radius 5 ≤ lcyl=λ0 ≤ 7, and beam waist 2.5 ≤ w0=λ0 ≤ 3. The insets show the curves at the three highest densities as a function of the rescaled detuning Δ=η.
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-5


 IV. INTRODUCTION OF RG SCHEME AND REFRACTIVE INDEX ANALYSIS
Our RG theory is based upon the key intuition gained in the collective scattering of just two atoms to build up an understanding of the many-atom problem in a hierarchical manner. To be specific, let us consider the problem of two identical atoms, whose distance is much smaller than a wavelength, ρ12 ≡ k0jr1 − r2j ≪ 1. Applying Eqs. (6) and (8), we can calculate the imaginary part of the “index” of the two-atom system, as illustrated in Fig. 4(a). One can see that the characteristic two-atom spectrum (blue line) is not twice the response of a single isolated atom (green dashed curve) but instead consists of two well-separated peaks with different linewidths and shifted resonances. To understand this behavior, we consider the normal modes of the two-atom system, as encoded in the eigenstates of the dimensionless matrix G, whose elements Gij were introduced in Eq. (7). When ρ12 ≪ 1, G is dominated by its off-diagonal components G12 1⁄4 G21 and, in particu
lar, by the purely real 1=ρ312 near-field term (which we
denote by Gnear
12 ). Specifically, in spherical coordinates
ρij ≡ ρijðcos θ ˆx þ sin θ cos φyˆ þ sin θ sin φzˆÞ, one obtains
Gnear
ij 1⁄4 3ð−1 þ 3cos2θÞ=ð4ρi3jÞ, which describes the strong, coherent, near-field coupling between the two dipoles. This process produces symmetric and antisymmetric eigenstates whose dimensionless normal-mode frequencies (real parts of the eigenvalues) are shifted as ω ≈ ∓ Gnear
12 and align with the resonant peaks seen in
Fig. 4(a). Given that Im G is also a 2 × 2 matrix with equal diagonal entries and equal off-diagonal entries, its eigenstates are also the same symmetric and antisymmetric modes. This case results in renormalized linewidths for these modes (given by the eigenvalues of Im G) of Γþ ≈ 2
and Γ− ≈ ρ212, which is simply the two-atom limit of the famous Dicke superradiance model [23]. The key insight is that, because of the large splitting, the total response in Fig. 4(a) is characterized by two well-separated resonances, which, although arising from the strong interaction of identical atoms, resemble the case of two inhomogeneous and noninteracting atoms, which were assigned these resonance frequencies and linewidths to start. This concept is at the heart of the RG approach for the many-atom case. We now discuss how strong, coherent, 1=ρi3j near-field interactions in a many-atom system can be treated by successively replacing strongly interacting pairs with optically equivalent, noninteracting atoms. Here, we focus on the main conceptual steps of our RG scheme, while additional justification of this scheme can be found in Sec. V. Given the discussion above, we anticipate that the scheme generates an optically equivalent ensemble containing atoms with different renormalized resonance frequencies ωi. Contrary to the two-atom case, however, the linewidths will not be renormalized within our RG scheme (see Sec. V). At any step of the RG flow, each pair
of atoms can either interact, or not, through the near-field coupling, depending on the previous RG steps. The normal modes of such a system are given by the eigenstates of the generalized N × N matrix M 1⁄4 diagðωÞ −  ̃G, where the elements G ̃ ij are defined as  ̃Gij 1⁄4 LijGnear
ij þ ðGij − Gnear
ij Þ. Here, diagðωÞ is a diagonal matrix containing the individual resonance frequencies ω 1⁄4 ðω1; ...; ωNÞ, while Lij 1⁄4 1 or 0 dictates whether the pair i, j is allowed to interact via the near field. At the beginning of the RG process, the optically equivalent ensemble corresponds to the physical one, and thus, all atoms are allowed to interact (Lij 1⁄4 1 for all pairs) and ωi 1⁄4 ω0. In three dimensions, the 1=ρ3 scaling of the nearfield interaction implies that if an atom has a particularly close-by and near-resonant neighbor, this pair will interact much more strongly with each other than with any other nearby atoms [43]. Suppose that atoms i, j (with Lij 1⁄4 1) are identified as the most strongly interacting pair by the prescription given below. Then, we can rewrite M as M 1⁄4 Mpair þ ðM − MpairÞ, where the only nonzero elements of Mpair involve atoms i, j. This effective 2 × 2 matrix reads
Mpair 1⁄4 hωiijI þ δωij −Gnear
ij
−Gnear
ij −δωij
; ð9Þ
where hωiij 1⁄4 ðωi þ ωjÞ=2 and δωij 1⁄4 ðωi − ωjÞ=2, and where we have included the coherent near-field interaction in Mpair. The remaining far-field interactions between atoms i and j, as well as near- and far-field interactions involving all other atoms, are included in ðM − MpairÞ. The large near-field interaction motivates diagonalizing Mpair first while treating ðM − MpairÞ as a perturbation. From the structure of Mpair, we define the pairwise interaction parameter Kij 1⁄4 LijjGnear
ij j=ðjδωijj þ 1Þ. A large value of Kij (which requires Lij 1⁄4 1) implies that the strong near-field interaction is able to strongly split the original resonances, including overcoming any possible differences in resonance frequencies δωij of the pair. We thus identify the most strongly interacting pair as that with the largest value of Kij, as pictorially depicted in the first panel of Fig. 4(b). Diagonalization of Mpair results in two, new, interacting resonance frequencies
ω 1⁄4 hωiij ∓
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
δωi2j þ ðGnear
ij Þ2
q
. We can then obtain an
approximately equivalent system by replacing the two original resonance frequencies ωi;j with the new values ω [second panel of Fig. 4(b)]. While the resulting normal modes are, in principle, delocalized between atoms i, j, to facilitate the RG, we randomly assign ωþ to either atom i or j, while ω− is then assigned to the other atom (see Appendix C on the issue of replacing atoms i, j with two new atoms placed at the midpoint of the original locations).
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-6


 This new system is described by a renormalized interaction matrix Meff 1⁄4 diagðωeffÞ −  ̃Geff, where ωeff 1⁄4 ðω1; ...; ωþ; ...; ω−; ...ωNÞ contains the two renormalized reso
nance frequencies and where G ̃ eff includes the new set of allowed near-field interactions Leff, which both forbid the renormalized pair from interacting again (i.e., Liejff 1⁄4 0) and prevent any backflow of the RG process (see Appendix B for more details). The RG process can be
iteratively repeated by identifying, at each step, the most strongly interacting pairs, and it ends once Kij ≤ Kcutoff ∼ 1, i.e., when all strong near-field interactions have been removed. In the numerics presented here, we take a cutoff parameter of Kcutoff 1⁄4 1. Other choices result in minor quantitative corrections, while the overall conclusions remain the same. The final result, as suggested in the third panel of Fig. 4(b), is that the original, homogeneous system
(a) (b)
(c) (d)
FIG. 4. Renormalization group analysis. (a) Representative optical response of two identical atoms separated by a distance ρ12 ≪ 1. Here, we plot the absorption spectrum (blue curve), which consists of two well-separated Lorentzians. The positions of the resonances are given approximately by ∓ Gn1e2ar, where Gn1e2ar ∝ 1=ρ312 is the near-field component of the Green’s function. To compare, we also plot twice the response of a single isolated atom (green dashed line). (b) Pictorial representation of the RG scheme for a many-atom system. At each step of the RG flow, the nearby pairs (identified by orange circles) that most strongly interact via their near fields are identified and replaced with atoms with different resonance frequencies (indicated by different colors) in such a way as to produce an equivalent optical response. At the end of the RG process (last panel), the overall system is equivalent to an inhomogeneously broadened ensemble of weakly interacting atoms. (c) Comparison between the maximum real refractive index predicted by the full coupled-dipole simulations of identical atoms (blue points), and the index of the equivalent, inhomogeneously broadened ensemble predicted by the RG (green). For each value of density, the maximum index is obtained by optimizing over detuning. For comparison, the MB and LL models both predict a maximum index given by the orange curve. The inset compares the rescaled spectra Re nðΔ=ηÞ of the RG (green) and full coupled-dipole (blue) simulations, given the points at densities η ≳ 2. (d) Rescaled probability distribution of effective, inhomogeneously broadened, resonance frequencies Pðωeff=ηÞ obtained from the application of the RG scheme. Given nine different values of the density η (ranging from η ≈ 2.5 up to η ≈ 80), the distributions of effective resonance frequencies are plotted with different colors, according to the bar on the right. The exact values chosen for the curves are emphasized by dotted white lines in the color bar. The curves at η ≈ 2.5 and η ≈ 3 are calculated using the cylindrical system studied in Fig. 3 (with thickness d 1⁄4 0.4λ0 and transverse radius lcyl 1⁄4 5λ0), while the distributions Pðωeff=ηÞ at densities η > 3 are evaluated using a spherical geometry of radius rsph 1⁄4 0.55λ0. Finally, for the case of density η ≈ 3, we plot (black dashed curve) the many-atom distribution of the eigenvalues of the near-field matrix −Gnear (also rescaled by a factor of 1=η for consistency), as discussed further in Sec. V. All distributions are obtained by accumulating results from about 100 different configurations of atomic positions.
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-7


 can be mapped to an optically equivalent system that is inhomogeneously broadened, with a smooth probability distribution of resonance frequencies PðωeffÞ. To validate the RG approach, we can use Eqs. (6) and (7) (with the near-field interactions of renormalized atoms suitably removed; see Appendix B) to calculate the maximum real index (optimized over detunings) as a function of density η of the ensemble with renormalized resonance frequencies. This is plotted in Fig. 4(c) (green), along with exact numerical simulations (blue) of Eq. (6) for the original system of identical atoms. These curves show good agreement for all densities and, in particular, reveal a maximum index of n ≈ 1.7 at high densities. For comparison, the maximum indexes of the MB and LL equations (orange) increase indefinitely with density. Furthermore, motivated by our previous observation that high-density spectra collapse onto the same curve when the detuning is rescaled by density [insets of Fig. 3 and Fig. 4(c)], in Fig. 4(d), we plot the rescaled probability distribution of effective resonance frequencies Pðωeff=ηÞ predicted by the RG. For all densities considered (2.5 ≲ η ≲ 80), we see that a single universal curve results; i.e., the amount of broadening grows directly with density. Based on this curve, we find that the number of near-resonant atoms per reduced cubic wavelength ðλ0=2πÞ3 1⁄4 k0−3,
within a range Γ0 of the original atomic resonance frequency, is approximately 0.3. The limited number of near-resonant atoms for light to interact with, regardless of how high the physical density is, directly explains the saturation of the maximum achievable index. We note that obtaining PðωeffÞ by the RG does not require solving the coupled equations of Eq. (7) but only the diagonalization of 2 × 2 pairwise matrices, and we can calculate this distribution for much higher densities up to η ∼ 80. Furthermore, as the RG only involves the “short-range” near-field interaction [see Eq. (9)], we expect the rescaled distribution to be unique in the bulk of the atomic medium. In other words, it should not depend sensitively on the specific geometry, provided that the system is sufficiently large that boundary effects are negligible. In Fig. 4(d), the curves for η ≤ 3 are obtained by a cylindrical geometry [the highest densities that we can compare to full coupled-dipole simulations, as in Fig. 4(c)]. For higher densities η > 3, when comparing with coupled-dipole simulations is no longer feasible, the extreme aspect ratio of the cylindrical geometry makes it inefficient to explore significantly higher densities using the RG. We then find it more efficient to switch to atoms within a spherical geometry, which has the smallest surface-area-to-volume ratio. Within the language of the RG, the universal distribution Pðωeff=ηÞ constitutes the (numerically obtained) fixed point, as the interaction parameter of a system flows toward Kij → 1. While it might be desirable to write down and analytically solve the RG flow equation for PðωeffÞ, this is quite challenging in our case because Kij not only depends
on the distance between atoms but also on their spatial orientation (as the near field is anisotropic) and the difference in resonance frequencies. As mentioned earlier, it is rather inconvenient to derive key optical properties of a system, like the index, by solving a set of equations [Eq. (7)] as large as the number of particles. At the same time, the RG approach clearly shows why conventional models (such as MB and LL) that treat atoms as a smooth medium fail at high densities [12,15,18] since the optical properties depend highly on granularity and on the strong interaction between an atom and a single, particularly close-by neighbor. Interestingly, the RG also provides a basis to develop a more accurate, smooth medium model. In particular, after the system is mapped to an inhomogeneously broadened distribution, PðωeffÞ, where near-field interactions and the influence of single neighbors are seen to be strongly reduced, one can finally apply a smooth medium approximation. Specifically, the MB equation [i.e., Eq. (4)] for the index can be readily generalized to an inhomogeneously broadened ensemble
nðΔÞ 1⁄4
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 þ 3πη
Z Pðωeff Þ
−Δ þ ωeff − i=2 dωeff
s
: ð10Þ
Substituting the distribution found in Fig. 4(d), at high densities η ≫ 1, this equation predicts a maximum index of n ≈ 1.8, in good agreement with full results. We stress that the emergence of a finite bound to the maximum index predicted by Eq. (10) can be directly related to the invariance of the distribution Pðωeff=ηÞ and thus to the linear growth of broadening with density.
V. MICROSCOPIC JUSTIFICATION OF THE RG SCHEME
In the previous section, we have established that our RG procedure reproduces well the dependence of the refractive index on density. We now present additional numerical and physical arguments that justify this approach and its approximations. Casual readers can consider skipping this section and jumping to Sec. VI. In this section, we specifically answer the following questions: (1) Strictly speaking, the RG is an approximate diagonalization of the many-atom near-field interaction matrix Gnear, in terms of pairwise blocks. Therefore, how well does our RG prescription reproduce the entire eigenvalue distribution of Gnear? (2) In our RG prescription, the collective symmetric and antisymmetric modes of two strongly interacting atoms are replaced by two new effective atoms with electric-dipole transitions and modified resonance frequencies. However, this prescription seemingly ignores the possibility that these modes (in particular, the antisymmetric one) could have a higher-order
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-8


 multipolar character. Then, why is such a replacement valid? (3) As a related point, these collective modes can be renormalized again if they strongly interact with a third nearby atom. As a higher-order multipolar mode can have a different scaling of the near field (∼1=ρ4 in the case of the antisymmetric mode), why does our replacement scheme with an electricdipole transition and a 1=ρ3 near-field interaction work? (4) Our RG prescription focuses on the strong interaction between nearby pairs due to the near field, but the 1=ρ far field associated with a radiating dipole might suggest that the large number of atoms far away from a given atom might have a dominant effect in the interactions. What justifies treating the near field first over the far field? (5) As seen in the case of just two interacting atoms [Fig. 4(a)], both the resonance frequencies and linewidths of the collective modes are modified. Thus, why is it incorrect to renormalize both resonance frequencies and linewidths pairwise in the many-atom problem?
A. Comparison of eigenvalue distributions
First, while we previously focused on the observable quantity of the refractive index, we note that mathematically, the RG approach is an attempt to approximately diagonalize the many-atom, near-field interaction matrix
Gnear
ij 1⁄4 3ð−1 þ 3cos2θÞ=ð4ρi3jÞ, in terms of pairwise blocks. We can thus test its accuracy by comparing the probability distribution of effective resonance frequencies PðωeffÞ obtained by the RG, with the probability distribution of the eigenvalues of −Gnear obtained by exact diagonalization of a many-atom, dense system. A remarkable agreement can be observed in Fig. 4(d), where the rescaled distribution of effective resonances Pðωeff=ηÞ is compared with the eigenvalue distribution of −Gnear (also rescaled by the density, black dashed curve), as calculated for the highest feasible density η ≈ 3 of our cylindrical system. We separately checked that different (higher) densities and different geometries give similar results. Although subtle, we point out, for future work, the presence of a slight asymmetry in the exact eigenvalue spectrum around ωeff 1⁄4 0, which does not appear in the RG-derived distribution PðωeffÞ. This asymmetry might arise from higherorder corrections to the RG (e.g., rare triplets of nearly equidistant atoms, where the pairwise picture fails).
B. Multipolar nature of collective modes
Even if the RG accurately predicts the resonance frequencies of a strongly interacting pair [e.g., the positions of the resonant peaks in Fig. 4(a)], one may wonder what the justification is for associating these two collective
modes with two new individual atoms, which we implicitly assumed, up to now, to be characterized by electric-dipole transitions like the original atoms. To frame the issue, we recall from Sec. IV that two, strongly interacting, identical atoms are diagonalized by a symmetric and an antisymmetric collective mode, where the two atomic electric dipoles, respectively, oscillate in phase or out of phase with one another. Clearly, the symmetric mode retains an electric-dipole character, as the two individual dipoles add to produce a dipole of doubled amplitude. This result can be observed in Fig. 5, where we compare the intensity pattern radiated by one single dipole d 1⁄4 d0 ˆx of fixed amplitude and direction [Fig. 5(a)] with that of two in-phase, close-by dipoles d1 1⁄4 d2 1⁄4 d0 ˆx [Fig. 5(b)]. However, the case of the antisymmetric mode is visibly more complex [Fig. 5(c)]. Intuitively, the two out-of-phase dipoles produce a vanishing electric-dipole response and are instead a hybrid of magnetic dipole and electric quadrupole modes. Interestingly, though, while the radiation pattern of Fig. 5(c) depends sensitively on the relative orientation of the two out-of-phase dipoles, if one averages over orientations, the pattern again closely resembles that of a
FIG. 5. Radiation pattern of a single dipole, compared to that of two in-phase or out-of-phase dipoles. (a) Given an isolated dipole d of fixed dipole amplitude d0 and direction xˆ , which is placed at ρ 1⁄4 0 and radiates light at the frequency ω0, we plot the intensity
of the radiated field IscðrÞ 1⁄4 jμ0ω20G ̄ ̄ ðr; ω0Þ · dj2=ð2μ0cÞ in the
xˆ − ˆz plane, with the value indicated in the color bar. (b,c)
Radiation pattern IscðrÞ 1⁄4 jμ0ω20
P
j1⁄41;2 G ̄ ̄ ðr − rj; ω0Þ · djj2= ð2μ0cÞ for two near-positioned dipoles of fixed amplitude d0 and direction xˆ , oscillating either in phase (b) or out of phase (c) with one another (i.e., d1 1⁄4 d2 1⁄4 d0xˆ ), and placed at
positions ρ1 1⁄4 −ρ2 1⁄4 0.1ðxˆ þ ˆzÞ=pffi2ffiffi. (d) Intensity radiated by two out-of-phase dipoles averaged over all possible interatomic orientations, keeping the mutual distance jρ1 − ρ2j 1⁄4 0.2 fixed. This pattern closely resembles that of a single oscillating dipole.
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-9


 single electric dipole [see Fig. 5(d)]. More concretely, in Appendix D, we show that the orientation-averaged, resonant scattering cross section associated with the antisymmetric mode is hσs−ci ≈ 0.94σsc, where we recall that
σsc 1⁄4 3λ20=ð2πÞ is the resonant cross section of a single atom with an electric dipolar response. To sum up, the antisymmetric mode, on average, is seen to behave almost identically to a single atom with an electric-dipole response, justifying such a replacement in our RG prescription. Furthermore, we show in Appendix D that this agreement is even stronger when considering pairs of strongly interacting atoms with different resonance frequencies δωij ≠ 0, which is a situation typically encountered in an actual RG flow.
C. Near-field interaction involving renormalized atoms
Having argued that the antisymmetric mode has an average optical response resembling that of a single electric dipole, we now turn to a second, related issue. Namely, since the antisymmetric mode is a hybrid of magnetic dipole and electric quadrupole modes, it should have a near-field scaling of 1=ρ4 at distances ρ much larger than the separation between the two composing atoms and much smaller than the optical wavelength. As the RG flow proceeds, a third atom that interacts strongly with this mode would then see such a scaling law at this distance [see Fig. 6(a)]. However, our RG prescription assumes that any new effective resonance has electric-dipole character and, in particular, around a 1=ρ3 near-field interaction with the third atom. We now argue that the RG prescription is a good approximation because, as the RG flow continues, it is likely that the third atom actually sits closer to one of the atoms in the pair (say, atom 1) than the pair separation itself [Fig. 6(b)]. In that case, the effective interaction strength between the antisymmetric mode of the pair and the third atom will scale as around 1=ρ313, exactly as if this mode was replaced by an electric dipolar atom. Mathematically, this case is possible because the interaction parameter Kij 1⁄4
jGnear
ij j=ðjδωijj þ 1Þ that governs when atoms are renormalized does not depend only on the closest distance of separation (via Gnear
ij ) but on the detunings δωij as well. To quantify this picture, we have run around 300 RG flows over random configurations of a dense medium (η 1⁄4 32) within a spherical geometry of radius rsph 1⁄4 0.55λ0. In Fig. 6(c), we plot several salient properties throughout the RG flow, averaged over the various runs. The horizontal axis denotes the relative position within the flow (0 ≤ NRG=Nfinal
RG ≤ 1). In particular, Nfinal
RG is the total number of pairs renormalized during the entire RG (starting from a homogeneous atomic medium, until one reaches Kij < Kcutoff 1⁄4 1 for all pairs), while NRG denotes the total number of renormalized pairs at any point in between. We recall that it is possible for an atom to be renormalized more than once, so that, in general, Nfinal
RG > N=2 for a dense
medium. For reference, in green, we plot the fraction N0=N of atoms that have never been renormalized up to that point. Notably, the fact that N0=N reaches nearly zero when NRG=Nfinal
RG ∼ 0.4 indicates that almost all renormalization events beyond this stage involve previously renormalized (and thus inhomogeneous) atoms. Separately, with blue circles, we show the average value of the interatomic distance between atoms comprising the renormalized pairs
(c)
(a) (b)
FIG. 6. Microscopic analysis of the renormalization of the antisymmetric modes. (a) Pictorial representation of the near-field interaction between the antisymmetric mode of a pair (represented by two out-of-phase dipoles, pink circles labeled 1 and 2) and a third atom (green circle, with label 3), which may sit very far from the pair (characterized by the distances ρ12 < ρ13 ∼ ρ23).
In this case, the interaction strength scales like 1=ρ413, reflecting the higher-order multipole nature of the out-of-phase dipoles. (b) Similar illustration for the case where the third atom sits closer to one atom of the pair (say, atom 1) than the pair separation itself (ρ13 < ρ12 ∼ ρ23). The interaction strength then scales like 1=ρ313. (c) System properties during the RG flow. The horizontal axis quantifies how many pairs NRG have been renormalized, from the beginning (NRG 1⁄4 0) towards the end (NRG 1⁄4 Nfinal
RG ) of the algorithm. As one atom can be renormalized more than once, typically Nfinal
RG > N=2. The blue circles represent the average interatomic distance ρRG of those pairs that get renormalized, while the orange squares show the average distance ρnearest between the atoms of those pairs and their respective nearest atom, chosen among those that are still allowed to interact (i.e., with Lij 1⁄4 1). The green triangles display the fraction of atoms N0=N that have never been renormalized up to that moment of the flow. The data represent the average over around 300 runs over different random atomic positions, uniformly sampled inside a sphere of radius rsph 1⁄4 0.55λ0 and density η ≈ 32. The bars show 1 standard deviation in the accumulated statistics.
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-10


 at that stage, and we compare it with the average distance between each atom of these pairs and its own nearest neighbor, as portrayed by the orange squares. As we are interested in the interaction between atoms that will possibly be renormalized in some subsequent RG step, we only count the nearest neighbors where Lij 1⁄4 1. The figure shows that we can roughly divide the RG flow into two parts. Before the critical value of NRG=Nfinal
RG ∼ 0.4, many atoms are still homogeneous, so the algorithm mostly renormalizes pairs of identical, nearest-neighbor atoms (as confirmed by the coincidence of the blue and orange curves). On the contrary, when NRG=Nfinal
RG ≳ 0.4, almost all atoms have already been renormalized at least once, and in particular, an effective atom representing an antisymmetric mode can potentially be renormalized again. In this regime, however, the nearest interacting neighbor to the two original atoms forming this mode is, on average, significantly closer than the distance between these two atoms, as evidenced by the blue curve being significantly higher than the orange one. This result confirms that the intuitive picture of Fig. 6(b) constitutes a typical case, which preserves the 1=ρ3 scaling of the nearfield interaction.
D. Near-field vs far-field interactions
We want to underline the importance of separating the effects of near-field and far-field interactions, which occur in an atomic medium. To this aim, we point out the historic work of Ref. [43], which used RG to understand the properties of permanent, static dipoles, which only experience a near-field 1=ρ3 interaction. Given only a near-field interaction in three dimensions, the interaction of a dipole with its nearest neighbor is then, indeed, dominant. However, we have a qualitatively different system of driven radiating dipoles. Naively, then, a similar argument considering the 1=ρ far field would suggest that atoms within a shell of radius ρ and ρ þ dρ of one atom at the origin would contribute an interaction strength of about ρdρ, such that the furthest atoms actually play the strong role. We argue that a RG process based on the near field is still the correct prescription, as the index should be a local property. Instead, the apparent “dominance” of the far field simply reflects the fact that the macroscopic geometry of an optical system (e.g., if it is shaped as a lens or prism) can drastically alter the overall optical response but not the index.
E. Linewidths in the RG prescription
Finally, we note that although the problem of just two atoms [Fig. 4(b)] can be interpreted in terms of renormalized resonance frequencies and linewidths, in the manyatom case, we only renormalize the resonance frequencies. As we discussed, the interaction between atoms is described by the dimensionless matrix G [as defined in Eq. (7)], whose real part Re G determines the coherent part of the interaction (i.e., the collective resonance
frequencies), while its imaginary part Im G is associated with the dissipative phenomena, thus dictating the collective linewidths. In the case of two identical atoms, Re G and Im G are both naturally and exactly diagonalized by the same symmetric and antisymmetric modes. However, in a many-atom ensemble, the different mathematical structures and physical origins of Re G and Im G become important. In particular, we recall that the 1=ρi3j near-field component of the Green’s function, Gnear
ij , is purely real and strongly divergent as two atoms approach each other, which motivates our RG theory based on diagonalizing these terms first. Physically, Im G does not contain a near-field term (recall that Im Gij → 1=2 as ρij → 0) since dissipation is associated with the radiation of energy into the far field. The absence of a near-field term implies that Im G does not yield an especially strong interaction between close atomic pairs and thus cannot be approximately diagonalized pairwise. Again, this makes sense physically because the emitted power by a collection of dipoles depends on the global interference between all dipoles and generally does not decompose into the sum of powers radiated by pairs. Separately, we have checked that if our RG prescription were modified to renormalize resonance frequencies and linewidths pairwise, it would predict a nonphysical optical response that tends to decrease (n → 1) in the limit of high densities, in contrast to the full numerical simulations.
VI. CONCLUSIONS
To summarize, we have shown that despite the large resonant scattering cross section of a single atom, a dense atomic medium does not exhibit an anomalously large optical response. Rather, strong near-field interactions between atomic pairs, combined with spatial disorder, result in an effective inhomogeneous broadening mechanism, which occurs even if the atoms are otherwise perfect, and yields a maximum index of n ≈ 1.7. The key role of atomic granularity in this process also illustrates why conventional smooth medium approximations fail to describe the near-resonant response. While we have focused on the linear refractive index, we believe that our RG formalism is valid, in general, for resonant disordered atomic media and that it constitutes a versatile new tool to study multiple scattering. Within the linear regime, the RG might be used to provide additional insight into the question of whether an Anderson localization transition exists in a 3D ensemble and, if so, under what conditions [31,32,53,65–67]. Furthermore, it would be interesting to explore the usage of RG toward the challenging problem of quantum, nonlinear scattering. As previously mentioned, the multiple scattering problem is formally encoded in a non-Hermitian Hamiltonian that describes light-mediated dipole-dipole interactions between atoms. In the limit of linear response, the resulting equations are equivalent to our coupled-dipole equations of Eq. (3), but
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-11


 beyond that, one is faced with the challenge of dealing with the exponentially large Hilbert space associated with N twolevel atoms. Perturbative diagrammatic approaches have only recently been developed to treat the dilute atom limit [54], but our understanding of the nonlinear physics beyond this regime is very limited. To this end, we hypothesize that a diagrammatic theory can also be developed in the dense, strong scattering regime, where strong interactions between nearby pairs are first nonperturbatively summed via the RG, while remaining interactions can be treated perturbatively. Our results could also have interesting implications for quantum technologies based on atomic ensembles. In particular, the total optical depth of a system, given by the product of the imaginary part of the index and system length, D ∼ ðIm nÞk0L, is a fundamental resource [68–70], with its magnitude establishing fundamental error bounds for most applications. As the imaginary part of the index also saturates with increasing density, this could place minimum size constraints on systems in order to achieve a given fidelity. Likewise, constraints on the maximum density could arise due to the induced inhomogeneous broadening, which typically constitutes an undesirable dephasing mechanism. Finally, it would be interesting to understand more fully how the optical properties of a dilute atomic medium eventually transform into the low refractive index of actual optical materials as the density is increased. Specifically, for a disordered ensemble, we have seen that the maximum index already saturates at densities that are approximately 6 orders of magnitude before the onset of chemical processes. We hypothesize that the onset of chemistry, and the phase transition toward a real material, does not qualitatively alter the optical response, provided that the system remains disordered and the electrons are tightly bound. Separately, it would be interesting to explore the same questions and transition for spatially ordered atomic systems, where the RG breaks down and one expects very different qualitative behavior, due to the possibility of strong constructive and destructive interference in light scattering. We note that there have been recent efforts to predict when a high index might occur within solid-state materials [71,72], and it would be interesting in future studies to develop a full theory combining quantum chemistry and multiple scattering to explore the transition from dilute atomic media to real materials.
ACKNOWLEDGMENTS
We acknowledge S. Grava, N. Fayard, J.-J. Greffet, S. Wu, and H. J. Kimble for stimulating discussions. F. A. acknowledges support from the ICFOstepstone–PhD Programme funded by the European Union’s Horizon 2020 Research and Innovation Programme under the Marie Skłodowska-Curie Grant Agreement No. 713729. D. E. C. acknowledges support from MINECO Severo Ochoa Grant No. CEX2019-000910-S, Generalitat de Catalunya through the CERCA program, Fundació
Privada Cellex, Fundació Mir-Puig, the European Union’s Horizon 2020 Research and Innovation Programme, under European Research Council Grant Agreement No. 639643, FET-Open Grant Agreement No. 899275 (DAALI), and Quantum Flagship Project 820445 (QIA), Plan Nacional Grant ALIQS (funded by Ministerio de Ciencia, Innovacion y Universidades, Agencia Estatal de Investigacion, and European Regional Development Fund), Fundación Ramón Areces Project CODEC, the Europa Excelencia program funded by Agencia Estatal de Investigacion (Project No. EUR2020112155, ENHANCE), and QuantumCAT (funded within the framework of the ERDF Operational Program of Catalonia, Ref. No. 001-P-001644).
APPENDIX A: LINEAR BEHAVIOR OF THE INDEX AS A FUNCTION OF THICKNESS
Our operative definition of the complex index of refraction, as given by Eq. (7) of the main text, is
htðΔÞi 1⁄4 exp fi1⁄2nðΔÞ − 1 k0dg: ðA1Þ
Since the refractive index is an intensive property by definition, it must not depend upon the thickness d that we choose in our numerics. Here, we show that our operative definition satisfies this condition. We consider the same physical system described in Fig. 2(a) of the main text, with w0 1⁄4 2.5λ0, lcyl 1⁄4 5λ0, and different values of the thickness. By applying Eqs. (6) and (7) of the main text, we compute the resonant (Δ 1⁄4 0) refractive index for growing values of the density η, and we plot its real or imaginary part in Figs. 7(a) and 7(b), respectively. The simulated values of the thickness are as follows: d 1⁄4 0.4λ0 (as in the main text, shown here in blue),
d 1⁄4 0.6λ0 (in green), and d 1⁄4 0.8λ0 (in orange). Moreover,
for the point at η ≃ 0.28, we evaluate the full spectra nðΔÞ, as represented in the insets of the figure. All curves show the same behavior, independently of d, both on resonance and when varying the detuning.
APPENDIX B: FULL DESCRIPTION OF RG ALGORITHM
Here, we provide a full description of the RG algorithm. We assume that we have an ensemble of N randomly positioned atoms. As shown in Eq. (7), each pair of atoms interacts through the coupling Gij 1⁄4
ð3π=k0Þ ˆx ·  ̄ ̄Gðρij; ω0Þ · ˆx, where ρij ≡ k0ðri − rjÞ. The 1=ρi3j near-field component of Gij reads
Gnear
ij 1⁄4 3
4ρi3j
ð−1 þ 3cos2θÞ; ðB1Þ
where we have represented ρij ≡ ρijðcos θ; sin θ cos φ;
sin θ sin φÞ in spherical coordinates. Here, we define
Gnear
jj 1⁄4 0, in accordance with the definition Gjj 1⁄4 i=2.
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-12


 This near-field interaction is purely real, and it describes a coherent interaction between dipoles. Let us now consider a generic step of the RG flow, where the atomic ensemble is already composed of effective atoms characterized by different atomic resonances and a specific set of allowed near-field interactions. As discussed in the main text, this system is described by the N × N matrix M 1⁄4 diagðωÞ − G ̃ , where the elements G ̃ ij read  ̃Gij 1⁄4 LijGnear
ij þ ðGij − Gnear
ij Þ. Numerically, this matrix is
initialized according to ωinit 1⁄4 ð0;...;0Þ and Liinjit 1⁄4 1 − δij, stating that all atoms are resonant at the frequency ω0 and cannot self-interact. At each step of the RG flow, we evaluate the list of couplings Kij 1⁄4 LijjGnear
ij j=ðjδωijj þ 1Þ [where δωij 1⁄4 ðωi − ωjÞ=2], ordering them from the largest to smallest in amplitude. Nominally, we should select the most strongly interacting pair and renormalize the pair properties, but the computational cost of this approach would be unfeasible for a large atom number. Therefore, we start from the most
strongly interacting pair (say, i, j), select it, and remove from the list all other pairs containing one of those atoms (e.g., i, k or j, k). We then proceed iteratively until we select Nstep most strongly interacting pairs. We choose Nstep to be a small fraction of the total atom number N (approximately 2.5%) since the maximum number of possible disjoint pairs scales as N=2. Nevertheless, we check that the results are insensitive to different choices. Given each pair ði; jÞ of the selected set, we diagonalize Mpair and define its eigenvalues as the new effective
resonances ω 1⁄4 hωiij ∓
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
δωi2j þ ðGnear
ij Þ2
q
, where hωiij 1⁄4
ðωi þ ωjÞ=2. We then substitute the initial frequencies (ωi, ωj) with the two new effective resonances in ω, the order of the labels being chosen randomly. We need to impose that the pair does not interact through the near field anymore, meaning that we must replace Liojld 1⁄4 1 with Linjew 1⁄4 0. At the same time, at any given stage of the RG flow, the resonance frequencies of any pair
(a) (b)
FIG. 7. Independence of the refractive index from the thickness of the ensemble. Given the physical system of Fig. 2(a) of the main text (with w0 1⁄4 2.5λ0, lcyl 1⁄4 5λ0), we compare the resonant (Δ 1⁄4 0) refractive index as a function of the density for various ensemble thicknesses: d 1⁄4 0.4λ0 (as in the main text, shown here in blue), d 1⁄4 0.6λ0 (in green), and d 1⁄4 0.8λ0 (in orange). Panels (a) and (b) illustrate the real and imaginary parts of the index, respectively. The insets show the full spectra nðΔÞ at a fixed density η ≃ 0.28. All data are obtained by averaging htðΔÞi over more than 1000 configurations.
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-13


 of effective atoms i and j might have been derived from a set of previous RG steps involving a set of atoms with indices fI0g and fJ0g, respectively. If the sets fI0g and fJ0g have some nonzero intersection, then atoms i and j must be omitted from a subsequent frequency renormalization step. Not omitting these atoms would violate the principle of the RG, that we are integrating or “freezing” out the degrees of freedom with the strongest interactions. Numerically, we efficiently enforce this constraint by replacing Lnew
ik 1⁄4 Lnew
jk 1⁄4 Lnew
ki 1⁄4 Lnew
kj 1⁄4 Lold
ik Lold
jk , ∀ k, anytime a pair ði; jÞ is renormalized. Since L has (at any step) zero-valued diagonal elements, this process directly ensures that Linjew 1⁄4 0. After all atoms of the step have been renormalized, we reevaluate the new set of K parameters and repeat the scheme. When all pairs exhibit K ≤ Kcut-off 1⁄4 1, we stop the RG flow, obtaining an ensemble of N inhomogeneously broadened atoms. Given a fixed value of the density η, we repeat this process for approximately 100 different spatial configurations in order to build up the final distribution PðωeffÞ. We extract the optical properties from the renormalized ensemble by applying Eq. (7) of the main text, modified in order to account for the new N × N matrix M emerging from the RG scheme. Thus, we obtain
ð−Δ þ ωiÞciðΔÞ − N X
j1⁄41
1⁄2Gij − ð1 − LijÞGnear
ij cjðΔÞ
1⁄4 Einðri; ω0Þ
E0
: ðB2Þ
APPENDIX C: DEFINITION OF EFFECTIVE POSITIONS IN THE RG SCHEME
In the main text [cf. Fig. 4(b)], we described how the optical response of a pair of atoms separated by a distance ρij ≪ 1 is characterized by two effective resonance frequencies, corresponding to the real parts of the eigenvalues of the two-atom system. The two collective modes are intrinsically delocalized in space (being formed by atoms with two different positions ri;j). As this delocalization is difficult to incorporate into the RG scheme, we instead attribute each of these two resonance frequencies to a new effective atom, with a well-defined position. In the main text, it was stated that the new effective atomic positions are assigned to those of the original pair, ri;j (randomly between the two possible permutations). A more natural choice, given that the two renormalized atoms are noninteracting, might be to place them at the midpoint ðri þ rjÞ=2 between the two original atoms, but here we discuss the problem with that approach. Specifically, for a finite-size sample, the atoms closest to the perimeter of the sample will only renormalize with
atoms that are closer to the interior. As illustrated in Fig. 8, this means that step by step, the shape of the cloud tends to shrink. This effectively distorts the ensemble and results in a higher density, as well as higher interaction strengths in the next step of the RG.
APPENDIX D: SCATTERING CROSS SECTION OF TWO NEAR-POSITIONED ATOMS
The optical response of an identical atomic pair is characterized by a symmetric and an antisymmetric normal mode. Here, we study the scattering cross sections of such modes, in the limit of near-positioned atoms. First of all, let us write the dimensionless positions (in units of k0−1) of the two atoms of the pair as
ρ1 1⁄4 −ρ2 1⁄4 ρ12
2 ðcos θ ˆx þ sin θ cos φyˆ þ sin θ sin φzˆÞ;
ðD1Þ
where ρ12 ≪ 1. The scattering cross section can be derived by means of the so-called optical theorem [9,73–78], which reads
σpair
sc ðΔÞ 1⁄4 σsc
2 Im
2 X
j1⁄41
EinðρjÞ
E0
cjðΔÞ; ðD2Þ
where σsc 1⁄4 3λ20=ð2πÞ is the resonant cross section of a single, isolated, electric dipolar atom, while the dimensionless coefficients cjðΔÞ are defined as in Eq. (7) of the main text. By plugging the solutions of Eq. (7) into Eq. (D2), one obtains a total cross section characterized by the two resonances ω , which are, respectively, associated with the symmetric and antisymmetric modes; thus, the resonant scattering cross sections of these two modes can be defined as σsc ≡ σpair
sc ðω Þ. In the limit where ρ12 ≪ 1, the two
resonances ω 1⁄4∓ ReG12∼ ∓ 1=ρ312 are well separated and can be efficiently resolved, leading to
FIG. 8. RG scheme based upon repositioning atoms. Because of the finite size of the sample, if one defines the positions of the new effective atoms as being at the midpoint between the original pair, then, at each RG step, the cloud effectively shrinks, resulting in a distortion of the ensemble.
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-14


 σsc
σsc
≃ ðE12 · v ÞðE12 · v Þ
Γ ; ðD3Þ
where we defined E12 ≡ fEinðρ1Þ; Einðρ2Þg=E0, as well as
the eigenstates v 1⁄4 f1; 1g=pffi2ffiffi and the decay rates Γ 1⁄4 1 2Im G12.
Assuming that the input field is either a ˆx-polarized, ˆz-directed Gaussian beam with w0 ≫ λ0 and focal point at r 1⁄4 0, or equivalently an ˆx-polarized, ˆz-directed plane wave, one can evaluate the cross sections in the limit of ρ12 ≪ 1, obtaining
σsþc
σsc
≃ 1; σs−cðθ; φÞ
σsc
≃ fðθ; φÞ
gðθÞ ; ðD4Þ
where fðθ; φÞ ≡ ðsin θ sin φÞ2 and gðθÞ ≡ 1⁄22 − cos2θ =5. As expected, the symmetric mode exhibits a perfect electric dipolar behavior, characterized by the same scattering cross section of a single isolated atom. On the contrary, the complex multipolar nature of the antisymmetric mode leads to a more complicated scattering cross section, which depends on the mutual orientation of the initial pair. This result suggests considering the average resonant cross section over all possible orientations of a pair, obtaining
σs−c
σsc
1⁄41
4π
Zπ
0
dθ
Z 2π
0
dφ σs−cðθ; φÞ
σsc
sin θ ≃ 0.94 ∼ 1;
ðD5Þ
which shows that, on average, the multipolar antisymmetric mode will scatter light very similarly to a pointlike dipolar atom. During the RG flow, one can also encounter pairs of effective atoms that have a detuning of δω12 1⁄4 ðω1 − ω2Þ=2 with respect to each other. In order for these pairs to strongly interact and be renormalized, the pairwise interaction parameter should satisfy K12 > 1,
which is roughly equivalent to jδω12=Gnear
12 j ≪ 1. In this limit, one can readily extend the previous calculation to the case of two different atoms. In particular, after averaging the resonant cross section of the (nearly) antisymmetric, multipolar mode over all possible orientations, one finds
σs−cðζÞ
σsc
1⁄45
2
2
641 − ð3ζ2 þ 1Þ
arctan h ffiffiffi1ffiffiffiffiffiffi
5ζ2þ2
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
5ζ2 þ 2
p
3
75; ðD6Þ
where ζ ≡ δω12=ðρ12Gnear
12 Þ, satisfying
0.94 ≲ σs−cðζÞ
σsc
≤ 1: ðD7Þ
Thus, we see that the multipolar mode of a pair of inequivalent atoms can also be well approximated in its optical response by a single electric dipolar atom.
[1] O. P. Rustgi, J. S. Nodvik, and G. L. Weissler, Optical Constants of Germanium in the Region 0–27 eV, Phys. Rev. 122, 1131 (1961). [2] H. R. Philipp and H. Ehrenreich, Optical Properties of Semiconductors, Phys. Rev. 129, 1550 (1963). [3] W. C. Walker and J. Osantowski, Ultraviolet Optical Properties of Diamond, Phys. Rev. 134, A153 (1964).
[4] P. L. Lamy, Optical Constants of Crystalline and Fused Quartz in the Far Ultraviolet, Appl. Opt. 16, 2212 (1977). [5] D. E. Aspnes and A. A. Studna, Dielectric Functions and Optical Parameters of Si, Ge, GaP, GaAs, GaSb, InP, InAs, and InSb from 1.5 to 6.0 eV, Phys. Rev. B 27, 985 (1983). [6] S. G. Warren, Optical Constants of Ice from the Ultraviolet to the Microwave, Appl. Opt. 23, 1206 (1984). [7] A. D. Papadopoulos and E. Anastassakis, Optical Properties of Diamond, Phys. Rev. B 43, 5090 (1991). [8] R. Kitamura, L. Pilon, and M. Jonasz, Optical Constants of Silica Glass from Extreme Ultraviolet to Far Infrared at Near Room Temperature, Appl. Opt. 46, 8118 (2007). [9] J. D. Jackson, Classical Electrodynamics, 3rd ed. (Wiley, New York, 1998).
[10] G. Grynberg et al., Introduction to Quantum Optics (Cambridge University Press, Cambridge, England, 2010). [11] M. Fleischhauer and S. F. Yelin, Radiative Atom-Atom Interactions in Optically Dense Media: Quantum Corrections to the Lorentz-Lorenz Formula, Phys. Rev. A 59, 2427 (1999). [12] J. Javanainen and J. Ruostekoski, Light Propagation beyond the Mean-Field Theory of Standard Optics, Opt. Express 24, 993 (2016).
[13] J. T. Manassah, Cooperative Radiation from Atoms in Different Geometries: Decay Rate and Frequency Shift, Adv. Opt. Photonics 4, 108 (2012). [14] J. Keaveney, A. Sargsyan, U. Krohn, I. G. Hughes, D. Sarkisyan, and C. S. Adams, Cooperative Lamb Shift in an Atomic Vapor Layer of Nanometer Thickness, Phys. Rev. Lett. 108, 173601 (2012). [15] J. Javanainen, J. Ruostekoski, Y. Li, and S.-M. Yoo, Shifts of a Resonance Line in a Dense Atomic Sample, Phys. Rev. Lett. 112, 113603 (2014).
[16] S. L. Bromley et al., Collective Atomic Scattering and Motional Effects in a Dense Coherent Medium, Nat. Commun. 7, 11039 (2016). [17] S. D. Jenkins, J. Ruostekoski, J. Javanainen, R. Bourgain, S. Jennewein, Y. R. P. Sortais, and A. Browaeys, Optical Resonance Shifts in the Fluorescence of Thermal and Cold Atomic Gases, Phys. Rev. Lett. 116, 183601 (2016). [18] H. Dobbertin, R. Löw, and S. Scheel, Collective DipoleDipole Interactions in Planar Nanocavities, Phys. Rev. A 102, 031701 (2020). [19] N. J. Schilder, C. Sauvan, J.-P. Hugonin, S. Jennewein, Y. R. P. Sortais, A. Browaeys, and J.-J. Greffet, Polaritonic Modes in a Dense Cloud of Cold Atoms, Phys. Rev. A 93, 063835 (2016).
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-15


 [20] N. J. Schilder, C. Sauvan, Y. R. P. Sortais, A. Browaeys, and J.-J. Greffet, Homogenization of an Ensemble of Interacting Resonant Scatterers, Phys. Rev. A 96, 013825 (2017). [21] N. J. Schilder, C. Sauvan, Y. R. P. Sortais, A. Browaeys, and J.-J. Greffet, Near-Resonant Light Scattering by a Subwavelength Ensemble of Identical Atoms, Phys. Rev. Lett. 124, 073403 (2020).
[22] R. H. Dicke, Coherence in Spontaneous Radiation Processes, Phys. Rev. 93, 99 (1954).
[23] M. Gross and S. Haroche, “Superradiance: An Essay on the Theory of Collective Spontaneous Emission, Phys. Rep. 93, 301 (1982). [24] S. J. Roof, K. J. Kemp, M. D. Havey, and I. M. Sokolov, Observation of Single-Photon Superradiance and the Cooperative Lamb Shift in an Extended Sample of Cold Atoms, Phys. Rev. Lett. 117, 073003 (2016). [25] M. O. Araújo, I. Krešić, R. Kaiser, and W. Guerin, Superradiance in a Large and Dilute Cloud of Cold Atoms in the Linear-Optics Regime, Phys. Rev. Lett. 117, 073002 (2016). [26] A. Asenjo-Garcia, M. Moreno-Cardoner, A. Albrecht, H. J. Kimble, and D. E. Chang, Exponential Improvement in Photon Storage Fidelities Using Subradiance and “Selective Radiance” in Atomic Arrays, Phys. Rev. X 7, 031024 (2017). [27] Y. He, L. Ji, Y. Wang, L. Qiu, J. Zhao, Y. Ma, X. Huang, S. Wu, and D. E. Chang, Geometric Control of Collective Spontaneous Emission, Phys. Rev. Lett. 125, 213602 (2020). [28] E. Shahmoon, D. S. Wild, M. D. Lukin, and S. F. Yelin, Cooperative Resonances in Light Scattering from TwoDimensional Atomic Arrays, Phys. Rev. Lett. 118, 113601 (2017). [29] R. J. Bettles, S. A. Gardiner, and C. S. Adams, Enhanced Optical Cross Section via Collective Coupling of Atomic Dipoles in a 2D Array, Phys. Rev. Lett. 116, 103602 (2016). [30] J. Rui, D. Wei, A. Rubio-Abadal, S. Hollerith, J. Zeiher, D. M. Stamper-Kurn, C. Gross, and I. Bloch, A Subradiant Optical Mirror Formed by a Single Structured Atomic Layer, Nature (London) 583, 369 (2020). [31] S. Skipetrov and I. Sokolov, Absence of Anderson Localization of Light in a Random Ensemble of Point Scatterers, Phys. Rev. Lett. 112, 023905 (2014). [32] S. E. Skipetrov and I. M. Sokolov, Search for Anderson Localization of Light by Cold Atoms in a Static Electric Field, Phys. Rev. B 99, 134201 (2019). [33] J. Pellegrino, R. Bourgain, S. Jennewein, Y. R. P. Sortais, A. Browaeys, S. D. Jenkins, and J. Ruostekoski, Observation of Suppression of Light Scattering Induced by DipoleDipole Interactions in a Cold-Atom Ensemble, Phys. Rev. Lett. 113, 133602 (2014). [34] S. Jennewein, L. Brossard, Y. R. P. Sortais, A. Browaeys, P. Cheinet, J. Robert, and P. Pillet, Coherent Scattering of Near-Resonant Light by a Dense, Microscopic Cloud of Cold Two-Level Atoms: Experiment Versus Theory, Phys. Rev. A 97, 053816 (2018). [35] W. Guerin, M. T. Rouabah, and R. Kaiser, Light Interacting with Atomic Ensembles: Collective, Cooperative and Mesoscopic Effects, J. Mod. Opt. 64, 895 (2017). [36] L. Chomaz, L. Corman, T. Yefsah, R. Desbuquois, and J. Dalibard, Absorption Imaging of a Quasi-Two-Dimensional
Gas: A Multiple Scattering Analysis, New J. Phys. 14, 055001 (2012). [37] B. Zhu, J. Cooper, J. Ye, and A. M. Rey, Light Scattering from Dense Cold Atomic Media, Phys. Rev. A 94, 023612 (2016). [38] S. D. Jenkins, J. Ruostekoski, J. Javanainen, S. Jennewein, R. Bourgain, J. Pellegrino, Y. R. P. Sortais, and A. Browaeys, Collective Resonance Fluorescence in Small and Dense Atom Clouds: Comparison between Theory and Experiment, Phys. Rev. A 94, 023842 (2016). [39] S. Jennewein, Y. R. P. Sortais, J.-J. Greffet, and A. Browaeys, Propagation of Light through Small Clouds of Cold Interacting Atoms, Phys. Rev. A 94, 053828 (2016). [40] L. Corman, J. L. Ville, R. Saint-Jalm, M. Aidelsburger, T. Bienaime ́, S. Nascimbe`ne, J. Dalibard, and J. Beugnon, Transmission of Near-Resonant Light through a Dense Slab of Cold Atoms, Phys. Rev. A 96, 053629 (2017). [41] S. Jennewein, M. Besbes, N. J. Schilder, S. D. Jenkins, C. Sauvan, J. Ruostekoski, J.-J. Greffet, Y. R. P. Sortais, and A. Browaeys, Coherent Scattering of Near-Resonant Light by a Dense Microscopic Cold Atomic Cloud, Phys. Rev. Lett. 116, 233601 (2016). [42] J. Keaveney, I. G. Hughes, A. Sargsyan, D. Sarkisyan, and C. S. Adams, Maximal Refraction and Superluminal Propagation in a Gaseous Nanolayer, Phys. Rev. Lett. 109, 233001 (2012).
[43] L. S. Levitov, Delocalization of Vibrational Modes Caused by Electric Dipole Interaction, Phys. Rev. Lett. 64, 547 (1990).
[44] D. S. Fisher, Random Antiferromagnetic Quantum Spin Chains, Phys. Rev. B 50, 3799 (1994). [45] K. Damle, O. Motrunich, and D. A. Huse, Dynamics and Transport in Random Antiferromagnetic Spin Chains, Phys. Rev. Lett. 84, 3434 (2000). [46] O. Motrunich, S.-C. Mau, D. A. Huse, and D. S. Fisher, Infinite-Randomness Quantum Ising Critical Fixed Points, Phys. Rev. B 61, 1160 (2000). [47] G. Refael and J. E. Moore, Entanglement Entropy of Random Quantum Critical Points in One Dimension, Phys. Rev. Lett. 93, 260602 (2004).
[48] F. Iglói and C. Monthus, Strong Disorder RG Approach of Random Systems, Phys. Rep. 412, 277 (2005).
[49] R. Vosk and E. Altman, Many-Body Localization in One Dimension as a Dynamical Renormalization Group Fixed Point, Phys. Rev. Lett. 110, 067204 (2013).
[50] G. Refael and E. Altman, Strong Disorder Renormalization Group Primer and the Superfluid-Insulator Transition, C.R. Phys. 14, 725 (2013). [51] A. Lagendijk and B. A. Van Tiggelen, Resonant Multiple Scattering of Light, Phys. Rep. 270, 143 (1996). [52] N. Fayard, A. Caz ́e, R. Pierrat, and R. Carminati, Intensity Correlations between Reflected and Transmitted Speckle Patterns, Phys. Rev. A 92, 033827 (2015). [53] F. Cottier, A. Cipris, R. Bachelard, and R. Kaiser, Microscopic and Macroscopic Signatures of 3D Anderson Localization of Light, Phys. Rev. Lett. 123, 083401 (2019). [54] T. Binninger, V. N. Shatokhin, A. Buchleitner, and T. Wellens, Nonlinear Quantum Transport of Light in a Cold Atomic Cloud, Phys. Rev. A 100, 033816 (2019).
ANDREOLI, GULLANS, HIGH, BROWAEYS, and CHANG PHYS. REV. X 11, 011026 (2021)
011026-16


 [55] L. Novotny and B. Hecht, Principles of Nano-Optics (Cambridge University Press, Cambridge, England, 2009). [56] F. J. G. De Abajo, Collective Oscillations in Optical Matter, Opt. Express 15, 11082 (2007). [57] P. De Vries, D. V. Van Coevorden, and A. Lagendijk, Point Scatterers for Classical Waves, Rev. Mod. Phys. 70, 447 (1998).
[58] B. Shapiro, Large Intensity Fluctuations for Wave Propagation in Random Media, Phys. Rev. Lett. 57, 2168 (1986). [59] M. T. Manzoni, M. Moreno-Cardoner, A. Asenjo-Garcia, J. V. Porto, A. V. Gorshkov, and D. E. Chang, Optimization of Photon Storage Fidelity in Ordered Atomic Arrays, New J. Phys. 20, 083048 (2018). [60] D. E. Chang, L. Jiang, A. V. Gorshkov, and H. J. Kimble, Cavity QED with Atomic Mirrors, New J. Phys. 14, 063003 (2012). [61] K. B. Davis, M. -O. Mewes, M. R. Andrews, N. J. van Druten, D. S. Durfee, D. M. Kurn, and W. Ketterle, BoseEinstein Condensation in a Gas of Sodium Atoms, Phys. Rev. Lett. 75, 3969 (1995). [62] M. H. Anderson, J. R. Ensher, M. R. Matthews, C. E. Wieman, and E. A. Cornell, Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor, Science 269, 198 (1995). [63] M. Born and E. Wolf, Principles of Optics, 7th ed. (Cambridge University Press, Cambridge, England, 1999). [64] N. Allard and J. Kielkopf, The Effect of Neutral Nonresonant Collisions on Atomic Spectral Lines, Rev. Mod. Phys. 54, 1103 (1982). [65] L. Bellando, A. Gero, E. Akkermans, and R. Kaiser, Cooperative Effects and Disorder: A Scaling Analysis of the Spectrum of the Effective Atomic Hamiltonian, Phys. Rev. A 90, 063822 (2014). [66] S. E. Skipetrov and J. H. Page, Red Light for Anderson Localization, New J. Phys. 18, 021001 (2016). [67] S. E. Skipetrov and I. M. Sokolov, Ioffe-Regel Criterion for Anderson Localization in the Model of Resonant Point Scatterers, Phys. Rev. B 98, 064207 (2018).
[68] A. V. Gorshkov, A. Andre ́, M. Fleischhauer, A. S. Sørensen, and M. D. Lukin, Universal Approach to Optimal Photon Storage in Atomic Media, Phys. Rev. Lett. 98, 123601 (2007). [69] K. Hammerer, A. S. Sørensen, and E. S. Polzik, Quantum Interface between Light and Atomic Ensembles, Rev. Mod. Phys. 82, 1041 (2010). [70] A. V. Gorshkov, J. Otterbach, M. Fleischhauer, T. Pohl, and M. D. Lukin, Photon-Photon Interactions via Rydberg Blockade, Phys. Rev. Lett. 107, 133602 (2011).
[71] F. Naccarato et al., Searching for Materials with High Refractive Index and Wide Band Gap: A First-Principles High-Throughput Study, Phys. Rev. Mater. 3, 044602 (2019). [72] A. A. Shubnic, R. G. Polozkov, I. A. Shelykh, and I. V. Iorsh, High Refractive Index and Extreme Biaxial Optical Anisotropy of Rhenium Diselenide for Applications in All-Dielectric Nanophotonics, Nanophotonics 9 (2020). [73] R. G. Newton, Optical Theorem and Beyond, Am. J. Phys. 44, 639 (1976).
[74] B. T. Draine, The Discrete-Dipole Approximation and Its Application to Interstellar Graphite Grains, Astrophys. J. 333, 848 (1988). [75] I. O. Sosa, C. Noguez, and R. G. Barrera, Optical Properties of Metal Nanoparticles with Arbitrary Shapes, J. Phys. Chem. B 107, 6269 (2003). [76] A. B. Evlyukhin, C. Reinhardt, and B. N. Chichkov, Multipole Light Scattering by Nonspherical Nanoparticles in the Discrete Dipole Approximation, Phys. Rev. B 84, 235429 (2011). [77] A. B. Evlyukhin, C. Reinhardt, E. Evlyukhin, and B. N. Chichkov, Multipole Analysis of Light Scattering by Arbitrary-Shaped Nanoparticles on a Plane Surface, J. Opt. Soc. Am. B 30, 2589 (2013). [78] R. Alaee, A. Safari, V. Sandoghdar, and R. W. Boyd, Kerker Effect, Superscattering, and Scattering Dark States in Atomic Antennas, Phys. Rev. Research 2, 043409 (2020).
MAXIMUM REFRACTIVE INDEX OF AN ATOMIC MEDIUM PHYS. REV. X 11, 011026 (2021)
011026-17
