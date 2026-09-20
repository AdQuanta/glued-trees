# Optical Properties of Dispersive Time-Dependent Materials - Full Text

> Source: https://pubs.acs.org/doi/10.1021/acsphotonics.3c00773
> Collected: 2026-09-20
> Published: 2024-03-20
> Zotero parent key: A2ZJLM5I
> Evidence: Zotero indexed PDF text

Optical Properties of Dispersive Time-Dependent Materials
Jamison Sloan,* Nicholas Rivera, John D. Joannopoulos, and Marin Soljacic
Cite This: ACS Photonics 2024, 11, 950−962 Read Online
ACCESS Metrics & More Article Recommendations s*ı Supporting Information
ABSTRACT: Time-varying optical materials have attracted recent interest for their potential to enable frequency conversion, nonreciprocal physics, photonic time-crystals, and more. However, the description of time-varying materials has been largely limited to regimes where material resonances (i.e., dispersion) can be neglected. In this work, we describe how the optics of these dispersive time-varying materials emerge from microscopic quantum mechanical models of time-driven systems. Our results are based on a framework for describing the optics of dispersive time-varying materials through quantum mechanical linear response theory. Importantly, we clarify how response functions for time-varying materials are connected to energy transfer. We provide three examples of our framework applied to systems which can be used to model a wide variety of experiments: few level models that can describe atoms, spins, or superconducting qubits, oscillator models that can describe the strong response of polar insulators, and strongly driven atom models which can describe the highly nonperturbative optical response of materials undergoing high harmonic generation. We anticipate that our results will be broadly applicable to electromagnetic phenomena in strongly timevarying systems.
KEYWORDS: time-varying, strongly driven, optical properties, linear response
■
INTRODUCTION
The propagation of electromagnetic waves through materials represents an essential component of light-matter interactions, and lies at the heart of countless physical phenomena and technological applications. In many bulk materials, the dominant features of electromagnetic wave propagation can be described by a simple complex-valued refractive index that encodes the speed of wave propagation as well as the rate of dissipation. In fact, the ability to describe a complex manybody system (such as a solid) with a frequency-dependent refractive index is critical for a practical description of many systems. Over the last century, a great deal of effort has gone into understanding the origins and fundamental properties of optical response, leading to important devices such as detectors, LEDs, solar cells, and lasers. Nowadays, artificial structures such as photonic crystals, layered 2D materials, and metamaterials are routinely created to provide further control over the optical response, leading to increased command over the interactions between light and matter. Many of the basic assumptions about the nature of optical response and wave propagation rely on considering optical materials as time-translation-invariant�the same at all times. However, a recent surge of interest has developed in the possibilities that may be enabled by materials which break this
assumption�in other words, materials which vary in time.1 In practice, time-varying materials are typically created by applying strong temporal modulations to stationary materials
in the form of external fields. These time-varying materials may
exhibit rich physics such as frequency conversion,2 scattering
from temporal interfaces,3,4 nonreciprocity,5,6 and amplifica
tion.7 Moreover, a recent interest has sparked in the study of so-called “photonic time crystals,” which have a strong temporally periodic index variation, enabling new directions
in topological physics8 and light-matter interactions.9,10 In the context of metamaterials, time has recently been identified as an additional degree of freedom which can be added to create
“spatiotemporal metamaterials”.11,12 Additionally, the possibility of strongly time-modulated materials introduces new fundamental questions about the nature of quantum lightmatter interactions in time-modulated systems, including
control over the generation of entangled photon pairs.13−15 To achieve these goals, it will become increasingly important to accurately describe the optical response of time-varying materials in the most general setting. Past work on timevarying media has typically assumed that the time modulations of a material occur at frequencies away from intrinsic
resonances in the material.8,16−21 In these cases, it is sufficient
Received: June 7, 2023
Revised: February 2, 2024 Accepted: February 2, 2024 Published: March 9, 2024
Article
pubs.acs.org/journal/apchd5
© 2024 American Chemical Society 950
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
Downloaded via TECHNION-ISRAEL INST OF TECHNOLOGY on October 11, 2024 at 12:31:58 (UTC).
See https://pubs.acs.org/sharingguidelines for options on how to legitimately share published articles.


 to consider a permittivity ε(t) that is nondispersive and associated with an instantaneous polarization response. However, there are many systems, especially those that vary quickly in time, which are not adequately accounted for by this framework. As one example, the description of wave propagation on a strongly driven conductor requires the simultaneous description of driving and plasmonic dispersion.
As another example, recent experiments22 in epsilon near zero (ENZ) materials have reached sufficiently fast index changes
that adiabatic ε(t) models may approach their limits.23 In fact, understanding the influence of dispersion has recently been identified as a key challenge in the field of time-varying
materials.24 Some semiclassical models have been proposed for
particular systems.24,25 Yet, there is still no comprehensive framework for describing the optical physics of dispersive timedependent materials from first principles. It is tempting to take a theoretical model (or data) for the optical response of an undriven system and then introduce time dependence. While this is a valid approach for slow variations, it is not reliable in general. The key issue is that in a strongly time-modulated system the optical response depends on the new microscopic dynamics of the driven system, which will in general not be adequately captured by this approach. Therefore, the optical response of time-driven materials should ideally be considered on the basis of first principles, starting from a microscopic description of the driven system. In this work, we present a general framework that describes the optics of dispersive time-dependent materials based on microscopic quantum mechanical dynamics. By doing so, we answer a fundamental question about the nature of energy transfer in time-varying systems, namely, the significance (or, in some cases, lack thereof) of the imaginary part of response functions. We also specialize many of our results to the particularly intriguing case of time-periodic (i.e., “Floquet”) systems. In this case, many of our results are simplified by the use of the Floquet theory to describe both the quantum and macroscopic electromagnetic aspects of problems. We provide examples of our framework across a variety of systems: timemodulated superconducting qubits in the GHz, timemodulated polar insulators with optical phonon resonances, and strongly driven gases which exhibit high harmonic generation (HHG). Our framework, when applied to these systems, enables us to discover a wide range of physics, such as
pulse propagation in dispersive photonic time-crystals, nonperturbative frequency conversion, and energy loss/gain. These findings point toward a future in which time-varying linear response theory is an important theoretical and experimental tool for studying time-varying optical materials. In an experimental setting, a great benefit of using linear response theory in these complex systems is that linear response functions can be measured rather than computed. Another advantage of this framework is that it allows one to characterize nonperturbative nonlinearities, which can be important in systems that are very strongly driven. The organization of this work is as follows: first, we give an overview of our framework, which incorporates quantum mechanical linear response theory and classical optics to describe wave propagation in dispersive time-varying materials. This section includes an important discussion about Kramers− Kronig relations and how response functions encode energy transfer in time-varying optical systems. We also summarize some of the important simplifications when these results are specialized to time-periodic (Floquet) systems, leading to a compact description of wave propagation in dispersive photonic time crystals. After describing the key foundations, we provide three distinct examples of our framework applied to different types of microscopic models for driven systems. Next, we describe wave propagation and energy transfer in a material whose optical response is characterized by time-modulated two-level systems. Intriguingly, we find that in the presence of sufficiently strong modulation, this type of system can exhibit resonant gain in its ground state. Such a model is relevant for describing metamaterials that could be formed from networks of superconducting qubits. Next, we describe the optical response and resultant scattering processes in a system described by a time-varying Lorentz oscillator model, which we refer to as a “Lorentz parametric oscillator.” Such a model is relevant for describing time-modulated polar insulators with an infrared optical response, which is dominated by optical phonon resonances. Finally, we describe the highly nonperturbative frequency conversion that may occur in gases undergoing HHG. This result paves the way toward using strongly time-driven materials to create artificial optical responses at ultraviolet and X-ray frequencies.
Figure 1. General framework for describing the optics of dispersive and strongly time-dependent systems. (a) Examples of time-dependent quantum mechanical systems whose optical response requires time-varying linear response theory. (b) Models of these microscopic dynamics can then be used to construct macroscopic response functions which may also vary spatially to account for material structures. For example, a dispersive dielectric structure ε(r, ω) in the absence of time-modulation can be described in terms of a two-frequency response function ε(r, ω, ω′) in the presence of time-modulation. (c) These response functions can be incorporated into the Maxwell equations to describe optical features of these systems, such as “free” wave propagation, scattering, and energy transfer.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
951


 ■ THEORETICAL FRAMEWORK
In this section, we describe our general framework for constructing new time-dependent optical materials from microscopic quantum mechanical models (Figure 1). In such models, the dynamics are described by the solution to the Schrödinger equation with a time-dependent Hamiltonian H(t). Generally, these microscopic dynamics can depend on many-body effects in a complicated manner. In this work, we will focus on materials which are well-described by constructing an effective bulk response from a collection of single particle dynamics; however, many of our conclusions hold more broadly. Once the relevant Schrödinger equation has been solved, the dipole response functions of single particles can be constructed and then transformed into bulk macroscopic response functions such as ε(ω, ω′). In systems where dissipation mechanisms are important, this process can also be followed by solving an appropriate master equation which rigorously incorporates the dissipative dynamics. With a macroscopic response function in hand, one can then use classical electrodynamics to describe wave propagation and energy transfer in dispersive, time-varying media. For example, strongly modulated systems which are periodic in time (“photonic time crystals”) can be associated with a band structure which indicates the relationship between wavevector and quasi-frequency in the driven material (see dispersion diagram in Figure 1c). In systems with strong light-matter hybridization, this provides a direct way to solve for the polarities of the driven system. Another example is the use of time-dependent response functions to compute frequencydependent scattering from a structure, such as a thin film of a time-dependent material. Experiments of this type have been
performed on ENZ materials,26,27 which have demonstrated
so-called temporal refraction.2 The linear response formulation that we detail in this work allows for the prediction of these behaviors in systems in which dispersion is critical.
Time-Varying Linear Response Theory. The foundation of our approach is time-varying linear response theory, which describes how some observable of a time-varying quantum mechanical system evolves due to the presence of a weak probe
field.28 For the context of this discussion, we will focus on the polarizability, which dictates how an electric field probe E(t) induces a change to the dipole moment ⟨δd(t)⟩, where ⟨⟩ denotes a quantum mechanical expectation value. While we will focus on the polarizability of a single point-like particle, these concepts apply equally well to other response functions such as susceptibility, permittivity, conductivity, magnetic permeability, etc. A dispersive time-driven material must, in general, be described with response functions which refer to two times (or
two frequencies).29 This is due to the fact that the system is not time-translation invariant, and thus, memory effects depend on the absolute time at which a probe interacts with the system of interest. For the polarizability example, the change to the dipole moment can be written in terms of the two-time polarizability α(t, t′) tensor and the probe electric field E(t) as
d(t) = dt (t , t )E(t ) (1a)
d( ) d E
= 2 ( , ) ( ) (1b)
where frequency domain polarizability is defined as
( , ) dt dt e e (t , t )
it i t
= (2)
The phase convention on the Fourier transform is chosen so that in the time-independent limit, α(ω, ω′) = 2πα(ω)δ(ω − ω′); hence, the usual relation ⟨δd(ω)⟩ = α(ω)E(ω) is recovered. The response function of any time-dependent system must be characterized by its temporal microscopic dynamics. In the case of a time-dependent point-like particle, the polarizability is given by the Kubo formula
(t , t ) = i (t t ) [d(t), d(t )] (3)
where d(t) is the interaction picture dipole operator, and the expectation value is taken in the initial state of the system. In solid state systems where many-body effects are important, the time-varying dielectric function or conductivity can be
appropriately formulated in a similar way.30,31
Causality and Kramers−Kronig Relations. In timeindependent systems, the requirement of passivity is tightly linked to the possible forms of a generic response function
χ(ω) via the Kramers−Kronig (K.K.) relations.32,33 When time-dependence is introduced, this passivity requirement dissolves as the drive provides energy to the system that can lead to gain, among other effects. Despite this added complexity, time-varying response functions are still constrained by causality. Specifically, any time-dependent linear response function χ(t, t′) must obey the relationship χ(t, t′) = θ(t − t′)χ(t, t′) so that changes to an observable at time t are only caused by interactions at times t′ < t. The extension of this requirement into the frequency domain through a double Fourier transform (see Supporting Information) generates the K.K. relationship
i
(, ) d ( , )
= (4)
where denotes the principal value. By taking the real and imaginary parts of eq 4, one can obtain a direct relationship between the real and imaginary parts of χ(ω, ω′). In the limit that the material is time translation-invariant, the response function takes the limiting form χ(ω, ω′) → χ(ω)·2πδ(ω − ω′), and the standard K.K. relation is recovered. Energy Transfer. In a time-independent material, the energy absorbed by the material from a passing wave at frequency ω is proportional to Im χ(ω). These time-dependent K.K. relations raise an immediate question about energy transfer in timedependent materials: does Im χ(ω, ω′) still encode energy dissipation (or gain) for a time-dependent material? We will show here that this is generally not the case. To do so, we consider the work performed by a probe field on a time-dependent polarizable particle. The total energy transferred to a point dipole can be written as
U d P( )
0
= . In this expression,
P( ) = Im[d( )·E*( )] is the energy per unit frequency
dissipated, d(ω) is the dipole moment, and E(ω) is the probe field. Assuming the point dipole is described by the polarizability α(ω, ω′), the energy dissipated per frequency is
P( ) Im d E E
= 2 *( ) ( , ) ( )
(5)
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
952


 Unlike the equivalent expression for time-independent media, eq 5 does not possess a clear sign; this is consistent with the general feature of time-dependent media that a
passing wave can lose or gain energy7,34 (and in fact, we will show cases where P > 0, in violation of passivity). Moreover, the amount of energy lost or gained can, in general, depend on the phase of passing waves. To see this explicitly, consider that for a monochromatic probe E(t) = E0 cos(ωpt − φ) of a single polarization incident upon an isotropic particle, the total energy dissipated is expressed as
U
E
2 Im ( , ) e ( , )
0
2 p
pp
2i pp
= [ + ] (6)
The form of eq 6 explicitly shows a contribution to the energy loss/gain, which depends on the phase φ of the probe. This is, for example, exactly the type of physics exemplified by an optical parametric oscillator, where the signal can either be exponentially amplified or attenuated depending on the phase of the input. Later, we give examples of systems where U can take on either sign, depending on whether the energy of the probe is absorbed or amplified. For a monochromatic probe, there are two contributions to the change in energy corresponding to the frequency components of the probe at ±ωp. The first contribution comes from Im α(ωp, ωp), which is independent of the probe phase. For this term, the positive frequency components of the probe field induce a dipole moment at that same positive frequency. It is this term that reduces to the usual relation that energy transfer is proportional to Im α(ω) in a timeindependent system. The second contribution comes from
Im[e−2iφ α(ωp, −ωp)], which depends explicitly on the temporal relationship between the probe field and dynamics of the driven system through the phase φ. For this term, the negative frequency component of probe −ω is shifted up by 2ωp to ωp. From this, we can see that dissipated energy can depend on both the real and imaginary parts of the response function, χ(ω, ω′).
From Microscopic to Macroscopic. The time-varying response functions discussed here are useful for describing not only energy transfer into a medium but also wave propagation. To see this, we consider the construction of potentially spatially and temporally varying response functions, which are used to describe some time-driven photonic structure. For many systems, the point-like particles described by a time-dependent polarizability α(ω, ω′) can be used to describe the optical response of bulk materials, as is routinely considered for time-independent media. In the simplest possible case, one assumes that the polarizable particles are packed with a volume density n, allowing one to define a unitless susceptibility χ(ω, ω′) by χ(ω, ω′) = (n/ε0)α(ω, ω′). Such a scheme neglects local field effects, which can be accounted for using a Clausius−Mossotti relation or a similar
method which is appropriate to the geometry.35 Spatial arguments can also be incorporated in the case that the material structure varies spatially or if the time-varying material possesses some joint spatiotemporal evolution. Such modulations have been recently considered in the context of
constructing “spatiotemporal metamaterials”11 and “spatiotem
poral photonic crystals”.36 We can thus write a form of Maxwell’s equations in frequency space which uses a two-frequency linear response function in its constitutive relation. To do so, it is helpful to
define a permittivity ε(r, ω, ω′) = 2πδ(ω − ω′) + χ(r, ω, ω′), which relates the displacement and electric fields as D(r, ) (r, , )E(r, )
0
d 2
= . Under this definition,
the electric field E(r, ω) in the presence of a current source J(r, ω) obeys
c
Er r Er
Jr
(, ) d
2 (, , ) (, )
i (, )
2
2
0
××
= (7)
Due to the time dependence, this form of the Maxwell equation is nonlocal in frequency space. In general, finite difference time-domain (FDTD) methods may be required in order to simulate the full spatial and temporal dependencies of time-driven systems. However, we show in the next section that for time-periodic systems, the linear response functions take a form that enables significant simplifications.
Specialization to Time-Periodic Systems. One general class of time-modulated systems which is of particular interest
is that in which the modulation is periodic in time.20,37 In certain cases, such systems have been termed “photonic time crystals” (PTCs). Most PTCs considered so far have been described in terms of a “nondispersive” permittivity ε(t) = ε(t + T), where T is the period. Furthermore, for materials to be considered PTCs, it is usually assumed that the relative temporal variations to the material are substantial (Δε ≳ 0.1), so that the nature of wave propagation departs substantially from that in an unmodulated counterpart. Due to their periodic nature, a spatially homogeneous PTC can be associated with a band structure that relates wavenumbers k to quasifrequencies Ω, which lie in a temporal Brillouin zone (TBZ) set by Ω0 ≡ 2π/T. This phenomenon is well studied and manifests many natural analogies to spatial photonic crystals. As an important extension of these ideas, we introduce the concept of dispersive PTCs that result from temporal modulations which are fundamentally dispersive. In this section, we specialize key results from the above to timeperiodic systems. The key result is that in a time-periodic system, a response function χ(ω, ω′) can be reduced to an integer series of response functions χk(ω). Form of Response Functions. In time-periodic systems, the harmonic nature of the problem places constraints on the form of the response functions. Specifically, periodicity imposes the time-domain constraint χ(t, t′) = χ(t + T, t′ + T). This immediately dictates that the frequency response is described by an integer series of response functions χk(ω), which are defined such that
( , ) ( )2 ( k )
k
k0
=· +
= (8)
From this form, we see that χk(ω) encodes how an applied field at frequency ω induces a response at frequency ω + kΩ0. K.K. Relations, Energy Transfer. The K.K. relationships take a more familiar form in time-periodic media. By assuming that χ(ω, ω′) obeys eq 8, we use eq 4 to deduce that the response function for each integer harmonic obeys the usual timeindependent K.K. relation
i
() d
()
k
k
= (9)
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
953


 For time-periodic media, the integer order response functions allow for a particularly informative description of loss and gain. In particular, Im α0(ω) encodes loss and gain, which are independent of the probe phase, while αk(ω) of nonzero order encodes loss and gain, which depend on the probe phase. If we send a monochromatic probe field at such a material, the energy dissipated U (from eq 6) reduces to
U
T
E
E
2 Im ( )
2 Im ( )e
kk k
0
2 p
0p
0
2 p
1p
2i 2p 0
=
+ []
= = (10)
This equation reveals several key pieces of information about the nature of energy transfer in time-periodic systems. We discuss these features by examining the two terms.
(1) In the first term, the imaginary part of the zeroth harmonic response function Im α0(ω) carries unambiguous information about energy transfer which does not depend on the phase of the probe field. Physically, α0(ω) encodes the polarization, which is created at the same frequency as the probe and is thus most closely connected to the dispersive response function of the undriven medium. Moreover, unlike in a ground-state time-independent system, Im α0(ω) is not restricted to be positive. This is analogous to an active medium which is pumped to an excited state, which can exhibit gain as characterized by a negative imaginary part of some response function. Instead here, the passivity can be broken by time-dependence rather than a population inversion.
(2) In the second term, the response function of orders k ≥ 1 can affect the dissipated energy through phasedependent effects under a special resonance condition. This resonance condition is indicated by a Kronecker delta function, which requires that 2ωp = kΩ0 for integer k. Physically, this condition results from negative frequency probe field components −ωp, which create polarization at frequencies which are shifted over by an integer number of harmonics: this positive frequency polarization can then interact with the positive frequency component ωp of the probe field to do work (positive or negative). It is worth noting that this is the same type of mechanism responsible for parametric amplification processes as described in nonlinear optics, which are
known to be sensitive to phase.38
For a given ωp and Ω, only one value of k, if any, can satisfy this condition. This potential additional term contains phase dependence within the Im operator. This leads us to conclude that the real and imaginary parts of αk(ω) for k ≠ 0 have no unique physical significance as far as energy transfer is
concerned. Thus, the sign of Im[αk(ω)e−2iφ] and the sign of the energy transfer depend on the phase relationship between the probe field and the underlying microscopic dynamics that govern αk(ω).
Eigenmodes in Periodic Systems. In a time-periodic system, we can seek solutions to the sourceless Maxwell equation in a bulk medium. Due to the time periodicity, and spatial translation invariance, the Maxwell−Floquet modes take the form E(r, t) e u e
nn
ik r n t ,
i( 0)
= · + , where k is the wavevector, Ω is a quasifrequency in the first temporal
Brillouin zone )
T, T
Ä
ÇÅÅÅÅÅÅ , and uΩ,n are a sequence of coefficients.
In a medium with permittivity
k
(, ) 2 ( ) ()
( )2 ( )
kk
bg
0
=
++
, the amplitude
of the wavevector |k| = kΩ and coefficients can be found for a given quasifrequency by solving the eigenvalue problem
c ( )u c ( )u k u
n
nn
n
m m n nm n
2
2 bg
2
2
2
+ = (11)
where Ωn ≡ Ω + nΩ0 is the quasifrequency shifted by n harmonics. This relation can be cast into a linear matrix problem, which yields the band structures of dispersive photonic time crystals, examples of which are shown later in the text. We note that in the presence of a very large loss or gain, an eigenmode expansion may not strictly form a complete basis for the set of possible solutions. However, in many cases, the eigenmode expansion may still provide accurate information about the dispersion relation. In systems where this approximation breaks down, Green’s function methods can be employed to describe the propagation of waves from sources.
■
RESULTS
Two-Level System. In this section, we discuss a two-level system (2LS) that has its energy splitting modulated strongly in time. When the modulation frequencies are close to the splitting frequency itself, the dispersive framework outlined above is required to describe the linear response correctly. We focus specifically on a system with a Hamiltonian H2LS(t) 2 (1 cos( 0t)) z
0
= + . Since the Hamiltonian is
periodic in time, we can use the insight of Floquet theory that the system should behave like a stationary system but with a ladder of quasi-energy levels. Physical systems which have
realized Hamiltonians of this type include driven spins,39
superconducting qubits,40 quantum dots,41 and strongly
modulated Rydberg atoms.42 A particularly appealing aspect of microwave schemes is that very strong modulations can be readily induced, leading to the nonperturbative regime of effects that do not fall under the purview of perturbative nonlinear optics. While we focus here on the σz-type modulation of a two-level system, many of the principles discussed here should carry over naturally to other types of two-level modulations, as well as systems with more discrete levels. While an undriven 2LS is restricted to making groundexcited transitions at the bare resonance frequency ω0, the time-dependent 2LS we describe here can make transitions separated by the harmonics of the drive. Thus, in a system which is well described in terms of a few energy levels, the driven system can exhibit an optical response at frequencies different than that of the undriven system. Using the Floquet states of the Hamiltonian, and the Kubo formula, we find the single-particle polarizability
d JJ JJ
() i i
kz
n
n kn
nn
n kn
nn
2
0
= + ++
+
Ä
Ç
ÅÅÅÅÅÅÅÅÅÅ
É
Ö
ÑÑÑÑÑÑÑÑÑÑ
(12)
Here, ωn ≡ ω0 + nΩ0 is the bare transition frequency shifted by n harmonics, Jn ≡ Jn(δω/Ω0) is the n-th order Bessel function
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
954


 evaluated at the driving strength parameter δω/Ω, Γn is the line width associated with each transition between Floquet levels, and z 0 is an expectation value taken in the equilibrium state. More discussion about this equilibrium as well as the damping rates is shown in the Supporting Information. As the fractional change in the frequency δω increases, the optical response of the system moves from a perturbative to a nonperturbative regime (Figure 2a−c). The plots show the response function of zeroth harmonic order α0(ω) for three modulation strengths δω/ω0 = {0, 0.4, 1.5} and with a modulation frequency Ω0 = ω0/2. This response function encodes the amplitude with which a probe at frequency ωp generates a change in the dipole moment at that same frequency. With no modulation, this describes the polarizability of a static 2LS, which is given by a Lorentzian formula (Figure 2a). For a stronger drive (δω/ω0 = 0.4), sidepeaks emerge, which indicate an optical response at ω0 ± Ω0. At this strength of modulation, only the first harmonic contributes substantially, although others are present at levels that are not yet apparent in Figure 2b. This behavior shifts as the modulation strength nears or exceeds static energy splitting ω0. Figure 2c shows an example of the nonperturbative regime in which multiple harmonic orders are relevant. In this extreme limit, the strongest optical response actually occurs at 2ω0,
indicating that absorptions several steps up the Floquet ladder occur more strongly than the transition at ω0. We also note that the overall magnitude of the response peaks is seen to decrease with increasing δω. In this sense, the optical response of the system is allocated across more frequencies but with less response at each frequency. In this particular case, the sum rule J1
mm
2=
= fixes the total response across all frequencies.42
Bulk Wave Propagation. Each of the three examples of the optical response regime described above comes with its own implications for wave propagation in a bulk optical system, which is characterized by these single-particle models. To demonstrate this, we consider a bulk optical medium which consists of time-dependent point particles packed with a number density n. The system is equivalently described by a plasma frequency ωp. It is then possible to compute the dispersion relation of plane waves which propagate in such a uniform time-dependent medium. Figures 2d−f shows the dispersion relations of bulk media with ωp = ω0/2 for the modulation parameters given in each corresponding column. Dispersion relations indicate the relationship between the wavevector k and the quasienergy Ω, which is taken to lie in the first temporal Brillouin zone (TBZ), −Ω0/2 < Ω ≤ Ω0/2. For the undriven medium (δω = 0), the dispersion relation is the same as that of a time-independent Lorentz oscillator but
Figure 2. Wave propagating in a time-driven two-level system from perturbative to nonperturbative regimes. (a−c) Real and imaginary parts of zeroth order polarizability α0(ω) as a function of frequency for three different drive strengths δω/ω0 = {0, 0.4, 1.5} and driving frequency Ω0 = ω0/
2. Loss parameter is taken to be Γ = 10−3ω0 for all peaks. (d−f) Dispersion relations for a time-periodic bulk medium which is composed of particles described by the polarizabilities αk(ω). Dispersion relations are plotted as a function of the quasifrequency Ω which lies in the temporal Brillouin zone −Ω0/2 < Ω ≤ Ω0/2. Sufficiently strong driving causes a gap to open in the momentum [panel (g)]. (h−j) Propagation of a Gaussian wavepacket constructed from the modes indicated by a red × in corresponding panels (d−f). The line traced out in (x, t) space indicates the group velocity of the packet. As the strength of the time modulation increases, new features such as temporal beating due to interference of harmonics and wavepacket spreading due to group velocity dispersion.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
955


 with frequencies folded into the first TBZ. Features such as the light-like and polariton-like parts of the dispersion can still be identified. In this regime, wavepackets propagate in the usual way (Figure 2g). Stronger driving (δω/ω0 = 0.4) brings about new changes to the band structure. For example, bands near the edges at Ω = Ω0/2 have moved up and down in pairs (marked by an arrow in Figure 2e), and some curvature has been introduced into bands. Additionally, there is an avoided crossing of the two lowest bands. While the wavepacket at the point marked on the band structure propagates coherently and with a similar group velocity to its unmodulated counterpart, a new beating behavior emerges in the amplitude due to the presence of multiple temporal harmonics in the modes which comprise the packet. As it propagates, the wavepacket exchanges energy back and forth with the medium through this behavior, which is only possible in the presence of broken time-translation symmetry. With driving strength in the extreme nonperturbative regime (δω/ω0 = 1.5), the band structure changes substantially. Most prominently, wavevector gaps are introduced, representing wavelengths which cannot propagate in the medium. Band gaps in “photonic time crystals” have been identified previously
in nondispersive settings.43,44 Additionally, the crossed bands shown in Figure 2d,e are seen to hybridize with one another, eliminating these sharp crossings. The panel below (Figure 2i) shows that a wavepacket centered around the marked mode propagates with amplitude oscillations as well as dispersion. This dispersion can be attributed to the band curvature which has developed for the example mode (red “x” in Figure 2g) as compared to the linear dispersion at the corresponding points of Figure 2d,e. Loss and Gain. We now discuss loss and gain in these types of systems, as described in the time-dependent linear response framework. In the absence of any driving, it is well known that a two-level system in its thermodynamic ground state can only absorb energy. The single-particle polarizability in this case is given by a Lorentzian form (Figure 2a). The quantity Im α0(ω) ≥ 0 gives the frequency-dependent loss, which peaks at ω0 due to absorptive transitions from the ground to the excited state. In a Floquet system, transitions from the ground to an excited state can also occur due to absorption of a photon at a frequency of ω0 + kΩ0 for some integer k. These resonances correspond exactly to the peaks shown in Figure 2b,c and also exhibit the property Im α0(ω) > 0. As discussed in the theory section, the quantity Im α0(ω) does possess significance for phase-independent energy transfer. From this, we see that the example parameters used in Figure 2 give purely absorptive systems. To complete our discussion of a modulated 2LS, we give an example of how such a time-dependent two-level system can exhibit both resonant gain and loss in its thermal equilibrium state. To do so, we consider a modulated two-level system with Ω = 0.4ω0. When strongly modulated (δω/ω0 = 2.2), a substantial contribution emerges from Floquet sidebands, which fall below the level of the original ground state. This means that the system can make ground-to-excited state transitions at frequencies ω0 + kΩ < 0 for sufficiently negative integers k. These transitions are schematically shown in Figure 3a. In the polarizability, these transitions appear as peaks with Im α0(ω) < 0 around the relevant resonances, corresponding to energy gain in the Floquet ground state. The gain peaks appear next to other peaks where Im α0(ω) > 0, which
correspond to absorptive transitions of the form shown in Figure 2. Thus, a two-level system modulated in this way can provide either absorption or gain to a probe field, depending on the frequency.
Time-Dependent Lorentz Oscillator. In this section, we use our framework to describe a medium that behaves as a harmonic oscillator with a time-varying frequency. One system that can be modeled this way under certain conditions is a polar insulator that is strongly driven by an external field. In polar insulators, such as silicon carbide (SiC) and hexagonal boron nitride (hBN), the optical response over some frequency
ranges is dominated by optical phonon resonances.45 In undriven polar insulators, these resonances lead to wellestablished peaks at transverse optical (TO) phonon frequency ωTO, which are described by a Lorentz oscillator model. However, in the presence of strong laser pulses, the TO phonon frequency of such a material may acquire a time
dependence.46,47 If the frequency of the modulating pulse is on the order of ωTO itself, then a dispersive time-dependent framework is needed to capture the optical behaviors around
ωTO. To do this, we use a model that we refer to as the “Lorentz parametric oscillator” (LPO). In this model, we assume that the response of the polar insulator can be characterized by that of a collection of point-like polarizable particles. Each of these particles is a harmonic oscillator with a time-varying resonance
frequency ω(t)2 = ω02(1 + f(t)), so that the Hamiltonian
governing the oscillator is H (t) m (t) x
p m
LPO 2
1 2
22
2
= + , where
x and p are the position and momentum operators, and m is the effective mass of the atom in the lattice. For |f(t)| ≪ 1, the first-order perturbative correction to the polarizability is given as
( , ) 2 ( )( ) ( , )
(0) (1)
= + (13)
where ( ) q
m
(0) 1
i
2
0
2 0
2
= is the ordinary Lorentz
oscillator contribution from f(t) = 0. In cases where the perturbative approximation breaks down, one can equivalently solve the equation of motion for a harmonic oscillator with time-varying frequency (sometimes referred to as the “Mathieu
equation”48) numerically and take Fourier transforms in order
Figure 3. Linear response representation of ground-state gain in a driven two-level system. (a) Floquet level diagram for a two-level system driven at frequency Ω/ω0 = 0.4 with strength δω/ω0 = 2.2. Arrows indicate absorptive and emissive transitions from the thermodynamic ground state to the excited state. (b) Energy transfer properties of the driven system can be visualized through Im α0(ω). Transitions with loss correspond to peaks where Im α0(ω) > 0, while transitions with gain correspond to peaks where Im α0(ω) < 0.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
956


 to obtain α(ω, ω′) more generally. However, in most cases, the perturbative regime should apply, and the first-order frequency space correction is given by
q
m
f
(, )
()
( i )( i )
(1)
2 0
2
0
22
0
22
=
(14)
where f(ω) is the Fourier transform of the modulation. The expression features two resonant Lorentz oscillator factors in the denominator at ω and ω′ and is consistent with expressions for resonant nonlinearities, such as Kerr non
linearities around an atomic resonance.38 To give an example of how this dispersive time-dependent response function can be used in optics, we consider the scattering of an incident wave from a slab of material described by χ(ω, ω′) for a periodic modulation f(t) = δω cos(Ω0t). The general concept of scattering from dispersive time-dependent
materials was recently explored.49 In this example, we will focus specifically on how dispersive resonance can greatly impact the reflection and transmission of waves from a material. To demonstrate this, we consider a thin film scattering problem which consists of a weak probe field at frequency ωp incident on a material ε(ω, ω′) of length L. If the material is time dependent with some periodicity Ω0, then in general, there will be reflected and transmitted waves of shifted frequencies ωp + kΩ0, where k is an integer. To elucidate the effect of dispersive resonances, we compare the scattering problem for two different time-dependent materials: (1) a nondispersive material which has a permittivity ε(t) = εbg(t) + δεf(t) and (2) a dispersive material described in the LPO model detailed above. For both materials, we use a periodic modulation profile, f(t) = cos(Ω0t), specifically focusing on the parametric resonance case given by Ω0 = 2ω0. Figure 4c,d shows the photonic time-crystal band structures
corresponding to materials (1) and (2) for δε = δω = 10−3. In the absence of dispersion, these two descriptions coincide. In the nondispersive case, the weak interaction means that the band structure simply corresponds to the undriven material dispersion ck/
k bg
= folded into the first temporal
Brillouin zone with quasifrequencies −Ω0/2 < Ω ≤ Ω0/2. Similarly, the dispersive band structure can be understood as that of an undriven Lorentz oscillator dispersion folded into the TBZ. In this particular case, we have chosen for parametric resonance (Ω0 = 2ω0), the steep branch of the dispersion due to the resonance at ω0 coincides with the band edge at Ω0/2. This parametric resonance leads to pronounced effects on the incoming waves. In Figures 4e,f, we show results for the transmission amplitude for an incident field at ω for shifted frequencies ω, ω − Ω0, and Ω0 for a thin film created from the nondispersive and dispersive materials described above. For the nondispersive modulation, the vast majority of the transmitted field lies at the incident frequency. In contrast, the dispersive material exhibits peaks of resonant conversion for incident frequency 3ω0. This occurs because at the parametric resonance condition (Ω = 2ω0), the downshifted harmonic lies at ω0, which is resonant with the oscillator denominators of eq 14. Since the interaction takes place in a thin film, radiation at incident or new frequencies may continue to reinteract with the material, leading to cascaded harmonics. This is, for example, the origin of a similar response
for the incident field of 5ω0. The differences between behavior between the dispersive and nondispersive models highlight the importance of using a model that is consistent with underlying microscopic dynamics. We now comment briefly on the relationship between the time-modulated two-level and Lorentz oscillator models. In the limit of time-independent systems, it is well known that both of these models exhibit the same form of dipole response, given
by α(0)(ω). The intuition behind this is that a weak field that probes the ground state of a harmonic oscillator can effectively only “see” the first transition of the oscillator ladder, so the two-level model is recovered. This close relationship dissolves when time modulations are introduced, as we have seen when comparing the two systems. A parametric drive involves more states of the harmonic oscillator ladder into the dynamics, so that the parametric oscillator model is fundamentally different than a modulated two-level system. The departure of these models here is not dissimilar to what unfolds in the nonlinear response of the static systems: the two-level system displays resonant nonlinearities, while the oscillator exhibits no
Figure 4. Optics of a time-modulated harmonic oscillator. (a) Quantum harmonic oscillator of frequency ω0 subject to a frequency modulation at frequency Ω0. The panel below shows the real and imaginary parts of χ1(ω) for parametric resonance when Ω0 = 2ω0, at
a modulation strength of δω = 10−3Ω0. (b) Incident probe field on a slab of material described by ε(ω, ω′). The slab of material has thickness L. Since the medium is time-varying, reflected and transmitted waves can be shifted by integer multiples of the drive frequency Ω0. (c) Band structure of a nondispersive medium with a time-dependent refractive index profile. This is the homogeneous medium dispersion relation ω = ck/n folded into the temporal Brillouin zone −Ω0/2 < Ω ≤ Ω0/2. (d) Band structure for the dispersive Lorentz parametric oscillator medium depicted in (a), with Ω0 = 2ω0. (e,f) Transmission spectrum for probe and shifted probe frequencies for the configuration depicted in (b) for both nondispersive and dispersive modulations.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
957


 nonlinearity at all. This serves as a clear example that models for the optical response of strongly driven materials should be considered carefully on the basis of microscopic dynamics.
High Harmonic Generation. In this section, we show how the time-dependent linear response framework provides a pathway to describe the IR to X-ray frequency optics of systems that exhibit HHG. The most basic configuration for such a system is a gas cell pumped with an extremely intense infrared laser pulse. For sufficiently strong pumps, the system exhibits highly nonperturbative effects of strong field physics, and many pump photons can be converted into single photons of frequencies which are more than one hundred times higher
than that of the pump.50,51 These systems serve as valuable sources of UV and X-ray photons, which are difficult to produce by any other means and also generate harmonic
combs which form attosecond pulses.52,53 More recently, HHG
has also been studied in solids.54 Although HHG systems have been studied for decades for light generation, there are untapped opportunities to use them as venues for new optical interactions. We propose that HHG systems represent an intriguing platform to study the optics of time-varying materials at high frequencies. From this point of
view, the strongly driven gas can itself be considered a timevarying optical medium. Due to the strong field strengths and atomic resonances involved in these systems, dispersion plays an important role. The general setup of a HHG system is shown in Figure 5a. In the absence of any probe field, the driven system acquires a
dipole moment |d(ω)|2, which oscillates at many harmonic multiples of the driving frequency, leading to HHG. If the emitted photons are considered quantum mechanically, HHG can be equivalently characterized as spontaneous emission from transitions between the Floquet quasi-energy levels of the
driven system.55 Using a 1D model of an atomic potential, we numerically solved the time-dependent Schrödinger equation for
H(t) V(x) E x sin( t)g(t)
p
2m 0 0
2
= + , where
V(x) 1/ x2 a2
= + is a “soft Coulomb” potential regulated by the parameter a, and g(t) is an envelope function which turns the drive on and off. Parameters were chosen so that the ionization energy of the potential matches that of neon. Using numerical evolution of this Hamiltonian, we directly computed the atomic polarizability α(t, t′) using the Kubo formula (eq
Figure 5. HHG as a time-dependent optical medium. (a) General setup of HHG consists of a gas sample which is irradiated with extremely strong IR laser pulses Edrive(t). In a 1D Coulomb potential model, the ground-state electron is ejected into the ionized continuum, generating a dipole
moment d(t) in the process. This induced dipole moment contains many harmonics of the drive frequency, as shown by the plot of |d(ω)|2. The harmonics continue up to a cutoff frequency, which is related to the ionization energy of the atom. (b) Two-time atomic susceptibility α(t, t′) of a single particle which undergoes the modulation shown in (a). (c) Two-frequency atomic susceptibility α(ω, ω′) which shows the frequency decomposition of α(t, t′). Harmonic stripes can be seen for ω′ = ω + kevenΩ0 due to the quasi-periodic nature of the modulation. (d−f) Induced dipole moments by probe fields at different frequencies and phases. (g−i) Induced dipole moment spectra corresponding to each of the probes in (d−f). Probe frequencies are marked with an arrow. Frequencies of the peaks are marked with dashed lines.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
958


 3). We note that in a Hermitian system, the polarizability α(t, t′) can be computed by evolving all eigenstates of the Hamiltonian in time and then taking expectation values of the appropriate operators to implement the time-domain Kubo formula directly. However, the numerical models used for HHG typically rely on absorbing boundary conditions, which break the Hermiticity and thus the completeness of eigenstates. Therefore, we compute the time-domain response function via the Liouvillian evolution in a manner consistent with the quantum regression theorem. We have verified that the response function α(t, t′) obtained through this method generates dipole responses to probe fields that match those obtained by directly incorporating the probe into the Hamiltonian. The results of this calculation are shown in Figure 5b. As dictated by the causality constraint, the dipole response is nonzero only for times of t > t′. Even though this system is driven for a relatively small number of periods, some features of the Floquet regime emerge. From the theoretical discussion around eq 8, we know that for a perfectly time periodic system the frequency polarizability α(ω, ω′) converges to a series of delta functions spaced at integer multiples of the drive. By numerically transforming the time-domain polarizability, we show that this holds approximately true. The squared magnitude of the frequency-domain polarizability |α(ω, ω′)|2 is shown in Figure 5c over a range of harmonics. The clear diagonal stripes adhere to lines for which ω′ = ω + kΩ0. For a general system, k can be any integer. However, the inversion symmetry of the potential and driving field we have chosen dictates that k may only take on even values, as is consistent
with the general framework for selection rules in HHG.56 In the limit of weak driving, where only a small number of harmonics can be produced, this constraint reduces to the wellknown fact that centrosymmetric materials have no χ(2) nonlinearity. We now explore the consequences of these response functions for weak probes that interact with the driven system. Figure 5d−f, shows the change in the time-dependent dipole moment Δd(t) induced by a probe field
E(t) E cos( t )e t t
pp
( ) /2
0
22
= for different probe fre
quencies and phases. Generically, the dipole moment peaks can appear at ±ωp + kΩ0, where k is an even integer. Different behaviors emerge depending on the frequency ωp and phase φ of the probe, which are visualized through the frequency spectrum |Δd(ω)|2 for different probe parameters. For an odd-harmonic probe (ωp = 11Ω0), the dipole responds at other odd frequencies (Figure 5g). A black arrow marks harmonic 11, which oscillates at an amplitude higher than that of the surrounding peaks. Nevertheless, notable contributions come from many peaks, extending up through around harmonic 50. Additionally, we note that the phase of the probe with respect to the pump can contribute substantially to the resulting output. In particular, we show examples of the phases φ = π/2, π. For some of the harmonics produced by the probe, the amplitude can vary by an order of magnitude or more, depending on the probe phase. This type of behavior has actually already been observed in the context of so-called “two-color HHG,” in which some harmonic of the drive (usually the third) is sent into the sample along with the
drive itself.57 In some sense, the pump−probe schemes discussed here are similar in nature.
So far, we have shown that an odd harmonic probe can essentially modify the normal HHG spectrum (which also consists only of odd harmonics in this example). However, we now show that weak probe fields sent at the time-driven system can also be used to generate dipole moments at frequencies that are not produced in the absence of the probe. For example, sending in a probe frequency at some even harmonic m induces a comb of dipole moments at frequencies kevenΩ0. This change to the dipole moment will radiate at even harmonics, which are not produced by the system in the absence of the probe. Such a configuration is shown in Figure 5e,h, where the probe is sent at harmonic 10. The result is an even comb of induced dipole moments, which will then radiate into even harmonics. Similarly to the odd probe, the probe harmonic stands out in strength above the others, and the probe phase can strongly influence the output. Finally, we show that probing at a nonharmonic frequency results in a pair of interleaved combs (Figure 5f,i). In particular, sending in a weak probe of harmonic ωp = 22.5ω0 produces dipole moment peaks at ±ωp + kevenΩ0, leading to induced dipole moments at nonharmonic frequencies but which are separated by even multiples of the drive. Moreover, this example indicates that the driven system will respond optically at tens of harmonics, which for a near-IR pump corresponds to optical response at wavelengths of 10 s of nanometers or below. Thus, these results show promise for the potential to use existing HHG systems as a platform to study the optical response of strongly driven systems, potentially leading to controllable optical materials, which can respond and convert frequencies in the UV and X-ray regime. While we have focused for clarity on a single-particle polarizability model, the two-frequency linear response framework naturally lends itself to the inclusion of spatial aspects of HHG problems, which can enable studies of phase-matching and
wave propagation.58,59 We additionally note that the time-dependent linear response is particularly appealing for the study of proberesponse in HHG because once a function such as α(t, t′) is computed through potentially time-consuming quantum mechanical simulations (i.e., results of Figure 5b), the response to any probe can be computed as a simple convolution integral. In fact, through energy dissipation/gain measurements, it may be possible in some cases to determine α(ω, ω′) experimentally, enabling inferences about how the system will respond to other probes. Such an approach may be particularly appealing in order to construct probe fields which will selectively enhance or suppress the generation of certain harmonics. This type of unifying framework is particularly appealing in the context of works which have explored the
effect of weak XUV probe fields on HHG.60−62 This framework could also be used to describe the high-frequency
parametric gain which has been observed in HHG systems,63 allowing for the creation of more efficient systems which amplify high frequency radiation.
■
CONCLUSIONS
In summary, we have presented a framework for describing electromagnetic response and wave propagation in dispersive time-varying quantum systems. We have established the fundamental properties of time-varying response functions, with a special focus on developing forms for use in timeperiodic (Floquet) systems. We have addressed fundamental questions about the nature of energy transfer (gain and loss) in
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
959


 these systems. In fact, the relationship between K.K. relations and energy transfer in time-varying materials that we have established can enable the use of absorption/gain measurements to construct the full complex response functions of timevarying systems. Additionally, we have shown selected examples of this framework to address a diverse set of problems that raise implications for superconducting microwave circuits, polar insulators in the IR, and UV/X-ray optics of HHG systems. We anticipate that this unifying approach will reveal further similarities among fields that would normally be considered disparate. One important future direction is the development of microscopic models to describe time-varying linear responses in more complex systems. For example, many recent works have focused on the electronic states that can be created in Floquet-driven matter (with a particular focus on topological
electronic properties).64 However, there is still much work to be done to use these descriptions of strongly driven solids to infer the optical properties of such materials. In some cases, free electron or few-band models may be sufficient to capture the key physics. In more complicated situations, timedependent density functional theory (TDDFT) may serve as an essential tool for computing time-varying response functions (e.g., ε(ω, ω′) for a strongly driven semiconductor). Once the optical response of a strongly driven material is appropriately characterized, it can be incorporated into either classical or quantum descriptions of electromagnetic phenomena. It will also be critical to develop methods for characterizing the general time-varying optical response through pump− probe experiments. Many experimental platforms of the current study consist of planar structures (polar insulators or ENZ materials), which are strongly driven. A typical protocol should consist of fixing the pump conditions and then measuring the amplitude and phase change of a probe which is varied in amplitude and phase. Such a measurement of complex reflection or transmission carries information that, in many cases, can be used to infer the material response functions based on a model of the geometry. This comparison between theory and experiment may be further aided by theoretical tools which are applicable in systems with
spherical49 or planar25,65 symmetry. In the classical domain, time-varying materials can lead to the propagation of new types of excitations in materials and new mechanisms for gain. It is well known that the propagation of waves in a medium with a simple periodic time-varying permittivity can, in theory, lead to PTCs with momentum bandgaps. In more complex settings where dispersion is important, strong temporal driving may lead to the generation of new “Floquet polaritons” in either bulk or structured media. Such Floquet polaritons on 2D materials could open up a new set of directions for the broad field of polaritonics. In the quantum domain, the appropriate use of response functions to describe time-varying materials may enable a general description of quantum light-matter interactions in time-varying materials. This can eventually lead to an accurate
quantum picture of “photonic quasiparticles”66 in time-varying materials which may interact with matter. The study of fundamental quantum light-matter interaction processes in time-driven materials is the first step toward answering questions about how they can be used to construct new devices such as amplifiers or lasers with new output properties or at frequencies that have been historically difficult to achieve.
■
ASSOCIATED CONTENT
s*ı Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acsphotonics.3c00773.
Derivations of general properties; Kubo formula for Floquet systems and generalized K.K. Relations; twolevel system derivations; derivation of polarizability; and Lorentz parametric oscillator derivations (PDF)
■
AUTHOR INFORMATION
Corresponding Author
Jamison Sloan − Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, United States; Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, United States; orcid.org/0000-0001-9944-2631; Email: jamison@mit.edu
Authors
Nicholas Rivera − Department of Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, United States; Department of Physics, Harvard University, Cambridge, Massachusetts 02138, United States; orcid.org/0000-0002-8298-1468
John D. Joannopoulos − Department of Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, United States Marin Soljacic − Department of Physics and Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, United States
Complete contact information is available at: https://pubs.acs.org/10.1021/acsphotonics.3c00773
Funding
J.S. acknowledges support from a Mathworks fellowship, as well as earlier support from a National Defense Science and Engineering Graduate Fellowship of the Department of Defense (F-1730184536). N.R. acknowledges the support of a Junior Fellowship from the Harvard Society of Fellows, as well as earlier support from a Computational Science Graduate Fellowship of the Department of Energy (DE-FG0297ER25308) and a Dean’s Fellowship from the MIT School of Science. This material is based on work supported in part by the Defense Advanced Research Projects Agency (DARPA) under agreement no. HR00112090081. This material is also based upon work supported in part by the Air Force Office of Scientific Research under award numbers FA9550-20-1-0115 and FA9550-20-1-0229; the work is also supported in part by the U.S. Army Research Office through the Institute for Soldier Nanotechnologies at MIT, under Collaborative Agreement Number W911NF-18-2-0048.
Notes
The authors declare no competing financial interest.
■
ACKNOWLEDGMENTS
We thank Ido Kaminer, Oren Cohen, and Matan Even Tzur for useful discussions.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
960


 ■ REFERENCES
(1) Galiffi, E.; Tirole, R.; Yin, S.; Li, H.; Vezzoli, S.; Huidobro, P. A.; Silveirinha, M. G.; Sapienza, R.; Alù, A.; Pendry, J. Photonics of timevarying media. Adv. Photonics 2022, 4, 014002. (2) Zhou, Y.; Alam, M. Z.; Karimi, M.; Upham, J.; Reshef, O.; Liu, C.; Willner, A. E.; Boyd, R. W. Broadband frequency translation through time refraction in an epsilon-near-zero material. Nat. Commun. 2020, 11, 2180.
(3) Pacheco-Peña, V.; Engheta, N. Temporal aiming. Light: Sci. Appl. 2020, 9, 129. (4) Plansinis, B.; Donaldson, W.; Agrawal, G. What is the temporal analog of reflection and refraction of optical beams? Phys. Rev. Lett. 2015, 115, 183901. (5) Shaltout, A.; Kildishev, A.; Shalaev, V. Time-varying metasurfaces and Lorentz non-reciprocity. Opt. Mater. Express 2015, 5, 2459−2467. (6) Li, H.; Yin, S.; Alù, A. Nonreciprocity and Faraday Rotation at Time Interfaces. Phys. Rev. Lett. 2022, 128, 173901. (7) Pendry, J. B.; Galiffi, E.; Huidobro, P. A. Gain mechanism in time-dependent media. Optica 2021, 8, 636−637. (8) Lustig, E.; Sharabi, Y.; Segev, M. Topological aspects of photonic time crystals. Optica 2018, 5, 1390−1395. (9) Dikopoltsev, A.; Sharabi, Y.; Lyubarov, M.; Lumer, Y.; Tsesses, S.; Lustig, E.; Kaminer, I.; Segev, M. Light emission by free electrons in photonic time-crystals. Proc. Natl. Acad. Sci. U.S.A. 2022, 119, No. e2119705119. (10) Lyubarov, M.; Lumer, Y.; Dikopoltsev, A.; Lustig, E.; Sharabi, Y.; Segev, M. Amplified emission and lasing in photonic time crystals. Science 2022, 377, 425.
(11) Caloz, C.; Deck-Leger, Z. L. Spacetime Metamaterials�Part I: General Concepts. IEEE Trans. Antennas Propag. 2020, 68, 1569− 1582. (12) Engheta, N. Metamaterials with high degrees of freedom: space, time, and more. Nanophotonics 2020, 10, 639−642. (13) Yablonovitch, E. Accelerating reference frame for electromagnetic waves in a rapidly growing plasma: Unruh-Davies-FullingDeWitt radiation and the nonadiabatic Casimir effect. Phys. Rev. Lett. 1989, 62, 1742−1745. (14) Sloan, J.; Rivera, N.; Joannopoulos, J. D.; Soljačić, M. Casimir light in dispersive nanophotonics. Phys. Rev. Lett. 2021, 127, 053603. (15) Kort-Kamp, W. J.; Azad, A. K.; Dalvit, D. A. Space-Time Quantum Metasurfaces. Phys. Rev. Lett. 2021, 127, 043603. (16) Law, C. Effective Hamiltonian for the radiation in a cavity with a moving mirror and a time-varying dielectric medium. Phys. Rev. A: At., Mol., Opt. Phys. 1994, 49, 433−437.
(17) Zurita-Sánchez, J. R.; Halevi, P.; Cervantes-Gonzalez, J. C. Reflection and transmission of a wave incident on a slab with a timeperiodic dielectric function ε(t). Phys. Rev. A: At., Mol., Opt. Phys. 2009, 79, 053821. (18) Chu, R.; Tamir, T. Wave propagation and dispersion in spacetime periodic media. Proc. Inst. Electr. Eng. 1972, 119, 797−806. (19) Harfoush, F.; Taflove, A. Scattering of electromagnetic waves by a material half-space with a time-varying conductivity. IEEE Trans. Antennas Propag. 1991, 39, 898−906.
(20) Fante, R. Transmission of electromagnetic waves into timevarying media. IEEE Trans. Antennas Propag. 1971, 19, 417−424.
(21) Holberg, D.; Kunz, K. Parametric properties of fields in a slab of time-varying permittivity. IEEE Trans. Antennas Propag. 1966, 14, 183−194. (22) Lustig, E.; Segal, O.; Saha, S.; Bordo, E.; Chowdhury, S. N.; Sharabi, Y.; Fleischer, A.; Boltasseva, A.; Cohen, O.; Shalaev, V. M.; Segev, M. Time-refraction optics with single cycle modulation. Nanophotonics 2023, 12, 2221−2230.
(23) Un, I.-W.; Sarkar, S.; Sivan, Y. Electronic-Based Model of the Optical Nonlinearity of Low-Electron-Density Drude Materials. Phys. Rev. Appl. 2023, 19, 044043.
(24) Solis, D. M.; Engheta, N. Functional analysis of the polarization response in linear time-varying media: A generalization of the Kramers-Kronig relations. Phys. Rev. B 2021, 103, 144303.
(25) Horsley, S.; Galiffi, E.; Wang, Y.-T. Eigenpulses of dispersive time-varying media. Phys. Rev. Lett. 2023, 130, 203803. (26) Alu, A.; Silveirinha, M. G.; Salandrino, A.; Engheta, N. Epsilonnear-zero metamaterials and electromagnetic sources: Tailoring the radiation phase pattern. Phys. Rev. B: Condens. Matter Mater. Phys. 2007, 75, 155410. (27) Reshef, O.; De Leon, I.; Alam, M. Z.; Boyd, R. W. Nonlinear optical effects in epsilon-near-zero media. Nat. Rev. Mater. 2019, 4, 535−551. (28) Kubo, R. Statistical-mechanical theory of irreversible processes. I. General theory and simple applications to magnetic and conduction problems. J. Phys. Soc. Jpn. 1957, 12, 570−586. (29) Landau, L. D.; Bell, J.; Kearsley, M.; Pitaevskii, L.; Lifshitz, E.; Sykes, J. Electrodynamics of Continuous Media; Elsevier, 2013; Vol. 8. (30) Rudner, M. S.; Lindner, N. H. Band structure engineering and non-equilibrium dynamics in Floquet topological insulators. Nat. Rev. Phys. 2020, 2, 229−244. (31) Wackerl, M.; Wenk, P.; Schliemann, J. Floquet-drude conductivity. Phys. Rev. B 2020, 101, 184204. (32) Kramers, H. A. La diffusion de la lumiere par les atomes. Atti Cong. Intern. Fisica 1927, 2, 545−557.
(33) de L Kronig, R. On the theory of dispersion of x-rays. J. Opt. Soc. Am. 1926, 12, 547−557.
(34) Galiffi, E.; Huidobro, P. A.; Pendry, J. B. An Archimedes’ screw for light. Nat. Commun. 2022, 13, 2523. (35) Aspnes, D. Local-field effects and effective-medium theory: a microscopic perspective. Am. J. Phys. 1982, 50, 704−709. (36) Sharabi, Y.; Dikopoltsev, A.; Lustig, E.; Lumer, Y.; Segev, M. Spatiotemporal photonic crystals. Optica 2022, 9, 585−592. (37) Morgenthaler, F. R. Velocity modulation of electromagnetic waves. IRE Trans. Microwave Theory Tech. 1958, 6, 167−172. (38) Boyd, R. W. Nonlinear Optics; Academic Press, 2019. (39) Jiang, M.; Su, H.; Wu, Z.; Peng, X.; Budker, D. Floquet maser. Sci. Adv. 2021, 7, No. eabe0719. (40) Deng, C.; Orgiazzi, J.-L.; Shen, F.; Ashhab, S.; Lupascu, A. Observation of floquet states in a strongly driven artificial atom. Phys. Rev. Lett. 2015, 115, 133601.
(41) Stehlik, J.; Liu, Y.-Y.; Eichler, C.; Hartke, T.; Mi, X.; Gullans, M.; Taylor, J.; Petta, J. R. Double quantum dot floquet gain medium. Phys. Rev. X 2016, 6, 041027.
(42) Clark, L. W.; Jia, N.; Schine, N.; Baum, C.; Georgakopoulos, A.; Simon, J. Interacting floquet polaritons. Nature 2019, 571, 532−536. (43) Biancalana, F.; Amann, A.; Uskov, A. V.; O’reilly, E. P. Dynamics of light propagation in spatiotemporal dielectric structures. Phys. Rev. E: Stat., Nonlinear, Soft Matter Phys. 2007, 75, 046607.
(44) Reyes-Ayona, J.; Halevi, P. Observation of genuine wave vector (k or β) gap in a dynamic transmission line and temporal photonic crystals. Appl. Phys. Lett. 2015, 107, 074101.
(45) Basov, D.; Fogler, M.; Garcia de Abajo, F. Polaritons in van der Waals materials. Science 2016, 354, aag1992. (46) Cartella, A.; Nova, T. F.; Fechner, M.; Merlin, R.; Cavalleri, A. Parametric amplification of optical phonons. Proc. Natl. Acad. Sci. U.S.A. 2018, 115, 12148−12151. (47) Sugiura, S.; Demler, E. A.; Lukin, M.; Podolsky, D. Resonantly enhanced polariton wave mixing and Floquet parametric instability. arXiv 2019, arXiv:1910.03582. (48) Ruby, L. Applications of the Mathieu equation. Am. J. Phys. 1996, 64, 39−44. (49) Ptitcyn, G.; Lamprianidis, A.; Karamanos, T.; Asadchy, V.; Alaee, R.; Müller, M.; Albooyeh, M.; Mirmoosa, M. S.; Fan, S.; Tretyakov, S.; et al. Floquet−Mie Theory for Time-Varying Dispersive Spheres. Laser Photonics Rev. 2023, 17, 2100683. (50) McPherson, A.; Gibson, G.; Jara, H.; Johann, U.; Luk, T. S.; McIntyre, I.; Boyer, K.; Rhodes, C. K. Studies of multiphoton production of vacuum-ultraviolet radiation in the rare gases. J. Opt. Soc. Am. B 1987, 4, 595−601.
(51) Lewenstein, M.; Balcou, P.; Ivanov, M. Y.; L’huillier, A.; Corkum, P. B. Theory of high-harmonic generation by low-frequency laser fields. Phys. Rev. A: At., Mol., Opt. Phys. 1994, 49, 2117−2132.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
961


 (52) Paul, P.-M.; Toma, E. S.; Breger, P.; Mullot, G.; Augé, F.; Balcou, P.; Muller, H. G.; Agostini, P. Observation of a train of attosecond pulses from high harmonic generation. Science 2001, 292, 1689−1692. (53) Krausz, F.; Ivanov, M. Attosecond physics. Rev. Mod. Phys. 2009, 81, 163−234. (54) Ghimire, S.; Reis, D. A. High-harmonic generation from solids. Nat. Phys. 2019, 15, 10−16.
(55) Gorlach, A.; Neufeld, O.; Rivera, N.; Cohen, O.; Kaminer, I. The quantum-optical nature of high harmonic generation. Nat. Commun. 2020, 11, 4598.
(56) Neufeld, O.; Podolsky, D.; Cohen, O. Floquet group theory and its application to selection rules in harmonic generation. Nat. Commun. 2019, 10, 405.
(57) Kim, I. J.; Kim, C. M.; Kim, H. T.; Lee, G. H.; Lee, Y. S.; Park, J. Y.; Cho, D. J.; Nam, C. H. Highly efficient high-harmonic generation in an orthogonally polarized two-color laser field. Phys. Rev. Lett. 2005, 94, 243901.
(58) L’Huillier, A.; Schafer, K.; Kulander, K. Higher-order harmonic generation in xenon at 1064 nm: The role of phase matching. Phys. Rev. Lett. 1991, 66, 2200−2203.
(59) Salieres, P.; L’Huillier, A.; Lewenstein, M. Coherence control of high-order harmonics. Phys. Rev. Lett. 1995, 74, 3776−3779. (60) Fleischer, A.; Moiseyev, N. Amplification of high-order harmonics using weak perturbative high-frequency radiation. Phys. Rev. A: At., Mol., Opt. Phys. 2008, 77, 010102.
(61) Fleischer, A. Generation of higher-order harmonics upon the addition of high-frequency XUV radiation to IR radiation: Generalization of the three-step model. Phys. Rev. A: At., Mol., Opt. Phys. 2008, 78, 053413. (62) Krüger, M.; Azoury, D.; Bruner, B. D.; Dudovich, N. The role of electron trajectories in XUV-initiated high-harmonic generation. Appl. Sci. 2019, 9, 378.
(63) Seres, J.; Seres, E.; Hochhaus, D.; Ecker, B.; Zimmer, D.; Bagnoud, V.; Kuehl, T.; Spielmann, C. Laser-driven amplification of soft X-rays by parametric stimulated emission in neutral gases. Nat. Phys. 2010, 6, 455−461. (64) Bao, C.; Tang, P.; Sun, D.; Zhou, S. Light-induced emergent phenomena in 2D materials and topological materials. Nat. Rev. Phys. 2022, 4, 33−48. (65) Yu, R.; Fan, S. Manipulating coherence of near-field thermal radiation in time-modulated systems. Phys. Rev. Lett. 2023, 130, 096902. (66) Rivera, N.; Kaminer, I. Light-matter interactions with photonic quasiparticles. Nat. Rev. Phys. 2020, 2, 538−561.
ACS Photonics pubs.acs.org/journal/apchd5 Article
https://doi.org/10.1021/acsphotonics.3c00773 ACS Photonics 2024, 11, 950−962
962
