# Stochastic modeling of superfluorescence in compact systems - Full Text

> Source: http://arxiv.org/abs/2312.06537
> Collected: 2026-09-20
> Published: 2024-09-04
> Zotero parent key: JRRS7TZE
> Evidence: Zotero indexed PDF text

Stochastic modeling of superfluorescence in compact systems
Stasis Chuchurka†∗ and Vladislav Sukharnikov†
Deutsches Elektronen-Synchrotron DESY, 22603 Hamburg, Germany Department of Physics, Universita ̈t Hamburg, 22761 Hamburg, Germany
Andrei Benediktovitch
Deutsches Elektronen-Synchrotron DESY, 22603 Hamburg, Germany
Nina Rohringer‡
Deutsches Elektronen-Synchrotron DESY, 22603 Hamburg, Germany Department of Physics, Universita ̈t Hamburg, 22761 Hamburg, Germany (Dated: September 5, 2024)
We propose an approach based on stochastic differential equations to describe superfluorescence in compact ensembles of multi-level emitters in the presence of various incoherent processes. This approach has a numerical complexity that does not depend on the number of emitters. The stochastic differential equations are derived directly from the quantum master equation. In this study, we present a series of numerical examples, comparing our solution to exact calculations and discussing the limits of applicability. For many relevant cases, the proposed stochastic differential equations provide accurate results and correctly capture quantum many-body correlation effects.
I. INTRODUCTION
Superfluorescence is a notable phenomenon in quantum optics, that is observed when incoherently excited atoms collectively emit radiation in the form of a highly energetic and short burst of light. The initially produced spontaneous emission couples the dipole moments of atoms, allowing them to synchronize the emission of photons. The phenomenon of superfluorescence traces its origins back to the seminal work of Dicke [1]. Since then, it has garnered significant theoretical interest [2–7] and has been a source of inspiration for numerous experimental studies. These studies include early demonstrations in gases [8–11] and solids [12], as well as more recent demonstrations in quantum dots [13], nitrogenvacancy centers [14], cold atoms [15, 16], and nuclei [17]. Earlier investigations spanned from optical [11] and infrared [18, 19] to millimeter [20, 21] wavelengths. The recent emergence of X-ray free-electron lasers has provided exciting opportunities to observe the phenomenon of superfluorescence in the X-ray domain [22–26]. Nevertheless, these new opportunities bring additional complications to the theoretical description of the underlying phenomena. For example, X-ray transitions often undergo significant decoherence in the form of the Auger-Meitner effect, which can intensely compete with the excitation process and substantially disrupt the synchronization of atomic dipoles. Therefore, the theoretical models that previously proved efficient need thorough revision. In Ref. [1], Dicke introduced a minimal model necessary for observing collective spontaneous emission. This
∗ stasis.chuchurka@desy.de † These authors contributed equally to this work. ‡ nina.rohringer@desy.de
model comprises a system of identical two-level quantum emitters interacting with a quantized electromagnetic field assumed to be uniform across the ensemble. Being indistinguishable, N emitters evolve through a ladder of (N +1) collective many-body states, synchronizing the radiation phases of the different emitters. This basic model can be generalized to include multi-level emitters [27] and incoherent processes [28, 29], which only partially diminish the collective nature of the interaction with the field. Providing invaluable insight from a theoretical point of view, these approaches, however, do not suggest an efficient strategy for numerical studies. Decomposing the quantum states in the basis set that accounts for the permutation symmetry results in a system of equations, the number of which grows polynomially with the number of atoms N . Although the resulting polynomial complexity allows treating a moderately large number of atoms (N ≲ 100) with a relatively acceptable computational effort [28], the problems involving a realistically large number of atoms still remain challenging. This numerical complexity has been acknowledged previously, as experiments often involve macroscopic numbers of atoms N ≫ 1. As outlined in Ref. [4], when the system is instantaneously excited, and there are no competing incoherent processes, quantum effects dominate in the early stages of superfluorescence. Subsequently, the evolution becomes classical, and we can effectively simulate the dynamics of quantum emitters by solving Bloch equations with statistically distributed initial dipole moments. By considering multiple regions with independently distributed initial conditions, we can conduct a numerical analysis of macroscopic distributed systems. However, if the initial incoherent excitation triggering superfluorescence is not instantaneous, and the quantum stage is further complicated by various incoherent processes, random initial conditions are no longer applicable. In such cases, several phenomenological strategies have
arXiv:2312.06537v2 [quant-ph] 4 Sep 2024


 2
been proposed. For instance, in Refs. [30–33], random initial conditions have been replaced by phenomenological noise terms acting as source terms in the MaxwellBloch equations. Nevertheless, as these methods are not derived from first principles, they come with certain limitations. For example, the widely used methodology proposed in Ref. [31] produces an incorrect temporal profile of spontaneous emission, as highlighted in Refs. [34, 35].
In summary, there is currently no numerically efficient and sufficiently accurate methodology available for providing a reliable quantitative characterization of collective spontaneous emission involving an arbitrary number of multi-level emitters, especially in the presence of incoherent processes and excitation. Therefore, our objective is to establish such a formalism based on first principles. The development of this formalism draws inspiration from a many-body phase-space description utilizing the positive P function. (for more details and examples, see Refs. [36–40]). While this approach offers a direct path to stochastic equations that can be efficiently sampled in a Monte Carlo style, unfortunately, it features certain limitations that manifest in practice as spiky, diverging solutions. These limitations and a potential method for mitigating them are thoroughly discussed in Refs. [41–43]. In these works, it has been demonstrated that quantum many-body systems allow certain freedom when modeled by stochastic differential equations. It turns out that there is more than one system of equations leading to the same expectation values. In practice, different systems of equations may exhibit different degree of divergent behaviour. The technique, which provides several strategies for choosing a more stable system of equations, is commonly referred to as stochastic gauges. The present article offers an analysis of how the mentioned instability issue impacts the simulation of superfluorescence and how we adopt stochastic gauges to resolve them.
Given the need to benchmark the proposed theoretical methodology, this article focuses exclusively on superfluorescence in compact systems. This choice is motivated by the fact that it can be exactly solved using methods based on the decomposition of the quantum state. Specifically, we adopt the methodology presented in Ref. [28]. The numerical benchmark suggests that the proposed methodology provides satisfactory results for a wide range of parameter values. Discrepancies, however, arise when the system evolves into a dark many-body state. Furthermore, we demonstrate that the presence of incoherent processes mitigates the prominence of this issue.
In our formalism, neither the form nor the number of equations depends on the number of emitters N in the system. N only enters the equations as a parameter, making the methodology free from the numerical difficulties inherent in techniques based on quantum state decomposition. For the extended methodology suitable for analyzing distributed systems, we refer the interested reader to Ref. [44].
Let us outline the structure of the article. In Sec. II, we construct the master equation for superfluorescence in compact systems. In Sec. III, we rephrase the quantummechanical problem in terms of stochastic differential equations. We also address numerical challenges encountered during the simulations and propose potential solutions. In Sec. IV, we analyze various conditions under which the phenomenon of superfluorescence can be observed. We begin with the simplest example in Sec. IV A, involving the cooperative emission of instantly excited two-level atoms. By comparing our simulations with those based on the methodology presented in Ref. [28], we evaluate the performance of our proposed method for various numbers of atoms and initial conditions. We demonstrate that under specific circumstances when the system evolves into a dark many-body state, our methodology fails to reproduce the correct behavior. When the influence of such states is not significant, we achieve adequate results with minimal computational resources. In Sec. IV B, we explicitly include excitation via incoherent pumping. This accentuates the challenge posed by dark states. We demonstrate how this issue can be mitigated by introducing decoherence typically present in experimental conditions. In Secs. IV C and IV D, we conclude the numerical examples by studying multi-level effects in superfluorescence observed in V - and Λ-systems. In this case, we demonstrate the performance of the methodology by constructing non-trivial three-particle correlation functions. In Sec. V, we give an overview of the accuracy, and efficiency of our methodology and share empirical observations made during the numerical studies.
II. COMPACT SYSTEMS
The dynamics of the field in distributed systems is generally complex and depends on many factors that are insignificant for our goal to introduce the key ideas of our stochastic formalism applied to superfluorescence. In Ref. [1], it was supposed that in a compact ensemble of atoms, the system size was considerably smaller than the wavelength of the field. As a result, the atoms saw an identical field. This simplified model neglects the influence of dipole-dipole interactions between the atoms that was shown to be detrimental to observing superfluorescence [4, 45–47]. In certain cases of strong dipole-dipole interactions, the so-called dipole blockade [48], suppresses the electronic transitions initiated by a narrow-band field. The effects of dipole-dipole interactions strongly depend on the geometry and distances between the emitters, thus defining the minimal interatomic distance beyond which the superradiant behavior takes place [49, 50]. Numerical analysis with fully implemented dipoledipole interactions is quite involved since it requires individual treatment of each atom due to the broken symmetry. One possible workaround is to replace the dipoledipole interacting atoms with atoms that interact only


 3
through the radiative field but possess different transition frequencies, mimicking the impact of the dipole-dipole interactions [51]. Another approach is to reduce the effect of the dipole-dipole interactions by introducing a bad cavity or an elongated dilute atomic system. The former approach will ultimately lead us to superfluorescence in compact systems. As shown in Ref. [52], proper use of a cavity eliminates the effect of dipole-dipole interactions, which may explain a good agreement between experiments in Refs. [53, 54] and a simple Dicke model without any account of dipole-dipole interactions. Indeed, a cavity selects optical wave vectors close to the transition frequency ω0, which filters out the dipole-dipole interactions and simplifies the spatial dependence of the field. Based on these assumptions, the problem of superfluorescence is considerably simplified and reduces to a Dicke master equation that we aim to solve by means of stochastic differential equations. Consider a system of N identical multi-level atoms characterized by a system of levels {|p⟩}, energies ħωp, and the following free Hamiltonian:
Hˆ0 =
X
p
ħωp
X
a
σˆa,pp.
Here, we utilize the operators σˆa,pq = |p⟩a⟨q|a to describe transitions between states for each atom a. Initially, atoms are uncorrelated and described by a density matrix symmetric under any permutation. The atomic levels are coupled to the quantized electric displacement field ˆD(r). The presence of the cavity makes its amplitude uniform across the sample. We suppose a field of single carrier wave vector k0 associated with the transition frequency ω0 = ck0 given by
ˆD(r) ≈ ˆD(+)eik0r + Dˆ(−)e−ik0r
=
X
λ
D0ˆaλeλeik0r + D∗
0 aˆ†
λe∗
λ e−ik0r .
Here, D0 = ipħω0ε0/[2V ], V is the quantization volume, ˆaλ and ˆa†
λ are the bosonic field operators, and the vectors eλ are the polarizations of the field perpendicular to k0. Among all the atomic levels, the light only couples two subsets: the ground state manifold |g⟩ and the excited state manifold |e⟩. Their energy splittings, denoted as ωee′ = ωe − ωe′ and ωgg′ = ωg − ωg′ , are assumed to be much smaller than the carrier frequency ω0. Later in this article, we use indices p, q, r, s, i, j to represent any arbitrary state, while specifically reserving indices g and e for states from the ground and excited state manifolds, respectively. The dynamics of the atomic populations is supposed to change on time scales large compared to 1/ω0, so that non-resonant contributions are neglected. Based on these approximations, we write the following interaction Hamiltonian
Vˆ = − 1
ε0
ˆD(+) X
e,g
deg
X
a
σˆa,egeik0ra + h.c. (1)
where dpq are the matrix elements of the dipole moment operators. The atomic coherences assemble in the sum P
a σˆa,egeik0ra reflecting the collective interaction
with the field mode1. Henceforth, we omit the multiplier eik0ra since it can be adjusted by shifting the phases of the states |e⟩ and |g⟩. We introduce collective dipole mo
ments ˆP(±) composed of the phased operators σˆa,pq as follows:
Pˆ (−) =
X
eg
deg
X
a
σˆa,eg ,
ˆP(+) =
X
eg
dge
X
a
σˆa,ge.
This gives a compact expression for the interaction Hamiltonian in Eq. (1):
Vˆ = − 1
ε0
ˆP(−)Dˆ(+) + ˆP(+)Dˆ(−) . (2)
Having only one mode in a cavity simplifies the spatial dynamics; however, it can only lead to optical phenomena such as quantum Rabi oscillations, collapse, and revivals [55, 56], which we do not intend to analyze in this article. Additionally, achieving collective spontaneous emission requires a substantial leakage of photons, as discussed in, for example, Ref. [5]. After an atom emits a photon, it makes effectively Q/[k0L] passes2 through the cavity before it gets damped. Here, Q is the quality factor, and L is the length of the cavity. In order to have collective spontaneous emission, the dynamics of the atomic populations and coherences must be much slower than the leakage of the field. In these circumstances, we can trace out the field degrees of freedom by applying the Born-Markov approximation, which leads to the well-known Dicke master equation formulated for multi-level atoms
dρˆ(t)
dt = L[ρˆ(t)] = i
ħ
h
ρˆ(t), Hˆ0 + Vˆin(t)
i
+ Lcoll.[ρˆ(t)] + Lincoh.[ρˆ(t)]. (3)
Initially, the field is coupled to the atoms through the interaction Hamiltonian Vˆ . After tracing out the field degrees of freedom, its role is taken over by two operators Lcoll.[ρˆ(t)] and Vˆin(t). The superoperator Lcoll.[ρˆ(t)] represents collective dissipation caused by the interaction of the atoms with their own light from previous passes:
Lcoll.[ρˆ(t)] = γ
2
X
α
hPˆ(+)
α ρˆ(t) , Pˆ(−)
α
i
+
hPˆ(+)
α , ρˆ(t) Pˆ(−)
α
i
,
1 In Ref. [53], the atomic sample is positioned at an antinode of a standing wave, which can be taken into account by neglecting
e±ik0ra .
2 Q/[k0L] is the decay rate of the intensity. The field amplitudes decay two times slower.


 4
where γ = 2Q/[V ħε0], and Pˆ(±)
α are components of the
vector operators ˆP(±). Since the atoms interact with the light collectively, Lcoll.[ρˆ(t)] eventually involves only the
collective dipole moments Pˆ (±). If the system is exposed to an externally applied field Din(r, t), which is uniform across the atomic ensemble:
Din(r, t) = D(+)
in (t)eik0r + D(−)
in (t)e−ik0r, (4)
it can be included in the master equation with the interaction Hamiltonian Vˆin(t) constructed similar to Vˆ (t) in Eq. (2)
Vˆin(t) = − 1
ε0
ˆP(−)D(+)
in (t) + ˆP(+)D(−)
in (t)
The amplitudes D(±)
in (t) can be deterministic complexvalued functions representing classical fields or quantum light in a coherent state. Moreover, D(±)
in (t) can have some statistical distribution that reproduces moments of normal-ordered field operators. The amplitudes D(±)
in (t) allow the inclusion of black-body photons or any arbitrary external field causing stimulated emission. Besides collective interaction with the radiation, atoms undergo a wide variety of incoherent processes, such as non-radiative decay, ionization. By introducing a separate independent reservoir for each atom and assuming that atoms interact with them identically, we apply the Markovian approximation [57, 58] and derive the most general form of Lincoh.[ρˆ(t)]:
Lincoh.[ρˆ(t)] = 1
2
X
a,p,q,
r,s
Γpqrs(t) σˆa,pqρˆ(t) , σˆa,sr
+ σˆa,pq, ρˆ(t) σˆa,sr . (5)
The characteristics of the incoherent processes enter the equations through the rates Γpqrs(t).
III. STOCHASTIC EQUATIONS
The master equation (3) is symmetric under atomic permutations. When the system starts from any symmetric density matrix, the problem can be solved for a moderately large number of atoms (N ≲ 100) by applying methods from Refs. [28, 29]. A simplified method from Ref. [27] can be used when the atoms start from a statistical mixture of symmetric pure states and interact only collectively, namely, without Lincoh.[ρˆ(t)]. The main drawback of these methods is their polynomial scaling with N .
The development of our formalism draws inspiration from the concept of a positive P function [36–40] used to generate stochastic differential equations for the problems involving bosonic fields. The final equations possess an intuitive form: the deterministic parts remind classical equations, whereas the quantum effects are attributed to the noise terms. We attempt to derive similar equations for a compact system of quantum emitters. First, we analyze the distinctions between the quantum description based on the master equation and the semi-classical one based on the Bloch equations [4, 55]. Further, we demonstrate how these equations can be enhanced with supplementary stochastic terms, characterized by specific statistical properties, to restore the missing quantum properties.
A. Optical Bloch equations
We start the derivation with the simplest possible ansatz for the density matrix ρˆ(t), assuming a complete factorization of the atomic degrees of freedom in terms of single-particle density matrices ρˆa(t):
ρˆ(t) =
Y
a
ρˆa(t). (6)
Furthermore, since the system is symmetric under permutations, we assume that all ρˆa(t) have the same matrix elements ρpq(t), so that
ρˆa(t) =
X
pq
ρpq (t)σˆa,pq .
Fig. 1 (a) schematically depicts this ansatz. Although this decomposition is suitable for the assumed initial state of a fully symmetric density matrix of uncorrelated atoms, the further evolution of the system can only be partially captured by this proposed ansatz. To get the equations for the variables ρpq(t), we generate the following equations for the expectation values Tr(σˆa,pqρˆ(t)):
d
dt Tr(σˆa,pqρˆ(t)) = Tr(σˆa,pqL[ρˆ(t)]).
Assuming the decomposition in Eq. (6), the expectation values Tr(σˆa,pqρˆ(t)) are equal to ρqp(t). The considered ansatz for the density matrix factorizes second-order correlators, namely:
Tr(σˆa,pqσˆb,rsρˆ(t)) = ρqp(t)ρsr(t), (7)
which leads to a closed system of equations known as Bloch equations [4, 55]:


 5
ρ ̇pq(t) = −iωpqρpq(t) + 1
2
X
i,j
2Γpiqj (t) ρij (t) − Γijip(t) ρjq(t) − ρpj (t) Γiqij (t)
+γ
2
X
r,s
2ρrs(t)dp<rds>q − dp>rdr<sρsq(t) − ρpr(t)dr>sds<q (8)
+i
ħε0
D(+)(t)
X
r
dp>rρrq(t) − ρpr(t) dr>q + i
ħε0
D(−)(t)
X
r
dp<rρrq(t) − ρpr(t) dr<q ,
where p > q means that index p corresponds to the subset of excited states {|e⟩} and index q represents the subset of
ground states {|g⟩}. Each atom interacts with the field amplitudes D(±)(t) that combine the incoming fields D(±)
in (t) and the field produced by the other N − 1 atoms:
D(+)(t) = D(+)
in (t) + iħε0
γ
2 (N − 1)
X
e,g
dgeρeg(t), D(−)(t) = D(−)
in (t) − iħε0
γ
2 (N − 1)
X
g,e
degρge(t). (9)
The factorization of the second-order correlators in Eq. (7) used in the derivations of the Bloch equations shows that these equations are valid only for systems with strong classical behavior. Let us reconstruct the neglected terms in the master equation (3) and analyze their structure. If we insert the decomposition from Eq. (6) in the master equation (3), and then apply Bloch equations (8), we notice that the right-hand side of L[ρˆ(t)] in Eq. (3) is restored only partially
L[ρˆ(t)] − dρˆ(t)
dt =
X
b̸=c
χˆb,c(t)
Y
a̸=b,c
ρˆa(t). (10)
This is schematically depicted in Figs. 1 (b) and (c). The time derivative of Eq. (6) can generate the terms, where only one ρˆa is modified, as illustrated on panel (b). Consequently, the remaining terms in Eq. (10) entangle pairs of ρˆa through χˆb,c(t) defined as follows:
χˆb,c(t) =
X
p,q,r,s
χpqrs(t)σˆb,pqσˆc,rs, (11)
where
χpqrs(t) = γ
2
X
r′
ρpr′ (t)dr′>q − ρpq(t)
X
g,e
deg ρge (t)
X
p′
dr<p′ ρp′s(t) − ρrp′ (t)dp′<s
+
X
r′
ρpr′ (t)dr′>q − dp>r′ ρr′q(t)
X
p′
dr<p′ ρp′s(t) − ρrs(t)
X
e,g
dgeρeg(t) + [p, q ⇄ r, s].
(12)
Here, the second term is generated by exchanging the pairs of indices (p, q) and (r, s). The structure of χˆb,c(t) is schematically illustrated in Fig. 1 (c) by a second term, which explicitly shows two-particle interactions.
B. Stochastic terms
Although χpqrs(t) looks complicated, the uncompensated terms in the right-hand side of Eq. (10) contain only entangled pairs of atoms, as Eq. (11) suggests. Nontrivial correlations of higher orders are not involved, so the terms in Eq. (11) can be correctly recaptured by adding appropriate stochastic terms to the Bloch equations (8). In addition to the deterministic time evolution, we introduce stochastic terms Fpq as described by the following equation:
ρ ̇pq (t) noise = Fpq({ρij (t)}, t). (13)
It is important to note that the properties of the noise terms can be generally parametrized by the dynamic variables ρij(t). We only constrain Fpq to be Gaussian white noise terms with zero mean and the following secondorder correlation properties:
Fpq({xij }, t)Frs({xij }, t′)
= κpqrs({xij}, t)δ(t − t′). (14)
The coefficients κpqrs will be specified later. Note that Eq. (14) is parameterized by free parameters xij, which can take on the role of the dynamic variables ρij(t), like, for instance, in Eq. (13). When included in the noise


 6
c
ab
FIG. 1. Schematic representation of the completely factorized density matrix (a) and its interaction with the time derivative (b) and L[ρˆ(t)] (c). In panel (a), we illustrate the density matrix of the whole ensemble as a product state composed of individual single-particle density matrices. The time derivative of this density matrix leads to a sum of products, where only single-particle density matrices are affected, as highlighted by the orange color in panel (b). Upon applying the collective Liouville operator, in addition to products where only a single particle is affected La[. . .], there is an additional contribution from two-particle interactions La̸=b[. . .]. This is represented in panel (c).
terms, the dynamic variables ρij(t) contribute their own statistics. To capture the statistical properties inherent solely in the noise terms Fpq, Eq.(14) is formulated without explicit dependence on ρij(t). We assume that the noise terms are integrated in Itoˆ’s sense. Typically, the stochastic equations are solved with the Monte Carlo approach. The proper statistics of the dynamic variables ρpq(t) is reconstructed by repeatedly solving equations with a randomly sampled stochastic contribution in accordance with their statistical properties. Since the variables are independently integrated for each repetition, the problem is parallelizeable, which gives a great advantage in performance compared to the methods based on the direct decomposition of the quantum state in some basis set. To reconstruct the density matrix ρˆ(t), we insert each realization of the variables ρpq (t) into the decomposition in Eq. (6) and aggregate all realizations of density matrices (6) into a normalized linear combination:
ρˆ(t) =
DY
a
ρˆa(t)
E
=
DY
a
X
pq
ρqp(t)σˆa,pq
E
=
X
i
" Y
a
X
pq
ρ(i)
qp (t)σˆa,pq
#
Nsample. (15)
This density matrix is no longer factorizable. Here, ρ(i)
qp (t)
represents the i-th realization of the variables ρqp(t), and Nsample is the total number of statistical realizations. We anticipate that this linear combination can restore missing entangled terms in Eq. (10). The remaining step is to identify a specific expression for κpqrs(t). Although the new decomposition in Eq. (15) does not change the expression for the first term L[ρˆ(t)], the
derivative dρˆ(t)
dt is modified by additional terms propor
tional to κpqrs, due to Itˆo’s lemma. Consider an arbitrary function S that depends on variables ρpq(t). If the variables ρpq(t) are governed by equations that include the noise terms from Eq. (13), Itˆo’s lemma can be expressed as:
dS
dt =
X
p,q
∂S
∂ρpq
dρpq
dt + 1
2
X
p,q,r,s
∂2S
∂ ρpq ∂ ρrs
κpqrs. (16)
Consequently, the full derivative of the density matrix in Eq. (15) acquires the following additional contribution:
dρˆ(t)
dt = ...
+
X
b̸=c
X
p,q,r,s
κpqrs({ρij (t)}, t)σˆb,pqσˆc,rs
Y
a̸=b,c
ρˆa(t) ,
that entangles pairs of atoms and has exactly the same form as the right-hand side of Eq. (10). Consequently, if


 7
the correlators of the noise terms taken as
κpqrs = χpqrs,
the Bloch equations (8), supplemented by the noise terms
from Eq. (13), fully satisfy the master equation (3). To simulate Fpq numerically, we have to decompose them in terms of independent noise terms. There is no unique decomposition, however, the structure of Eq. (12) suggests the most compact one, given by the following expression:
Fpq({ρij(t)}, t) =
rγ
2
X
r
dp<rρrq(t) − ρpr(t)dr<q f(t) + ρpr(t)dr>q − dp>rρrq(t) g(t)
+
rγ
2
X
r
ρpr(t)dr>q − ρpq(t)
X
g,e
degρge(t) f†(t) +
rγ
2
X
r
dp<rρrq(t) − ρpq(t)
X
e,g
dgeρeg(t) g†(t),
(17)
where we introduce vectors f(t), f†(t), g(t), g†(t) whose components are Gaussian white noise terms independent of the dynamic variables ρrq(t). The vectors f(t), f†(t) are statistically independent from the vectors g(t), g†(t). The vectors f(t), f†(t) have the correlation properties
⟨fα(t)fβ(t′)⟩ = ⟨f †
α(t)f †
β(t′)⟩ = 0,
⟨fα(t)f †
β(t′)⟩ = δαβδ(t − t′),
(18)
that can only be sampled by complex-valued Gaussian white noise terms. Corresponding stochastic properties hold for g(t) and g†(t). The number of the components of the vectors f(t), f†(t), g(t), g†(t) is defined by the dimensionality of the dipole moment vector deg. Eq. (18) does not uniquely define the form of the noise terms. One can simply choose f†(t), g†(t) to be complex conjugates of f(t), g(t). Another freedom is given by rescaling of the noise terms: if f(t) is divided and f†(t) is multiplied by the same number, the statistical properties in Eq. (18) are preserved. This freedom of choice is equivalent to the diffusion gauge in the context of positive P representation formalism [43]. The way we fix the form of the elementary noise terms f(t), f†(t), g(t), g†(t) is discussed in Sec. III C. Adding the noise terms enriches the Bloch equations with the spontaneous nature of the quantum mechanics, allowing a correct treatment of the spontaneous emission — an indispensable triggering process of superfluorescence. As mentioned in the introduction, many authors recognized the importance of adding stochastic terms into semi-classical equations by different phenomenological approaches [30–33]. Our approach is based on rigorous derivation and hence can serve as a base for further investigations and approximate methods. Note that the noise decomposition in Eq. (17) conserves the “trace” of the effective density matrix ρpq(t)
X
p
ρ ̇pp(t) =
X
p
Fpp({ρij(t)}, t) = 0.
This property is important for generating compact expressions for the expectation values. Based on the de
composition in Eq. (15), one can show that the one and two-particle expectation values possess intuitive expressions in terms of the stochastic variables ρpq(t):
Tr(σˆa,pqρˆ(t)) = ⟨ρqp(t)⟩,
Tr(σˆa,pqσˆb,rsρˆ(t)) = ⟨ρqp(t)ρsr(t)⟩, (19)
where a ̸= b. Similar expressions hold for high-order correlation functions.
C. Stochastic freedom
Unfortunately, the stochastic terms Fpq(t) break an important property of the variables ρpq(t) expected from the original, deterministic Bloch equations. Starting from Hermitian initial conditions, the Bloch equations preserve the Hermiticity of the variables ρpq(t). By Hermiticity, we henceforth refer to the condition where ρpq(t) = ρq∗p(t). However, in order to sample the correlator χpqrs(t), the noise terms must be non-Hermitian, that is, Fpq(t) ̸= Fq∗p(t), which makes the dynamic variables
ρpq(t) non-Hermitian as well, namely ρ∗pq(t) ̸= ρqp(t). In a broader context, the non-Hermiticity of the effective density matrix signifies a doubling of the number of independent dynamic variables compared to the anticipated semi-classical scenario, where atoms are characterized by Hermitian one-particle density matrices. This doubling of dynamic variables is also inherent in phasespace methods based on positive P representation [36]. Breaking of the Hermiticity comes with the drawback of diverging behavior of the solutions of the Bloch equations. Even without any noise terms, the original Bloch equations written for non-Hermitian variables may lead to unstable solutions with hyperbolic divergence:
ρpq(t) ∼ 1
t − t0
.
As the singularity is approached, the dynamic variables become anti-Hermitian, that is, ρeg(t) = −ρg∗e(t). Consequently, attempting to simulate Eq. (8) with the noise


 8
terms in Eq. (17) leads to an unstable temporal dependence of expectation values. In the context of the positive P representation, the same stability issues are encountered, which motivated the development of so-called stochastic gauges [42, 43] (in Appendix A, we adopt these stochastic gauges for our formalism). In the provided references, it has been discovered that a quantum many-body system can be modeled by more than one system of stochastic differential equations. Consequently, the preferable choice is to opt for the system of equations that demonstrates less divergent behavior, which is the key idea behind stochastic gauges. Specifically, we employ two techniques known as drift and diffusion gauges, as introduced in Refs. [42, 43]. The stochastic drift gauges allow us to alter the deterministic components of the stochastic differential equations. This modification must be compensated by an appropriate re-weighting of the stochastic trajectories. According to the drift gauging procedure reproduced in Appendix B, we include a weight coefficient Ω(t) = eC0(t) in the decomposition of the density matrix in Eq. (15):
ρˆ(t) =
D
Ω(t)
Y
a
X
pq
ρqp(t)σˆa,pq
E
. (20)
This change is also reflected in the expressions for the expectation values in Eq. (19):
Tr(σˆa,pqρˆ(t)) = ⟨Ω(t)ρqp(t)⟩,
Tr(σˆa,pqσˆb,rsρˆ(t)) = ⟨Ω(t)ρqp(t)ρsr(t)⟩, (21)
where a ̸= b. The form of the equation for the weight coefficient directly depends on how we modify the deterministic parts. The modification of the deterministic part of the Bloch equations should counteract the unbounded growth of the dynamic variables ρpq(t). Even for the determinstic Bloch equations, one can expect divergent solutions for a small violation of Hermitcity of the dynamic variables. Consequently, when the full stochastic Bloch equations are considered, the noise terms seed this non-Hermiticity, which then leads to divergence due to the structure of the deterministic terms. The structure of the deterministic terms can be slightly modified to ensure that it does not lead to any instability. Specifically, we implement the following substitution in Eq. (9):
X
g,e
degρge(t) → 1
2
X
g,e
deg ρge(t) + ρ∗
eg(t) ,
X
e,g
dgeρeg(t) → 1
2
X
e,g
dge ρeg(t) + ρ∗
ge(t) .
(22)
The fields become Hermitian after this substitution, namely D(+)(t) = D(−)∗(t). This modification of the deterministic parts can be achieved using stochastic drift gauges, which requires introducing a weight coefficient
Ω(t) = eC0(t). According to the expressions given in Appendix B, the coefficient C0(t) starts from zero and satisfies the following equation:
dC0(t)
dt = N − 1
2
rγ
2
X
g,e
h
f†(t)deg ρge(t) − ρ∗
eg (t)
+ g†(t)dge ρeg(t) − ρ∗
ge(t)
i
. (23)
Note that the right-hand side of this equation is proportional to the anti-Hermitian parts of the variables ρpq(t). Since the weight coefficient Ω(t) involves the exponentiation of C0(t), which is itself proportional to (N − 1), Ω(t) can rapidly grow over time. Consequently, the averaging in Eq. (21) may require a large number of statistical realizations to converge. To reduce the need for the proposed drift gauge, we introduce two additional techniques. First, we notice that the drift gauge is not always required since the original equations do not always increase the anti-Hermitian parts of the dynamic variables. We can apply the drift gauge once the relative increase of the anti-Hermitian parts per time step exceeds a certain limit. In practice, we have found that an individual stochastic trajectory requires gauging only when the population inversions are not negative, i.e., Re [ρee(t) − ρgg(t)] ≥ 0 for any excited state |e⟩ and ground state |g⟩. Since the variables are complex at the level of single trajectories, we take the real parts of the populations. In the context of superfluorescence, the positive sign of the population inversions causes exponential amplification of the field components D(±)
α (t), whereas negative population inversions lead to their absorption. Consequently, positive population inversions increase both the Hermitian and anti-Hermitian parts of the field components, which can trigger diverging behavior. Negative population inversions, in contrast, reduce the fields and their anti-Hermitian parts, making gauging unnecessary. A second technique is based on the flexibility provided by the correlation properties of the elementary noise vectors f(t), f†(t), g(t), and g†(t). This method is known as the diffusion gauge, as discussed in Refs. [42, 43]. In Eq. (18), we have only outlined their correlation properties without prescribing any specific form. As mentioned before, there is no unique way to define them. One of the possible representations, which we later employ in the numerical simulations, takes the following form:
fα(t) = ηα(t)f ̄α(t), f †
α(t) = η−1
α (t)f ̄∗
α(t),
gα(t) = θα(t)g ̄α(t), g†(t) = θ−1
α (t)g∗
α(t), (24)
where θα(t) and ηα(t) can take on any values. The only constraint is that they must be statistically independent of the noise terms from the future. Eq. (24) explicitly associates the noise terms f(t) and f†(t) with a single vector of independent complex noise terms f ̄(t). Similarly, g(t) and g†(t) are linked to g ̄(t). These new noise terms, f ̄(t)


 9
and g ̄(t), consist of independent and normal Gaussian white real noise terms f ̄1(t), f ̄2(t),  ̄g1(t), and g ̄2(t):
f ̄(t) = √12
f ̄1(t) + i ̄f2(t) ,
g ̄(t) = √12 ( ̄g1(t) + i ̄g2(t)) .
(25)
The explicit representation in Eq. (24) preserves the correlation properties in Eq. (18) regardless of the form of θα(t) and ηα(t). To reduce the need for the drift gauge presented in Eq. (22), we fix the form of the functions θα(t) and ηα(t) in such a way that the anti-Hermitian parts of the dipole moments
X
g,e
deg,α ρge(t) − ρ∗
eg(t) (26)
are minimized for each component α. The resulting expressions for θα(t) and ηα(t) can be found in Appendix C. However, in certain cases, these two techniques aimed at reducing the need for the stochastic drift gauge are insufficient to control the growth of the weight coefficient Ω(t). In these circumstances, large absolute values of the weight coefficient Ω(t) lead to spikes in temporal profiles of expectation values. While the proposed gauging techniques do not entirely resolve the instability issue, they significantly mitigate it. To improve convergence, trajectories with a weight coefficient exceeding e5 in absolute value are removed in the numerical examples given in Sec. IV. Besides the structure of the deterministic terms, another source of divergence exists that cannot be efficiently addressed with the stochastic drift gauge. In practice, we have observed that quadratic contributions in the noise terms, as given in Eq. (17), can, in certain cases, cause unbounded growth of the density matrix ρpq(t). When the absolute value of one of the density matrix elements exceeds 100, such realizations are removed from the statistical sample in the numerical examples presented in Sec. IV. The comparison with the full quantum-mechanical simulations presented in Sec. IV shows that omitting the unstable stochastic trajectories after applying the stochastic gauges does not significantly compromise the accuracy. As demonstrated in Sec. V, this strategy performs noticeably better than using the ungauged original equations (8) with the noise terms given in Eq. (17).
IV. NUMERICAL ANALYSIS
We illustrate the proposed formalism through a series of numerical examples. The deterministic components of the stochastic equations are numerically integrated using the adaptive step-size method Tsit5, which is implemented in the DifferentialEquations.jl library [59].
The noise components are integrated using the EulerMaruyama method [60, 61]. We use 105 stochastic trajectories to construct statistical averages. The simulations based on the stochastic formalism are compared with those based on the methodology presented in Ref. [28]. For both methods, the maximum allowed timestep was limited to Tmax/104. Here, Tmax represents the last point on the dimensionless time grid. The dynamics of the stochastic density matrix ρpq(t) is defined by Eq. (8) with noise terms given in Eq. (17). As proposed in in Sec. III C, we apply stochastic gauges to mitigate the instabilities. We modify the equations according to Eq. (22), namely by making the deterministic part of the field Hermitian. This adjustment requires the introduction of an additional variable C0(t), which re-weights the trajectories, as shown in Eq. (20). Additionally, we employ the diffusion gauge presented in Eq. (24) and Appendix C to suppress the increase of nonHermitian dipole moment components. As explained at the end of Sec. III C, a stochastic trajectory is removed from the statistical sample if it exhibits diverging behavior, with its weight coefficient Ω(t) exceeding e5 or any density matrix element growing above 100. The number of excluded trajectories is given in the caption of each figure. Before we proceed with numerical simulations, let us link the expectation values of quantum-mechanical operators with the respective stochastic variables. Specifically, we will examine the average populations of atomic levels using the following expression:
pq(t) = 1
N
X
a
Tr(σˆa,qqρˆ(t)) = ⟨Ω(t)ρqq(t)⟩,
where Eq. (20) has been utilized. In compact systems, the field properties can be expressed through the atomic operators and, consequently, through the associated stochastic variables. Up to an insignificant factor, the intensity of the emission polarized along the α-axis is given by the product of collective dipole moments:
Iα(t) = Tr
hPˆ(−)
α Pˆ(+)
α ρˆ(t)
i
. (27a)
Utilizing Eq. (20), we express the intensities Iα(t) in terms of the stochastic variables ρpq(t):
Iα(t) = N
X
e1 ,e2 ,g
de1g,α dge2,α ⟨Ω(t)ρe2e1 (t)⟩
+ N (N − 1)
X
e1 ,e2
g1 ,g2
de1g1,α dg2e2,α Ω(t)ρg1e1 (t) ρe2g2 (t) .
(27b)
The full intensity is found by summing all the components.


 10
e
a
d
bc
f
FIG. 2. Solutions to the stochastic equations, modified as described in Sec. III C. The semi-transparent lines correspond to quantum expectation values, while the opaque lines represent stochastic averages. The intensities (d, e, f) have been normalized to the maximum value in the panel. The subplots below each row show the absolute difference between populations and normalised intensities based on stochastic averages and quantum expectation values. For the cases of N = 2, 3, 4 (a, d), we have omitted 22, 4, 3 unstable trajectories, respectively.
A. Cooperative emission of two-level atoms
Let us revisit the example of identical two-level atoms collectively interacting with their own field. The ground state manifold {|g⟩} collapses to a single state |1⟩, and the excited state manifold {|e⟩} reduces to a single state |2⟩.
When the ensemble starts from the fully excited state, characterized by ρ22(0) = 1, with all other matrix elements set to zero, the phenomenon of superradiance is observed. Fig. 2 shows the excited state population and emission intensity for different numbers of atoms N . We exclude the single-atom case N = 1 since it does not require the extension of the ansatz (6) beyond the singleparticle density matrix. Thus, the noise terms are unnecessary in this case. Increasing the value of N leads to faster depopulation of the excited state and a narrower, more pronounced peak in intensity. As depicted in Figs. 2, the discrepancy between stochastic averages and quantum expectation values remains less than 1.0%. Panels (a) and (d) show that the difference is higher for smaller N . We attribute this increase to the non-linear noise terms that become comparable to the deterministic parts for small N . Moreover, it can lead to unstable
trajectories and small spikes in intensities, as observed in the simulations shown in Figs. 2 (a, d).
In Fig. 2 we used 105 stochastic realizations. In practice, much fewer trajectories are required for the convergence of selected observables. Fig. 3 demonstrates the convergence of population and intensity for different numbers of stochastic realizations. For qualitative analysis, averaging over 102 trajectories is enough, while averaging over 103 trajectories already gives accurate averages. Based on our experience, 1000 trajectories are also sufficient to achieve good accuracy for other systems discussed later. In addition to the direct comparison with quantum averages, we use another criterion of convergence: imaginary parts of such observables as populations or intensities should vanish after averaging. For a single trajectory, the imaginary part is comparable to the real part, thus it does not have physical meaning. Statistical averages represent observables only after averaging over a significant amount of trajectories.
There is a special case when the initial state is statistically mixed. As shown in Ref. [28], if the system is prepared in the state without coherences ρ12(0) = ρ21(0) = 0


 11
a bc
def
FIG. 3. Convergence of the stochastic averages (dashed lines) to the exact quantum expectation values (solid lines) for different numbers of atoms N . The atomic ensemble is initially fully excited, i.e. ρ22(0) = 1.0, and other matrix elements are zero. The observables chosen here are the probability of finding an excited atom (a, b, c) and the intensity of the emitted field (d, e, f). Intensity is normalized to the maximum. The dotted lines represent the imaginary parts of corresponding quantities. As expected, they disappear with the increasing number of trajectories.
and only with the diagonal elements:
ρ11(0) = p1, ρ22(0) = p2, (28)
with p2 < 1, the collective emission process becomes weaker. The ensemble reaches a steady state with a nonzero probability of finding an excited atom, namely
⟨ρ(ss)
22 ⟩ > 0, where ss stands for steady state3. In this steady state, the field intensity, as defined in Eq. (27), is zero, implying that:
⟨ρ(ss)
22 ⟩ + (N − 1) ⟨ρ(ss)
12 ρ(ss)
21 ⟩ = 0. (29)
This, in turn, implies that ⟨ρ(ss)
12 ρ(ss)
21 ⟩ < 0, a condition that can only be met when the dipole moments exhibit significant non-Hermitian behavior at the level of individual stochastic realizations. Our gauges aim to minimize the non-Hermitian components, and finding appropriate gauging to account for this particular case remains a separate challenge. And indeed, this special case is not fully
3 Here, in averages we dropped out the weight function for brevity.
reproduced by the stochastic equations, see Fig. 4. Panels (a-c) show that, for a small number of atoms N = 2, the excited state population does not converge to the correct curve, while the intensity exhibits slow convergence and noisy behavior at later time moments. As demonstrated in Fig. 4 (d-i), the situation improves when the number of atoms increases. Specifically, the percentage of unstable trajectories becomes lower. Additionally, the absolute difference between populations and intensities, based on stochastic and full quantum-mechanical approaches, decreases.
Note that the case of p1 = p2 = 0.5 consistently exhibits worse performance in terms of absolute differences and numbers of unstable trajectories for any number of atoms. In Ref. [28], an analytical expression for the steady-state density matrix was found. Initial conditions enter this expression as a single parameter (p1 p2) ≤ 1/4. The larger this parameter, the stronger the population trapping effect becomes, making it more challenging to reproduce the correct curves using the stochastic methodology.
The population trapping effect occurs due to the assumption that all the atoms experience the same field.


 12
h
gi
f
e
d
c
b
a
FIG. 4. The excited state population and emission intensity plotted for different numbers of atoms N and varying initial conditions. The semi-transparent lines correspond to the quantum expectation values, while the opaque lines represent the stochastic averages. The absolute differences between these values are indicated by gray dotted lines. We label some plots with ×10−1, ×10−2, ×10−3 to highlight that the corresponding difference values should be multiplied by this factor. We excluded the following numbers of unstable trajectories: (a) 131 (0.13%); (b) 178 (0.18%); (c) 170 (0.17%); (d) 32 (0.03%); (e) 109 (0.11%); (f) 40 (0.04%); (h) 17 (0.02%).
This field is immediately updated according to the current value of the dipole moments. At some point, the emission and absorption processes balance each other, and the ensemble does not relax to the ground state but rather evolves into a quasi-stationary state.
B. Incoherent pumping
In a more realistic situation, the excitation of the ensemble is not instantaneous. The system’s initial condition may be prepared by continuous incoherent pumping, as in x-ray lasing experiments [22, 62]. A pump pulse ion
izes neutral atoms, opening the lasing transition in the ionized atoms, see Fig. 5 (a) for a sketch of the level structure. In Ref. [28], it was shown that if the system is pumped incoherently, it reaches a steady state similar to the ones in Fig. 4, in which the atoms are not fully relaxed. At the level of stochastic equations, the additional variable describing the population of the neutral state is required, denoted by ρ00(t). This state is coupled to the excited state only through the incoherent pumping 0 → 2 with the rate κ(t). The time dependence of κ(t) defines the pump profile. Pumping results in an additional term


 13
a
bc
FIG. 5. (a) Level structure of the pumped two-level atoms. Neutral atoms are photoionized by a pump pulse with a profile κ(t). Excited ions relax via collective emission 2 → 1 with a rate γ. We compare the stochastic (opaque lines) and quantum (semi-transparent lines) expectation values for two cases: N = 10 (b) and N = 100 (c). We have selected a Gaussian envelope
for the pump, κ(t) = Ip exp
h
− (t−t0)2
2τ 2
i
/√2πτ 2, with the following parameters used for calculations: Ip = 10, t0 = 2.0/γ, and
τ = 0.5/γ. We excluded 199 (0.20%) (b) and 3871 (3.87%) (c) unstable trajectories.
bc
def
a
FIG. 6. Regularization of the incoherently pumped system from Fig. 5 by introducing an additional non-radiative dissipation channel 2 → 1 with a rate Γ. The semi-transparent lines correspond to quantum expectation values, while the opaque lines represent stochastic averages. We neglected (a) 268 (0.27%); (b) 119 (0.12%); (c) 59 (0.06%); (d) 2699 (2.70%); (e) 1061 (1.06%); and (f) 493 (0.49%) unstable trajectories.


 14
in equation for ρ22(t):
ρ ̇22(t) = ... + κ(t) ρ00(t),
while the new variable satisfies the stochastic equation:
ρ ̇00(t) = −κ(t)ρ00(t)
− ρ00(t)
rγ
2
X
e,g
degρge(t)f †(t) + dgeρeg(t)g†(t) .
(30)
In our simulations, we have used a Gaussian pump profile. The stochastic averages are depicted in Fig. 5. Although the superradiant dynamics is accurately reproduced, we encounter the same issue as in Fig. 4, where the steady states are captured incorrectly. While the populations do not maintain constant values, the intensities show slow convergence and small spikes at the end of the evolution time. For a larger number of atoms N = 100 in panel (c), the situation does not improve, in contrast to Fig. 4 (g, i). Additionally, the number of unstable trajectories increases. Perhaps, the continuous pumping process generates a more intricate steady state, posing challenges for accurate reproduction by our stochastic formalism.
As pointed out in Ref. [28], additional dissipation channels disrupt the formation of the steady states. Ref. [28] assumed the Meitner-Auger decay of the excited state. Alternatively, one could consider non-radiative dissipation to the ground state (2 → 1) with a rate Γ as follows:
ρ ̇11(t) = . . . + Γρ22(t), ρ ̇22(t) = . . . − Γρ22(t),
ρ ̇12(t) = . . . − Γ
2 ρ12(t), ρ ̇21(t) = . . . − Γ
2 ρ21(t).
Fig. 6 illustrates the impact of non-radiative dissipation on the discrepancies observed in Fig. 5. For N = 10 and 100, we increase the dissipation rate Γ from 0.1γ (panel (a, d)) to 0.3γ (panel (c, f)), which gradually improves the performance of the stochastic method. Populations show better agreement with the full quantum simulations, while intensities exhibit better convergence and fewer spikes. Additionally, the number of unstable trajectories decreases. Based on our experience, systems with a larger number of atoms may require a higher dissipation rate. In the given examples, the additional dissipation with the rate of the same order of magnitude as spontaneous emission, i.e., Γ ∼ γ, is sufficient for regularization.
In conclusion, the ratio between timescales of superradiance, pumping, and dissipation directly influences the formation of steady states. Notably, when these steady states are less prominent, the stochastic formalism consistently yields accurate averages.
C. Quantum beats in V -system
So far, we have considered only models with lasing between two levels. To demonstrate that our formalism correctly captures many-level effects, we consider a V type configuration with two excited states |2⟩ , |3⟩ and a single ground state |1⟩, as shown in Fig. 7 (a). The energy gap between excited states ∆ is much smaller than the center frequency ∆ ≪ ω0. Fluorescence from emitters with such a level structure may exhibit quantum beating, a fundamental quantum phenomenon that has been observed in various spectral ranges, including optical [63, 64], XUV [65, 66], and x-rays [67]. In the context of collective emission, quantum beating is superimposed with superfluorescent behavior [68, 69]. Here, we consider superfluorescence in Helium gas under presence of a weak magnetic field, as in Ref. [66]. We consider transitions from states 2 to 1 and 3 to 1 with slightly different strengths:
d31 = d√321 (ex − iey) , d21 = d√221 (ex + iey) ,
where |d31|2 = 1 and |d21|2 = 0.75. The transition between the excited states is forbidden, namely d32 = 0. If we assume that each atom in the ensemble is initially prepared in a coherent superposition of excited states, such as:
|ψ⟩a = |2⟩a − |3⟩a
√2 ,
we can observe quantum beats in the intensity of both the x- and y-components of the field [70]. In this scenario, the initial collective state of the ensemble is separable, following Eq. (6), and each atom is characterized by a single-particle density matrix with the following components:
ρ22(0) = ρ33(0) = 0.5, ρ23(0) = ρ32(0) = −0.5,
while all other matrix elements are zero. As demonstrated in Fig. 7 (b, c), our formalism reproduces the quantum beats. For N = 2 atoms in panel (b), we additionally plot intensity curves in the logarithmic scale (a small box at the top right corner). The stochastic formalism agrees well with the full quantum-mechanical calculations. Only the low-amplitude oscillations are not reproduced, because they are at the level of statistical fluctuations. Let us also analyze a system starting from a statistical mixture. We focus on the most challenging scenario where the initial state has no coherences, and the excited states are statistically equally populated:
ρ22(0) = ρ33(0) = 0.5, ρ23(0) = ρ32(0) = 0.0.
In this case, there are no quantum beats in the intensity, and the ensemble evolves into a nontrivial steady state.


 15
a
c
b
FIG. 7. Quantum beats in a V -type system, depicted on the left (a), calculated for N = 2 (b) and N = 20 (c) atoms. In both cases, we have taken ∆ = 15 γ, and plotted populations (upper row) and normalized intensities (lower rows) of the field for both polarizations. For intensity curves (b), we give the same plots in a logarithmic scale in small boxes. The intensities of different polarization components are normalized to the maximum full intensity. The semi-transparent lines correspond to quantum expectation values, while the opaque lines represent stochastic averages. We omitted 47 (0.05%) diverging trajectories for the case of N = 2 (b).
As depicted in Fig. 8 (a), our formalism does not entirely reproduce this steady state for longer evolution times. With multi-level atoms, we can construct another class of observable, namely a three-operator correlator:
⟨ρ12(t) ρ23(t) ρ31(t)⟩
= (N − 3)!
N!
X
μ1 ̸=μ2 ̸=μ3
Tr (σˆμ1,13 σˆμ2,32 σˆμ3,21 ρˆ(t)) .
Such correlators are often factorized in semi-classical and approximated approaches [35]. However, when there is no initial coherence, any factorization of this operator results in zero. Hence, it is important to demonstrate how our formalism reproduces such correlators. As shown in Fig. 8 (a), the convergence of the three-operator correlator becomes problematic only when the system approaches the steady state. In reality, the atoms are not pumped instantaneously. To simulate the effect of a pump pulse, we introduce an additional level |0⟩ described by ρ00(t), as in Sec. IV B. All atoms start from this state and are incoherently pumped to the excited states according to:
ρ ̇ee(t) = ... + κ(t)
2 ρ00(t), e = 2, 3,
while ρ00(t) satisfies Eq. (30). The simulations in Fig. 8 (d) reveal that the convergence problems are more pronounced when the system is pumped. Specifically, the intensity curves have spikes and the three-operator correlator does not converge after the emission peak around
tγ ≈ 2.0. This is due to the stronger influence of steady states since more population is trapped in the excited states compared to the case without pumping. We regularize these issues by introducing additional non-radiative damping of excited states to the ground states with a rate Γ:
ρ ̇11(t) = . . . + Γ
X
e
ρee(t) (31a)
ρ ̇ee(t) = . . . − Γρee(t), (31b)
where e = 2, 3. The coherences decay according to:
ρ ̇1e(t) = . . . − Γ
2 ρ1e(t), (31c)
ρ ̇e1(t) = . . . − Γ
2 ρe1(t), (31d)
ρ ̇e1e2 (t) = . . . − Γρe1e2 (t), (31e)
In Fig. 8 (b, c) and (e, f), we have found a minimal value of Γ required to mitigate the discrepancies. As in the previous section, values of Γ ∼ γ are sufficient. To stabilize higher-order correlators, larger dissipation rates are necessary. With this additional damping, all observables are reproduced for a chosen time range, including the three-operator correlator. As in simulations illustrated in Fig. 6, larger Γ decreases the number of unstable trajectories. This demonstrates that our formalism goes beyond semi-classical models and, when properly regularized, fully captures the quantum effects of manybody correlations.


 16
a bc
de f
FIG. 8. The dynamics of the ensemble of N = 20 atoms with the V -type level structure depicted in Fig. 7 (a). In order to mitigate the discrepancies, we introduce additional non-radiative dissipation channels from the excited states to the ground state (2, 3 → 1) with a rate Γ (see Eqs. (31)). The semi-transparent lines correspond to quantum expectation values, while the opaque lines represent stochastic averages. In the upper row (a, b, c), atoms start from the mixed state without coherence ρ22(0) = ρ33(0) = 0.5, the rest is zero. In the lower row (d, e, f), atoms are incoherently pumped, and similar issues with steady states arise. We chose the same profile as in Fig. 5 for the pump. The gray line demonstrates the evolution of ρ00(t). Overall we omitted (a) 427 (0.43%); (b) 174 (0.17%); (c) 63 (0.06%); (d) 2503 (2.50%); (e) 239 (0.24%) and (f) 4 (0.004%) unstable trajectories. Both polarization components of intensity exhibit identical profiles, and we depict only one of them.


 17
bc
a
FIG. 9. Lasing from an ensemble of atoms with a Λ-type level structure, as depicted in (a). The separation between ground states ∆ is much smaller than the center frequency ω0. We present the evolution of populations and intensity components for N = 2 (b) and N = 20 (c) atoms. Intensity components are normalized to the maximum full intensity. The semi-transparent lines correspond to quantum expectation values, while the opaque lines represent stochastic averages. We neglected 383 (0.39%) (b) and 2229 (2.23%) (c) unstable realizations.
D. Lasing in Λ-system
Quantum beats in V -systems are predicted by semiclassical models and stochastic electrodynamics approaches [55]. However, some semi-classical and stochastic models incorrectly predict quantum beats in Λsystems [55, 71], with one excited state |3⟩ and two ground states |1⟩ and |2⟩, as shown in Fig. 9 (a). To demonstrate our formalism’s predictive power as a true quantum model, we study such a Λ-system with orthogonal transition polarizations:
d31 = d√321 (ex − iey) , d32 = d√322 (ex + iey) .
Here, |d31|2 = 1 and |d32|2 = 0.75. The transition between the ground states is forbidden. Our equations predict the absence of intensity beats, which aligns with the results from quantum simulations. In Fig. 9 (b, c), we present population and intensity curves for N = 2 and N = 20. Both polarization components of the field do not show any signs of beating and share the same profile. For this reason, we depict only one polarization component for the further examples. When the system has reached the ground states, where no dynamics is expected, the population curves exhibit a slight deviation from the quantum expectation values for both N = 2 and 20. Additionally, spikes are observed in the intensity curves for N = 2. For larger N , the number of unstable trajectories increases. The observed discrepancy suggests that, although the excited state is depopulated, a nontrivial steady state forms, possessing specific correlations between the ground states.
As in the previous section, we also consider the ensemble prepared in a mixed state without coherences. We assume that all levels are initially populated as follows:
ρ33(0) = 0.5, ρ22(0) = ρ11(0) = 0.25,
and other matrix elements are zero. The solution reveals that the ensemble does not relax completely to the ground states but evolves into a steady state with some population remaining in the excited state, as in Fig. 10 (a). The formation of this state is accompanied by unstable behavior of the three-body correlator, which does not converge after tγ ≈ 1.0. The same issues appear when the excited state is incoherently pumped with the following additional term in the equations:
ρ ̇33(t) = . . . + κ(t) ρ00(t),
where κ(t) defines the pump profile, and ρ00(t) satisfies Eq. (30). The final state is also a steady state with a nonzero probability of finding an excited atom, as shown in Fig. 10 (d). The stochastic averages converge to incorrect values, and the three-body operator becomes unstable for later time moments. We attempt to regularize these issues by introducing non-radiative damping of the excited state to the ground states (3 → 1, 2) with a rate Γ
ρ ̇33(t) = . . . − 2Γρ33(t), (32a)
ρ ̇gg(t) = . . . + Γρ33(t), (32b)
ρ ̇g3(t) = . . . − Γρg3(t), (32c)
ρ ̇3g(t) = . . . − Γρ3g(t), (32d)


 18
ef
d
bc
a
FIG. 10. The dynamics of an ensemble of N = 20 atoms with the Λ-type level structure depicted in Fig. 9 (a). The figure composition is the same as in Fig. 8. Semi-transparent lines represent quantum expectation values, while opaque lines show stochastic averages. The upper row (a, b, c) considers atoms starting from the mixed initial state ρ11(0) = ρ22(0) = 0.25 and ρ33(0) = 0.50, with the rest being zero. The lower row (d, e, f) shows atoms being incoherently pumped. To address convergence issues, non-radiative damping of the excited state at rate Γ is introduced (see Eqs. (32)). The gray line shows the evolution of ρ00(t). Unstable realizations omitted: (a) 2383 (2.38%); (b) 985 (0.99%); (c) 735 (0.74%); (d) 1550 (1.55%); (e) 351 (0.35%); (f) 159 (0.16%). Both polarization components of intensity exhibit identical profiles, so only one is depicted.


 19
where g = 1, 2. Consequently, the excited state is depopulated at a rate of 2Γ. We found the damping rates sufficient to regularize populations and intensities in Fig. 10 (b, c) and (e, f). However, the three-operator correlator still does not converge, although it shows a right trend. A possible explanation is that the ensemble does not simply evolve into a mixture of ground states. Calculations based on Ref. [28] reveal that the system in Fig. 10 (c) evolves into a steady state with the following non-zero correlation:
⟨ρ(ss)
12 ρ(ss)
21 ⟩ < 0, (33)
where ss stands for steady state. As the product
ρ(ss)
12 ρ(ss)
21 becomes negative upon averaging, it indicates that the coherences ρ12(t) and ρ21(t) are non-Hermitian at the level of single realizations. This nontrivial dynamics may cause slow convergence of the three-operator correlators observed in Fig. 10. The coherences between the ground states ρg1̸=g2 (t) are not damped by any additional non-radiative decay, which does not prevent slow convergence of the observables involving ρg1̸=g2 (t), such as the analyzed three-particle correlator. Effective regularization would require either stronger decoherence to prevent the buildup of the correlations or the introduction of another dissipation channel for ρg1̸=g2 (t).
V. DISCUSSION
A. Computational effort
Firstly, we address the issue of computational efficiency. Table I provides clear evidence of the effectiveness of the stochastic methodology. For each system analyzed in this article, we compare the average computational time required to simulate a single stochastic trajectory with that of a full quantum-mechanical simulation. The stochastic methodology allows parallelization and remains independent of N across all the examples provided. In contrast, the polynomial complexity of full quantum-mechanical calculations sharply raises the computational time with an increase in N . The performance of the stochastic method is primarily determined by the number of atomic levels M , which defines the number of underlying stochastic differential equations M 2. As depicted in Fig. 3, convergence of stochastic averages for chosen observables is typically achieved with 102–103 trajectories. Based on numerical simulations, pumped V and Λ systems also require 103 trajectories to achieve good agreement with the quantum-mechanical simulations. Even without parallelization, the stochastic simulations for the twenty pumped V -systems demonstrated in Fig. 8 (c) take between 3 and 30 seconds, noticeably less than the 178 seconds required by full quantummechanical calculations. For larger N and with the implementation of parallelization, the difference becomes even more pronounced.
High-order correlation functions
Another crucial aspect is the convergence of various expectation values. The higher the order of the correlation function, the more pronounced the challenges with convergence become. This issue is consistently observed when the system reaches a special steady state, leading to the effective density matrix ρpq(t) becoming nonHermitian at the level of individual realizations. This problem was demonstrated in the context of superfluorescence from two-level atoms in Sec. IV A and discussed following Eq. (29). A similar concern was addressed in the context of a Λ-type system after Eq. (33) in Sec. IV D. Our drift gauge is designed to ensure the Hermitian behavior of the effective density matrix, and finding appropriate gauging methods to address these steady states remains an open challenge. In our approach, the convergence issue can only be avoided by introducing additional dissipation for the problematic steady states.
B. Unstable trajectories
Despite the expectation that stochastic gauges can reduce instabilities, almost every numerical example in Sec. IV features unstable trajectories, which we associate with the presence of specific steady states. Keeping these unstable trajectories causes large spikes in the temporal profiles of the averages. A larger statistical sample does not smooth the curves; instead, it leads to more diverging trajectories and a higher number of spikes after averaging. Therefore, we omit the unstable trajectories, as detailed in Sec. III C. Fig. 11 shows the percentage of omitted trajectories for different level schemes and numbers of emitters, focusing on systems with incoherent pumping. Since incoherent decay processes can mitigate steady-state problems and divergences, each panel in Fig. 11 displays multiple simulations with different decay rates Γ. Qualitatively, each system exhibits similar behavior. Beyond a certain number of atoms, the percentage of omitted trajectories grows faster. This behavior systematically shifts to larger numbers of atoms with an increase in decay rate Γ. We expect that the simulations yield more trustworthy results when the percentage of disregarded trajectories decreases.
C. Stochastic gauging
Since both the gauged and ungauged equations can yield diverging trajectories, comparing simulations based on them could provide valuable insights. We revisit the example of pumped two-level systems discussed in Sec. IV B. Specifically, we focus on the scenario depicted in Fig. 6 (f) with Γ = 0.3γ. Fig. 12 presents two examples, one with N = 100 and another with N = 1000. For N = 100, a quantum-mechanical solution is also included


 20
TABLE I. Comparison of computational efforts between the stochastic and quantum-mechanical methods. Each row corresponds to an individual atomic system investigated in the article. The computational time for solving the master equation is averaged over 10 runs. The time required to integrate a single stochastic trajectory (along with one standard deviation) is evaluated based on over 100 realizations. The asterisk (*) in front of the figure number indicates that the simulations are conducted under identical conditions but with a different number of atoms.
for comparison. Panels (a), (b), (f), and (g) demonstrate simulations based on the gauged equations. The statistical averages shown in panels (a) and (f) are based on all realizations, including the unstable ones, which have large weight coefficients and significantly impact the resulting curves. After excluding 500 unstable realizations, the curves become much smoother, as shown in panels (b) and (g). In particular, panel (b) shows that removing these unstable realizations leads to a good agreement with the full quantum-mechanical simulations. Panels (c)-(e) and (h)-(j) showcase simulations based on the ungauged stochastic differential equations. Comparing panels (a) and (c), we observe that convergence issues emerge earlier with the ungauged equations. Panels (d) and (e) illustrate how the averages change as unstable trajectories are gradually removed. Notably, the ungauged equations produce significantly more unstable trajectories than the gauged ones. Furthermore, removing these unstable trajectories does not improve the averages, as evidenced by comparisons with the full quantummechanical simulations. Although we cannot compare the stochastic methodology with full quantum-mechanical simulations for N = 1000, a visual inspection suggests that the gauged simulations yield more physically accurate results. Comparing panels (f) and (h), we notice that convergence issues arise earlier with the ungauged equations. Panels (i) and (j) demonstrate that removing unstable trajectories leads to negative intensities when stochastic gauging is not ap
plied. This unphysical behavior does not occur in the gauged simulations shown in panel (g). The discrepancy between simulations based on the ungauged equations and those based on the full quantummechanical approach is not always as drastic as in the example of pumped two-level systems. For instance, superfluorescence in N = 20 Λ-systems, studied in Sec. IV D, can be accurately modeled using both the gauged and ungauged equations. However, the gauged equations exhibit slightly more unstable behavior due to the influence of the weight coefficient. This suggests that the gauging condition proposed in Sec. III C can be further refined, which is a topic for future investigations.
D. Weight function
After highlighting the importance of stochastic gauging, let us discuss some of its specifics. In all our numerical illustrations, we employ the drift gauging technique by modifying the deterministic terms only during the amplification of emission, specifically when Re(ρee−ρgg) ≥ 0 for any excited state |e⟩ and ground state |g⟩. In exchange for this modification we introduce the weight function Ω(t), which assigns a statistical weight to each trajectory. Additionally, we constantly apply the diffusion gauge that rescales noise terms. Although the drift gauge can, in principle, be applied constantly, this approach leads to inaccurate simulations due to the exponential


 21
bc
a
FIG. 11. Percentage of omitted trajectories for different level schemes, numbers of emitters and decay rates Γ. Panel (a) depicts pumped two-level systems (Sec. IV B), panel (b) pumped V systems (Sec. IV C), and panel (c) pumped Λ systems (Sec. IV D).
e
bcd
a
j
gh i
f
FIG. 12. Simulations of population dynamics and intensity profiles for pumped two-level systems (Sec. IV B), comparing gauged and ungauged equations for N = 100 and N = 1000. The semi-transparent lines correspond to quantum expectation values. The opaque lines represent stochastic averages. The top row shows simulations for N = 100 based on gauged equations with all realizations (a) and with 500 unstable realizations omitted (b), and ungauged equations with all realizations (c), 205 most diverging realizations omitted (d), and all 13 464 diverging realizations omitted (e). The bottom row shows simulations for N = 1000 based on gauged equations with all realizations (f) and with 1745 unstable realizations omitted (g), and ungauged equations with all realizations (h), 65 most diverging realizations omitted (i), and all 4442 diverging realizations omitted (j).


 22
cd
ab e
FIG. 13. Numerical simulations of the population dynamics and intensity profiles of superfluorescence in 100 pumped two-level atoms studied in Sec. IV B, comparing different gauging strategies. Here, we introduce stronger non-radiative decay with a rate of Γ = 0.8γ. The semi-transparent lines correspond to quantum expectation values, while the opaque lines represent stochastic averages. (a) The drift gauge is applied only when population inversions are positive, with averaging performed with the weight function Ω(t). The gray-filled area shows gauging frequency. (b) Constant application of the drift gauge with the weight function. The results show strong intensity spikes and incorrect averages. (c) Similar to panel (a), but averaging is done without the weight function. The expectation values are similar to (a) with a slight discrepancy in intensity around tγ = 2. (d) Constant application of the drift gauge without the weight function. The expectation values worsen compared to (b), with discrepancies appearing earlier. (e) Ungauged simulations provided for comparison, demonstrating the necessity of gauging for accurate results.
growth of the weight function. However, when the gauging is applied carefully, following the guidance in Sec. III C, our simulations yield correct results. Similarly to Sec. V C, we consider an example of N = 100 pumped two-level atoms. Here, we introduce a stronger non-radiative decay, specifically, Γ = 0.8 γ. In Fig. 13 (a), the drift gauge is utilized only when there is an amplification of emission and the statistical averages include the weight function Ω(t). The grayshaded area in the plot illustrates how frequently the drift gauge is applied. On average, the drift gauge is mostly applied until the mean intensity reaches its peak. After this peak, the probability of applying the gauge drops abruptly to zero. In the opposite case, when the drift gauge is constantly applied, the obtained averages are incorrect, as demonstrated in Fig. 13 (b). More unstable trajectories are observed, and the expectation values exhibit many spikes. This clearly shows that the drift gauge should be applied as rarely as possible and only when necessary. When the drift gauge is used carefully and the system features sufficiently strong dissipation, the weight function Ω(t) becomes less important. To demonstrate this, simulations in Fig. 13 feature a higher dissipation rate compared to those in Fig. 12. As shown in Fig. 13 (c), if we apply the drift and diffusion gauge as suggested in Sec. III C but without using the weight function, the ex
pectation values remain almost the same as in Fig. 13 (a). Only the intensity curve shows a small discrepancy around tγ = 2.0. Additionally, since the weight coefficient does not enter expectation values, there are no unstable trajectories in the simulations shown in panel (c). Notably, in the case when simulations are constantly gauged, omitting the weight function makes expectation values even worse, as suggested by comparing panel (d) with panel (b). Although the spikes disappear, discrepancies between the statistical and quantum-mechanical approaches appear earlier. Remarkably, not using the weight function results in fewer discrepancies compared to the unnecessary application of the drift gauge. Since the weight function does not significantly impact the results, it is worth exploring whether gauging is necessary at all. Panel (e) displays the expectation values based on the ungauged equations. These expectation values considerably deviate from the exact solution, unlike cases in panels (a) and (c), proving that stochastic gauging is indeed necessary and improves the stability and accuracy of the simulations, even without the weight function. It is important to note that omitting the weight function significantly changes the expectation values if the dissipation is not sufficiently strong. Specifically, if the simulations shown in Figs. 12 (b) and (g) had not in


 23
cluded the weight function, the intensity curves would have featured a characteristic dip below zero, as observed in Fig. 12 (j). Therefore, we conclude that the weight coefficient can be safely disregarded when the system features strong dissipation processes, a condition typically encountered in experiments.
VI. CONCLUSION
The main achievement of this work is the development of a numerically efficient formalism, grounded in first principles, that reliably characterizes collective spontaneous emission for any number of multi-level emitters, especially in the presence of incoherent processes, within established bounds of applicability. In this work, we focused on compact systems for benchmarking our methodology, as they can be solved exactly through quantum state decomposition. While our methodology generally yielded satisfactory results across a wide parameter range, we uncovered discrepancies when the system entered specific steady states. We showed that the presence of incoherent processes mitigated these issues. Crucially, our formalism is characterized by equations that do not depend on the number of emitters, eliminating the numerical difficulties associated with traditional techniques based on quantum state decomposition. Throughout the article, we have examined various scenarios and cases, from cooperative emission of instantly excited two-level atoms to complex multi-level systems, such as V - and Λ-type systems, showcasing the versatility
and performance of our methodology. Our formalism has broad applicability for studying superfluorescence and superradiance across different spectral regions and emitter level structures. In particular, the approach offers an extension to previous methodologies [4, 10] and incorporates the preparation of the excited state manifold through pumping. While our numerical examples primarily focus on superfluorescence initiated by full inversion or incoherent pumping, the versatility of our proposed formalism enables the examination of systems characterized by initial macroscopic dipole moments and seeding fields resonant with atomic transitions. Additionally, the stochastic formalism can address superfluorescence in distributed media [44, 73], allowing for the study of propagation effects. Our work offers valuable insights into the numerical challenges of simulating superfluorescence, the performance and limitations of our methodology, and its practical applicability in studying this fascinating quantum phenomenon.
ACKNOWLEDGMENTS
S.C. and V.S. acknowledge the financial support of Grant-No. HIDSS-0002 DASHH (Data Science in Hamburg-Helmholtz Graduate School for the Structure of the Matter). V.S. acknowledges the financial support of the Cluster of Excellence “CUI: Advanced Imaging of Matter” of the Deutsche Forschungsgemeinschaft (DFG) — EXC 2056 — project ID 390715994.
[1] R. H. Dicke, Coherence in Spontaneous Radiation Processes, Phys. Rev. 93, 99 (1954). [2] G. S. Agarwal, Master-Equation Approach to Spontaneous Emission, Phys. Rev. A 2, 2038 (1970). [3] R. H. Lehmberg, Radiation from an N -Atom System. I. General Formalism, Phys. Rev. A 2, 883 (1970). [4] M. Gross and S. Haroche, Superradiance: An essay on the theory of collective spontaneous emission, Physics Reports 93, 301 (1982). [5] R. K. Bullough, Photon, quantum and collective, effects from Rydberg atoms in cavities, Hyperfine Interactions 37, 71 (1987). [6] A. A. Svidzinsky, J.-T. Chang, and M. O. Scully, Cooperative spontaneous emission of N atoms: Many-body eigenstates, the effect of virtual Lamb shift processes, and analogy with radiation of N classical oscillators, Phys. Rev. A 81, 053821 (2010). [7] O. Rubies-Bigorda, S. Ostermann, and S. F. Yelin, Characterizing superradiant dynamics in atomic arrays via a cumulant expansion approach, Phys. Rev. Res. 5, 013091 (2023). [8] N. Skribanowitz, I. P. Herman, J. C. MacGillivray, and M. S. Feld, Observation of Dicke Superradiance in Optically Pumped HF Gas, Phys. Rev. Lett. 30, 309 (1973).
[9] H. M. Gibbs, Q. H. F. Vrehen, and H. M. J. Hikspoors, Single-Pulse Superfluorescence in Cesium, Phys. Rev. Lett. 39, 547 (1977). [10] Q. H. F. Vrehen and M. F. H. Schuurmans, Direct Measurement of the Effective Initial Tipping Angle in Superfluorescence, Phys. Rev. Lett. 42, 224 (1979). [11] P. Cahuzac, H. Sontag, and P. Toschek, Visible superfluorescence from atomic europium, Optics Communications 31, 37–41 (1979). [12] M. S. Malcuit, J. J. Maki, D. J. Simkin, and R. W. Boyd, Transition from superfluorescence to amplified spontaneous emission, Phys. Rev. Lett. 59, 1189 (1987). [13] G. Raino`, M. A. Becker, M. I. Bodnarchuk, R. F. Mahrt, M. V. Kovalenko, and T. Sto ̈ferle, Superfluorescence from lead halide perovskite quantum dot superlattices, Nature 563, 671 (2018). [14] C. Bradac, M. T. Johnsson, M. van Breugel, B. Q. Baragiola, R. Martin, M. L. Juan, G. K. Brennen, and T. Volz, Room-temperature spontaneous superradiance from single diamond nanocrystals, Nature Communications 8, 10.1038/s41467-017-01397-4 (2017). [15] W. Guerin, M. O. Ara ́ujo, and R. Kaiser, Subradiance in a Large Cloud of Cold Atoms, Phys. Rev. Lett. 116, 083601 (2016).


 24
[16] D. C. Gold, P. Huft, C. Young, A. Safari, T. G. Walker, M. Saffman, and D. D. Yavuz, Spatial Coherence of Light in Collective Spontaneous Emission, PRX Quantum 3, 010338 (2022). [17] R. Ro ̈hlsberger, K. Schlage, B. Sahoo, S. Couet, and R. Ru ̈ffer, Collective Lamb Shift in Single-Photon Superradiance, Science 328, 1248 (2010). [18] A. Flusberg, T. Mossberg, and S. Hartmann, Observation of Dicke superradiance at 1.30 μm in atomic Tl vapor, Physics Letters A 58, 373–374 (1976). [19] M. Gross, C. Fabre, P. Pillet, and S. Haroche, Observation of Near-Infrared Dicke Superradiance on Cascading Transitions in Atomic Sodium, Physical Review Letters 36, 1035–1038 (1976). [20] M. Gross, P. Goy, C. Fabre, S. Haroche, and J. M. Raimond, Maser Oscillation and Microwave Superradiance in Small Systems of Rydberg Atoms, Physical Review Letters 43, 343–346 (1979). [21] L. Moi, P. Goy, M. Gross, J. M. Raimond, C. Fabre, and S. Haroche, Rydberg-atom masers. I. A theoretical and experimental study of super-radiant systems in the millimeter-wave domain, Physical Review A 27, 2043–2064 (1983). [22] N. Rohringer, D. Ryan, R. A. London, M. Purvis, F. Albert, J. Dunn, J. D. Bozek, C. Bostedt, A. Graf, R. Hill, S. P. Hau-Riege, and J. J. Rocca, Atomic inner-shell Xray laser at 1.46 nanometres pumped by an X-ray freeelectron laser, Nature 481, 488 (2012). [23] C. Weninger, M. Purvis, D. Ryan, R. A. London, J. D. Bozek, C. Bostedt, A. Graf, G. Brown, J. J. Rocca, and N. Rohringer, Stimulated Electronic X-Ray Raman Scattering, Phys. Rev. Lett. 111, 233902 (2013). [24] H. Yoneda, Y. Inubushi, K. Nagamine, Y. Michine, H. Ohashi, H. Yumoto, K. Yamauchi, H. Mimura, H. Kitamura, T. Katayama, T. Ishikawa, and M. Yabashi, Atomic inner-shell laser at 1.5- ̊angstro ̈m wavelength pumped by an X-ray free-electron laser, Nature 524, 446 (2015). [25] T. Kroll, C. Weninger, R. Alonso-Mori, D. Sokaras, D. Zhu, L. Mercadier, V. P. Majety, A. Marinelli, A. Lutman, M. W. Guetg, F.-J. Decker, S. Boutet, A. Aquila, J. Koglin, J. Koralek, D. P. DePonte, J. Kern, F. D. Fuller, E. Pastor, T. Fransson, Y. Zhang, J. Yano, V. K. Yachandra, N. Rohringer, and U. Bergmann, Stimulated X-Ray Emission Spectroscopy in Transition Metal Complexes, Phys. Rev. Lett. 120, 133203 (2018). [26] L. Mercadier, A. Benediktovitch, C. Weninger, M. A. Blessenohl, S. Bernitt, H. Bekker, S. Dobrodey, A. Sanchez-Gonzalez, B. Erk, C. Bomme, R. Boll, Z. Yin, V. P. Majety, R. Steinbru ̈gge, M. A. Khalal, F. Penent, J. Palaudoux, P. Lablanquie, A. Rudenko, D. Rolles, J. R. Crespo Lo ́pez-Urrutia, and N. Rohringer, Evidence of Extreme Ultraviolet Superfluorescence in Xenon, Phys. Rev. Lett. 123, 023201 (2019). [27] R. E. F. Silva and J. Feist, Permutational symmetry for identical multilevel systems: A second-quantized approach, Physical Review A 105, 10.1103/physreva.105.043704 (2022). [28] V. Sukharnikov, S. Chuchurka, A. Benediktovitch, and N. Rohringer, Second quantization of open quantum systems in Liouville space, Physical Review A 107, 10.1103/physreva.107.053707 (2023). [29] M. Gegg and M. Richter, Efficient and exact numerical approach for many multi-level systems in open system
CQED, New Journal of Physics 18, 043037 (2016). [30] G. Slavcheva, J. Arnold, and R. Ziolkowski, FDTD Simulation of the Nonlinear Gain Dynamics in Active Optical Waveguides and Semiconductor Microcavities, IEEE Journal of Selected Topics in Quantum Electronics 10, 1052 (2004). [31] O. Larroche, D. Ros, A. Klisnick, A. Sureau, C. Mo ̈ller, and H. Guennou, Maxwell-Bloch modeling of x-ray-lasersignal buildup in single- and double-pass configurations, Phys. Rev. A 62, 043815 (2000). [32] H.-T. Chen, T. E. Li, M. Sukharev, A. Nitzan, and J. E. Subotnik, Ehrenfest+R dynamics. I. A mixed quantum–classical electrodynamics simulation of spontaneous emission, The Journal of Chemical Physics 150, 044102 (2019). [33] T. E. Li, H.-T. Chen, and J. E. Subotnik, Comparison of Different Classical, Semiclassical, and Quantum Treatments of Light–Matter Interactions: Understanding Energy Conservation, Journal of Chemical Theory and Computation 15, 1957 (2019). [34] S. Krusˇiˇc, K. Buˇcar, A. Miheliˇc, and M. Zˇitnik, Collective effects in the radiative decay of the 2 1P state in helium, Phys. Rev. A 98, 013416 (2018). [35] A. Benediktovitch, V. P. Majety, and N. Rohringer, Quantum theory of superfluorescence based on two-point correlation functions, Physical Review A 99, 013839 (2019). [36] P. D. Drummond and M. S. Hillery, The quantum theory of nonlinear optics (Cambridge University Press, 2014). [37] P. Deuar and P. D. Drummond, Stochastic gauges in quantum dynamics for many-body simulations, Computer Physics Communications 142, 442 (2001), arXiv:quant-ph/0203108 [quant-ph]. [38] S. W ̈uster, J. F. Corney, J. M. Rost, and P. Deuar, Quantum dynamics of long-range interacting systems using the positive-P and gauge-P representations, Phys. Rev. E 96, 013309 (2017). [39] P. Deuar and P. D. Drummond, Correlations in a BEC Collision: First-Principles Quantum Dynamics with 150 000 Atoms, Phys. Rev. Lett. 98, 120402 (2007). [40] P. Deuar, A. Ferrier, M. Matuszewski, G. Orso, and M. H. Szyman ́ska, Fully Quantum Scalable Description of Driven-Dissipative Lattice Models, PRX Quantum 2, 010319 (2021). [41] A. Gilchrist, C. W. Gardiner, and P. D. Drummond, Positive P representation: Application and validity, Phys. Rev. A 55, 3014 (1997). [42] P. Deuar and P. D. Drummond, First-principles quantum dynamics in interacting Bose gases II: stochastic gauges, Journal of Physics A: Mathematical and General 39, 2723 (2006). [43] P. Deuar, First-principles quantum simulations of manymode open interacting Bose gases using stochastic gauge methods, arXiv:cond-mat/0507023 (2005), arXiv: condmat/0507023. [44] S. Chuchurka, A. Benediktovitch, i. c. v. Kruˇsiˇc, A. Halavanau, and N. Rohringer, Stochastic modeling of x-ray superfluorescence, Phys. Rev. A 109, 033725 (2024). [45] R. Friedberg and S. R. Hartmann, Temporal evolution of superradiance in a small sphere, Physical Review A 10, 1728 (1974). [46] J. P. Clemens, L. Horvath, B. C. Sanders, and H. J. Carmichael, Collective spontaneous emission from a line of atoms, Physical Review A 68, 023809 (2003).


 25
[47] R. T. Sutherland and F. Robicheaux, Collective dipoledipole interactions in an atomic array, Physical Review A 94, 013847 (2016). [48] D. Comparat and P. Pillet, Dipole blockade in a cold Rydberg atomic sample, Journal of the Optical Society of America B 27, A208 (2010). [49] S. J. Masson and A. Asenjo-Garcia, Universality of Dicke superradiance in arrays of quantum emitters, Nature Communications 13, 2285 (2022). [50] E. Sierra, S. J. Masson, and A. Asenjo-Garcia, Dicke Superradiance in Ordered Lattices: Dimensionality Matters, Physical Review Research 4, 023207 (2022). [51] F. Andreoli, M. J. Gullans, A. A. High, A. Browaeys, and D. E. Chang, Maximum Refractive Index of an Atomic Medium, Physical Review X 11, 10.1103/physrevx.11.011026 (2021). [52] E. V. Goldstein and P. Meystre, Dipole-dipole interaction in optical cavities, Physical Review A 56, 5135 (1997). [53] J. M. Raimond, P. Goy, M. Gross, C. Fabre, and S. Haroche, Statistics of Millimeter-Wave Photons Emitted by a Rydberg-Atom Maser: An Experimental Study of Fluctuations in Single-Mode Superradiance, Physical Review Letters 49, 1924 (1982). [54] T. Laske, H. Winter, and A. Hemmerich, Pulse Delay Time Statistics in a Superradiant Laser with Calcium Atoms, Physical Review Letters 123, 10.1103/physrevlett.123.103601 (2019). [55] M. O. Scully and M. S. Zubairy, Quantum optics (1999). [56] J. H. Eberly, N. B. Narozhny, and J. J. SanchezMondragon, Periodic Spontaneous Collapse and Revival in a Simple Quantum Model, Physical Review Letters 44, 1323 (1980). [57] P. Meystre and M. Sargen, Elements of Quantum Optics (Springer Berlin Heidelberg, 2007).
[58] M. Gegg, Identical Emitters, Collective Effects and Dissipation in Quantum Optics (Technische Universita ̈t Berlin, 2017). [59] C. Rackauckas and Q. Nie, DifferentialEquations.jl – A Performant and Feature-Rich Ecosystem for Solving Differential Equations in Julia, Journal of Open Research Software 5, 15 (2017). [60] G. N. Milstein and M. V. Tretyakov, Stochastic Numerics for Mathematical Physics, Scientific Computation (Springer Berlin Heidelberg, Berlin, Heidelberg, 2004) pp. 82,167. [61] G. Maruyama, Continuous markov processes and stochastic equations, Rendiconti del Circolo Matematico di Palermo 4, 48–90 (1955). [62] C. Weninger and N. Rohringer, Transient-gain photoionization x-ray laser, Phys. Rev. A 90, 063828 (2014). [63] E. B. Aleksandrov, Optical measurements of the interference of nondegenerate atomic states, Soviet Physics Uspekhi 15, 436 (1973). [64] H. Bitto and J. Robert Huber, Molecular quantum beat spectroscopy, Optics Communications 80, 184 (1990). [65] Y. Hikosaka, H. Iwayama, and T. Kaneyasu, Zeeman quantum beats of helium Rydberg states excited by synchrotron radiation, Journal of Synchrotron Radiation 27, 675 (2020). [66] A. C. LaForge, A. Benediktovitch, V. Sukharnikov, Sˇ. Krusˇicˇ, M. Zˇitnik, M. Debatin, R. W. Falcone, J. D. Asmussen, M. Mudrich, R. Michiels, F. Stienkemeier, L. Badano, C. Callegari, M. D. Fraia, M. Ferianis, L. Giannessi, O. Plekan, K. C. Prince, C. Spezzani,
N. Rohringer, and N. Berrah, Time-resolved quantum beats in the fluorescence of helium resonantly excited by XUV radiation, Journal of Physics B: Atomic, Molecular and Optical Physics 53, 244012 (2020). [67] E. Gerdau, R. R ̈uffer, R. Hollatz, and J. P. Hannon, Quantum Beats from Nuclei Excited by Synchrotron Radiation, Physical Review Letters 57, 1141 (1986). [68] Q. H. F. Vrehen, H. M. J. Hikspoors, and H. M. Gibbs, Quantum Beats in Superfluorescence in Atomic Cesium, Physical Review Letters 38, 764 (1977). [69] D. Bartholdtsen and R. H. Rinkleff, Superfluorescent transitions in an external magnetic field, Zeitschrift fuer Physik D Atoms, Molecules and Clusters 30, 265 (1994). [70] S. Haroche, Quantum beats and time-resolved fluorescence spectroscopy, in Topics in Applied Physics (Springer Berlin Heidelberg, 1976) pp. 253–313. [71] J. Gea-Banacloche, M. O. Scully, and M. S. Zubairy, Vacuum Fluctuations and Spontaneous Emission in Quantum Optics, Physica Scripta T21, 81 (1988). [72] R. S. Liptser and A. N. Shiryayev, Statistics of Random Processes I (Springer New York, 1977). [73] S. Chuchurka, V. Sukharnikov, and N. Rohringer, Hermitian stochastic methodology for x-ray superfluorescence, Phys. Rev. A 109, 063705 (2024).
Appendix A: Stochastic gauges
In Refs. [42, 43], the derivation of the stochastic gauge transformation was based on the freedom in decomposing the density matrix in terms of projectors constructed from coherent states. On one hand, the projectors are not defined uniquely; on the other hand, these projectors are analytical functions of their arguments, providing even more freedom. All of these observations indicate that the probabilistic interpretation of the density matrix is not unique. Since it is sampled using stochastic equations, the choice of these equations is also not unique. The most natural choice of stochastic equations does not necessarily lead to a stable numerical solution. Stochastic gauges offer the possibility of finding a more stable system of equations. To apply stochastic gauges to our equations, we introduce stochastic freedom in a broader context. Let’s start by investigating an arbitrary system of stochastic differential equations that yield a vector of stochastic processes, denoted as x(t). The exact form of these equations and their origin may be disregarded in this appendix. Consider the following characteristic function:
χ(λ, t) =
D
exp λ · x(t)
E
. (A1)
Its derivatives provide all the necessary information to calculate any expectation values of interest, namely:
⟨f [x(t)]⟩ = f ∂
∂λ χ(λ, t)
λ=0
.
Consequently, χ(λ, t) is uniquely defined in the vicinity of λ = 0, since its derivatives at the point λ = 0 determine all observables.


 26
Now, consider another system of equations that generates a different vector of stochastic processes, denoted as x′(t), but yields exactly the same expectation values. The corresponding characteristic functions χ′(λ, t) must be identical to χ(λ, t):
χ(λ, t) = χ′(λ, t). (A2)
The explicit form of the stochastic trajectories x(t) or x′(t) is unknown, and only their stochastic differential equations are provided. Therefore, we cannot immediately construct the corresponding characteristic functions and compare them. We can only proceed in the spirit of mathematical induction. First, we ensure that the initial conditions for x′(0) lead to the same characteristic function, satisfying Eq. (A2) at t = 0. Then, assuming that Eq. (A2) holds for later times t, we guarantee that the temporal derivatives of the characteristic functions are preserved:
∂
∂t χ(λ, t) = ∂
∂t χ′(λ, t) (A3)
The possibility of having multiple equivalent differential equations arises from the fact that the involved stochastic processes are, generally speaking, complex. In other words, the components of the vectors x(t) and x′(t) are, in reality, pairs of independent dynamic variables. However, the construction of expectation values does not involve these variables separately. In Eq. (A1), the derivative with respect to λ cannot extract only the real or imaginary part of xi(t). This property is the key source of stochastic freedom.
Appendix B: Drift gauge
To provide an example of how the concept of stochastic gauge transformations from Appendix A can be applied, we will derive the so-called drift gauge [43] in the spirit of Girsanov’s theorem [72]. In certain cases, stochastic differential equations take the form
dx(t)
dt = A(x(t), t) + ξ(x(t), t)
where the drift terms A(x, t) can lead to diverging stochastic trajectories. Here, ξ(x, t) represents Gaussian white noise terms with zero first moments and arbitrary second-order correlators. Unfortunately, neglecting diverging trajectories can result in incorrect expectation values. To tackle the numerical instability of divergent trajectories, one can opt for different stochastic equations with alternative drift terms. We will denote the new solution as x′(t) and the alternative drift term as A′(x′, t). The new stochastic differential equations have the same initial conditions and read as follows:
dx′(t)
dt = A′(x′, t) + ξ(x′(t), t)
To compensate for this change, one can introduce a weight coefficient Ω(t) = eC0(t), which can be used to calculate expectation values based on the new stochastic variables:
⟨f (x(t))⟩ = ⟨f (x′(t))Ω(t)⟩.
Consequently, the new characteristic function has the following form:
χ′(λ, t) =
D
exp λ · x′(t) + C0(t)
E
.
We can always formally write an equation of motion for C0(t):
dC0(t)
dt = A0(x′(t), t) + ξ0(x′(t), t),
where A0 is a new drift and ξ0 is a new Gaussian white noise term. We assume that ξ0(x, t) has a zero average and yet unknown correlation properties:
⟨ξ0(x, t)ξ0(x, t′)⟩ = σ0(x, t)δ(t − t′),
⟨ξ(x, t)ξ0(x, t′)⟩ = σ(x, t)δ(t − t′).
The main goal is to find the drift A0 for the weight coefficient and the correlation properties σ0 and σ that com
pensate for the change in drift terms ∆A = A′ − A at the level of the characteristic function. Following Appendix A, we proceed in the spirit of mathematical induction and assume that χ′(λ, t) = χ(λ, t) is satisfied for a certain t. Let’s check if the same holds for the derivatives:
∂
∂t [χ′(λ, t) − χ(λ, t)]
= λ · ∆A ∂
∂λ, t + σ ∂
∂λ, t
A0
∂
∂λ, t + 1
2 σ0
∂
∂λ, t
!
χ(λ, t) .
In the derivation of this expression, we have used Itˆo’s lemma from Eq. (16). To make the right-hand side equal to zero for any λ, we have to choose the following correlation properties for the noise terms:
⟨ξ0(x, t)ξ0(x, t′)⟩ = −2A0(x, t)δ(t − t′),
⟨ξ(x, t)ξ0(x, t′)⟩ = −∆A(x, t)δ(t − t′).
This constitutes the essence of the drift gauge. Notably, our derivations are not based on the properties of projectors used to decompose the density matrix; our result is applicable to any system of stochastic trajectories, including the modified Bloch equations for the variables ρpq (t).


 27
Appendix C: Diffusion gauge
In this section, we provide the expressions for ηα(t) and θα(t) used in our numerical simulations. These expressions are derived by substituting the decomposition from
Eq. (25) into the expression in Eq. (26). Subsequently, we minimize this expression with respect to ηα(t) and θα(t), aiming to mitigate the amplification of non-Hermitian components. The resulting functions, ηα(t) and θα(t), take the following form:
η4
β(t) =
P
α P (ee)
αβ (t) − P (+)
α (t)P (−)
β (t)
2
+ P (−)
α (t)P (−)
β (t)
2
P
α P (ee)
βα (t) − P (gg)
αβ (t)
2,
θ4
β(t) =
P
α P (ee)
βα (t) − P (+)
β (t)P (−)
α (t)
2
+ P (+)
α (t)P (+)
β (t)
2
P
α P (ee)
αβ (t) − P (gg)
βα (t)
2,
where for simplicity we introduced the following tensors:
P (gg)
αβ (t) =
X
e,g,g′
deg,α ρgg′ (t) dg′e,β ,
P (ee)
αβ (t) =
X
e,e′ ,g
dge,α ρee′ (t) de′g,β .
and the following vectors that are stochastic counterparts of the polarization fields:
P(+)(t) =
X
e,g
dge ρeg(t),
P(−)(t) =
X
e,g
deg ρge(t).
