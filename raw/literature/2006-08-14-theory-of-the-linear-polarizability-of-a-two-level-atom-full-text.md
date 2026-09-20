# Theory of the linear polarizability of a two-level atom - Full Text

> Source: https://iopscience.iop.org/article/10.1088/0953-4075/39/15/S04
> Collected: 2026-09-20
> Published: 2006-08-14
> Zotero parent key: QXJKUTCZ
> Evidence: Zotero indexed PDF text

Journal of Physics B: Atomic, Molecular and Optical Physics
Theory of the linear polarizability of a two-level atom*
To cite this article: Rodney Loudon and Stephen M Barnett 2006 J.Phys.B:At.Mol.Opt.Phys. 39 S555
View the article online for updates and enhancements.
You may also like
Anisotropic density fluctuations, plasmons, and Friedel oscillations in nodal line semimetal Jun-Won Rhim and Yong Baek Kim

The polarizability of a confined atomic system: an application of the Dalgarno–Lewis method T V C Antão and N M R Peres

Influence of the quantum well dielectric permittivity on the two-dimensional plasmon-phonon V Ya Aleshkin, A A Dubinov and A O Rudakov

This content was downloaded from IP address 132.68.239.10 on 31/10/2024 at 09:18


 INSTITUTE OF PHYSICS PUBLISHING JOURNAL OF PHYSICS B: ATOMIC, MOLECULAR AND OPTICAL PHYSICS
J. Phys. B: At. Mol. Opt. Phys. 39 (2006) S555–S563 doi:10.1088/0953-4075/39/15/S04
Theory of the linear polarizability of a two-level atom*
Rodney Loudon1 and Stephen M Barnett2
1 Electronic Systems Engineering, University of Essex, Colchester CO4 3SQ, UK 2 Department of Physics, University of Strathclyde, Glasgow G4 0NG, UK
Received 26 January 2006, in final form 12 March 2006 Published 24 July 2006 Online at stacks.iop.org/JPhysB/39/S555
Abstract
The polarizability of a two-level atom in the presence of radiative damping alone is derived by a Green function calculation. The rotating-wave approximation is not made, either in the interaction of the atom with the incident light or in its interaction with the scattered optical field. In contrast to previous work, the derivation takes account of the modification of the system ground state brought about by the non-rotating-wave part of the latter interaction. The final expression satisfies the optical theorem in addition to the other general requirements on the polarizability.
1. Introduction
The dynamic electronic polarizability α(ω) plays a key role in the interpretation of a range of optical experiments on atoms and molecules. With only the ground state populated, α(ω) has the form of a sum of contributions from the various excited states. It is therefore possible to derive expressions for the contribution of the lowest excited state by consideration of a two-level atom. Many optical processes for the atom are well described by a nonresonant form of α(ω),
α(ω) = d2
3 ̄h
{1
ω0 − ω + 1
ω0 + ω
}
, (1)
where d is the real transition dipole moment, ω0 is the transition frequency and the 3 comes from an orientation average [1]. The two terms in (1) arise respectively from the rotatingwave and non-rotating-wave terms in the Hamiltonian that describes the interaction between the incident light and the atom. Much use of the multi-level version of this nonresonant polarizability has been made in a wide variety of calculations on radiation–molecular and intermolecular interactions (see [2] for example). The main interest of the present paper, however, is focused on the resonant properties of the polarizability, where radiative frequency shifts δ and damping terms iγ must be included in the denominators, so that α(ω) becomes complex. The damping terms represent the decay
* This paper was presented at The Power of QED meeting at University College London on 12 September 2005 and it is dedicated to the memory of Edwin Power.
0953-4075/06/150555+09$30.00 © 2006 IOP Publishing Ltd Printed in the UK S555


 S556 R Loudon and S M Barnett
of an excited atom by emission of radiation into the scattered field modes. At the simplest level of approximation, γ is taken as γ (ω0), equal to one half the spontaneous emission rate in the atomic excited state, proportional to ω3
0 and independent of the frequency ω of the incident light. Many textbook derivations, for example [3], insert the damping ‘by hand’ to obtain the form
α(ω) = d2
3 ̄h
{1
ω0 − ω − iγ (ω0) + 1
ω0 + ω + iγ (ω0)
}
, (2)
where ω is set equal to ω0 in the general expression
γ (ω) = d2ω3/6π ε0 ̄hc3. (3)
The generalization to a complex polarizability brings in a range of universal conditions on the form of α(ω) [4]. Thus the causality condition that excitation of the atom cannot precede the arrival of incident light requires all the poles of α(ω) to lie in the negative imaginary part of the complex ω plane. Again, although ω is usually considered as a positive quantity, the requirement that a real field must produce a real polarization produces the so-called crossing relation,
α(−ω) = α∗(ω). (4)
Finally, energy conservation requires the rate of removal of energy from the incident light by interaction with the atom, proportional to Im α(ω), to equal the rate of emission of scattered light by the atom, proportional to |α(ω)|2. In detail,
ω
ε0c Im α(ω) = ω4
2π ε2
0c4 |α(ω)|2 = σ (ω), (5)
where σ (ω) is the total scattering cross section for light of frequency ω. This relation is known as the optical theorem.
The textbook form of α(ω) given in (2) has its poles in the negative imaginary part of the complex plane and the crossing relation (4) is satisfied. It does not, however, satisfy the optical theorem, principally because (2) contains the damping rate from (3) evaluated at the transition frequency ω0. Previous derivations of the polarizability or susceptibility of a twolevel atom have improved the expression in (2) by calculations that include its interaction with scattered light in the Hamiltonian of the coupled atom–field system. The methods used include diagonalization of the Hamiltonian [3], a Green function evaluation similar to that used below [5] and Laplace transform solution of the Schr ̈odinger equation [6]. However, all these calculations use the rotating-wave approximation (RWA), with the non-rotating-wave terms in the Hamiltonian for the interaction of the atom with the scattered light neglected. It has recently been shown [7] that this RWA misses important contributions to γ . The damping γ (ω) is proportional to ω3 in the corrected expression for α(ω), consistent with the notion that the scattering of light of frequency ω should be controlled by emission into field modes of this same frequency. More recently still, it has been shown [8] that even the corrected expression for α(ω) is deficient, as it does not satisfy the optical theorem in (5), and energy conservation is therefore violated. The aim of the present paper is to rectify this deficiency. It is shown in section 2 that the problem arises from the retained non-rotating-wave parts in the interaction of the atomic transition with the continuum of scattered field modes. These parts provide a coupling of the usually-assumed system ground state, with the atom in its lowest eigenstate and no scattered photon excited, to the excited atomic eigenstate plus a single scattered photon. The true system ground state is thus a linear combination of these two states, which must be used in the evaluation of various equilibrium expectation values that occur in the expression for the


 Theory of the linear polarizability of a two-level atom S557
πˆ πˆ †
e
g
hω0
0
gk
Figure 1. Representation of the two-level atom with the notation for transition operators and interaction strength.
polarizability. The Green function calculation of the polarizability is outlined in section 3 and the relevant Green functions are evaluated in section 4. The properties of α(ω) are derived in section 5 and the conclusions are given in section 6. Parallel independent derivations of the same expression for the polarizability have been made by other methods of calculation [9].
2. Two-level atomic model
Consider an atom that has two levels, ground |g〉 and excited |e〉, with energies 0 and  ̄hω0, as represented in figure 1. The transition between the two levels has coupling coefficient gk and the associated projection operators are denoted as
πˆ = |g〉〈e| and πˆ † = |e〉〈g|. (6)
The Hamiltonian is
Hˆ =  ̄hω0πˆ †πˆ +
∫
dk  ̄hωkaˆ†
kaˆk + i ̄h
∫
dk gk
(aˆk − aˆ†
k
)(πˆ † + πˆ ), (7)
where aˆ†
k and aˆk are the photon creation and destruction operators, with commutator
[aˆk, aˆ†
k′
] = δ(k − k′). (8)
The photon vacuum state is denoted by |0〉 and the excited states by |{nk}〉. The single-photon states have the orthonormalization
〈1k|1k′ 〉 = δ(k − k′). (9)
The coupling coefficient in (7) is given by
 ̄hgk =
(  ̄hωk
16π 3ε0
)1/2
ek · d, (10)
where ek is the mode polarization and d is the dipole moment of the transition, assumed real for simplicity. The two transverse polarizations are not shown explicitly but are included in the wavevector label k, in order to simplify the notation. Note that the rotating-wave approximation is not made in the coupling term in (7), as the complete interaction is needed to obtain the correct expression for the polarizability [7]. It follows that the state |g〉|0〉 with the atom in its ground state and no photons excited is not an eigenstate of the Hamiltonian [10, 11]. In order to calculate various expectation values needed for the polarizability, it is necessary to derive the form of the system ground state. To a


 S558 R Loudon and S M Barnett
sufficient approximation for present purposes, we can use the result of standard second-order perturbation theory [12] to write the ground state as [11]
|g〉|0〉 + i
∫
dk gk
ωk + ω0
|e〉|1k〉 − 1
2
∫
dk g2
k
(ωk + ω0)2 |g〉|0〉, (11)
where an additional term of order g2
k in |g〉|1k, 1k′〉 is omitted as it does not contribute
to the present calculation. The perturbed eigenstate is normalized to order g2
k. It is now straightforward to calculate the ground-state expectation values
〈[πˆ , πˆ †]〉 = 1 − 2
∫
dk g2
k
(ωk + ω0)2 , (12)
〈aˆ†
k′ aˆk
〉 = gk′ gk
(ωk′ + ω0)(ωk + ω0) , (13)
〈aˆkπˆ †〉 = 0 (14)
and
〈aˆ†
kπˆ †〉 = −i gk
ωk + ω0
, (15)
all correct to order g2
k. These expectation values are used in sections 4 and 5.
3. Green function method
The linear polarizability α(ω) and susceptibility χ (ω) of the two-level atom for a probe field of frequency ω are calculated by the use of thermodynamic Green functions [13], using the relation
α(ω) = − d2
3 εli→m0+ Gω+iε(πˆ + πˆ †, πˆ + πˆ †) = ε0V χ (ω), (16)
where the susceptibility refers to a medium with volume V per atom. The factor of 3 in the denominator results from a three-dimensional average of the transition dipole orientation. The Green function at temperature T for general operators Aˆ and Bˆ is defined by
Gω+iε(Aˆ , Bˆ ) = ∑
r,s
exp(−Er /kBT ) − exp(−Es/kBT )
Tr{exp(−Hˆ /kBT )}
〈r|Aˆ |s〉〈s|Bˆ |r〉
 ̄h(ω + iε) + Er − Es
, (17)
where |r〉, |s〉 and Er , Es are the exact eigenstates and eigenvalues respectively of the complete system Hamiltonian Hˆ . The addition of a positive infinitesimal imaginary part to ω ensures that the Green function is retarded, with its poles in the lower half of the complex plane, as required by causality. The polarizability is defined for both positive and negative frequencies and it must satisfy the crossing relation (4), although evaluations are usually made for positive ω. The frequencies that appear in the Hamiltonian (7) are strictly positive. The Green function has the property of distributivity with respect to arguments that consist of sums of operators, and (16) is therefore expanded as
α(ω) = − d2
3 εli→m0+{Gω+iε(πˆ , πˆ †) + Gω+iε(πˆ †, πˆ †) + Gω+iε(πˆ †, πˆ ) + Gω+iε(πˆ , πˆ )}. (18)
It follows from the basic definition of the Green function [13] that
Gω+iε(πˆ †, πˆ ) = G∗−ω+iε(πˆ , πˆ †) and Gω+iε(πˆ , πˆ ) = G∗−ω+iε(πˆ †, πˆ †). (19)


 Theory of the linear polarizability of a two-level atom S559
The crossing relation (4) is therefore automatically satisfied and only the first two Green functions in (18) need be calculated explicitly. The calculation proceeds via the equation of motion for general operators in the form [13, 14]
 ̄hω G(Aˆ , Bˆ ) = 〈[Aˆ , Bˆ ]〉 + G([Aˆ , Hˆ ], Bˆ ), (20)
where the ω + iε subscript on G is understood. Where appropriate, we use the technique of truncation of the hierarchy of equations for the Green functions generated by successive applications of (20). The temperature is here taken as T = 0, so that only the ground-state expectation values derived in section 2 are needed.
4. Polarizability Green functions
It follows from (7) that
[πˆ , Hˆ ] =  ̄hω0πˆ + i ̄h
∫
dk gk
(aˆk − a†
k
)[πˆ , πˆ †]. (21)
The equation of motion from (20) for the first Green function in (18) is therefore
 ̄h(ω − ω0)G(πˆ , πˆ †) = 〈[πˆ , πˆ †]〉 + i ̄h
∫
dk gkG((aˆk − aˆ†
k
)[πˆ , πˆ †], πˆ †). (22)
This is the first equation in the hierarchy and it brings in a new Green function. It is convenient to separate the new Green function into the parts that involve the photon destruction and the photon creation operators. Straightforward application of the equation of motion (20) gives
 ̄h(ω − ωk)G(aˆk[πˆ , πˆ †], πˆ †) = −2〈aˆkπˆ †〉
+ i ̄h
∫
dk′ gk′ G({aˆk
(aˆk′ − aˆ†
k′
) + (aˆk′ − aˆ†
k′
)aˆk
}(πˆ − πˆ †), πˆ †) (23)
 ̄h(ω + ωk)G(aˆ†
k[πˆ , πˆ †], πˆ †) = −2〈aˆ†
kπˆ †〉
+ i ̄h
∫
dk′ gk′ G({aˆ†
k
(aˆk′ − aˆ†
k′
) + (aˆk′ − aˆ†
k′
)aˆ†
k
}(πˆ − πˆ †), πˆ †). (24)
These equations form the second stage of the hierarchy and no approximations have been made so far in the calculation. However, the expectation value (14) that appears on the right of (23) can be neglected to second order in gk. Further, the hierarchy can be truncated by the use of approximations to decouple the Green functions of higher order in gk. The expectation value (13) of photon operators that appear in the Green functions on the right-hand sides of both (23) and (24) gives contributions of third order in gk. The integrals can thus be approximated by taking vacuum expectation values of the photon operators and, with the use of (8),
 ̄h(ω − ωk)G(aˆk[πˆ , πˆ †], πˆ †) = −i ̄hgkG(πˆ − πˆ †, πˆ †) (25)
and
 ̄h(ω + ωk)G(aˆ†
k[πˆ , πˆ †], πˆ †) = −2〈aˆ†
kπˆ †〉 + i ̄hgkG(πˆ − πˆ †, πˆ †). (26)
The Green function needed for (22) is therefore
G((aˆk − aˆ†
k
)[πˆ , πˆ †], πˆ †) = 2〈aˆ†
kπˆ †〉
 ̄h (ωk + ω) + igk
(1
ωk − ω − 1
ωk + ω
)
G(πˆ − πˆ †, πˆ †). (27)


 S560 R Loudon and S M Barnett
The new Green function on the right-hand side of (27) is the second in the basic expression (18) for the polarizability. Its equation of motion is
(ω + ω0)G(πˆ †, πˆ †) = −i
∫
dk gkG((aˆk − aˆ†
k
)[πˆ , πˆ †], πˆ †) (28)
and the Green function on the right-hand side is given by (27). Thus (22), (27) and (28) form a closed set of equations for the required Green functions. It is convenient to define
I (ω) =
∫
dk g2
k
(1
ωk − ω − 1
ωk + ω
)
= −I (−ω), (29)
and the equations to be solved then take the forms


[ω − ω0 + I (ω)]G(πˆ , πˆ †) = 〈[πˆ , πˆ †]〉
 ̄h + 2i
 ̄h
∫
dk gk
〈aˆ†
kπˆ †〉
ωk + ω + I (ω)G(πˆ †, πˆ †)
[ω + ω0 + I (ω)]G(πˆ †, πˆ †) = − 2i
 ̄h
∫
dk gk
〈aˆ†
kπˆ †〉
ωk + ω + I (ω)G(πˆ , πˆ †).
(30)
The solutions are
G(πˆ , πˆ †) = −
[ω0 + ω + I (ω)]〈[πˆ , πˆ †]〉 + 2i(ω0 + ω) ∫ dk gk
〈aˆ†
kπˆ †〉
ωk + ω
 ̄h[ω2
0 − ω2 − 2ωI (ω)] (31)
G(πˆ †, πˆ †) = −
I (ω)〈[πˆ , πˆ †]〉 + 2i (ω0 − ω) ∫ dk gk
〈aˆ†
kπˆ †〉
ωk + ω
 ̄h [ω2
0 − ω2 − 2ωI (ω)] , (32)
correct to order g2
k in numerators and denominators. The two remaining Green functions needed for the polarizability in (18) are obtained from the relations (19), to give
α(ω) = 2d2ω0
3 ̄h
〈[πˆ , πˆ †]〉 + 2 ∫ dk g2
k
ωk + ω0
(1
ωk − ω + 1
ωk + ω
)
ω2
0 − ω2 − 2ωI (ω) , (33)
with the use of (15) and (29).
5. Properties of the two-level polarizability
Consider first the denominator of (33). With iε now added to ω in the definition (29) of I (ω), the values of the integrals in the limit ε → 0+ are conveniently separated into real and imaginary parts as
εli→m0+
∫
dk g2
k
ωk ± ω ± iε = ±(ω) ∓ i ±(ω), (34)
where the real part on the right is a level shift, given by the principal-value integral
±(ω) = ℘
∫
dk g2
k
ωk ± ω , (35)
and the imaginary part is a level width or damping rate, given by
±(ω) = π
∫
dk g2
kδ (ωk ± ω) . (36)


 Theory of the linear polarizability of a two-level atom S561
As the ωk are all positive, evaluation of the integrals with the use of (10) and inclusion of the two transverse polarizations gives [3]
+(ω) = − d2ω3
6π ε0 ̄hc3 θ(−ω) and −(ω) = d2ω3
6π ε0 ̄hc3 θ(ω), (37)
where θ(ω) is the usual unit step function. It follows that
εli→m0+ I (ω + iε) = −(ω) + i −(ω) − +(ω) + i +(ω). (38)
The quantities −(ω) and −(ω) are interpreted as the frequency shift and damping of level |e〉 respectively, while +(ω) and +(ω) are the shift and damping of level |g〉. The two shifts are nonzero but the ground-state damping vanishes for positive frequencies, as in (37). For frequencies close to the resonance at ω = ω0, it is usually a good approximation to substitute ω0 for ω in the expressions (35) and (36) for the level shifts and the surviving width −(ω). The resonant level damping from (37) is then
−(ω0) = d2ω3
0
/6π ε0 ̄hc3. (39)
The FWHM of the resonant transition is twice this quantity, in agreement with the expression for the decay rate of the excited state obtained, for example, from Fermi’s golden rule [3]. More generally, the level dampings in (37) can be written as a single expression
γ (ω) ≡ −(ω) + +(ω) = d2 |ω|3/6π ε0 ̄hc3, (40)
valid for all real ω, positive and negative. The level shifts in I (ω) can also be combined with the use of (35) as
δ(ω) ≡ −(ω) − +(ω) = ℘
∫
dk 2ωg2
k ω2
k − ω2 . (41)
The frequency ω +δ(ω) is an odd function of ω. Note that the denominator of the polarizability (33) contains the sum γ (ω) of the widths but the difference δ(ω) of the shifts. Now consider the numerator of (33). The expectation-value first term, given by (12),
contains an integral that differs from the level shift integral in (35), but it has the property
∫
dk g2
k
(ωk + ω0)2 < 1
ω0
∫
dk g2
k
ωk + ω0
= +(ω0)
ω0
. (42)
The integral term in the numerator of (33) is expressed with the use of (34) and a partial-fraction calculation as
2
∫
dk g2
k
{1
ωk − ω
1
ω0 + ω + 1
ωk + ω
1
ω0 − ω − 1
ωk + ω0
2ω0 ω2
0 − ω2
}
=2
ω2
0 − ω2 {(ω0 − ω)[ −(ω) − +(ω0) + i −(ω)]
+ (ω0 + ω)[ +(ω) − +(ω0) − i +(ω)]}
=2
ω2
0 − ω2 {ω0 [ −(ω) + +(ω) − 2 +(ω0) + i ( −(ω) − +(ω))]
− ω [ −(ω) − +(ω) + i ( −(ω) + +(ω))]} , (43)
with use of the property +(ω0) = 0 from (37). The final expression for the polarizability is now obtained by substitution of (12) and (43) into the numerator of (33). Substitution of (38) gives the denominator of (33) as
ω2
0 − ω2 − 2ω[ −(ω) − +(ω) + i( −(ω) + +(ω))]. (44)
The crossing relation (4) is clearly satisfied.


 S562 R Loudon and S M Barnett
The polarizability takes a much simpler form if it is assumed that the contribution in (42) and the level shifts in (43) and (44) can be ignored or amalgamated into appropriate renormalized frequencies, when
α(ω) ≈ 2d2ω0
3 ̄h
1 + 2i −(ω)
ω0 + ω − 2i +(ω)
ω0 − ω ω2
0 − ω2 − 2iω [ −(ω) + +(ω)] . (45)
Two of the main quantities of interest determined by the polarizability are the rate of loss of energy from an incident beam by excitation of the atom and the rate of re-radiation of energy by the excited atom, whose equality is expressed by the optical theorem (5). It follows from (37) and (45) that, for positive ω and correct to order d4,
Im α(ω) = 4d2
3 ̄h
ω2
0 −(ω)
(ω2
0 − ω2)2 + 4ω2 2−(ω)
= 2d4
9π ε0 ̄h2c3
ω2
0ω3
(ω2
0 − ω2)2 + 4ω2 2−(ω)
, (46)
and
|α(ω)|2 = 4d4
9 ̄h2
ω2
0
(ω2
0 − ω2)2 + 4ω2 2−(ω)
. (47)
The optical theorem is therefore satisfied and the total cross-section defined in (5) shows the usual Rayleigh scattering ω4 dependence for ω ω0 [3], with
σ (ω) = 2d4ω4
9π ε2
0  ̄h2 c4 ω2
0
. (48)
Note that the expression (47) for |α(ω)|2 is reproduced by the sum of the squares of the real and imaginary parts of α(ω) from (45) only when the -dependent terms in the numerator and denominator of the second factor on the right are neglected. This is consistent with the accuracy of the calculation, which is valid only to order g2
k.
Note finally that the static polarizability is a real quantity on account of the vanishing of +(0) and −(0) given by (37). For the simpler form of α(ω) given by (45),
α(0) ≈ 2d2/3 ̄hω0, (49)
and the more general form with numerator taken from (12) and (43) has a small additional real correction from the level shift terms.
6. Conclusions
The main results of the calculation are the expressions for the polarizability of a two-level atom obtained by combination of (33), (12), (43) and (44) or, in a simplified form, by (45). These expressions contain denominators equivalent to those found in previous work [7] but the numerators are different. The differences are caused by corrections evaluated here to take account of the form (11) of the system ground state, which results from the non-rotatingwave terms in the coupling of the atom to the scattered field. This procedure produces the more complicated form of numerator given by the sum of expressions from (12) and (43). The previous expression [7] for α(ω) is reproduced when only the 1 is retained in (12) and all of the contribution in (43) is neglected; similarly, the simplified expression (45) reverts to previous results when only the 1 in the numerator is retained. Conformity with the requirements of causality and the crossing relation is ensured by the Green function method of calculation, as explained in section 3. The more elusive requirement of energy conservation, expressed by the optical theorem, is achieved via the additional complexity in the numerator of the


 Theory of the linear polarizability of a two-level atom S563
polarizability derived here. In contrast to previous derivations, our final expressions for α(ω) thus satisfy all of the general requirements on the polarizability of a two-level atom. The two-level atom treated here is, of course, a drastic approximation to the multi-level atoms that pervade the real world. It provides a reasonable model for the spectral properties of atoms at frequencies ω close to resonance with an atomic transition frequency ω0. The nonresonant second terms in the expressions (1) and (2) for the polarizability can be ignored for such frequencies and the more exact expressions derived here can be greatly simplified. Nonresonant phenomena are poorly described by two-level theories, when many excited states generally make significant contributions. Against this background, the very detailed attention given here to the two-level atom is justified as a first step towards a multi-level theory. It seemed too large a jump to treat the general atom initially, when even two levels had not been treated in a way that respected the conservation of energy. The results of work currently in progress on the multi-level polarizability, including the effects of elevated temperature, will be reported in due course.
Acknowledgments
The calculations reported here were carried out in parallel with alternative derivations of essentially the same results that will be published separately [9]. We thank Paul Berman, Bob Boyd and Peter Milonni for their generous sharing of information on their work, which greatly assisted our own efforts. We have also benefited from communications with David Andrews and Gabriel Barton.
References
[1] Power E A and Thirunamachandran T 1971 J. Chem. Phys. 55 5322 [2] Passante R, Power E A and Thirunamachandran T 1998 Phys. Lett. A 249 77 [3] Loudon R 1973 The Quantum Theory of Light 1st edn (Oxford: Oxford University Press) [4] Nussenzveig H M 1972 Causality and Dispersion Relations (New York: Academic) [5] Jedrkiewicz O and Loudon R 2000 J. Opt. B 2 R47 [6] Agarwal G S and Boyd R W 2003 Phys. Rev. A 67 043821 [7] Milonni P W and Boyd R W 2004 Phys. Rev. A 69 023814 [8] Milonni P W 2005 unpublished [9] Berman P, Boyd R W and Milonni P W 2006 in preparation [10] Milonni P W 1994 The Quantum Vacuum (San Diego: Academic) [11] Compagno G, Passante R and Persico F 1995 Atom–Field Interactions and Dressed Atoms (Cambridge: Cambridge University Press) [12] Schiff L I 1955 Quantum Mechanics (New York: McGraw-Hill) [13] Zubarev D N 1960 Sov. Phys.—Usp. 3 320 [14] Pike E R and Swain S 1971 J. Phys. A: Gen. Phys. 4 555
