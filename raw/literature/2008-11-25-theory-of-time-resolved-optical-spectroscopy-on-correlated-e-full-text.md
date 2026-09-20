# Theory of time-resolved optical spectroscopy on correlated electron systems - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevB.78.205119
> Collected: 2026-09-20
> Published: 2008-11-25
> Zotero parent key: 5HVV7WQB
> Evidence: Zotero indexed PDF text

arXiv:0808.1005v1 [cond-mat.str-el] 7 Aug 2008
Theory of time-resolved optical spectroscopy on correlated electron systems
Martin Eckstein and Marcus Kollar
Theoretical Physics III, Center for Electronic Correlations and Magnetism, Institute for Physics, University of Augsburg, 86135 Augsburg, Germany (Dated: August 7, 2008)
The real-time dynamics of interacting electrons out of equilibrium contains detailed microscopic information about electronically correlated materials, which can be read out with time-resolved optical spectroscopy. The reflectivity that is typically measured in pump-probe experiments is related to the nonequilibrium optical conductivity. We show how to express this quantity in terms of real-time Green functions using dynamical mean-field theory. As an application we study the electrical response of the Falicov-Kimball model during the ultrafast buildup of the gapped phase at large interaction.
I. INTRODUCTION
Electronic correlations are known to give rise to highly unusual phenomena such as heavy fermion behavior or the Mott metal-insulator transitions.1 In recent years a new perspective for this field has been provided by various pump-probe spectroscopies, which can directly track the time evolution of strongly interacting systems far from equilibrium. For example, the dynamics of electrons in the vicinity of a Mott metalinsulator transition was investigated using time-resolved photoemission spectroscopy2 and time-resolved optical spectroscopy.3,4,5,6,7 In these experiments, the sample is first excited by an intense laser pulse (pump); a second pulse (probe), which comes at a controlled timedelay, is then used to characterize the transient state by means of photoemission or optical spectroscopy. Pumpprobe experiments with femtosecond time-resolution are now commonly used for the investigation of dynamics in molecules,8 metals,9 and semiconductors.10 Recent development of shorter and shorter pulses has pushed the limiting time-resolution below 10 fs for optical frequencies,11 and into the attosecond regime for pulses in the extreme ultraviolet.12
For solids it is often a subtle task to distinguish the contribution of various degrees of freedom to a specific phenomenon. The Mott transition is induced by the Coulomb repulsion between electrons, but can occur simultaneously with a change of the lattice structure, obscuring the primary origin of the phase transition. In time-resolved experiments, however, different degrees of freedom can be identified if they evolve on different time scales.2,7 In particular, the lattice usually reacts much slower than the electronic system. Many phenomena that are already visible at low time resolution can be explained in terms of a two-temperature model,2,13 which assumes that the electronic system is in thermal equilibrium at any given time, but may have a different temperature than the lattice.
On the other hand, pump-probe experiments allow for an investigation of the electronic real-time dynamics. For example, two-photon photoemission spectroscopy can monitor the ultrafast thermalization of a pumped elec
tron gas in metals within several 100 fs.9,14 In semiconducting GaAs, the buildup of a screened Coulomb interaction in the electron-hole plasma created by the photoexcitation of electrons into the conduction band has been tracked using time-domain THz spectroscopy.15 In particular the latter experiment probes the true quantum dynamics of the state, which can no longer be described by a simple rate equation but requires the full manyparticle Hamiltonian.16,17 It would be very interesting to measure the electronic dynamics in strongly interacting systems, which may dominate, e.g., the ultrafast buildup of intermediate metallic states across insulator-to-metal transitions,3,4,6,7 or the melting of correlation-induced long-range order after an external perturbation.5 The goal of this paper is to set up the framework for a microscopic description of time-resolved optical measurements in such strongly correlated electron systems. For timeresolved photoemission spectroscopy, the microscopic description was recently derived in Ref. 18. The microscopic formalism of isolated quantum manybody systems out of equilibrium was given independently by Baym and Kadanoff,19 and Keldysh20 in terms of realtime Green functions. It provides the starting point for a nonequilibrium perturbation theory,21,22 which is however bound to fail for strong interactions. Dynamical mean-field theory (DMFT),23 which becomes exact in the limit of infinite spatial dimension,24 also applies to the non-perturbative regime. DMFT self-consistently maps a lattice model onto an auxiliary single-site problem. The equilibrium theory has been instrumental in understanding many correlation-induced phenomena, such as the Mott transition, both for simple model systems,23 and for real materials.25,26 Recently, DMFT for nonequilibrium has been formulated in the framework of Keldysh theory.27 It has been used to investigate the FalicovKimball model28,29 under the influence of strong electrical fields,27,30 as well as its relaxation over the metalinsulator transition after a sudden change of the interaction parameter.31 Similar investigations for the Hubbard model still require new techniques for the solution of the effective single-site problem. However, promising candidates for this task have been developed during the last years.32,33 The main purpose of this paper is to discuss the probe


 2
process in optical spectroscopy in terms of linear response of a nonequilibrium state to an electromagnetic field. For this state, which might originate from the application of a pump pulse, the time evolution is assumed to be known from DMFT. The response is given by the two-time optical conductivity σ(t, t′), that relates the current at time t to electrical fields in the sample at earlier times t′.34 For systems in equilibrium DMFT has already been successfully used to understand optical spectroscopy in correlated materials.35 The standard expression for the frequency-dependent conductivity σ(ω) in DMFT36 is quite simple and contains only single-particle Green functions, because vertex corrections to the current-current correlation function vanish for isotropic systems.36,37 In this paper we derive an expression for the two-time conductivity σ(t, t′) from nonequilibrium DMFT, which turns out to be a direct generalization of the equilibrium expression36 to Keldysh language. In particular, our derivation shows when the inclusion of vertex corrections becomes mandatory in nonequilibrium situations, and under which conditions similar simplification occur for σ(t, t′) as for σ(ω). We then apply the theory to a simple lattice model for interacting electrons in a single band,
H =∑
ijσ
Vσ
ij c†
iσcjσ + U ∑ i
ni↑ni↓ − ∑ iσ
μσniσ. (1)
Here c(†)
iσ are annihilation (creation) operators for two
species of fermions (σ = ↓,↑) on lattice site i, which interact via a local Coulomb repulsion U . The first term in (1) is a tight-binding description of the electronic band. Eq. (1) is the Hamiltonian of the defines the Hubbard model if the hopping Vijσ does not depend on the flavor σ, or the Falicov-Kimball model28 if one particle species is immobile (V ↑
ij = 0). Both models have a rich phase di
agram as a function of interaction and filling, including metallic, insulation and ordered phases. In the presence of electromagnetic fields [with scalar and vector potential Φ(r, t) and A(r, t)], the hopping amplitudes acquire Peierls phase factors38,39
Vij = V ̃ij exp

 
ie ħc
Rj
∫
Ri
dr A(r, t)


 , (2)
and a potential term −e ∑
iσ Φ(Ri, t)c†
iσciσ is added to
the Hamiltonian, where −e is the charge of an electron. Here and throughout a tilde indicates that the quantity is taken in zero external field. Nonequilibrium DMFT can potentially model the full pump-probe process by including the pump field explicitly in Eq. (2). In the application of the general result to the Falicov-Kimball model we use an idealized nonequilibrium situation instead, where the “pumping” is an instantaneous event; we only have to know the excited state after the pumping, which is taken as initial state for the
subsequent time evolution. This permits an investigation of the relaxation between the various phases. For instance, we can start from a metallic state and follow the relaxation in the insulating parameter regime of the Hamiltonian. Below we model this situation by a sudden increase of the interaction parameter U . We therefore allow for arbitrary time dependence of all parameters U ,
μ and V ̃ijσ in the Hamiltonian (1).
This paper is outlined as follows. In Section II, we define the optical conductivity in nonequilibrium experiments, and discuss its relation to the reflectivity in timeresolved measurements. In Section III we shortly review DMFT for nonequilibrium. We then derive the nonequilibrium optical conductivity in DMFT in Section IV. Finally, in Section V we apply the theory to the FalicovKimball model and investigate the response of the system during the ultrafast buildup of the gapped phase at large interaction.
II. TIME-RESOLVED OPTICAL SPECTROSCOPY
To understand the results of time-resolved optical spectroscopy it is necessary to know how weak electromagnetic pulses of finite length propagate through the sample, which is not in equilibrium due to the applied pump pulse.34,40,41 The current δj is the linear response induced by the probe field,
δjα(r, t) =
t
∫
−∞
dt′ σαβ(t, t′) δEβ(r, t′), (3)
which defines the optical conductivity σαβ(t, t′) for samples that are not in equilibrium. (Here and throughout α and β are cartesian components of the vectors, and repeated indices are summed over.) Note that only the response (3) is linear in the probe field δEβ(r, t′), while arbitrarily strong electric pump fields might be acting on the sample. The wavelength in optical spectroscopy is typically much larger than the lattice spacing of the sample, so that the linear response relation (3) is essentially local in space. On the other hand it is not local in time, and unless there is a clear separation between the time scales that govern the electromagnetic response and the relaxation of the nonequilibrium state, σ(t, t′) depends not only on the difference of its time arguments but on both t and t′ separately. Of course σ(t, t′) is always causal, i.e., it vanishes for t < t′. Knowledge of σ(t, t′) is sufficient to calculate the reflected and transmitted pulses from Maxwell’s equations, assuming that the induced current inside the sample is given by Eq. (3).34,40,41 However, the relation to measurable quantities is more complicated than for samples that are in equilibrium. To illustrate we this consider a typical time-resolved reflection experiment, performed at normal incidence, on a sample that is infinite in the y-z plane (cf. Fig. 1). Outside the sample light propa


 3
cτ
cτ
E (τ)
E (τ)
0
refl
x
L
d
d
t>0
t<0
x=c(t−t )
x=−c(t−t )
FIG. 1: Time-resolved reflection experiment. For t → −∞ a probe pulse E0(t, x) = zˆE0(t − td − x/c) propagates in +x direction without dispersion (upper panel). The sample is hit at times near t = td, and emits the reflected pulse Erefl(t, x) = zˆErefl(t − td + x/c), which propagates in −x direction after leaving the sample (lower panel).
gates without dispersion, so that we may write E0(t, x) = zˆE0(t − td − x/c) and Erefl(t, x) = zˆErefl(t − td + x/c) for incident and reflected pulses at x → −∞, respectively. The functions E0(τ ) and Erefl(τ ) are centered around τ = 0, and td is the probe delay. For simplicity we assumed cubic symmetry, such that the polarization direction zˆ for both pulses is the same. We then define a generalized reflection coefficient r(t, t′),34
Erefl(τ ) =
∞
∫
0
ds r(td + τ, td + τ − s)E0(τ − s), (4)
providing a linear relation between the two pulses. The full two-dimensional time-dependence of r(t, t′) can be deduced from experiment by suitably choosing the pulse, and measuring at all possible pump-probe delays td. However, if the optical conductivity σ(t, t′) depends on t and t′ separately, then there is no simple relation to the reflection coefficient r(t, t′).41 This is evident from the definition (4), which shows that a sample which is not in equilibrium can modulate the pulse frequency. From now on we use an approximate form for r(t, t′), which is valid for reflection from a very thin slab (with thickness L → 0), such that the phase lag between the borders is negligible. In this case Maxwell’s equations are easily solved, yielding34
r(t, t′) = L
c σ(t, t′). (5)
A more realistic description, which takes the finite thickness of the sample and its inhomogeneous excited state into account, requires the numerical simulation of the pulse propagation40 and of the inverse problem41 of obtaining σ(t, t′) from r(t, t′). However, the treatment of such effects is beyond the scope of this paper, the goal of which is to calculate the optical conductivity σ(t, t′) microscopically for an interacting many-body system that is not in equilibrium.
III. DMFT FOR NONEQUILIBRIUM
DMFT for nonequilibrium usually starts from thermal equilibrium at some early time t = tmin.27,31 For t ≥ tmin the system evolves according to the Hamiltonian (1), driven out of equilibrium if the Hamiltonian changes with time. Thermodynamic variables and optical response functions are obtained from the retarded, advanced and lesser real-time Green functions,
GiRjσ(t, t′) = −iΘ(t − t′)〈{ciσ(t), c†
jσ(t′)}〉 (6a)
GiAjσ(t, t′) = iΘ(t′ − t)〈{ciσ(t), c†
jσ(t′)}〉 (6b)
G<
ijσ (t, t′) = i〈c†
jσ(t′)ciσ(t)〉. (6c)
(Although retarded and advanced Green functions are in fact related by symmetry, both are given here for later reference.) The average 〈·〉 = Tr[ρ0·] in Eq. (6) is over initial states at t = tmin, distributed according to the grand-canonical density matrix ρ0 ∝ exp[−βH(tmin)] at inverse temperature β. The operators ciσ(t) = U (t, tmin)ciσU (tmin, t) are in Heisenberg representation with respect to the full time evolution U (t, t′) = Tt ̄ exp[−i ∫ t′
t dt ̄H(t ̄)]. Using the Keldysh
formalism20,21,22 the Green functions (6) are then calculated in terms of a more general contour-ordered Green function Gij,σ(t, t′) = −i〈TCciσ(t)c†
jσ(t′)〉 with time ar
guments on the contour C that runs from tmin to some larger time tmax on the real axis, then from tmax to tmin, and finally to tmin − iβ on the imaginary time axis. For
the retarded, advanced and lesser components one has21
GiRjσ (t, t′) = Θ(t − t′)[G−+
ijσ (t, t′) − G+−
ijσ (t, t′)] (7a)
= G++
ijσ (t, t′) − G+−
ijσ (t, t′) (7b)
GiAjσ (t, t′) = Θ(t′ − t)[G+−
ijσ (t, t′) − G−+
ijσ (t, t′)] (7c)
= G+−
ijσ (t, t′) − G−−
ijσ (t, t′) (7d)
G<
ijσ (t, t′) = G+−
ijσ (t, t′), (7e)
where the superscripts ± indicate whether the first and second time arguments are on the upper or lower realtime branch of the contour, respectively.
From now on we only consider translationally invariant nonequilibrium states, i.e., we assume that the Green function Gij,σ(t, t′) depends only on the difference Ri − Rj, with diagonal Fourier transform Gkσ(t, t′). This assumes that the electromagnetic fields do not depend on explicitly on position either, which is justified for experiments at optical frequencies, as discussed above in Sec. II. We use a gauge with zero scalar potential Φ, for which electrical field is given by E(t) = −∂tA(t)/c. The hopping amplitude Vij [Eq. (2)] then also depends only on the distance Ri −Rj ; its Fourier transform ǫkσ(t) is given


 4
by38,39
ǫkσ(t) = ∑
j
Vσ
ij exp[ik(Rj − Ri)] = ǫ ̃k+ e
ħc A(t),σ , (8a)
ǫ ̃kσ = ∑
j
V ̃ σ
ij exp[ik(Rj − Ri)] , (8b)
i.e., ǫkσ(t) is obtained from the zero-field dispersion ǫ ̃kσ by a time-dependent shift in momentum. The interacting contour Green function satisfies the Dyson equation21,22
[(G−1
kσ − Σkσ) ∗ Gkσ](t, t′) = δC(t, t′), (9)
where Σkσ(t, t′) is the contour self-energy and Gkσ(t, t′) is the noninteracting Green function, whose inverse
G−1
kσ (t, t′) = δC(t, t′)[i∂C
t + (μσ − ǫkσ(t))/ħ] (10)
can be written as a differential operator on the contour. Here (f ∗ g)(t, t′) = ∫
C dt ̄f (t, t ̄)g(t ̄, t′) is the convolution
of two functions along the contour, δC(t, t′) is the con
tour delta function [defined by ∫
Cdt ̄f (t ̄)δC(t ̄, t) = f (t)],
and ∂tC denotes the contour derivative.27 The unique solution of Eq. (9) is determined by antiperiodic boundary conditions for the contour Green functions in both time arguments.21,22 The DMFT self-energy is local in space, i.e., Σkσ is independent of k for a translationally invariant system. This approximation becomes exact in the limit of infinite spatial dimensions,24 both for the equilibrium self-energy and the Keldysh self-energy.27 In DMFT the local selfenergy Σσ(t, t′) and the local Green function Gσ(t, t′),
Gσ(t, t′) ≡ Giiσ(t, t′) = 1
N
∑
k
Gkσ(t, t′) , (11)
(N is the number of lattice sites in the sample) are determined from an auxiliary problem in which the degrees of freedom at a single lattice site i are coupled to some unknown environment. The latter must be determined selfconsistently, by solving the auxiliary problem together with the Dyson equation (9). As the precise form of the local problem in terms of its many-body action does not enter into the derivation of the electromagnetic response below, we refer to previous work for further details.27,31
IV. OPTICAL CONDUCTIVITY IN DMFT
The current operator for the Hamiltonian (1) is defined42,43,44 by the relation j(r) = −cδH/δA(r). Using Eq. (2), we obtain the current in the long wave-length limit as
〈j(t)〉 =
〈1
V
∫
ddrj(r)eiqr
〉
q→0
, (12a)
= ie
V
∑
kσ
vkσ (t)G<
kσ(t, t) , (12b)
the current vertex is given by
vkσ (t) = ħ−1∂kǫkσ(t) = ħ−1∂kǫ ̃k+ e
ħc A(t),σ . (12c)
and V is the volume of the sample. Although the response to arbitrarily strong fields is described by DMFT27, here we are interested in the linear current response to a weak probe field. We define the susceptibility
χαβ(t, t′) = δ〈jα(t)〉/Aβ(t′). (13)
In the chosen gauge with E(t) = −∂tA(t)/c, the susceptibility χαβ(t, t′) is related to the optical conductivity σαβ(t, t′) [Eq. (3)] by
σαβ (t, t′) = −c
∞
∫
t′
dt ̄χαβ(t, t ̄). (14)
The susceptibility (13) is related to the current-current correlation function, which can be evaluated in analogy to the equilibrium case.36 Here we prefer to take the derivative of (12b) directly, where the vector potential enters both in the vertex vkσ(t) and in the Green function
G<
kσ(t, t). This yields the diamagnetic and paramagnetic
contributions to the susceptibility,
χαβ (t, t′) = χdαiβa(t, t′) + χpm
αβ (t, t′) , (15a)
χdαiβa(t, t′) = ie
V
∑
kσ
δvα
kσ (t)
δAβ(t′) G<
kσ(t, t) , (15b)
χpm
αβ (t, t′) = ie
V
∑
kσ
vα
kσ (t) δG<
kσ(t, t)
δAβ (t′) . (15c)
The paramagnetic contribution can be found from a variation of the lattice Dyson equation (9),
δGkσ = −Gkσ ∗ [δG−1
kσ − δΣσ] ∗ Gkσ. (16)
Some simplifications occur in the absence of anisotropies. We note that the second term in (16), containing the k-independent self-energy, does not contribute to the k-sum in Eq. (15c) if, under inversion of k, (i) Gkσ is symmetric and (ii) the vertex vkσ is antisymmetric. These conditions are met by an isotropic system without external fields, and are therefore generally valid for systems with inversion symmetry in equilibrium.37 However, the isotropy may be lost when an initially isotropic system is driven out of equilibrium, e.g., when a current is induced by the electrical pump field. Furthermore, the vertex (12c) is no longer antisymmetric when an electrical field is present in addition to the probe field, i.e., when the paramagnetic susceptibility (15c) is evaluated at A 6= 0. Experimentally these anisotropic effects in otherwise isotropic systems show up as a dependence of the signal on the relative polarization of pump and probe pulses. However, when the anisotropy is caused entirely by the pump pulse, the inversion symmetry of Gkσ∗ δΣσ∗ Gkσ can be restored by averaging over the pump pulse


 5
polarization. Then this term again drops out in (15c), provided that vkσ(t) is antisymmetric (i.e., A(t) = 0). In order to study such anisotropic effects, vertex corrections contained in δΣσ must be taken into account (even for cubic lattices), by solving a Bethe-Salpeter equation on the Keldysh contour, with the irreducible vertex function δΣσ/δGσ from the auxiliary single-site problem as input. In the following we only consider the completely isotropic relaxation between homogeneous phases, such that the vertex corrections δΣσ can be disregarded. Eq. (15c) is evaluated at zero field, so that only the first
term δFkσ(t1, t2) = −[Gkσ ∗ δ(G−1
kσ ) ∗ Gkσ](t1, t2) con
tributes to δGkσ in Eq. (16). This corresponds to keeping only the elementary bubble diagram for the currentcurrent correlation function.36 The two convolutions in
δFkσ(t1, t2) collapse to a single one because [δG−1
kσ ](t, t′)
∝ δC(t, t′). In order to obtain δG<
kσ(t, t) we take t1 = t
and t2 = t on the upper and lower branch of the contour, respectively [cf. Eq. (7)]. The contour integral is then transformed into an integral along the real axis,
δFkσ(t+, t−) = e
ħc
∞
∫
−∞
dt ̄vkσ (t ̄)δA(t ̄)
× [G++
kσ (t, t ̄)G+−
kσ (t ̄, t) − G+−
kσ (t, t ̄)G−−
kσ (t ̄, t)] (17)
from which the optical conductivity σαβ(t, t′) can be read
off. From Eq. (7), together with the relations G<
kσ (t, t′)
= −G<
kσ(t′, t)∗ and GkRσ(t, t′) = GkAσ(t′, t)∗, we finally
obtain the paramagnetic susceptibility
χpm
αβ (t, t′) = −2χ0
∑
kσ
v ̃α
kσ v ̃β
kσIm[GkRσ (t, t′)G<
kσ(t′, t)],
(18a)
where χ0 = e2/(V ħc) and v ̃kσ = ∂kǫ ̃k,σ/ħ. The diamagnetic contribution follows directly from (12c):
χdαiβa(t, t′) = iχ0
ħ δ(t − t′)∑
kσ
(∂kα∂kβ ǫ ̃kσ)G<
kσ(t, t) . (18b)
Eqs. (14) and (18) constitute our final DMFT expressions for the optical conductivity (provided that anisotropic effects are disregarded, as discussed above). The optical conductivity (14) can be written as
σαβ (t, t′) = [σreg
αβ (t, t′) + Dαβ(t)]Θ(t − t′) , (19)
i.e., it splits into its regular part
σreg
αβ (t, t′) = c
t′
∫
−∞
dt ̄χpm
αβ (t, t ̄) , (20)
which vanishes in the limit t′ → −∞, and the Drude
contribution
Dαβ(t) ≡ lim
t′→−∞ σαβ (t, t′) (21a)
= σdαiβa(t) − c
t
∫
−∞
dt ̄χpm
αβ (t, t ̄), (21b)
which does not depend on the time difference at all. In
the latter expression, σdαiβa(t) = −c ∫ ∞
−∞ dt′ χdαiβa(t, t′) is the weight of the delta function in Eq. (18b). A finite Drude contribution Dαβ(t) 6= 0 indicates perfect metallic behavior, because it gives rise to a delta function at zero frequency in the partially Fourier-transformed optical conductivity
σ ̃αβ(t, ω) =
∞
∫
0
ds ei(ω+i0)sσαβ (t, t − s) (22a)
= σ ̃reg
αβ (t, ω) + iDαβ(t)
ω + i0 . (22b)
Note that Eqs. (18) and (20) can be checked by inserting equilibrium Green functions
GkRσ(t, t′) = −iΘ(t − t′)
∫
dω Akσ(ω)eiω(t′−t) , (23a)
G<
kσ(t, t′) = i
∫
dω Akσ(ω)f (ω)eiω(t′−t) , (23b)
with the spectral function Akσ(ω) = −Im[GkRσ(ω +
i0)]/π and the Fermi function f (ω) = 1/(1 + eβω), which depend only on time differences, into Eq. (22). Then the well-known expression for the regular part of the optical conductivity in equilibrium,36
Re σreg
αβ (ω) = πcχ0
∑
kσ
v ̃α
kσ v ̃β
kσ ×
∞
∫
−∞
dω′ Akσ(ω′)Akσ(ω + ω′)[f (ω′) − f (ω + ω′)]
ω , (24)
is recovered.
V. PUMP-PROBE SPECTROSCOPY ON THE FALICOV-KIMBALL MODEL
A. The Falicov-Kimball model in nonequilibrium
In the remaining part of this paper we focus on a specific electronic model, the Falicov-Kimball model. This lattice model describes itinerant (↓) electrons and immobile (↑) electrons that interact via a repulsive local interaction U .28 The Hamiltonian is given by Eq. (1) with V ↑
ij = 0. The Falicov-Kimball model has been
an important benchmark for the development of DMFT in equilibrium, because the effective single-site problem


 6
for the mobile particles is quadratic and can be solved exactly.45 It currently plays a similar role for nonequilibrium DMFT,27,30,31 in particular since no appropriate real-time impurity solver is yet available for the Hubbard model. In spite of its apparent simplicity the Falicov-Kimball model has a rich phase diagram containing metallic, insulating, and charge-ordered phases.29 In the following we fix the filling of both particle species (n↓ = n↑ = 1/2), and consider only the homogeneous phase without symmetry breaking. This phase undergoes a metal-insulator transition at a critical interaction U = Uc,45,46,47 from the gapless phase at U < Uc to the gapped phase at U > Uc. Below we assume that the system is prepared in thermal equilibrium for times t < 0. Then the interaction parameter U is changed abruptly at t = 0. In this way we study the relaxation of the system in the insulating parameter regime, starting from a weakly correlated state (U < Uc). This mimics an experiment similar to the one described in Ref. 15, where the buildup of a weakly correlated state is studied with time-resolved spectroscopy, starting from an uncorrelated state of electrons just after their excitation into an empty conduction band. Note that in this interpretation the state of the conduction band immediately after the pump pulse is the initial state for the relaxation process. The relaxation dynamics after such an interaction quench was recently investigated with DMFT using the exact Green functions Gk↓(t, t′) of the mobile particles.31 However, only thermodynamic observables were discussed in Ref. 31, with a special focus on their steady state value in the long-time limit. Here we consider instead hypothetical time-resolved experiments that are performed on the system during relaxation, i.e., we use the Green functions from Ref. 31 to evaluate the optical conductivity from Eq. (18). Momentum summations in (18) are performed for a hypercubic lattice, taking the dispersion ǫ ̃k to be that of a semielliptic density of
states,48 ρ(ǫ) = (2/πW 2)√W 2 − ǫ2 (cf. App. A). The half-bandwidth W = 2 sets the energy scale, such that the critical interaction is Uc = W = 2.
B. Optical conductivity and reflected electrical field
We study relaxation far in the insulating regime (U = 6), starting from an initial metallic state (U = 1). The optical conductivity σ(t, t − s) for this case is shown in Fig. 2a as a function of t and s. There are five regions [(i) to (v)] in this plot that we want to discuss in detail. In regions (i) [t < 0] and (ii) [t → ∞], σ(t, t − s) depends only on the time-difference s, indicating that the system is in a stationary state. For (i) this is the initial equilibrium state, and for (ii) it corresponds to the final steady state.31 The Fourier transformation (22a) of the conductivity exhibits a broad peak at ω = 0, both for the initial state [σ ̃(t = 0, ω)] and the final state [σ ̃(t = ∞, ω)]
-0.1
0
0.1
0.2
0.3
t [2−h/W]
s [2−h/W]
(i) (ii)
(iii)
(iv)
(v)
a❍
σ(t,t-s)/σ0
0 2 4 6 8 10
0
2
4
6
8
10
0
0.2
0.4
0.6
0.8
0246
Re σ~(t,ω)
ω [W/2−h]
b❍
σ~(t=0,ω)
σ~(t=∞,ω) T=2.070
0246
0.1
0.2
0.3
0.4
σdia(t)/σ0
t [2−h/W]
c❍
FIG. 2: (a) Optical conductivity σ(t, t − s) for the quench from the ground state at U = 1 (initial temperature T = 0) to U = 6 (nf = nc = 1/2, half-bandwidth W = 2). The unit of the conductivity is σ0 = N a2e2W/(2ħ2V ), where a is the lattice constant. In the region above the upper dashed line, t − s < 0. Below the lower dashed line the relaxation is essentially complete. (b) Fourier transform (22a) of the optical conductivity in the initial and final stationary state, and for an equilibrium state at U = 6, with the same excitation energy relative as the final state (T = 2.070). (c) Diamagnetic contribution (18b) to the susceptibility.
(cf. Fig. 2b). This clear indication of metallic behavior of the final state may seem surprising, since the interaction is far above the critical interaction Uc. However, a finite DC conductivity should be expected because the final state is highly excited with respect to the ground state at U = 6. In fact, the excitation energy corresponds to an effective temperature T = 2.070, for which the equilibrium DC conductivity σ(0) is already quite sizable even at U = 6 (dotted curve in Fig. 2b). However, σ(0) is still considerably lower compared to σ ̃(t = ∞, 0). This is a signature of the incomplete relaxation in the FalicovKimball model: The system does not relax to thermal equilibrium, but reaches a non-thermal steady state, as shown in Ref. 31 for thermodynamic quantities. In the present context we find that the electromagnetic response of the non-thermal final state combines some features of the insulating state (a peak around ω = 6 due to excitations across the gap) with a sizable DC conductivity. Full


 7
thermalization is expected only due to coupling to further degrees of freedom or further hopping or interaction terms that are not contained in (1). For t−s < 0 and t > 0 [region (iii) in Fig. 2a], σ(t, t−s) determines the current after the pumping at t = 0 caused by an electrical field applied to the sample before the pumping. It thus measures a combination of the electromagnetic response of the initial state and the subsequent decay of the induced current for t > 0. By contrast, in region (iv) in Fig. 2a it describes the response of the nonequilibrium state alone, and hence gives direct insight into various relaxation processes. True nonequilibrium dynamics can be observed only when both t − s and t are smaller than some relaxation time τstat, after which the response is stationary, i.e., when σ(t, t − s) depends on s only. In the present case the relaxation is virtually complete after only a few times of the inverse half-bandwidth (τstat ≈ 8/W = 4, below the lower dotted line in Fig. 2a). Therefore the relaxation time and the time scales of the electromagnetic response, which is set by the decline of σ(t, t − s) for s → ∞, apparently have the same order of magnitude. In spite of this very fast relaxation nontrivial transient behavior can be observed before the stationary state is reached. Consider σ(t, t − s) at s = 0, which traverses almost two damped oscillation cycles with an approximate period 2πħ/U before reaching its final value (Fig. 2c). Recall that σ(t, t) is given by the delta function weight σdia(t) of the diamagnetic susceptibility (18b) [cf. Eqs. (20) and (21)]. These oscillations are the hallmark of dynamics that are dominated by a Hubbard-type density interaction such as U ∑
i ni↑ni↓. In fact, when
the Hamiltonian is given only by this interaction term, the time evolution-operator exp[itU ∑
i ni↑ni↓] itself is
time-periodic,49 and oscillations should therefore be visible in all nonlocal quantities. These so-called collapseand-revival oscillations were first observed and described in experiments with ultra-cold atomic gases,49 where the Hamiltonian of the system can be designed in a controlled way. Finally we note that the conductivity σ(t, t − s) vanishes in the limit s → ∞ , i.e., the Drude weight (21) vanishes for all times [region (v) in Fig. 2a]. This is well known for the Falicov-Kimball model in equilibrium:29 unlike in the Hubbard model,43 the mobile particles do not form a perfect metal even at T = 0 because of the disordered background of immobile particles. Mathematically the vanishing of Dαβ(t) is due to the cancellation of the two terms in (21). Since each of them has a nontrivial time dependence (cf. Fig. 2c), this cancellation represents a strong check for our numerical evaluation of the conductivity. To illustrate the relation of the optical conductivity to time-resolved THz experiments, we use the simple expression (5) for the reflection coefficient, and calculate the reflected field Erefl(τ ; td) according to the definition (4), using a single cycle incident pulse E0(τ ) =
sin(τ ) exp(−2τ 2). The result is shown in Fig. 3. For short
-0.5
0
0.5
1
E0(τ) [a.u.]
a❍
--00000100......246842
τ [2−h /W]
td [2−h /W]
b❍
Erefl(τ;td)
-1 0 1 2 3 4 5
-2
-1
0
1
2
3
4
5
×
×
FIG. 3: Result of an idealized spectroscopy experiment (cf. Fig. 1): (a) Incident pulse. (b) Reflected pulse Erefl(τ ; td) [from Eqn. (4) and (5)], for a delay td of the incident pulse with respect to the start of the relaxation at t = 0. The region below the diagonal dotted line is not influenced by the quench at all. Above the horizontal dotted line (td & τstat = 4) the reflected signal is converged. For td < τstat, at least one revival peak at td = 2πħ/U is clearly visible (crosses).
delay times td between the incident pulse and the pumpevent at t = 0, the profile of the reflected field depend strongly on td. On the other hand, for times td & τstat, the relaxation is essentially complete, and Erefl(τ ) has developed a longer oscillating tail. This general behavior is also seen in the experiment of Ref. 15. In Fig. 3 the oscillations in Erefl(τ ) as a function of τ are characteristic of the gap in the final state. Furthermore, the abovementioned transient 2πħ/U -periodic oscillations are visible in the td dependence of the reflected field Erefl(τ ) at small τ .
VI. CONCLUSION
In this paper we generalized the familiar equilibrium expression for the optical conductivity in DMFT to the linear electromagnetic response of a nonequilibrium state. We find that the two-time optical conductivity σ(t, t′), which is probed in time-resolved optical spectroscopies, can be expressed in terms of electronic real-time Green functions [see Eqs. (14) and (18)], which can be obtained from the DMFT solution. The expression for σ(t, t′) is completely general. Only anisotropic effects are disregarded that would lead to a dependence of the signal on the relative polarization direction of pump and probe pulses, i.e., averaging over the pump-probe direction is assumed. As a first application we have applied the theory to


 8
a hypothetical pump-probe experiment on the FalicovKimball model. The pumping out of equilibrium was modelled by a sudden change in the interaction parameter, after which an electrical field pulse probes the relaxation between metallic and insulating phases. We observe very fast relaxation with a relaxation time comparable to the inverse bandwidth, such that no clear separation of the time scales occurs between the intrinsic relaxation and electromagnetic response. Moreover, the two-time optical conductivity reveals transient oscillations in the response on a shorter time scale on the order of the inverse interaction. These collapse-and-revival oscillations are expected to be very robust, e.g., for different densities. Using time-resolved spectroscopy it may thus be possible to observe this phenomenon, which is known from experiments with ultracold atoms in optical lattices, in the relaxation of correlated electrons in solids as well. In the future, it should become feasible to solve the DMFT equations also for the Hubbard model in nonequilibrium. This will provide important insight into the dynamics of the pumped Mott insulator at short timescales.
Acknowledgements
We thank Dieter Vollhardt for valuable discussions. M.E. acknowledges support by Studienstiftung des Deutschen Volkes. This work was supported in part by the SFB 484 of the Deutsche Forschungsgemeinschaft.
APPENDIX A: MOMENTUM SUMMATIONS
For the homogeneous and isotropic relaxation without external fields discussed in Section V, the evaluation of momentum sums is performed along the same lines as in equilibrium:36 Because the DMFT self-energy Σkσ ≡ Σσ is local, the momentum k enters the DMFT equations (9)-(11) only via the single-particle energy ǫ ̃kσσ [Eq. (8b)], i.e., Gkσ(t, t′) ≡ Gǫ ̃kσσ(t, t′) in zero field.31 The k sums in Eq. (11), (18a), and (18b) can then be reduced to integrals over a single energy variable27,50 by introducing the local density of states
ρσ(ǫ) = ∑
k
|〈i|kσ〉|2δ(ǫ − ǫ ̃kσ) (A1)
and the dispersion function
Dσ
αβ(ǫ) = 1
N
∑
k
δ(ǫ − ǫ ̃kσ)v ̃α
kσ v ̃β
kσ. (A2)
In Eq. (A1), |kσ〉 is the single particle state of the hopping matrix V ̃ijσ; for a Bravais lattice one has |〈i|kσ〉|2 =
1/N . For any function g(ǫ) we thus obtain the relations
1 N
∑
k
g(ǫ ̃kσ) =
∞
∫
−∞
dǫ ρσ(ǫ) g(ǫ) (A3)
in Eq. (11), and
1 N
∑
k
v ̃α
kσ v ̃β
kσ g(ǫ ̃kσ) =
∞
∫
−∞
dǫ Dσ
αβ(ǫ) g(ǫ) (A4)
1
ħ2N
∑
k
(∂kα∂kβ ǫ ̃kσ) g(ǫ ̃kσ) =
∞
∫
−∞
dǫ [∂ǫDσ
αβ(ǫ)] g(ǫ)
(A5)
in Eqs. (18a) and (18b). Here the last relation is proven using partial integration and the identity v ̃kσ∂ǫδ(ǫ − ǫ ̃kσ) = −∂kδ(ǫ − ǫ ̃kσ). In this work we use a semielliptic density of states,
ρ↓(ǫ) = (2/πW 2)√W 2 − ǫ2 for the mobile particles in the Falicov-Kimball model, which leads to a simple self-consistency condition for the auxiliary single-site problem.31 In the limit of infinite coordination number, this density of states is obtained for nearest-neighbor hopping on the Bethe lattice, but also for a particular choice of longer range hopping amplitudes on the hypercubic lattice.48 In the latter case one obtains48
D↓
αβ(ǫ) = δαβ
W a2
4ħ2√1 − (ǫ/W )2 ×
exp

−2 erf−1
(
ǫ
√1 − (ǫ/W )2 + W sin−1(ǫ/W ) πW/2
)2 

(A6)
for the dispersion function (A2), where a is the lattice constant. We adopt this form for the mobile particles in the Falicov-Kimball model; D↑
αβ = 0 for the immobile
species.
1 M. Imada, A. Fujimori, and Y. Tokura, Rev. Mod. Phys. 70, 1039 (1998). 2 L. Perfetti, P. A. Loukakos, M. Lisowski, U. Bovensiepen, H. Berger, S. Biermann, P. S. Cornaglia, A. Georges and
M. Wolf, Phys. Rev. Lett. 97, 067402 (2006). 3 T. Ogasawara, M. Ashida, N. Motoyama, H. Eisaki, S. Uchida, Y. Tokura, H. Ghosh, A. Shukla, S. Mazum


 9
dar, and M. Kuwata-Gonokami, Phys. Rev. Lett. 85, 2204 (1000). 4 S. Iwai, M. Ono, A. Maeda, H. Matsuzaki, H. Kishida, H. Okamoto, and Y. Tokura, Phys. Rev. Lett. 91, 057401 (2003). 5 M. Chollet, L. Guerin, N. Uchida, S. Fukaya, H. Shimoda, T. Ishikawa, K. Matsuda, T. Hasegawa, A. Ota, H. Yamochi, G. Saito, R. Tazaki, S. Adachi, and S. Koshihara, Science 307, 86 (2005). 6 H. Okamoto, H. Matsuzaki, T. Wakabayashi, T. Takahashi, and T. Hasegawa, Phys. Rev. Lett. 98, 037401 (2007). 7 C. Ku ̈bler, H. Ehrke, R. Huber, A. Halabica, R. F. Haglung, Jr. Leitenstorfer, and A. Leitenstorfer, Phys. Rev. Lett. 99, 116401 (2007). 8 A. H. Zewail, J. Phys. Chem. A 104, 5660 (2000). 9 H. Petek and S. Ogawa, Prog. in Surf. Sci. 56, 239 (1997). 10 W. M. Axt and T. Kuhn, Rep. Prog. Phys. 67, 433 (2004). 11 G. Steinmeyer, D. H. Sutter, L. Gallmann, N. Matuschek, and U. Keller, Science 286, 1507 (1999). 12 M. Hentschel, R. Kienberger, Ch. Spielmann, G. A. Reider, N. Milosevic, T. Brabec, P. Corkum, U. Heinzmann, M. Drescher, F. Krausz, Nature 414, 509 (2001). 13 P. B. Allen, Phys. Rev. Lett. 59, 1460 (1987). 14 W. S. Fann, R. Storz, H. W. K. Tom and J. Bokor, Phys. Rev. Lett. 68, 2834 (1992). 15 R. Huber, F. Tauser, A. Brodschelm, M. Bichler, G. Abstreiter, A. Leitenstorfer, Nature 414, 286 (2001). 16 L. B ́anyai, Q. T. Vu, B. Mieck, and H. Haug, Phys. Rev. Lett. 81, 882 (1998). 17 N.-H. Kwong and M. Bonitz, Phys. Rev. Lett. 84, 1768 (2000). 18 J. K. Freericks, H. R. Krishnamurthy, and Th. Pruschke, arXiv/cond-mat:0806.4781.
19 L. P. Kadanoff and G. Baym, Quantum Statistical Mechanics (W. A. Benjamin, New York, 1962). 20 L. V. Keldysh, J. Exptl. Theoret. Phys. 47, 1515 (1964) [Sov. Phys. JETP 20, 1018 (1965)]. 21 J. Rammer and H. Smith, Rev. Mod. Phys. 58, 323 (1986). 22 H. Haug and A.-P. Jauho, Quantum Kinetics in Transport and Optics of Semiconductors (Springer, Berlin, 1996).
23 A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg, Rev. Mod. Phys. 68, 13 (1996). 24 W. Metzner and D. Vollhardt, Phys. Rev. Lett. 62, 324 (1989). 25 K. Held, I. A. Nekrasov, G. Keller, V. Eyert, N. Blu ̈mer, A. K. McMahan, R. T. Scalettar, Th. Pruschke, V. I. Anisimov, and D. Vollhardt, Phys. Status solidi 243, 2599 (2006). 26 G. Kotliar and D. Vollhardt, Phys. Today 57, Vol. 3, 53 (2004). 27 J. K. Freericks, V. M. Turkowski, and V. Zlatic ́, Phys. Rev. Lett. 97, 266408 (2006); J. K. Freericks, Phys. Rev. B 77, 075109 (2008). 28 L. M. Falicov and J. C. Kimball, Phys. Rev. Lett. 22, 997 (1969). 29 J. K. Freericks and V. Zlatic ́, Rev. Mod. Phys. 75, 1333 (2003). 30 N. Tsuji, T. Oka, and H. Aoki, arXiv:0808.0379. 31 M. Eckstein and M. Kollar, Phys. Rev. Lett. 100, 120404 (2008). 32 F. B. Anders and A. Schiller, Phys. Rev. Lett. 95, 196801 (2005). 33 Ph. Werner, A. Comanac, L. de Medici, M. Troyer, and
A J. Millis, Phys. Rev. Lett. 97, 076405 (2006). 34 J. T. Kindt and C. A. Schmuttenmaer, J. Chem. Phys. 110, 8589 (1999). 35 M. J. Rozenberg, G. Kotliar, H. Kajueter, G. A. Thomas, D. H. Rapkine, J. M. Honig, and P. Metcalf, Phys. Rev. Lett. 75, 105 (1995). 36 Th. Pruschke, D. C. Cox, and M. Jarrell, Phys. Rev. B 47, 355 (1993). 37 A. Khurana, Phys. Rev. Lett. 64, 1990 (1990). 38 R. Reierls, Z. Physik 80, 763 (1933). 39 J. M. Luttinger, Phys. Rev. 84, 814 (1951). 40 M. C. Beard and C. A. Schmuttenmaer, J. Chem. Phys. 114, 2903 (2001). 41 J. M. Schins, E. Hendry, M. Bonn, and H. G. Muller, J. Chem. Phys. 127, 094308 (2007). 42 B. S. Shastry and B. Sutherland, Phys. Rev. Lett. 65, 243 (1990). 43 D. J. Scalapino, S. R. White, and S. C. Zhang, Phys. Rev. Lett. 68, 2830 (1992). 44 The current is gauge-invariant and satisfies the continuity equation for the density ρ(r) = P
iσ δ(r −Ri)c†
iσciσ, as under a gauge transformation the Hamiltonian transforms as H{A+∇Λ} = e−igH{A}eig, where g = e
ħc
R ddrΛ(r)ρ(r). 45 U. Brandt and C. Mielsch, Z. Phys. B 75, 365 (1989). 46 P. G. J. van Dongen and D. Vollhardt, Phys. Rev. Lett. 65, 1663 (1990). 47 P. G. J. van Dongen, Phys. Rev. B 45, 2267 (1992). 48 N. Blu ̈mer and P. G. J. van Dongen, In ”Concepts in Electron Correlation”, Eds.: A. C. Hewson, V. Zlatic ́, NATO Science Series, Kluwer (2003); arXiv:cond-mat/0303204. 49 M. Greiner, O. Mandel, Th. W. H ̈ansch, and I. Bloch, Nature 419, 51 (2002). 50 In the presence of external fields this is no longer true, See V. Turkowski and J. K. Freericks, Phys. Rev. B 71, 085104 (2005).
