# Influence of radiative damping on the optical-frequency susceptibility - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.69.023814
> Collected: 2026-09-20
> Published: 2004-02-27
> Zotero parent key: TW5Q3ZVE
> Evidence: Zotero indexed PDF text

arXiv:physics/0309001v1 [physics.atom-ph] 29 Aug 2003
Influence of radiative damping on the optical-frequency
susceptibility
P. W. Milonni
Theoretical Division (T-DOT), Los Alamos National Laboratory,
Los Alamos, New Mexico 87545
Robert W. Boyd
Institute of Optics, University of Rochester, Rochester, New York 14627
(Date textdate; Received textdate; Revised textdate; Accepted textdate;
Published textdate)
Abstract
Motivated by recent discussions concerning the manner in which damping appears in the
electric polarizability, we show that (a) there is a dependence of the nonresonant contri
bution on the damping and that (b) the damping enters according to the “opposite sign
prescription.” We also discuss the related question of how the damping rates in the polar
izability are related to energy-level decay rates.
1


 I. INTRODUCTION
Several recent papers address the question of how material damping effects should
be included in the response of an atom or molecule to an applied electric field [1]-[5].
We will consider the simplest case, that of the linear atomic polarizability, which in
the absence of damping is given by the Kramers-Heisenberg formula,
αi(ω) = e2
3ħ
∑
j
|rji|2
(1
ωji − ω + 1
ωji + ω
)
(1)
for state i. Here ωji and rji are the transition (angular) frequency and coordinate
matrix element, respectively, between states i and j, and the field frequency ω is
assumed to be far removed from any of the atomic transition frequencies ωji. More
generally one associates damping rates γji with the different transitions and writes
αi(ω) = e2
3ħ
∑
j
|rji|2
(1
ωji − ω − iγji
+1
ωji + ω + iξγji
)
(2)
where ξ = +1 according to the so-called “opposite sign” prescription and ξ = −1
in the “constant sign” prescription. The difference appears only in the nonresonant
terms, and is therefore unimportant in most situations. However, the question of
which prescription is the correct one raises some interesting points, as we shall see,
and the purpose of this paper is to address some of these points as well as to answer
the question of whether one should take ξ = +1 or ξ = −1 in equation (2).
One might ask first whether a damping term should appear at all in the nonres
onant part of the Kramers-Heisenberg formula, i.e., whether we should in fact take
ξ = 0 instead of either ξ = +1 or ξ = −1. An analysis involving the diagonalization
of the (two-level) atom-field Hamiltonian in the rotating-wave approximation, for in
stance, shows that there is no damping term in the nonresonant denominator [6], a
result that is certainly accurate for most practical purposes. In a broader context the
issue here is an old one. Thus the imaginary part of the polarizability (2) implies an
absorption coefficient having the usual Lorentzian form
γ
(ω − ω0)2 + γ2 (3)
2


 as well as a nonresonant part
γ
(ω + ω0)2 + γ2 (4)
for a transition of frequency ω0 and linewidth γ, and one might question whether, as a
matter of principle, (4) contributes to the absorption lineshape. In his consideration
of possible corrections to the Weisskopf-Wigner lineshape, Lamb [7] noted that “such
a contribution [as (4)] appears in some derivations,” but added that it would be
negligible compared with the resonant contribution (3).
The effect of damping on the nonresonant part of the polarizability is not an
entirely trivial matter, and the literature relating to the subject reveals significant
disagreement on some rather basic aspects of dissipation theory. The purpose of this
paper is to address the principal points where there is disagreement and to obtain
what we regard as the correct form of the polarizability when damping is included.
In the following section we consider the problem of the electric-dipole interaction of
a two-level atom with the quantized electromagnetic field, assuming that all but one
of the field modes are initially unoccupied. Using the rotating-wave approximation
(RWA) for the atomic source field but not for the applied field, we obtain exactly
the result cited earlier [6], and in particular we find that there is no contribution
from (radiative) damping to the nonresonant term in the polarizability. In Section
III we go beyond the RWA in the atomic source field and find that the damping now
appears in the nonresonant term, and that it does so in accordance with the “opposite
sign” prescription. Section IV presents a discussion of these results, including their
connection to the classical theory of radiative damping. Section V focuses on the
form of the damping rate γji, and we argue that, contrary to what sometimes appears
in the literature, γji depends on the sum rather than the difference of the level decay
rates. Our conclusions are summarized in Section VI.
3


 II. DERIVATION OF LINEAR POLARIZABILITY: RWA
The model we consider is described by the Hamiltonian
H = ħω0σz + ∑
k
ħωka†
kak − dEσx = ħω0σz + ∑
k
ħωka†
kak − iħ
∑
k
Ck(ak − a†
k)(σ + σ†)
(5)
for a two-level atom (TLA) with transition frequency ω0 and dipole moment d inter
acting with the electromagnetic field. The σ operators are the usual Pauli operators,
with σ and σ† the lowering and raising operators for the TLA. ak and a†
k are the anni
hilation and creation operators for field mode k, and Ck = (d · ek,λ/ħ)(2πħωk/V )1/2,
with V the quantization volume. The subscript k denotes (k, λ), where k is the
wave vector assocated with a plane-wave mode of frequency ωk = |k|c and ek,λ is a
corresponding polarization unit vector (k · ek,λ = 0, ek,λ · e∗
k,λ′ = δλλ′ , λ = 1, 2).
The commutation relations for the atom and field operators give the Heisenberg
equations of motion
σ ̇ = −iω0σ + ∑
k
Ck(σzak − a†
kσz) (6)
 ̇ak = −iωkak + Ck(σ + σ†) (7)
We have chosen a normal ordering for the field annihilation and creation operators,
which is especially useful in the case that the applied field is described by a coherent
state [Eq. (11)]. As we are interested only in determining the linear response, the
equation of motion for σz will not be needed for our purposes.
The formal solution of equation (7) is
ak(t) = ak(0)e−iωkt + Ck
∫t
0
dt′[σ(t′) + σ†(t′)]eiωk(t′−t) (8)
In one version of the rotating-wave approximation (RWA) we ignore the coupling
between the creation operator for the field and the raising operator for the atom;
this corresponds, for the purpose of obtaining the equation of motion for the field
operators, to the neglect of the terms a†
kσ† and σak in the Hamiltonian (5). In this
4


 approximation the equation of motion for σ becomes
σ ̇ (t) = −iω0σ(t) + ∑
k
Ck[σz(t)ak(0)e−iωkt − a†
k (0)σz (t)eiωk t ]
+
∑
k
Ck2
∫t
0
dt′σz(t)σ(t′)eiωk(t′−t) (9)
Note that we are not making an RWA in the free-field operators ak(0) and a†
k(0), so
that both annihilation and creation free-field operators [ak(0) and a†
k(0)] appear in
(9).
Taking expectation values over the initial atom-field state on both sides of (9), we
have
〈σ ̇ (t)〉 = −iω0〈σ(t)〉 + ∑
k
Ck[〈σz(t)ak(0)〉e−iωkt − 〈a†
k (0)σz (t)〉eiωk t ]
+
∑
k
Ck2
∫t
0
dt′〈σz(t)σ(t′)〉eiωk(t′−t) (10)
We assume that the initial field state |ψF 〉 corresponds to a single occupied mode
described by a coherent state with
ak(0)|ψF 〉 = α|ψF 〉 , 〈ψF |a†
k(0) = α∗〈ψF | (11)
corresponding to the expectation value
〈E(t)〉 = i
( 2πħω V
)1/2
[αe−iωt − α∗eiωt] ≡ E0 cos ωt (12)
of the applied electric field. Thus
∑
k
Ck[〈σz(t)ak(0)〉e−iωkt − 〈a†
k(0)σz(t)〉eiωkt] = − i
ħ dxE0 cos ωt〈σz(t)〉 (13)
where dx is the component of the dipole matrix element along the direction of the
applied field; d2x = d2/3 for the spherically symmetric atom.
We assume that the operator σz, which corresponds to the population inversion,
changes sufficiently slowly that we may take
〈σz(t)σ(t′)〉 ∼= 〈σz(t′)σ(t′)〉 = −〈σ(t′)〉 (14)
5


 in the integral appearing in (10). Since we want to obtain the polarizability for
the TLA in a particular state, we assume further that the atom remains with high
probability in its initial state. Assuming this initial state to be the lower state, we
approximate 〈σz(t)〉 by −1, so that, using (13) and the approximation (14), we replace
(10) by
〈σ ̇ (t)〉 = −iω0〈σ(t)〉 + i d
ħ dxE0 cos ωt − ∑
k
Ck2
∫t
0
dt′〈σ(t′)〉eiωk(t′−t) (15)
We seek a solution of (15) of the form
〈σ(t)〉 = se−iωt + reiωt (16)
with s and r constants to be determined. This implies
i(ω0 − ω)se−iωt + i(ω0 + ω)reiωt = idx
2ħ E0(e−iωt + eiωt) − [γ−(ω) − i∆−(ω)]se−iωt
− [γ+(ω) − i∆+(ω)]reiωt (17)
where
γ±(ω) = Re ∑
k
Ck2
∫t
0
dt′ei(ωk±ω)(t′−t) → V
8π3
2π ħV
∫
d3kωk
∑
λ
|d · ek,λ|2πδ(ωk ± ω)
= d2
4π2ħc3
∫
dΩΩ3πδ(Ω ± ω)
∫π
0
dθ sin3 θ
= 2d2
3ħc3
∫∞
0
dΩΩ3δ(Ω ± ω) = 2d2ω3
3ħc3 U (±ω) (18)
and
∆±(ω) = 2d2
3πħc3 P
∫∞
0
dΩΩ3
Ω ± ω (19)
for t >> 1/ω, where U is the unit step function. Note that the damping rate γ−(ω) is
frequency-dependent [8]. (∆±(ω) is obviously divergent but, as discussed in Section
4, this has no direct bearing on our conclusions regarding the effect of damping on
the polarizability.) To obtain the polarizability α(ω) we write
p = dx〈σx〉 = dx(〈σ〉 + 〈σ†〉) = 2dxRe[(r + s∗)e−iωt] ≡ Re[α(ω)E0e−iωt] (20)
6


 for the induced dipole moment. This yields
α(ω) = d2
3ħ
(1
ω0 − ω − ∆−(ω) − iγ−(ω) + 1
ω0 + ω − ∆+(ω) + iγ+(ω)
)
(21)
Note that γ+(ω) = 0, and that therefore there is no damping contribution to the
second (nonresonant) term. γ−(ω0) is half the radiative decay rate of the upper state
in the absence of any applied field.
III. DERIVATION OF LINEAR POLARIZABILITY WITHOUT RWA
Let us now recalculate the polarizability, this time retaining both terms inside the
integral of equation (8), i.e., without making the RWA in the (source) field produced
by the atom under consideration. Then (9) is replaced by
〈σ ̇ (t)〉 = −iω0〈σ(t)〉 − i dx
ħ E0 cos ωt〈σz(t)〉
+
∑
k
Ck2
∫t
0
dt′[〈σz(t)σ(t′)〉 + 〈σz(t)σ†(t′)〉]eiωk(t′−t)
−
∑
k
Ck2
∫t
0
dt′[〈σ†(t′)σz(t)〉 + 〈σ(t′)σz(t)〉]e−iωk(t′−t) (22)
when we take expectation values as before. The approximations tantamount to (14)
are
〈σz(t)σ(t′)〉 ∼= 〈σz(t′)σ(t′)〉 = −〈σ(t′)〉
〈σz(t)σ†(t′)〉 ∼= 〈σz(t′)σ†(t′)〉 = 〈σ†(t′)〉
〈σ†(t′)σz(t)〉 ∼= 〈σ†(t′)σz(t′)〉 = −〈σ†(t′)〉
〈σ(t′)σz(t)〉 ∼= 〈σ(t′)σz(t′)〉 = 〈σ(t′)〉 (23)
where we use the equal-time identities σz(t)σ(t) = −σ(t)σz(t) = −σ(t). Using these
approximations in (22), together with the approximation 〈σz(t)〉 ∼= −1 in the second
term, we obtain the non-RWA extension of (15):
〈σ ̇ (t)〉 = −iω0〈σ(t)〉 + idx
ħ E0 cos ωt + ∑
k
Ck2
∫t
0
dt′[−〈σ(t′)〉 + 〈σ†(t′)〉]eiωk(t′−t)
−
∑
k
Ck2
∫t
0
dt′[−〈σ†(t′)〉 + 〈σ(t′)〉]e−iωk(t′−t) (24)
7


 It is important to note that in equations (23) we have used the commutation relations
between σz(t) and σ(t), σ†(t), and have obviously not made the approximation that
σz could be replaced by −1. The latter approximation is made only in the second
term of (22), where σz multiplies the applied field but no atom operator, so that the
approximation does not violate the commutation relations from which we obtained
the equations of motion. The two approximations are different: that made in (23)
assumes that σz(t) varies little on time scales ∼ 1/ωk for field frequencies ωk ∼ ω that
will contribute significantly to the variation of 〈σ(t)〉, whereas that made in replacing
〈σz(t)E0 cos ωt by −E0 cos ωt assumes that the atom remains with high probability in
its lower state because the field frequency lies outside the absorption linewidth. The
difference between these two approximations involving σz turns out to be irrelevant
for the final results when the RWA is made, as is clear from (14).
We again have a solution of the form (16), now with s and r satisfying
Xs + U r∗ = dx
2ħ E0
V s + Y r∗ = dx
2ħ E0 (25)
where
X = ω0 − ω − [∆−(ω) − ∆+(ω)] − i[γ−(ω) + γ+(ω)]
U = [∆−(ω) − ∆+(ω)] + i[γ−(ω) + γ+(ω)]
Y = ω0 + ω + [∆−(ω) − ∆+(ω)] + i[γ−(ω) + γ+(ω)]
V = [∆−(ω) − ∆+(ω)] + i[γ−(ω) + γ+(ω)] (26)
Assuming that γ±(ω) and ∆±(ω) are small in magnitude compared to ω0 ± ω, we
have
s ∼= dxE0
2ħ
1
X = dxE0
2ħ
1
ω0 − ω − [∆−(ω) − ∆+(ω)] − i[γ−(ω) + γ+(ω)]
r∗ ∼= dxE0
2ħ
1
Y = dxE0
2ħ
1
ω0 + ω + [∆−(ω) − ∆+(ω)] + i[γ−(ω) + γ+(ω)] (27)
8


 and, from (20),
α(ω) = d2/3ħ
ω0 − ω − [∆−(ω) − ∆+(ω)] − i[γ−(ω) + γ+(ω)] + d2/3ħ
ω0 + ω + [∆−(ω) − ∆+(ω)] + i[γ−(ω) + γ+(ω)] (28)
IV. DISCUSSION
In contrast to the RWA result (21), ∆±(ω) and γ±(ω) appear in both the resonant
and nonresonant terms of (28). Consider first the physical significance of ∆±(ω),
assuming that the frequency ω of the initially occupied field mode is sufficiently close
to ω0 that we may take
∆−(ω) ≈ ∆−(ω0) = 2d2
3πħc3 P
∫∞
0
dΩΩ3 Ω − ω0
(29)
and focusing only on the resonant term in α(ω). In a more complete analysis involving
the transformation from the fundamental minimal coupling form of the Hamiltonian
to the electric dipole form, it is found that the additional term 2π ∫ d3P⊥ · P⊥ ap
pearing in the transformed Hamiltonian has the effect of replacing (29) by [9]
∆−(ω0) ≈ 2d2ω02
3πħc3 P
∫∞
0
dΩΩ ω − ω0
(30)
With this modification it is seen that ∆(ω0) ≡ ∆−(ω0) − ∆+(ω0) is simply the (un
renormalized) TLA radiative frequency shift, i.e., the difference in the radiative level
shifts of the two levels [10]. In general, however, the approximation (29) is not appli
cable, and the radiative level shifts ħ∆±(ω) depend on the frequency of the initially
occupied mode. In the polarizability (28) the frequency shift ∆(ω) ≡ ∆−(ω) − ∆+(ω)
adds to the field frequency ω in both the resonant and nonresonant terms, whereas
in the RWA ∆+(ω) does not appear in the resonant term and ∆−(ω) does not appear
in the nonresonant term. In other words, the RWA does not correctly include the
radiative frequency shift as the difference in the radiative level shifts of the TLA.
The expressions for the level shifts ħ∆±(ω) are specific to the TLA model, but
are easily generalized to the case of a real atom. This extension, even with the
9


 standard renormalization procedures, still leaves us with divergent level shifts in the
nonrelativistic approximation. A high-frequency cutoff mc2/ħ results in Bethe’s ap
proximation to the Lamb shift [10]. Since this procedure is very well known, and
we are in any case only concerned with the form in which the radiative corrections
appear in the polarizability, and not their numerical values, we will simply assume
henceforth that the frequency shift has been accounted for in writing ω0 ± ω.
Thus
α(ω) = d2
3ħ
(1
ω0 − ω − iγ(ω) + 1
ω0 + ω + iγ(ω)
)
(31)
where γ(ω) = γ−(ω) + γ+(ω). Like ∆(ω), iγ(ω) is effectively an addition to the
applied field frequency ω. Unlike the frequency shift, however, the damping rate γ(ω)
is half the sum of the decay rates γ±(ω) of the two levels. Of course the decay rate
γ+(ω) of the ground state in our two-level model is zero but, as discussed in the next
section, (31) is valid more generally when the decay rate of the lower level of the
transition is not zero. That is, the damping rate appearing in the contribution to the
polarizability from any given transition involves half the sum of the decay rates of
the two levels of the transition.
Regardless of whether the lower-level decay rate vanishes, the non-RWA result (31)
shows that both the resonant and nonresonant contributions to the polarizability have
a nonvanishing damping term in their denominators, this damping term being half the
upper-level decay rate. In particular, it is seen that the damping appears according
to the “opposite sign prescription,” i.e., ξ = +1 is the correct choice in the dispersion
formula (2). The same conclusion was reached by different lines of reasoning by
Buckingham and Fischer [2].
Note that, if γ is taken to be a (positive) constant, independent of frequency, then
the opposite sign prescription is consistent with the causality requirement that the
polarizability should be analytic in the upper half of the complex ω plane [11]. But in
general the decay rates are in fact frequency-dependent [8], and causality is ensured
only if the model used to calculate γ(ω) is itself causal. In fact, as recalled below,
radiative damping provides an example in which this is not the case.
10


 In one approach to a classical calculation of the natural lineshape, one considers the
solution x(t) = A0e−γt sin(ω0t) of a damped dipole oscillator with resonance frequency
ω0. The lineshape is taken to be proportional to the squared modulus of the Fourier
transform
a(ω) = A0
2π
∫∞
0
dte−γteiωt sin(ω0t) ∝
(1
ω0 − ω − iγ + 1
ω0 + ω + iγ
)
(32)
and is seen to be consistent with the “opposite sign” prescription. In contrast to this,
an old paper by Weisskopf [12] implies the result
a(ω) ∝
(1
ω0 − ω − iγ − 1
ω0 + ω − iγ
)
(33)
which is consistent with the “constant sign” prescription. However, since this result
is based on the integral appearing in (32), it seems that (33) involves a sign error or
perhaps just a typographical error.
Since the absorption coefficient may for our purposes be taken to be proportional
to the imaginary part of α(ω), equation (31) implies an absorption lineshape propor
tional to
L(ω) = γ
(ω0 − ω)2 + γ2 − γ
(ω0 + ω)2 + γ2 (34)
The same result, for γ taken to be a constant, was obtained on the basis of the
Lorentz model by Van Vleck and Weisskopf [13], who noted that the minus sign in
the nonresonant term “must be used because the excitation of the molecule is here
accompanied by emission rather than absorption of a light quantum,” a process which
is excluded when the RWA is made [14].
It is also of interest to compare the result (31) with the corresponding result given
by the classical theory of radiative damping based on the equation
x ̈ + ω02x − 2e2
3mc3
.x..= eE0 cos ωt (35)
The polarizability of the classical dipole oscillator described by this equation is
αcl(ω) = e2/m
ω02 − ω2 − 2
3 (ie2/mc3)ω3
= e2
2mω′0
(1
ω′0 − ω − iγcl(ω) + 1
ω′0 + ω + iγcl(ω)
)
(36)
11


 where ω′0 = √ω02 − γc2l(ω) and γcl(ω) = (e2/3mc3)ω2. The replacements e2/2mω′0 →
e2f1/2mω′0 and e2ω2/3mc3 → e2f2ω2/3mc3, where f1 = 2mω′0d2/e2ħ and f2(ω) =
(2mωd2/e2ħ), make the classical result (35) equivalent to (31). These replacements
involving effective oscillator strengths f1 and f2 are the usual substitutions required to
put classical oscillator results in agreement with some of the corresponding quantum
mechanical expressions.
The ω3 in the denominator of (36), or in other words the third derivative of x in
equation (35), leads to a pole in the upper half of the complex ω plane, thus violating
the causality requirement that the polarizability be analytic in the upper half-plane.
The nonrelativistic theory of radiative reaction is well known to be acausal, but the
acausality occurs on such a short time scale that relativistic quantum effects must
be taken into account. For most practical purposes the acausality is of no conse
quence. Thus, for instance, equation (36) leads to the correct extinction coefficient
(∝ ωIm[α(ω)]) due to Rayleigh scattering.
V. RELATION OF DAMPING IN THE POLARIZABILITY TO LEVEL DE
CAY RATES
These considerations are easily extended beyond the two-level model, with the
result that the linear atomic polarizability has the form
αi(ω) = 1
3ħ
∑
j
|rji|2
(1
ωji − ω − iγji(ω) + 1
ωji + ω + iγji(ω)
)
(37)
The damping rate γji(ω) has a “dephasing” contribution associated, for instance,
with elastic collisions, as well as a contribution associated with the decay rate of the
atomic states i and j. Here we consider only the latter contribution, which is due to
radiative decay and other loss processes. In the case of radiative decay, for instance,
γji is found, by a straightforward multilevel generalization of the calculations in the
preceding sections, to be half the sum of the radiative decay rates associated with the
12


 two states i and j:
γji(ω) = 2e2ω3
3ħc3


∑
Ej >Em
|rjm|2 + ∑
Ei >Em
|rim|2

 (38)
where Em denotes the energy of state m. If we replace ω3 by ω03 in this formula, we
obtain half the spontaneous decay rate of state j in the case that the field is initially
in the vacuum state. This result was obtained, for example, by Weisskopf and Wigner
[15], Landau [16], and many others [9]. The same conclusion is reached in the more
general case where the energy levels decay by nonradiative channels: γji(ω) is half
the sum of the total decay rates of the states i and j.
Various authors, however, have calculated or assumed—erroneously, in our
opinion—that γji involves the difference in the decay rates of the states i and j [17],
[18], [19]. In addition to the Heisenberg-picture calculation leading to the conclusion
that γji involves the sum rather than the difference of energy-level decay rates, as
presented in this paper, the following simple argument can be used. Let ci(t) and cj(t)
be the (Schro ̈dinger-picture) probability amplitudes for states i and j, and let γi and
γj be the decay rates of these states. Then ci∗(t)cj(t) and ci(t)cj∗(t), which determine
the polarizability, decay at exp[−1
2 (γi +γj)t], and so the linewidth in the polarizability
must involve the sum of γi and γj rather than the difference. Sushchinskii [17], for
instance, expresses his results in terms of complex energies Ei′ = Ei − 1
2 iΓi and their
differences Ei′ − Ej′ = Ei − Ej − 1
2 i(Γi − Γj), whereas the appropriate differences
entering into the polarizability are Ei′∗ − Ej′ and Ei′ − Ej′∗.
Finally we note that Andrews et al. [19] have stated a polarizability sum rule which
in the simplest case of the linear polarizability can be expressed as ∑
i αi(ω) = 0. A
physical plausibility argument for this sum rule can be adduced as follows. If pi is the
probability that the atom is in state i, then the linear polarizability at field frequency
ω is
α(ω) = ∑
i
piαi(ω) (39)
Consider the idealized limit in which all the pi are equal. Then the polarizability and
therefore the induced emission or absorption rate at frequency ω becomes proportional
13


 to just ∑
i αi(ω). But if all the states are equally populated the net induced emission
and absorption rate must vanish, implying the polarizability sum rule conjectured by
Andrews et al. From the expression (37) it follows that this sum rule is statisfied
only if γji is symmetric in i and j, i.e., γji must involve the sum rather than the
difference of γi and γj. (We note that, in the case of the constant sign prescription for
the damping terms in the polarizability, the polarizability sum rule would be satisfied
only if γji were antisymmetric in i and j.)
VI. SUMMARY
Following a standard, nonrelativisitic approach, we have considered specifically
the case of a two-level atom interacting with the quantized electromagnetic field, one
mode of which is initially occupied and described by a coherent state. Working in
the Heisenberg picture, we calculated the polarizability with and without making
the RWA for the atomic source field. In the RWA we obtained a known result,
and in particular the nonresonant contribution to the polarizability was found to
have no damping factor in its denominator. Going beyond the RWA, however, we
found that both the resonant and nonresonant contributions to the polarizability have
the radiative damping rate in their denominators, and that the polarizability has a
form that is consistent with the so-called opposite sign prescription for including the
damping.
The radiative frequency shift appearing in the non-RWA expression for the
polarizability depends on the radiative level shifts in the correct way, i.e., it is the
difference of the two level shifts. The damping rate appearing in the non-RWA
expression for the polarizability is half the sum of the radiative decay rates of the
two levels, in contrast to the difference of the decay rates that has been obtained or
assumed in some treatments. The fact that the polarizability depends symmetrically
on the decay rates of the energy levels is consistent with the polarizability sum rule
of Andrews et al. [19] when the (correct) opposite sign prescription is used.
14


 Acknowledgement
We thank D. L. Andrews, L. C. D ́avila Romero, and G. E. Stedman for help
ful correspondence, and P. R. Berman and J. H. Carter for useful discussions and
suggestions. R. W. Boyd gratefully acknowledges support by ONR under award
N00014-02-1-0797, by DoE under award DE-FG02-01ER15156, and by ARO under
award DAAD19-01-1-0623.
[1] D. L. Andrews, S. Naguleswaran, and G. E. Stedman, Phys. Rev. A57, 4925 (1998).
[2] A. D. Buckingham and P. Fischer, Phys. Rev. A61, 035801 (2000).
[3] G. E. Stedman, S. Naguleswaran, D. L. Andrews, and L. C. Da ́vila Romero, Phys.
Rev. A63, 047801 (2001).
[4] A. D. Buckingham and P. Fischer, Phys. Rev. A63, 047802 (2001).
[5] D. L. Andrews, L. C. D ́avila Romero, and G. E. Stedman, Phys. Rev. A67, 055801
(2003).
[6] R. Loudon, The Quantum Theory of Light (Clarendon Press, Oxford, 1973), p. 192.
See also G. S. Agarwal and R. W. Boyd, Phys. Rev. A67, 043821 (2003), for a different
approach to the same result.
[7] W. E. Lamb, Jr., Phys. Rev. 85, 259 (1952).
[8] See G. S. Agarwal and R. W. Boyd, Reference [6].
[9] See, for instance, P. W. Milonni, Phys. Rep. 25, 1 (1976).
[10] See, for instance, P. W. Milonni, The Quantum Vacuum. An Introduction to Quantum
Electrodynamics (Academic Press, San Diego, 1994), Section 4.9.
[11] See, for instance, H. M. Nussenzveig, Causality and Dispersion Relations (Academic
Press, New York, 1972).
[12] V. Weisskopf, Phys. Z. 34, 1 (1933).
[13] J. H. Van Vleck and V. F. Weisskopf, Rev. Mod. Phys. 17, 227 (1945).
15


 [14] Van Vleck and Weisskopf went on to show that, when the dipole orientations or phases
after each collision are treated statistically according to the Boltzmann distribution,
rather than assumed to be random as in the original Lorentz treatment, one obtains
an absorption lineshape in which the nonresonant contribution is added rather than
subtracted from the resonant term. Then, instead of the vanishing absorption predicted
by the original Lorentz treatment when the absorption frequency ω0 → 0, one obtains
the Debye lineshape.
[15] V. F. Weisskopf and E. Wigner, Z. Phys. 63, 54 (1930).
[16] L. D. Landau, Z. Phys. 45, 430 (1927).
[17] M. M. Sushchinskii, Raman Spectra of Molecules and Crystals (Israel Program for
Scientific Translations, New York, 1972), p. 38.
[18] L. Hecht and L. D. Barron, Mol. Phys. 79, 887 (1993); Chem. Phys. Lett. 225, 519
(1994).
[19] D. L. Andrews, L. C. D ́avila Romero, and G. E. Stedman, Phys. Rev. A67, 055801
(2003).
16
