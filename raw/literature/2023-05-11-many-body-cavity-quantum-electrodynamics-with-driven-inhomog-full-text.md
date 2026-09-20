# Many-body cavity quantum electrodynamics with driven inhomogeneous emitters - Full Text

> Source: https://www.nature.com/articles/s41586-023-05884-1
> Collected: 2026-09-20
> Published: 2023-05-11
> Zotero parent key: 7LB2E9AQ
> Evidence: Zotero indexed PDF text

Nature | Vol 617 | 11 May 2023 | 271
Article
Many-body cavity quantum electrodynamics with driven inhomogeneous emitters
Mi Lei1,2,3,7, Rikuto Fukumori1,2,3,7, Jake Rochman1,2,3, Bihui Zhu4, Manuel Endres3,5, Joonhee Choi3,5,6 ✉ & Andrei Faraon1,2,3 ✉
Quantum emitters coupled to optical resonators are quintessential systems for exploring fundamental phenomena in cavity quantum electrodynamics (cQED)1 and are commonly used in quantum devices acting as qubits, memories and transducers2. Many previous experimental cQED studies have focused on regimes in which a small number of identical emitters interact with a weak external drive3–6, such that the system can be described with simple, effective models. However, the dynamics of a disordered, many-body quantum system subject to a strong drive have not been fully explored, despite its importance and potential in quantum applications7–10. Here we study how a large, inhomogeneously broadened ensemble of solid-state emitters coupled with high cooperativity to a nanophotonic resonator behaves under strong excitation. We discover a sharp, collectively induced transparency (CIT) in the cavity reflection spectrum, resulting from quantum interference and collective response induced by the interplay between driven inhomogeneous emitters and cavity photons. Furthermore, coherent excitation within the CIT window leads to highly nonlinear optical emission, spanning from fast superradiance to slow subradiance11. These phenomena in the many-body cQED regime enable new mechanisms for achieving slow light12 and frequency referencing, pave a way towards solid-state superradiant lasers13 and inform the development of ensemble-based quantum interconnects9,10.
Cavity quantum electrodynamics (cQED) offers the ability to investigate and understand the interactions between light and matter at the most fundamental level1. The field has enjoyed great experimental advancements in the past decades, as the rapid development of microscopic and nanoscopic devices and laser trapping techniques have shown a diverse and rich set of phenomena3,14. Such progress has also led to the use of cQED in quantum technology applications, including quantum information processing15,16, light field manipulation5,17, single-photon generation18 and quantum communication9,19,20, as the ability to change the properties of the emitters with light (and vice versa) has proved to be an indispensable tool for highly controlled quantum operations. Although many works in cQED have focused on one or a few cavitycoupled emitters4,5,16–18,20–24, there has been growing interest in the study of cQED with a macroscopic ensemble of emitters25–28, as the increased complexity offers deeper fundamental insights as well as expanded technological capabilities. Cavity-coupled ensembles of rare-earth ions doped in solids are an ideal platform for such a study29,30, as they offer highly stable transitions in both the optical and microwave domains at cryogenic temperatures31 and can be readily integrated into nanoscale devices32. In contrast to atomic gas systems25,27, the solid-state implementation offers the added benefit of on-chip integration for quantum applications such as high-bandwidth quantum memories and transducers33,34. Here the high bandwidth is necessary for frequency multiplexing in memories and high-speed conversion in transducers,
and is achieved as a result of the natural spectral inhomogeneity of the solid-state emitters. For such devices to operate efficiently, one must engineer a system with high cooperativity, which is a dimensionless figure of merit that describes the ratio between the collective coupling strength of the cavity–emitter system to dissipation, decoherence and disorder. As improvements to material and device parameters are made towards increasing this cooperativity, it becomes critical to fully understand any associated cQED phenomena that may emerge. In this work, we study an ensemble of approximately 106 171Yb3+ ions embedded in YVO4 coupled to a nanophotonic cavity (Fig. 1a and Extended Data Fig. 1), subjected to a strong driving field such that the resonant ions are excited. The relatively low spectral inhomogeneity, the strong transition dipole moment35 and the cavity coupling lead to a high optical cooperativity of up to 24 (Supplementary Information). This allows for strongly enhanced light–matter interactions, enabling the investigation of complex collective and many-body phenomena36. In particular, we discover a sharp transparency window in the cavity reflection spectrum, which we call collectively induced transparency (CIT) (Fig. 1b,c). We find that the quantum interference of many inhomogeneously broadened emitters plays a critical role in producing the CIT window, mechanistically distinguishing itself from other types of transparencies37. Taking advantage of the CIT effect, we further control the population distribution within the Dicke space11, which allows the observation of dissipative many-body dynamics in the form of
https://doi.org/10.1038/s41586-023-05884-1
Received: 8 August 2022
Accepted: 24 February 2023
Published online: 26 April 2023
Check for updates
1Kavli Nanoscience Institute, California Institute of Technology, Pasadena, CA, USA. 2Thomas J. Watson, Sr., Laboratories of Applied Physics, California Institute of Technology, Pasadena, CA, USA. 3Institute for Quantum Information and Matter, California Institute of Technology, Pasadena, CA, USA. 4Homer L. Dodge Department of Physics and Astronomy, The University of Oklahoma, Norman, OK, USA. 5Division of Physics, Mathematics and Astronomy, California Institute of Technology, Pasadena, CA, USA. 6Present address: Department of Electrical Engineering, Stanford University, Stanford, CA, USA. 7These authors contributed equally: Mi Lei, Rikuto Fukumori.✉e-mail: joonhee.choi@stanford.edu; faraon@caltech.edu


 272 | Nature | Vol 617 | 11 May 2023
Article
superradiance and subradiance (Fig. 1d). The features of the observed dynamics are well explained by numerical simulations based on a many-body master equation.
CIT
To explore cQED phenomena for a driven, inhomogeneous many-body system, we first characterize the cavity–ion coupling by measuring the cavity reflection spectrum. Scanning with low laser power, the spectrum shows broad peaks centred around the atomic resonances reaching
unit reflection with about 3 GHz width, larger than the ensemble inhomogeneous linewidth of 150 MHz (Extended Data Fig.2). These peaks are known as dipole-induced reflectivity (DIR), resulting from strong ion–cavity coupling38 (Fig. 1b, middle). Specifically, in steady state under continuous driving, the cavity field ⟨a⟩ depends on the sum of the atomic coherences σ j
− of individual emitters as a ∝ ∑ j σ
N
=1 j
− , in which σj = ∣g j e∣
− for the jth ion. As such, even if most ions remain in the ground state at weak excitation, the Yb ions still modify the internal cavity field owing to the non-zero atomic coherence. This in turn influences the cavity reflectivity, leading to DIR. However, when the laser power is increased, we observe the formation of a sharp dip around the centre of the DIR, which both deepens and narrows with increasing power (Fig. 2b). A Lorentzian fit to the dip gives a minimum width of 50 MHz, and a maximum normalized depth approaching 1 (Fig. 2d; Methods). We find that the origin of such a transparency window can be understood as the collective contribution of the inhomogeneous ensemble to the cavity field (Fig. 2a). For clarity, the individual contributions of on-resonance and off-resonance ions (with respect to the laser) should be considered separately. For resonant ions, strong driving saturates their steady-state populations to the completely mixed state, in which both atomic inversion and coherence vanish, thus having no influence on the cavity field. By contrast, the off-resonant ions are only weakly excited, such that their atomic coherence is inversely proportional to the ion detuning Δj, that is, σj ∝ ∆ j
− −1 (Supplementary Information). This means that ions at equal and opposite detunings are out of phase with equal amplitude, such that their pairwise contributions to the cavity field will destructively interfere. In particular, when the laser frequency is in the centre of the inhomogeneous line, all of the contributions from the detuned ions cancel with each other (Fig. 2a, centre). Thus, the combination of these two effects, (1) the saturation of the on-resonance ions and (2) the pairwise destructive interference of the off-resonant ions, leads to a transparency (the CIT) that emerges at the centre of the inhomogeneous line (Methods). It is worth noting that CIT is unique to systems consisting of a large ensemble of emitters with an appreciable inhomogeneous broadening39 and does not occur for just a few emitters (Supplementary Information). Going beyond the qualitative description, we derive an analytical expression for the width of CIT (ΔCIT) using the N-atom TavisCummings Hamiltonian40 under appropriate approximations (Methods):
∆∆
CC
≈1
1 − (1)
γγ gμ
CIT
inh
4
s 2
 
 
in which γ = γ + γ
2d
s is the total decoherence rate, consisting of the spontaneous decay rate γs and the excess dephasing rate γd, g is the single ion–cavity coupling rate, C = 4Ng2/(κΔinh) is the ensemble cooperativity and μ is the cavity mean photon number in the absence of ions, representing the rescaled driving laser power (Methods). The measured CIT widths and depths show excellent agreement with the predicted power dependence (Fig. 2d; Methods). Crucially, at high powers, we expect the dip width to be narrowed by the ensemble cooperativity, reaching ΔCIT ≈ Δinh/C. Intuitively, this is because higher cooperativity leads to a larger contribution towards DIR for even a small number of imbalanced ions, effectively increasing the sensitivity to the imbalance near the ensemble centre, which narrows the CIT. This indicates that, if C ≫ 1, the CIT width can be substantially narrower than the inhomogeneous broadening of an ensemble, ultimately limited by the homogeneous linewidth (Extended Data Fig. 3). Given our C and Δinh, the expected minimum linewidth is 13 MHz, narrower than the measured value of 50 MHz. This discrepancy can be partially attributed to spectral diffusion, which effectively increases γ and causes a breakdown of some of the assumptions made to derive the approximate analytical
Atomic density
Time
Superradiance
Superradiant ladder
Subradiance
Dicke space
J
M 2
1
–1
–2
0
210
Subradiant space
984 nm
DIR CIT
Bare cavity Weak drive Strong drive
Detuning
ΔCIT
Δinh
Reflection Reflection
a
b
c
d
Photon emission
Yb ion
Reflection
Detuning
Ain
|e〉
|g〉
g
N
c
Γc ∝ g2/N
N – Nc
Fig. 1 | cQED with driven inhomogeneous emitters. a, Schematic description of the cavity–ion interaction. An inhomogeneous ensemble of ions is coupled to a one-sided cavity with total decay rate κ. The input field Ain is coupled into the cavity with rate κc. The interaction strength between the cavity field and a single ion is g. Two spectrally indistinguishable ions have an effective cavity-mediated dissipation rate Γc = 4g2/κ. Each Yb ion can be regarded as an effective two-level system consisting of a ground state (|g⟩) and an excited state (|e⟩), whose transition wavelength is around 984 nm (dashed box). b, Reflection spectrum of a cavity without ions showing the bare cavity resonance (left), with ions under weak drive showing DIR (middle) and with ions under strong drive showing DIR and CIT (right). c, Zoom-in of the right part of b, showing CIT. CIT opens a transmissive window narrower than the inhomogeneous linewidth and allows for the excitation of ions in the centre of the ion distribution. d, Schematic of superradiance (orange) and subradiance (blue) that are enhanced (suppressed) decays in which emissions from ions constructively (destructively) interfere. Inset shows the Dicke space for four two-level systems in the |J,M⟩ basis48, in which the J = 2 manifold forms the superradiant ladder and the rest form the subradiant subspace (Methods).


 Nature | Vol 617 | 11 May 2023 | 273
expression equation (1) (Methods). To account for this, numerical simulations of the cavity reflection (without the above approximations) provide a better match to the experimental width (Fig. 2c; Methods).
Dissipative many-body dynamics
CIT enables the investigation of the rich dynamics of a driven subensemble near the transparency window, as the effect of the off-resonant ions
on the cavity field is cancelled and more light is allowed to enter the cavity. To investigate the dynamics, we tune the laser to the centre of the CIT and detect the cavity emission after pulsed excitation (Fig. 3a). For state initialization, the system is driven to a non-equilibrium steady state using a long pulse (Supplementary Information). Varying the excitation power prepares the system into different initial states, followed by distinct emission dynamics (Fig. 3b). Analysing the peak counts of the emission, we find that the trend of peak counts with power is strongly non-monotonic, forming an S-shaped curve (Fig. 3c). To systematically characterize the observed nonlinear dynamics, we classify three power regimes (I, II and III) based on the slope of the S-curve. In regime I, with low powers, the decay is predominantly fast. A characteristic 1/e decay time is measured to be about 150 ns, faster than the fastest expected Purcell decay of a single ion coupled to the cavity (roughly 1.4 μs; Fig. 3b, inset). In regime II, with intermediate powers, both a fast and a slow decay compared with the Purcell-enhanced rate are observed. In regime III, with higher power, a continuum of different decay lifetimes are observed, leading to a stretched exponential decay. To gain a microscopic understanding of this nonlinear power dependence, we use a master equation to describe driven dynamics in the presence of decoherence and dissipation. The numerical simulation of the entire inhomogeneous ensemble of N ≈ 106 ions is not tractable. However, the phase cancellation in CIT negates the influence of the off-resonance ions on the cavity field, which allows us to initially only consider the dynamics of the resonant ions. Furthermore, we note that the cavity mediates photon exchange between ions, which triggers collective dissipation with rate proportional to Γc = 4g2/κ (Methods). As the system dissipation is dominated by Γc, a smaller number of ions that sit within a spectral window whose width is about Γc can be treated as indistinguishable ions. To this end, we first simulate a small-scale homogeneous ensemble. Specifically, we study a toy model of six identical ions whose dynamics can be described using the Dicke states, the coupled basis defined for indistinguishable two-level systems11. As shown in Fig. 1d and Extended Data Fig. 4, vertical decays between the Dicke states are enhanced and superradiant, and diagonal decays are suppressed and can only decay through individual dissipation channels, which we call subradiance (see Methods for details, including semantics). To effectively capture the existence of several decay rates among the various Dicke states, as well as a clear separation between fast (superradiant) and slow (subradiant) decays, we use a phenomenological stretched bi-exponential fit and extract the relevant fit parameters, which also clearly shows the presence of the three distinct regimes discussed earlier (Fig. 3d; Methods). By simulating the dynamics of this system using the master equation, we find that the peak emission is a good indicator for the population distribution of the Dicke states prepared by the drive (Methods). The simulated peak emission matches the trend measured in regimes I and II, in which distinct temporal dynamics are attributed to decays from different parts of the Dicke space (Extended Data Fig. 5). In regime I, we attribute the fast decay to superradiance, dominantly from the collective dissipation within the superradiant ladder, as we expect to have populated only the low-excitation superradiant states within a narrow bandwidth of the ensemble (Fig. 3f, top). From the measured fast decay rate, we estimate the number of ions participating in superradiance to be on the order of about 50 (Supplementary Information). With increased power, we expect that the system climbs up the superradiant ladder and reaches Dicke states with larger decay rates, leading to even faster emission. This is consistent with the observed trend of decreasing τ1 in regime I as shown in Fig. 3d. At even higher powers, strong driving of the superradiant ladder allows for substantial population to diffuse into the subradiant space by means of decoherence processes, resulting in the slow decay observed in regime II (refs. 41,42) (Fig. 3f, middle). Populating several dark subradiant states exhibiting different decay rates manifests as a stretched exponential decay in the emission dynamics.
Detuning
Ion phase
–π/2 π/2
0
Atomic density
a Laser
Experiment Simulation
bc
d
–1 0 1 Laser detuning (GHz)
Reflection (a.u.)
Reflection (a.u.)
–1 0 1 Laser detuning (GHz)
0.01 nW 0.02 nW 0.50 nW
0
0.5
1.0
Normalized CIT depth
012 Power (nW)
40
60
80
100
CIT width (MHz)
|e〉
|g〉
|e〉
|g〉
0.04 nW 0.08 nW 2.00 nW
Fig. 2 | CIT. a, Physical origin of CIT, showing the phase distribution of atomic coherence of the inhomogeneous ensemble. The ions far detuned from the laser frequency are out of phase on the two sides, denoted in red and blue. The resonant ions are denoted in white. The left and right Bloch spheres contain the Bloch vectors of the red-detuned and blue-detuned ions, respectively. Three scenarios with different laser frequencies are shown. If the laser is detuned from the ensemble centre (top and bottom), there is imbalance in the ion phases, whereas if the laser is centred (middle), the ion phases cancel and lead to CIT. b, Measured cavity reflection spectra at three different powers, vertically shifted for clarity. Sharp dips resulting from CIT appear at the centre of the DIR peaks, which become deeper and narrower with increased power. c, Corresponding simulated cavity reflection spectra (Methods). d, Extracted Lorentzian fit width (blue) and depth (orange) with power, error bars represent the standard errors of the fit. The CIT depth is normalized with respect to the cavity depth. Solid lines are the fits from our theoretical prediction (Methods). a.u., arbitrary units.


 274 | Nature | Vol 617 | 11 May 2023
Article
In regime III, a completely mixed state of equal population in each Dicke state can be reached (Fig. 3f, bottom). Further increasing the power excites more of the off-resonance ions, whereas the subensemble of the on-resonance ions addressed in regimes I and II remains in the completely mixed state. This leads to the emergence of intermediate decays, departing from the homogeneous Dicke subensemble picture, which suggests that a wider excitation bandwidth at high powers should be considered in numerical simulations. To this end, we simulate a larger number of emitters by including a Lorentzian distributed ensemble of ions with experimental inhomogeneous linewidth (Methods). Specifically, the dynamics of each subensemble is computed separately and incoherently added, by assuming that the subensembles are effectively non-interacting (Extended Data Fig. 6). The emergence of the upturn of the peak counts at high powers is reproduced by the simulation (Fig. 3e), consistent with the experimental observation in regime III.
Control over coherent emission
To demonstrate control over the dissipative many-body dynamics and to show further evidence of the beyond-single-atom nature of the cavity emission, we first modify the decay dynamics by changing the number of ions. Specifically, we tune the number of ions resonant with our excitation laser Nres through optical hole burning and then observe the changes in the S-curve (Fig. 4a). On increasing Nres, the S-curve shifts towards higher power in regimes I and II, along with an increase in the maximum of peak counts (Fig. 4b). The shift implies the formation of a larger superradiant ladder when the number of local homogeneous ions increases, which requires more excitation power to optically pump into the subradiant subspace (Supplementary Information). However, regime III is observed to be largely insensitive to a change in Nres, as indicated by the overlap of the S-curves, because spectral hole burning
only changes the population locally in frequency without affecting the number of detuned ions, as illustrated in Fig. 4a. We provide further evidence of the traversal of the Dicke space by measuring the coherence of the emission through heterodyne detection (Methods). The beat note between the emission and the excitation laser provides the rate and amount of coherent decay through its width Γbeat and amplitude Abeat, respectively (Fig. 4c, inset). We first note the increase of Abeat in regime I, indicating the increase in population of the superradiant ladder. Later, Abeat decreases in regime II, corresponding to the incoherent coupling to the subradiant subspace. Finally, in regime III, Abeat vanishes because of the absence of coherent decay, as the population has undergone incoherent processes to reach the completely mixed state. Because only decays within the superradiant ladder are coherent with respect to the excitation, Γbeat represents the rate of superradiance within the superradiant ladder. For comparison, we extract the fast decay part of the time dynamics of photon emission as a single exponential with the rate Γ1, which captures all of the enhanced decays from both superradiant and subradiant subspaces (Fig. 4d, filled markers). The comparison between Γbeat and Γ1 can then be used to evaluate the relative decay contributions from the two subspaces. We find that Γ1 overlaps with Γbeat for low powers, confirming that all of the fast decays in regime I are within the superradiant ladder. However, entering regime II, Γ1 deviates from Γbeat (for powers beyond the dashed lines in Fig. 4d). This observation of Γ1 < Γbeat in regime II indicates that Γ1 also includes some incoherent decays slower than Γbeat, which point to the enhanced decays within the subradiant subspace (Extended Data Fig. 4a). Last, we have also performed another measurement by varying the frequency of the probe laser to control the number of driven ions and observed that the nonlinear S-curve shifts along the expected direction (Extended Data Fig.7). We have also confirmed that all of the
0 5 10 15 20 Time (μs)
0
10
20
Counts (kcts)
0 0.5
Time (μs)
5
15
Counts (kcts)
Purcell
10
30
Peak (kcts)
10
30
Peak (a.u.)
0.1
10
Time (μs)
Purcell
WW12
0
1
Amplitude
AA12
0 20 40 Power (nW)
0 20 40 Power (nW)
0
0.5
1.0
Stretch factor
xx12
Atomic
density
Detuning
I
II
III +
+ + ...
...+
Excitation bandwidth
Dicke space occupation
J
M
50 μs
Excitation
Peak counts
Emission
Simulation
ac
bd
e
f
II
III
I
II III
I
Experiment
Fig. 3 | Observation and analysis of dissipative many-body cavity emission. a, Measurement schematic. After a 50-μs-long excitation pulse, peak counts are obtained by integrating the counts within the first 128 ns. b, Three representative cavity emission time traces from each of the three power regimes with equal peak counts (3, 14 and 26 nW). All traces are fit to a phenomenological stretched bi-exponential fit, A exp[−(t /τ ) ] + A exp[−(t /τ ) ] + b
xx 1 12 2
1 2 (Methods). Inset, single-exponential fit for the first 500 ns of the emission excited with 3 nW, with higher time resolution. The fitted decay lifetime of approximately 150 ns (solid line) shows an enhancement beyond the fastest expected Purcell decay of about 1.4 μs (dashed line). c, Peak counts with varying excitation power. The three labelled points correspond to the data shown in b. d, Fit parameters, A1,2, τ1,2 and x1,2, of the time traces. The transparency of the data points in the decay times τ1,2
and stretch factors x1,2 are weighted by their relative amplitudes A
A +A
1,2 12
to
emphasize the importance of the parameters. In regime III (for powers greater than 20 nW), x1 is set to 1, as there is no longer a distinct fast decay (Methods). e, Master equation simulation of 91 subensembles of identical ions, for a total of N = 569 ions. Incoherently adding the peak emission of detuned subensembles qualitatively reproduces the S-curve observed in the experiment (Methods). f, Schematics of excitation bandwidth and Dicke space occupation in the three power regimes. In regime I, only a narrow bandwidth is excited and primarily the low-excitation superradiant states are occupied. In regime II, the bandwidth increases and the subradiant subspace becomes populated. In regime III, the bandwidth further increases and the off-resonant subensembles get excited while leaving the on-resonance subensemble in a completely mixed state. a.u., arbitrary units.


 Nature | Vol 617 | 11 May 2023 | 275
experimental findings for CIT and subradiance and superradiance are reproducible and consistent with our theoretical predictions, independent of the choice of the optical emission lines between the A, E and I transitions (Extended Data Fig. 8). All of these complementary
experiments lend strong support to our microscopic understanding and control of an inhomogeneous ensemble.
Discussion and outlook
In this work, we have investigated the spectral response and open quantum dynamics of a large cQED system, showing a sharp CIT and highly nonlinear, dissipative many-body dynamics. Notably, the CIT width is found to be narrowed by cooperativity, indicating that improvements in fabrication and material properties towards increasing cooperativity can lead to much narrower transparencies, potentially useful as frequency references. The sudden cavity phase shift across the CIT (Extended Data Fig.9) can provide a new mechanism to achieve optical nonlinearities and the storage of light12. In particular, we demonstrate a proof-of-principle optical switch using CIT and posit that, with further optimization, a fast, high-contrast two-port optical switch can be realized (Extended Data Fig. 10). Further, the observed optical superradiance and subradiance represent a key step towards enabling narrow-linewidth superradiant lasers13 and long-lived subradiant memories43,44 in the solid state, whereas the control over the population of the Dicke space opens the door for dissipation-based engineering of state preparation45,46. Moreover, operating with a detuned cavity may enable investigation of the coherent photon-mediated interaction between the ions (Supplementary Information), opening new possibilities for studying coherent spin-exchange effects and quantum simulations25,47 in a solid-state platform. Finally, the improved understanding in this regime of collective and many-body cQED phenomena informs the development of high-cooperativity solid-state quantum memories and transducers9,10.
Online content
Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-023-05884-1.
1. Haroche, S. & Kleppner, D. Cavity quantum electrodynamics. Phys. Today 42, 24–30 (1989). 2. Awschalom, D. D., Hanson, R., Wrachtrup, J. & Zhou, B. B. Quantum technologies with optically interfaced solid-state spins. Nat. Photon. 12, 516–527 (2018). 3. Walther, H., Varcoe, B. T., Englert, B.-G. & Becker, T. Cavity quantum electrodynamics. Rep. Prog. Phys. 69, 1325 (2006).
4. Thompson, R., Rempe, G. & Kimble, H. Observation of normal-mode splitting for an atom in an optical cavity. Phys. Rev. Lett. 68, 1132 (1992). 5. Englund, D. et al. Controlling cavity reflectivity with a single quantum dot. Nature 450, 857–861 (2007). 6. Lukin, D. M. et al. Two-emitter multimode cavity quantum electrodynamics in thin-film silicon carbide photonics. Phys. Rev. X 13, 011005 (2023). 7. Kurucz, Z., Wesenberg, J. H. & Mølmer, K. Spectroscopic properties of inhomogeneously broadened spin ensembles in a cavity. Phys. Rev. A 83, 053852 (2011). 8. Diniz, I. et al. Strongly coupling a cavity to inhomogeneous ensembles of emitters: potential for long-lived solid-state quantum memories. Phys. Rev. A 84, 063810 (2011). 9. Afzelius, M. & Simon, C. Impedance-matched cavity quantum memory. Phys. Rev. A 82, 022310 (2010). 10. Williamson, L. A., Chen, Y.-H. & Longdell, J. J. Magneto-optic modulator with unit quantum efficiency. Phys. Rev. Lett. 113, 203601 (2014). 11. Dicke, R. H. Coherence in spontaneous radiation processes. Phys. Rev. 93, 99–110 (1954). 12. Novikova, I., Walsworth, R. L. & Xiao, Y. Electromagnetically induced transparency-based slow and stored light in warm atoms. Laser Photonics Rev. 6, 333–353 (2012). 13. Bohnet, J. G. et al. A steady-state superradiant laser with less than one intracavity photon. Nature 484, 78–81 (2012). 14. Blais, A., Grimsmo, A. L., Girvin, S. M. & Wallraff, A. Circuit quantum electrodynamics. Rev. Mod. Phys. 93, 025005 (2021). 15. Duan, L.-M. & Kimble, H. J. Scalable photonic quantum computation through cavityassisted interactions. Phys. Rev. Lett. 92, 127902 (2004). 16. Dordević, T. et al. Entanglement transport and a nanophotonic interface for atoms in optical tweezers. Science 373, 1511–1514 (2021). 17. Mücke, M. et al. Electromagnetically induced transparency with single atoms in a cavity. Nature 465, 755–758 (2010). 18. Keller, M., Lange, B., Hayasaka, K., Lange, W. & Walther, H. Continuous generation of single photons with controlled waveform in an ion-trap cavity system. Nature 431, 1075–1078 (2004).
a
A
Burn off
AC
Burn on
Detuning
Atomic
density
J
M
J
M
b
c
d
0
10
20
Peak (kcts)
Burn off Burn on
0
0.5
1.0
Normalized Abeat
405 410 Beat frequency (MHz)
0
1
Amplitude
Γbeat
Abeat
0 20 40 Power (nW)
0
5
10
15
Decay rate (MHz)
Γbeat
Γ1
|e〉
|g〉
|Aux〉
Fig. 4 | Control and characterization of dissipative many-body dynamics through hole burning. a, Schematic representations of hole burning (left, no hole burning; right, with hole burning). The C transition connects another state |Aux⟩ in the ground-state manifold to the excited state |e⟩. Optical pumping on the C transition transfers population from |Aux⟩ to |g⟩, introducing an antihole in the original distribution of the A transition. This increases the local ion density of the A transition at the probe frequency (coloured thin bars) and expands the Dicke space (shaded areas). See Methods for a detailed description of the A and C transitions and the |Aux⟩ state. b, Peak emission counts measured as a function of excitation laser power with (red) and without (blue) hole burning. The S-curve shifts towards higher power when the burning is on. c, Normalized beat-note amplitude Abeat for burning off (blue) and on (red). The two datasets are separately normalized, as the amplitude strongly depends on the local oscillator polarization, which can vary between experiments. Inset shows the experimental characterization of width Γbeat and amplitude Abeat of a beat signal from a heterodyne measurement (Methods). d, Single-exponential fit Γ1 (filled markers) from the time-dynamics measurement and extracted width Γbeat from a Lorentzian fit (open markers) from coherence measurements for burning off (blue) and burning on (red). Error bars represent standard errors of the fits. In b–d, vertical dashed lines indicate the turning points between regimes I and II.


 276 | Nature | Vol 617 | 11 May 2023
Article
19. Kimble, H. J. The quantum internet. Nature 453, 1023–1030 (2008). 20. Reiserer, A. & Rempe, G. Cavity-based quantum networks with single atoms and optical photons. Rev. Mod. Phys. 87, 1379–1418 (2015). 21. Yoshie, T. et al. Vacuum Rabi splitting with a single quantum dot in a photonic crystal nanocavity. Nature 432, 200–203 (2004). 22. Mlynek, J. A., Abdumalikov, A. A., Eichler, C. & Wallraff, A. Observation of Dicke superradiance for two artificial atoms in a cavity with high decay rate. Nat. Commun. 5, 5186 (2014). 23. Mirhosseini, M. et al. Cavity quantum electrodynamics with atom-like mirrors. Nature 569, 692–697 (2019). 24. Evans, R. E. et al. Photon-mediated interactions between quantum emitters in a diamond nanocavity. Science 362, 662–665 (2018). 25. Norcia, M. A. et al. Cavity-mediated collective spin-exchange interactions in a strontium superradiant laser. Science 361, 259–262 (2018). 26. Angerer, A. et al. Superradiant emission from colour centres in diamond. Nat. Phys. 14, 1168–1172 (2018). 27. Periwal, A. et al. Programmable interactions and emergent geometry in an array of atom clouds. Nature 600, 630–635 (2021). 28. Blaha, M., Johnson, A., Rauschenbeutel, A. & Volz, J. Beyond the Tavis-Cummings model: revisiting cavity QED with ensembles of quantum emitters. Phys. Rev. A 105, 013719 (2022). 29. Temnov, V. V. & Woggon, U. Superradiance and subradiance in an inhomogeneously broadened ensemble of two-level systems coupled to a low-Q cavity. Phys. Rev. Lett. 95, 243602 (2005). 30. Greiner, C., Boggs, B. & Mossberg, T. W. Superradiant emission dynamics of an optically thin material sample in a short-decay-time optical cavity. Phys. Rev. Lett. 85, 3793–3796 (2000). 31. Thiel, C., Böttger, T. & Cone, R. Rare-earth-doped materials for applications in quantum information storage and signal processing. J. Lumin. 131, 353–361 (2011). 32. Zhong, T., Rochman, J., Kindem, J. M., Miyazono, E. & Faraon, A. High quality factor nanophotonic resonators in bulk rare-earth doped crystals. Opt. Express 24, 536–544 (2016). 33. Businger, M. et al. Non-classical correlations over 1250 modes between telecom photons and 979-nm photons stored in 171Yb3+:Y2SiO5. Nat. Commun. 13, 6438 (2022). 34. Lauk, N. et al. Perspectives on quantum transduction. Quant. Sci. Technol. 5, 020501 (2020). 35. Kindem, J. M. et al. Characterization of 171Yb3+:YVO4 for photonic quantum technologies. Phys. Rev. B 98, 024404 (2018).
36. Reitz, M., Sommer, C. & Genes, C. Cooperative quantum phenomena in light-matter platforms. PRX Quantum 3, 010201 (2022). 37. Qin, H., Ding, M. & Yin, Y. Induced transparency with optical cavities. Adv. Photonics Res. 1, 2000009 (2020). 38. Waks, E. & Vuckovic, J. Dipole induced transparency in drop-filter cavity-waveguide systems. Phys. Rev. Lett. 96, 153601 (2006). 39. King, G. G. G., Barnett, P. S., Bartholomew, J. G., Faraon, A. & Longdell, J. J. Probing strong coupling between a microwave cavity and a spin ensemble with Raman heterodyne spectroscopy. Phys. Rev. B 103, 214305 (2021). 40. Tavis, M. & Cummings, F. W. Exact solution for an N-molecule—radiation-field Hamiltonian. Phys. Rev. 170, 379–384 (1968). 41. Cipris, A. et al. Subradiance with saturated atoms: population enhancement of the long-lived states. Phys. Rev. Lett. 126, 103604 (2021). 42. Glicenstein, A., Ferioli, G., Browaeys, A. & Ferrier-Barbut, I. From superradiance to subradiance: exploring the many-body Dicke ladder. Opt. Lett. 47, 1541–1544 (2022). 43. Shen, Z. & Dogariu, A. Subradiant directional memory in cooperative scattering. Nat. Photon. 16, 148–153 (2022). 44. Ferioli, G., Glicenstein, A., Henriet, L., Ferrier-Barbut, I. & Browaeys, A. Storage and release of subradiant excitations in a dense atomic cloud. Phys. Rev. X 11, 021031 (2021). 45. Verstraete, F., Wolf, M. M. & Ignacio Cirac, J. Quantum computation and quantum-state engineering driven by dissipation. Nat. Phys. 5, 633–636 (2009). 46. Kastoryano, M. J., Reiter, F. & Sørensen, A. S. Dissipative preparation of entanglement in optical cavities. Phys. Rev. Lett. 106, 090502 (2011). 47. Lewis-Swan, R. J. et al. Cavity-QED quantum simulator of dynamical phases of a Bardeen-Cooper-Schrieffer superconductor. Phys. Rev. Lett. 126, 173601 (2021). 48. Gross, M. & Haroche, S. Superradiance: an essay on the theory of collective spontaneous emission. Phys. Rep. 93, 301–396 (1982).
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.
© The Author(s), under exclusive licence to Springer Nature Limited 2023


 Methods
Device
The substrate is a 3.0 × 3.0 × 0.5-mm piece of 171Yb3+:YVO4 (a × a × c), measured to have a Yb doping concentration of 86 parts per million using glow discharge mass spectrometry49. The device is fabricated directly in the substrate using focused ion-beam milling. The optical cavity is formed by periodic grooves milled into a triangular nanobeam waveguide, with a slight aperiodicity in the centre that forms a defect creating the cavity mode. A 45° angled coupler couples the light from free space to the waveguide with an efficiency of roughly 25%. Further details on the device fabrication can be found in ref. 32. On the basis of the concentration of Yb ions and the cavity volume, we estimate that N ≈ 7 × 105 ions are coupled to the cavity with varying coupling strengths (Supplementary Information). The cavity is tuned into resonance with the 2F7/2 to 2F5/2 transition of Yb around λ = 984 nm using nitrogen gas condensation. The large cavity linewidth (κ = 2π × 44 GHz) covers all three transitions aligned along the cavity polarization (labelled as A, E and I in Extended Data Fig.2a). The narrow optical inhomogeneous linewidths (Δinh = 2π × 150 MHz) compared with the separation between those transitions (a few gigahertz) enables each transition to be addressed as independent two-level systems. Because of this, in the main text, we have focused primarily on the A transition for simplicity. The nanoscale cavity allows for tight confinement of the electromagnetic field, resulting in a small mode volume of about a cubic wavelength (≈ 1(λ/n)3, in which n is the refractive index). In conjunction with the relatively strong dipole moment of Yb in YVO4 (refs. 31,35), these factors enable high-vacuum Yb ion–cavity coupling g up to approximately 2π × 35 MHz, leading to a large collective ensem ble cooperativity C = 4Ng2/(κΔinh) > 1 in the optical regime. Considering the distribution of g, we obtain the root mean square of g as g ≈ 2π × 10.6 MHz
2 (Supplementary Information). Using this, we extract C ≈ 12 for the A and E transitions and C ≈ 24 for the I transition, which has twice the population as it connects degenerate doublets, in good agreement with expectation from system parameters (Supplementary Information).
Experimental set-up
The optical set-up for the experiments is shown in Extended Data Fig.1. Not all parts of the set-up are used in all of the measurements. The lasers addressing transitions A and C are both TOPTICA DL pro, tunable around 980 nm. Both lasers can be frequency locked (not shown in Extended Data Fig. 1) to a stable reference optical cavity using the Pound–Drever–Hall method and we measure a laser linewidth of approximately 600 Hz over 10 μs using the delayed homodyne method. The lasers can also be frequency swept by modulating the internal piezoelectric actuator. In this mode, the laser is free running, in which the linewidth is measured to be 50 kHz, with a slower drift in the centre frequency on the order of a few megahertz over tens of seconds. A Thorlabs S130 photodiode power sensor is used to measure excitation powers. The actual powers that reach the cavity are calibrated by measuring round-trip losses from the cavity. We measure approximately 10% of the light reaching the device, including the angled coupler efficiency of around 25%. However, we note that, owing to slight differences between measurements of the laser polarization and device coupling, there are probably slight discrepancies in all calibrated powers. Acousto-optic modulators (AOMs) are used to gate optical pulses for pulsed measurements. Two AOMs are used in series for the probe laser, giving an extinction of about 100 dB. The light is sent to the device by means of an optical circulator (Precision Micro-Optics) and focused onto the angled coupler with an aspheric lens doublet, which is mounted on a three-axis piezo nanopositioner stack (Attocube) for fine alignment. The device itself is mounted on the mixing chamber plate of a Bluefors dilution refrigerator with a base temperature of around 40 mK with no external magnetic field applied. The reflected signal
from the circulator is sent to a superconducting nanowire single-photon detector (SNSPD) held at 900 mK and photon counts are time tagged with a Swabian Time Tagger 20. A gating AOM is used before the SNSPD to selectively attenuate the intense reflected input pulses. The coherence measurements of the cavity emission were taken by splitting off part of the input laser as a local oscillator to beat with the emission50. The beat signal was subsequently detected by the SNSPD and Fourier transformed to obtain the power spectra. All of the radiofrequency drives used to drive the AOMs were phase synchronized. To maximize the signal-to-noise ratio, it is desirable to integrate for a long time. However, long integration time requires phase stability of all parts of the experiment, particularly the fibres. Owing to this, we found that an integration time of 1 s provides sufficient signal-to-noise ratio while maintaining the phase stability. To further improve the signal-to-noise ratio, we repeatedly integrated the signal for 1 s and averaged the power spectra. An example of the power spectra is shown in Fig. 4c, inset, in which the beating frequency is around 408 MHz, given our chosen frequency difference between our probe and the local oscillator.
Theoretical model
To model our system, we first consider each ion as a two-level system (|e⟩ and |g⟩, as labelled in Extended Data Fig.2a) and consider the TavisCummings Hamiltonian in the laser frame40:
∑∑
H ∆ a a ∆σ g a σ σ a
i κA a a
= +1
2 + ( +)
− ( −)
(2)
j
N
jj
z
j
N
c jj
†
=1 =1
†− +
c in
†
Here a is the bosonic cavity field operator, σj
± and σj
z are the spin ladder operators and the Pauli Z operators describing the atomic coherence and inversion of the jth ion, respectively. Δc is the cavity-laser detuning, Δj is the jth ion-laser detuning, g is the ion–cavity coupling rate and κc Ain is the excitation field strength that enters the cavity, in
which κc is the input coupling rate and A = P
ħω
in in is related to the input laser power Pin at frequency ω. Note that here we consider homogeneous g for simplicity; see Supplementary Information for a discussion on inhomogeneous g. To model the cavity reflection spectrum and CIT, we use the above Hamiltonian and derive the equations of motion fora, σj
− and σj
z in the Heisenberg picture:

 

∑
a ̇ = − i∆ + κ2 a − ig σ − κ2 μ (3)
j
N
cj =1
−
σ ̇ = −(i∆ + γ)σ + igσ a (4)
j jj j
− −z
σ = 2ig (a σ − σ a) − γ (1 + σ ) (5)
j
z
jj j
†− + z s
̇
in which we have introduced the corresponding dissipation terms of the operators, cavity decay rate κ, total atomic decoherence rate γ and
spontaneous emission rate γs. We further use μ ≈ κ A
κ
4
in
c2
2 , which is the cavity mean photon number in the absence of ions, representing the rescaled driving laser power (Supplementary Information). Meanwhile, for modelling the dynamics, we introduce the dissipative mechanisms through the Lindblad operators:
= κ aρ a − 1 a aρ ρ a a
2 −1
2 (6)
cav t
†† tt
†

 

L
=γ ∑ σ ρσ − 1σ σ ρ ρσ σ
2 −1
2 (7)
j
N
em s =1 j j j j j j
− t
+ +− tt
+−
L
 



 Article
L = γ ∑ (σ ρ σ − ρ ) (8)
j
N
j
z j
z
deph d =1 t t
in which Lcav is the cavity dissipation, Lem is the local spontaneous emission, deph
L is the local dephasing and ρt is the total density operator consisting of the cavity field and the atoms. As we are in the bad cavity regime in which κ is much larger than all of the other system rates, the cavity mode is adiabatically eliminated, which changes cav
L to:
= Γ J ρJ − 1 J J ρ ρJ J
2 −1
2 (9)
col c
− + +− +−

 

L
in which J = ∑ j σ
N j
±
=1
± is the collective atomic coherence and Γc = 4g2/κ is the Purcell-enhanced decay rate of a single ion. Similarly, the cavity mode is eliminated from the Hamiltonian (Supplementary Information), giving:
∑∑
H ≈ 1 ∆ σ gμ σ σ
2 − ( + ) (10)
j
N
jj
z
j
N
at j j =1 =1
+−
Lem and Ldeph can be reduced to the many-body atomic density operator ρ, obtained by taking the trace over the cavity field subspace. Using these, we solve the following master equation:
ρ = −i [H , ρ] + L + L + L (11)
at col em deph
̇
Derivation of the analytical expression for CIT Using the input–output formalism, A = κ a + A
out c in, we first obtain the cavity reflection
RA
A
κ
= = κ2 μ a + 1 (12)
out
in
2 c
2
To get a neat analytical expression, we first assume a Lorentzian distribution of ions and also make the following assumptions: High cooperativity:
C ≫ 1 (13a)
Intermediate power:
∆ g
γ
γ μ γγ
g
4 4 (13b)
inh
2
ss 2
≫≫
 
 
Appreciable inhomogeneity and good coherence:
≫
∆
γ C (13c)
inh
With the above conditions, equations (3)–(5) are solved in the steady state. We find that the cavity reflection R as a function of laser frequency ωL near the centre of the ensemble ω0 has a Lorentzian profile:
()
RA
ωω
=1−
+ ( − ) (14)
∆ 2
2
L0
2
CIT
in which ( ) ( )
A= −
κ κ
∆ C
C∆ ∆
κ κ
2
c inh CIT inh
c and C = Ng
κ∆
42
inh (Supplementary Infor
mation) and
 
 
∆∆
CC
=1
1 − (15)
γγ gμ
CIT
inh
4
s 2
The Lorentzian dip given by equation (14) is the observed CIT dip, with width ΔCIT. We further define the normalized depth ηCIT
()
()
ηA
η
C γγ
gμ
κ
κ C γγ
gμ
=
=1
1− 1− 4 − 1− 4
(16)
∆
κ κ
CIT
2
2
bare
s 2
cs 2
2
CIT
c


 








 
which is the amplitude of this Lorentzian dip normalized by the bare
cavity depth ( )
η =1− 1− κ
bare κ
2 c 2 . In the limit of high power (μ), ηCIT approaches 1, at which the absolute reflectivity will ultimately be limited by the bare cavity reflectivity. Hence, if the cavity is critically coupled ( = 0.5
κ κ
c ), zero reflection or full transparency can be realized. Although the analytical expressions above give the intuition behind CIT (Supplementary Information), an arbitrary distribution can be numerically solved without making the assumptions listed in equations (13a), (13b) and (13c), which is how the results in Fig. 2c are obtained. This gives CIT widths closer to the experimental values. Note that the power used in the simulation in Fig. 2c is four times smaller than that in the experiment in Fig. 2b, which is attributed to discrepancy of the realistic distribution of ions and power-calibration errors in the experiment. Specifically, we found that making the simulated ion distribution imperfect or asymmetric resulted in requiring more power to effectively reach the high-power regime, at which the CIT width reaches its minimum.
Master equation simulations of dynamics
For modelling the dynamics, we solve the master equation in equation (11) using QuTIP (Supplementary Information). However, the full master equation simulation of our large ensemble is intractable. To this end, we make use of the fact that, in this bad cavity limit, the cavity dissipation turns into collective emission proportional to Γc as in equation (9). Here Γc describes the cavity-mediated collective dissipation rate among ions, defining an effective spectral bandwidth within which the ions are considered to be indistinguishable (Supplementary Information). Hence we simulate a mesoscopic, homogeneous ensemble to aid in the qualitative understanding of our system dynamics. In simulating our system, we must first establish a connection between experimental measurements and simulatable quantities. We note that the peak counts reflect the cavity population at the end of the excitation pulse (Supplementary Information). In the fast-cavity regime, and in the absence of an input field, the cavity population depends on the atomic states as ⟨ a†a⟩ = Γc⟨ J+J−⟩, in which ⟨ J+J−⟩ can be written as:
∑∑
J J = σ σ + σ σ . (17)
i
N
ii ij
N
ij
+−
=1
+−
Individual
≠
+−
Correlation
Here the first term is the sum of the emissions of individual ions and the second term represents the correlation between different ions. We simulate different parts in equation(17) with a toy model of six identical ions with experimental coupling and dissipation rates (Extended Data Fig. 5a). The trend of ⟨ J+J−⟩ indeed qualitatively matches the experimental observations for regimes I and II. The initial increase of ⟨ J+J−⟩ is because of the build-up of positive correlations, or superradiance. With higher power, the correlations decrease, owing to an increase of population in the subradiant subspace. This is substantiated by the evolution of the population in the superradiant and subradiant subspaces with power (Extended Data Fig. 5b,c). We note that an increase


 then decrease of emission can be associated with the saturation of the coherence, also seen with just a single emitter. However, we find that the underlying mechanism for our observation with dense, inhomogeneous emitters is fundamentally different from the above phenomenon (see Supplementary Information for details).
Modelling regime III
Although the modelling of a small, homogeneous ensemble qualitatively captures the experimental behaviour in regimes I and II (Extended Data Fig.5a), regime III cannot be modelled in this way. To this end, we include some frequency inhomogeneity to our model to capture the fact that, as we increase power, we increase our excitation bandwidth and thus excite more ions detuned from the laser. To incorporate more ions in our simulation, we first exploit the permutational symmetry of identical particles using the Permutational Invariant Quantum Solver (PIQS; Supplementary Information) to decrease our computation time, allowing upwards of 30 identical ions to be readily simulated. Also, to incorporate inhomogeneity, we would ideally like to approximate sufficiently detuned ions as separate ensembles whose contribution to the cavity population ⟨a†a⟩ can be incoherently summed. To this end, we compare two cases with seven ions in Extended Data Fig.6. One case is simulating the full system of seven ions, with two ions detuned by 5 MHz. Another case is the incoherent addition of five ions on resonance and two ions detuned by 5 MHz, in which each system is solved separately and the peak emission summed afterwards. Although there is an offset in the values of the peak emission at certain powers, the qualitative behaviour remains the same. Combining the above two assumptions, we simulate an inhomogeneous ensemble of ions following a Lorentzian distribution. We indeed qualitatively reproduce the experimentally observed behaviour in regime III, in which the excitation of off-resonant ions leads to the increase of peak emission at high powers, giving rise to the nonlinear S-shaped profile.
Data fits
CIT widths and depths. As the distribution of ions in our experimental system is approximately Lorentzian, based on equations(15) and (16), we use the following functions to fit the power-dependent CIT width and the depth:
∆p
= 1 − (18)
p P
CIT, fit
1 2
η pp
Pp p
P
= 1 − − 1 − (19)
CIT,fit 4
2 3
2
2




 




in which p1,2,3,4 are free-fitting parameters and P is the excitation power. The fit parameters are left floating, as the purpose of these fits is to validate the analytically derived power scaling, which contains some approximations that may make it inexact in certain regimes. This is already apparent in the discrepancy of the minimum CIT width, at which the analytical value is a few times smaller than the experimental and numerically simulated values. Regardless, we find that the extracted fit parameters from Fig. 2d and Extended Data Fig.8 are physically reasonable based on our system parameters, for both the A and I transitions. First, p1, representing the minimum CIT width, is fit to 42(36) MHz for the A(I) transitions. p2, the prefactor to the excitation power, is fit to 0.08(0.25), for which the larger value for the I transition reflects both the larger cooperativity
and the dephasing. The analytical expression of p2 is C ħωγ γκ
gκ
s2
2c
and,
substituting the system parameters, we obtain about 0.07(1.4), accounting for optical losses and the factor of 4 discrepancy found in the numerical simulations. We attribute the discrepancy of p2 for the I
transition to an overestimation of the dephasing rate, which we assumed to be a hundred times worse than the A transition. p3 is the extracted fit for the cavity in-coupling ratio κc/κ, fit to 0.3(0.1), a good match to the estimated value of κc/κ ≈ 0.2 measured in similar devices. Correspondingly, p4 is fit to 1.2(1.1), consistent with its analytical expression κ κ
1
(1 − / )
c.
We note that the measured CIT depths in Fig. 2d and Extended Data Fig. 8 are normalized against the bare cavity depth, determined by κc. For the experiment data, we set the cavity resonance minimum to be 0 (which we take to be the minimum of the edge of the DIR, as the cavity is broad) and the DIR maximum to be 1. This is done to eliminate the background counts of reflected light that do not enter the cavity.
Decay fits. To characterize the power-dependent, non-single exponential decay profiles in Fig. 3, we use the following phenomenological stretched bi-exponential fit:
y(t) = A exp[−(t /τ ) ] + A exp[−(t /τ ) ] + b (20)
xx 1 12 2
12
with a fast stretched exponential decay with time constant τ1, amplitude A1 and stretch factor x1 and a slower stretched exponential decay with time constant τ2, amplitude A2, stretch factor x2 and background b (Supplementary Information). The fit parameters (Fig. 3d) reflect the distinct decay behaviours in each of the three regimes, consistent with the observations in Fig. 3b,c. In particular, we see a clear transition in the fitted decay time from superradiance to subradiance at around 20 nW of power, as there is an emergence of slow decay (τ2) and increase of τ1. Further details on the justification of the fitting function are provided in the Supplementary Information. To capture both the fast decay (which requires fine timing resolution at the nanosecond level) and the slow decay (which requires data out to hundreds of microseconds after the excitation), we use two different data-taking methodologies. To first capture the fast decay, we zoom into the first few microseconds of the decay with 1-ns resolution. This allows us to fit the decay to a stretched exponential in regimes I and II. At the same time, a separate dataset with a timing resolution of 128 ns is taken such that we can enquire to longer timescales. We use this dataset to fit the slow decay in blue. However, in regime III, as shown in Fig. 3b, the decay is smoother without a clear distinction between fast and slow decay. Because of this, we only use the 128-ns-timing-resolution dataset and force x1 = 1, as here the fast decay simply samples the fastest decay in the smooth, multiexponential profile.
Dicke states
The Dicke states can be described in the | J,M⟩ basis, with J = [N/2, N/2 − 1,...] ( J ≥ 0) and M = [−J, −J + 1,..., J], in which M is the projection quantum number associated with the number of atomic excitations (Fig. 1c). The states with maximum J are symmetric under permutation of atoms, forming the so-called superradiant ladder. Decays between states with the same J (Extended Data Fig. 4a) are all collectively enhanced beyond Γc and, in particular, we call such decays within the superradiant ladder superradiance. Meanwhile, any process that does not conserve J is forbidden by symmetry to occur collectively and must occur through individual dissipation, such as spontaneous emission (Extended Data Fig. 4b,d,e) or dephasing51 (Extended Data Fig. 4c,f). Because the system starts in the ground state and the coherent laser drives the system up the superradiant ladder, the states with J < N/2, which form the subradiant subspace, can only be populated through decoherence. In particular, the states | J,−J⟩ in the subradiant subspace cannot collectively decay and thus are the long-lived dark subradiant states. Here we also clarify our reasoning for the nomenclature used for the Dicke states. The superradiant ladder consists of the states with J = N/2 and decays between them are all superradiant. Technically, Dicke defined the J = N/2, M = 0 state to be the superradiant state 11. However,


 Article
for our purposes, we consider all of the enhanced, coherent decays within the ladder to be superradiant, as they are enhanced beyond the single-atom decay. Meanwhile, the subradiant subspace is defined as the space formed by the rest of the states, as such states cannot be driven collectively with a coherent drive. We note that decays within the subradiant subspace are not always slower than Γc. In fact, all of the decays within the same J are faster than Γc, even in the subradiant subspace, as shown in Extended Data Fig. 4a for J ≤ 2. Strictly speaking, subradiance is defined as inhibition of emission owing to the destructive interference among indistinguishable emitters. By this definition, subradiant decay is forbidden and cannot be observed. However, there are some processes that can break subradiance for us to observe that there was suppression of decay. Hence, the experimentally observed slow decay is because of dephasing and individual spontaneous emission processes from the dark subradiant states ( J < N/2, M = −J). For simplicity, in the main text, we refer to this decay as subradiant decay or subradiance, as they provide evidence of subradiance.
Data availability
The data that support the findings of this study are available from the corresponding authors on reasonable request.
49. Bartholomew, J. G. et al. On-chip coherent microwave-to-optical transduction mediated by ytterbium in YVO4. Nat. Commun. 11, 3266 (2020).
50. Shcherbatenko, M. et al. Potential of a superconducting photon counter for heterodyne detection at the telecommunication wavelength. Opt. Express 24, 30474–30484 (2016). 51. Zhang, Y., Zhang, Y.-X. & Mølmer, K. Monte-Carlo simulations of superradiant lasing. New J. Phys. 20, 112001 (2018).
Acknowledgements We thank A. Ruskuc, T. Xie, C.-J. Wu, O. Vendrell and R. Finkelstein for discussion. This work was supported by the US Department of Energy, Office of Science, National Quantum Information Science Research Centers, Co-design Center for Quantum Advantage (contract number DE-SC0012704), Institute for Quantum Information and Matter, an NSF Physics Frontiers Center (PHY-1733907) with support from the Moore Foundation and by the Office of Naval Research awards no. N00014-19-1-2182 and N00014-22-1-2422 and the Army Research Office MURI programme (W911NF2010136). The device nanofabrication was performed in the Kavli Nanoscience Institute at the California Institute of Technology. M.L. acknowledges the support from the Eddleman Graduate Fellowship. R.F. acknowledges the support from the JASSO Graduate Scholarship. J.R. acknowledges the support from the Natural Sciences and Engineering Research Council of Canada (NSERC) (PGSD3-502844-2017). J.C. acknowledges support from the IQIM Postdoctoral Fellowship.
Author contributions A.F. conceived the experiment. M.L. and R.F. built the experimental set-up, performed the measurements and analysed the data. J.R. fabricated the device. M.L., R.F., B.Z., M.E., J.C. and A.F. interpreted the results. M.L., R.F., J.C. and A.F. wrote the manuscript, with input from all authors. All work was supervised by J.C. and A.F.
Competing interests The authors declare no competing interests.
Additional information
Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41586-023-05884-1.
Correspondence and requests for materials should be addressed to Joonhee Choi or Andrei Faraon. Peer review information Nature thanks the anonymous reviewers for their contribution to the peer review of this work. Peer reviewer reports are available. Reprints and permissions information is available at http://www.nature.com/reprints.


 Laser A
Laser C
Wavemeter
Locking
Locking
1 2
3 40mK
900mK
PM
Beamsplitter
Polarization controller
Power meter
Acousto-optic modulator (AOM)
Variable attenuator
Circulator
PM
RF SW TTL AWG
AOM Driving
RF SW RF Switch
Signal generator
Superconducting nanowire single photon detector (SNSPD)
AWG Waveform
generator On-chip device
Burn
Probe
Local oscillator
a
b
Extended Data Fig. 1 | Experimental setup. a, Laser A addresses the A
transition. Optical pulses are generated using AOMs, which are driven with gated radiofrequency sources. Part of it can be split off for use as a local oscillator for heterodyne measurements. A second laser, laser C, can be used to
perform optical hole burning on the C transition. The combined light is sent through a circulator, to the device and the reflected light is sent to a SNSPD for time-resolved photon counting. b, Scanning electron microscopy image of the device.


 Article
AE I
984 nm
AE I
~GHz
~GHz
171Yb3+:YVO4
2F5/2(0)
2F7/2(0)
AE
I
ab
c
Extended Data Fig. 2 | Cavity–ion coupling. a, Energy-level spectrum of 171Yb3+:YVO4 at zero external magnetic field. The optical transitions whose polarizations are along the cavity mode are shown in blue (A, E, I). Because the three transitions are separated by an amount on the order of GHz, larger than the inhomogeneous broadening, each transition is spectrally well resolved and can be regarded as an isolated, effective two-level system; for example, the levels labelled |e⟩ and |g⟩ form a two-level system for the A transition. b, Schematic showing the relative population of ions in each transition, in which the I transition has double the population owing to a doubly degenerate ground state. c, Cavity reflection spectrum at weak laser power shows three DIR peaks corresponding to the A, E and I transitions. The peak corresponding to A is marked with orange, as we focus on this transition in the main text.


 0.2 0.4 0.6 0.8 1 1.2 1.4 /2π (kHz)
3.5
4
4.5
5
5.5
CIT width (kHz)
-10 -5 0 5 10 Laser detuning (kHz)
0.4
0.6
0.8
1
Cavity reflection
a
b
Extended Data Fig. 3 | Numerical simulation under the mean-field approximation of cavity reflection for a system with higher cooperativity. a, Simulated cavity reflection showing narrow CIT for Δinh/(2πC) = 1 kHz and γ/2π = 0.3 kHz. b, CIT width with varying γ in this high-cooperativity system, showing a strong dependence on γ. See Supplementary Information for simulation details.


 Article
0.8γd
Collective decay (|J,M> → |J,M-1>)
6Γc
10Γc
12Γc
4Γc
6Γc 2Γc
2Γc
6Γc
12Γc
4Γc
10Γc
6Γc
J
M
3210
3
2
1
0
-1
-2
-3
5γs
J
M
3210
3
2
1
0
-1
-2
-3
Individual decay (|J,M> → |J-1,M-1>)
3.3γs
2γs
1γs
0.3γs
3.6γs
1.8γs
0.6γs
1.7γs
0.8γd
J
M
3210
3
2
1
0
-1
-2
-3
Individual dephasing (|J,M> → |J-1,M>)
1.3γd
1.5γd
1.3γd
0.9γd
1.2γd
0.9γd
0.8γd
Individual decay (|J,M> → |J,M-1>)
J
M
3210
3
2
1
0
-1
-2
-3 J
M
3210
3
2
1
0
-1
-2
-3
Individual decay (|J,M> → |J+1,M-1>)
0.07γs
0.2γs
0.4γs
0.7γs
0.3γs
1γs
2γs
J
M
3210
3
2
1
0
-1
-2
-3
Individual dephasing (|J,M> → |J+1,M>)
3γs
1γs
abc
def
1γs
2γs
2γs
2γs
2γs
1γs
1γs
2γs
2γs
1γs
2γs
2γs
0.2γd
0.2γd
0.3γd
0.6γd
0.3γd
0.5γd
0.7γd
0.5γd
1.5γd
Extended Data Fig. 4 | Decay rates between Dicke states in a bad cavity regime. Here Dicke states are formed by six identical two-level systems. a, Collective decay (red) governed by Γc = 4g2/κ decays vertically, preserving total spin J. b,d,e, Individual decay (green) governed by spontaneous emission
γs decays diagonally. c,f, Individual dephasing (beige) γd couples neighbouring J states with the same M. With higher M, the diagonal decay rates are faster towards larger J and slower towards smaller J.


 0.5 1 2
Power (arb)
a
b
c
Extended Data Fig. 5 | Master equation simulation of dissipative
many-body dynamics. a, Simulation of six identical ions excited with a long (50-μs) pulse. The peak of total squared atomic polarization ⟨ J+J−⟩ (red) is plotted as a function of excitation power along with individual (blue) and correlation (orange) terms from equation (17), in which the peak amplitudes are calculated from the values immediately after the excitation pulse, to emulate the peak counts measurements. b, Simulated population dynamics of different subspaces in the Dicke basis as a function of excitation power. Note that the superradiant ladder here refers to all of the states in the J = 3 manifold except the ground state. We find that the evolution of the superradiant population with power aligns with the correlation term in a. c, Simulated Dicke state population distribution for different powers. The size of the black circles represents the relative population weights at the end of the excitation pulse. With low power (power = 0.5 AU, left), primarily the lower excitation superradiant ladder (orange bars) is populated. With increased power (power = 1 AU, middle), the subradiant subspace (blue bars) begins to populate, including the long-lived dark subradiant states. At high power (power = 2 AU, right), the system approaches a completely mixed state. Here the population distribution seems to be unequal among the Dicke states owing to the varying degeneracies of the states in the subradiant subspace.


 Article
Extended Data Fig. 6 | Comparison of simulated uncoupled and coupled ensembles. Master equation simulation of the peak counts with power for a single homogeneous ensemble of five ions (red), two coupled subensembles of five ions at 0 MHz and two ions detuned by 5 MHz (blue) and two uncoupled subensembles of five ions at 0 MHz and two ions detuned by 5 MHz (orange). Here uncoupled refers to the fact that the peak emission is simulated separately for the subensembles of five and two ions and later added together. Note that the peak emission reflects the cavity population ⟨a†a⟩ (Methods). The qualitatively similar behaviour of the uncoupled and coupled subensemble cases motivates the simulation of an inhomogeneous ensemble by means of incoherent addition of many uncoupled smaller subensembles in Fig. 3e.


 ab c
Detuning (MHz)
Peak (kcts) Detuning (MHz)
0 20 40 Power (nW)
-20
-10
0
10
20
5
10
15
20
0 20 40 Power (nW)
0
10
20
Peak (kcts)
±0
±5
±10
-10 0 10 Detuning (MHz)
11
13
15
Max peak (kcts)
Extended Data Fig. 7 | Frequency and power dependence of peak counts. a, Peak counts with excitation power and laser detuning. We repeat the pulsed excitation measurement at different frequencies along the inhomogeneous line in the A transition and observe that the S-curve shifts to higher power. b, Horizontal cuts of a at different detunings. Dashed red line indicates the maximum peak counts for different detunings. c, Extracted local maximum of peak counts as a function of laser detuning. The maximum of peak counts decreases with increased detuning from the centre. We note that this
behaviour differs from Fig. 4b, in which the S-curve also shifted towards higher powers and the maximum of peak counts increased with laser detuning. Here the S-curve shifts towards higher powers because of the CIT profile; as the laser is detuned from the centre, less power enters the cavity, resulting in effectively more power being required to excite the ions. At the same time, the decrease of the maximum of peak counts indicates that there are less ions resonant with the laser when detuned from the centre.


 Article
a
b
Extended Data Fig. 8 | CIT width and depth comparison between the A and I transitions. Measured CIT width (a) and depth (b) with power and corresponding fits for the A (red) and I (blue) transitions. We expect the I transition to have different width and depth values, as the cooperativity is twice as high, but the dephasing rate is expected to be more than 100 times larger than A. Although we find similar depth values, the width differs between the two. In particular, the I transition starts out much broader than A, as expected from the worse coherence properties. Despite this, the minimum width is slightly narrower for the I transition, indicating that indeed the cooperativity is larger for the I transition. Further discussion of the fit parameters is in Methods.


 -1.5 -1 -0.5 0 0.5 1 1.5 Detuning (GHz)
0.4
0.6
0.8
1
Reflection
0.5π
π
1.5π
Phase of cavity field
Extended Data Fig. 9 | Numerical simulation of the cavity phase across the CIT. The simulated cavity phase arg(a) (red) across the CIT for a laser power of 0.5 nW, exhibiting a relative π phase shift. The corresponding cavity reflection spectrum (blue) as a function of laser frequency for reference, identical to Fig. 2c, purple line.


 Article
ab
Fit to 0.6 μs
0 123 Time (μs)
0.2
0.4
0.6
0.8
1
1.2
Reflection
Pump off
Pump on
Reflection (Port 1)
Transmission (Port 2)
Transmission (Port 2)
Reflection (Port 1)
Pump on
Reflection Input
Input
Extended Data Fig. 10 | Optical switch based on CIT. a, CIT response time. We park the laser at the centre of the CIT and measure the reflection as a function of time after turning the pump on. The reflection signal decreases as the CIT is created in sub-μs timescales. b, Schematic of an ideal two-port optical switch with an integrated filter with CIT. A transmission port and a transverse pump port are added to realize this application. For the best extinction ratio, the
cavity should be two-sided and critically coupled such that κ1/κ = κ2/κ = 0.5, in which κ1 and κ2 are the coupling rates from ports 1 and 2, respectively. The top schematic shows that when the pump is off and DIR is formed, the signal is entirely reflected (port 1). The bottom schematic shows that, when the pump is on and CIT is created, the signal is transmitted (port 2) within the CIT window (spectral filter). See Supplementary Information for a more detailed discussion.
