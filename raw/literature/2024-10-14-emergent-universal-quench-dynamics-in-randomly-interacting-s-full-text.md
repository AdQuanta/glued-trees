# Emergent universal quench dynamics in randomly interacting spin models - Full Text

> Source: https://www.nature.com/articles/s41567-024-02664-0
> Collected: 2026-09-20
> Published: 2024-10-14
> Zotero parent key: 7R6ZJNN7
> Evidence: Zotero indexed PDF text

Nature Physics
nature physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
Emergent universal quench dynamics in randomly interacting spin models
Yuchen Li 1,2,13, Tian-Gang Zhou 3,13, Ze Wu1,2,4,13, Pai Peng 5, Shengyu Zhang1,2,4,6, Riqiang Fu 7, Ren Zhang6,8, Wei Zheng4,6,9, Pengfei Zhang 10,11 , Hui Zhai 3,6 , Xinhua Peng 1,2,4,6 & Jiangfeng Du 1,2,4,6,12
Universal behaviour often emerges in the low-energy equilibrium physics of quantum many-body systems, despite their microscopic differences. Recently, there has been a growing interest in studying the far-from-equilibrium dynamics of quantum many-body systems. Such dynamics usually involve highly excited states beyond the traditional low-energy theory description. Whether universality can also emerge in such non-equilibrium dynamics is the subject of current research. Here, we report the experimental observation of universal dynamics by monitoring the spin depolarization process in a solid-state nuclear magnetic resonance system, described by an ensemble of randomly interacting spins. The spin depolarization can be related to temporal spin–spin correlation functions at high temperatures. We discover that these correlation functions obey a universal functional form. This finding helps us identify the dominant interacting processes in the spin depolarization dynamics that lead to universality. Our observation demonstrates the existence of universality even in non-equilibrium dynamics at high temperatures, thereby complementing the well-established universality in low-energy physics.
Universality refers to when a set of simple rules and a small number of parameters can universally describe a physical phenomenon across various systems, despite their complicated and distinct microscopic details. Numerous examples have demonstrated that universal behaviours can occur in different subfields of physics. For examples, in atomic physics, a single parameter, the s-wave scattering length, governs the low-energy scattering between two atoms1,2. In other words, regardless of the specific atomic species with different interatomic Van der Waals potentials, their low-energy interaction properties tend to be
identical as long as their s-wave scattering lengths are the same. Similarly, in condensed matter physics, systems within the quantum critical regime exhibit identical low-energy properties if they belong to the same universality class, even though their microscopic Hamiltonians can be vastly different3. However, most known examples of universal behaviours occur in low-energy physics. In contrast, far-from-equilibrium quantum dynamics always involves highly excited states. In particular, we often study a type of quench dynamics where we start with an initial state at
Received: 16 November 2023
Accepted: 12 September 2024
Published online: xx xx xxxx
Check for updates
1CAS Key Laboratory of Microscale Magnetic Resonance and School of Physical Sciences, University of Science and Technology of China, Hefei, China. 2Anhui Province Key Laboratory of Scientific Instrument Development and Application, University of Science and Technology of China, Hefei, China. 3Institute for Advanced Study, Tsinghua University, Beijing, China. 4CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Hefei, China. 5Frontiers Science Center for Nano-optoelectronics, School of Physics, Peking University, Beijing, China. 6Hefei National Laboratory, Hefei, China. 7National High Magnetic Field Laboratory, Tallahassee, FL, USA. 8School of Physics, Xi’an Jiaotong University, Xi’an, China. 9Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China. 10Department of Physics, Fudan University, Shanghai, China. 11Shanghai Qi Zhi Institute, Shanghai, China. 12Institute of Quantum Sensing and School of Physics, Zhejiang University, Hangzhou, China. 13These authors contributed equally: Yuchen Li, Tian-Gang Zhou, Ze Wu. e-mail: pengfeizhang.physics@gmail.com; hzhai@tsinghua.edu.cn; xhpeng@ustc.edu.cn


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
Thus, a nuclear spin in one molecule interacts identically with any other nuclear spin in another molecule. Furthermore, the presence of an external magnetic field causes all spins to rotate along the z ̂direction with a characteristic timescale
of 10−9 s. This rapid motion can be effectively eliminated by applying a
unitary transformation exp(−iγHB0 ∑
ia
S ̂z
iat). After taking the secular
approximation39, we obtain the Hamiltonian
Ĥ = ħ ∑
i<j,ab
Jij (−S ̂x
iaS ̂x
jb − S ̂y
iaS ̂y
jb + 2S ̂z
iaS ̂z
jb) , (3)
where Jij ≡ ( μ0/4π)(ħγ2H/2R3
ij)(1 − 3 cos2 θij) . θij represents the angle
between Rij and the z ̂ direction. Now, randomness arises because the molecules occupy lattice sites, and in a powder sample, the orientations between the lattice axes and the z ̂ direction are random. Figure 1d,e presents the probability distributions of Jij calculated from the lattice structure. It demonstrates that Jij can be regarded as random variables, with a mean and variance satisfying Jij = 0 and J2
ij = 4J2/N. N = NmNa is
the total number of spins, in which Nm is the number of molecules and Na = 16 represents the number of 1H in each molecule. We calibrated J within the range 2π[1432, 1502] Hz (Supplementary Note 2), with an average value J ̄ = (2π) 1,460 Hz, which is used later in the notation for
the dimensionless timescale J ̄t. Next, by periodically applying a radio-frequency (RF) pulse sequence, as shown in Fig. 1f (refs. 17–21,40), the Hamiltonian in
high temperature and follow its unitary evolution, which is governed by a quantum many-body Hamiltonian, such as cold atoms4,5, ions6,7, nitrogen-vacancy centres8,9 and nuclear magnetic resonance (NMR) systems10–21. Such dynamics can be attributed to temporal correlation functions at infinite temperatures4–13,15,18–30. Discovering universality in such dynamics complements established universality in low-energy equilibrium physics. So far, such examples are still rare. A recent experiment in a cold-atom system has revealed universal Kardar–Parisi–Zhang scaling for such quench dynamics in an integrable spin chain4. In contrast, in this article, we study spin models with random and all-to-all interactions using a solid-state NMR system. We reveal a couple of universal parameters in this system that can capture the main features of the quench dynamics, including both spin depolarization dynamics and multiple quantum coherence (MQC). Our findings represent substantial progress in alignment with previous work on the dynamical behaviours of NMR spin systems10–12,22,23.
To be concrete, let us consider an initial density matrix ρ̂ ∝ + εÔ,
where ε is a small parameter and Ô is a traceless operator as a perturbation to the infinite-temperature ensemble. This density matrix undergoes time evolution governed by a quantum many-body Hamiltonian Ĥ, given by ρ̂(t) = e−iĤt/ħρ̂ eiĤt/ħ. Then, by measuring the expectation
value of operator Ô at varying evolution time, we can access the
autocorrelation function as ⟨Ô(t)⟩ = Tr[Ôρ̂(t)] ∝ CC(t) , where
CC(t) = 1
cO Tr[Ô(t)Ô(0)] is the autocorrelation function with normaliza
tion constant cO such that CC(0) = 1. This autocorrelation function is defined at infinite temperatures because it equally incorporates contributions from all eigenstates, thereby reflecting the properties of the many-body Hamiltonian. During the Heisenberg evolution, the operator complexity of Ô(t)continuously increases31,32, resulting in CC(t)decaying. Therefore, the universality observed in CC(t) ultimately stems from the
universal behaviour in the complexity theory of operator growth24. Our experiments were conducted on a powder sample of adamantane (C10H16)14,19,33–35. Each adamantane molecule contains 16 hydrogen atoms (1H), and each 1H carries nuclear spin S = 1/2. There are approximately 109 to 1012 molecules contained in a single granule of the powder, which has a size of the order of micrometres (Fig. 1a). These spins interact with each other through magnetic dipolar interactions. The sample was placed in a uniform magnetic field B0 = 9.4 T along the z ̂ direction. Therefore, the Hamiltonian reads
Ĥ = −ħγHB0 ∑
ia
S ̂z
ia
+∑
(i,a)<( j,b)
μ0 ħ2 γ2H 4πr 3
ia, jb
[Ŝia ⋅ Ŝjb − 3(Ŝia ⋅ ria, jb)(Ŝjb ⋅ ria, jb)
r2
ia, jb
],
(1)
where Ŝia = (S ̂x
ia, S ̂y
ia, S ̂z
ia) are the spin operators for each 1H. i and j label molecules positioned on a face-centred cubic lattice (Fig. 1b). The indices a, b = 1, ..., 16 label the spin-1/2 within each molecule. The constraint (i, a) < (j, b) is defined as a < bwhen i = jand otherwise i < j. μ0 is the vacuum magnetic permeability and γH is the proton’s gyromagnetic ratio. ria, jb = Rij + la − lb and ria,jb = ∣ria,jb∣, where Rij denotes the displacement between the centres of two molecules. la and lb are the vectors from the centre of a molecule to each nuclear spin carrier 1H. γHB0 represents the strength of the Zeeman splitting resulting from the external magnetic field. At room temperature, each molecule undergoes rapid rotation around its centre due to thermal motion, with a characteristic timescale of 10−11 s (Fig. 1c)36. This timescale is much faster than the timescale of a dipolar interaction, which is approximately 10−3 s. By averaging the Hamiltonian over the solid angles la and lb and to the leading-order approximation, the Hamiltonian of equation (1) becomes36–38
Ĥ = ∑
i<j,ab
μ0 ħ2 γ2H 4πR3
ij
[Ŝia ⋅ Ŝjb − 3(Ŝia ⋅ Rij)(Ŝjb ⋅ Rij)
R2
ij
] − ħγHB0 ∑
ia
S ̂z
ia .
(2)
a
f
C
H
0
0.04
0.12
d
0.02
0.06
0.10
Probability
MagneticieldB0
Jij
i
j
Rotating molecule
Adamantane powder
Single-crystal structure
Jij (Hz)
Probability
t = 0, quench
h
t
B0
Prepare ρα Engineer HF
B0
t
0
X Y ×n
Y X X Y Y X –X Y– Y– Y– Y
–X –X –X
RF pulse sequence
bc
e
50 μm
0.08
–400 –200 0 200
–400 –200 0 200
Measure Oα
Fig. 1 | Experimental protocol. a, Microscopic picture of powder sample of adamantane (C10H16). The granules, whose sizes are of the order of micrometres, exhibit random orientations. b, In one granule, the adamantane molecules form a face-centred cubic lattice. The orientation of the static magnetic field B0 relative to the lattice principal axes determines the values of the secular dipolar coupling strength Jij. c, Each molecule undergoes rapid rotation around its lattice site due to thermal motion. The lattice site effectively serves as a time-averaged position for all the nuclear spins within the same molecule. 1H carries nuclear spin-1/2 and 12C carries no spin. d,e, Probability distributions of the intermolecular coupling Jij, for a given orientation of B0 (d) and for the distribution averaged over 105 random orientations denoted by arrows in the spherical surface (e). Up to the 13th neighbour couplings were incorporated in the calculation. f, Experimental protocol of the quench dynamics. First, we prepared a polarized initial density matrix ρ̂α ∝ + ε ∑ia S ̂α
ia, α = x ̂, y ̂ or z ̂. Then, the state evolved under the anisotropic random spin models engineered by the RF pulse sequence illustrated below and also used in refs. 17–21,40, after which we measured the magnetization Ôα = ∑iaS ̂α
ia.


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
equation (3) can be further engineered into a more general form according to the average Hamiltonian theory41
Ĥ = ħ ∑
i<j,ab
Jij (ξxS ̂x
iaS ̂x
jb + ξyS ̂y
iaS ̂y
jb + ξzS ̂z
iaS ̂z
jb) + ... (4)
Here ξα (α = x ̂, y,̂ z ̂) represents three anisotropic parameters that are subjected to a constraint ∑αξα = 0, which is inherited from the Hamiltonian of equation (3) and conserved under global rotations. Note that the measurement is summed over random crystalline orientations, which facilitates equation (4), a random spin model in the sense of ensemble average. The various configurations of (ξx, ξy, ξz) can be achieved by manipulating the pulse intervals (Methods and Supplementary Information). The Floquet-engineered random spin model in equation (4) is not integrable and generically prethermalizes an initial state with finite energy to quasi-equilibrium, which can be char
acterized by a canonical ensemble ρ̂pre = e−βĤ/ZZ, where ZZ is the parti
tion function and β is determined by the initial-state energy18,20,42–44. The Hamiltonian information is, thus, inherited by the prethermal state ρ̂pre, which can be learned from state tomography (Methods and Supplementary Information). Deviations from the target Hamiltonian configurations were calibrated to be within 3%. The term ... in equation
(4) represents residual terms other than S ̂α
iaS ̂α
jb, and the total weight of these terms was calibrated to be less than 20%. In the experiment, we considered three different initial density
matrices, denoted as ρ̂α ∝ + εÔα. Here, Ôα = ∑iaS ̂α
ia (α = x ̂, y ̂ or z ̂)
represents the total spin along different directions, and ε ≈ 6.4 × 10−5. We evolved the initial density matrix under the Hamiltonian of equation
(4). Subsequently, we measured ⟨Ôα(t)⟩. As discussed earlier, the result
corresponds to the normalized autocorrelation function CCα(t). The most notable finding of this experiment is the discovery of a universal functional form for CCα(t). Specifically, for α = x ̂, we introduce two quantities, namely, Wx and Γ, which are quadratic polynomials of the microscopic parameters ξα proposed in ref. 45:
Wx ≡ −ξx2 + ξy2 − 4ξyξz + ξz2, (5)
Γ ≡ ξx2 + ξy2 + ξz2. (6)
Using these two polynomials, we introduced two characteristic energy scales ħωx ≡ cħ√|Wx| J and ħλ ≡ cħ√Γ J . Here c is an o(1) con
stant. For α = y ̂ or α = z ̂, we introduced Wy and Wz through permutations asWy = −ξy2 + ξz2 − 4ξzξx + ξx2 andWz = −ξz2 + ξx2 − 4ξxξy + ξy2. ħωy and ħωz were then defined correspondingly. We found that CCα(t) can be described well by
{a cos(ωαt + φ) e−λt, if Wα > 0,
a cosh(ωαt + φ) e−λt ≈ a′ e−(λ−ωα)t, if Wα < 0, (7)
where a, a′ and φ are non-universal constants. This functional form was motivated by a quasinormal mode analysis for non-equilibrium dynamics. Quasinormal modes are collective modes with complex frequencies ωa − iλa,whichgovernthedynamicallyoscillatoryanddecayingresponse in strongly interacting systems46,47. Here, a labels different modes. In the long-time limit, we retained only the mode with the smallest λa, resulting inthefunctionalformproposedinequation(7)(see‘Large-M expansion’ in Methods and Supplementary Note 6B for a detailed derivation). Our results reveal the universal scaling functions between (ωα, λ) and the microscopic parameters in the Hamiltonian. As a consequence, this framework easily enables the establishment of a precise criterion for determining the presence of oscillatory or monotonic decay in spin relaxation dynamics. By offering a quantitative understanding, this advance marks a notable step forward in alignment with previous research10–12,22,23. However, despite the effectiveness and simplicity of equation (7), it leads to larger deviations from the experimental data around the transition point Wα = 0, where the multi-mode dynamics become more evident.
Equation (7) is confirmed by the experimental data presented in Fig. 2. We polarized the system initially in three different directions
α = x ̂, y,̂ z ̂ respectively and then measured ⟨Ôα⟩ for ξz = 0.2 and
ξx ∈ [−0.4, 0.2]. The spin depolarization dynamics of ⟨Ôα⟩ are depicted
inFig.2a–c.Wefittedthesecurvesusingthefunction A cos(Ωt + Φ) e−Λt and obtained Ω and Λ for each case. Importantly, this approach does not assume the existence of an oscillating-to-monotonic transition. Comparing with equation (7), we predicted (Ω, Λ) = (ωα, λ) when Wα > 0, whereas (Ω, Λ) = (0, λ − ωα) when Wα < 0. Given the constraint ∑αξα = 0, we have Wx = −6ξyξz, Wy = −6ξzξx and Wz = −6ξxξy. In this experiment, we fixed ξz = 0.2. Thus, when α = x ̂, we found Wx = 1.2(0.2 + ξx) > 0 for ξx > −0.2. As shown in Fig. 2a,d, the auto
correlation function oscillated when ξx > −0.2, and the frequency Ω/J ̄
scaled as c√Wx , where J ̄ is the average value of J determined experi
mentally. Figure 2g demonstrates that Λ/J ̄scaled with c√Γ for ξx > −0.2
and scaled with c(√Γ − √−Wx) for ξx < −0.2. From the fitting, we
obtained c = 0.91(7). Similarly, for α = y ̂, we have Wy = −1.2ξx > 0 for
ξx < 0, where the frequency Ω/J ̄ is fitted by c√Wy and Λ/J ̄ by c√Γ . For
ξx > 0, the frequency was zero, and Λ/J ̄ was fitted by c(√Γ − √−Wy).
The fitting gave c = 0.91(7), as shown in Fig. 2b,e,h. For α = z ̂, Wz = 6ξx(0.2 + ξx) > 0 for ξx > 0 or ξx < −0.2, where the frequency was
fitted by c√Wz and Λ/J ̄ by c√Γ . For −0.2 < ξx < 0, the frequency was
zero, and Λ/J ̄ was fitted by c(√Γ − √−Wz) . The fittings yielded c = 0.87(10), as shown in Fig. 2c,f,i. The constants c obtained from the three fittings are consistent with each other within the error bars. As a check of self-consistency, note that when Γ = −Wx, then Λ = 0, and our ansatz shows that CCx(t) does not decay at all. Observe that Γ = −Wx implies ξy = ξz, and the system restores spin rotational symmetry
along x ̂. Therefore, Ôx commutes with the Hamiltonian, and the total
spin along x ̂should not evolve in time. Similar conditions hold for α = y ̂
and z ̂. This observation is also consistent with our experimental findings, indicating that our system remained coherent and that decoherence was negligible within the experimental timescale. Furthermore, this scaling behaviour has been confirmed by exact-diagonalization calculations and approximation methods such as large-M expansion and mean-field theory (see the Methods for further details)45. Each theoretical approach has its own advantages and disadvantages. The exact-diagonalization method captures the exact non-equilibrium quantum dynamics for SU(2) spin but only for small system size N. The semiclassical method captures the non-equilibrium spin dynamics through the Landau–Lifshitz equation of the non-equilibrium dynamics for intermediate system size N. The large-M expansion captures the leading-order contribution to non-equilibrium dynamics for large system size N, which is rigorous at large M for SU(2) × SU(M) spin. Notably, the same combinations of the anisotropic parameters in the Hamiltonian enter the non-equilibrium dynamics, leading to the universal polynomial scaling of the oscillation frequency and decay rate. Figure 3a,b compares Ω and Λ obtained by these three theoretical methods with the experimental data, showing the good agreement. All the theoretical results obey the universal function form shown in equations (5)–(7) but with slightly different values of c. Below, we will discuss some physical intuitions as to why the quantities Wα and Γ emerge as universal parameters in the quench dynamics. In low-energy physics, universality arises when a specific set of diagrams becomes the most relevant and dominates the physical process under consideration, for instance, near a symmetry-breaking phase-transition point in the Landau paradigm48. In our case, we argue that the same reasoning applies to the emergence of universality in quench dynamics, albeit with a focus on the infinite-temperature autocorrelation function CCα(t).
Without loss of generality, we consider α = x ̂ and the correlation
function CCx(t) = 1
cO ∑ij,ab⟨S ̂x
ia(t)S ̂x
jb(0)⟩ . The experimental result sug
gests that the dominant contributions to ⟨S ̂x
ia(t)S ̂x
jb(0)⟩ contain a few


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
interaction channels, which can be identified by examining the terms
⟨ĤS ̂x
iaĤS ̂x
jb⟩ and ⟨Ĥ2S ̂x
iaS ̂x
jb⟩ (Supplementary Note 6E). This argument can
be justified with large-M theory and mean-field theory45, which are two of the most popular approximation schemes for studying spin models. The large-M expansion has been particularly successful for studying a randomly interacting spin model known as the Sachdev–Ye model49, which was later extended to the celebrated Sachdev–Ye–Kitaev model50–52. These two terms are illustrated by the Feynman diagrams in Fig. 3c–f, with contributions from i = j given in Fig. 3c,d, and contributions from i ≠ j given in Fig. 3e,f. Lengthy but straightforward calculations demonstrate that the contribution from diagram Fig. 3c is exactly proportional to Γ as defined in equation (6), whereas the contributions from diagrams Fig. 3d–f can be combined into Wx as defined in equation (5) (Supplementary Note 6E). That the experimental data can be captured well by these parameters reveals the underlying physics behind the dynamics, indicating that this non-equilibrium process is dominated by the interaction processes shown in Fig. 3. This universal behaviour can also be applied to similar models realized in other physical systems. As a concrete example, a similar random spin model has been realized by Rydberg atoms excited in an ultracold atomic gas, and a non-monotonic dependence of the relaxation dynamics on the anisotropic parameter ratio was observed5. This dependence also aligns with the dependency of the decay rate on the anisotropic parameters presented in this work.
For a given direction α, whether Wα > 0 or Wα < 0 not only distinguishes two types of quench dynamics for the two-point correlator but also marks the difference in higher-order correlators. We now investigate the higher-order correlation by studying MQCs53–58. The experimental protocol, as described in refs. 57,58, was used to extract the MQC spectrum by using its relation with the out-of-time-order (OTO)
correlator F(φ, t) = 1
cO Tr[e−iÔαφ Ôα(t) eiÔαφ Ôα(t)] (refs. 6,15,59–65).
F(φ, t) can be expanded as F(φ, t) = ∑m I (α)
m (t) e−imφ, where I (α)
m repre
sents the intensity of the mth-order quantum coherences in the eigen
basis of Ôα. I (α)
0 incorporates both the zero-quantum coherences and
populations (diagonal elements). In this protocol, we first evolved ρ̂α with the many-body Hamilto
nian Ĥ for a time duration t. Then, we applied a spin rotation with angle
φ given by exp(−iÔαφ). This was followed by another evolution under
the Hamiltonian −Ĥ for the same time duration t. Afterwards, we meas
ured the expectation value ⟨Ôα⟩. Like the measurement of the autocorrelation function, this protocol allowed us to measure the OTO correlator F(φ, t), as
⟨Ôα⟩ = Tr[eiĤt/ħ e−iÔαφ e−iĤt/ħ ρ̂α eiĤt/ħ eiÔαφ e−iĤt/ħ Ôα]
= Tr[e−iÔαφ ρ̂α(t) eiÔαφ Ôα(t)]
∝ F(φ, t).
(8)
Cx(t)
–0.4 –0.2 0 0.2
ξx
–0.4 –0.2 0 0.2
ξx
–0.4 –0.2 0 0.2
ξx
–0.4 –0.2 0 0.2
ξx
–0.4 –0.2 0 0.2
ξx
–0.4 –0.2 0 0.2
ξx
0
0.4
0.6
0.2
c = 0.91(7)

Λ/J
0
0.4
0.6
0.2

Λ/J
0
0.4
0.6
0.2

Λ/J
0
0.4
0.6
0.2
c = 0.91(7)
c = 0.87(10)
a dg
b
c fi
eh
0246
0
0.5
1.0
Cy(t)
0
0.5
1.0
J–t
ξx 0.20 0.15 0.10 0.05 0
–0.05 –0.10 –0.15 –0.20 –0.25 –0.30 –0.35 –0.40
× 2π
0246 J–t
× 2π
Cz(t)
0
0.5
1.0
0246 J–t
× 2π
0
0.4
0.6
0.2
0
0.4
0.6
0.2
Ω/J– Ω/J– Ω/J
Fig. 2 | Dynamical evolution of spin polarization during the quench
dynamics. a–c, Experimental measurements of CCα(t) ∝ ⟨Ôα⟩, with Ôα = ∑iaS ̂α
ia. The data were normalized by the value at t = 0. Error bars (~10−4) are incorporated within the markers of the data points to represent the 95% confidence intervals determined from read-out noise (Supplementary Fig. 2a). The initial-state density matrix was prepared as ρ̂α ∝ + εÔα. We have α = x ̂ (a), α = y ̂ (b) and α = z ̂(c). We fixed ξz = 0.2 and ∑αξα = 0 in the Hamiltonian of equation (4). The colours denote the different values of ξx, which vary from −0.4 to 0.2. The solid lines represent the fittings using a general function A cos(Ωt + Φ) exp(−Λt),
from which both Ω and Λ were obtained. d–f, Oscillation frequencies Ω/J ̄
extracted from a–c plotted as a function of ξx for α = x ̂ (d), y ̂ (e) and z ̂(f). The
solid lines denote zero when Wα < 0 and fits c√Wα for Wα > 0. g–i, Λ/J ̄ extracted from a–c plotted as a function of ξx for α = x ̂ (g), y ̂ (h) and z ̂(i). The solid lines are fits c√Γ when Wα > 0 and fits c(√Γ − √−Wα) for Wα < 0. The constant c was
obtained from simultaneous fitting of both Ω/J ̄ and Λ/J ̄. The 95% confidence intervals are given in parentheses. The error bars for data points in d–i include both the 95% confidence intervals estimated from the fitting residuals and the fluctuation due to varying the fitting range (from 15 to 41 points). This strategy reduced the fitting error caused by the ambiguity of the fitting range, thereby enhancing the reliability of the fitting results.


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
Then, by varying the rotation angle φ and time duration t and subsequently applying a Fourier transform with respect
to φ, the MQC spectrum {I (α)
m (t)} was obtained. Note that
∂2F(φ, t)/∂φ2|φ=0 = − ∑m I (α)
m (t)m2 = 1
cO Tr([Ôα(t), Ôα]2) , which is the
OTO commutator59. This connection between MQC and the OTO commutator allowed us to characterize information scrambling in the system59.
Figure 4 shows the results for I (α)
m (t) for two cases with α = z ̂.
Figure 4a depicts the case with (ξx, ξy, ξz) = (−0.125, −0.025, 0.15) and
Wz = −0.01875 < 0. In this scenario, we observed a monotonic decay of
I (z)
0 , with its weight gradually spreading into higher-order quantum
coherences. Figure 4b illustrates the case with (ξx, ξy, ξz) = (−0.1, 0.1, 0) and Wz = 0.06 > 0. In this situation, clear oscillations were observed for
both I (z)
0 (t) and I (z)
±2 (t). Besides, it seems that I (z)
0 (t) and I (z)
±2 (t)oscillated
with a frequency roughly double that of CCz(t), as indicated by the time
points when I (z)
0 (t), I (z)
±2 (t)and CCz(t)reached their initial trough or peak:
J ̄t (I)
dip/2π ≈ 1.29, J ̄t (I)
peak/2π ≈ 1.22and J ̄t (CC)
dip /2π ≈ 2.37. This is reasonable
considering that the OTO commutator Tr([Ôz(t), Ôz]2) involves a
square of Ôz(t)Ôz. This observation was verified by varying the Hamiltonian configurations (Supplementary Information), and it demonstrates the emergence of universality in a complementary aspect of quantum dynamics beyond autocorrelation functions. To conclude, we experimentally studied the far-from-equilibrium quench dynamics in randomly interacting spin models using solid-state NMR systems. The mean strength of the random interaction was the only energy scale in the Hamiltonian governing the dynamics. Hence, this problem is intrinsically a strongly interacting many-body problem that lacks small perturbation parameters. Developing a physical understanding of such a system at non-equilibrium is one of the most challenging problems. Numerical methods, like exact diagonalization, are limited to systems much smaller than the actual physical system and do not provide insightful physical intuitions. Approximation schemes, such as large-M theory, do provide helpful intuition but involve uncontrolled errors. In light of these challenges, quantitative
comparisons between theory and experiment become particularly valuable. To this end, accurate calibration of the Hamiltonian parameters and high-quality data of the quantum dynamics with inevident decoherence are required. Here, by reaching consistency between experiment, approximate theory and numerical diagonalization, we revealed a few universal parameters and uncovered dominating interacting processes for this quench dynamics, which can be generalized to similar non-equilibrium dynamics in cold atoms, nitrogen-vacancy centres and other systems.
b
cd ef
a
LM, c = 0.73(4)
ED, c = 0.97(5)
MF, c = 1.05(6)
Exp., c = 0.91(7)
0.6
0.6
0.5
0.4
0.3
0.2
0.1
0
0.2
–0.4 –0.3 –0.2 –0.1 0 0.1 0.2
0
0.4
Ω/J
ξx
–0.4 –0.3 –0.2 –0.1 0 0.1 0.2
ξx

Λ/J
Sx Sx Sx Sx Sx Sx Sx Sx
Fig. 3 | Theoretical results and diagrammatic analysis. a,b, Frequency (a) and decay rate (b) obtained from the large-M expansion (LM), exact diagonalization (ED), mean-field theory (MF) and the experimental data (Exp.), which are represented by different colours. The error bars include both the 95% confidence intervals estimated from the fitting residuals and the fluctuations due to varying the fitting range. The solid lines are simultaneous fittings of the frequency Ω/J ̄
and the decay rate Λ/J ̄ using their theoretical piecewise functions determined
from equation (7): (Ω, Λ)/J ̄ = c(√Wx, √Γ ) when Wx > 0 and
(Ω, Λ)/J ̄ = c(0, √Γ − √−Wx) when Wx < 0. The uncertainties of the constants c in
the parentheses denote the 95% confidence intervals. c–f, These four diagrams
represent contributions from ∑i,a Tr[Ĥ2S ̂x
iaS ̂x
ia](c), ∑i,a Tr[ĤS ̂x
iaĤS ̂x
ia ] (d),
∑(i,a)≠( j,b) Tr[ĤS ̂x
iaĤS ̂x
jb] (e) and ∑(i,a)≠( j,b) Tr[Ĥ2S ̂x
iaS ̂x
jb](f). In each diagram, the
dots represent spin operators. Two of these are labelled as S ̂x as they are the corresponding operators in the two-point correlator. The loops represent the trace of spin operators, whereas the arrows indicate the order of spin operator contractions. The wavy lines and their associated dots denote the vertices of random spin interactions.
ab
01 2345
–0.2
0
0.2
0.4
0.6
0.8
1.0
× 2π
Cz and I(mz)
I0
(z)
I±2
(z)
I±4
(z)
tpeak
(I)
tdip
(I)
tdip
(C)
I±6
(z)
I±8
(z)
I±10
(z)
Cz
J–t
0 1 2 3 4 × 25π
J–t
Fig. 4 | MQCs for randomly interacting spin models. a,b, MQC intensities of different orders in the eigenbasis of Ôz, denoted as I (z)
m , depicted as functions of
the evolution time J ̄t. The values of (ξx, ξy, ξz) were (−0.125, −0.025, 0.15) (a) and
(−0.1, 0.1, 0) (b). At each time J ̄t, the data were normalized by
F(φ, t)|φ=0 = ∑m I (z)
m (t) to ensure that ∑m I (z)
m (t) = 1. The different curves are for
various values of the coherence order m. The error bars (~10−4) incorporated within the markers of the data points represent the 95% confidence intervals determined from read-out noise (Supplementary Fig. 2a). The solid lines denote the cubic spline interpolations. From b, we found that I (z)
0 (t) reached its initial
trough at J ̄t (I)
dip/2π ≈ 1.29 and that I (z)
±2 (t) reached its initial peak at
J ̄t (I)
peak/2π ≈ 1.22, whereas CCz(t) reached its initial trough at J ̄t (CC)
dip /2π ≈ 2.37.
a,b, ×2π indicates that the x-axis coordinate equals the x-axis scale value multiplied by 2π.


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
Online content
Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41567-024-02664-0.
References
1. Chin, C., Grimm, R., Julienne, P. & Tiesinga, E. Feshbach resonances in ultracold gases. Rev. Mod. Phys. 62, 1225 (2010). 2. Pethick, C. J. & Smith, H. Bose-Einstein Condensation in Dilute Gases (Cambridge Univ. Press, 2008). 3. Sachdev, S. Quantum Phase Transitions (Cambridge Univ. Press, 2011). 4. Wei, D. et al. Quantum gas microscopy of Kardar-Parisi-Zhang superdiffusion. Science 376, 716–720 (2022). 5. Geier, S. et al. Floquet Hamiltonian engineering of an isolated many-body spin system. Science 374, 1149 (2021). 6. Gärttner, M. et al. Measuring out-of-time-order correlations and multiple quantum spectra in a trapped-ion quantum magnet. Nat. Phys. 13, 781–786 (2017). 7. Joshi, M. K. et al. Observing emergent hydrodynamics in a long-range quantum magnet. Science 376, 720–724 (2022). 8. Zu, C. et al. Emergent hydrodynamics in a strongly interacting dipolar spin ensemble. Nature 597, 45–50 (2021). 9. Martin, L. S. et al. Controlling local thermalization dynamics in a Floquet-engineered dipolar ensemble. Phys. Rev. Lett. 130, 210403 (2023). 10. Morgan, S. W., Fine, B. V. & Saam, B. Universal long-time behavior of nuclear spin decays in a solid. Phys. Rev. Lett. 101, 067601 (2008). 11. Sorte, E. G., Fine, B. V. & Saam, B. Long-time behavior of nuclear spin decays in various lattices. Phys. Rev. B 83, 064302 (2011). 12. Meier, B., Kohlrautz, J. & Haase, J. Eigenmodes in the long-time behavior of a coupled spin system measured with nuclear magnetic resonance. Phys. Rev. Lett. 108, 177602 (2012). 13. Ramanathan, C., Cappellaro, P., Viola, L. & Cory, D. G. Experimental characterization of coherent magnetization transport in a one-dimensional spin system. New J. Phys. 13, 103015 (2011). 14. Álvarez, G. A., Suter, D. & Kaiser, R. Localization-delocalization transition in the dynamics of dipolar-coupled nuclear spins. Science 349, 846–848 (2015). 15. Li, J. et al. Measuring out-of-time-order correlators on a nuclear magnetic resonance quantum simulator. Phys. Rev. X 7, 031011 (2017). 16. Rovny, J., Blum, R. L. & Barrett, S. E. Observation of discrete-time-crystal signatures in an ordered dipolar many-body system. Phys. Rev. Lett. 120, 180603 (2018). 17. Wei, K. X., Ramanathan, C. & Cappellaro, P. Exploring localization in nuclear spin chains. Phys. Rev. Lett. 120, 070501 (2018). 18. Wei, K. X. et al. Emergent prethermalization signatures in out-of-time ordered correlations. Phys. Rev. Lett. 123, 090605 (2019). 19. Sánchez, C. M. et al. Perturbation independent decay of the Loschmidt echo in a many-body system. Phys. Rev. Lett. 124, 030601 (2020). 20. Peng, P., Yin, C., Huang, X., Ramanathan, C. & Cappellaro, P. Floquet prethermalization in dipolar spin chains. Nat. Phys. 17, 444–447 (2021). 21. Peng, P., Ye, B., Yao, N. Y. & Cappellaro, P. Exploiting disorder to probe spin and energy hydrodynamics. Nat. Phys. 19, 1027–1032 (2023). 22. Fine, B. V. Long-time relaxation on spin lattice as a manifestation of chaotic dynamics. Int. J. Mod. Phys. B 18, 1119–1159 (2004).
23. Fine, B. V. Long-time behavior of spin echo. Phys. Rev. Lett. 94, 247601 (2005). 24. Zhang, R. & Zhai, H. Universal hypothesis of autocorrelation function from Krylov complexity. Quantum Front. 3, 7 (2024). 25. Ljubotina, M., Žnidarič, M. & Prosen, T. Spin diffusion from an inhomogeneous quench in an integrable system. Nat. Commun. 8, 16117 (2017). 26. Ljubotina, M., Žnidarič, M. & Prosen, T. Kardar-Parisi-Zhang physics in the quantum Heisenberg magnet. Phys. Rev. Lett. 122, 210602 (2019). 27. Gopalakrishnan, S. & Vasseur, R. Kinetic theory of spin diffusion and superdiffusion in XXZ spin chains. Phys. Rev. Lett. 122, 127202 (2019). 28. Gopalakrishnan, S., Vasseur, R. & Ware, B. Anomalous relaxation and the high-temperature structure factor of XXZ spin chains. Proc. Natl Acad. Sci. USA. 116, 16250–16255 (2019). 29. Dupont, M. & Moore, J. E. Universal spin dynamics in infinite-temperature one-dimensional quantum magnets. Phys. Rev. B 101, 121106 (2020). 30. Ljubotina, M., Desaules, J.-Y., Serbyn, M. & Papić, Z. Superdiffusive energy transport in kinetically constrained models. Phys. Rev. X 13, 011033 (2023). 31. Roberts, D. A., Stanford, D. & Susskind, L. Localized shocks. J. High Energy Phys. 2015, 51 (2015).
32. Parker, D. E., Cao, X., Avdoshkin, A., Scaffidi, T. & Altman, E. A universal operator growth hypothesis. Phys. Rev. X 9, 041017 (2019). 33. Rufeil-Fiori, E., Sánchez, C. M., Oliva, F. Y., Pastawski, H. M. & Levstein, P. R. Effective one-body dynamics in multiple-quantum NMR experiments. Phys. Rev. A 79, 032324 (2009). 34. Sánchez, C. M., Acosta, R. H., Levstein, P. R., Pastawski, H. M. & Chattah, A. K. Clustering and decoherence of correlated spins under double quantum dynamics. Phys. Rev. A 90, 042122 (2014). 35. Álvarez, G. A. & Suter, D. NMR quantum simulation of localization effects induced by decoherence. Phys. Rev. Lett. 104, 230403 (2010). 36. Resing, H. A. NMR relaxation in adamantane and hexamethylenetetramine: diffusion and rotation. Mol. Cryst. Liq. Cryst. 9, 101–132 (1969). 37. McCall, D. W. & Douglass, D. C. Nuclear magnetic resonance in solid adamantane. J. Chem. Phys. 33, 777–778 (1960). 38. Smith, G. W. On the calculation of second moments of nuclear magnetic resonance lines for large molecules. Adamantane molecule. J. Chem. Phys. 35, 1134–1135 (1961).
39. Abragam, A. The Principles of Nuclear Magnetism (Oxford Univ. Press, 1961). 40. Suter, D., Liu, S. B., Baum, J. & Pines, A. Multiple quantum NMR excitation with a one-quantum Hamiltonian. Chem. Phys. 114, 103–109 (1987). 41. Haeberlen, U. & Waugh, J. S. Coherent averaging effects in magnetic resonance. Phys. Rev. 175, 453 (1968). 42. Deutsch, J. M. Eigenstate thermalization hypothesis. Rep. Prog. Phys. 81, 082001 (2018). 43. Mori, T., Kuwahara, T. & Saito, K. Rigorous bound on energy absorption and generic relaxation in periodically driven quantum systems. Phys. Rev. Lett. 116, 120401 (2016). 44. Abanin, D. A., De Roeck, W., Ho, W. W. & Huveneers, F. Effective Hamiltonians, prethermalization, and slow energy absorption in periodically driven many-body systems. Phys. Rev. B 95, 014112 (2017). 45. Zhou, T. G., Zheng, W. & Zhang, P. Universal aspect of relaxation dynamics in random spin models. Preprint at https://doi.org/ 10.48550/arXiv.2305.02359 (2023). 46. Konoplya, R. A. & Zhidenko, A. Quasinormal modes of black holes: from astrophysics to string theory. Rev. Mod. Phys. 83, 793–836 (2011).


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
47. Witczak-Krempa, W. & Sachdev, S. Quasinormal modes of quantum criticality. Phys. Rev. B 86, 235115 (2012). 48. Shankar, R. Renormalization-group approach to interacting fermions. Rev. Mod. Phys. 66, 129 (1994). 49. Sachdev, S. & Ye, J. Gapless spin-fluid ground state in a random quantum Heisenberg magnet. Phys. Rev. Lett. 70, 3339 (1993). 50. Kitaev, A. A simple model of quantum holography (part 2). Talk at the Kavli Institute for Theoretical Physics, University of California, Santa Barbara https://online.kitp.ucsb.edu/online/entangled15/ kitaev2/ (2015). 51. Maldacena, J. & Stanford, D. Remarks on the Sachdev-Ye-Kitaev model. Phys. Rev. D 94, 106002 (2016). 52. Chowdhury, D., Georges, A., Parcollet, O. & Sachdev, S. Sachdev-Ye-Kitaev models and beyond: window into non-Fermi liquids. Rev. Mod. Phys. 94, 035004 (2022). 53. Aue, W. P., Bartholdi, E. & Ernst, R. R. Two dimensional spectroscopy. Application to nuclear magnetic resonance. J. Chem. Phys. 64, 2229–2246 (1976). 54. Wokaun, A. & Ernst, R. R. Selective detection of multiple quantum transitions in NMR by two-dimensional spectroscopy. Chem. Phys. Lett. 52, 407–412 (1977). 55. Drobny, G., Pines, A., Sinton, S., Weitekamp, D. P. & Wemmer, D. Fourier transform multiple quantum nuclear magnetic resonance. Faraday Symp. Chem. Soc. 13, 49 (1978).
56. Bodenhausen, G. Multiple-quantum NMR. Prog. Nucl. Magn. Reson. Spectrosc. 14, 137–173 (1980).
57. Yen, Y. & Pines, A. Multiple quantum NMR in solids. J. Chem. Phys. 78, 3579–3582 (1983). 58. Baum, J., Munowitz, M., Garroway, A. N. & Pines, A. Multiple quantum dynamics in solid state NMR. J. Chem. Phys. 83, 2015–2025 (1985).
59. Gärttner, M., Hauke, P. & Rey, A. M. Relating out-of-time-order correlations to entanglement via multiple-quantum coherences. Phys. Rev. Lett. 120, 040402 (2018).
60. Larkin, A. I. & Ovchinnikov, Y. N. Quasiclassical method in the theory of superconductivity. Sov. Phys. JETP 28, 1200–1205 (1969). 61. Shenker, S. H. & Stanford, D. Multiple shocks. J. High Energy Phys. 2014, 46 (2014). 62. Kitaev, A. Hidden correlations in the Hawking radiation and thermal noise. Talk given at the Fundamental Physics Prize
Symposium. Kavli Institute for Theoretical Physics https://online. kitp.ucsb.edu/online/joint98/kitaev/ (2014). 63. Maldacena, J., Shenker, S. H. & Stanford, D. A bound on chaos. J. High Energy Phys. 2016, 106 (2016).
64. Hosur, P., Qi, X.-L., Roberts, D. A. & Yoshida, B. Chaos in quantum channels. J. High Energy Phys. 2016, 4 (2016). 65. Landsman, K. A. et al. Verified quantum information scrambling. Nature 567, 61 (2019).
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.
© The Author(s), under exclusive licence to Springer Nature Limited 2024


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
Methods
Hamiltonian engineering
By periodically applying the RF pulse sequence to the natural dipolar Hamiltonian, we could engineer the desired form of the anisotropic Heisenberg models of equation (4) as an effective time-independent Hamiltonian by the average Hamiltonian theory41. The basic building block of the RF pulse train is an eight-pulse sequence, which was initially introduced to study MQCs40. Explicitly, the eight-pulse sequence is represented as follows:
(τz, x, τy, y, 2τx, y, τy, x, 2τz, x, τy, y, 2τx, y, τy, x, τz),
where x and y denote the RF pulses that induce collective π/2 rotations along the x̂and y ̂directions, respectively. By adjusting the pulse intervals τα such that τα = [1 + ξα] τ, we can realize different configurations of the anisotropic parameters (ξx, ξy, ξz) to the leading order of the Magnus expansion66.
Hamiltonian calibration
We calibrated the actually realized anisotropic parameters (ξx′ , ξy′, ξz′)
and the weight of residual terms other than Ŝα
iaS ̂α
jbin the effective Floquet
Hamiltonian ĤF. We employed the Floquet prethermalization
hypothesis43,44, which assumes that the system attains a quasi-stationary state ρ̂pre, approximately characterized by a canonical ensemble associ
ated with the effective Hamiltonian ĤF before being heated to infinite temperature. We then have
ρ̂pre ≈ e−βeffĤF
Tr (e−βeffĤF ) ∝ − βeffĤF, (9)
where βeff represents the effective inverse temperature, which is determined by the initial state ρ̂0 through energy conservation
Tr( ρ̂0ĤF) = Tr( ρ̂preĤF). The Floquet prethermalization has been experi
mentally demonstrated in spin chains with dipolar interactions18,20. As elaborated in the Supplementary Information, we initially prepared states with finite inverse spin temperatures and then allowed them to prethermalize under the Ĥ of equation (4) with various aniso
tropic configurations for a time period of J ̄t ≥ 14π. In addition, we
prepared dipolar-ordered states67,68 as a reference state using the Jeener–Broekaert method67. The traceless components of the density matrix of these states are given by
δρ̂xD ∝ ∑
i≠j,ab
Jij (−S ̂y
iaS ̂y
jb − S ̂z
iaS ̂z
jb + 2S ̂x
iaS ̂x
jb) , (10)
and the other two dipolar-ordered states δρ̂yDand δρ̂zDcan be determined through cyclic permutations. In the experiment, we measured the inner products between the prethermal state and each of the dipolar-ordered states. These inner products are proportional to the anisotropic parameters:
Tr ( ρ̂preδρ̂xD) ∝ (2ξ′x − ξ′y − ξ′z) ∑
i≠j,ab
J2
ij ∝ ξ′x. (11)
Similarly, we found that Tr( ρ̂preδρ̂yD) ∝ ξ′y and Tr( ρ̂preδρ̂zD) ∝ ξ′z . This determines the actual anisotropic parameters (ξ′x, ξ′y, ξ′z). The discrepan
cies between these parameters and their target values (ξx, ξy, ξz) are quantified by ∆ ≡ ||ξ′ − ξ|| / ||ξ||. Throughout all the realized configurations, the values of Δ were calibrated to be within 3% (Supplementary Note 4). The weight of the residual terms, denoted as ⋯in the overall effec
tive Hamiltonian of equation (4), is defined by ε ≡ √Tr(⋯2)/ Tr(Ĥ2). It primarily leverages the orthogonal relationships between the residual term in the prethermal states ρ̂pre and the dipolar-ordered states δρ̂αD and incorporates more inner product measurements. The values of ε were determined to be less than 20% across all the realized configurations (Supplementary Note 4).
Exact diagonalization
In the exact-diagonalization calculations, we were restricted to a simplified model consisting of a single spin-1/2 on each molecule with system size up to N = 8. The Hamiltonian is
ĤED = ∑
i<j
Jij (ξxS ̂x
i S ̂x
j + ξyS ̂y
i S ̂y
j + ξzS ̂z
i S ̂z
j ) , (12)
where Jij is modelled as a random variable obeying a normal distribution Jij ∼ NN[0, (2J/√N)2]. For each disorder realization of Jij, we prepared the initial state as a thermal density matrix, denoted as ρ̂ ∝ exp(−β(ĤED + δ ̂H)), where β = ħ/(kBT) denotes the inverse tempera
ture. We introduced an external polarization field δ ̂H = −g ∑i Ŝx
i . We
fixed βJ = 0.2 and g/J = 2, as explained in ‘Parameters in the numerical simulations’. The system was then allowed to evolve under the Hamiltonian of equation (12), and the result was averaged over 103 random realizations.
Large-M expansion
We transformed the randomly interacting spin model of equation (4) into a theory of randomly interacting fermions by adopting the Abrikosov fermion representation. In this representation, the spin operators are
expressed as S ̂α
ia = 1
2 ∑ss′ c ̂†
ia,s(σ α)ss′ cîa,s′ ( s, s′ =↑, ↓), limited to the single
occupation subspace. Our main interest lies in the spin polarization dynamics, which can be expressed as ⟨Ôx(t)⟩ = −iN(G≷
↑↓(t, t) + G≷
↓↑(t, t))/2.
Here the real-time Green’s functions are defined as G>
ss′ (t1, t2) ≡ −i⟨cia,s(t1)c†
ia,s′ (t2)⟩ and G<
ss′ (t1, t2) ≡ i⟨c†
ia,s′ (t2)cia,s(t1)⟩ . The
evolution of these Green’s functions can be described by a set of classical equations, commonly known as the Kadanoff–Baym equation:
i∂t1 G≷ = ΣR ∘ G≷ + Σ≷ ∘ GA,
−i∂t2 G≷ = GR ∘ Σ≷ + G≷ ∘ ΣA, (13)
where GR/A are the retarded and advanced Green’s functions. Σ≷ and ΣR/A represent the real-time self-energies, which satisfy ΣR/A = ±Θ (±t12) (Σ> − Σ<) . To make further theoretical advances, an SU(M) × SU(2) generalization was introduced, which is like the approach used in refs. 45,69. By taking both the large-N and the large-M limit, melon diagrams play a dominant role in the self-energies, as in the Sachdev–Ye–Kitaev model. This leads to
Σ≷(t1, t2) = J2
4∑
α,α′
ξαξα′ σ α′ G≷(t1, t2)σ α Tr [σ α′ G≷(t1, t2)σ αG≶(t2, t1)] . (14)
Numerically, we prepared the system in an initial state described by a thermal ensemble at βJ = 0.2 with a polarization field g/J = 2. The corresponding initial Green’s functions were obtained through iterations. Subsequently, we evolved G≷ by combining equation (13) and equation (14) to determine ⟨Ôx(t)⟩. Besides, by conducting a quasinormal mode analysis, one can analytically derive the long-time spin relaxation dynamics of equation (7) within the large-M approximation45. This calculation is elaborated in the Supplementary Information.
Mean-field theory
Another theoretical scheme for analysing randomly interacting spin models is the mean-field theory. Here, we introduce the average polarization on each molecule as M̂α
i= 1
Na ∑a S ̂α
ia. Due to the statistical averaging, we expected the fluctuation of M̂α
i to be small, allowing us to approximate it as a classical vector Mα
i . The Heisenberg equation for
M̂ then becomes
dMα
i
dt = Na ∑
j,βγ
Jij εαβγ ξβ Mβ
j Mγ
i . (15)


 Nature Physics
Artic e https://doi.org/10.1038/s41567-024-02664-0
In the numerical simulation, we investigated a system with 2 × 103 molecules. The initial configuration of Mα
i was randomly generated using an independent Gaussian distribution, with mean Mi = ( βg
4 , 0, 0), βg = 0.4 and variance (δMα
i )2 = 1/(4Na). Subsequently, we evolved Mα
i
according to equation (15) for each random realization and computed
⟨Ôα⟩ = Na ∑i Mα
i . The final result was then averaged over 20 independent simulations.
Parameters in the numerical simulations
The NMR experiment was conducted at room temperature, necessitating the conditions βJ ≪ 1 and βg ≪ 1. Additionally, the external magnetic field strongly polarized the state, so that the initial state could be
approximated by ρ̂ ∝ exp (−βĤdip + βg ∑ia S ̂α
ia) ≈ ̂ + βg ∑ia S ̂α
ia . This required that the magnitude of the external field must be substantially larger than the characteristic strength of the dipolar interaction Ĥdip (equation (3)), that is, g/J ≫ 1. All the parameters in the numerical simulations satisfied these conditions. In the Supplementary Information, we demonstrate that a moderate change of parameters yields qualitatively similar results. In particular, the oscillation frequencies and decay rates remain independent of β and g.
Data availability
Source data are provided with this paper. The data used in this research are also available at https://github.com/tgzhou98/QuenchRandom-Spin and https://github.com/lyuchen96/QuenchRandom-Spin. The data for Fig. 3 are available at the first site, whereas the second site provides the data for Figs. 1, 2 and 4 and for the Supplementary Information. Further data are available from the corresponding authors upon reasonable request.
Code availability
The code used to produce Fig. 3 is available at https://github.com/ tgzhou98/Quench-Random-Spin, which contains three packages of numerical simulations and one package for fitting and the corresponding error bar analysis. The code used for Figs. 1, 2 and 4 and for the Supplementary Information is available at https://github.com/lyuchen96/ Quench-Random-Spin.
References
66. Magnus, W. On the exponential solution of differential equations for a linear operator. Commun. Pure Appl. Math. 7, 649–673 (1954). 67. Jeener, J. & Broekaert, P. Nuclear magnetic resonance in solids: thermodynamic effects of a pair of RF pulses. Phys. Rev. 157, 232–240 (1967).
68. Cho, H., Cory, D. G. & Ramanathan, C. Spin counting experiments in the dipolar-ordered state. J. Chem. Phys. 118, 3686–3691 (2003). 69. Zhou, T. G., Pan, L., Chen, Y., Zhang, P. & Zhai, H. Disconnecting a traversable wormhole: universal quench dynamics in random spin models. Phys. Rev. Res. 3, L022024 (2021).
Acknowledgements
We thank K. Gong, Y. Wang and R. Gao for experimental assistance and D. Suter for helpful discussions. This work is supported by the Innovation Program for Quantum Science and Technology (Grant Nos. 2021ZD0303205 to X.H.P., 2021ZD0302005 to H.Z. and 2021ZD0302004 to W.Z.), the National Natural Science Foundation of China (Grant Nos. 12261160569, 12150014 and 11927811 to X.H.P., GG2030007011 and GG2030040453 to W.Z., 12374477 to P.Z. and 12174300 to R.Z.), a Tang Scholarship (R.Z.), the Beijing Outstanding Young Scholar Program (H.Z.) and the XPLORER Prize (H.Z. and X.H.P.). R.F. acknowledges support from the National High Magnetic Field Lab, which is supported by the National Science Foundation (Grant Nos. DMR-1644779 and 2128556) and the State of Florida. This work was partially carried out at the Instruments Center for Physical Science, University of Science and Technology of China.
Author contributions
Y.L., Z.W. and X.P. designed the experimental protocol. Y.L. performed the measurements. P.P., S.Z. and R.F. assisted with the experiments and numerical simulations. T.G.Z., R.Z., W.Z., P.Z. and H.Z. developed the theory. H.Z., X.P. and J.D. supervised the project. All authors contributed to analysing the data, discussing the results and writing the manuscript.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41567-024-02664-0.
Correspondence and requests for materials should be addressed to Pengfei Zhang, Hui Zhai or Xinhua Peng.
Peer review information Nature Physics thanks the anonymous reviewers for their contribution to the peer review of this work.
Reprints and permissions information is available at www.nature.com/reprints.
