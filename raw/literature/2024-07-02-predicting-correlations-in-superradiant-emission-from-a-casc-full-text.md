# Predicting correlations in superradiant emission from a cascaded quantum system - Full Text

> Source: http://arxiv.org/abs/2407.02154
> Collected: 2026-09-20
> Published: 2024-07-02
> Zotero parent key: 42R92HG9
> Evidence: Zotero indexed PDF text

Predicting correlations in superradiant emission from a cascaded quantum system
Felix Tebbenjohanns, Constanze Bach, and Arno Rauschenbeutel
Department of Physics, Humboldt-Universita ̈t zu Berlin, 10099 Berlin, Germany
Christopher D. Mink and Michael Fleischhauer
Department of Physics and Research Center OPTIMAS, RPTU Kaiserslautern-Landau, 67663 Kaiserslautern, Germany (Dated: July 3, 2024)
In recent experiments, a novel type of cascaded quantum system has been realized using nanofibercoupled cold atomic ensembles. This setup has enabled the study of superradiant decay of highly excited collective spin states of up to a thousand atoms, featuring unidirectional coupling mediated by the waveguide mode. The complexity arising from the large, multi-excited ensemble and the cascaded interactions between atoms makes conventional simulation methods unsuitable for predicting the correlations of superradiant emission beyond the first order. To address this challenge, we developed a new simulation technique based on the truncated Wigner approximation for spins. Our stochastic simulation tool can predict the second-order quantum coherence function, g(2), along with other correlators of the light field emitted by a strongly excited cascaded system of two-level emitters. This approach thus provides an effective and scalable method for analyzing cascaded quantum systems with large numbers of particles.
I. INTRODUCTION
Simulating the dynamics of a many-body system typically requires computational effort that scales exponentially with the number of particles due to the exponential size of the configuration space. Many problems, especially classical ones, can be efficiently approximated using various simulation techniques, such as Monte-Carlo sampling. For dynamical quantum many-body problems, however, Monte-Carlo methods can not always be applied. One significant example of such a system is an ensemble of two-level atoms with dipoles coupled through the quantized electromagnetic field [1]. In a typical experimental setup, effective two-level atoms are prepared in a well-defined initial state and probed using resonant or near-resonant light. Under certain experimental conditions, the large Hilbert space can be truncated, enabling efficient calculation of the ensemble dynamics. For instance, in the weakly driven regime where the atoms are mostly in the ground state, the ensemble behaves as a linear system of harmonic oscillators, which can be solved efficiently [2–5]. However, even in the fewexcitation regime, it remains challenging to predict correlations beyond the Gaussian approximation, such as intensity-intensity correlations of the radiated or scattered field, as a mean-field theory is not sufficient [6]. Another notable case is a very dense ensemble. As Dicke demonstrated, N two-level atoms with pairwise distances much smaller than the wavelength of the emitted light explore only a small number of N + 1 symmetric Dicke states [7, 8]. In such cases, realizable in solid-state systems [9] or, effectively, by using a waveguide or an optical cavity to mediate the coupling between the atoms, a fully inverted ensemble emits its stored energy in a superradiant burst of light [10, 11]. Interestingly, recent theoretical [12] and experimental [13] studies have revealed that superradiant bursts also occur in cascaded quantum systems [14, 15]. In
such systems, which can be realized through chiral atomwaveguide coupling [16], information flows unidirectionally through the ensemble. Unlike the Hamiltonian studied by Dicke, which is symmetric under particle exchange, the Hamiltonian of a cascaded atomic system lacks this symmetry [17–19]. Consequently, the Hilbert space cannot be truncated similarly, making the problem of a driven-dissipative cascaded quantum system beyond the weak drive limit intrinsically exponentially complex. Current state-of-the-art experiments with chirally coupled two-level systems typically involve either a small number of atoms (N ≪ 10) [20–23] or weak coupling to the waveguide [24, 25]. In the former scenario, numerical tools such as QuTiP can solve the full dynamics. In the latter case, the cascaded system is sufficiently coupled to an external reservoir, which allows for a semiclassical description that accounts for leading-order quantum effects while being numerically inexpensive even for a large number of particles. For example, some of the authors have recently introduced a model with linear computational complexity which quantitatively predicts the intensity radiated by an atomic ensemble that is weakly chirally coupled to a waveguide [13]. However, this model cannot compute higher-order correlations, even in the case of weak coupling. Notably, this includes the secondorder quantum coherence function, g(2), which has been explored in a recent experiment measuring the intensityintensity correlations of a superradiant burst of light [26]. Here, we apply another semiclassical model to a cascaded system of weakly coupled quantum emitters subject to drive and losses. This model has recently been put forward by some of the authors [27, 28] and extends the discrete truncated Wigner approximation for spins [29].
The manuscript is structured as follows. In Sec. II, we review the master equation for an ensemble of waveguidecoupled two-level atoms, focusing on the cascaded system. We discuss its relation to the dissipative Dicke model and show that a cascaded quantum system can
arXiv:2407.02154v1 [quant-ph] 2 Jul 2024


 2
Nanofiber-coupled atoms Coincidence detection
0
1
2
0 5 10 15 20 25 30
Example data and simulation
Model system
FIG. 1. Schematic of the setup. N two-level atoms are coupled to a waveguide. The coupling constant to the waveguided mode is direction-dependent, and we assume β+ ≫ β−, where β+ and β− determine the coupling to the forward and backward direction, respectively. This realizes a cascaded quantum system. We are interested in correlators of the output mode aˆout, such as the output power P (t) = ⟨ˆa†
outˆaout⟩ and Glauber’s second-order quantum correlation function G(2)(t, t) = ⟨ˆa†
out ˆa†
outˆaoutˆaout⟩. In Ref. [26], this model is implemented using the D2 transition of nanofibercoupled cold cesium atoms (excited state lifetime 30 ns). In the bottom panel, we show experimental data from Ref. [26] of P (t) (blue shaded area) and g(2)(t, t) = G(2)(t, t)/P (t)2 (black data points) for the ensemble decaying from the fully inverted state |e · · · e⟩. The blue and purple solid lines are the corresponding theoretical predictions, which we calculated using a truncated Wigner approximation approach, as laid out in this work.
not be reduced to the latter. In Sec. III, we model the system using a set of quantum Langevin equations in the Heisenberg picture, which assume a particularly simple form. In our main section IV, following a brief review of the truncated Wigner approximation for spins, we derive the stochastic differential equations describing the cascaded system. In Sec. V, we present an efficient method to compute relevant correlators of the field radiated by the cascaded system. Specifically, we calculate the time-dependent power, intensity-intensity correlation, and total angular momentum for up to one thousand atoms, which are initialized in the fully inverted state. Beyond its general significance, our model has been successfully employed for the theoretical analysis of the measurement results presented in the aforementioned experimental work [26]. In Fig. 1, we present a sample set of experimental data along with its theoretical prediction.
II. WAVEGUIDE QED: MASTER EQUATION
The system under consideration is sketched in the middle panel of Fig. 1. An ensemble of N two-level atoms with energy spacing ωeg is coupled to the modes of a single-mode waveguide. We label the atoms with indices n = 1, . . . , N in ascending order of their non-overlapping positions z1 < z2 < · · · < zN along the waveguide. As is commonly considered in the literature [30–32], we treat the interaction between the atoms and their surrounding electromagnetic field within dipole and rotating wave approximations, we trace out the light field, and we eliminate it using a Born-Markov approximation. This results in a Lindblad master equation for just the atomic degrees of freedom (we set ħ = 1) [33, 34]
d
dt ρˆ = − i[Hˆ , ρˆ] +
X
mn
Γmn
 
σˆnρˆσˆ†m − 1
2 {σˆ†mσˆn, ρˆ}
 
,
(1a)
Hˆ = −
X
n
∆nσˆ†nσˆn + 1
2
X
n
Ωnσˆ†n + Ω∗nσˆn
 
+
X
mn
Jmnσˆ†mσˆn. (1b)
Here, {A, B} = AB + BA denotes the anticommutator, σˆn = |gn⟩ ⟨en| is the spin-lowering operator of the nth atom and |gn⟩ and |en⟩ are, respectively, the ground and
excited state of the nth atom. Further, Ωn is the Rabi frequency due to a classical driving field and ∆n denotes the detuning between the atoms and the field. The radiative interactions Jmn = −i(Vmn − Vn∗m)/2 and collective
decay rates Γmn = Vmn + Vn∗m are respectively given as the hermitian and antihermitian part of the matrix Vmn. The latter is given by the matrix element [34]
Vmn ∝ d∗m · G↔(zm, zn, ωeg) · dn, (2)
where we omitted a real-valued prefactor. Here, G↔ is the electromagnetic Green’s tensor in the presence of the waveguide, and dn is the atomic dipole moment of the
nth atom. If a transversal magnetic field is applied to the atoms, their preferred direction of emission into the waveguide can be controlled by tuning their polarization. More specifically, linearly polarized light results in a bidirectional emission whereas circularly polarized light leads to unidirectional propagation of light into either direction ±z. With a closer analysis of the Green’s tensor [35–37], the matrix element Vmn can be approximated in practice by
Vmn
Γ0
=

 
 
1
2, m = n
β+eikzzmn , m > n
β−e−ikzzmn , m < n
, (3)
where kz = neffωeg/c is the wavenumber of the guided mode with effective refractive index neff, and zmn = zm − zn is the signed distance between atoms m and


 3
n. Furthermore, Γ0 is the inverse life time of the excited state of a single atom coupled to the waveguide, and β+ and β− are the coupling strengths of an atom to the forward- and backward-propagating waveguide mode, respectively. A single excited atom emits a photon into the forward-propagating waveguide mode with probability β+, into the backward-propagating waveguide mode with probability β−, and into the free space with probability 1 − β+ − β−, see Fig. 1 for a depiction. Here, we assume that the atoms do not interact through free space, thus effectively assuming a separation between atoms that is large enough. The explicit expressions for the rates are then
Jmn
Γ0
= sgn(zmn)
2i β+eikzzmn − β−e−ikzzmn   , (4a)
Γmn
Γ0
=
(
1, m = n,
β+eikzzmn + β−e−ikzzmn , m ̸= n , (4b)
with the signum function sgn(x). When β+ = β− = 0, the atoms only independently emit into the free space, whereas β+ = 1, β− = 0 indicates that every photon is emitted into the +z-direction of the waveguide. Let us now turn to the experimentally realized case [13, 26] of partial coupling to a unidirectional waveguide, i.e. β− ≈ 0 and β+ < 1. To simplify notation, we will omit the superscript + in the following, i.e. β = β+. Additionally, a resonant coherent field with amplitude α propagating through the waveguide can be included by
substituting ∆n = 0 and Ωn = 2α√βΓ0eikzzn into (1b). The complex-valued field amplitude α is scaled such that |α|2 is the photon flux through the waveguide at the input. In the following, we measure time in units of the excited state lifetime, such that Γ0 = 1. The master equation of the chiral waveguide thus reads [12, 17, 18, 38, 39]
d
dt ρˆ = −i[Hˆ0 + Hˆcasc, ρˆ] + Lcoll[ρˆ] + L0[ρˆ] (5)
with (h.c. stands for Hermitian conjugate)
Hˆ0 = pβ
X
n
ασˆ†n + h.c.  , (6a)
Hˆcasc = − i
2β
X
m
X
n<m
σˆ†mσˆn − h.c.  , (6b)
Lcoll[ρˆ] = β
X
m,n
 
σˆnρˆσˆ†m − 1
2
 σˆ†mσˆn, ρˆ
 
, (6c)
L0[ρˆ] = (1 − β)
X
n
 
σˆnρˆσˆ†n − 1
2
 σˆ†nσˆn, ρˆ
 
. (6d)
Decay to free space modes is described by the Lindblad term L0[ρˆ], while the (cascaded) interaction Hamiltonian Hˆcasc as well as the collective decay Lindblad term Lcoll[ρˆ] are responsible for the collective dynamics in this cascaded quantum system. Here, we applied the transformation e−ik0zn σˆn → σˆn, which simplifies the expressions and which is equivalent to a co-rotating frame of
reference. Note that this is only possible in the case of unidirectional coupling. The goal of this work is to find numerical predictions for time-dependent correlators of the output of the waveguide,
ˆaout = α − ipβ
X
n
σˆn, (7)
such as the field E(t) = ⟨ˆaout(t)⟩, the output flux
P (t) = ⟨aˆ†
out(t)ˆaout(t)⟩, and the second-order correlation
G(2)(t, t) = ⟨aˆ†
out(t)ˆa†
out(t)ˆaout(t)ˆaout(t)⟩. In principle, one could directly solve the master equation (5) and then derive the output correlators. In practice however, the numerical solution of Eq. (5) is not accessible for N ≫ 10 due to the exponentially large Hilbert space. Various possibilities to obtain approximate solutions have been put forward. Since for weakly driven ensembles, the dynamics only depend on the optical density of the ensemble, which is proportional to the product of the number of atoms N and the coupling constant β, one can reduce the complexity by decreasing N while increasing β. While this methods ceases to work in principle for strongly driven ensembles, it has been used with some success in a free-space system in Ref. [40]. There, the authors approximate their ensemble consisting of some thousands of atoms with finite distances by a model system of about 10 atoms with perfect particle-exchange symmetry, as envisioned by Dicke [7]. This reduces the dynamics to d
dt ρˆ = −iα[Sˆ + Sˆ†, ρˆ] + SˆρˆSˆ† − {Sˆ†Sˆ, ρˆ}/2,
with the totally symmetric lowering operator Sˆ = P
n σˆn,
such that the system stays in a small part of the Hilbert space and the above mentioned correlators can be efficiently computed. In a cascaded quantum system, however, even in the absence of free space decay, the cascaded contribution of Eq. (6b) results in the excitation of less cooperative states and thus impedes a numerically inexpensive treatment along the above mentioned lines.
III. HEISENBERG-LANGEVIN EQUATIONS
As a first approach, let us express the master equation (5) equivalently as a set of quantum Langevin equations for the individual spin operators σˆn [41]. In App. A, we show explicitly that for a cascaded quantum system these take the particularly simple and intuitive form (n = 1, . . . , N )
dσˆn
dt = − 1
2 σˆn −i(1−2σˆ†nσˆn)
 pβaˆn + p1 − βvˆinn
 
. (8)
Here, aˆn and vˆinn are field operators of, respectively, the waveguide and the free-space modes impinging on the nth atom. These fulfil the bosonic commutator relations [ˆan(t), (ˆan)†(t′)] = [vˆinn(t), (vˆinn)†(t′)] = δ(t − t′),
and [aˆn(t), (vˆinn)†(t′)] = 0. For the first atom in the chain, ˆa1(t) = α(t) is the coherent input field. Because of the unidirectional waveguide, the field operator ˆan+1(t),


 4
which appears in the quantum Langevin equation for atom n + 1 as an input mode, is identified with the output mode of atom n. This relationship is given by the input-output equation (n = 1, . . . , N ) [41]
ˆan+1 = ˆan − ipβσˆn. (9)
Equations (8) and (9) represent a complete description of the cascaded quantum system. Note that the second term of Eq. (8) is non-linear and is responsible for making the solution to these equations difficult to obtain, in general. In the limit of weak atomic excitation, one can neglect the term σˆ†nσˆn ≈ 0, resulting in linear equations of motion, which can be solved analytically [5, 42]. Here, we assume that the first atom is driven by a coherent state, effectively obtaining the optical Bloch equations for the first atom. Importantly, we cannot assume any other of the fields aˆn with n ≥ 2 to be coherent, as the field radiated by a two-level atom is famously not coherent in general. In Ref. [13], some of us presented a heuristic model, where the photonic state of the field ˆan is approximated by a classical mixture of coherent states with the complex amplitude αn(φ) = pPnc(t) + eiφpPninc(t), where the angle φ is drawn from a uniform distribution on the interval (0, 2π). This model, in which the field ˆan has both a coherent and an incoherent contribution with respective flux Pnc(t) and Pninc(t), accurately predicts loworder correlators such as the output field E(t) and flux P (t) with a linear computational complexity in the number of atoms. Importantly, this method cannot, by design, predict higher-order correlators, such as G(2)(t, t). In the following, we will therefore apply a novel approximative model of a cascaded quantum system, based on the truncated Wigner approximation, which is both computationally simple and able to predict higher-order correlators.
IV. TRUNCATED WIGNER APPROXIMATION
In this section, we give a short introduction to the truncated Wigner approximation method for spins. For more details, we refer the reader to Refs. [27, 28]. The main result of this section is given by the stochastic differential equations (22), which can be evaluated numerically. Let us consider a linear transformation from the Hilbert space spanned by N two-level atoms to the Wigner phase space [43, 44]. In particular, the elements of the Hilbert space, which are operators Aˆ, transform into their corresponding Weyl symbol WAˆ(Ω) by expanding Aˆ into an
overcomplete basis
ˆ∆(Ω) =
N
O
n=1
1 2
 1 + √3 cos θn
√3e−iφn sin θn
√3eiφn sin θn 1 − √3 cos θn
 
(10)
with Ω = (θ1, φ1, · · · θN , φN ). This yields
Aˆ =
Z
dΩ WAˆ(Ω) ˆ∆(Ω), (11)
where
dΩ =
N
Y
n=1
sin(θn)
2π dθndφn. (12)
The Weyl symbols WAˆ(Ω) are elements of the Wigner
phase space and can be represented as complex-valued functions on N spheres, i.e. Ω → WAˆ(Ω) ∈ C.
Note that the kernel ∆ˆ (Ω) is given by a superposition of the spherical harmonics Ylm(θn, φn) with l = 0, 1. Since the spherical harmonics are orthogonal, all spherical harmonics with l ≥ 2 in WAˆ(Ω) map to the zero op
erator ˆ0. Therefore, the Weyl symbol of some operator Aˆ is not uniquely defined, i.e. it possesses a gauge freedom. Specifically, one can add any spherical harmonic with l ≥ 2 to a Weyl symbol, without changing the operator it maps to [27]. The Weyl symbol corrresponding to Aˆ, which only consists of l = 0, 1 spherical harmonics is given by
WAˆ(Ω) = Tr
hAˆ∆ˆ (Ω)
i
. (13)
For example, the single-atom operators 1n, σˆn, and σˆ†nσˆn are transformed to their corresponding Weyl symbols as
W1n (Ω) = 1, (14a)
Wσˆn (Ω) =
√3
2 e−iφn sin(θn), (14b)
Wσˆ†
nσˆn (Ω) = 1 + √3 cos(θn)
2 . (14c)
Furthermore, for two single-atom operators Aˆn and Aˆm, which act on different atoms n ̸= m, we have
WAˆnAˆm (Ω) = WAˆn (Ω)WAˆm (Ω), (15)
while such a factorization is in general not true for two arbitrary operators. Let us now define the Wigner function W (Ω) as the Weyl symbol of the density operator ρˆ, such that
ρˆ =
Z
dΩ W (Ω) ˆ∆(Ω). (16)
Taking the trace of Eq. (16) and considering the normalization conditions of density matrix and kernel, Tr[ρˆ] =
Tr
h ˆ∆(Ω)
i
= 1, yields R dΩ W (Ω) = 1. From the her
miticity of ρˆ and ∆ˆ (Ω), it follows that W (Ω) ∈ R. Thus, W (Ω) is a quasi probability function. The difference to a proper probability density function (PDF) lies in the fact that W (Ω) can be negative for some values of Ω. Now, one can map the master equation (5) to the Wigner phase space, where it takes the form
∂
∂t W (Ω, t) = DW (Ω, t), (17)
with some high-order differential operator D. This is achieved by using the so called correspondence rules or


 5
Bopp operators which translate the action of an operator on the density matrix ρˆ(t) to a differential operator acting on the Wigner function W (Ω, t) [44]. Their exact form for the SU(2) spin operators was first derived in Ref. [45]. Since the transformation (11) is linear, we can find the individual differential operators for all terms on the righthand side of Eq. (5) before adding them up. So far, this transformation of the master equation is exact, and thus finding a solution W (Ω, t) is as hard as finding the solution of ρˆ(t). An approximate solution of W (Ω, t) can, however, be obtained efficiently if the following two conditions are fulfilled. First, we require that at some point in time t = 0, W (Ω, 0) is positive-semidefinite on the whole domain, such that it can be interpreted as a proper PDF. In fact, it is sufficient if W (Ω, 0) is positive after some gauge transformation. Second, we approximate the differential operator D ≈ DFP, where the operator DFP only consists of first and second derivatives with respect to θn and φn in such a way that Eq. (17) becomes a Fokker-Planck equation [46]. The explicit truncated correspondence rules for many-spin systems are derived in Refs. [27, 28]. Note that there are different truncation approximations depending on the specific application. Different from phase-space approximations to bosonic fields, where the inverse occupation number of relevant modes serves as an expansion parameter, there is not such a general smallness parameter here and a case-to-case discussion of the relevance of the neglected terms is needed. If both of these requirements are fulfilled, one can first generate a set of angles Ω according to the PDF W (Ω, 0), and then propagate these in time according to a set of coupled stochastic differential equations (SDE) of the form
dΩn = fn(Ω)dt +
N
X
m=1
Gnm(Ω)dWm(t). (18)
Here, dWm(t) are Wiener increments with dWm(t) = 0 and dWn(t)dWm(t) = δmndt, fn(Ω) are functions describing the drift of the system, and Gnm(Ω) are functions describing the diffusion. The overline denotes stochastic averaging. Both fn(Ω) and Gnm(Ω) follow from DFP of the Fokker-Planck equation. These SDEs are numerically solved to produce a large set of trajectories Ω(t). Finally, in order to find a specific atomic correlator ⟨Aˆ(t)⟩ at some time t, consider the identity
⟨Aˆ(t)⟩ = Tr[Aˆρˆ(t)] =
Z
dΩ W (Ω, t)Tr
hAˆ ˆ∆(Ω)
i
=
Z
dΩ W (Ω, t)WAˆ(Ω).
(19)
Therefore, ⟨Aˆ(t)⟩ is given by the phase space expectation value of the function WAˆ(Ω). This can be directly
evaluated on the numerically simulated sample set Ω(t), i.e.
⟨Aˆ(t)⟩ ≈ WAˆ(Ω(t)). (20)
Let us now detail these steps for our cascaded quantum system. At first, we note that any product state ρˆ =
N
n ρˆn maps to a Wigner function, which factorizes as
W (Ω) = Q
n Wn(Ωn). Using the aforementioned gauge
freedom, the states |gn⟩ and |en⟩ are represented by the positive Wigner functions
Wn(Ωn) = 1
sin(θn) δ
 
θn − arccos
  √±13
  
, (21)
where the plus (minus) sign is taken for the excited (ground) state. Positive Wigner functions corresponding to arbitrary other single-particle states characterized by the Bloch-vector (u, v, w) can be found in App. C. At t = 0, we thus generate a random sample of vectors Ω, where the components θn, φn are drawn from the PDF Wn(Ωn). The SDEs corresponding to our master equation are described in Ref. [28] and App. B and read with n = 1, . . . , N :
dθn = fn(0)dt + Re  f coll
n dt + gcoll
n dZ  , (22a)
dφn = g(n0)dWn − cot θnIm  f coll
n dt + gcoll
n dZ  . (22b)
Here, the independent atomic decay is modelled by the terms
fn(0) = (1 − β)
 
cot θn + csc θn
√3
 
, (23a)
g(n0) = p1 − β
s
1 + 2 cot θn
 
cot θn + csc θn
√3
 
, (23b)
together with N independent Wiener increments dWn. In fact, these terms follow exactly from the Lindblad term L0[ρˆ] of the master equation without approximation [27]. The collective terms of the master equation, Hˆcasc and Lcoll[ρˆ], give rise to a drift and a diffusion term. These terms have been approximated as indicated above, reading
f coll
n =β
2
 
cot θn + √3 sin θn
 
+ 2ipβeiφn Wˆan (Ω),
(24a)
gcoll
n = −pβeiφn , (24b)
together with the complex-valued Wiener increment dZ, for which dZ2 = 0, |dZ|2 = 2dt. Importantly, dZ is the same Wiener increment for all atoms n as it describes the collective coupling to a single guided mode. Because of the cascaded interaction, f coll
n only depends on Wˆan (Ω),
the Weyl-symbol of the field before the nth atom. This can be solved iteratively according to
Wˆan+1 (Ω) =
(
Wˆan (Ω) − i√βWσˆn (Ωn), n ≥ 1
α, n = 0 , (25)
which follows directly from the input-output equation (9) and substantially simplifies the calculations.


 6
Summarizing the working principle of this stochastic simulation, we first generate a random set of vectors Ω according to the PDF (21), which represents the initial product state of the atoms. These vectors are then propagated in time according to Eqs. (22) to Eq. (25). Notice that the number of computations required for accommodating one additional atom is constant, rendering the simulation time a linear function of N . Once the simulation is performed, one obtains the output field directly as
E(t) ≈ WˆaN+1 (Ω). (26)
Similarly one could then derive expressions for P (t) and G(2)(t, t). However, a naive implementation of these would lead to a sum over N 2 and N 4 terms, respectively, spoiling the linear scaling of the computation time. In the following we provide an iterative method, which allows the calculation of these (and other) correlators in linear number of computation steps.
V. HIGHER-ORDER CORRELATORS
At the core of the cascaded interaction lies the inputoutput equation (9), which relates the field operator after the nth atom to the field operator before it. Based on this equation, we find the following iterative expressions for higher-order correlators of the field after the nth atom,
aˆ†
n+1ˆan+1 = aˆ†naˆn + ipβ σˆ†naˆn − h.c. 
+ βσˆ†nσˆn,
(27a)
aˆ2†
n+1ˆa2n+1 = aˆ2n†aˆ2n + 2ipβ σˆ†nˆa†nˆa2n − h.c. 
+ 4βˆa†nσˆ†nσˆnˆan,
(27b)
ˆa†
n+1ˆa2n+1 = aˆ†naˆ2n − ipβ 2ˆa†nˆanσˆn − σˆ†nˆa2n
 
+ 2βσˆ†nσˆnaˆn,
(27c)
ˆa2n+1 = aˆ2n − 2ipβσˆnˆan, (27d)
where we made use of σˆ2n = 0 and [σˆn, ˆan] = 0 [41]. Note
that since the waveguide operator aˆn = α −i√β Pn−1
k=1 σˆk
does not act on the nth atom, Eq. (15) yields Wσˆnˆan = Wσˆn Wˆan . With this, the above expressions transform to iterative equations for the corresponding Weyl-symbols as
Wˆa†
n+1 ˆan+1 = Wˆa†
nˆan + ipβ Wσˆ∗n Wˆan − c.c. 
+ βWσˆ†
nσˆn ,
(28a)
Wˆa2†
n+1 ˆa2
n+1
= 2ipβ
 
Wσˆ∗n Wˆa†
n ˆa2n
− c.c.
 
+ Wˆa2†
n ˆa2n
+ 4βWˆa†
n ˆan Wσˆ†
nσˆn ,
(28b)
Wˆa†
n+1 ˆa2
n+1
= − ipβ
 
2Wˆa†
nˆan Wσˆn − Wσˆ∗n Wˆa2n
 
+ Wˆa†
n ˆa2n
+ 2βWσˆ†
nσˆn Wˆan ,
(28c)
Waˆ2
n+1 = Wˆa2n − 2ipβWσˆn Wˆan . (28d)
For the input field of the first atom, we have Wˆa†
1aˆ1 =
|α|2, Wˆa2†
1 ˆa21 = |α|4, Wˆa†
1ˆa21 = |α|2α, and Wˆa21 = α2.
These iterative expressions demonstrate that one can compute the Weyl-symbols Wˆa†
nˆan (Ω) and Wˆa2†
n+1 ˆa2
n+1
(Ω)
in linear time-complexity, since for each atom a constant number of computations is added. Finally, using Eq. (20), we approximate the optical flux and secondorder correlation as
Pn(t) ≈ Wˆa†
nˆan (Ω(t)), (29a)
G(n2)(t, t) ≈ Wˆa2†
n ˆa2n
(Ω(t)). (29b)
The normalized second-order coherence function can then be computed as
g(n2)(t, t) = G(n2)(t, t)
Pn(t)2 ≈
Wˆa2†
n ˆa2n
(Ω(t))
Wˆa†
nˆan (Ω(t))2 . (29c)
The above arguments can be extended to the calculations of other single-time correlators. In Fig. 2, we show some simulations which we performed using the truncated Wigner approximation for spins (TWA). In particular, we compute the output correlators P (t) in panel a), G(2)(t, t) in panel b), and g(2)(t, t) = G(2)(t, t)/P (t)2 in panel c) for an ensemble of N cascaded atoms as explained above. In panel d), we compute the total angular momentum
⟨ˆS2⟩ = ⟨Sˆx2 + Sˆy2 + Sˆz2⟩
=1
4
X
m,n
⟨σˆxmσˆnx + σˆymσˆyn + σˆzmσˆzn⟩ (30)
in analogy to the other correlators. Here, σˆnx, σˆyn, σˆzn are
the Pauli matrices associated with the nth atom. Initially, the system is fully excited and we show in blue the TWA simulations of N = 10, 100, 1000 atoms with a coupling constant of β = 1, 0.1, 0.01, such that the product βN = 10 is constant. For comparison, we show an exact calculation of the Master equation for N = 10 atoms using QuTiP (dark red dashed). It can be seen that especially the initial dynamics is well captured by the TWA. Note that while the TWA’s simulation time is linear in N , the QuTiP-simulation time is exponential in N , making it impossible to compare them to the TWA simulations with N ≫ 10. Notably, the dynamics of the cascaded quantum system is qualitatively different to that of an ensemble which remains in the symmetric Dicke states [7, 8] (light red dashed). This is most clearly visible in panel d), since ⟨Sˆ2⟩ is maximal and constant for the symmetric Dicke states with ⟨Sˆ2⟩ = (N/2)(N/2 + 1) [8]. In stark contrast, ⟨ˆS2⟩ decays in a cascaded quantum system, because the system leaves the symmetrically excited states, even in the loss-less case of β = 1. We note that, while the TWA captures the early dynamics well, it can fail at large times. There, some of the predictions become even unphysical yielding, e.g., a


 7
0
25
50
75 a) P (t)/Γ0 β = 10/N
TWA, N = 1000 TWA, N = 100 TWA, N = 10 Dicke, N = 10 QuTiP, N = 10
0
5
10 b) G(2)(t, t)/(1000Γ2
0)
0
2
4
c) g(2)(t, t)
0.00 0.25 0.50 0.75 1.00 1.25 1.50 Γ0 t
0.00
0.25
0.50
0.75
1.00
1.25 d) 〈ˆS2(t)〉/ [(N/2) (N/2 + 1)]
0.00 0.25 0.50 0.75 1.00 1.25 1.50 Γ0 t
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00 e) g(2)(t, t)/(1 − 1/N )
β = 0.01 N = 10 N = 100 N = 300 N = 500 N = 700 N = 1000
0.0 0.5 1.0 1.5 Γ0 t
0.6
0.8
1.0
1.2
1.4
A/π
tlimit
f) g(2)(t, t), β = 0.01, N = 1000
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
FIG. 2. Dynamic simulation of the correlators P (t), G(2)(t, t), g(2)(t, t), and ⟨Sˆ2(t)⟩ of a cascaded quantum system as indicated. In the left panels a) to d), we have β = 10/N , such that the product βN = 10 is fixed. The initial state is the fully inverted state |e · · · e⟩, i.e. A = π in Eq. (32). In blue, TWA predictions from N = 10, β = 1 (light blue) to N = 1000, β = 0.01 (dark blue). TWA predictions are shown as solid lines for t < tlimit and as dotted lines for t > tlimit. The time tlimit is the time when the remaining radiated energy is less than N/1000 photons, see main text. For comparison, we show the corresponding predictions of the Dicke model for N = 10 atoms (dashed light red) and the numerical solution of the full cascaded Master equation using QuTiP for β = 1, N = 10 (dashed dark red). In panel e), we compare g(2)(t, t) for different atom numbers as indicated with β = 0.01. For more than 1/β = 100 atoms (red colors), second-order quantum coherence builds up during the emission, indicated by the decrease of g(2)(t, t). For fewer than 1/β = 100 atoms (blue colors), g(2)(t, t) is constant. In panel f) we show as a color plot g(2)(t, t) for initial states parameterized by the pulse area A according to Eq. (32). In panels a) to e), the shaded grey areas indicate the (one-sigma) uncertainty due to a finite number of simulated trajectories. The number of trajectories was 278,000 for β = 0.01, 15,000 for β = 0.1, and 595,000 for β = 1. For panel f), we simulated 37,000 trajectories.
negative value of g(2)(t, t). This happens once the optical power in the waveguide is close to vacuum. In this limit, the truncation approximation for collective processes used in the TWA simulations becomes inac
curate [28]. For this reason, we define the time tlimit by
Z∞
tlimit
dt P (t) = N
1000 , (31)
i.e., the integrated flux after tlimit is equivalent to less than N/1000 photons. For t > tlimit, we expect a large


 8
systematic error on the TWA predictions, and indicate this by the dotted lines in panels a) to e) and by the black solid line in panel f). It can be seen that the unphysical predictions only happen for t > tlimit. In panels e) and f), we show TWA simulations of the second-order coherence function g(2)(t, t) for a coupling strength of β = 0.01. This is motivated by recent experimental results with these parameters [26]. In panel e), the initial state is the fully inverted state |ψ0⟩ = |e · · · e⟩,
for which the initial value of g(2)(0, 0) is 2(1 − 1/N ), reminiscent of a thermal source [47]. For a small number of atoms (N < 1/β = 100, blue lines), g(2)(t, t) = g(2)(0, 0) stays constant as a function of time, because the atoms remain in a product state. However, for a large atom number (N > 1/β = 100, red lines), second-order coherence builds up as g(2)(t, t) tends towards unity and the ensemble becomes entangled. Importantly, this effect, which was measured experimentally in Ref. [26], is a consequence of the collective emission process, for which the same threshold of N ≳ 1/β = 100 is known, see Ref. [13]. Finally, in panel f), we show g(2)(t, t) as a color plot for N = 1000 atoms and β = 0.01. Here, the initial state of the ensemble is the product state
|ψ0⟩ =
N
O
n=1
 
cos
 A
2
 
|gn⟩ − i sin
 A
2
 
|en⟩
 
, (32)
which is characterized by the Rabi-pulse area A. When
A is sufficiently different from π (|A − π| ≳ 2π/√N ≈ 0.06π), the ensemble has a sizable dipole moment, making the emitted light coherent, i.e. g(2)(0, 0) ≈ 1. Interestingly, in that regime of superradiance the TWA simulation predicts a sharp peak of g(2)(t, t) for a finite time t > 0, where the second-order coherence function can reach values much larger than 2. This peak happens well before the time tlimit, i.e., for times where we expect the TWA predictions to be accurate. This effect may be used for realizing a source of highly bunched pulses of light [48]. Let us finally remark that in our simulations we assume the idealized situation of homogeneous atom-waveguide coupling and of exact preparation of the initial state (32). For the TWA simulations in both Ref. [26] and Fig. 1, however, we extended our simulations to incorporate experimental nonidealities. Firstly, we simulated the resonant Rabi-pulse with finite pulse length T ≈ 0.13/Γ0 and pulse area A, which is sent through the waveguide [13]. Secondly, we included inhomogeneous coupling, i.e., each atom features its own coupling strength βn, which is randomly drawn from an appropriate distribution [25]. We note that the modelling of these experimental nonidealities is necessary to achieve quantitative agreement between simulation and experiment, and can be readily in
corporated into the TWA simulations. VI. CONCLUSIONS
In this case study, we applied the truncated Wigner approximation for spins to a cascaded quantum system initially prepared in a highly excited state, such as the fully inverted state |e · · · e⟩. We began by reviewing the master equation of the system and the equivalent HeisenbergLangevin equations, emphasizing that a cascaded quantum system cannot be reduced to the celebrated dissipative Dicke model, even in the limit of a lossless system. Using the TWA, we demonstrated that the cascaded nature of the system allows for stochastic simulation with a time complexity that scales linearly with the number of atoms in the ensemble. We presented simulations of various correlations beyond first order, such as the secondorder quantum coherence function g(2) of the output field, for a range of ensemble sizes and coupling strengths. To estimate the error introduced by the TWA, we compared its predictions to a full calculation of the master equation, which takes exponential time in N , for sufficiently small ensembles. This error is vanishingly small for weak atom-waveguide coupling, β ≪ 1, making this simulation method valuable for current experiments involving thousands of nanofiber-coupled atoms [26]. In the opposite limit of strong coupling, β = 1, the error remains surprisingly small, indicating that our method is applicable to a broader range of experiments. To our knowledge, this is the only computational method in the literature that can handle simulations of intensity-intensity correlations for thousands of atoms in a cascaded quantum system within a feasible timeframe. Future work will involve testing the applicability of this method for even higher-order correlators, such as three- and four-photon coincidences [49, 50]. Additionally, applying the quantum regression theorem to the TWA could enable access to multiple-time correlators like G(2)(t1, t2) with t1 ̸= t2, which is an experimentally accessible quantity. We expect TWA-based simulations to be useful for many other waveguide QED experiments with large atom numbers, where solving the master equation is infeasible.
ACKNOWLEDGMENTS
We thank Philipp Schneeweiss for insightful discussions. F.T., C.B., and A.R. gratefully acknowledge funding by the Alexander von Humboldt Foundation in the framework of the Alexander von Humboldt Professorship endowed by the Federal Ministry of Education and Research. C.M. and M.F. gratefully acknowledge financial support from the DFG through SFB TR 185, project number 277625399.


 9
Appendix A: Equivalence of Langevin equation approach and master equation.
In this appendix, we show that for our cascaded quantum system, the combination of the quantum Langevin equations (8) and the input-output equations (9) are equivalent to the master equation (5). We mainly apply the formalism put forward by Gardiner and Collett [41] to a cascaded quantum system. For the special case of two atoms coupled in a cascaded fashion, we refer also to Gardiner’s work in Ref. [14]. First, let us consider an arbitrary atomic operator Qˆn of a single atom n, which can be written as
Qˆn = c0 + c1σˆn + c2σˆ†n + c3σˆ†nσˆn (A1)
with arbitrary complex numbers c0, c1, c2, c3. From Eq. (8), we find the quantum Langevin equation of Qˆn as
d dt
Qˆn = c1
dσˆn
dt + c2
dσˆ†n
dt + c3
 
σˆ†n
dσˆn
dt + h.c.
 
=−
 
[Qˆn, σˆ†n]
 1
2 σˆn + iˆbinn
 
+
 1
2 σˆ†n − i(ˆbinn)†
 
[σˆn, Qˆn]
 
, (A2)
where ˆbinn = √βnaˆn +√1 − βnvˆinn is the input mode of the atom. Compared to the main text, in this appendix we treat the slightly more general case where the coupling stregth of the atoms can be inhomogenous, i.e. each atom has an individual coupling constant βn. Let us now consider an arbitrary atomic operator of the form Aˆ = N
n Qˆn, which we
rewrite as Aˆ = AˆnL
N Qˆn
N AˆnR, where AˆnL = N
k<n Qˆk only acts on atoms with indices k < n, while AˆnR = N
k>n Qˆk
only acts on atoms with indices k > n. Note that AˆnL and AˆnR commute with both σˆn and σˆ†n, and that the terms in
the paranthesis, σˆn/2 + iˆbinn and σˆ†n/2 − i(ˆbinn)† commute with all system operators, including AˆnL and AˆnR [41]. Using
the product rule, the quantum Langevin equation for Aˆ thus reads
d dt
Aˆ =
X
n
AˆnL
 d
dt
Qˆn
 
AˆnR =
X
n
 
[σˆ†n, Aˆ]
 1
2 σˆn + iˆbinn
 
+
 1
2 σˆ†n − i(ˆbinn)†
 
[Aˆ, σˆn]
 
, (A3)
By turning from the Heisenberg to the Schr ̈odinger picture, we find
Tr
hρˆ ̇Aˆ
i
=d
dt ⟨Aˆ⟩ = Tr
 
ρˆ d
dt
Aˆ
 
=
X
n
Tr
 
ρˆ
 
[σˆ†n, Aˆ]
 1
2 σˆn + iˆbinn
 
+
 1
2 σˆ†n − i(ˆbinn)†
 
[Aˆ, σˆn]
  
=
X
n
Tr
  
σˆnρˆσˆ†n − 1
2
 σˆ†nσˆn, ρˆ − i
 
σˆ†nˆbinnρˆ − ˆbinnρˆσˆ†n − ρˆ(ˆbinn)†σˆn + σˆnρˆ(ˆbinn)† 
 
Aˆ
 
=
X
n
Tr
  
σˆnρˆσˆ†n − 1
2
 σˆ†nσˆn, ρˆ − ipβn σˆ†nˆanρˆ − ˆanρˆσˆ†n − ρˆ(ˆan)†σˆn + σˆnρˆ(ˆan)† 
 
Aˆ
 
.
(A4)
In the last two steps, we respectively used the cyclic property of the trace and assumed that the free-space input
modes are vacuum, i.e. vˆinnρˆ = 0 and thus ˆbinnρˆ = √βnˆanρˆ. Now, we make use of the input-output equation (9) and
we expand the input field as ˆan = α − i Pn−1
k=1
√βkσˆk, where α is the coherent input field. Since Eq. (A4) is correct for arbitrary atomic operators Aˆ, we can find the master equation of the cascaded quantum system as
d
dt ρˆ =
X
n
 
σˆnρˆσˆ†n − 1
2
 σˆ†nσˆn, ρˆ − ipβn σˆ†naˆnρˆ − ˆanρˆσˆ†n − ρˆ(ˆan)†σˆn + σˆnρˆ(ˆan)† 
 
=
X
n
"
σˆnρˆσˆ†n − 1
2
 σˆ†nσˆn, ρˆ − ipβn[ασˆ†n + h.c., ρˆ] −
n−1
X
k=1
pβnβk σˆ†nσˆkρˆ − σˆkρˆσˆ†n + h.c. 
#
= − i[Hˆ0, ρˆ] + L0[ρˆ] +
X
k,n
pβkβnσˆkρˆσˆ†n −
"
1 2
X
n
βn
 σˆ†nσˆn, ρˆ +
X
k<n
pβnβkσˆ†nσˆkρˆ +
X
k>n
pβn βk ρˆσˆ †n σˆk
#
= − i[Hˆ0 + Hˆcasc, ρˆ] + L0[ρˆ] + Lcoll[ρˆ]
(A5)
with
Hˆ0 = α
X
n
pβnσˆ†n + h.c., (A6a)
Hˆcasc = − i
2
X
k<n
pβkβn σˆ†nσˆk − h.c.  , (A6b)
Lcoll[ρˆ] =
X
k,n
pβk βn
 
σˆkρˆσˆ†n − 1
2
 σˆ†nσˆk, ρˆ
 
, (A6c)
L0[ρˆ] =
X
n
(1 − βn)
 
σˆnρˆσˆ†n − 1
2
 σˆ†nσˆn, ρˆ
 
. (A6d)
For homogeneous coupling, i.e. βn = β, one regains the master equation (5) from the main text. By performing each


 10
step in reverse, one can also turn the master equation into the quantum Langevin equations. This shows that both descriptions are equivalent.
Appendix B: From master equation to stochastic differential equations
The derivation of the stochastic differential equations (SDEs) from the master equation is detailed in Ref. [28]. The rules described therein can almost directly be applied here, with one exception. There, it was assumed that the coherent coupling coefficients Jmn between atoms are real valued. In our case, the chiral atom-waveguide coupling leads to complex-valued Jmn. The modification due to the imaginary part of Jmn is as follows: in the SDEs. (49)
of Ref. [28] one needs to replace Jmn sin(φmn) by Im Jmneiφmn   and Jmn cos(φmn) by Re Jmneiφmn  . With this modification, the SDEs of the main text, Eqs. (22), follow from Ref. [28]. In the following table, we summarize the transformation of all terms in the cascaded master equation (5) to the corresponding terms in the SDE.
Term in master equation, d
dt ρˆ = Term in SDE,
  dθn dφn
 
=
−i[Hˆ0, ρˆ] = −i[
X
n
α
pβnσˆ†
n + h.c., ρˆ] −2pβn
  Im  eiφn α 
Re  eiφn α  cot θn
 
dt
L0[ρˆ] =
X
n
(1 − βn)
 
σˆnρˆσˆ†
n− 1
2
n
σˆ†
nσˆn, ρˆ
o
 

 
(1 − βn)
 
cot θn + cs√c θ3n
 
dt
√1 − βn
r
1 + 2 cot θn
 
cot θn + cs√c θ3n
 
dWn

 
Lcoll[ρˆ] =
X
m,n
ΓD
mn
 
σˆnρˆσˆ†
m− 1
2
n
σˆ†
mσˆn, ρˆ
o
 
with ΓD
mn = √βmβn
√βn 2
  √βn cot θn + √3 P
m
√βm sin(θm) cos(φmn)  dt − 2Re  eiφn dZ 
√3 cot(θn) P
m
√βm sin(θm) sin(φmn)dt + 2 cot(θn)Im  eiφn dZ 
 
−i[Hˆcasc, ρˆ] = −i
" X
m,n
Jmnσˆ†
mσˆn, ρˆ
#
with Jmn =
√βmβn
2i sgn(m − n)
−√3
X
m
sin(θm)
√βmβn
2 sgn(m − n)
  cos(φmn) cot(θn) sin(φmn)
 
dt
In Ref. [28], these rules can be found in Eqs. (16), (49), and (51). For the last rule concerning the cascadedinteraction term Hˆcasc, one needs to use the slight modification as laid out above. The SDEs in the right column can be rephrased iteratively, as shown in the main text in Eqs. (22) to (25).
Appendix C: Initial state
The discussion around Eq. (21) demonstrates a possible positive semi-definite Wigner function W (Ω) for a single atom polarized to either its ground state |g⟩ or its excited state |e⟩. In this appendix, we provide a positive semi-definite Wigner function W (Ω) for an arbitrary single-particle state
ρˆ = 1
2 (1 + uσˆx + vσˆy + wσˆz) , (C1)
where (u, v, w) = (⟨σˆx⟩ , ⟨σˆy⟩ , ⟨σˆz⟩) is the Bloch vector and σˆx, σˆy, σˆz are the Pauli matrices. Since for any product state of the ensemble, the Wigner function factorizes to W (Ω) = Q
n Wn(Ω), all such product states can be sampled.
In Ref. [27] a possible implementation for any single-particle pure state, i.e. spin-coherent state, is shown, which can be generated from a rotation of the two states |g⟩ , |e⟩. However, since the Wigner function is not uniquely defined, there are other possible implementations. Here, we present a rather simple one, which allows to simulate even mixed states, i.e. states where the length of the Bloch vector is less than one. We remind the reader, that a simple evaluation of Eq. (13) for the state ρˆ does yield a corresponding Wigner function, which however is not positive semi-definite, and can thus not serve as a PDF from which one can sample particular values of Ω.


 11
Consider the Wigner function
W (Ω) = A
sin(θ) δ(θ − θw)
 
1+ 1
A
u cos φ + v sin φ
√3 − w2
 2
(C2)
with θw = arccos(w/√3) and A = 1
2
 
1+
q
1 − 2 u2+v2
3−w2
 
. Note that A is real-valued and positive, which follows with
u2 + v2 + w2 ≤ 1 from
1 − 2 u2 + v2
3 − w2 ≥ 1 − 21 − w2
3 − w2 = 1 + w2
3 − w2 > 0.
From this it can be checked straight-forwardly, that W (Ω) ≥ 0 is positive semi-definite. Finally we have
Z
dΩ W (Ω)

 
1
Wσˆx (Ω) Wσˆy (Ω) Wσˆz (Ω)


=
Z
dΩ W (Ω)

  
1
√3 sin(θ) cos(φ)
√3 sin(θ) sin(φ)
√3 cos(θ)

  
=

 
1 u v w


 , (C3)
which shows that W (Ω) transforms to an arbitrary single-atom state ρˆ by Eq. (16).
[1] K. Hammerer, A. S. Sørensen, and E. S. Polzik, Quantum interface between light and atomic ensembles, Rev. Mod. Phys. 82, 1041 (2010). [2] M. O. Scully, E. S. Fry, C. H. R. Ooi, and K. Wo ́dkiewicz, Directed spontaneous emission from an extended ensemble of n atoms: Timing is everything, Phys. Rev. Lett. 96, 010501 (2006). [3] J. H. Eberly, Emission of one photon in an electric dipole transition of one among n atoms, Journal of Physics B: Atomic, Molecular and Optical Physics 39, S599 (2006). [4] P. W. Courteille, S. Bux, E. Lucioni, K. Lauber, T. Bienaime ́, R. Kaiser, and N. Piovella, Modification of radiation pressure due to cooperative scattering of light, The European Physical Journal D 58, 69–73 (2010). [5] T. S. do Espirito Santo, P. Weiss, A. Cipris, R. Kaiser, W. Guerin, R. Bachelard, and J. Schachenmayer, Collective excitation dynamics of a cold atom cloud, Phys. Rev. A 101, 013617 (2020). [6] K. J. Kusmierek, S. Mahmoodian, M. Cordier, J. Hinney, A. Rauschenbeutel, M. Schemmer, P. Schneeweiss, J. Volz, and K. Hammerer, Higher-order mean-field theory of chiral waveguide QED, SciPost Phys. Core 6, 041 (2023). [7] R. H. Dicke, Coherence in spontaneous radiation processes, Phys. Rev. 93, 99 (1954). [8] M. Gross and S. Haroche, Superradiance: An essay on the theory of collective spontaneous emission, Phys. Rep. 93, 301 (1982). [9] K. Cong, Q. Zhang, Y. Wang, G. T. Noe, A. Belyanin, and J. Kono, Dicke superradiance in solids [invited], J. Opt. Soc. Am. B 33, C80 (2016). [10] N. Skribanowitz, I. Herman, J. MacGillivray, and M. Feld, Observation of Dicke superradiance in optically pumped HF gas, Phys. Rev. Lett. 30, 309 (1973). [11] M. Gross, C. Fabre, P. Pillet, and S. Haroche, Observation of near-infrared Dicke superradiance on cascading transitions in atomic sodium, Phys. Rev. Lett. 36, 1035 (1976).
[12] S. Cardenas-Lopez, S. J. Masson, Z. Zager, and A. Asenjo-Garcia, Many-body superradiance and dynamical mirror symmetry breaking in waveguide qed, Phys. Rev. Lett. 131, 033605 (2023). [13] C. Liedl, F. Tebbenjohanns, C. Bach, S. Pucher, A. Rauschenbeutel, and P. Schneeweiss, Observation of superradiant bursts in a cascaded quantum system, Phys. Rev. X 14, 011020 (2024). [14] C. W. Gardiner, Driving a quantum system with the output field from another driven quantum system, Phys. Rev. Lett. 70, 2269 (1993). [15] H. J. Carmichael, Quantum trajectory theory for cascaded open systems, Phys. Rev. Lett 70, 2273 (1993). [16] P. Lodahl, S. Mahmoodian, S. Stobbe, A. Rauschenbeutel, P. Schneeweiss, J. Volz, H. Pichler, and P. Zoller, Chiral quantum optics, Nature 541, 473 (2017). [17] K. Stannigel, P. Rabl, and P. Zoller, Driven-dissipative preparation of entangled states in cascaded quantumoptical networks, New J. Phys. 14, 063014 (2012). [18] H. Pichler, T. Ramos, A. J. Daley, and P. Zoller, Quantum optics of chiral spin networks, Phys. Rev. A 91, 042116 (2015). [19] J. Kumlin, K. Kleinbeck, N. Stiesdal, H. Busche, S. Hofferberth, and H. P. B ̈uchler, Nonexponential decay of a collective excitation in an atomic ensemble coupled to a one-dimensional waveguide, Phys. Rev. A 102, 063703 (2020). [20] I. J. Luxmoore, N. A. Wasley, A. J. Ramsay, A. C. T. Thijssen, R. Oulton, M. Hugues, S. Kasture, V. G. Achanta, A. M. Fox, and M. S. Skolnick, Interfacing spins in an ingaas quantum dot to a semiconductor waveguide circuit using emitted photons, Phys. Rev. Lett. 110, 037402 (2013). [21] I. So ̈llner, S. Mahmoodian, S. L. Hansen, L. Midolo, A. Javadi, G. Kirsˇansk ̇e, T. Pregnolato, H. El-Ella, E. H. Lee, J. D. Song, and et al., Deterministic photon–emitter coupling in chiral photonic circuits, Nature Nanotechnology 10, 775–778 (2015).


 12
[22] N. Stiesdal, H. Busche, K. Kleinbeck, J. Kumlin, M. G. Hansen, H. P. B ̈uchler, and S. Hofferberth, Controlled multi-photon subtraction with cascaded rydberg superatoms as single-photon absorbers, Nat. Commun. 12, 4328 (2021). [23] C. Joshi, F. Yang, and M. Mirhosseini, Resonance fluorescence of a chiral artificial atom, Phys. Rev. X 13, 021039 (2023). [24] R. Mitsch, C. Sayrin, B. Albrecht, P. Schneeweiss, and A. Rauschenbeutel, Quantum state-controlled directional spontaneous emission of photons into a nanophotonic waveguide, Nat. Commun. 5, 5713 (2014). [25] C. Liedl, S. Pucher, F. Tebbenjohanns, P. Schneeweiss, and A. Rauschenbeutel, Collective radiation of a cascaded quantum system: From timed Dicke states to inverted ensembles, Phys. Rev. Lett. 130, 163602 (2023). [26] C. Bach, F. Tebbenjohanns, C. Liedl, P. Schneeweiss, and A. Rauschenbeutel, (work in progress). [27] C. D. Mink, D. Petrosyan, and M. Fleischhauer, Hybrid discrete-continuous truncated wigner approximation for driven, dissipative spin systems, Phys. Rev. Res. 4, 043136 (2022). [28] C. D. Mink and M. Fleischhauer, Collective radiative interactions in the discrete truncated Wigner approximation, SciPost Phys. 15, 233 (2023). [29] J. Schachenmayer, A. Pikovski, and A. M. Rey, Manybody quantum spin dynamics with monte carlo trajectories on a discrete phase space, Phys. Rev. X 5, 011022 (2015). [30] L. Allen and J. Eberly, Optical Resonance and TwoLevel Atoms, Dover Books on Physics (Dover Publications, 2012). [31] M. O. Scully and M. S. Zubairy, Quantum Optics (Cambridge University Press, 1997).
[32] H. J. Carmichael, An Open Systems Approach to Quantum Optics: Lectures Presented at the Universit ́e Libre de Bruxelles, October 28 to November 4, 1991, An Open Systems Approach to Quantum Optics: Lectures Presented at the Universite ́ Libre de Bruxelles, October 28 to November 4, 1991 No. Bd. 18 (Springer Berlin Heidelberg, 1993). [33] G. Calajo ́ and D. E. Chang, Emergence of solitons from many-body photon bound states in quantum nonlinear media, Phys. Rev. Res. 4, 023026 (2022). [34] A. S. Sheremet, M. I. Petrov, I. V. Iorsh, A. V. Poshakinskiy, and A. N. Poddubny, Waveguide quantum electrodynamics: Collective radiance and photon-photon correlations, Rev. Mod. Phys. 95, 015002 (2023). [35] D. Dzsotjan, A. S. Sørensen, and M. Fleischhauer, Quantum emitters coupled to surface plasmons of a nanowire: A green’s function approach, Phys. Rev. B 82, 075427 (2010). [36] D. Dzsotjan, J. Ka ̈stel, and M. Fleischhauer, Dipoledipole shift of quantum emitters coupled to surface plas
mons of a nanowire, Phys. Rev. B 84, 075419 (2011). [37] F. Le Kien and A. Rauschenbeutel, Nanofiber-mediated chiral radiative coupling between two atoms, Phys. Rev. A 95, 023838 (2017). [38] F. L. Kien and K. Hakuta, Cooperative enhancement of channeling of emission from atoms into a nanofiber, Phys. Rev. A 77, 013801 (2008). [39] S. Mahmoodian, G. Calajo ́, D. E. Chang, K. Hammerer, and A. S. Sørensen, Dynamics of many-body photon bound states in chiral waveguide QED, Phys. Rev. X 10, 031011 (2020). [40] G. Ferioli, S. Pancaldi, A. Glicenstein, D. Clement, A. Browaeys, and I. Ferrier-Barbut, Non-gaussian correlations in the steady-state of driven-dissipative clouds of two-level atoms (2024), arXiv:2311.13503 [quant-ph]. [41] C. W. Gardiner and M. J. Collett, Input and output in damped quantum systems: Quantum stochastic differential equations and the master equation, Phys. Rev. A 31, 3761 (1985). [42] R. Pennetta, M. Blaha, A. Johnson, D. Lechner, P. Schneeweiss, J. Volz, and A. Rauschenbeutel, Collective radiative dynamics of an ensemble of cold atoms coupled to an optical waveguide, Phys. Rev. Lett. 128, 073601 (2022). [43] C. Brif and A. Mann, Phase-space formulation of quantum mechanics and quantum-state reconstruction for physical systems with lie-group symmetries, Phys. Rev. A 59, 971 (1999). [44] A. Klimov, J. Romero, and H. Guise, Generalized su (2) covariant wigner functions and some of their applications, Journal of Physics A: Mathematical and Theoretical 50, 323001 (2017). [45] D. Zueco and I. Calvo, Bopp operators and phase-space spin dynamics: Application to rotational quantum brownian motion, Journal of Physics A: Mathematical and Theoretical 40 (2006).
[46] H. Risken, The Fokker-Planck Equation, 2nd ed. (Springer, 1996). [47] R. Loudon, The quantum theory of light, 3rd ed. (Oxford University Press, 2000). [48] F. Jahnke, C. Gies, M. Aßmann, M. Bayer, H. Leymann, A. Foerster, J. Wiersig, C. Schneider, M. Kamp, and S. Ho ̈fling, Giant photon bunching, superradiant pulse emission and excitation trapping in quantum-dot nanolasers, Nat. Commun. 7, 11540 (2016). [49] N. Tomm, S. Mahmoodian, N. O. Antoniadis, R. Schott, S. R. Valentin, A. D. Wieck, A. Ludwig, A. Javadi, and R. J. Warburton, Photon bound state dynamics from a single artificial atom, Nature Physics 19, 857–862 (2023). [50] L. Drori, B. C. Das, T. D. Zohar, G. Winer, E. Poem, A. Poddubny, and O. Firstenberg, Quantum vortices of strongly interacting photons, Science 381, 193 (2023).
