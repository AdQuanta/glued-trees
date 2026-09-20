# Probing many-body dynamics in a two-dimensional dipolar spin ensemble - Full Text

> Source: https://www.nature.com/articles/s41567-023-01944-5
> Collected: 2026-09-20
> Published: Unknown
> Zotero parent key: JM85XB6G
> Evidence: Local Zotero PDF

nature physics

Article                                                                                               https://doi.org/10.1038/s41567-023-01944-5


Probing many-body dynamics in a
two-dimensional dipolar spin ensemble

Received: 20 March 2021                            E. J. Davis1,6, B. Ye 1,6, F. Machado 1,2,6, S. A. Meynell3, W. Wu 1,2, T. Mittiga1,2,
                                                   W. Schenken3, M. Joos3, B. Kobrin1,2, Y. Lyu 1, Z. Wang1,2, D. Bluvstein4, S. Choi1,
Accepted: 5 January 2023
                                                   C. Zu1,2,5, A. C. Bleszynski Jayich 3 & N. Y. Yao 1,2,4
Published online: 16 March 2023

   Check for updates                               The most direct approach for characterizing the quantum dynamics of
                                                   a strongly interacting system is to measure the time evolution of its full
                                                   many-body state. Despite the conceptual simplicity of this approach, it
                                                   quickly becomes intractable as the system size grows. An alternate approach
                                                   is to think of the many-body dynamics as generating noise, which can be
                                                   measured by the decoherence of a probe qubit. Here we investigate what the
                                                   decoherence dynamics of such a probe tells us about the many-body system.
                                                   In particular, we utilize optically addressable probe spins to experimentally
                                                   characterize both static and dynamical properties of strongly interacting
                                                   magnetic dipoles. Our experimental platform consists of two types of spin
                                                   defects in nitrogen delta-doped diamond: nitrogen-vacancy colour centres,
                                                   which we use as probe spins, and a many-body ensemble of substitutional
                                                   nitrogen impurities. We demonstrate that the many-body system’s
                                                   dimensionality, dynamics and disorder are naturally encoded in the probe
                                                   spins’ decoherence profile. Furthermore, we obtain direct control over the
                                                   spectral properties of the many-body system, with potential applications in
                                                   quantum sensing and simulation.


Understanding and controlling the interactions between a single quan-        for decades, including seminal work exploring the decoherence of
tum degree of freedom and its environment represents a fundamen-             paramagnetic defects in solids6,7,13–16,19. More recently, many of the
tal challenge within the quantum sciences1–9. Typically, one views this      developed techniques have re-emerged in the study of solid-state spin
challenge through the lens of mitigating decoherence—enabling one            ensembles containing optically polarizable colour centres. The ability
to engineer a highly coherent qubit by decoupling it from the environ-       to prepare spin-polarized pure states enables fundamentally new
ment2–5,10–12. However, the environment itself may consist of a strongly     prospects in quantum science, from the exploration of novel phases
interacting many-body system, which naturally leads to an alternate          of matter20 to the development of new sensing protocols21.
perspective, namely using the decoherence dynamics of the qubit to                 Prospects for optically polarizable spin ensembles in quantum
probe the fundamental properties of the many-body system6,7,13–18. Dis-      sensing and simulation could be further enhanced by moving to
cerning the extent to which such ‘many-body noise’ can provide insight       two-dimensional systems, which represents a long-standing engi-
into transport dynamics, low-temperature order and generic correlation       neering challenge for the colour centre community22–24. Despite
functions of an interacting system remains an essential open question.       continued advances in fabrication, the stochastic nature of defect
     The complementary goals of probing and eliminating many-body            generation strongly constrains the systems one can create. The poten-
noise have motivated progress in magnetic resonance spectroscopy             tial rewards are substantial enough to merit repeated engineering


1
 Department of Physics, University of California, Berkeley, CA, USA. 2Materials Science Division, Lawrence Berkeley National Laboratory, Berkeley,
CA, USA. 3Department of Physics, University of California, Santa Barbara, CA, USA. 4Department of Physics, Harvard University, Cambridge, MA, USA.
5
  Department of Physics, Washington University, St. Louis, MO, USA. 6These authors contributed equally: E.J. Davis, B. Ye and F. Machado.
    e-mail: ania@physics.ucsb.edu; norman.yao@berkeley.edu


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                     836
Article                                                                                                              https://doi.org/10.1038/s41567-023-01944-5


                                                                                                           Z
              a                                         b                                                                e
                        e—                                                                                                                            π        t          π
                                                                                                                                                      2                   2
                                                                                                                     φ
                                                                                                                                                      π                   π
                                                                                                                                                      2       π           2

                                                                                                                          S(ω)




                                                                                                                                    1/τc                  ω
                                                                                                                         f           Ballistic            Random walk
                                                            d
                                                                                                                                                                   D/2α
             c
                                                                                                                         log φ2
                                                                           5


                                                            ρ 14N (a.u.)
                         |1
                                                                                     8 nm
                                                                                                                                    D/α
                                     |–1                                  3
                   ∆0          ωNV                |↑                                                                                                         DEER/Ramsey
                                            ωP1                                                                                            3D/2α
                                                                           1                                                                                  Spin echo
                                                                                                                                               τc
                               |0                |↓
                                                                               0                               500                                    log t
                                                                                   Depth (nm)
                                                                                                                                                 14
Fig. 1 | Experimental platform and theoretical framework. a, A delta-doped              spectrometry measurement of the density of N as a function of depth for
layer of 14N (green) is grown on a diamond substrate. NV centres are created via        sample S1. The presence of a thin layer is indicated by a sharp nitrogen peak
local electron irradiation (orange beam) and subsequent high-temperature                with a 8-nm width, limited by the secondary ion mass spectrometry resolution.
annealing. b, Schematic depiction of a two-dimensional layer of NV (red) and P1         e, The overlap between the many-body spectral function (blue) and the power
(blue) centres. Dilute NV centres function as probe spins of the dense, disordered      spectrum of the filter function ∣f(ω; t)∣2 determines the variance of the
P1 system. The P1 centres exhibit spin-flip dynamics driven by magnetic                 phase ∼ χ(t) (equation (2)). ∣f(ω; t)∣2 for both a Ramsey/DEER pulse sequence
dipole–dipole interactions (zoom). Ising interactions with the P1 system cause          (purple) and a spin echo pulse sequence (orange) are shown. f, Schematic
the NV to accumulate a phase, ϕ, during noise spectroscopy (Bloch sphere).              depiction of the variance of the phase, ⟨ϕ2 ⟩ = −2 log C(t), as a function of the
c, NV and P1 level structure in the presence of a magnetic field, B, applied along      measurement duration t, for both Ramsey/DEER (purple) and spin echo (orange).
the NV axis. We work within an effective spin 1/2 subspace of the NV centre,            The labelled slopes indicate the predicted stretch powers in both the early-time
{|0⟩ , |−1⟩}, with level splitting, ωNV. The corresponding P1 splitting, ωP1, is        ballistic regime and the late-time random-walk regime (Table 1). The cross-over
strongly off-resonant from the NV transition. d, Secondary ion mass                     occurs at the correlation time, τc.




efforts: Two-dimensional, long-range interacting spin systems are                      many-body system. Unlike previous work on lower-dimensional
known to host interesting ground-state phases such as spin liquids25–27.               ordered systems in magnetic resonance spectroscopy30–32, we cannot
Moreover, two-dimensional spin ensembles enable improved sensing                       leverage conventional methods such as X-ray diffraction to charac-
capabilities owing to increased coherence times and uniform distance                   terize our disordered spin ensemble. To the best of our knowledge,
from the target (Supplementary Information).                                           studying the decoherence dynamics provides the only robust method
     In this article, we investigate many-body noise generated by a thin               to determine the effective dimensionality seen by the spins.
layer of paramagnetic defects in diamond. Specifically, we combine                          The stretch power of the NV centres’ decoherence can also dis-
nitrogen delta doping during growth with local electron irradiation                    tinguish between different forms of spectral diffusion, shedding light
to fabricate a diamond sample (S1) where paramagnetic defects are                      on the nature of local spin fluctuations. In particular, we demonstrate
confined to a layer whose width is, in principle, smaller than the aver-               that the P1 spin-flip dynamics are inconsistent with the conventional
age spin defect spacing (Fig. 1a,b)22–24. This layer contains a hybrid spin            expectation of telegraph noise but rather follow that of a Gauss–
system consisting of two types of defects: spin 1 nitrogen vacancy (NV)                Markov process (Table 1). Understanding the statistical properties
centres and spin 1/2 substitutional nitrogen (P1) centres. The dilute NV               of the many-body noise and the precise physical settings where such
centres can be optically initialized and read out, making them a natural               noise emerges remains the subject of active debate4,6,16,33–39. Finally,
probe of the many-body noise generated by the strongly interacting                     the cross-over in time between different stretch powers allows one
P1 centres. In addition, we demonstrate a complementary role for                       to extract the many-body system’s correlation time. We demonstrate
the NV centres, as a source of spin polarization for the optically dark                this behaviour by actively controlling the correlation time of the P1
P1 centres. In particular, by using a Hartmann–Hahn protocol, we                       system via polychromatic driving, building upon techniques previously
directly transfer polarization between the two spin ensembles.                         utilized in broadband decoupling schemes40.
     We experimentally characterize the P1 system’s many-body
noise via the decoherence dynamics of NV probe spins. To elucidate                     Theoretical framework for decoherence
our results, we first present a theoretical framework that unifies and                 dynamics induced by many-body noise
generalizes existing work, predicting a non-trivial temporal profile                   We first outline a framework, building upon classic results in NMR
that exhibits a cross-over between two distinct stretched exponential                  spectroscopy, for understanding the decoherence dynamics of probe
decays (for the average coherence of the probe spins) (Fig. 1)6,13–16,19,28.           spins coupled to an interacting many-body system. This will enable us to
Beyond solid-state spin systems, the framework naturally extends to                    present a unified theoretical background for understanding the experi-
a broader class of quantum simulation platforms, including trapped                     mental results in subsequent sections6,14,15,19,28,41–43. The dynamics of a
ions, Rydberg atoms and ultracold polar molecules29. Crucially, we                     single probe spin generically depend on three properties: (1) the nature
demonstrate that the associated stretch powers contain a wealth of                     of the system–probe coupling, (2) the system’s many-body Hamiltonian
information about both the static and dynamical properties of the                      Hint and (3) the measurement sequence itself. Crucially, by averaging
many-body spin system.                                                                 across the dynamics of many such probe spins, one can extract global
     We focus on three such properties. First, the stretch power con-                  features of the many-body system (Fig. 1b). We distinguish between two
tains a direct signature revealing the dimensionality of the disordered                types of ensemble averaging that give rise to distinct signatures in the


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                                              837
Article                                                                                                             https://doi.org/10.1038/s41567-023-01944-5

                                                                                                                     2
Table 1 | Predicted early- and late-time stretch powers of                             C(t) = ⟨Re[e−iϕ(t) ]⟩ ≈ e−⟨ϕ ⟩/2 , where ⟨ϕ2 ⟩ = ∑i J2z χ(t)/r2α
                                                                                                                                                     i
                                                                                                                                                        (refs. 4,13,39,44;
the probe spin decoherence profile when coupled to a                                   see the Supplementary Information for supporting derivations).
D-dimensional system via power-law Ising interactions                                  Here, χ(t) encodes the response of the probe spins to the noise
∼1/rα. We distinguish between Gaussian and telegraph                                   spectral density, S(ω), of the many-body system:
spin-flip noise in the many-body system, which gives rise
to different predictions for the early-time spin echo stretch
                                                                                                                 χ(t) ≡ ∫ dω |f(ω; t)|2 S(ω),                         (2)
power

Many-body noise properties       Measurement               Early-time   Late-time
                                 sequence                  (ballistic   (random        where f(ω; t) is the filter function associated with a particular pulse
                                                           regime)      walk regime)   sequence (for example, Ramsey spectroscopy or spin echo) of total
                                                           stretch      stretch        duration t (Fig. 1e).
                                                           power        power
                                                                                            Intuitively, S(ω) quantifies the noise power density of spin flips in
                                  DEER/Ramsey              D/α          D/2α           the many-body system. It is the Fourier transform of the autocorrela-
                                  Spin echo                3D/2α        D/2α           tion function, ξ(t) ≡ 4 ⟨szi (t)szi (0)⟩, and captures the spin dynamics at
                                                                                       the level of two-point correlations45. For Markovian dynamics,
                                                                                       ξ(t) = e−|t|/τc, where τc defines the correlation time after which a spin,
                                  DEER/Ramsey              D/α          D/2α           on average, retains no memory of its initial orientation. In this case,
                                  Spin echo                1 + D/α      D/2α           S(ω) is Lorentzian and one can derive an analytic expression for χ
                                                                                       (refs. 15,19,37,41; see the Supplementary Information for supporting
                                                                                       derivations).
                                                                                            A few remarks are in order. First, the premise that many-body
                                                                                       Hamiltonian dynamics produce Gaussian-distributed phases ϕ(t)—
decoherence: (1) an average over many-body trajectories (that is, both                 while often assumed—is challenging to analytically justify6,15,16,33,46.
spin configurations and dynamics) that yields information about the                    Indeed, a well-known counterexample of non-Gaussian spectral diffu-
microscopic spin fluctuations (for simplicity, we focus our discussion                 sion occurs when the spin dynamics can be modelled as telegraph noise,
on the infinite-temperature limit, but the analysis can be extended to                 that is, stochastic jumps between discrete values szi = ±si (refs. 16,34).
finite temperature) and (2) an average over positional randomness                      The precise physical settings where such noise emerges remain the
(that is, random locations of the system spins) that yields information                subject of active debate4,6,16,33–39. Second, we note that our Markovian
about both dimensionality and disorder.                                                assumption is not necessarily valid for a many-body system at early
     To be specific, let us consider a single spin 1/2 probe coupled to                times or for certain forms of interactions, which can also affect the
a many-body ensemble via long-range, 1/rα Ising interactions:                          decoherence dynamics.

                                          Jz z z                                       Average over positional randomness
                              Hz = ∑          s ̂p sî ,                         (1)
                                      i   rαi                                          The probe’s decoherence depends crucially on the spatial distribution
                                                                                       of the spins in the many-body system. For disordered spin ensembles,
where ri is the distance between the probe spin sp̂ and the ith system                 explicitly averaging over their random positions yields a decoherence
spin sî , and the Ising coupling strength Jz implicitly includes any                  profile:
angular dependence. Such power-law interactions are ubiquitous
                                                                                                                N
in solid-state, atomic and molecular quantum platforms (for example,                                                dD ri       −J2z χ(t)           2
                                                                                                                                                           D/2α
                                                                                                    C(t) = ∫ ∏            exp [           ] = e−an[Jz χ(t)] ,         (3)
Ruderman–Kittel–Kasuya–Yosida interactions, electric/magnetic                                                   i=1
                                                                                                                     V           2r  2α
                                                                                                                                     i
dipolar interactions, van der Waals interactions, etc.).
     Physically, the system spins generate an effective magnetic                       where a is a dimensionless constant and N is the number of
field at the location of the probe (via Ising interactions), which can be              system spins in a D-dimensional volume V at a density n ≡ N/V
measured with Ramsey spectroscopy (Fig. 1e, inset)7. In particular, we                 (see the Supplementary Information for supporting derivations)19.
                                                               z
envision initially preparing the probe in an eigenstate of sp̂ and subse-              By contrast, for spins on a lattice or for a single probe spin, the
quently rotating it with a π/2 pulse such that the initial normalized                  exponent of the coherence scales as ∼ J2z χ(t) (Supplementary
                             x
coherence is unity, C ≡ 2 ⟨s ̂p ⟩ = 1. The magnetic field, which fluctuates            Information).
due to many-body interactions, causes the probe to Larmor precess                           A resonance counting argument underlies the appearance of both
(Fig. 1b, inset and Supplementary Information). The phase associated                   the dimensionality and the interaction power law in equation (3).
with this Larmor precession can be read out via a population imbalance,                Roughly, a probe spin is only coupled to system spins that induce a
after a second π/2 pulse.                                                              phase variance larger than some cutoff ϵ. This constraint on the mini-
                                                                                                                                                             1/2α
                                                                                       mum variance defines a volume of radius rmax ≈ [ J2z χ(t)/ϵ]  contain­
Average over many-body trajectories                                                    ing Ns ≈ nrDmax spins, implying that the total variance accrued at any
                                                                                 x
For a many-body system at infinite temperature, C(t) = 2Tr[ρ(t)s ̂p ] ,                                                  D/2α
                                                                                       given time is ϵNs ≈ [ J2z χ(t)] . Thus, the positional average simply
where ρ(t) is the full density matrix that includes both the system and
                                                                                       serves to count the number of spins to which the probe is coupled.
the probe. The spin fluctuations are determined by the microscopic
details of the many-body dynamics whose full analysis is intractable.
To make progress, we approximate each spin as a stochastic classical                   Decoherence profile
           z
variable sî (t) → szi (t). The statistical properties of such variables and           The functional form of the probe’s decoherence, C(t), encodes a
their resulting ability to capture the experimental observations provide               number of features of the many-body system. We begin by elucidating
important insights into the nature of fluctuations in strongly interact-               them in the context of Ramsey spectroscopy. First, one expects a some-
ing spin systems.                                                                      what sharp cross-over in the behaviour of C(t) at the correlation
     The phase of the Larmor precession is given by                                    time τc. For early times, t ≪ τc, the phase variance accumulates as in a
         t
ϕ(t) = ∫0 dt′ Jz ∑i szi (t′ )/rαi. Assuming that ϕ(t) is Gaussian distributed,         ballistic trajectory with χ ∼ t2, while for late times, t ≫ τc, the variance
one finds that the average probe coherence decays exponentially as                     accumulates as in a random walk with χ ∼ t (refs. 15,28,41). This leads to a


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                                     838
Article                                                                                                                                                       https://doi.org/10.1038/s41567-023-01944-5

             a                                        t
                                                                                                                                     in the case of spin echo, the decoupling π pulse (Fig. 1e, inset) is
                                  Laser
                                   NV
                                             π
                                             2     π
                                                            π
                                                            2
                                                                                                                                     ineffective on timescales larger than the correlation time, since the
                                   P1              π                                                                                 spin configurations during the two halves of the free evolution are
                                                                                                                                     completely uncorrelated. Moreover, this same loss of correlation
                                                                                                                                     implies that the phase accumulation is characterized by incoherent
                                                                                                     1/3
                                                                                                                                     Gaussian diffusion, regardless of the specific nature of the spin

            –log C(t)
                        10
                             0

                                        1
                                                                                                                                     dynamics (for example, Markovian versus non-Markovian or
                                                                           1                                                         continuous versus telegraph).

                                                                    C(t)
                                                                                                                                     Experimentally probing many-body noise in
                                                                           0                                                         strongly interacting spin ensembles
                                             2/3                            0                   15    0                 5
                                                                                   t (µs)                    t (µs)                  Our experimental samples contain a high density of spin 1/2 P1 centres
                                                                                                                                     (Fig. 1b, blue spins) which form a strongly interacting many-body
                                                      0                                 1                           2
                                                 10                                10                          10
                                                                                                                                     system coupled via magnetic dipole–dipole interactions:
                                                                           Time, t (µs)
             b                                                                                                                                                   J0         + −       − +              z z
                                                                                                                                                                     [cij (sî sĵ + sî sĵ ) + cij̃ sî sĵ ] ,
                              1
                        10                                                                                                                            Hint = ∑    3
                                                                                                                                                                                                                    (4)
                                                                                                                                                             i<j rij
                                                                t
                                     Laser
                                                      π                        π
                                            NV        2         π              2                                                     where J0 = 2π × 52 MHz nm3, rij is the distance between P1 spins
                                            P1
                                                                                                                                     i and j and c, c ̃capture the angular dependence of the dipolar inter­action
                                                                                                                                     (Supplementary Information). We note that H int contains

            –log C(t)
                             0
                        10
                                                                                                                                     only the energy-conserving terms of the dipolar interaction.
                                                          3/2                               1
                                                                                                                                          The probes in our system are spin 1 NV centres, which can be
                                                                                                                                     optically initialized to |ms = 0⟩ using 532 nm laser light. An applied
                                                                                   C(t)                                              magnetic field B along the NV axis splits the |ms = ±1⟩ states, allowing
                                                                                                                                     us to work within the effective spin 1/2 manifold {|0⟩ , |−1⟩}. Micro­
                             –1                                                             0                                        wave pulses at frequency ωNV are used to perform coherent spin
                        10                                                                      0                  5
                                                                                                          t (µs)                     rotations (that is, for Ramsey spectroscopy or spin echo) within this
                                                                    0                                                            1
                                                            10                                                              10       manifold (Fig. 1c).
                                                                           Time, t (µs)                                                   Physically, the NV and P1 centres are also coupled via dipolar
                                                                                                                                     interactions. However, for a generic magnetic field strength, they
Fig. 2 | Dimensionality and dynamics from many-body noise. a, The
normalized coherence for a DEER measurement on sample S1 (blue) and
                                                                                                                                     are highly detuned, that is, ∣ωNV − ωP1∣ is on the order of gigahertz,
sample S2 (yellow) as a function of the free evolution time t. Dashed blue                                                           owing to the zero-field splitting of the NV centre (Δ0 = 2π × 2.87 GHz)
lines indicate the predicted early- and late-time stretch powers of 2/3 and 1/3,                                                     (Fig. 1c). Since typical interaction strengths in our system are on the
respectively, for a dipolar spin system in two dimensions. The dashed yellow                                                         order of megahertz, direct polarization exchange between an NV
line depicts the predicted early-time stretch power of 1 for a dipolar spin system                                                   and P1 is strongly off-resonant. The strong suppression of
in three dimensions (Table 1). Together, these data demonstrate the two- and                                                         spin-exchange interactions between NV and P1 centres simplifies
three-dimensional nature of samples S1 and S2, respectively. The lower right                                                         the full magnetic dipole–dipole Hamiltonian to a system–probe
insets show the same data on a linear scale. The top left inset shows the DEER                                                       Ising coupling of precisely the form given by equation (1) with α = 3
pulse sequence. b, Spin echo measurements on three-dimensional dipolar spin                                                          (Supplementary Information).
ensembles in samples S3 (teal) and S4 (red) clearly exhibit a stretch power of
3/2 (dotted lines) over nearly two decades in time. This is consistent with the
                                                                                                                                     Delta-doped sample fabrication
presence of Gaussian noise and allows one to explicitly rule out telegraph noise.
                                                                                                                                     Sample S1 was grown via homoepitaxial plasma-enhanced
The lower right inset shows the same data on a linear scale. The top left inset
                                                                                                                                     chemical vapour deposition using isotopically purified methane
shows the spin echo pulse sequence. All data are presented as mean ± s.e.m.
                                                                                                                                     (99.999% 12C)22. The delta-doped layer was formed by introdu­cing
                                                                                                                                     natural-abundance nitrogen gas during growth (5 sccm, 10 min)
                                                                                                                                     in between nitrogen-free buffer and capping layers. To create the
                                                                                                                                     vacancies necessary for generating NV centres, the sample was
simple prediction, namely that the stretch power, β, of the probe’s                                                                  electron irradiated with a transmission electron microscope set to
exponential decay (that is, − log C ∝ ⟨ϕ2 ⟩ ∼ tβ ) changes from D/α to                                                               145 keV (ref. 23) and subsequently annealed at 850 °C for 6 h.
D/2α at the correlation time (Fig. 1f).
      Second, moving beyond Ramsey measurements by changing the                                                                      Two-dimensional spin dynamics
filter function, one can probe more subtle properties of the many-body                                                               We begin by performing double electron-electron resonance
noise. In particular, a spin echo sequence filters out the leading-order                                                             (DEER) measurements on sample S1. While largely analogous to
DC contribution from the many-body noise spectrum, allowing one                                                                      Ramsey spectroscopy (Table 1), DEER has the technical advantage
to investigate higher-frequency correlations of the spin-flip dynam-                                                                 that it filters out undesired quasi-static fields (for example, from
ics. Different types of spin-flip dynamics naturally lead to different                                                               hyperfine interactions between the NV and host nitrogen nucleus)7,24.
phase distributions. For the case of Gaussian noise, one finds that                                                                  As shown in Fig. 2a (inset, blue data), the NV’s coherence decays on a
(at early times) χ ∼ t3. However, in the case of telegraph noise, the                                                                timescale of approximately 5 μs.
analysis is more subtle since higher-order moments of ϕ(t) must be                                                                        To explore the functional form of the probe NV’s decoherence, we
taken into account. This leads to markedly different early-time predic-                                                              plot the negative logarithm of the coherence, − log C(t), on a log–log
tions for β, dependent on both the measurement sequence as well as                                                                   scale, such that the stretch power, β, is simply given by the slope of
the many-body noise (Table 1).                                                                                                       the data. At early times, the data exhibit β = 2/3 for over a decade
      At late times, however, one expects the probe’s coherence to agree                                                             in time (Fig. 2a, blue data). At a timescale of approximately 3 μs
across different pulse sequences and spin-flip dynamics. For example,                                                                (vertical dashed line), the data cross over to a stretch power of β = 1/3


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                                                                                    839
Article                                                                                                                                         https://doi.org/10.1038/s41567-023-01944-5


                                     a                                          b                                            c
                                                Two dimensional (S1)                      Three dimensional (S2)                                              t
                                                                                10
                                                                                      1                                         Laser
                                                                                                                                                    π                    π
                                                                                                                                 NV                 2         π          2

                                                                                            1
                                                                                                                                 P1                          (π)
                                     10
                                          0
                                               2/3                                                                              Ω, δω
                                                                        1/3     10
                                                                                     0




                         –log C(t)
                                                                                                                                                                    τc



                                          –1                                         –1
                                                                                                         3/2                      Siz (t)
                                     10                                         10
                                                          Ω/2π = 0.61 MHz                             Ω/2π = 0.26 MHz                                   τc
                                                     1
                                                                                10
                                                                                      1                                                                       t
                                                                                                                             d         6

                                          0
                                                                                                                                                                  Sample S1
                                     10                                              0
                                                                                10

                         –log C(t)
                                                                                                                                        4

                                                                                                                             τc (µs)
                                                                                                                                        2
                                          –1                                         –1
                                     10                                         10
                                                          Ω/2π = 1.22 MHz                             Ω/2π = 1.18 MHz
                                                                                      1
                                                                                                                                       0
                                                                                10                                                          0                 2               4
                                                Spin echo                                 Spin echo
                                                                                                                             e         20
                                                DEER                                      DEER
                                     10
                                          0                                                                         1/2
                                                                                     0
                                                                                                                                                                  Sample S2

                         –log C(t)
                                                                                10


                                                                                                                             τc (µs)   10
                                                                                     –1
                                     10
                                          –1
                                                                                10
                                                         Ω/2π = 2.44 MHz                              Ω/2π = 2.35 MHz
                                                                                                                                       0
                                               10
                                                    0
                                                              10
                                                                1
                                                                        10
                                                                            2
                                                                                            10
                                                                                                 0
                                                                                                                    10
                                                                                                                         1
                                                                                                                                        10              1            2        3

                                                         Time, t (µs)                                Time, t (µs)                                       Ω/2π (MHz)

Fig. 3 | Tuning the correlation time of the bath. a,b, Measurements of DEER                               mean ± s.e.m. c, An incoherent drive field (light blue) with power ∼Ω2 and
(blue and orange) and spin echo (red and teal) on two- and three-dimensional                              linewidth δω is applied to the P1 spins during the free evolution time t of both
samples (S1 and S2) for different powers of the polychromatic (that is,                                   DEER and spin echo sequences to tune the correlation time of the many-body
incoherent) drive at fixed linewidth δω of 2π × 18 MHz and 2π × 20 MHz,                                   system. In this case, szi (t) evolves as a Gaussian random process [schematic for
respectively. The time at which the two signals overlap (vertical dashed lines) acts                      short (blue) and long (grey) correlation time τc]. d,e, The correlation times, τc,
as a proxy for the correlation time and decreases as the power of the incoherent                          extracted from fitting the data to equation (5) for samples S1 (purple) and S2
driving increases (top to bottom panels). The data are well fitted by analytic                            (green) plotted as a function of Ω, agreeing well with a simple theoretical model
expressions for [χ(t)]D/2α (equation (5)) (dashed curves). Data are presented as                          (dashed grey curves). Data presented as best fit values ± fitting error.




for another decade in time. This behaviour is in excellent agreement                                      binary variables, thereby generating telegraph noise. For the specific
with that expected for two-dimensional spin dynamics driven by                                            case of dipolar spin ensembles, this expectation dates back to
dipolar interactions (Fig. 1f and Table 1).                                                               seminal work from Klauder and Anderson6. The intuition behind
     For comparison, we perform DEER spectroscopy on a conventional                                       this noise model is most easily seen in the language of the master
three-dimensional NV–P1 system (sample S2; Methods). As shown in                                          equation—each individual spin ‘sees’ the remaining system as a
Fig. 2a (orange), the data exhibit β = 1 for a decade in time, consistent                                 Markovian bath. The resulting local spin dynamics are then charac­
with the prediction for three-dimensional dipolar interactions                                            terized by a series of stochastic quantum jumps that flip the spin
(Table 1). However, the cross-over to the late-time ‘random walk’ regime                                  orientation and give rise to telegraph noise. Alternatively, in the
is difficult to experimentally access because the larger early-time                                       Heisenberg picture, the same intuition can be understood from the
                                                                                                                                      z
stretch power causes a faster decay to the noise floor.                                                   spreading of the operator sî . This spreading hides local coherences in
                                                                                                          many-body correlations, leading to an ensemble of telegraph-like,
Characterizing microscopic spin-flip dynamics                                                             classical trajectories (Supplementary Information).
To probe the nature of the microscopic spin-flip dynamics in our                                               We conjecture that the observation of Gaussian spectral
system, we perform spin echo measurements on three dimensional                                            diffusion in our system is related to the presence of disorder, which
samples (S3 and S4 (type IB)), which exhibit a much higher P1-to-NV                                       strongly suppresses operator spreading 50. To illustrate this
density ratio (Methods). For lower relative densities (that is, samples S1                                point, consider the limiting case where the operator dynamics are
                                                                                                                                                                              z
and S2), the spin echo measurement contains a confounding                                                 constrained to a single spin. In this situation, the dynamics of sî (t)
signal from interactions between the NVs themselves (Methods).                                            follow a particular coherent trajectory around the Bloch sphere
     In both samples (S3 and S4), we find that the coherence exhibits a                                   and the rate at which the probe accumulates phase is continuous.
stretched exponential decay with β = 3/2 for well over a decade in time                                   Averaging over different trajectories of the coherent dynamics
(Fig. 2b). Curiously, this is consistent with Gaussian spectral diffusion                                 naturally leads to Gaussian noise.
where β = 3D/2α = 3/2 but patently inconsistent with the telegraph
noise prediction of β = 1 + D/α = 2. While in agreement with prior                                        Controlling the P1 spectral function
measurements on similar samples38, this observation is actually                                           Next, we demonstrate the ability to directly control the P1 noise spec-
rather puzzling and related to a question in the context of dipolar                                       trum for both two- and three-dimensional dipolar spin ensembles (that
spin noise4,6,7,13–16,19,28,33–39,47–49. In particular, one naively expects that                          is, samples S1 and S2). In particular, we engineer the shape and linewidth
spins in a strongly interacting system should be treated as stochastic                                    of S(ω) by driving the P1 system with a polychromatic microwave tone40.


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                                                        840
Article                                                                                                         https://doi.org/10.1038/s41567-023-01944-5

This drive is generated by adding phase noise to the resonant microwave                     a     1.0
signal at ωP1 to produce a Lorentzian drive spectrum with linewidth
δω (Fig. 3c). While such techniques originated in the context of                                                           Laser
                                                                                                  0.8
broadband noise decoupling40, here we directly tune the correla-                                                                                           τp
                                                                                                                            NV
tion time of the P1 system and measure a corresponding change in
                                                                                                  0.6
the cross-over timescale between coherent and incoherent spin
dynamics15,49.                                                                             C(t)
                                                                                                  0.4
      Microscopically, the polychromatic drive leads to a number
of physical effects. First, tuning the Rabi frequency, Ω, of the drive
provides a direct knob for controlling the correlation time, τc, of                               0.2

the P1 system. Second, since the many-body system inherits the
noise spectrum of the drive, one has provably Gaussian statistics                                  0

for the spin variables szi (Supplementary Information). Third, our                                      0           250         500                        750            1,000

earlier Markovian assumption is explicitly enforced by the presence                                                       Time, t (µs)
of a Lorentzian noise spectrum. Taking these last two points together
allows one to analytically predict the precise form of the NV probe’s                       b
                                         D/2α                                                     1.0
decoherence profile, − log C(t) ∼ χ(t)        , for either DEER or spin                                                                      10
                                                                                                                                                  0




                                                                                                                                 –log C(t)
echo spectroscopy:
                                                                                                  0.8
                                                      t
                                                   −
                 χDEER (t) = 2τc t − 2τ2c (1 − e     τc   ),                                      0.6
                                                                                                                                             10
                                                                                                                                                  –1
                                                                                                                                                   10
                                                                                                                                                       1
                                                                                                                                                                  10
                                                                                                                                                                      2
                                                                                                                                                                           10
                                                                                                                                                                             3



                                                   t               t
                                                                         (5)               C(t)
                                                                                                                                                                 t (µs)
                                             −                 −
                 χSE (t) = 2τc t − 2τ2c (3 + e τc − 4e 2τc ) .                                    0.4


                                                                                                        Laser
                                                                                                  0.2
     We perform both DEER and spin echo measurements as a function                                       NV         t
of the power (∼Ω2) of the polychromatic drive for our two-dimensional                                    P1         t
                                                                                                   0
sample (S1) (Fig. 3a). As expected, for weak driving (Fig. 3a, top), the
                                                                                                        0         200     400                600                800       1,000
DEER signal (blue) is analogous to the undriven case, exhibiting a
                                                                                                                          Time, t (µs)
cross-over from a stretch power of β = 2/3 at early times to a stretch
power of β = 1/3 at late times. For the same drive strength, the spin                       c
echo data (red) also exhibit a cross-over between two distinct stretch
powers, with the key difference being that β = 3D/2α = 1 at early times.                          0.8
This represents an independent (spin echo based) confirmation of
the two-dimensional nature of our delta-doped sample.
     Recall that, at late times (that is t ≳ τc), one expects the NV’s coher-
                                                                                                  0.7
ence C(t) to agree across different pulses sequences (Fig. 1f). This                       C

is indeed borne out by the data (Fig. 3). In fact, the location of this
                                                                                                        Laser
late-time overlap provides a proxy for estimating the correlation
                                                                                                  0.6   NV         ΩNV
time and is shown as the dashed grey lines in Fig. 3a. As one increases
                                                                                                         P1        ΩP1
the power of the drive (Fig. 3a), the noise spectrum, S(ω), naturally
                                                                                                                    ts
broadens. In the data, this manifests as a shortened correlation
time, with the location of the DEER/echo overlap shifting to earlier                                    0           2.5          5.0                       7.5            10.0
timescales (Fig. 3a).                                                                                                     ΩP1/2π (MHz)
     Analogous measurements on a three-dimensional spin ensemble
                                                                                Fig. 4 | Hybrid two-dimensional spin system for simulation and sensing.
(sample S2) reveal much the same physics (Fig. 3b), with stretch powers         a, We measure T2 with spin echo (blue), XY-8 (orange) and DROID (red) pulse
again consistent with a Gauss–Markov prediction (Table 1). For weak             sequences with interpulse spacing of τp = 100 ns. The spin echo and XY-8
driving, C(t) is consistent with the early-time ballistic regime for over       decoherence profiles are fitted by equation (5), while DROID is fitted by
a decade in time (Fig. 3b, top). However, it is difficult to access late                                            1/2
                                                                                a stretched exponential ∼ e−(t/T2 ) . The 1/e lifetimes (grey line) for spin echo,
enough timescales to observe an overlap between DEER and spin echo.             XY-8 and DROID are 22 μs, 47 μs and 302 μs, respectively. Inset: schematic of
Crucially, by using the drive to push to shorter correlation times, we          dynamical decoupling sequence with interpulse spacing τp. b, Spin-locked NV
can directly observe the late-time random-walk regime in three dimen-           depolarization profile. Only NV centres (orange) or both NV and P1 centres
sions, where β = 1/2 (Fig. 3b, middle and bottom).                              (green) are driven at a Rabi frequency of 2π × 5 MHz. The resonant spin-exchange
     Remarkably, as evidenced by the dashed curves in Fig. 3a,b our             interactions reduce the spin-locking relaxation time T1ρ by a factor of 3. The top
data exhibit excellent agreement—across different dimensionalities,             inset shows the same data plotted on a log–log scale to elucidate stretch powers.
drive strengths and pulse sequences—with the analytic predictions               Bottom inset: spin-locking pulse sequence. c, Hartmann–Hahn polarization
presented in equation (5). Moreover, by fitting χD/2α simultaneously            exchange resonance. The NV Rabi frequency ΩNV is fixed at 2π × 5 MHz. When the
                                                                                P1 Rabi frequency ΩP1 matches ΩNV, a reduction in contrast is induced by the
across spin echo and DEER datasets for each Ω, we quantitatively
                                                                                resonant polarization exchange between NV and P1 centres. The data are fitted by
extract the correlation time, τc. Up to an 𝒪𝒪(1) scaling factor, we find
                                                                                a Lorentzian (dashed curve) with a linewidth of 2π × 1.2 MHz. Inset: Hartmann–
that the extracted τc agrees well with the DEER/echo overlap time.
                                                                                Hahn pulse sequence, with fixed spin-locking duration ts = 200 μs. All data
In addition, the behaviour of τc as a function of Ω also exhibits quanti­
                                                                                presented as mean ± s.e.m.
tative agreement with an analytic model that predicts τc ∼ δω/Ω2 in
the limit of strong driving (Fig. 3d,e).
     We emphasize that, although one observes β = 3D/2α in both the             Gaussian spectral diffusion emerges from isolated, disordered,
driven (Fig. 3a,b) and undriven (Fig. 2b) spin echo measurements,               many-body dynamics, while in the former case, it is imposed by the
the underlying physics is extremely different. In the latter case,              external drive.


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                                                  841
Article                                                                                                 https://doi.org/10.1038/s41567-023-01944-5

A two-dimensional solid-state platform for                                    Conclusion and outlook
quantum simulation and sensing                                                Our results demonstrate the diversity of information that can be
Our platform offers two distinct paths towards quantum simulation and         accessed via the decoherence dynamics of a probe spin ensemble.
sensing using strongly interacting, two-dimensional, spin-polarized           For example, we shed light on a long-standing debate about the nature
ensembles. First, treating the NV centres themselves as the many-body         of spin-flip noise in a strongly interacting dipolar system4,6,16,33–39,48,49.
system directly leverages their optical polarizability. However, given        Moreover, we directly measure the correlation time of the many-body
their relative diluteness, it is natural to ask whether one can access        system and introduce a technique to probe its dimensionality. This tech-
regimes where the NV–NV interactions dominate over other energy               nique is particularly useful for disordered spin ensembles embedded in
scales. Conversely, treating the P1 centres as the many-body system           solids58,59, where a direct, non-destructive measurement of nanoscale
takes advantage of their higher densities and interaction strengths,          spatial properties is challenging with conventional toolsets.
with the key challenge being that these dark spins cannot be optically             One can imagine generalizing our work in a number of promising
pumped. Here, we demonstrate that both of these paths are viable for          directions. First, the ability to fabricate and characterize strongly
sample S1: (1) we show that the dipolar interactions among NV centres         interacting, two-dimensional dipolar spin ensembles opens the
can dominate their decoherence dynamics, using advanced dynamical             door to a number of intriguing questions within the landscape
decoupling sequences, and (2) we demonstrate direct polarization              of quantum simulation. Indeed, dipolar interactions in 2D are quite
exchange between NV and P1 centres, providing a mechanism to spin             special from the perspective of localization, allowing one to experi-
polarize the P1 system.                                                       mentally probe the role of many-body resonances55,56. In the context
                                                                              of ground-state physics, the long-range, anisotropic nature of the
Interacting NV ensemble                                                       dipolar interaction has also been predicted to stabilize a number of
To demonstrate NV–NV interaction-dominated dynamics, we                       exotic phases, ranging from supersolids to spin liquids25,26. Connect-
compare the decoherence timescales between spin echo, XY-8                    ing this latter point back to noise spectroscopy, one could imagine
and disorder-robust interaction decoupling (DROID) dynamical                  tailoring the probe’s filter function to distinguish between different
decoupling sequences51. The spin echo effectively decouples static            types of ground-state order.
disorder, while the XY-8 sequence further decouples NV–P1 inter­                   Second, dense ensembles of two-dimensional spins also promise
actions. As depicted in Fig. 4a, XY-8 pulses extend the spin echo             a number of unique advantages with respect to quantum sensing21,22,24.
decay time (defined as the 1/e time) by approximately a factor of             For example, a 2D layer of NVs fabricated near the diamond surface
two. With NV–P1 interactions decoupled, our hypothesis is that                would exhibit a pronounced enhancement in spatial resolution
the dynamics are now driven by dipolar interactions between the NV            (set by the depth of the layer) compared with a three-dimensional
centres. To test this, we perform a DROID decoupling sequence, which          ensemble at the same density, ρ (refs. 22,60). In addition, for samples
eliminates the dipolar dynamics between NV centres51 (Methods).               where the coherence time is limited by spin–spin interactions, a lower
Remarkably, this extends the coherence time by nearly an order of             dimensionality reduces the coordination number and leads to an
magnitude, demonstrating that NV–NV interactions are, by far, the             enhanced T2 scaling as n−α/D (Supplementary Information).
dominant source of many-body dynamics in this regime. Moreover, the                Third, one can probe the relationship between operator spreading
XY-8 decoherence thus provides an estimate of an average NV spin–spin         and Gauss–Markov noise by exploring samples with different relaxation
spacing of 15 nm.                                                             rates, interaction power laws, disorder strengths and spin densities33,49.
                                                                              One could also utilize alternate pulse sequences, such as stimulated
Interacting P1 ensemble                                                       echo, to provide a more fine-grained characterization of the many-body
The polarization of the optically dark P1 ensemble can be realized            noise (for example, the entire spectral diffusion kernel)28,33.
by either (1) working at low temperatures and large magnetic                       Finally, our framework can also be applied to long-range-interacting
fields52 or (2) using NV centres to transfer polarization to the P1           systems of Rydberg atoms, trapped ions and polar molecules. In such
centres. Here, we focus on the latter. While NV–P1 polarization               systems, the ability to perform imaging and quantum control at
transfer has previously been demonstrated53,54, it has not been               the single-particle level allows for greater freedom in designing
measured in a two-dimensional system. Indeed, conjectures about               methods to probe many-body noise. As a particularly intriguing
localization in such systems indicate that polarization transfer could        example, one could imagine a non-destructive, time-resolved generali­
be highly suppressed55,56.                                                    zation of many-body noise spectroscopy, where one repeatedly
     To investigate, we employ a Hartmann–Hahn sequence designed              interrogates the probe without projecting the many-body system.
to transfer polarization between NV and P1 spins in the rotating
frame53,54. In particular, we drive the NV and P1 spins independently,        Online content
with Rabi frequencies ΩNV and ΩP1. When only the NV centres are driven,       Any methods, additional references, Nature Portfolio reporting sum-
we are effectively performing a so-called spin-locking measurement57.         maries, source data, extended data, supplementary information,
For ΩNV = 2π × 5 MHz, we find that the NV centres depolarize on a             acknowledgements, peer review information; details of author contri-
timescale of T1ρ = 1.05(3) ms (Fig. 4b, orange). The data are cleanly fit     butions and competing interests; and statements of data and code avail-
by a simple exponential and consistent with phonon-limited decay              ability are available at https://doi.org/10.1038/s41567-023-01944-5.
(Fig. 4b, inset). By contrast, when the driving satisfies the Hartmann–
Hahn condition, ΩNV = ΩP1, the NV and P1 spins can resonantly                 References
exchange polarization. To characterize this, we fix ΩNV = 2π × 5 MHz          1.   Purcell, E. M. in Confined Electrons and Photons (eds Burstein, E. &
and choose a spin-locking duration ts = 200 μs. By sweeping the P1 Rabi            Weisbuch, C.) 839–839 (Springer, 1995).
frequency, we indeed observe a resonant polarization exchange feature         2.   Viola, L., Knill, E. & Lloyd, S. Dynamical decoupling of open
centred at ΩP1 = 2π × 5 MHz with a linewidth of ∼ 2π × 1.2 MHz (Fig. 4c),          quantum systems. Phys. Rev. Lett. 82, 2417–2421 (1999).
consistent with the intrinsic P1 linewidth. As illustrated in Fig. 4b, on     3.   Houck, A. et al. Controlling the spontaneous emission of a
resonance, the NV depolarization is notably enhanced via polarization              superconducting transmon qubit. Phys. Rev. Lett. 101, 080502
transfer to the P1 centres and the data exhibit a three-fold decrease in           (2008).
the decay time. Moreover, the data are well fitted with a stretch power of    4.   De Lange, G., Wang, Z., Riste, D., Dobrovitski, V. & Hanson, R.
β = 1/3 (Fig. 4b, inset), which is also indicative of interaction-dominated        Universal dynamical decoupling of a single solid-state spin from a
decay47 (Methods).                                                                 spin bath. Science 330, 60–63 (2010).


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                       842
Article                                                                                           https://doi.org/10.1038/s41567-023-01944-5

5.  Tyryshkin, A. M. et al. Electron spin coherence exceeding seconds    31. Cho, G. & Yesinowski, J. P. H and 19f multiple-quantum NMR
    in high-purity silicon. Nat. Mater. 11, 143–147 (2012).                  dynamics in quasi-one-dimensional spin clusters in apatites.
6. Klauder, J. & Anderson, P. Spectral diffusion decay in spin               J. Phys. Chem. 100, 15716–15725 (1996).
    resonance experiments. Phys. Rev. 125, 912 (1962).                   32. Cho, H., Ladd, T. D., Baugh, J., Cory, D. G. & Ramanathan, C.
7. Schweiger, A. & Jeschke, G. Principles of Pulse Electron                  Multispin dynamics of the solid-state NMR free induction decay.
    Paramagnetic Resonance (Oxford University Press on Demand,               Phys. Rev. B 72, 054427 (2005).
    2001).                                                               33. Mims, W. Phase memory in electron spin echoes, lattice relaxation
8. Kofman, A. & Kurizki, G. Acceleration of quantum decay processes          effects in CaWO4: Er, Ce, Mn. Phys. Rev. 168, 370 (1968).
    by frequent observations. Nature 405, 546–550 (2000).                34. Abe, E., Itoh, K. M., Isoya, J. & Yamasaki, S. Electron-spin phase
9. Romach, Y. et al. Spectroscopy of surface-induced noise using             relaxation of phosphorus donors in nuclear-spin-enriched silicon.
    shallow spins in diamond. Phys. Rev. Lett. 114, 017601 (2015).           Phys. Rev. B 70, 033204 (2004).
10. Kleppner, D. Inhibited spontaneous emission. Phys. Rev. Lett. 47,    35. Zhong, M. et al. Optically addressable nuclear spins in a solid with
    233 (1981).                                                              a six-hour coherence time. Nature 517, 177–180 (2015).
11. Kotler, S., Akerman, N., Glickman, Y., Keselman, A. & Ozeri, R.      36. de Sousa, R. & Sarma, S. D. Theory of nuclear-induced spectral
    Single-ion quantum lock-in amplifier. Nature 473, 61–65 (2011).          diffusion: spin decoherence of phosphorus donors in si and gaas
12. Bar-Gill, N. et al. Suppression of spin-bath dynamics for improved       quantum dots. Phys. Rev. B 68, 115322 (2003).
    coherence of multi-spin-qubit systems. Nat. Commun. 3, 1–6           37. Wang, Z.-H. & Takahashi, S. Spin decoherence and electron spin
    (2012).                                                                  bath noise of a nitrogen-vacancy center in diamond. Phys. Rev. B
13. Herzog, B. & Hahn, E. L. Transient nuclear induction and double          87, 115122 (2013).
    nuclear resonance in solids. Phys. Rev. 103, 148–166 (1956).         38. Bauch, E. et al. Decoherence of ensembles of nitrogen-vacancy
14. Kubo, R., Toda, M. & Hashitsume, N. Statistical Physics II:              centers in diamond. Phys. Rev. B 102, 134210 (2020).
    Nonequilibrium Statistical Mechanics, Vol. 31 (Springer Science &    39. Hanson, R., Dobrovitski, V., Feiguin, A., Gywat, O. & Awschalom, D.
    Business Media, 2012).                                                   Coherent dynamics of a single spin interacting with an adjustable
15. Salikhov, K., Dzuba, S.-A. & Raitsimring, A. M. The theory of            spin bath. Science 320, 352–355 (2008).
    electron spin-echo signal decay resulting from dipole–dipole         40. Ernst, R. R. Nuclear magnetic double resonance with an incoherent
    interactions between paramagnetic centers in solids. J. Magn.            radio-frequency field. J. Chem. Phys. 45, 3845–3861 (1966).
    Reson. (1969) 42, 255–276 (1981).                                    41. Hu, P. & Hartmann, S. R. Theory of spectral diffusion decay using
16. Chiba, M. & Hirai, A. Electron spin echo decay behaviours of             an uncorrelated-sudden-jump model. Phys. Rev. B 9, 1–13 (1974).
    phosphorus doped silicon. J. Phys. Soc. Jpn. 33, 730–738 (1972).     42. Cucchietti, F. M., Paz, J. P. & Zurek, W. H. Decoherence from spin
17. Altman, E., Demler, E. & Lukin, M. D. Probing many-body states of        environments. Phys. Rev. A 72, 052113 (2005).
    ultracold atoms via noise correlations. Phys. Rev. A 70, 013603      43. de Sousa, R. in Electron Spin Resonance and Related Phenomena
    (2004).                                                                  in Low-Dimensional Structures (ed Fanciulli, M.) 183–220
18. Hofferberth, S. et al. Probing quantum and thermal noise in an           (Springer, 2009).
    interacting many-body system. Nat. Phys. 4, 489–495 (2008).          44. Yang, W., Ma, W.-L. & Liu, R.-B. Quantum many-body theory for
19. Fel’dman, E. B. & Lacelle, S. Configurational averaging of dipolar       electron spin decoherence in nanoscale nuclear spin baths.
    interactions in magnetically diluted spin networks. J. Chem. Phys.       Rep. Prog. Phys. 80, 016001 (2017).
    104, 2000–2009 (1996).                                               45. Kogan, S. Electronic Noise and Fluctuations in Solids (Cambridge
20. Choi, S. et al. Observation of discrete time-crystalline order in        Univ. Press, 2008).
    a disordered dipolar many-body system. Nature 543, 221–225           46. Witzel, W. & Sarma, S. D. Quantum theory for electron
    (2017).                                                                  spin decoherence induced by nuclear spin dynamics in
21. Sushkov, A. et al. Magnetic resonance detection of individual            semiconductor quantum computer architectures: spectral
    proton spins using quantum reporters. Phys. Rev. Lett. 113, 197601       diffusion of localized electron spins in the nuclear solid-state
    (2014).                                                                  environment. Phys. Rev. B 74, 035322 (2006).
22. Ohno, K. et al. Engineering shallow spins in diamond with            47. Choi, J. et al. Depolarization dynamics in a strongly interacting
    nitrogen delta-doping. Appl. Phys. Lett. 101, 082413 (2012).             solid-state spin ensemble. Phys. Rev. Lett. 118, 093601 (2017).
23. McLellan, C. A. et al. Patterned formation of highly coherent        48. Zhidomirov, G. & Salikhov, K. Contribution to the theory of
    nitrogen-vacancy centers using a focused electron irradiation            spectral diffusion in magnetically diluted solids. Sov. J. Exp.
    technique. Nano Lett. 16, 2450–2454 (2016).                              Theor. Phys. 29, 1037 (1969).
24. Eichhorn, T. R., McLellan, C. A. & Bleszynski Jayich, A. C.          49. Glasbeek, M. & Hond, R. Phase relaxation of photoexcited triplet
    Optimizing the formation of depth-confined nitrogen vacancy              spins in cao. Phys. Rev. B 23, 4220 (1981).
    center spin ensembles in diamond for quantum sensing.                50. Witzel, W. M., Carroll, M. S., Cywiński, Ł. & Sarma, S. D. Quantum
    Phys. Rev. Mater. 3, 113802 (2019).                                      decoherence of the central spin in a sparse system of dipolar
25. Yao, N. Y., Zaletel, M. P., Stamper-Kurn, D. M. & Vishwanath, A. A       coupled spins. Phys. Rev. B 86, 035452 (2012).
    quantum dipolar spin liquid. Nat. Phys. 14, 405–410 (2018).          51. Zhou, H. et al. Quantum metrology with strongly interacting spin
26. Chomaz, L. et al. Long-lived and transient supersolid behaviors in       systems. Phys. Rev. X 10, 031003 (2020).
    dipolar quantum gases. Phys. Rev. X 9, 021012 (2019).                52. Takahashi, S., Hanson, R., Van Tol, J., Sherwin, M. S. & Awschalom,
27. Semeghini, G. et al. Probing topological spin liquids on a               D. D. Quenching spin decoherence in diamond through spin bath
    programmable quantum simulator. Science 374, 1242–1247 (2021).           polarization. Phys. Rev. Lett. 101, 047601 (2008).
28. Anderson, P. W. & Weiss, P. R. Exchange narrowing in                 53. Belthangady, C. et al. Dressed-state resonant coupling between
    paramagnetic resonance. Rev. Mod. Phys. 25, 269–276 (1953).              bright and dark spins in diamond. Phys. Rev. Lett. 110, 157601 (2013).
29. Georgescu, I. M., Ashhab, S. & Nori, F. Quantum simulation.          54. Laraoui, A. & Meriles, C. A. Approach to dark spin cooling in a
    Rev. Mod. Phys. 86, 153 (2014).                                          diamond nanocrystal. ACS Nano 7, 3403–3410 (2013).
30. Engelsberg, M., Lowe, I. & Carolan, J. Nuclear-magnetic-             55. Bruin A. Many-body delocalization in a strongly disordered
    resonance line shape of a linear chain of spins. Physical Review B       system with long-range interactions: finite-size scaling.
    7, 924 (1973).                                                           Phys. Rev. B 91, 094202 (2015).


Nature Physics | Volume 19 | June 2023 | 836–844                                                                                              843
Article                                                                                               https://doi.org/10.1038/s41567-023-01944-5

56. Yao, N. Y. et al. Many-body localization with dipoles. Phys. Rev. Lett.   Open Access This article is licensed under a Creative Commons
    113, 243002 (2014).                                                       Attribution 4.0 International License, which permits use, sharing,
57. Hartmann, S. & Hahn, E. Nuclear double resonance in the rotating          adaptation, distribution and reproduction in any medium or format,
    frame. Phys. Rev. 128, 2042 (1962).                                       as long as you give appropriate credit to the original author(s) and the
58. Cappellaro, P., Ramanathan, C. & Cory, D. G. Dynamics and                 source, provide a link to the Creative Commons license, and indicate
    control of a quasi-one-dimensional spin system. Phys. Rev. A 76,          if changes were made. The images or other third party material in this
    032317 (2007).                                                            article are included in the article’s Creative Commons license, unless
59. Lukin, D. M., Guidry, M. A. & Vučković, J. Integrated quantum             indicated otherwise in a credit line to the material. If material is not
    photonics with silicon carbide: challenges and prospects.                 included in the article’s Creative Commons license and your intended
    PRX Quantum 1, 020102 (2020).                                             use is not permitted by statutory regulation or exceeds the permitted
60. Rosskopf, T. et al. Investigation of surface magnetic noise by            use, you will need to obtain permission directly from the copyright
    shallow spins in diamond. Phys. Rev. Lett. 112, 147602 (2014).            holder. To view a copy of this license, visit http://creativecommons.
                                                                              org/licenses/by/4.0/.
Publisher’s note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.       © The Author(s) 2023




Nature Physics | Volume 19 | June 2023 | 836–844                                                                                                  844
Article                                                                                                   https://doi.org/10.1038/s41567-023-01944-5

Methods                                                                          Sample S2. A detailed characterization of the three-dimensional
Sample preparation and characterization                                          sample S2 is given in ref. 24 (sample C041). Here, we describe the key
Sample S1. Sample fabrication                                                    properties relevant for the present study. The sample was grown
      Here, we add to the details provided in Section Delta-doped sam-           by depositing a 32 nm diamond buffer layer, followed by a 500 nm
ple fabrication. Sample S1 was grown on a commercially available                 nitrogen-doped layer (99%15N), and finished with a 50 nm undoped
Element-6 electronic grade (100) substrate, polished by Syntek61 to a            diamond capping layer. Vacancies were created by irradiating with
surface roughness less than 200 pm. Throughout the plasma-enhanced               145 keV electrons at a dosage of 1021 cm−2, and vacancy diffusion was
chemical vapour deposition growth process22, we used 400 sccm of                 activated by annealing at 850 °C for 48 h in an Ar/Cl atmosphere.
hydrogen gas with a background pressure of 25 Torr, and a microwave              The resulting NV density is ∼0.4 ppm, obtained through instanta-
power of 750 W. The sample temperature was held at 800 °C.                       neous diffusion measurements24. The P1 density is measured to be
NV density                                                                       ∼20 ppm through a modified DEER sequence24. The average spacing
      We estimate the NV areal density in sample S1 via the XY-8                 between P1 centres (∼4 nm) is much smaller than the thickness of
decoherence profile62, which is dominated by intragroup NV interac-              the nitrogen-doped layer, ensuring three-dimensional behaviour of
tions (that is, within the NV group aligned with the applied magnetic            the spin ensemble.
field B) (Fig. 4a). We therefore treat the XY-8 data as a Ramsey measure-
ment of the average NV–NV coupling, which we convert to a density                Samples S3 and S4. Samples S3 and S4 used in this work are syn-
using the dipolar interaction strength J0 = 2π × 52 MHz nm3. We com-             thetic type Ib single/crystal diamonds (Element Six) with intrinsic
pare the XY-8 data with numerically computed Ramsey decoherence,                 substitutional 14N concentration of ∼100 ppm (calibrated with an NV
which we calculate as follows: We consider a central probe NV inter­             linewidth measurement63). To create NV centres, the samples were
acting with a bath of other NVs, placed randomly in a thin slab of thick-        first irradiated with electrons (2 MeV energy and 1 × 1018 cm−2 dosage)
ness w with density nNV  3D
                            /4 (one NV group). After selecting a random spin     to generate vacancies. After irradiation, the diamonds were annealed
configuration for the bath NVs, we compute the Ramsey signal ∼ cos(ϕ)            in vacuum (∼10−6 Torr) with temperature >800 °C. The NV densities
for the probe NV. We then average over many such samples, and the                for both samples were measured to be ∼0.5 ppm using a spin-locking
resulting curve exhibits a stretched exponential decay of the form               measurement63.
                2/3
C(t) = e−(t/T2 ) . This functional form matches our expectation for the
early-time ballistic regime (Table 1), because we have not included flip-        Experimental methods
flop dynamics in the numerical model. We treat the decoherence as                Experimental details for sample S1. The delta-doped sample S1 was
arising only from intragroup Ising interactions, which is correct at short       mounted in a scanning confocal microscope. For optical pumping and
times when the NV centres are spin polarized. With the above prescrip-           readout of the NV centres, about 100 μW of 532 nm light was directed
tion, we compute a set of Ramsey signals (Extended Data Fig. 1a, dashed          through an oil-immersion objective (Nikon Plan Fluor 100×, NA 1.49).
lines) as a function of areal density nNV   3D
                                               w, which we compare against       The NV fluorescence was separated from the green 532 nm light by
the XY-8 data (Extended Data Fig. 1a, orange points). The estimated              using a dichroic filter and collected on a fibre-coupled single-photon
areal density is thus nNV 3D
                             w = 19 ± 2 ppm nm, corresponding to a density       counter. A magnetic field B was produced by using a combination of
nNV
  3D
     =  3.2 ± 0.3   ppm assuming   a layer with thickness of w = 6 nm.           three orthogonal electromagnetic coils and a permanent magnet, and
P1 density                                                                       aligned along one of the diamond crystal axes. The microwaves used
      We estimate the P1 density by using a similar procedure but with           to drive magnetic dipole transitions for both NV and P1 centres were
DEER data instead of XY-8 data. We first remove the contribution due             delivered via an Omega-shaped stripline with typical Rabi frequencies
to NV–NV interactions from the DEER signal by subtracting an inter-              of ∼2π × 10 MHz.
polation of the XY-8 data (Extended Data Fig. 1a) from the raw DEER              DROID and Hartmann–Hahn sequences
data. Then, we compare the measured early-time dynamics with numer-                   Here, we describe the pulse sequences used to perform the
ically computed curves for a range of P1 densities nP1    3D
                                                             /3 (Extended Data   measurements shown in Fig. 4. In Fig. 4a, we compare the coherence
Fig. 1b). Here, we include a factor of 1/3 in the P1 density because the         times across different dynamical decoupling sequences, demons­
microwave tone ωP1 addresses only one-third of the P1 spins (the ‘P1-1/3         trating that the longest coherence times are achieved when we
group’) in our DEER measurement, which are separated by ∼ 100 MHz                decouple both on-site disorder and dipolar NV–NV dynamics using a
from the four other groups due to the hyperfine interaction63,64. By             DROID sequence proposed by Choi et al.62. To achieve the best decou-
comparing the data and theory curves, we estimate an areal density               pling, we experimented with a few variations on the well-known
of nP1
     3D
        w = 85 ± 10 ppm nm ≈ 1.4(1) × 10−2 nm−2.                                 DROID-60 sequence51. These measurements are plotted in Extended
      At fixed areal density, the numerics indicate that the DEER                Data Fig. 3. The DROID-60 data exhibit a pronounced coherent
decoherence profile depends on the layer thickness (Extended Data                oscillation (purple points), which we attribute mainly to errors in
Fig. 1d). The same dependence is not present in the XY-8 dynamics due            composite pulses formed by sequential π/2 rotations along different
to the relatively small density of NV centres (Extended Data Fig. 1c).           axes. The data exhibiting the longest coherence time (red points) are
Although this method does not yield nanometre resolution, our obser-             obtained using so-called sequence H (fig. 9 of ref. 62). We hypothesize
vations are inconsistent with a layer with w > 6 nm, placing a more              that sequence H behaves more predictably precisely because it elimi-
stringent bound on the thickness of the layer. The areal density                 nates composite pulses.
nP1
  3D
     w = 85 ± 10 ppm nmcorresponds to nP1    3D
                                                = 14 ± 2 ppm, assuming a layer        In Fig. 4b,c, we demonstrate polarization transfer between NV and
with thickness of w = 6 nm.                                                      P1 spins using a Hartmann–Hahn sequence. Following an initial π/2
      Other spin 1/2 paramagnetic defects in diamond65 may have the              pulse, the NV centres are spin-locked with Rabi frequency ΩNV, while
same resonant frequency as the P1-1/3 group, causing a possible syste­           the P1 centres are simultaneously driven with Rabi frequency ΩP1, for
matic error in our method for estimating the P1 density. To determine            a duration ts. A final π/2 pulse is applied before detection. When the
whether such defects are present in sample S1, we measured the P1                two Rabi frequencies are equal, that is, ΩNV = ΩP1, the spins are resonant
spectrum and compared the relative integrated areas under the peaks              in the rotating frame, and spin-exchange interactions enhance the
for the P1-1/3, 1/4 and 1/12 groups, thus obtaining an estimate of the           depolarization rate. The resonant depolarization data (Fig. 4b, green
relative densities between P1 groups. As shown in Extended Data Fig. 2,          curve) are well fitted by the functional form
the results agree with the expected ratios 1:0.75:0.25 and are consistent                                                       D/2α
with a negligible contribution of non-P1 defects to the DEER signal.                                       C(t) = e−t/T1ρ e−(t/τ)      ,               (6)


Nature Physics
Article                                                                                                 https://doi.org/10.1038/s41567-023-01944-5

where the first factor captures phonon-limited exponential decay and          is made noisier, for example, by reversibly worsening the quality of the
the second factor captures the independent depolarization channel             diamond surface (Extended Data Fig. 4b, green points). A subsequent
driven by spin-exchange interactions, with stretch power β = 1/3 (ref. 47).   three-acid clean restores the original β = 2/3 stretch power (Extended
We determine T1ρ = 1.05(3) ms from the NV spin-locking measurement            Data Fig. 4a, red points).
(Fig. 4b, orange curve).
                                                                              Data analysis and fitting
Experimental details for sample S2. Sample S2 was mounted in a                Normalization of decoherence data. The coherence of the NV spins
confocal microscope. For optical initialization and readout, about            is read out via the population imbalance between {|0⟩ , |−1⟩} states. The
350 μW of 532 nm light was directed through an air objective (Olympus         maximum measured contrast ≲8% is proportional (not equal) to the
UPLSA 40×, NA 0.95). The NV fluorescence was similarly separated              normalized coherence C(t). To see a physically meaningful stretch power
from the 532 nm light by using a dichroic mirror and directed onto a          in our log–log plots of the data (Figs. 2 and 3), it is necessary to normalize
fibre-coupled avalanche photodiode. A permanent magnet produced a             the data by an appropriate value that captures our best approximation
field of about 320 G at the location of the sample. The field was aligned     of the t = 0 time point for the DEER and spin echo measurements.
along one of the NV axes, and alignment was demonstrated by maxi-             Samples S1, S3 and S4: t = 0 measurement
mizing the 15N nuclear polarization66. Microwaves were delivered with              For a given pulse sequence (for example, Ramsey or spin echo)
a free-space rf antenna positioned over the sample.                           and fixed measurement duration t, we perform a differential readout
                                                                              of the populations in the |0⟩ and |−1⟩ spin states of the NV, which miti-
Experimental details for samples S3 and S4. Samples S3 and S4                 gates the effect of NV and P1 charge dynamics induced by the laser
were mounted in a confocal microscope. For optical initialization             initialization and readout pulses. As depicted schematically in
and readout, about 3 mW of 532 nm light was directed through an               Extended Data Fig. 5, we allow the NV charge dynamics to reach steady
air objective (Olympus LUCPLFLN, NA 0.6). The NV fluorescence was             state (I) before applying an optical pumping pulse (II). Subsequently,
separated from the 532 nm light by using a dichroic mirror and directed       we apply microwave pulses to both the NV and P1 spins (for example
onto a fibre-coupled photodiode (Thorlabs). The magnetic field was            Ramsey or spin echo pulse sequences as shown in Figs. 2 and 3) (III).
produced with an electromagnet with field strength of ∼174 G (∼275 G)         Finally, we detect the NV fluorescence (IV) to measure the NV popula-
for sample S3 (S4). The field was aligned along one of the NV axes, and       tion in |0⟩, obtaining a signal S0. We repeat the same sequence a second
microwaves were delivered using an Omega-shaped stripline with                time, with one additional π pulse before detection to measure the
typical Rabi frequencies of ∼2π × 10 MHz.                                     NV population in |−1⟩, obtaining a signal S−1. The raw contrast, Craw, at
                                                                              time t is then computed as Craw(t) ≡ [S0(t) − S−1(t)]/S0(t), and is typically
Polychromatic drive. The polychromatic drive was generated by phase           ≲8%. We normalize the raw contrast to the t = 0 measurement to obtain
modulating the resonant P1 microwave tone67. A random array of phase          the normalized coherence, C(t), defined above as
jumps Δθ was pre-generated and loaded onto an arbitrary waveform
                                                                                                        C(t) = Craw (t)/Craw (t = 0).                   (7)
generator controlling the IQ modulation ports of a signal generator.
The linewidth of the drive δω was controlled by fixing the s.d. of the
phase jumps σ = √δωδt in the pre-generated array, where 1/δt = 1              Sample S2: t = 0 measurement
gigasample per second was the sampling rate of the arbitrary wave­form            For sample S2, we have an early-time, rather than a t = 0, measure-
generator. The power in the drive was calibrated by measuring                 ment at t = 320 ns for spin echo and DEER sequences. Because the DEER
Rabi oscillations of the P1 centres without modulating the phase, that        signal decays on a much faster timescale than the spin echo signal, we
is, by setting δω = 0.                                                        normalize both datasets to the earliest-time spin echo measurement.

Spin echo for samples S1 and S2 without polychromatic                         Data analysis for Fig. 3. We separate our discussion of the data analysis
driving                                                                       relevant to Fig. 3 into two parts. First, we discuss how comparing the
In Section Characterizing microscopic spin-flip dynamics, we dis-             D = 2 and D = 3 best fits to the DEER measurements enables us to identify
cussed spin echo measurements limited by NV–P1 interactions (as one           the dimensionality of the underlying spin system. Second, armed with
would naively expect) and which exhibit an early-time stretch power of        the fitted dimensionality, we fit spin echo and DEER measurements
β = 3D/2α = 3/2. These measurements were performed on samples S3              simultaneously to equation (5) to extract the correlation time τc of
and S4 that exhibit a P1-to-NV density ratio of ∼200. By contrast, spin       the P1 system. We note that, except for the t = 0 normalization point
echo measurements on samples S1 and S2, with P1-to-NV density ratios          (Section Normalization of decoherence data in the Methods), we only
of ∼ 10 and ∼ 40, respectively, exhibit an early-time stretch of β = D/α      consider data at times t > 0.5 μs, to mitigate any effects of early-time
(Extended Data Fig. 4), consistent with the prediction for a Ramsey           coherent oscillations caused by the hyperfine coupling between the
measurement (Table 1). Here, we are discussing a ‘canonical’ spin echo        NV and its host nitrogen nuclear spin.
measurement with no polychromatic drive (Fig. 2b, inset), and thus            Determining the dimensionality of the system
these data are not in contradiction with those presented in Fig. 3.                To determine the dimensionality of the different samples S1
     A possible explanation for the observed early-time stretch               and S2, we focus on the DEER signal, where the stretch power is given
β = D/α is that the spin echo signal is limited by NV–NV interactions         by β = D/α in the early-time ballistic regime and β = D/2α in the late-time
rather than by NV–P1 interactions. To understand this limitation, it          random-walk regime. Employing both Gaussian and Markovian
is important to realize that the measured spin echo signal actually           assumptions, a closed form for the decoherence can be obtained as
contains at least two contributions: (1) the expected spin echo signal                                                                  D/2α
                                                                                                                          DEER
from NV–P1 interactions, arising because the intermediate π                                              CDEER (t) = e−A[χ       (t)]
                                                                                                                                               ,        (8)
pulse decouples the NVs from any quasi-static P1 contribution and
(2) a Ramsey signal from NV interactions with other NVs, arising              where χDEER is defined in equation (5) (Supplementary Information).
because these NVs are flipped together by the π pulse, and the intra-              Armed with equation (8), we consider the decoherence dynamics
group Ising interactions are not decoupled.                                   for different powers of the polychromatic drive for both D = 2 and D = 3
     Our hypothesis that NV–NV interactions limit the spin echo               (with α = 3, as per the dipolar interaction). We compare the reduced χ2fit
coherence in sample S1 is supported by the fact that a stretch power of       goodness-of-fit parameters for the two values of D, and demonstrate
β = 3D/2α = 1 can in fact be observed in spin echo data if the environment    that the stretch power analysis above indeed agrees with the


Nature Physics
Article                                                                                                   https://doi.org/10.1038/s41567-023-01944-5

dimensionality that best explains the observed DEER data. Changing              62. Choi, J. et al. Robust dynamic Hamiltonian engineering of
the dimension D does not change the number of degrees of freedom                    many-body spin systems. Phys. Rev. X 10, 031002 (2020).
in the fit, so a direct comparison of χ2fit is meaningful. Our results are      63. Zu, C. et al. Emergent hydrodynamics in a strongly interacting
summarized in Extended Data Fig. 6, where we observe that for sample                dipolar spin ensemble. Nature 597, 45–50 (2021).
S1 indeed the D = 2 fitting leads to a smaller χ2fit, while for sample S2 the   64. Hall, L. T. et al. Detection of nanoscale electron spin resonance
data are best captured by D = 3 (Extended Data Fig. 6). Independently               spectra demonstrated using nitrogen-vacancy centre probes in
fitting both the extracted signal C(t) as well to its negative logarithm            diamond. Nat. Commun. 7, 10211 (2016).
− log C(t) yields the same conclusions. This analysis complements the           65. Grinolds, M. et al. Subnanometre resolution in three-dimensional
discussion above in terms of the early-time and late-time stretch power             magnetic resonance imaging of individual dark spins.
of the decay.                                                                       Nat. Nanotechnol. 9, 279–284 (2014).
Extracting the correlation time τc                                              66. Jacques, V. et al. Dynamic polarization of single nuclear spins by
      Having determined the dimensionality of samples S1 and S2, we                 optical pumping of nitrogen-vacancy color centers in diamond at
now turn to characterizing the correlation times of the P1 spin systems             room temperature. Phys. Rev. Lett. 102, 057403 (2009).
in these samples. To robustly extract τc, we perform a simultaneous fit         67. Joos, M., Bluvstein, D., Lyu, Y., Weld, D. M. & Jayich, A. B.
to both the DEER signal with equation (8) and the spin echo signal with             Protecting qubit coherence by spectrally engineered driving of
                                                D/2α
                                                                                    the spin environment. npj Quantum Inf. 8, 47 (2022).
                                           SE
                            CSE (t) = e−A[χ (t)]       ,                 (9)
                                                                                Acknowledgements
assuming a single amplitude A and correlation time τc for both nor-             We gratefully acknowledge the insights of and discussions with M.
malized signals. Here, χDEER/SE depends on τc as defined in equation (5).       Aidelsburger, D. Awschalom, B. Dwyer, C. Laumann, J. Moore, E. Urbach
     To carefully evaluate the uncertainty in the extracted correlation         and H. Zhou. This work was support by the Center for Novel Pathways
time, we take particular care to propagate the uncertainty in the t = 0         to Quantum Coherence in Materials, an Energy Frontier Research
data used to normalize the raw contrast, that is, Craw(t = 0) (Section          Center funded by the U.S. Department of Energy, Office of Science,
Normalization of decoherence data in the Methods). Owing to the two             Basic Energy Sciences (materials growth, sample characterization
normalization methods for samples S1 and S2 (Section Normalization              and noise spectroscopy), the US Department of Energy (BES grant
of decoherence data in the Methods), we estimate the uncertainty in             no. DE-SC0019241) for driving studies and the Army Research
two different ways:                                                             Office through the MURI programme (grant no. W911NF-20-1-0136)
•   For samples S1, S3 and S4, we consider fluctuations of the nor-             for theoretical studies, the W. M. Keck foundation, the David and
    malization value, Craw(t = 0), by ±10%. This is meant to account            Lucile Packard Foundation and the A. P. Sloan Foundation. E.J.D.
    for a possible effect of the hyperfine interaction in this data             acknowledges support from the Miller Institute for Basic Research in
    point, as well as any additional systematic error.                          Science. S.A.M. acknowledges the support of the Natural Sciences and
•   For sample S2, we first compute a linear interpolation of the               Engineering Research Council of Canada (NSERC) (funding reference
    early-time spin echo decoherence to t = 0. We then sample the               no. AID 516704-2018) and the NSF Quantum Foundry through
    normalization uniformly between this extrapolated value and                 Q-AMASE-i programme award DMR-1906325. D.B. acknowledges
    the earliest spin echo value.                                               support from the NSF Graduate Research Fellowship Programme
                                                                                (grant DGE1745303) and The Fannie and John Hertz Foundation.
     By sampling over the possible values of Craw(t = 0), we build a
distribution over the extracted values of τc fitting to both the coher-         Author contributions
ence, C(t), and its logarithm, − log C(t). The reported values in Fig. 3d,e     E.J.D., W.W., T.M, W.S., M.J., Y.L., Z.W. and C.Z. performed the
correspond to the mean and s.d. evaluated over this distribution.               experiments. B.Y., F.M., B.K., D.B. and S.C. developed the theoretical
     We end this section by commenting that, as the drive strength is           models and methodology. E.J.D., F.M. and W.W. performed the
reduced, the spin echo signal looks increasingly similar to the undriven        data analysis. S.M. and A.B.J. prepared and provided the diamond
spin echo data (Extended Data Fig. 4), that is, the early-time stretch          substrates. A.B.J and N.Y.Y. supervised the project. E.J.D, B.Y., F.M., C.Z.
changes from β = 3D/2α to β = D/α. Our explanation for this observed            and N.Y.Y wrote the manuscript, with input from all authors.
stretch is given in Section Spin echo for samples S1 and S2 without poly-
chromatic driving in the Methods. The deviation from the expected               Competing interests
functional form for the decoherence leads to a large uncertainty in the         The authors declare no competing interests.
extracted correlation time. The data also deviate from the model for larger
drive strengths, for example, Ω = 2π × 4.05 MHz, δω = 2π × 20 MHz, where        Additional information
our assumption that δω ≫ Ω is no longer valid (Extended Data Fig. 7).           Extended data is available for this paper at
                                                                                https://doi.org/10.1038/s41567-023-01944-5.
Data availability
Data supporting the findings of this paper are available from the cor-          Supplementary information The online version contains supplementary
responding authors upon request. Source data are provided with                  material available at https://doi.org/10.1038/s41567-023-01944-5.
this paper. Source data for Figs. 1–4 and Extended Data Figs. 1–7 are
provided with this paper.                                                       Correspondence and requests for materials should be addressed to
                                                                                A. C. Bleszynski Jayich or N. Y. Yao.
Code availability
Code developed for the data analysis and visualization is available from        Peer review information Nature Physics thanks Nir Bar-Gill and the
the corresponding author upon request.                                          other, anonymous, reviewer(s) for their contribution to the peer review
                                                                                of this work
References
61. Syntek. Products 1: various industrial diamonds. Syntek                     Reprints and permissions information is available at
    http://www.syntek.co.jp/en/products/ (2023).                                www.nature.com/reprints.



Nature Physics
Article                                                                                                             https://doi.org/10.1038/s41567-023-01944-5




Extended Data Fig. 1 | Defect densities. (a-b) NV and P1 areal densities.               late times (grey shaded regions), the noise dynamics approach an incoherent
Computed dynamics (dashed lines) for early-time Ramsey decoherence caused               random walk and should not be used to compute the density within this analysis,
by NV-NV interactions (a) and NV-P1 interactions (b), as a function of the NV areal     because the numerics do not include flip-flop interactions. (c-d) Effect of
density nNV
         3D
            w and the P1 areal density nP1
                                        3D
                                           w, respectively. We compare these            finite-thickness layer. At fixed areal density 19ppm ⋅ nm, choosing different layer
numerical results against the measured decoherence dynamics obtained via the            widths w does not affect the computed dynamics (dashed curves, c). For higher
XY-8 sequence (orange points, a) and the DEER sequence [after removing the NV           density P1 centers nP13D
                                                                                                                 = 85 ppm ⋅ nm, the finite thickness of the layer can induce
contribution via the red interpolation in (a)] (purple points, b) to obtain the areal   a sizable effect on the DEER decoherence dynamics (purple points, d) at early
density of defects in sample S1. We estimate the areal density of NV centers to be      times. Numerical calculations are plotted as dotted lines.
nNV
 3D
    w = 19 ± 2 ppm ⋅ nm and the P1 density to be nP13D
                                                       w = 85 ± 10 ppm ⋅ nm. At




Nature Physics
Article                                                                                                           https://doi.org/10.1038/s41567-023-01944-5




Extended Data Fig. 2 | Relative density extraction for three of the five different P1 groups. The P1 spectrum is fit to a sum of three Lorentzian curves (dashed line).
The relative areas of the three dips are 1 : 0.74 : 0.26, which is consistent with the expected ratio 1 : 0.75 : 0.25.




Nature Physics
Article                                                                                                          https://doi.org/10.1038/s41567-023-01944-5




Extended Data Fig. 3 | The measured decoherence profiles of variations on           sequences that do not require composite pulses, see for example Seqs. A, H, G in
DROID-60. Due to imperfections in our composite microwave pulses, pulse error       Fig. 9 of ref. 62. The data exhibiting the longest coherence time (Seq. H, τp = 100ns,
accumulates coherently in the DROID-60 (ref. 62) sequence and a pronounced          red points) are also shown in Fig. 4(a) of the main text.
oscillation is observed (purple points). To avoid such oscillations, we implement




Nature Physics
Article                                                                                                             https://doi.org/10.1038/s41567-023-01944-5




Extended Data Fig. 4 | Undriven DEER and spin echo data. (a) In sample S1, with        unchanged. (c) As in panel (a), the spin echo data (teal) for sample S2, presumably
a clean surface, both the DEER (blue) and spin echo (red) data exhibit a stretch       limited by NV-NV interactions rather than the bath, exhibit the same stretch
power β = 2/3. (b) After worsening the surface quality, the spin bath becomes          power β = 1 as the DEER data. The DEER data in (a, c) are also plotted in Fig. 2(a) of
noisier and we observe the expected β = 1 stretch power in the echo data (green);      the main text.
in the DEER data (purple) the correlation time τc increases but the stretch power is




Nature Physics
Article                                                                                                     https://doi.org/10.1038/s41567-023-01944-5




Extended Data Fig. 5 | Experiment sequence schematic for differential           The differential measurement subtracts the fluorescence obtained from two
measurement. The pulses for the laser (green), photodetector readout (blue),    sequences (before and after the dotted vertical line), which are identical except
and microwaves addressing the NV (orange) and P1 (red) transitions are shown.   for an additional π-pulse on the NV spins.




Nature Physics
Article                                                                                                         https://doi.org/10.1038/s41567-023-01944-5




                                  2                                                                                                           2
Extended Data Fig. 6 | Reduced χfit for fits to the DEER measurements on samples S1 (a) and S2 (b) for four different fit models. Reduced χfit for fits to the DEER
measurements on samples S1 (a) and S2 (b) for four different fit models.




Nature Physics
Article                                                                                                    https://doi.org/10.1038/s41567-023-01944-5




Extended Data Fig. 7 | DEER and spin echo for sample S1 (a) and sample S2       obtained for sample S2 plotted in (b) does not exhibit the correct “random-walk”
(b), under a fast incoherent drive. DEER and spin echo for sample S1 (a) and    regime stretch power of 1/2, even though the DEER and spin echo signals overlap
sample S2 (b), under a fast incoherent drive. The Rabi frequencies for panels   at all measured times.
(a) and (b) are Ω = 2π × 3.45MHz and Ω = 2π × 4.05MHz, respectively. The data




Nature Physics
