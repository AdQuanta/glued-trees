# Observation of a transition between dynamical phases in a quantum degenerate Fermi gas - Full Text

> Source: https://www.science.org/doi/10.1126/sciadv.aax1568
> Collected: 2026-09-20
> Published: 2019-08-02
> Zotero parent key: MRN2JNMH
> Evidence: Zotero indexed PDF text

P H Y S I C S Copyright © 2019 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original U.S. Government Works. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC).
Observation of a transition between dynamical phases in a quantum degenerate Fermi gas
Scott Smale1*, Peiru He2,3*, Ben A. Olsen1, Kenneth G. Jackson1, Haille Sharum1, Stefan Trotzky1, Jamir Marino2,3, Ana Maria Rey2,3†, Joseph H. Thywissen1†
A proposed paradigm for out-of-equilibrium quantum systems is that an analog of quantum phase transitions exists between parameter regimes of qualitatively distinct time-dependent behavior. Here, we present evidence of such a transition between dynamical phases in a cold-atom quantum simulator of the collective Heisenberg model. Our simulator encodes spin in the hyperfine states of ultracold fermionic potassium. Atoms are pinned in a network of single-particle modes, whose spatial extent emulates the long-range interactions of traditional quantum magnets. We find that below a critical interaction strength, magnetization of an initially polarized fermionic gas decays quickly, while above the transition point, the magnetization becomes long-lived because of an energy gap that protects against dephasing by the inhomogeneous axial field. Our quantum simulation reveals a nonequilibrium transition predicted to exist but not yet directly observed in quenched s-wave superconductors.
INTRODUCTION
The challenge faced in understanding out-of-equilibrium systems is that the powerful formalism of statistical physics, which has allowed a classification of quantum phases of matter based on simple principles such as minimization of free energy, does not apply. A diverse range of nonequilibrium phenomena has been observed, including synchronization (1–5), self-organization (6–9), quantum chaos (10, 11), Loschmidt echo singularities (12), and time crystals (13, 14). A proposed organizing principle is that transitions, reminiscent of those found between thermodynamic ground states, can also be found between dynamical phases (15–19). In general terms, a nonequilibrium phase transition is characterized by the existence of a critical point separating phases with distinct dynamical properties in many-body systems. The analog of thermodynamic order parameters is found in long-time average observables, which have a nonanalytic dependence on system parameters. In driven open systems, energy and particle number are not necessarily conserved, and nonequilibrium transitions are typically signaled by different steady states that occur upon varying system parameters such as pump or loss rates (20–22), independently of initial conditions. In closed systems, dynamics are often initiated by quenching control parameters, with qualitatively distinct behaviors observed below, above, or at a critical point (15–18) that can depend on the initial state of the system. The label “dynamical phase transition” has been applied not only to the boundary between two dynamical phases but also to the nonanalytic behavior in real-time dynamics of the return probability amplitude (12, 23), which does not require an order parameter to be defined (24). The phenomenon under investigation in our work is the former case, which we will refer to as a transition between dynamical phases (TDP) to avoid confusion. The theoretical study of these transitions has encompassed a broad range of platforms including collective
spin models (25–27), nonequilibrium phases of superconductors (28–30), interacting fermions and bosons on the lattice (15–17, 31, 32), and quantum field theories (18, 33); however, experimental investigations have so far been restricted to self-trapping transitions in bosonic systems (34–38) and the transverse-field Ising model realized with trapped-ion chains (19). Here, we report the observation of a transition between two dynamical phases of a quantum degenerate Fermi gas. The sample under investigation consists of neutral potassium atoms (40K) confined in a harmonic optical trap and cooled to nanokelvin temperatures. The controllable interactions of this closed quantum system enable a broad search for nonequilibrium phenomena that arise from the interplay of atomic contact interactions, quantum statistics, and motion. Using collective magnetization as an order parameter, system dynamics are observed directly and compared to theoretical models at various levels of approximation. We understand and analyze our system through a mapping of the single-particle eigenstates of the harmonic trap onto a lattice in mode space, as depicted in Fig. 1. By tuning the interaction strength to suppress collisions that would change the occupancy of the modes, the atoms become pinned on the conceptual lattice, enabling the description of our system with a spin model (39–41); here
H^ =ħ 1⁄4 i∑hi^sZ
i i∑;j Jijs^i ⋅ s^j ð1Þ
where s^i 1⁄4 1=2f^sX
i ; s^iY ; ^siZg are spin-1/2 operators acting on the ith atom and X, Y, and Z denote orientations in Bloch space. This is the collective Heisenberg model, a canonical model for magnetism (42) in which the nonlocal spin-spin couplings Jij compete with an inhomogeneous axial field, hi (39–41). Similar treatments of fermionic systems using a spin model have been used successfully in optical lattice clocks (39, 43–46) in the microkelvin regime. However, in those experiments, undesirable inelastic collisions limited the number, N ≲ 50, and prevented the study of transitions between welldefined dynamical phases. The stability of low-lying hyperfine states and control over interactions in our experiment allow us to explore many-body dynamics in macroscopic ultracold samples of N ≃ 3 × 104 alkali atoms at nanokelvin temperatures and test the spin model in this new regime.
1Department of Physics and Centre for Quantum Information and Quantum Control, University of Toronto, Ontario M5S 1A7, Canada. 2JILA, National Institute of Standards and Technology, and Department of Physics, University of Colorado, Boulder, CO 80309, USA. 3Center for Theory of Quantum Matter, University of Colorado, Boulder, CO 80309, USA. *These authors contributed equally to this work. †Corresponding author. Email: arey@jilau1.colorado.edu (A.M.R.); jht@physics. utoronto.ca (J.H.T.)
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 1 of 8
Downloaded from https://www.science.org on November 07, 2024


 We find that below a critical interaction strength, the magnetization of an initially polarized gas quickly decays, while above this critical point, the magnetization becomes long-lived and is protected by an energy gap against inhomogeneous field-induced dephasing. These observed dynamical phases are a manifestation of an emergent property in a many-body dynamical quantum system. The transition would be absent for small particle number since the emergence of a sufficiently strong gap from weak two-body collisions relies upon a collective nonlinearity. We then implement a many-body echo sequence (4, 47, 48), which is a direct test of reversibility. This allows us to identify the boundaries of the parameter regime in which the complex far-from-equilibrium dynamics of interacting fermions is quantitatively described by the collective Heisenberg model. The successful mapping allows us to implement quantum simulations of the nonequilibrium phases predicted to exist in quenched s-wave superconductors by Richardson-Gaudin models (28–30) but not yet directly observed, given the need for ultrafast probes (49).
RESULTS
The simulation cycle begins with a noninteracting sample fully polarized in the lower spin state ∣↓〉, which ensures that no site in the mode lattice is doubly occupied. Nonequilibrium dynamics are initiated by a fast radio-frequency (rf) pulse that rotates the collective magnetization into the XY plane. The time evolution of transverse magnetization is probed using a Ramsey sequence: Following the initial p/2 pulse, atoms evolve for a variable time t, after which a second p/2 pulse is applied, and the total populations in the ∣↓〉 and ∣↑〉 states are measured with a Stern-Gerlach technique. Shot-to-shot field drifts on the microtesla scale prevent a reproducible accumulated phase in the Ramsey sequence. We estimate the magnitude of the transverse coherence by repeating the sequence at least 10 times and using a maximumlikelihood estimator that assumes a randomized interferometric phase (see Materials and Methods for further details). This procedure mea
sures the total transverse magnetization 2
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ðSXÞ2 þ ðSY Þ2
q
=N, where
SX;Y;Z 1⁄4 〈^SX;Y;Z〉 with S^X;Y;Z 1⁄4 ∑i ^sX;Y;Z
i as collective spin operators.
However, since SZ is a constant of motion in our simulation and set to zero by the first p/2 pulse, we can simply interpret the signal as 2S/N,
with S 1⁄4
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
∑p1⁄4X;Y;Z ðSpÞ2
q
as the total magnetization.
The optical confinement creates a potential that is approximately harmonic, with frequencies w = {wx, wy, wz} = 2p × {395,1140,950} Hz along three spatial directions. Spin-dependent curvature in the confinement potential produces a further shift ±Dw in the oscillator frequency between the ∣↓〉 and ∣↑〉 states. Since the resultant energy shift depends linearly on the index of the single-particle motional ei
genstates, labeled by ni 1⁄4 nix,ny
i,nizg, it constitutes an inhomogeneous
axial field in mode space, hi 1⁄4 2ni  ̇ Dw 1⁄4 2ðnixDwx þ ny
i Dwy þ nizDwzÞ. The strength of the inhomogeneity is tuned in two ways: using the polarization of one of the laser beams forming the optical trap to change Dw (see Materials and Methods) and using temperature to change the average mode index n within the range of 20 to 30. Interactions are proportional to the s-wave scattering length a of the colliding atoms, which are tuned by a magnetic Feshbach resonance near
20 mT (50). We factor Jij as UJ ij, where U 1⁄4 4pa ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mwx wy wz =ħ
p sets an overall scale and J ij is a mode-dependent coupling factor proportional to the density-density overlap of the single-particle eigenmodes of the ith and jth particles (see the Supplementary Materials). Because of the extended nature of the motional wave functions, the J ij are long
ranged and e1=
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
∣np
i np
j∣
q
in each direction p = x, y, z. The TDP is
observed in a weak-scattering regime, where atoms remain frozen in their initial modes and dynamics involve only spin degrees of freedom (3, 4, 51). The precise control of a required an improved determination of the zero-crossing field, Bzc, at which a = 0. As described in Materials and Methods, we find Bzc = 20.907(1) mT.
Dynamical phase diagram
Figure 2 shows an exploration of the nonequilibrium phase diagram using total magnetization at 100 ms, S(t = 100 ms), as the order parameter. Simulations were run with scans of mean interaction strength J = 〈∑i,j Jij/N2〉T (Fig. 2, A to C) or scans of axial field in
homogeneity h~ 1⁄4
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ∑ihi2=N ð∑ihi=NÞ2
q
T
(Fig. 2, E to G), where
the indices i and j run over N populated modes. The thermal average, 〈⋯〉T, is performed by averaging over different realizations of populated modes drawn from a Fermi-Dirac distribution. Several distinct regions appear: a dynamical ferromagnet with high persistent S at large positive or negative NJ and a paramagnetic phase with low S at smaller ∣NJ∣. Measurements are compared to a mean-field treatment of Eq. 1, where the jth atom experiences an effective magnetic field, Bj, which depends only on the local field, hj, and the average magnetization of the other atoms in the ensemble
H^ mf =ħ 1⁄4 j∑
s^j ⋅ Bj ð2Þ
where Bj 1⁄4 hjZ ∑i2Jij〈s^i〉. Here, the indices i and j run over a set of N populated modes drawn from a finite temperature Fermi-Dirac distribution, and Z is a unit vector. The TDP is a consequence of the opening of an interaction energy gap between the fully polarized manifold and the remainder of the Hilbert space, as further discussed below. Numerical solutions of the corresponding 3N nonlinear Bloch
equations show that above some critical interaction strength, Jcðh~Þ,
Dephasing
Exchange
Mode changes
Fig. 1. Simulation of the collective Heisenberg model with a local inhomogeneous axial field using weakly interacting fermions in a mode space lattice. Each site in mode space (left) has an occupancy of 0 or 1 and experiences a local field hi that causes single-spin precession at a rate that depends on the mode (top right). Atoms experience long-range spin-exchange interactions Jij (middle right). Mode-changing collisions would move atoms between sites in mode space (bottom right) but are not included in the spin model.
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 2 of 8
Downloaded from https://www.science.org on November 07, 2024


 the dynamics become gapped and ferromagnetic order (meta)stabilizes,
while below Jcðh~Þ, the gas partially demagnetizes. The numerical calculations take into account finite temperature effects by averaging over solutions generated by different sets of populated modes sampled from a Fermi-Dirac distribution (see the Supplementary Materials). In the ungapped phase, exchange interactions are not strong enough to prevent demagnetization, rendering the system prone to dephasing induced by inhomogeneous hi. In contrast to thermodynamic ferromagnetism, which occurs only for J > 0, the dynamical ferromagnet is a spin-locked state that can be stabilized by either repulsive or attractive exchange interactions. The red lines in Fig. 2 show S(t = 100 ms) calculated by this model using ab initio determination of J, a set of field curvatures that match all observations in this manuscript (see the Supplementary Materials), and
a decay envelope [e−G(a)t] discussed in detail further below. The white solid line in Fig. 2D shows the TDP steady-state (t → ∞ ) phase bound
ary that sets Jcðh~Þ. While we are unable to probe the system at infinite time and thereby reveal the strict steady-state limit, we find, as shown
by the corroboration in Fig. 2, that t = 100 ms ≈ 40 (wx/2p)−1 is sufficiently long to capture the nonequilibrium phase diagram as a function
of J and ~h.
Transition between dynamical phases
To gain understanding of the scaling expected near the TDP, one can use a simplified “all-to-all” model, in which coupling constants are replaced by their mean value, Jij → J. In this limit, Eq. 2 becomes integrable and maps to a Richardson-Gaudin model, a model used to describe fermionic superconductors when the Bardeen Cooper Schrieffer Hamiltonian is expressed in terms of Anderson pseudospins (52). Borrowing the methodology developed for dealing with dynamical phases in superconductors (30, 53, 54), one can obtain the frequency spectrum
ruling the nonequilibrium dynamics from the roots of L2(u), where L(u) is the Lax vector of the auxiliary variable u (see the Supplementary
Materials). The roots can be found using the property that L2(u) is an integral of motion of the dynamics and can be evaluated for convenience at time t = 0. When the roots compress in the neighborhood of the real axis, the long-time limit ofS(t) relaxes to a zero. This corresponds to the normal phase or “phase I” in the language of superconductors (30). On the other hand, the appearance of a pair of complex conjugate roots determines the TDP critical point and the emergence of a phase characterized by a nonzero steady-state order parameter, S(∞) > 0, i.e., “phase II.” While the precise scaling of the order parameter near the TDP can be complex, since it is determined by the spectrum of the hi, we find that above the critical point in our system, it can be approximated by the analytic expression
Sð∞Þ ≈
pffi3ffiffiah~
2Jeff
cot
pffi3ffiffiah~
NJeff
!
ð3Þ
This formula is exact (with a = 1 and Jeff = J) for the case of a onedimensional (1D) system Dwy, z = 0 at zero temperature. To account for noncollective interactions, higher dimensions, and finite temperature, we introduce renormalization parameters a and Jeff = bJ. The critical inter
action strength is Jcðh~Þ 1⁄4 2pffi3ffiffiah~=ðbNpÞ. An alternate order parameter in the nonequilibrium ferromagnetic phase is the gap frequency
W 1⁄4 2∣Jeff ∣Sð∞Þ ≈ pffi3ffiffia h~cot
pffi3ffiffiah~
NJeff
!
ð4Þ
In the ferromagnetic phase,S(t) exhibits transient oscillations at the gap frequency W, which slowly damp as it reaches S(∞). The gap frequency
goes to zero at Jcðh~Þ in a nonanalytic manner. As discussed below, we observe each of these signatures in the quantum simulation. The collective nature of these phenomena is emphasized by an alternative interpretation of the gap. The initial p/2 pulse can be said
0.0 0.2 0.4 0.6 0.8 1.0
Collective interaction strength
Magnetization
−50 −25 0 25 50
5
10
15
20
−9 −6 −3 0 3 6 9
A
B
C EF G
Fig. 3
Scattering length
Inhomogeneity
0.0
0.2
0.4
0.6
0.8
1.0 −15 −10 −5 0 5 10 15
0.0
0.2
0.4
0.6
0.8
1.0
−90 −60 −30 0 30 60 90
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
4 6 8 10 12
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
A
B
C
DE
F
G
Fig. 2. Nonequilibrium phase diagram. (A to C and E to G) Magnetization S at t = 100 ms versus interaction strength J and inhomogeneity ~h. Blue circles are experimental data, and red lines are theory calculations scaled by e−G(a)t at t = 100 ms (see Fig. 4). These are cuts through a nonequilibrium phase diagram (D) calculated using magnetization at t = 100 as the order parameter. The dashed white line shows a cut at the inhomogeneity used in Fig. 3. The solid white lines show the steady-state (t → ∞) phase boundary for a/b = 0.27 determined by the critical point of the magnetization in cuts of constant ~h. Error bars on data points are statistical. Bands in theory correspond to uncertainty in Bzc. All theory calculations except for the solid white line are finite-time thermally averaged numerics, as described in the main text.
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 3 of 8
Downloaded from https://www.science.org on November 07, 2024


 to create a superposition of ∣S = N/2, ms〉 Dicke states, where S and mS
are eigenvalues of the collective operators S^2 1⁄4 ∑p1⁄4X;Y;ZðS^pÞ2 and
^SZ, respectively. All mS states have the same energy in the rotating frame of the rf pulse. A finite energy gap ħW inhibits the production of spin waves (generated by the inhomogeneous hi) and keeps the dynamics within the collective Dicke manifold: Flipping a single spin would reduce S to (N/2 − 1) and change the exchange energy, propor
tional to J^S2, by NJ. Figure 3 (A to E) shows the qualitative change in dynamical be
havior as J crosses Jc for fixed h~. Below the TDP, S(t) decays monotonically in time (Fig. 3A), but above the transition, S(t) oscillates around a nonzero magnetization (Fig. 3, C to E). All observations can be reproduced by the same theoretical model shown in Fig. 2 (red lines) if J ij are scaled by 0.8 from their ab initio values, perhaps because of an increased sampling of trap anharmonicity due to the higher
temperature used in this dataset to increase h~ or because of a renormalization of coupling constants due to resonant mode-changing processes (55). The TDP is seen in three observables (Fig. 3, F to H): first, by a departure from ungapped dynamics; second, by looking for a jump in S at 100 ms; and last, by a finite value of W.
The c2 measure in Fig. 3F compares both data and calculations to SJ=0(t), the calculated time evolution for J = 0. The sharp increase near NJ/2p ≈ 10 Hz in both experiment and theory indicates the qualitative deviation of the dynamics from the paramagnetic phase. The magnetization at t = 100 ms (in Fig. 3G) also shows an increase near NJ/2p ≈ 10 Hz. Numerical solutions of the mean-field dynamics with thermal averaging at finite time (red band) and without thermal averaging in steady state (solid black line) agree well with the experimental data. The simplified all-to-all model (Eq. 3, dotted black line) agrees only qualitatively. The gap frequency W in Fig. 3H is found from
Distance from noninteracting dynamics (a.u.)
FG H
Hold time (ms) Hold time (ms) Hold time (ms) Hold time (ms) Hold time (ms)
0 50 100 150 200 0 50 100
0.0
0.2
0.4
0.6
0.8
1.0
0 50 100 150 200 0 50 100 150 200 0 50 100 150
ABCDE
Absolute value of scattering length
Absolute value of collective interaction strength | |/
Magnetization
at 100 ms
Magnetization
0 3 6 0 5 10 15 20 25 0 5 10 15 20 25
0 10 0 20 40 60 0 20 40 60
Gap frequency
0
10
20
30
40
0.0
0.2
0.4
0.6
0.8
0
50
100
150
0 15 30
0.0
0.2
0.4
0.6
0.8
1.0
0 15 30
0
10
20
30
Jc
Fig. 3. Transition between dynamical phases. (A to E) Time-dependent magnetization S(t) for fixed ~h 1⁄4 2p 18:1ð1Þ Hz. As interaction strength increases, data (blue points, with statistical error bars) and theory (red lines, with error bands due to bias field uncertainty) deviate from noninteracting dynamics (dashed black curve) after some time. (F) Experiment and theory are compared via c2 distance to noninteracting dynamics, both significantly deviating for NJ/2p ≳ 10 Hz or a ≳ 3a0. a.u., arbitrary units. (G) The interpolated magnetization at 100 ms agrees well with numerical solutions of the mean-field dynamics with thermal averaging at finite time (red band) and without thermal averaging in steady state (solid black line) but only qualitatively with the analytic approximation of Eq. 3 (dotted black line). (H) The gap frequency W shows good agreement between data and all three levels of theory. W is fit to the analytic formula of Eq. 4 to find NJc/2p = 7.8(1.1) Hz, indicated by the green band. Insets in (G) and (H) compare the analytic approximation given by Eqs. 3 and 4 (dotted black line), with the exact all-to-all numerical solution using the Lax vector approach (orange line) and with the corresponding mean-field numerical solution assuming all-to-all couplings (green circles). Apart from the insets, theory curves are scaled by e−G(a)t to account for beyond spin model processes (see Fig. 4). Error bars on data points are statistical. The theory uncertainty (red band) is dominated by Bzc, and the width of the green Jc band is ± two standard deviations.
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 4 of 8
Downloaded from https://www.science.org on November 07, 2024


 a fitting function that uses a damped sinusoid for later times and SJ=0 for early times (see the Supplementary Materials). By fitting the gap parameter to the analytic formula in Eq. 4, we extract a nonzero critical interaction strength NJc/2p = 7.8(1.1) Hz. Using the location of the step
in c2 (Fig. 3G), we exclude time sequences with∣a∣< 3a0, where the oscillation frequency diverges. The excellent agreement of all three measures with theory based on Eq. 1 confirms that our quantum simulator probes the TDP in the collective Heisenberg model. The significance of the observation is further clarified in Fig. 3 (G and H) by comparison to various approximation levels. Finite-time effects and thermal averaging play a minor role, validating our interpretation of S at sufficiently large t as the steady-state order parameter. Inhomogeneous coupling (Jij ≠ J) plays a significant role for S but less so for W. Comparisons to the exact Lax vector analysis [insets in Fig. 3 (G and H)] show the close similarity of the observed TDP to the phase I–to–phase II transition in dynamical superconductors (28–30).
Effective time reversal
Figure 4 describes a further set of simulations that probe the limits of validity in which our system is described by a spin-lattice model. Figure 4 (A and B) shows that S(t = 100 ms) decreases at sufficiently large a despite a larger gap. This is accompanied by a breakdown in microscopic reversibility, as seen by comparing to a sequence with a many-body
reversal of the spin model (Fig. 4C), in which H^ Y → H^ Y (4, 47, 48). Signatures of time reversibility within the window ∣a∣≲ 20a0 are seen from the nearly J-independent dynamics of S in both the gapped and ungapped phases. The reversibility of demagnetization in our system in this regime is a significant validation of Eq. 1 since the many-body echo sequence does not reverse all terms (e.g., the spin-independent harmonic oscillator term) in the full Hamiltonian. Two processes prevent full reversibility in our simulation: stray magnetic field gradients and collisional processes. These are quantified
by introducing an empirical dephasing rate G(a) = G0 + (a/a0)2g to the
transverse magnetization such that SX, Y(t) → SX, Y(t)e−G(a)t. Figure 4 (B and C) compares data with calculations using a best-fit G 1
0 1⁄4 0:57 s
without echo and G 1
0 1⁄4 0:25 s with echo and g−1 = 600 s. Here, G0 accounts for the single-particle mode-changing processes generated by magnetic field gradients, which are enhanced by a spin reversal (1, 40). g parametrizes mode-changing collisions that take place at a rate that increases quadratically with a and takes a value anticipated by kinetic theory for our experimental density, temperature, and polarization (see the Supplementary Materials). At larger ∣a∣, coherence is lost and a quantum picture becomes unnecessary, as shown by the success of a semiclassical picture to describe diffusive transverse demagnetization (3, 4, 56–60). Figure 4A shows an extended phase diagram, where it can be seen that trapped fermions simulate the collective Heisenberg model only in a restricted parameter window of many-body quantum coherence.
DISCUSSION
In summary, we demonstrate the existence of a TDP in a neutral Fermi gas in a regime of reversible dynamics near the zero crossing of a Feshbach resonance. We outline a direct connection to nonequilibrium phases in the Richardson-Gaudin models for superconductivity, thereby extending experimental observations of TDP’s beyond prior manifestations in Josephson- and Ising-type systems (19, 34–38). Moreover, the excellent agreement between spin-model calculations and a two-axis exploration of the dynamical phase diagram with >104 spins provide experimental evidence of the scaling behavior and universal character of TDPs. The collective nature of the dynamics observed here could protect many-body states in other systems of interest for applied quantum technologies. For example, gap protection would increase the coherence time in optical lattice clocks operated in the quantum degenerate regime (61). Furthermore, using the effective time-reversal capability
0.0
0.2
0.4
0.6
0.8
1.0
−100 −50 0 50 100
−600 −400 −200 0 200 400 600
0.0
0.2
0.4
0.6
0.8
1.0
Time (ms)
AB
C
D
E
−400 −200 0 200 400
−80 −40 0 40 80
5
10
15
20
0.0 0.2 0.4 0.6 0.8 1.0
B
Fig. 2D
Fig. 3
Magnetization
Scattering length
Inhomogeneity
Collective interaction strength
Bias field
0 50 100
Time (ms)
0 50 100
Bias field
−100 0 100
0.0
1.0−20 0 20
Fig. 4. From reversibility to the breakdown of collective Heisenberg model simulation. (A) Spin-model mean-field dynamical phase diagram across a wider range than Fig. 2D showing significant dephasing. (B and D) Magnetization versus interaction strength, with constant bias field. Here, S decreases for very small or very large interactions. The large ∣NJ∣ behavior is captured by augmenting the spin model dynamics with a phenomenological dephasing term (red curves). (C and E) Magnetization versus interaction strength, with a many-body echo sequence that reverses the sign of H^ Y at t/2. The bias field is held at B1 in the first half of the evolution time, yielding scattering length a1 and collective interaction strength NJ1, while in the second half, B2 is chosen such that a2 = −a1 and NJ2 = −NJ1. The initialization, spin reversal, and readout pulses are performed at Bzc. The magnetization can be recovered for ∣NJ∣/2p ≲ 100 Hz, a region shown in more detail by the inset in (C). A small systematic error DBzc ~ 2 mT leads to a shift Da ~ 0.3a0 in azc, a1, and a2, included in the theory curves.
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 5 of 8
Downloaded from https://www.science.org on November 07, 2024


 demonstrated here, together with technical improvements to magnetic field stability and homogeneity, our system could provide a fruitful platform to measure out-of-time order correlations and scrambling of quantum information (48) or test spectroscopic protocols that use time reversal to relax the detection resolution required for spectroscopy beyond the standard quantum limit (62).
MATERIALS AND METHODS
The neutral atomic sample was prepared using laser cooling, magnetic and optical trapping, and evaporative and sympathetic cooling in an atom-chip apparatus described previously (63, 64). The hyperfine states used to encode spin information are the F = 9/2, mF = −9/2 (for ∣↓〉), and mF = −7/2 (for ∣↑〉) states. At the beginning of a simulation sequence, the fermionic ensemble had a typical temperature of several hundred nanokelvin, with data taken in the range of T ~ 0.3 to
0.5 EF/kB, where EF 1⁄4 ð6NÞ1=3ħw is the Fermi energy and w is the geometric mean trap frequency. There was no optical lattice: Confinement was produced by a crossed-beam 1064-nm optical dipole trap, and the map in Fig. 1 is purely conceptual. The magnetic field and its gradients were controlled using a combination of microfabricated wires on the atom chip ≈200 mm from the atoms and macroscopic coils external to the vacuum system. The field was calibrated through rf spectroscopy of the∣↓〉 to∣↑〉 transition. During a typical experimental run, drifts are ≲1 mT. Taking advantage of the symmetry of the many-body dynamics with a, we determined the magnetic field corresponding to a = 0 by observing the magnetization after t = 100 ms at various magnetic fields and then fitting the resulting profile to find the center. The mean result of 10 such trials taken across 6 months results in Bzc = 20.907(1) mT, which is an improvement in uncertainty by an order of magnitude over previous measurements (see the Supplementary Materials for data and literature comparison). Magnetic field gradients, which lead to periodic oscillation of the spin clouds (see the Supplementary Materials), were measured by displacing the trap center and repeating rf spectroscopy. In the optimal configuration, gradients are {13(1),12(1),2(5)} mT/m. The differential displacements Di resulting from these gradients are small compared
to the harmonic oscillator length ai2 1⁄4 ħ=mwi, as dimensionless dis
placements Di/ai = {2.1,0.4,0.1} × 10−2. In this Di ≪ ai regime, the more general XXZ spin model (41) reduces to the Heisenberg model used here. The effective axial field hi in the Heisenberg Hamiltonian is the potential energy differential between the ∣↓〉 and ∣↑〉 states, as sampled by the occupied motional eigenstates. Since one can always subtract a constant potential term, dynamics depend only on the inhomogeneity in hi,
quantified through its root mean square spread h~ . There are both magnetic and optical contributions to hi. The leading-order magnetic field contribution is curvature in real space. Direct spectroscopic data can bound this to ≲500 mT/m2, which is compatible with the 200 mT/m2 best-fit curvature in the model. The optical contribution
to ~h is tuned using the polarization of the trapping light. For far-detuned light, the differential fractional vector light shift (VLS) experienced by the atoms is approximately PgF(dFS/3d), where P is the polarization of the light, gF is the g-factor of the hyperfine sublevels, d is the frequency detuning, and dFS is the fine-structure splitting of the electronic excited state. For a full range of polarization P ∈ [ −1,1] of the optical dipole trapping beam propagating along the z axis, the resulting VLS should modify the trap frequency along x by roughly ±0.06 Hz or ±0.015%.
This control over h~ allows the vertical exploration in the dynamical phase diagram shown in Fig. 2. The magnetization 2S/N was determined using repeated measurements and a maximum-likelihood estimator, as follows. Each experimental image measures N↑, N↓ at the end of a Ramsey sequence. The
fraction of spin-↑, f = N↑/N, relates to the collective spin as f = 1/2 +
(SY/N)cosq + (SX/N)sinq, where q is the phase lag of the second p/2 pulse. However, the typical evolution times (100 ms) exceed the clock coherence time (1.5 ms) so that the accumulated phase f randomizes
the orientation of the transverse spin, SY = Scosf, SX = Ssinf. This yields f = 1/2 + (S/N) cos (q′), where q′ = q − f is a random phase. To reconstruct the offset O and amplitude A of a Ramsey fringe F = O + Acos (q′) from a set of fractions fi acquired in several experimental runs with the same conditions, we assumed a probability distribution
pð f ; A; OÞ 1⁄4 ∫p
0
ffid2ffiffiqpffiffi′
p sp exp ðAcosq′ þ O f Þ2
2s2
which is a convolution of the noise-free probability distribution and Gaussian noise with width s, calibrated to be s = 0.01. We constructed a log-likelihood function for a set of n fraction measurements, lðA; O; ffigÞ 1⁄4 1
n ∑n
i1⁄41 logðpðfi; A; OÞÞ, from which we numerically computed the maximum-likelihood amplitude A and fringe offset O, as well as confidence intervals. Where O falls outside the range of 0.50 ± 0.05, we discarded the data; otherwise, the peak-to-peak amplitude 2A was taken as the best estimate of 2S/N.
SUPPLEMENTARY MATERIALS
Supplementary material for this article is available at http://advances.sciencemag.org/cgi/ content/full/5/8/eaax1568/DC1 Fig. S1. Order parameters predicted by Lax vector analysis in a 1D system. Fig. S2. Approximate form of the Lax vector in a 3D system. Fig. S3. Effective mean-field potential. Fig. S4. Magnetization dynamics for noninteracting particles. Fig. S5. Determination of the Feshbach zero crossing. Fig. S6. Spin-echo amplitude near the Feshbach zero crossing. Fig. S7. Fits to time series. Fig. S8. Equilibrium scattering rate versus temperature. Fig. S9. Nonequilibrium scattering rate. Table S1. Determination of 40K Feshbach resonance parameters. References (65–75)
REFERENCES AND NOTES
1. C. Deutsch, F. Ramirez-Martinez, C. Lacroûte, F. Reinhard, T. Schneider, J. N. Fuchs, F. Piéchon, F. Laloë, J. Reichel, P. Rosenbusch, Spin self-rephasing and very long coherence times in a trapped atomic ensemble. Phys. Rev. Lett. 105, 020401 (2010). 2. C. Solaro, A. Bonnin, F. Combes, M. Lopez, X. Alauze, J.-N. Fuchs, F. Piéchon, F. P. D. Santos, Competition between spin echo and spin self-rephasing in a trapped atom interferometer. Phys. Rev. Lett. 117, 163003 (2016). 3. F. Piéchon, J. N. Fuchs, F. Laloë, Cumulative identical spin rotation effects in collisionless trapped atomic gases. Phys. Rev. Lett. 102, 215301 (2009). 4. X. Du, Y. Zhang, J. Petricka, J. E. Thomas, Controlling spin current in a trapped fermi gas. Phys. Rev. Lett. 103, 010401 (2009).
5. M. A. Norcia, R. J. Lewis-Swan, J. R. K. Cline, B. Zhu, A. M. Rey, J. K. Thompson, Cavity-mediated collective spin-exchange interactions in a strontium superradiant laser. Science 361, 259–262 (2018). 6. K. Baumann, C. Guerlin, F. Brennecke, T. Esslinger, Dicke quantum phase transition with a superfluid gas in an optical cavity. Nature 464, 1301–1306 (2010). 7. J. Klinder, H. Keßler, M. Wolke, L. Mathey, A. Hemmerich, Dynamical phase transition in the open Dicke model. Proc. Natl. Acad. Sci. U.S.A. 112, 3290–3295 (2015). 8. J. Leonard, A. Morales, P. Zupancic, T. Esslinger, T. Donner, Supersolid formation in a quantum gas breaking a continuous translational symmetry. Nature 543, 87–90 (2017).
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 6 of 8
Downloaded from https://www.science.org on November 07, 2024


 9. J.-R. Li, J. Lee, W. Huang, S. Burchesky, B. Shteynas, F. Ç. Top, A. O. Jamison, W. Ketterle, A stripe phase with supersolid properties in spin–orbit-coupled Bose–Einstein condensates. Nature 543, 91–94 (2017). 10. C. Neill, P. Roushan, M. Fang, Y. Chen, M. Kolodrubetz, Z. Chen, A. Megrant, R. Barends, B. Campbell, B. Chiaro, A. Dunsworth, E. Jeffrey, J. Kelly, J. Mutus, P. J. J. O’Malley, C. Quintana, D. Sank, A. Vainsencher, J. Wenner, T. C. White, A. Polkovnikov, J. M. Martinis, Ergodic dynamics and thermalization in an isolated quantum system. Nat. Phys. 12, 1037–1041 (2016). 11. S. Chaudhury, A. Smith, B. E. Anderson, S. Ghose, P. S. Jessen, Quantum signatures of chaos in a kicked top. Nature 461, 768–771 (2009). 12. P. Jurcevic, H. Shen, P. Hauke, C. Maier, T. Brydges, C. Hempel, B. P. Lanyon, M. Heyl, R. Blatt, C. F. Roos, Direct observation of dynamical quantum phase transitions in an interacting many-body system. Phys. Rev. Lett. 119, 080501 (2017). 13. J. Zhang, P. W. Hess, A. Kyprianidis, P. Becker, A. Lee, J. Smith, G. Pagano, I.-D. Potirniche, A. C. Potter, A. Vishwanath, N. Y. Yao, C. Monroe, Observation of a discrete time crystal. Nature 543, 217–220 (2017). 14. S. Choi, J. Choi, R. Landig, G. Kucsko, H. Zhou, J. Isoya, F. Jelezko, S. Onoda, H. Sumiya, V. Khemani, C. von Keyserlingk, N. Y. Yao, E. Demler, M. D. Lukin, Observation of discrete time-crystalline order in a disordered dipolar many-body system. Nature 543, 221–225 (2017). 15. M. Eckstein, M. Kollar, P. Werner, Thermalization after an interaction quench in the Hubbard model. Phys. Rev. Lett. 103, 056403 (2009). 16. M. Schiró, M. Fabrizio, Time-dependent mean field theory for quench dynamics in correlated electron systems. Phys. Rev. Lett. 105, 076401 (2010). 17. B. Sciolla, G. Biroli, Quantum quenches and off-equilibrium dynamical transition in the infinite-dimensional bose-hubbard model. Phys. Rev. Lett. 105, 220401 (2010). 18. A. Gambassi, P. Calabrese, Quantum quenches as classical critical films. Europhys. Lett. 95, 66007 (2011). 19. J. Zhang, G. Pagano, P. W. Hess, A. Kyprianidis, P. Becker, H. Kaplan, A. V. Gorshkov, Z.-X. Gong, C. Monroe, Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator. Nature 551, 601–604 (2017). 20. S. Diehl, A. Tomadin, A. Micheli, R. Fazio, P. Zoller, Dynamical phase transitions and instabilities in open atomic many-body systems. Phys. Rev. Lett. 105, 015702 (2010). 21. L. M. Sieberer, S. D. Huber, E. Altman, S. Diehl, Dynamical critical phenomena in driven-dissipative systems. Phys. Rev. Lett. 110, 195301 (2013). 22. J. Marino, S. Diehl, Quantum dynamical field theory for nonequilibrium phase transitions in driven open systems. Phys. Rev. B 94, 085150 (2016). 23. N. Fläschner, D. Vogel, M. Tarnowski, B. S. Rem, D.-S. Lühmann, M. Heyl, J. C. Budich, L. Mathey, K. Sengstock, C. Weitenberg, Observation of dynamical vortices after quenches in a system with topology. Nat. Phys. 14, 265–268 (2018). 24. M. Heyl, A. Polkovnikov, S. Kehrein, Dynamical quantum phase transitions in the transverse-field ising model. Phys. Rev. Lett. 110, 135704 (2013). 25. B. Žunkovič, A. Silva, M. Fabrizio, Dynamical phase transitions and Loschmidt echo in the infinite-range XY model. Phil. Trans. R. Soc. A 374, 20150160 (2016). 26. B. Žunkovič, M. Heyl, M. Knap, A. Silva, Dynamical quantum phase transitions in spin chains with long-range interactions: Merging different concepts of nonequilibrium criticality. Phys. Rev. Lett. 120, 130601 (2018). 27. A. Lerose, B. Žunkovič, J. Marino, A. Gambassi, A. Silva, Impact of nonequilibrium fluctuations on prethermal dynamical phase transitions in long-range interacting spin chains. Phys. Rev. B 99, 045128 (2019). 28. J. Dukelsky, S. Pittel, G. Sierra, Colloquium: Exactly solvable Richardson-Gaudin models for many-body quantum systems. Rev. Mod. Phys. 76, 643–662 (2004). 29. R. A. Barankov, L. S. Levitov, B. Z. Spivak, Collective rabi oscillations and solitons in a time-dependent bcs pairing problem. Phys. Rev. Lett. 93, 160401 (2004). 30. E. A. Yuzbashyan, M. Dzero, V. Gurarie, M. S. Foster, Quantum quench phase diagrams of an s-wave BCS-BEC condensate. Phys. Rev. A 91, 033628 (2015). 31. C. Kollath, A. M. Läuchli, E. Altman, Quench dynamics and nonequilibrium phase diagram of the Bose-Hubbard model. Phys. Rev. Lett. 98, 180601 (2007). 32. H. Hennig, T. Neff, R. Fleischmann, Dynamical phase diagram of Gaussian wave packets in optical lattices. Phys. Rev. E 93, 032219 (2016). 33. A. Chiocchetta, A. Gambassi, S. Diehl, J. Marino, Dynamical crossovers in prethermal critical states. Phys. Rev. Lett. 118, 135701 (2017). 34. T. Anker, M. Albiez, R. Gati, S. Hunsmann, B. Eiermann, A. Trombettoni, M. K. Oberthaler, Nonlinear self-trapping of matter waves in periodic potentials. Phys. Rev. Lett. 94, 020403 (2005). 35. M. Albiez, R. Gati, J. Fölling, S. Hunsmann, M. Cristiani, M. K. Oberthaler, Direct observation of tunneling and nonlinear self-trapping in a single bosonic Josephson junction. Phys. Rev. Lett. 95, 010402 (2005).
36. S. Levy, E. Lahoud, I. Shomroni, J. Steinhauer, The a.c. and d.c. Josephson effects in a Bose-Einstein condensate. Nature 449, 579–583 (2007). 37. M. Abbarchi, A. Amo, V. G. Sala, D. D. Solnyshkov, H. Flayac, L. Ferrier, I. Sagnes, E. Galopin, A. Lemaitre, G. Malpuech, J. Bloch, Macroscopic quantum self-trapping and Josephson oscillations of exciton-polaritons. Nat. Phys. 9, 275 (2013).
38. A. Reinhard, J.-F. Riou, L. A. Zundel, D. S. Weiss, S. Li, A. M. Rey, R. Hipolito, Self-trapping in an array of coupled 1D bose gases. Phys. Rev. Lett. 110, 033001 (2013). 39. M. J. Martin et al., A quantum many-body spin system in an optical lattice clock. Science 341, 632–636 (2013). 40. A. P. Koller, J. Mundinger, M. L. Wall, A. M. Rey, Demagnetization dynamics of noninteracting trapped fermions. Phys. Rev. A 92, 033608 (2015). 41. A. P. Koller, M. L. Wall, J. Mundinger, A. M. Rey, Dynamics of interacting fermions in spin-dependent potentials. Phys. Rev. Lett. 117, 195302 (2016).
42. A. Auerbach, Interacting Electrons and Quantum Magnetism (Springer, 1994).
43. X. Zhang, M. Bishof, S. L. Bromley, C. V. Kraus, M. S. Safronova, P. Zoller, A. M. Rey, J. Ye, Spectroscopic observation of SU(N)-symmetric interactions in Sr orbital magnetism. Science 345, 1467–1473 (2014). 44. A. M. Rey, A. M. Rey, A. V. Gorshkov, C. V. Kraus, M. J. Martin, M. Bishof, M. D. Swallows, X. Zhang, C. Benko, J. Ye, N. D. Lemke, A. D. Ludlow, Probing many-body interactions in an optical lattice clock. Ann. Phys. 340, 311–351 (2014). 45. M. D. Swallows, M. Bishof, Y. Lin, S. Blatt, M. J. Martin, A. M. Rey, J. Ye, Suppression of collisional shifts in a strongly interacting lattice clock. Science 331, 1043–1046 (2010). 46. S. L. Bromley, S. Kolkowitz, T. Bothwell, D. Kedar, A. Safavi-Naini, M. L. Wall, C. Salomon, A. M. Rey, J. Ye, Dynamics of interacting fermions under spin–orbit coupling in an optical lattice clock. Nat. Phys. 14, 399–404 (2018). 47. A. Widera, S. Trotzky, P. Cheinet, S. Fölling, F. Gerbier, I. Bloch, V. Gritsev, M. D. Lukin, E. Demler, Quantum spin dynamics of mode-squeezed luttinger liquids in twocomponent atomic gases. Phys. Rev. Lett. 100, 140401 (2008). 48. M. Gärttner, J. G. Bohnet, A. Safavi-Naini, M. L. Wall, J. J. Bollinger, A. M. Rey, Measuring out-of-time-order correlations and multiple quantum spectra in a trapped-ion quantum magnet. Nat. Phys. 13, 781–786 (2017). 49. R. Matsunaga, N. Tsuji, H. Fujita, A. Sugioka, K. Makise, Y. Uzawa, H. Terai, Z. Wang, H. Aoki, R. Shimano, Light-induced collective pseudospin precession resonating with Higgs mode in a superconductor. Science 345, 1145–1149 (2014). 50. C. Chin, R. Grimm, P. Julienne, E. Tiesinga, Feshbach resonances in ultracold gases. Rev. Mod. Phys. 82, 1225–1286 (2010). 51. S. S. Natu, E. J. Mueller, Anomalous spin segregation in a weakly interacting twocomponent Fermi gas. Phys. Rev. A 79, 051601 (2009). 52. P. W. Anderson, Random-phase approximation in the theory of superconductivity. Phys. Rev. 112, 1900–1916 (1958). 53. E. A. Yuzbashyan, M. Dzero, Dynamical vanishing of the order parameter in a fermionic condensate. Phys. Rev. Lett. 96, 230404 (2006). 54. E. A. Yuzbashyan, O. Tsyplyatyev, B. L. Altshuler, Relaxation and persistent oscillations of the order parameter in fermionic condensates. Phys. Rev. Lett. 96, 097005 (2006). 55. A. P. Koller, M. Beverland, A. V. Gorshkov, A. M. Rey, Beyond the spin model approximation for Ramsey spectroscopy. Phys. Rev. Lett. 112, 123001 (2014). 56. C. Lhuillier, F. Laloë, Transport properties in a spin polarized gas, II. J. Phys. 43, 225–241 (1982). 57. B. R. Johnson, J. S. Denker, N. Bigelow, L. P. Lévy, J. H. Freed, D. M. Lee, Observation of nuclear spin waves in spin-polarized atomic hydrogen gas. Phys. Rev. Lett. 53, 302 (1984). 58. W. J. Gully, W. J. Mullin, Observation of spin rotation effects in polarized 3He-4He mixtures. Phys. Rev. Lett. 52, 1810–1813 (1984). 59. J. M. McGuirk, H. J. Lewandowski, D. M. Harber, T. Nikuni, J. E. Williams, E. A. Cornell, Spatial resolution of spin waves in an ultracold gas. Phys. Rev. Lett. 89, 090402 (2002). 60. M. Koschorreck, D. Pertot, E. Vogt, M. Köhl, Universal spin dynamics in two-dimensional Fermi gases. Nat. Phys. 9, 405–409 (2013). 61. S. L. Campbell, R. B. Hutson, G. E. Marti, A. Goban, N. Darkwah Oppong, R. L. McNally, L. Sonderhouse, J. M. Robinson, W. Zhang, B. J. Bloom, J. Ye, A Fermi-degenerate threedimensional optical lattice clock. Science 358, 90–94 (2017). 62. E. Davis, G. Bentsen, M. Schleier-Smith, Approaching the Heisenberg limit without single-particle detection. Phys. Rev. Lett. 116, 053601 (2016). 63. A. B. Bardon, S. Beattie, C. Luciuk, W. Cairncross, D. Fine, N. S. Cheng, G. J. A. Edge, E. Taylor, S. Zhang, S. Trotzky, J. H. Thywissen, Transverse demagnetization dynamics of a unitary Fermi gas. Science 344, 722–724 (2014). 64. S. Trotzky, S. Beattie, C. Luciuk, S. Smale, A. B. Bardon, T. Enss, E. Taylor, S. Zhang, J. H. Thywissen, Observation of the leggett-rice effect in a unitary Fermi gas. Phys. Rev. Lett. 114, 015301 (2015).
65. P. Smacchia, M. Knap, E. Demler, A. Silva, Exploring dynamical phase transitions and prethermalization with quantum noise of excitations. Phys. Rev. B 91, 205136 (2015). 66. S. Falke, H. Knöckel, J. Friebe, M. Riedmann, E. Tiemann, C. Lisdat, Potassium ground-state scattering parameters and Born-Oppenheimer potentials from molecular spectroscopy. Phys. Rev. A 78, 012503 (2008). 67. T. Loftus, C. A. Regal, C. Ticknor, J. L. Bohn, D. S. Jin, Resonant control of elastic collisions in an optically trapped Fermi gas of atoms. Phys. Rev. Lett. 88, 173201 (2002). 68. C. A. Regal, M. Greiner, D. S. Jin, Observation of resonance condensation of fermionic atom pairs. Phys. Rev. Lett. 92, 040403 (2004).
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 7 of 8
Downloaded from https://www.science.org on November 07, 2024


 69. J. P. Gaebler, J. T. Stewart, T. E. Drake, D. S. Jin, A. Perali, P. Pieri, G. C. Strinati, Observation of pseudogap behaviour in a strongly interacting Fermi gas. Nat. Phys. 6, 569–573 (2010). 70. R. Jördens, “Metallic and Mott-insulating phases in fermionic quantum gases,” thesis, ETH Zürich (2010). 71. U. Schneider, L. Hackermüller, J. P. Ronzheimer, S. Will, S. Braun, T. Best, I. Bloch, E. Demler, S. Mandt, D. Rasch, A. Rosch, Fermionic transport and out-of-equilibrium dynamics in a homogeneous Hubbard model with ultracold atoms. Nat. Phys. 8, 213–218 (2012). 72. A. Ludewig, “Feshbach Resonances in 40K,” thesis, University of Amsterdam (2012). 73. C. Shkedrov, Y. Florshaim, G. Ness, A. Gandman, Y. Sagi, High-sensitivity rf spectroscopy of a strongly interacting Fermi gas. Phys. Rev. Lett. 121, 093402 (2018). 74. T. Lepers, D. Davesne, S. Chiacchiera, M. Urban, Numerical solution of the Boltzmann equation for the collective modes of trapped Fermi gases. Phys. Rev. A 82, 023609 (2010). 75. M. E. Gehm, S. L. Hemmer, K. M. O’Hara, J. E. Thomas, Unitarity-limited elastic collision rate in a harmonically trapped Fermi gas. Phys. Rev. A 68, 011603 (2003).
Acknowledgments: We thank A. Koller and C. Luciuk for early work on this project and V. Gurarie, B. Lev, J. Thompson, M. Foster, and D. Stamper-Kurn for discussions. Funding: This work is supported by NSERC; the Air Force Office of Scientific Research grants FA9550-13-10063 and FA9550-18-1-0319 and its Multidisciplinary University Research Initiative grant
(MURI); the Army Research Office grants W911NF-15-1-0603, W911NF-16-1-0576, and W911NF-19-1-0210; the Defense Advanced Research Projects Agency (DARPA); the NSF grant PHY1820885; JILA-NSF grant PFC-173400; and the National Institute of Standards and Technology. Author contributions: The work was conceived by A.M.R., J.H.T., and S.T. Experiments were performed by S.S., B.A.O., H.S., K.G.J., and S.T. Data were analyzed by S.S., P.H., and B.A.O. Theoretical models and simulation were done by P.H., J.M., J.H.T., and A.M.R. All authors contributed to manuscript preparation. Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials.The datasets generated and analyzed during the current study are available from the corresponding authors upon reasonable request.
Submitted 26 February 2019 Accepted 26 June 2019 Published 2 August 2019 10.1126/sciadv.aax1568
Citation: S. Smale, P. He, B. A. Olsen, K. G. Jackson, H. Sharum, S. Trotzky, J. Marino, A. M. Rey, J. H. Thywissen, Observation of a transition between dynamical phases in a quantum degenerate Fermi gas. Sci. Adv. 5, eaax1568 (2019).
SCIENCE ADVANCES | RESEARCH ARTICLE
Smale et al., Sci. Adv. 2019; 5 : eaax1568 2 August 2019 8 of 8
Downloaded from https://www.science.org on November 07, 2024
