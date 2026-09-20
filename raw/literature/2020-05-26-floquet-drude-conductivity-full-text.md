# Floquet-Drude conductivity - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevB.101.184204
> Collected: 2026-09-20
> Published: 2020-05-26
> Zotero parent key: Q5C8CDDV
> Evidence: Zotero indexed PDF text

PHYSICAL REVIEW B 101, 184204 (2020)
Floquet-Drude conductivity
Martin Wackerl ,* Paul Wenk ,† and John Schliemann‡
Institute for Theoretical Physics, University of Regensburg, 93040 Regensburg, Germany
(Received 26 November 2019; revised manuscript received 18 March 2020; accepted 21 April 2020; published 26 May 2020)
A generalization of the Drude conductivity for systems which are exposed to periodic driving is presented. The probe bias is treated perturbatively by using the Kubo formula, whereas the external driving is included nonperturbatively using the Floquet theory. Using a different type of four-times Green functions disorder is approached diagrammatically, yielding a fully analytical expression for the Floquet-Drude conductivity. Furthermore, the Floquet Fermi “golden rule” is generalized to t-t′ Floquet states, connecting the Floquet-Dyson series with scattering theory for Floquet states. It is shown that a low-energy approximation like the parabolic one fails significantly to give the correct conductivity in a system under driving.
DOI: 10.1103/PhysRevB.101.184204
I. INTRODUCTION
Paul Drude published his theory of electric transport in metals as long ago as 1900 [1,2], which is today known as the Drude theory. To the present day several approaches have been developed to deepen the understanding of the microscopic mechanisms occurring in charge transport, including scattering theory using Fermi’s “golden rule” [3,4] or quantum corrections to the Drude conductivity. The latter covers weak (anti)localization [5,6] in the form of geometry or spin dependent corrections [7–15]. In contrast to studies of static systems the development of lasers and masers generated a rising activity on explicitly time-dependent Hamiltonians, where the external field cannot be considered a small perturbation [16]. In the most recent decade, owing to the possibility of changing the topology of a system by means of external driving, the investigation of transport in driven systems increased [17–26]. This includes transport in driven systems [27,28], either with or without disorder [29–31], or the photovoltaic Hall effect [19]. Most works studying the renormalization of conductivity, due to an external driving, use a perturbative approach regarding the external driving [20,22]. We present a general formalism that allows the determination of the Drude conductivity in the presence of a nonperturbative external driving. We unify linear-response theory and Floquet formalism to account for the probe bias and an external driving, providing an alternative approach to the Keldysh formalism. Using a different type of four-times Green’s-function formalism we derive both a Floquet-Dyson series and a generalized Floquet Fermi golden rule. To prove the consistency, both are shown to yield the same scattering time, a link that was missing so far. Even more important, the theory properly describes not only intra- but also inter-Floquet-replica scattering being completely neglected so far in literature. Finally, we present
*martin.wackerl@ur.de †paul.wenk@ur.de ‡john.schliemann@ur.de
a closed analytical form for the Floquet-Drude conductivity and apply the developed theory to a parabolic approximation of the two-dimensional electron gas (2DEG) and the corresponding tight-binding model both with circularly polarized external driving. Regarding the 2DEG, the analysis shows that previous results have been overestimating the effect of the driving on the conductivity. The driven tight-binding model shows an entirely different driving dependency even in the low-energy limit. This observation is mainly caused by the different eigenstates rather than the similar spectra. In conclusion, low-energy models are likely to give an incorrect result for the conductivity in presence of an external driving.
II. KUBO FORMULA FOR PERIODICALLY DRIVEN SYSTEMS
Our first aim is to express the linear conductivity using Floquet states [16,32,33],
|ψα (t )〉 = exp
(
−i
h ̄ εαt
)
|uα (t )〉, (1)
where α is labeling a discrete set of quantum numbers and εα are the corresponding quasienergies [34,35]. The periodicity of the Floquet functions, which are eigenstates of the Floquet Hamiltonian
HF (t ) = H (t ) − ih ̄∂t , (2)
allow for the Fourier expansion |uα (t )〉 = ∑
n e−in t |unα〉 with being the frequency of the external driving. The probe bias, with the corresponding vector potential A(q, ω), is treated perturbatively in linear-response theory, i.e., using the Kubo formula in momentum space [36],
〈Ja(q, ω)〉 = i
h ̄ V
∑
b
∫∞
−∞
dt′
∫∞
−∞
dt {eiωt (t − t ′)
× 〈[Ja(q, t ), Jb(−q, t ′)]〉Ab(q, t ′)}
− e2n
m Aa(q, ω), (3)
2469-9950/2020/101(18)/184204(16) 184204-1 ©2020 American Physical Society


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
with a, b ∈ {x, y, z}, ω being the frequency of the response current, V the volume of the system, e < 0 the electron charge, (·) the Heaviside function, m the effective electron mass, and n the electron density. 〈·〉 denotes the statistical average with respect to the system’s state which will in the presence of external driving not be in equilibrium. However, in what follows we shall assume the system to be in a stationary state so that occupation numbers of Floquet states are time independent [18,27,37–41]. Treating the external driving nonperturbatively, the current operators are expanded using Floquet states |ψα〉 = c†α |0〉,
Ja,b(q, t ) = ∑
αβ
J a,b
αβ (q, t )c†
αcβ , (4)
with the fermionic annihilation (creation) operators c(α†). The
expansion coefficients are the matrix elements Ja,b
αβ (q, t ) =
〈ψα (t )| Ja,b(q) |ψβ (t )〉. The current expectation value is no longer a simple product of conductance and electric field E = −∂t A since it is convoluted over the bias frequency ω′,
〈Ja(q, ω)〉 = ∑
b
∫∞
−∞
dω′ σ ̄ ab(q, ω, ω′)E b(q, ω′). (5)
Thus far, the conductivity tensor σ ̄ ab depends on the bias frequency, the momentum q, and on the resulting current frequency ω,
σ ̄ ab(q, ω, ω′) = i
h ̄ ωV
∑
αβ
∞ ∑
n1 ..n4 =−∞
( fα − fβ )
×
〈unα1
∣∣ ja(q)∣∣un2
β
〉〈un3
β
∣∣ jb(−q)∣∣unα4
〉
ω+ 1
h ̄ (εα − εβ ) + (n1 − n2 ) + i0+
× δ[ω + (n1 − n2 + n3 − n4) − ω′]
+ i e2n
mω δabδ(ω − ω′), (6)
with the single-particle current operator ji and the distribution function fα,β = 〈c†
α,β cα,β 〉. In what follows we limit our cal
culations to a position independent driving field, i.e., q = 0. Since we are ultimately interested in the DC conductivity, Eq. (5) simplifies to
〈Ja(q, ω)〉 = ∑
b
σ ab(q, ω)E b(q, ω), (7)
as shown in Appendix A. This allows us to express the real part of the longitudinal DC conductivity as
ωR→e0 [σ xx (0, ω)] = π h ̄
V
(e
m
)2 ∫ λ+h ̄ /2
λ−h ̄ /2
dε
(
−∂ f
∂ε
)
σ (ε) (8)
along with the definition
σ (ε) =
∑ ∞
nn′ =−∞
∑
αβ
〈un
α
∣∣ px ∣∣un
β
〉 〈un′
β
∣∣ px ∣∣un′
α
〉
× δ(ε − εα )δ(ε − εβ ), (9)
and the abbreviation Reω→0[·] for limω→0 Re[·]. A similar result has already been derived in Ref. [18] using the Keldysh framework. In derivating Eq. (8) one requires the difference of
two quasienergies to always be smaller than the photon energy of the external driving. Thus far, we have not used the convenient choice of the quasienergy [42] to be in [−h ̄ /2, h ̄ /2), however we must choose a suitable, possibly momentum dependent function λ such that
∀α : λ − h ̄
2 εα < λ + h ̄
2 . (10)
III. FOUR-TIMES FLOQUET GREEN’S FUNCTION AND CONDUCTIVITY
In this section we set up a formalism using four-times Green’s functions to express the result of the foregoing section for the conductivity in terms of Green’s functions. These are the building blocks for the Floquet-Dyson equation. First, we define a t-t′ state for the th Floquet zone [16,43–45]:
∣∣ψα (t , t ′ )〉 = e−(i/h ̄ )(εα+ h ̄ )t |uα (t ′ )〉 ei t′ , (11)
recovering for t = t′ the Floquet state solution |ψα (t )〉 of the time-dependent Schrödinger equation. For details of the t-t′ formalism the authors refer to Appendix B and Refs. [16,46,47]. From the states given in Eq. (11) a bare four-times Green function is constructed:
G r,a
0 (t1, t2, t ′
1, t′
2) = ∓i [±(t1 − t2)]
×1
T
∑ ∞
=−∞
∑
α
∣∣ψα (t1, t ′
1 )〉 〈ψα (t2, t ′
2)∣∣ (12)
with the period T = 2π / and periodicity
G r,a
0 (t1, t2, t ′
1, t′
2 ) = Gr,a
0 (t1 + T, t2 + T, t ′
1, t′
2) = Gr,a
0 (t1, t2, t ′
1 + T,t′
2 + T ). (13)
This propagator fulfills
[i∂t1 − 1
h ̄ HF (t ′
1 )]Gr,a
0 (t1, t2, t ′
1, t′
2)
= δ(t1 − t2 )
∑ ∞
s=−∞
δ(t ′
1 − t′
2 + sT )1. (14)
Fourier transforming the Green function and expanding the Floquet function into a Fourier series yields
G r,a
0 (ε, t′
1, t′
2) = 1
T
∑ ∞
n,n′ =−∞
G r,a
0 (ε, n, n′)
× e−in t′
1 ein′ t ′
2 . (15)
Generalizing the completeness relation of the Floquet functions to different times,
∑
α
|uα (t ′
1)〉〈uα (t ′
2 )|
∑ ∞
=−∞
δ(t ′
1 − t′
2+ T)
=1
∑ ∞
=−∞
δ(t ′
1 − t′
2 + T ), (16)
gives particular insight to the Lehmann representation of the four-times Floquet Green function:
G r,a
0 (ε, t′
1, t′
2 ) = 1 ∑∞
=−∞ δ(t ′
1 − t′
2+ T)
1
h ̄ ε − 1
h ̄ HF (t ′
1) . (17)
184204-2


 FLOQUET-DRUDE CONDUCTIVITY PHYSICAL REVIEW B 101, 184204 (2020)
One can show that the Fourier coefficients [46,47],
G r,a
0 (ε, n, n′) =
∑ ∞
=−∞
∑
α
∣∣unα+
〉〈unα′+
∣∣
1
h ̄ ε − 1
h ̄ εα − ± i0+ , (18)
are equal to the inverse of the Floquet matrix [27,29,30,4853]. The periodicity of the Floquet eigenstates [54,55] suggests defining the unitary transformation T as in Sec. V of Ref. [56] which diagonalizes the Green function,
[D(ε )]nn′
αβ ≡ [T †Gr,a
0 (ε)T ]nn′
αβ (19)
= δαβ δnn′
1
h ̄ ε − 1
h ̄ εα − n ± i0+ , (20)
where we denoted the matrix spanned by the Fourier com
ponents of the Green function as [Gr,a
0 (ε)]nn′ = Gr,a
0 (ε, n, n′). The Green function defined in Eq. (15) is used to express the conductivity from Eq. (8) as
ωR→e0[σ xx (0, ω)]
= −1
4π h ̄V
(e
m
)2 ∫ λ+ h ̄
2
λ− h ̄
2
dε
(
−∂ f
∂ε
)∫ T
0
dt′
1
∫T
0
dt′
2
× tr{px[Gr
0(ε, t′
1, t′
2) − Ga
0 (ε, t′
1, t′
2 )]px (t ′
1 ↔ t′
2)}. (21)
A justification for the use of the t-t′ formalism is given in Appendix B 3.
IV. FLOQUET-DYSON EQUATION
The focus of this section is to formulate a perturbative approach to include disorder in the expression of the conductivity described by bare propagators, i.e., Eq. (21). In the following, we will use the notation
〈x| Gr,a(t1, t2, t ′
1, t′
2 ) |x′〉 ≡ Gr,a(t1, t2, x, x′, t ′
1, t′
2), (22)
〈x| Gr,a(ε, t ′
1, t′
2 ) |x′〉 ≡ Gr,a(ε, x, x′, t ′
1, t′
2), (23)
for the matrix elements of the Green function in real space. The Green function for the system with an impurity potential V (x1, t1, t ′
1) at site x1 is supposed to fulfill
[i∂t1 − 1
h ̄ HF (x1, t1, t ′
1 )]Gr,a
p (t1, t2, x1, x2, t ′
1, t′
2)
= δ(t1 − t2)δ(x1 − x2 )
∑ ∞
s=−∞
δ(t ′
1 − t′
2 + sT )1 (24)
with HF (x1, t1, t ′
1 ) = HF (x1, t ′
1 ) + V (x1, t1, t ′
1). We limit the calculation presented here to the time-independent potential V (x), as including an explicit time dependence is straightforward; see Appendix C. Following the standard steps [36,5759], we can derive a recursive integral expansion, i.e., a Dyson series, for the Green function, in the case of a system perturbed by impurities:
G r,a
p (ε, x1, x2, n, n′ ) = Gr,a
0 (ε, x1, x2, n, n′)
+1
h ̄
∫
Vx
dx
∑ ∞
n1 =−∞
G r,a
p (ε, x1, x, n, n1)V (x)
× Gr,a
0 (ε, x, x2, n1, n′). (25)
The impurity potential V (x) = ∑Nimp
i v(x − ri ) is assumed to be a Gaussian random potential, which is uncorrelated such that the impurity average yields 〈v(x)v(x′)〉imp = Vimpδ(x −
x′) ⇔ ν(k) = Vimp and 〈v(x)〉imp = 0 (white noise) [58,59]. Fourier transforming Eq. (25) into momentum space and performing a disorder average one arrives at the expression for the disorder averaged Green function:
Gr,a(ε, k) = Gr,a
0 (ε, k) + Gr,a
0 (ε, k)
×
∑ ∞
n=1
[ r,a(ε, k)Gr,a
0 (ε, k)]n, (26)
where the self-energy r,a(ε, k) is the sum over all irreducible diagrams. Applying the transformation T , the solution of the recursive Eq. (26) in the eigenbasis is governed by
T †(k)Gr,a(ε, k)T (k)
= [D(ε, k) + T †(k) r,a(ε, k)T (k)]−1, (27)
with the diagonal matrix D(ε, k) given in Eq. (19). The difference of the retarded and advanced self-energy in the first-order Born approximation (1BA) can be related to a scattering time derived within the framework of the Floquet Fermi golden rule for t-t′ states (11) as shown in the next section.
V. GENERALIZED FLOQUET FERMI GOLDEN RULE
In the following the steps of the derivation of the Fermi golden rule for t-t′ Floquet states are similar to the one applied in Refs. [25,36]. The difference lies in the use of the t-t′ Floquet states, see Eq. (11), instead of the Floquet states. A t-t′ state fulfills
ih ̄ ∂
∂t
∣∣ψα (t , t ′)〉 = HF (t ′)∣∣ψα (t , t ′)〉. (28)
The corresponding time-evolution operator fulfilling this Schrödinger equation is given by
U0(t , t0, t ′ ) = e−(i/h ̄ )HF (t′)(t−t0 ). (29)
If a perturbation is switched on at time t0 the Schrödinger equation becomes
ih ̄ ∂
∂t
∣∣ α (t , t ′)〉 = [HF (t ′) + V (t , t ′)]∣∣ α (t , t ′)〉, (30)
with the boundary condition |ψα (t , t ′)〉 = | α (t , t ′)〉 for t t0. Changing into the interaction picture with
∣∣ α (t , t ′)〉
I = U†
0 (t , t0, t ′)∣∣ α (t , t ′)〉, (31)
VI (t , t ′) = U †
0 (t , t0, t ′)V (t , t ′)U0(t , t0, t ′), (32)
184204-3


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
one finds up to first order in the potential V
∣∣ α (t , t ′)〉
I ≈ ∣∣ψα (t0, t ′)〉
+1
ih ̄
∫t
t0
dt1 VI (t1, t ′)∣∣ψα (t0, t ′)〉 (33)
and for the overlap
〈ψ ′
β (t , t ′′)∣∣ α (t , t ′)〉
= 〈ψ ′
β (t , t ′′)∣∣ψα (t , t ′)〉
+1
ih ̄
∫t
t0
dt1
〈ψ ′
β (t1, t ′′)∣∣V (t1, t ′)∣∣ψα (t1, t ′)〉. (34)
In the next step let us consider the matrix element where the t-t′ Floquet states have the same time dependence but different Floquet indices,
a′
αβ (t , t ′ ) =
∑ ∞
n=−∞
a′
αβ (t , n) ein t′ (35)
= 〈ψβ (t , t ′)∣∣ ′
α (t , t ′)〉
≈ δαβ ei ( − ′ )(t′−t )
+1
ih ̄
∫t
t0
dt1
〈ψβ (t1, t ′)|V (t1, t ′)∣∣ψ ′
α (t1, t ′ )〉.
(36)
The Fourier coefficients for a perturbation, which is timeindependent in the second time argument, are governed by
a′
αβ (t , n) = 1
T
∫T
0
dt′ a ′
αβ (t , t ′ ) ein t′ (37)
= δαβ δn, − ′ e−in t
+1
ih ̄
∫t
t0
dt1 e(i/h ̄ )[εα −εβ +( − ′ )h ̄ ]t1
×
∑ ∞
m=−∞
〈um+ +n
α
∣∣V (t1)∣∣um+ ′
β
〉. (38)
We see that the transition amplitude is only a function of the difference of the Floquet indices, a ′
αβ (t , t ′ ) = a( − ′)
αβ (t , t ′ ).
Analog to the last section, t0 can be set to zero and for α = β Eq. (36) simplifies to
a′
αβ (t , t ′) = − i
h ̄
∫t
0
dt1
〈ψβ (t1, t ′)∣∣V (t1, t ′)∣∣ψ ′
α (t1, t ′)〉. (39)
Now, let us assume a scattering event from a t-t′ Floquet state into another t-t′ Floquet state with constant quasienergy, given by
∣∣ψα (ε, t , t ′ )〉 ≡ e−(i/h ̄ )(ε+ h ̄ )t ∣∣uα (t ′ )〉ei t′ . (40)
The quasienergy is independent of the quantum number. This state is not an eigenstate of the Hamiltonian, nevertheless it fulfills
〈ψα (t , t ′)∣∣ψ ′
β (ε, t , t ′ )〉 = δαβ e−(i/h ̄ )[ε−εα+( ′− )h ̄ ]t ei ( ′− )t′ .
(41)
Hence, Eq. (39) remains valid if the final state is of the same form as in Eq. (40). Consider now a scattering event from
a t -t ′ Floquet state ψα (k′, t , t ′) into a state with constant
energy ε,
ψα (k′, t , t ′ ) = e−(i/h ̄ )[εα (k′)+ h ̄ ]t uα (k′, t ′ ) i t′
e−(i/h ̄ )[ε+ ′h ̄ ]t uβ (k, t ′ ) i ′ t′ . (42)
The Fourier coefficient of the matrix element in the case of a scattering as in Eq. (42) for a time-independent perturbation is given by
a′
αβ (k, k′, t, n)
= −i Vkk′
h ̄
∫t
0
dt ′ e(i/h ̄ )[ε−εα (k′ )−( − ′ )h ̄ ]t′
×
∞ ∑
m=−∞
[um+ +n
β (k)]∗um+ ′
α (k′)
= −i Vkk′
h ̄
∫t
0
dt ′ e(i/h ̄ )[ε−εα (k′ )−( − ′ )h ̄ ]t′ c − ′+n
βα (k, k′),
(43)
with cn
αβ (k, k′) ≡
∑ ∞
m=−∞
[um+n
α (k)]∗um
β (k′). (44)
This allows for a definition of the transition probability matrix
[A ′ j j′
αβ (k, k′, t )]
n,n′ := ∑
γ
a′
γ α (k, k′, t , n)[a j j′
γ β (k, k′, t , n′ )]∗.
(45)
Equivalently to the derivation of the Floquet Fermi golden rule presented in Ref. [42] [see Eq. (D10) in Appendix D], in the limit t → ∞ the transition probability matrix becomes
[A ′ j j′
αβ (k, k′, t )]
n,n′
= 4π 2V 2
kk′
∑
γ
c − ′+n
αγ (k, k′)
× δ[ε − εγ (k′) − ( − ′)h ̄ ]
× [c j− j′+n′
βγ (k, k′)]∗ δ[ε − εγ (k′) − ( j − j′)h ̄ ]. (46)
Since the quasienergies are always defined to be in the central Floquet zone, cf. Eq. (D13), the probability matrix simplifies to
[A ′ j j′
αβ (k, k′, t )]
n,n′
= 4π 2V 2
kk′
∑
γ
cn
αγ (k, k′)
× [cn′
βγ (k, k′)]∗ δ2[ε − εγ (k′)]. (47)
The square of the delta distribution can be rewritten as [25]
δ2(ε) = δ(ε)δ(0) = δ(ε)
2π h ̄ tli→m∞
∫ t/2
−t /2
dt ′e(i/h ̄ )0t′ (48)
= δ(ε)t
2π h ̄ . (49)
Using this relation and performing the time derivative of each
184204-4


 FLOQUET-DRUDE CONDUCTIVITY PHYSICAL REVIEW B 101, 184204 (2020)
matrix element yields
nn′
αβ (k, k′) ≡
d [A ′ j j′
αβ (k, k′, t )]
n,n′
dt (50)
= 2π
h ̄ V 2
kk′
∑
γ
cn
αγ (k, k′)
× [cn′
βγ (k, k′)]∗ δ[ε − εγ (k′)]. (51)
Finally, one can perform an impurity average and identify 〈V 2
kk′ 〉imp = Vimp. Summing the rate over all momenta one gets
the inverse scatting time matrix,
(1
τ(ε, k)
)nn′
αβ
≡1
Vk′
∑
k′
〈 nn′
αβ (k, k′ )〉
imp (52)
= 2π
h ̄ Vimp
1
Vk′
∑
k′
∑
γ
cn
αγ (k, k′ )[cn′
βγ (k, k′ )]∗
× δ[ε − εγ (k′)] (53)
= i{T †(k)[ r
1BA(ε, k) − a
1BA(ε, k)]T (k)}nn′
αβ .
(54)
This expression is equal to the result derived from the Dyson series for the Floquet Green function. To our knowledge, this remarkable connection has not been established before. It comprises both inter- as well as intra-Floquet band scattering [60,61]. One can provide a connection to previous studies by setting n = n′ = 0 in Eq. (50), which results in the scattering rates given Refs. [17,42] [see Eq. (D20) in Appendix D]. For reasons of comparability, the Fermi golden rule for Floquet states is derived in detail in Appendix D. However, in general the relaxation rate matrix is not diagonal in the Floquet space nor can it be reduced to the (n, n′) = (0, 0) element only, as will be discussed later on. Also, one should notice that only on the diagonal is the difference of the retarded and advanced self-energy equal to the imaginary part of the retarded selfenergy.
VI. FLOQUET-DRUDE CONDUCTIVITY
Now, let us consider only the self-energy corrections during the disorder average and perform the time integration in Eq. (21). The disorder is not supposed to change the eigenenergies of the bare system, hence we drop all off-diagonal elements of the self-energy. This allows us to proceed analytically and ultimately express the conductivity in a compact way,
ωR→e0 [σ xx (0, ω)]
= h ̄
4π V
(e
m
)2 ∫ h ̄ /2
−h ̄ /2
dε
(
−∂ f
∂ε
)
×1
Vk
∑
k
k2
x
∑
α
∑ ∞
n=−∞
[( 1
2τ(ε, k)
)nn
αα
]2
×
{( 1
h ̄ ε − 1
h ̄ εα − n )2 +
[( 1
2τ(ε, k)
)nn
αα
]2}−2
. (55)
VII. APPLICATION TO A 2DEG
For a simple nontrivial application of the method described above we chose a 2DEG from a direct semiconductor close to the point under illumination with circularly polarized light. To allow for a direct comparison with existing theories on the topic of conductivity in driven systems we first apply our theory to the most simple model: The lowest s-type conduction band is approximated by a parabolic Hamiltonian H = p2/2m. The vector potential of the radiation,
A(t ) = Ax cos( t )ˆx + Ay sin( t )ˆy, (56)
is coupled to the momentum via minimal coupling leading to the time-dependent Hamiltonian
H (t ) = h ̄2
2m {k2 + γ 2 + 2γ [kx cos( t ) + ky sin( t )]}, (57)
with Ax = Ay =: A and the light parameter γ := eA/h ̄. The solution of the time-dependent Schrödinger equation was already given by Kibis [25]. To evaluate the expression for the conductivity, one has to specify the distribution function further. In the off-resonant regime, absorption of photons is suppressed, hence, a Fermi distribution can be assumed. However, since the parabolic spectrum is unbounded, it is not obvious how to set the Fermi energy εF for the driven parabolic spectrum [42]. Here, we truncate the momentum range to set the Fermi energy; see Appendix E. Evaluating Eq. (52) yields for the scattering time on the diagonal
(1
τ(εF , k)
)nn
= Vimpm
h ̄ 3
∑ ∞
m=−∞
J2
m+n(zk )J2
m(zε ), (58)
together with
zk = h ̄2γ k
m
/
h ̄ , zε = h ̄2γ √
2mεF /h ̄2
m
/
h ̄ . (59)
We can further disregard all pairings of only retarded or only advanced Green’s functions in Eq. (55), since they give a contribution of the order of 1/(εF τ0) with τ0 being the scattering time of the undriven system [59]. Aside from the relation between the Fermi energy and the relaxation rate, in the driven case one finds an important relation between the relaxation rate and the driving frequency. This ratio controls whether or not only the n = 0 element in Eq. (58) is significant: If τ0 1, the broadening of the nonzero Floquet modes is small enough such that the leaking into the central Floquet zone is negligibly small, as depicted in Fig. 1. The theory presented here also makes the regime accessible where τ0 1. In that case, the nonzero Floquet modes contribute significantly; see Fig. 2. But even in the off resonant regime, τ0 1, previous studies [20] overestimate the effect of circular driving as will be shown in the following. The central entry of the product of the retarded Green function with an advanced one is
[Gr (εF , k)Ga(εF , k)]00 ≈ 2π h ̄ (τ(εF , k))00δ(εF − k ). (60)
Applying these simplifications to Eq. (55), one arrives at the conductivity
ωR→e0 [σ xx (0, ω)] = 1
V4π
( e2
m
)
k2
F [τ(εF , kF )]00, (61)
184204-5


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
1234
2
3
4
5
6
7
8
k2
k1
k
ε
FIG. 1. The peaks show the broadening of the Floquet bands caused by the scattering time. The blue shaded area is the central Floquet zone. If τ0 1, the leaking of the nonzero Floquet modes (red curves) into the central Floquet zone is negligibly small.
where the scattering time is evaluated at the Fermi energy and
Fermi wave vector kF = √2mεF /h ̄. Hence, the ratio between conductivity without driving and dressed conductivity is given by
ωR→e0 [σ xx (0, ω)]
ωR→e0 [σ xx (0, ω)]∣∣γ =0
=1
∑∞
l=−∞ J 4
l (zε ) . (62)
In Fig. 3 we present the conductivity of a 2DEG irradiated by a circularly (σc) polarized light of intensity I. For comparison also the results in the case of linearly polarized light are shown. We conclude that for a parabolic spectrum approximation the central entry of the scattering time used in Eq. (61) is equal to the result which one yields from the Floquet Fermi
FIG. 2. The peaks show the broadening of the Floquet bands caused by the scattering time. The blue shaded area is the central Floquet zone. If τ0 1, the nonzero Floquet modes are leaking into the central Floquet zone. The red shaded area marks the contribution of the −1 Floquet band to the conductivity.
0 10 20 30 40
0
2
4
6
8
10
12
0 40 250
0.9997
1
FIG. 3. The Drude conductivity of a 2DEG irradiated by a circularly (σc) and linearly polarized light of intensity I is plotted in comparison to the undriven case (σ0). For linearly polarized light, σ⊥
and σ‖ are shown. The ratio √EF /meV/[ /(rad/s)]2 = √10/1024 is chosen. The vertical lines indicate the minima of σc. The inset shows the result for σc for a square lattice with lattice constant a = 5.6 Å, h ̄ = 0.3 THz, EF = 10 meV, and hopping energy g = 1.83 eV. For the same parameters the parabolic result, Eq. (62), is σc/σ0 = 1 + 0.1I/(mW/cm2 ) + O[I/(mW/cm2 )]2.
golden rule [17,25,42]. It is used, e.g., by the authors of Ref. [20] to calculate the conductivity. However, the equation ibid overestimates the effect of the driving for the latter. Our method allows us to go beyond the parabolic approximation. Let us examine a square lattice tight-binding model since here the spectrum is bounded. We define the lattice vectors as a1 = a(1, 0)T and a2 = a(0, 1)T and restrict the model to only nearest-neighbor hopping. Applying minimal coupling the corresponding Hamiltonian is given by
H (t ) = −g
[∑
n
eik·an · ei(e/h ̄ )A(t )·an + H.c.
]
, (63)
where g is the hopping parameter. The quasienergy can be obtained in an analytical form, see Appendix F,
= −2g
[
J0
(
a eAx
h ̄
)
cos(kxa) + J0
(
a eAy
h ̄
)
cos(kya)
] .
(64)
In this case it can be explicitly shown that the current, averaged over one period T , is given by  ̄J(k) = −e∇k (k)/h ̄; see Appendix G. With this at hand and Eq. (55) the Drude conductivity can be readily calculated applying the triangle integration method [62–64]. The result for circularly polarized light is plotted in the inset of Fig. 3. It shows that in the case of a bounded spectrum the features appear at different driving intensities and can even disappear completely for reasonable intensities and driving frequencies in the THz regime. A more detailed comparison between both models is given in Appendix F 2. The inverse scattering times for exemplary parameters for both models of the 2DEG are depicted in
184204-6


 FLOQUET-DRUDE CONDUCTIVITY PHYSICAL REVIEW B 101, 184204 (2020)
FIG. 4. Ratio between the central entry of the dressed inverse scattering time with the bare scattering time [1/τ00(k)]/[1/τ00(k)|γ =0] for the parabolic dispersion. The Fermi energy was set to 10 meV, the driving frequency to 0.3 THz, and the intensity to 5 mW/cm2. The Fermi energy is shown as purple contour.
Figs. 4 and 5. Figure 4 shows the normalized inverse scattering time for the parabolic dispersion for some representative parameters. In the presence of the driving the inverse scattering time is significantly changed compared to the static case complying with the change of the conductivity depicted in Fig. 3. To support the comparability of the effective model and the tight-binding description the parameters are chosen to be equal for Fig. 5 and Fig. 4. In contrast to the parabolic dispersion the scattering time for the square lattice is barely
FIG. 5. Ratio between the central entry of the dressed inverse scattering time with the bare scattering time [1/τ00(k)]/[1/τ00(k)|γ =0] for the tight-binding model. The Fermi energy was set to 10 meV, the driving frequency to 0.3 THz, and the intensity to 5 mW/cm2. The Fermi energy is shown as purple contour. It can be seen that the scattering time compared on the Fermi contour is barely changed by the driving.
changed due to the driving at the Fermi energy (see Fermi contour).
VIII. CONCLUSION
In this paper the Drude conductivity under an external driving has been investigated, including a formalism which allows for a rigorous derivation of the conductivity from an appropriate Dyson series by means of the Floquet formalism. The considerations are based on linear-response theory regarding the probe bias, whereas the external driving is incorporated nonperturbatively. Providing a new type of four-time Floquet Green functions, we were able to express the conductivity in terms of the aforementioned Green functions. This representation was so far missing. This type of Green functions allows for the formulation of a Dyson series, leading under the assumption of Gaussian white noise to the Floquet selfenergy in Born approximation. To prove consistency of the presented considerations a generalized Floquet Fermi golden rule was derived yielding the same result for the scattering time as the Dyson series, a connetion that was missing so far. Neglecting coherent scattering processes leads to a compact expression for the Floquet-Drude conductivity. Due to its generality, the presented formalism can be applied to a broad class of materials. As a first application we investigated the conductivity for two basic models for a 2DEG. We have shown that the effective continuum model yields a strikingly different prediction for the conductivity compared to the tightbinding approach. The deviations of the predictions for the conductivity are caused by the different eigenstates of the models rather than the similar spectra.
ACKNOWLEDGMENT
This work was supported by the Deutsche Forschungsgemeinschaft via Grant No. GRK 1570 and Project No. 336985961.
APPENDIX A: FLOQUET KUBO FORMULA FOR THE LINEAR CONDUCTIVITY
In a driven system the current is not simply a product of resistance and electric field; see Eq. (5) together with Eq. (6). Rather, the conductivity depends on both the frequency spectrum of the bias ω′ as well as a response frequency ω. Furthermore, we introduce
ω ≡  ̃ω + p ⇔ |  ̃ω| /2 with p ∈ Z, (A1)
and require that the electric field E b depends only on frequencies |  ̃ω′| /2. With this, Eq. (5) becomes
〈Ja(q,  ̃ω + p )〉 = ∑
b
∫ /2
− /2
d  ̃ω′ σ ̄ ab
× (q,  ̃ω + p ,  ̃ω′)E b(q,  ̃ω′), (A2)
where the conductivity tensor is given by
σ ̄ ab(q,  ̃ω + p ,  ̃ω′)
=i
h ̄ (  ̃ω + p )V
∑
αβ
∑ ∞
n1 ..n4 =−∞
184204-7


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
× fα − fβ
 ̃ω + p + 1
h ̄ (εα − εβ ) + (n1 − n2 ) + i0+
× 〈unα1
∣∣ j (q)∣∣un2
β
〉〈un3
β
∣∣ j j (−q)|unα4
〉
× δ[  ̃ω + p + (n1 − n2 + n3 − n4) −  ̃ω′]
+ i e2n
m(  ̃ω + p ) δ jδ(  ̃ω + p −  ̃ω′). (A3)
The argument of the δ distribution of the first term can become zero if and only if
n1 − n2 + n3 − n4 = −p. (A4)
Since we are ultimately interested in the DC limit, we consider only the case where p = 0. Taking only the real part of the longitudinal conductivity one yields
Re [σ xx (0,  ̃ω)]
=π
V
(e
m
)2 ∑ ∞
n,n′ =−∞
∑
αβ
[ fα − fβ
h ̄ ω
× 〈un
α
∣∣ px ∣∣un
β
〉〈un′
β
∣∣ px ∣∣un′
α
〉 δ[ω + 1
h ̄ (εα − εβ )]]
. (A5)
In the limit of  ̃ω → 0 one ends up with Eq. (8).
APPENDIX B: t-t′ FORMALISM
1. Separating the periodic from the aperiodic time dependence
In the t-t′ formalism one starts from the Floquet states |ψα (t )〉 = exp(− i
h ̄ εαt ) |uα (t )〉 but formally discriminates the
time dependence of the exponential from periodic time dependence as
|ψα (t ′, t )〉 = e−(i/h ̄)εαt |uα (t ′ )〉, (B1)
where obviously
|ψα (t , t )〉 = |ψα (t )〉. (B2)
The advantage of this artifice lies in the fact that the evolution of the states as a function of t is governed by the operator
UF (t ′, t ) = e−(i/h ̄ )HF (t′)t , (B3)
i.e.,
|ψα (t ′, t )〉 = UF (t ′, t − t0 )|ψα (t ′, t0 )〉 (B4)
= e−(i/h ̄ )εαt0 e−(i/h ̄ )HF (t′ )(t−t0 )|uα (t ′ )〉 (B5)
= e−(i/h ̄ )εαt |uα (t ′ )〉, (B6)
which avoids any time ordering. On the space of all states depending periodically with period T on a parameter t′ having dimension of time, we define the scalar product
(φ|χ ) = 1
T
∫T
0
dt ′ 〈φ(t ′)|χ (t ′)〉 (B7)
=1
T
∫T
0
dt ′ 〈φ|t ′〉〈t ′|χ 〉, (B8)
which is equal to the scalar product introduced by Sambe [45]. The notation
〈t ′|ψ〉 := |ψ (t ′)〉 (B9)
suggests to consider t′ as a coordinate rather than a time parameter. The corresponding operator tˆ′ can be defined to act multiplicatively on the above wave functions,
tˆ′|ψ (t ′)〉 = 〈t ′|tˆ′|ψ〉 = t ′|ψ (t ′)〉, (B10)
and the canonically conjugate operator is
wˆ := −ih ̄∂t′ = HF (t ′) − H (t ′) ⇒ [wˆ , tˆ′] = −ih ̄ (B11)
with a complete system of orthonormalized periodic eigenfunctions
〈t ′|l〉 = e−i lt′ , wˆ |l〉 = l h ̄ |l〉, (k|l ) = δkl (B12)
with k, l ∈ Z,
∞ ∑
l =−∞
〈t ′
1|l〉〈l|t ′
2〉 = T
∑ ∞
s=−∞
δ(t ′
1 − t′
2 + sT ) (B13)
= 〈t ′
1|t ′
2〉. (B14)
In obtaining the completeness relation we have taken into account the Fourier expansion of the Dirac comb,
∑ ∞
r=−∞
eir t = T
∑ ∞
s=−∞
δ(t + sT ). (B15)
Switching between the two pertaining representations amounts, up to signs and prefactors, in the usual Fourier expansion,
〈l|ψ〉 = 1
T
∫T
0
dt ′ 〈l|t ′〉〈t ′|ψ〉 (B16)
=1
T
∫T
0
dt ′ ei lt′ 〈t ′|ψ 〉 (B17)
⇔ 〈t ′|ψ〉 =
∑ ∞
l =−∞
〈t′|l〉〈l|ψ〉 (B18)
=
∑ ∞
l =−∞
e−i lt′ 〈l|ψ 〉. (B19)
Finally, the analogs of the wave functions ψα (q, t ) =
〈q|ψα (t )〉 read in the t-t′ formalism
ψα (q, t ′, t ) = 〈q|ψα (t ′, t )〉 = 〈q, t ′|ψα (t )〉. (B20)
2. Field operators and one-particle Green functions
Generalizing the states (B1) we define
∣∣φr
α (t ′, t )〉 = eir (t′−t )|ψα (t ′, t )〉 (B21)
= e−(i/h ̄ )(εα+rh ̄ )t eir t′ |uα (t ′ )〉 (B22)
with
φr
α (q, t ′, t ) = 〈q∣∣φr
α (t ′, t )〉 = 〈q, t ′∣∣φr
α (t )〉 (B23)
and the simple properties
∣∣φr
α (t ′, t )〉 = UF (t ′, t − t0 )∣∣φr
α (t ′, t0 )〉, (B24)
184204-8


 FLOQUET-DRUDE CONDUCTIVITY PHYSICAL REVIEW B 101, 184204 (2020)
(φr
α (t )∣∣φs
β (t )) = δαβ δrs, (B25)
∑
α
∞ ∑
r=−∞
∣∣φr
α (t ′
1, t )〉〈φr
α (t ′
2, t )∣∣
= 1T
∞ ∑
s=−∞
δ(t ′
1 − t′
2 + sT ). (B26)
In second quantization, this allows us to define a system of creation and annihilation operators b†αr (t ), bαr (t ) with
∣∣φr
α (t )〉 = b†
αr (t )|0〉, bαr (t )|0〉 = 0 (B27)
and
[bαr (t ), b†
βs(t )]± = δαβ δrs, (B28)
[bαr (t ), bβs(t )]± = [b†
αr (t ), b†
βs(t )]± = 0. (B29)
Field operators can be constructed as
(q, t′, t ) = ∑
α
∑ ∞
r=−∞
φr
α (q, t ′, t )bαr (t ), (B30)
fulfilling
[ (q1, t ′
1, t ), †(q1, t ′
2, t )]±
= δ(q1 − q2) T
∑ ∞
s=−∞
δ(t ′
1 − t′
2 + sT ) (B31)
with again all other (anti)commutators at equal times t being zero, and
〈q2, t ′
2| †(q1, t ′
1, t )|0〉 = δ(q1 − q2) T
∞ ∑
s=−∞
δ(t ′
1 − t′
2 + sT ).
(B32)
The Floquet Hamiltonian HF can be formulated as
HF (t ) = ∑ α
∑ ∞
r=−∞
(εα + rh ̄ )b†
αr (t )bαr (t ) (B33)
and is neither bounded from below nor from above. Going over to the Heisenberg picture,
H (q, t′, t ) = U †
F (t ′, t ) (q, t ′, t )UF (t ′, t )
=∑
α
∞ ∑
r=−∞
φr
α (q, t ′, t )bαr (0), (B34)
we yield the retarded/advanced one-particle Green function
Gr/a(q1, t ′
1, t1, q2, t ′
2, t2 )
= ∓i [±(t1 − t2)] 1
T 〈[ H (q1, t ′
1, t1 ), †
H (q2, t ′
2, t2 )] 〉
= ∓i [±(t1 − t2)] 1
T
×
∑ ∞
r=−∞
∑
α
φr
α (q1, t ′
1, t1 )[φr
α (q2, t ′
2, t2 )]∗
= ∓i [±(t1 − t2)] 1
T
∞ ∑
r=−∞
∑
α
[e−(i/h ̄ )(εα +rh ̄ )(t1−t2 )
× 〈q1|uα (t ′
1)〉〈uα (t ′
2 )|q2〉eir (t′
1−t ′
2)], (B35)
or, formulated as a Green operator,
Gˆr/a(t ′
1, t1, t ′
2, t2 )
= ∓i [±(t1 − t2)] 1
T
∑ ∞
r=−∞
∑
α
∣∣φr
α (t ′
1, t1 )〉〈φr
α (t ′
2, t2 )∣∣
= ∓i [±(t1 − t2)] 1
T
∑ ∞
r=−∞
∑
α
[e−(i/h ̄ )(εα +rh ̄ )(t1−t2 )
× |uα (t ′
1)〉〈uα (t ′
2 )|eir (t′
1−t ′
2)]. (B36)
These quantities have the significant property
(
i∂t1 − 1
h ̄ HF (t ′
1)
)
Gˆr/a(t1, t2, t ′
1, t′
2)
= δ(t1 − t2 )
∑
α
|uα (t ′
1)〉〈uα (t ′
2)| 1
T
∞ ∑
r=−∞
eir (t′
1−t ′
2)
= δ(t1 − t2)1
∞ ∑
s=−∞
δ(t ′
1 − t′
2 + sT ), (B37)
where we have used Eqs. (B15) and the completeness relation of the Floquet functions |uα (t )〉. As the expressions (B36)
depend only on the difference t1 − t2 and are periodic in t′
1,
t′
2 we can go over to Fourier components as
Gˆr/a(ω, n1, n2 )
=
∫∞
−∞
dt eiωt
∞ ∑
n1 ,n2 =−∞
e−in1 t′
1+in2 t ′
2 Gˆr/a(t ′
1, t, t′
2, 0)
=1
T
∑ ∞
r=−∞
∑
α
∣∣un1+r
α
〉〈un2+r
α
∣∣
ω− 1
h ̄ (εα + rh ̄ ) ± i0+ , (B38)
where the last line follows from
(±t ) = ±i
2π
∫∞
−∞
dω e−iωt
ω ± i0+ . (B39)
Moreover, with the spectral density
A(q1, t ′
1, t1, q2, t ′
2, t2 )
=1
2π T 〈[ H (q1, t ′
1, t1 ), †
H (q2, t ′
2, t2 )] 〉
=1
2π T
∞ ∑
r=−∞
∑
α
[e−(i/h ̄ )(εα+rh ̄ )(t1−t2 )
× 〈q1|uα (t ′
1)〉〈uα (t ′
2 )|q2〉eir (t′
1−t ′
2)], (B40)
having Fourier components
A(ω, q1, t ′
1, q2, t ′
2)
=1
T
∞ ∑
r=−∞
∑
α
{δ[ω − (εα + rh ̄ )]
× 〈q1|uα (t ′
1)〉〈uα (t ′
2 )|q2〉eir (t′
1−t ′
2)}, (B41)
184204-9


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
we obtain the familiar Lehmann representation of the Green function,
Gr/a(ω, q1, t ′
1, q2, t ′
2) =
∫∞
−∞
dω′ A(ω, q1, t ′
1, q2, t ′
2)
ω − ω′ ± i0+ . (B42)
In summary, when treating t′ not as a time parameter but rather as a state coordinate, the remaining time evolution in t is governed by the Floquet Hamiltonian being independent of t. Thus, we are left with an effectively time-independent Hamiltonian, and many formal manipulations known for such a situation work just in the same way. Note, however, that (i) the physical case still requires t = t′, and (ii) the Floquet Hamiltonian (B33) fails to be bounded from below.
3. Justification of the t-t′ formalism
The necessity to use the t-t′ formalism is far from obvious, hence, we would like to clarify why it is useful. We start with the Green function of the time-dependent Schrödinger equation
Gr,a
0 (t1, t2 ) = ∓i [±(t1 − t2 )]
∑
α
|ψα (t1)〉〈ψα (t2)|. (B43)
It is desirable to draw on the result from the Kubo formula in the static case where the conductivity can be written as a trace over the difference of retarded and advanced Green’s functions. The ansatz is therefore
σ ̃ ≡ tr{px[Gr
0(·) − Ga
0 (·)] px [Gr
0(·) − Ga
0(·)]}. (B44)
The time dependencies of the Green functions Gr,a(·) are left blank intentionally, since the above expression should only show the desired structure. If σ ̃ is assumed to have the above form, there are only a few possible time dependencies of the Green functions. In the following some attempts, using the Green function of the time-dependent Schrödinger equation, are presented that fail to reproduce the result obtained directly from Eq. (9). Using the two-time Green function together with the same time ordering as in Eq. (21) yields the expression
σ (t1, t2 ) = tr{px[Gr
0(t1, t2 ) − Ga
0(t1, t2 )]
× px[Gr
0(t2, t1 ) − Ga
0(t2, t1)]}. (B45)
Introducing Wigner coordinates
t = t1 − t2, T = t1 + t2
2 , (B46)
where the relative time is Fourier transformed into energy space and the mean time is averaged over one driving cycle leading to
σ (ε) = ∑
αβ
∑ ∞
nn′ =−∞
〈un
α
∣∣ px ∣∣un
β
〉〈un′
β
∣∣ px ∣∣un′
α
〉
× δ(ε + εα − εβ ). (B47)
While the ordering of the Floquet indices is correct, the above quantity is proportional to a single delta distribution and thus not equal to Eq. (9). Any different time ordering in Eq. (B45) leads to an incorrect ordering of the Floquet indices. Next, the attempt is analyzed where the Green functions depend on different relative times and the common mean time
is averaged,
σ (t , t ′) = 1
T
∫T
0
dT tr{px[Gr
0(t , T ) − Ga
0(t , T )]
× px[Gr
0(t ′, T ) − Ga
0(t ′, T )]}. (B48)
Now perform a Fourier transformation of both relative times onto the same energy,
σ (ε) =
∫∞
−∞
dt
∫∞
−∞
dt ′ e(i/h ̄ )ε(t+t′)σ (t , t ′ ), (B49)
which leads to the correct result for the conductivity if and only if the distribution function fulfills
∂f
∂[ε + (n + n′) 2
] = ∂f
∂ε ∀ n, n′ ∈ Z. (B50)
The last equation requires a half integer periodicity of the derivative of the distribution function, which is likely not to be fulfilled by an actual distribution function. Rather curious, defining a function by neglecting the summation over the Floquet indices in Eq. (12), namely
G ̃ r,a(ε, t ′
1, t′
2) = 1
T
∑
α
|uα (t ′
1)〉 〈uα (t ′
2 )|
1
h ̄ ε − 1
h ̄ εα ± i0+ , (B51)
allows us to reproduce the result form the Kubo formula
σ (ε) =
∫T
0
dt′
1
∫T
0
dt′
2 tr{px[G ̃ r (ε, t ′
1, t′
2 ) − G ̃ a(ε, t ′
1, t′
2 )]
× px[G ̃ r (ε, t ′
2, t′
1) − G ̃ a(ε, t ′
2, t′
1)]}. (B52)
However, the function given in Eq. (B51) is not a Green function of the Schrödinger equation or of the t-t′ Schödinger equation. The results presented in this section are not intended to prove that it is not possible to express Eq. (9) in terms of the Green function of the time-dependent Schrödinger equation. Nevertheless, it demonstrates that a naive ansatz fails. If the structure given in Eq. (B44) is desired, one way to solve the problem is to use the four-time Green functions introduced in Sec. III.
APPENDIX C: DYSON SERIES FOR TIME-DEPENDENT PERTURBATIONS
Here, we use the same notation as in Eqs. (22). As already shown in the latter, the bare Green function G0 fulfills the equation
[i∂t1 − 1
h ̄ H 0
F (x1, t ′
1 )]Gr,a
0 (t1, t2, x1, x2, t ′
1, t′
2)
= δ(t1 − t2 )δ(x1 − x2 )
∞ ∑
s=−∞
δ(t ′
1 − t′
2 + sT )1 (C1)
with the definition of the Floquet Hamiltonian for the unperturbed system
H0
F (x1, t ′
1) = H (x1, t ′
1 ) − ih ̄∂t′
1 . (C2)
The Hamiltonian for the perturbed one has the form
HF (x1, t1, t ′
1) = H0
F (x1, t ′
1 ) + V (x1, t1, t ′
1), (C3)
184204-10


 FLOQUET-DRUDE CONDUCTIVITY PHYSICAL REVIEW B 101, 184204 (2020)
where we stress that the dependency on t1 is fully kept by the potential. Obviously, the bare Green function G0 fulfills
[i∂t1 − 1
h ̄ HF (x1, t1, t ′
1)
+1
h ̄ V (x1, t1, t ′
1 )]Gr,a
0 (t1, t2, x1, x2, t ′
1, t′
2)
= δ(t1 − t2 )δ(x1 − x2 )
∞ ∑
s=−∞
δ(t ′
1 − t′
2 + sT )1. (C4)
We are interested in the Green function of the perturbed system Gp being a solution of
[i∂t1 − 1
h ̄ HF (x1, t1, t ′
1 )]Gr,a
p (t1, t2, x1, x2, t ′
1, t′
2)
= δ(t1 − t2 )δ(x1 − x2 )
∞ ∑
s=−∞
δ(t ′
1 − t′
2 + sT )1. (C5)
Equating Eqs. (C4) and (C5) we get
[i∂t1 − 1
h ̄ HF (x1, t1, t ′
1 )]Gr,a
p (t1, t2, x1, x2, t ′
1, t′
2)
= [i∂t1 − 1
h ̄ HF (x1, t1, t ′
1 )]Gr,a
0 (t1, t2, x1, x2, t ′
1, t′
2)
+1
h ̄ V (x1, t1, t ′
1 ) Gr,a
0 (t1, t2, x1, x2, t ′
1, t′
2). (C6)
The bare Green function is periodic in both t′
1, and t ′
2,
G r,a
0 (t , t2, x, x2, t ′
1 + T,t′
2 + T ) = Gr,a
0 (t , t2, x, x2, t ′
1, t′
2 ). (C7)
Therefore, without loss of generality one can use the restriction
t′
1, t′
2 ∈[− T
2, T
2
]. (C8)
Making use of the periodicity of the Green function and requiring that the potential is as well periodic in the second time argument,
V (x, t1, t ′
1 + T ) = V (x, t1, t ′
1), (C9)
one can show that ∫
Vx
dx
∫∞
−∞
dt
∫ T /2
−T /2
dt ′ δ(t1 − t )δ(x1 − x)
×
∑ ∞
s=−∞
δ(t ′
1 − t ′ + sT )V (x, t , t ′ )Gr,a
0 (t , t2, x, x2, t ′, t ′
2)
=
∫ T /2
−T /2
dt′
∑ ∞
s=−∞
δ(t ′
1 − t ′ + sT )V (x1, t1, t ′)
× Gr,a
0 (t1, t2, x1, x2, t ′, t ′
2)
= V (x1, t1, t ′
1 )Gr,a
0 (t1, t2, x1, x2, t ′
1, t′
2), (C10)
where in the last step we have used that the argument of the delta distribution can only be zero if s = 0. Comparing this equation with Eq. (C6) one finds a Dyson expansion for the Green function of the perturbed system,
G r,a
p (t1, t2, x1, x2, t ′
1, t′
2 ) = Gr,a
0 (t1, t2, x1, x2, t ′
1, t′
2)
+1
h ̄
∫
Vx
dx
∫∞
−∞
dt
∫ T /2
−T /2
dt ′ Gr,a
p (t1, t , x1, x, t ′
1, t ′)
× V (x, t , t ′ )Gr,a
0 (t , t2, x, x2, t ′, t ′
2). (C11)
If one assumes that the potential depends only on the periodic time component
V (x, t , t ′) = V (x, t ′) ⇔ HF (x, t , t ′) = HF (x, t ′) (C12)
the Green function depends only on the difference t1 − t2,
G r,a
p (t1, t2, x1, x2, t ′
1, t′
2 ) = Gr,a
p (t1 − t2, x1, x2, t ′
1, t′
2). (C13)
Applying Fourier transform on Eq. (C11) with respect to t1 − t2, one yields in energy space
G r,a
p (ε, x1, x2, t ′
1, t′
2 ) = Gr,a
0 (ε, x1, x2, t ′
1, t′
2)
+1
h ̄
∫
Vx
dx
∫ T /2
−T /2
dt ′ Gr,a
p (ε, x1, x, t ′
1, t ′)
× V (x, t ′ )Gr,a
0 (ε, x, x2, t ′, t ′
2), (C14)
where the explicit form of the bare Green function is given by
G r,a
0 (ε, x1, x2, t ′
1, t′
2)
=1
T
∑ ∞
r=−∞
∑
α
uα (x1, t ′
1 )[uα (x2, t ′
2 )]∗
1
h ̄ ε − 1
h ̄ εα − r ± i0+ eir (t′
1−t ′
2)
=1
T
∑
nn′
G r,a
0 (ε, x1, x2, n, n′ )e−in t′
1 ein′ t ′
2 . (C15)
The Fourier coefficients are given by
G r,a
0 (ε, x1, x2, n, n′) =
∑ ∞
r=−∞
∑
α
unα+r (x1 )[un′+r
α (x2 )]∗
1
h ̄ ε − 1
h ̄ εα − r ± i0+ ,
(C16)
where we used the shortened notation
uα (x1, t ′
1 ) ≡ 〈x1|uα (t ′
1)〉, un
α (x1) ≡ 〈x1
∣∣un
α
〉. (C17)
Since we required the potential to be periodic in the second time argument it can be expanded in a Fourier series,
V (x, t′) =
∞ ∑
n=−∞
Vn(x)e−in t′ . (C18)
This allows us to rewrite Eq. (C14) and perform the remaining time integration,
G r,a
p (ε, x1, x2, n, n′ ) = Gr,a
0 (ε, x1, x2, n, n′) (C19)
+1
h ̄
∫
Vx
dx
∞ ∑
n1 ,n2 =−∞
G r,a
p (ε, x1, x, n, n1)
× Vn1−n2 (x)Gr,a
0 (ε, x, x2, n2, n′). (C20)
APPENDIX D: FLOQUET FERMI GOLDEN RULE
A generalization of Fermi’s golden rule [3,4,36,58,65] to time periodic Hamiltonians, i.e., the Floquet Fermi golden rule, was already derived by Kitagawa et al. in Ref. [17]. However, a detailed derivation and discussion of the “scattering theory for Floquet-Bloch states” is given in Ref. [42]. The Floquet Fermi golden rule was used by Kibis in Ref. [25] in order to explain the suppression of backscattering of conduction electrons in the presence of a high-frequency electric field. In regard to Fermi’s golden rule for the t-t′ Floquet states, the
184204-11


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
derivation of the Floquet Fermi golden rule is presented here in detail. It is assumed that the solution of the time-dependent Schrödinger equation
ih ̄ ∂
∂t |ψα (t )〉 = H (t )|ψα (t )〉 (D1)
and the corresponding time evolution operator U0(t, t0) are known. In the presence of a time-dependent perturbation V (t ) the Schrödinger equation becomes
ih ̄ ∂
∂t | α (t )〉 = [H (t ) + V (t )]| α (t )〉. (D2)
The potential V (t ) is switched on at a reference time t0 such that the solutions of the Schrödinger equation coincide for times t t0,
|ψα (t )〉 = | α (t )〉 for t t0. (D3)
At times t t0 the particle is assumed to be in an eigenstate of the unperturbed Hamiltonian. Standard perturbation theory leads to the transition amplitude
〈ψβ (t )| α (t )〉 = δαβ + 1
ih ̄
∫t
t0
dt ′ 〈ψβ (t ′)|V (t ′)|ψα (t ′)〉
(D4)
up to first order in the potential. Without loss of generality t0 can be set to zero and for α = β the first nontrivial order of Eq. (D4) is given by
aαβ (t ) = − i
h ̄
∫t
0
dt ′ 〈ψβ (t ′)|V (t ′)|ψα (t ′)〉. (D5)
This formula, the Floquet Fermi golden rule, is equal to Eq. (10) of Ref. [25]. To proceed further, scattering from a Floquet state into a state with constant quasienergy
|ψα (ε, t )〉 = e−(i/h ̄)εt |uα (t )〉 (D6)
is considered. The quasienergy ε is independent of the quantum number. Hence, this state is not an eigenstate of the Hamiltonian, nevertheless it fulfills
〈ψα (t )|ψβ (ε, t )〉 = δαβ e(i/h ̄)(εα−ε)t . (D7)
Consequently, Eq. (D5) remains valid if the final state is |ψα (ε, t )〉. Now, consider a scattering event from a Floquet
state ψα (k′, t ) into a state with constant energy ε,
ψα (k′, t ) = e−(i/h ̄ )εα (k′)t uα (k′, t ) e−(i/h ̄ )εt uβ (k, t ). (D8)
If the perturbation V (t ) is time independent Eq. (D5) becomes
aαβ (k, k′, t ) = − iVkk′
h ̄
∑ ∞
nn′ =−∞
∫t
0
dt ′ e(i/h ̄ )[ε−εα (k′ )−(n−n′ )h ̄ ]t′
× [un′
β (k)]∗un
α (k′) (D9)
with Vkk′ = 〈φk,r|V (r)|φk′,r〉 where φk,r = exp(−ik · r)/√V.
Shifting t′ by −t/2 yields the probability density
|aαβ (k, k′, t )|2
= V2
kk′
h ̄ 2
∣∣∣∣
∞ ∑
nn′ =−∞
e(i/2h ̄ )[ε−εα (k′ )−(n−n′ )h ̄ ]t
× [un′
β (k)]∗un
α (k′)
∫ t/2
−t /2
dt ′ e(i/h ̄ )[ε−εα (k′ )−(n−n′ )h ̄ ]t′
∣∣∣∣
2
.
(D10)
In the long-time limit t → ∞ this simplifies to
|aαβ (k, k′, t )|2 = 4π 2V 2
kk′
∣∣∣∣
∞ ∑
nn′ =−∞
[un′
β (k)]∗un
α (k′)
× δ[ε − εα (k′) − (n − n′)h ̄ ]
∣∣∣∣
2
. (D11)
The quasienergies ε and εα (k) are chosen to be in the central Floquet zone such that
∀k : |ε − εα (k)| h ̄ , (D12)
δ(ε − εα − nh ̄ )δ(ε − εα − mh ̄ )
= δ2(ε − εα − nh ̄ )δnm. (D13)
Hence, Eq. (D11) becomes
|aαβ (k, k′, t )|2 = 4π 2V 2
kk′
∑ ∞
n=−∞
c−n
βα (k, k′ )[c−n
βα (k, k′ )]∗
× δ2[ε − εα (k′) − nh ̄ ] (D14)
with
cn
αβ (k, k′) :=
∑ ∞
m=−∞
[um+n
α (k)]∗um
β (k′). (D15)
The square of the delta distribution can be rewritten as shown in Eq. (48). The transition probability is then
αβ (k, k′) := d|aαβ (k, k′, t )|2
dt (D16)
= 2π
h ̄ V 2
kk′
∑ ∞
n=−∞
c−n
βα (k, k′ )[c−n
βα (k, k′ )]∗
× δ[ε − εα (k′) − nh ̄ ]. (D17)
The delta distribution can only have support if n = 0. Performing an impurity average according to the main text leads to 〈V 2
kk′ 〉imp = Vimp such that
〈 αβ (k, k′ )〉imp = 〈 αβ (k, k′ )〉imp (D18)
= 2π
h ̄ Vimp
∣∣c0
βα (k, k′)∣∣2δ[ε − εα (k′)]. (D19)
The scattering time is then governed by the sum over all initial states and the sum over all momenta,
1
τβ (ε, k) = 1
Vk′
∑
k′
∑
α
〈 αβ (k, k′ )〉imp (D20)
184204-12


 FLOQUET-DRUDE CONDUCTIVITY PHYSICAL REVIEW B 101, 184204 (2020)
−5 −4 −3 −2 −1 1 2 3 4 5
−15
−10
−5
5
10
15
k2
k1
εF
k
ε
FIG. 6. The Floquet zones are chosen to wrap around the parabolas. The quasi-Fermi energy is only defined in a certain momentum range, i.e., k ∈ [k1, k2 ), in the central Floquet zone.
= 2π
h ̄ Vimp
1
Vk′
∑
k′
∑
α
∣∣c0
βα (k, k′)∣∣2 δ[ε − εα (k′)]. (D21)
The last equation is the Floquet Fermi golden rule.
APPENDIX E: DEFINITION OF THE FLOQUET ZONE
In the following we would like focus on the a parabolic spectrum and describe the appropriate choice of the function λ, which defines the boundary for the quasienergy εα,
∀α : λ − h ̄
2 εα < λ + h ̄
2 . (E1)
Since the spectrum is not bounded, one has to choose the Floquet zone as indicated in Fig. 6. This limits the validity of the calculation to the τ0 1 regime as will be clear in the following. However, this limitation is only a peculiarity of the unbounded spectrum: In the derivation of the main text we defined the quasienergies to fulfill
∀k,k′ : |εα (k) − εβ (k′)| < h ̄ . (E2)
As a consequence, in a system with a single band the condition forces the band width to be smaller than h ̄ . Obviously this cannot be fulfilled by the parabolic spectrum. In the latter case, the momentum range where the quasi-Fermi energy is defined has to be truncated, as depicted with a red line in Fig. 6: k1 and k2 are functions of the driving frequency . For decreasing the momenta k1 and k2 move closer together. If the momentum range k ∈ [k1, k2) is of the order of the broadening of the Green function, the truncation leads to an incorrect result for the conductivity.
APPENDIX F: EXAMPLE: DRIVEN SQUARE LATTICE
1. Closed expression for the Floquet functions
In this section we derive a fully analytic solution of the time-dependent Schrödinger equation for the quadratic lattice
with time-periodic driving and compare it with the results for the parabolic dispersion. As in the main text, we define the two lattice vectors of the square lattice with a lattice constant a as
a1 = a
(1
0
)
, a2 = a
(0
1
)
(F1)
and choose the vector potential as
A=
(Ax sin( t ) Ay cos( t )
)
, (F2)
which allows us to tune the polarization between linear, elliptic, and circular for appropriate choices of amplitudes Ax, Ay. The time-dependent tight-binding Hamiltonian with hopping parameter g and a limitation to nearest-neighbor hopping is this given by
H (t ) = −g[eik·a1 · ei(e/h ̄ )A·a1 + eik·a2 · ei(e/h ̄ )A·a2 + H.c.].
(F3)
In the following we will make use of the identities
∫
dt eiγ sin( t ) =
∞ ∑
n=−∞
Jn(γ )
∫
dt ein t (F4)
=∑
n=0
Jn(γ )
in ein t + J0(γ )t , (F5)
∫
dt eiγ cos( t ) = 2
∞ ∑
n=1
inJn(γ )
n sin(n t ) + J0(γ )t, (F6)
which are based on the Jacobi-Anger expansion [66]. To solve the time-dependent Schrödinger equation
ih ̄ ∂
∂t ψk(t ) = H (t )ψk(t ) (F7)
we choose the ansatz
ψk (t ) = e−(i/h ̄ )F (t ) with F (t ) =
∫
dt H (t ). (F8)
Integrating the Hamiltonian (F3) yields
F (t ) = − 2g[J0(aγx ) cos(kxa) + J0(aγy ) cos(kya)]t
− geikxa ∑
n=0
Jn(aγx )
in ein t − ge−ikxa ∑
n=0
Jn(aγx )
−in e−in t
− 2geikya
∞ ∑
n=1
inJn(aγy )
n sin(n t )
− 2ge−ikya
∑ ∞
n=1
(−i)nJn(aγy )
n sin(n t ). (F9)
The light parameters are defined by γi = eAi/h ̄. The quasienergy is the nonoscillatory part of F (t ), thus
= −2g[J0(aγx ) cos(kxa) + J0(aγy ) cos(kya)]. (F10)
184204-13


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
FIG. 7. The conductivity (shifted and rescaled) for a driven square lattice model is shown as a function of intensity I for different numbers of Floquet modes taken into account.
The Floquet function can be, under the use of the JacobiAnger expansion [66], expressed as
u(t , γx, γy ) = ∏
n=0
∞ ∑
′ =−∞
J
(
− 2g
h ̄
Jn(aγy )
n
)
×J ′
(
− 2g
h ̄
(−1)nJn(aγx )
n
)
× ei (kya+n t )ei ′(kxa+n t− nπ
4 ) (F11)
=∏
n=0
∞ ∑
′ =−∞
cn, , ′ ei( + ′)n t (F12)
=
∑ ∞
n=−∞
us
n(γx, γy ) e−in t (F13)
together with
cn, , ′ := J
(
− 2g
h ̄
Jn(aγy )
n
)
J′
(
− 2g
h ̄
(−1)nJn(aγx )
n
)
× ei kya ei ′(kxa−nπ/4). (F14)
The closed expression for the Floquet functions has been used to calculate the inset of Fig. 3. A substantial number of Floquet modes have to be taken into account to calculate the conductivity. Figure 7 shows the convergence of the numerical calculations for a different number of Floquet modes taken into account.
2. Comparison with the continuum model
As promised in Sec. VII, we would like to clarify the difference between the results for the conductivity in the continuum case and the tight-binding model. Corresponding to Eq. (62), features related to the driving are visible if
zεF = h ̄2γ kF
m
/h ̄ , with γ = eA
h ̄ , (F15)
is of the order of 1, since the first zero of the Bessel function J0 is at ≈2.4. Now let us consider the tight-binding model. In contrast to the parabolic spectrum the Floquet functions of the circularly driven square lattice are rather complicated
FIG. 8. The absolute value of the Floquet function u0 plotted as a function of the intensity I for different kF directions φ. The dashed lines correspond to the approximation Eq. (F17) [only the term proportional to (kF γ )2 is taken into account]. Parameters: EF = 10 meV, = 0.3 THz.
as can be seen by examining Eq. (F13). However, we can approximate them for small γi and k and focus on |u0| to get a grasp on how they depend on the intensity. For simplification we set γx = γy and choose spherical coordinates for the wave vectors, kx = kF cos(φ), ky = kF sin(φ). A lengthy calculation yields
us
0(γ , γ ) = 2π
∫T
0
dt u(t, γ , γ ) (F16)
= 1 − 2 − √2 sin(2φ)
8
( αa2kF γ )2
− 3(2√2 − 3)
256
( αaγ )4
− α2
256
a4γ 4
2 + O(k4−p
F γ p), (F17)
with α = 2g/h ̄ and p ∈ {0, . . . , 4}. The corresponding up
0 for the parabolic case can be deduced from Ref. [20]:
up
0 = J0(zεF ) (F18)
= 1 − h ̄2k2
F
2m
γ2
2m 2 + O(z3
εF
). (F19)
A comparison of both cases results in
up
0
us
0
≈1
1 − sin(2φ)
√2
, (F20)
which gives on average 〈up
0/us
0〉φ = √2. Although this is a rough estimate (taking into account all Floquet functions the difference in conductivity is even more significant, as shown in Fig. 3) it shows that already at small intensities I ∼ γ 2 one can expect a difference between the result for the conductivity depending on whether the parabolic approximation is used or the tight-binding model. For moderate values of EF = 10 meV and a low driving frequency = 0.3 THz we also evaluate the full expression for us
0, Eq. (F13). The result is plotted in Fig. 8 where it is also compared to the approximation Eq. (F17). A convergence test, shown in Fig. 9, shows that a considerable number of Bessel functions have to be taken into account in Eq. (F13) to reach convergence at
184204-14


 FLOQUET-DRUDE CONDUCTIVITY PHYSICAL REVIEW B 101, 184204 (2020)
FIG. 9. Check of convergence of the Floquet function u0 with the number of maximal n, l, and l′ taken into account in Eq. (F14), here, as an example, for a wave-vector direction of φ = π /4. Parameters: EF = 10 meV, = 0.3 THz.
I > 1 mW/cm2. In Fig. 10 the same result is compared to the continuum approximation result.
APPENDIX G: CURRENT OPERATOR FOR THE SQUARE LATTICE
Following Ref. [67], the current density j is given by the continuity equation
∂ρ(r, t )
∂t = −∇ · j(r, t ), (G1)
where ρ describes the density of particles. Introducing the
polarization operator P(t ) = ∫ d3r rρ(r, t ), it can be shown that
∂P(t )
∂t =
∫
d3r r ∂ρ(r, t )
∂t = −
∫
d3r r∇ · j(r, t ) (G2)
=
∫
d3r j(r, t ). (G3)
Now, assume a hopping Hamiltonian in second quantization. The polarization operator is the product of position operator rm and particle number operator nm = a†
mam,
P=e
∑
m
rmnm. (G4)
FIG. 10. The absolute value of the Floquet function u0 plotted as a function of the intensity I. The dashed line corresponds to the Floquet function up
0 of the continuum model, Eq. (F18). Parameters: EF = 10 meV, = 0.3 THz.
Using the Heisenberg equation of motion the current operator is
J(t ) = ∂P
∂t = i
h ̄ [H, P] (G5)
= ie
h ̄
∑
n,m
(rn − rm )gn,m(t )a†
nam. (G6)
First, we assume that only hopping to nearest neighbors is present. The nearest-neighbor vectors are denoted as δ such that the current operator becomes
J(t ) = i e
h ̄
∑
n, j
δ j gδj (t )a†
nan+δj . (G7)
In the last step we assumed that the hopping amplitude is only a function of the difference of the positions. Expanding the creation and annihilation operators in momentum space
a(†)
n =∑
k
e(−)ik·rn a(†)
k (G8)
and performing the sum over all positions yields for the current operator
J(t ) = i eg
h ̄
∑
j,k
δ j ei(e/h ̄ )A(t )·δ j eik·δ j a†
kak (G9)
≡∑
k
J(k, t ) a†
kak. (G10)
Now focus on the square lattice with nearest-neighbor vectors δ1 = a(1, 0)T and δ1 = a(0, 1)T and circularly polarized
driving A(t ) = A( cos( t ), sin( t ))T. The current coefficient becomes
J(k, t )
= i ega
h ̄
(eik·δ1 ei(e/h ̄ )A(t )·δ1 − e−ik·δ1 e−i(e/h ̄ )A(t )·δ1
eik·δ2 ei(e/h ̄ )A(t )·δ2 − e−ik·δ2 e−i(e/h ̄ )A(t )·δ2
)
(G11)
= i ega
h ̄
∑ ∞
n=−∞
(eik·δ1 inJn(γ )ein t − e−ik·δ1 (−i)nJn(γ )e−in t
eik·δ2 Jn(γ )ein t − e−ik·δ2 Jn(γ )e−in t
) .
(G12)
Now focus on the n = 0 component, i.e., average over one driving period,
 ̄J(k) ≡ 1
T
∫ 2π/
0
dt J(k, t ) (G13)
= i ega
h ̄ J0(γ )
(eik·δ1 − e−ik·δ1
eik·δ2 − e−ik·δ2
)
(G14)
= −2 ega
h ̄ J0(γ )
(sin (kx a ) sin(kya)
)
. (G15)
Comparison with the quasienergy of the circularly driven square lattice (k) = −2gJ0(γ )[cos(kxa) + cos(kya)] yields
 ̄J(k) = − e
h ̄ ∇k (k). (G16)
184204-15


 WACKERL, WENK, AND SCHLIEMANN PHYSICAL REVIEW B 101, 184204 (2020)
[1] P. Drude, Ann. Phys. 306, 566 (1900). [2] P. Drude, Phys. Z. 14, 161 (1900). [3] P. A. M. Dirac, Proc. R. Soc. London, Ser. A 114, 243 (1927). [4] E. Fermi, Nuclear Physics: A Course Given by Enrico Fermi at the University of Chicago, Midway reprint (University of Chicago Press, Chicago, 1974). [5] B. L. Al’tshuler, A. G. Aronov, A. I. Larkin, and D. E. Khmel’nitskii, Sov. Phys. JETP 54, 0411 (1981). [6] S. Hikami, A. I. Larkin, and Y. Nagaoka, Prog. Theor. Phys. 63, 707 (1980). [7] S. Chakravarty and A. Schmid, Phys. Rep. 140, 193 (1986). [8] C. W. J. Beenakker and H. van Houten, Phys. Rev. B 38, 3232 (1988). [9] S. V. Iordanskii, Y. B. Lyandageller, and G. E. Pikus, JETP Lett. 60, 206 (1994). [10] D. H. Berman, M. Khodas, and M. E. Flatté, Phys. Rev. X 4, 011048 (2014). [11] W. Knap, C. Skierbiszewski, A. Zduniak, E. LitwinStaszewska, D. Bertho, F. Kobbi, J. L. Robert, G. E. Pikus, F. G. Pikus, S. V. Iordanskii, V. Mosser, K. Zekentes, and Y. B. Lyanda-Geller, Phys. Rev. B 53, 3912 (1996). [12] I. V. Lerner, B. L. Althsuler, V. I. Fal’ko, and T. Giamarchi, in Strongly Correlated Fermions and Bosons in Low-Dimensional Disordered Systems, Nato Science Series II (Springer, Netherlands, 2002), pp. 117–164. [13] P. Wenk and S. Kettemann, Phys. Rev. B 81, 125309 (2010). [14] M. Kammermeier, P. Wenk, J. Schliemann, S. Heedt, and T. Schäpers, Phys. Rev. B 93, 205306 (2016). [15] S. Kettemann, Phys. Rev. Lett. 98, 176808 (2007). [16] M. Grifoni and P. Hänggi, Phys. Rep. 304, 229 (1998). [17] T. Kitagawa, T. Oka, A. Brataas, L. Fu, and E. Demler, Phys. Rev. B 84, 235108 (2011). [18] Y. Zhou and M. W. Wu, Phys. Rev. B 83, 245436 (2011). [19] T. Oka and H. Aoki, Phys. Rev. B 79, 081406(R) (2009). [20] S. Morina, O. V. Kibis, A. A. Pervishko, and I. A. Shelykh, Phys. Rev. B 91, 155312 (2015). [21] M. A. Skvortsov, J. Exp. Theor. Phys. Lett. 67, 133 (1998). [22] A. A. Pervishko, O. V. Kibis, S. Morina, and I. A. Shelykh, Phys. Rev. B 92, 205403 (2015). [23] J. Shi and X. C. Xie, Phys. Rev. Lett. 91, 086801 (2003). [24] H. Dehghani, T. Oka, and A. Mitra, Phys. Rev. B 91, 155422 (2015). [25] O. V. Kibis, Europhys. Lett. 107, 57003 (2014). [26] T. Herrmann, Z. D. Kvon, I. A. Dmitriev, D. A. Kozlov, B. Jentzsch, M. Schneider, L. Schell, V. V. Bel’kov, A. Bayer, D. Schuh, D. Bougeard, T. Kuczmik, M. Oltscher, D. Weiss, and S. D. Ganichev, Phys. Rev. B 96, 115449 (2017). [27] M. Genske and A. Rosch, Phys. Rev. A 92, 062108 (2015). [28] I. Esin, M. S. Rudner, G. Refael, and N. H. Lindner, Phys. Rev. B 97, 245401 (2018). [29] P. Titum, N. H. Lindner, M. C. Rechtsman, and G. Refael, Phys. Rev. Lett. 114, 056801 (2015). [30] P. Titum, N. H. Lindner, and G. Refael, Phys. Rev. B 96, 054207 (2017). [31] P. Titum, Ph.D. thesis, California Institute of Technology, 2016. [32] G. Floquet, Annales scientifiques de l’École Normale Supérieure 12, 47 (1883). [33] M. Holthaus, J. Phys. B: At., Mol. Opt. Phys. 49, 013001 (2015).
[34] Y. B. Zel’Dovich, Sov. Phys. JETP 24, 1006 (1967). [35] V. Ritus, Sov. Phys. JETP 24, 1041 (1967). [36] G. D. Mahan, Many-particle Physics (Springer Science & Business Media, New York, 2013). [37] A. K. Gupta, O. E. Alon, and N. Moiseyev, Phys. Rev. B 68, 205101 (2003). [38] H. Hsu and L. E. Reichl, Phys. Rev. B 74, 115406 (2006). [39] A. Scholz, A. López, and J. Schliemann, Phys. Rev. B 88, 045118 (2013). [40] T. Shirai, T. Mori, and S. Miyashita, Phys. Rev. E 91, 030101(R) (2015). [41] T. Shirai, J. Thingna, T. Mori, S. Denisov, P. Hänggi, and S. Miyashita, New J. Phys. 18, 053008 (2016). [42] T. Bilitewski and N. R. Cooper, Phys. Rev. A 91, 033601 (2015). [43] D. F. Martinez, J. Phys. A: Math. Gen. 36, 9827 (2003). [44] K. Drese and M. Holthaus, Eur. Phys. J. D 5, 119 (1999). [45] H. Sambe, Phys. Rev. A 7, 2203 (1973). [46] D. F. Martinez, J. Phys. A: Math. Gen. 38, 9979 (2005). [47] D. F. Martinez and R. A. Molina, Eur. Phys. J. B 52, 281 (2006). [48] A. K. Eissing, V. Meden, and D. M. Kennes, Phys. Rev. Lett. 116, 026801 (2016). [49] A. K. Eissing, V. Meden, and D. M. Kennes, Phys. Rev. B 94, 245116 (2016). [50] C. O. Taberner, Master’s thesis, University of Copenhagen, 2017. [51] H. Aoki, N. Tsuji, M. Eckstein, M. Kollar, T. Oka, and P. Werner, Rev. Mod. Phys. 86, 779 (2014). [52] J. F. Rentrop, S. G. Jakobs, and V. Meden, Phys. Rev. B 89, 235110 (2014). [53] B. H. Wu and J. C. Cao, J. Phys.: Condens. Matter 20, 085224 (2008). [54] J. H. Shirley, Ph.D. thesis, California Institute of Technology, 1963. [55] J. H. Shirley, Phys. Rev. 138, B979 (1965). [56] N. Tsuji, T. Oka, and H. Aoki, Phys. Rev. B 78, 235124 (2008).
[57] K. F. Henrik Bruus, Many-Body Quantum Theory in Condensed Matter Physics (Oxford University Press, New York, 2004). [58] E. Akkermans and G. Montambaux, Mesoscopic Physics of Electrons and Photons (Cambridge University Press, Cambridge, UK, 2007). [59] J. Rammer, Quantum Transport Theory (CRC Press, 2018). [60] K. I. Seetharam, C.-E. Bardyn, N. H. Lindner, M. S. Rudner, and G. Refael, Phys. Rev. B 99, 014307 (2019). [61] K. I. Seetharam, C.-E. Bardyn, N. H. Lindner, M. S. Rudner, and G. Refael, Phys. Rev. X 5, 041050 (2015). [62] M. S. Methfessel, M. H. Boon, and F. M. Mueller, J. Phys. C: Solid State Phys. 16, L949 (1983). [63] G. Wiesenekker, G. te Velde, and E. J. Baerends, J. Phys. C: Solid State Phys. 21, 4263 (1988). [64] R. Winkler, J. Phys.: Condens. Matter 5, 2321 (1993). [65] J. Sakurai and J. Napolitano, Modern Quantum Mechanics (Addison-Wesley, New York, 2011). [66] M. Abramowitz and I. Stegun, Handbook of Mathematical Functions: With Formulas, Graphs, and Mathematical Tables, Dover Books on Mathematics (Dover, New York, 2012). [67] M. Genske, Ph.D. thesis, Universität zu Köln, 2017.
184204-16
