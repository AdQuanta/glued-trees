# Introduction to the Dicke Model: From Equilibrium to Nonequilibrium, and Vice Versa - Full Text

> Source: https://onlinelibrary.wiley.com/doi/abs/10.1002/qute.201800043
> Collected: 2026-09-20
> Published: Unknown
> Zotero parent key: GZC48RA3
> Evidence: Zotero indexed PDF text

Introduction to the Dicke model: from equilibrium to nonequilibrium, and vice versa
Peter Kirton,1, 2 Mor M. Roses,3 Jonathan Keeling,1 and Emanuele G. Dalla Torre3
1SUPA, School of Physics and Astronomy, University of St Andrews, St Andrews, KY16 9SS, United Kingdom 2Vienna Center for Quantum Science and Technology, Atominstitut, TU Wien, 1040 Vienna, Austria 3Department of Physics and Center for Quantum Entanglement Science and Technology, Bar-Ilan University, Ramat Gan 5290002, Israel
The Dicke model describes the coupling between a quantized cavity field and a large ensemble of two-level atoms. When the number of atoms tends to infinity, this model can undergo a transition to a superradiant phase, belonging to the mean-field Ising universality class. The superradiant transition was first predicted for atoms in thermal equilibrium and was recently realized with a quantum simulator made of atoms in an optical cavity, subject to both dissipation and driving. In addition to this atomic realization, quantum simulation of the Dicke model has also been proposed in a number of other experimental systems, including superconducting qubits, trapped ions, and using spin-orbit coupling for cold atoms. In this Progress Report, we offer an introduction to some theoretical concepts relevant to the Dicke model, reviewing the critical properties of the superradiant phase transition, and the distinction between equilibrium and nonequilibrium conditions. In addition, we explain the fundamental difference between the superradiant phase transition and the more common lasing transition. Our report mostly focuses on the steady states of atoms in single-mode optical cavities, but we also mention some aspects of real-time dynamics, as well as other quantum simulators, including superconducting qubits, trapped ions, and using spin-orbit coupling for cold atoms. These realizations differ in regard to whether they describe equilibrium or non-equilibrium systems.
CONTENTS
I. Historical background 1
II. Models and experiments 3
III. Threshold of the superradiant transition 5
IV. Universality in and out of equilibrium 7
V. Beyond-mean-field methods 10
VI. Superradiance and lasing 12
VII. Closely related models 14
VIII. Conclusion 16
I. HISTORICAL BACKGROUND
Superradiance was first introduced in 1954 by Dicke to describe the emission of light by a large ensemble of atoms[1]. Dicke considered N two-level atoms that are initially prepared in their excited state. At a given time, one of the atoms decays by emitting a photon. This induces a chain reaction that leads to the decay of all the N atoms and the emission of N photons in free space. Dicke explained that if all the atoms are trapped within a fraction of a wavelength, the photons emitted will be indistinguishable. In this case, the emission processes will interfere constructively, giving rise to an electromagnetic field with amplitude proportional to N and an energy density proportional to N 2. The scaling laws of this
transient superradiance differ from the decay of N independent atoms, where the light is emitted incoherently and has an energy density proportional to N .
In 1973, Hepp and Lieb[2] discovered a different type of steady-state superradiance, which occurs when the ensemble of atoms is coupled to the quantized mode of a cavity. They considered the thermal equilibrium properties of the resulting Dicke model and demonstrated that it shows a continuous phase transition between a normal and a superradiant phase. To achieve a meaningful thermodynamic limit, Hepp and Lieb[2] assumed that the coupling between the two level systems and the photon
field decreases as 1/√N . Under this assumption, in the normal phase, the number of photons n does not grow with N , while in the superradiant phase, n is proportional to N . The paper by Hepp and Lieb is written in a mathematical style, which was soon reformulated in a form more transparent to physicists by Wang and Hioe[3]. Their analysis was later refined by Refs. [4–6] who showed that the transition survives in the presence of counter-rotating terms, which however shift the position of the transition by a factor of 1/2.
In spite of the significant theoretical interest, the superradiant transition had not been realized experimentally, until recent times. The major difficulty is that the transition requires very strong coupling between the atoms and the cavity, such that the photon-atom coupling is of the order of the atomic and cavity frequencies. From a theoretical perspective, several authors studied whether the superradiant transition can be reached using only the dipole coupling between the atoms and the cavity. These studies gave rise to a fundamental debate around the validity of a no-go theorem for the superradiant transition, which will be discussed in Sec. II D.


 2
FIG. 1. Schematic representation of the driven-dissipative Dicke model, based on internal degrees of freedom and proposed by Dimer et al.[7]. In this realization, each atom is modeled by a 4-level scheme and is coupled to the cavity through stimulated Raman emissions. In the steady state, the system absorbs energy from the external time dependent pump (at frequency ωp) and dumps it into several dissipative channels (γ↓ and κ).
In the last decade, two uncontested ways to realize the Dicke model and its superradiant transition have been demonstrated theoretically and experimentally. The first approach was proposed by Dimer et al.[7] and is based on a 4-level scheme (see Fig. 1). In this setup, the coupling between the atoms and the photons is induced by stimulated Raman emission, and can be made arbitrarily strong. This proposal was recently realized by Zhiqiang et al..[8]. The second approach was inspired by an earlier experiment, proposed by Domokos and Ritsch[9], and realized by Black et al.[10]. These authors considered a gas of thermal atoms that are trapped inside a cavity. The atoms are illuminated by an external coherent pump and scatter photons into the cavity (see Fig. 2). It was found that for strong enough pump intensities, the atoms self-organize in a checkerboard pattern, where the atoms are preferentially separated by an integer multiple of the photon’s wavelength, and scatter light coherently. This analysis was later extended to the case of a Bose-Einstein condensate (BEC) theoretically by Nagy et al.[11] and experimentally by Baumann et al.[12]. In a BEC, the atoms are delocalized, and the phase of the scattered light is random. In this situation, the scattered photons are incoherent and their number does not grow with N . In contrast, in the self-organized state, all atoms emit photons coherently, giving rise to a superradiant phase, where the number of photons is proportional to N . Following this reasoning, Refs. [11, 12] showed that the onset of self-organization can be mapped to the superradiance transition of the Dicke model, see Sec. II. This study was later extended to narrow linewidth[13] and multimode[14] cavities.
The two above-mentioned realizations of the superradiant transition in the Dicke model involve drivendissipative systems. In both settings, the coupling between the atoms and the photons is achieved through an external time-dependent pump. This allows arbitrarily strong effective light-matter coupling strengths, enabling the transition. As a consequence of being driven, these
κκ
Pump
FIG. 2. Cartoon of the self-organization transition. When the pump strength is below threshold (left), the atoms are delocalized and scatter light incoherently in the cavity. Above threshold (right) the atoms feel an optical lattice from the interference of pump and cavity light, and organize into a checkerboard lattice. Adapted from Ref. [21].
systems cannot be described by an equilibrium Dicke model, but one needs to take into account the drive and dissipation present. This subtle difference was initially dismissed because, in the limit of vanishing losses, the critical coupling of the driven-dissipative model coincides with the value of the equilibrium case, see Sec. III. Because the driven-dissipative model does not have a welldefined temperature, it was tempting to identify the experiment with a zero-temperature quantum phase transition. However, later studies[15–17] showed that the phase transition has the same universal properties as the equilibrium transition at finite temperature. This equivalence can be understood in terms of an emergent low-frequency thermalization, which will be reviewed in Sec. IV. These approaches can be considered as analog quantum simulators of the Dicke model: the driving scheme is designed to engineer an effective Dicke model with tunable parameters allowing exploration of the phase diagram. As discussed further in Sec. II D, there also exist proposals for digital or hybrid analog-digital quantum simulation of the Dicke model using superconducting qubits or trapped
ions[18–20].
The main goals of this Progress Report are (i) to present simple physical arguments to understand the commonalities and differences between the superradiant phase transition in the equilibrium Dicke model and its non-equilibrium counterparts (Secs. II-IV), (ii) to introduce some analytical and numerical approximations, used to study the Dicke model (Sec. V); and (iii) to set the superradiant transition in the wider context of closely related models and transitions (Sections VI and VII). For a broader discussion of the phenomena of superradiance and the Dicke model, we refer the reader to a number of other relevant reviews: Gross and Haroche[22] discusses the transient superradiance first predicted by Dicke; Garraway[23] presents the Dicke model and its phase transitions from a quantum optics perspective; Ritsch et al.[24] discusses the self organization of atoms in optical cavities and dynamical optical lattices.


 3
II. MODELS AND EXPERIMENTS
A. The Dicke model at equilibrium
The Dicke model describes a single bosonic mode (often a cavity photon mode) which interacts collectively with a set of N two-level systems (the atoms). The Dicke Hamiltonian is given by
H = ωca†a + ωz
N
∑
j=1
σz
j + √2λN (a + a†)
∑
j
σx
j . (1)
Here a†(a) are the creation (annihilation) operators of the photon, satisfying [a, a†] = 1, and σα
i are spin operators,
satisfying [σx
j , σy
k ] = iδj,kσz
j (note that σα = τ α/2, where
τ α are Pauli matrices). The model has three tuning parameters: the photon frequency ωc, the atomic energy splitting ωz, and the photon-atom coupling λ. To understand the nature of the superradiant transition, it is useful to analyze the symmetries of this model. By applying the transformation a → −a and σx → −σx, the Hamiltonian remains unchanged. This gives a symmetry group with only two elements (when this transformation is applied twice it brings back to the original state) and is formally associated with a Z2 group. This symmetry arises due to the conservation of the parity of the total number of excitations (i.e. the number of photons, plus the number of excited spins), and is analogous to the Ising symmetry of ferromagnets. As we will see, the superradiant transition indeed shares the same critical exponents as the mean-field Ising transition. The Dicke model, Eq. (1), depends on the atomic degrees of freedom through the total spin operators Sα =
∑
j σα
j only. Using this definition, the Dicke model becomes
H = ωca†a + ωzSz + √2λN (a + a†)Sx . (2)
This Hamiltonian commutes with the total spin S2 = (Sx)2 + (Sy)2 + (Sz)2. Consequently, it connects only states with the same total spin S, i.e. that belong to the same Dicke manifold. This symmetry provides a significant simplification of the problem because it allows the description of the atomic degrees of freedom in terms of N + 1 states, rather than the entire Hilbert space of size 2N [25]. This symmetry can however be broken by physical processes that act on individual atoms, which will be described in Sec. II C.
B. Raman transitions and self-organization
As mentioned in the introduction, the Dicke model was realized experimentally in two ways: (i) using stimulated Raman emission between two hyperfine states in the ground state manifold of a cold atomic cloud, and (ii) coupling to the motional degrees of freedom of a BEC.
The former realization[7] involves a 4-level scheme, schematically drawn in Fig. 1. The mapping to the Dicke model is straightforward: ωz is the effective splitting between the two ground states (taking into account any differential Stark shifts due to the external drive), and
λ/√N the strength of the stimulated Raman emission into the cavity mode. Note that this coupling is achieved by using two distinct external fields. These two processes correspond to σ+
i a + σ−
i a† and σ+
i a† + σ−
i a†, respectively, and are often referred to as rotating and counterrotating. When the two processes have equal strength, one recovers the Dicke model of Eq. (1). By varying the relative strength, it is possible to realize a generalized Dicke model, with different prefactors to the rotating and counter-rotating terms, which will be discussed further in Sec. VI B. In the latter realization[11, 12], the mapping to the Dicke model was achieved by considering two momentum modes of the atoms (the BEC at q = 0 and the first recoil at kL = 2π/λ). It is not immediately clear that this mapping is completely justified. Firstly, it is not a priori clear that one may neglect higher order scatterings, at multiples of kL. Secondly, the mapping only holds if the atoms are initially found in a BEC. However, in practice, the self-organization transition occurs in a thermal state as well[9, 10]: a detailed analysis revealed that the superradiance phase transition is essentially unaffected by the BEC transition[26]. Hence, we present here a different mapping of the self-organization transition to the Dicke model, which does not require a BEC. Our derivation assumes that the atoms do not interact and are initially found in the superradiant phase. In this state, the atoms scatter light into a standing wave of the cavity field, whose period is λ/2. However, to enable superradiance, the atoms need to preferentially occupy sites that are separated by an integer multiple of λ in the longitudinal direction of the cavity. Having denoted all the possible sites as even or odd, we introduce the spin variables σx
j , which indicate whether the atom j is on an even
(σx
j = 1/2) or odd (σx
j = −1/2) site. Depending on their positions, the atoms scatter light from the pump, and create cavity photons, with a phase of either 0 or π. If we define Neven and Nodd as the operators that count the number of atoms on the even and odd sites, respectively, the photon-atom coupling can be written as λ(t)a†(Neven−Nodd)+H.c. = 2λ(t)a† ∑
j σx
j +H.c., where λ(t) = λ exp(iωpt) is proportional to the pump field and oscillates at the pump frequency ωp. In addition, the atoms can experience quantum tunneling between even and odd sites. This process is described by the spin-flip operator ωzσz
j , where ωz is the tunnelling rate. By combining these terms, we obtain the Dicke model
H(t) = ωca†a + ωz
N
∑
j=1
σz
j + 2 (λ(t)a + λ∗(t)a†)
N
∑
j=1
σx
j.
(3)


 4
In general, the parameters in this model may have a nontrivial dependence on the pump strength. (For instance in a standing-wave pump profile, the tunneling matrix element is given by the difference of eigenvalues of the Mathieu equation. See the Appendix A.1 of Ref. [27].) On approaching the transition, the standing wave becomes weaker and ωz achieves its maximal possible value, which equals to the recoil energy ER = k2
L/2m. In this limit, Eq. (3) becomes identical to the Dicke model obtained by Ref. [11], which started by considering a BEC of atoms.
C. Driven-dissipative models
The explicit time dependence of Eq. (3) can be removed by shifting to an appropriate rotating frame, i.e. by using the gauge transformation a → eiωpta. This transformation brings Eq. (3) to the time-independent Dicke model, Eq. (1), with a renormalized cavity frequency ωc → ωc − ωp. If the system were closed, this transformation would have no physical consequences. However, when the system is coupled to a bath, the transformation changes the properties of the bath, pushing it out of equilibrium. In particular, since all frequencies are renormalized down by ωp, the transformation leads to a bath with both positive and negative frequencies, while equilibrium baths have positive eigenfrequencies only. Hence, there are two equivalent ways to describe the driven-dissipative Dicke model: (i) in the laboratory frame, where the bath is in thermal equilibrium but the Hamiltonian is time dependent, and (ii) in the rotating frame, where the Hamiltonian is time independent, but the baths are effectively out of equilibrium. In this report we follow the second, more common approach, and work in the rotating frame. Since the optical frequency is the largest scale in the problem, the baths can be approximated as Markovian[28]. As discussed for example in Ref. [17], Markovian baths generally violate the equilibrium fluctuation-dissipation relation. This is because of the negative frequency bath components described above. These cannot be found at thermal equilibrium because their partition function is not normalizable (for a bath mode at frequency ωb < 0,
Z = T r[eβ|ωb|a†a] → ∞). In practice, this is not a problem because the occupation of the bath modes is actually set by their frequencies in the laboratory frame ωp + ωb > 0, rather than in the rotating frame, ωb < 0. For optical frequencies at room temperature, the occupation of the bath modes can be safely approximated to zero, giving rise to the Lindblad-form master equation
ρ ̇ = −i[H, ρ] +
∑
i
γiD [Li] (4)
where ρ is the system’s density matrix, and
D [L] ≡ 2LρL† − {L†L, ρ} . (5)
rate L operator physical process
κ a cavity decay
γ
∑
j σ−
j = S− collective atomic decay
γ↓ σ−
j single-atom decay
γφ σz
j single-atom dephasing
TABLE I. Main sources of dissipation that were considered in the literature[29–31] .
Physically, the rates γi and operators Li correspond to different sources of dissipation. For experiments on the Dicke model, the most relevant sources of dissipation are listed in Table I, and can be divided in two main categories: collective effects (κ and γ) and single atoms effects (γ↓ and γφ). In Sec. III we will explain how to deal with these categories. Other sources of dissipation, such as the loss of atoms, require going beyond the picture of a fixed number of two-level systems coupled to light, and will not be considered here.
D. Other realizations of the Dicke model
In Sec. I, we mentioned a no-go theorem for the superradiant transition by Rzazewski[32]. These authors claimed that the superradiant transition cannot be reached using dipole couplings between atoms and photons. The key observation of Rzazewski[32] is that the Dicke model is incomplete, because it is not invariant under gauge transformations of the electromagnetic field. A minimal change which recovers this invariance is to add a term proportional to the square of the vector potential. The Thomas-Reiche-Kuhn sum rule then implies that the strength of this additional term is exactly that needed to inhibit the phase transition, leading to a “nogo” theorem[33, 34]. The validity of this no-go theorem is still debated. In particular, a full quantum treatment of the problem requires not only the A2 terms, but a description of the longitudinal Coulomb interactions between dipoles. By considering a full description of a realistic system of atoms in a real cavity, Refs. [35–39] showed that a phase transition can occur in the right geometry. Since the “photon creation” operator describes different physical fields in different gauges, it is important to check what physical fields acquire macroscopic expectations in such a transition. Such analysis reveals that this transition is adiabatically connected to a crystalline transition for motional degrees of freedom[37], or to a ferroelectric transition for dipole couplings[39]. Very recent works[40, 41] have also noted that since the two-level approximation has a different meaning in different gauges, its validity at strong coupling is not gauge invariant: as such[40] shows that only in the dipole gauge can the two-level approximation be trusted. The question of how to properly describe matter–light coupling has also recently been discussed in the context of combining cavity quantum electrodynam


 5
ics with density functional theory[42, 43]. The realization of the Dicke model using Raman driving circumvents the no-go theorem, for the following reasons: Firstly, the effective matter-light couplings appearing in this Hamiltonian are a combination of the bare coupling, the pump strength and the detuning. As such, these are not subject to any oscillator-strength sum-rule. Moreover, even the bare couplings appearing in the effective coupling relate to transitions between ground and excited atomic states, rather than direct transitions between the low energy states forming the two-level system. Finally, the effective cavity frequency is tunable through the pump-cavity detuning. As a result of all of these points, there is no longer any constraint on the relation between the parameters of the model, and a superradiant transition is possible. An A2 term may nonentheless be present, but the system’s parameters can be chosen such that this term is weak enough to be ignored. In addition, the original equilibrium superradiant transition of the Dicke model is possible in a grand canonical ensemble[44, 45]. In such an ensemble, one minimizes the grand potential Φ = −kBT ln(ZGC), where ZGC = Tr [exp(−β(H − μNex))], and Nex = a†a + ∑
j σz
j + 1/2. The chemical potential μ shifts the effective parameters ωc, ωz → ωc − μ, ωz − μ such that the sum rule required for the no-go theorem no longer holds. Considering this ensemble only makes sense if the Hamiltonian preserves the number of excitations, i.e. working in the limit where counter-rotating terms can be dropped, giving rise to the Tavis–Cummings model (see Sec. VI A). Conceptually, this corresponds to considering a perfect cavity prepared with an initial finite excitation density and then asking for the ground state. This model can also describe the Bose–Einstein condensation of exciton-polaritons — superpositions of microcavity photons and excitons[46, 47] — in the limit of a very good cavity[48, 49]. Another context in which the Dicke transition is expected to be possible involves circuit QED[50]. Here, the two-level atoms are replaced by superconducting qubits, coupled to a common microwave resonator. This again can be considered as an analog quantum simulator, with the superconducting qubits acting as tunable artificial atoms. There has been much discussion on whether the Hamiltonian describing such a system should contain A2 terms, and as such, whether it is subject to the no-go theorem[51–57]. For at least some designs of circuit, if one starts from the classical Kirchoff equations (i.e. conditions on the currents and voltages) of the circuit, and proceeds to quantize these equations, the resulting Hamiltonian is not necessarily subject to the no-go theorem. i.e., there are cases where either the A2 term is absent, or where it is present, but with a weaker coupling strength than required to prevent the phase transition. The above realizations of the Dicke model involve coupling to a photonic mode, at optical or microwave frequencies. In addition, the Dicke model can be realized in any case where many spin degrees of freedom couple to a common bosonic mode. There have been several
proposals for realizing such a model where the bosonic mode corresponds to motion in an harmonic trap, i.e. a mechanical phonon mode, rather than a photon. One widely studied example involves coupling the electronic states of trapped ions to their center of mass motion[20, 58–60]. In fact, the natural coupling between a standing wave laser and an ion leads to a position dependent matrix element[61]. Writing this position in terms of vibrational raising and lowering operators, one can expand in the Lamb-Dicke regime to produce an effective Dicke model[20, 59]. Alternately, a state-dependent optical potential can be used to couple the electronic state of the ion to the center of mass mode[58, 62, 63]. Such an approach has been realized experimentally in Ref. [60], where an adiabatic sweep from the normal to the superradiant state has been studied. A similar idea has also been realized by Hamner et al.[64], using a spin-orbit coupled BEC in an harmonic trap. Here spin-orbit coupling produces a coupling between atomic motion and the internal spin state. The cloud of atoms is reduced to a single motional degree of freedom by the non-fragmentation of an interacting BEC. Using this mapping to the Dicke model, the experimentally observed transition between a polarized and unpolarized state of the atoms can be understood as an analogue of the superradiant phase transition. All the above examples describe various routes to analog quantum simulation of the Dicke model, i.e. they involve directly engineering a Dicke Hamiltonian, and then studying the steady state or dynamics of this model. In addition, there have been other proposals to use digital quantum simulation, i.e. to replace time evolution under the Dicke Hamiltonian with a sequence of discrete unitary gates that leads to the same evolution. In particular, schemes have been proposed to realize such digital quantum simulation using superconducting qubits[18, 19].
III. THRESHOLD OF THE SUPERRADIANT TRANSITION
In this section we give an overview of some simple techniques for finding the critical point in the Dicke model both in and out of equilibrium. These approaches are based on mean-field theory, and give an intuitive understanding of the superradiant transition.
A. Equilibrium transition
In equilibrium we can calculate the critical coupling of the Dicke model, Eq. (1), by minimizing its meanfield free energy. Within this approach, we assume the photons to be in a coherent state |α〉, defined by a|α〉 = α|α〉, where α is a real variational parameter. In this state, the energy of the cavity is ωc〈a†a〉 = ωcα2 and


 6
each atom experiences the Hamiltonian
h(α) = ωzσz
i + √4λN ασx
i . (6)
The partition function is then given by
Z(α) = Tr[e−βH ] = e−βωcα2 (Tr e−βh)N , (7)
where β = 1/T is the inverse temperature. By definition, the free energy is
F (α) = − 1
β ln(Z(α)) = ωcα2 − N
β ln (2 cosh βE) , (8)
where E =
√
ωz2
4 + 4λ2
N α2 is the eigenvalue of h(α). By optimizing F as a function of α, one finds that if λ < λc the minimum is at α = 0 while for λ > λc the minimum is at α 6= 0. The critical value λc is found by the condition F ′′(α = 0) = 0, or
λc = 1
2
√
ωcωz coth
( βωz 2
)
. (9)
Note that this critical coupling smoothly evolves down to zero temperature (β → ∞), where one obtains λc =
√ωc ωz /2.
One may also use the above approach to find the critical exponent β that controls how the order parameter α evolves beyond the critical λ. In general, for λ > λc we minimize the free energy by solving dF (α)/dα = 0, or
ωcα = N
2 tanh(βE) dE
dα = 2λ2 tanh(βE)
E α, (10)
and since α 6= 0 this gives ωcE = 2λ2 tanh(βE). For small α we can expand E = (ωz/2) + 4λ2α2/N ωz. Expanding both sides of Eq. (10) to order α2, one finds
α = √N A(λ)(λ2 − λc2), (11)
where A(λ) is a function of coefficients which is finite at λ = λc for all temperatures. One finds that in the
superradiant state, the order parameter scales as √N and develops as α ∼ (λ − λc)β, with β = 1/2. These results are valid both for zero and non-zero temperatures. Nevertheless, as we will explain in Sec. IV, the these two transitions are actually fundamentally different.
B. Holstein–Primakoff transformation
An alternative description of the Dicke model relies on the Holstein-Primakoff (HP) representation[65], which maps the total spin operators Sα to a bosonic mode b
Sz → −N
2 + b†b, S+ → b†√
N − b†b . (12)
In the large N limit (where N 〈b†b〉), Eq. (12) simpli
fies to Sx → √N (b + b†) and the Dicke model, Eq. (2), becomes equivalent to two coupled Harmonic oscillators
HHP = ωca†a + ωzb†b + λ(a + a†)(b + b†) . (13)
Since the HP transformation relies on the total spin representation, this approach can include collective decay channels only, κ and γ in Table I[66]. Being a quadratic Hamiltonian, the model (13) can be analytically solved at equilibrium, as well as out of equilibrium, in many different ways. In the following sections we will briefly summarize how this is done using master equations, as well as Keldysh path integrals. Within the master equation approach, Eq. (4), one has
ρ ̇ = −i[HHP , ρ] + κD[a] + γD[b]. (14)
Eq. (14) gives rise to linear equations of motion for the operators a and b, which can be equivalently rewritten in terms of classical expectations,
 ̇a = (−iωc − κ)a − iλ(b + b†) (15)
 ̇b = (−iωz − γ)b − iλ(a + a†). (16)
These equations can be written in a matrix notation as
v ̇ (t) =M v(t), (17)
with v = (a, a†, b, b†)T and
M=

   
−(κ + iωc) 0 −iλ −iλ 0 −(κ − iωc) iλ iλ −iλ −iλ −(γ + iωz) 0 iλ iλ 0 −(γ − iωz)

   
.
(18)
We now relate this expression to the retarded Green’s function and the Keldysh path integral formalism. The Keldysh formalism allows one to extend path integrals to systems away from thermal equilibrium. Many comprehensive introductions to this approach can be found in textbooks[67, 68] as well as reviews of its application to driven-dissipative systems[69]. Given these excellent introductions, we do not aim here to discuss the derivation of this path integral, but provide a brief summary of its significance instead. The key feature of the Keldysh formalism is the separate treatment of the retarded/advanced Green’s function, GR/A, and the Keldysh Green’s function, GK. The former describe the response of the system to an external drive, while the latter captures thermal and quantum fluctuations inherent to the system. At thermal equilibrium these two quantities are linked by the the fluctuation-dissipation relations, which become invalid in the presence of external time-dependent drives. Formally, the distinction between GR/A and GK is achieved by the introduction of two separate fields that describe the evolution of the left (ket) and right (bra) side of the density matrix, respectively.


 7
As explained in Appendix A, Eq. (17) can be used to derive the retarded Green’s function of the system
[GR(ω)]−1 =S−1 (ω − iM ) , (19)
here S represents the equal-time commutation relations
Si,j =
〈[
vi(0), v†
j (0)
]〉
and in the present case is given
by:
S = diag(1, −1, 1, −1). (20)
Plugging Eqs. (18) and (20) into Eq. (19) one finds
[GR
HP (ω)]−1 =

   
ω − ωc + iκ 0 −λ −λ 0 −ω − ωc − iκ −λ −λ −λ −λ ω − ωz + iγ 0
−λ −λ 0 −ω − ωz − iγ

   
(21)
In the limit of γ → 0, this expression is equivalent to the retarded Green’s function derived in Ref. [17]. The superradiant transition corresponds to the requirement that one of the eigenvalues of M goes to zero, or equivalently that det[GR(ω = 0)] = 0. This condition can be easily evaluated to deliver
λc = 1
2
√
ωz2 + γ2
ωz
ωc2 + κ2
ωc
. (22)
In the limit κ, γ → 0, Eq. (22) recovers the zero temperature limit of the equilibrium result, Eq. (9). However, as we will explain in Sec. IV, the transition of the open system is in a different universality class than the zero temperature limit.
C. Critical coupling in the presence of single-atom losses
The Holstein-Primakoff approximation assumes that the total spin of the model is conserved. As a consequence, it cannot describe processes that act on individual atoms, such as the single-atom decay γ↓ and dephasing γφ mentioned in Sec. II C. The effect of these processes on the critical coupling can be found by considering the equations of motion for the expectation values of the physical observables. Starting from the Hamiltonian in Eq. (1) and including the single atom decay sources, one finds[30]:
∂t 〈a〉 = − (iωc + κ) 〈a〉 − i2λ
√
N 〈σx〉 (23)
∂t〈σ+〉 = (iωz − γT )〈σ+〉 − 2√iNλ Re[〈aσz〉] (24)
where γT = γφ + γ↓. The above equations are exact, but do not form a closed set due to the terms 〈aσz〉. However,
in the mean-field limit one can assume this factorizes as 〈aσz〉 = 〈a〉〈σz〉. This produces a closed set of mean field equations which are analogous to the Maxwell-Bloch (MB) classical theory of a laser[70]. The critical coupling of the superradiant transition can be found through a linear stability analysis of Eqs. (23) and (24)[30]: By retaining only terms that are linear in 〈a〉 and 〈σ+〉, one obtains the same form as Eq. (17), with
MMB =

   
−(κ + iωc) 0 −iλ −iλ 0 −(κ − iωc) iλ iλ 2iλ〈σz〉 2iλ〈σz〉 −(γT + iωz) 0 −2iλ〈σz〉 −2iλ〈σz〉 0 −(γT − iωz)

   
,
(25)
and v = (〈a〉, 〈a†〉, 〈σ−〉, 〈σ+〉)T . The superradiant transition occurs when the determinant of the above matrix vanishes, or equivalently:
λc = 1
2
√
(ωz2 + γ2
T )(ωc2 + κ2) −2〈σz 〉ωz ωc
. (26)
Note that if the atoms are initially fully polarized in the down state, i.e. 〈σz〉 = −1/2, then Eqs. (25) and (26) become equivalent to Eqs. (18) and (22).
IV. UNIVERSALITY IN AND OUT OF EQUILIBRIUM
In this section we describe the critical properties of the superradiant transition, from a theoretical perspective: We first review the results obtained for the Dicke model at equilibrium (IV A) and out-of-equilibrium (IV B), and then explain the universal nature of these results in terms of analogous models of simple nonlinear oscillators (IV C).
A. Equilibrium transition of the Dicke model
For a closed system at zero temperature, physical quantities in the normal phase of the Dicke model can be computed directly from the quadratic model of Eq. (13). This Hamiltonian can be diagonalized using a Bogoliubov transformation. For simplicity, let us consider the specific case of ωc = ωz = 1. In this case, the Hamiltonian (13) can be written as
H=1
2 (p2
a + p2
b) + 1
2 (xa xb)
(
1 2λ 2λ 1
)(
xa
xb
)
(27)
where xa = (a + a†)/√2 and pa = i(a† − a)/√2. This Hamiltonian is diagonalized by the eigenmodes x± =


 8
(xa ± xb)/√2 and p± = (pa ± pb)/√2, with eigenfrequencies ω± = 1 ± 2λ. In the new basis, the Hamiltonian decouples into two independent harmonic oscillators: H± = (p2± +ω2±x2±)/2. The superradiant transition occurs when one of ω± = 0, or equivalently |λ| = λc = 1/2, as predicted by Eq. (9). Let us now consider separately the zero and finite temperature cases. In the former case, one needs to calculate the ground state of an harmonic oscillator, where
〈x2±〉 = 1/√2ω±, leading to
〈x2
a〉 = 〈x2
+〉 + 〈x2
−〉 = 1
2√λc + λ + 1
2√λc − λ . (28)
We can use this result to compute the critical exponent γ, defined by 〈a†a〉 ∼ |λ − λc|−γ. The number of photons is 〈a†a〉 = (〈x2a〉 + 〈p2a〉 − 1)/2, where 〈x2a〉 diverges at
the transition according to Eq. (28), while 〈p2a〉 remains finite. Consequently, the number of photons diverges as (λc − λ)−1/2, leading to γ = 1/2. For a system at a finite temperature T , one has 〈x2±〉 = coth(β√(λc ± λ)/2)/(2√(λc ± λ)). When the temperature is high compared to the mode frequency (which is always the case near the transition for the mode with vanishing frequency), one can approximate
〈x2±〉 = T /(√2(λ ± λc)), leading to the critical exponent γ = 1. These critical exponents are valid for any value of the ωc/ωz ratio and demonstrate the difference between mean-field phase transitions at zero and finite temperatures.
B. Non-equilibrium transition of the Dicke model
For a driven-dissipative model, it is necessary to use non-equilibrium techniques. Within the HP approximation, one obtains a quadratic Keldysh action of the form[17]
SN = 1
2
∫
ω
V†
(
0 [GA
HP ]−1
[GR
HP ]−1 DK
HP
)
V . (29)
Here V = (v; v ̄), where v is defined above and v ̄ are auxiliary fields that allow us to describe the occupation of the bosons. For Markovian baths, DK is frequency independent and, if considering just photon loss, one simply has:
DK
HP = 2i diag(κ, κ, 0, 0). (30)
By inverting Eq. (29) one can compute any two-point correlation function of the cavity and the spin. This method is formally equivalent to the quantum regression theorem for Markovian baths: the convenient matrix notation easily extends to the case of several variables. One specific quantity that can be computed using this method is the number of photons in the cavity n = 〈a†a〉, which is related to the Keldysh Green’s function by
2n + 1 = ∫ dω/(2π)GK(ω). This quantity diverges at the phase transition as[15, 16]
〈a†a〉 = λ2
2ωzωc(1 − (λ/λc)2) ∼ 1
λc − λ (31)
where here λc = (1/2)√ωz(ωc2 + κ2)/ωc. Thus, for the driven-dissipative system, the critical exponent is γ = 1, as in the equilibrium case at finite temperature. This correspondence holds for other properties of the phase transition: for example, although the photon-atom entanglement diverges at the zero temperature transition[71–73], this quantity remains finite at the driven-dissipative transition[74]. These observations suggest that the universal properties of driven-dissipative systems are analogous to equilibrium one, at a finite effective temperature. This generic phenomenon will be explained in more detail in Sec. IV D.
C. Landau theory of a mean-field phase transition
As we have seen, the mean-field critical exponent of the transition at zero temperature differs from the nonequilibrium steady state. This difference can be understood using a simple Landau model of a mean-field Ising transition:
H = p2
2 +1
2 (λc − λ)x2 + 1
4N x4 . (32)
Here x and p are canonical coordinates. This model describes a phase transition at λc: for λ < λc the energy has a single minimum at x = 0, while for λ > λc two
minima are found at xmin = ±√N (λ − λc). The effect of spontaneous symmetry breaking corresponds to the choice of one of the two equivalent minima. The expression for xmin defines the critical exponent of the model β = 1/2. As discussed in Sec. III A, this matches the equilibrium result for both the zero and finite temperature Dicke model. The exponent β for the out of equilibrium Dicke model is less straightforward, as it cannot be found from a quadratic theory. However it is derived in a number of works including[7] and indeed found to be β = 1/2. Thus the Landau theory recovers the correct expression for the Dicke model both at equilibrium and out of equilibrium (see Table II). The critical exponent γ depends on the specific context of the transition. To understand this difference it is sufficient to consider three specific examples of the harmonic oscillator (for simplicity we focus on the normal phase at λ < λc):
1. Quantum phase transition (QPT) – If the system is at zero temperature, 〈x2〉 is given by the zero-point motion of the harmonic oscillator, Eq. (32) with N → ∞,
〈x2〉QP T = 1
2(λc − λ)1/2 , (33)
leading to the critical exponent γQP T = 1/2.


 9
2. Classical phase transition (CPT) – If the system is at finite temperature, one can apply the equipartition theorem to establish that in the classical limit when
kBT √λc − λ, then 〈(λc − λ)x2〉 = kBT . Thus,
〈x2〉CP T = kBT
λc − λ (34)
or equivalently γ = 1. As the mode frequency goes to zero at the transition, the transition point is always in
the classical limit, kBT √λc − λ. This result also holds for an open system coupled to an equilibrium bath at temperature T . In this case the dynamics are described by the Langevin equation
x ̈ − ηx ̇ + (λ − λc)x2 = f (t). (35)
Here correlations of the Langevin noise f (t) are determined by the fluctuation-dissipation theorem (FDT), 〈f (t)f (t′)〉 = 4ηkBT δ(t − t′). By inverting Eq. (35) one retrieves Eq. (34)[75]. As expected, for a classical system the insertion of an equilibrium bath does not modify the (equal-time) correlation functions of the system, and the critical exponent γ is left unchanged.
3. Non-equilibrium steady state (NESS) – In the presence of an external drive, the equilibrium FDT is violated, and the random noise source of Eq. (35) will be determined by a generic function 〈f (t)f (t′)〉 = F (t − t′) and
〈x2〉NESS =
∫ dω 2π
F (ω)
(ω2 + λ − λc)2 + ω2η2 , (36)
where F (ω) is the Fourier transform of F (t − t′). To extract the critical exponent of the transition, it is then sufficient to assume that F is analytic around ω = 0, such that for small ω, F (ω) ≈ F0. Under these conditions, for λ . λc,
〈x2〉 ≈ F0
2η(λ − λc) (37)
and γNESS = γCPT = 1.
The model (32) allows us to compute a third critical exponent, ζ. This exponent is defined by the divergence of 〈x2〉 at the critical point, λ = λc, as a function of N . At the transition, the system is governed by H = p2/2 + (1/N )x4. We again need to distinguish the quantum case from the classical one. At zero temperature, the system is found in the ground state of the Hamiltonian, where 〈p2〉 = (1/4N )〈x4〉 ∼ (1/N )(〈x2〉)2. Considering that 〈x2p2〉 ∼ 1, one obtains that 〈x2〉 = N 1/3, or ζ = 1/3. In contrast, at finite temperatures, one can again apply the equipartition theorem to deduce that 〈x4/N 〉 = kBT , and thus 〈x2〉 ∼ N 1/2, or ζ = 1/2.
D. Effective low-frequency temperature
Given the equivalence seen above between the thermal and non-equilibrium critical behavior, it is useful
exponent definition QPT CPT NESS
[25, 76–78] [15–17]
β 〈x〉 ∼ δλβ 1/2 1/2 1/2
γ 〈x2 − 〈x〉2〉 ∼ |δλ|−γ 1/2 1 1
ζ 〈x2〉λ=λc ∼ N ζ 1/3 1/2 1/2
TABLE II. Critical exponents of mean-field phase transitions (such as the Dicke model). The transition point is set at δλ ≡ λ − λc = 0. The critical theory of the non-equilibrium steady state (NESS) are the same as the classical phase transition (CPT) exponents.
to push this connection further and try to identify an effective temperature for the non-equilibrium case. In quantum optics, this is usually done by comparing the mode occupation with an equilibrium ensemble. In the case of the Dicke model, this approach would lead to an effective temperature that diverges at the transition. To describe the critical properties of the transition it is therefore more convenient to focus on the universal low energy behavior, leading to the definition of a low-energy effective temperature (LEET)[17]. The concept of LEET can be understood by considering a single oscillator x. The commutation and anti-commutation relations of x at different times are respectively described by
GR(t − t′) = i [x(t), x(t′)] , GK (t − t′) = i {x(t), x(t′)} (38)
The universal properties of the phase transition are determined by the low-frequency expansions of GR and GK
ImGR(ω) = Bω + O(ω3) and GK (ω) = A + O(ω2). (39)
Here, we have assumed that both functions are analytic around ω = 0 and noted that by definition, they are respectively antisymmetric and symmetric with respect to ω → −ω. The LEET is defined by inspection of the fluctuationresponse ratio:
χ(ω) ≡ GK (ω)
Im[GR(ω)] (40)
At thermal equilibrium χ(ω) = coth(ω/2T ) and in particular at small ω, χ(ω) ≈ 2T /ω, i.e. a Rayleigh-Jeans distribution. For systems out of thermal equilibrium, χ(ω) is a generically unknown function. However, by using Eq. (39), we find that in general
χ(ω) ≈ A
Bω (41)
This expression allows us to define an effective lowfrequency temperature as T ∗ = A/2B. Note that in this derivation our only assumption was that GR(ω) and


 10
GK(ω) are analytic around ω = 0. For generic nonequilibrium systems, this assumption seems to be valid: the only known exception are quantum systems at zero temperature, where χ(ω) = sign(ω). The emergence of a low-frequency effective temperature is a generic feature of non-integrable non-equilibrium systems, and as such has a long history, see e.g. Refs. [79, 80]. In the context of many-body quantum systems it is predicted to occur in systems as different as voltagebiased two-dimensional gases[81–83], noise-driven resistively shunted Josephson junctions[84, 85], and BECs of exciton polaritons[86, 87]. This effect has a close analogy to the eigenstate thermalization hypothesis (ETH)[88–90]. This principle states that closed systems generically tend to thermalize at long times. Here, the long time delay after the quench is substituted by low-frequencies, i.e. long time differences between two times in a steady state.
V. BEYOND-MEAN-FIELD METHODS
The above-mentioned mean-field analysis has two main limitations: (i) it is valid only in the limit of N → ∞ and (ii) it assumes that all the atoms are coupled homogeneously to the cavity. To overcome these two limitations, different methods have been developed.
A. Bosonic diagrammatic expansion
As we discussed in Sec. III B, the superradiant transition can be described in terms of Holstein–Primakoff (HP) bosons. Keldysh diagrams offer a natural platform to study 1/N corrections, by considering higher order terms in the HP expansion[17, 91]. Let us, for example, consider the number of photons at the critical coupling, for the driven dissipative model. As discussed in Sec. IV C, this number grows as N 1/2. The prefactor was computed in Ref. [17] and found to be in excellent agreement with the numerics for small N – see Fig. 3. See also Ref. [91] for a study of the relaxation dynamics close to the superradiant transition.
B. Fermionic diagrammatic expansion
An alternative method to obtain a controlled perturbative expansion in 1/N is given by the fermionic path integral approach[29]. The key idea is to describe each atomic degree of freedom using the Majorana fermion representation of spin-1/2[93–95]. In this language the spin is replaced by a complex fermion f and a Majorana fermion η. The former keeps track of the polarization of the spins f †f = 1/2 − σz, while the latter ensures the correct commutation relations are respected. This formalism allowed the authors of Ref. [29] to develop a controlled 1/N expansion of the Dicke model. The key
0.6 0.8 1
1
1.5
2
2.5
3
3.5
4
4.5
g/gc
2〈n〉+1
234
0.4
0.6
0.8
1
1.2
1.4
1.6
ln(N)
ln( 2〈n〉c+1 )
FIG. 3. Number of photons at the critical coupling λ = λc, as a function of N , for a Dicke model with ωz = 2, ωc = κ = 1, and γ = 0. Diagrammatic expansion (o), Monte-Carlowave-function method[35, 92] (+), and ζ = 1/2 critical scaling (dashed lines). Reproduced from Ref. [17].
result was that to leading order in 1/N , only one-loop diagrams (and their products) survive. These diagrams can be exactly resummed using the common Dyson resummation, i.e. by adding a self-energy contribution to the free Green’s function of the cavity: [GaR]−1 → [GaR]−1 + ΣaR.
Here [GaR]−1 is the 2 × 2 upper-left block of Eq. (21) and
ΣaR is a loop integral. Importantly, this expression simply corresponds to the spin-spin correlation function and can be written as
ΣR
a (ω) = − 8λ2
N
N
∑
j=1
∫∞
0
dt Im [〈σx
j (t)σx
j (0)〉] eiωt .
(42)
This result has a simple physical meaning: The coupling between the atoms and the cavity is proportional
to 1/√N . Thus, in the limit N → ∞ the feedback of the cavity onto the atoms is negligible below threshold. As a consequence, the cavity feels the free evolution of the spins, and the superradiance transition is determined by a sum over N independent terms. This result is analogous to the Lamb theory of lasing[28, 96–98], where the feedback of the cavity on the atoms is neglected (see Sec. VI for a discussion on the similarities and differences between superradiance and lasing). The superradiant transition occurs when the dressed Green’s function has a pole at zero frequency, or
det [[GR
a ]−1(0) + ΣR
a (0)] = 0 (43)
Substituting Eq. (42) in the expression for [GaR]−1, we obtain the condition for the superradiant transition
det
[(
iκ − ωc + ΣaR(0) ΣaR(0) ΣaR(0) −iκ − ωc + ΣaR(0)
)]
=0,


 11
where we used the fact that ΣaR(0) is real by definition. A direct evaluation leads to
ω2
c + κ2 + 2ωcΣR
a (0) = 0 , (44)
This approach has two limiting cases that coincide with earlier results: (i) For a system at thermal equilibrium 〈σz〉 = (1/2) tanh(ωz/2T ) and γ = 0. In this case, ΣaR(0) = 4λ2〈σz〉/ωz, and we recover the equilibrium result, Eq. (9). (ii) In the presence of single-atom decay and dephasing
〈σx
j (t)σx
j (0)〉 = e−γT t [cos(ωzt) + i〈σz〉 sin(ωzt)] . (45)
where γT = γφ + γ↓. In this case, ΣaR(0) =
4λ2〈σz
j 〉ωz/(ωz2 + γ2), and Eq. (44) becomes equivalent to Eq. (26). In addition, the present diagrammatic approach allows us to consider inhomogeneous systems: Eq. (44) shows that the transition is governed by the disorder-averaged value of λ ̄2 = (1/N ) ∑
j λ2
j . One particular application is the case of inhomogeneous broadening when coupling to Raman transitions between hyperfine states, discussed by Ref. [31]. Furthermore, if the energy splitting of the twolevel atoms is disordered, one sees this approach gives the (ωc2 + κ2)/ωc = 4〈λ2
i /ωz,i〉. An application of this occurs when considering transitions between motional states of a thermal gas[26], for which the two-level system energy, ωzi = ki+Qrecoil − ki with k = ħ2k2/2m, depends on the Boltzmann distributed initial momentum of the atoms.
C. Cumulant expansion
A further way to consider systems with finite N is to derive a hierarchy of coupled equations for all moments of the photon and spin operators. In the thermodynamic limit, N → ∞, only the mean-field parts of these equations survive while at large but finite N the second order correlation functions can give an accurate picture of the behavior. When analyzing the dynamics using simply mean-field theory it is necessary to introduce symmetry breaking terms by hand. This is because the normal state is always a solution to the mean-field equations. By considering the second moments of the distribution one may look for discontinuities in quantities such as the photon number which respect the Z2 symmetry of the model. This allows us to only consider a reduced set of equations for the second moments which respect these symmetries. These techniques are closely related to those used in laser theory to describe the emergence of spontaneous coherence
there[70, 99].
For the Dicke model there are three distinct classes of these equations. The first are those that describe correlations of the photon mode
∂t
〈a†a〉 = −2κ 〈a†a〉 − λN Im[Cax] (46)
∂t 〈aa〉 = −2(iωc + κ) 〈aa〉 − iλN Cax (47)
where we have denoted Cax = 〈aσx〉. The second type of equations are those which involve correlations between the photon and spin degrees of freedom:
∂tCax = − (iωc + κ + γT ) Cax − ωzCay
−iλ
[
(N − 1) Cxx + 1
2
]
, (48)
∂tCay = − (iωc + κ + γT ) Cay − λ 〈σz〉 (〈aa〉 + 〈a†a〉)
+ωzCax − iλ
[
(N − 1)Cxy − i 1
2 〈σz〉
]
.
(49)
In these equations Cαβ means 〈σα
i σβ
j6=i〉 the correlation
between σα at one site and σβ at another. All such correlations are equivalent since each atom is identical. These cross correlations obey:
∂tCxx = −2ωzCxy − 2γT Cxx, (50)
∂tCyy = 2ωzCxy − 2γT Cyy − 4λ 〈σz〉 Re[Cay], (51)
∂tCzz = 4λ 〈σz〉 Re[Cay] − 4γ↓
(
Czz + 1
2 〈σz〉
)
, (52)
∂tCxy = ωz(Cxx − Cyy) − 2γT Cxy − 2λ 〈σz〉 Re[Cax]. (53)
In writing these expression we have broken third order moments into products of first and second moments by assuming that the third order cumulants vanish. These equations do not put any restrictions on the types of decay processes which can be present and those written above include both collective decay channels such as photon loss and individual atomic loss and dephasing. In most cases, the decay channels only shift the position of the transition. One important exception was found by Ref. [30], who showed that the presence of dephasing (γφ) without losses (γ↓ = 0) completely suppresses the transition: This effect is demonstrated in Fig. 4, which shows the behavior at a value of the coupling far above the mean-field prediction for the location of the transition. This figure shows the reduced photon number (〈a†a〉/N ), as a function of N , for various combinations of loss processes. In the case of γ↓ = 0, the dynamics always reaches a normal state with an average
photon number that scales only as √N . This effect is due to the depolarization of the atoms due to sub-leading terms in the 1/N expansion, which can be compensated by decay processes (γ↓ 6= 0) that polarize the atoms. As we will see below, this prediction is in good agreement with the numerical results obtained for finite N .
D. Numerical approaches
For small numbers of atoms it is straightforward to find the exact Hamiltonian or Liouvillian of the appropriate model, determine the density operators in a thermal or steady-state ensemble, and calculate all possible observables. To reach larger system sizes it is possible to use


 12
101
102
0.0
0.1
0.2
0.3
0.4
0.5
102
FIG. 4. Number of photons for λ > λc, obtained from the cumulant expansion method (lines) and from the numerics (dots). The lines correspond, from top to bottom, to γ↓ = γφ = 0 (black), γ↓ = 0.1, γφ = 0 (blue), γ↓ = 0.1, γφ = 0.2 (green) and γ↓ = 0, γφ = 0.02 (red). Other parameters are:
λ√N = 0.9, ωc = 1, ωz = 1, κ = 1/2. Reproduced from Ref. [30].
the collective spin representation of the Dicke model as in Eq. (2). The Hilbert space dimension then scales linearly with the number of atoms and so the problem can again be straightforwardly diagonalized. This approach is, however, limited to only studying collective decay processes. More sophisticated methods are required to study the problem efficiently when individual loss processes are present. In this more general case, a subtle symmetry can be exploited to efficiently calculate the behavior of the system. This remaining symmetry is a permutation symmetry at the level of the density matrix rather than in the Hilbert space: If the master equation can be written as a sum of processes where each term only affects a single site i, then swapping any pair of sites leaves the state unchanged. In this case, each element of the density matrix (ignoring the photon) must obey:
〈sL
1 . . . sL
i . . . sL
j . . . sL
N | ρ |sR
1 . . . sR
i . . . sR
j . . . sR
N〉
≡ 〈sL
1 . . . sL
j . . . sL
i . . . sL
N | ρ |sR
1 . . . sR
j . . . sR
i . . . sR
N〉,
where sL(R) = ±1/2. The full density matrix then separates into sets of permutation-symmetric elements. To find the dynamics of the system it is sufficient to propagate a single representative element from each of these sets, therefore gaining a combinatoric reduction to the size of the Liouvillian. The steady state can also be calculated by finding, in this restricted space, the eigenvector of the Liouvillian with eigenvalue 0. This approach has been applied to a variety of problems which preserve this permutation symmetry. For example, it was used to study spin ensembles[100], lasing models[101], coherent surface plasmons[102], the competition between collective and individual decay channels[103], the behavior of an ensemble of Rydberg polaritons[104], equilibrium properties of a model with a
larger local Hilbert space[105], subradiant states in the Dicke model[106], the effect of individual losses on transient superradiant emission[107] and the crossover between superradiance and lasing[108] (see Sec. VI B). These results are reviewed in Ref. [109], while libraries which implement this method can be found at Refs. [110–112]. This method was also applied to the Dicke model, to study the effect of individual loss processes on the superradiant transition. As shown in Fig. 4, the numerical results are in quantitative agreement with the above-mentioned cumulant expansion[30], valid for large N . Thus, a combination of these two methods is able to cover the entire range of number of atoms; from N = 1 to ∞.
VI. SUPERRADIANCE AND LASING
In this section we discuss the relation between the superradiance transition and lasing. To make this connection clear, in Sec. VI A we first discuss a canonical model of lasing, namely the Tavis–Cummings model. Next, in Sec. VI B we introduce a generalized Dicke model that interpolates between the Dicke and the Tavis–Cummings model. This family of models provides a link between the superradiant transition and the closely related phenomenon of lasing. In Secs. VI C-VI D, we describe different types of lasing transitions (regular lasing, counter lasing, and superradiant lasing) and explain their similarities and differences with the superradiant transition.
A. The Tavis–Cummings model
The Tavis–Cummings model is given by a Dicke model without counter-rotating terms:
H = ωca†a + ωz
N
∑
j=1
σz
j + √λN
N
∑
j=1
(aσ+
j + aσ−
j ) (54)
This model conserves the total number of excitations Nex = a†a + ∑
j σz
j . This symmetry is associated with a
U (1) gauge symmetry a → eiφa and σ− → eiφσ−. The equilibrium Tavis–Cummings model has a phase transi
tion at λ = √ωcωz, where the symmetry is spontaneously broken. This critical coupling differs by a factor of two from the Dicke result, as only half the matter-light coupling terms are present. In the presence of decay, the Tavis–Cummings model does not show a superradiant transition[21, 113, 114]. This result has a simple physical meaning: because the model does not have counter-rotating terms, it will always flow to a trivial steady state, where the cavity is empty and the spins are polarized in the σz = −1/2 direction. The superradiant transition occurs only if the total number of excitations is kept constant (when no loss processes are present). The Tavis–Cummings model can nevertheless show a lasing transition if the atoms are pumped.


 13
In what follows, we explain the difference between the superradiant transition and the lasing transition, by considering a simple model in which both transitions occur.
B. Generalized Dicke model
The generalized Dicke model is a simple interpolation between the Dicke model (1) and the Tavis–Cummings model (54),
H = ωca†a + ωz
N
∑
j=1
σz
j + √λN
N
∑
j=1
(aσ+
j + a†σ−
j)
+ λ′
√N
N
∑
j=1
(aσ−
j + a†σ+
j ) . (55)
This model includes the Dicke model (λ = λ′) and the Tavis–Cummings model (λ′ = 0) as special cases. It can be realized using the 4-level scheme described in Sec. II, where rotating and counter-rotating terms are induced by two separate pumping fields. Using the Holstein–Primakoff approximation[65], one can map this model to two coupled harmonic oscillators:
H = ωca†a + ωzb†b + λ(ab† + a†b) + λ′(ab + a†b†) . (56)
This Hamiltonian can be represented as a 4 × 4 matrix
H=1
2 (a a† b b†)

   
ωc 0 λ λ′ 0 ωc λ′ λ λ λ′ ωz 0 λ′ λ 0 ωz

   

   
a†
a b†
b

   
(57)
where λ± = λ ± λ′. Following the same analysis as in Sec. III B one obtains
G−1
R=

   
ω − ωc + iκ 0 −λ −λ′ 0 −ω − ωc − iκ −λ′ −λ −λ −λ′ ω − ωz 0
−λ′ −λ 0 −ω − ωz

   
(58) where κ is the cavity decay rate. The superradiant transition is signaled by det[G−1
R (ω = 0)] = 0, or
(λ2 − λ′2)2 − 2(λ2 + λ′2)ωcωz + (κ2 + ω2
c )ω2
z = 0 (59)
Let us now consider the two above-mentioned limiting cases: in the Dicke model (λ = λ′), one recovers Eq. (22). In contrast, for the Tavis–Cummings model (λ′ = 0). the superradiant transition occurs for
(λ2 − ωcωz)2 + κ2ω2
z = 0. (60)
This condition cannot be satisfied for any κ 6= 0, in agreement with the results of Sec. VI A. In general, for any finite κ, the critical coupling diverges when approaching the TC limit of λ′ → 0[21]. It is worth also noting that
identical behavior occurs if we set λ = 0 and consider the model with only only counter-rotating terms. In fact this limit is also the Tavis-Cummings model after a unitary transform, rotating the spin by π about the x axis, thus sending σ± → σ∓ and σz → −σz. When considering the full phase diagram of dissipative Dicke model with λ 6= λ′, some new features can arise. In particular there exists a phase where both the normal state and superradiant state are stable, and a multicritical point where this phase vanishes, as has been reported a number of times[21, 114, 115].
C. Regular and counter-lasing transitions
Although the Tavis–Cummings model cannot undergo a superradiant transition, this model can describe the transition to a lasing state[28]. We first discuss how this distinct form of coherent light arises in this model, before considering how the lasing state and superradiant states can be related and distinguished. To obtain lasing, it is sufficient to supplement the TC model, Eq. (54), by an incoherent driving term that pumps the atoms in the excited state. This effect can be described by adding a Lindblad operator to Eq. (4) where L = σ+ with a rate γ↑. This process is directly analogous to a three-level model of a laser, where one of the levels is pumped incoherently, leading to population inversion. The resulting phase transition leads to a lasing state, rather than a superradiant state. The relation of lasing and superradiance is made clear if one considers the generalized Dicke model (with λ′ 6= λ) combined with the incoherent pumping discussed above[108]. In this case, one sees two distinct ordered states: a lasing state that continuously connects to the state with λ′ = 0, and a superradiant state that connects to the Dicke model with λ′ = λ, γ↑ = 0. These two states occupy disconnected regions on the λ′, γ↑ phase diagram – see Fig. 5. From a physical perspective, the lasing and superradiant transitions can be clearly distinguished as lasing only occurs when 〈σz〉 > 0, while the superradiant state occurs only for 〈σz〉 < 0[108]. In addition to the presence or absence of inversion, the lasing and superradiant phases have a different nature: In the superradiant phase the field is locked to the rotating frame of the pump. In contrast, in a lasing phase, the coherent emission is not locked to the pump frequency and is time dependent in the frame of the pump. From a mathematical perspective the Dicke transition corresponds to a subcritical pitchfork instability, where a single eigenvalue vanishes[116]. In contrast, the lasing transition corresponds to a critical Hopf bifurcation, i.e. to a point where two eigenvalues become unstable simultaneously, by crossing the real axis without passing through the origin. Because the unstable modes have a finite real part, this transition generically leads to oscillations. Other examples of Hopf bifurcations in generalized Dicke models were predicted by Ref. [27] and Ref. [58], who


 14
FIG. 5. Phase diagram of the generalized Dicke model, Eq. (55), with repumping γ↑. This model shows regions of superradiance (SR), counter-lasing (CL), and regular lasing (RL). A normal (N) region separates the regions without population inversion (SR and CL) from the regular lasing region. Numerical parameters: ωz = 1, ω0 = 1, λ = 0.9, κ = 0.5, γT = 0.5. Adapted from Ref. [108].
considered the effects of additional terms, such as U Sz2 and ΩSx. When the instability is crossed, the system generically gives rise to oscillating superradiant phases, described by limit cycles [27, 117]. In addition to standard lasing for the inverted state, a lasing instability can alternatively be obtained for the Dicke model with negative detuning of the cavity (ωc < 0), where the superradiant transition does not occur[13, 31]. Moreover, even in the absence of incoherent pumping (〈σz〉 < 0) and for positive cavity detunings (ωc > 0), a lasing transition can be obtained in the generalized Dicke model of Sec. VI B. This transition occurs when the counter-rotating terms lead to a coherent emission of photons from the cavity. It was termed the “inverted-lasing”[108] or “counter-lasing”[118] transition and had been observed experimentally by Zhiqiang et al.[8], see Fig. 6.
D. Superradiant lasers
As noted above, the Tavis–Cummings model with incoherent pumping can undergo a transition to a coherent state, i.e. lasing. The connection between this transition and the transient superradiance discussed by Dicke has been considered a number of times[119–122]. As mentioned in Sec. I, in the absence of a cavity, transient superradiance produces a coherent pulse by effectively synchronizing the emission of all atoms through the collective decay process. By placing many atoms in a bad cavity, and continuously incoherently repopulating the excited state, one may try to drive a continuous superradiance process, which has been termed a superradiant laser[120]. Such a device based on atomic transitions can boast a very narrow linewidth, determined by the sharply defined atomic resonance frequency, rather than the cavity. If one uses a suppressed electronic transition for the lasing level, this
FIG. 6. Comparison between (a) experimental and (b) theoretical phase diagrams for the generalized Dicke system, Eq. (55), in the absence of repumping. The system can be either normal (N), superradiant (SR), or unstable/counterlasing (U). The SR regime below the yellow line shows transient oscillations in time and is possibly related to the oscillating superradiance of Ref. [27]. The parameters used for theoretical calculation correspond to the experimental values: cavity mode frequency ωc = 100 kHz, dissipation κ = 107 kHz, and energy splitting ωz = 77kHz. The atomic polarization is assumed to be 〈σz〉 = −0.25 and the dissipation γT = 30kHz. Reproduced from Ref. [118].
allows a very small natural linewidth γ, but yet superradiant lasing can emerge in the collective strong coupling regime, N λ2 κγ. Moreover, the linewidth at peak lasing power scales as N −2; this suggests a potential mHz linewidth from 106 atoms, a level that could significantly improve atomic clock accuracies[121]. Earlier works[120] were based on a three-level lasing scheme, and did not address how superradiant lasing arises in the presence of individual decay and dephasing of the atoms. A simpler two-level description was given in Refs. [121, 122], using the cumulant expansion approach described in Sec. V C. Such a superradiant laser has been realized experimentally, in a scheme where the lasing transition was actually a two photon Raman transition[123, 124], enabling tuning of both the matter light coupling λ and the effective natural linewidth γ of the transition.
VII. CLOSELY RELATED MODELS
So far in this review, we have focused on the Dicke model, as well as the generalized Dicke model in which we allow distinct strengths of the rotating and counterrotating terms. There do however exist a number of models that are closely related to the Dicke model, involving


 15
coupling between many two-level systems and a common cavity mode, as well as models such as the Rabi model that can be shown to have a close connection to superradiance. Here we provide a brief summary of these models, and the novel physics they can introduce.
A. Extended Dicke models
The Raman driving scheme used to realize the Dicke model generates additional terms that need to be taken into account. In particular, the difference between the cavity-photon-induced Stark shifts in the two atomic states leads to a term U a†aσz. This term can also be seen as a modification of the cavity frequency depending on the atomic state. For the motional state realization, such a term is inevitable (due to the different overlaps between the two momentum states with the cavity optical lattice)[11, 12]. For the Raman realization, the strength of U can in principle be turned to zero[7]. Such a term has been studied extensively in Ref. [27], where it was seen to enable bistability between normal and superradiant states, as well as distinct superradiant states and time-dependent attractors, i.e. limit cycles. Another additional term that can be easily engineered is a drive, HF = F (a+a†), which corresponds to a coherent light source coupled directly to the cavity mode. This term has the same physical effect as H′
F = F σx, these two forms being related by a unitary transformation. This latter term arises naturally in many realizations of the Dicke model using trapped ions[20, 58, 59, 62, 63]. These two terms break the Z2 symmetry of the Dicke model, and thus destroy the phase transition. However, there can still be optical bistability[125] between a high field and low field state, i.e. the open-system analog of a first order phase transition. The behavior of this model at large driving has also been recently discussed in Ref. [115], establishing the connection to breakdown of the photon blockade seen in the single-atom Jaynes-Cummings model[126].
B. Disordered Dicke model
The above models involve adding extra terms to the Dicke model; another class of closely related models involves considering the role of disorder. i.e., returning to Eq. (1) in terms of individual two-level systems, and allowing different energies or coupling strengths for different systems:
H = ωca†a +
N
∑
j=1
ωj
zσz
j + √2N (a + a†)
∑
j
λj σx
j . (61)
Such models have been studied in a wider variety of contexts, including the effects of disorder on dynamical superradiance in a low Q cavity[127], the phase diagram of microcavity polaritons[128, 129], solid state quantum
memories[130], as well as for cold atom in optical cavities, accounting for the spatial variation of the cavity modes[31]. Several works in this context have investigated the dynamics of an initially prepared state, using either brute force numerics for small systems[131–133], or matrix product state approaches[134]. The existence of such disorder prevents the simplification of replacing individual spins by a collective spin operator, hence the need for efficient numerical methods to explore this enlarged Hilbert space[134]. It is however notable that in the case where ωzj
is disordered, while λj = λ, the model can be shown to be integrable, as a special case of a Richardson-Gaudin model[135–138]. In addition to the dynamics, one can also calculate the phase diagram of the disordered Dicke model by mean-field approaches[128, 129], showing that the disorder does not destroy the superradiant phase, but modifies the phase boundary.
C. Floquet Dicke models
Another class of driven-dissipative generalized Dicke models involve time dependent couplings. In particular, Floquet-Dicke models where λ(t) = λ0 +∆λ cos(Ωt) have been considered[139]. These models show a complex phase diagram, depending on the ratio of the drive frequency to other energy scales in the model. Recent work on the same model has studied how time dependent driving can suppress the formation of the superradiant state[140].
D. Scaling limit of the Rabi model
We finally consider a model that has a quite different structure to the Dicke model, but nonetheless can show a similar superradiance transition. This is the Rabi model, describing the coupling between a quantized harmonic oscillator and a single spin:
H = ωca†a + ωzσz + 2λ(a + a†)σx . (62)
To observe the superradiant transition in this model, Hwang et al.[141, 142] proposed considering the limit in which the atomic splitting ωz tends to infinity. This limit
can be formally studied by defining ωz = ηω ̃z, λ = λ ̃√η and considering the limit of η → ∞ such that λ2/(ωcωz) remains finite. If one considers the mean field ansatz of Sec. III A, one finds the ground state free energy
F (α) = ωcα2 − 1
2
√
η2ω ̃z2 + 16ηλ ̃2α2. In order to consider
the limit η → ∞, it is convenient to consider α = √ηx which gives:
F (x) = η
[
ωcx2 − 1
2
√
ω ̃z2 + 16λ ̃2x2
]
. (63)
This expression is equivalent to the T = 0 form of Eq. (8) with η playing the role of the number of atoms. In the limit η → ∞, there is a sharp phase transition at λ ̃ =
√ω ̃zωc/2, analogous to the Dicke model.


 16
The phase transition of this model can also be found by adiabatically eliminating the state of the two-level system using a Schrieffer-Wolff transformation, leading to an effective photon-only problem
H = − ωz
2 + ωca†a − λ2
ωz
(a + a†)2 (64)
After a Bogoliubov transformation, this expression gives a photon frequency, √ωc(ωc − 4λ2/ωz), which vanishes at the transition.
VIII. CONCLUSION
The Dicke model is one of the fundamental models of cavity quantum electro-dynamics (cavity-QED), describing the coupling of many atoms to a single cavity mode. The thermodynamic limit of this model is achieved by considering an infinite number of atoms, whose coupling to the cavity tends to zero. This model can undergo a phase transition to a superradiant state at a critical value of the light-matter coupling. Various physical realizations of this model have been considered, which may be thought of as analog quantum simulators of the Dicke model, built from driven atoms in cavities, superconducting qubits, or trapped ions. In this Progress Report, we introduced the reader to the equilibrium and nonequilibrium behavior of this model and showed how to calculate the critical properties of the superradiant transition. For simplicity, we focused on the simplest realization of the Dicke model where mean-field theory gives a good understanding of the behavior. Our discussion focused on the theoretical aspects of the transition. Experiments were able to probe a diverging susceptibility at the transition[143], but the critical exponents were not found to match the theoretical expectations[144]. This point certainly deserves further investigation. A natural generalization of this model involves two coupled cavity modes, leading to a competition between two superradiant phases. At the interface between these two phases the model shows an enlarged U (1) symmetry[145, 146], as realized experimentally recently[147, 148]. Such experiments have prompted theoretical discussion of the possibility of a vestigial ordered phase[149], where the two cavities become phase locked but without superradiance, as well as the nature of the excitations close to the U (1) symmetric point[150]. A further extension in this direction leads to multi-mode cavities, which give rise to spatially varying, cavity-mediated interactions among the atoms [14, 151, 152]. This system may lead to critical behavior beyond a mean field description[153, 154], give rise to new glassy phases[155–158], and have potential applications for memory storage[159, 160] and optimization problems[161]. The analysis of driven dissipative Dicke model raises many interesting questions. For example, the zerotemperature Dicke model was considered by Emary and
Brandes[162, 163] in the framework of classical and quantum chaos. These authors found that the Dicke model (but not the Tavis–Cummings model) has a sharp transition between regular and chaotic motion. Interestingly, in the limit of large N , the position of the onset of chaos coincides with the quantum phase transition. The relation between quantum chaos and thermalization in the Dicke model was studied for example by Refs. [164–168]. To fully access the chaotic regime, it is necessary to go beyond the linear stability analysis reviewed in this report. In addition to the critical behavior of the open Dicke model discussed in this review, other works have analyzed the behavior of this model from alternate perspectives, such as quantum information approaches[169], large deviation approaches and the s-ensemble[170], and fluctuation-dissipation relations[171]. As we have shown, despite its long history, the Dicke model has continued to reveal new insights about the relation of phase transitions in equilibrium and driven systems. As a paradigmatic model of many body quantum optics, it continues to play an important role in framing discussions of collective behavior. Given the variety of different directions currently studied experimentally and theoretically, it is likely new understanding will continue to arise from this field in the future. Acknowledgments We would like to thank QingHu Chen, Sebastian Diehl, Peter Domokos, Tobias Donner, Andreas Hemmerich, Benjamin Lev, Francesco Piazza, Peter Rabl, and Nathan Shammah for reading an earlier version of this manuscript and giving important comments. P.K. acknowledges support from EPSRC (EP/M010910/1) and the Austrian Academy of Sciences (O ̈ AW). P.K. and J.K. acknowledge support from EPSRC program “Hybrid Polaritonics” (EP/M025330/1). M.M.R. and E.G.D.T. are supported by the Israel Science Foundation Grant No. 1542/14.
Appendix A: Equations of motion and retarded Green’s functions
In this appendix we show how to obtain the retarded Green’s functions of a set of operators, starting from their Heisenberg equations of motion. Our approach applies to equations of motion given by the linear relation,
v ̇ (t) =M v(t), (A1)
Our goal is to find the corresponding retarded Green’s function, defined by
GR
i,j (t) =−i
〈[
vi(t), v†
j (0)
]〉
θ(t). (A2)
We denote the equal-time correlation functions of these
operators by a constant matrix Si,j =
〈[
vi(0), v†
j (0)
]〉
.
In terms of this matrix, we may write:
∂tGR
i,j (t) = −iδ(t)Si,j + Mi,kGR
k,j(t). (A3)


 17
By defining the Fourier transform as
f (ω) =
∞
∫
−∞
dt eiωtf (t),
we can write Eq. (A3) in the matrix form
(M + iω1)GR(ω) = iS.
This equations can be explicitly inverted to give
GR(ω) = [ω1 − iM ]−1 S. (A4)
This expression gives a general connection between the linear equations of motions for a set of operators, and the retarded Green’s function for the same set of operators. Note that this expression is valid as long as the equaltime commutators, Si,j, are constant in time.
[1] R. H. Dicke, Coherence in Spontaneous Radiation Processes, Phys. Rev. 93, 99 (1954).
[2] K. Hepp and E. H. Lieb, Equilibrium statistical mechanics of matter interacting with the quantized radiation field, Phys. Rev. A 8, 2517 (1973). [3] Y. K. Wang and F. T. Hioe, Phase Transition in the Dicke Model of Superradiance, Phys. Rev. A 7, 831 (1973).
[4] F. Hioe, Phase transitions in some generalized Dicke models of superradiance, Phys. Rev. A 8, 1440 (1973). [5] H. Carmichael, C. Gardiner, and D. Walls, Higher order corrections to the Dicke superradiant phase transition, Phys. Lett. A 46, 47 (1973).
[6] G. C. Duncan, Effect of antiresonant atom-field interactions on phase transitions in the Dicke model, Phys. Rev. A 9, 418 (1974). [7] F. Dimer, B. Estienne, A. S. Parkins, and H. J. Carmichael, Proposed realization of the Dicke-model quantum phase transition in an optical cavity QED system, Phys. Rev. A 75, 013804 (2007). [8] Z. Zhiqiang, C. H. Lee, R. Kumar, K. Arnold, S. J. Masson, A. Parkins, and M. Barrett, Nonequilibrium phase transition in a spin-1 Dicke model, Optica 4, 424 (2017). [9] P. Domokos and H. Ritsch, Collective Cooling and SelfOrganization of Atoms in a Cavity, Phys. Rev. Lett. 89, 253003 (2002). [10] A. T. Black, H. W. Chan, and V. Vuleti ́c, Observation of Collective Friction Forces due to Spatial SelfOrganization of Atoms: From Rayleigh to Bragg Scattering, Phys. Rev. Lett. 91, 203001 (2003). [11] D. Nagy, G. Ko ́nya, G. Szirmai, and P. Domokos, Dicke-Model Phase Transition in the Quantum Motion of a Bose-Einstein Condensate in an Optical Cavity, Phys. Rev. Lett. 104, 130401 (2010). [12] K. Baumann, C. Guerlin, F. Brennecke, and T. Esslinger, Dicke quantum phase transition with a superfluid gas in an optical cavity, Nature 464, 1301 (2010). [13] J. Klinder, H. Keßler, M. Wolke, L. Mathey, and A. Hemmerich, Dynamical phase transition in the open Dicke model, Proc. Nat. Acad. Sci. 112, 3290 (2015). [14] V. D. Vaidya, Y. Guo, R. M. Kroeze, K. E. Ballantine, A. J. Kolla ́r, J. Keeling, and B. L. Lev, TunableRange, Photon-Mediated Atomic Interactions in Multimode Cavity QED, Phys. Rev. X 8, 011002 (2018). [15] D. Nagy, G. Szirmai, and P. Domokos, Critical exponent of a quantum-noise-driven phase transition: The open
system Dicke model, Phys. Rev. A 84, 043637 (2011). [16] B. O ̈ ztop, M. Bordyuh, O. E. M ̈ustecapliog ̆lu, and H. E. Tu ̈reci, Excitations of optically driven atomic condensate in a cavity: theory of photodetection measurements, New J. Phys. 14, 085011 (2012). [17] E. G. Dalla Torre, S. Diehl, M. D. Lukin, S. Sachdev, and P. Strack, Keldysh approach for nonequilibrium phase transitions in quantum optics: Beyond the Dicke model in optical cavities, Phys. Rev. A 87, 023831 (2013). [18] A. Mezzacapo, U. Las Heras, J. Pedernales, L. DiCarlo, E. Solano, and L. Lamata, Digital quantum Rabi and Dicke models in superconducting circuits, Sci. Rep. 4, 7482 (2014).
[19] L. Lamata, Digital-analog quantum simulation of generalized Dicke models with superconducting circuits, Sci. Rep. 7, 43768 (2017).
[20] I. Aedo and L. Lamata, Analog quantum simulation of generalized Dicke models in trapped ions, Phys. Rev. A 97, 042317 (2018). [21] J. Keeling, M. J. Bhaseen, and B. D. Simons, Collective Dynamics of Bose-Einstein Condensates in Optical Cavities, Phys. Rev. Lett. 105, 043001 (2010). [22] M. Gross and S. Haroche, Superradiance: An essay on the theory of collective spontaneous emission, Phys. Rep. 93, 301 (1982).
[23] B. M. Garraway, The Dicke model in quantum optics: Dicke model revisited, Philos. Trans. Royal Soc. A 369, 1137 (2011). [24] H. Ritsch, P. Domokos, F. Brennecke, and T. Esslinger, Cold atoms in cavity-generated dynamical optical potentials, Rev. Mod. Phys. 85, 553 (2013). [25] Q.-H. Chen, Y.-Y. Zhang, T. Liu, and K.-L. Wang, Numerically exact solution to the finite-size Dicke model, Phys. Rev. A 78, 051801 (2008). [26] F. Piazza, P. Strack, and W. Zwerger, Bose–Einstein condensation versus Dicke–Hepp–Lieb transition in an optical cavity, Ann. Phys. 339, 135 (2013). [27] M. J. Bhaseen, J. Mayoh, B. D. Simons, and J. Keeling, Dynamics of nonequilibrium Dicke models, Phys. Rev. A 85, 013817 (2012). [28] M. O. Scully and M. S. Zubairy, Quantum Optics (Cambridge University Press, 1997). [29] E. G. Dalla Torre, Y. Shchadilova, E. Y. Wilner, M. D. Lukin, and E. Demler, Dicke phase transition without total spin conservation, Phys. Rev. A 94, 061802 (2016). [30] P. Kirton and J. Keeling, Suppressing and restoring the Dicke superradiance transition by dephasing and decay,


 18
Phys. Rev. Lett. 118, 123602 (2017). [31] Z. Zhiqiang, C. H. Lee, R. Kumar, K. Arnold, S. J. Masson, A. Grimsmo, A. Parkins, and M. Barrett, Dicke model simulation via cavity-assisted Raman transitions, (2018), 1801.07888. [32] K. Rza ̇zewski, K. W ́odkiewicz, and W. Z ̇ akowicz, Phase transitions, two-level atoms, and the A 2 term, Phys. Rev. Lett. 35, 432 (1975). [33] I. Bialynicki-Birula and K. Rza ̇zewski, No-go theorem concerning the superradiant phase transition in atomic systems, Phys. Rev. A 19, 301 (1979).
[34] J. Keeling, Coulomb interactions, gauge invariance, and phase transitions of the Dicke model, J. Phys. 19, 295213 (2007). [35] A. Vukics and P. Domokos, Adequacy of the Dicke model in cavity QED: A counter-no-go statement, Phys. Rev. A 86, 053807 (2012). [36] A. Vukics, T. Grießer, and P. Domokos, Elimination of the A-Square Problem from Cavity QED, Phys. Rev. Lett. 112, 073601 (2014). [37] A. Vukics, T. Grießer, and P. Domokos, Fundamental limitation of ultrastrong coupling between light and atoms, Phys. Rev. A 92, 043835 (2015). [38] T. Grießer, A. Vukics, and P. Domokos, Depolarization shift of the superradiant phase transition, Phys. Rev. A 94, 033815 (2016). [39] D. De Bernardis, T. Jaako, and P. Rabl, Cavity quantum electrodynamics in the nonperturbative regime, Phys. Rev. A 97, 043820 (2018). [40] D. De Bernardis, P. Pilar, T. Jaako, S. De Liberato, and P. Rabl, Breakdown of gauge invariance in ultrastrong-coupling cavity QED, arXiv:1805.05339 (2018), 1805.05339. [41] A. Stokes and A. Nazir, Gauge ambiguities in ultrastrong-coupling QED: the Jaynes-Cummings model is as fundamental as the Rabi model, arXiv:1805.06356 (2018), 1805.06356. [42] J. Flick, M. Ruggenthaler, H. Appel, and A. Rubio, Atoms and molecules in cavities, from weak to strong coupling in quantum-electrodynamics (QED) chemistry, Proc. Natl. Acad. Sci. 114, 3026 (2017). [43] V. Rokaj, D. M. Welakuh, M. Ruggenthaler, and A. Rubio, Light–matter interaction in the long-wavelength limit: no ground-state without dipole self-energy, J. Phys. B 51, 034005 (2018). [44] P. Eastham and P. Littlewood, Bose condensation in a model microcavity, Solid State Commun. 116, 357 (2000). [45] P. R. Eastham and P. B. Littlewood, Bose condensation of cavity polaritons beyond the linear regime: The thermal equilibrium of a model microcavity, Phys. Rev. B 64, 235101 (2001). [46] H. Deng, H. Haug, and Y. Yamamoto, Excitonpolariton Bose-Einstein condensation, Rev. Mod. Phys. 82, 1489 (2010). [47] I. Carusotto and C. Ciuti, Quantum fluids of light, Rev. Mod. Phys. 85, 299 (2013). [48] J. Kasprzak, M. Richard, S. Kundermann, A. Baas, P. Jeambrun, J. M. J. Keeling, F. M. Marchetti, M. H. Szymanska, R. Andre ́, J. L. Staehli, V. Savona, P. B. Littlewood, B. Deveaud, and L. S. Dang, Bose-Einstein condensation of exciton polaritons., Nature 443, 409 (2006).
[49] Y. Sun, P. Wen, Y. Yoon, G. Liu, M. Steger, L. N. Pfeiffer, K. West, D. W. Snoke, and K. A. Nelson, Bose-Einstein Condensation of Long-Lifetime Polaritons in Thermal Equilibrium, Phys. Rev. Lett. 118, 016602 (2017). [50] A. A. Houck, H. E. Tu ̈reci, and J. Koch, On-chip quantum simulation with superconducting circuits, Nat. Phys. 8, 292 (2012).
[51] P. Nataf and C. Ciuti, No-go theorem for superradiant quantum phase transitions in cavity QED and counterexample in circuit QED, Nat. Commun. 1, 72 (2010). [52] O. Viehmann, J. von Delft, and F. Marquardt, Superradiant Phase Transitions and the Standard Description of Circuit QED, Phys. Rev. Lett. 107, 113602 (2011). [53] C. Ciuti and P. Nataf, Comment on “Superradiant Phase Transitions and the Standard Description of Circuit QED”, Phys. Rev. Lett. 109, 179301 (2012). [54] N. Lambert, Y. Matsuzaki, K. Kakuyanagi, N. Ishida, S. Saito, and F. Nori, Superradiance with an ensemble of superconducting flux qubits, Phys. Rev. B 94, 224510 (2016). [55] M. Bamba, K. Inomata, and Y. Nakamura, Superradiant Phase Transition in a Superconducting Circuit in Thermal Equilibrium, Phys. Rev. Lett. 117, 173601 (2016). [56] T. Jaako, Z.-L. Xiang, J. J. Garcia-Ripoll, and P. Rabl, Ultrastrong-coupling phenomena beyond the Dicke model, Phys. Rev. A 94, 033850 (2016).
[57] M. Bamba and N. Imoto, Circuit configurations which may or may not show superradiant phase transitions, Phys. Rev. A 96, 053857 (2017). [58] S. Genway, W. Li, C. Ates, B. P. Lanyon, and I. Lesanovsky, Generalized Dicke nonequilibrium dynamics in trapped ions, Phys. Rev. Lett. 112, 023603 (2014). [59] J. Pedernales, I. Lizuain, S. Felicetti, G. Romero, L. Lamata, and E. Solano, Quantum rabi model with trapped ions, Sci. Rep. 5, 15472 (2015). [60] A. Safavi-Naini, R. Lewis-Swan, J. Bohnet, M. Ga ̈rttner, K. Gilmore, J. Jordan, J. Cohn, J. Freericks, A. Rey, and J. Bollinger, Verification of a many-ion simulator of the Dicke model through slow quenches across a phase transition, Phys. Rev. Lett. 121, 040503 (2018). [61] D. Leibfried, R. Blatt, C. Monroe, and D. Wineland, Quantum dynamics of single trapped ions, Rev. Mod. Phys. 75, 281 (2003). [62] D. Porras and J. I. Cirac, Effective Quantum Spin Systems with Trapped Ions, Phys. Rev. Lett. 92, 207901 (2004). [63] C.-C. J. Wang, A. C. Keith, and J. K. Freericks, Phonon-mediated quantum spin simulator employing a planar ionic crystal in a Penning trap, Phys. Rev. A 87, 013422 (2013). [64] C. Hamner, C. Qu, Y. Zhang, J. Chang, M. Gong, C. Zhang, and P. Engels, Dicke-type phase transition in a spin-orbit-coupled Bose–Einstein condensate, Nat. Commun. 5, 4023 (2014). [65] T. Holstein and H. Primakoff, Field Dependence of the Intrinsic Domain Magnetization of a Ferromagnet, Phys. Rev. 58, 1098 (1940). [66] J. Gelhausen, M. Buchhold, and P. Strack, Many-body quantum optics with decaying atomic spin states: (γ, κ) Dicke model, Phys. Rev. A 95, 063824 (2017).


 19
[67] A. Altland and B. Simons, Condensed Matter Field Theory (Cambridge University Press, 2010).
[68] A. Kamenev, Field Theory of Non-Equilibrium Systems, 1st ed. (Cambridge University Press, 2011). [69] L. M. Sieberer, M. Buchhold, and S. Diehl, Keldysh field theory for driven open quantum systems, Reports on Progress in Phys. 79, 096001 (2016).
[70] H. Haken, The semiclassical and quantum theory of the laser, in Quantum Optics, edited by S. M. Kay and A. Maitland (Academic Press, New York, 1970) p. 201. [71] N. Lambert, C. Emary, and T. Brandes, Entanglement and the phase transition in single-mode superradiance, Phys. Rev. Lett. 92, 073602 (2004). [72] N. Lambert, C. Emary, and T. Brandes, Entanglement and entropy in a spin-boson quantum phase transition, Phys. Rev. A 71, 053804 (2005). [73] T.-L. Wang, L.-N. Wu, W. Yang, G.-R. Jin, N. Lambert, and F. Nori, Quantum Fisher information as a signature of the superradiant quantum phase transition, New J. Phys. 16, 063039 (2014).
[74] E. Wolfe and S. Yelin, Certifying separability in symmetric mixed states of N qubits, and superradiance, Phys. Rev. Lett. 112, 140402 (2014).
[75] N. G. Van Kampen, Stochastic processes in physics and chemistry, Vol. 1 (Elsevier, 1992).
[76] J. Vidal and S. Dusuel, Finite-size scaling exponents in the Dicke model, Europhys. Lett. 74, 817 (2006). [77] T. Liu, Y.-Y. Zhang, Q.-H. Chen, and K.-L. Wang, Large-N scaling behavior of the ground-state energy, fidelity, and the order parameter in the Dicke model, Phys. Rev. A 80, 023810 (2009). [78] M. Liu, S. Chesi, Z.-J. Ying, X. Chen, H.-G. Luo, and H.-Q. Lin, Universal scaling and critical exponents of the anisotropic quantum Rabi model, Phys. Rev. Lett. 119, 220601 (2017). [79] P. Hohenberg and B. I. Shraiman, Chaotic behavior of an extended system, Physica D 37, 109 (1989). [80] M. C. Cross and P. C. Hohenberg, Pattern formation outside of equilibrium, Rev. Mod. Phys. 65, 851 (1993). [81] A. Mitra, S. Takei, Y. B. Kim, and A. J. Millis, Nonequilibrium Quantum Criticality in Open Electronic Systems, Phys. Rev. Lett. 97, 236808 (2006). [82] A. Mitra and A. J. Millis, Current-driven quantum criticality in itinerant electron ferromagnets, Phys. Rev. B 77, 220404 (2008). [83] S. Takei, W. Witczak-Krempa, and Y. B. Kim, Nonequilibrium quantum criticality in bilayer itinerant ferromagnets, Phys. Rev. B 81, 125430 (2010). [84] E. G. Dalla Torre, E. Demler, T. Giamarchi, and E. Altman, Quantum critical states and phase transitions in the presence of non equilibrium noise, Nat. Phys. 6, 806 (2010). [85] E. G. Dalla Torre, E. Demler, T. Giamarchi, and E. Altman, Dynamics and universality in noise-driven dissipative systems, Phys. Rev. B 85, 184302 (2012). [86] L. Sieberer, S. Huber, E. Altman, and S. Diehl, Dynamical critical phenomena in driven-dissipative systems, Phys. Rev. Lett. 110, 195301 (2013). [87] L. Sieberer, S. Huber, E. Altman, and S. Diehl, Nonequilibrium functional renormalization for drivendissipative Bose-Einstein condensation, Phys. Rev. B 89, 134310 (2014).
[88] J. M. Deutsch, Quantum statistical mechanics in a closed system, Phys. Rev. A 43, 2046 (1991).
[89] M. Srednicki, Chaos and quantum thermalization, Phys. Rev. E 50, 888 (1994). [90] M. Rigol, V. Dunjko, and M. Olshanii, Thermalization and its mechanism for generic isolated quantum systems, Nature 452, 854 (2008).
[91] J. Lang and F. Piazza, Critical relaxation with overdamped quasiparticles in open quantum systems, Phys. Rev. A 94, 033628 (2016). [92] K. Mølmer, Y. Castin, and J. Dalibard, Monte Carlo wave-function method in quantum optics, J. Opt. Soc. Am. B 10, 524 (1993).
[93] A. M. Tsvelik, Quantum field theory in condensed matter physics (Cambridge university press, 2007). [94] A. Shnirman and Y. Makhlin, Spin-Spin correlators in the Majorana representation, Phys. Rev. Lett. 91, 207204 (2003). [95] P. Schad, Y. Makhlin, B. Narozhny, G. Scho ̈n, and A. Shnirman, Majorana representation for dissipative spin systems, Ann. Phys. 361, 401 (2015). [96] W. E. Lamb Jr, Theory of an optical maser, Phys. Rev. 134, A1429 (1964). [97] G. Agarwal and S. D. Gupta, Steady states in cavity QED due to incoherent pumping, Phys. Rev. A 42, 1737 (1990).
[98] P. Gartner, Two-level laser: Analytical results and the laser transition, Phys. Rev. A 84, 053804 (2011).
[99] H. Haken, Cooperative phenomena in systems far from thermal equilibrium and in nonphysical systems, Rev. Mod. Phys. 47, 67 (1975). [100] B. A. Chase and J. M. Geremia, Collective processes of an ensemble of spin-1/2 particles, Phys. Rev. A 78, 052101 (2008). [101] M. Xu, D. A. Tieri, and M. J. Holland, Simulating open quantum systems by applying SU(4) to quantum master equations, Phys. Rev. A 87, 062101 (2013). [102] M. Richter, M. Gegg, T. S. Theuerholz, and A. Knorr, Numerically exact solution of the many emitter ̆cavity laser problem: Application to the fully quantized spaser emission, Phys. Rev. B 91, 035306 (2015). [103] F. Damanet, D. Braun, and J. Martin, Cooperative spontaneous emission from indistinguishable atoms in arbitrary motional quantum states, Phys. Rev. A 94, 033838 (2016). [104] Z.-X. Gong, M. Xu, M. Foss-Feig, J. K. Thompson, A. M. Rey, M. Holland, and A. V. Gorshkov, Steady-state superradiance with Rydberg polaritons, arXiv:1611.00797 (2016), 1611.00797. [105] M. A. Zeb, P. G. Kirton, and J. Keeling, Exact states and spectra of vibrationally dressed polaritons, ACS Photonics 5, 249 (2018). [106] M. Gegg, A. Carmele, A. Knorr, and M. Richter, Superradiant to subradiant phase transition in the open system Dicke model: Dark state cascades, New J. Phys. 20, 013006 (2018). [107] N. Shammah, N. Lambert, F. Nori, and S. De Liberato, Superradiance with local phase-breaking effects, Phys. Rev. A 96, 023863 (2017). [108] P. Kirton and J. Keeling, Superradiant and lasing states in driven-dissipative Dicke models, New J. Phys. 20, 015009 (2018). [109] N. Shammah, S. Ahmed, N. Lambert, S. De Liberato, and F. Nori, Open quantum systems with local and collective incoherent processes: Efficient numerical simulation using permutational invariance, arXiv:1805.05129


 20
(2018), 1805.05129.
[110] P. Kirton, peterkirton/permutations: Permutations v1.0 (2017), https://doi.org/10.5281/zenodo.376621. [111] M. Gegg and M. Richter, PsiQuaSP–A library for efficient computation of symmetric open quantum systems, Sci. Rep. 7, 16304 (2017). [112] N. Shammah and S. Ahmed, PIQS: Permutational Invariant Quantum Solver (2018), https://doi.org/10.5281/zenodo.1212802. [113] J. Larson and E. K. Irish, Some remarks on  ́superradiantp ́hase transitions in light-matter systems, J. Phys. A 50, 174002 (2017). [114] M. Soriente, T. Donner, R. Chitra, and O. Zilberberg, Dissipation-Induced Anomalous Multicritical Phenomena, Phys. Rev. Lett. 120, 183603 (2018). [115] R. Gutie ́rrez-Ja ́uregui and H. J. Carmichael, Dissipative quantum phase transitions of light in a generalized Jaynes-Cummings-Rabi model, Phys. Rev. A 98, 023804 (2018).
[116] S. H. Strogatz, Nonlinear dynamics and chaos: with applications to physics, biology, chemistry, and engineering (CRC Press, 2018).
[117] F. Piazza and H. Ritsch, Self-ordered limit cycles, chaos, and phase slippage with a superfluid inside an optical resonator, Phys. Rev. Lett. 115, 163601 (2015). [118] Y. Shchadolova, M. Roses, M. Lukin, E. Dalla Torre, and E. Demler, Fermionic formalism for drivendissipative multi-level systems, arXiv:1804.03543 (2018), 1804.03543. [119] M. I. Kolobov, L. Davidovich, E. Giacobino, and C. Fabre, Role of pumping statistics and dynamics of atomic polarization in quantum fluctuations of laser sources, Phys. Rev. A 47, 1431 (1993). [120] F. Haake, M. I. Kolobov, C. Fabre, E. Giacobino, and S. Reynaud, Superradiant laser, Phys. Rev. Lett. 71, 995 (1993). [121] D. Meiser, J. Ye, D. R. Carlson, and M. J. Holland, Prospects for a Millihertz-Linewidth Laser, Phys. Rev. Lett. 102, 163601 (2009). [122] D. Meiser and M. J. Holland, Intensity fluctuations in steady-state superradiance, Phys. Rev. A 81, 063827 (2010). [123] J. G. Bohnet, Z. Chen, J. M. Weiner, D. Meiser, M. J. Holland, and J. K. Thompson, A steady-state superradiant laser with less than one intracavity photon, Nature 484, 78 (2012). [124] J. G. Bohnet, Z. Chen, J. M. Weiner, K. C. Cox, and J. K. Thompson, Relaxation Oscillations, Stability, and Cavity Feedback in a Superradiant Raman Laser, Phys. Rev. Lett. 109, 253602 (2012). [125] C. M. Bowden and C. C. Sung, First- and second-order phase transitions in the Dicke model: Relation to optical bistability, Phys. Rev. A 19, 2392 (1979).
[126] H. J. Carmichael, Breakdown of Photon Blockade: A Dissipative Quantum Phase Transition in Zero Dimensions, Phys. Rev. X 5, 031028 (2015). [127] V. V. Temnov and U. Woggon, Superradiance and Subradiance in an Inhomogeneously Broadened Ensemble of Two-Level Systems Coupled to a Low-Q Cavity, Phys. Rev. Lett. 95, 243602 (2005). [128] F. M. Marchetti, J. Keeling, M. H. Szyman ́ska, and P. B. Littlewood, Thermodynamics and Excitations of Condensed Polaritons in Disordered Microcavities, Phys. Rev. Lett. 96, 066405 (2006).
[129] F. M. Marchetti, J. Keeling, M. H. Szyman ́ska, and P. B. Littlewood, Absorption, photoluminescence, and resonant Rayleigh scattering probes of condensed microcavity polaritons, Phys. Rev. B 76, 115326 (2007). [130] I. Diniz, S. Portolan, R. Ferreira, J. G ́erard, P. Bertet, and A. Auffeves, Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for long-lived solid-state quantum memories, Phys. Rev. A 84, 063810 (2011). [131] O. Tsyplyatyev and D. Loss, Dynamics of the inhomogeneous Dicke model for a single-boson mode coupled to a bath of nonidentical spin-1/2 systems, Phys. Rev. A 80, 023803 (2009). [132] D. O. Krimer, S. Putz, J. Majer, and S. Rotter, NonMarkovian dynamics of a single-mode cavity strongly coupled to an inhomogeneously broadened spin ensemble, Phys. Rev. A 90, 043852 (2014). [133] D. O. Krimer, M. Zens, S. Putz, and S. Rotter, Sustained photon pulse revivals from inhomogeneously broadened spin ensembles, Laser Photonics Rev. 10, 1023 (2016). [134] H. S. Dhar, M. Zens, D. O. Krimer, and S. Rotter, Variational Renormalization Group for Dissipative Spin-Cavity Systems: Periodic Pulses of Nonclassical Photons from Mesoscopic Spin Ensembles, (2018), 1806.02394. [135] J. Dukelsky, G. G. Dussel, C. Esebbag, and S. Pittel, Exactly Solvable Models for Atom-Molecule Hamiltonians, Phys. Rev. Lett. 93, 050403 (2004).
[136] A. Kundu, Quantum integrability and Bethe ansatz solution for interacting matter-radiation systems, J. Phys. A 37, L281 (2004). [137] H. Tschirhart and A. Faribault, Algebraic Bethe ans ̈atze and eigenvalue-based determinants for Dicke-JaynesCummings-Gaudin quantum integrable models, J. Phys. A 47, 405204 (2014).
[138] E. A. Yuzbashyan, Integrable time-dependent Hamiltonians, solvable Landau-Zener models and Gaudin magnets, Ann. Phys. (N.Y.) 392, 323 (2018). [139] V. M. Bastidas, C. Emary, B. Regler, and T. Brandes, Nonequilibrium Quantum Phase Transitions in the Dicke Model, Phys. Rev. Lett. 108, 043003 (2012). [140] J. G. Cosme, C. Georges, A. Hemmerich, and L. Mathey, Dynamical control of order in a cavity-BEC system, (2018), 1806.10573. [141] M.-J. Hwang, R. Puebla, and M. B. Plenio, Quantum phase transition and universal dynamics in the Rabi model, Phys. Rev. Lett. 115, 180404 (2015). [142] M.-J. Hwang, P. Rabl, and M. B. Plenio, Dissipative phase transition in the open quantum Rabi model, Phys. Rev. A 97, 013825 (2018). [143] R. Landig, F. Brennecke, R. Mottl, T. Donner, and T. Esslinger, Measuring the dynamic structure factor of a quantum gas undergoing a structural phase transition, Nat. Commun. 6, 7046 (2015). [144] F. Brennecke, R. Mottl, K. Baumann, R. Landig, T. Donner, and T. Esslinger, Real-time observation of fluctuations at the driven-dissipative Dicke phase transition, Proc. Nat. Acad. Sci. 110, 11763 (2013). [145] J. Fan, Z. Yang, Y. Zhang, J. Ma, G. Chen, and S. Jia, Hidden continuous symmetry and Nambu-Goldstone mode in a two-mode Dicke model, Phys. Rev. A 89, 023812 (2014).
[146] A. Baksic and C. Ciuti, Controlling Discrete and Con


 21
tinuous Symmetries in “Superradiant” Phase Transitions with Circuit QED Systems, Phys. Rev. Lett. 112, 173601 (2014). [147] J. L ́eonard, A. Morales, P. Zupancic, T. Esslinger, and T. Donner, Supersolid formation in a quantum gas breaking a continuous translational symmetry, Nature 543, 87 (2017). [148] J. Le ́onard, A. Morales, P. Zupancic, T. Donner, and T. Esslinger, Monitoring and manipulating Higgs and Goldstone modes in a supersolid quantum gas, Science 358, 1415 (2017). [149] S. Gopalakrishnan, Y. E. Shchadilova, and E. Demler, Intertwined and vestigial order with ultracold atoms in multiple cavity modes, Phys. Rev. A 96, 063828 (2017). [150] J. Lang, F. Piazza, and W. Zwerger, Collective excitations and supersolid behavior of bosonic atoms inside two crossed optical cavities, New J. Phys. 19, 123027 (2017). [151] A. J. Kolla ́r, A. T. Papageorge, K. Baumann, M. A. Armen, and B. L. Lev, An adjustable-length cavity and Bose–Einstein condensate apparatus for multimode cavity QED, New J. Phys. 17, 043012 (2015). [152] A. J. Kolla ́r, A. T. Papageorge, V. D. Vaidya, Y. Guo, J. Keeling, and B. L. Lev, Supermode-DensityWave-Polariton Condensation, Nat. Commun. 8, 14386 (2017). [153] S. Gopalakrishnan, B. L. Lev, and P. M. Goldbart, Emergent crystallinity and frustration with BoseEinstein condensates in multimode cavities, Nat. Phys. 5, 845 (2009). [154] S. Gopalakrishnan, B. L. Lev, and P. M. Goldbart, Atom-light crystallization of Bose-Einstein condensates in multimode cavities: Nonequilibrium classical and quantum phase transitions, emergent lattices, supersolidity, and frustration, Phys. Rev. A 82, 043612 (2010). [155] S. Gopalakrishnan, B. L. Lev, and P. M. Goldbart, Frustration and glassiness in spin models with cavitymediated interactions, Phys. Rev. Lett. 107, 277201 (2011). [156] P. Strack and S. Sachdev, Dicke Quantum Spin Glass of Atoms and Photons, Phys. Rev. Lett. 107, 277202 (2011). [157] M. Buchhold, P. Strack, S. Sachdev, and S. Diehl, Dicke-model quantum spin and photon glass in optical cavities: Nonequilibrium theory and experimental signa
tures, Phys. Rev. A 87, 063622 (2013). [158] P. Rotondo, E. Tesio, and S. Caracciolo, Replica symmetry breaking in cold atoms and spin glasses, Phys. Rev. B 91, 014415 (2015). [159] S. Gopalakrishnan, B. L. Lev, and P. M. Goldbart, Exploring models of associative memory via cavity quantum electrodynamics, Philos. Mag. 92, 353 (2012). [160] V. Torggler, S. Kra ̈mer, and H. Ritsch, Quantum annealing with ultracold atoms in a multimode optical resonator, Phys. Rev. A 95, 032310 (2017). [161] V. Torggler, P. Aumann, H. Ritsch, and W. Lechner, A Quantum N-Queens Solver, arXiv:1803.00735 (2018), 1803.00735. [162] C. Emary and T. Brandes, Quantum Chaos Triggered by Precursors of a Quantum Phase Transition: The Dicke Model, Phys. Rev. Lett. 90, 044101 (2003). [163] C. Emary and T. Brandes, Chaos and the quantum phase transition in the Dicke model, Phys. Rev. E 67, 066203 (2003). [164] N. Lambert, Y.-n. Chen, R. Johansson, and F. Nori, Quantum chaos and critical behavior on a chip, Phys. Rev. B 80, 165308 (2009). [165] A. Altland and F. Haake, Quantum chaos and effective thermalization, Phys. Rev. Lett. 108, 073601 (2012). [166] A. Altland and F. Haake, Equilibration and macroscopic quantum fluctuations in the Dicke model, New J. Phys. 14, 073011 (2012). [167] L. Bakemeier, A. Alvermann, and H. Fehske, Dynamics of the Dicke model close to the classical limit, Phys. Rev. A 88, 043835 (2013).
[168] E. G. Dalla Torre, Scale invariant distribution functions in few-body quantum systems, arXiv:1709.01942 (2017), 1709.01942 [quant-ph]. [169] A. Dey, S. Mahapatra, P. Roy, and T. Sarkar, Information geometry and quantum phase transitions in the Dicke model, Phys. Rev. E 86, 031137 (2012). [170] P. Rotondo, J. Minar, J. Garrahan, I. Lesanovsky, and M. Marcuzzi, Singularities in large deviations of work in quantum quenches, arXiv:1802.09293 (2018), 1802.09293. [171] J. Mur-Petit, A. Relan ̃o, R. Molina, and D. Jaksch, Revealing missing charges with generalised quantum fluctuation relations, Nat. Commun. 9, 2006 (2018).
