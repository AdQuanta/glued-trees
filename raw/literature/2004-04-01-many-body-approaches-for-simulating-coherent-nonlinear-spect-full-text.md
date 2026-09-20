# Many-Body Approaches for Simulating Coherent Nonlinear Spectroscopies of Electronic and Vibrational Excitons - Full Text

> Source: https://pubs.acs.org/doi/10.1021/cr020681b
> Collected: 2026-09-20
> Published: 2004-04-01
> Zotero parent key: 42YX2IZQ
> Evidence: Zotero indexed PDF text

Many-Body Approaches for Simulating Coherent Nonlinear Spectroscopies of Electronic and Vibrational Excitons
Shaul Mukamel* and Darius Abramavicius
Department of Chemistry, University of California, Irvine, California 92697
Received September 19, 2003
Contents
1. Introduction 2073 2. The Nonlinear Optical Response 2076 3. Coherent Multidimensional Signals 2077 4. The Fluctuating Exciton Hamiltonian for Molecular Aggregates
2078
5. The Cumulant Expansion for Gaussian Fluctuations (CGF)
2080
5.1. Diagonal (Energy) Fluctuations 2080 5.2. Off-Diagonal Fluctuations and Exciton Transport
2082
5.3. Numerical Simulations 2083 6. The Nonlinear Exciton Equations (NEE) 2085 6.1. Closing the Many-Body Hierarchy 2085 6.1.1. The Local Field Factorization 2086 6.1.2. Pure State Factorization 2087 6.1.3. Exciton Population Factorization 2087 6.2. The Relaxation Terms 2087 6.3. Numerical Integration of the NEE; Selecting the Desired Signal
2088
7. Discussion 2089 8. Acknowledgments 2091 9. Appendix A. The Generalized Frenkel Exciton Hamiltonian
2091
10. Appendix B. Mapping Molecular Aggregates onto the Fluctuating Multilevel Model
2092
11. Appendix C: The Master Equation for Incoherent Exciton Hopping
2093
12. Appendix D: The Doorway and the Window Functions
2093
13. Appendix E: The NEE Matrix 2094 14. Appendix F: Derivation of the Relaxation Matrices
2094
15. Appendix G: Relaxation Rates for the Overdamped Brownian Oscillator Spectral Density
2096
16. References 2096
1. Introduction
Many important molecular systems are made out of assemblies of coupled localized chromophores. Examples are molecular crystals,1-3 J aggregates,4-8 biological light-harvesting complexes,9-16 organic nanostructures,17 and supramolecular structures.18-23 The description of elementary electronic excitations of
such systems is greatly simplified when the chromophores have non-overlapping charge distributions. The excitations are then known as Frenkel excitons, and their localization and energy-transfer dynamics have been extensively studied using the Frenkel exciton Hamiltonian,1,2,3,24-31 whose parameters may be obtained from electronic structure calculations performed on the individual chromophores;32 the global electronic excitations of the system are computed by diagonalizing the exciton Hamiltonian, which is a much simpler task than the direct manyelectron simulation of the entire assembly. The Wannier exciton model of semiconductors33-35 is an extension of the Frenkel exciton model and shares the same type of simplifications. The exciton model may also be applied to vibrational excitations of coupled localized vibrations of oligomers or polymers made out of similar repeat units,36-38 e.g. the amide bands of peptides.39-43 In this case we need to examine the transition charge densities: the derivatives of the charge density distribution with respect to various localized vibrations.43 When these charge densities do not overlap, the coupling between local modes is electrostatic, and the coupling coefficients become simple functions of the atomic coordinates.44-46 Vibrational excitons are also denoted vibrons. The exciton model may also be used when the charge (or transition charge density) distributions weakly overlap. The calculation of electronic or vibrational couplings then requires a higher level of theory, which includes exchange. These are denoted through-bond as opposed to through-space (electrostatic) couplings. Ab initio simulations suggest that through-bond effects contribute to the nearestneighbor coupling of amide I modes.43,47,48 Optical spectroscopy is a powerful tool for the study of vibrations and electronic excitations of molecules. Linear spectra of excitonic systems often consist of a few broadened features that result from the interplay of numerous factors: intermolecular couplings, exciton localization, disorder, and coupling to phonons. It is impossible to pinpoint these various factors unambiguously using the limited information provided by absorption line shapes. As an example, let us consider the vibrational spectra of the 1600-1700 cm-1 amide I band in proteins which originates from the stretching motion of the CdO peptide bond (coupled to in-phase N-H bending and C-H stretching).49 This mode has a strong transition dipole moment and is clearly distinguishable from other vibrational modes of the amino acid side chains.
* Corresponding author. Tel.: (949) 824-7600. Fax: (949) 8248571. E-mail: smukamel@uci.edu. URL: http://www.chem.uci.edu/ smukamel/.
Chem. Rev. 2004, 104, 2073−2098 2073
10.1021/cr020681b CCC: $48.50 © 2004 American Chemical Society Published on Web 04/14/2004
Downloaded via TECHNION-ISRAEL INST OF TECHNOLOGY on October 16, 2024 at 08:06:53 (UTC).
See https://pubs.acs.org/sharingguidelines for options on how to legitimately share published articles.


 Dependence of the amide I line position on a particular secondary structure is widely utilized in polypeptide and protein structure determination.50-52 However, a protein usually folds into a complex threedimensional structure, which consists of several polypeptide segments forming different types of secondary structures.49,53 This folding results in strong interactions between remote bonds39 which affect the structure of exciton states. Linear infrared
absorption spectra of peptides such as globular protein segments39,54,55 thus yield only limited information about the structure.
Nonlinear optical techniques provide considerably more detailed information on the structure and dynamics of excitations in assemblies of coupled molecular chromophores. Coherent nonlinear experiments conducted by the application of sequences of femtosecond optical pulses56-58 provide a multidimensional view of molecular structure as well as vibrational and electronic motions, interactions, and relaxation processes. Recent advances in pulse-shaping techniques which allow researchers to vary the envelopes, polarization directions, durations, and time delays, tune the frequencies, and control the phases of optical pulses59-64 have made it possible to extend concepts developed in NMR to the optical regime.57,65,66 Both NMR and laser pulse sequences may be designed to accomplish specific tasks:67,68 the spectral resolution may be improved by narrowing the line shapes in specific directions, and desired features may be enhanced by the design of elaborate pulse sequences, performing coherent superpositions of various phase-locked heterodyne techniques, and through polarization-sensitive measurements. By displaying the signals as correlation plots of various time delays,57,69-72 these techniques reveal detailed information about the microscopic dynamics of coupled localized excitations such as electronic excitations of aggregates73 or vibrational spectra of peptides.74-77 Peak intensities provide direct signatures of distances between chromophores, and their profiles probe fluctuations through the spectral density of the dynamics of the environment.78-85 Multidimensional techniques have the capacity to probe the entire pathway for vibrational relaxation86 and conformational fluctuations87 in real time in a single measurement.88,89 A broad arsenal of techniques, such as pump-probe,90,91 fluorescence depolarization,92 photonecho,83-85,93 hole-burning94-96 and fluorescence interferometry97 applied to molecular aggregates, provide an improved understanding of the exciton structure and migration.98-101 Population transfer and relaxation in the excited state are directly measured by the pump-probe102-104 and fluorescence-up conversion105 techniques. The photon-echo can selectively eliminate static inhomogeneous broadening57 in a two-level system. However, this does not apply to systems such as excitons in aggregates where multiple electronic states can be excited collectively.
Similar developments have taken place in infrared vibrational techniques. Multidimensional signals carry detailed information on the structure of proteins106,107 and molecular liquids.108-113 Femtosecond pumpprobe and dynamic hole-burning experiments have been used to investigate the vibrational relaxation and anharmonicity of the amide I vibrations in N-methylacetamide (NMA) and three small globular peptides, apamin, scyllatoxin, and bovine,81 where strong coupling to slow vibrational motions leads to exciton localization and self-trapping.
In this article we survey the theoretical approaches and key concepts needed for the design and interpretation of multidimensional spectroscopic techniques in systems of localized electronic or vibrational
Shaul Mukamel, who is currently the Chancellor Professor of Chemistry at the University of California, Irvine, received his Ph.D. in 1976 from Tel Aviv University, followed by postdoctoral appointments at MIF and the University of California at Berkeley and faculty positions at Rice University, the Weizmann Institute, and the University of Rochester. He has been the recipient of the Sloan, Dreyfus, Guggenheim, Alexander von Humboldt Senior Scientist, and the Lippincott awards. He is a fellow of the American Physical Society and of the Optical Society of America. His research interests in theoretical chemical physics and biophysics include developing a Liouville-space quasiparticle approach to femtosecond spectroscopy and to many-body theory of electronic and vibrational excitations of molecules, molecular aggregates, nanostructures, and semiconductors; designing optical and infrared pulse sequences for probing structure and folding dynamics of proteins by multidimensional coherent spectroscopies, nonlinear X-ray, and single-molecule spectroscopy; photon statistics; and electron transfer and energy funneling in photosynthetic complexes and dendrimers. He is the author of the popular textbook, Principles of Nonlinear Optical Spectroscopy (Oxford University Press, 1995).
Darius Amramavicius was born in 1974 in Alytus, Lithuania. He received his M.S. degree under the direction of Professor Leonal Valkunas from Vilnius University in 1998, and then began his Ph.D. work on the theoretical studies on charge photogeneration, transport, and recombination in organic molecular solids. He received his Ph.D. degree under the supervision of Professor Leonas Valkunas from the Institute of Physics in Vilnius, Lithuania, in 2002. He joined the group of Professor Shaul Mukamel in 2002 at the University of Rochester (New York). He moved to the University of California in Irvine in 2003, together with the group. His current research interests are in the field of theoretical physics of nonlinear optical response of molecular aggregates and peptides.
2074 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 chromophores.37,38 This complex many-body problem requires an extensive numerical effort which grows very rapidly with molecular size. In periodic systems (e.g. molecular crystals), the computational effort may be reduced to the size of the repeat unit; the physical size of the system is no longer a factor. However, molecular aggregates and biomolecules are not usually periodic. The problem becomes much more tractable by adopting an exciton Hamiltonian that conserves the number of excitations; nonconserving processes are controlled by the ratio of intermolecular couplings to the optical frequency, which is typically small in both molecular aggregates and coupled high-frequency vibrations. The energy spectrum then consists of well-separated groups of energy levels representing single excitations, double excitations, etc., and only the radiation field can change their number. By classifying the optical techniques according to their dependence on the power of the incoming fields, we find that very few types of elementary excitations need to be considered at each order. This provides a convenient computational strategy as well as a basis for an intuitive physical picture.57 The manifolds with different numbers of excitons are shown in Figure 1. The lowest (single-exciton) manifold is accessible by linear optical techniques (e.g. linear absorption), whereas doubly excited (two-exciton) states can be monitored by third-order spectroscopies. Successively higher manifolds may be probed with higher order techniques. The pattern of multiple excitations is sensitive to the aggregate structure and connectivity of the various chromophores. Femtosecond multidimensional techniques then reveal the correlations between the various chromophores and vibrational relaxation pathways,114 in complete analogy with multidimensional NMR spectroscopies.67 Population and phase relaxation processes, induced by fluctuations caused by interactions with the environment (bath), i.e. solvent or low-frequency intramolecular modes, result in line-broadening and spectral shifts and have direct signatures on multidimensional signals.57,78,115-118 We shall model these fluctuations using a multimode Brownian oscillator Hamiltonian,101,116,118,119 which can represent an arbitrary distribution of bath time scales and interpolates between the fast (homogeneous) and the slow (inhomogeneous) bath limits.120-122 We survey two approaches for computing the nonlinear optical response of excitons and relating it to bath spectral densities. The first, denoted cumulant expansion of Gaussian fluctuations (CGF), is based on closed correlation function expressions derived by
coupling the dynamical exciton variables to a harmonic bath. The resulting Gaussian fluctuations may then be incorporated using the second-order cumulant expansion. The second is based on the nonlinear exciton equations (NEE), which provide a collective oscillator, quasiparticle picture for exciton dynamics. The quasiparticle approach is commonly adopted in calculations of optical properties of the Wannier excitons in semiconductors which are based on the semiconductor Bloch equations (SBE).35,123 The NEE share some conceptual similarities with the SBE but extend them to a broader set of dynamical variables in real space (rather than in momentum, k space). The CGF and the NEE approaches make different approximations, leading to different ranges of applicability. The CGF is formulated in the eigenstate basis, and the optical response is described in terms of transitions among states. The NEE, in contrast, use a single-exciton basis and view the nonlinear response in terms of scattering among excitons (quasiparticles). The expensive computation of multiple exciton states is totally avoided. The NEE are limited to a Hamiltonian that conserves the number of excitons, whereas the CGF can accommodate any exciton Hamiltonian with arbitrary couplings.124-127 The CGF incorporates the full bath spectral densities with arbitrary distribution of time scales, whereas the NEE are limited to fast bath fluctuations which result in Markovian relaxation operators. The NEE computational effort scales more favorably with molecular size: the multiple summations and interference effects (cancellation of very large contributions) in the CGF may limit its accuracy and may complicate the analysis for extended systems.128,129 In section 2 we present a general expression for the first- and third-order nonlinear polarization in terms of nonlinear response functions and susceptibilities. The various detection modes and their relations to the nonlinear polarization in the time domain and in terms of Wigner spectrograms are reviewed in section 3. The generalized Frenkel exciton Hamiltonian of molecular aggregates composed of multilevel chromophores is presented in Appendix A. The simplified Hamiltonian used in this review is introduced in section 4. It retains only the essential (resonant) exciton couplings and includes a coupling to a bath with an arbitrary spectral density. The key ingredients and the physical picture of the response of excitons may be introduced and understood by considering a more basic fluctuating Hamiltonian model of a multilevel system coupled to a bath. The exciton system can be mapped onto this generic model by a suitable transformation, which is given in Appendix B. In section 5 we present the CGF approach for computing the optical response of a fluctuating multilevel model with primary Brownian oscillator coordinates linearly coupled to the exciton system and to a harmonic bath. General expressions are first derived for the first- and third-order polarizations of a simplified model of diagonal systembath couplings (energy fluctuations) responsible for the line broadening. The nonlinear response function is calculated using the second-order cumulant expansion, which is exact for this model. Off-diagonal couplings cause exciton transport, which is subsequently described by the doorway-window representation.
Figure 1. (a) Molecular aggregate made of three two-level chromophores. J indicates intermolecular coupling and μag is the transition dipole moment in the local basis. (b) The exciton level scheme and the transition dipoles. The oneexciton (|e1〉), two-exciton (|e2〉), and three-exciton (|e3〉) manifolds may be observed in third-order measurements.
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2075


 The alternative, equation of motion, approach to nonlinear response is presented in section 6. The NEE for an aggregate of multilevel chromophores in a local chromophore basis are presented in section 6.1, and the relaxation operators are derived in section 6.2. In section 6.3 we show how to compute signals generated in specific directions by selecting the relevant components of the polarization in the course of numerical integration of the NEE. General discussion and comparison of the CGF and NEE approaches are finally given in section 7. Details of the master equation and the relaxation kernel for exciton transport used in section 5 are given in Appendix C; Appendix D gives the doorway and window function expressions used in section 5. Closed expressions for the NEE operators are given in Appendix E. The relaxation operators derived in Appendix F, and computed using the overdamped Brownian oscillator spectral density for the bath are given in Appendix G.
2. The Nonlinear Optical Response
The interaction of a molecule located at r with an optical field E(r,t) is given by Hˆ int ) -Pˆ ‚E(r,t), where Pˆ is a polarization operator. We are using the dipole approximation, which holds provided the molecule is small compared with the wavelength of the relevant optical transitions. The molecular response to the optical field is described by the induced polarization:57
where Fˆ(t) is the density matrix describing the state of the molecule and Tr(...) denotes the trace. When the optical field is much weaker than the Coulomb fields between electrons and nuclei within the molecule, the interaction with the optical field may be taken into account perturbatively, whereby the density matrix is expanded as57,130,131
where the superscript n denotes the order in the field, and the nth-order polarization is then defined as
The density matrix is obtained by solving the Liouville equation
where the total Hamiltonian is ˆH ) Hˆ 0 + Hˆ int, Hˆ 0 being the Hamiltonian of molecule and its environment. The polarization may generally be expanded in the form57
Here, S(n)(tn,tn-1,...,t1) denotes the nth-order response function and tn ≡ τn+1 - τn is the time delay between
two consecutive interactions with the optical field (see Figure 2). The response function is given by the following expression in Liouville space:57
Here,
is the Green function of the Liouville equation corresponding to molecular Hamiltonian H, where the Liouville operator is defined by its action on an arbitrary operator A, L A ≡ [Hˆ 0,A], and θ(t) is the Heavyside step function (θ(t) ) 0 for t < 0 and θ(t) ) 1 for t g 0). The polarization superoperators are defined as
The first-order polarization is expressed in terms of the linear response function S(1):
where Greek subscripts R ) x, y, z denote cartesian components and Sσ,R
(1) is a second-rank tensor. Since the second-order response vanishes for centrosymmetric systems,130,132 the lowest order nonlinear response in solution is third order. The corresponding response function is similarly given by a fourth-rank tensor:
Figure 2. (Upper panel) Laser pulse sequence in a threepulse, four-wave mixing experiment. Three pulses, k1, k2, and k3, create the nonlinear polarization in the sample, which generates the new optical field in the direction ks ) (ks ( ks ( ks. k4 ) ks is the heterodyne field. (Lower panel) The peak ordering and time variables.
S(n)(tn,tn-1,...,t1) )
in Tr[P+G (tn)P-G (tn-1)P- ... G (t1)P-Fˆ(-∞)] (2.6)
G (t) ) θ(t) exp(-iL t) (2.7)
P-A ≡ Pˆ A - A Pˆ
P+A ≡ 1
2(Pˆ A + A Pˆ ) (2.8)
Pσ
(1)(r,t) ) ∑R
∫
0
∞ dt1Sσ,R
(1) (t1)ER(r,t - t1) (2.9)
Pσ
(3)(r,t) ) R∑‚γ
∫∫∫0
∞ dt3 dt2 dt1 Sσ,γ‚R
(3) (t3,t2,t1) ×
Eγ(r,t - t3)E‚(r,t - t3 - t2) ER(r,t - t3 - t2 - t1) (2.10)
P(r,t) ≡ 〈Pˆ 〉 ) Tr(Pˆ Fˆ(t)) (2.1)
Fˆ(t) ) Fˆ(0)(t) + Fˆ(1)(t) + Fˆ(2)(t) + Fˆ(3)(t) + ... (2.2)
P(n)(r,t) ) Tr(Pˆ Fˆ(n)(t)) (2.3)
dFˆ
dt ) -i[Hˆ , Fˆ] (2.4)
P(n)(r,t) ) ∫0
∞ dtn ∫0
∞ dtn-1 ... ∫0
∞dt1
S(n)(tn,tn-1,...,t1)E(r,t - tn)E(r,t - tn - tn-1) ... E(r,t - tn - tn-1 ... - t1) (2.5)
2076 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 Alternatively, the polarization may be expressed in the frequency domain using the linear and the third-order susceptibility tensors,  ̄σ,R
(1) (-ωa;ωa) ≡
 ̄σ,R
(1) (ωa) and  ̄σ,R‚γ
(3) (-ωs;ωa,ωb,ωc):
ER(r,ωa) is the optical field in the frequency domain:
The response functions and the nonlinear susceptibilities are related by a Fourier transform:
where ωs ≡ ωa + ωb + ωc and the sum ∑p runs over all 3! ) 6 permutations of ωa,ωb,ωc.57 For clarity we shall hereafter omit the tensor notation.
3. Coherent Multidimensional Signals
We consider the molecular response to a sequence of laser pulses (Figure 2), whose electric field is given by
Here, E ̃ jR(t) is the slowly varying complex envelope function of pulse j with polarization R (R ) x,y,z) centered at time thj, with carrier frequency jωj and wavevector kj. c.c. denotes the complex conjugate. Most generally, a third-order process requires four external fields: three (j ) 1, 2, 3) interact with the system, and the fourth, heterodyne, field (j ) 4) is used for the detection. In the frequency domain (see eq 2.13), eq 3.1 reads
where E ̃ jR(ω) exp(iφjR(ω)) is a Fourier transform of the
envelope E ̃ jR(t). The envelope function, E ̃ jR(ω - jωj), and its phase, φjR, are taken to be real.
The nonlinear polarization is the most general optical observable, since heterodyne detection can measure separately the real and the imaginary parts of the complex polarization. We next survey various detection methods.
To connect the nonlinear polarization with experiment, we first expand it in k space:
where the possible wavevectors of the induced polarization are ks ) ( k1 ( k2 ( k3. The signal generally depends on many parameters, jωj, jτj, kj, as well as the entire amplitude, E ̃ jR(ω), and phase, φjR(ω), profiles. Multidimensional correlation plots can thus be made by numerous choices of parameters. We shall focus on the parametric dependence of the signal on time delays tj ≡ jτj+1 - jτj. The simplest detection measures the time-integrated field intensity, and the signal is ∫-∞
+∞ |Es(t)|2 dt. Within the slowly varying amplitude approximation, the signal field is proportional to the polarization, Es(t) ∝ iPs
(n)(t),57,133 and the third-order signal in the ks direction, which depends parametrically on the two time delays (Figure 2), is given by
This is known as the information homodyne detection mode. Additional information may be obtained by time gating: the signal is focused onto a nonlinear crystal where it is mixed with an additional laser pulse to perform up-conversion. The laser pulse creates a time gate for the signal and the polarization is measured within the duration of the laser pulse. This measurement yields the absolute value of polarization Ihom(t1,t2,t3) ) |Ps
(3)(t)|2.
Heterodyne detection can select both the real and the imaginary parts of the polarization. It involves mixing the generated field Es(t) with the heterodyne field E4(t) which has the same wavevector. The signal is then given by I(t1,t2,t3) ) ∫-∞
+∞ |Es(t) + E4(t)|2 dt. The heterodyne field is much stronger than the signal field, and the |Es(t)|2 contribution can be neglected. Subtracting the intensity of the heterodyne field, the heterodyne signal is finally given by
The time resolution is now determined by the heterodyne field, and the signal depends linearly rather than quadratically on Ps
(3)(t). By choosing different phases of the heterodyne field, it is possible to measure separately the real and the imaginary parts of the polarization.
We shall also use a mixed time/frequency representation of the signal:
Pσ
(1)(r,t) ) ∑R
∫
-∞
∞ dωa exp(-iωat) ̄σ,R
(1) (ωa)ER(r,ωa)
(2.11)
Pσ
(3)(r,t) ) R∑‚γ
∫∫∫∫-∞
∞ dωs dωa dωb dωc exp(
iωst) ̄σ,R‚γ
(3) (-ωs;ωa,ωb,ωc)ER(r,ωa)E‚(r,ωb)Eγ(r,ωc)
(2.12)
ER(r,ω) ≡ ∫-∞
∞ dτ ER(r,τ) exp(iωτ) (2.13)
 ̄σ,R
(1) (ωa) ≡ ∫0
∞ dt1 Sσ,R
(1) (t1) exp(iωat1) (2.14)
 ̄σ,R‚γ
(3) (-ωs;ωa,ωb,ωc) ≡ 1
3!∑p
∫∫∫0
∞dt3 dt2 dt1 ×
Sσ,R‚γ
(3) (t3,t2,t1) exp(i(ωa + ωb + ωc)t3 + i(ωa + ωb)t2 +
iωat1) (2.15)
E(r,t) ) j) ∑1
4
∑
R
E ̃ jR(t - jτj) exp[i(kjr) - i jωjτ] + c.c.
≡ j) ∑1
4
∑
R
EjR(r,t) + c.c. (3.1)
E(r,ω) ) j) ∑1
4
∑
R
E ̃ jR(ω - jωj) exp{ikjr + i(ω - jωj)jτj +
iφjR(ω - jωj)} + c.c. (3.2)
P(3)(r,t) ) ∑s
Ps
(3)(t) exp(iksr) (3.3)
Ihom(t1,t2) ) ∫-∞
+∞|Ps
(3)(t)|2 dt (3.4)
Ihet(t1,t2,t3) ) Im∫-∞
+∞E4
/(t)Ps
(3)(t)dt (3.5)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2077


 Alternaltivelly, the time- and frequency-resolved signals and fields may be displayed using the Wigner spectrogram:133-135
The spectrogram directly shows what fraction of the field energy is contained in a given time and frequency window. Integrating over the frequencies gives the instantaneous field energy,
while integrating over the time gives the energy density spectrum,
The one-dimensional projections of the spectrogram (eqs 3.8 and 3.9) are known as marginals. We next express the heterodyne signal in the Wigner representation. Usually, the heterodyne field is a replica of one of the incoming fields in a nonlinear experiment. We expand the polarization to linear order in this field:
Defining the mixed time/frequency response function
the heterodyne signal assumes the form133,134
where W4(t,ω) is the heterodyne field spectrogram, given by eq 3.7. Equation 3.12 is exact and holds for arbitrary field envelopes. For impulsive (very short) pulses, the Wigner distribution is narrowly peaked at the time of heterodyne field jτ4, and eq 3.12 reduces to
In the other extreme of ideal frequency domain experiments, the spectrogram is narrowly peaked around its carrier frequency jω4, and
where
In the pump-probe technique, the third-order polarization originates from two interactions with the pump and one with the probe. The probe serves as the heterodyne field since the signal is measured in the probe direction. The pump-probe technique may thus be viewed as self-heterodyne detection. Using Wigner spectrograms, the pump probe signal is given
by133,134
The signal is thus expressed as an overlap integral of three functions: the pump spectrogram W1(t′,ω′), the third-order response function S(3)(t′′,ω′′,t′,ω′), and the probe spectrogram W2(t′′,w′′). In the following sections we outline methods and models for computing the polarization and the nonlinear signals of electronic and vibrational excitons.
4. The Fluctuating Exciton Hamiltonian for Molecular Aggregates
We consider a molecular aggregate made out of N interacting chromophores, each having (M + 1) levels (the ground state + M excited states). The total Hamiltonian is given by
Here the three terms represent the isolated aggregate, the interaction with the optical field, and the interaction with the environment (bath). We denote the a excited state of molecule m by |ma〉 and the ground state by |m0〉 and introduce exciton creation
Bˆ ma
† ≡ |ma〉〈m0| and annihilation Bˆ ma ≡ |m0〉〈ma| operators, where a and b ) 1, ..., M. The most general Frenkel exciton Hamiltonian for molecular aggregates is presented in Appendix A. We shall consider the following approximate form where we neglect all nonresonant terms in eqs A3-A7:
where Ωma is excitation energy of state a of chromophore m, Jma,nb is the resonant exciton coupling, and K m,n
aa,bb is the quartic coupling. This Hamiltonian conserves the number of excitons (Heitler-London approximation) since it contains only interactions between states with the same number of excitons.136 In NMR, J and K are known as strong and weak couplings, respectively.67 The dipole interaction with the optical field is
where the polarization operator P is given by
The first term describes the creation (annihilation)
Ihet(ω1,t2,ω3) )
∫
0
+∞∫0
+∞ dt1 dt3 Ihet(t1,t2,t3) exp(iω1t1 + iω3t3) (3.6)
Ws(t,ω) ) ∫-∞
+∞Es
/(t - τ/2)Es(t + τ/2) exp(iωτ) dτ
(3.7)
∫
-∞
+∞Ws(t,ω) dω ) 2π|Es(t)|2 (3.8)
∫
-∞
+∞Ws(t,ω) dt ) |Es(ω)|2 (3.9)
Ps(t) ) ∫-∞
+∞ dτ S ̃ (1)(t,τ)E4(τ) (3.10)
S ̃ (1)(t,ω) ) ∫-∞
+∞S ̃ (1)(t + τ/2,t - τ/2) exp(iωτ) dτ (3.11)
Ihet(t1,t2,t3) ) ∫-∞
+∞ dt ∫-∞
+∞ dω
2πW4(t,ω)S ̃ (1)(t,ω)
(3.12)
Ihet(t1,t2,t3) ) S ̃ (1)(jτ4,jτ4) ∝ Im{Eh
/(jτ4)Ps(jτ4)} (3.13)
Ihet(t1,t2,t3) ) S ̃ (1)( jω4, jω4) ∝ Im{Eh
/( jω4)Ps( jω4)} (3.14)
S ̃ (1)(ω1,ω2) )
∫
-∞
+∞ dτ1 dτ2S ̃ (1)(τ1,τ2) exp(iω1τ1 + iω2τ2) (3.15)
IPP( jω1,jτ1, jω2,jτ2,) ) ∫∫∫∫ dt′ dt′′ dω′ dω′′
W2(t′′,w′′)S(3)(t′′,ω′′,t′,ω′)W1(t′,ω′) (3.16)
Hˆ ) Hˆ S + Hˆ SF + Hˆ SB (4.1)
Hˆ S ) m∑a
ΩmaBˆ ma
† Bˆ ma + ma∑nb
m*n
(Jma,nbBˆ ma
† Bˆ nb +
K m,n
aa,bbBˆ ma
† Bˆ nb
† Bˆ maBˆ nb) (4.2)
Hˆ SF ) -Pˆ ·E(t) (4.3)
Pˆ ) m∑,a
μma(Bˆ ma
† + Bˆ ma) +m,∑ab
μm,abBˆ ma
† ˆBmb (4.4)
2078 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 of excitation from (to) the ground state, while the second represents transitions between excited states. μma is the transition dipole moment connecting the ground state with excited state a of molecule m, and μm,ab is the transition dipole connecting the excited states b and a of molecule m. Dipole elements involving two molecules are negligible since the molecular wave functions do not overlap. The third term in eq 4.1, ˆHSB, represents a bath and its coupling with the exciton system. In general, the bath induces fluctuations in all the Hamiltonian matrix elements, which result in decay of coherences and population redistributions. We shall adopt the displaced multimode Brownian harmonic oscillator model and assume the following form for Hˆ SB:57,137,138
The first term represents a set of harmonic Brownian oscillator degrees of freedom j with the momentum Pj, coordinate Qj, reduced mass Mj, and frequency Ωh j. These primary Brownian oscillator coordinates are linearly coupled to the system; i.e., their equilibrium is linearly displaced between excited states with the displacements given by dmanb,j. In addition, they are linearly coupled to the bath coordinates qν (with momenta pν) as described by the second term in eq 4.5, where mν is the reduced mass of the bath oscillator, jων is its frequency, and zνj is the coupling strength between the primary oscillator and bath coordinates. We shall denote the key part of ˆHSB, which is responsible for the system coupling to the Brownian oscillators, by
where
and hhmanb,j ) Mj Ωh j
2dmanb,j. The bath introduces fluctuations into the system Hamiltonian through the collective coordinates Qmanb
(c) . Diagonal interactions with the bath (Qmama
(c) ) cause fluctuations of energies, whereas off-diagonal interactions (Qmanb
(c) with a * b) modulate the couplings among excited states. The fluctuations of the collective coordinates can be characterized by the matrix of spectral densities:
where the expectation value and the time evolution are taken with respect to the bath Hamiltonian.
Equation 4.8 contains all the relevant information about the fluctuations necessary for computing the optical response of the system.137 Assuming that the primary coordinates Qj are uncorrelated, the total spectral density (eq 4.8) can be recast in the form
where
is the spectral density of the jth Brownian oscillator. The relevant bath information is contained in the spectral density:
which is given by
We shall use the Brownian oscillator spectral
density57,137-139
where
is the friction parameter and σj is a spectral shift. The two are connected by the Kramers-Kronig relation:
Assuming that γj is independent of frequency,57 we note two limiting forms of the spectral density. For small friction (γj , Ωj) the oscillator is underdamped,
and in the opposite overdamped limit (γj . Ωj),
with λj′ ) (2Mj Ωh j
2)-1 and Λj ) Ωh j
2/γj. For intermediate friction, the correlation function shows damped temporal oscillations and the spectral density has broad peaks. Nuclear solvent fluctuations are typically overdamped. Assuming a single primary coordinate (j ) 1) and substituting eq 4.17 into eq 4.9, the spectral
C′m′ anb,m′a′n′b′(ω) ) ∑j
hh manb,j hh m′a′n′b′,j Cj′′(ω) (4.9)
Cj′′(ω) ) - 1
2∫-∞
+∞ dt exp(iωt)〈[Qj(t),Qj(0)]〉 (4.10)
K′ν′(ω) ≡ - 1
2∫-∞
+∞ dt exp(iωt)〈[qν(t),qν(0)]〉 (4.11)
K′ν′(ω) ) 1
2mν jων
2π[δ(ω - jων) - δ(ω + jων)] (4.12)
Cj′′(ω) ) 1
2Mj
ωγj(ω)
(ω2 - ωσj(ω) - Ωj
2)2 + ω2γj
2(ω) (4.13)
γj(ω) ) 1
Mjω∑ν
zνj
2 K′ν′(ω) (4.14)
σj(ω) ) - 1
πPP∫-∞
+∞ dω′ γj(ω′)
ω′ - ω (4.15)
Cj′′(ω) ) 1
2Mj Ωj
2π[δ(ω - Ωj) - δ(ω + Ωj)] (4.16)
Cj′′(ω) ) 2λj′
ωΛj
ω2 + Λj
2 (4.17)
Hˆ SB ) ma ∑nb∑j [ P j
2
2Mj
+
Mj Ωh j
2
2 (Qj - dmanb,j)2] ˆBma
† ˆBnb +
∑
ν [ pν
2
2mν
+
mν jων
2
2 (qν - ∑j
zνjQj
mν jων
2)2] (4.5)
Hˆ ′SB ≡ ma∑nb
Qmanb
(c) Bˆ ma
† Bˆ nb (4.6)
Qmanb
(c) ) ∑j
hhmanb,jQj (4.7)
C′m′ anb,m′a′n′b′(ω) ≡
-1
2∫-∞
+∞ dt exp(iωt)〈[Qmanb
(c) (t),Qm′a′n′b′
(c) (0)]〉 (4.8)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2079


 density assumes the form
Here, λmanb,m′a′n′b′ ≡ M1
2Ω1
4dmanb,1dm′a′n′b′,1λ′1 is the bath
reorganization energy associated with the collective coordinates Qmanb
(c) and Qm′a′n′b′
(c) , and Λmanb,m′a′n′b′ rep
resents the inverse time scale of its fluctuations. This Hamiltonian constitutes the starting point for both the CGF and the NEE approaches which will be developed in the coming sections.
5. The Cumulant Expansion for Gaussian Fluctuations (CGF)
The molecular aggregate Hamiltonian introduced in section 4 can be mapped into a more general model of a multilevel system with Brownian oscillator fluctuations. This is done by diagonalization and a suitable transformation which is introduced in Appendix B. In this section we compute the nonlinear response of a fluctuating multilevel system. This calculation is not limited to the specific form of the Hamiltonian eqs 4.2 and B7. The model includes diagonal and off-diagonal fluctuations of the Hamiltonian matrix elements, which cause decay of coherences and redistribution of populations. We start by introducing the multilevel chromophore model with (M + 1) eigenstates (the ground state g and excited states a, b, ...) with energies Ωa, Ω.... Setting the ground-state energy to 0, the molecular Hamiltonian reads
The first term represents the isolated multilevel system, and the second describes the interaction with the optical field E(r,t), through the polarization operator
μag is the transition dipole moment between the ground state and state a, and μab is the transition dipole moment between excited states a and b. This Hamiltonian is identical to the exciton eigenstate representation given in eqs B7 and B8, provided we set g ≡ 0, a ≡ R, jR.... The system-bath interaction is given by
where the sum runs over all states, including the ground state. The fluctuations of the collective coordinates will be described by the matrix of spectral densities:
where the expectation value and the time evolution are taken with respect to the bath Hamiltonian. Equation 4.8 contains all relevant information about the fluctuations necessary for computing the optical response of the system. We adopt the model of eq 4.5 for the bath with the single overdamped Brownian oscillator (j ) 1) spectral density:
Here, λab,a′b′ and Λab,a′b′ are analogous to eq 4.18. We further define the line width parameter ∆ab,a′b′
2≡
2kBT/λab,a′b′. λaa,aa represents the magnitude of fluctuations of the energy of state a, while λab,ab represents the fluctuations of the coupling between states a and b. This is a convenient parameter for classifying different regimes of energy fluctuations. We shall introduce two types of dimensionless parameters, η and κ, to characterize the model. η are defined by118
where ηab controls the correlation of fluctuation amplitudes. It follows from the Cauchy-Schwartz inequality that ∆aa,bb
2 e ∆aa,aa∆bb,bb. We thus have -1 e ηab e 1. The fluctuations are anticorrelated for ηab ) -1, uncorrelated for ηab ) 0, and fully correlated for ηab ) 1. The second type of dimensionless parameter, κab ) Λaa,bb/∆aa,bb, denotes the ratio of the inverse time scale of the bath to the amplitude of the fluctuations. It controls the line shape; in the slow bath limit (κab < 1) the line shape is a Gaussian and gradually turns into a Lorentzian as κab is increased.57,140
5.1. Diagonal (Energy) Fluctuations
By setting Qab
(c) ) Qaa
(c)δab in eq 5.3, the model represents diagonal fluctuations. The optical response functions can then be calculated using the second-order cumulant expansion, which is exact for this model.57,116 For the linear response it yields57
where J(t1) ) 〈Pˆ (t1)Pˆ (0)〉 is a two-point correlation function of the polarization and the polarization operator is given in the Heisenberg representation:
where Hˆ 0 is the material part of the total Hamiltonian (setting E(r,t) ) 0 in eq 5.1). θ(t) is the Heavyside function (θ(t) ) 0 for t < 0, θ(t) ) 1 for t g 0). The angular brackets 〈‚‚‚〉 denote the trace over the equilibrium density matrix,
C′m′ anb,m′a′n′b′(ω) ) 2λmanb,m′a′n′b′
ωΛmanb,m′a′n′b′
ω2 + Λmanb,m′a′n′b′
2
(4.18)
Hˆ ) ∑a
Ωa|a〉〈a| - Pˆ E(r,t) + Hˆ SB (5.1)
ˆP ) ∑a
(μag|a〉〈g| + μga|g〉〈a|) + a∑,b
μab| b〉〈a| (5.2)
Hˆ SB ) a∑,b
Qab
(c)|a〉〈b| (5.3)
C′a′b,a′b′(ω) ≡ - 1
2∫-∞
+∞ dt exp(iωt)〈[Qab
(c)(t),Qa′b′
(c) (0)]〉 (5.4)
C′a′b,a′b′(ω) ) 2λab,a′b′
ωΛab,a′b′
ω2 + Λab,a′b′
2 (5.5)
∆aa,bb
2 ≡ ηab∆aa,aa∆bb,bb (5.6)
S(1)(t1) ) iθ(t1)[J(t1) - J*(t1)] (5.7)
Pˆ (t1) ) exp(iHˆ 0t1)Pˆ exp(-iHˆ 0t1) (5.8)
jFg ) a ∑
Faa|a〉〈a| (5.9)
2080 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 and Faa is the equilibrium population of the state a. Expanding the two-point correlation function in the system basis set, we get
where 〈‚‚‚〉B denotes an average with respect to the equilibrium distribution of the bath. Assuming the Condon approximation, i.e., that the transition dipole operator does not depend on the bath coordinates, we obtain
where Ωνν′ ) Ων - Ων′ and g ̃ ab(t1) are the frequency and the line-broadening function for the a-b transition, which is related to correlation functions of bath fluctuations,
and Uba(t) ≡ Qbb
(c)(t) - Qaa
(c)(t) represents the fluctuations of the a-b transition frequency. An (M + 1)-level system has M (M + 1)/2 distinct transitions represented by different Uab functions and the corresponding gab(t) functions. We can reduce the number of line-broadening functions, we define the line-broadening function associated with fluctuations of individual energy levels (rather than the transitions):
We now have (M + 1) independent variables Qaa
(c)(τ)
with (M + 1)2 distinct correlation functions. Comparing eqs 69 and 70, we obtain
where g′ab(t) are directly related to the diagonal
spectral densities of the bath, C′a′a,bb(ω):57
Substituting the overdamped Brownian oscillator spectral density (eq 4.18), we get in the hightemperature limit
Introducing the symmetrized g function,
the two-point polarization correlation function finally becomes
The third-order response function is similarly given by a sum of eight terms, each representing a distinct Liouville-space pathway:57
where57
and the four-point correlation function is given by
The subscript D in eq 5.19 stands for diagonal fluctuations. Expanding eq 5.21 in the system eigenstates, we get
The four-point correlation function may also be expressed using the line-broadening functions introduced earlier, again, by using second-order cumulant expansion:116
where
where tij ) ti - tj and i, j ) 1, 2, 3, 4. Substituting eq 5.14 into eq 5.24 and using the symmetric g
J(t1) ) a∑b
Faa|μba|2 ×
exp[-iΩbat1 - 1
2(gaa(t1) + gbb(t1)) + gba(t1)] (5.18)
SD(t3,t2,t1) ) i3θ(t3)θ(t2)θ(t1)p∑)1
4
{Rp(t3,t2,t1) 
Rp
/(t3,t2,t1)} (5.19)
R1(t3,t2,t1) ) F(t1,t1 + t2,t1 + t2 + t3,0)
R2(t3,t2,t1) ) F(0,t1 + t2,t1 + t2 + t3,t1)
R3(t3,t2,t1) ) F(0,t1,t1 + t2 + t3,t1 + t2)
R4(t3,t2,t1) ) F(t1 + t2 + t3,t1 + t2,t1,0) (5.20)
F(t4,t3,t2,t1) ) 〈Pˆ (t4)Pˆ (t3)Pˆ (t2)Pˆ (t1)〉 (5.21)
F(t4,t3,t2,t1) ) ab∑cd
Faa〈Pad(t4)Pdc(t3)Pcb(t2)Pba(t1)〉B
(5.22)
F(t4,t3, t2, t1) ) ab∑cd
Faa μad μdc μcb μba ×
exp(i(Ωadt4 + Ωdct3 + Ωcbt2 + Ωbat1)
-1
2f(t4,t3,t2,t1)) (5.23)
f(t4,t3,t2,t1) )  ̃gad(t43) +  ̃gad(t41) -  ̃gad(t31) 
 ̃gac(t43) -  ̃gac(t21) +  ̃gac(t42) +  ̃gac(t31) +  ̃gab(t21) +
 ̃gab(t41) -  ̃gab(t42) +  ̃gdc(t43) +  ̃gdc(t32) -  ̃gdc(t42) 
 ̃gdb(t32) -  ̃gdb(t41) +  ̃gdb(t42) +  ̃gdb(t31) +  ̃gcb(t32) +
 ̃gcb(t21) -  ̃gcb(t31) (5.24)
〈Pˆ (t1)Pˆ (0)〉 ) a∑b
〈Pab(t1)Pba(0)〉BFaa (5.10)
J(t1) ) a∑b
Faa|μba|2 exp[-iΩbat1 -  ̃gba(t1)] (5.11)
jgab(t) ) ∫0
t dτ1 ∫0
τ1 dτ2 〈Uab(τ1)Uab(τ2)〉 (5.12)
g′ab(t) ≡ ∫0
t dτ1∫0
τ1 dτ2〈Qaa
(c)(τ1)Qbb
(c)(τ2)〉 (5.13)
 ̃gab(t) ) g′aa(t) + g′bb(t) - g′ab(t) - g′ba(t) (5.14)
g′ab(t) ) ∫-∞
∞ dω 2π
1 - cos(ωt)
ω2 coth( pω
2kBT)C′a′a,bb(ω) +
i∫-∞
∞ dω 2π
sin(ωt) - ωt
ω2 C′a′a,bb(ω) (5.15)
g′ab(t) ) (2Tλab
Λab
2 - i λab
Λab)(exp(-Λab|t|) + Λabt - 1)
(5.16)
gab(t) ≡ g′ab(t) + g′ba(t) (5.17)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2081


 function (eq 5.17), we obtain
Equation 5.25 depends on (M + 1)2 independent correlation functions gab(t). This number may be reduced for high-frequency (optical) transitions where only the ground state is thermally populated. By choosing this state as a reference, we can express all the energies with respect to it. We can then set Qgg
(c)
) 0 and separate the total correlation function into two terms:118,119
Here,
and
f1 contains only transitions to and from the ground state g f a f g f b f g, whereas f2 also includes transitions among the excited states g f a f b f c f g and the number of independent line-broadening functions is reduced to M 2.
5.2. Off-Diagonal Fluctuations and Exciton Transport
The exact expressions for the third-order optical response function obtained above include only diagonal couplings to the bath representing energy fluctuations. Fluctuations of off-diagonal elements are responsible for exciton transport. Once off-diagonal fluctuations are included, the model is no longer exactly solvable. However, useful approximate expressions may be derived using projection operator techniques in the doorway-window representation.101 The time-resolved signal is represented as a convolution of three terms: a doorway function, an evolution term, and a window function. This picture holds as long as the excitation and detection are
temporally well separated. The doorway function describes the changes in the system after the primary interaction with the optical field, which creates a nonstationary state. The subsequent evolution of the system takes place in the absence of the optical field, and the window function represents the response of the new state to additional interactions with the field.
The total response function to lowest order in the system-bath coupling then becomes
SD, which contains the contribution of diagonal fluctuations, was given by eq 5.19. The additional contribution, SOD, due to off-diagonal fluctuations is given by
We shall refer to the first two terms in eq 5.30 as the hopping and the bleaching terms, respectively. They represent sequential (incoherent) contributions. The first term describes incoherent excitation transport. The doorway function Dh a represents the population of the excited state a created by two interactions with the radiation field. Wh b is the window function which gives the contribution of the excited state b population to the signal. Exciton hopping is described by the master equation:78
where Kab is the exciton transfer rate matrix and Gba(t′′ - t′) is the Green function of the master equation, defined by Fbb(t′′ - t′) ) ∑aGba(t′′ - t′)Faa(0). It represents the conditional hopping probability from state a to b during the t′′ - t′ time interval.
The second term in eq 5.30 represents a Ramantype contribution whereby the system is back in the ground state (g) during t2. Dg(t) and Wg(t) are the corresponding doorway and window functions. This term gives the limiting contribution for long t2 and is independent of t2. For short t2, exciton transport is negligible and SOD(t3,0,t1) must vanish. This is guaranteed by the third term in eq 5.30, since only population contributions are left in SD(t1,τ2,t3) at long τ2, which cancels the first two terms in eq 5.30 for t2 ) 0.
To lowest order in the system-bath interaction, we have Dh a(t′,t1) ) Da(t1)δ(t′) and Wh b(t3,t2 - t′′) ) Wb(t3) δ(t2 - t′′), and eq 5.30 is simplified to101
The Green function in this limit is given in Appendix C, and the corresponding doorway and window functions are presented in Appendix D.
f(t4,t3,t2,t1) ) gaa(t41) + gbb(t21) + gcc(t32) +
gdd(t43) - gab(t21) - gab(t41) + gab(t42) + gac(t21) + gac(t43) - gac(t31) - gac(t42) - gad(t43) - gad(t41) + gad(t31) - gbc(t21) - gbc(t32) + gbc(t31) + gbd(t32) + gbd(t41) - gbd(t31) - gbd(t42) - gcd(t32) - gcd(t43) + gcd(t42) (5.25)
F(t4,t3,t2,t1) ) a∑b
μgb μbg μga μag ×
exp[i(-Ωbgt4 + Ωbgt3 - Ωagt2 + Ωagt1) 
1
2f1(t4,t3,t2,t1)] +
∑
abc
μgcμcbμbaμag ×
exp[i(-Ωcgt4 - Ωbct3 + Ωbat2 + Ωagt1) 
1
2f2(t4,t3,t2,t1)] (5.26)
f1(t1,t2,t3,t4) ) gaa(t21) + gbb(t43) + gab(t32) + gab(t41) - gab(t31) - gab(t42) (5.27)
f2(t1,t2,t3,t4) ) gaa(t21) + gbb(t32) + gcc(t43) 
gab(t21) - gab(t32) + gab(t31) + gac(t32) + gac(t41) 
gac(t31) - gac(t42) - gbc(t32) - gbc(t43) + gbc(t42) (5.28)
S(t3,t2,t1) ) SD(t3,t2,t1) + SOD(t3,t2,t1) (5.29)
SOD(t3,t2,t1) ) a∑b ∫0
t2 dt′′∫0
t′′ dt′ Wh b(t3,t2 - t′′) ×
Gba(t′′ - t′)Dh a(t′,t1) + Wg(t3)Dg(t1) - SD(t3,∞,t1) (5.30)
d
dtFbb(t) )∑c
[KbcFcc(t) - KcbFbb(t)] (5.31)
SOD(t3,t2,t1) ) a∑b
Wb(t3)Gba(t2)Da(t1) +
Wg(t3)Dg(t1) - SD(t3,∞,t1) (5.32)
2082 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 5.3. Numerical Simulations
Given the exciton Hamiltonian and the matrix of spectral densities, we can now compute the thirdorder response of aggregates. The eigenstate parameters are defined by comparing eqs 5.1 and 5.2 with eqs B7 and B8. The exciton states R,jR now correspond to molecular excited states a, and the transition dipole moments μR and μR,‚h correspond to molecular transition dipole moments μag and μab.
The correlation functions f1 and f2 represent terms which do not (f1) and do (f2) involve the two-exciton states in the sum-over-states expansion. The response and the line-broadening functions are obtained using the transformed spectral densities in the exciton representation. The same considerations apply to the exciton transport induced by off-diagonal couplings with the bath. The third-order nonlinear response can probe incoherent hopping of exciton populations in the local basis set. Thus, the sequential component of the response function is calculated in terms of the one-exciton states.
Aggregates made of two-level molecules in the exciton basis have distinct one-, two-, three-, ..., exciton manifolds (see Figure 1). There are four possible third-order techniques, with signal wavevectors kI ) -k1 + k2 + k3, kII ) k1 - k2 + k3, kIII ) k1 + k2 - k3, and kIV ) k1 + k2 + k3. The Feynman diagrams57 given in Figure 3 show the processes which contribute to each of these signals.
The capacity of third-order techniques to resolve various secondary structural motifs of peptides is demonstrated in Figure 4.141 Shown is the kI signal I(ω1,t2 ) 0,ω3) (eq 3.6) around the amide I transition energy for three different structures: R-helix, 310helix, and antiparalel ‚-sheet. Ideal structures were used, and the couplings between different amide I modes were computed using the dipole-dipole coupling model,142 yielding a distinct coupling pattern for each structure.
Each peptide bond is modeled as an anharmonic three-level system. The two-exciton manifold consists of doubly excited states (overtones) mixed with pairs of singly excited states (combination band). There are
Figure 3. Double-sided Feynman diagrams representing the Liouville-space pathways contributing to the third-order response of an aggregate in the rotating wave approximation. Each box shows the diagrams contributing to a four-wave mixing signal generated in the various possible directions: kI ) -k1 + k2 + k3, kII ) k1 - k2 + k3, kIII ) k1 + k2 - k3, and kIV ) k1 + k2 + k3. Diagrams (a), (b), (d), and (e) include only one-exciton states. Diagrams (c), (f), (g), and (h) also include two-exciton states, and diagram (i) includes three-exciton states. The level scheme is given in Figure 1.
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2083


 two distinct peaks for R-helix and 310-helix: longitudinal (polarized along the axis of the helix) and transverse (perpendicular). The splitting is much larger in the 310-helix. The 310-helix signal shows clear cross-peaks between the longitudinal and transverse transitions, suggesting strong correlation between these states. The signal for the antiparalel ‚-sheet has two diagonal transitions. The strongest transition is in-plane. The transition which is perpendicular to the plane is the second strongest transition in the system. The clearly visible crosspeaks show correlations between the different transitions and indicate strong couplings among vibrations, characteristic to each structure. Figure 4 focused on the peak pattern and used simple Lorentzian line shapes. In general, the line shapes carry useful dynamical information about bath fluctuations. Typically fast and slow fluctuations result in Lorentzian and Gaussian profiles, respectively, whereas arbitrary bath time scales may yield more complex line shapes. The kI, kII, and kIII signals for a model of two anharmonic vibrations with overdamped bath fluctuations with arbitrary correlations and time scales are presented in Figure 5.118 In this model, the two vibrations have identical anharmonicities. Only the fundamental frequencies
are fluctuating, and the anharmonicities are fixed. The correlations of these fluctuations are measured by the parameter η, which represents correlated (η ) 1), uncorrelated (η ) 0), and anticorrelated (η ) -1) fluctuations. The peak positions in the 2D plots indicate different transition energies. Diagonal peaks correspond to fundamental transitions (observed in
Figure 4. kI signal of the amide I band for various second
ary structure motifs of peptides:141 (top) R-helix, (middle) 310-helix, and (bottom) antiparalel ‚-sheet. Shown is |I(ω1,t2 ) 0,ω3)| (eq 3.6) on a logarithmic scale for the polarization ZZYY. The zero frequency corresponds to (ω1 ) Ω0, ω3 ) Ω0), with the fundamental frequency Ω0 )1675
cm-1 and the anharmonicities 16 cm-1.
Figure 5. Signals of various wave-mixing techniques for a model dimer of two interacting vibrations calculated using the CGF method.118 Shown is I(ω3,t2 ) 0,ω1) (eq 3.6). The parameters of the model are given in ref 118. Slow, intermediate, and fast bath limits of the overdamped Brownian oscillator model show a different peak pattern. The different peaks in the signals kI, kII, and kIII reflect the different transitions involved in the nonlinear experiment. The parameter η defines the correlation type of fluctuations of different chromophores: η ) -1 (anticorrelated), η ) 0 (uncorrelated), and η ) 1 (positively correlated).
2084 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 linear absorption), while cross-peak intensities indicate the coupling strength between vibrations. The separation of the overtone from the diagonal peaks reflects the anharmonicity. Fast bath fluctuations lead to circular peaks in (ω1,ω3) correlation plots (eq 3.6), while slow static fluctuations give elliptical peaks, which represent homogeneous (along the offdiagonal direction) and inhomogeneous (along the diagonal direction) line broadenings. Positively and negatively correlated transitions show different orientations of the elliptical shapes.
6. The Nonlinear Exciton Equations (NEE)
In this section we present an alternative, equations of motion approach for computing the nonlinear response.143-145 These equations, written in the local basis, avoid the computation of eigestates, which is an expensive task for large aggregates. The approach is restricted to a Hamiltonian which conserves the number of excitons. Like the CGF, this method includes diagonal and off-diagonal fluctuations of the Hamiltonian matrix elements. However, the Markovian approximation for the bath limits the method to Lorentzian line shapes.
6.1. Closing the Many-Body Hierarchy
To derive the NEE, we start with the aggregate Hamiltonian (eq 4.2), where the polarization operator is given by eq 4.4. The optical signal is expressed in terms of the expectation value of the polarization operator, P(t) ≡ 〈P〉, which depends on 〈Bˆ ma〉, 〈Bˆ ma
†〉
) 〈Bˆ ma〉*, and 〈Bˆ ma
† Bˆ mb〉 (see eq 4.4). We start with the Heisenberg equation of motion for an arbitrary operator Aˆ :
The equation of motion for the exciton annihilation operator Bˆ contains higher order products of the creation and annihilation operators generated by the commutator with the Hamiltonian:
where we have neglected the bath and hma,nb ) Ωmaδmnδab + Jma,nb(1 - δmnδab). Once we take expectation values, this equation is not closed, since 〈Bˆ ma〉 is coupled to higher dynamical variables 〈Bˆ ma
† Bˆ nb〉,
etc. We can supplement eq 6.2 by the Heisenberg
equation of these higher variables. Thus, the direct application of the Heisenberg equation yields an infinite many-body hierarchy of equations for products of operators.146 Fortunately, for the present model the hierarchy may be rigorously truncated order by order in the radiation field, allowing an exact calculation of the nonlinear response functions. Because only the radiation field can change the number of excitons, only a limited number of electronic excitations need to be considered at each order. For example, the third-order optical response depends only on products of up to three operators, and higher products can be neglected since they only show up at higher orders in the optical field. The hierarchy can thus be rigorously truncated by retaining the following variables:78
where the indices m, n, and k correspond to different chromophores and a, b, and c represent various excited states of each chromophore. Overall we have (NM ) Bma variables, (NM )2 Yma,nb and Nma,nb vari
ables, and (NM )3 Zma,nb,kc variables. Bma describe oneexciton dynamics, and the nonlocal variables Yma,nb represent the coherent two-exciton motion and the interaction between them. The variables Nma,nb constitute the exciton density matrix, which represents populations and coherences of one-exciton states, and Zma,nb,kc are three-point variables. The NEE equations read
LB, LY, LN, and LZ are linear terms describing the free evolution of non-interacting excitons. The terms KB, K Y, and K Z are responsible for the two-exciton motion and interactions between excitons in the isolated system. In particular, KB is responsible for the two-exciton contribution to the optical polarization and K Y and K Z represent the exciton-exciton scattering. Linear interaction with the optical field comes from EB, and the nonlinear interaction is represented by FB, FY, FN, and FZ. Closed expressions for the terms L, K, E, and F are given in Appendix E. The relaxation terms ΓB, ΓY, ΓN, and ΓZ will be introduced in the next subsection.
-i ∂ ˆA
∂t ) [Hˆ , ˆA] (6.1)
-i
∂Bˆ ma
∂t ) l∑d
-hma,ldBˆ ld +
∑
ldd′
(hma,ld′Bˆ md
† Bˆ mdBˆ ld′ +
hmd,ld′Bˆ md
† Bˆ maBˆ ld′) 
∑
ld
(K l,m
dd,aa + K m,l
aa,dd)Bˆ ld
† Bˆ ldBˆ ma 
μmaE(t) 
∑
d
(μmaBˆ md
† Bˆ md + μmdBˆ md
† Bˆ ma 
μm,adBˆ md)E(t) (6.2)
Bma ≡ 〈Bˆ ma〉 (6.3)
Yma,nb ≡ 〈Bˆ maBˆ nb〉 (6.4)
Nma,nb ≡ 〈Bˆ ma
† Bˆ nb〉 (6.5)
Zma,nb,kc ≡ 〈Bˆ ma
† Bˆ nbBˆ kc〉 (6.6)
-i ∂B
∂t ) LB + K B + E B + F B + i Γ B (6.7)
-i ∂Y
∂t ) LY + KY + FY + i ΓY (6.8)
-i ∂N
∂t ) LN + F N + i Γ N (6.9)
-i ∂Z
∂t ) LZ + K Z + F Z + i Γ Z (6.10)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2085


 Substituting the linear terms (eqs E1-E4) and writing explicitly the matrix elements of eqs 6.76.10, we obtain
The response to short pulses can be viewed as a sequence of impulsive couplings with the fields followed by periods of free evolution. The latter can be described by the following Green functions, which are the formal solutions of the NEE when the field is turned off (E(t) ) 0). After the first interaction the system evolution is described by
with KB ) 0 since higher order variables have not yet been created. The second interaction creates the second-order variables, and their evolution is described by
The third interaction creates the third-order variables Zma,nb,kc and
Neglecting the relaxation terms ΓB, the one-exciton evolution in eq 6.15 is described by the one-exciton eigenfunctions ÊR(ma) and eigenvalues, obtained by solving the eigenvalue equation:
We then have
Here, the time dependence represents the free evolution of eigenstates, while the sum over eigenfunctions reflects transformation to the local chromophore basis
set. The evolution of two- and three-point exciton variables includes exciton-exciton scattering terms, which can be expressed using the exciton scattering matrix related to the Bethe-Salpeter equation.57,78 The NEE have been gradually developed over the past few years.147-149 Spano and Mukamel first showed how theories based on the local field approximation can be extended by adding two-exciton (Y) variables to properly account for two-exciton resonances.144 Equations of motion for one- and twoexciton variables avoid the explicit calculation of twoexciton states, tracing the origin of the third-order nonlinear optical response to exciton-exciton scattering.149-151 Extensions were then made to molecular aggregates made of three-level molecules152 and to semiconductors.153,154 Other relevant variables have subsequently been identified.150,151 The simplest way to include the coupling with phonon degrees of freedom is to eliminate the nuclear variables and incorporate their effects through relaxation rates. This results in the Redfield equation for the reduced exciton density matrix.115-156 Phonon-induced dephasing has been incorporated into the theories of  ̄(3) in two-level molecular aggregates by including the N variables and applying certain factorization schemes for closing the equations.157,158 This level of theory is equivalent to the SBE with dephasing used for semiconductors. The resulting expressions for  ̄(3) describe adequately transient-grating experiments; however, they do not apply when both exciton transport and two-exciton resonances are important, which is the case in pump-probe and photon-echo spectroscopies. In their latest form (eqs 6.7-6.10),143,147 the NEE provide closed form Green function expressions for the optical response that maintain the complete bookkeeping of time ordering. Applications were made to a broad range of spectroscopies of J-aggregates,147 pump-probe spectroscopy of light-harvesting antenna complexes,159 photon-echoes,160 and four-wave mixing.161 Additional effects of strong coupling to phonons can be incorporated in equations of motion describing polaron transport101,156,162 or by solving equations of motion for reduced wave packets which involve the dynamics of a few important collective nuclear coordinates.137 These extensions go beyond the scope of this review.
6.1.1. The Local Field Factorization
Several factorization schemes may be used in some cases to further simplify the NEE. The linear terms LB, LY, LN, and LZ describe the dynamics of excitons in the absence of exciton-exciton interaction and relaxation. Neglecting the exciton interaction terms KY and KZ, the higher order variables can be factorized as
where Bma(t) is given by eq 6.15. In this approxima
Yma,nb(t) ≡ Bma(t)Bnb(t) (6.21)
Nma,nb(t) ≡ Bma
/ (t)Bnb(t) (6.22)
Zma,nb,kc(t) ≡ Bma
/ (t)Bnb(t)Bkc(t) (6.23)
-i
∂Bma
∂t ) l∑d
(-hma,ldBld) + (K B)ma + (E B)ma +
(F B)ma + i(Γ B)ma (6.11)
-i
∂Yma,nb
∂t ) l∑d
(-hma,ldYld,nb - hnb,ldYma,ld) +
(KY)ma,nb + (FY)ma,nb + i(ΓY)ma,nb (6.12)
-i
∂Nma,nb
∂t ) l∑d
(hld,maNld,nb - hnb,ldNma,ld) +
(F N)ma,nb + i(Γ N)ma,nb (6.13)
-i
∂Zma,nb,kc
∂t ) l∑d
(hld,maZld,nb,kc - hnb,ldZma,ld,kc 
hkc,ldZma,nb,ld) + (K Z)ma,nb,kc + (F Z)ma,nb,kc +
i(Γ Z)ma,nb,kc (6.14)
Bma(t) ) Gma,m′a′
B (t)Bm′a′(0) (6.15)
Yma,nb(t) ) Gmanb,m′a′n′b′
Y (t)Ym′a′,n′b′(0) (6.16)
Nma,nb(t) ) Gmanb,m′a′n′b′
N (t)Nm′a′,n′b′(0) (6.17)
Zma,nb,kc(t) ) Gmanbkc,m′a′n′b′k′c′
Z (t)Zm′a′,n′b′,k′c′(0) (6.18)
- l∑d
hma,ldÊR(ld ) ) RÊR(ma) (6.19)
Gma,nb
B (t) ) ∑R
ÊR(ma)ÊR(nb) ei Rt (6.20)
2086 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 tion, each molecule described by Bma is decoupled from the others, except for the presence of local electric field, Ema
B + ∑nb Jma,nbBnb + ∑nb(K m,n
aa,bb +
K n,m
bb,aa)Bnb
/ Bnb.
6.1.2. Pure State Factorization
Due to exciton-exciton scattering, the Y variables may not be factorized. If the system has a weak relaxation and pure dephasing can be neglected, the system remains in a pure state; i.e., the bra and ket components of the density matrix evolve independently. The N and Z variables then can be factorized
as Nmanb ) Bma
/ Bnb and Zma,nb,kc ) Bma
/ Ynb,kc. We are then left with two equations for B and Y. Here the decay of coherences is ignored while exciton-exciton scattering is properly accounted for. This approximation, thus, holds in some ultrafast experiments when relaxation may be neglected.
6.1.3. Exciton Population Factorization
Assuming fast pure dephasing, all correlations among chromophores can be neglected. In this case, Zma,nb,kc ) Nma,mbBkcδmn. We now have closed equations only for B and N. The dynamics of the Nma,mb variables may be described by the Bloch equations.
6.2. The Relaxation Terms
In general, all elements of the system Hamiltonian may fluctuate; however, we restrict the discussion to the quadratic diagonal and off-diagonal fluctuations given in eq 4.6. Each state of the system is linearly coupled to the bath oscillators. The relaxation terms were calculated to second order in the system-bath coupling. We expand the terms in the following form:
The relaxation terms can be calculated using the linear coupled variables, defined in Appendix F:
These terms appear in the NEE when the bath Hamiltonian and the system-bath coupling are
included in the Heisenberg equations. Equations of motion of the linear coupled variables are also given in Appendix F. To calculate RB, we first write the solution of coupled variable Bh ma,j
q , which follows from eq F23:
where
where Cj′′(ω) is a spectral density of j coordinate (eq
4.10). Then the relaxation rate follows by substituting eq 6.32 in eq 6.28 and using eq 6.24:
where we have used Bld(t - τ) ) Gld,m′a′
B† (τ)Bm′a′(t),
and Gma,m′a′
B is given by eq 6.15. The relaxation term RN is obtained by following the same procedure. We write the solution of the coupled
N manb,j
q variable:
Substituting eq 6.35 in eq 6.30 and using eq 6.26, we get
where we have used factorized Green functions inside
the integral, Gmanb,m′a′n′b′
N (τ) ) Gma,m′a′
B† (τ)Gnb,n′b′
B (τ), and
Nma,nb(t - τ) ) Gmanb,m′a′n′b′
N† (τ)Nm′a′,n′b′(t). Rmanb,m′a′n′b′
N
is known as the Redfield relaxation operator.115
(ΓB)ma ≡ m∑′a′
Rma,m′a′
B Bm′a′ (6.24)
(ΓY)ma,nb ≡ m′a∑′n′b′
Rmanb,m′a′n′b′
Y Ym′a′,n′b′ (6.25)
(ΓN)ma,nb ≡ m′a∑′n′b′
Rmanb,m′a′n′b′
N Nm′a′,n′b′ (6.26)
(ΓZ)ma,nb,kc ≡ ∑
m′a′n′b′k′c′
Rmanbkc,m′a′n′b′k′c′
Z Zm′a′,n′b′,k′c′
(6.27)
(iΓB)ma ) l∑dj
(-hh mald,jBh ld,j
q ) (6.28)
(iΓY)manb ) l∑dj
(- hhmald,j hY ldnb,j
q - hhnbld,j hY mald,j
q ) (6.29)
(iΓN)manb ) l∑dj
(hh mald,jNh ldnb,j
q - hh nbld,jNh mald,j
q ) (6.30)
(iΓZ)manbkc ) l∑dj
(hh mald,jZh ldnbkc,j
q - hh nbld,jZh maldkc,j
q
hh kcld,jZh manbld,j
q ) (6.31)
Bh ma,j
q (t) )
-i∫0
∞ dτ ldl∑′d′
Gma,ld
B (τ)hhldl′d′,jMj(τ)Bl′d′(t - τ) (6.32)
Mj(τ) ) 1
2∫-∞
+∞ dω
2π Ch j′′(ω)[coth( pω
2kBT) cos(ωτ) 
i sin(ωτ)] (6.33)
Rma,m′a′
B ) ∫0
∞ dτ ∑
ld,l′d′,l′′d′′
Gl′d′,l′′d′′
B (τ)∑j
hh mal′d′,j hh l′′d′′ld,j Mj(τ)Gld,m′a′
B† (τ) (6.34)
Nh manb,j
q (t) ) -i∫0
∞dτ ∑
ld,m′a′n′b′
[Gmanb,m′a′n′b′
N (τ)hhm′a′ld,j Mj(-τ)Nld,n′b′(t - τ) 
Gmanb,m′a′n′b′
N (τ)hhn′b′ld,j Mj(τ)Nm′a′,ld(t - τ)] (6.35)
Rmanb,m′a′n′b′
N ) ∫0
∞ dτ ∑
m′′a′′n′′b′′ld,l′d′
[Gl′d′,ld
B† (τ)Gnb,n′′b′′
B (τ) ∑j
hh l′d′ma,j hh m′′a′′ld,j Mj(-τ) 
Gld,m′′a′′
B† (τ)Gnb,ld
B (τ) ∑j
hh l′d′ma, j hh ldn′′b′′,j Mj(τ) 
Gma,ld
B† (τ)Gl′d′,n′′b′′
B (τ) ∑j
hh nbl′d′,j hh m′′a′′ld,j Mj(-τ) +
Gma,m′′,a′′
B† (τ)Gl′d′,ld
B (τ) ∑j
hh nbl′d′,j hh ldn′′b′′,j Mj(τ)] ×
Gm′′a′′,m′a′
B (τ)Gn′′b′′,n′b′
B† (τ) (6.36)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2087


 The relaxation terms RY and RZ calculated by neglecting exciton-exciton scattering assume the form:
Closed expressions for these relaxation terms, using the overdamped Brownian oscillator spectral density for the bath, are given in Appendix G.
6.3. Numerical Integration of the NEE; Selecting the Desired Signal
The NEE may be solved perturbatively in the fields, resulting in closed Green function expressions for the response functions. These expressions have been reviewed recently78 and will not be repeated here. The Green function expressions are most useful for either very short or very long optical pulses, where the signal is directly related to the response function in the time domain or in the frequency domain, respectively. For arbitrary pulse shapes it may be more convenient to compute the polarization directly by integrating the equations of motion which contain the field envelopes.163-166 The nonlinear polarization induced by three optical fields with wavevectors k1, k2, and k3 and carrier frequencies jω1, jω2, and jω3 (see eq 22) can be expanded as
with u, v, and w ) 0, (1, (2, .... The different contributions may be distinguished experimentally through the wavevector ks ) uk1 + vk2 + wk3 of the signal. In a perturbative solution it is straightforward to select the desired contribution. A nonperturbative, finite field, numerical solution, however, yields the entire polarization, which is a sum of all contributions. To extract the desired component of the polarization, we use the following expansion of the optical field:
where Eu,v,w(t) is the slowly varying amplitude for mode (u,v,w), and Íj ≡ kjr - jωjt (with j ) 1, 2, 3) is the phase of mode j (see eq 3.1). Comparing eq 6.40 with eq 3.1, we note that the incoming field has only six modes (u,v,w) ) ((1, 0, 0), (0, (1, 0), (0, 0, (1), where the sign “+” (“-”) reflects forward (backward) propagation. Due to nonlinearities of the system, additional modes are generated in the polarization and in all NEE variables, i.e.,
Substitution of these Fourier expansions into the NEE results in the following equations for the various Fourier components:
where the mixing of different Fourier amplitudes is caused by the nonlinear terms. In a three-pulse experiment the optical field has six components (two
Rmanb,m′a′n′b′
Y ) Rma,m′a′
B δnb,n′b′ + Rnb,n′b′
B δma,m′a′ (6.37)
Rmanbkc,m′a′n′b′k′c′
Z ) (Rma,m′a′
B )*δnb,n′b′δkc,k′c′ +
Rnb,n′b′
B δma,m′a′δkc,k′c′ + Rkc,k′c′
B δma,m′a′δnb,n′b′ (6.38)
P(t) ) u,v∑,w
Pu,v,w(t) exp[i(uk1 + vk2 + wk3)r 
(u jω1 + v jω2 + w jω3)t] (6.39)
E(r,t) ) u,v∑,w
Eu,v,w(t) exp(iuÍ1 + ivÍ2 + iwÍ3)
(6.40)
Bma(t) ) u,v∑,w
Bma(u,v,w) exp(iuÍ1t + ivÍ2t + iwÍ3t)
(6.41)
Yma,nb(t) )
∑
u,v,w
Yma,nb(u,v,w) exp(iuÍ1t + ivÍ2t + iwÍ3t) (6.42)
Nma,nb(t) )
∑
u,v,w
Nma,nb(u,v,w) exp(iuÍ1t + ivÍ2t + iwÍ3t) (6.43)
Zma,nb,kc(t) )
∑
u,v,w
Zma,nb,kc(u,v,w) exp(iuÍ1t + ivÍ2t + iwÍ3t) (6.44)
-i
∂Bma(u,v,w)
∂t ) (u jω1 + v jω2 + w jω3)Bma(u,v,w) +
∑
ld
(-hma,ld + iRma,ld
B )Bld(u,v,w) + (KB)ma(u,v,w) +
(EB)ma(u,v,w) + (FB)ma(u,v,w) (6.45)
-i
∂Yma,nb(u,v,w)
∂t ) (u jω1 + v jω2 + w jω3)Yma,nb(u,v,w) +
∑
ld
[(-hma,ld + iRma,ld
B )Yld,nb(u,v,w) +
(-hnb,ld + iRnb,ld
B )Yma,ld(u,v,w)] +
(KY)manb(u,v,w) + (FY)manb(u,v,w) (6.46)
-i
∂Nma,nb(u,v,w)
∂t )
(u jω1 + v jω2 + w jω3)Nma,nb(u,v,w) +
∑
ld
[hma,ldNld,nb(u,v,w) - hnb,ldNma,ld(u,v,w)] +
im′a∑′n′b′
Rmanb,m′a′n′b′
N Nm′a′n′b′(u,v,w) +
(FN)manb(u,v,w) (6.47)
-i
∂Zma,nb,kc(u,v,w)
∂t )
(u jω1 + v jω2 + w jω3)Zma,nb,kc(u,v,w) +
∑
ld
[(-hma,ld + iRma,ld
B )Zld,nb,kc(u,v,w) +
(-hnb,ld + iRnb,ld
B )Zma,ld,kc(u,v,w) +
(-hkc,ld + iRkc,ld
B)Zma,nb,ld(u,v,w)] +
(KZ)manbkc(u,v,w) + (FZ)manbkc(u,v,w) (6.48)
2088 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 for each field). For instance,
where Ema(p) is associated with the pulse envelope of field j ) 1, 2, 3. The rotating-wave approximation (RWA) is easily implemented in eqs 6.45-6.48. Since the Fourier amplitudes are slowly varying, the slow terms are selected only when u jω1 + v jω2 + w jω3 are close to a frequency associated with the dynamic variables. Only, the following modes survive the RWA:
The actual number of important components is, thus, much smaller than the entire three-dimensional space of Fourier components, and the NEE can be solved numerically for the various Fourier components. For instance, (u,v,w), corresponding to the four independent third-order techniques, are
For a two-pulse experiment, a two-dimensional Fourier transform is required to extract a particular optical signal, which simplifies the computations considerably. As an application of the NEE, we show simulation of the pump-probe spectrum of the bacterial lightharvesting complex LH2.167 This is a key biological unit of photosynthesis responsible for primary solar energy absorption, which is later funneled into the reaction center (via LH1 complex) where charge separation converts sunlight into chemical energy.9 The photosynthetic antenna consists of two rings of chromophores: the B800 complex absorbs at 800 nm, while B850 absorbs at 850 nm. The structures of these are very similar. Both consist of 18 bacteriochlorophylls (BCls) placed in the ring, while the distances between BCls of the B800 complex is larger than in the B850 complex. The B850 excitons are delocalized due to intermolecular interactions, as indicated by the red-shifted absorption band. Due to larger distances in the B800 ring, the interactions between BCls in B800 are weak, and different BCls respond independently.
Interactions with the vibrations and structural disorder of the system are also key factors in the exciton dynamics. Carotenoid (Car) molecules, which are part of the photosynthetic antenna, have a much higher absorption band (at 450 nm). Recently, Herek et al. observed shifting of Car absorption bands depending on the electronic state of the LH2 system.102 This effect can be accounted for by the quartic interactions Kmn (eq 4.2). The NEE parameters may be obtained using additional data obtained from various experiments. Linear absorption provides information about energies of eigenstates. We assume that the BChls composing the B800 and B850 rings are identical. The different absorption energies of the rings come from different coupling between the molecules. Couplings between chromophores may be obtained by fitting the B850 absorption spectra. The line widths may be tuned by varying the interaction strength with the bath. The quartic coupling was obtained by comparing experimental nonlinear spectra with simulations. Using these parameters, we have developed a simple model of the LH2 complex which mimics the results of ref 102. The B800 and B850 complexes were represented as two two-level dimers, A and B (see Figure 6a). To represent the B850 complex, we added a strong coupling between the chromophores inside the B dimer. Car is represented as an additional (C) twolevel chromophore. We assumed different fourthorder couplings between A-C and B-C. Thus, in the Hamiltonian in eq 4.2 the indices a, b, ... may be omitted since we have only one excited state per chromophore and m, n, ... now correspond to chromophores A1, A2, B1, B2, and C. The relaxation operators were computed by assuming a Brownian oscillator model for diagonal and offdiagonal fluctuations of the Hamiltonian.167 The simulated linear absorption and pump-probe spectra in the regions of BCls and Car are presented in Figure 6. The linear absorption consist of three bands at 11 900 (B850), 12 500 (B800), and 22 000 cm-1 (Car). We have further simulated the pumpprobe spectrum, where the pump excited B dimer and probing was done in the regions 11 000-14 000 and 21 000-23 000 cm-1. The spectrum reveals excitonic effects of B dimer and energy flow A f B. The C absorption band shifts to higher energies (since Umn is positive) immediately following the excitation. The shift decreases as population is transferred to the B dimer since the quartic B-C coupling is smaller than that of A-C.
7. Discussion
The fluctuating multilevel Hamiltonian116,118,168 captures the essential features and trends of the optical response of chromophore aggregates coupled to a bath. The CGF correlation function expressions presented in section 5 for the linear and the thirdorder optical response of multilevel chromophores are based on the Condon approximation, where the transition dipole is assumed to be independent of
(EB)ma(u,v,w) ) -{δu,-1δv,0δw,0Ema(1) +
δu,1δv,0δw,0Ema
/ (1) + δu,0δv,-1δw,0Ema(2) +
δu,0δv,1δw,0Ema
/ (2) + δu,0δv,0δw,-1Ema(3) +
δu,0δv,0δw,1Ema
/ (3)} (6.49)
Bma(u,v,w) S u jω1 + v jω2 + w jω3 ≈ Ωma (6.50)
Yma,nb(u,v,w) S u jω1 + v jω2 + w jω3 ≈ Ωma + Ωnb
(6.51)
Nma,nb(u,v,w) S u jω1 + v jω2 + w jω3 ≈ -Ωma + Ωnb (6.52)
Zma,nb,kc(u,v,w) S u jω1 + v jω2 + w jω3 ≈ -Ωma +
Ωnb + Ωkc (6.53)
-k1 + k2 + k3 S (-1,+1,+1); k1 - k2 + k3 S (+1,-1,+1)
k1 + k2 - k3 S (+1,+1,-1); k1 + k2 + k3 S (+1,+1,+1)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2089


 nuclear coordinates. Diagonal fluctuations induced by the bath, which determine the line shape, are computed using the second-order cumulant expansion which is exact for a harmonic Gaussian bath. The relevant bath information is contained in the collective Brownian oscillator spectral densities which determine the spectral broadening functions. Offdiagonal fluctuations lead to relaxation processes of coherences and of populations. Exciton transport induced by off-diagonal fluctuations was calculated perturbatively using projection operator techniques.101,169,170 Computing the response involves several steps: (i) finding the one- and two-exciton eigenstates, (ii) computing the transition dipole moments in the exciton basis, and (iii) computing the transformation matrices of the spectral densities to the exciton basis. The line-broadening functions
define the line shapes which can take an arbitrary form, and off-diagonal bath fluctuations lead to various relaxation processes of coherences and populations. Thus, the CGF formalism can describe various fluctuations with an arbitrary distribution of time scales. Single-exciton states can be found by diagonalizing the single-exciton Hamiltonian. Calculation of higher (double-, triple-, ...) exciton states and of their correlation functions becomes numerically expensive for large aggregates. These difficulties are avoided by using a second, dynamical method for computing the nonlinear response. Using the nonlinear exciton equations78,143,171 given in section 6, the number of variables in the NEE scales as (NM)3, where N is the number of chromophores and M is the number of excited states in each chromophore.
Figure 6. Pump-probe signal of a five-chromophore aggregate representing photosynthetic antenna and a carotenoid molecule.167 (a) The B800 complex is represented by a dimer A, the B850 complex is represented by a dimer B, and the carotenoid system is represented by a chromophore C. The energies of the chromophores composing A and B dimers are identical: ΩA1 ) ΩA2 ) ΩB1 ) ΩB2 ) 12 500 cm-1. The second-order coupling between chromophores B1 and B2, JB1,B2 ) 600
cm-1. The excited-state energy of chromophore C represents Car absorption: ΩC ) 22 000 cm-1. C is quartically coupled
to A and B: KA1,C ) KA2,C ) 300 cm-1 and KB1,C ) KB2,C ) 100 cm-1. The A dimer is pumped in the pump-probe experiment.
(b) The linear absorption showing three lines: A dimer (12 500 cm-1), B dimer (11 900 cm-1), and C (22 000 cm-1). (c) Pump-probe signal showing exciton transfer between A and B in the 11 000-14 000cm-1 region. (d) The time-dependent line shift in the absorption of the C chromophore is solely induced by the quartic coupling and vanishes if we set K ) 0 in the Hamiltonian eq 4.2.
2090 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 Since the NEE avoid the computation of the eigenstates of the system, they can be used for larger molecular aggregates than the CGF. However, the simplified Redfield description of the bath can describe only fast bath motions, which yields Lorentzian line shapes. Slow bath fluctuations can be readily incorporated by performing an ensemble average of the response functions. Thus, only slow and fast baths can be accounted for by the NEE, whereas the CGF expressions can describe coupling to a bath with an arbitrary distribution of time scales.
The solution of the NEE yields expressions for the optical response in terms of Green functions representing the free dynamics of the various variables when the external field is switched off. The singleexciton variables are described by GB. Similarly, we can introduce a Green function for the 〈Bˆ maBˆ nb〉 variables that describes the motion of two-exciton and exciton-exciton scattering, and a third Green function for the exciton density matrix 〈Bˆ ma
† Bˆ nb〉 that describes incoherent exciton motion induced by exciton-phonon scattering. By representing the response in terms of these three Green functions,143 we obtain a collective quasiparticle picture for exciton dynamics and the nonlinear response.
If the energy levels of the aggregate form a harmonic ladder, the system becomes linear; i.e., the induced polarization will always be linear in the applied field, and all nonlinear response functions R(2), R(3), etc. must vanish identically. This is the celebrated Lorentz oscillator model for the linear response.172 In the CGF picture, the vanishing of the nonlinear response is a result of a delicate interference among many Liouville-space pathways. Only when all the terms are carefully added, they exactly cancel, reflecting a destructive interference of various nonlinear paths. In contrast, in the NEE this interference is naturally built-in from the start, avoiding the computation of spurious almost-canceling quantities. This point may be highlighted by expressing the Green functions in terms of zero-order Green functions of non-interacting excitons and exciton scattering matrix. Bozonization schemes may then be used173-176 to express the optical response through scattering of quasiparticles (rather than the more traditional picture of transitions among global eigenstates). Optical nonlinearities are generated by deviations from the linearly driven harmonic model which enter through anharmonicities, nonlinearities in the expansion of the polarization operator in powers of the primary variables, and the non-boson nature of the primary variables (deviations from boson statistics). These induce exciton scattering processes which in turn give rise to optical nonlinearities.
The dynamical NEE approach immediately cures many problems associated with the sum-over-states approach and provides an extremely useful physical insight with greatly reduced computational effort. Moreover, by describing the optical response in real space, it provides an intuitive picture, which is particularly suitable for the interpretation of femtosecond spectroscopies.
The NEE extend the semiconductor Bloch equations (SBE) which were successfully used to describe the optical response of semiconductor systems (bulk, quantum dots, quantum wells, and superlattices). The two share several important fundamental similarities.17,35,153,177-183 Femtosecond techniques probe the interplay of coherent and incoherent dynamics, elastic and inelastic scattering, and self-trapping of excitons. The Wannier-type excitons in semiconductors are formed by an electron in the conduction band and a hole in the valence band. Molecular excitations moving coherently across the system (Frenkel excitons) can be also considered as electron-hole pairs with the constraint that the electron and the hole must reside on the same molecule at all times. Due to the absence of intermolecular charge transfer in molecular assemblies, the number of Frenkel oneexciton states scales, ∼ N, with the number of molecules N, whereas the number of Wannier excitons (we refer to all electron-hole pair states as excitons regardless of whether their relative motion is bound or not) scales ∼ N 2. Similarly, the number of two
exciton states scales ∼ N 2 and ∼ N 4, respectively. Due
to this difference,184 the higher level NEE which, unlike the SBE, properly account for the structure of two-exciton resonances can be more easily utilized in the modeling of molecular nanostructures.
8. Acknowledgments
The support of the National Institutes of Health grant no. 1 RO1 GM59230-10A2 is gratefully acknowledged. This material is based upon work supported by the National Science Foundation grant no. CHE-0132571. We wish to thank Dr. Vladimir Chernyak who was instrumental in developing the present formalism. We thank Wei Zhuang and Ravindra Venkatramani for most useful discussions.
9. Appendix A. The Generalized Frenkel Exciton Hamiltonian
The Hamiltonian of an aggregate made of molecules with non-overlapping charge distributions, Hˆ S (the first term in eq 4.1), may be expanded in the basis set of individual chromophores:143
where Fm
ab ≡ |ma〉〈mb| is a complete set of operators of the mth molecule, a,b,c,d ) 0 ..., M run over the molecular states, 0 being the ground state, and Hma and H mn
ab,cd are matrix elements. The first term describes the isolated molecules and the second represents intermolecular interactions. The operators Fm
ab can be recast using exciton creation, Bˆ ma
† ≡ |ma〉〈m0|, and annihilation operators, Bˆ ma ≡ |m0〉〈ma|, where a and b ) 1, ..., M. These satisfy the Pauli commutation relations:
Using these definitions we get Fm
ab ) Bˆ ma
† Bˆ mb, Fm
a0 )
Hˆ S ) ∑m a ∑
HmaFm
aa + m∑n
m*n
∑
abcd
H mn
ab,cdFm
abFn
cd (A1)
[Bˆ ma,Bˆ nb
† ] ) δm,nδa,b(1 - ∑c
Bˆ mc
† Bˆ mc) - δm,nBˆ mb
† Bˆ ma
(A2)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2091


 Bˆ ma
† , Fm
0a ) Bˆ ma, and Fm
00 ) 1 - ∑aBˆ ma
† Bˆ ma. Substituting these in eq A1, we get32
where
Equations A3-A7 constitute the most general form of the exciton Hamiltonian.1-3,32 All coefficients Ωma,
V′ma, V′m′ a, V′m′′,ab, Jma,nb, Km,n
ab,cd, U′ma,nb, U′m′ a,nb, W′a,bc
m,n,
and W′′ab,c
m,n are linear combinations of Hma and H mn
ab,cd.
Hˆ 1 represents the isolated molecule and Hˆ 3 represents the contribution of the electric field on each chromophore created by other molecules of the aggregate. The local field shifts the energy of the state (Ωma * Hma) and couples the various energy levels through the terms V′ma, V′m′ a, and V′m′′,ab. Hˆ 3 is a
single-molecule coupling term which can be eliminated by rediagonalizing the single-chromophore Hamiltonians. The coupling between chromophores is represented by ˆH2 and Hˆ 4. ˆH2 has quadratic Jma,nb and quartic Km,n
ab,cd resonant couplings which conserve the number of excitons. ˆH4 couples states with different number of excitons. All parameters can be obtained using, e.g., time-dependent density functional theory (TDDFT) computations of excited states of individual chromophores.32 When the intermolecular coupling Hmn
ab,cd (typically smaller than 500 cm-1 in molecular aggregates) is much smaller than the transition energies Hma
(∼20 000 cm-1), the off-resonant terms given by Hˆ 3 and Hˆ 4 make negligible contributions to the optical response and may be neglected. This results in the Hamiltonian, eq 4.2. This approximation also typically holds for coupled vibrational chromophores.
10. Appendix B. Mapping Molecular Aggregates onto the Fluctuating Multilevel Model
We consider a molecular aggregate made of N interacting two-level chromophores (M ) 1), as
shown in Figure 1. Setting a ) b ) 1 in eq 4.2, we get
with the polarization operator
With this Hamiltonian, only the optical field can change the number of excitons and only two groups of resonant excited states (one- and two-exciton states) contribute to the third-order optical signals (see Figures 1 and 3). The third-order response depends on the ground state of the aggregate (where all chromophores are in their ground states), N oneexciton states, and N(N - 1)/2 two-exciton states. These eigenstates can be obtained by diagonalizing the relevant blocks of the Hamiltonian. The one- and two-exciton energies will be denoted as R and Rˆ, respectively, with the corresponding wave functions:
and
Equation B3 defines the one-exciton creation, bˆR
†, and annihilation operators, bˆR, whereas eq B4 defines the two-exciton creation, ˆcjR
†, and annihilation operators, cˆ jR. The two-exciton states are obtained by acting with two-exciton creation operators cˆ† which are bilinear combinations of the one-exciton creation operators Bˆ †. All parameters of the fluctuating exciton Hamiltonian (eqs 5.1 and 5.2) may be obtained from the aggregate Hamiltonian (eq B1) by applying transformations involving the exciton eigenstates, ÊR(m) and ψjR(mn). We define the transformation matrices:
and
Using these operators, the exciton Hamiltonian (eqs B1 with B2) can be recast in the form
with the polarization operator
Hˆ S ) ∑m
ΩmBˆ m
† Bˆ m + m∑n
m*n
(Jm,n Bˆ m
† Bˆ n +
Km,n Bˆ m
† Bˆ n
†Bˆ mBˆ n) (B1)
Pˆ )∑m
μm(Bˆ m
† + Bˆ m) (B2)
bˆ R
†|0〉 ≡ ∑m
ÊR(m)Bˆ m
† |0〉 (B3)
cˆ jR
† |0〉 ≡ m,n;∑m<n
ψjR(mn)Bˆ m
+Bˆ n
+|0〉 (B4)
T R,‚;mn
(1) ≡ ÊR(m)Ê‚(n) (B5)
T jR,h‚;mn
(2) ≡ ∑k
(ψjR(mk) + ψjR(km))(ψh‚(nk) + ψh‚(kn))
(B6)
Hˆ ) ∑R
Rbˆ R
†bˆ R + j ∑R
jRcˆ jR
†cˆ jR - Pˆ ‚E(r,t) + Hˆ SB (B7)
Pˆ ) ∑R
μR(bˆ R + bˆ R
†) + ∑R ∑h‚
μR,h‚(bˆ R
† cˆ h‚ + cˆ h‚
†bˆR) (B8)
Hˆ S ) Hˆ 1 + Hˆ 2 + Hˆ 3 + Hˆ 4 (A3)
Hˆ 1 ) ∑m ∑a
ΩmaBˆ ma
† Bˆ ma (A4)
Hˆ 2 ) m∑n
m*n{ a∑b
Jma,nbBˆ ma
† Bˆ nb +
∑
abcd
K m,n
ab,cdBˆ ma
† Bˆ nc
† Bˆ mbBˆ nd} (A5)
Hˆ 3 ) ∑m { a ∑
(V ′maBˆ ma
† + V ′m′ aBˆ ma) +
∑
ab
a*b
V ′m′′,abBˆ ma
† Bˆ mb} (A6)
Hˆ 4 ) m∑n
m*n{ a∑b
(U′ma,nb Bˆ ma
† Bˆ nb
† + U′m′ a,nb Bˆ maBˆ nb) +
∑
abc
(W′a,bc
m,n Bˆ ma
† Bˆ nb
† Bˆ nc + W′′ab,c
m,n Bˆ ma
† Bˆ mbBˆ nc)} (A7)
2092 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 The excitonic transition dipole moments μR and μR,‚ˆ reflect optical transitions to the exciton state R and among exciton states (belonging to different manifolds) R and ‚h, respectively. The transition dipole moments are given by
The coupling of the system with the bath is now given by
Here, QR,‚
(c) are collective bath coordinates in the exciton basis set. Since our Hamiltonian conserves the number of excitons, exciton hopping can take place only within the one-exciton or the two-exciton manifolds; bath-induced relaxation between these manifolds is not allowed. The collective bath coordinates are then simply given by
The spectral densities in the exciton basis set are similarly obtained from their local basis set counterparts:
where the molecular spectral densities were defined by eq 4.8. Equtions B7 and B8 are identical to eqs 5.1 and 5.2. Thus, the molecular aggregate Hamiltonian (eq B1) has been reduced to a fluctuating multilevel system. Correlations among fluctuations in the eigenstate basis may arise either from delocalized primary coordinates, which induce correlated fluctuations in different molecules, or from through-space couplings in the system, which connect different locally uncorrelated modes.
11. Appendix C: The Master Equation for Incoherent Exciton Hopping
The Green function of eq 87 satisfies the master equation (eq 88):101
Invoking the Markovian approximation, Kab reads
where Kh ab is given by a sum of two correlation functions related to off-diagonal fluctuations of the Hamiltonian,
where
The density matrix jFb represents a bath-equilibrated excited state, which is given by
and jFg is the equilibrium ground state.
Kh ab depends on the off-diagonal spectral broadening functions:
We then have
Here a “dot” stands for a time derivative, and
where we have also defined
12. Appendix D: The Doorway and the Window Functions
The incoherent doorway and window terms in eq 5.30 may be expressed using the line-broadening functions.101 SD(t3,∞,t1) accounts for part of the total response function (related to the system without the off-diagonal system-bath interactions) associated
μa ) ∑m
μmÊR(m) (B9)
μR,h‚ ) m∑,n
ψh‚(mn)(ÊR(m)μn + ÊR(n)μm) (B10)
Hˆ SB ) ∑
R,‚
QR‚
(c)bˆ R
†bˆ‚ + ∑
jR,h‚
Q jR h‚
(c)cˆ jR
†cˆ h‚ (B11)
QR,‚
(c) ) m∑,n
Qmn
(c) T R‚,mn
(1) (B12)
Q jR, h‚
(c) ) m∑,n
Qmn
(c) T jRh‚,mn
(2) (B13)
C′′′e
R‚,R′‚′(ω) ) mn∑m′n′
T R‚,mn
(1) T R′‚′,m′n′
(1) C′m′ n,m′n′(ω)
(B14)
C′′′e
R‚,jRh‚′(ω) ) mn∑m′n′
T R‚,mn
(1) T jR′h‚′,m′n′
(2) C′m′ n,m′n′(ω) (B15)
C′′′e
jRh‚,R′‚′(ω) ) mn∑m′n′
T jRh‚,mn
(2) T R′‚′,m′n′
(1) C′m′ n,m′n′(ω) (B16)
C′′′e
ˆRh‚, ˆR′h‚′(ω) ) mn∑m′n′
T jRh‚,mn
(2) T jR′h‚′,m′n′
(2) C′m′ n,m′n′(ω) (B17)
d
dtGba(t) )∑c
[KbcGca(t) - KcbGba(t)] (C1)
Kab ) ∫0
∞ dt Kh ab(t) (C2)
Kh ab(t) ) K ab
L (t) + (K ab
L (t))* (C3)
Kh ab(t) ) 〈Bb
†(t)Ba(t)Qba
(C)(t)Ba
†(0)Bb(0)Qab
(C)(0)jFb〉 (C4)
jFb ) ltifm∞ exp(-iL0t)Bb
†jFgBb (C5)
gab,cd(t)∫-∞
∞ dω 2π
1 - cos(ωt)
ω2 coth( pω
2kBT)C′a′b,cd(ω) +
i∫-∞
∞ dω 2π
sin(ωt) - ωt
ω2 C′a′b,cd(ω) (C6)
K ba
L (t) ) K ba
F (t){  ̈gb,a,a,b(t) - [g ̆ a,b,a,a(t) - g ̆ a,b,b,b(t) +
2iλa,b,a,a][g ̆ a,a,b,a(t) - g ̆ b,b,b,a(t) +
2iλb,a,a,a]} for t > 0 (C7)
K ba
F (t) ) exp[-i(Ωb - Ωa)t - gb,b,b,b(t) - ga,a,a,a(t) +
ga,a,b,b(t) + gb,b,a,a(t) - 2i(λa,a,a,a - λb,b,a,a)t] (C8)
λb,a,b′,a′ ) -ltifm∞ Im(dgb,a,b′,a′(t)
dt ) (C9)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2093


 with excited-state populations. This function may in turn be expressed in terms of the doorway and windows functions, Da(t) and Wa(t):
where
Here,
and
Using the second-order cumulant expansion, the correlation functions are expressed in terms of the line-broadening functions:
The ground-state doorway and window functions are given by
13. Appendix E: The NEE Matrix
In this appendix we define the matrices appearing in eqs 6.7-6.10 (L, K, E, and F). The L terms are defined as follows:
where hma,ld ) Ωmaδma,ld + Jmald(1 - δml) and δma,ld ≡
δm,lδa,d.
The two-exciton terms are given by
Note that Yma,mb ) 0 and Zma,nb,nc ) 0. The linear interaction with the optical field is
For the nonlinear part of the interaction we have
where Em,ad ) -μm,adE(t).
14. Appendix F: Derivation of the Relaxation Matrices
The relaxation terms in the NEE are calculated using the first-order coupled variables:143
SOD(t3,∞,t1) ) ∑a
Wa(t3)Da(t1) + Wg(t3)Dg(t1) (D1)
Da(t) ) Da
L(t) + Da
L(-t) (D2)
Wa(t) ) Wa
L(t) - Wa
L(-t) (D3)
Da
L(t) ) -μa
2〈Ba(t)Ba
†(0)jFg〉 (D4)
Wa
L(t) ) iμa
2〈Ba
†(0)Ba(t)jFa〉 
iμab
2 〈Ba
†(t)Bb(t)Bb
†(0)Ba(0)Fa〉 (D5)
Da
L(t) ) -μa
2 exp[-iΩat - gaa(t)] (D6)
Wa
L(t) ) iμa
2 exp(-iΩat - gaa
/ (t) + 2iλaat) 
i∑b
μab
2 exp(-i(Ωb - Ωa)t - gaa(t) - gbb(t) +
2gab(t) + 2i(λab - λaa)t) (D6)
Dg(t) ) -∑a
Da(t) (D7)
Wg(t) ) i∑a
(Da
L(t) - Da
L(-t)) (D9)
(LB)ma ) l∑d
-hma,ldBld (E1)
(LY)ma,nb ) l∑d
-hma,ldYld,nb - hnb,ldYma,ld (E2)
(LN)ma,nb ) l∑d
hld,maNld,nb - hnb,ldNma,ld (E3)
(LZ)ma,nb,kc ) l∑d
hld,maZld,nb,kc - hnb,ldZma,ld,kc 
hkc,ldZma,nb,ld (E4)
(KB)ma ) ld∑d′
(hma,ld′Zmd,md,ld′ + hmd,ld′Zmd,ma,ld′) 
∑
ld
(Kl,m
dd,aa + Km,l
aa,dd)Zld,ld,ma (E5)
(KY)ma,nb )δm,n[ l∑d
(hma,ldYld,ma + hmb,ldYma,ld) +
(EmaBmb + EmbBma) +
∑
d
(Em,adYmd,mb + Em,bdYma,md)] (E6)
(KZ)ma,nb,kc ) δn,k[ l∑d
(-hld,maZld,nb,nc +
hnb,ldZma,ld,nc) + hnc,ldZma,nb,ld - EmaYnb,nc +
EnbNma,nc + EncNma,nb] (E7)
(EB)ma ≡ Ema ) -μmaE(t) (E8)
(F B)ma ) ∑d
(EmaNmd,md + EmdNmd,ma - Em,adBmd)
(E9)
(F Y)ma,nb ) -(EmaBnb + EnbBma) 
∑
d
(Em,adYmd,nb + En,bdYma,nd) (E10)
(F N)ma,nb ) (EmaBnb - EnbBma
/ ) + ∑d
(Em,adNmd,nb 
En,bdNma,nd) (E11)
(F Z)ma,nb,kc ) (EmaYnb,kc - EnbNma,kc - EkcNma,nb)
(E12)
〈Bˆ maQj〉 ≡ Bh ma,j
q (F1)
〈Bˆ maBˆ nbQj〉 ≡ Yh manb,j
q (F2)
〈Bˆ ma
† Bˆ nbQj〉 ≡ Nh manb,j
q (F3)
〈Bˆ ma
† Bˆ nbBˆ kcQj〉 ≡ hZ manbkc,j
q (F4)
2094 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 and
To find the evolution of the coupled variables, we write their Heisenberg equations. We assume that the bath oscillators are independent. We also neglect nonlinear terms and terms in the equations for the coupled variables which depend on the optical field. We can then factorize the second-order coupled terms:
The resulting equations for the first-order coupled variables are
Similarly:
and finally:
Here we used uj ) Mj
-1, vj ) -Mj Ωh 2, and wj ) 〈QsQs〉, and [Ps,Qs] ) -i, 〈PsQs〉 ) -i/2, and 〈QsQs〉 ) 1/(2Mj Ωh j) coth(p Ωh j/(2kBT)). The equations are solved to second order in the system-bath interaction. We next construct a general form of the solution of the equations for the coupled system-bath. For arbitrary variables Aq and Ap satisfying the equations
the general solution reads
〈Bˆ maPj〉 ≡ Bh ma,j
p (F5)
〈Bˆ maBˆ nbPj〉 ≡ Yh manb,j
p (F6)
〈Bˆ ma
† Bˆ nbPj〉 ≡ Nh manb,j
p (F7)
〈Bˆ ma
† Bˆ nbBˆ kcPj〉 ≡ Zh manbkc,j
p (F8)
〈Bˆ ma
† ...Bˆ nb
† Bˆ kc...Bˆ ldQjQj〉 ) 〈Bˆ ma
† ...Bˆ nb
† Bˆ kc...Bˆ ld〉〈QjQj〉
(F9)
〈Bˆ ma
† ... ˆBnb
† ˆBkc... ˆBldPjQj〉 ) 〈Bˆ ma
† ...Bˆ nb
† Bˆ kc...Bˆ ld〉〈PjQj〉
(F10)
-i
∂Bh ma,j
q
∂t ) - l∑d
hma,ldBh ld,j
q - iujBh ma,j
p
wj l∑d
hhmald,jBld (F11)
-i
∂Yh manb,j
q
∂t ) l∑d
(-hma,ld Yh ldnb,j
q - hnb,ld Yh mald,j
q )
iujYh manb,j
p + wj l∑d
(-hh mald,jYld,nb - hh nbld,jYma,ld)
(F12)
-i
∂Nh manb,j
q
∂t ) l∑d
(hma,ld Nh ldnb,j
q - hnb,ld Nh mald,j
q )
iujNh manb,j
p + wjm∑′a′
(hh mald,jNld,nb - hh nbld,jNma,ld)
(F13)
-i
∂Zh manbkc,j
q
∂t ) l∑d
(hma,ldZh ldnbkc,j
q - hnb,ldZh maldkc,j
q
hkc,ld Zh manbld,j
q ) - iuj Zh manbkc,j
p+
wj l∑d
(hh mald,jZld,nb,kc - hh nbld,jZma,ld,kc 
hh kcld,j Zma,nb,ld) (F14)
-i
∂Bh ma,j
p
∂t ) - l∑d
hma,ld Bh ld,j
p - ivj Bh ma,j
q
i
2 l∑d
hhmald,jBld (F15)
-i
∂ hY manb,j
p
∂t ) l∑d
(-hma,ld hY ldnb,j
p - hnb,ld hY mald,j
p )
ivj hY manb,j
q -i
2 l∑d
(- hhmald,jYld,nb - hhnbld,jYma,ld) (F16)
-i
∂Nh manb,j
p
∂t ) l∑d
(hma,ld Nh ldnb,j
p - hnb,ld Nh mald,j
p )
ivj Nh manb,j
q +i
2 l∑d
( hhmald,jNld,nb + hhnbld,jNma,ld) (F17)
-i
∂Zh manbkc,j
p
∂t ) l∑d
(hma,ld Zh ldnbkc,j
p - hnb,ld hZmaldkc,j
p
hkc,ld Zh manbld,j
p ) - ivj hZmanbkc,j
q +i
2 l∑d
( hhmald,j Zld,nb,kc +
hhnbld,jZma,ld,kc + hhkcld,jZma,nb,ld) (F18)
-i∂Qj
∂t ) -iMj
-1Pj (F19)
-i
∂Pj
∂t ) iMj Ωh 2Qj + ima∑nb
hh manb,jNma,nb (F20)
i∂Aq
∂t - hAAq - i
MAp ) W q(t) (F21)
i∂Ap
∂t - hAAp - iM Ωh 2Aq ) W p(t) (F22)
Aq(t) ) -i∫0
∞ dτ[cos(Ωh τ)GA(τ)W q(t - τ) +
1
MΩh sin(Ωh τ)GA(τ)Wp(t - τ)] (F23)
Ap(t) ) -i∫0
∞ dτ[cos(Ωh τ)GA(τ)W p(t - τ) 
M Ωh sin(Ωh τ)GA(τ)W q(t - τ)] (F24)
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2095


 where GA(τ) ) exp(ihAτ) is a Green function of the equation
Using eq F23, we can obtain all four relaxation terms in the NEE. Since we are using a simplified form of the relaxation terms for the Y and the Z variables, we need the solutions for Bh ma,j
q and
Nh manb,j
q , which are given in eqs 6.32 and 6.35.
15. Appendix G: Relaxation Rates for the Overdamped Brownian Oscillator Spectral Density
The four-point spectral density similar to eqs 4.9 and 4.16 contains all relevant information on the bath:143
We define the matrix of phonon Green function corresponding to extension of eq 6.33:143
Using eqs G1, G2, and 6.34, RB can be rewritten: RN can be also expressed using eqs G1, G2, and
6.36:
In the following we will use the overdamped Brownian oscillator spectral density (eq 4.18) for the
bath:57,169
The relaxation terms are then expressed using a Fourier transform of the phonon Green function withthe Lorentzian spectral density. Thus, we define the functions:
leading to169
Here, vq ) 2πqkBT are the Matsubara frequencies. Using the Green function expressions (eq 6.20), RB becomes
where Ah manb,kcld ≡ λ hh manb hh kcld and ωR1,R2 ) R1 - R2.
RN can also be rewritten in terms of the function Φ((ω) using the same Green function (eq 6.20):
16. References
(1) Davydov, A. S. Theory of Molecular Excitons; McGraw-Hill: New York, 1962.
(2) Silinsh, E. A.; Capek, V. Organic Molecular Crystals: Interaction, Localization and Transport Phenomena; AIP Press: New York, 1994.
(3) Pope, M.; Swenberg, C. E. Electron Processes in Organic Crystals; Oxford University Press: New York/Oxford, 1999. (4) Juzeliunas, G.; Knoester, J. J. Chem. Phys. 2000, 112, 2325. Didraga, C.; Knoester, J. J. Lumin. 2003, 102-103, 60. Bednarz, M.; Malyshev, V. A.; Knoester, J. Phys. Rev. Lett. 2003, 91, 217401. (5) Kamalov, V. F.; Struganova, I. A.; Yoshihara, K. Chem. Phys. Lett. 1993, 213, 559.
(6) Gadonas, R.; Feller, K. H.; Pugzlys, A. Opt. Commun. 1994, 112, 157. Gaizauskas, E.; Feller, K. H.; Gadonas, R. Opt. Commun. 1995, 118, 360. (7) Misawa, K.; Machida, S.; Horie, K.; Kobayashi, T. Chem. Phys. Lett. 1995, 240, 210. Misawa, K.; Kobayashi, T. Nonlin. Opt. 1996, 15, 81. Kobayashi, T. Mol. Cryst. Liq. Cryst. 1996, 283, 17. (8) Kobayashi, T. J-aggregates; World Scientific: Singapore, 1996. (9) van Amerogen, H.; Valkunas, L.; van Grondelle, R. Photosynthetic Excitons; World Scientific: Singapore, 2000. (10) Andrews, D. L.; Demidov, A. A. Resonance Energy Transfer; John Wiley & Sons: New York, 1999.
i∂G
∂τ - hAG ) iδ(τ) (F25)
C′m′ anb, m′a′n′b′(ω) ) ∑j
hh manb,j hh m′a′n′b′,j
2Mj Ωh j
2π{δ(ω - Ωh j) - δ(ω + Ωh j)} (G1)
M(τ) ) 1
2 ∫-∞
+∞ dω
2π C′′(ω){coth( pω
2kBT) cos(ωτ) 
i sin(ωτ)} (G2)
Rma,m′a′
B)
∑
m′′a′′ ∫-∞
+∞ dτkc,∑k′c′
Gkc,k′c′
B (τ)Mmakc,k′c′m′′a′′(τ)Gm′′a′′,m′a′
B† (τ)
(G3)
Rmanb,m′a′n′b′
N ) m′′a′∑′n′′b′′ ∫0
∞ dτ kc∑ld
{Gkc,ld
B† (τ)Gnb,n′′b′′
B (τ)
Mma,kc;ld,m′′a′′(-τ) + Gma,m′′a′′
B† (τ)Gkc,ld
B (τ)Mnb,kc;ld,n′′b′′(τ) 
Gkc,m′′a′′
B† (τ)Gnb,ld
B (τ)Mma,kc;ld,n′′b′′(τ) - Gma,ld
B† (τ)Gkc,n′′b′′
B (τ)
Mnb,kc;ld,m′′a′′(-τ)}Gm′′a′′,m′a′
B (τ)Gn′′b′′,n′b′
B† (τ) (G4)
C′′manb,m′a′n′b′(ω) ) hh manb hh m′a′n′b′2λ Λω
Λ2 + ω2 (G5)
Φ(ω)( ) 1
2∫0
∞ dt exp(iωt) ∫-∞
+∞dω
2π(coth( pω
2kBT)
cos(ωt) - i sin(ωt)) Λω
Λ2 + ω2 (G6)
Φ(ω)( ) (cot( pΛ
2kBT) - i) Λ
Λ - iω +
4kBTΛq∑)1
∞ νq
νq
2 + Λ2
1
νq - iω
(G7)
Rma,m′a′
B ) m′∑′a′′ kc,∑k′c′ R1 ∑R2
ÊR1(kc)ÊR1(k′c′)
ÊR2(ma′′a′′)ÊR2(m′a′)Ah makc,k′c′m′′a′′Φ+(ωR1,R2) (G8)
Rmanb,m′a′n′b′
N )∑
m′′a ′,n′′b′′ kc∑,ld R1R2 ∑R3R4
ΛÊR3(m′′a′′)
ÊR3(m′a′)ÊR4(n′′b′′)ÊR4(n′b′) ×
[Ah makc,ldm′′a′′Φ-(ωR2,R1 - ωR4,R3)ÊR1(kc)ÊR1(ld )
ÊR2(nb)ÊR2(n′′b′′) +
Ah nbkc,ldn′′b′′Φ+(ωR2,R1 - ωR4,R3)ÊR1(ma)ÊR1(m′′a′′)
ÊR2(kc)ÊR2(ld ) 
Ah makc,ldn′′b′′Φ+(ωR2,R1 - ωR4,R3)ÊR1(kc)ÊR1(m′′a′′)
ÊR2(nb)ÊR2(ld ) 
Ah nbkc,ldm′′a′′Φ-(ωR2,R1 - ωR4,R3)ÊR1(ma)ÊR1(ld )
ÊR2(kc)ÊR2(n′′b′′)] (G9)
2096 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius


 (11) Tretiak, S.; Middleton, C.; Chernyak, V.; Mukamel, S. J. Phys. Chem. B 2000, 104, 4519.
(12) van Grondelle, R.; Dekker, J. P.; Gillbro, T.; Sundstr ̈om, V. Biochim. Biophys. Acta 1994, 1187, 1.
(13) Sundstr ̈om, V.; van Grondelle, R. In Anoxygenic Photosynthetic Bacteria; Blankenship, R. E., Madiga, M. T., Baner, C., Eds.; Kluwer Academic: Dordrecht, 1995. (14) Zuber, H.; Brunishplz, R. A. Photosynthesis: Physical Mechanism and Chemical Patterns; Cambridge University Press: New York, 1980. (15) Scheer, H. Chlorophylls; CRC Press: Boca Raton/Ann Arbor/ Boston/London, 1991. (16) Damjanovic, A.; Kosztin, I.; Kleinekathofer, U.; Schulten, K. Phys. Rev. E 2002, 65, 031919.
(17) Mukamel, S.; Chemla, D. S. Chem. Phys. 1996, 210, Special Issue on Confined Excitations in Molecular and Semiconductor Nanostructures. (18) Forrest, S. R. Chem. Rev. 1997, 97, 1793. (19) McBranch, D. W.; Sinclair, M. B. In Primary Photoexcitations in Conjugated Polymers: Molecular Exciton versus Semiconductor Band Model; Sariciftci, N. S. Ed.; World Scientific Publishing: Singapore, 1997. (20) Puccetti, G.; Blanchard-Desce, M.; Ledoux, I.; Lehn, J. M.; Zyss, J. J. Phys. Chem. 1993, 97, 9385.
(21) Blanchard-Desce, M.; Wortmann, M.; Lebus, S.; Lehn, J.; Kramer, P. Chem. Phys. Lett. 1995, 243, 526.
(22) Blanchard-Desce, M.; Lehn, J. M.; Barzoukas, M.; Ledoux, I.; Zyss, J. Chem. Phys. 1994, 181, 281.
(23) Baldo, M. A.; Thompson, M. E.; Forrest, S. R. Nature 2000, 403, 750. (24) Monshower, R.; Abrahamsson, M.; van Mourik, F.; van Grondelle, R. J. Phys. Chem. B 1997, 101, 7241.
(25) Leupold, D.; Stiel, H.; Teuchner, K.; Nowak, F.; Saudner, W.; U ̈ cker, B.; Scheer, H. Phys. Rev. Lett. 1996, 77, 4675. (26) Wu, H. M.; Reddy, N. R. S.; Small, G. J. J. Phys. Chem. B 1997, 101, 651. (27) van Oien, A. M.; Ketlaars, M.; K ̈ohler, J.; Aartsma, T. J.; Schmidt, J. Science 1999, 285, 400. (28) Matsushita, Mf.; Ketlaars, M.; van Oien, A. M.; K ̈ohler, J.; Aartsma, T. J.; Schmidt, J. Biophys. J. 2001, 80, 1604. (29) Sumi, H. J. Phys. Chem. B 1999, 103, 252. (30) Scholes, G.; Fleming, G. R. J. Phys. Chem. B 2000, 104, 1854. (31) Juzeliunas, G.; Andrews, D. L. In Quantum Electrodynamics of Resonance Energy Transfer; Prigogine, I., Rice, S. A., Eds.; Advances in Chemical Physics 112; Wiley: New York, 2000. (32) Mukamel, S.; Berman, O. J. Chem. Phys. 2003, 119, 12194. (33) Wannier, G. H. Phys. Rev. 1937, 52, 191. Mott, N. F. Trans. Faraday Soc. 1938, 34, 500. (34) Sh  ̈afer, W.; Wegener, M. Semiconductor Optics and Transport Phenomena; Springer-Verlag: New York, 2002. Chemla, D. S.; Shah, J.; Nature 2001, 411, 549.
(35) Haug, H.; Koch, S. W. Quantum Theory of Optical and Electronic Properties of Semiconductors; World Scientific Ltd.: Singapore, 1993. (36) Davydov, A. S. Solitons in Biology; Elsevier: Dordrecht, 1989. (37) Kopelman, R. In Excited States; Lim, E. C., Ed.; Acedemic: New York, 1975. (38) Scott, A. C. Phys. Rep. 1992, 217, 1. (39) Torii, H.; Tasumi, M. J. Chem. Phys. 1992, 96, 3379. (40) Krimm, S.; Bandeker, J. J. Adv. Protein Chem. 1986, 38, 181. (41) Rubtsov, I. V.; Wang, J.; Hochstrasser, R. M. J. Phys. Chem. A 2003, 107, 3384. (42) Rubtsov, I. V.; Wang, J.; Hochstrasser, R. M. J. Chem. Phys. 2003, 118, 7733.
(43) Moran, A.; Mukamel, S. Proc. Natl. Acad. Sci. U.S.A. 2004, 101, 506-510.
(44) Krimm, S.; Abe, Y. Proc. Natl. Acad. Sci. U.S.A. 1972, 69, 2788. (45) Moore, W.; Krimm, S. Proc. Natl. Acad. Sci. U.S.A. 1975, 72, 4933. (46) Krimm, S.; Bandekar, J. J. Adv. Protein Chem. 1986, 38, 181. (47) Hamm, P.; DeGrado, W.; Hochstrasser, R. Proc. Natl. Acad. Sci. U.S.A. 1999, 96, 2036.
(48) Torii, H.; Tasumi, M. J. Raman Spectrosc. 1998, 29, 81.
(49) Creighton, T. E. Proteins: Structures and Molecular Properties, 2nd ed.; W. H. Freeman: New York, 1993. (50) Surewicz, W. K.; Mantch, H. H.; Chapman, D. Biochemistry 1993, 32, 389.
(51) Leckson, M.; Mantsch, H. Crit. Rev. Biochem. Mol. Biol. 1995, 30, 95. (52) Barth, A.; Zscherp, C. Q. Rev. Biophys. 2002, 35, 369. Surewicz, W. K.; Mantsch, H.; Chapman, D. Biochemistry 1993, 32, 389. Haris, P. I.; Chapman, D. Trends Biochem. Sci. 1992, 17, 328. Susi, H.; Byler, D. M. Methods Enzymol. 1986, 130, 290. (53) Kubelka, J.; Hofrichter, J.; Eaton, W. Curr. Opin. Struct. Biol. 2004, 14, 1.
(54) Torii, H.; Tasumi, M. In Infrared Spectroscopy of Biomolecules; Mantsch, H., Chapman, D., Eds.; Wilei-Liss: New York, 1996. (55) Torii, H.; Tasumi, M. J. Chem. Phys. 1992, 97, 92.
(56) Ultrafast Phenomena XIII; Miller, R. D., Muriname, M. M., Scherer, N. F., Weiner, A. M., Eds.; Springer: Berlin/Heidelberg, 2002.
(57) Mukamel, S. Principles of Nonlinear Optical Spectrscopy; Oxford University Press: New York, 1995.
(58) Fleming, G. R. Chemical Applications of Ultrafast Spectroscopy; International Series of Monographs on Chemistry 13; Oxford University Press: New York, 1994. (59) Weiner, A. W.; Leird, D. E.; Weiderrecht, G. P.; Nelson, K. A. Science 1990, 247, 1317.
(60) Tull, J. X.; Dugan, M. A.; Warren, W. S. Adv. Magn. Opt. Reson. 1997, 20, 1. Tull, J. X.; Dugan, M. A.; Warren, W. S. J. Opt. Sci. Am. B 1997, 14, 2348.
(61) Scherer, N. F.; Carlson, R. J.; Matro, A.; Du, M.; Rugiero, A. J.; Romero-Rochin, V.; Cina, J. A.; Fleming, G. R.; Rice, S. A. J. Chem. Phys. 1991, 95, 1487. (62) Dantus, M. Annu. Rev. Phys. Chem. 2001, 52, 639.
(63) Rabitz, H.; de Vivie-Riedle, R.; Motzkus, M.; Kompa, K. Science 2000, 288, 824. (64) Brixner, T.; Krampert, G.; Niklaus, P.; Gerber, G. Appl. Phys. B: Lasers Opt. 2002, 74, S133.
(65) Chernyak, V.; Mukamel, S. J. Chem. Phys. 1998, 108, 5812. (66) Bergt, M.; Brixner, T.; Kiefer, B.; Strehle, M.; Gerber, G. J. Phys. Chem. A 1999, 103, 10381.
(67) Ernst, R. R.; Bodenhausen, G.; Wokaun, A. Principles of Nuclear Magnetic Resonance in One and Two Dimensions; Clarendon Press: Oxford, 1987. Sanders, J. K. M.; Hunter, B. K. Modern NMR Spectroscopy; Oxford: New York, 1993.
(68) Evans, J. N. Biomolecular NMR Spectroscopy; Oxford: New York, 1995. (69) Tanimura, Y.; Mukamel, S. J. Chem. Phys. 1993, 99, 9496. (70) Mukamel, S. Annu. Rev. Phys. Chem. 2000, 51, 691.
(71) Mukamel, S., Hochstrasser, R. M., Eds. Chem. Phys. 2001, 266 (2/3), Special Issue on Multidimensional Spectroscopies. (72) Okumura, K.; Tanimura, Y. J. Phys. Chem. A 2003, 107, 8092. (73) Ohta, K.; Yang, M.; Fleming, G. J. Chem. Phys. 2001, 115, 7609. (74) Hamm, P.; Hochstrasser, R. M. Structure and dynamics of proteins and peptides: femtosecond two-dimensional spectroscopy. In Ultrafast Infrared and Raman Spectroscopy; Fayer, M. D., Ed.; Marcel Dekker Inc.: New York, 2001. (75) Hamm, P.; Lim, M.; DeGrado, W. F.; Hochstrasser, R. M. J. Chem. Phys. 2000, 112, 1907.
(76) Khalil, M.; Tokmakoff, A. Chem. Phys. 2001, 266, 213. Zimdars, D.; Tokmakof, A.; Chen, S.; Greenfield, S. R.; Faier, M. D. Smith, T. I.; Schwettman, H. A. Phys. Rev. Lett. 1993, 70, 2718. Golonzka, O.; Khalil, M.; Demirdoven, N.; Tokmakof, A. Phys. Rev. Lett. 2001, 86, 2154.
(77) Bredenbeck, J.; Helbing, J.; Behrendt, R.; Renner, C.; Moroder, L.; Wachtveitl, J.; Hamm, P. J. Phys. Chem. B 2003, 107, 7654. (78) Zhang, W. M.; Cherniak, V.; Mukamel, S. J. Chem. Phys. 1999, 110, 5011. (79) Zanni, M. T.; Ge, N.; Kim, Y. S.; Hochstrasser, R. M. Proc. Natl. Acad. Sci. U.S.A. 2001, 98, 11265.
(80) Ge, N.; Zanni, M. T.; Hochstrasser, R. M. J. Phys. Chem. A 2002, 106, 962. (81) Hamm, P.; Lim, M.; Hochstrasser, R. M. J. Phys. Chem. B 1998, 102, 6123. (82) Hamm, P. Chem. Phys. 1995, 200, 415. (83) Joo, T.; Albrecht, A. C. Chem. Phys. 1993, 176, 233. (84) Joo, T.; Jia, Y. W.; Yu, J. Y.; Jonas, D. M.; Fleming, G. R. J. Phys. Chem. 1996, 100, 2399.
(85) Jimenez, R.; van Mourik, F.; Yu, J. Y.; Fleming, G. R. J. Phys. Chem. B 1997, 101, 7350.
(86) Deak, J. C.; Rhea, S. T.; Iwaki, L. K.; Dlott, D. D. J. Phys. Chem. A 2000, 104, 4866. Iwaki, L. K.; Dlott, D. D. J. Phys. Chem. A 2000, 104, 9101. (87) Scheurer, C.; Mukamel, S. J. Chem. Phys. 2002, 116, 6803. (88) Gaffney, K. J.; Davis, P. H.; Piletic, I. R.; Levinger, N. E.; Fayer, M. D. J. Phys. Chem. A 2002, 106, 12012. Asbury, J. B.; Steinel, T.; Stromberg, C.; Gaffney, K. J.; Piletic, I. R.; Goun, A.; Fayer, M. D. Phys. Rev. Lett. 2003, 91, 237402. Asbury, J. B.; Steinel, T.; Stromberg, C.; Gaffney, K. J.; Piletic, I. R.; Fayer, M. D. J. Chem. Phys. 2003, 119, 12981.
(89) Tian, P.; Keusters, D.; Suzaki Y.; Warren, W. S. Science 2003, 300, 1553. Hybl, J. D.; Ferro, A. A.; Jonas, D. M. J. Chem. Phys. 2001, 115, 6606. (90) Pullerits, T.; Chachisvilis, M.; Sundstr ̈om, V. J. Phys. Chem. 1996, 100, 10787. Pullerits, T.; Chachisvilis, M.; Jones, M. R.; Hunter, C. N.; Sundstro ̈m, V. Chem. Phys. Lett. 1994, 224, 355. (91) Nagarajan, V.; Alden, R. G.; Williams, J. C.; Parson, W. W. Proc. Natl. Acad. Sci. U.S.A. 1996, 93, 13774.
(92) Bradforth, S. E.; Jimenez, R.; van Mourik, R.; van Grondelle, R.; Fleming, G. R. J. Phys. Chem. 1995, 99, 16179. Jimenez, R.; Dikshit, S. N.; Bradforth, S. E.; Fleming, G. R. J. Phys. Chem. 1996, 100, 6825. (93) Yu, J. Y.; Nagasawa, Y.; van Grondelle, R.; Fleming, G. R. Chem. Phys. Lett. 1997, 280, 404.
Many-Body Approaches to Exciton Modeling Chemical Reviews, 2004, Vol. 104, No. 4 2097


 (94) Reddy, N. R. S.; Cogdell, R. J.; Zhao, L.; Small, G. J. Photochem. Photobiol. 1993, 57, 35. Reddy, N. R. S.; Small, G. J.; Seibert, M.; Picorel, R. Chem. Phys. Lett. 1991, 181, 391. (95) Caro, C. D.; Visschers, R. W.; van Grondelle, R.; Vo ̈lker, S. J. Phys. Chem. 1994, 98, 10584.
(96) van der Laan, H.; Schmidt, T.; Visschers, R. W.; Visschers, K. J.; van Grondelle, R.; Vo ̈lker, S. Chem. Phys. Lett. 1990, 170, 231. (97) Milota, F.; Tortschanoff, A.; Sperling, J.; Kuna, L.; Sz ̈ocs, V.; Kauffmann, H. F. Appl. Phys. A 2004, 78, 497. Milota, F.; Sperling, J.; Szo ̈cs, V.; Tortschanoff, A.; Kauffmann, H. F. J. Chem. Phys. 2004, in press.
(98) Hu, X.; Schulten, K. Phys. Today 1997, 28 (Aug). (99) Hoff, A. J.; Deisenhofer, J. Phys. Rep. 1997, 287, 1. (100) Pullerits T.; Sundstr ̈om, V. Acc. Chem. Res. 1996, 29, 381. (101) Zhang, W. M.; Meier, T.; Chernyak, V.; Mukamel, S. J. Chem. Phys. 1998, 108, 7763. Zhang, W. M.; Meier, T.; Chernyak, V.; Mukamel, S. Philos. Trans. R. Soc. London, Ser. A 1998, 356, 405. (102) Herek, J. L.; Polivka, T.; Pullerits, T.; Fowler, G. J. S.; Hunter, C. N.; Sundstrom, V. Biochemistry 1998, 37, 7057. (103) Abramavicius, D.; Gulbinas, V.; Valkunas, L.; Shiu, Y.-J.; Liang, K. K.; Hayashi, M.; Lin, S. H. J. Phys. Chem. A 2002, 106, 8864. (104) Chachisvilis, M.; Zewail, A. H. J. Phys. Chem. A 1999, 103, 7408. Zewail, A. H. Femtochemistry-Ultrafast Dynamics of the Chemical Bond; World Scientific: New Jersey, Singapore, 1994; 20th Century Chemistry Series, Vols I and II. (105) Sperling, J.; Milota, F.; Tortschanoff, A.; Warmuth, C.; Mollay, B.; Ba ̈ ssler, H.; Kauffmann, H. F. J. Chem. Phys. 2002, 117, 10877. (106) Tokmakoff, A.; Lang, M. J.; Larson, D. S.; Fleming, G. R.; Chernyak, V.; Mukamel, S. Phys. Rev. Lett. 1997, 79, 2702. (107) Mukamel, S.; Piryatinski, A.; Chernyak, V. Acc. Chem. Res. 1999, 32, 145. (108) Piryatinski, A.; Lawrence, C. P.; Skinner, J. L. J. Chem. Phys. 2003, 118, 9672. (109) Piryatinski, A.; Lawrence, C. P.; Skinner, J. L. J. Chem. Phys 2003, 118, 9664. (110) Lawrence, C. P.; Skinner, J. L. J. Chem. Phys 2003, 119, 1623. (111) Lawrence, C. P.; Skinner, J. L. J. Chem. Phys 2003, 119, 3840. (112) Merchant, K. A.; Xu, Q. H.; Thompson, D. E.; Fayer, M. D. J. Phys. Chem. A 2002, 106, 8839.
(113) Gaffney, K. J.; Piletic, I. R.; Fayer, M. D. J. Phys. Chem. A 2002, 106, 9428. (114) De `ak, J. C.; Iwaki, L. K.; Dlott, D. D. J. Phys. Chem. A 1998, 102, 8193. Dea` k, J. C.; Iwaki, L. K.; Dlott, D. D. Chem. Phys. Lett. 1998, 293, 405. (115) Fain, B. Irreversibilities in Quantum Mechanics; Kluwer Academic Publishers: Dordrecht/Boston/London, 2000. (116) Mukamel, S. Phys. Rev. A 1983, 28, 3480. (117) Dreyer, J.; Moran, A.; Mukamel, S. J. Phys. Chem. B 2003, 107, 5967. (118) Venkatramani, R.; Mukamel, S. J. Chem. Phys. 2002, 117, 11089. (119) Meier, T.; Cherniak, V.; Mukamel, S. J. Chem. Phys. 1997, 107, 8759. (120) Sung, J.; Silbey, R. J. J. Chem. Phys. 2001, 115, 9266. (121) Larsen, D. S.; Ohta, K.; Xu, Q. H.; Cyrier, M.; Fleming, G. R. J. Chem. Phys. 2001, 114, 8008.
(122) Ohta, K.; Larsen, D. S.; Yang, M.; Fleming, G. R. J. Chem. Phys. 2001, 114, 8020. (123) Banyai, L.; Koch, S. W. Semiconductor Quantum Dots; World Scientific: Singapore, 1993. (124) Ward, J. F. Rev. Mod. Phys. 1965, 37, 1. (125) Orr, B. J.; Ward, J. F. Mol. Phys. 1971, 20, 513. (126) Bredas, J. L.; Adant, C.; Tackx, P.; Persoons, A.; Pierce, B. M. Chem. Rev. 1994, 94, 243. (127) Zyss, J.; Chemla, D. S. Nonlinear Optical Properties of Organic Molecules and Crystals; Academic Press: Orlando, 1987; Vols. 1 and 2. (128) Rodenberger, D. C.; Heflin, J. R.; Garito, A. F. Nature 1992, 359, 309. (129) Heflin, J. R.; Wong, K. Y.; Zamanikhamiri, O.; Garito, A. F. Phys. Rev. B 1988, 38, 1573.
(130) Bloembergen, N. Nonlinear Optics; Benjamin: New York, 1965. (131) Mukamel, S.; Loring, R. F. J. Opt. Soc. Am. B 1986, 3, 595. (132) Kanis, D. R.; Ratner, M. A.; Marks, T. J. Chem. Rev. 1994, 94, 195. (133) Mukamel, S.; Ciurdariu, C. C.; Khidekel, V. IEEE J. Quantum Electron. 1996, 32, 1278.
(134) Mukamel, S.; Ciurdariu, C. C.; Khidekel, V. Adv. Chem. Phys. 1997, 101, 345. Mukamel, S. J. Chem Phys. 1997, 107, 4165. (135) Schleich, W. P. Quantum Optics in Phase Space; Wiley: New York, 2001. (136) Fermi resonances often occur in coupled vibrations, say between a single quantum of one vibration and a double quantum of a mode with half the frequency. Such effects are neglected in our Hamiltonian. (137) Cherniak, V.; Mukamel, S. J. Chem. Phys. 1996, 105, 4565. (138) Caldeira, A. O.; Leggett, A. J. Physica 1983, 121A, 587.
(139) Mukamel, S.; Piryatinski, A.; Cherniak, V. J. Chem. Phys. 1999, 110, 1711. (140) Kubo, R.; Toda, M.; Hashitsume, N. Statistical Mechanics; Springer-Verlag: Berlin/Heidelberg, 1985. (141) Zhuang, W.; Abramavicius, D.; Mukamel, S. Manuscript in preparation. (142) Torii, H.; Tasumi, M. J. Raman Spectrosc. 1998, 29, 81. (143) Chernyak, V.; Zhang, W. M.; Mukamel, S. J. Chem. Phys. 1998, 109, 9587. (144) Spano, F. C.; Mukamel, S. Phys. Rev. A 1989, 40, 5783. Spano, F. C.; Mukamel, S. Phys. Rev. Lett. 1991, 66, 1197. Spano, F. C.; Mukamel, S. J. Chem. Phys. 1991, 95, 7526. (145) Mukamel, S. In Molecular Nonlinear Optics; Zyss, J., Ed.; Academic Press: New York, 1994. (146) Abrikosov, A. A.; Gorkov, L. P.; Dzyaloshinski, Y. E. Methods of Quantum Field Theory in Statistical Physics; Dover Publications: New York, 1975. Kadanoff, L. P.; Baym, F. Quantum Statistical Mechanics; Benjamin: New York, 1962. Mahan, G. D. Many-Particle Physics; Plenum: New York, 1990. (147) Chernyak, V.; Wang, N.; Mukamel, S. Phys. Rep. 1995, 263, 213. (148) Jenkins, J.; Mukamel, S. J. Chem. Phys. 1993, 98, 7046. Wagersreiter, T.; Mukamel, S. J. Chem. Phys. 1996, 105, 7997. (149) Chernyak V.; Mukamel, S. Phys. Rev. B 1993, 48, 2470. Chernyak V.; Mukamel, S. J. Chem. Phys. 1994, 100, 2953. (150) Leegwater, J. A.; Mukamel, S. Phys. Rev. A 1992, 46, 452. (151) Leegwater, J. A.; Mukamel, S. J. Chem. Phys. 1994, 101, 7388. (152) Ku ̈ hn, O.; Chernyak, V.; Mukamel, S. J. Chem. Phys. 1996, 105, 8586. (153) Chernyak, V.; Mukamel, S. J. Opt. Soc. Am. B 1996, 13, 1302. (154) Victor, K.; Axt, V. M.; Stahl, A. Phys. Rev. B 1995, 51, 14164. Axt, V. M.; Stahl, A. Z. Phys. B 1994, 93, 4195. (155) Redfield, A. G. Adv. Magn. Reson. 1965, 1, 1. (156) Pollard, W. T.; Felts, A. K.; Friesner, R. A. Adv. Chem. Phys. 1996, 93, 77.
(157) Knoester, J.; Mukamel, S. Phys. Rep. 1991, 205, 1. (158) Dubovsky, O.; Mukamel, S. J. Chem. Phys. 1991, 95, 7828. (159) Meier, T.; Chernyak, V.; Mukamel, S. J. Phys. Chem. B 1997, 101, 7332. (160) Chernyak, V.; Mukamel, S. Phys. Rev. Lett. 1995, 74, 4895. (161) Chernyak, V.; Mukamel, S. Phys. Status Solidi 1995, 189, 67. (162) Silbey, R.; Munn, R. W. J. Chem. Phys. 1980, 72, 2763. Munn, R. W.; Silbey, R. J. Chem. Phys. 1985, 83, 1843. Munn, R. W.; Silbey, R. J. Chem. Phys. 1985, 83, 1854. (163) Abramavicius, D.; Mukamel, S. J. Chem. Phys. 2004, 120, in press. (164) Domcke, W.; Stock, G. Adv. Chem. Phys. 1997, 100, 1. (165) Seidner, L.; Stock, G.; Domcke, W. J. Chem. Phys. 1995, 103, 3998. (166) Lindberg, M.; Binder, R.; Koch, S. W. Phys. Rev. A 1992, 45, 1865. (167) Abramavicius, D.; Mukamel, S. J. Phys. Chem. B 2004, 108, in press. (168) Sung, J.; Silbey, R. J. J. Chem. Phys. 2001, 115, 9266. (169) Chernyak, V.; Minami, T.; Mukamel, S. J. Chem. Phys. 2000, 112, 7953. (170) Zwanzig, R. Lect. Theor. Phys. 1961, 3, 106. Zwanzig, R. Physica 1964, 30, 1109. (171) Piryatinski, A.; Chernyak, V.; Mukamel, S. Chem. Phys. 2001, 266, 285. (172) Kuhn, O.; Rupasov, V.; Mukamel, S. J. Chem. Phys. 1996, 104, 5821. (173) Holstein, T.; Primakoff, H. Phys. Rev. 1940, 58, 1098. (174) Dyson, F. J. Phys. Rev. 1956, 102, 1217. (175) Wentzel, G. Phys. Rev. 1957, 108, 1593. Usui, T. Prog. Theor. Phys. 1960, 23, 787.
(176) Agranovich, V. M.; Toshich, B. S. Sov. Phys. JETP 1968, 26, 104. (177) Perakis, I. E. Chem. Phys. 1996, 210, 259. (178) Kner, P.; Bar-Ad, S.; Marquezini, M. V.; Chemla, D. S.; Sch ̈afer, W.; Phys. Rev. Lett. 1997, 78, 1319. Sch  ̈afer, W.; Kim, D. S.; Shah, J.; Damen, T. C.; Cunningham, J. E.; Goossen, K. W.; Pfeiffer, L. N.; Ko ̈hler, K. Phys. Rev. B 1996, 53, 16429. (179)  ̈Ostreich, T.; Sch ̈onhammer, K.; Sham, L. J. Phys. Rev. Lett. 1995, 74, 4698. (180) Bartels, G.; Axt, V. M.; Victor, K.; Stahl, A.; Leisching, P.; K ̈ohler, K. Phys. Rev. B 1995, 51, 11217. Bartels, G.; Cho, G. C.; Dekorsy, T.; Kurz, H.; Stahl, A.; Ko ̈hler, K, Phys. Rev. B 1997, 55, 16404. (181) Schmitt-Rink, S.; Chemla, D. S.; Miller, D. B. Adv. Phys. 1989, 38, 89. Schmitt-Rink, S.; Miller, D. B.; Chemla, D. S. Phys. Rev. B 1987, 35, 8113. (182) Schmitt-Rink, S.; Mukamel, S.; Leo, K.; Shah, J.; Chemla, D. S. Phys. Rev. A 1991, 44, 2124.
(183) Meier, T.; Rossi, F.; Thomas, P.; Koch, S. W. Phys. Rev. Lett. 1995, 75, 2558. Hader, J.; Meier, T.; Koch, S. W.; Rossi, F.; Linder, N. Phys. Rev. B 1997, 55, 13799. (184) Axt, V. M.; Mukamel, S. Rev. Mod. Phys. 1998, 70, 145.
CR020681B
2098 Chemical Reviews, 2004, Vol. 104, No. 4 Mukamel and Abramavicius
