# Cavity-QED Quantum Simulator of Dynamical Phases of a Bardeen-Cooper-Schrieffer Superconductor - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevLett.126.173601
> Collected: 2026-09-20
> Published: 2021-04-27
> Zotero parent key: RV44B6IS
> Evidence: Zotero indexed PDF text

A cavity-QED quantum simulator of dynamical phases of a BCS superconductor
Robert J. Lewis-Swan,1, 2, 3, 4 Diego Barberena,3, 4 Julia R. K. Cline,3 Dylan J. Young,3 James K. Thompson,3 and Ana Maria Rey3, 4
1Homer L. Dodge Department of Physics and Astronomy, The University of Oklahoma, Norman, Oklahoma 73019, USA 2Center for Quantum Research and Technology, The University of Oklahoma, Norman, Oklahoma 73019, USA 3JILA, NIST, Department of Physics, University of Colorado, Boulder, CO 80309, USA 4Center for Theory of Quantum Matter, University of Colorado, Boulder, CO 80309, USA (Dated: March 25, 2021)
We propose to simulate dynamical phases of a BCS superconductor using an ensemble of cold atoms trapped in an optical cavity. Effective Cooper pairs are encoded via internal states of the atoms and attractive interactions are realized via the exchange of virtual photons between atoms coupled to a common cavity mode. Control of the interaction strength combined with a tunable dispersion relation of the effective Cooper pairs allows exploration of the full dynamical phase diagram of the BCS model, as a function of system parameters and the prepared initial state. Our proposal paves the way for the study of non-equilibrium features of quantum magnetism and superconductivity by harnessing atom-light interactions in cold atomic gases.
Introduction: The development of a generic framework to understand the properties of non-equilibrium quantum states is a long-standing challenge in modern physics. Theoretical work [1–6] combined with technical advances in the control and characterization of many-body physics in cold atom experiments [7–15] has led to new developments in this direction, such as extending the concept of phase transitions to non-equilibrium situations. Specifically, dynamical phase transitions (DPTs) [1, 16–20] have been introduced to classify distinct regimes of dynamical behaviour that arise after a sudden quench of a control parameter in a closed system. DPTs are characterized by the existence of a time-averaged order parameter that demonstrates non-analytic behaviour at the boundary between dynamical phases.
A long standing example of such dynamical phases are those predicted to emerge from quenches of Bardeen–Cooper–Schrieffer (BCS) superconductors, which has been theoretically investigated in both the condensed matter[21–30] and high energy communities [31]. However, experimental progress towards observing these phases has been limited so far to transient dynamics on rapid time-scales in terahertz pump-probe experiments [32, 33]. Recent proposals to enhance pairing by coupling materials to cavities and adjustable external laser driving might facilitate probing the predicted BCS phases in solid state systems [34].
Here, motivated by developments studying dynamical phase transitions in state-of-the-art quantum simulators, we present a proposal to emulate the non-equilibrium dynamics of the BCS model of superconductivity with cavity-QED [9, 13, 35–38]. Our scheme leverages the tunability and control available in this platform to map out the dynamical phase diagram over a broad range of system parameters and initial states, demonstrating the power of cavity-QED systems as quantum simulators of superconductivity and quantum magnetism [39–42].
BCS model and dynamical phases: The BCS model of superconductivity for s-wave interacting fermions is characterized by the Hamiltonian [43],
Hˆ = −χ
∑
k,k′
cˆ†
k,↑cˆ†
−k,↓cˆk′,↑cˆ−k′,↓ +
∑
k,σ
εkcˆ†
k,σcˆk,σ. (1)
Here, cˆ†
k,σ (cˆk,σ) creates (annihilates) a fermion of momentum k and spin σ =↑, ↓. The first term describes attractive s-wave interactions χ ≥ 0 that lead to the formation of Cooper pairs. The single-particle dispersion is εk = k2/(2m) − μ with μ the chemical potential and m the particle mass. Throughout the manuscript we set ħ = 1. This “reduced” BCS model assumes that only Cooper pairs are created and destroyed with zero center-of-mass momentum and neglects pair-breaking processes, so the low-energy physics can be described using only the presence or absence of Cooper pairs at each momentum mode. The physics of the model is further simplified by introducing Anderson pseudospin-1/2 operators,
σˆ−
k = cˆk,↑cˆ−k,↓, σˆz
k = cˆ†
k,↑cˆk,↑ + cˆ†
−k,↓cˆ−k,↓ − 1. (2)
The two eigenstates of σˆz
k encode the presence/absence of a Cooper pair with momentum k, which are created (annihilated) by σˆ+
k (σˆ−
k ). Equation (1) then becomes:
Hˆ = −χ
∑
k,k′
σˆ+
k σˆ−
k′ +
∑
k
εkσˆz
k = −χSˆ+Sˆ− +
∑
k
εkσˆz
k,
(3) where Sˆ± = ∑
k σˆ±
k are collective spin operators. The ground-state |ψ〉gs of (3) within BCS theory is characterized by the expectations [26]
〈σˆ+
k 〉gs = 1
2
∆gs
√
∆2gs + ε2
k
, 〈σˆz
k〉gs = εk
√
∆2gs + ε2
k
, (4)
arXiv:2011.13007v2 [quant-ph] 23 Mar 2021


 2
FIG. 1. (a) BCS dynamical phases illustrated by the pairing amplitude |∆(t)|. Characteristic t−1/2 decay of phase II is indicated by the faded line. (b) Example BCS ground-state on the Bloch sphere. The single-particle inversion 〈σˆz
k〉 correlates with the sign of the dispersion εk [Eq. (4)]. (c) BCS physics can be simulated in a cavity by encoding a spin-1/2 into a pair of internal atomic states with transition frequency ωa, which are coupled to a single common cavity mode. The spin-1/2 atoms are divided into two ensembles (shown as blue and red) featuring mean energy splittings with opposite sign, ± 0/2.
as shown schematically on the Bloch sphere in Fig. 1(b). Here, the BCS pairing gap, ∆gs ≡ χ〈Sˆ−〉gs, is defined self-consistently. Prior studies in superconductors and fermionic superfluids [26, 27, 44] have used the BCS Hamiltonian (3) to describe the gap dynamics after a quench of the pairing gap from the ground-state value ∆gs to a final value ∆f [26, 27]. Equation (3) is expected to provide a valid treatment of the gap dynamics on timescales for which pair breaking processes can be neglected, provided the quench is done faster than the inverse of the quasiparticle gap. In the mean-field (classical) limit the dynamics falls into three distinct dynamical phases according to the behaviour of the magnitude of |∆(t)| = χ|S−(t)|. Throughout, we adopt the notation O(t) ≡ 〈Oˆ(t)〉 when making a mean-field approximation, i.e., 〈Oˆ1(t)Oˆ2(t)〉 =
〈Oˆ1(t)〉〈Oˆ2(t)〉. As t → ∞ the dynamics are: Phase I) |∆(t)| → 0, Phase II) |∆(t)| → const with transient oscillations that decay as ∝ t−1/2, or Phase III) |∆(t)| features persistent oscillations. Illustrations of |∆(t)| in each phase are shown in Fig. 1(a). We discuss below how these phases arise from a competition between the interactions and the distribution of single-particle splittings εk.
BCS physics in a cavity-QED simulator: We propose to explore the phase diagram of the BCS model by emulating the Hamiltonian (3) in a cavity. In our proposed scheme, an ensemble of atoms is distributed in a standing wave optical lattice supported by the cavity. Each atom, which we index by the label j, encodes a spin-1/2 degree of freedom in a pair of stable internal states, | ↑〉j and | ↓〉j, which map to the presence or absence of a Cooper
pair, respectively. The use of the index j compared to the momentum label k in a real BCS superconductor will be shown to be irrelevant. Spin-spin interactions ∝ Sˆ+Sˆ− are mediated by the exchange of virtual photons between atoms via a single common cavity mode (at frequency ωc) far-detuned from the atomic resonance (at frequency ωa) [9, 35, 45, 46]. These photon-mediated interactions are analogous to the phonon-mediated interactions in a BCS superconductor. Tunable (inhomogeneous) single-particle energy shifts εj σˆz
j can be realized via external fields that generate AC Stark or Zeeman shifts of the internal atomic states. An important ingredient for the observation of the dynamical phases I-III is the ability to prepare initial states correlated with the distribution of splittings εj. For example, in the BCS ground-state [Eq. (4)], the sign of the inversion 〈σˆz
k〉 of the Anderson pseudospins correlates with the sign of the single-particle dispersion εk. Motivated by this case, we consider initial states where the atoms are split into a pair of ensembles where the spin configuration of the atoms in each ensemble is correlated with the sign of the ensemble’s average splitting. Concretely, we consider 2N atoms divided into two equal ensembles and initialized as a product of coherent spinstates [47] lying on the equatorial plane of the Bloch sphere separated by a relative azimuthal opening angle ∆φ0: |ψ0〉 = |π/2, ∆φ0/2〉+ ⊗ |π/2, −∆φ0/2〉− [see Fig. 1 and Fig. 2(a)] where the subscript ± denotes each ensemble. Here, |θ, φ〉 ≡ ⊗
j
[cos(θ/2)| ↓〉j + eiφsin(θ/2)| ↑〉j
]
where the product runs over j = 1, ..., N or j = N + 1, ..., 2N atoms respectively for the ± ensembles. Lastly, following the BCS ground-state we assume a uniform distribution of splittings εj ∈ [± 0/2 − W/4, ± 0/2 + W/4] where the sign of 0 differs for each ensemble and is matched to the sign of ±∆φ0/2. It is the mean ± 0/2 and characteristic width W/2 rather than the precise distribution of εj (e.g., uniform or normal) that is important to characterize the physics discussed below. Preparation of the two ensembles and correlation with ± 0 can be achieved by spatially selective energy shifts of atoms in the cavity [45] [Fig. 1(c)] or by addressing different internal levels [35, 48] (see later discussion) [49]. Accessible dynamical phase diagram: In Fig. 2 we explore the accessible dynamical phases. Panel (b) shows the dynamical phase diagram for mean splitting 0/(χN ) = 0.1. The phase diagram is computed via a Lax analysis [24, 26, 27] that is a method for integrable models, such as Eq. (3), to determine the frequency spectrum that rules the dynamics of the order parameter. The spectrum is extracted from the roots of L2(u), the squared norm of the Lax vector L(u), a polynomial defined in terms of a complex variable u that encodes the conserved quantities of the model. A spectrum with all real roots defines phase I, with one pair of complex roots phase II and with two pairs of complex roots phase III. The asymptotic behaviour of |∆(t)| follows from the nature of the roots


 3
FIG. 2. (a) Typical initial state for opening angle ∆φ0. The orientation of each ensemble (red and blue collective Bloch vectors) is correlated with the sign of ± 0. (b) Mean-field BCS dynamical phase-diagram as a function of ∆φ0 andcharacteristic width W of the single-particle noise distribution, with fixed 0/(χN ) = 0.1. The phase diagram is evaluated numerically (see Ref. [50]) and some small structure (e.g., regions of phase II within phase III) are likely artefacts of the methods precision. (c) Time-traces of the pairing amplitude |∆(t)| for each phase [parameters indicated by marker in (b)].
of L2(u), which we compute numerically [50]. Physically, the dynamical phases depend on the competition between single-particle dephasing generated by W and 0 and the spin-locking effect generated by the interactions with strength set by χN [51–58]. The spinlocking is induced by the existence of a many-body gap that suppresses local spin flips and favors spin alignment [35, 36, 59]. Such behaviour also resembles synchronization observed in arrays of coupled oscillators with dissipation [60, 61]. Other consequences associated with the many-body gap include the stabilization of localization effects in fully connected models under specific initial conditions [62, 63]. For small inhomogeneity, W 0, χN we predict phase III dynamics independent of the opening angle ∆φ0. Within each ensemble a gap opens between the manifold of collective states (this includes the initial fully polarized states) and those that are spatially inhomogeneous, preventing dephasing of the individual spins of each ensemble. In addition, the interplay between the homogeneous single-particle energy splitting ± 0 (that generates precession of the ensembles in opposing directions about the z-axis of the Bloch sphere), and the collective interaction (that also drives a rotation of each ensemble along a common self-generated axis set by the total transverse magnetization [35, 48]), leads to persistent nonlinear oscillations in the effective pairing amplitude |∆(t)| = |S+(t)| [see also Fig. 3(a)]. Phase II emerges for 2 0 < W . χN and opening angles away from ∆φ ≈ ±π [50]. The transition from phase III to II is driven by the ensembles no longer having a well-defined relative energy splitting correlated with their initial orientation. Thus, in contrast to phase III, spin
FIG. 3. (a) Typical trajectories of the collective Bloch vector of each ensemble (red and blue) for W χN, 0 as 0 is tuned between phases IIIa and IIIb. (b) Phase diagram characterized by amplitude A ≡ max(|∆(t)|) − min(|∆(t)|) of oscillations in |∆(t)|. The critical boundary c
0 between phases IIIa and IIIb is indicated by the red line. (c) Maximum of the
total inversion difference Jz =
( ∑
j∈+ σz
j −∑
j∈− σz
j
)
/2 and
frequency, ωosc, of oscillations of |∆(t)| as a function of 0.
locking of the entire ensemble of 2N atoms determines the dynamics. This means that while the pairing amplitude |∆(t)| remains large, oscillations are transient and suppressed rather than stabilized by the interactions. Finally, phase I emerges for W & χN independent of 0. Single-particle physics dominates for all initial conditions and the pairing amplitude vanishes due to rapid dephasing of the individual spins, |∆(t)| → 0. Beyond these three known regimes we also predict the emergence of two previously unidentified sub-phases within phase III for W χN, 0, which we label as IIIa and IIIb. These sub-phases are delineated by a critical splitting c0 = χN
2 [1 + cos(∆φ0)] [50]. Phase IIIa),
0 < c0, is dominated by interactions and characterized by a strictly non-zero pairing amplitude, |∆(t)| > 0 that exhibits nonlinear oscillations with an approximate frequency ωosc ∝ χN . Phase IIIb) is characterized by the pairing amplitude periodically vanishing, |∆(t)| = 0, and the physics is dominated by the single-particle splitting 0 such that the frequency of oscillations scales as ωosc ∝ 0. In Fig. 3(a) we illustrate typical trajectories of the collective Bloch vector of each ensemble in sub-phases IIIa and IIIb for an initial state with ∆φ0 = 0, which are representative of the dominant physics for |∆φ0| . π. For small 0 c0 and ∆φ0 π the Bloch vectors remain trapped close to their initial polarization due to the strong interactions, leading to |∆(t)| > 0. As 0 increases nearer to the transition, c0, the interactions still dominate and their interplay with the single particle term leads to a deflection of the trajectories of the Bloch vectors close to the north and south poles. Above c0 the trajectories abruptly snap to large orbits near the equa


 4
tor and quickly approach the precession expected for two independent ensembles (e.g., dominated by the σˆz term of the Hamiltonian). Even though phase IIIb is technically absent for ∆φ0 = ±π by our definition (as |∆(0)| = 0), we still observe rich non-trivial oscillations for 0 χN
with frequency ωosc ∝ √
0χN [50].
Quantitatively, the IIIa and IIIb sub-phases are delineated by abrupt changes in different observables, including the magnitude A ≡ max(|∆(t)|) − min(|∆(t)|) , the frequency ωosc of oscillations of |∆(t)| [Figs. 3(b) and (d)] and the maximum excursion of the collective spins away from the equator of the Bloch sphere, measured by
the differential inversion Jz =
( ∑
j∈+ σz
j −∑
j∈− σz
j
)
/2
[Fig. 3(c)].
Experimental realization and robustness of proposal: In a cavity-QED experiment, the dynamical phases can be characterized by detection of intracavity light leaking out through the cavity mirrors [35]. By operating in the limit where the cavity mode is far off-resonance from the atomic transition, the virtual photons that mediate the interactions are adiabatically eliminated and slaved to the spins, such that atomic information is imprinted onto the phase and amplitude of the cavity field via the approximate relation a(t) ∝ S−(t) ∝ ∆(t) [35, 50]. The light intensity then serves as a proxy for the BCS pairing amplitude, |a(t)|2 ∝ |∆(t)|2, while the frequency spectrum of a(t) can also be a useful diagnostic to distinguish the dynamical phases. Moreover, by continuously performing heterodyne detection of the small amount of light leaking through the cavity mirrors we are able to in principle construct time-traces of the pairing amplitude within a single experimental trial.
To demonstrate our proposal is robust to relevant decoherence and technical factors, we model an experiment where the spin-1/2 is encoded using the narrow linewidth 1S0-3P1 optical transition of 87,88Sr. Here, sub-ensembles can be prepared via spatially dependent light-shifts from the side of the cavity, or in 87Sr by applying spatially dependent magnetic fields and addressing the ±9/2 nuclear spin levels of the transition. We use parameters from Ref. [9] and include single-particle decoherence due to the natural linewidth of the transition γ/(2π) = 7.5 kHz and spatially inhomogeneous atom-light coupling arising due to the incommensurate wavelengths of the standing wave optical lattice confining the atoms and the relevant cavity mode [9, 35, 50]. The latter leads to a spatial modulation of the spin-spin interactions χ → χi,j. Our predictions should also be qualitatively relevant for other cavity-based systems that can realize an effective χSˆ+Sˆ− interaction, e.g., Raman transitions [45, 46].
In Fig. 4(a) we model the transition between phases I and III as a function of the inhomogeneity strength W at fixed 0/(χN ) = 0.1 and initial state ∆φ0 = π. The phases are distinguished in the frequency spectrum of the cavity field F[a](ω), with phase III signaled by a pair of
FIG. 4. Dynamics of intracavity field a(t). (a) Frequency spectrum of intracavity field, F[a](ω), as a function of W/(χN ), and typical timetraces of |a|2 in phases (i) III and (ii) I. Initial state is ∆φ0 = π/2. (b) Same, but as a function of opening angle ∆φ0 and time traces are in phases (i) II and (ii) III. Simulations are for fixed W/(χN ) = 0.1. Both (a) and (b) use fixed 0/(χN ) = 0.1 and color scales are normalized. (c) Signatures of phase IIIa and phase IIIb in differential inversion Jz and oscillation frequency ωosc of |a|2 for W = 0 for different ∆φ0. Critical c
0 for each ∆φ0 is indicated by a vertical line. The absence of plotted results for ωosc below the approximate transition c
0 for each ∆φ0 indicates the lack of appreciable oscillations in the simulations. All relevant parameters (e.g., g, γ and κ) are taken from Refs. [9, 35] and results are rescaled for N = 106 (see also Ref. [50]).
robust peaks in the spectrum that disappear in phase I. The peaks are consistent with the entwined but distinguishable precession of the two ensembles that leads to beating of the intensity |a(t)|2 as shown in the accompanying time-trace. The oscillations in the intracavity intensity |a(t)|2 are robust to the inhomogeneous interactions and the exponential decay induced by γ. The transition between the phases occurs at W/(χN ) ≈ π/2, which is consistent with the model Eq. (3) when the inhomogeneous atom-light coupling is taken into account by a simple rescaling to the corresponding mean value χ → χi,j = χ/2 [50]. Similarly, the phase II-III transition can be observed by varying the initial opening angle ∆φ0 at fixed W/(χN ) = 0/(χN ) = 0.1. The spectrum of the intracavity field shows the signature dual peaks of phase III for π/2 . ∆φ0 ≤ π, while phase II is signaled by a single peak for 0 ≤ ∆φ0 . π/2. The latter indicates dynamics of a single collective ensemble, with finite but non-oscillatory


 5
pairing amplitude.
Lastly, signatures of the phase IIIa-IIIb transition in the differential inversion and oscillation frequency of |a(t)|2 are shown in Fig. 4(c). Decoherence blunts the expected cusp in the inversion, although the peak value lines up closely with the expected transition upon accounting for inhomogeneous interactions. The oscillation frequency clearly distinguishes the trivial/non-trivial regimes for ∆φ0 = π. On the other hand, we find that for ∆φ0 = 0, π/2 the relatively small oscillations in |a(t)|2 predicted for phase IIIa are destroyed by decoherence,and instead the transition between IIIa and IIIb is marked by an abrupt vanishing of any discernible peak in the spectrum (indicated by the absence of data).
Conclusions: We have reported a proposal to observe the dynamical phases of a BCS superconductor in a cavityQED quantum simulator. Realizing these phases via a spin degree of freedom instead of actual Cooper pairs overcomes the need to reach the ultra cold temperatures at which pairing occurs. The versatility of this platform allows us to probe the dependence of the dynamical phases on the initial state and system parameters in a controllable, isolated setting. Our predictions pave the way for future studies of more complex non-equilibrium phenomena in models of quantum magnetism and superconductivity so far not seen in real materials or high energy systems.
Acknowledgements: We acknowledge helpful discussions with Anjun Chu, Nathan Schine, Victor Gurarie and Emil Yuzbashyan. This work is supported by the AFOSR grant FA9550-18-1-0319, by the DARPA and ARO grant W911NF-16-1-0576, the ARO single investigator award W911NF-19-1-0210, the NSF PHY1820885, NSF JILAPFC PHY-1734006 and NSF QLCI-2016244 grants, and by NIST.
[1] B. Sciolla and G. Biroli, Dynamical transitions and quantum quenches in mean-field models, Journal of Statistical Mechanics: Theory and Experiment 2011, P11003 (2011). [2] M. Heyl, A. Polkovnikov, and S. Kehrein, Dynamical quantum phase transitions in the transverse-field ising model, Phys. Rev. Lett. 110, 135704 (2013). [3] M. Heyl, Dynamical quantum phase transitions: a review, Reports on Progress in Physics 81, 054001 (2018). [4] B. Zˇunkoviˇc, M. Heyl, M. Knap, and A. Silva, Dynamical quantum phase transitions in spin chains with long-range interactions: Merging different concepts of nonequilibrium criticality, Phys. Rev. Lett. 120, 130601 (2018). [5] S. B. Ja ̈ger, J. Cooper, M. J. Holland, and G. Morigi, Dynamical phase transitions to optomechanical superradiance, Phys. Rev. Lett. 123, 053601 (2019). [6] C.-M. Halati, A. Sheikhan, H. Ritsch, and C. Kollath, Numerically exact treatment of many-body selforganization in a cavity, Phys. Rev. Lett. 125, 093604
(2020). [7] P. Jurcevic, H. Shen, P. Hauke, C. Maier, T. Brydges, C. Hempel, B. P. Lanyon, M. Heyl, R. Blatt, and C. F. Roos, Direct observation of dynamical quantum phase transitions in an interacting many-body system, Phys. Rev. Lett. 119, 080501 (2017). [8] J. Zhang, G. Pagano, P. W. Hess, A. Kyprianidis, P. Becker, H. Kaplan, A. V. Gorshkov, Z.-X. Gong, and C. Monroe, Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator, Nature 551, 601 (2017). [9] J. A. Muniz, D. Barberena, R. J. Lewis-Swan, D. J. Young, J. R. K. Cline, A. M. Rey, and J. K. Thompson, Exploring dynamical phase transitions with cold atoms in an optical cavity, Nature 580, 602 (2020). [10] S. Smale, P. He, B. A. Olsen, K. G. Jackson, H. Sharum, S. Trotzky, J. Marino, A. M. Rey, and J. H. Thywissen, Observation of a transition between dynamical phases in a quantum degenerate fermi gas, Science Advances 5, 10.1126/sciadv.aax1568 (2019). [11] T. Tian, H.-X. Yang, L.-Y. Qiu, H.-Y. Liang, Y.-B. Yang, Y. Xu, and L.-M. Duan, Observation of dynamical quantum phase transitions with correspondence in an excited state phase diagram, Phys. Rev. Lett. 124, 043001 (2020). [12] A. Chu, J. Will, J. Arlt, C. Klempt, and A. M. Rey, Simulation of xxz spin models using sideband transitions in trapped bosonic gases (2020), arXiv:2004.01282 [condmat.quant-gas]. [13] K. Baumann, C. Guerlin, F. Brennecke, and T. Esslinger, Dicke quantum phase transition with a superfluid gas in an optical cavity, Nature 464, 1301 (2010). [14] J. Klinder, H. Keßler, M. Wolke, L. Mathey, and A. Hemmerich, Dynamical phase transition in the open dicke model, PNAS 112, 3290 (2015). [15] R. M. Kroeze, Y. Guo, V. D. Vaidya, J. Keeling, and B. L. Lev, Spinor self-ordering of a quantum gas in a cavity, Phys. Rev. Lett. 121, 163601 (2018). [16] M. Eckstein, M. Kollar, and P. Werner, Thermalization after an interaction quench in the Hubbard model, Phys. Rev. Lett. 103, 056403 (2009). [17] M. Schiro ́ and M. Fabrizio, Time-dependent mean field theory for quench dynamics in correlated electron systems, Phys. Rev. Lett. 105, 076401 (2010). [18] A. Gambassi and P. Calabrese, Quantum quenches as classical critical films, EPL 95, 66007 (2011). [19] P. Smacchia, M. Knap, E. Demler, and A. Silva, Exploring dynamical phase transitions and prethermalization with quantum noise of excitations, Phys. Rev. B 91, 205136 (2015). [20] P. Kirton, M. M. Roses, J. Keeling, and E. G. Dalla Torre, Introduction to the dicke model: From equilibrium to nonequilibrium, and vice versa, Advanced Quantum Technologies 2, 1800043 (2019). [21] A. F. Volkov and S. M. Kogan, Collisionless relaxation of the energy gap in superconductors, Sov. Phys. JETP 38, 1018 (1974). [22] R. A. Barankov, L. S. Levitov, and B. Z. Spivak, Collective rabi oscillations and solitons in a time-dependent bcs pairing problem, Phys. Rev. Lett. 93, 160401 (2004). [23] E. A. Yuzbashyan, V. B. Kuznetsov, and B. L. Altshuler, Integrable dynamics of coupled fermi-bose condensates, Phys. Rev. B 72, 144524 (2005). [24] E. A. Yuzbashyan, B. L. Altshuler, V. B. Kuznetsov,


 6
and V. Z. Enolskii, Nonequilibrium cooper pairing in the nonadiabatic regime, Phys. Rev. B 72, 220503 (2005). [25] E. A. Yuzbashyan, O. Tsyplyatyev, and B. L. Altshuler, Relaxation and persistent oscillations of the order parameter in fermionic condensates, Phys. Rev. Lett. 96, 097005 (2006). [26] R. A. Barankov and L. S. Levitov, Synchronization in the bcs pairing dynamics as a critical phenomenon, Phys. Rev. Lett. 96, 230403 (2006). [27] E. A. Yuzbashyan, M. Dzero, V. Gurarie, and M. S. Foster, Quantum quench phase diagrams of an s-wave bcsbec condensate, Phys. Rev. A 91, 033628 (2015). [28] H. P. O. Collado, J. Lorenzana, G. Usaj, and C. A. Balseiro, Population inversion and dynamical phase transitions in a driven superconductor, Phys. Rev. B 98, 214519 (2018). [29] H. P. Ojeda Collado, G. Usaj, J. Lorenzana, and C. A. Balseiro, Fate of dynamical phases of a bcs superconductor beyond the dissipationless regime, Phys. Rev. B 99, 174509 (2019). [30] H. P. Ojeda Collado, G. Usaj, J. Lorenzana, and C. A. Balseiro, Nonlinear dynamics of driven superconductors with dissipation, Phys. Rev. B 101, 054502 (2020). [31] Y. Pehlivan, A. B. Balantekin, T. Kajino, and T. Yoshida, Invariants of collective neutrino oscillations, Phys. Rev. D 84, 065008 (2011). [32] R. Matsunaga, Y. I. Hamada, K. Makise, Y. Uzawa, H. Terai, Z. Wang, and R. Shimano, Higgs amplitude mode in the bcs superconductors nb1−xtixN induced by terahertz pulse excitation, Phys. Rev. Lett. 111, 057002 (2013). [33] R. Matsunaga, N. Tsuji, H. Fujita, A. Sugioka, K. Makise, Y. Uzawa, H. Terai, Z. Wang, H. Aoki, and R. Shimano, Light-induced collective pseudospin precession resonating with higgs mode in a superconductor, Science 345, 1145 (2014). [34] H. Gao, F. Schlawin, M. Buzzi, A. Cavalleri, and D. Jaksch, Photoinduced electron pairing in a driven cavity, Phys. Rev. Lett. 125, 053602 (2020). [35] M. A. Norcia, R. J. Lewis-Swan, J. R. K. Cline, B. Zhu, A. M. Rey, and J. K. Thompson, Cavity-mediated collective spin-exchange interactions in a strontium superradiant laser, Science 361, 259 (2018). [36] E. J. Davis, A. Periwal, E. S. Cooper, G. Bentsen, S. J. Evered, K. Van Kirk, and M. H. Schleier-Smith, Protecting spin coherence in a tunable heisenberg model, Phys. Rev. Lett. 125, 060402 (2020). [37] V. D. Vaidya, Y. Guo, R. M. Kroeze, K. E. Ballantine, A. J. Kolla ́r, J. Keeling, and B. L. Lev, Tunable-range, photon-mediated atomic interactions in multimode cavity qed, Phys. Rev. X 8, 011002 (2018). [38] H. Ritsch, P. Domokos, F. Brennecke, and T. Esslinger, Cold atoms in cavity-generated dynamical optical potentials, Rev. Mod. Phys. 85, 553 (2013). [39] P. Strack and S. Sachdev, Dicke quantum spin glass of atoms and photons, Phys. Rev. Lett. 107, 277202 (2011). [40] S. Gopalakrishnan, B. L. Lev, and P. M. Goldbart, Frustration and glassiness in spin models with cavitymediated interactions, Phys. Rev. Lett. 107, 277201 (2011). [41] S. P. Kelly, A. M. Rey, and J. Marino, The effect of active photons on dynamical frustration in cavity qed (2020), arXiv:2012.04660 [cond-mat.dis-nn]. [42] E. Colella, S. Ostermann, W. Niedenzu, F. Mivehvar,
and H. Ritsch, Antiferromagnetic self-ordering of a fermi gas in a ring cavity, New Journal of Physics 21, 043019 (2019). [43] V. Gurarie and L. Radzihovsky, Resonantly paired fermionic superfluids, Annals of Physics 322, 2 (2007), january Special Issue 2007. [44] M. S. Foster, M. Dzero, V. Gurarie, and E. A. Yuzbashyan, Quantum quench in a p + ip superfluid: Winding numbers and topological states far from equilibrium, Phys. Rev. B 88, 104511 (2013). [45] E. J. Davis, G. Bentsen, L. Homeier, T. Li, and M. H. Schleier-Smith, Photon-mediated spin-exchange dynamics of spin-1 atoms, Phys. Rev. Lett. 122, 010405 (2019). [46] A. Shankar, L. Salvi, M. L. Chiofalo, N. Poli, and M. J. Holland, Squeezed state metrology with bragg interferometers operating in a cavity, Quantum Science and Technology 4, 045010 (2019). [47] J. M. Radcliffe, Some properties of coherent spin states, Journal of Physics A: General Physics 4, 313 (1971). [48] R. J. Lewis-Swan, M. A. Norcia, J. R. K. Cline, J. K. Thompson, and A. M. Rey, Robust spin squeezing via photon-mediated interactions on an optical clock transition, Phys. Rev. Lett. 121, 070403 (2018). [49] It should also be possible to prepare initial states that are split by their projection along the z direction, rather than the projection along x (set by ∆φ0) that would follow even more closely the BCS ground state. However, varying the relative azimuthal opening angle gives similar physics and is more robust to typical experimental constraints [50]. [50] See Supplemental Material at [URL will be inserted by publisher], which contains Refs. [9, 24, 26, 27, 35, 47, 64, 65]. [51] C. Lhuillier and F. Laloe, Transport properties in a spin polarized gas, i, J. Phys. France 43, 197 (1982). [52] W. J. Gully and W. J. Mullin, Observation of spin rotation effects in polarized 3He-4He mixtures, Phys. Rev. Lett. 52, 1810 (1984). [53] B. R. Johnson, J. S. Denker, N. Bigelow, L. P. L ́evy, J. H. Freed, and D. M. Lee, Observation of nuclear spin waves in spin-polarized atomic hydrogen gas, Phys. Rev. Lett. 53, 302 (1984). [54] E. P. Bashkin, Spin waves and quantum collective phenomena in boltzmann gases, Soviet Physics Uspekhi 29, 238 (1986). [55] J. M. McGuirk, H. J. Lewandowski, D. M. Harber, T. Nikuni, J. E. Williams, and E. A. Cornell, Spatial resolution of spin waves in an ultracold gas, Phys. Rev. Lett. 89, 090402 (2002). [56] X. Du, L. Luo, B. Clancy, and J. E. Thomas, Observation of anomalous spin segregation in a trapped fermi gas, Phys. Rev. Lett. 101, 150401 (2008). [57] C. Deutsch, F. Ramirez-Martinez, C. Lacrouˆte, F. Reinhard, T. Schneider, J. N. Fuchs, F. Pi ́echon, F. Laloe ̈, J. Reichel, and P. Rosenbusch, Spin self-rephasing and very long coherence times in a trapped atomic ensemble, Phys. Rev. Lett. 105, 020401 (2010). [58] G. Kleine B ̈uning, J. Will, W. Ertmer, E. Rasel, J. Arlt, C. Klempt, F. Ramirez-Martinez, F. Pi ́echon, and P. Rosenbusch, Extended coherence time on the clock transition of optically trapped rubidium, Phys. Rev. Lett. 106, 240801 (2011). [59] A. M. Rey, L. Jiang, M. Fleischhauer, E. Demler, and M. D. Lukin, Many-body protected entanglement genera


 1
tion in interacting spin systems, Phys. Rev. A 77, 052305 (2008). [60] B. Zhu, J. Schachenmayer, M. Xu, F. Herrera, J. G. Restrepo, M. J. Holland, and A. M. Rey, Synchronization of interacting quantum dipoles, New Journal of Physics 17, 083063 (2015).
[61] K. Y, Chemical Oscillations, Waves, and Turbulence (New York: Dover, 2003). [62] L. F. Santos, F. Borgonovi, and G. L. Celardo, Cooperative shielding in many-body systems with long-range
interaction, Phys. Rev. Lett. 116, 250402 (2016). [63] G. L. Celardo, R. Kaiser, and F. Borgonovi, Shielding and localization in the presence of long-range hopping, Phys. Rev. B 94, 144206 (2016). [64] M. Foster and V. Gurarie, private communication. [65] G. R. Dennis, J. J. Hope, and M. T. Johnsson, XMDS2: Fast, scalable simulation of coupled stochastic partial differential equations, Computer Physics Communications 184, 201 (2013).
Supplemental Material: A cavity-QED quantum simulator of dynamical phases of a BCS superconductor
LAX ANALYSIS
We gain analytic insight into the dynamical phase diagram of the BCS model by employing a Lax analysis. This is a a tool that, building on the integrability of the BCS model, allows for the characterization and even solution of the asymptotic (t → ∞) dynamics. In the following sections we give a brief summary of results in the classical limit, pertinent in particular for Figs. 2 and 3 of the main text. A more detailed discussion of the Lax analysis can be found in, e.g., Ref. [24, 27] and references therein.
Lax vector and classification of dynamical phase diagram
Throughout our analysis we work with the pseudospin BCS Hamiltonian [Eq. (3) of the main text],
Hˆ = χSˆ+Sˆ− +
∑
j
εj σˆz
j . (S1)
We will focus on the mean-field (classical) dynamics of the model generated by the approximation 〈Oˆ1Oˆ2〉 =
〈Oˆ1〉〈Oˆ2〉 and adopt the notation O ≡ 〈Oˆ〉 for simplicity. Given the form of the Hamiltonian (S1) we also introduce the associated (mean-field) Lax vector [24, 26, 27],
~L(u) = 1
2
∑
j
~σj (0) u − εj
− zˆ
χ . (S2)
The Lax vector is explicitly defined with respect to
the initial state characterized by the expectation values ~σj(0) = (〈σˆx
j (0)〉, 〈σˆy
j (0)〉, 〈σˆz
j (0)〉).
The mean-field dynamical phase diagram of Hˆ given the initial conditions ~σj(0) can be constructed by an analysis of the properties of ~L(u) [24, 26, 27]. Specifically, the dynamical phases are defined in terms of the properties of the complex roots {u1, u2, ..., un} of the equation ~L(u) · ~L(u) = 0: Phase I corresponds to zero complex roots, phase II is defined by a single pair of complex roots, and phase III is accompanied by two pairs of complex roots.
To be concrete in our analysis we must specify the initial states which are fed into the definition of the Lax vector. In the main text we consider splitting the atoms inte a pair of ensembles, each of N atoms, initialized as a product of coherent spin-states [47] lying on the equatorial plane of the Bloch sphere separated by a relative azimuthal opening angle ∆φ0: |ψ0〉 = |π/2, ∆φ0/2〉+ ⊗ |π/2, −∆φ0/2〉− (see Fig. 1 and Fig. 2(a) of the main text) where the subscript ± denotes each ensemble. Here, we have used |θ, φ〉 ≡
⊗
j
[cos(θ/2)| ↓〉j + eiφsin(θ/2)| ↑〉j
] where the product over j runs over j = 1, ..., N or j = N + 1, ..., 2N atoms respectively for the ± ensembles. For |ψ0〉 we then have ~σj(0) = (cos(∆φ0/2), ±sin(∆φ0/2), 0) where the ± is correlated with the ensemble. Moreover, we assume the single-particle energies are sampled uniformly from εj ∈ [± 0 − W/2, ± n + W/2]/2 for each ensemble. Substituting the state and single-particle dispersion into Eq. (S2) and taking the continuum limit as N → ∞ we compute the Lax vector ~L(u) = Lx(u)xˆ+Ly(u)yˆ−(1/χ)zˆ,
χLx(u) = 2χN
W cos
( ∆φ0 2
)[
ArcTanh
( 4u
W −2 0
)
+ ArcTanh
( 4u
W +2 0
)]
,
χLy(u) = χN
W sin
( ∆φ0 2
)
log
[ (4u)2 − (W − 2 0)2 (4u)2 − (W + 2 0)2
]
.
(S3)


 2
Analytically solving for the roots of ~L(u) · ~L(u) = 0 is in general not possible for arbitrary choices of system parameters W, 0, χN and initial state ∆φ0. As a consequence we typically solve for the roots using a numerical algorithm, which will be detailed momentarily. However, there are three limiting cases of the parameters for which relatively simple analytic forms of the roots exist and significant insight into the phase diagram can be garnered: (i) ∆φ0 = π, (ii) W χN, 0, and (iii) 0 W, χN . For case (i), ∆φ0 = ±π, we are able to analytically solve the roots and characterize the phase diagram for any values of W/(χN ) and 0/(χN ). A straightforward solution of ~L(u) · ~L(u) = 0 yields two pairs of complex roots,
u1± = ± 1
4
√
(W − 2 0)2 − e−i W
χN (W + 2 0)2
1 − e−i W
χN
,
u2± = ± 1
4
√
(W − 2 0)2 − ei W
χN (W + 2 0)2
1 − ei W
χN
, (S4)
which exist only for W/(χN ) < π. If W/(χN ) ≥ π then no complex roots exist. This allows us to diagnose the dynamical phases: For W/(χN ) < π the long-time dynamics are phase III, while for W/(χN ) ≥ π the dynamics are phase I. Phase II does not exist for any choice of W/(χN ) or 0/(χN ).
Case (ii) describes a scenario where the inhomogeneity is small compared to both the interactions and the uniform energy splitting, W χN, 0, and admits an approximate analytic solution for any ∆φ0. To compute the roots we first expand the squared Lax vector to lowestorder in W ,
~L(u) · ~L(u) = 1 + 4χ2N 2
(4u2 − 20)2
[
4u2cos2
( ∆φ0 2
)
+2
0sin2
( ∆φ0 2
)]
+ O(W 2), (S5)
and then solve ~L(u) · ~L(u) = 0 to find
u1± = 1
2
√
20 − χ2N 2[1 + cos(∆φ0)] ± χ√N2
√
χ2N 2[3 + 4cos(∆φ0) + cos(2∆φ0)] − 8 20,
u2± = − 1
2
√
20 − χ2N 2[1 + cos(∆φ0)] ± χ√N2
√
χ2N 2[3 + 4cos(∆φ0) + cos(2∆φ0)] − 8 20.
(S6)
The existence of these two pairs of complex roots is insensitive to the choice of ∆φ0 and always true for W χN, 0. Thus, we predict that for small inhomogeneity the long-time dynamics is always phase III. Lastly, case (iii) considers the case where only the inhomogeneous splitting and interactions dominate the physics, 0 W, χN . Computing the squared Lax vector to lowest-order in 0,
~L(u) · ~L(u) = 1 + 16 χ2N 2
W 2 ArcTanh2
( 4u W
)
cos2
( ∆φ0 2
)
,
(S7) yields a single pair of complex roots
u± = ± iW
4 tan
[W
4χN sec
( ∆φ0 2
)]
, (S8)
only for W/(χN ) < 2πcos(∆φ0/2). If W/(χN ) ≥ 2πcos(∆φ0/2) no complex roots exist. This allows us to diagnose: For W/(χN ) < 2πcos(∆φ0/2) the dynamics is phase II, while for W/(χN ) ≥ 2πcos(∆φ0/2) the dynamics is phase I. We stress that these phases and the transition at W/(χN ) = 2πcos(∆φ0/2) only exist in the limit 0 W, χN . In general, we resort to a numerical search for roots of ~L(u) · ~L(u) = 0. This is the procedure used to generate Fig. 2a of the main text. We use the inbuilt function
fsolve of MATLAB 2020a to search for complex-valued roots of the squared Lax vector as a function of system parameters and initial state. An exhaustive search is performed by running many iterations of the root finding algorithm for each choice of W , 0, χN and ∆φ0. To make this computation efficient we perform our search at fixed ∆φ0, 0, χN and begin at small inhomogeneity W χN, 0 for which we can use the results of Eq. (S6) as the initial guess for the algorithm. The roots are expected to change relatively smoothly as a function of W (until they vanish) and so we use the roots found for the current value of W as the subsequent starting point for the next value of W . To validate our numerical results, we compare the roots found by the numerical search algorithm to the analytic results for cases (i)-(iii) discussed above in Fig. S2. For case (i), e.g., restricting to ∆φ = π, we observe exact quantitative agreement in terms of both the predicted roots and the presence of dynamical phases I and III (Fig. S2a). More generically, our numerical results for arbitrary ∆φ (Fig. S2b) are consistent with the expected result of phase III for W 0, χN [case ii)] and the boundary between phases II and I at W/(χN ) = 2πcos(∆φ0/2) [case iii)]. The breakdown of the latter prediction near ∆φ ≈ ±π in the numerical results is also consistent, as our assumption that 0 W would be in contradiction


 3
FIG. S1. (a) Complex roots of the squared Lax vector, ~L(u) · ~L(u) = 0, for ∆φ0 = π and 0/(χN ) = 0.1. We compare the results of the numerical search algorithm (blue markers) and the predictions of Eq. (S4) (red lines). No complex roots exist for W/(χN ) ≥ π. (b) Numerically evaluated dynamical phase diagram as a function of ∆φ0 and W/(χN ) at fixed 0/(χN ) = 0.1. We compare the numerical results to analytic predictions for the phase II/I boundary (red dashed line). The phase III/II transition is also indicated at W = 2 0 (dashed black line). (c) Generic phase III/II transition for arbitrary splittings and fixed ∆φ0 = 0. We indicate W = 2 0 (dashed blue line) to guide the eye.
with the predicted phase boundary.
In Fig. S2b (also Fig. 2b of the main text) we identify that a transition between phases III and II occurs when the inhomogeneous and uniform splittings become comparable, W = 2 0 . χN , and ∆φ 6= ±π. To support the generality of this observation we compute the phase diagram as a function of both W/(χN ) and 0/(χN ) for fixed ∆φ0 = 0 and present the results in Fig. S2c. Our data illustrates that there is always a consistent transi
tion between phases II and III at W = 2 0.
Dynamical phase diagram of alternative initial states
Throughout the main text we focused on the accessible dynamical phase diagram of the BCS model in the context for specific set of initial conditions parameterized by the state |ψ0〉 = |π/2, ∆φ0/2〉+ ⊗ |π/2, −∆φ0/2〉− with ∆φ0 ∈ [−π, π]. Here, |θ, φ〉± ≡
⊗
j∈±
[cos(θ/2)| ↓〉j + eiφsin(θ/2)| ↑〉j
] is a spin coherent state. This choice of state was motivated by both the fact that it shares qualitative features with the BCS ground-state and that it can be prepared relatively accurate in the experiment when taking into account all technical considerations, including inhomogeneity of the atom-light coupling (see Sec. and later discussion). The former connection is of note because prior work in the literature studying the BCS dynamical phase diagram has focused on quenches from the BCS ground-state. As highlighted in the main text, it is convenient to define the BCS ground-state in the pseudospin representation via the single-particle spin expectation values,
〈σˆ+
j 〉gs = 1
2
∆gs
√
∆2gs + ε2
j
, 〈σˆz
j 〉gs = εj
√
∆2gs + ε2
j
, (S9)
where we have adopted the subscript j to mirror the conventions of the cavity-QED case for simplicity. The crucial feature of this ground-state in terms of the dynamical phase diagram is that the sign of the initial inversion 〈σˆz
j 〉gs is correlated with the sign of the single-particle energy splitting εj. It is this feature that we seek to mimic with our initial state, by correlating the sign of the azimuthal angle ±∆φ0/2 of each spin ensemble with the sign of the energy splitting 0. Based on our results and comparison with the literature, this type of correlation appears to be a necessary requirement for the observation of phase III. For completeness, and mindful of the rapidly advancing technical capabilities in state-of-the-art cavity-QED experiments, we also summarize in this SM the dynamical phase diagram which might be accessed with an initial state that more closely follows the BCS ground-state: |ψ′0〉 = | π
2 + ∆θ0
2 , 0〉+ ⊗ | π
2 − ∆θ0
2 , 0〉−. Here, the relative opening angle ∆θ0 between the ensembles is with respect to the elevation, which means that the signs of 〈σˆz
j〉 will be correlated with the sign of the energy splitting 0 in much closer correspondence to the BCS ground-state Eq. (S9), as can be seen from the initial expectation values ~σj(0) = (cos(∆θ0/2), 0, ±sin(∆θ0/2)). In Fig. S2 we present the numerically evaluated dynamical phase diagram for this state and compare to the equivalent phase diagram for |ψ0〉. To be consistent with Fig. 2b of the main text we fix 0/(χN ) = 0.1 and probe the dependence on W/(χN ) and opening angle ∆θ0. We limit our


 4
scan over the latter to 0 ≤ ∆θ0 / π−π/8 because our numerical algorithm performs poorly when the initial state becomes too closely aligned with the poles. We find that the dynamical phase diagram of the BCS-like state |ψ′0〉 is very similar to the results in the main text, both qualitatively in terms of the presence of all three dynamical phases but also quantitatively in terms of the transition
points as a function of W/(χN ) and ∆θ0.
We can make the last connection quantitatively rigorous by solving for the roots of the squared Lax vector in the same limiting cases ii) and iii) from our prior analysis. First, for W 0, χN [case ii)] we again find two pairs of complex roots (excluding when ∆θ0 = ±π).
u1± = − 1
4
√
4 20 − 2χ2N 2 − 2χN
[
χN cos(∆θ0) − 4 0sin
( ∆θ0 2
)]
± iχN
2 cos
( ∆θ0 2
)
,
u2± = 1
4
√
4 20 − 2χ2N 2 − 2χN
[
χN cos(∆θ0) − 4 0sin
( ∆θ0 2
)]
± iχN
2 cos
( ∆θ0 2
)
.
(S10)
This result indicates we should expect phase III for small enough inhomogeneity and regardless of the initial opening angle (excluding the trivial case when ∆θ0 = ±π). Secondly, for 0 W/(χN ) [case iii)] we have
u± = ± iW
4 tan
[W
4χN sec
( ∆θ0 2
)]
, (S11)
for W/(χN ) < 2πcos(∆θ0/2). This result demonstrates there exists a transition between phases II and I at W/(χN ) = 2πcos(∆θ0/2) identically to our previous analysis of case iii) for the state |ψ0〉.
Analytic solution of phase III from Lax analysis
The dynamics of the BCS pairing amplitude, |∆(t)|, in phase III can be solved exactly in certain cases. Specifically, by adopting an amplitude-phase parametrization of the pairing term, ∆(t) = √R(t)eiφ(t), and substitution of this into the classical equations of motion [24, 26] a description of the dynamics of the amplitude R(t) can be reduced to the single differential equation
R ̇ 2 = 4(R+ − R)(R − R−)(R + R ̃). (S12)
Here, R± and R ̃ are obtained from the roots of the Lax vector [27, 64]. Denoting the two pairs of complex roots as u ̄1± = u ̄1r ± iu ̄1i and u ̄2± = u ̄2r ± iu ̄2i we have
R± = (|u ̄1i| ± |u ̄2i|)2 and R ̃ = (u ̄1r − u ̄2r)2. Before proceeding further, we point out that some features of the pairing amplitude oscillations in phase III can already be predicted. Specifically, we have that the oscillation amplitude is A = max(|∆(t)|)−min(|∆(t)|) = √R+−√R−. For certain cases, Eq. (S12) can be solved analytically. In particular, when ∆φ0 = π we have that |u ̄1i| = |u ̄2i| [see Eq. (S4)] so that R− = 0. Then, a solution to Eq. (S12) is
|∆(t)| = √R+
∣ ∣ ∣ ∣
sn
(
t
√R ̃, − R+
R ̃
)∣ ∣ ∣ ∣
, (S13)
FIG. S2. Dynamical phase diagram for: (a) |ψ′
0〉 = |π/2 + ∆θ0/2, 0〉+ ⊗ |π/2 − ∆θ0/2, 0〉− and (b) |ψ0〉 = |π/2, ∆φ0/2〉+ ⊗ |π/2, −∆φ0/2〉−. Parameters are identical to Fig. 2b of main text, particularly 0/(χN ) = 0.1. Some small structure, particularly the protrusion of phase III into phase II in panel (a), is likely a numerical artefact related to the breakdown of our numerical algorithm as it requires a minimum tolerance as an input to distinguish roots.
where sn(u, m) is a Jacobi elliptic function. The nonlinear oscillations of |∆(t)| can then be determined to have an amplitude A = √R+ and a period T =
4K (−R+ /R ̃ )/
√R ̃ where K(m) is the complete elliptic integral of the first kind. In the limit of W 0 χN


 5
FIG. S3. Amplitude A ≡ max(|∆(t)|) − min(|∆(t)|) of oscillations in |∆(t)| obtained analytically from Eqs. (S13) and (S4) (solid black line) and numerical integration of mean-field equations of motion following from the Hamiltonian (S1) for N = 103 (grey markers). Calculations are for an initial state with ∆φ = π, 0/(χN ) = 0.1 and varying W/(χN ). Phases I and III, equivalent to A = 0 or A 6= 0 in this case, are indicated by the blue and yellow backgrounds, respectively.
we can simplify R+ = R ̃ ≈ 0χN/2 from Eq. (S4). This results in a pair of observations: i) the amplitude of os
cillations vanishes as A = √
0χN /√2 for small splitting, and similarly ii) the frequency ωosc of oscillations is ap
proximately ωosc ∼ 1/T ∝ √
0χN . This latter result is clearly illustrated in Fig. 3d of the main text. As further verification of both our Lax analysis and the predictions of Eq. (S13) we compare the amplitude A for dynamics of the initial state with ∆φ0 = π obtained from: i) the analytic solution of the Lax roots Eq. (S4), and ii) full numeric integration of the mean-field equations of motion following from the Hamiltonian (S1). Results are plotted in Fig. S3. We observe excellent quantitative agreement, not only in terms of the boundary between phases I and III but also the predicted A as a function of W/(χN ). Small differences are entirely attributable to finite size effects (e.g., analytic results assume N → ∞ and thus a continuous distribution of εj).
Phases IIIa and IIIb
We also report in the main text an identification of sub-phases IIIa and IIIb in the limit W χN, 0. Our classification of these sub-phases is instead related to the characterization of the real and imaginary parts of the two pairs of complex roots present for phase III. To be concrete, we define sub-phases IIIa and IIIb by the effective order parameter R−, which was previously introduced in the differential equation (S12). To recap, R− = (|u ̄1i| − |u ̄2i|)2 where we have written the roots of the squared Lax vector in the form u ̄1± = u ̄1r ± iu ̄1i and u ̄2± = u ̄2r ± iu ̄2i. Phase IIIa exists for R− = 0 and phase IIIb for R− 6= 0. Inspecting Eq. (S12) we observe that R± define the maximum and minimum values of the
oscillations in |∆(t)|2, so clearly we can also interpret phase IIIa as oscillations where the pairing amplitude periodically vanishes |∆| = 0, whereas in phase IIIb the pairing amplitude is strictly greater than zero always, |∆| > 0.
Mathematically, the condition R− = 0 corresponds to the case where the magnitude of the imaginary part of the Lax roots is identical for both pairs, i.e., |u ̄1i| = |u ̄2i|. In the limit of W χN, 0 we can use the results of Eq. (S6) to identify that this condition occurs for a critical splitting
c
0 = χN
2 [1 + cos(∆φ0)]. (S14)
EXPERIMENTALLY REALISTIC MODEL
In Fig. 4 of the main text we present quantitative predictions illustrative of the dynamical phases based upon state-of-the-art cavity-QED experiments. Here, we summarize the model these calculations are based upon. For the interested reader, further detail regarding the derivation of our model can be found in Ref. [9] and the associated Supplementary Information.
Emulated BCS-like Hamiltonian
We consider an ensemble of 2N atoms confined in a standing wave optical lattice supported by a cavity. Each atom encodes a spin-1/2 in a pair of long-lived electronic states, | ↑〉 and | ↓〉, which are separated by a narrow linewidth optical transition of frequency ωa. A single common cavity mode couples the electronic states with single-photon Rabi frequency 2g. In the limit that the cavity mode at frequency ωc is far detuned from the
atomic transition |δc| = |ωc−ωa| g√N , then the cavity field can be adiabatically eliminated and the intracavity photons serve only to mediate effective exchange interactions between the spins. Single-particle energy shifts can be generated by applying external fields to generate Stark or Zeeman shifts of the electronic states. Combining these effects with relevant sources of decoherence leads to an effective description for the atomic system in terms of a Lindblad master equation for the density matrix ρˆa,
dρˆa
dt = − i
ħ
[Hˆ , ρˆa
]
+ Ls[ρˆa], (S15)
with Hamiltonian
Hˆ = ħ
∑
i,j
χij σˆ+
i σˆ−
j+
∑
i
εj σˆz
i , (S16)


 6
and decoherence due to spontaneous emission at rate γs described by the Lindblad jump operator,
Ls[ρˆ] = γ
2
∑
i
2σˆ−
i ρˆσˆ+
i − σˆ+
i σˆ−
i ρˆ − ρˆσˆ+
i σˆ−
i . (S17)
In the Hamiltonian (S16) the all-to-all interactions are characterized by χij = −gigj/δc. The inhomogeneity is inherited from the spatial variation of the atomlight coupling, gj ∝ gcos(kdj) for kd = πλL/λc, due to the incommensurate wavelengths of the confining lattice, λL = 813 nm, and cavity mode, λc = 689 nm. In numerical simulations (see later discussion) we typically observe that the main consequence of inhomogeneous interactions is to effectively re-scale the interactions to their rootmean-square value, χ → χ/2. This is also consistent with related work published in Refs. [9, 35].
State preparation
State preparation is realized by a combination of coherent single-particle rotations and shifts of the internal atomic levels. Specifically, we assume that all spins are initially prepared in the single-particle state | ↓〉j. The cavity is suddenly injected with coherent light which is tuned to be resonant with the atomic transition [9]. This process can be modelled as a single-particle term Hrot = ∑
j
Ωj
2 σˆy
j . The inhomogeneity of the driving term Ωj = Ω0cos(kdj) ∝ gj is again inherited from the inhomogeneous atom-light coupling gj. In our simulations, we apply Hrot for a time τrot so that Ω0τrot = π/2, i.e., a π/2-pulse is engineered with respect to the strongest coupled atoms, i.e., Ωj = Ω0. For simplicity, we assume Ω0 χN, 0, W such that interactions and energy shifts can be ignored during state preparation. After the single-particle rotation sequence, the variable opening angle ∆φ0 of the initial state can be generated by suddenly turning on a (selective) large uniform energy splitting between the atoms of each ensemble, e.g., εj = ± 0, to generate precession of each ensemble about the zaxis. This could be achieved, for example, by a spatially
selective optical Stark shift of the internal levels | ↑〉 and | ↓〉.
The combination of these two coherent operations leads to initial states of the form |ψ0〉 = |ψ0〉+ ⊗ |ψ0〉− where |ψ0〉± =
⊗
j
[cos(θj/2)| ↓〉j + e±i∆φ/2sin(θj/2)| ↑〉j
] with θj = (π/2)cos(kdj) and j runs over 1, ..., N or N + 1, ..., 2N for the respective ensembles.
Measurement of pairing amplitude via leaked light
The BCS pairing amplitude, proportional to the transverse spin coherence, can be monitored in experiment by detecting the light which leaks out through the cavity mirrors. Specifically, when the cavity field is eliminated to yield the effective spin model Eq. (S15), at the meanfield level the intra-cavity field is related to the spins via
〈ˆa〉 = −2
2δc − iκ
∑
j
gj 〈σˆ−
j 〉. (S18)
We use this relation to plot the dynamics of the intracavity field in Fig. 4 of the main text.
Numerical simulation and parameters
To simulate the experimental system we solve the mean-field equations of motion associated with the master equation (S15). Specifically, we use the software package XMDS2 [65] to numerically integrate the system of equations generated by O ̇ = Tr[Oˆ d
dt ρˆa] with the approx
imation 〈Oˆ1(t)Oˆ2(t)〉 = 〈Oˆ1(t)〉〈Oˆ2(t)〉. To account for inhomogeneities in the effective spinspin interactions and state preparation we model a system composed of two distinct ensembles (±) of atoms spatially distributed at lattice sites j = 1, 2, ..., 2Nsim. Typically, we take Nsim = 102 − 103 and re-scale all parameters and results to match a true atom number of N = 106. We adopt relevant parameters from Ref. [9]: g/(2π) = 10.9 kHz, γs/(2π) = 7.5 kHz, δc/(2π) = −50 MHz and κ/(2π) = 153 kHz.
