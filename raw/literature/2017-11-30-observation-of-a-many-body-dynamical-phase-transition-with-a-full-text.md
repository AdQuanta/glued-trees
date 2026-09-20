# Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator - Full Text

> Source: https://www.nature.com/articles/nature24654
> Collected: 2026-09-20
> Published: 2017-11-30
> Zotero parent key: AGUEW439
> Evidence: Zotero indexed PDF text

30 november 2017 | voL 551 | nATUre | 601
LeTTer doi:10.1038/nature24654
Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator
J. Zhang1, G. Pagano1, P. W. Hess1, A. Kyprianidis1, P. becker1, H. Kaplan1, A. v. Gorshkov1, Z.-X. Gong1† & C. monroe1,2
A quantum simulator is a type of quantum computer that controls the interactions between quantum bits (or qubits) in a way that
can be mapped to certain quantum many-body problems1,2. As it becomes possible to exert more control over larger numbers of qubits, such simulators will be able to tackle a wider range of problems, such as materials design and molecular modelling, with the ultimate limit being a universal quantum computer
that can solve general classes of hard problems3. Here we use a quantum simulator composed of up to 53 qubits to study nonequilibrium dynamics in the transverse-field Ising model with long-range interactions. We observe a dynamical phase transition after a sudden change of the Hamiltonian, in a regime in which
conventional statistical mechanics does not apply4. The qubits are represented by the spins of trapped ions, which can be prepared in various initial pure states. We apply a global long-range Ising interaction with controllable strength and range, and measure each individual qubit with an efficiency of nearly 99 per cent. Such high efficiency means that arbitrary many-body correlations between qubits can be measured in a single shot, enabling the dynamical phase transition to be probed directly and revealing computationally intractable features that rely on the long-range interactions and high connectivity between qubits.
There have been many recent demonstrations of quantum simulators with varying numbers of qubits and degrees of individual qubit
control2. For instance, small numbers of qubits stored in trapped atomic
ions5,6 and superconducting circuits7,8 have been used to simulate various magnetic spin or Hubbard models, with preparation and measurement of individual qubit states. Large numbers of atoms have been used to simulate similar models, but with global control and
measurements9 or with correlations that appear over only a few atom
sites10. Such quantum simulators are excellent platforms for studying
quantum systems out of equilibrium11. However, an outstanding challenge is to increase the number of qubits while maintaining control and measurement of individual qubits, with the goal of performing simulations or implementing algorithms to tackle problems that cannot be solved efficiently using classical means. Atomic systems are excellent candidates for this challenge, because their qubits can be made to be virtually identical, with flexible and reconfigurable control through external optical fields and high initialization and detection efficiency for individual qubits. Recent work with Rydberg
atoms12,13 has demonstrated many-body quantum dynamics with up to 51 atoms coupled through van der Waals interactions. Here we present quantum simulations at a similar scale using the more controllable system of trapped atomic ions, the many-body qubit interactions of which are mediated by their long-range Coulomb-coupled motion. We perform a quantum simulation of a dynamical phase transition (DPT) with up to 53 qubits. The understanding of such nonequilibrium behaviour is of interest in a wide range of subjects, includ
ing social science14, cellular biology15, astrophysics and quantum
condensed matter physics16. Recent theoretical studies of DPTs17–19 involve the transverse-field Ising model—the quintessential model of
quantum phase transitions20. Recent experiments have investigated
DPT with cold neutral atoms21 and up to 10 trapped-ion qubits, with
the transverse field dominating the interactions22. These studies have
considered long-time spin relaxation dynamics17,19 and non-analytic
time evolution of non-local quantities18,19,22. In this experiment, we use a quantum quench—a sudden change in the Hamiltonian of the system—to bring a collection of interacting
trapped-ion qubits out of equilibrium5,6,22,23. The theoretical description of the dynamics is made difficult by the population of exponentially many excited states of the many-body spectrum as the number of qubits is increased, typically accompanied by high entanglement density between the qubits. Given the long-range interactions between the qubits, the growth in entanglement can be much faster than in
locally connected systems12,13,24, limiting efficient numerical simulation
using matrix product states to short-time dynamics25. The nature of the long-range Ising interaction also leads to unique dynamical features (discussed below) and an emergent higher dimensionality of
the system19,26. We experimentally realize a quantum many-body Hamiltonian with
long-range Ising interactions and flexible tuning parameters27, where the strength and the range of the interactions can both be tuned. As outlined in Fig. 1, we initialize the qubits (effective spin-1/2 systems) in a product state, all polarized along the x direction of the Bloch sphere, and then suddenly turn on the Hamiltonian of the transverse-field Ising model (setting the Planck constant h = 1)
∑∑
= σσ + σ
<
H J B (1)
ij
ij ix jx z i
iz
Here σγ
i (γ ∈{ x, y, z}) is the Pauli matrix acting on the ith spin along
the γ direction of the Bloch sphere, Jij is the Ising coupling between spins i and j, and Bz denotes the transverse magnetic field, which acts as the control parameter for crossing dynamical criticality in the DPT. In Fig. 1b we show a simplified Bloch-sphere representation of the DPT. The spins quickly evolve from the longitudinally polarized initial state, and then either precess about a large transverse magnetic field (green curves) or stay pinned near the initial conditions when the transverse field is small (blue curves). To implement the quantum Hamiltonian (see Methods), each
spin in the chain is encoded in the 2S1/2|F = 0, mF = 0〉 ≡ |↓〉z and
|F = 1, mF = 0〉 ≡ |↑〉z hyperfine ‘clock’ states of a 171Yb+ ion and separated by a frequency of ν0 = 12.642821 GHz. We store a chain of up to N = 53 ions in a linear radio-frequency Paul trap (Methods) and initialize the qubits in the product state |↓↓...↓〉x, where |↓〉x ≡ |↓〉z − |↑〉z. Spin–spin interactions are generated by spin-dependent optical dipole forces from an applied laser field, which give rise to tunable long-range
Ising couplings that fall off approximately algebraically as Jij ≈ J0/|i − j|α (refs 27, 28). The power-law exponent α is set to between 0.8 and 1.0 in the experiment, and the maximum interaction strengths are
1Joint Quantum Institute and Joint Center for Quantum Information and Computer Science, University of Maryland Department of Physics and National Institute of Standards and Technology, College Park, Maryland 20742, USA. 2IonQ, Inc., College Park, Maryland 20740, USA. †Present address: Department of Physics, Colorado School of Mines, Golden, Colorado 80401, USA.
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 602 | nATUre | voL 551 | 30 november 2017
r SeeArCHLeTTer
J0 = (0.82, 0.56, 0.38, 0.65) kHz, for 8, 12, 16 and 53 spins, respectively. The transverse field is generated by a controllable Stark shift of the spin qubit splitting from the same laser field (Methods).
Finally, we measure the magnetization of each spin 〈σix〉. We rotate
all of the spins by π/2 about the y axis of the Bloch sphere (exchanging
σix ↔ σiz) and then illuminate the ions with resonant radiation and col
lect the σiz-dependent fluorescence on a camera with site-resolved
imaging28. We estimate a spin detection efficiency of about 99% for each qubit (see Methods), providing access to all possible many-body correlators in a single shot. The simplest observable of quench dynamics, after evolving the system under the transverse-field Ising model for time t, is the average magnetization of the spins along x:
∑
〈σ (t)〉 = N1 〈σ (t)〉
x
i
ix
In Fig. 2 we show the measured average magnetization for N = 16 spins through 2πJ0t = 4.8, for different values of the transverse field. We formulate a renormalized field Bz to account for the divergence of the energy density of the long-range Ising interactions, so that the ratio Bz/J0 is meaningful in the thermodynamic limit (see Methods). This
enables a fair comparison of the DPT for different numbers of spins in the chain. The evolution of the time-dependent magnetization separates into two distinctive regimes: one that breaks the global Z2 symmetry
(σ → − σ
ix,y ix,y ) of the Ising Hamiltonian (Fig. 2a), as was set by the
initial conditions explicitly, and one that restores this symmetry (Fig. 2c), with the intermediate time dynamics oscillating around and relaxing to zero average magnetization. Between these two regimes we observe a relaxation to a non-zero steady value (Fig. 2b). Cumulative time-averages (insets in Fig. 2)
∫
〈σ 〉 t = t 〈σ τ 〉 τ
() 1 ( )d
x
t
x
0
reveal the long-time magnetization plateaus. The DPT is expected to occur between the small- and large-transversefield regimes as the spin alignment changes abruptly from ferromagnetic to paramagnetic in the long-time limit (Fig. 1). This phase transition is well-established for α = 0, as shown in Methods. There is strong
numerical evidence that such a transition will survive20,29 for the small values of α chosen in our experiments, but not for α → ∞, in which case interactions are nearest-neighbour only.
Time
Time
Initialize spins
Quantum quench
Measurement
x magnetization
ab
x
z
Camera
Figure 1 | Illustration of the DPT from a quantum quench. We subject a system of interacting spins to a sudden change in the Hamiltonian and study the resulting quantum dynamics. a, An isolated spin system is prepared in a product state, and then an Ising spin–spin interaction is suddenly turned on, along with a tunable transverse magnetic field (see text for details). At the end of the evolution, we measure the spin magnetizations along the initial spin orientation direction using a camera. Blue spins and shaded arrows indicate the initial spin polarization; red spins and arrow indicate the projective measurement of spin-down in the measurement basis; and spin and lines of other colours indicate
interacting spins in superpositions. b, A Bloch-sphere representation19 of the average spin magnetization. Spins are initially fully polarized along the longitudinal x direction of the Bloch sphere, and then evolve with Ising interactions along x competing with the transverse field along z, resulting in oscillations and relaxations. Blue curves illustrate the quench dynamics with a low transverse field; green curves indicate the dynamics with a large transverse field across criticality. The grey line indicates a level of zero average magnetization along x.
0.0 0.5 1.0 1.5 2.0
–1.0
–0.5
0.0
0.5
1.0
Time (ms)
Average spin magnetization
0.0 0.5 1.0 1.5 2.0
–1.0
–0.5
0.0
0.5
1.0
0.0 0.5 1.0 1.5 2.0 Time (ms)
0.0 0.5 1.0 1.5 2.0
–1.0
–0.5
0.0
0.5
1.0
0.0 0.5 1.0 1.5 2.0 Time (ms)
0.0 0.5 1.0 1.5 2.0
–1.0
–0.5
0.0
0.5
1.0
a bc
Bz /J0 = 0.6
~ Bz /J0 = 0.8
~ Bz /J0 = 1.6
~
Figure 2 | Real-time spin dynamics after a quantum quench of 16 spins in an Ising chain. a, Polarized spins evolve under the long-range Ising Hamiltonian with a small transverse field (B /J = 0.6
z 0 ). The broken symmetry given by the initial polarized state is preserved during the evolution. b, When the transverse field is increased (B /J = 0.8
z 0 ), the dynamics shows a faster initial relaxation, before settling to a non-zero plateau. c, Under larger transverse fields (B /J = 1.6
z 0 ), the Larmor
precession takes over and the spins oscillate and relax to zero average magnetization. The dashed lines are numerical simulations based on exact diagonalization. Insets show cumulative time averages of the spin magnetization, smoothing out temporal fluctuations and showing the plateaus. Each point is the average of 200 experimental repetitions. Error bars are statistical, computed from quantum projection noise and detection infidelities as described in Methods.
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 30 november 2017 | voL 551 | nATUre | 603
LeTTerr SeeArCH
Further signatures of the DPT are observed by measuring the spatially averaged two-spin correlations
C = N ∑ 〈σ σ 〉
1
ij
ix jx
2 2,
From the behaviour of the magnetizations described above, we expect that C2 → 1 for small Bz and C2 → 1/2 for large Bz at long times, because the collective spin precesses around the z axis and C2 oscillates between 1 and 0. In Fig. 3 we show the cumulative time-averaged correlations. Near the critical value of Bz we observe the emergence of a dip in C2, which is a direct signature of the DPT. The sharpening of the dip for larger system sizes is not strong, which might be due to a logarithmic finite-size scaling (see Methods). For a non-integrable system such as the long-range transverse-field Ising model studied here, it might be conjectured that the spins even
tually reach a thermal distribution30. However, we find that this is true only for small Bz (Fig. 3a, b). We note that the thermal values of the correlator C2 do not exhibit a dip or signatures of a phase transition with varying Bz/J0 for the system sizes that we are able to model numerically. Interestingly, thermalization appears to break down in this quenched system, which we suspect is a consequence of the inherent
long-range nature of the Ising interactions31. We further explore many-body dynamical properties of this system by investigating higher-order correlations, which are even harder to cal
culate classically25. Through high-efficiency single-shot state detection of all of the spins, we measure the distribution of domain sizes in the chain directly as a higher-order correlation observable (see Methods). Single-shot images for N = 53 spins are shown in Fig. 4a and are reconstructed from binary thresholding and image convolution of the fluorescence distribution of the ion chain (see Methods). The occurrence of long domains of correlated spins in the state |↑〉x (fluorescing spins) signifies the fully polarized initial state, in which the correlations are largely preserved by the interactions. With an increasing transverse field, the absence of spin ordering is reflected by exponentially small probabilities of observing long strings. We plot the domain length statistics at late times in Fig. 4a (see Methods) for three transverse field strengths, B /J = (0.1, 1.0, 1.6)
z 0 . The dashed lines in Fig. 4a are fits to exponentials on the histogram of domain sizes. The rare occurrence of especially large domains (see, for example, the red boxes in Fig. 4a) demonstrates the existence of many-body high-order
ab
cd
0.0 0.5 1.0 1.5 2.0
0.2
0.4
0.6
0.8
1.0
Correlations
0.2
0.4
0.6
0.8
1.0
Correlations
8 spins 12 spins
16 spins
Transverse field,
0.0 0.5 1.0 1.5 2.0
53 spins
Bz /J0
~ Transverse field, Bz /J0
~
Figure 3 | Two-body correlations. a–d, Long-time-averaged values of the two-body correlations C2 over all pairs of spins as a function of the transverse field Bz/J0 for different numbers of spins in the chain. The final evolution times correspond to 2πJ0t = (10.3, 5.3, 4.8, 6.5) for 8 (a), 12 (b), 16 (c) and 53 (d) spins, respectively. Statistical error bars are ±1s.d. from measurements covering 21 different time steps. Solid lines in a–c are exact numerical solutions to the Schrödinger equation; the shaded regions take into account uncertainties from experimental Stark shift calibration errors. Dashed lines in a and b are calculations using a canonical (thermal) ensemble with an effective temperature corresponding to the initial energy density. For N = 53 spins (d), the correlations are uniformly degraded from residual Stark shifts across the ion chain, so in this case we normalize to the maximum correlation at small field (see Methods). Exact diagonalization for N = 53 spins is not possible, so we instead fit the experimental data to a Lorentzian function with linear background (dashed line).
ab
Transverse field,
0.0 0.5 1.0 1.5 2.0
12
14
16
18
20
Mean largest domain size
Bz /J0
~
0 10 20 30 40 50 Domain sizes
Occurrences
0 20 30 40 50 Domain sizes
0 10 20 30 40 50
100
101
102
104
Domain sizes
103
100
101
102
104
103
100
101
102
104 103 Bz /J0 = 1.6
~
Bz /J0 = 1.0
~
Bz /J0 = 0.1
~
10
Figure 4 | Domain statistics and reconstructed single-shot images of 53 spins. a, Top and bottom, reconstructed images based on binary detection of spin states (see Methods). The top image shows a chain of 53 ions in ‘bright’ (corresponding to |↑〉x) spin states. The other three images show 53 ions in combinations of ‘bright’ and ‘dark’ (corresponding to |↓〉x) spin states. Centre, statistics of the domain size, or of blocks with spins pointing along the same direction, for different values of the transverse field. Histograms are plotted on a logarithmic scale to visualize the rarity of regions with large domains; example large domains for the different transverse fields (coloured coded) are boxed in the top and bottom images.
Dashed lines are fits to exponential functions, which are expected for a thermal state of the spins and could thus characterize defects such as imperfect preparation and measurement of the qubits. Long tails of deviations from the exponential are clearly visible, and vary depending on Bz/J0. b, Mean largest domain size over the repeated single experimental shots. Error bars are the standard deviation of the mean (see Methods). Dashed line represents a piecewise linear fit, from which we extract the transition point (see text). The green, yellow and red data points correspond to the transverse fields shown in the domain statistics data in a.
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 604 | nATUre | voL 551 | 30 november 2017
r SeeArCHLeTTer
correlations, with the order given by the length of the domain. In Fig. 4b we plot the mean largest domain size as a function of the normalized transverse field strength, for late times and repeated experimental shots. The average longest domain size ranges from 12 to 20 and exhibits a sharp transition across the critical point of the DPT. We fit this observable using a piecewise linear function and extract the critical point to be B /J = 0.89(7)
z 0 (see Methods for more details). The DPT studied here, with up to 53 trapped-ion qubits, is to our knowledge the largest quantum simulation ever performed with highefficiency single-shot measurements of individual qubits. This provides access to arbitrary many-body correlators that carry information that is difficult or impossible to model classically. This experimental platform can be extended to tackle provably hard quantum problems
such as Ising sampling32. Given an even higher level of control over the interactions between spins, as already demonstrated for smaller
numbers of trapped-ion qubits33, this same system can be upgraded to a universal quantum computer.
Online Content Methods, along with any additional Extended Data display items and Source Data, are available in the online version of the paper; references unique to these sections appear only in the online paper.
received 3 August; accepted 20 October 2017.
1. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phys. 21, 467–488 (1982). 2. Trabesinger, A. (ed.) Quantum simulation. Nat. Phys. 8, 263–299 (2012).
3. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2011). 4. Hinrichsen, H. Non-equilibrium phase transitions. Physica A 369, 1–28 (2006). 5. Richerme, P. et al. Non-local propagation of correlations in quantum systems with long-range interactions. Nature 511, 198–201 (2014). 6. Jurcevic, P. et al. Quasiparticle engineering and entanglement propagation in a quantum many-body system. Nature 511, 202–205 (2014). 7. Barends, R. et al. Digital quantum simulation of fermionic models with a superconducting circuit. Nat. Commun. 6, 7654 (2015). 8. Kandala, A. et al. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. Nature 549, 242–246 (2017). 9. Gärttner, M. et al. Measuring out-of-time-order correlations and multiple quantum spectra in a trapped-ion quantum magnet. Nat. Phys. 13, 781–786 (2017). 10. Kuhr, S. Quantum-gas microscopes: a new tool for cold-atom quantum simulators. Natl. Sci. Rev. 3, 170–172 (2016). 11. Eisert, J., Friesdorf, M. & Gogolin, C. Quantum many-body systems out of equilibrium. Nat. Phys. 11, 124–130 (2015). 12. Labuhn, H. et al. Tunable two-dimensional arrays of single Rydberg atoms for realizing quantum Ising models. Nature 534, 667–670 (2016). 13. Bernien, H. et al. Probing many-body dynamics on a 51-atom quantum simulator. Nature 551, https://doi.org/10.1038/nature24622 (2017). 14. Reia, S. M. & Fontanari, J. F. Effect of long-range interactions on the phase transition of Axelrod’s model. Phys. Rev. E 94, 052149 (2016). 15. Davies, P. C., Demetrius, L. & Tuszynski, J. A. Cancer as a dynamical phase transition. Theor. Biol. Med. Model. 8, 30 (2011).
16. Zurek, W. H. Cosmological experiments in condensed matter systems. Phys. Rep. 276, 177–221 (1996). 17. Yuzbashyan, E. A., Tsyplyatyev, O. & Altshuler, B. L. Relaxation and persistent oscillations of the order parameter in fermionic condensates. Phys. Rev. Lett. 96, 097005 (2006).
18. Heyl, M., Polkovnikov, A. & Kehrein, S. Dynamical quantum phase transitions in the transverse-field Ising model. Phys. Rev. Lett. 110, 135704 (2013). 19. Zunkovic, B., Heyl, M., Knap, M. & Silva, A. Dynamical quantum phase transitions in spin chains with long-range interactions: merging different concepts of non-equilibrium criticality. Preprint at https://arxiv.org/ abs/1609.08482 (2016). 20. Sachdev, S. Quantum Phase Transitions (Cambridge Univ. Press, 1999). 21. Fläschner, N. et al. Observation of a dynamical topological phase transition. Preprint at https://arxiv.org/abs/1608.05616 (2016). 22. Jurcevic, P. et al. Direct observation of dynamical quantum phase transitions in an interacting many-body system. Phys. Rev. Lett. 119, 080501 (2017). 23. Neyenhuis, B. et al. Observation of prethermalization in long-range interacting spin chains. Sci. Adv. 3, e1700672 (2017). 24. Gong, Z.-X., Foss-Feig, M., Brandão, F. G. S. L. & Gorshkov, A. V. Entanglement area laws for long-range interacting systems. Phys. Rev. Lett. 119, 050501 (2017).
25. Peschel, I., Wang, X. & Kaulke, M. Density-Matrix Renormalization: A New Numerical Method in Physics (Springer, 1999).
26. Maghrebi, M. F., Gong, Z.-X. & Gorshkov, A. V. Continuous symmetry breaking in 1D long-range interacting quantum systems. Phys. Rev. Lett. 119, 023001 (2017). 27. Porras, D. & Cirac, J. I. Effective quantum spin systems with trapped ions. Phys. Rev. Lett. 92, 207901 (2004). 28. Islam, R. et al. Emergence and frustration of magnetism with variable-range interactions in a quantum simulator. Science 340, 583–587 (2013). 29. Halimeh, J. C. et al. Prethermalization and persistent order in the absence of a thermal phase transition. Phys. Rev. B 95, 024302 (2017). 30. Rigol, M. & Srednicki, M. Alternatives to eigenstate thermalization. Phys. Rev. Lett. 108, 110601 (2012). 31. Campa, A., Chavanis, P.-H., Giansanti, A. & Morelli, G. Dynamical phase transitions in long-range Hamiltonian systems and Tsallis distributions with a time-dependent index. Phys. Rev. E 78, 040102 (2008). 32. Barahona, F. On the computational complexity of Ising spin glass models. J. Phys. A 15, 3241–3253 (1982). 33. Debnath, S. et al. Demonstration of a small programmable quantum computer with atomic qubits. Nature 536, 63–66 (2016).
Acknowledgements We acknowledge discussions with M. Cetina, L. Duan, A. Polkovnikov, M. Heyl, M. Maghrebi, P. Titum and J. Iosue. This work is supported by the ARO and AFOSR Atomic and Molecular Physics Programs, the AFOSR MURI on Quantum Measurement and Verification, the IARPA LogiQ programme, the ARO MURI on Modular Quantum Systems, the ARL Center for Distributed Quantum Information, the NSF Quantum Information Science programme, and the NSF Physics Frontier Center at JQI. G.P. is supported by the IC Postdoctoral Research Fellowship Program.
Author Contributions J.Z., G.P., P.W.H., A.K., P.B., H.K. and C.M. all contributed to experimental design, construction, data collection and analysis. Z.-X.G. and A.V.G. contributed to the theory for the experiment. All authors contributed to this manuscript.
Author Information Reprints and permissions information is available at www.nature.com/reprints. The authors declare competing financial interests: details are available in the online version of the paper. Readers are welcome to comment on the online version of the paper. Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. Correspondence and requests for materials should be addressed to J.Z. (jiehang.zhang@gmail.com).
reviewer Information Nature thanks C. Muschik and C. Roos for their contribution to the peer review of this work.
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 letter reSeArCH
MethOds
Confinement of long ion chains. The ion chain is confined in a three-layer linear Paul trap with a transverse centre-of-mass motional frequency34 of νcm = 4.85 MHz. The harmonic axial confinement is kept low enough that the lowest energy conformation of the ions is linear; for 8–16 ions the axial centre-of-mass frequency is about 400 kHz and for 53 ions it is about 200 kHz. The ion spacing is anisotropic across the chain, with typical spacings of 1.5μm at the centre of the chain and 3.5 μm at either end35. The effective lifetime of an ion chain is limited by Langevin collisions with the residual background gas in the ultrahigh-vacuum apparatus36, which in general re-order the crystal but can also melt the crystal and even ultimately eject the ions as a result of radio-frequency heating or other mechanisms. The chain melting can be mitigated by quickly re-cooling the chain, and we expect that occasionally it returns to the crystalized phase without notice. Occasionally, such collisions with
the background gas are inelastic, either populating the 171Yb+ ion in the metastable
F7/2 state or forming a YbH+ molecule. The 355-nm Raman laser quickly returns the ions to their atomic ground-state manifold, with a small probability of creating doubly charged ions. The mean time between Langevin collisions is expected to be of the order of one collision per hour per trapped ion, and we expect that the mean lifetime of a chain of ions might therefore scale inversely with the number of ions. For 53 ions we observe an average lifetime of about 5 min. However, we observe rare events whereby a long ion chain survives for about 30 min. We speculate that either the chain is consistently re-captured instantaneously, or the local pressure in the chamber is anomalously low during these periods. Because we can load an ion chain in less than 1 min, we achieve a reasonable duty cycle of collecting data. To further scale up the system size, a cryogenic ion trap system could be used to efficiently reduce the pressure and the collision energies, which could enable quantum simulations with well over 100 ions. State preparation. Two off-resonant laser beams at 355 nm globally address the ions and drive stimulated Raman transitions between the two hyperfine qubit clock states 2S1/2|F = 0, mF = 0〉 and |F = 1, mF = 0〉. The Raman beatnotes (frequency difference between two beams) are provided by the frequency comb from the mode-locked laser, resulting in coherent qubit rotations37,38. The ion chain is about 100 μm in length, and the beams are focused to a 200-μm full-width at halfmaximum along the ion chain, resulting in a 30%–40% intensity imbalance between the centre and edges of the chain. To prepare each individual ion in the |↓〉x ≡ |↓〉z − |↑〉z state, we first optically pump the ions in the |↓〉z state with an
efficiency of more than 99%37 and then apply a π/2 rotation around the y axis. However, if we use a single pulse for the rotation, then the inhomogeneity of the beam leads to reduced Rabi frequencies near the edge of the chain and hence an imperfect qubit rotation to the desired initial state. To mitigate this effect, we use a composite pulse compensation sequence (BB1 dynamical decoupling39), written for each spin i as
π/ =  σ σ σ σ
− π 
 − π 
− π 
 
− π 

θ θθ
U ( 2) exp i 2 exp( i )exp i 2 exp i 4
i i i iy
13
where, in addition to the π/2 rotation exp(−iπσ /4)
iy , three additional rotations
are applied: a π pulse along an angle θ = cos−1(−1/16) = 93.6°, a 2π pulse along 3θ, and another π pulse along θ, where the axes of these additional rotations are in the x–y plane of the Bloch sphere with the specified angle referenced to the x axis. With this scheme, we estimate a state preparation fidelity of up to 99% per spin for the well-compensated ions at the middle of the chain, and an average fidelity of 93%, limited by the ions at the edges of the chain. Generating the Ising Hamiltonian. We generate spin–spin interactions by applying a spin-dependent optical dipole force that is induced by the global Raman beams, which are aligned with a wavevector difference Δk along a principal axis of transverse motion34. Two beatnotes of the non-copropagating Raman beams are tuned near the transverse upper and lower motional sideband frequencies at ν0 ± μ, in the usual Mølmer–Sørensen configuration40. In the Lamb–Dicke regime,
this gives rise to the Ising-type Hamiltonian34 in equation (1) with Ising coupling between ions i and j,
∑
Ων μ ν
= − ≈ | − |α
J bb J
i j (2)
ij
m
im jm
m
2R 2 2
0
Here Ω is the global (carrier) Rabi frequency, νR = hΔk2/(8π2M) is the recoil frequency, bim is the normal-mode transformation matrix of the ith ion with the mth normal mode (∑ |b | = ∑ |b | = 1
i im m im
2 2 )35, M is the mass of a single ion and νm is the frequency of the mth normal mode. Here, the beatnote frequency detuning μ is assumed to be sufficiently far from all sidebands,|μ − ν | Ωb ν /ν
m im R m,
so that the spins only couple through the motion virtually and phonon production is suppressed.
The approximate power-law exponent in equation (2) can in principle be tuned in the range 0 < α < 3, but in practice we are restricted to 0.5 < α < 1.8 so as to avoid motional decoherence and experimental drifts. We set α to be roughly constant across different system sizes by adjusting the detuning from the nearest (centre-of-mass) sideband to the values μ − νm = (56, 69, 82, 60) kHz for N = (8, 12, 16, 53) ions, with respective nearest-neighbour Ising couplings J0 = (0.82, 0.56, 0.38, 0.65) kHz. For the case of 53 spins, we use a higher Raman laser intensity to produce a relatively high Ising coupling strength, and whereas α ≈ 0.8 for N = (8, 12, 16), α ≈ 1 for N = 53. The ratio of the spontaneous emission rate from the off-resonant Raman beams to the Ising coupling is expected to be less than 0.003 for N = 53 ions. However, as the system is scaled to larger numbers of spins, the intensity must ultimately be reduced to prevent the creation of phonons from the increasing number of nearby sideband transitions. The residual entanglement between phonons and spin would lead to effective spin decoherence. The scaling of these errors with the number of spins depends on the details of the Ising interactions and sideband detuning, but holding these parameters constant while keeping phonon errors low will lead to a ratio of spontaneous emission to Ising coupling that is expected to grow as N . Nevertheless, these fundamental sources of decoherence are not expected to be substantial, even for hundreds of spins. With α < 1, the long-range interaction term in the Hamiltonian in equation (1) is non-extensive for a one-dimensional linear chain. To have a well-defined thermodynamic limit of the Hamiltonian, the couplings are typically rescaled to J = J /N
ij ij using the Kac normalization constant41
∑
N= N
J J
1
ij
ij
,0
Because all of our observables are functions of the ratio of the field to the Ising coupling strength (Bz/J0), we instead equivalently renormalize the magnetic field using B = B /N
z z and retain the original form of the Ising coupling.
Generating the transverse magnetic field. To generate the effective magnetic field, we adjust the two Raman beatnotes asymmetrically to ν0 ± μ + Bz, resulting in a uniform effective transverse magnetic field of Bz in equation (1) (not yet Kacrenormalized as described above). To induce the quantum quench, the sidebands are switched on in about 100 ns using acousto-optic modulators, which control the detuning and amplitude of the Raman beatnotes. These two beatnotes correspond to different beam angles out of the acousto-optic modulator, so we image these beams onto the ion chain to maximize the overlap of all frequency components. We measure a residual effective linear gradient of magnetic field across the chain, resulting from a fourth-order Stark shift gradient42 that arises from the non-perfect overlap of the two beatnotes. This effect is measured to be ΔBz = ±0.65 kHz end-to-end on a 16-ion chain, and was included in the numerics. This gradient is dominated by uniform magnetic fields Bz > 2 kHz, but still plays a part at zero or small magnetic fields, causing an effective depolarization of the initial state |↓↓...↓〉x. Additional spin depolarizations can be caused by Stark-shift fluctuations and calibration errors, or by residual spin–phonon coupling. These effects are responsible for the slight decay that is seen in Fig. 2a and for the zero-field error in Fig. 3c, d.
Single-shot detection and image processing. We detect the ion spin state by globally rotating all of the spins into the measurement basis (composite (BB1) π/2 pulse as describe above, to rotate x basis into z basis), followed by the scattering of resonant laser radiation on the 2S1/2|F = 1〉 − 2P1/2|F = 0〉 cycling transition (wavelength near 369.5 nm and radiative line width γ/2π ≈ 20 MHz). The |↑〉z ‘bright’ state fluoresces strongly whereas the |↓〉z ‘dark’ state fluoresces almost no photons
because the laser is far from resonance37. The fluorescence of the ion chain is imaged onto an electron-multiplying (EM) CCD camera (Model Andor iXon 897) using an imaging objective with a numerical aperture of 0.4 and a magnification of 60. The fluorescence of each ion covers roughly a 5 × 5 array of pixels on the EMCCD. After collecting the fluorescence for an integration time of 300 μs, we collect a mean of about 20 photons per bright ion, distributed in a circular region of interest around the centre of the ion’s position. In every single shot, we use a simple binary threshold to determine the state of each ion (|↓〉z or |↑〉z), providing a binary detection of the quantum state of any ion with nearly 99% accuracy. The residual 1% errors include off-resonant optical pumping of the ion between states during detection, readout noise and background counts, and crosstalk between adjacent ions. The regions of interest of the individual ions on the camera are determined from periodically acquiring diagnostic images, whereby a resonant re-pumper laser is applied, causing each ion to fluoresce strongly regardless of its state. The signal-tobackground-noise ratio in the diagnostic shots is larger than 100, yielding precise knowledge of the centre locations. Ion separations range from 1.5 μm to 3.5 μm depending on the trap settings and the distance from the chain centre, and are
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 reSeArCH letter
always much larger than the resolution limit of the diffraction-limited imaging system ( −
+
500 nm
0100 Airy ring radius projected at the ion position). We use the pre-determined ion centres to process the individual detection shots, and optimize the integration area on the EMCCD camera to collect each ion’s fluorescence while minimizing crosstalk. We estimate crosstalk to be dominated by nearest-neighbour fluorescence, which can bias a dark ion to be erroneously read as bright with less than 1% probability. The larger inhomogeneities of inter-ion spacings near the edge of the chain do not introduce additional infidelities, as long as they are well illuminated by the detection laser beam.
Statistical data analysis of domain size. Here we present a detailed analysis of the domain statistics presented in Fig. 4. The domain size is directly related to ‘formation probabilities’, which have recently attracted theoretical interest43. The raw domain statistics are analysed from the binary tally of bright and dark ions, after sorting them into domains with consecutive spins up (bright) or down (dark). The collection of all 200 experimental repetitions for the last 5 time steps (out of 21 time steps overall) are treated equally, resulting in the distribution shown in Fig. 4a. The particular choice of the last 5 time steps is a compromise between being insensitive to early-time dynamics in the magnetic field and increasing the sample size for reduced statistical errors. To analyse the large domains, or the outliers of the distributions in Fig. 4, we find the largest domain in each single shot and plot the statistical distribution in Extended Data Fig. 1. In the main text, the mean (standard error of the mean) is used to extract the data (error bars) presented in Fig. 4b. This has an underlying assumption that the central limit theorem holds for our largest-domain-size statistics. We analyse the distribution in the observed data and fit the histogram to a two-parameter Gamma distribution, shown as the dashed lines in Extended Data Fig. 1. From the fit parameters we extract the mean, taking the skewness of the distribution into account. This systematically shifts the largest domain size by about 1 for all datasets, and a piecewise fit similar to that described in the main text yields the critical point B /J = 0.92(7)
z 0 from this alternative method of data analysis, in good agreement with that obtained in the main text. As a comparison with theory, in Extended Data Fig. 2 we plot the observed mean domain size for 16 spins next to an exact calculation of the mean domain size under the same conditions. The general trend of the data is qualitatively reproduced by theory, although the extremes are tempered in the data, possibly from imperfections in the preparation or measurement of the spins and inhomogeneous fields. Analytical study of the DPT for α = 0. In this section, we show analytically that in the limit α → 0 (Jij = J0 for i ≠ j) the spatially averaged two-point correlation C2 measured in the experiment undergoes a DPT when Bz/J0 crosses unity, in the
thermodynamic and long-time limit. (The average magnetization 〈σx〉 (ref. 43) undergoes a similar DPT, but the second-order correlator that we study here has the advantage that its infinite-time average can be used as a static order parameter.) The case α ≈ 1 in our experiment cannot be treated analytically or numerically for large system sizes, but appears to have dynamics qualitatively similar to the α = 0 case treated here analytically. We first rewrite the Hamiltonian for α = 0
H =J Σ + Σ
N ( ) B (3)
x zz
00 2
using collective spin operators
∑
Σ =σ
=
xyz
i
N
ix y z
,,
1
,,
Here the Ising interactions are normalized to make H0 extensive (see above), which enables a well-defined thermodynamic limit. According to the Heisenberg equation, we have (setting h = 1)
Σ = Σ =− Σ
t iH B
d
d [, ] 2
x x zy
0
We note that the thermodynamic limit (N → ∞ ) coincides with the semi-classical limit for the Hamiltonian in equation (3). We can thus assign to the values of Σx,y,z classical vectors of length N on a Bloch sphere: (Σx, Σy, Σz) = N(cosθ, sinθsinφ, sinθcosφ). The above equation of motion can then be reduced to
tθ = B φ
d
d 2 sin
z
together with the equation cosφ = (J /B )sinθ
0 z that comes from energy conservation. Given the initial state θ(t=0)=0, the dynamics of the correlationC = cos θ
2 2 can be obtained analytically. In the long-time limit, we find a time-averaged value of
∫
∫
∫
∞≡ 〈 〉
=
ξ θθ
θ ξθ
θ
→∞
/−
/−
C ( ) lim T1 C (t) dt
(4)
T
T
BJ
BJ
2 0
2
0
cos d 2 ( ) sin
0
d
2 ( ) sin
z
z
2
02 2
02 2
whereξ = | / |
sin− [min( B J , 1)]
z
1 0 . We plot C (∞)
2 as a function of Bz/J0 in Extended Data Fig. 3. A sharp dip is observed, confirming the existence of the DPT. To understand how C (∞)
2 at B /J = 1
z 0 scales with N, we note that although there are only N + 1 orthogonal quantum states for the collective spin Σ with length N, the Bloch sphere has a surface area of 4π. Thus, each orthogonal quantum state occupies a small area on the Bloch sphere with a radius that scales as1/ N , owing to the usual uncertainty relation between the different projections of spin. As a result, the upper limit of the integral over θ in equation (4) can reach only π/2 − ε, with ε ∼ 1/ N as N → ∞. It can therefore be shown that for large N
∞∼
/ →C N
lim ( ) 1
log( )
BJ 12
z0
We conclude that the size of the dip in the DPT decreases logarithmically with N, which may qualitatively explain why only a weak sharpening of the DPT is observed in the experiment as the spin chain grows in size. Data availability. The data presented in the figures and that support the other findings of this study are available from the corresponding author on reasonable request.
34. Kim, K. et al. Entanglement and tunable spin–spin couplings between trapped ions using multiple transverse modes. Phys. Rev. Lett. 103, 120502 (2009). 35. James, D. F. Quantum dynamics of cold trapped ions with application to quantum computation. Appl. Phys. B 66, 181–190 (1998). 36. Wineland, D. J. et al. Experimental issues in coherent quantum-state manipulation of trapped atomic ions. J. Res. Natl. Inst. Stand. Technol. 103, 259–328 (1998). 37. Olmschenk, S. et al. Manipulation and detection of a trapped Yb+ hyperfine qubit. Phys. Rev. A 76, 052314 (2007). 38. Hayes, D. et al. Entanglement of atomic qubits using an optical frequency comb. Phys. Rev. Lett. 104, 140501 (2010). 39. Brown, K. R., Harrow, A. W. & Chuang, I. L. Arbitrarily accurate composite pulse sequences. Phys. Rev. A 70, 052318 (2004). 40. Sørensen, A. & Mølmer, K. Quantum computation with ions in thermal motion. Phys. Rev. Lett. 82, 1971–1974 (1999). 41. Kac, M. & Thompson, C. J. Critical behavior of several lattice models with long-range interaction. J. Math. Phys. 10, 1373–1386 (1969). 42. Lee, A. C. et al. Engineering large Stark shifts for control of individual clock state qubits. Phys. Rev. A 94, 042308 (2016). 43. Najafi, K. & Rajabpour, M. Formation probabilities and Shannon information and their time evolution after quantum quench in the transverse-field XY chain. Phys. Rev. B 93, 125139 (2016).
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 letter reSeArCH
Extended Data Figure 1 | Distributions of the largest domain size. Statistics of the largest domain size in each experimental shot (200 experiments for each of the last 5 time steps). Considering only the largest domains of each shot eliminates the undesirable biasing towards small domain sizes that is present in Fig. 4a. Domain sizes are related
to many-body correlators, with a domain size of N corresponding to an N-body correlator. Dashed lines are fits to a two-parameter Gamma
distribution proportional to e−x/βxα−1, with shape parameter α and scale parameter β.
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 reSeArCH letter
Extended Data Figure 2 | Domain size observable for 16 spins. Mean
maximum domain size as a function of the (Kac-normalized41) transverse field for 16 spins. Experimental data are analysed as for Fig. 4b. The dashed line is a numerical simulation of the Hamiltonian determined from the experimental parameters. Error bars, 1 s.d.
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.


 letter reSeArCH
Extended Data Figure 3 | Theoretical calculations of the correlations. The spatially and long-time averaged correlation C (∞)
2 (defined in equation (4)), calculated as a function of Bz/J0 for α = 0. The finite-N curves are calculated using exact diagonalization; the N = ∞ curve is calculated analytically from equation (4).
© 2017 Macmillan Publishers Limited, part of Springer Nature. All rights reserved.
