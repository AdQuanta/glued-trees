# Quantum many-body theory for electron spin decoherence in nanoscale nuclear spin baths - Full Text

> Source: https://iopscience.iop.org/article/10.1088/0034-4885/80/1/016001
> Collected: 2026-09-20
> Published: 2017-01-01
> Zotero parent key: I7CQ4U3S
> Evidence: Zotero indexed PDF text

REVIEW
Quantum many-body theory for electron spin decoherence in nanoscale nuclear spin baths
To cite this article: Wen Yang etal 2017 Rep.Prog.Phys. 80 016001
View the article online for updates and enhancements.
You may also like
One decade of quantum optimal control in the chopped random basis Matthias M Müller, Ressa S Said, Fedor Jelezko et al.

Quantum systems in silicon carbide for sensing applications S Castelletto, C T-K Lew, Wu-Xi Lin et al.

Quantum discord and its allies: a review of recent progress Anindita Bera, Tamoghna Das, Debasis Sadhukhan et al.

This content was downloaded from IP address 132.68.239.10 on 30/08/2024 at 11:04


 1 © 2016 IOP Publishing Ltd Printed in the UK
Reports on Progress in Physics
Wen Yang1, Wen-Long Ma2,3 and Ren-Bao Liu2,3,4
1 Beijing Computational Science Research Center, Beijing 100193, People’s Republic of China
2 Department of Physics, The Chinese University of Hong Kong, Shatin, N. T., Hong Kong, People’s Republic of China 3 Centre for Quantum Coherence, The Chinese University of Hong Kong, Shatin, N. T., Hong Kong, People’s Republic of China
4 Institute of Theoretical Physics, The Chinese University of Hong Kong, Shatin, N. T., Hong Kong, People’s Republic of China
E-mail: rbliu@phy.cuhk.edu.hk
Received 9 March 2016, revised 13 July 2016 Accepted for publication 11 August 2016 Published 4 November 2016
Corresponding Editor Jian-Wei Pan
Abstract
Decoherence of electron spins in nanoscale systems is important to quantum technologies such as quantum information processing and magnetometry. It is also an ideal model problem for studying the crossover between quantum and classical phenomena. At low temperatures or in light-element materials where the spin–orbit coupling is weak, the phonon scattering in nanostructures is less important and the fluctuations of nuclear spins become the dominant decoherence mechanism for electron spins. Since the 1950s, semi-classical noise theories have been developed for understanding electron spin decoherence. In spin-based solid-state quantum technologies, the relevant systems are in the nanometer scale and nuclear spin baths are quantum objects which require a quantum description. Recently, quantum pictures have been established to understand the decoherence and quantum many-body theories have been developed to quantitatively describe this phenomenon. Anomalous quantum effects have been predicted and some have been experimentally confirmed. A systematically truncated clustercorrelation expansion theory has been developed to account for the many-body correlations in nanoscale nuclear spin baths that are built up during electron spin decoherence. The theory has successfully predicted and explained a number of experimental results in a wide range of physical systems. In this review, we will cover this recent progress. The limitations of the present quantum many-body theories and possible directions for future development will also be discussed.
Keywords: electron spin decoherence, nuclear spin baths, quantum many-body theory, quantum dots, donors, nitrogen-vacancy centers
(Some figures may appear in colour only in the online journal)
Quantum many-body theory for electron
spin decoherence in nanoscale nuclear
spin baths
Review
0034-4885/17/016001+42$33.00
doi:10.1088/0034-4885/80/1/016001
Rep. Prog. Phys. 80 (2017) 016001 (42pp)


 Review
2
1. Introduction
A quantum object can be in a superposition of states. An isolated quantum object can be in a pure state with full quantum coherence, a state in which each component of the superposition has a deterministic coefficient up to a global phase factor. Quantum coherence gives rise to a series of non-classical phenomena such as interference and entanglement. It is also the basis of quantum technologies [1–3], such as quantum cryptography [4, 5], quantum-enhanced imaging and sensing [6–8], and quantum computers [9, 10]. Realistic quantum systems are always coupled to environments; thus the quantum coherence is destroyed by the environmental noise [11–13]. On the one hand, such decoherence processes prevent quantum interference, restore classical behaviors, and pose a critical challenge to quantum technologies. On the other hand, decoherence could be utilized to reveal information about the environments. This prospect has been pursued for a long time in magnetic resonance spectroscopy [14], where the decoherence of a large number of electronic or nuclear spins are used to reveal the interactions and motions of atoms in bulk materials. In recent years, the progress in active control and measurement of single spins have allowed single spins to be used as ultrasensitive quantum sensors to reveal the structures and dynamics of the environments with nanoscale resolution [15–17] (see [18] for a review). Additionally, a great diversity of physical systems have been proposed for spin-based quantum technologies and quantum sensing. In particular, the spins of individual electrons and atomic nuclei offer a promising combination of environmental isolation and controllability; thus they can serve as the basic units of quantum machines: the qubits. Electronic and nuclear spins in semiconductors have distinct technical advantages such as scalability and compatability with modern semiconductor technology [19], tunable spin properties by energy-band and wavefunction engineering, and the ability to manipulate the spins by using the well-established electron spin resonance and nuclear magnetic resonance techniques as well as optical and electrical approaches [20]. Here, we concentrate on semiconductor quantum dots (QDs) [21] and impurity/defect centers such as phosphorus and bismuth donors in silicon [22] and nitrogenvacancy centers in diamond [23]. In these nanoscale systems, a few electronic or nuclear spins (referred to as central spins for clarity) can be addressed, so they are used as qubits, while the many unresolved nuclear spins form a magnetic environment that causes decoherence of the central spins. In addition, the central spins are directly coupled to nearby electronic spins from impurities and defects and are also influenced by charge and voltage fluctuations (e.g. from lattice vibration and nearby electron/hole gases and trapped charges) via spin–orbit coupling. However, these environmental noises can be suppressed, e.g. by careful material and device engineering to remove parasitic charge and spin defects, lowering the temperature to suppress phonon scattering, or using light-element materials to suppress the spin–orbit coupling. Therefore, the most relevant noise sources for the central spins in quantum technologies are the nuclear spins.
Since the 1950s, the semi-classical picture of spectral diffusion has been adopted to study central spin decoherence in spin baths [24–26]. The semi-classical theory treats the spin bath as a source of classical magnetic noise. In modern quantum nanodevices, the wave function of the central spin is localized, so the nuclear spins coupled to the central spin form a nanoscale spin bath. The central spin and the nanoscale spin bath form a closed system in the time scale of interest (see figure 1) and the quantum nature of the spin bath becomes important. In recent years, quantum pictures have been established to understand central spin decoherence. Through the quantum theory, anomalous quantum effects have been predicted, some of which have been experimentally confirmed. To quantitatively describe central spin decoherence, a variety of quantum many-body theories have been developed, including the paircorrelation approximation [27–29], cluster expansion [30, 31], linked-cluster expansion [32], cluster-correlation expansion (CCE) [33, 34], disjoint cluster approximation [35, 36], and ring diagram approximation [37, 38]. In particular, the CCE theory [33, 34] provides a systematic account of the manybody correlations in nanoscale spin baths that lead to central spin decoherence. The CCE method has successfully predicted and explained a number of experimental results in a wide range of solid state systems. Here, we will provide a pedagogical review of the basic concepts of coherence and decoherence, the recent quantum many-body theories, their relationships, limitations, and possible directions for future development. The organization of this review is as follows. In the first three sections, we introduce the basic concepts (section 2), decoherence theory (section 3) and coherence protection (section 4) based on the semi-classical noise model. Then, we introduce, in section 5, the concept of quantum noise and, in
Figure 1. A central spin and nanoscale spin bath evolve as a closed system in the relevant timescales. The thermal distribution of the spin bath causes a static thermal noise, and the quantum evolution of the spin bath induces a dynamical quantum noise. The rest of universe indicates the larger environment beyond the spin bath, which induces classical noises (static or dynamical).
Rep. Prog. Phys. 80 (2017) 016001


 Review
3
section 6, a full quantum picture of central spin decoherence. In section 7, we introduce the coupling of the central spin to the phonon and nuclear spin baths and experimental measurements in paradigmatic solid-state physical systems that identify the nuclear spin bath as the most relevant decohering environment. Next we review the microscopic quantum many-body theories for central spin decoherence in nuclear spin baths (section 8) and discuss a series of quantum decoherence effects (section 9). Finally, the possible directions for future development are discussed in section 10. For convenience, we take  =1 throughout this review.
2. Basic concepts of spin decoherence
In this section, we introduce the basic concepts for the environmental noise-induced decoherence of a central spin1/2, including quantum coherence and decoherence, density matrix and ensembles, classification of central spin decoherence and their geometric representation with Bloch vectors, and description of central spin decoherence caused by the simplest environmental noises: rapidly fluctuating noise and static noise. Under an external magnetic field, the central spin is quantized along that magnetic field (defined as the z axis) and its evolution is governed by the Zeeman Hamiltonian
ˆˆ
H =ωS,
0 0 z (1)
with two energy eigenstates| ↑ ⟩ (spin up) and| ↓ ⟩ (spin down). A general pure superposition state of a spin-1/2 can be parametrized by two real numbers θ and φ as
θ φ⟩ θ ⟩ θ ⟩
| ≡ | ↑ + φ| ↓
, cos 2 sin 2 e .
i (2)
Quantum coherence is fully preserved when the central spin is isolated from the environment and undergoes unitary evolution according to its own, deterministic Hamiltonian. For example, the Zeeman Hamiltonian in equation (1) leads to
the coherent evolution |θ φ |θ φ = |θ φ + ω
, e− , , t
iH t 0
0
〉→ 〉 〉
ˆ.
The couplings of the central spin to the environment amounts to measurement of the central spin by the environment (with the results unknown to any observers though). As a result, the central spin undergoes random collapses from a fully coherent pure state into an incoherent mixture (i.e. a statistical ensemble) of distinct pure states, i.e. quantum coherence breaking or decoherence in short.
2.1. Temporal ensembles and spatial ensembles
A quantum system in a pure state|ψ⟩is described by the density operator ρˆ =|ψ⟩⟨ψ|, while a quantum system that is found in the kth distinct pure state |ψk⟩ with probability pk (k = 1, 2, ) is described by the density operator ρˆ = ∑k pk |ψk⟩⟨ψk|. In the energy eigenstates | ↑ ⟩ and | ↓ ⟩ of the central spin, the density operator becomes a 2 × 2 density matrix as
ˆ⎡
⎣⎢ ⎤
⎦⎥
ρ ρρ
ρρ
= ↑↑ ↑↓
↓↑ ↓↓ ,
where the diagonal matrix elements ρ↑↑ and ρ↓↓ describe the population of each energy eigenstate, and the off-diagonal elements ρ↓↑ = ρ↑↓
∗ describe the phase correlation between different energy eigenstates. The density matrix ρˆ(t) describes the statistics of many identical measurements over an ensemble of central spins. In recent years, single-shot measurement of a single central spin has been demonstrated in various solid-state systems [39–48]. For such single-spin measurements, one still needs to repeat the measurement cycle (i.e. initialization-evolution-measurement) many times to retrieve the correct probabilities of different measurement outcomes. In this case, each cycle corresponds to a sample of the temporal ensemble. According to the characteristic timescale of the noise fluctuation (see section 3.1.2 for more details), the environmental noises fall into two categories: dynamical quantum noises that change randomly during the evolution of each sample and static thermal noises that remain invariant for each sample, but change randomly from sample to sample (see section 5 for discussions about the difference between dynamical quantum noises and static thermal noises). Note that ‘noises’ that remain invariant during all repeated measurements just renormalize the external field and do not cause decoherence, e.g. decoherence is suppressed under fast measurements [41, 48, 49]. In traditional spin resonance measurements, a large number of spatially separated central spins are simultaneously prepared, evolved, and measured. In this case, each central spin is a sample of the spatial ensemble. Since spatially separated spins may be subjected to different static macroscopic conditions (e.g. due to inhomogeneous magnetic fields, g-factors, and strains), this introduces additional static noises that could qualitatively change the central spin dephasing [50]. Nevertheless, since static noises are just static inhomogeneities of the environments for different samples, they can be eliminated by techniques that remove these inhomogeneities, such as spin echo [51, 52]. It is also possible to employ environmental engineering to suppress quasi-static noises. For example, to combat electron spin decoherence in nuclear spin baths, a widely pursued approach is to narrow the distribution of the quasi-static noise by polarizing the bath [53–55], quantum measurements of the bath [48, 56–59], and nonlinear feedback between the electron spins and the nuclear spin baths [60–65] (see [66] for the theories about the nonlinear feedback). Thus, the dynamical quantum noises are the most relevant mechanism of central spin dephasing. Single-spin and many-spin measurements would give similar statistics if the dynamical quantum noises do not vary appreciably for spatially separated spins.
2.2. Classification of decoherence processes
The state of the central spin can be visualized by the Bloch vector defined as 2〈 ˆS(t)〉 ≡ 2 Tr[ ˆSρˆ(t)]through the decomposition
ρˆ(t) = Iˆ + ⟨ ˆS(t)⟩ ⋅ σˆ
2,
where Iˆ is the identity matrix and σˆ = (σˆ , σˆ , σˆ )
x y z T are Pauli matrices along the x/y/z directions. The Bloch vector of the general pure state |θ, φ⟩ in equation (2) is a unit vector with polar angle θ and azimuth angle φ (figure 2(a)). The unitary
Rep. Prog. Phys. 80 (2017) 016001


 Review
4
evolution transforms a pure state into another pure state with the length of the Bloch vector preserved. For example, the coherent evolution |θ, φ⟩ → |θ, φ + ω0t⟩ governed by the Zeeman Hamiltonian in equation (1) is mapped to the Larmor precession of the Bloch vector around the magnetic field (z axis) (figure 2(b)): ⟨ ̇S(t)⟩ = ω e × ⟨ ˆS(t)⟩
0 z or equivalently
⟨S ̇ (t)⟩ = 0
z and ⟨ ( )⟩ = − ω ⟨ ˆ ( )⟩
−−
St St
 ̇ i 0 , where ≡ ±
S± S iS
x y.
By contrast, spin decoherence transforms, via non-unitary evolution, a pure state into a mixed state, described by a Bloch vector with shrinking length. The environmental noise induces two kinds of changes to the central spin state:
1. Spin relaxation (also called longitudinal relaxation or T1 process in literature), which refers to the change of the diagonal populations ρ↑↑(t) and ρ↓↓(t) or equivalently the longitudinal component of the Bloch vector
⟨ ˆ ( )⟩ = ρ ( ) − ρ ( )
↑↑ ↓↓
2 Sz t t t , as shown in figure 3(a). 2. Spin dephasing (also called transverse relaxation or the T2 process in literature), which refers to the decay of the off-diagonal coherence
() ()
()
⟨ ˆ ( )⟩ ⟨ ˆ ( )⟩
ρ
ρ
≡=
↑↓
↑↓
−
−
Lt t S t
S
0 0 (3)
or equivalently the transverse components 〈Sˆx(t)〉 =
Reρ↑↓(t) and ⟨ ˆ ( )⟩ = − ρ↑↓( )
S t Im t
y of the Bloch vector, as shown in figure 3(b).
The spin relaxation (T1 process) is always accompanied by spin dephasing (T2 process), but there are two kinds of physical mechanisms that contribute to pure dephasing (i.e. without causing spin relaxation): (1) dynamical quantum noises lead to ‘true’ decoherence (Tφ process) [67]; (2) static thermal
noises lead to inhomogeneous dephasing (T∗2 process). For T1 and Tφ processes, to provide an intuitive physical picture, we only consider noises that fluctuate and hence lose memory much faster than central spin decoherence.
2.3. Spin relaxation (T1 process)
When the environmental noise induces the central spin-flip between | ↑ ⟩ and | ↓ ⟩, the central spin energy changes by an amount ω0, which is compensated by the environment to
ensure the conservation of energy. For noises that fluctuate rapidly and hence lose memory much faster than the central spin relaxes, the random central spin-flip is memoryless, i.e. the central spin state at time t completely determines its state at the next instant. If ρˆ(t) = |ψ〉〈ψ| is a pure superposition |ψ⟩ ≡ |ψ ⟩+|ψ ⟩
↑ ↓ of the spin-up component |ψ↑⟩ and spin-down component|ψ↓⟩ and the environment induces the random jump | ↑ ⟩ → | ↓ ⟩ at a constant rate γ (figure 3(a)), then during a small interval dt, the component |ψ↓⟩ remains intact, while |ψ↑⟩
has a probability γdt to incoherently jump to ˆ |ψ ⟩ = ˆ |ψ⟩
−↑ −
S S. Therefore, the central spin state at the next instant t + dt is given by the density matrix
ˆ( ) ˆ ˆ( ) ˆ ˆ ˆ( ) ˆ
††
ρ t + dt = M ρ t M + M ρ t M ,
1 10 0
which describes the incoherent mixture of the collapsed component γ ˆ |ψ⟩ ≡ ˆ |ψ⟩
dt S− M1 and the non-collapsed component
⟩ ⟩ ⟩ˆ⟩
( / ) ˆ† ˆ
|ψ + − γ |ψ ≈ |ψ ≡ |ψ
γ
↓ ↑ − −−
1 dt e M .
dt 2 S S 0
This evolution corresponds to a general binary-outcome weak measurement of the central spin by the environment (with the results unknown to any observers): depending on the two possible outcomes, the central spin collapses to Mˆ1|ψ⟩ or Mˆ 0|ψ⟩. The central spin evolution due to the random jump | ↑ ⟩ → | ↓ ⟩ is
[ ( )] → ˆ( ) ˆ( ) [ ˆ ] ˆ( )
⟩⟩
ρ ≡ ρ + −ρ =γ ρ
|↑ |↓ −
t tt t D
t St
 ̇d
d,
where [ ˆ] ˆ ˆ ˆ ˆ { ˆ ˆ ˆ}/
††
D L ρ ≡ LρL − L L, ρ 2 is the standard Lindblad form for dissipation. In general, an environment could not only induce | ↑ ⟩ → | ↓ ⟩ by absorbing an energy quantum ω0 from the central spin, but also induce the reverse process | ↓ ⟩ → | ↑ ⟩ by delivering an energy quantum ω0 to the central spin. When the environment is in thermal equilibrium with an inverse temperature β ≡ 1/(kBTenv), the latter process would be slower than the former process by a Boltzmann factor e−βω0, e.g. for T = 0
env , the environment is in its ground state and hence cannot deliver the energy quantum ω0, so the latter process is blocked. Including both processes, the environment-induced central spin evolution is described by
ργ ρ
ρ ρρ
ρ ρρ
=+ =
− −−
− −−
βω
−− +
↑↑ ↑↑ ↑↓
↓↑ ↓↓ ↓↓
[ ( )] (D[ ˆ ] D[ ˆ ]) ˆ( )
() ()
() ()
⎡
⎣
⎢⎢⎢⎢⎢
⎤
⎦
⎥⎥⎥⎥⎥
t S St
t
T
t
T t
T
t
T
 ̇e 2
2
,
T
eq
11
1
eq
1
10
(4)
Figure 2. A central spin quantized in a magnetic field along the z axis: (a) geometric representation of a general pure state as a Bloch vector, and (b) central spin evolution as the precession of the Bloch vector around the magnetic field.
Figure 3. Evolution of the Bloch vector under (a) spin relaxation and (b) spin dephasing.
Rep. Prog. Phys. 80 (2017) 016001


 Review
5
which is characterized by a single time constant ≡ [( + βω )γ]−
T 1e
11
0 (so-called spin relaxation time) and drives the central spin into thermal equilibrium with the environment:
ρ≡ = +
+
β
β
βω
βω
βω
−
−
⎡
⎣
⎢⎢⎢⎢
⎤
⎦
⎥⎥⎥⎥
e
Tre
1
1e 0
0e
1e
.
H
H
eq 0
0
0
0
0
ˆ
ˆ
ˆ
During the spin relaxation process, both the populations and the off-diagonal coherence of the central spin exponentially decay to their respective thermal equilibrium values, with the decay rate of the latter being only half that of the former.
2.4. ‘True’ decoherence by dynamical quantum noises (Tφ process)
During pure dephasing, the environmental noise induces random jumps of the relative phase between the energy eigenstates | ↑ ⟩ and | ↓ ⟩ of the central spin. For noises that lose memory much faster than the spin dephasing, the central spin evolution is memoryless. Again, we take ρˆ(t) =|ψ⟩⟨ψ| and assume that the environment induces the random phase jump |ψ⟩ → σˆz|ψ⟩ at a constant rate γφ. The central spin state at the next instant
t + dt is an incoherent mixture of γ σˆ |ψ⟩ ≡ ˆ |ψ⟩
φdt z Mc and
⟩ ⟩ˆ ⟩
( / ) ˆ†ˆ
− γ |ψ ≈ |ψ ≡ |ψ
φ − γφ σ σ
1 dt e M ,
dt 2 nc
zz
described by the density matrix ρ + = ρ +
ˆ( ) ˆ ˆ( ) ˆ †
t dt Mc t Mc
ρ
ˆ ˆ( ) ˆ †
M tM
nc nc. This incoherent collapse corresponds to a general binary-outcome weak measurement of the central spin by the environment (with the results unknown to any observers). The central spin evolution due to this process assumes the standard Lindblad form
ρ γ σρ
ρ
ρ
==
−
−
φ
φ
φ
↑↓
↓↑
φ
⎡
⎣
⎢⎢⎢⎢⎢
⎤
⎦
⎥⎥⎥⎥⎥
t Dt
t
T
t
T
 ̇
0
0
,
Tz
[ ( )] [ ˆ ] ˆ( )
()
( ) (5)
which is characterized by a single time constant φ ≡ γφ
T 1/(2 ) (so-called pure dephasing time). During ‘true’ decoherence, the longitudinal Bloch vector component remains invariant, while the magnitude of the transverse components decay exponentially on a timescale Tφ (figure 3(b)).
2.5. Inhomogeneous dephasing by static thermal noises (T∗2 process)
In the presence of static noises, the central spin evolution is governed by the Hamiltonian  ̃
ˆˆ ˆ
H ≡H +b⋅S
b 0 , where the local field  ̃b remains static for each sample of the ensemble, but fluctuates from sample to sample according to a certain probability distribution P (b)
inh . For a sample subjected to the local field b, the central spin undergoes unitary evolution
ˆ ( ) ˆ( )
ˆˆ
ρ =− ρ
t e 0e
Ht Ht b
ii
b b and its Bloch vector〈 ˆS(t)〉 ≡ Tr[ ˆSρˆ (t)]
bb
undergoes coherent precession ⟨ ̇S(t)⟩ = (ω e + b) × ⟨ ˆS(t)⟩
bb
0z
that preserves its length. The density matrix that describes the ensemble is
ˆ( ) ˆ ( ) ( )
∫
ρ t = ρ t P b db,
b inh (6)
and the Bloch vector is
⟨ ˆ ( )⟩ ⟨ ˆ ( )⟩ ( )
∫
S t = S t P b db.
b inh
In principle, the inhomogeneous distribution of the local field can result in both spin relaxation and spin dephasing. When the external field is much stronger than the noise field, the transverse noises  ̃  ̃
bx, by can barely tilt the precession axis away from the z axis. In this case, the longitudinal spin relaxation is suppressed by the large energy splitting ω0 between the spin-up | ↑ ⟩ and spin-down | ↓ ⟩ eigenstates,
and only pure dephasing by the longitudinal noise b ̃z occurs (see figure 4): the different precession frequencies of different samples lead to progressive spreading out of their azimuth angles φ (t) = (ω + b )t
j 0 j and hence decay of the transverse Bloch vector components ⟨ ˆ ( )⟩
S− t . The off-diagonal coherence (the intrinsic phase factor e−iω0t removed)
() ( )
∫
=−
L t e P b db
bt
inh i inh (7)
decays on a timescale T∗2 ∼ inverse of the characteristic width of the static noise distribution P (b)
inh . Such decay by classical ensemble averaging over static noises is called ‘inhomoge
neous dephasing’ (T∗2 process). For the commonly encountered Gaussian distribution
( ) /( )
π
=−
Pb b
1
2e ,
bb
inh rms
2 2 rms
2
(8)
the spin coherence shows the Gaussian decay:
( ) (/ )
=− ∗
Lt e ,
tT
inh 2 2 (9a)
T∗ = b
2.
2
rms
(9b)
As will be discussed in section 4, the T∗2 process can be completely removed by spin-echo techniques.
2.6. Summary
Including the unitary evolution under the external field (equation (1)) and a fixed local field b, as well as the T1 and Tφ processes caused by rapidly fluctuating noises that lose memory much faster than central spin decoherence (equations (4) and (5)), the
Figure 4. Geometric representation of inhomogeneous dephasing due to averaging over an ensemble of coherently precessing samples.
Rep. Prog. Phys. 80 (2017) 016001


 Review
6
density matrix of the central spin obeys the Lindblad master equation
ρρ
ρ ρρ
ρ ρρ
=− + −
−
−
↑↑ ↑↑ ↑↓
↓↑ ↓↓ ↓↓
⎡
⎣
⎢⎢⎢⎢⎢
⎤
⎦
⎥⎥⎥⎥⎥
t H bS t
t
T
t
T
t
T
t
T
 ̇i , ,
bb
bb
bb
0z
eq
12
2
eq
1
( ) [ ˆ ˆ ˆ ( )]
[ ˆ ( )] [ ˆ ( )]
[ ˆ ( )] [ ˆ ( )]
where ≡ [ /( ) + / φ]−
T 1 2T 1 T
2 1 1 (⩽ 2T1) is the spin dephasing time. In the presence of inhomogeneous dephasing, the density matrix ρˆ(t) is obtained by averaging ρˆb(t) over the distribution of b. Note that, although spin relaxation imposes an upper limit on the spin dephasing time via T ⩽ 2T
2 1, in typical cases of central spin decoherence T2 is much shorter than T1
and is limited by pure dephasing (Tφ and T∗2 processes).
3. Semi-classical noise theory for spin decoherence
A simple theoretical treatment of spin decoherence is to describe the environment as a source of classical magnetic noise  ̃b(t) with zero mean ⟨ ̃b(t)⟩ = 0, so the central spin Hamiltonian is
 ̃
ˆ( ) ˆ ( ) ˆ
H t = ω S + b t ⋅ S.
0 z (10)
The time-dependent transverse noises  ̃ ( ) ≡  ̃ ( ) ±  ̃ ( )
b± t b t ib t
xy
could randomly tilt the precession axis away from the z axis, flip the central spin between the unperturbed eigenstates | ↑ ⟩ and | ↓ ⟩, and hence induce spin relaxation. The longitudinal
noise b ̃z(t) randomly modulates the central spin precession frequency along the z axis and induces pure dephasing. Here, we consider a strong external magnetic field and hence a large unperturbed precession frequency ω0, so that the noise can be treated as a perturbation.
3.1. Basic concept of classical noise
We take a real, scalar noise b ̃(t) with zero mean ⟨b ̃(t)⟩ = 0 to explain some basic concepts of classical noises. A classical noise is specified by the probability distribution for each realization of the noise, e.g. the probability distribution P(b , b , )
0 1 for the noise b ̃ ≡ b ̃(t )
n n at all the time points t ≡ n∆t
n . Below, we introduce two important characteristics of noises: statistics and auto-correlations (or equivalently spectra). We will particularly focus on Gaussian noises, which are the simplest and also a commonly encountered type of noise statistics. Among various noise spectra, we highlight two simple cases, namely static noises and rapidly fluctuating noises which lose memory much faster than central spin decoherence.
3.1.1. Statistics. According to the form of P(b , b , )
0 1 , noises are often classified as Gaussian or non-Gaussian. Gaussian noises are one of the simplest and most widely encountered noises. For a Gaussian noise, the random variables b ̃ , b ̃ , 
01
obey the multivariate normal distribution
( ) (/) ( )
∝∑
−−
P b ,b , e ,
bC b 01
12 ij
i ij j
1
(11)
where C−1 is a positive-definite symmetric matrix. In the continuous form, the Gaussian distribution as a functional of the noise b ̃(t) has the form [ ( )] ( / ) ( ) ( ) ( )
∝ ∫∫
−−
P b t e 1 2 dt dt b t C t ,t b t
1 2 1 1 1 2 2,
where ( )
C− t , t
1 1 2 is a positive-definite symmetric matrix. As a key property, an arbitrary linear combination  ̃  ̃
φ≡∑ c b
n n n of
Gaussian random variables is still Gaussian, i.e. still obeys normal distribution. Averaging over Gaussian noises can be obtained explicitly, e.g.
⟨  ̃⟩ ⟨  ̃ ⟩/
=
φ −φ
ee,
i 2 2 (12)
which can be readily verified by assuming that φ ̃ obeys Gaussian distribution ( ) /( )
/( )
φ ≡ −φ σ π σ
Pe 2
2 2 2 . As suggested by equation (11), the distribution and hence all moments of the Gaussian noise are completely determined by the matrix C:
⟨b ̃ b ̃ ⟩ = (C) ,
i j i,j (13a)
⟨b ̃ b ̃ b ̃ b ̃ ⟩ = (C) (C) + (C) (C) + (C) (C) ,
i j k l i,j k,l i,k j,l i,l j,k (13b)
⟨ ̃  ̃  ̃ ⟩ ( ) ( ) ( )
∑
=−

b b b C C  C ,
i i i ii ii i i P
M p p p p pM pM
1 2 2 1 2 3 4 2 1 2 (13c)
where ∑P runs over all possible pairings of {i1, , i2M}. Equation (13) is the Wick’s theorem for Gaussian noises, and equation (13a) shows that the matrix C in equation (11) is the covariance matrix of the Gaussian noise.
3.1.2. Noise auto-correlations. A classical noise is usually characterized by its auto-correlation
C(τ) = ⟨b ̃(τ)b ̃(0)⟩, (14)
or equivalently the noise spectrum (the power distribution)
( ) ()
∫
ω ≡ ωτ τ τ
S e C d,
i (15)
both of which are even functions. The auto-correlation C(τ) is usually maximal at τ = 0 and decays with increasing |τ|. For example, the electron spin bath is usually modeled by the Ornstein–Uhlenbeck noise [68–71], which is Gaussian and has the auto-correlation
() /
τ = −|τ| τ
C be
rms
2 c (16)
and the noise spectrum
() ()
(/ )
ω= π δ τω
S 2b ,
rms
2 1 c (17)
where δ ∆ ≡ γ π ∆ + γ
γ 22
( ) ( / )/( )
( ) is the Lorentzian shape function. The auto-correlation or noise spectrum has three important properties: auto-correlation (or memory) time τc, the behavior of high-frequency cutoff, and the noise power
b ≡ ⟨b ̃ (0)⟩ = ⟨b ̃ (t)⟩
rms
2 2 2 . The auto-correlation time τc, which quantifies how fast the noise fluctuates, is the characteristic time for the auto-correlation to decay. Equivalently, 1/τc is the characteristic cutoff frequency above which the noise spectrum decays significantly (see equations (16) and (17) for the Ornstein–Uhlenbeck noise). If τc is large compared with the achievable timescale of control over the central spin and
Rep. Prog. Phys. 80 (2017) 016001


 Review
7
the high-frequency tail of the spectrum decays faster than power-law decay, then the noise is said to have a hard highfrequency cutoff. Otherwise, the noise has a soft cutoff. For example, the noise spectrum of the Debye phonon bath [72], S(ω) = 2αωΘ(ωD − ω) with Θ(ω) the Heaviside step function, has a hard cutoff, while that of the Ornstein–Uhlenbeck
noise has a soft cutoff as it decays as 1/ω2 at high frequency. The noise power is equal to the area of the noise spectrum:
() ()
∫∫
ωω
π ωω
π
==
−∞
∞∞
bS S
d
2
d.
rms
2
0
For a fixed noise power, rapidly fluctuating noise has a low and broad spectrum (figure 5(a)), while slowly fluctuating noise has a high and narrow spectrum (figure 5(b)). As will be discussed in section 3.3, the broad noise spectrum underlies the motional narrowing phenomenon in magnetic resonance spectroscopy [14, 25].
3.1.3. Markovian and non-Markovian noises and stochastic processes. Considering that there is considerable inconsistency in the terminology of Markovian/non-Markovian stochastic processes, noises, and decoherence, here we would like to make clear our usage of terminology, yet without the intention of unifying the usage in the vast literature. We note that it is useful to distinguish the noise and the stochastic process (such as phonon scattering, atom–atom collisions, and nuclear spin flip-flops) that causes the noise. A classical noise as the collection of the random variables b ̃ ≡ b ̃(t )
n n at all the time points t ≡ n∆t
n is characterized by the probability distribution P(b0) of b ̃0 and the probability distribution ( | − )
P b b , , b
n 0 n 1 of b ̃n conditioned on b ̃k being bk (k = 0, 1, , n − 1). The noise is caused by certain microscopic stochastic processes. A stochastic process is called Markovian or memoryless if the distribution of b ̃n depends
on b ̃n−1 only, i.e. ( | ) = ( | )
−−
P b b , , b P b b
n 0 n 1 n n 1 , so that the probability distribution of the noise can be written as
P(b , b , b , ) = P(b )P(b |b )P(b |b )  .
0 1 2 0 1 0 2 1 (18)
Physically, this occurs when the stochastic process (such as a phonon scattering, an atom–atom collision, or a nuclear spin flip-flop) takes a time much shorter than the timescale under consideration. For example, the atom–atom collision is Markovian under the impact approximation, and a phonon scattering is Markovian for a timescale much greater than ∼1 picosecond. On the other hand, a noise, caused by either a Markovian or non-Markovian stochastic process, is termed Markovian or memoryless when its auto-correlation time τc is much shorter than the central spin decoherence time. In general, a Markovian or non-Markovian noise could be produced by either a non-Markovian or Markovian stochastic process. For example, the Ornstein–Uhlenbeck noise (equations (16) and (17)) is caused by the Ornstein–Uhlenbeck process, which is characterized by a Gaussian distribution
( ) /( )
= − /( ) π
Pb e 2 b
bb
0 2 rms
0
2
rms
2 for the initial value b ̃0 and a
Gaussian conditional distribution for b ̃n [73]:
( )( )
( ) /( )
/
πσ
| =| =
σ −−
− − −∆ τ −
P b b , , b P b b e
2,
nn nn
bb
10 1
e2
n t c n 12 2
(19)
where /
σ= − −∆ τ
b 1e t
rms 2 c . Obviously, the OrnsteinUhlenbeck process is Markovian since the distribution of b ̃n only depends on bn−1. However, the Ornstein–Uhlenbeck noise has the auto-correlation ⟨  ̃  ̃ ⟩ /
= −| − | τ
bb b e
nm t t
rms
2 n m c (see
equation (16) for its continuous form), so it could be either Markovian or non-Markovian depending on whether or not its auto-correlation time τc is much larger than the central spin decoherence time. In addition, the Ornstein–Uhlenbeck noise is also Gaussian since its distribution function P(b , b , )
01
can be put into the form of equation (11). Under the classification based on τc, two kinds of noises are relatively simple: quasi-static noise with τc  duration of each measurement cycle (∼central spin decoherence time), and Markovian noise with τc  duration of each measurement cycle. The static noise  ̃( )  ̃
b t = b is completely specified by its static distribution P (b)
inh , so inhomogeneous dephasing caused by static noise can be easily treated (see section 2.5). The Markovian noise gives memoryless random jumps of the central spin, as described intuitively in section 2.3 (for T1 process) and section 2.4 (for Tφ process) in terms of two phenomenological jump rates γ and γφ.
3.2. Spin relaxation by transverse noises
For the sake of simplicity, let us assume b ̃ (t) = 0
z . The transverse noise-induced central spin-flip can be understood in a simple physical picture first proposed by Bloembergen et al [14, 74]: the Fourier spectrum b ̃±(ω) of the transverse noises
 ̃ ()
b± t may have nonzero components near the unperturbed spin-precession frequency ω0 and these components would induce resonant transitions between the two unperturbed eigenstates | ↑ ⟩ and | ↓ ⟩ at a rate proportional to the noise spectrum
( ) ⟨  ̃ ( )  ̃ ( )⟩ ⟨  ̃ ( ) ⟩
∫
ω ≡ τ τ∝ | ω |
ωτ
−+ ±
S b b0e d b
i 2 at frequency ω0. Usually the noise must fluctuate rapidly (τ   1/ω
c 0) in order for its spectrum to have a significant high-frequency
Figure 5. Schematic of the noise spectra for (a) a noise that fluctuates on a timescale τ  t
c and (b) a noise that fluctuates on a timescale τ   t
c , where t is the evolution time.
Rep. Prog. Phys. 80 (2017) 016001


 Review
8
component at ω0, so usually τc  central spin relaxation time (T1), i.e. the noise is Markovian. When ⟨  ̃ ( )  ̃ ( ′)⟩
−+
b t b t is the only nonvanishing noise auto-correlation, the Born–Markovian approximation [14] gives the intuitive result (equation (4)) for the environment-induced central spin evolution, with β = 0 (i.e. the classical noise is equivalent to an environment at infinite temperature) and an explicit expression for the central spin-jump rate:
()
γω
==
T
1S
2 4,
1
0
which is the noise spectrum at the central spin transition frequency ω0 (as spin relaxation involves an energy transfer ω0), thus a rapidly fluctuating Markovian noise with τ   1/ω
c0
contributes significantly to spin relaxation (figure 5(a)), while non-Markovian noises contribute negligibly (figure 5(b)).
3.3. Pure dephasing by longitudinal noises
Here, we assume b ̃ (t) = b ̃ (t) = 0
x y and write b ̃z(t) as b ̃(t) for
brevity. In the interaction picture with respect to Hˆ0, the Hamiltonian
Hˆ (t) = Sˆ b ̃(t),
z (20)
describes the random jumps of the central spin-transition frequency or equivalently diffusion of the resonance line (similar to Brownian motion). Therefore, this model is known as random frequency modulation or spectral diffusion in the context of magnetic resonance spectroscopy following the pioneering work of Anderson [24, 25, 73] and Kubo [26]. In the context of quantum computing, this model was elaborated by de Sousa and Das Sarma [75–77] to explain the spin-echo experiments for donor electron spins in silicon [78–82]. The theory gives reasonable order-of-magnitude agreement (within a factor of 3) for the dephasing time, but fails to explain the e−τ2 decay of the echo envelope [83]. For a general noise, a random relative phase
 ̃( )  ̃( )
∫
φ≡ ′′
t b t dt
t
0 (21)
is accumulated between the unperturbed eigenstates | ↑ ⟩ and | ↓ ⟩, leading to the decay of the off-diagonal coherence
( ) ⟨  ̃( )⟩
= −φ
L t e i t . (22)
In contrast to spin relaxation caused by the high-frequency part (near ω0) of the noise, the pure dephasing is dominated by the low-frequency part of the noise (see figure 5), because high-frequency components ω  1/t are effectively averaged out in equation (21). Significant dephasing appears when the root-mean-square
phase fluctuation ⟨φ ̃2(t)⟩ attains unity, i.e. the dephasing time T2 can be estimated from ⟨φ ̃ (T )⟩ = 1
2 2 , where
⟨  ̃ ( )⟩ ⟨  ̃( )  ̃( )⟩
∫∫
φ t = dt dt b t b t .
tt
2
0
1 0
2 1 2 (23)
Here, the accumulation of the random phase depends crucially on the ratio between τc and T2:
1. Quasi-static noise (τ  1/b ∼ T
c rms 2). Here,  ̃( )  ̃
φ t ≈ bt and
hence the phase fluctuation ⟨φ ̃ (t)⟩ ≈ b t
2 rms increases linearly with time. This gives inhomogeneous dephasing on a time scale T = T∗ ∼ 1/b  τ
2 2 rms c, consistent with the discussion in section 2.5. In this regime, the dephasing time is determined only by the noise power and is independent of τc. 2. Markovian noise ( 1 b T
c rms 2
τ  /  ). The noise tends to average out itself during a single measurement cycle, leading to a slow, diffusive increase of the phase
fluctuation ⟨φ ̃ (t)⟩ ∼ (b τ ) t /τ
2 rms c c. This result can
also be obtained from equation (23) by noting that only |t − t |   τ
1 2 c contributes significantly to the int
egral. This gives ‘true’ decoherence on a time scale
T T 1 b 1/b
2 rms
2 c rms c
= φ ∼ /( τ )   τ . Actually, the use of the Born–Markovian approximation recovers the intuitive result (equation (5)) with an explicit expression for the central spin-jump rate:
T
Sb b
1
2
0
4,
rms
2 c rms
γ= = ∼ τ
φφ

( ) (24)
which is the noise spectrum at zero frequency (as pure dephasing involves no energy transfer). The above discussions show that faster fluctuations of the noise lead to longer dephasing time or, in terms of the Fourier transform of L(t), a narrower magnetic resonance line. This is the motional narrowing phenomenon in magnetic resonance spectroscopy [14, 25], where the random motion of atoms makes the magnetic noise fluctuate rapidly and hence reduces the width of the magnetic resonance line of the central spin.
On sufficiently short timescales, any noise with a hard highfrequency cutoff becomes static and the small random phase can be treated up to the second order to give Gaussian inhomogeneous dephasing ( ) ( ) /
=−
L t ebt
inh 2
rms 2 (see equation (9)). However, the entire dephasing profile over the timescale ∼ T2 depends on the specific statistics and auto-correlation of the noise. If the noise is Gaussian, then the dephasing can be obtained from equation (12) as [24]
( ) ⟨  ̃ ( )⟩/
= −φ
Lt e .
t2
2
According to the discussions following equation (23), quasistatic noise (b τ  1
rms c ) gives Gaussian inhomogeneous dephasing ( ) ( / )
=− ∗
L t e tT
inh 2 2 on a short timescale T∗ ∼ 2 /b  τ
2 rms c,
consistent with equation (9). Markovian noise (b τ  1
rms c ) gives exponential ‘true’ decoherence ( ) /
=− φ
L t e t T on a much longer
timescale Tφ ∼ 1/(brmsτ )  τ
2 c c, consistent with equation (24). In the intermediate regime, the dephasing profile depends sensitively on the noise spectrum, e.g. the spectrum of the OrnsteinUhlenbeck noise in equation (17) gives
( ) ( ( ))
/
= − τ + τ − −| | τ
L t exp b t b 1 e ,
t
rms
2 c rms
2 c
2c
whichreducestotheexponentialdecoherencewithTφ = 1/(brmsτ )
2c
for t  τc and the Gaussian inhomogeneous dephasing with T∗ = 2 /b
2 rms for t  τc.
Rep. Prog. Phys. 80 (2017) 016001


 Review
9
4. Semi-classical noise theory of dynamical decoupling
Dynamical decoupling (DD) is a powerful approach to suppressing the central spin decoherence. The key idea is to dynamically average out the coupling of the central spin to the environment by frequently flipping the central spin. The DD approach originated from the Hahn echo in nuclear magnetic resonance [51] and was later developed for high-precision magnetic resonance spectroscopy [84–86]. Then, the idea of DD was introduced in quantum computing [87–90], which stimulated numerous studies on applications and extensions to suppressing qubit decoherence for quantum computing (see [91] for a review). DD can efficiently suppress decoherence when the DD-induced central spin-flip is much faster than the autocorrelation time τc of the environmental noise, so that the lost coherence can be retrieved before it is dissipated irreversibly in the environment. According to section 3.2, spin relaxation is usually dominated by Markovian noise with τ   1/ω
c 0, while flipping the central spin usually requires a duration   1/ω0; thus DD is inefficient for suppressing spin relaxation. As discussed in section 3.3, pure dephasing is usually dominated by non-Markovian noises and especially static noise, so DD is efficient for combating pure dephasing. Therefore, we only consider pure dephasing in this section.
In a general N-pulse DD scheme, the N instantaneous π-pulses are applied successively at τ1 < τ2 <  < τN to induce the flip between | ↑ ⟩ and | ↓ ⟩ and the central spin is measured at a later time td. In the Schrödinger picture, the central spin
Hamiltonian consists of the external field term Hˆ0 (equation (1)), the DD control term
ˆ ( ) ( )ˆ
= ∑ πδ − τ
=
H t t S,
n
N
c nx 1
(25)
and the noise term  ̃( ) ˆ
b t Sz. A convenient way is to work in the interaction picture with respect to Hˆ + Hˆ (t)
0 c , where the central spin Hamiltonian is (see equation (20))
ˆ ( ) ( )  ̃( ) ˆ
H t = s t b t Sz (26)
and s(t) is the DD modulation function: it starts from s(0) = +1 and changes its sign every time the central spin is flipped by a π-pulse, i.e. each π-pulse in the DD switches the sign of the environmental noise. The spin decoherence in the absence of any control is called free-induction decay (FID), which corresponds to a constant modulation function s(t) ≡ +1. Intuitively, when the sign switch by DD is more frequent than the fluctuation of the noise b ̃(t) (τc > pulse interval), DD could effectively speed up the noise fluctuation and suppress dephasing efficiently (reminiscent of motional narrowing). On the other hand, when the sign switch coincides with the characteristic fluctuation of a noise, DD could resonantly enhance the effect of the noise b ̃(t), causing rapid decoherence. Below we discuss two important cases: static noises and and Gaussian noises.
If the noise is static during each measurement cycle [0, td],
then  ̃( )  ̃ ( )
∫
φ t = b s t dt
t d0
d vanishes when td satisfies the echo
condition:
()
∫ s t dt = 0.
t
0
d
(27)
This means that a static noise can be completely eliminated at the echo time td. The simplest DD scheme is the Hahn echo [51], where a π-pulse is applied at τ followed by a measurement at t = 2τ
d. For Gaussian noises, the central spin dephasing is completely determined by the noise auto-correlation:
( ) ⟨  ̃ ( )⟩/
= −φ
Lt e ,
t
d2
2 d (28)
where [92]
⟨  ̃ ( )⟩ ( ) ( )
∫
φ ωω ω
π
=
−∞
∞
t t S F td
2
2d d
2 d (29)
is determined by the overlap integral of the noise spectrum
( ) ⟨  ̃( )  ̃( )⟩ ( )
∫
ω ≡ = −ω
ω −∞
∞
S b t b 0 ei tdt S and the dimensionless
noise filter
( ) () ( )
∫
ω ≡ = −ω
−ω
F t t st t F t
1 ed ,
tt
d d
20
i
2
d
d
(30)
which is related to the Fourier transform of the DD modulation function s(t) and obeys F(ωt ) ⩽ 1
d as well as the normal
ization ( ) /
∫ ω ω= π
−∞
∞F t d 2 t
d d.
This noise-filter formalism [92] provides a physically transparent understanding of dephasing caused by Gaussian noise and its control by DD in the frequency domain, e.g. coherence protection can be achieved by designing the noise filter to minimize the overlap integral in equation (29). For FID, the filter
( ) ( /)
( /)
ωω
ω
ω
F t= t ≡
t
sin 2 t
2 sinc 2
FID d
2d
d2
2 d (31)
passes low-frequency noises (ω   π/td) but attenuates highfrequency noises (ω   π/td) (black solid line in figure 6), i.e. low-frequency noises are most effective in causing pure dephasing. For quasi-static noise (τ  t
c d), the noise spectrum (blue line in figure 6) is well within the low-pass regime of the filter (black line in figure 6), so all noise power passes, leading to rapid inhomogeneous dephasing (equation (9)). For Markovian noise (τ  t
c d), the noise spectrum is broad (red line
Figure 6. Noise filter for FID and spectra of slowly fluctuating (blue line, τ  t
c,slow d) and fast fluctuating (red line, τ  t
c,fast d)
noises.
Rep. Prog. Phys. 80 (2017) 016001


 Review
10
in figure 6) and remains nearly a constant ( )  ̄
S ω ≈ S ∼ brmsτ
2c
within the low-pass regime, so φ ≈
( )  ̄
t St
2 d d leads to exponential dephasing on a time scale ∼ 1/S ̄ ∼ 1/(brmsτ )
2 c  inhomogeneous dephasing time. A particularly interesting DD sequence is the N-pulse Carr–Purcell–Meiboom–Gill (CPMG-N) [93, 94] consisting of N instantaneous π-pulses applied at τ = t (n − 1/2)/N
nd
(n = 1, 2, , N ), respectively. The filter for CPMG-N control is
() ()
( /)
ωω
ω
=
ω
ω
−
∓
Ft t
t
2
sin
cos
1 cos
2
t
N t N
CPMG N d
4 4 2 2
d
d2
d
d
(upper sign for even N and lower sign for odd N), which, for N  1 has a primary peak at ω = Nπ/td = π/τ (τ ≡ td/N is the pulse interval) and a bandwidth ∼ π/td (see figure 7). Near this peak,
( ) ( / )/ ( / )/
ωπ π
≈=
ω π τ ω πτ
− −− − −
F t 4e 4e .
t Nt N
CPMG N d 2
12
2
12
d
2 d2 2 2 2
As mentioned before, for DD to be efficient, the pulses must be applied faster than the noise auto-correlation time (τ < τc). For CPMG-N, this is equivalent to that the filter’s peak frequency π/τ > noise cutoff frequency 1/τc. For Markovian noise with τc  τ, the noise spectrum is nearly constant over the entire band-pass window of the filter, so DD has no effect.
5. Quantum noise versus classical noise
In the semi-classical theory of central spin decoherence, the central spin is treated as a quantum object, while the spin bath is approximated by a classical noise. In spin-based solidstate quantum technologies, the nanoscale spin bath is also a quantum object and requires a quantum description. Within the characteristic timescale of central spin decoherence, the central spin and the spin bath can be regarded as a closed quantum system (see figure 1). Here, we are only interested
in the most relevant mechanism for electron spin decoherence in nuclear spin baths: pure dephasing, i.e. we assume that the central spin-transition frequency ω0 is far beyond the high-frequency cutoff of the bath noise spectrum. In this case, the central spin and the bath are described by a general pure dephasing Hamiltonian [27–29]
ˆ ˆ ˆˆ
H = H + bS
B z (32)
in the interaction picture with respect to Hˆ0 (equation (1)),
where HˆB is the bath Hamiltonian and bˆ is the bath noise operator coupled to the central spin. Below, we will classify the noises from the spin bath into two categories according to their natures, namely static thermal noises and dynamical quantum noises. It should be noted that the noises from the ‘rest of universe’ (figure 1), which is taken as classical, can be static or dynamical. Ultimately, all noises have a quantum origin (e.g. the thermal distribution of a spin bath can be ascribed to entanglement between the bath and the rest of universe). Here, the static thermal noise and the dynamical quantum noise are differentiated in the sense that the spin bath and the central spin are regarded as a closed quantum system in the timescale of interest.
5.1. Static thermal noises
The initial state of the bath is the maximally mixed thermal state (relevant for nuclear spin baths):
ˆˆ
ˆ ⟩⟨
∑
ρ= = | |
I
I PJ J
Tr ,
J
J
B
eq (33)
When [bˆ, Hˆ ] = 0
B , {|J⟩} can be chosen as the common eigen
states of bˆ and HˆB. If the initial state of the bath were a pure state |J⟩, then it would remain in |J⟩, and during the measurement cycle the central spin would evolve under a constant
noise field b = 〈J|bˆ|J〉
J from ρˆ(0) to ˆ ( ) ˆ( )
ˆˆ
ρ ≡− ρ
t e 0e
J
ib S t ib S t
Jz Jz
with an oscillating off-diagonal coherence ( ) = −
L t e ibJt, while the coupled system would evolve as
ρˆ(0) ⊗ |J⟩⟨J|evol⟶ution ρˆ (t) ⊗ |J⟩⟨J|.
J
The ensemble average over the thermal distribution in equation (33) gives the evolution
ˆ( ) ⟩⟨ ⟶ ˆ ( ) ⟩⟨
∑∑
ρ 0 ⊗ P |J J|evolution ρ t ⊗ P |J J|
J
J J
JJ
which coincides with the decoherence induced by a static noise with the distribution P (b) ≡ ∑ P δ(b − b )
inh J J J (see equation (7) of section 2.5). In this sense, the thermal noise (caused by the thermal distribution of the bath states) amounts to inhomogeneous dephasing. The static thermal noise usually dominates the FID of central spin coherence, but it can be completely removed by DD at the echo time.
5.2. Dynamical quantum noises
When [Hˆ , bˆ] ≠ 0, the eigenstate of the noise operator bˆ is
not necessarily the eigenstate of HˆB. Thus, even if the bath is
Figure 7. (a) Noise filter functions for FID (N = 0) and CPMG-N sequence for fixed total evolution time td. (b) CPMG-N filter function for fixed pulse interval τ .
Rep. Prog. Phys. 80 (2017) 016001


 Review
11
initially in an eigenstate of bˆ, the intrinsic bath Hamiltonian HˆB would drive the bath into different eigenstates, producing a dynamical noise on the central spin. This noise is best described in the interaction picture of the bath, where the total Hamiltonian
ˆ ( ) ˆ( ) ˆ
H t = b t Sz (34)
with the noise operator in the interaction picture,
ˆ( ) ˆ
ˆˆ
≡−
b t e be
iH t iH t
B B , being the quantum analog of the classical noise b ̃(t). Note that if [Hˆ , bˆ] = 0, then bˆ(t) would have no time dependence. Thus, the dynamical nature of the noise is ascribed to the quantum nature of the bath5. The quantum noise bˆ(t) at different times, in contrast to the classical noise, does not commute in general. So the decoherence of the central spin,
( ) ⟨(  ̄ )( )⟩
( / ) ˆ( ) ( / ) ˆ( )
∫∫
=− −
′′ ′′
L t T e Te
i 2 b t dt i 2 b t dt
tt
00
involves the time-ordering (anti-time-ordering) superoperator T (T ̄ ). For a large many-body bath, the effect of the dynamical noise is similar for most initial states |J⟩. Therefore, the central spin coherence can be approximated as
L(t) ≈ L (t)L (t)
inh dyn (35)
up to a global phase factor, i.e. the decoherence can be separated into the effect of the static thermal noise, i.e. L (t)
inh in
equation (7), and that due to the dynamical quantum noise (the ‘true’ decoherence), i.e.
( ) ⟨ (  ̄ )( ) ⟩
( / ) ˆ( ) ( / ) ˆ( )
∫∫
=| |
−−
′′ ′′
L t J T e Te J .
bt t bt t dyn
i2 d i2 d
tt
0 0 (36)
Note that |L (t)|
dyn is similar for most initial states |J⟩ of a large many-body bath.
In the presence of the DD control Hamiltonian Hˆc(t) (equation (25)), we can work in the interaction picture with respect to ˆ ˆ ( ) ˆ
H +H t +H
0 c B, where the total Hamiltonian is
ˆ ( ) ( ) ˆ( ) ˆ
H t = s t b t Sz. (37)
At the echo time, the static thermal noise is completely removed, so the central spin undergoes ‘true’ decoherence due to the dynamical quantum noise:
( ) ⟨(  ̄ )( )⟩
( / ) ( ) ˆ( ) ( / ) ( ) ˆ( )
∫∫
=− −
L t T e Te
stbt t stbt t d
i2 d i2 d
tt
0
d
0
d
(38)
〈 (  ̄ )( ) 〉
( / ) ( ) ˆ( ) ( / ) ( ) ˆ( )
∫∫
≈| |
−−
J T e Te J ,
i 2 s t b t dt i 2 s t b t dt
tt
0
d
0
d
(39)
where the second line is similar for most initial states |J⟩.
5.3. Quantum Gaussian noises
A close analogy to the classical noise model is possible when the commutator [bˆ(t1), bˆ(t2)] is a c-number, so that T and T ̄ play no role up to a phase factor. This happens when the bath
state ρˆB
eq can be mapped to a non-interacting bosonic state and
bˆ(t) can be mapped to a bosonic field operator (i.e. a linear combination of creation and annihilation operators), so that the quantum noise is Gaussian. In this case, the off-diagonal coherence assumes exactly the same form as equation (22) for classical Gaussian noise:
() ⟨ ⟩
ˆ( )
= −φ
Lt e ,
t
d id
where
ˆ( ) ( ) ˆ( )
∫
φ t ≡ s t b t dt
t
d 0
d
is the quantum analog to the classical random phase φ ̃(td). Using linked-cluster expansion for non-interacting bosons (see section 8.3) and assuming ⟨bˆ(t)⟩ = 0 (just for simplicity) gives an exact result
Lt
t t t st st bt bt
e,
d d , 2.
t
tt
d /2
2d 0 1 0 2 1 2 1 2
2d
dd
∫∫
φ
=
=
−φ
()
〈 ˆ ( )〉 ( ) ( )〈{ ˆ( ) ˆ( )}/ 〉
〈 ˆ ( )〉
(40)
The above equation has exactly the same form as the classical case (equation (28)). The quantum Gaussian noise is best illustrated in the spinboson model [72], in which the central spin is linearly coupled to a collection of non-interaction bosonic modes {bˆm}
in thermal equilibrium, corresponding to ˆ ˆ† ˆ
=∑ ω
H bb
B m m mm
and ˆ ( ˆ ˆ )
†
b=∑ λ b +b
m m m m . Under DD control, the total Hamiltonian in the interaction picture assumes the standard form (equation (37)), where the quantum noise
ˆ( ) ( ˆ ˆ )
†
= ∑λ +
ω −ω
bt b e b e
m
m mi t m i t
mm
is Gaussian. The quantum noise spectrum as the Fourier transform of ⟨{bˆ(t ), bˆ(t )}/2⟩
1 2 is readily obtained as
( ) [  ̄( ) / ][ ( ) ( )]
∑
S ω = 2π λ n ω + 1 2 δ ω + ω + δ ω − ω ,
m
mm m m
2
where  ̄(ω) = /( − )
βω
n 1 e 1 is the Bose–Einstein distribution. The exact central spin dephasing is obtained by substituting this spectrum into the noise-filter formalism (equations (28) and (29)).
5.4. Can quantum baths be simulated by classical noises?
The key difference between classical noises and quantum noises is that the former commutes at different times, while the latter does not. This means that the action of bˆ(t) at an earlier time changes its action on the bath evolution at a later time. By contrast, in the classical model (equations (21) and (22)), only the integral of the classical noise matters, i.e. the classical noise at different times do not influence each other. In the presence of DD control, we need to replace bˆ(t) with s(t)bˆ(t). Therefore,
the sign switch of bˆ(t) due to a DD pulse at an earlier time may
change the action of bˆ(t) at a later time, i.e. controlling the central spin may change the quantum noise itself. This is the so-called quantum back-action from the central spin [95–97]:
5 Here, the central spin and the spin bath forms a closed system, so the thermal noise from the spin bath is static and the quantum noise from the spin bath is dynamical. Noises from other environments that are not explicitly included in our model (equation (32)) can also be dynamical and are often treated as classical.
Rep. Prog. Phys. 80 (2017) 016001


 Review
12
the evolution of the quantum bath conditioned on the central spin state (see section 6 for details) governs the quantum noise. It is desirable to simulate quantum baths (or equivalently quantum noises) with classical noises. First, computing central spin decoherence caused by a quantum bath requires a large amount of numerical simulations of the many-body dynamics of the bath, while computing the decoherence caused by classical noises, especially classical Gaussian noise, is much simpler. Second, controlling the central spin does not change the classical noise, so the noise-filter formalism of DD allows efficient reconstruction of the classical noise [98–102], which in turn can be used to efficiently design optimal quantum control to suppress the central spin decoherence. By contrast, controlling the central spin can actively change the quantum noise itself. On the one hand, this provides more flexibility in engineering the quantum noise. On the other hand, this makes it impossible to describe the quantum noise without referring to the control over the central spin. The question is ‘under what circumstances can a quantum bath be approximated by a classical noise?’ That is, given a central spin in a quantum bath, is it possible to find a classical noise (Gaussian or non-Gaussian) that is capable of faithfully reproducing the decoherence of the central spin under all classical controls (not necessarily DD)? The answer to this general question is still absent due to the existence of a diverse range of classical noises and controls. Here, we restrict ourselves to a simpler question: is it possible to find a Gaussian noise to faithfully reproduce the decoherence of the central spin under all possible classical controls? According to section 5.3, this is possible when the quantum noise is Gaussian, i.e. when the state of the bath can be mapped to a noninteracting bosonic state and the quantum noise can be mapped to a bosonic field operator (i.e. a linear combination of creation and annihilation operators) such as the spin-boson model in section 5.3. Actually, according to equation (40), if a quantum noise is Gaussian, it is equivalent to a classical noise that has the same noise spectrum. Therefore, the question of approximating a quantum bath as a classical Gaussian noise is equivalent to the question about the Gaussian nature of the quantum bath.
5.4.1. One-spin bath. To illustrate the condition required for the Gaussian noise approximation to be valid, let us first consider the simplest spin ‘bath’, namely, a bath that has only one
spin-1/2 ˆIm. Without loss of generality we assume the bath Hamiltonian ˆ ˆ
H = ωmI m
z
B and the noise operator as ˆ ˆ
b = 2λmI m
x
(therefore, the bath causes a dynamical quantum noise such as that in section 5.2). The initial state of the bath is taken as the spin-down eigenstate of its intrinsic Hamiltonian. Under either the short-time condition |λ |t  1
m d or off-resonant condition |λ |  |ω |
m m , the coupling to the central spin only weakly perturbs the bath, so we can map the initial state of the bath into the
vacuum state|0⟩m of a Holstein–Primakoff boson mode{ ˆ ˆ† }
bm, bm :
=− ≈
ˆ− ˆ ˆ ˆ ˆ
†
⎛
⎝⎜ ⎞
⎠⎟
I 1 bb b b,
m m m m m (41)
ˆ ˆˆ /
†
I = b b − 1 2.
m
z
m m (42)
Then, we have ˆ ˆ ˆ /
†
H =ω b b −ω 2
B m m m m and ˆ ( ˆ ˆ† )
b≈λ b +b
mm m
and recover the single-mode version of the spin-boson model, which has been discussed in section 5.3. Substituting the quantum noise spectrumS(ω) = πλm[δ(ω + ωm) + δ(ω − ωm)]
2
into the noise-filter formalism immediately gives the central spin decoherence under Gaussian noise approximation:
( ) ( )/
= −λ ω
Lt e ,
F tt
Gau d 2
mm
2 dd
2
where F(z) is the noise filter determined by the DD sequence. Under either the short-time condition|λ |t  1
m d or off-resonant condition |λ |  |ω |
m m , the central spin decoherence caused by this bath spin is small and the Gaussian approximation results indeed agree well with the exact results, e.g. the FID
()
()
( / ) ( /)
λ
λω
λω
=
=− +
+
−λ ω ω
Lt
Lt t
e,
1 2 sin 2 ,
t
m
mm
mm
Gau 2 sin 2
2
22
2
22
mm m
22 2
and the Hahn echo at t = 2τ
d:
()
() ( )
( / ) ( /)
τ
τ λω
λω
λ ωτ
=
=− +
+
− λ ω ωτ
L
L
2e ,
2 1 8 sin 2 .
mm
mm
mm
Gau 8 sin 2
22
2 22
4
22
mm m
22 4
If the bath consists of many independent spin-1/2s, then we can map the initial state of the mth bath spin into the vacuum state of the mth Holstein–Primakoff boson mode and obtain the many-mode spin-boson model discussed in section 5.3.
5.4.2. Many-body bath. A spin bath that has many-body interactions can, in general, be written as Hˆ = ∑ ε |m⟩⟨m|
B mm
and its initial state can be taken as an eigenstate |k⟩. Gen
erally, the noise operator bˆ could induce the excitations |k⟩ → |m⟩ (m ≠ k) with amplitudes λ ≡ ⟨m|bˆ|k⟩
mk and energy costs ω ≡ ε − ε
mk m k. When all excitations are off-resonant (|λ |  |ω |
mk mk ) or when the time is short |λ |t  1
mk d , we can approximate the excitation by a boson mode bˆmk to obtain
a spin-boson model, where ˆ ( ˆ )
()
†
≈∑ λ +
≠
b b h.c.
m k mk mk and
ˆ ˆˆ
()
†
≈ε +∑ ≠ ω
H bb
B k m k mk mk mk.
5.4.3. Electronic and nuclear spin baths. For a central electron spin in an electron spin bath, the central spin and the bath spins are alike and are typically coupled together through magnetic dipolar interactions. Thus, the central spin decoherence caused by many bath spins is usually much faster than the bath spin evolution caused by a single central spin, i.e., within the time scale of the central spin decoherence, the short-time condition is satisfied and the quantum noise from the electron spin bath can be approximated by classical Gaussian noise. This has been confirmed by many theoretical and experimental studies [68, 69, 71, 103, 104], where the noise spectrum obtained by fitting the central spin decoherence under different DD controls agrees with a widely used classical Gaussian noise: the Ornstein–Uhlenbeck noise (equations (16) and (17)). Witzel et al [70] further demonstrates that the spectrum of the quantum noise directly calculated from the
Rep. Prog. Phys. 80 (2017) 016001


 Review
13
quantum many-body theory (see section 8.4.4) agrees reasonably with the Ornstein–Uhlenbeck noise and can well describe the central spin decoherence under various DD control, unless a few bath spins are strongly coupled to the central spin. In that case, the quantum noise is dominated by a few strongly coupled bath spins and cannot be approximated as classical Gaussian noise. For a central electron spin in a nuclear spin bath, the hyperfine interaction (HFI) between the bath spin and the central spin is much stronger than the magnetic dipolar interaction between nuclear spins, but could be weaker than the Zeeman splitting of individual nuclear spins under a strong magnetic field (see section 7 for various interactions in paradigmatic physical systems). In other words, the off-resonant condition could be satisfied for the evolution of individual nuclear spins, but is not for the evolution of nuclear spin clusters. Two situations have been found where the nuclear spin bath can be approximated by classical Gaussian noise:
1. Anisotropic HFI (equation (50)) and intermediate magnetic field. Here, the magnetic field is not too strong such that central spin decoherence is dominated by the noise from individual nuclear spins instead of nuclear spin pairs, and not too weak such that the nuclear spin Zeeman splitting  HFI (off-resonant condition satisfied). Tuning the magnetic field allows the crossover between Gaussian and non-Gaussian behaviors, as observed experimentally for the 13C nuclear spin bath in the NV center [105, 106]. 2. Decoherence of electron-nuclear hybrid spin-1/2 near the so-called ‘clock’ transitions of a Bi donor in silicon [97]. Near the ‘clock’ transition, electron-nuclear hybridization dramatically suppresses the HFI between the hybrid spin1/2 and the 29Si nuclear spin bath. This leads to two effects. First, it prolongs the coherence time by two orders of magnitude (from ∼0.8 ms to ∼90 ms) [107]. Second, when the suppressed HFI becomes weaker than the intrinsic 29Si bath dynamics (off-resonant condition satisfied), the bath can be well approximated by classical Gaussian noise (with the bath auto-correlation function shown in figures 8(a) and (b)), as confirmed by the excellent agreement between the semi-classical model with a Gaussian noise, the exact results from the quantum many-body theory, and experimental measurements [97], as shown in figures 8(c) and (d). Away from the ‘clock’ transitions, the HFI becomes larger and the Gaussian noise model is no longer valid.
5.4.4. Test of Gaussian noise model in real systems. The DD noise spectroscopy method based on the Gaussian noise model has been widely used to characterize the baths [98–100]. The main idea is to use a specific DD control sequence (such as CPMG-N with large N) with the filter function approximated as a Dirac delta function at ω = ± πN /t
0 d (see figure 9(a)),
tF t ,
dd 0 0
(ω ) ≈ π[δ(ω − ω ) + δ(ω + ω )]
Then, following equations (28) and (29), the bath noise spectrum can be determined as
S( ± ω ) = −2ln[L(t )]/t .
0 dd
However, this method can reproduce a meaningful bath noise spectrum only if the the bath can be described by a semi-classical Gaussian noise model. For example, in the natSi:Bi system, we use the DD noise spectroscopy method to determine the effective noise spectra corresponding to the CPMG-100 case, and then use the derived noise spectra to calculate the spin decoherence under other DD control sequences [97]. Close to the ‘clock’ transition, the nuclear spin bath produces approximately a Gaussian noise, then the DD noise spectroscopy method can not only reproduce the spin decoherence curves for other DD control (see figure 9(b)), but also well reproduce the exact noise spectrum obtained from exact quantum calculations (figure 9(c)). However, far away from the ‘clock’ transition, the Gaussian noise approximation is not valid any more, so we find increasing discrepancies between the exact decoherence model and the semi-classical model using the DD noise spectroscopy method as the pulse number of CPMG-N deviates from 100 (figure 9(d)).
Figure 8. Experimental test of Gaussian noise model in natSi:Bi system. (a) Relative auto-correlation function C(t) − C(0) of the 29Si nuclear spin bath at the ‘clock’ transition of bismuth
donors in silicon (B = 79.9
CT mT) calculated by the CCE method (CCE-M denotes the Mth-order CCE truncation by keeping cluster correlations up to a certain size M, see section 8.4.4 for details). Here, a specific nuclear spin configuration is chosen with the external magnetic field B∥[1 1 0]. (b) C(t) − C(0) (solid lines) at the ‘clock’ transition for several magnetic field
orientations in the [0 0 1] − [1 1 0] plane with θ = 0 corresponding to [0 0 1]. Results are obtained by averaging over 50 different nuclear spin configurations. Dashed lines are fits of the form ∆ {exp[−(|t|/τ) ] − 1}
2 n . ((c) and (d)) Comparisons of electron spin decoherence obtained by the quantum model (solid lines), the semiclassical model (dashed lines), and the experimental measurement (circles) for the magnetic fields near the ‘clock’ transition. Here,
N = 2, 4, 8, 16, 32, 64, 128 corresponds to the DD control CPMG-2, XY-4, XY-8, XY-16, (XY-16) × 2, (XY-16) × 4, (XY-16) × 8. In theoretical calculations, CPMG-N is equivalent to XY-DD. Reproduced figure with permission from [97]. Copyright 2015 by the American Physical Society.
Rep. Prog. Phys. 80 (2017) 016001


 Review
14
6. Quantum picture of central spin decoherence
Up to now, we have given two different interpretations of central spin decoherence. First, random modulation of the central spin’s transition frequency by classical noises (section 3) or quantum noises (section 5). Second, random state collapses of the central spin due to measurement by the environment (section 2), but the environment is not explicitly treated there. In this section, we give a full quantum picture [27, 31, 108] that substantiates the previous intuitive measurement interpretation of central spin decoherence. The starting point is the general pure-dephasing Hamiltonian in equation (32) for the closed quantum system consisting of the central spin and the bath [27–29]:
= + = |↑ ↑|+ |↓ ↓|
+−
H S b H H Hˆ ,
zB
ˆ ˆ ˆ ˆ ˆ 〉〈 〉〈 (43)
where ˆ ≡ ˆ ± ˆ/
H± H b 2
B are the bath Hamiltonians depending on the central spin states being | ↑ ⟩ or | ↓ ⟩. The initial state of the bath is the maximally mixed thermal state (equation (33)). However, central spin decoherence under DD control is usually insensitive to the initial state of the bath (as discussed in section 5.2). This allows us to take a pure state |J⟩ sampled from the thermal ensemble (see equation (33)) as the initial state of the bath to provide a transparent quantum picture of decoherence [27–29]. Note that a pure initial state of the bath can, in principle, be prepared via special methods such as quantum measurements of the bath [48, 56–59] and nonlinear feedback [60–66, 109].
6.1. Decoherence as a result of measurement by environment
Now the initial state of the whole system is the product of the central spin state |ψ⟩ = | ↑ ⟩ + | ↓ ⟩
+−
C C and the pure
bath state |J⟩. The bath undergoes bifurcated evolution
⟩ → ( )⟩ ⟩
ˆ
|| ≡ |
± −±
J J t e iH t J (figure 10(a)), and the coupled system evolves into an entangled state
|Ψ( )⟩ ≡ | ↑ ⟩ ⊗ | ( )⟩ + | ↓ ⟩ ⊗ | ( )⟩
+ +− −
t C J t C J t . (44)
During this process, the population of the unperturbed central spin eigenstates | ↑ ⟩ and | ↓ ⟩ remains unchanged, but the offdiagonal coherence
( ) ⟨ ( ) ( )⟩ ⟨ ⟩
ˆˆ
= | =| |
−+ −
−+
Lt J t J t Je e J
iH t iH t (45)
generally decays due to the bifurcated bath evolution [27–29]. From the viewpoint of quantum measurement [13, 110], the central spin state | ↑ ⟩ (| ↓ ⟩) is recorded in the bath pathway |J+(t)⟩ (|J−(t)⟩). The off-diagonal coherence between | ↑ ⟩ and | ↓ ⟩ is the overlap between these two pathways of the bath. Below, we discuss two specific cases.
1. [bˆ, Hˆ ] = 0
B . The initial bath state |J⟩ can be chosen as a
common eigenstate of HˆB and bˆ, with eigenvalues εJ and bJ, respectively.Then,thetwopathways ( )⟩ ⟩
( /)
|= |
ε
± −±
J t e i b 2t J
JJ
are identical up to a phase factor and completely indistinguishable. There is no quantum entanglement between the central spin and the bath, and the central spin coherence ()= −
L t e ibJt does not decay, but just acquires a phase due to the static noise field bJ, consistent with the discussions in section 5.1. 2. [bˆ, Hˆ ] ≠ 0
B . The initial state |J⟩, if taken as an eigen
state of HˆB, is generally not an eigenstate of bˆ, so it undergoes bifurcated evolution into different pathways |J±(t)⟩. Correspondingly, the central spin coherence
( ) ≈ ⟨ ( )| ( )⟩
−+
L t J t J t decays due to the bifurcated bath evolution and hence quantum entanglement between the central spin and the bath. Using = ∫
− − − ′′
+T
ˆ ˆ ( ) ˆ( )
e ee
H t Ht bt t
i i i/2 d
t B0
and = ∫
− ′′
− T ̄
ˆ ( ) ˆ( ) ˆ
ee e
iH t i/2 b t dt iH t
t
0 B , we immediately see that
⟨ ( )| ( )⟩
−+
J t J t is just the ‘true’ decoherence L (t)
dyn caused by the dynamical quantum noise (equation (36)), which has been discussed in section 5.2. When the two pathways of the bath become orthogonal and hence completely distinguishable at a certain time, the central spin is perfectly measured by the bath and its off-diagonal coherence vanishes completely.
Figure 9. (a) Filter function t F(ωt )
d d for CPMG-100 noise spectroscopy with td = 10 ms. (b) Calculated Bi donor electron spin decoherence under an exact quantum model (solid lines) and semiclassical model obtained from noise spectroscopy of the CPMG-100 DD (dashed lines), evaluated close to the ‘clock’ transition (B + 10
CT
G). (c) Comparison of the noise spectrum from the CPMG-100 spectral decomposition in (b) to the exact one from CCE calculations. (d) similar to (b) but for the magnetic field far from the ‘clock’
transition (B + 1000
CT G). Reproduced figure with permission from [97]. Copyright 2015 by the American Physical Society.
Figure 10. Schematic illustration of the bifurcated bath evolution pathways dependent on the central spin states: (a) for FID; (b) for the central spin being flipped by a π-pulse at an intermediate time. Here, the initial state of the spin bath is assumed to be a pure state |J⟩.
Rep. Prog. Phys. 80 (2017) 016001


 Review
15
Finally, we note that upon decomposing the bath states into the unnormalized common part and the unnormalized difference part as | ( )⟩ ≡ |  ̃ ( )⟩ ± |  ̃ ( )⟩
J± t J t J t
nc c , the entangled state can be rewritten as
|Ψ(t)⟩ =|ψ⟩ ⊗ |J ̃ (t)⟩ + σˆ |ψ⟩ ⊗ |J ̃ (t)⟩,
nc z c (46)
i.e. the central spin state |ψ⟩ and the phase-flipped state σz|ψ⟩ are recorded in the unnormalized bath states |J ̃ (t)⟩
nc and |J ̃c(t)⟩,
respectively. If |J ̃c(t)⟩ is orthogonal to |J ̃ (t)⟩
nc , then the central spin density matrix would be an incoherent mixture of
⟨J ̃ (t)|J ̃ (t)⟩ |ψ⟩ ≡ Mˆ |ψ⟩
nc nc nc and ⟨J ̃ (t)|J ̃ (t)⟩ σˆ |ψ⟩ ≡ Mˆ |ψ⟩
c c z c,
which recovers our intuitive discussion for Markovian environmental noise in section 2.4.
6.2. Coherence recovery by dynamical decoupling
To recover the central spin coherence lost into the bath, it is necessary to erase the measurement information by making the two bath pathways |J±(t)⟩ identical up to a phase factor. For this purpose, the simplest approach is the Hahn echo [51], in which a π-pulse is applied to the central spin at time τ to exchange the evolution direction of the two pathways (see figure 10(b)). At t > τ, the two pathways are
( )⟩ ⟩
ˆ( ) ˆ
|= |
ττ
± − ∓− − ±
Jt e e J
iH t iH and the coupled system evolves into |Ψ( )⟩ = | ↓ ⟩ ⊗ | ( )⟩ + | ↑ ⟩ ⊗ | ( )⟩
+ +− −
t C J t C J t . The intersection of the two pathways | ( )⟩ ≈ φ| ( )⟩
+−
Jt e Jt
d i d at a certain time td would erase the measurement information and restore the central spin coherence, as shown in figure 10(b) [27–29]. Under a general DD characterized by the DD modulation function s(t), by working in the interaction picture defined by the control Hamiltonian (equation (25)), the total Hamiltonian becomes ˆ ( ) ˆ ˆ
H + s t bS
B z. The two bath pathways start from |J⟩ and bifurcate into | ( )⟩ = ˆ ( )| ⟩
±±
Jt Ut J
d d , where
ˆ ( ) [ ˆ ( )ˆ/ ]
≡∫
± −±
U t Te H s t b t
d i 2d
t 0
d B are the bifurcated bath evolution operators. Then, the central spin coherence is
( ) ⟨ ˆ ( )ˆ ( ) ⟩
†
=| |
−+
Lt JU t U t J .
d d d (47)
For example, the FID ( ) ⟨ ⟩
ˆˆ
=| |
τ− τ
−+
Lt Je e J
iH iH and the Hahn echo ( ) ⟨ ⟩
ˆˆ ˆ ˆ
=τ= | |
τ τ− τ− τ
−+ − +
Lt 2 Je e e e J
HH H H
d i i i i . For [bˆ, Hˆ ] = 0
B , as long as td satisfy the echo condition (equation (27)), we have| ( )⟩ = | ⟩
ε
±−
J t e tJ
d i J d and hence L(t ) = 1
d , i.e. the phase due to the static noise field bJ is completely refocused.
6.3. Ensemble average
In practice, we should use the thermal state ρˆB
eq (equation (33)) as the initial state of the bath; then we recover the results in section 5.2. The FID as given by equation (35) is the product of inhomogeneous dephasing due to the thermal noise (equation (7)) and ‘true’ decoherence due to the quantum noise (equation (36) or equation (45)) that is usually independent of |J⟩ [27, 97, 111]. Under DD, the former is removed,
so ( ) = ⟨ ( )| ( )⟩
−+
Lt J t J t
d d d is ‘true’ decoherence due to the quantum noise (equation (39) or equation (47)). The discussions above for a central spin-1/2 can be easily generalized to a general multi-level system with eigenstates
{|n⟩} and the pure-dephasing Hamiltonian ˆ ⟩⟨
∑ H |m m|
mm
[95, 97]. The off-diagonal coherence L (t) ≡ ⟨n|ρˆ(t)|m⟩
n,m for a given quantum transition |m⟩ ↔ |n⟩ can be mapped to that of a central spin-1/2 once the states {|m⟩, |n⟩} are identified as
{| ↑ ⟩, | ↓ ⟩} with Hˆ ≡ (Hˆ + Hˆ )/2
B m n and ˆ ˆ ˆ
b≡H −H
m n.
7. Physical systems
Electron spins localized in solid-state nanostructures are promising candidates of qubits for quantum information processing and quantum sensing. These ‘artificial atoms’ occur when the impurities or defects in semiconductor nanostructures produce localized potentials to confine one (or a few) electrons or holes (i.e. an empty electron state in the valence band of semiconductors), analogous to electrons bound to atomic nuclei. For such electron spins, the most relevant environments are the phonon bath and the nuclear spins of the host lattices. The electron spins couple indirectly to the phonon baths via spin–orbit coupling, and couples directly to the nuclear spin baths via the hyperfine interaction (HFI). In this section, we first introduce these interactions and then review central spin decoherence due to these interactions in typical semiconductor nanostructures.
7.1. Phonon and spin baths
7.1.1. Phonon scattering via spin–orbit coupling. Electric fields are not directly coupled to the electron spin ˆS. Indirect coupling occurs due to the relativistic correction
ˆ ( (ˆ) ˆ) ˆ
H = m c ∇V r × p ⋅ S
1
2
so
0
22
to the non-relativistic Hamiltonian for the electron moving in a potential V (r). Due to this spin–orbit coupling term, the electron spin eigenstates become mixtures of spin and orbital states; thus fluctuating electric fields can induce transitions between these eigenstates (i.e. spin relaxation) [112–114] and randomly modulate the transition frequency (i.e. pure dephasing) [115, 116]. In carefully designed systems (where the charge fluctuations are suppressed), the most relevant source of electrical noises is the lattice vibration (i.e. the phonon bath). The phonon energy spectrum ranges over a few tens of meV, much larger than the electron spin transition energy (∼μeV), so the phonon noise is Markovian and usually limits the electron spin T1 and, at high temperatures, also limits the electron spin T2 (see section 2). At low temperatures and in light-element materials where spin–orbit coupling is weak, phonon scattering is suppressed and the experimentally measured electron spin T1 is very long, ranging from tens of microseconds up to seconds (see [21] for a review). At low temperature, the phonon-limited electron spin T2 is estimated as T ≈ 2T
2 1 [115], but the experimentally measured T2 is much shorter as it is limited by the hyperfine interaction with the nuclear spin bath.
7.1.2. Hyperfine interaction. For a nuclear spin ˆInα of species
α located at α
Rn , its magnetic moment γαˆInα produces a vec
tor potential = (μ / π)(γ ˆ × ρ )/ρ
α αα α α
A 4I
n n nn
0
3 at the location r
Rep. Prog. Phys. 80 (2017) 016001


 Review
16
of the electron with ρ ≡ −
αα
rR
n n . The total vector potential
≡∑ α α
A n An due to all the nuclei gives rise to the electron
nuclear magnetic coupling γ ( ˆp ⋅ A + A ⋅ ˆp)/2 + γ ˆS ⋅ (∇ × A)
ee
[14], which is the sum of the contact HFI
ˆ ˆ ˆ( )
∑ρ
= μ γγ ⋅ δ
α
αα α
H IS
2
3,
n
nn
c0
e
the dipolar HFI
ˆ ( ˆ )(ˆ ) ˆ ˆ
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
∑ ρρ
μ
π γγ ρ ρ
= ⋅ ⋅ −⋅
α
α
αα α
α
α
α
H S I SI
43 ,
n
nn n
n
n
n
d0
e5 3
and the nuclear-orbital interaction
ˆ ˆˆ
∑
μ
π γγ ρ
=⋅
α
α
αα
α
H LI
4,
n
nn
n
orb 0
e3
where γ ≈ 1.76 × 10 rad /(s ⋅ T )
e
11 is the gyromagnetic ratio (positive) for free electrons and ˆ ˆ
≡ρ ×
αα
Lp
n n is the electronorbital angular momentum around the nucleus. The magnetic interaction involves the coupling of the electron orbital and electron spin to the nuclear spin. At low temperature, the localized electron in a nanostructure stays in its ground orbital ψ(r), so the magnetic interaction should be averaged over ψ(r) to yield the effective spin–spin interaction. The spin–spin contact HFI
 ̄ ⟨ ˆ ⟩ ˆˆ
∑
= ψ| |ψ = ⋅
α
αα
H H a SI,
n
c c n n (48)
where the HFI coefficient = ( μ / )γ γ |ψ( )|
α αα
a 23 R
nn
0e
2 is determined by the electron density at the site of the nucleus. The contact HFI is strong for electrons in the conduction band of III–V semiconductors (mostly s-orbital) and silicon (hybridization of s, p, and d orbitals), but vanishes in graphene, carbon nanotubes, and the valence band of III–V semiconductors since their primary component—the p-orbital—vanishes at the site of the nucleus [119]. For III–V semiconductors with a nondegenerate s-orbital conduction band minimum at the Γ point, the ground orbital can be written as ψ(r) = Ω F(r)uc(r), where Ω is the unit cell volume, F(r) is the slowly varying
envelope function normalized as ( )
∫ |F r | dr = 1
2 , and uc(r) is the s-orbital band-edge Bloch function that is conveniently
normalized as ( )
∫| | =
Ω u r dr 1
c 2 , such that ≡ | ( )|
αα
d uc Rn 2 is
the electron density on the nucleus of species α [118]. So the HFI coefficient becomes = Ω| ( )|
αα α
a A FR
n n 2, where
α = μ γ γα α
Ad
2
3
0
e (49)
is the HFI constant that only depends on the species of the nuclear spin (through γα) and the semiconductor material (through dα). The numerical values of γα and Aα for some relevant isotopes in III–V semiconductor QDs are listed in table 1. For silicon, there are six equivalent conduction band minima at = ±
kλ k0ex, ±k0ey, ±k0ez, where k ≡ 0.85(2π/a )
0 Si
and a 5.43
Si = Å is the lattice constant of silicon. Thus,
the ground orbital of a hydrogen-like donor in silicon is
ψ( ) = ( / ) ∑λ λ( ) λ( ) λ⋅
r 1 6 F r u r eik r, where ( )
λ λ⋅
u r eik r is the
Bloch function at the λth minimum consisting of s, p, and d orbitals with the normalization u r 2 dr
∫ | | =Ω
λ
Ω ( ) . The hydro
gen-like envelope function associated with ±k0ex is [76, 120]
() ( )
/( ) ( )/( )
π
= − ++
F
na nb
r 1e ,
x x nb y z na
2
2 2 22 2
with similar expressions for Fy(r) and Fz(r) by appropriate permutations of x,y,z. Here, a = 25.09 Å and b = 14.43 Å are characteristic lengths for hydrogenic impurities in silicon, n = 0.81 (0.64) for phosphorus (bismuth) donors [76, 121, 122]. The donor electron density at the silicon lattice site Rn is given by [120] |ψ | = ∑ ⋅
αα α
=
(R ) (2d /3)[ F (R ) cos(k R e )]
n xyz n n
2 Si , , 0 2,
where ≡ | ( )| ≈
λ
d u R 186
Si n 2 is the electron density on the silicon site in silicon crystal [76, 123]. The spin–spin dipolar HFI
 ̄ ⟨ˆ ⟩ ˆ ˆ
∑
= ψ| |ψ = ⋅ ⋅
α
αα
H H SA I,
n
d d n n (50)
where the dipolar HFI tensor
[ ] () ⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
∫
μ
πγγ ψ
ρ
ρρ
≡ | | ρ −δ
αα
α
αα
α
A rr
4
3d
n ij
n
n
i n
j
n
, 0 ij
e
2
32
with i,j = x, y, z. The dipolar HFI and the nuclear-orbital interaction H ̄ ≡ ⟨ψ|Hˆ |ψ⟩
orb orb are negligible for the s-orbital conduction band of III–V semiconductors. They become appreciable for donors in silicon (due to significant p- and d-orbital components in the band-edge Bloch functions) and even dominate for electrons in graphene, carbon nanotubes, and the valence band of III–V semiconductors [119, 124–127], where the atomic p-orbital is the primary component of the Bloch functions and hence the contact HFI vanishes. If ψ(r) is localized in the vicinity of r ̄ and far from the nucleus,
Table 1. Spin moment, natural abundance, gyromagnetic ratio, HFI constant, and quadrupole moment of some isotopes that appear in III-V semiconductor quantum dots (QDs), with the reduced Planck constant ħ = 1 and hence 1 μeV ≈ 1.52 ns−1.
75As 113In 115In 69Ga 71Ga
Spin moment Iα 3/2 9/2 9/2 3/2 3/2 Abundance fα 100% 4.28% 95.72% 60.1% 39.9% γα (10−3 rad ns−1T−1) 45.8 58.5 58.6 64.3 81.8 Aα (rad ns−1) 69.8 85.1 85.3 56 73 Qα (10−31 m2) 314 759 770 171 107
Note: The quadrupole moments are from [117]. Other data for In and As are from [28], while those for Ga are from [118] and [119].
Rep. Prog. Phys. 80 (2017) 016001


 Review
17
then the dipolar HFI  ̄ ⟨ ˆ ⟩ ˆ → ̄
H = ψ|H |ψ = H |r r
d d d reduces to the magnetic dipolar interaction between two point-like magnetic moments; while if ψ(r) overlaps the nucleus, then H ̄d is dominated by the interaction of the nuclear spin with the on-site electron spin density [125]. Recently the manipulation and decoherence of valence band electrons (i.e. holes) in QDs is under active study (see [128] for a review).
7.1.3. Intrinsic nuclear spin interactions. The interaction between nuclear spins has been well studied in NMR experiments and in theories (for a review, see [129]). The direct magnetic dipolar interaction has the dipolar form
ˆ ˆ ˆ (ˆ )(ˆ )
⎛
⎝⎜⎜
⎞
⎠⎟⎟
∑μ
= πγ γ ⋅ − ⋅ ⋅
αβ
αβ
αβ α β
≠
H RR
I I I RI R
1
24
3,
d
nm
nm n m NN
0
35
(51) where ≡ α − β
RR R
n m is the relative displacement between the locations α
Rn and β
Rm of the two nuclei. The indirect nuclear interaction is mediated by virtual excitation of electron–hole pairs due to the HFI between nuclei and valence electrons [130–134]. When the virtual excitation is caused by the contact HFI, the indirect coupling has the isotropic
exchange form ˆ ˆ ˆ
=− ⋅
αβ α β
H B II
nm n m
NN
ex
,
ex , where α β
Bn ,m
ex is
determined by the band structure of the material. When the virtual excitation of electron–hole pairs involves both the contact and dipolar HFI, the indirect nuclear spin coupling has the same form as the direct dipolar interaction in equation (51) except for a multiplicative factor that depends on the internuclear distance. When the virtual excitation is caused by the dipolar HFI alone, the indirect coupling is the sum of an isotropic exchange term and dipole–dipole term. Except for the direct dipolar coupling, experimental characterization of indirect couplings is very limited. Due to the vanishing electric dipole moment of the nucleus, the nuclear spin is not coupled to constant electric fields. However, a nucleus with spin I > 1/2 has a finite electric quadrupole moment, so a nuclear spin ˆI located at R with quadrupole moment Q is coupled to the on-site electric field gradient tensor ≡ ∂ ( )/∂ ∂ | =
V Vx x x
ij i j x R
2 through ˆ ˆ
=∑ =
H VQ
Q ij x y z ij ij
,, ,
where [14]
ˆ ( ) (ˆˆ ˆ ˆ) ( )
⎡
⎣⎢ ⎤
⎦⎥
Q ≡ eQ− + − δ +
I I II II I I
62 1
3
21
ij i j j i ij
is the nuclear spin quadrupole tensor. In the principal axis OXYZ of the electric field gradient tensor, only diagonal components V , V , V
XX YY ZZ survive. Using the non-axial parameter η ≡ (V − V )/V
XX YY XX and Laplace equation V + V + V = 0
XX YY ZZ allows the quadrupolar interaction to be simplified to [14]
Hˆ = e(QV− ) [ ˆ − ( + ) + η( ˆ − ˆ )]
I I I II I I
42 1 3 1 .
Q
ZZ Z XY
2 22
The quadrupole moments of some relevant isotopes in III–V QDs are listed in table 1. In a crystal with cubic symmetry, the electric field gradient tensor obeys V = V = V
XX YY ZZ, which together with the
Laplace equation dictates vanishing electric field gradient and quadrupolar interaction. Nonzero quadrupolar interaction could arise from broken cubic symmetry by lattice distortion due to semiconductor heterostructure, dopants, or defects. The quadrupolar interactions have important effects on the nuclear spin dynamics [14] and hence the auto-correlations of the noises on a central electron spin coupled to the nuclear spin bath [135]. Recently Chekhovich et al measured [136] straininduced quadrupolar interactions in self-assembled QDs and found that they suppress the nuclear spin flip-flops [137], while in gate-defined GaAs QDs, the quadrupolar interaction was found to reduce the electron spin coherence time by causing faster decorrelation of the nuclear spin noise [138].
7.2. Electron spin decoherence in solid-state nano-systems
The widely studied systems include semiconductor QDs [139–141], phosphorus and bismuth donors in silicon [82, 142, 143], and nitrogen-vacancy (NV) centers in diamond [144, 145]. In these systems, electron or hole spins act as qubits. At low temperatures, the spin-phonon scattering processes are largely suppressed [112, 113, 115, 146], so the main noise source for electron spin qubits in these systems are the nuclear spin baths of the host lattice. As a convention, we use T∗2 for the dephasing time in FID (since FID is usually dominated by inhomogeneous dephasing), and use T2 for the dephasing time under various DD controls, where inhomogeneous dephasing has been removed.
7.2.1. Semiconductor quantum dots. Electron spins in QDs are among the earliest candidates for quantum computing [140, 147]. A QD is a semiconductor nanostructure with size ranging from a few to hundreds of nanometers. The electrons in QDs experience quantum confinement in all three spatial dimensions, with their energies, wave functions, and hence spin properties tunable by the QD size and shape [21, 148, 149]. There are different ways to fabricate QDs, e.g. gatedefined QDs [148] confine electrons by an electrostatic potential from electric voltages on lithographically defined metallic gates (figure 11(a)), while self-assembled QDs [150] confine electrons with a deep potential that is created during the random semiconductor growth process (figure 11(b)). There are also QDs formed by interface fluctuation in GaAs/AlGaAs quantum well structures [151]. The weakly confined electrons in gate-defined QDs can be controlled electrically at very low temperatures (<1 K), and strongly confined electrons in selfassembled QDs and interface fluctuation QDs can be controlled optically at slightly higher temperatures (∼4 K). A critical issue for electron spin qubits in III–V semiconductor QDs is the inevitable presence of nuclear spins in the semiconductor substrate since all stable isotopes of the III–V semiconductors have nonzero nuclear spins [152, 153]. The thermal noise (see sections 5.1 and 6.3) from the nuclear spin bath leads to rapid inhomogeneous dephasing of the electron spin on a timescale T∗ ∼ 10
2 ns [21]. When this inhomogeneous dephasing is removed by the Hahn echo, the quantum dynamical noise from the nuclear spin bath still limits the electron spin
Rep. Prog. Phys. 80 (2017) 016001


 Review
18
dephasing time T2 to a few microseconds [21]. Fortunately, the nuclear spin noise has a rather long auto-correlation time τc ∼1 ms (∼the inverse of nuclear spin interactions, see table 2)6, so it can be significantly suppressed by various DD sequences, e.g. the multi-pulse CPMG has extended the T2 of a singlet-triplet qubit in gate-defined GaAs double QDs from ∼1 μs [154–156] to ∼1 ms [157, 158]. Recently, silicon-based QDs have been developed, such as QDs in Si/SiGe heterostructures and gated nanowires (see [22] for a review). As the only silicon isotope 29Si that has non-zero spin is of low natural abundance (4.7%), the measured electron spin T∗ ≈ 360
2 ns in Si/SiGe double QDs [159] is longer than in GaAs QDs by more than one order of magnitude, and further improvements are expected for devices using isotopically enriched 28Si.
7.2.2. Donors in silicon and related materials. As the dominant material in the semiconductor industry, silicon provides a platform to accommodate both quantum and classical information technologies. Electron and nuclear spins of individual donors in silicon have been proposed as qubits ever since the early years of solid-state quantum information [142]. After Kane’s influential proposal, different architectures have been proposed in which electron spin [160] and orbital [161, 162], nuclear spin [22], an electron and its donor nuclear spin [163] are used as qubits. Silicon has three stable isotopes: 28Si (natural abundance 92.2%), 29Si (natural abundance 4.7%), and 30Si (natural
abundance 3.1%), among which only 29Si has a nonzero nuclear spin I = 1/2, in sharp contrast to III–V group semiconductors where all isotopes have nonzero nuclear spins. The low concentration of spinful nuclear isotopes and weak spin–orbit coupling in silicon results in long electron spin coherence times compared to that of spin qubits in III–V group semiconductor QDs. For high-mobility two-dimensional electron systems, their T1 and T2 reach a few microseconds at low temperature [164], limited by phonon scattering via spin–orbit coupling. When the electron spin is tightly bound to a donor, the spin–orbit coupling is further suppressed, so at low temperatures its T1 can reach minutes to hours [165], while its T2 is usually limited by T1 process at high temperature, or by other donor electron spins and the sparse 29Si nuclear spin bath at low temperature [73]. Among all the group-V dopants in silicon, phosphorus donors in natural silicon (natSi:P) or isotopically purified 28Si (28Si:P) have been widely studied. Phosphorus has only one stable isotope 31P with nuclear spin I = 1/2 (figure 12(a)). The P donor electron spins were exhaustively studied almost sixty years ago in the first electron-nuclear double resonance experiment [120]. At low donor concentrations, the electron T1 increases dramatically with decreasing temperature, reaching thousands of seconds at low temperature ∼1 K [42, 79, 165, 166], while the 31P nuclear spin relaxation time exceeds 10 h [120]. At low temperature, the extrapolated T2 of an isolated 28P donor electron spin from spin-echo measurements can reach 60 ms [79], comparable with T1 ∼280 ms. In a natSi:P system, T2 of the P donor electron spin under spin-echo control is limited by the 29Si nuclear spin bath to ∼1 ms [79]. Recently, unprecedented long electron spin T ≈ 12
2 s [167] and nuclear spin dephasing time up to a few minutes were reported in ultrapure 28Si crystals [102, 168, 169]. Due to its exceptional long relaxation and dephasing times, the 31P nuclear spin is a good candidate as long-lived quantum memory or combined with the donor electron spin into a hybrid quantum register (figure 12(a)) [163]. Recently, bismuth donors in silicon (Si:Bi) have attracted much attention as they have a number of advantages over the P donors in silicon. Bismuth has one long-lived isotope 209Bi with nuclear spin I = 9/2 (figure 12(b)). Compared with the Si:P system, the Bi donors in silicon have a much larger nuclear spin I = 9/2 and a much stronger on-site HFI A = 1.4754 GHz [120] between the Bi electron spin and the 209Bi nuclear spin. The much stronger on-site HFI in Si:Bi strongly mixes the electron and the nuclear spin even under moderate magnetic field. This enables an electron-nuclear hybrid qubit, where each level consists of nearly equal superpositions of the electronic and Bi nuclear spin components [170]. Consequently, the strong magnetic dipolar interaction between the electron spin and the microwave magnetic field can induce rapid NMR transitions on the nanosecond timescale, two orders of magnitude faster than conventional NMR [143, 171] and several orders of magnitude faster than the decoherence of the hybrid qubit T ∼ 0.5
2 ms, limited by 29Si nuclear spins. By tuning the magnetic field to the ‘clock’ transition between hybridized levels, whose frequency is insensitive to variations in the magnetic field to first order, an electron spin coherence time T2 of up to 3 s has been observed [107].
Figure 11. (a) A gate-defined double quantum dot, with 2DEG for two-dimensional electron gas. (b) A self-assembled quantum dot. Scale bar ∼5 nm. Reproduced by permission from Macmillan Publishers Ltd: [20]. Copyright 2008.
Table 2. Characteristic energy scales in an InAs QD with dimensions 35 × 35 × 6 nm3 under a magnetic field of 1 T [28], with ħ = 1.
μs−1 μeV mK
Electron Zeeman splitting 105 102 103 Nuclear Zeeman splitting 50 0.05 0.5 Hyperfine interaction 1 10−3 10−2 N-N dipolar interaction 10−4 10−7 10−6
6 Here, the nuclear spin noise refers to the nuclear Overhauser field (i.e. ˆˆ
≡∑ α α α
h aI
n n n in equation (48) and ˆ ˆ
≡∑ ⋅
αα α
h AI
n n n in equation (50)). In a moderate to strong magnetic field, the electron spin decoherence is usually caused by the fluctuation of the longitudinal component hˆz along the external
magnetic field. The auto-correlation time of hˆz is determined by the nuclear spin interactions as τc ∼1 ms, while that of the transverse components hˆx,hˆy could be much shorter, since not only nuclear spin interactions, but also the spread of Larmor precession frequencies of different nuclei contribute to their decorrelation. Also, note that when the nuclear spins are polarized, it will take a much longer time (from seconds to hours) for the average value of hˆz to relax to its thermal equilibrium value.
Rep. Prog. Phys. 80 (2017) 016001


 Review
19
7.2.3. Nitrogen-vacancy centers in diamond and related systems. The negatively charged NV center in diamond consists of a substitutional nitrogen atom adjacent to a carbon vacancy, which has C3v symmetry with the symmetry axis pointing from the nitrogen to the vacancy (NV axis) (figure 13(a)). The ground state of the NV center 3A2 is a spin triplet (S = 1) with the degenerate m = ± 1 doublet states energetically higher than the m = 0 sublevel by the zero-field splitting D = 2.87
gs GHz (figure 13(b)), where m is the spin projection along the N-V symmetry axis. Since Gruber et al observed the magnetic resonance of individual NV centers by optical confocal microscopy at room temperature [144], NV centers have been intensively studied for quantum information processing [172–175] and quantum sensing [18, 176–180]. The high Debye temperature of the diamond crystal, the weak spin–orbit coupling, and low abundance (≈1.1%) of
spinful 13C isotopes (I = 1/2) allow very long spin-coherence time of the NV center ground state. The NV electron spin T1 can reach a few milliseconds at room temperature (even as long as minutes at low temperature) [181, 182]. The NV electron spin T2 is usually limited by its coupling to other electron spins and the 13C nuclear spins in diamond. In type-Ib diamond samples, the main paramagnetic centers are nitrogen donors with one unpaired electron spin (the P1 centers). For typical P1 concentration (∼102 ppm), these P1 centers limit the NV electron spin T∗ ∼ 0.1
2 μs for FID [71, 103]. In high-purity type-IIa diamond samples, the NV electron spin T∗2 is limited by HFI with the 13C nuclear spin bath to a few microseconds [52, 172, 183–185]. When the concentration of
the 13C isotope is reduced by isotropic purification, the room temperature T2 can reach a few milliseconds [181, 186, 187], limited by T1. Although most of the distant 13C nuclei weakly coupled to the NV electron spin serve as a detrimental source of noise that limits the NV electron spin T2, the on-site nitrogen atomic nucleus and a few proximal 13C nuclei strongly coupled to the NV center electron spin [185] have exceptional long coherence times (exceeding one second) and can be individually addressed and manipulated through their HFI with the NV electron spin [43, 172, 174, 188]. These nuclear spins serve as a beneficial quantum memory.
The NV center in diamond possesses two distinguishing features compared with other solid state qubit systems: (i) highly localized electronic states well isolated from sources of decoherence, leading to millisecond spin-coherence time at room temperature; (ii) a series of optical transitions that allow highfidelity optical initialization and readout of the NV electron spin state under ambient conditions. These exceptional quantum properties have motivated efforts to search for similar defects in other semiconductors [189], as they may offer an expanded range of functionality. First-principle computations and magnetic resonance experiments [189–194] suggest several defects in SiC as good candidates, such as Si-C divacancy [192, 195], Si and carbon vacancies [190, 194, 196, 197], and TV2a center [191]. In particular, the three most common SiC polytypes (3CSiC, 4H-SiC, and 6H-SiC) all host optically addressable defect spin states with long coherence time ∼ a few tens of microseconds at room temperature [198], e.g. T∗ ∼ 1
2 μs and T2 ∼ a few hundred microseconds in 4H-SiC [195]. In addition, rareearth-doped crystals and silicon-vacancy centers in diamond are receiving increasing interest. A long coherence time T2 = 2ms close to the measured T1 = 4.5ms has been reported for the electron spin of a single Ce3+ ion in yttrium aluminum garnet (YAG) crystal [199]. For electron spins in silicon-vacancy centers in SiC, T∗ > 45
2 ns and T1 = 2.4ms have been reported [200, 201].
Figure 12. Energy levels of phosphorus and bismuth donors in silicon. (a) P donor electron spin-1/2 couples to the 31P nuclear spin-1/2 via a moderate HFI of strength A = 117.5 MHz. (b) Bi donor electron spin-1/2 couples to the 209Bi nuclear spin-9/2 via strong HFI with a strength A = 1.745 GHz. Panel (a) reproduced with permission from [82]. Copyright 2006. Panel (b) reproduced by permission from Macmillan Publishers Ltd: [107], copyright 2013.
Figure 13. (a) Structure of an NV defect center in the diamond lattice. (b) Energy levels of an NV center in diamond: green, upward arrow for off-resonant optical transitions, red, downward arrow for fluorescence, and dashed arrows for non-radiative, spinflip decay. Panel (a) is reproduced by permission from Macmillan Publishers Ltd: [187], copyright 2009. Panel (b) is reproduced by permission from Macmillan Publishers Ltd: [177]. Copyright 2008.
Rep. Prog. Phys. 80 (2017) 016001


 Review
20
8. Microscopic quantum many-body theories
In previous sections, we have described the central spin decoherence in a quantum bath using a generic pure dephasing Hamiltonian (equation (43)). In this section, we focus on the most relevant issue in quantum computing: the decoherence of a central electron spin in a nanoscale nuclear spin bath in semiconductor nanostructures, such as quantum dots, donors in silicon, and diamond NV centers. First we give the microscopic Hamiltonian relevant for these systems.
8.1. Microscopic model
Under moderate to strong external magnetic field (whose axis is defined as the z axis), the non-secular terms of the HFI between the electron spin and various intrinsic nuclear spin interactions (as discussed in section 7.1.3) are suppressed.
The total Hamiltonian includes the electron Zeeman term
ˆˆ
H ≡ω S
0 0 z, the nuclear Zeeman term (for simplicity, we consider one nuclear spin species with spin I and gyromagnetic ratio γI)
∑∑
≡−γ ≡ω
ˆ ˆˆ
H B I I,
ZI
j
j
z I j
j
z
the secular part ˆ ˆ ˆ ˆ
S ∑ a I ≡Sh
i ii
z
z z z of the HFI (ai is the HFI coefficient and hˆz is widely known as the nuclear Overhauser field), the diagonal part
ˆ ˆˆ
≡ ∑λ
≠
H II
1
2i j
ij i
z j
z
d d (52)
and pair-wise flip-flops part
ˆ ˆˆ
≡∑λ
≠
+−
H II
ij
ij i j
ff ff
(53)
of intrinsic nuclear spin interactions, and electron-mediated nuclear spin flip-flop term ˆ  ̃
2SzHff, where [27–29, 38]
∑∑
= +ω ≈ ω ≡ λ
≠
+−
≠
+−
 ̃ ˆ ˆ ˆˆ  ̃ˆˆ
H h h aa I I I I
44 ,
xy
ij
ij ij ij
ij i j
ff
22
00
ff (54)
hˆx, hˆy are the transverse parts of ˆ ˆ
h≡∑ aI
i i i and in the approx
imation we have neglected a small correction ∼ ∑i ai /ω
2 0 to
the electron Zeeman splitting. In the interaction picture with respect to ˆ ˆ
H0 + HZ, the total Hamiltonian assumes the standard pure dephasing form (equation (43)), where [27–29]
=+± +
Hˆ± Hˆ Hˆ ( H ̃ hˆ )
1
22
d ff ff z (55a)
∑ ∑∑
=± + λ + λ ±λ
≠≠
+−
ˆ ˆ ˆ (  ̃ )ˆ ˆ
aI II I I
2
1
2.
j
j j
z
ij
ij i
z j
z
ij
ij ij i j
d ff ff
(55b)
This corresponds to ˆ ˆ ˆ
H ≡H +H
B d ff and ˆ  ̃ ˆ
b ≡ 2Hff + hz. As listed in table 2, the HFI {ai} are much larger than various nuclear
spin interactions  ̃
λ ,λ ,λ
ij ij ij
d ff ff. Also, note that the intrinsic nuclear
spin interactions λij, λij
d ff are local, i.e. negligible between distant
nuclear spins, while the electron-mediated nuclear spin interactions λ ̃ij
ff are non-local. The initial state of the nuclear spin bath is the thermal state
ˆˆ
ρ ∝I
B
eq (equation (33)), which is maximally mixed even at very low temperature (e.g. a few Kelvins) due to the small nuclear Zeeman splitting. Choosing a different initial state of the bath will change the thermal noise and hence inhomogeneous dephasing, but usually does not influence the ‘true’ decoherence due to the quantum noise. For ‘true’ decoherence, sometimes we may take the initial state of the bath as a pure product state
|J⟩ = ⊗j |mj⟩ (56)
of the Zeeman eigenstate of each bath spin (Iˆ |m 〉 = m |m 〉)
j
z
j j j.
The central spin decoherence can be written as an integral over the contour C: 0 → t → 0
d:
() ⟨ ⟩
ˆ( )
∫
=−
Lt T e ,
Hz z dC
id
C (57)
where ⟨⟩ ≡ ⟨J||J⟩ for a pure initial state or 〈〉 ≡
Tr[ρˆB ()]
eq for a thermal initial state,
ˆ( ) ( )ˆ ( )ˆ ˆ ( )ˆ ˆ
∑ ∑∑
=ω + λ +λ
≠≠
+−
Hz zI zII zI I
1
2
j
jj
z
ij
ij i
z j
z
ij
ij i j
d ff (58)
is the bath Hamiltonian on the contour, ω (z) ≡ a s(z)/2
j j,
( ) ( ) ̃
λ z ≡λ +s z λ
ij ij ij
ff ff ff, λij(z) ≡ λij
d d, and s(z) is the DD modula
tion function on the contour C: it starts from +1 and switches its sign whenever the central spin is flipped or at td. FID corresponds to s(z) ≡ +1 on the upper branch and s(z) ≡ −1 on the lower branch. Some examples of s(z) are shown in figure 14. For an arbitrary function ( ) ≡ + ( )
f z f t (z ∈ upper branch) or f−(t) (z ∈ lower branch), the contour integral is defined as
() () ()
∫∫ ∫
≡+
+−
f z dz f t dt f t dt
t
C0 t
0
d
d
.
8.2. Noises from spin bath dynamics: general considerations
The central spin decoherence is the product of inhomogeneous dephasing due to the thermal noise and ‘true’ decoherence due to the quantum noise (see section 5.2). The former usually dominates the FID, but is completely removed by any DD at the echo time, so only the quantum noise, which is usually independent of the initial state of the bath, contributes to central spin decoherence under DD.
8.2.1. Thermal noise. On the timescale of inhomogeneous dephasing, nuclear spin interactions Hˆd, Hˆff, H ̃ff can be
neglected and ( ) ⟨ ˆ ⟩
≡−
L t e ihzt . For a sufficiently large number of nuclear spins, hˆz as the sum of many independent random
Figure 14. Contour modulation function for different DD sequences: (a) FID, (b) Hahn echo, and (c) CPMG-2.
Rep. Prog. Phys. 80 (2017) 016001


 Review
21
variables obeys the Gaussian statistics. This gives the Gaussian inhomogeneous dephasing (see equation (9))
( ) ( ) / /( )
=≡
− −∗
Lt e e
ht tT
inh 2
rms 2 2 2 2 (59)
on a timescale
T∗ = h
2
2
rms
with
⟨ˆ ⟩ ( ) ∑
≡ =+
h h II a
1
3,
i
rms i
2 z
22
which is insensitive to the specific distribution of {ai}. From table 1, the typical inhomogeneous dephasing time is estimated as T∗2 ∼ a few nanoseconds for a QD containing
N ∼ 104–106 nuclei [27–29].
8.2.2. Quantum noises from nuclear spin clusters. Quantum noises are determined by the quantum fluctuations of the baths. According to equation (55), the elementary excitations of the bath are flip-flops of bath spin pairs. On a short timescale, the flip-flops of different pairs are nearly independent. On a longer timescale, the successive flip-flop of different pairs involving a common bath spin generates correlated fluctuation of larger and larger clusters. When central spin decoherence time is relatively long (e.g. for a small 13C nuclear spin bath in diamond NV centers), or when the correlated fluctuation of small clusters are reduced by DD control, the correlated fluctuations of larger clusters become important. In recent years, microscopic quantum many-body theories have been developed to quantitatively describe the correlated fluctuations of nuclear spin clusters and the induced electron spin decoherence in nanoscale nuclear spin baths. The paircorrelation approximation [27–29] and density matrix cluster expansion [30, 31] are the first two quantum many-body theories, which have been independently developed and are equivalent in the leading order. The former treated the flipflop of different pairs as independent and provides a transparent physical picture for central spin decoherence, but neglects the correlated fluctuation of larger clusters. The latter provides a convenient way to include the leading-order effect of correlated fluctuation of larger clusters, but may not converge to the exact results for relatively small baths. The subsequent theory, the ‘linked-cluster expansion’ (LCE) [32], accurately accounts for the fluctuations due to successively higher-order interactions among the nuclear spins through Feynman diagrams of successively higher order, but becomes increasingly inefficient at higher orders and may not converge for a relatively small spin bath. When each nuclear spin is coupled to all the other nuclear spins (see equation (54) for an example), a large-N expansion (N is the number of nuclear spins) of LCE is possible (so-called ring diagram approximation [37, 38, 203]), which turns out to be equivalent to the semi-classical noise model [157, 204]. For a simple and accurate account of the correlated fluctuation of large clusters, the CCE has been developed [108, 202], which covers the validity ranges of previous theories, produces the exact results even for relatively
small baths, and has successfully predicted and explained a series of experimental results for various solid-state systems. In the following sections, we will review these many-body theories. First we introduce the LCE, which accounts for various fluctuation processes through Feynman diagrams. Then, we introduce the ring diagram approximation as a partial summation of an infinite number of certain Feynman diagrams. Next, CCE is introduced as an expansion method corresponding to an infinite summation of all the Feynman diagrams. Finally, we will give a conceptual understanding of CCE as a systematic method to treat the correlated fluctuation of larger spin clusters in a canonical quantum spin system (while the cluster expansion and disjoint cluster approximation [35, 36] can be regarded as certain approximations to the CCE), thus it can be used to calculate not only central spin decoherence, but also other quantities such as the quantum noise spectrum of the spin bath. Before discussing the different many-body theories, we emphasize that in cluster expansion and CCE the term ‘cluster’ refers to a group of physical bath spins, e.g. a three-spin cluster contains three different bath spins. The ‘linked-cluster expansion’ (LCE) is a diagrammatic expansion with respect to the number of interaction lines in a Feynman diagram, e.g. a third-order Feynman diagram contains three interaction lines, but does not necessarily contain three different bath spins. By contrast, the CCE theory and the cluster expansion theory are expansions with respect to the number of bath spins, e.g. a three-spin cluster contains three different bath spins. Nevertheless, there is a close connection between the number of bath spins contained in a cluster and the order of Feynman diagrams. This allows us to establish a connection between the CCE and the LCE (to be discussed shortly).
8.3. Linked-cluster expansion
Linked-cluster expansion (LCE) is a standard many-body technique to evaluate the average of a general time-ordered exponential, as defined by its Taylor expansion:
〈 〉 ( ) 〈 [ ˆ( ) ˆ( )]〉
ˆ( )  
∫∫
∑
∫ ≡−
−
=
∞
TT
i
e n ! dz dz O z O z ,
Oz z
n
n
C nn
id 0 C1 C C 1
C
(60)
where the average 〈〉 is carried out over a non-interacting
ensemble of bosons, fermions, or spin systems [32], and Oˆ(z) consists of bosonic (or fermionic) field operators or spin operators in the interaction picture. An example is the contour Hamiltonian in equation (58), where the spin operators in the interaction picture are ˆ ( ) ˆ
I z ≡I
i
z i
z and ˆ ( ) ˆ
≡
±±
Iz I
i i.
LCE dictates that the expansion in equation (60) can be reduced to an exponential function of linked diagrams—hence
the name LCE. When Oˆ(z) = φ ̃ is a classical Gaussian ran
dom variable or when ˆ( ) ( ˆ ˆ† )
O z =∑ α c +β c
m m m m m is a bosonic
field operator, there is only one linked diagram correspond
ing to (−1/2)⟨φ ̃2⟩ or (−1/2)⟨Oˆ 2⟩, so LCE reduces to equations (12) or (40). Here, we introduce the LCE for spin baths relevant for central spin decoherence in nuclear spin baths, thus the average Tr NI
〈〉 ≡ [ρˆ ()] refers to a non-interacting spin bath state
Rep. Prog. Phys. 80 (2017) 016001


 Review
22
ˆ
ˆˆ
ˆ
ˆ
∑
ρ
ω
=
=
β
β
−
−
HI
e
Tre
,
.
H
H
i
ii
z
NI
NI
NI
NI
The spin operators in the interaction picture are taken to be:
Iz e I
i i iz i
=ε
± ±±
ˆ ( ) ˆ and I z I
i
z i
z
=
ˆ ( ) ˆ , where in general εi could be different from ωi.
8.3.1. LCE for spin baths. The first key ingredient of LCE
for a spin bath is the concept of contraction [205], defined
between a spin raising operator ˆ ( )
I i+ z1 and an arbitrary spin
operator ˆ ( )
I jα z2 in the interaction picture:
Iz Iz Iz Iz
G z ,z e I ,I z .
ji i j
ij i z z j i
2• 1• 1• 2•
, 21i 2
i1 2
δ
≡
≡
αα
εα
++
−+
[ ˆ ( )] [ ˆ ( )] [ ˆ ( )] [ ˆ ( )]
( ) [ ˆ ˆ ]( )
( ) (61)
where z is the time on the contour C, G (z , z ) = θ(z − z )
i21 2 1
[1 + n(ωi)] + θ(z1 − z2)n(ωi) is the contour Green’s function, θ(z) is the Heaviside step function on the contour, and ω≡ −
βω
n( ) 1/(e 1) is the Bose–Einstein distribution function. The contraction can be visualized by Feynman diagrams as sketched in figure 15(a). The contraction of ˆ ( )
I i+ z1 and ˆ ( )
I iα z2 is represented by an arrow going from ˆ ( )
I i+ z1 to ˆ ( )
I iα z2 : the arrow itself represents ( )
e ε ( − )G z , z
zz i
i 21
i 1 2 , while the commu
tator [ ˆ ˆ ]( )
α α
I i+, I i z is to be taken at the end of the arrow. Since
[ˆ ˆ ] ˆ
=
++
Iz, I I and [ ˆ ˆ ] ˆ
=−
−+
I , I 2Iz, the contraction of ˆ ( )
I i+ z1 and
Iˆi (z )
z
2 [or ˆ ( )
I i− z2 ] eliminates ˆ ( )
I i+ z1 and converts Iˆi (z )
z
2 [or ˆ ( )
I i− z2 ]
to ˆ ( )
I i+ z2 [or−2Iˆi (z )
z
2 ], reducing the number of spin operators by one. Note that the contraction of spin operators is quite different from the contraction of bosonic or fermionic field operators: the latter is just a c-number, while the former is still a spin operator that should be used in subsequent contractions. For example, as
shown in figure 15(b1), the contraction of ˆ ( )
I i+ z1 and Iˆi (z )
z
2 pro
duces ˆ ( )
I i+ z2 , which in turn contracts with ˆ ( )
I i− z3 and produces
(−2)Iˆi (z )
z
3 . Another example is shown in figure 15(b2): the contraction of ˆ ( )
I i+ z1 (or ˆ ( )
I i+ z2 ) and ˆ ( )
I i− z3 produces (−2)Iˆi (z )
z
3,
then Iˆi (z )
z
3 contracts with ˆ ( )
I i+ z2 [or ˆ ( )
I i+ z1 ] to produce ˆ ( )
I i+ z3 ,
which in turn contracts with ˆ ( )
I i− z4 to produce (−2)Iˆi (z )
z
4 . Here,
the order of the contraction does not change the result. The second key ingredient is Wick’s theorem for spin operators [32, 108, 205–207]. Let us consider an arbitrary contour time-ordered product of spin operators in the interaction picture (spin operators commute inside the TC product)
⟨ [ ˆ ( ) ˆ ( )]⟩ = { ρˆ [ ˆ ( ) ˆ ( )]}
αγ αγ
T I z  I z Tr T I z  I z .
C i 1 k n NI C i 1 k n (62)
Wick’s theorem states that the contour time-ordered product of spin operators TC[] in equation (62) can be replaced by the sum of all possible fully contracted products containing only Iˆz operators. If TC[] contains different numbers of Iˆ+ and Iˆ− operators, then equation (62) vanishes. For example, the diagram in figure 15(a1) vanishes since it only contains one Iˆ+ operator, but no Iˆ− operator, while all the other diagrams in figure 15 containing equal numbers of Iˆ+and Iˆ−operators are fully
contracted products. As another example, [ ˆ ( ) ˆ ( ) ˆ ( )]
+−
T I zI z I z
ii
z i
C 12 3
has two possible fully contracted products: a connected diagram
([ ˆ ( )] [ ˆ ( )] ) ( ˆ ( ))
+−

I z Iz I z
ii
z i
1 • 2 • 3 (figure 15(b1)) and a disconnected
diagram [ ˆ ( )] [ ˆ ( )] × ˆ ( )
+−
I z I z Iz
ii i
z
1 • 3 • (figure 15(b3)). By applying Wick’s theorem to each TC product, equation (60) can be decomposed as the sum of fully contracted products or equivalently diagrams, including connected ones and disconnected ones. The LCE theorem states that all these diagrams can be resummed into an exponential form [208]:
∫ =π
−
〈T 〉 〈 〉
ˆ( ) ˆ
e e,
Oz z C
id
C (63)
where πˆ represents the sum of all the connected diagrams contained in equation (60). Taking the contour bath Hamiltonian in equation (58) as an example, all the topologically inequivalent connected diagrams up to the fourth order of the bath interactions are shown in figure 16. For a spin-1/2 bath, the average J  J over a pure product state |J⟩ (equation (56)) (an eigenstate of HˆNI) can be taken as the average over a zero-temperature ensem
ble [Tr ρˆNI ], with ω < 0
i (or >0) for mi = ↑ (or ↓ ). Therefore, the ‘true’ decoherence caused by a bath in the pure state |J⟩ can be written as [32, 108, 207]:
() ⟨ ⟩
ˆ( )
∫
= | | =π
−
Lt JT e J e,
Hz z dC
id
C (64)
where
⟨ˆ⟩ ⟨ ⟩
ˆ( )
∫
π ≡ |π| = | |
−
J J JT e Hz zJ
C
id connected
C (65)
is the sum of all connected Feynman diagrams contained in
⟨⟩
ˆ( )
||
−∫
JT e Hz zJ
Ci d
C . Here, each constituent diagram of π is a c-number, obtained from the constituent diagram of πˆ by replacing Iˆi
z with ⟨J|Iˆ |J⟩ = m
i
z
i. When bath spins are higher than 1/2, the average J  J over a pure product state |J⟩ (equation (56)) can still be taken as a zero-temperature ensemble Tr[ρˆNI ] as long as each bath spin is mapped to a composite of pseudo-spin-1/2s [108]. The LCE has been applied to the phosphorus donor electron spin in a 29Si nuclear spin bath [32, 207]. The connected
Figure 15. Diagrammatic representation of the contraction of (a) two and (b) three spin operators. The spin operators Iˆ+, Iˆ−, and Iˆz correspond to a filled circle, an empty circle, and an empty square.
Rep. Prog. Phys. 80 (2017) 016001


 Review
23
Feynman diagrams have been evaluated up to the fourth order of the bath interactions. The results agree reasonably with the experimental data [82]. The FID is dominated by the leadingorder flip-flop process of nuclear spin pairs (the third diagram in figure 16). Under higher-order DD, it is necessary to take higher-order diagrams into account, but the tedious diagram counting and evaluation make it difficult to go to very high orders.
8.3.2. Ring diagram approximation. The difficulty in counting and evaluating higher-order Feynman diagrams in LCE could be greatly simplified under a relatively weak magnetic field [37, 38, 203], where the electron-mediated nuclear spin
interactions λ ̃ij
ff dominate over the intrinsic interactions λij
ff and
λij
d. In this case λij
ff and λij
d in equation (58) can be dropped, the total Hamiltonian becomes ˆ ˆ ˆ
H = Szb with ˆ ˆ  ̃
b ≡ h + 2H
z ff
(equation (54)), and the decoherence L t e b s t t
d id
t 0
d
=∫
−
() 〈 〉
ˆ ()
(see equation (57)) is completely removed by any DD at the echo time (in this case decoherence comes from the flip-flop between nuclei of different species [37, 38, 203]). The ‘true’ decoherence due to quantum noises in FID [37, 38, 203],
∫∫
=| |=| |≈
−− −
′′ ′′
( ) 〈 〉 〈 T 〉 〈T 〉
ˆ  ̃()  ̃()
L t Je J J e J e
bt H t t H t t
dyn i 2i d 2i d
tt 0 ff 0 ff
is described by the simplified ‘contour’ Hamiltonian
 ̃ ()  ̃ ˆ ˆ ( )/
= ∑λ
≠
+− −
H t IIe .
ij
ij i j a a t
ff
ff i 2
ij
Thus, all the Feynman diagrams (figure 16) involving λij(z)
d
and ωj(z) vanish. Since each nuclear spin couples to all the other nuclear spins with comparable strength, the value of a Feynman diagram involving m different nuclear spins is of the order O(Nm) with N being the number of nuclear spins. This enables a leading-order expansion with respect to 1/N [32, 37, 38, 203]: among all the Feynman diagrams containing
the same number of interaction lines, it suffices to keep only those diagrams involving the maximal number of nuclear
spins, i.e. all the ring diagrams contained in ∫
− ′′
〈T 〉
 ̃()
e 2i H t dt
t 0 ff
(figure 17).This is the ring diagram approximation [37, 38, 203]. For t  inverse HFI, it gives a power-law decay7
() /
≈+
L t tT
1
1i ,
dyn dyn
(66)
which is insensitive to the specific distribution of the HFI coefficients {ai}, on a timescale
ω
T ≡h .
dyn
0
rms
2 (67)
For t  Tdyn, the denominator 1 + it /T ≈ it /T
dyn dyn gives rise to a π/2 phase shift of the electron Larmor precession. Powerlaw behavior and a long-time π/4 phase shift has also been observed in the single-spin Rabi oscillation decay [103, 209]. For long times t  inverse HFI, it gives an exponential decay [28, 210] on a timescale that depends sensitively on the distribution of {ai}. The relevance of the power-law decay and the exponential decay depends on the magnetic field. For weak fields such that Tdyn  inverse HFI, most of the coherence decay follows the short-time power-law behavior in equation (66). By contrast, in the opposite limit Tdyn  inverse HFI, most of the coherence decays exponentially. Under spin echo, the calculated decoherence under weak magnetic fields agrees with the experiment in gated GaAs QDs [156]. At slightly stronger magnetic fields, characteristic oscillations with frequencies equal to the differences of the nuclear Zeeman frequencies of different nuclear species are predicted [37, 38] and subsequently observed experimentally [157]. Essentially, the ring diagram approximation assumes that all the spin operators in H ̃ff(z) commute with each other
Figure 16. Topologically inequivalent connected diagrams up to the fourth order for the Hamiltonian in equation (58). Here, dotted lines connected to a single empty square denote ωj(z), dotted lines connected to two empty squares denote λij(z)
d , and wavy lines denote λij (z)
ff , e.g. the first (second) diagram represents the first (second) term of Hˆ (z). Reproduced with permission from [108]. Copyright 2008 by the American Physical Society.
Figure 17. Ring diagrams containing up to (a) two, (b) three, and (c) four nuclear spins.
7 Here, we have removed a phase factor eit/Tdyn, which is an artifact of using = ∑ ≠ λ
+−
 ̃  ̃ˆˆ
2H 2 i j ij I i I j
ff
ff instead of the more accurate expression
2H h h 2
xy
ff
22
= + ω0
 ̃ ( ˆ ˆ )/( ) (see equation (54)): the latter contains a small correction (1/2ω ) ∑ a [I(I + 1) − (Iˆ ) ] ≈ 1/T
ii i
z
0 2 2 dyn to the electron Zeeman splitting.
Rep. Prog. Phys. 80 (2017) 016001


 Review
24
[37, 38]. This involves an O(1/N) error [211] and is equivalent to a semi-classical treatment of the quantum noise. A detailed discussion can be found in [204] and [212]. Taking the ‘true’ decoherence in the FID as an example, on a timescale t  inverse HFI,
=− =−+ ω
() 〈 〉 〈 〉
 ̃ ( ˆ ˆ ) /( )
Lt e e .
Ht h h t
dyn 2i i 2
xy
ff
22
0
Regarding hˆx and hˆy as independent, classical quasi-static Gaussian noise obeying the distribution = −
P h e h2 2hrms
2
() /
/( ) ( 2π hrms) gives
L t P h dh P h dh e ,
x x y y h ht
dyn i 2
xy
22 0
∫∫
≈ −+ ω
( ) ( ) ( ) ( ) /( )
which reproduces equations (66) and (67).
8.4. Cluster-correlation expansion
The key idea of CCE is to factorize equation (57) into the product of cluster-correlation terms, each of which accounting for the irreducible, correlated fluctuations in a given bath spin cluster. For a finite-time evolution as in the central spin decoherence problem, a convergent result is obtained by truncating the expansion up to a certain cluster size. The two-spin cluster truncation of the CCE corresponds to the pair-correlation approximation [27–29]. When the central spin decoherence comes from the contribution of a large number of cluster correlation terms and the contribution from each individual term is small, as is the usual case for relatively large baths, CCE coincides with the cluster expansion [30, 31]. For small baths, however, central spin decoherence may be dominated by the coherent dynamics of a few cluster correlation terms. In this case, CCE converges to the exact results while the cluster expansion does not. CCE has been applied to electron spin decoherence for phosphorus donors in silicon (Si:P) [213], bismuth donors in silicon (Si:Bi) [143, 170, 214], radical spins in malonic acid crystals [215], and diamond NV center [111]. The calculated results agree well with the experimental data, including the decoherence timescale, the temporal profile, and its dependence on the magnetic field. The CCE also provides convincing theoretical demonstrations of atomic-scale sensing of distant nuclear spin clusters [16] and anomalous decoherence effects [95]. Both effects have been observed subsequently [96, 216] and these experiments are well explained by CCE calculations. CCE can be understood from two different viewpoints. First, CCE is a re-grouping and infinite summation of all the LCE diagrams [108]. Second, CCE is a systematic method to treat the irreducible, correlated fluctuation of successively larger spin clusters in a canonical ensemble, so CCE can also be used to calculate other quantities such as the quantum noise spectrum. The first understanding applies to a pure product state |J⟩ of the bath (equation (56)). The second understanding leads to two formulations: CCE for a general non-interacting bath state has a simpler form [202], but CCE for a pure product state of a general spin bath has better convergence [108].
8.4.1. CCE as infinite summation of LCE diagrams. For a pure product state |J⟩ (equation (56)) of the spin bath, the connection between LCE (equations (64) and (65)) to CCE is based on the observation that each connected LCE diagram can be
expanded as the sum of diagrams involving the flip-flops of different clusters of spins. As an example shown in figure 18(a) for a spin-1/2 bath, a third-order LCE diagram involving the flip-flop of a spin pair contains diagrams for spin clusters (1,2), (1,3), , where the numbers stand for the indices of the spins that have been flipped. Thus, all the connected diagrams can be classified according to the spin clusters instead of the interaction orders. For an arbitrary (empty or non-empty) cluster C, we define the cluster-correlation term π ̃(C) as the sum of all connected diagrams in which all (and only) the spins in cluster C have been flipped. For instance, some of the diagrams constituting π ̃(∅) and π ̃(i, j) for a spin-1/2 Hamiltonian in equation (58) are shown in figures 18(b) and (c), respectively. With these {π ̃} functions, the exact LCE is expressed as
 ̃( )
{ }
∑
⊆
π= π C
C
,
1,2, ,N (68)
i.e. the sum of cluster-correlation terms for all spin clusters (including the empty cluster ∅) in the N-spin bath. In particular, the infinite summation of all the connected diagrams for a certain cluster C and all its subsets
( )  ̃( )
∑⊆
π ≡ π′
′
CC
CC
, (69)
is just equal to π (equation (65)) with all the terms involving the flip-flop of spins outside the cluster C dropped, or, equivalently, with the bath Hamiltonian Hˆ (z) = Hˆ (ˆI1, , IˆN)
replaced with ({ˆ } {⟨ |ˆ | ⟩})
∈C ∉C
H I , JI J
j j in which the spins outside the cluster are mean-field averaged. Thus, we have
⟨⟩
( ) ˆ ({ˆ } {⟨ ˆ ⟩})
∫
=| |
π − ||
∈∉
T
C CC
e J e J.
H I JI J z C
i, d
jj
C (70)
For small clusters C, the Hamiltonian ˆ ({ˆ } {⟨ |ˆ | ⟩})
∈C ∉C
H I , JI J
jj
only contains spin operators inside the cluster C; thus π(C) can be calculated from equation (70) by direct diagonalization. This, in turn, allows {π ̃(C)} to be extracted recursively from equation (69):
∑⊂
π =π − π ′
′
CC C
CC
,
 ̃( ) ( )  ̃( ) (71)
e.g. π ̃(∅) = π(∅) and π ̃(i) = π(i) − π ̃(∅).
For a cluster C containing |C| bath spins, each diagram in π ̃(C) consists of at least |C| off-diagonal interaction lines that
Figure 18. (a) Expansion of a third-order connected diagram into diagrams involving the flip-flops of different clusters of spins. (b) and (c) show the diagrams contained in π ̃(∅) and π ̃(i, j),
respectively. Reproduced with permission from [108]. Copyright 2008 by the American Physical Society.
Rep. Prog. Phys. 80 (2017) 016001


 Review
25
connect all the spins in cluster C into a linked cluster (see figure 18 for examples), thus π ∼ λ | |
CC
fftd
 ̃( ) ( ) , where λff is the
typical value of the off-diagonal interactions λij (z)
ff . On a timescale td  1/λff, cluster-correlation terms of large clusters are small, so equation (68) can be truncated, e.g. keeping clustercorrelation terms containing up to M bath spins gives the Mthorder truncated CCE (CCE-M for short):
 ̃( )  ̃( )  ̃  ̃
()
⩽
() ( )
∑
π = π =π ∅ +π + +π
||
C
C
,
M
M
1M
where  ̃  ̃( )
()
π ≡ ∑| |= π C
C
M
M is the total contribution from all M-spin cluster-correlation terms. If each bath spin interacts, on average, with q spins, then the number of linked clusters containing m bath spins is ∼ −
Nqm 1 and  ̃ ( / )( )
()
π ∼ N q qλ t
mm
ff d .
Therefore, a sufficient condition for convergence of CCE is
λ
t <q
1.
d
ff
(72)
which is usually much longer than the electron spin decoherence time.
8.4.2. CCE without LCE: general non-interacting bath state. The CCE formalism described below can be directly used to calculate the average of a general time-ordered exponential over an arbitrary non-interacting ensemble ˆ ˆ
ρNI = ⊗iN=1ρi
(ρˆi for the ith bath spin), i.e. equation (57) with Hˆ (z) being a general spin bath Hamiltonian (not necessarily equation (58)) and Tr NI
〈〉 ≡ [ρˆ ()]. However, for clarity we consider equation (57) with Hˆ (z) given by equation (58), but the initial state of the bath is a general non-interacting state ρˆNI. The first step is to define the cluster term
() ⟨ ⟩
ˆ()
∫
≡−
CT C
Le ,
Hz z C
id
C (73)
where ˆ ( )
HC z is obtained from Hˆ (z) by dropping all the bath
spins outside cluster C, e.g. ˆ ( ) ( ) ˆ
H{ } z = ω z I
i ii
z and H z =
ˆ i,j ( )
{} ω +ω +λ +λ +
+−
z I z I z I I z I I h.c.
ii
z
jj
z
ij i
z j
z
ij i j
d ff
( ) ˆ ( ) ˆ ( ) ˆ ˆ ( )( ˆ ˆ ). The key observation is that when a cluster C can be divided into two subsets C1 and C2 such that ˆ ( )
HC z does not contain any interaction between the two subsets, L(C) is factorizable: (L C) = L(C1)L(C2). This allows singling out the irreducible, correlated fluctuations of different clusters by defining a hierarchy of cluster-correlation terms {L ̃(C )}:
L ̃(i) ≡ L(i), (74a)
 ̃( ) ( )
 ̃( )  ̃( )
≡

Lij Lij
LiL j
, , , (74b)
 ̃( ) ( )
 ̃( )
≡∏ ′
′⊂
CC
C
C
LL
L.
C
(74c)
The central spin coherence is expressed exactly as the product of all possible cluster-correlation terms:


∏ ∏∏
⊆
==
≠
⎛
⎝⎜ ⎞
⎠⎟
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
C
C
L L L i L i, j .
1,2, ,N i i j
 ̃( ) ( )  ̃( )
{}
(75)
Since Hˆ (z) contains pair-wise interactions λij (including
λij
d and λij
ff), the pair-correlation term ln L ̃(i, j) is at least firstorder in λijtd since L(i, j) = L(i)L( j ) and hence ln L ̃(i, j) = 0 when λ = 0
ij . By mathematical induction, it can be proved that the cluster-correlation term ln L ̃(C) vanishes if the interac
tions contained in ˆ ( )
HC z cannot connect all the spins in group C into a linked cluster. Consequently, in the Taylor expansion of ln L ̃(C) with respect to the bath interaction times the evolution time td, the bath interaction coefficients contained in every term must: (i) connect all the spins in group C into a linked cluster, (ii) ensure that each spin inside cluster C is flipped an even number (0, 2, 4, ) of times, and, if the initial state of the bath ˆ ˆ
ρ ∝I
NI is maximally mixed, (iii) ensure that every bath spin inside cluster C appears an even number (2, 4, 6, ) of times. Condition (i) alone ensures that ln L ̃(C) is at least (|C|−1)th-order, while conditions (ii) and (iii) usually
make the order of ln L ̃(C) even higher. For example, the Taylor expansion of ln L i, j
 ̃( ) with respect
to λijt
d d and λij t
ff d satisfying conditions (i) and (ii) reads
ln L i, j = c λ t + c λ t + c λ t + O t ,
ij ij ij
1 d d 2 d d 2 3 ff d 2 d
3
 ̃( ) ( ) ( ) ( )
as shown diagrammatically in figure 19(a). In the first and second terms/diagrams, spin i and spin j are not flipped. In the third term/diagram, each spin is flipped twice. If the initial state of the bath is maximally mixed, then condition (iii) dictates that the first term/diagram vanishes since in this term/ diagram each spin only appears once. In this case, the leading Taylor expansion of ln L ̃(i, j) is second-order, including
two terms: (λijt )
d d 2 and (λij t )
ff d 2. Similarly, according to conditions (i) and (ii), the Taylor expansion of ln L ̃(i, j, k) is at least second-order. The lowest, second-order expansion
includes three terms (λ t )(λ t )
ij ik
d d d d , (λ t )(λ t )
ij jk
d d d d , (λ t )(λ t )
ki kj
d d d d, as shown diagrammatically in figure 19(b). As these terms/ diagrams are obtained from the first one by interchanging i,j,k, they can be represented by a single diagram (the last diagram in figure 19(b)). The third-order expansions are shown diagrammatically in figure 19(c): the first diagram denotes
(λ t )(λ t )(λ t )
ij jk ki
d d d d d d , the second diagram denotes (λ t ) (λ t )
ij ik
dd2 d d
and other terms obtained by interchanging i,j,k, the third
diagram denotes (λ t )(λ t )(λ t )
ij jk ki
ff d ff d ff d , and the fourth diagram denotes (λ t ) (λ t )
ij ik
ff d 2 d d and other terms obtained by interchanging i,j,k. If the initial state of the bath is maximally mixed, then condition (iii) further dictates that all the second-order diagrams in figure 19(b) and the second and fourth diagrams in figure 19(c) should vanish. In this case, ln L ̃(i, j, k) is thirdorder, with the leading-order term being (λ t )(λ t )(λ t )
ij jk ki
dd d d d d
and (λ t )(λ t )(λ t )
ij jk ki
ff d ff d ff d . For an arbitrary cluster C, ln L ̃(C) is at least (|C|−1)th-order, or at least |C|th-order if the initial state of the bath is maximally mixed. On a timescale td 1/λ (λ is the typical value of bath spin interactions), cluster-correlation terms for large clusters are
Rep. Prog. Phys. 80 (2017) 016001


 Review
26
small, so the exact CCE (equation (75)) can be truncated, e.g. the Mth-order truncated CCE (CCE-M for short):
 ̃( )  ̃  ̃  ̃
()
⩽
() () ( )
∏
==
||
C
C
L L LL L ,
M
M
12 M
(76)
where  ̃  ̃( )
( ) ≡ ∏| |= C
C
LL
m
m is the contribution of m-spin
cluster-correlation terms. For example, CCE-1, L = L =
1  ̃1
() ()
L(1)L(2)  L(N ), provides a good description for the FID, which is dominated by inhomogeneous dephasing. CCE-2 gives
( )  ̃ ̃
() () ()
L 1, 2, , N = L L
2 1 2 , which is just the pair-correlation approximation [27–29]. By going to higher-order truncations, the contribution from cluster-correlation terms of larger clusters can be included accurately and systematically. For small truncation size M, the cluster-correlation terms can be easily calculated by exact numerical diagonalization. If each bath spin interacts, on average, with q spins, then the number of connected size-m clusters is ∼ −
Nqm 1. Since  ̃( ) ∼ (λ )| |−
CC
ln L td 1 (λ is the typical bath interaction), the contribution from m-spin correlation is  ̃ ( )
( )∼ λ −
ln L m N q td m 1. Therefore, a sufficient condition for the convergence of CCE is
λ
t <q
1.
d (77)
When the spin bath can be divided into many nonoverlapping clusters C , C , 
1 2 such that the interactions between different clusters are small, we can regard each cluster as an effective bath spin and apply the CCE formalism to these effective spins. Namely,
L ̃(C ) ≡ L(C ),
i i (78a)
 ̃( ) ( )
 ̃( )  ̃( )
≡

CC CC
CC
LL
LL
, ,,
,
ij
ij
i j (78b)
and the central spin coherence is expanded exactly as
( )  ̃( )
⎛
⎝⎜ ⎞
⎠⎟
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
∏∏
=
≠
L L C L C,C ,
i
i
ij
i j (79)
similar to equations (74) and (75). When the correlation between different subsets are neglected, equation (79) reduces to the disjoint cluster approximation [35]: L = ∏i L(Ci).
8.4.3. CCE without LCE: pure bath state. The CCE formalism for general non-interacting bath states treats both the
off-diagonal interactions λij
ff and diagonal interactions λij
d
as perturbations. However, for a pure product bath state |J⟩ (equation (56)), the diagonal interactions alone do not cause non-trivial evolution of the bath. In other words, the essential spin bath dynamics starting from a product state |J⟩ is the spin flip-flop by the off-diagonal interactions: the diagonal interactions can be exactly taken into account and only the offdiagonal interactions need to be treated as perturbations. This goal has been achieved by the CCE formalism in section 8.4.1 with the assistance of diagrammatic LCE [32]. Here, we present an alternative formulation of this approach without relying on the LCE. We are interested in the ‘true’ decoherence
⟨⟩
ˆ( )
∫
≡| |
−
L JT e J ,
J
Hz z C
id C
where contour Hamiltonian Hˆ (z) = H(ˆI1, , ˆIN) is written as an explicit function of all the bath spin operators. The CCE formalism described below applies to a general spin bath Hamiltonian, but we consider Hˆ (z) given in equation (58) for the sake of clarity. The idea of CCE is to single out the contributions from irreducible, correlated fluctuations from successively larger clusters. First, replacing all bath spin operators in H(ˆI1, , ˆIN) with their mean-field averages ˆI → ⟨J|ˆI |J⟩
j j gives the c-number mean-field Hamiltonian H(⟨J|ˆI1|J⟩, , ⟨J|ˆIN|J⟩) and hence the mean-field contribution without involving the flip of any bath spins
( ) (⟨ ˆ ⟩ ⟨ ˆ ⟩)
∫
∅≡ − ||  | |
Le .
J
i H J I J , , J I J dz
N
C 1 (80)
Since LJ(∅) is trivially evaluated, hereafter focus is put on the decoherence caused by the dynamic fluctuation of bath spins:
() ⟨ ⟩
ˆ
∫
δ ≡ ∅= | |
−δ
LL T
L J e J,
J
J
J
Hz C
id C
where
δHˆ ≡ H(ˆI , , ˆI ) − H(⟨J|ˆI |J⟩, , ⟨J|ˆI |J⟩)
1N 1 N
is the bath Hamiltonian with the mean-field part removed. To proceed, the decoherence due to the dynamical fluctuation of a non-empty cluster C is defined as
() ()
() ⟨ ⟩
ˆ
∫
δ ≡ ∅≡ | |
−δ
CCT C
LL
L J e J,
J
J
J
Hz C
id
C (81)
where
δ ˆ ≡ ({ˆ } {⟨ |ˆ | ⟩}) − (⟨ |ˆ | ⟩ ⟨ |ˆ | ⟩)
∈∉ 
C CC
H H I , JI J H JI J , , JI J
jj 1 N
(82)
is the fluctuation part of the Hamiltonian of cluster C, obtained from δHˆ by replacing bath spin operators outside cluster C
Figure 19. Diagrammatic representation of the lowest-order processes contributing to ensemble cluster-correlation terms for (a) L ̃(i, j),(b) and (c) L ̃(i, j, k). Solid (dashed) line for off-diagonal (diagonal) spin–spin interaction.
Rep. Prog. Phys. 80 (2017) 016001


 Review
27
with their mean-field averages ˆ → ⟨ |ˆ | ⟩
∉C ∉C
I JI J
j j . By definition, δHˆC does not contain any bath spin operators outside cluster C. The key observation is that if cluster C can be divided into two subsets C1 and C2 such that (A) Hˆ (z) does not contain
any interaction between C1 and C2, or (B) Hˆ (z) contains no spin-flip terms for the spins of one subset (say C1), then δLJ(C) can be factorized as δL (C) = δL (C )δL (C )
J J 1 J 2 . This is because condition (A) leads to ˆ ˆ ˆ
δ =δ +δ
CCC
HHH
1 2, i.e. the dynamical fluctuation of C1 and C2 are independent, while condition (B) allows all operators inside C1 to be replaced with their meanfield averages (i.e. spins in C1 has no dynamical fluctuation), so that δL (C ) = 1
J 1 and δL (C) = δL (C )
J J 2 . This motivates the following definition of a hierarchy of cluster-correlation terms, in a way similar to the previous section:
δL ̃ (i) ≡ δL (i),
J J (83a)
 ̃( ) ( )
 ̃()  ̃( )
δδ
δδ
≡

L ij L ij
Li L j
, ,,
J
J
J J (83b)
 ̃( ) ( )
 ̃( )
δδ
δ
≡∏ ′
′⊂
CC
C
C
LL
L.
J
J
C J (83c)
The decoherence is expressed exactly as the product of all possible cluster-correlation terms:
 ̃( )
{}
∏
⊆
δ= δ

C
C
L L.
J N
J
1,2, , (84)
So defined cluster-correlation δL ̃J(C) vanishes if the interac
tions contained in δHˆC cannot connect all the spins in group C into a linked cluster (i.e. cluster C consists of two subsets with independent dynamical fluctuation), or if the off-diagonal interaction terms contained in δHˆC do not flip certain spins inside cluster C (i.e. these spins have no dynamical fluctuation). Therefore, the cluster-correlation term δL ̃J(C) accounts for the irreducible, fully correlated dynamical fluctuation of all spins in cluster C. Consequently, in the Taylor expansion
of ln δL ̃J(C) with respect to λij t
ff d and λijt
d d, the interaction coefficients contained in every term must (i) connect all the spins in group C into a linked cluster, and (ii) ensure that every spin in cluster C is flipped an even (2, 4, 6, ) number of times. Conditions (i) and (ii) ensure that ln δL ̃J(C) is at least |C| th-order in (λfftd), where λff is the typical off-diagonal bath
interactions. Taking the Taylor expansion of ln δL ̃ (i, j)
J as an example, the first few terms in the expansion are shown diagrammatically in figure 20(a), including the lowest, second-order term (λij t )
ff d 2 (first diagram), the third-order term
(λ t )(λ t )
ij ij
d d ff d 2 (second diagram), and the fourth-order terms
(λ t ) (λ t )
ij ij
d d 2 ff d 2 (third diagram) and (λij t )
ff d 4 (fourth diagram).
Similarly, the Taylor expansion of ln δL ̃ (i, j, k)
J is shown diagrammatically in figure 20(b), including the lowest, thirdorder term (λ t )(λ t )(λ t )
ij jk ki
ff d ff d ff d (first diagram), the fourth-order
term (λ t )(λ t )(λ t )(λ t )
ij ij jk ki
d d ff d ff d ff d and other terms obtained by
interchanging i, j, k (second diagram), the fourth-order term
(λ t ) (λ t )
ij jk
ff d 2 ff d 2 and other terms obtained by interchanging i, j, k (third diagram). The first few terms in the Taylor expansion of ln δL ̃ (i, j, k, l)
J are shown in figure 20(c), including the lowest, fourth-order term (first diagram) and a few fifth-order terms (other diagrams). For the Taylor expansion of ln δL ̃J(C) for a general cluster C, the lowest-order term is the ring diagram formed by |C| off-diagonal interaction lines, such as the first diagram in figures 20(a)–(c); thus ln δL ̃J(C) is |C|th-order in λfftd. On a timescale td  1/λff, the exact CCE (equation (84)) can be truncated, e.g. the Mth-order truncated CCE (CCE-M for short) is:
 ̃( )
()
⩽
∏
δ= δ
||
C
C
L L.
J
M
M
J (85)
For a relatively small truncation size M, the cluster-correlation terms can be calculated by exact numerical diagonalization. CCE-1 gives  ̃ ( )  ̃ ( )
()
δ L = δL 1  δL N
JJ J
1 , corresponding to the independent precession of individual bath spin in the meanfield produced by other bath spins. CCE-2 accounts for the irreducible bath spin correlations up to pairs and is equivalent to the pair-correlation approximation [27–29]. Going to successively higher-order truncations allows systematic inclusion of successively higher-order irreducible correlations in the spin bath evolution and accurate description of the decoherence under various DD controls (figure 21(a)). In terms of π ̃(C) in section 8.4.1, we have ( )
 ̃( ) = ∅
eπ ∅ LJ and  ̃ ( )
 ̃( ) = δ
πC
e C LJ for non-empty C; thus a sufficient condition for convergence is still equation (72). However, in some cases, the convergence could even go well beyond. One such scenario is a disordered spin bath with highly non-uniform or even random spin-splitting energies for different spins. In this case the disorder-induced localization effect would bound the size of irreducible fully correlated clusters up to a critical size M0, such that CCE-M0 would converge to the exact results on any timescales (see figure 21(b) for an example). The random spin splitting of bath spins inside a cluster C may come from their random couplings to the central spin or to the mean-field averages of other bath spins outside cluster C, e.g. in δHˆC, the spin splitting of the jth spin inside C consists of two non-uniform parts: s z aj 2
( ) / due to HFI and λ
∑ ||
∉C 〈J Iˆ J〉
k jk k
z
d due to coupling to external bath spins. This
Figure 20. Diagrammatic representation of the lowest-order processes contributing to cluster-correlation terms (for a pure initial state of the bath) of (a) δL ̃J(i, j), (b) δL ̃ (i, j, k)
J , and (c) δL ̃ (i, j, k, l)
J. Solid (dashed) line for off-diagonal (diagonal) spin–spin interaction.
Rep. Prog. Phys. 80 (2017) 016001


 Review
28
observation makes it possible to modify the CCE to improve its convergence [69]. The hybrid CCE [69] is the same as the CCE in section 8.4.2 except for a different definition of ˆ ( )
HC z and hence L(C) (equation (73)): instead of dropping all the
bath spins outside cluster C from the bath Hamiltonian Hˆ (z),
now ˆ ( )
HC z is obtained from Hˆ (z) by dropping the terms that flip the bath spins outside cluster C. Thus, L(C) in hybrid CCE is connected to the cluster-correlation terms δLJ(C) in section 8.4.3 via
() ( ) () ()
∑∑
L C = P L ∅ δL C = P L C .
J
JJ J
J
J J (86)
The mean fields from external bath spins randomizes the splitting of bath spins inside C and improves the convergence, although it is not obvious whether or not the hybrid CCE converges to the exact results: here, L(C) is no longer factorizable even if C can be divided into two subsets with no inter-subset interactions, so ln L ̃(C) (as defined in equation (74)) does not
vanish even if the interactions contained in ˆ ( )
HC z cannot connect all the spins in group C into a linked cluster. In practice, the ensemble average in equation (86) has exponential complexity. The algorithm to deal with this issue and detailed discussion of its applications to Si:P, silicon QDs, and NV centers can be found in [69]. Finally, when the spin bath consists of many nonoverlapping subsets C , C , 
1 2 with weak inter-subset interactions, we can regard each subset as an effective bath spin and apply the CCE formalism (equations (83) and (84)) to these effective spins, in the same way as equations (78) and (79).
8.4.4. CCE for quantum noise auto-correlation function. Recently, the idea of CCE has been adapted [70, 97] to cal
culate the auto-correlation ⟨bˆ(t)bˆ⟩ of the quantum noise
ˆ( ) ˆ
ˆˆ
≡−
b t e be
iH t iH t
B B driven by an interacting bath Hamiltonian HˆB, where the noise operator ˆ ˆ
=∑
b j bj is the sum of operators
of individual spins (e.g. ˆ ˆ
b =a ⋅I
j j j) and 〈〉 ≡ Tr[ρˆB()] is the ensemble average in a product bath state ˆ ˆ
ρB = ⊗j ρj. The first step is to define the quantum noise from a spin cluster,
ˆ() ˆ ˆ ˆ
≡−
CC
CC
b t e be
iH t iH t
where ˆ ˆ
=∑∈
CC
bb
j j and HˆC is the Hamiltonian of a cluster C, obtained from the bath Hamiltonian by dropping all bath spins except for those in cluster C. The second step is to define the noise auto-correlation
( ) ⟨ ˆ( ) ˆ⟩ ⟨ ˆ( )⟩⟨ ˆ⟩
{ }≡ −

C t btb bt b
1,2, ,N (87)
and the contribution from a cluster C:
( ) ≡ ⟨ ˆ ( ) ˆ ⟩ − ⟨ ˆ ( )⟩⟨ ˆ ⟩
C CC C C
C t b t b b t b , (88)
where N is the number of bath spins. If a cluster C consists of two subsets C1 and C2 and HˆC does not contain any interaction between these two subsets, then the noise auto-correlation from this cluster is additive: ( ) = ( ) + ( )
CCC
Ct C t C t
1 2 . This motivates the definition of a hierarchy of cluster-correlation terms:
 ̃() ()  ̃ ()
∑⊂
≡−
′
′
CC CC
C
C t C t C t , (89)
e.g. C ̃ (t) ≡ C (t)
i i ,  ̃ ( ) ( )  ̃( )  ̃( )
{} {}
C t ≡C t −C t −C t
i,j i,j i j , etc. By
definition, the pair-correlation  ̃ ( )
{}
Ct
i,j vanishes when there is no interaction between spin i and spin j, thus  ̃ ( )
{}
Ct
i,j is at least first-order in the bath spin interactions. Similarly,  ̃ ( )
CC t vanishes when the interactions contained in HˆC cannot connect the spins in group C into a linked cluster; thus  ̃ ( )
CC t is at least (|C|−1)th-order in the bath spin interactions. Finally, the noise auto-correlation is approximated by truncating the expansion, e.g. keeping cluster-correlation terms containing up to M spins gives (CCE-M for short):
()  ̃()
{}
()
⩽
∑
=
||

CC
C
C t C t.
N
M
M
1,2, ,
, (90)
Since ( )
CC t and hence  ̃ ( )
CC t for small |C| can be easily calculated by exact numerical diagonalization, equation (90) provides a systematic approach to calculate the auto-correlation up to successively higher orders of inter-spin correlation, e.g. for a non-interacting spin bath, the cluster contributions  ̃ ( ) =
CC t 0 for |C| ⩾ 2, so CCE-1 gives the exact result:
( ) = ∑  ̃( ) = ∑ ( )
C 1, 2, , N i C i i C i , even in the presence of rapid single-spin dynamics such as that induced by the anisotropic HFI (see section 9.1.2). We notice that the original formulation [70, 97] of the CCE of noise auto-correlation uses a slightly different definition:
( ) ⟨ ˆ( ) ˆ⟩ ⟨ ˆ ⟩
{ }≡ −
′
C t btb b ,
1,2, ,N
2 (91)
Figure 21. ‘True’ decoherence from CCE compared with the exact solutions for one-dimensional spin-1/2 XY model consisting of N = 100 bath spins. (a) FID, Hahn echo, and under CPMG2 control. The level splitting of bath spins vary smoothly with location. (b) FID. The level splitting of bath spins varies randomly with location. Reproduced with permission from [108]. Copyright 2008 by the American Physical Society
Rep. Prog. Phys. 80 (2017) 016001


 Review
29
( ) ≡ ⟨ˆ ( )ˆ ⟩−⟨ˆ ⟩
′C C C C
C t b t b b2
(92) instead of equations (87) and (88). In this case, even when a cluster C consists of two subsets C1 and C2 and HˆC does not contain any interaction between these two subsets, the cluster term ( )
C′C t does not reduce to ( ) + ( )
′′
CC
Ct Ct
1 2 due to the
existence of cross-correlation terms (⟨ ˆ ( )⟩ − ⟨ ˆ ⟩)⟨ ˆ ⟩
C CC
bt b b
1 1 2 and
(⟨ ˆ ( )⟩ − ⟨ ˆ ⟩)⟨ ˆ ⟩
C CC
bt b b
2 2 1 . Thus, this formulation is essentially a short-time perturbative expansion of W(t) around t = 0 [70]. For a maximally mixed bath state ˆ ˆ
ρ ∝I
B , the cross-correlation terms vanish; thus ( ) = ( ) − ( )
′C C C
C t C t C 0 , i.e. the original formulation coincides with equations (87)–(89).
8.4.5. Numerical techniques. The CCE calculations converge rapidly for the electron spin decoherence in nuclear spin baths with short-ranged dipolar interactions, such as the decoherence of the electron spin of an NV center caused by the 13C nuclear spins with natural abundance 1.1% in diamond [16, 95, 111] and the decoherence of the donor (phosphorus or bismuth) electron spin caused by the 29Si nuclear spins with natural abundance 4.7% in silicon [97, 143, 207, 217–219], as shown in figure 22. Here, we summarize the main steps of performing the CCE calculations in realistic systems and provide the numerical tricks in each step [69, 97, 111, 207].
Step 1: choosing the initial state of the bath. Since the maximally mixed thermal bath state and a typical pure product bath state sampled from the thermal ensemble give similar ‘true’ decoherence (see section 5.2), espe
cially for a relatively large bath (such as the 29Si nuclear spin bath in silicon), it is preferable to calculate the ‘true’ decoherence with the CCE method for a pure bath state (section 8.4.3), which has faster convergence [69, 97] than that for a general noninteracting bath state (section 8.4.2). The thermal noise is relevant only for the FID and amounts to a multiplicative factor L (t)
inh
(equation (59)). Step 2: determining the size of the nuclear spin bath. The bath spins can be chosen as those within a certain threshold distance Rc away from the central spin (or threshold HFI strength), which is gradually increased until convergence. Typically, R ∼ 4
c nm (including N ∼ 500 bath spins) for the natural 13C nuclear spin bath in diamond [16, 95] and R ∼8
c nm (including N ∼ 5000 bath spins) for the natural 29Si nuclear spin bath in silicon [97, 207]. Step 3: defining effective bath spins. A cluster of bath spins that are fully linked via very strong interactions is identified as a large effective spin, so the bath is divided into many non-overlapping, strongly linked clusters C , C , 
12 ,
or equivalently many effective spins. Then, subsequent steps and the CCE all apply to these effective spins (see equations (78) and (79)). Step 4: selecting contributing clusters. For a given truncation size M, it is not necessary to keep all the clusters containing M effective spins, since only clusters with fully correlated fluctuations contribute to central spin
decoherence. For nuclear spins coupled through shortrange dipolar interactions and within the central spin decoherence time, significant inter-spin correlation develops only among a few nearest neighbors, especially among those that are fully linked through sufficiently strong interactions. Thus, it suffices to keep clusters whose diameter is smaller than a certain upper cutoff dc, which is gradually increased till convergence. Typically dc ∼ 1 nm for both the natural 13C nuclear spin bath in diamond and the natural 29Si nuclear spin bath in silicon [16, 97, 207]. A lower cutoff λmin in the cluster connectivity strength λC (defined as the smallest interaction necessary to complete the full connectivity of the cluster C) is also preferred [69].
Finally, the Monte Carlo sampling technique can be used when there are too many contributing clusters.
8.5. Real-space cluster expansion
As one of the first quantum many-body theories for central spin decoherence, the density matrix cluster expansion [30, 31] provides a convenient method to include multi-spin correlations, in the spirit of the virial expansion for interacting gases in grand canonical ensembles. In terms of L(C) defined in equation (73) of section 8.4.2, cluster expansion defines the (irreducible) cluster-correlation terms {W (C)} by subtracting all reducible parts:
W (i) ≡ L(i), (93a)
W (i, j) ≡ L(i, j) − W (i)W ( j), (93b)
W (i, j, k) ≡ L(i, j, k) − W (i)W ( j)W (k) − W (i)W ( j, k) (93c)
− ( ) ( )− ( ) ( )

W j W i, k W k W i, j , (93d)
() () ( )
{}
∑∏
≡− α
αα
CC C
CC
W L W , (93e)
Figure 22. Convergence of CCE in realistic nuclear spin baths. (a) Decoherence of the NV electron spin transition |+1⟩ ↔ |−1⟩
under CPMG-5 control and B = 0.3 T along the NV axis, caused by the 13C nuclear spins with natural abundance 1.1%. (b) Decay of Hahn echo of the Bi donor electron spin near the ‘clock’ transition
(B = B + 0.3
CT mT with B = 79.9
CT mT), caused by the 29Si nuclear spins with natural abundance 4.7%. Panel (a) is reproduced with permission from [95], copyright 2011 by the American Physical Society. Panel (b) is reproduced with permission from the supplementary information of [97]. Copyright 2015 by the American Physical Society.
Rep. Prog. Phys. 80 (2017) 016001


 Review
30
where in the last line the sum runs over all possible partitions of the cluster C into non-overlapping and non-empty subsets C,C ,
1 2 . The central spin coherence can be expressed exactly in terms of these cluster-correlation terms:
( ) ()
{}
∑∏
= +α
αα
C
CC
L W 1, 2, , N W , (94)
where the sum in the last line runs over all possible partitions of all bath spins {1, 2, , N} into non-overlapping and nonempty subsets C , C , 
1 2 .8 The cluster-correlation terms {W (C)} in cluster expansion have very similar properties as the cluster-correlation terms L ̃(C) in CCE (see section 8.4.2), e.g. W (C) vanishes if the
interactions contained in ˆ ( )
HC z cannot connect all the spins in group C into a linked cluster, so W (C) is at least (|C|−1) th-order in (λtd), where λ is the typical interaction strength in the bath. Keeping cluster-correlation terms containing up to M spins gives the Mth-order truncated cluster expansion (CE-M for short):
()
()
{} ⩽
∑∏
=α ||
αα α
C
CC C
L W,
M
, M (95)
where the sum runs over all possible partitions of the bath into non-overlapping non-empty clusters C , C , 
1 2 of size up to M. In the cluster expansion for interacting gases in grand canonical ensembles with translational symmetry, the evaluation of a truncated cluster expansion reduces to the calculation of a finite number of cluster terms {W (Cα)} with |Cα| ⩽ M, which can be easily done by exact numerical diagonalization. For a finite-size spin bath or for a bath without translational symmetry, however, it is very difficult to calculate the sum in equation (95) even for a small M. When all the cluster terms {W (C)} are individually small, equation (95) can be approximated by a factorized form by adding some overlapping terms that are higher-order small quantities. For example, the contour Hamiltonian in equation (58) gives W(i) = L(i) = 1 at the echo time of DD control, so CE-M can be approximated by
 ̄ [ ( )]
()
⩽⩽
()
∏∏
= +≈
α
<| | <| |
αα
α
C
CC
C
L 1W e .
M
MM
W
1 1 (96)
Comparing the factorized form in equation (96) to the exact CE-M in equation (95), the error  ̄
() () ()
L ≡L −L
MMM
err
 ̄
( )( ) ( )( )
() () ()
∑∑
≡−
=+ +
<< << <

L LL
W i, j W j, k W i, j, k W k, l ,
M MM
ijk ijkl
err
(97) contains the products of all possible cluster terms sharing at least one spin. Such overlapping terms are higher-order small
quantities and hence equation (96) is justified when each individual cluster term for |Cα| > 1 is small, e.g. for large spin baths, where the number of contributing clusters is large and hence the contribution from each individual cluster remains small within the timescale of decoherence. The error ( )
LM
err from the overlapping terms becomes relevant for small spin baths, where the coherent dynamics of a small number of multi-spin clusters dominating the decoherence may persist well beyond the bath spin flip-flop time, such that the small-term condition is no longer satisfied. In this case the cluster expansion may not converge to the exact results. The factorized CE-M (equation (96)) has been applied to electron and/or nuclear spin decoherence in Si:P (caused by 29Si nuclei with natural abundance 4.7%) [30, 31, 220, 221], Si:Bi [143], GaAs QDs (caused by 69Ga, 71Ga, and 75As nuclei), and Si:SiGe QDs (caused by 73Ge and 29Si nuclei) [31, 222]. For electron spin echo in Si:P, cluster expansion provides a complete understanding of the experimentally measured decay profile [79–82, 223] (see figure 23 for an example), including the envelope modulation by strong anisotropic HFI with a few proximal 29Si nuclei (as discussed in section 9.1.2), the dependence on the magnetic field orientations and 29Si abundance, and the transition of the electron spin resonance lineshape from Gaussian (for 29Si abundance f ⩾ f0) to Lorentzian (for f ⩽ 1.2%), which arises from ensem
ble averaging of the inhomogeneous dephasing −( / ∗)
e t T2 2 of each individual donor over the distribution of T∗2 [14, 50]. Cluster expansion also shows that many-pulse CPMG could prolong the electron spin coherence time in Si:P and GaAs QDs by factors of 4–10 [217] and that in a Si:Bi system, the hybridi
zation of the Bi donor electron spin with 209Bi nuclear spin could significantly change the decay of the electron spin Hahn echo caused by the 29Si nuclei [143]. For 31P donor nuclear spins in GaAs and Si [220], cluster expansion gives negligible decoherence on the timescale of 100 μs in GaAs:P and 1–2 ms in Si:P under CPMG sequences with 2–4 π-pulses, indicating
the promising role of 31P nuclear spin as a long-lived quantum memory.
8.6. Limitations of the many-body theories and possible extension
Despite the unprecedented understanding of the central spin decoherence under many experimental conditions, the available many-body theories are still subject to several limitations. First, the theories in section 8 are restricted to the pure dephasing model (equation (32) or (43)), which is justified when the central spin splitting  bath spin splitting. A possible extension is to generalize the idea of CCE to spin relaxation, e.g. the evolution of ⟨Sˆz(t)⟩ can be calculated by applying the CCE
formalism to L(t) ≡ ⟨Sˆ (t)⟩/⟨Sˆ (0)⟩
z z . Second, for fast convergence of these theories, the size of the contributing bath spin clusters (i.e. those with appreciable correlated fluctuations) should be relatively small within the central spin decoherence time, so that their contributions can be obtained by exact diagonalization or other methods. Therefore, these theories also
8 For translationally invariant spin baths such that W(i) = W1, W (i, j) = W2, , equation (94) simplifies to
(/)( /)
∑
=

LN W
m
W m
! 1!
!
2! !
N
mm
mm
,,
1
1
2
2
12
12
subjected to the constraint ∑ lm = N
l l . The quantity ξ /
∑ L N! =
N
NN
ξ
exp ∑ W l !
l
ll
( / ) corresponds to the virial expansion of interacting identical gases in grand canonical ensembles.
Rep. Prog. Phys. 80 (2017) 016001


 Review
31
require short-range interactions between bath spins (i.e. small q in equations (77) or (72)), which in turn necessitates a large central spin splitting. Otherwise (e.g. in weak magnetic fields [38, 53, 210, 224] or near the optimal work points [97, 219]) the successive flip-flops of the central spin with different bath spins may rapidly induce long-range correlations in the bath, beyond the description of existing theories. For very small central spin splitting, the intrinsic bath spin interactions can be neglected, so the coupled system is described by the central spin model
ˆ ˆ ˆ ˆˆ
∑
H = ω S + ω I + S ⋅ h,
I i
i
z
0 z (98)
where ˆ ˆ
h≡∑ aI
i i i. This model allows the central spin and
the bath spins to exchange spin angular momentum, a feature that is absent from pure dephasing models. The central spin evolution due to equation (98) has been studied by a great diversity of approaches, including semi-classical models that treat the bath spins as classical stochastic variables [153, 225–227], exact analytical solutions for uniform HFI [228–230] or fully polarized spin baths [152, 231], direct numerical modelling [203, 232–235] and Bethe ansatz solutions [236, 237] for small baths containing a few tens of spins. For large baths, non-Markovian master equations [53, 210, 224, 238–240] and equation of motion approaches [241, 242] have been used, but they require strong magnetic fields under which central spin relaxation is suppressed while pure dephasing is usually dominated by the intrinsic nuclear spin interactions. Recently, central spin decoherence on a timescale  inverse of the HFI has been treated by the time-dependent density matrix renormalization group [243, 244] and resumming the time-convolutionless master equation [245]. The former shows that for large baths, the central spin dynamics is well described by the semi-classical model (equation (10)) with a classical Gaussian noise  ̃b(t), or by treating both the central spin and the bath spins as classical vectors subjected to random initial orientations. The latter shows that the central spin dynamics depend on the HFI coefficients {ai} only
through ∑i ai
2 and hence can be approximated by an exactly solvable model with uniform HFI, consistent with the energytime uncertainty relations [211]. The central spin dynamics on longer timescales, which depend sensitively on the specific distribution of {ai}, remains an open issue.
9. Quantum decoherence effects
According to the idea of CCE, the contribution of bath dynamics to the central spin decoherence is the product of irreducible, correlated fluctuations from bath spin clusters of different sizes (see equations (76) and (85)). In this section we discuss some quantum decoherence effects caused by these fluctuations. In a relatively weak magnetic field or for the FID, the decoherence is dominated by the fluctuation of single-spin clusters; thus CCE-1 gives a good approximation [106, 111]. In a strong magnetic field or under Hahn echo control, the fluctuation of single-spin clusters is frozen or its effect is suppressed by DD, and the correlated fluctuation of nuclear spin pairs dominates, thus CCE-2 is usually sufficient [95, 111, 218]. Under high-order DD [111, 207] or near the optimal working points (e.g. for the electronicnuclear hybrid spin qubit in Si:Bi system) [97, 219], multispin correlation becomes pronounced, so higher-order truncation of CCE is needed to get convergent results.
9.1. Single spin fluctuation
In a relatively weak magnetic field, each individual nuclear spin has a large quantum fluctuation since the Zeeman energy and the HFI are comparable and do not commute with each other, while the pairwise nuclear flip-flop processes have a much weaker effect as the dipolar interaction between nuclear spins is usually much weaker than the energy cost of the pairwise flip-flop due to the HFI gradient. In this case, we can assume the central spin ˆS (S = 1/2) is coupled to a bath of
non-interacting nuclear spins {ˆIj} (I = 1/2 for simplicity), described by the pure dephasing Hamiltonian,
Figure 23. Spin-echo decay in Si:P for ten different magnetic field orientations ranging from [0 0 1] to [1 1 0]. Apart from a few common fitting parameters for all curves, each curve is fitted with two parameters: the decoherence time TSD due to 29Si nuclei and its exponent n. These fitting parameters (black triangles) are compared with the cluster expansion calculations (red triangles) in (b). Right (Left) triangles correspond to n (TSD). The fitted n deviates from theory only at small magnetic field angles, where the nearest-neighbor dipolar flip-flop interactions approach zero. Reproduced with permission from [221]. Copyright 2007 by the American Physical Society.
Rep. Prog. Phys. 80 (2017) 016001


 Review
32
ˆˆ ˆ ˆ
∑∑
H =S h ⋅I + h ⋅I,
j
j
bj
j
j
z B j (99)
where ˆ ˆ
b≡∑ h ⋅I
jj
b j with h j
b being the HFI coupling, and the intrinsic bath Hamiltonian ˆ ˆ
H =∑ h ⋅I
jj
B B j with h j
B being the external magnetic field. The bath Hamiltonian conditioned on
the central spin state is ˆ ˆ
()
=∑ ⋅
±±
H hI
j j describing the bath
spin precession around the fields /
( )= ±
h± h h 2
jj
B j
b.
The single-spin fluctuation causes two possible effects. For isotropic HFI, we have [bˆ, Hˆ ] = 0
B , so the thermal noise from bath spins leads to inhomogeneous dephasing of the central spin in FID. For anisotropic HFI (equation (50)), we have[bˆ, Hˆ ] ≠ 0
B, so the quantum noise from bath spins gives rise to modulation effects in central spin decoherence (see appendix for the Bloch vector representation of single nuclear spin dynamics).
9.1.1. Isotropic HFI: inhomogeneous dephasing. For isotropic HFI (e.g. for a conduction electron confined in a III–V
semiconductor QD) [27, 28], h j
b and h j
B are both along the z axis and equation (99) reduces to ˆ ˆ ˆ ˆ
= ∑ +∑
H S hI hI
jj
b j
z
jj
B j
z
z. In this case, bˆ commutes with the bath Hamiltonian HˆB, so the noise is static and leads to Gaussian inhomogeneous dephasing for the FID (cf equation (59)),
() ( / ) (/ )
∏
= ≈− ∗
L t cos h t 2 e ,
j
j
b tT
FID 2 2
where the inhomogeneous dephasing time T∗ = 2 /h
2 rms with
= ∑( )
h j hj
b
rms
1 2
2 being the root-mean-square fluctuation of
the noise field [106]. DD can largely remove the effect of sin
gle-spin clusters. So one would have to go to higher-order correlations of the nuclear spins to correctly describe the ‘true’ decoherence.
9.1.2. Anisotropic HFI: decoherence envelope modulation.
For anisotropic HFI (equation (50)), the noise field h j
b deviates from the direction of h j
B (pointed along z axis), then even non-interacting bath spins could cause nontrivial electron spin decoherence. The anisotropic HFI can exist for donors (or QDs) in silicon and NV centers in diamond (see section 7.1.2).
The FID is entirely determined by the magnitudes h(j±) of the
fields h(j±) and their relative angle Θj:
() ()
() ()
() () () ()
∏
∏
=
= Θ − +Θ +
+− +−
⎡
⎣
⎢⎢
⎤
⎦
⎥⎥
Lt Lt
h ht h ht
cos 2 cos 2 sin 2 cos 2 .
j
j
j
j jj j jj
FID FID
22
(100)
We decompose the anisotropic HFI as = + ⊥
h he h
j
b j
bz
j
, z b, .
In the short-time limit, L (t)
FID shows Gaussian decay: () ( ) /
≈ −∑
L t e ht
FID 8
jj
b,z 2 2 for h  h
j
b j
B and ( ) ( ) /
≈ −∑
L t e ht
FID 8
jj
b2 2
for h  h
j
b j
B [111]. In a longer time-scale, since sin Θj =
⊥ +−
h h hh
j
b j
B
jj
,
( )/( )
( ) ( ) , we have|sin Θ|  1for h  h
j
b j
B or h  h
j
b j
B;
thus in a strong external magnetic field h h
j
b j
B
(  ), the
jth nuclear spin contributes a dominant slow oscillation
∼ cos(h t /2)
j
b,z modulated by a small-amplitude, fast oscilla
tion ∼ cos(h j t)
B to the central spin decoherence [246]. In QDs or shallow donors with a large nuclear spin bath, the rapid inhomogeneous dephasing usually makes this effect invisible. In diamond NV centers with a rather small nuclear spin bath, however, the electron spin decoherence is usually dominated by a few strongly coupled bath spins. In this case, the modulation effects are manifested as the deviation of the decoherence away from Gaussian profile, which has been observed experimentally [106]. The Hahn echo
()
() ()
⎡
⎣
⎢⎢
⎤
⎦
⎥⎥
∏
τ ττ
= −Θ
+−
L hh
2 1 2 sin sin 2 sin 2
j
j
jj
H 2 2 2 (101)
shows non-Gaussian decay in the short time limit:
() /
τ ≈ −| × | τ
L2 eh h
H8
j
B j
b 2 4 . On a longer time-scale, the second term in equation (101) gives rise to modulations with amplitude ∼ sin Θj
2 on the electron spin-echo decay (called electron spin-echo envelope modulation, see figure 24 for an example), where sin Θj is called the modulation depth parameter [221]. The modulation depth is appreciable for those nuclei with the HFI and Zeeman energy comparable, i.e.
h ∼h
j
b j
B. When the magnetic field orientation (defined as the z axis) is chosen such that h j
b is perpendicular to h j
B and hence () ()
==
+−
hhh
j j j, periodic restoration of spin coherence can be achieved at sin(h τ /2) = 0
j [221].
9.2. Pair-correlation effect
In the strong magnetic field regime, the individual nuclear spin fluctuations are suppressed (apart from a trivial inhomogeneous dephasing for the FID), so central spin decoherence is caused by the correlated fluctuation of larger nuclear spin clusters. On a short timescale compared with the inverse nuclear spin interactions, the correlated fluctuation are mainly from the nuclear spin-pair dynamics, so it can be described by CCE-2 or equivalently the pair-correlation approximation [27–29].
Figure 24. Theoretical and experimental results for electron spin-echo decay. The theoretical curve is the product of spin-echo envelope modulation due to anisotropic HFI-induced bifurcated evolution of individual nuclear spins, the non-Markovian decay
e−(2τ/TSD)n due to nuclear spin flip-flop dynamics, and Markovian decay e−2τ/T2. Reproduced with permission from [221]. Copyright 2007 by the American Physical Society.
Rep. Prog. Phys. 80 (2017) 016001


 Review
33
Here, we focus on ‘true’ decoherence and take the initial state of the nuclear spin bath as |J⟩ (equation (56)). For the
Hamiltonian in equation (55), we have δL ̃ (i) = 1
J and hence
()
{}
∏
L = L i, j
J
ij
J ,
up to a trivial phase factor, where
() ⟨ ⟩
ˆ (ˆ ˆ {⟨ ˆ ⟩})
{}
∫
≡| |
− ||
∉
L i, j J T e J
J
HI I JI J z C
i ,, d
i j m ij
C,
is the decoherence due to the nuclear spin pair {i,j}, whose
effective Hamiltonian ˆ (ˆ ˆ {⟨ ˆ ⟩})
{}
||
∉
H I,I, J I J
i j k i,j is obtained from the total Hamiltonian by replacing all spin operators outside cluster C by their mean-field averages. There are N(N − 1) pairs in the bath, as labeled by k ≡ (i, j). The initial state of the kth pair is mapped to the spindown state of a spin-1/2 pseudo-spin σˆ k: |⇓⟩ ≡ |m⟩ |n⟩
k i j, while the flip-flopped state is mapped to the spin-up state of this pseudo-spin: |⇑⟩ ≡ |m + 1⟩ |n − 1⟩
k i j. Therefore, the flip-flop dynamics of each nuclear spin pair are mapped to the flip dynamics of the pseudo-spins starting from the initial state |J⟩ = ⊗k |⇓⟩k. Here, the flip of the kth pseudo-spin gives a state |J, k⟩ that is energetically higher than |J⟩ by an amount ⟨ | ˆ | ⟩−⟨ | ˆ | ⟩= ±
±±
J, k H J, k J H J Dk Zk, while the transition
amplitude from |J⟩ to |J, k⟩ is ⟨ | ˆ | ⟩ = ±
±
J, k H J Bk Ak, with
Dk from the diagonal nuclear spin interaction Hˆd, Bk ∝ λij
ff
from the nuclear spin flip-flop interaction Hˆff, Ak ∝ λ ̃ij
ff from
the electron spin-mediated nuclear spin interaction H ̃ff, and Z = (a − a )/2
k i j the energy cost of a pair flip due to the diagonal HFI Sˆzhˆz. Thus, Bk and Dk are nonzero only for neighboring nuclear spins (i.e. local pairs), while Ak remains nonzero even for non-local pairs, but is suppressed under a strong magnetic field. The kth pseudo-spin is described by the Hamiltonian [27–29]
ˆ ( ) ˆ/ ˆ/
()
= ± ± ⋅σ ≡ ⋅σ
±±
H 2B 2A , 0, D Z 2 h 2.
k k k kkk k k
Typically |Z |  |B | ∼ |D |  |A |
k k k k , thus the pseudo-spin dynamics is dominated by its coupling to the central spin. The pseudo-spin description provides a transparent geometric picture for central spin decoherence and its control by DD in terms of Bloch vectors, as well as magic coherence recovery via controlled disentanglement [28, 29].
9.2.1. Non-local and local pair correlations. The pseudospins are separated into two groups, corresponding to local pairs (group GB) with ( )
( )≈ ±
h ± 2B , 0, Z
k k k and non-local pairs (group GA) with ( )
( )≈±
h ± 2A , 0, Z
k k k , respectively. Thus, the centralspincoherenceisfactorizedas L t = L t × L t
J AB
( ) ( ) ( ),
where ( ) ( )
/ G/
≡∏ | |
∈
L t Lt
AB k k
A B . These two kinds of nuclear spin pairs have qualitatively different contributions to electron spin decoherence, for both FID and under DD control. Within the timescale of interest t  1/|B |, 1/|A |
k k , the contributions from local and non-local pairs to the FID are [27–29]
() ( ) ( /) ()
G
∏∫
==
∈
−−
Lt e e ,
A k
t A Zt t S xt x x
2 sinc 2 sinc d
A
kk A
22 2 2
(102)
() ( / ) ( /)
G
∏∫
==
∈
−−
Lt e e ,
k
t BZ Zt t S xtx x x
B 2 sinc 2
1
2 sinc 2 d
kk
k
B
4 22 4 B 2 4
(103)
with
() ( )
G
∑
ω ≡ δ ω−
∈
S Z A,
A k
kk
2
A
(104)
() ( )
G
∑
ω ≡ δ ω−
∈
S Z B,
k
kk
B2
B
(105)
which are the pseudo-spin excitation spectra (see figure 25(b)). In the short time limit (t  1/|Zk|), the decoherence caused by non-local pairs is
( ) (/ )
G≈
∈−
L te ,
k tT
A
2,A 2 (106)
which shows Gaussian decay (red lines in figure 25(a)) on a timescale
G
=
∑∈
T A
1
2
,
A
kk
2, 2
A
(107)
while the decoherence caused by local pairs is
( ) (/ )
G≈
∈−
L te
k tTB
B
2, 4 (108)
which shows quartic decay (blue lines in figure 25(a)) on a timescale
( / )/
G
= ∑∈
T BZ
1
2.
B
k kk
2, 2 2 1 4 B
(109)
Figure 25. (a) Non-Markovian-to-Markovian crossover in electron spin decoherence. The dotted lines are the short-time profile. (b) Excitation spectra for non-local and local nuclear spin pairs. Reproduced with permission from [28]. Copyright 2007 IOP Publishing and Deutsche Physikalische Gesellschaft.
Rep. Prog. Phys. 80 (2017) 016001


 Review
34
Here, the Gaussian decay in equation (106) is actually the expansion of the power-law decay in equation (66) in the short time limit t  Tdyn, and T2,A is equivalent to Tdyn, which is independent of the specific distribution of the HFI coefficients {ai} because the difference a − a
i j is unimportant due to energy-time uncertainty in the short time regime [224]. On longer time scales, the sinc function dictates that only pairs with ω ∈ [−1/t, 1/t] contribute significantly, indicative of an energy conservation condition. For sufficiently large t such that ( )
SA/B ω can be regarded as constant S ̄A/B within [−1/t, 1/t], both |LA(t)| and |LB(t)| show exponential decay (see figure 25(a)) on timescales that depend sensitively on the distribution of the HFI coefficients (since energy conservation becomes important for long time dynamics), in agreement with the ring diagram approximation (see the discussions after equation (67)). The crossover from power-law decay to exponential decay indicates the crossover from the non-Markovian regime (t  1/Zk) to the Markovian regime (t > 1/Zk). Similar results have also been derived by a nonMarkovian master equation approach [224]. For even longer times (which are relevant for a highly polarized spin bath), the decoherence is determined by the complex structure of the collective modes of the bath and becomes very sensitive to the distribution of {ai}, e.g. exponential decay [38] and power-law decay [224, 241, 242] have been predicted. Under DD control, the central spin decoherence caused by non-local nuclear spin pairs are largely suppressed, while the local pairs contributes most to central spin decoherence [27, 28]. Under the Hahn echo control, the central spin coherence at the echo time t = 2τ is [27–29]
( ) ( /) (/) (/)
G
∏∫
τ≈ =
τ τ ττ
∈
−−
L2 e e ,
k
ZB Z S x x x x
H 2 sinc 2 2 sinc 2 d
kk k
B
4 22 4 B 2 4
which shows quartic decay e−(2τ/TH)4 with coherence time TH = 2 T2,B, which is 2 times that of the FID time. This shows that disturbing the central spin state changes the bifurcated bath evolution, which in turn changes the central spin decoherence. At the longer timescale 1/|Z |  τ  1/|B |
k k,
the coherence decays exponentially, indicative of Markovian behavior [27, 28].
9.2.2. Magic coherence recovery. The magic recovery of central spin coherence was predicted for an central electron spin in a nuclear spin bath in the strong field regime (HFI  nuclear Zeeman splitting) [29]. In this case, the noise opera
tor ˆ ˆ
=∑
b aI
jjj
z comes from the isotopic HFI between the
electron spin and the nuclear spins. For nuclear spin-1/2’s, the flip-flop | ↑ ⟩ | ↓ ⟩ ↔ | ↓ ⟩ | ↑ ⟩
i j i j of each nuclear spin pair k ≡ (i, j) is mapped to the precession of the kth pseudo-spin
σk: |⇑⟩ ≡ | ↑ ⟩ | ↓ ⟩
k i j and |⇓⟩ ≡ | ↓ ⟩ | ↑ ⟩
k i j. The pseudo-spin field
is /
( )= ±
h± h h 2
kk
B k
b with h = X e + Z e
k
B k
Bx k
B z and h = Z e
k
b k
b z,
where Xk , Z
B k
B are the intrinsic nuclear spin flip-flop amplitude and energy cost, respectively, due to nuclear dipolar interactions, while Zk
b is the HFI induced correction to the energy cost.
The bifurcated evolution | ⟩ → | ±( )⟩
J J t of the pseudo-spin starting from a pure state (say |J〉 = |⇑〉) can be mapped to Bloch vectors σ±(t) and the central spin decoherence is determined by their distance = |σ − σ |
+−
d(t) (t) (t) (see the appendix). When Z = 0
k
B , the fields ( )
( )= ±
h ± X , 0, Z
kk
B k
b lead to a t2 increase of d(t) in the short time limit, while the application of a π pulse at time τ reverses the evolution direction and
gives rise to coherence recovery at the magic time t = 2 τ
mag
instead of the echo time t = 2τ
d (see the appendix). Here, the presence of Zk
B does not change the t2 increase of d(t), so it shows the same magic coherence recovery (see figures 26(b) and (c)). More generally, under an arbitrary DD characterized by the modulation function s(t), the distance
() ( )
() ∫
∝ ′′ ′
d t t s t dt
t
1
0 (110)
vanishes (and hence coherence recovery occurs) at the
magic time tmag as determined by ( )
∫ ts t dt = 0
t
0
mag , e.g.
t = N(N + 1) τ
mag for the DD consisting of N equally spaced π-pulses τk = τ (see figures 26(a) and (d)). By contrast, in the absence of intrinsic bath dynamics (h = 0
k
B ), the distance d(t) ∝ t. Under DD control, the distance
() ( )
() ∫
∝ ′′
d t s t dt
t
0
0 (111)
vanishes at the echo time t = 2τ
d , corresponding to the elimination of inhomogeneous dephasing at the echo time. Equations (110) and (111) are reminiscent of the Taylor expansion of the classical random phase φ ̃(td) =
∫∫
≈∑
s t b t dt b s t t dt
t
nn
tn 00
dd
( )  ̃( )  ̃ ( ) based on  ̃( )  ̃
=∑
bt bt
n n n. For a pure initial state of the bath (no classical analog), the low
est-order term d (0)(t) is absent, so d (1)(t) = 0 gives rise to magic coherence recovery at tmag, suggesting that elimination of the coupling to the environment is not a necessary condition for the recovery of coherence. For a thermal initial state of the bath, since the time-averaged coupling between the central spin and the bath is nonzero at the magic time in the first order, the rapid inhomogeneous dephasing will prevent magic coherence recovery from being observed. Direct observation of magic coherence recovery is possible once the inhomogeneous nuclear spin distribution is narrowed, e.g. a projective measurement of the noise operator bˆ could be used to limit the nuclear spin configurations by post-selection [56–58].
9.2.3. Anomalous decoherence effects. An important feature of classical decoherence theories is that different processes coupled to the same noise source have similar decoherence behaviors and stronger noises cause faster decoherence. However, this is not the case in the quantum picture, since stronger coupling to the environment allows DD control to strongly manipulate the environmental dynamics to recover the lost coherence. For example, the spin-1 electronic state of the NV center in diamond with eigenstates {|m⟩} (m = 0, ± 1)
is subjected to noises from the 13C nuclear spin bath. Surprisingly, under DD control, the double transition |+1⟩ ↔ |−1⟩ could have longer coherence time than the single transition
Rep. Prog. Phys. 80 (2017) 016001


 Review
35
|0⟩ ↔ | ± 1⟩, even though the noise amplitude for the former is twice that for the latter [95, 96]. This anomalous decoherence effect can be understood from the manipulation of pseudospin evolutions via DD control of the central spin. In the semi-classical noise picture, the nuclear spin bath can be described as a random fluctuating local field [25, 26]. For Gaussian noise [70, 92, 97], the central spin decoherence
for the transition |m⟩ ↔ |n⟩ is ( ) ( ) ⟨  ̃ ( )⟩/
=−− φ
Lt e
mn m n t
,2
2 2 , which obeys the scaling relation
| |=| |
+− ±
L t L t,
1, 1 0, 1 4
( ) ( ) (112)
We can see that decoherence of a double transition L+1, −1(t) decays in the same way as that of single transitions ( )
±
Lt
0, 1 ,
but is faster. The scaling relation in equation (112) remains valid when the electron spin is subjected to arbitrary DD control. However, numerical calculations in the quantum picture shows that under DD control with more and more π pulses, the classical scaling relation in equation (112) is violated more and more significantly, and finally the double quantum coherence even decays slower than the single quantum coherence (see figure 27(b)). This counterintuitive effect can be understood by analyzing the microscopic nuclear spin bath evolution ˆ ( ) ˆ
≡−
Ut e
m iHmt conditioned on the central spin state, where ˆ ˆ ˆ
H ≡ H + mb
m B . Under a moderate magnetic field ( 0.1 T) along the N-V symmetry axis (z axis), the flip of individual nuclear spins is suppressed by the large nuclear Zeeman splitting, so the elementary excitation of the nuclear spins is the flip-flop of nuclear spin pairs, which can be mapped to the precession of non-interacting pseudo-spins with the effective Hamiltonian conditioned on the electron spin state,
ˆ ˆ ( )ˆ
()
∑∑
H = h ⋅ σ = h + mh ⋅ σ .
m k
k
mk
k
k
B k
bk
eff
where h = Z e
k
b k z comes from the HFI (Z ≡ 〈⇑|bˆ|⇑〉
kk k
b
kk
− 〈⇓| ˆ|⇓〉 ) and h = X e
k
B k x is from the nuclear dipolar interaction (X ≡ 2 ⟨⇑|Hˆ |⇓⟩
kk k
B ), so the coupling to the central spin dominates the bath dynamics (h  h
k
b k
B). According to equation (101), the Hahn echo of electron spin coherence for the transition |m⟩ ↔ |n⟩ is
()
( ) ()
⎡
⎣⎢ ⎤
⎦⎥
∏
τ ττ
L = −Θ h h
2 1 2 sin sin 2 sin 2 ,
mn
k
k
mn k
m k
n
,
H 2, 2 2
Figure 26. (a) Bifurcated trajectories of pseudo-spin Bloch vectors under the control of a sequence of equally spaced π-pulses. (b) similar to (a) but for the CPMG-2 control. (c) ‘True’ decoherence under Hahn echo control, with the π-pulse applied at τ = 17 μs (indicated by
the blue arrow). (d) Contour plot of ‘true’ decoherence under the Hahn echo versus evolution time t and pulse delay time τ. The left tilted
dashed line indicates t = τ. The right tilted dashed line indicates the echo time t =2τ. The horizontal line is the cut for the curve in (c). (e) ‘True’ decoherence under a sequence of π-pulses (indicated by purple vertical lines) at intervals of 10 μs. Panels (a) and (b) are reproduced with permission from [28], copyright 2007 IOP Publishing and Deutsche Physikalische Gesellschaft. Panels (c)–(e) are reproduced with permission from [29]. Copyright 2007 by the American Physical Society.
Figure 27. (a) Measured single (black line with square symbols) and double (red line with circle symbols) quantum coherence, under the control of different numbers of equally spaced pulses (CPMG-1, CPMG-2 and CPMG-5, from top to bottom). The scaled single quantum coherence | + |
L0, 1 4 (blue line with triangle symbols) is also shown for comparison. (b) The theoretical results, plotted in the same format as in (a). Adapted by permission from Macmillan Publishers Ltd: [96]. Copyright 2011.
Rep. Prog. Phys. 80 (2017) 016001


 Review
36
where Θk
m,n is the angle between ( )
hk
m and ( )
hk
n . The decay in the short time limit is
() / ( ) /
( ) ()
∏∏
τ≈ =
−| × | τ − − | × | τ
L2 e e ,
mn kk
h h mn h h
,
H 88
k
m k
n k
B k
b
24 2 24
which obeys the classical scaling in equation (112). At a longer timescale, however, the strong coupling to the central
spin makes the two fields of ( τ)
+−
L2
1, 1
H nearly antiparallel
(sin Θ+ −  1)
k
1, 1 , while those of the single quantum coherence are nearly perpendicular ( Θ ≈ )
±
sin 1
k
0, 1 . Consequently, the long time decay of the double quantum coherence is much smaller than that of the single quantum coherence, thus violating equation (112) at longer times. The application of more π pulses prolongs the electron spin coherence time and makes this long time behavior more pronounced. This anomalous decoherence has been experimentally observed by Huang et al in type-IIa diamond at room temperature [96]. In the experimental setup, the magnetic field is weak, so the electron spin decoherence is mainly caused by the single 13C nuclear spin dynamics, quite similar to the pseudo-spin dynamics discussed above.
9.3. Multi-spin correlation effects
The effects of multi-spin correlations on central spin decoherence become pronounced when the coherence time is prolonged to be comparable or longer than the inverse of typical nuclear-nuclear interaction, which can be realized by applying multi-pulse DD control [111, 207, 217] or tuning
the external magnetic field near some optimal working points [97, 218, 219] (also called ‘clock’ transitions [107] where the central spin is insensitive to the magnetic noise in the first order). The CCE method can explicitly show the contributions of different multi-spin clusters in the nuclear spin bath to central spin decoherence, providing an intuitive tool to identify the underlying nuclear spin processes. For NV centers in diamond and donor spins in silicon, the CCE-2 calculations (truncated up to the clusters with two nuclear spins) always give converged results for the Hahn echo of spin coherence [111, 218], indicating the pairwise flip-flop processes dominate the central spin decoherence. For central spin decoherence under multi-pulse DD control [111] or near the optimal working points in silicon [97, 219] , the CCE-6 calculations (truncated up to the clusters with six nuclear spins) are always needed to give converged results, indicating that the multi-spin correlations contributes significantly to central spin decoherence. More interestingly, recent studies show that DD control of the central spin can selectively suppress or amplify certain many-body processes in the nuclear spin bath [207]. In this case, LCE provides a systematic and transparent way to visualize the gradual development of different many-body processes in a nanoscale spin bath, by analyzing the individual influence of each LCE diagram on the central spin decoherence [32]. For example, consider a central electron spin in a relatively large nuclear spin bath with a strong external magnetic field and the HFI between the central spin and bath spins much larger than the nuclear–nuclear interactions, such as shallow donors in silicon (e.g. Si:P and Si:Bi) and electron
Figure 28. Revealing many-body correlations in nuclear spin baths by central spin decoherence. (a) Electron spin of a phosphorus donor in silicon interacts with a bath of 29Si nuclear spin-1/2s possessing various many-body processes. (b) topologically inequivalent connected Feynman diagrams corresponding to different many-body processes in the nuclear spin bath: (I) V2—second-order pairwise flip-flop, (II–V) V4z—fourth-order pairwise flip-flop dressed by diagonal interactions. (c) Measured (solid lines) and calculated (dashed lines) coherence
of the P-donor electron spin in the natural 29Si nuclear spin bath under CPMG control. (d) Comparisons of the experimental (solid lines) and theoretical (dashed line) decay times TSD (blue) and stretched exponents n (magenta) of the central spin decoherence under the CPMG control in (c). Reproduced by permission from Macmillan Publishers Ltd: [207]. Copyright 2014.
Rep. Prog. Phys. 80 (2017) 016001


 Review
37
spin in semiconductors (e.g. GaAs and InAs quantum dots). For CPMG-N (or UDD-N) control of the central spin with odd N, the second-order pairwise flip-flop diagram (V2 term in figure 28(b)) dominates the central spin decoherence and almost fully reproduces the exact decoherence calculated from CCE, while for CPMG-N control with even N, the effects of the second-order pairwise flip-flop diagram are canceled and the fourth-order flip-flop diagrams (V4z terms in figure 28(b)), corresponding to a renormalized pairwise flip-flop dressed by the diagonal interactions (or pairwise flip-flop processes of two nuclear spins renormalized the dipolar diagonal interaction with the other nuclear spins in the bath), dominates the decoherence. This even-odd effect indicates that the secondorder flip-flop (V2 term figure 28(b)) and fourth-order flip-flop processes (V4z term in figure 28(b)) can be selectively detected by applying an appropriate number of DD pulses, as has been theoretically predicted and experimentally observed recently in a Si:P system [207]. Actually, a similar even-odd effect has been noticed before in cluster expansion calculations [217] (without analyzing the underlying microscopic processes): in the presence of an even (odd) number of DD pulses, the decoherence scale as ln L = O(λ4) [ln L = O(λ2)] with respect to the dipolar interaction strength λ between bath spins. In
the experiment [207], the measured decoherence e−(t/TSD)n caused by 29Si nuclei has a stretching factor n oscillating between about 2 (for odd N) and 4 (for even N), as shown in figures 28(c) and (d), indicating the detection of either the second-order flip-flop processes or fourth-order flip-flop processes. The different signatures of the many-body processes in the bath under DD control of the central spin, in particular the even-odd effect in the number of DD control pulses, provide a useful approach to studying many-body physics in the nuclear spin bath.
10. Summary and outlook
Central electron spin decoherence in nanoscale nuclear spin baths is a critical issue for quantum technologies. In recent years, quantum pictures and quantum many-body theories have been established and have provided a quantitative description and unprecedented understanding of the central spin decoherence under many experimental conditions (such as DD control and moderate to strong magnetic fields). Accompanying the great progresses in prolonging the central spin coherence time through various DD schemes, the coherent evolution of the central spin in turn serves as an ultrasensitive probe for weak signals [178–180, 247, 248] and many-body dynamics in the environments [249–254] with nanoscale resolution. When the semi-classical noise model and especially the noise filter description are valid [97], central spin decoherence under DD control has been used to reconstruct the environmental noise spectra [98–101], which in turn can be used to design optimal quantum control for protecting the quantum coherence and quantum gates [70]. In particular, the decay of the central spin coherence on very long timescales (up to seconds [97]) allows study of the low-energy excitations in the environment, since as the evolution time t increases, the
noises that cause significant central spin decoherence have frequencies ∼1/t. Central spin decoherence under DD control has also been widely used for quantum sensing of single nuclear spins [15, 16]. When the period of the DD control matches the transition frequencies of the target nuclear spin(s) [16], the noises from the target nuclear spins are resonantly amplified, causing enhanced central spin decoherence (manifested as a sharp coherence dip when sweeping the DD period). Several groups have adopted the DD scheme to successfully detect single 13C nuclear spins [17, 255, 256] and 13C clusters [216] in diamond. Shallow NV centers near the surface have also been used to sense the NMR of single protein molecules [257] and nano-scale NMR of nuclear species [258, 259] on diamond surfaces. Recently, there are also new proposals and concepts for quantum sensing, such as using multiple NV spins as the quantum sensor [260], distinguishing nuclear spins of different species by sweeping the DD pulse number [261], and design of multi-dimensional DD to distinguish the nuclear spin correlations in single molecules [262, 263]. Another promising avenue is to employ the central spin decoherence to reveal the many-body physics and thermodynamic properties of the environment, since in some cases the central spin decoherence caused by the environment is directly related to the partition function of the environment. It has been found that central spin coherence shows sharp decay when the environment is tuned near a quantum critical point [249, 250]. For a central spin homogenously coupled to a ferromagnetic Ising model, the central spin coherence vanishes at times corresponding to the Lee-Yang zeros of the partition function of the Ising model [251, 252]. Moreover, central spin decoherence has extended the phase transitions in the environment to the complex plane of physical parameters [253] and enabled thermodynamic holographs of the partition function of the environment [254].
Acknowledgments
We acknowledge support by Hong Kong RGC/GRF, Hong Kong RGC-ANR Joint Scheme, CUHK Vice Chancellor’s One-off Discretionary Fund, the NSFC (Grant No. 11274036 and No. 11322542), the MOST (Grant No. 2014CB848700), NSFC program for 'Scientific Research Center' (Program No. U1530401), and computational support from the Beijing Computational Science Research Center (CSRC).
Appendix. Bloch vector representation of single spin dynamics
We consider that the bath consists of a single spin-1/2, which starts from a pure spin-up state |J〉 = |⇑〉 along the z axis and
bifurcates into two pathways ( )⟩ ⟩
ˆ
|=|
± −±
J t e iH t J with
ˆ ˆ ˆ/ ( ) σˆ
=± = ± ⋅
H± H b h h
2 2 2.
b BB
The pathways can be mapped to the Bloch vectors
σ ( ) ≡ ⟨ ( )|σˆ | ( )⟩
± ±±
t J t J t , which start from ez at t = 0 and then undergo Larmor precession around the fields h± on a unit
Rep. Prog. Phys. 80 (2017) 016001


 Review
38
sphere. The central spin decoherence |L(t)| = 1 − d (t)/4
2 2 is
determined by the distance ( ) =|σ ( ) − σ ( )|
+−
d t t t between the Bloch vectors [27, 28]. To visualize the bifurcated bath evolution, we consider two special cases: (A) = ( ± )
h± X, 0, Z and (B) = ( ± )
h± X, 0, Z . In either case, the bath spin pre
cesses with angular frequency h = X + Z
2 2 on a circle of
radius sin θ = X /h. For case (A), the FID
( ) ⟶/ /
=− θ −

L t ht t h
1 2 sin sin 2
2 2 1 e Xt 2
22
shows Gaussian decay in the short time limit, corresponding to a linear increase of the distance d(t) ≈ 2Xt with time (figures A1(a) and (c)). At t = π/h, the distance is maximal d = 2 sin(2θ)
max and the coherence is minimal: L = cos(2θ)
min . Under the Hahn echo control, the distance in the short time limit is d (t) ≈ 2X(τ − (t − τ))
H , so central spin decoherence is minimized at the echo time
t = 2τ.
d (A.1)
For case (B), the FID [27, 28]
() ( )
⟶/ ( / ) /
=− θ − θ
−− −

L t ht i ht
th
1 2 cos sin 2 cos sin
1 e Zt X t Z X t
22
i1 6 8
22 2 24
exhibits t4 decay in the short time limit, corresponding to a quadratic increase of the distance d(t) ≈ XZt2 with time (figures A1(b) and (d)). At t = π/h, the distance is maximal d = 2 sin(2θ)
max and the coherence is minimal: L = cos(2θ)
min .
Under Hahn echo control, the distance in the short time limit is d (t) ≈ [(τ − (t − τ ))]XZ
H 2 2 2 , so central spin decoherence is minimized at the magic time:
t = 2 τ.
mag (A.2)
The different coherence recovery times (equations (A.1) and (A.2)) follow from the different time dependences of the Bloch vector distances: d(t) ∝ t for case (A) and d(t) ∝ t2 for case (B). For case (A) (figure A1(c)), the Bloch vectors σ±(t) move in opposite directions with almost constant velocity X. After the π pulse, both Bloch vectors reverse their velocities, so minimal distance occurs at 2τ. For case (B) (figure A1(d)), both Bloch vectors move away from the −y axis quadratically with time, e.g. the distance of each Bloch vector from the −y axis reaches τ2 at t = τ. If there were no π pulses at τ, then evolution from τ to 2 τ would double the distance to 2τ2. Now, the π pulse reverses the evolution direction of both Bloch vectors, so σ±(t) both return to the −y axis at 2 τ. Such coherence recovery at a ‘magic’ time (i.e. different from the echo time) was first predicted in [28, 29] and is discussed in more detail in section 9.2.2.
References
[1] Benioff P 1980 J. Stat. Phys. 22 563 [2] Feynman R 1982 Int. J. Theor. Phys. 21 467 [3] Deutsch D 1985 Proc. R. Soc. A 400 97 [4] Bennett C H and Brassard G 1984 Proc. Int. Conf. Comput. Syst. Signal Process. (Bangalore, India) vol 175 p 8
[5] Gisin N, Ribordy G, Tittel W and Zbinden H 2002 Rev. Mod. Phys. 74 145
[6] Caves C M 1981 Phys. Rev. D 23 1693 [7] Budker D and Romalis M 2007 Nat. Phys. 3 227 [8] Giovannetti V, Lloyd S and Maccone L 2011 Nat. Photon. 5 222 [9] DiVincenzo D P 1995 Science 270 255 [10] Ladd T D, Jelezko F, Laflamme R, Nakamura Y, Monroe C and O’Brien J L 2010 Nature 464 45 [11] Leggett A J, Chakravarty S, Dorsey A T, Fisher M P A, Garg A and Zwerger W 1987 Rev. Mod. Phys. 59 1 [12] Prokof’ev N V and Stamp P C E 2000 Rep. Prog. Phys. 63 669 [13] Zurek W H 2003 Rev. Mod. Phys. 75 715
Figure A1. Larmor precession of the Bloch vectors σ±(t) of the two bath pathways around (a) = ( ± )
h± X, 0, Z and (b) = ( ± )
h± X, 0, Z . (c) and (d) are the correspondings projection of the Bloch vectors in the xoy plane.
Rep. Prog. Phys. 80 (2017) 016001


 Review
39
[14] Abragam A 1961 The Principles of Nuclear Magnetism (New York: Oxford University Press) [15] Cole J H and Hollenberg L C L 2009 Nanotechnology 20 495401 [16] Zhao N, Hu J-L, Ho S-W, Wan J T K and Liu R-B 2011 Nat. Nanotechnol. 6 242
[17] Zhao N, Honert J, Schmid B, Klas M, Isoya J, Markham M, Twitchen D, Jelezko F, Liu R-B, Fedder H and Wrachtrup J 2012 Nat. Nano 7 657
[18] Rondin L, Tetienne J-P, Hingant T, Roch J-F, Maletinsky P and Jacques V 2014 Rep. Prog. Phys. 77 056503 [19] Moore G E 1965 Electronics 38 114 [20] Hanson R and Awschalom D D 2008 Nature 453 1043 [21] Hanson R, Kouwenhoven L P, Petta J R, Tarucha S and Vandersypen L M K 2007 Rev. Mod. Phys. 79 1217 [22] Morton J J L, McCamey D R, Eriksson M A and Lyon S A 2011 Nature 479 345 [23] Awschalom D D, Epstein R and Hanson R 2007 Sci. Am. 84 297 [24] Anderson P W and Weiss P R 1953 Rev. Mod. Phys. 25 269 [25] Anderson P W 1954 J. Phys. Soc. Japan 9 316 [26] Kubo R 1954 J. Phys. Soc. Japan 9 935
[27] Yao W, Liu R-B and Sham L J 2006 Phys. Rev. B 74 195301 [28] Liu R-B, Yao W and Sham L J 2007 New J. Phys. 9 226 [29] Yao W, Liu R-B and Sham L J 2007 Phys. Rev. Lett. 98 077602 [30] Witzel W M, de Sousa R and Das Sarma S 2005 Phys. Rev. B 72 161306 [31] Witzel W M and Das Sarma S 2006 Phys. Rev. B 74 035322 [32] Saikin S K, Yao W and Sham L J 2007 Phys. Rev. B 75 125314 [33] Yang W and Liu R B 2008 Phys. Rev. B 77 085302 [34] Yang S, Gong M, Li C, Zou X and Guo G 2009 Phys. Rev. B 80 235322 [35] Maze J R, Taylor J M and Lukin M D 2008 Phys. Rev. B 78 094303 [36] Hall L T, Cole J H and Hollenberg L C L 2014 Phys. Rev. B 90 075201 [37] Cywiński L, Witzel W M and Das Sarma S 2009 Phys. Rev. Lett. 102 057601
[38] Cywiński L, Witzel W M and Das Sarma S 2009 Phys. Rev. B 79 245314 [39] Elzerman J M, Hanson R, Willems van Beveren L H, Witkamp B, Vandersypen L M K and Kouwenhoven L P 2004 Nature 430 431 [40] Hanson R, van Beveren L H W, Vink I T, Elzerman J M, Naber W J M, Koppens F H L, Kouwenhoven L P and Vandersypen L M K 2005 Phys. Rev. Lett. 94 196802 [41] Barthel C, Reilly D J, Marcus C M, Hanson M P and Gossard A C 2009 Phys. Rev. Lett. 103 160503 [42] Morello A et al 2010 Nature 467 687 [43] Neumann P, Beck J, Steiner M, Rempp F, Fedder H, Hemmer P R, Wrachtrup J and Jelezko F 2010 Science 329 542
[44] Vamivakas A N, Lu C-Y, Matthiesen C, Zhao Y, Falt S, Badolato A and Atature M 2010 Nature 467 297 [45] Robledo L, Childress L, Bernien H, Hensen B, Alkemade P F A and Hanson R 2011 Nature 477 574 [46] Delteil A, Gao W-b, Fallahi P, Miguel-Sanchez J and Imamoğlu A 2014 Phys. Rev. Lett. 112 116802 [47] Waldherr G et al 2014 Nature 506 204 [48] Shulman M D, Harvey S P, Nichol J M, Bartlett S D, Doherty A C, Umansky V and Yacoby A 2014 Nat. Commun. 5 5156
[49] Delbecq M R et al 2016 Phys. Rev. Lett. 116 046802 [50] Dobrovitski V V, Feiguin A E, Awschalom D D and Hanson R 2008 Phys. Rev. B 77 245212 [51] Hahn E L 1950 Phys. Rev. 80 580 [52] Jelezko F, Gaebel T, Popa I, Gruber A and Wrachtrup J 2004 Phys. Rev. Lett. 92 076401
[53] Coish W A and Loss D 2004 Phys. Rev. B 70 195340 [54] London P et al 2013 Phys. Rev. Lett. 111 067601 [55] Liu G-Q, Jiang Q-Q, Chang Y-C, Liu D-Q, Li W-X, Gu C-Z, Po H C, Zhang W-X, Zhao N and Pan X-Y 2014 Nanoscale 6 10134 [56] Giedke G, Taylor J M, D’Alessandro D, Lukin M D and Imamoğlu A 2006 Phys. Rev. A 74 032316 [57] Klauser D, Coish W A and Loss D 2006 Phys. Rev. B 73 205302 [58] Stepanenko D, Burkard G, Giedke G and Imamoglu A 2006 Phys. Rev. Lett. 96 136401
[59] Cappellaro P 2012 Phys. Rev. A 85 030301 [60] Greilich A, Shabaev A, Yakovlev D R, Efros A L, Yugova I A, Reuter D, Wieck A D and Bayer M 2007 Science 317 1896
[61] Xu X, Yao W, Sun B, Steel D G, Bracker A S, Gammon D and Sham L J 2009 Nature 459 1105 [62] Sun B, Chow C M E, Steel D G, Bracker A S, Gammon D and Sham L J 2012 Phys. Rev. Lett. 108 187401 [63] Latta C et al 2009 Nat. Phys. 5 758 [64] Bluhm H, Foletti S, Mahalu D, Umansky V and Yacoby A 2010 Phys. Rev. Lett. 105 216803
[65] Togan E, Chu Y, Imamoglu A and Lukin M D 2011 Nature 478 497
[66] Yang W and Sham L J 2013 Phys. Rev. B 88 235304 [67] Joos E, Zeh H D, Kiefer C, Giulini D, Kupsch J and
Stamatescu I-O 2003 Decoherence and the Appearance of a Classical World in Quantum Theory (New York: Springer) (doi:10.1007/978-3-662-05328-7) [68] Dobrovitski V V, Feiguin A E, Hanson R and Awschalom D D 2009 Phys. Rev. Lett. 102 237601
[69] Witzel W M, Carroll M S, Cywiński L and Das Sarma S 2012 Phys. Rev. B 86 035452
[70] Witzel W M, Young K and Das Sarma S 2014 Phys. Rev. B 90 115431 [71] de Lange G, Wang Z H, Riste D, Dobrovitski V V and Hanson R 2010 Science 330 60 [72] Uhrig G S 2007 Phys. Rev. Lett. 98 100504 [73] Klauder J R and Anderson P W 1962 Phys. Rev. 125 912 [74] Bloembergen N, Purcell E M and Pound R V 1948 Phys. Rev. 73 679
[75] de Sousa R and Das Sarma S 2003 Phys. Rev. B 67 033301 [76] de Sousa R and Das Sarma S 2003 Phys. Rev. B 68 115322 [77] de Sousa R, Shenvi N and Whaley K B 2005 Phys. Rev. B 72 045330 [78] Chiba M and Hirai A 1972 J. Phys. Soc. Japan 33 730 [79] Tyryshkin A M, Lyon S A, Astashkin A V and Raitsimring A M 2003 Phys. Rev. B 68 193207 [80] Abe E, Itoh K M, Isoya J and Yamasaki S 2004 Phys. Rev. B 70 033204 [81] Ferretti A, Fanciulli M, Ponti A and Schweiger A 2005 Phys. Rev. B 72 235201 [82] Tyryshkin A M, Morton J J L, Benjamin S C, Ardavan A, Briggs G A D, Ager J W and Lyon S A 2006 J. Phys.: Condens. Matter 18 S783
[83] de Sousa R 2009 Top. Appl. Phys. 115 183
[84] Mehring M 1983 Principles of High Resolution NMR in Solids 2nd edn (Berlin: Springer) (doi:10.1007/978-3-642-68756-3) [85] Rhim W-K, Pines A and Waugh J S 1970 Phys. Rev. Lett. 25 218
[86] Haeberlen U 1976 High Resolution NMR in Solids: Selective Averaging (New York: Academic) [87] Viola L and Lloyd S 1998 Phys. Rev. A 58 2733 [88] Ban M 1998 J. Mod. Opt. 45 2315 [89] Zanardi P 1999 Phys. Lett. A 258 77 [90] Viola L, Knill E and Lloyd S 1999 Phys. Rev. Lett. 82 2417 [91] Yang W, Wang Z-Y and Liu R-B 2011 Front. Phys. 6 2
Rep. Prog. Phys. 80 (2017) 016001


 Review
40
[92] Cywinski L, Lutchyn R M, Nave C P and Das Sarma S 2008 Phys. Rev. B 77 174509
[93] Carr H and Purcell E M 1954 Phys. Rev. 94 630 [94] Meiboom S and Gill D 1958 Rev. Sci. Instrum. 29 688 [95] Zhao N, Wang Z-Y and Liu R-B 2011 Phys. Rev. Lett. 106 217205 [96] Huang P, Kong X, Zhao N, Shi F, Wang P, Rong X, Liu R-B and Du J 2011 Nat. Commun. 2 570 [97] Ma W-L, Wolfowicz G, Li S-S, Morton J J L and Liu R-B 2015 Phys. Rev. B 92 161403 [98] Álvarez G A and Suter D 2011 Phys. Rev. Lett. 107 230501 [99] Bar-Gill N, Pham L, Belthangady C, Le Sage D, Cappellaro P, Maze J, Lukin M, Yacoby A and Walsworth R 2012 Nat. Commun. 3 858
[100] Bylander J, Gustavsson S, Yan F, Yoshihara F, Harrabi K, Fitch G, Cory D G, Nakamura Y, Tsai J-S and Oliver W D 2011 Nat. Phys. 7 565
[101] Cywiński L 2014 Phys. Rev. A 90 042307 [102] Muhonen J T et al 2014 Nat. Nano 9 986 [103] Hanson R, Dobrovitski V V, Feiguin A E, Gywat O and Awschalom D D 2008 Science 320 352 [104] Wang Z-H and Takahashi S 2013 Phys. Rev. B 87 115122 [105] Reinhard F et al 2012 Phys. Rev. Lett. 108 200402 [106] Liu G-Q, Pan X-Y, Jiang Z-F, Zhao N and Liu R-B 2012 Sci. Rep. 2 432
[107] Wolfowicz G, Tyryshkin A M, George R E, Riemann H, Abrosimov N V, Becker P, Pohl H-J, Thewalt M L W, Lyon S A and Morton J J L 2013 Nat. Nano 8 561 [108] Yang W and Liu R-B 2008 Phys. Rev. B 78 085315 [109] Yang W and Sham L J 2012 Phys. Rev. B 85 235319 [110] Brune M, Hagley E, Dreyer J, Maitre X, Maali A, Wunderlich C, Raimond J M and Haroche S 1996 Phys. Rev. Lett. 77 4887
[111] Zhao N, Ho S-W and Liu R-B 2012 Phys. Rev. B 85 115303 [112] Khaetskii A V and Nazarov Y V 2000 Phys. Rev. B 61 12639 [113] Khaetskii A V and Nazarov Y V 2001 Phys. Rev. B 64 125316 [114] Woods L M, Reinecke T L and Lyanda-Geller Y 2002 Phys. Rev. B 66 161318 [115] Golovach V N, Khaetskii A and Loss D 2004 Phys. Rev. Lett. 93 016601 [116] Semenov Y G and Kim K W 2004 Phys. Rev. Lett. 92 026601 [117] Pyykko P 2008 Mol. Phys. 106 1965 [118] Paget D, Lampel G, Sapoval B and Safarov V I 1977 Phys. Rev. B 15 5780
[119] Coish W A and Baugh J 2009 Phys. Status Solidi B 246 2203 [120] Feher G 1959 Phys. Rev. 114 1219 [121] Richard S, Aniel F and Fishman G 2004 Phys. Rev. B 70 235204 [122] Zwanenburg F A, Dzurak A S, Morello A, Simmons M Y, Hollenberg L C L, Klimeck G, Rogge S, Coppersmith S N and Eriksson M A 2013 Rev. Mod. Phys. 85 961 [123] Shulman R G and Wyluda B J 1956 Phys. Rev. 103 1127 [124] Fischer J, Coish W A, Bulaev D V and Loss D 2008 Phys. Rev. B 78 155329 [125] Testelin C, Bernardot F, Eble B and Chamarro M 2009 Phys. Rev. B 79 195440 [126] Chekhovich E A, Krysa A B, Skolnick M S and Tartakovskii A I 2011 Phys. Rev. Lett. 106 027402 [127] Chekhovich E A, Glazov M M, Krysa A B, Hopkinson M, Senellart P, Lemaitre A, Skolnick M S and Tartakovskii A I 2013 Nat. Phys. 9 74 [128] Chesi S, Wang X J and Coish W A 2014 Eur. Phys. J. Plus 129 1
[129] Slichter C P 1990 Principles of Magnetic Resonance (Berlin: Springer) (doi:10.1007/978-3-662-09441-9) [130] Bloembergen N and Rowland T J 1955 Phys. Rev. 97 1679 [131] Shulman R G, Mays J M and McCall D W 1955 Phys. Rev. 100 692
[132] Shulman R G, Wyluda B J and Anderson P W 1957 Phys. Rev. 107 953
[133] Shulman R G, Wyluda B J and Hrostowski H J 1958 Phys. Rev. 109 808
[134] Sundfors R K 1969 Phys. Rev. 185 458 [135] Sinitsyn N A, Li Y, Crooker S A, Saxena A and Smith D L 2012 Phys. Rev. Lett. 109 166605
[136] Chekhovich E A, Kavokin K V, Puebla J, Krysa A B, Hopkinson M, Andreev A D, Sanchez A M, Beanland R, Skolnick M S and Tartakovskii A I 2012 Nat. Nano 7 646 [137] Chekhovich E A, Hopkinson M, Skolnick M S and Tartakovskii A I 2015 Nat. Commun. 6 6348 [138] Botzem T, McNeil R P G, Mol J-M, Schuh D, Bougeard D and Bluhm H 2016 Nat. Commun. 7 11170 [139] Kastner M A 1993 Phys. Today 46 24 [140] Loss D and DiVincenzo D P 1998 Phys. Rev. A 57 120 [141] Gupta J A, Awschalom D D, Peng X and Alivisatos A P 1999 Phys. Rev. B 59 R10421
[142] Kane B E 1998 Nature 393 133 [143] George R E, Witzel W, Riemann H, Abrosimov N V, Nötzel N, Thewalt M L W and Morton J J L 2010 Phys. Rev. Lett. 105 067601
[144] Gruber A, Dräbenstedt A, Tietz C, Fleury L, Wrachtrup J and Borczyskowski C V 1997 Science 276 2012 [145] Doherty M W, Manson N B, Delaney P, Jelezko F, Wrachtrup J and Hollenberg L C 2013 Phys. Rep. 528 1
[146] Bulaev D V and Loss D 2005 Phys. Rev. Lett. 95 076805 [147] Imamoğlu A, Awschalom D D, Burkard G, DiVincenzo D P, Loss D, Sherwin M and Small A 1999 Phys. Rev. Lett. 83 4204 [148] Kouwenhoven L P, Austing D G and Tarucha S 2001 Rep. Prog. Phys. 64 701
[149] Reimann S M and Manninen M 2002 Rev. Mod. Phys. 74 1283 [150] Warburton R J 2013 Nat. Mater. 12 483 [151] Gammon D, Shanabrook B V and Katzer D S 1991 Phys. Rev. Lett. 67 1547
[152] Khaetskii A V, Loss D and Glazman L 2002 Phys. Rev. Lett. 88 186802 [153] Merkulov I A, Efros A L and Rosen M 2002 Phys. Rev. B 65 205309 [154] Petta J R, Johnson A C, Taylor J M, Laird E A, Yacoby A, Lukin M D, Marcus C M, Hanson M P and Gossard A C 2005 Science 309 2180 [155] Greilich A, Yakovlev D R, Shabaev A, Efros A L, Yugova I A, Oulton R, Stavarache V, Reuter D, Wieck A and Bayer M 2006 Science 313 341 [156] Koppens F H L, Nowack K C and Vandersypen L M K 2008 Phys. Rev. Lett. 100 236802
[157] Bluhm H, Foletti S, Neder I, Rudner M, Mahalu D, Umansky V and Yacoby A 2011 Nat. Phys. 7 109 [158] Malinowski F K, Martins F, Nissen P D, Barnes E, Rudner M S, Fallahi S, Gardner G C, Manfra M J, Marcus C M and Kuemmeth F 2016 arXiv:1601.06677 [cond-mat.mes-hall] [159] Maune B M et al 2012 Nature 481 344 [160] Vrijen R, Yablonovitch E, Wang K, Jiang H W, Balandin A, Roychowdhury V, Mor T and DiVincenzo D 2000 Phys. Rev. A 62 012306 [161] Barrett S D and Milburn G J 2003 Phys. Rev. B 68 155307 [162] Hollenberg L C L, Dzurak A S, Wellard C, Hamilton A R, Reilly D J, Milburn G J and Clark R G 2004 Phys. Rev. B 69 113301 [163] Skinner A J, Davenport M E and Kane B E 2003 Phys. Rev. Lett. 90 087901
[164] Tyryshkin A M, Lyon S A, Jantsch W and Schäffler F 2005 Phys. Rev. Lett. 94 126802
[165] Feher G and Gere E A 1959 Phys. Rev. 114 1245 [166] Castner T G 1962 Phys. Rev. Lett. 8 13 [167] Tyryshkin A M et al 2012 Nat. Mater. 11 143
Rep. Prog. Phys. 80 (2017) 016001


 Review
41
[168] Morton J J L, Tyryshkin A M, Brown R M, Shankar S, Lovett B W, Ardavan A, Schenkel T, Haller E E, Ager J W and Lyon S A 2008 Nature 455 1085 [169] Steger M, Saeedi K, Thewalt M, Morton J, Riemann H, Abrosimov N, Becker P and Pohl H-J 2012 Science 336 1280 [170] Morley G W, Lueders P, Hamed Mohammady M, Balian S J, Aeppli G, Kay C W M, Witzel W M, Jeschke G and Monteiro T S 2013 Nat. Mater. 12 103 [171] Morley G W, Warner M, Stoneham A M, Greenland P T, van Tol J, Kay C W M and Aeppli G 2010 Nat. Mater. 9 725 [172] Jelezko F, Gaebel T, Popa I, Domhan M, Gruber A and Wrachtrup J 2004 Phys. Rev. Lett. 93 130501 [173] Wrachtrup J and Jelezko F 2006 J. Phys.: Condens. Matter 18 S807 [174] Dutt M V G, Childress L, Jiang L, Togan E, Maze J, Jelezko F, Zibrov A S, Hemmer P R and Lukin M D 2007 Science 316 1312
[175] Jiang L, Dutt M V G, Togan E, Childress L, Cappellaro P, Taylor J M and Lukin M D 2008 Phys. Rev. Lett. 100 073001 [176] Balasubramanian G et al 2008 Nature 455 648 [177] Maze J R et al 2008 Nature 455 644 [178] Taylor J M, Cappellaro P, Childress L, Jiang L, Budker D, Hemmer P R, Yacoby A, Walsworth R and Lukin M D 2008 Nat. Phys. 4 810
[179] Hall L T, Cole J H, Hill C D and Hollenberg L C L 2009 Phys. Rev. Lett. 103 220802
[180] Hall L T, Hill C D, Cole J H, Stadler B, Caruso F, Mulvaney P, Wrachtrup J and Hollenberg L C L 2010 Proc. Natl Acad. Sci. 107 18777
[181] Takahashi S, Hanson R, van Tol J, Sherwin M S and Awschalom D D 2008 Phys. Rev. Lett. 101 047601 [182] Jarmola A, Acosta V, Jensen K, Chemerisov S and Budker D 2012 Phys. Rev. Lett. 108 197601
[183] Kennedy T A, Colton J S, Butler J E, Linares R C and Doering P J 2003 Appl. Phys. Lett. 83 4190 [184] Hanson R, Gywat O and Awschalom D D 2006 Phys. Rev. B 74 161203 [185] Childress L, Gurudev Dutt M V, Taylor J M, Zibrov A S, Jelezko F, Wrachtrup J, Hemmer P R and Lukin M D 2006 Science 314 281
[186] Gaebel T et al 2006 Nat. Phys. 2 408 [187] Balasubramanian G et al 2009 Nat. Mater. 8 383 [188] Pfaff W, Taminiau T H, Robledo L, Bernien H, Markham M, Twitchen D J and Hanson R 2013 Nat. Phys. 9 29 [189] Weber J R, Koehl W F, Varley J B, Janotti A, Buckley B B, Van de Walle C G and Awschalom D D 2010 Proc. Natl Acad. Sci. 107 8513
[190] Mizuochi N, Yamasaki S, Takizawa H, Morishita N, Ohshima T, Itoh H and Isoya J 2002 Phys. Rev. B 66 235202 [191] Son N T, Zolnai Z and Janzén E 2003 Phys. Rev. B 68 205211 [192] Baranov P G, Ilin I V, Mokhov E N, Muzafarova M V, Orlinskii S B and Schmidt J 2005 JETP Lett. 82 441–3 [193] Son N T, Carlsson P, ul Hassan J, Janzén E, Umeda T, Isoya J, Gali A, Bockstedte M, Morishita N, Ohshima T and Itoh H 2006 Phys. Rev. Lett. 96 055501 [194] Baranov P G, Bundakova A P, Soltamova A A, Orlinskii S B, Borovykh I V, Zondervan R, Verberk R and Schmidt J 2011 Phys. Rev. B 83 125203 [195] Koehl W F, Buckley B B, Heremans F J, Calusine G and Awschalom D D 2011 Nature 479 84 [196] Orlinski S B, Schmidt J, Mokhov E N and Baranov P G 2003 Phys. Rev. B 67 125207
[197] Baranov P, Bundakova A, Borovykh I, Orlinskii S, Zondervan R and Schmidt J 2007 JETP Lett. 86 202
[198] Falk A L, Buckley B B, Calusine G, Koehl W F, Dobrovitski V V, Politi A, Zorman C A, Feng P X-L and Awschalom D D 2013 Nat. Commun. 4 1819 [199] Siyushev P et al 2014 Nat. Commun. 5 3895 [200] Pingault B, Becker J N, Schulte C H H, Arend C, Hepp C, Godde T, Tartakovskii A I, Markham M, Becher C and Atatüre M 2014 Phys. Rev. Lett. 113 263601 [201] Rogers L J et al 2014 Phys. Rev. Lett. 113 263602 [202] Yang W and Liu R-B 2009 Phys. Rev. B 79 115320 [203] Cywinski L, Dobrovitski V V and Das Sarma S 2010 Phys. Rev. B 82 035315 [204] Neder I, Rudner M S, Bluhm H, Foletti S, Halperin B I and Yacoby A 2011 Phys. Rev. B 84 035441 [205] Vaks V G, Larkin A I and Pikin S A 1968 Sov. Phys.—JETP 26 188
[206] Yang D H-Y and Wang Y-L 1974 Phys. Rev. B 10 4714 [207] Ma W-L, Wolfowicz G, Zhao N, Li S-S, Morton J J and Liu R-B 2014 Nat. Commun. 5 4822 [208] Abrikosov A A, Gorkov L P and Dzyaloshinski I E 1963 Methods of Quantum Field Theory in Statistical Physics (Englewood Cliffs, NJ: Prentice Hall) [209] Koppens F H L, Klauser D, Coish W A, Nowack K C, Kouwenhoven L P, Loss D and Vandersypen L M K 2007 Phys. Rev. Lett. 99 106803
[210] Coish W A, Fischer J and Loss D 2008 Phys. Rev. B 77 125329 [211] Barnes E, Cywiński L and Das Sarma S 2011 Phys. Rev. B 84 155315 [212] Cywinski L 2011 Acta Phys. Pol. A 119 576 [213] Witzel W M, Carroll M S, Morello A, Cywiński L and Das Sarma S 2010 Phys. Rev. Lett. 105 187602 [214] Balian S J, Kunze M B A, Mohammady M H, Morley G W, Witzel W M, Kay C W M and Monteiro T S 2012 Phys. Rev. B 86 104428 [215] Du J, Rong X, Zhao N, Wang Y, Yang J and Liu R B 2009 Nature 461 1265
[216] Shi F, Kong X, Wang P, Kong F, Zhao N, Liu R-B and Du J 2014 Nat. Phys. 10 21
[217] Witzel W M and Das Sarma S 2007 Phys. Rev. Lett. 98 077601 [218] Balian S J, Wolfowicz G, Morton J J L and Monteiro T S 2014 Phys. Rev. B 89 045403 [219] Balian S J, Liu R-B and Monteiro T S 2015 Phys. Rev. B 91 245416 [220] Witzel W M and Das Sarma S 2007 Phys. Rev. B 76 045218 [221] Witzel W M, Hu X and Das Sarma S 2007 Phys. Rev. B 76 035212 [222] Witzel W M, Rahman R and Carroll M S 2012 Phys. Rev. B 85 205312 [223] Abe E et al 2010 Phys. Rev. B 82 121201 [224] Coish W A, Fischer J and Loss D 2010 Phys. Rev. B 81 165315 [225] Semenov Y G and Kim K W 2003 Phys. Rev. B 67 073301 [226] Erlingsson S I and Nazarov Y V 2004 Phys. Rev. B 70 205327 [227] Al-Hassanieh K A, Dobrovitski V V, Dagotto E and Harmon B N 2006 Phys. Rev. Lett. 97 037204 [228] Melikidze A, Dobrovitski V V, De Raedt H A, Katsnelson M I and Harmon B N 2004 Phys. Rev. B 70 014435 [229] Kozlov G 2007 Sov. Phys.—JETP 105 803 [230] Bortz M and Stolze J 2007 Phys. Rev. B 76 014304 [231] Khaetskii A, Loss D and Glazman L 2003 Phys. Rev. B 67 195329 [232] Schliemann J, Khaetskii A and Loss D 2003 J. Phys.: Condens. Matter 15 R1809
[233] Dobrovitski V V and De Raedt H A 2003 Phys. Rev. E 67 056702
Rep. Prog. Phys. 80 (2017) 016001


 Review
42
[234] Dobrovitski V V, De Raedt H A, Katsnelson M I and Harmon B N 2003 Phys. Rev. Lett. 90 210401 [235] Zhang W, Dobrovitski V V, Al-Hassanieh K A, Dagotto E and Harmon B N 2006 Phys. Rev. B 74 205313 [236] Faribault A and Schuricht D 2013 Phys. Rev. Lett. 110 040405 [237] Faribault A and Schuricht D 2013 Phys. Rev. B 88 085323 [238] Breuer H-P, Burgarth D and Petruccione F 2004 Phys. Rev. B 70 045323 [239] Fischer J and Breuer H-P 2007 Phys. Rev. A 76 052119 [240] Ferraro E, Breuer H-P, Napoli A, Jivulescu M A and Messina A 2008 Phys. Rev. B 78 064309 [241] Deng C and Hu X 2006 Phys. Rev. B 73 241303 [242] Deng C and Hu X 2008 Phys. Rev. B 78 245301 [243] Stanek D, Raas C and Uhrig G S 2013 Phys. Rev. B 88 155305 [244] Stanek D, Raas C and Uhrig G S 2014 Phys. Rev. B 90 064301 [245] Barnes E, Cywiński L and Das Sarma S 2012 Phys. Rev. Lett. 109 140403 [246] Saikin S and Fedichkin L 2003 Phys. Rev. B 67 161302 [247] Chernobrod B M and Berman G P 2005 J. Appl. Phys. 97 014903 [248] Degen C L 2008 Appl. Phys. Lett. 92 243111 [249] Quan H T, Song Z, Liu X F, Zanardi P and Sun C P 2006 Phys. Rev. Lett. 96 140604
[250] Chen S-W, Jiang Z-F and Liu R-B 2013 New J. Phys. 15 043032 [251] Wei B-B and Liu R-B 2012 Phys. Rev. Lett. 109 185701 [252] Peng X, Zhou H, Wei B-B, Cui J, Du J and Liu R-B 2015 Phys. Rev. Lett. 114 010601
[253] Wei B-B, Chen S-W, Po H-C and Liu R-B 2014 Sci. Rep. 4 5202 [254] Wei B-B, Jiang Z-F and Liu R-B 2015 Sci. Rep. 5 15077 [255] Kolkowitz S, Unterreithmeier Q P, Bennett S D and Lukin M D 2012 Phys. Rev. Lett. 109 137601 [256] Taminiau T H, Wagenaar J J T, van der Sar T, Jelezko F, Dobrovitski V V and Hanson R 2012 Phys. Rev. Lett. 109 137602 [257] Shi F et al 2015 Science 347 1135 [258] Mamin H J, Kim M, Sherwood M H, Rettner C T, Ohno K, Awschalom D D and Rugar D 2013 Science 339 557 [259] Staudacher T, Shi F, Pezzagna S, Meijer J, Du J, Meriles C A, Reinhard F and Wrachtrup J 2013 Science 339 561 [260] Ma W-L, Li S-S, Cao G-Y and Liu R-B 2016 Phys. Rev. Appl. 5 044016
[261] Ma W-L and Liu R-B 2016 Phys. Rev. Appl. 6 024019 [262] Ma W-L and Liu R-B 2015 arXiv:1512.03548 [quant-ph] [263] Boss J M, Chang K, Armijo J, Cujia K, Rosskopf T, Maze J R and Degen C L 2016 Phys. Rev. Lett. 116 197601
Wen Yang obtained his BSc (2002) from the Beijing Normal University and PhD (2007) from Institute of Semiconductors, Chinese Academy of Sciences. He was a postdoctoral fellow at the Chinese University of Hong Kong from 2007 to 2008. Next he worked as a postdoctoral researcher at the University of California, San Diego from 2008 to 2011. Since November 2011, he has been an assistant professor at Beijing Computational Science Research Center. His research deals with the theory of nanoscale transport, spin decoherence and coherence protection, and quantum sensing and metrology.
Wen-Long Ma obtained his BSc from The University of Science and Technology Beijing in 2010. In 2015, he got his PhD from the Institute of Semiconductors, Chinese Academy of Sciences supervised by Professor Shu-Shen Li in the State Key Laboratory of Superlattices and Microstructures. Since August 2015, he has been a postdoctoral fellow in Department of Physics, The Chinese University of Hong Kong. His current research deals with spin decoherence in solid-state systems and quantum sensing toward single-molecule nuclear magnetic resonance.
Ren-Bao Liu obtained a BSc from Nanjing University in 1995 and a PhD in Physics from the Institute of Semiconductors, Chinese Academy of Sciences in 2000. He was a postdoctoral fellow in the Institute of Advanced Study, Tsinghua University (2000-2002) and in the Department of Physics, University of California, San Diego (2002-2005). He joined the Department of Physics, The Chinese University of Hong Kong in 2005 as an assistant professor and was promoted to the full professorship in 2014. Now he is the Director of Centre for Quantum Coherence and an Outstanding Fellow of Faculty of Science, The Chinese University of Hong Kong. His research interest ranges from spinbased quantum computing, quantum sensing, quantum bio-physics, extreme nonlinear THz optics in condensed matter systems, and topological quantum optics.
Rep. Prog. Phys. 80 (2017) 016001
