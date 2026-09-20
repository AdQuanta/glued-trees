# Linear polarizabilities of two- and three-level atoms - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.77.043835
> Collected: 2026-09-20
> Published: 2008-04-29
> Zotero parent key: VUFJDL5R
> Evidence: Publisher or author-preprint PDF

PHYSICAL REVIEW A 77, 043835 共2008兲

                                   Linear polarizabilities of two- and three-level atoms

                                                               Peter W. Milonni
                                         104 Sierra Vista Drive, White Rock, New Mexico 87544, USA

                                                                Rodney Loudon
                        Computing and Electronic Systems, University of Essex, Colchester CO4 3SQ, United Kingdom

                                                                Paul R. Berman
         Michigan Center for Theoretical Physics, FOCUS Center, and Physics Department, University of Michigan, Ann Arbor,
                                                    Michigan 48109-1040, USA

                                                              Stephen M. Barnett
                             Department of Physics, University of Strathclyde, Glasgow G4 0NG, United Kingdom
                                          共Received 17 November 2007; published 29 April 2008兲
                    Different expressions for the linear polarizability of a two-level atom with radiative corrections have been
                 derived recently. We show that an expression said to differ from that obtained by the present authors is in fact
                 consistent with it. The same-sign and opposite-sign prescriptions for linewidths are revisited with respect to the
                 polarizability, the scattering amplitude, and the optical theorem. Both prescriptions represent approximations to
                 more general expressions in the two-level case, and neither is correct for transitions between excited atomic
                 states, as we demonstrate by calculating the linear polarizability of a three-level atom.

                 DOI: 10.1103/PhysRevA.77.043835                      PACS number共s兲: 42.65.An, 32.10.Dk, 32.70.Jz, 32.80.⫺t


                         I. INTRODUCTION                                        In the context of Raman scattering the + sign prescription
   The linear response of an atom in state i to a field of                  has been used by Placzek 关1兴 and Hassing and Svendsen 关2兴,
                                                                            for instance. The latter authors state that the majority of au-
frequency ␻ is described by the polarizability ␣i共␻兲: the
                                                                            thors use the − sign prescription, and Raman cross sections
electric dipole moment p共t兲 induced by the electric field
                                                                            with the − sign are indeed found in various publications 关3兴.
E0 cos ␻t is                                                                    The recent interest in these different sign prescriptions
                  1                                                         was stimulated by Andrews et al. 关4兴, who argued in favor of
            p共t兲 = 关␣i共␻兲E0e−i␻t + ␣i共− ␻兲E0ei␻t兴.                 共1兲      the − sign. Other authors 关2,5–8兴 have presented arguments
                  2
                                                                            in favor of the + sign. The general case of frequency-
The imaginary part of the polarizability is due to damping                  dependent damping rates has not, to our knowledge, been
effects such as spontaneous emission, and the reality of p共t兲               analyzed. The special case of radiative damping, where
demands that the “crossing relation”                                        ␥ ji共␻兲 ⬀ ␻3, has been treated using the model in which the
                                                                            polarizable particle is a two-level atom 关6–10兴. Even in this
                           ␣i共− ␻兲 = ␣ⴱi 共␻兲                       共2兲      simplified model the calculation is nontrivial because it re-
be satisfied. The complex polarizability is generally written               quires a treatment of radiative corrections beyond the so-
in terms of the atom’s transition frequencies ␻ ji = 共E j                   called rotating-wave approximation. The polarizability in
− Ei兲 / ប and transition electric dipole moments d ji in one of             this model has been calculated using the Heisenberg and
                                                                            Schrödinger pictures 关6,8兴, time-dependent Green functions
two ways:
                                                                            关7兴, and Feynman propagators 关9兴.
    ␣ i共 ␻ 兲 =
                  1
                    兺
                 3ប j
                            冉
                      兩d ji兩2
                                     1
                                              +
                                                      1
                              ␻ ji − ␻ − i␥ ji ␻ ji + ␻ ⫾ i␥ ji
                                                               冊. 共3兲
                                                                                The calculation in Ref. 关6兴 supports the + sign convention,
                                                                            but small correction terms are required in order to satisfy the
                                                                            optical theorem in the case of Rayleigh scattering, where the
A similar formula applies in the more general case of Raman                 incident and scattered field frequencies are identical 关7,8兴.
scattering, where two photon frequencies, those of the inci-                From their elegant analysis for a two-level atom, Bialynicki-
dent and scattered fields, appear in the denominators; again                Birula and Sowiński 关9兴, while concluding that the + sign
the scattering tensor is written with either a + sign or a − sign           prescription applies for the polarizability, obtain an expres-
in the nonresonant term. The sign of the damping rate ␥ ji                  sion “quite different from” that derived in Ref. 关7兴, which is
with respect to the transition frequency ␻ ji in the resonant               essentially the same as that obtained later by different meth-
and nonresonant terms defines the “opposite sign” 共+兲 and                   ods in Ref. 关8兴. They also conclude that it is the − sign
“same sign” 共−兲 prescriptions. The crossing relation obvi-                  prescription that applies for the scattering amplitude.
ously implies that the + sign in Eq. 共3兲 is the correct choice,                 In the following section we review the results obtained in
and this is consistent with the causality condition that ␣i共␻兲              Refs. 关7–9兴 for the polarizability of a two-level atom with
must be analytic in the upper half of the complex ␻ plane;                  radiative damping, and show that they are identical in a
but the situation is not nearly so simple because the damping               weak-coupling approximation. The results are consistent
rates are in general frequency-dependent.                                   with the opposite-sign prescription when an approximation is

1050-2947/2008/77共4兲/043835共12兲                                      043835-1                            ©2008 The American Physical Society
MILONNI et al.                                                                                 PHYSICAL REVIEW A 77, 043835 共2008兲


                                                                                               关âk,âk⬘兴 = ␦共k − k⬘兲.
                                                                                                       †
made to a more general expression for the polarizability. We                                                                               共7兲
also consider briefly the scattering amplitude in this model,
which was not considered in Refs. 关6–8兴, and present a
simple argument supporting the conclusion of Bialynicki-
                                                                                                  A. Polarizability
Birula and Sowiński 关9兴 that the − sign applies in the lowest-
order approximation to the scattering amplitude.                         We define
   In Sec. III, we consider a three-level atom model in which
transitions are allowed between the ground level and the first
excited level and between the two excited levels. Following
a time-dependent Green function approach used previously
                                                                                          ⌬12共⫾ ␻兲 = P      冕    dk
                                                                                                                         jk2
                                                                                                                      ␻k ⫾ ␻
                                                                                                                                           共8兲

for the two-level model 关7兴, we calculate the contribution to       and
the polarizability from the transition between the two excited
states. Whereas one could justifiably argue for the opposite-
sign expression as an approximation to the two-level polar-
izability, we find that neither of the two sign prescriptions for
                                                                               ⌫12共⫾ ␻兲 = ␲        冕   dkjk2 ␦共␻k ⫾ ␻兲

the polarizability provide valid approximations in the three-
level case. Our conclusions are summarized in Sec. IV. In the
Appendix we briefly describe the calculation of the three-
                                                                                              =
                                                                                                     2
                                                                                                    d12
                                                                                                  6␲⑀0បc3
                                                                                                            冕0
                                                                                                                ⬁
                                                                                                                    d⍀⍀3␦共⍀ ⫾ ␻兲,          共9兲

level polarizability using the Schrödinger picture.
                                                                    where P denotes the principal part of the integral, and
   Nonresonant contributions to resonant Rayleigh cross sec-
                                                                    −⌬12共+␻兲 and −⌬12共−␻兲 with ␻ ⬎ 0 are, respectively, the
tions 关11兴 and the natural line shape of the hydrogen atom
                                                                    共unrenormalized兲 radiative level shifts of the lower and upper
关12兴 have recently been evaluated numerically for their pos-
                                                                    states. Without an applied field of frequency ␻ the 共vacuum兲
sible relevance to the determination of atomic energy levels
                                                                    level shifts are −⌬12共␻0兲 and −⌬12共−␻0兲, where ␻0 共⬎0兲 is
and fundamental constants from observed spectra. In evalu-
                                                                    the atom’s transition frequency. The quantity ⌫12共−␻兲 for ␻
ating such “problematic nonresonant contributions” 关11兴 the
                                                                    ⬎ 0 is half the spontaneous emission rate of the upper state,
effects of damping on them have been ignored, which is an
                                                                    whereas ⌫12共␻兲 vanishes for ␻ ⬎ 0. The notation here is con-
excellent 共and generally assumed兲 approximation, given the
                                                                    sistent with that of the following section, where the expres-
relative smallness of the nonresonant terms. The questions
                                                                    sions 共8兲 and 共9兲 are derived.
addressed in this and the earlier papers related to the fre-
                                                                        The ground-state polarizability ␣1共␻兲 obtained in Refs.
quency dependence of the decay parameters, while of funda-
                                                                    关7,8兴 may be written in this notation as 关14兴
mental theoretical interest, appear to be of no practical con-
cern for even the most accurate of present spectroscopic                                  2
                                                                                        2d12 ␻0            1
studies.                                                                   ␣ 1共 ␻ 兲 =
                                                                                          ប ␻20 − ␻2 − 2i␻关␥12共␻兲 − i␦12共␻兲兴
                     II. TWO-LEVEL ATOM

  The interaction Hamiltonian for a two-level atom and the
                                                                                         冋
                                                                                        ⫻ 1+2
                                                                                                   ⌬12共− ␻兲 − ⌬12共␻0兲 + i⌫12共− ␻兲
                                                                                                              ␻ + ␻0
quantized electromagnetic field is

               Ĥ⬘ = iប   冕   dk共âk − âk† 兲jk共 ˆ␴ + ˆ␴†兲.   共4兲
                                                                                        +2
                                                                                             ⌬12共␻0兲 − ⌬12共␻兲 + i⌫12共␻兲
                                                                                                       ␻ − ␻0
                                                                                                                        ,      册          共10兲

                                                                    with
The coupling coefficient is defined by

                   បjk =   冉    ប␻k 1/2
                               16␲3⑀0
                                        冊
                                        ek · d12 ,            共5兲
                                                                                         ␥12共␻兲 = ⌫12共− ␻兲 + ⌫12共␻兲,

                                                                                         ␦12共␻兲 = ⌬12共− ␻兲 − ⌬12共␻兲.                      共11兲
where âk and âk† are destruction and creation operators for
mode k, respectively, ek is the mode polarization and d12 is        The expression 共10兲 satisfies the crossing relation 共2兲 as well
the transition dipole moment connecting the lower 共兩1典兲 and         as the optical theorem in the form
upper 共兩2典兲 states, and is assumed real 关13兴. The two trans-
verse polarizations are not shown explicitly but are included
in the wave-vector label k, in order to simplify the notation.
We follow here the notation of Refs. 关6,8兴 for the lowering
                                                                            Im ␣1共␻兲 =
                                                                                               1
                                                                                                    冉 冊
                                                                                                   2␻3
                                                                                              4␲⑀0 3c3
                                                                                                       兩␣1共␻兲兩2                共␻ ⬎ 0兲,   共12兲

and raising operators for the two-level atom:
                                                                    when terms up to fourth order are retained, consistent with
                   ˆ␴ = 兩1典具2兩,         ˆ␴† = 兩2典具1兩,               the approximations made in obtaining Eq. 共10兲 关7,8兴. Equa-
                                                                    tion 共12兲 is simply the statement that the power lost by the
                                                                    applied field equals the power radiated by the atom. If the
                 兩2典具2兩 = ␴ˆ †␴ˆ ,       兩1典具1兩 = ␴ˆ ␴ˆ † .   共6兲
                                                                    small, second, and third terms in brackets in Eq. 共10兲 are
The photon operator commutator is                                   neglected, we obtain the polarizability derived in Ref. 关6兴:

                                                              043835-2
LINEAR POLARIZABILITIES OF TWO- AND THREE- …                                                             PHYSICAL REVIEW A 77, 043835 共2008兲


             ␣ 1共 ␻ 兲 ⬇
                           2
                          d12
                               冋         1
                           ប ␻0 − ␻ − ␦12共␻兲 − i␥12共␻兲
                                                                             The second-order polarizability obtained by Bialynicki-
                                                                          Birula and Sowiński is obtained by setting b̃ = 0 关9兴. To this

                                                      册
                                                                          order,
                                          1
                          +                             .        共13兲                                         2␻0
                              ␻0 + ␻ + ␦12共␻兲 + i␥12共␻兲
                                                                                                       ˜ 共␻兲 + i sgn共␻兲⌫
                                                                                        ␻20 − ␻2 − 2␻0关⌬               ˜ 共␻兲兴
This has the physically appealing feature that the radiative
frequency shift −␦12共␻兲 in the denominators is the difference                                                     1
of the upper- and lower-state level shifts, and the damping                                  ⬇
terms are consistent with the opposite-sign prescription. As                                     ␻0 − ␻ − ˜              ˜ 共␻兲
                                                                                                          ⌬共␻兲 − i sgn共␻兲⌫
already noted, however, Eq. 共13兲 does not satisfy the optical                                                     1
theorem.                                                                                         +                                 .         共19兲
                                                                                                              ˜              ˜ 共␻兲
                                                                                                     ␻0 + ␻ − ⌬共␻兲 − i sgn共␻兲⌫
   If we retain the small terms in brackets in Eq. 共10兲 but let
them approach zero, we can bring them into the denomina-                  This is consistent with the same-sign convention for the po-
tors 关1 + x ⬇ 1 / 共1 − x兲兴 and write                                      larizability. For ␻ ⬎ 0, for instance,
␣ 1共 ␻ 兲 ⬇                                                                                           2␻0
       2
     2d12 ␻0                               1                                                  ˜ 共␻兲 + i sgn共␻兲⌫
                                                                               ␻20 − ␻2 − 2␻0关⌬               ˜ 共␻兲兴
                                                                      ,
        ប                      ˜ 共␻兲 + i sgn共␻兲⌫
                ␻20 − ␻2 − 2␻0关⌬               ˜ 共␻兲 − 2⌬ 共␻ 兲兴
                                                         12 0                                        1                            1
                                                                                 ⬇                                  +                            .
                                                                 共14兲                ␻0 − ␻ − ˜       ˜ 共␻兲
                                                                                              ⌬共␻兲 − i⌫                 ␻0 + ␻ − ˜       ˜ 共␻兲
                                                                                                                                 ⌬共␻兲 − i⌫
where sgn共␻兲 ⬅ 兩␻兩 / ␻ and                                                                                                                   共20兲

                              ˜⌫共␻兲 = d12兩␻兩 ,
                                       2    3
                                                                          Bialynicki-Birula and Sowiński, however, argue that “near
                                                                 共15兲     both resonances,”when ␻ ⬇ ⫾ ␻0,
                                      6i⑀0បc3
                                                                                                     2␻0
                       ˜ 共␻兲 = ⌬ 共− ␻兲 + ⌬ 共␻兲.
                       ⌬                                         共16兲                         ˜ 共␻兲 + i sgn共␻兲⌫
                                                                                                              ˜ 共␻兲兴
                                12        12                                   ␻20 − ␻2 − 2␻0关⌬
The notation follows that of Bialynicki-Birula and Sowiński                                     1                     1
关9兴 except that we use a tilde instead of a circumflex, the                      ⬇                        +                       .
                                                                                              ˜       ˜             ˜       ˜ 共␻兲
                                                                                     ␻0 − ␻ − ⌬共␻兲 − i⌫共␻兲 ␻0 + ␻ − ⌬共␻兲 + i⌫
latter used here to denote operators. Bialynicki-Birula and
Sowiński employ a renormalization such that a mass m0                                                                                        共21兲
+ ␦m = m, which corresponds to ␻0 / 2 in our notation, appears
in the unperturbed Hamiltonian while a term −␦m is added to               This expression follows when ␻ ⬎ 0 in the resonant part of
the interaction Hamiltonian, so that the effective free-atom              Eq. 共19兲 but ␻ ⬍ 0 in the nonresonant part; but it is clear
Hamiltonian is 共m − ␦m兲␺ˆ †␴ˆ z␺ˆ , where ␴ˆ z = 兩2典具2兩 − 兩1典具1兩, ␺ˆ is   from Eq. 共1兲 that this is an inappropriate juxtaposition of
the second-quantized fermion field describing the two-level               positive and negative frequencies in the expression for
atom, and ប ⬅ 1. In our model the free-atom Hamiltonian is                ␣1共␻兲: the argument of ␣1共␻兲 must be strictly positive or
1                                                                         strictly negative. Note also that in Eq. 共19兲 the effective fre-
2 ប␻0␴z. To compare our polarizability with that obtained by
       ˆ
Bialynicki-Birula and Sowiński, therefore, we must replace                quency shift ˜⌬共␻兲 is actually the sum of the two level shifts.
                                                                              Regarding this sum of level shifts, it is interesting to re-
2 ␻0 by m − ␦m, which is 2 ␻0 − ⌬12共␻0兲 in our notation. Mak-
1                        1

ing the substitution                                                      consider the calculations in Refs. 关6,8兴 when the approxima-
                                                                          tion ˆ␴z ⬇ −1 is made; this renders the two-level model effec-
                          ␻0 → ␻0 − 2⌬12共␻0兲                     共17兲     tively equivalent to a harmonic oscillator. In this
                                                                          approximation the equation of motion 共14兲 in Ref. 关8兴 yields
in Eq. 共14兲, we obtain                                                    the polarizability
                2␻0d12
                    2
                                                                                            2 ␻ 0d 2              1
   ␣ 1共 ␻ 兲 ⬇                                                                  ␣ 1共 ␻ 兲 =                                             ,
                  ប                                                                            ប ␻2 − ␻2 − 2␻ 关⌬
                                                                                                               ˜ 共␻兲 + i sgn共␻兲⌫
                                                                                                                               ˜ 共␻兲兴
                                                                                                         0          0
                                   1 − b̃                                                                                                    共22兲
                ⫻                                            ,
                                      ˜ 共␻兲 + i sgn共␻兲⌫
                  ␻ − ␻ − 2␻ 共1 − b̃兲关⌬
                   2   2                              ˜ 共␻兲兴
                   0               0                                      the same as that implied by the left-hand side of Eq. 共21兲.
                                                                 共18兲     That is, if the two-level atom is approximated by a harmonic
                                                                          oscillator, we obtain the second-order polarizability of
where b̃ = 2⌬12共␻0兲 / ␻0. Expressing this result in the notation          Bialynicki-Birula and Sowiński. The difference in the radia-
of Bialynicki-Birula and Sowiński, we see that it corresponds             tive level shifts appearing in Eq. 共10兲 is traceable in Refs.
exactly to their fourth-order polarizability. 关See Eq. 共114兲 of           关6,8兴 to the operator identity ˆ␴z ˆ␴† = + ˆ␴†, which is violated
Ref. 关9兴.兴                                                                when ˆ␴z is set to −1.

                                                                    043835-3
MILONNI et al.                                                                                                            PHYSICAL REVIEW A 77, 043835 共2008兲

    We can summarize our view of the situation as follows.
The expression 共10兲 for the linear polarizability of a two-
level atom satisfies the crossing relation and the optical theo-
                                                                                                 a fi共t兲 =
                                                                                                              −i
                                                                                                              ˜ 共␻兲
                                                                                                             2⌫
                                                                                                                          冉
                                                                                                                    j ki j k f
                                                                                                                                     1
                                                                                                                                              +
                                                                                                                                                    1
                                                                                                                                         ˜ 共␻兲 ␻ + ␻ − i⌫
                                                                                                                               ␻0 − ␻ − i⌫      0
                                                                                                                                                        ˜ 共␻兲 冊
                                                                                                                                                              ,

rem. It was obtained by a calculation consistent to second                                                                                                    共26兲
order in the atom-field coupling, as exemplified in the calcu-
lation in the following section. If we approximate it by a sum                              which follows the same-sign prescription. We have used the
of resonant and nonresonant terms 关Eq. 共13兲兴, the crossing                                  approximations 共24兲 and ignored radiative shifts in order to
relation is still satisfied, the radiative frequency shift appears,                         verify as simply as possible the conclusion of Bialynicki-
as expected, as the difference of the two radiative level                                   Birula and Sowiński that this prescription is appropriate for
shifts, and the expression is consistent with the opposite-sign                             the scattering amplitude. They obtain, in our notation, a scat-
prescription. The optical theorem, however, is violated in this                             tering amplitude 关see Eqs. 共89兲 and 共92兲 of Ref. 关9兴兴
approximation. In a weak-coupling limit we can approximate                                                                 2␻0                    1
Eq. 共10兲 by the fourth-order result 共18兲 of Bialynicki-Birula                                           a fi ⬀                          ⬇
and Sowiński. This form satisfies the crossing relation but                                                      ␻20 − ␻2 − 2i␻0˜⌫共␻兲                 ˜ 共␻兲
                                                                                                                                            ␻0 − ␻ − i⌫
not the opposite-sign prescription, and moreover the radia-                                                                1
tive frequency shift that appears is the sum rather than the                                                     +                                            共27兲
                                                                                                                               ˜ 共␻兲
                                                                                                                     ␻0 + ␻ − i⌫
difference of the radiative level shifts. In other words, our
expression 共10兲 for the polarizability is consistent in a weak-                             when radiative shifts are ignored.
coupling limit with that of Bialynicki-Birula and Sowiński,                                     For ␻ ⬎ 0, as assumed implicitly in scattering theory 关15兴,
but if we replace Eq. 共10兲 by that limiting form we forfeit
                                                                                            the polarizability 共18兲 with b̃ ⬇ 0 and the scattering ampli-
two of its most desirable properties. On the other hand, Eq.
                                                                                            tude 共27兲 have exactly the same frequency dependence to
共10兲 is to be taken as the correct expression to order ˜⌫共␻兲 / ␻0                           lowest order in the atom-field coupling. In other words, these
共assuming ␻ ⬎ 0兲; as a consequence, neither the same nor                                    expressions, like Eq. 共10兲, are consistent with the optical
opposite sign prescription is strictly valid in describing the                              theorem as expressed either in terms of the polarizability or
two-level polarizability.                                                                   the scattering amplitude. The optical theorem, though an ex-
                                                                                            act consequence of unitarity, cannot, of course, be expected
                                                                                            to be satisfied exactly when approximate formulas are de-
                         B. Scattering amplitude                                            rived for polarizabilities or scattering amplitudes.
    Consider now the scattering amplitude for the process                                       Mukamel 关16兴 has presented formal arguments supporting
兩i典 → 兩f典 in which for both the initial state 兩i典 and the final                             the same-sign prescription for the scattering amplitude and
state 兩f典 the two-level atom is in its lower state and there is a                           the opposite-sign prescription for the linear response 共polar-
single photon in the field. The second-order scattering am-                                 izability兲. We note, however, that in his Green-function for-
plitude may be written as                                                                   malism the linewidth ˜⌫共␻兲 in our Eq. 共26兲, for example, is

                                 冕 冕
                                   t           t1                                           replaced by the usual 共frequency-independent兲 ⑀ 共→0+兲 that
                         1
           a fi共t兲 = −                 dt1          dt2具f兩Ĥ⬘共t1兲Ĥ⬘共t2兲兩i典,        共23兲    ensures advanced and retarded Green functions. As such his
                         ប2        0          0                                             conclusions follow ipso facto from the assumption that the
                                                                                            scattering amplitude is determined by a retarded Green func-
where Ĥ⬘共t兲 is the interaction Hamiltonian 共4兲 in the Heisen-                              tion while the linear response is determined by the sum of
berg picture and the atom and field operators are assumed to                                advanced and retarded Green functions. In this connection it
evolve approximately according to their free evolution ex-                                  should be noted that the different signs of the ⑀’s in the
cept that the raising and lowering operators for the atom are                               nonresonant parts of the scattering amplitude and the polar-
damped at the rate ˜⌫共␻兲:                                                                   izability may already be found in the treatise of Berestetskii
                                                                           ˜                et al. 关17兴. They point out explicitly that “the expression for
     âk共t兲 ⬇ âk共0兲e−i␻kt                 and       ˆ␴共t兲 ⬇ ˆ␴共0兲e−i␻0te−⌫共␻兲t .           the 关scattering amplitude兴 differs from 关the expression for the
                                                                                    共24兲    polarizability兴 by a change in the sign of the imaginary part
                                                                                            in the denominator of the 关nonresonant兴 term.”
We ignore the radiative frequency shift here in order to focus                                  The use of same sign and opposite sign prescriptions
on the damping. It follows from Eq. 共23兲 that                                               seems to serve little or no purpose when nonresonant contri-

                         冕 冕
                         t             t1                                                   butions to the polarizability and scattering amplitude are in-
                                                             ˜                 ˜
  a fi共t兲 = − jki jk f       dt1            dt2关e−i关␻−␻0−i⌫共␻兲兴t1ei关␻−␻0+i⌫共␻兲兴t2           cluded. For positive ␻, the expressions for the two-level po-
                         0             0                                                    larizability and scattering amplitude have identical structure
                             ˜                         ˜                                    to second order in the coupling,
            + ei关␻+␻0+i⌫共␻兲兴t1e−i关␻+␻0−i⌫共␻兲兴t2兴,                                   共25兲
                                                                                                                                 2␻0
 where ki and k f refer, respectively, to the initial and final                                                                                               共28兲
 photons, which are assumed to have the same frequency ␻.                                                                ␻20 − ␻2 − 2i␻0˜⌫共␻兲
 Evaluating the integrals, and ignoring terms associated with                               共neglecting radiative shifts兲 so it is not possible for one to be
 an unphysical switching on of the interaction, we obtain, for                              described by the same sign and the other by the opposite
˜⌫共␻兲t Ⰷ 1,                                                                                 sign. The actual order of the calculation is somewhat confus-

                                                                                      043835-4
LINEAR POLARIZABILITIES OF TWO- AND THREE- …                                                                        PHYSICAL REVIEW A 77, 043835 共2008兲

ing since width and shift parameters appear both in reso-                                  兩3典具3兩 = ˆ␲† ˆ␲ ,        兩2典具2兩 = ˆ␲ ˆ␲† = ˆ␳† ˆ␳ ,         兩1典具1兩 = ˆ␳ ˆ␳† ,
nance 共and antiresonance兲 denominators, as well as in cor-
                                                                                                                                                                       共33兲
rections to these terms. For example, in Eqs. 共19兲 and 共27兲,
correction terms of order ˜⌫共␻兲 / ␻0 are neglected, but these                         and their nonvanishing commutators are
can be of the same order as the contribution from the ˜⌫共␻兲
term in the antiresonance denominators in those equations. In                                 关 ˆ␲, ˆ␲†兴 = 兩2典具2兩 − 兩3典具3兩,       关 ˆ␳, ˆ␳†兴 = 兩1典具1兩 − 兩2典具2兩, 共34兲
other words,
           2␻0
␻20 − ␻2 − 2i␻0˜⌫共␻兲
                              ⬇   冋         1
                                                ˜ 共␻兲
                                      ␻0 − ␻ − i⌫
                                                          +
                                                                      1
                                                                        ˜ 共␻兲
                                                              ␻0 + ␻ − i⌫
                                                                                册                       关 ˆ␲, ˆ␳兴 = − 兩1典具3兩,     关 ˆ␲†, ␳ˆ †兴 = 兩3典具1兩.

                                                                                      Since the calculation here will employ the Green-function

                                      冉             冊
                                            ˜ 共␻兲                                     approach of Ref. 关7兴, we adopt the notation used there for the
                                           i⌫                                         projection operators. The result obtained for the polarizabil-
                                  ⫻ 1−                                     共29兲
                                             ␻0                                       ity by this method may be shown to be the same as that
                                                                ˜
                                                                                      obtained in the Heisenberg picture following the methods of
and there is no justification for dropping the i⌫␻共␻0 兲 term since                    Refs. 关6,8兴.
it can lead to corrections in the denominators of order ˜⌫共␻兲.                           The three bare atomic levels are perturbed by the interac-
Instead of using same or opposite sign expressions, one is                            tion Ĥ⬘ to form linear combinations given by second-order
better off using the “exact” expression 共28兲 for the polariz-                         perturbation theory 关18兴. The calculations that follow use
ability or scattering amplitude.                                                      only expectation values for the form of state 兩2典 as dressed
                                                                                      by the vacuum field, denoted by 兩2⬘典 and given by


                                                                                                再 冕冋                                                           册冎
             III. THREE-LEVEL POLARIZABILITY
    Consider now a three-level atom with ground state 兩1典,                                             1                gk2            jk2
                                                                                       兩2⬘典 = 1 −              dk              +                                    兩2,0典
lower and upper excited states 兩2典 and 兩3典, and energies                                                            共␻32 + ␻k兲2 兩␻21 − ␻k + i⑀⬘兩2

                                                                                                 冕 再                                                               冎
                                                                                                       2
ប␻1 = 0, ប␻2, and ប␻3. It is assumed that transitions are al-
                                                                                                                   gk                   jk
lowed from the lower excited state 兩2典 to both the upper                                        +i     dk                兩3,1k典 −                兩1,1k典 ,
excited state 兩3典 and to the ground state 兩1典, with coupling                                                    ␻32 + ␻k          ␻21 − ␻k + i⑀⬘
coefficients gk and jk, respectively, for the photon of wave                                                                                                           共35兲
vector k. There are no allowed direct transitions between
states 兩1典 and 兩3典. This configuration of energy levels pro-                          where ␻ij = ␻i − ␻ j so that ␻2 = ␻21 and ␻3 = ␻31. The bare
vides radiative damping for the two excited states via the                            states are indicated by the unperturbed state labels 1, 2, and 3
decay routes 兩3典 → 兩2典 and 兩2典 → 兩1典. The derived expression                          for the atom and 0 and 1k for the field. The infinitesimal ⑀⬘
for the polarizability will thus include widths and shifts for                        represents the decay of field modes in a notional cavity and
both excited states.                                                                  the photon frequency is written ␻k − i⑀⬘ in terms that would
    The Hamiltonian of the interacting atom-photon system is                          otherwise diverge at ␻21 = ␻k. The integral in the first term of
Ĥ = Ĥ0 + Ĥ⬘, where                                                                 Eq. 共35兲 results from normalization of the perturbed wave

                                                 冕
                                                                                      function. Other, noncontributing, terms of second order in
                                                                                      the radiative couplings are omitted. Expectation values with
            Ĥ0 = ប␻2 ˆ␲ ˆ␲† + ប␻3 ˆ␲† ˆ␲ +             dkប␻kâk† âk ,
                                                                                      respect to state 兩2⬘典 are indicated by angle brackets and given
                                                                                      by

          Ĥ⬘ = iប   冕   dk共âk − âk† 兲兵gk共 ˆ␲† + ˆ␲兲 + jk共 ˆ␳† + ˆ␳兲其.   共30兲
                                                                                           具关 ˆ␲, ˆ␲†兴典 = 1 −   冕 再 dk
                                                                                                                             2gk2
                                                                                                                                     +
                                                                                                                                             jk2
                                                                                                                                                        ,           冎
                                                                                                                          共␻32 + ␻k兲2 兩␻21 − ␻k + i⑀⬘兩2
The coupling coefficients are defined by
                                                                                                                                                                       共36兲
                         បgk =   冉
                                ប␻k 1/2
                               16␲3⑀0
                                            冊
                                        ek · d23 ,
                                                                                                                    具âk ˆ␲†典 = 具âk␳ˆ 典 = 0,                          共37兲

                         បjk =   冉          冊
                                      ប␻k 1/2
                                     16␲3⑀0
                                              ek · d12 ,                   共31兲
                                                                                            具âk† ˆ␲†典 = − i
                                                                                                                  gk
                                                                                                               ␻32 + ␻k
                                                                                                                            and     具âk† ˆ␳典 = i
                                                                                                                                                          jk
                                                                                                                                                    ␻21 − ␻k − i⑀⬘
                                                                                                                                                                   ,
where d23 and d12 are the dipole moments of the two allowed
                                                                                                                                                                       共38兲
transitions, assumed real 关13兴. The projection operators in
Eq. 共30兲 are defined by                                                               all correct to second order in gk and jk.
                          ˆ␲ = 兩2典具3兩,     ˆ␲† = 兩3典具2兩,
                                                                                                                A. Green function method
                           ␳ˆ = 兩1典具2兩,    ␳ˆ † = 兩2典具1兩,                  共32兲
                                                                                           The linear polarizability of the three-level system is given
so that                                                                               by

                                                                                043835-5
MILONNI et al.                                                                                         PHYSICAL REVIEW A 77, 043835 共2008兲


 ␣1共␻兲 = − lim G␻+i⑀„d23共 ˆ␲ + ˆ␲†兲 + d12共 ˆ␳ + ˆ␳†兲,d23共 ˆ␲ + ˆ␲†兲         give a closed set of equations that can be solved for the
            ⑀→0+                                                            Green functions that appear in Eq. 共42兲.
          + d12共 ˆ␳ + ˆ␳†兲….                                        共39兲
                                                                                       B. Approximate solutions for Green functions
The addition of a positive infinitesimal imaginary part to ␻
ensures that the Green function is retarded, with its poles in                   It follows from Eqs. 共30兲, 共32兲, and 共34兲 that
the negative-imaginary part of the complex plane, as is re-
quired by considerations of causality 关19兴. The Green func-
tion for general operators Â and B̂ is defined by
                                                                                  关 ˆ␲,Ĥ兴 = ប␻32 ˆ␲ + iប   冕   dk共âk − âk† 兲兵gk关 ˆ␲, ˆ␲†兴 − jk ˆ␳ ˆ␲其.

                                                                                                                                                          共45兲
                               exp共− Er/kBT兲 − exp共− Es/kBT兲
       G␻+i⑀共Â,B̂兲 = 兺                                                     The equation of motion from Eq. 共44兲 is therefore

                                                                                                                                 冕
                        r,s          Tr兵exp共− Ĥ/kBT兲其

                           具r兩Â兩s典具s兩B̂兩r典                                        ប共␻ − ␻32兲G共 ˆ␲, ˆ␲†兲 = 具关 ˆ␲, ˆ␲†兴典 + iប         dkG兵共âk − âk† 兲
                       ⫻                     ,                      共40兲
                         ប共␻ + i⑀兲 + Er − Es
                                                                                                                ⫻共gk关␲
                                                                                                                     ˆ ,␲
                                                                                                                        ˆ †兴 − jk␳ˆ ␲
                                                                                                                                    ˆ 兲, ␲
                                                                                                                                         ˆ †其.            共46兲
where 兩r典, 兩s典 and Er, Es are the exact eigenstates and eigen-
                                                                            This is the first equation in the hierarchy and it brings in new
values, respectively, of the system Hamiltonian Ĥ. The com-                Green functions.
posite dipole operator that appears in the Green function of                   It is convenient to separate the new Green functions into
Eq. 共39兲, here denoted D̂, is Hermitian and it is not difficult             the four parts obtained from the product of factors in its first
to show from the definition in Eq. 共40兲 that                                argument. The commutators needed for the new equations of
                                                                            motion are
        G␻+i⑀共D̂,D̂兲 = 兵G−␻+i⑀共D̂,D̂兲其ⴱ = G−␻−i⑀共D̂,D̂兲.            共41兲
The polarizability therefore satisfies the crossing relation 共2兲
and it follows that ␣1共0兲 must be real. Evaluations are usu-
                                                                             †âk关 ˆ␲, ˆ␲†兴,Ĥ‡ = ប␻kâk关 ˆ␲, ˆ␲†兴 + iប     冕 ⬘dk 兵gk⬘关âk共âk⬘ − âk⬘兲
                                                                                                                                                          †



ally made for positive or zero ␻ and the frequencies that                                                        †
                                                                                                   + 共âk⬘ − âk⬘兲âk兴共 ˆ␲ − ˆ␲†兲
appear in the Hamiltonian 共30兲 are strictly positive.                                                                 †                   †
   The Green function in Eq. 共39兲 contains contributions in                                        + jk⬘关âk共âk⬘ − âk⬘兲␳ˆ † − 共âk⬘ − âk⬘兲âk␳ˆ 兴其
the pairs of operators that refer to the two transitions sepa-
rately and also interference terms that involve the operators                                   → ប␻kâk关 ˆ␲, ˆ␲†兴 − iបgk共 ˆ␲ − ˆ␲†兲 − iបjk ˆ␳† ,
of both transitions. The contribution to the polarizability                                                                                               共47兲
from the transition between states 兩2典 and 兩3典 alone is
                                                                            where the final expression results from the replacement of
       ␣2共␻兲 = − d23
                  2
                     lim 兵G␻+i⑀共 ˆ␲, ˆ␲†兲 + G␻+i⑀共 ˆ␲†, ˆ␲†兲                the photon operator products by their vacuum expectation
                        ⑀→0+                                                values, with the use of Eq. 共7兲 and 具âk† âk典 = 0. Similarly
                 + G␻+i⑀共 ˆ␲†, ˆ␲兲 + G␻+i⑀共 ˆ␲, ˆ␲兲其,               共42兲         †âk† 关␲
                                                                                        ˆ ,␲
                                                                                           ˆ †兴,H‡ → − ប␻kâk† 关␲
                                                                                                                ˆ ,␲
                                                                                                                   ˆ †兴 + iបgk共␲
                                                                                                                               ˆ −␲
                                                                                                                                  ˆ †兲 − iបjk␳ˆ ,
and we restrict our attention to this partial polarizability. The                                                                                         共48兲
individual Green functions are related by

        G␻+i⑀共 ˆ␲†, ˆ␲兲 = 兵G−␻+i⑀共 ˆ␲, ˆ␲†兲其ⴱ = G−␻−i⑀共 ˆ␲, ˆ␲†兲              关âk ˆ␳ ˆ␲,Ĥ兴 = ប共␻3 + ␻k兲âk␳ˆ ˆ␲ + iប     冕 ⬘                        †
                                                                                                                              dk 兵âk ˆ␳ ˆ␲共âk⬘ − âk⬘兲
                          and
                                                                                              ⫻关gk⬘共 ˆ␲† + ˆ␲兲 + jk⬘共 ˆ␳† + ˆ␳兲兴
                          G␻+i⑀共 ˆ␲, ˆ␲兲 = 兵G−␻+i⑀共 ˆ␲†, ˆ␲†兲其ⴱ ,   共43兲
                                                                                                           †
                                                                                              − 共âk⬘ − âk⬘兲关gk⬘共 ˆ␲† + ˆ␲兲 + jk⬘共 ˆ␳† + ˆ␳兲兴âk ˆ␳ ˆ␲其
again readily derived from the definition in Eq. 共40兲. It is
therefore necessary to calculate only the first two Green                                   → ប共␻3 + ␻k兲âk ˆ␳ ˆ␲ − iបgk ˆ␳ ,                             共49兲
functions in Eq. 共42兲.
                                                                            and
   The calculation proceeds via the Green-function equation
of motion for general operators Â and B̂ in the form 关20,21兴                              关âk† ˆ␳ ˆ␲,Ĥ兴 → ប共␻3 − ␻k兲âk† ˆ␳ ˆ␲ − iបjk ˆ␲ .             共50兲

              ប␻G共Â,B̂兲 = 具关Â,B̂兴典 + G共关Â,Ĥ兴,B̂兲,               共44兲    The corresponding equations of motion 共44兲 are

where ␻ is shorthand for ␻ + i⑀ and this subscript on G is                  共␻ − ␻k兲G共âk关 ˆ␲, ˆ␲†兴, ˆ␲†兲 = − igkG共 ˆ␲ − ˆ␲†, ˆ␲†兲 − ijkG共␳ˆ †, ˆ␲†兲,
understood. Where appropriate, we use the technique of trun-                                                                                              共51兲
cation of the hierarchy of equations for the Green functions
generated by successive applications of Eq. 共44兲. The calcu-                ប共␻ + ␻k兲G共âk† 关␲
                                                                                             ˆ ,␲
                                                                                                ˆ †兴, ␲
                                                                                                      ˆ †兲 = − 2具âk† ␲
                                                                                                                      ˆ †典 + iបgkG共␲
                                                                                                                                   ˆ −␲
                                                                                                                                      ˆ †, ␲
                                                                                                                                           ˆ †兲
lations for the three-level system are approximated by ne-
glect of terms of order higher than the second in gk and jk to                                                       − iបjkG共 ˆ␳, ˆ␲†兲,                   共52兲

                                                                      043835-6
LINEAR POLARIZABILITIES OF TWO- AND THREE- …                                                                       PHYSICAL REVIEW A 77, 043835 共2008兲




and
               共␻ − ␻31 − ␻k兲G共âk ˆ␳ ˆ␲, ˆ␲†兲 = − igkG共 ˆ␳, ˆ␲†兲,           共53兲
                                                                                                          J共␻31 ⫾ ␻兲 =      冕    dk
                                                                                                                                            jk2
                                                                                                                                      ␻31 − ␻k ⫾ ␻
                                                                                                                                                   ,                  共61兲


       ប共␻ − ␻31 + ␻k兲G共âk† ˆ␳ ˆ␲, ˆ␲†兲 = 具âk† ˆ␳典 − iបjkG共␲, ˆ␲†兲,
                                                                                     where ␻ is shorthand for ␻ + i⑀ throughout. Elimination of all
                                                                             共54兲    except the required Green functions from the equations listed
where expectation values that could appear on the right-hand                         above then produces the pair of equations
sides of Eqs. 共51兲 and 共53兲 are omitted in accordance with
Eq. 共37兲. These four equations form the second level of the
hierarchy and they again bring in new Green functions.                               − ប兵␻32 − ␻ − I共␻兲 − J共␻31 − ␻兲其G共 ˆ␲, ˆ␲†兲 − បI共␻兲G共 ˆ␲†, ˆ␲†兲

                                                                                                                冕 再                                           冎
    Evaluation of the Green functions G共 ˆ␳† , ˆ␲†兲 in Eq. 共51兲
and G共 ˆ␳ , ˆ␲†兲 in Eqs. 共52兲 and 共53兲 produces expressions of                                                          2gk具âk† ˆ␲†典     jk具âk† ˆ␳典
                                                                                           = 具关 ˆ␲, ˆ␲†兴典 + i     dk                  −               ,               共62兲
the first order in the coupling coefficients gk and jk. These                                                            ␻k + ␻         ␻31 − ␻k − ␻
two Green functions can therefore be neglected in accor-
dance with the restriction of the polarizability to terms of
second order in the coupling. The new Green function
G共 ˆ␲† , ˆ␲†兲 on the right-hand sides of Eqs. 共51兲 and 共52兲 is the                   − បI共␻兲G共 ˆ␲, ˆ␲†兲 + ប兵␻32 + ␻ + I共␻兲 − J共␻31 + ␻兲其G共 ˆ␲†, ˆ␲†兲
second in the basic expression 共42兲 for the polarizability. Its
equation of motion is                                                                      =−i   冕   dk
                                                                                                          2gk具âk† ˆ␲†典
                                                                                                           ␻k + ␻
                                                                                                                        .                                             共63兲

       共␻ + ␻32兲G共 ˆ␲†, ˆ␲†兲 = − i      冕   dkG兵共âk − âk† 兲共gk关 ˆ␲, ˆ␲†兴
                                                                                     The solutions of these simultaneous equations have the com-
                                      − jk␲ ␳ 兲, ␲ 其.
                                          ˆ †ˆ†   ˆ†                         共55兲    mon denominator

The Green function associated with the 关␲
                                        ˆ ,␲
                                           ˆ †兴 term has al-                                D = ប关␻32 − ␻ − I共␻兲 − J共␻31 − ␻兲兴关␻32 + ␻ + I共␻兲
ready been evaluated in Eqs. 共51兲 and 共52兲. The remaining                                         − J共␻31 + ␻兲兴 + ប关I共␻兲兴2
Green functions need the commutators
                                                                                                ⬇ ប兵␻32
                                                                                                     2
                                                                                                        − ␻2 − 2␻I共␻兲 − 共␻32 − ␻兲J共␻31 + ␻兲
关âk␲ ␳ ,Ĥ兴
      ˆ †ˆ†
                                                                                                  − 共␻32 + ␻兲J共␻31 − ␻兲其,                                             共64兲
                  = − ប共␻3 − ␻k兲âk ˆ␲† ˆ␳† + iប    冕 ⬘ dk 兵âk ˆ␲† ˆ␳†
                                                                                     which is seen to be invariant under reversal of the sign of ␻.
                                   †
                        ⫻共âk⬘ − âk⬘兲关gk⬘共␲
                                           ˆ†+␲
                                              ˆ 兲 + jk⬘共␳ˆ † + ␳ˆ 兲兴                 The numerators are obtained from
                                  †
                     − 共âk⬘ − âk⬘兲关gk⬘共 ˆ␲† + ˆ␲兲 + jk⬘共 ˆ␳† + ˆ␳兲兴âk ˆ␲† ˆ␳†其
                                                                                     G共 ˆ␲, ˆ␲†兲D = − 关␻32 + ␻ + I共␻兲 − J共␻31 + ␻兲兴具关 ˆ␲, ˆ␲†兴典

                                                                                                                            冕 再                                         冎
                  → − ប共␻3 − ␻k兲âk ˆ␲† ˆ␳† − iបjk ˆ␲†                       共56兲
and                                                                                                                               2gk具âk† ˆ␲†典     jk具âk† ␳ˆ 典
                                                                                                       − i共␻32 + ␻兲          dk                 −
                                                                                                                                   ␻k + ␻         ␻31 − ␻k − ␻
              关âk† ˆ␲† ˆ␳†,Ĥ兴 → − ប共␻3 + ␻k兲âk† ˆ␲† ˆ␳† − iបgk ˆ␳† .      共57兲
                                                                                                     ⬇ − 共␻32 + ␻兲具关 ˆ␲, ˆ␲†兴典 − I共␻兲 + J共␻31 + ␻兲

                                                                                                                        冕 再
The corresponding equations of motion are
                                                                                                                                         2gk2
                                                                                                       − 共␻32 + ␻兲          dk
           共␻ + ␻31 − ␻k兲G共âk␲
                              ˆ †␳ˆ †, ␲
                                       ˆ †兲 = − ijkG共␲
                                                     ˆ †, ␲
                                                          ˆ †兲               共58兲                                                 共␻k + ␻兲共␻32 + ␻k兲
and

          共␻ + ␻31 + ␻k兲G共âk† ˆ␲† ˆ␳†, ˆ␲†兲 = − igkG共 ˆ␳†, ˆ␲†兲.            共59兲
                                                                                                       +
                                                                                                                         jk2
                                                                                                           共␻31 − ␻k − ␻兲共␻21 − ␻k − i⑀⬘兲
                                                                                                                                                       冎              共65兲


The right-hand side of Eq. 共59兲 can be set equal to zero in
accordance with the remarks that precede Eq. 共55兲.                                   and

                                                                                                                                                   冕
   The Green functions that appear in Eqs. 共46兲, 共51兲–共55兲,
                                                                                                                                                            2gk具âk† ˆ␲†典
共58兲, and 共59兲 form a closed set and the functions needed for                         G共 ˆ␲†, ˆ␲†兲D = − I共␻兲具关 ˆ␲, ˆ␲†兴典 − i共␻32 − ␻兲                  dk
the polarizability 共42兲 can be determined by the solution of                                                                                                 ␻k + ␻
these simultaneous equations. It is convenient to define
                                                                                                                                       冕               2gk2

                       冕 冉                             冊
                                                                                                       ⬇ − I共␻兲 − 共␻32 − ␻兲                dk                      .
                                    1      1                                                                                                    共␻k + ␻兲共␻32 + ␻k兲
              I共␻兲 =      dkgk2         −       = − I共− ␻兲                   共60兲
                                  ␻k − ␻ ␻k + ␻                                                                                                                       共66兲
and

                                                                               043835-7
MILONNI et al.                                                                                     PHYSICAL REVIEW A 77, 043835 共2008兲

In each of these last three expressions, the second forms
show approximations correct to order gk2 and jk2 in the de-
nominator and numerators. It is easily shown with the use of
                                                                                冕   dk
                                                                                               jk2
                                                                                         ␻21 − ␻k ⫾ i⑀⬘
                                                                                                        → − ⌬12共− ␻21兲 ⫿ i⌫12共− ␻21兲.

Eq. 共60兲 that the Green function in Eq. 共66兲 is invariant under                                                                          共72兲
reversal of the sign of ␻, a general property of Green func-
tions with repeated arguments, Â = B̂. The remaining Green               The real parts are level shifts, given by principal-value inte-
functions are found by application of the relations in Eq.                grals, and the imaginary parts are level widths or damping
共43兲.                                                                     rates, with

                       C. Partial polarizability ␣2(␻)
   The partial polarizability given by Eq. 共42兲 is
                                                                                              ⌫23共⫾ ␻兲 = ␲   冕   dkgk2 ␦共␻k ⫾ ␻兲,        共73兲

                                            2 N
                                 ␣2共␻兲 = − d23                   共67兲
                                                                                                             冕
                                                 ,
                                               D
                                                                                     ⌫12共− ␻31 ⫾ ␻兲 = ␲          dkjk2 ␦共␻k − ␻31 ⫾ ␻兲   共74兲
where D is given by Eq. 共64兲 and
  N = − 2␻32具关 ˆ␲, ˆ␲†兴典 + J共␻31 + ␻兲 + J共␻31 − ␻兲

                                 再冉
                                                                          and

         − 4␻32    冕     dkgk2
                                         1       1
                                                         冊
                                                         1

                                                                                                             冕
                                              −
                                      ␻32 + ␻k ␻k + ␻ ␻ − ␻32

                                                 冎
                                                                                           ⌫12共− ␻21兲 = ␲        dkjk2 ␦共␻k − ␻21兲.
             冉                           冊
                                                                                                                                         共75兲
              1       1       1
         −         −
           ␻32 + ␻k ␻k − ␻ ␻ + ␻32

         −   冕   dkjk2   再冉         1
                                          −
                                                 1
                                                             冊
                                                          ␻ + ␻32
                              ␻31 − ␻k − ␻ ␻21 − ␻k − i⑀⬘ ␻ − ␻32
                                                                          The functions −⌬23共−␻兲 and ⌫23共−␻兲 are interpreted, respec-
                                                                          tively, as the level shift and damping of level 兩3典, while
                                                                          −⌬23共␻兲 and ⌫23共␻兲 are the shift and damping of level 兩2典

         +   冉         1
                             −
                                    1        ␻ − ␻32
                 ␻31 − ␻k + ␻ ␻21 − ␻k + i⑀⬘ ␻ + ␻32
                                                     冊
                                                     .       冎   共68兲
                                                                          arising from its coupling to level 兩3典, i.e., these quantities all
                                                                          result from the radiative coupling gk between states 兩3典 and
                                                                          兩2典. For positive ␻, ⌫23共␻兲 = 0 for all ␻, as expected on physi-
With ␻ replaced by ␻ + i⑀, and in the limit ⑀ → 0+, it is con-            cal grounds from the absence of spontaneous emission in the
venient to use the separation into real and imaginary parts,              upwards direction. While ⌫12共−␻31 − ␻兲 is nonzero for all ␻,
following notation introduced in Sec. II:                                 ⌫12共−␻31 + ␻兲 is nonzero only for ␻ ⬍ ␻31. The frequencies
                                                                          ␻31 ⫾ ␻, and therefore the damping rates ⌫12共−␻31 ⫿ ␻兲, ap-
                                                                          pear through frequency mixing of the applied field and a

             冕
                                                                          source field that oscillates at ␻31. The latter results from the
                          gk2
                 dk               → ⌬23共⫾ ␻兲 ⫿ i⌫23共⫾ ␻兲,        共69兲     possibility of transitions between the states 兩1典 and 兩3典 via the
                      ␻k ⫾ ␻ ⫾ i⑀                                         allowed 兩1典 ↔ 兩2典 and 兩2典 ↔ 兩3典 transitions.
                                                                              The partial polarizability 共67兲 is quite complicated when
                                                                          these expressions are substituted. It is instructive to consider
so that, from Eq. 共60兲,
                                                                          its form when all of the level shifts are neglected and only
                                                                          the damping terms are retained. The denominator is then

  lim I共␻ + i⑀兲 = ⌬23共− ␻兲 + i⌫23共− ␻兲 − ⌬23共␻兲 + i⌫23共␻兲
  ⑀→0+                                                                     D = ប关␻32 − ␻ − i␥23共␻兲 − i⌫12共− ␻31 + ␻兲兴关␻32 + ␻
                         = ␦23共␻兲 + i␥23共␻兲,                                    + i␥23共␻兲 + i⌫12共− ␻31 − ␻兲兴 + ប关I共␻兲兴2 ⬇ ប兵␻32
                                                                                                                             2
                                                                                                                                − ␻2
where                                                                           − 2i␻␥23共␻兲 + i共␻32 − ␻兲⌫12共− ␻31 − ␻兲
                         ␦23共␻兲 = ⌬23共− ␻兲 − ⌬23共␻兲,                            − i共␻32 + ␻兲⌫12共− ␻31 + ␻兲其                              共76兲

                         ␥23共␻兲 = ⌫23共− ␻兲 + ⌫23共␻兲.             共70兲     and the numerator is


                                                                                          再
   Similarly
                                                                                                 2i⌫23共− ␻兲 2i⌫23共␻兲 i⌫12共− ␻31 − ␻兲
     J共␻31 ⫾ ␻兲 =            冕              jk2                            N = − 2␻32 1 +
                                                                                                  ␻32 + ␻
                                                                                                           −
                                                                                                             ␻32 − ␻
                                                                                                                     +
                                                                                                                         ␻32 + ␻

                                                                                                                           冎
                                 dk
                                    ␻31 − ␻k ⫾ ␻ ⫾ i⑀
                                                                                    i⌫12共− ␻31 + ␻兲 2i␻⌫12共− ␻21兲
                         → − ⌬12共− ␻31 ⫿ ␻兲 ⫿ i⌫12共− ␻31 ⫿ ␻兲                   −                  +              .                      共77兲
                                                                                        ␻32 − ␻       ␻32
                                                                                                        2
                                                                                                          − ␻2
                                                                 共71兲
and, with ⑀⬘ → 0 ,       +                                                The polarizability from Eq. 共67兲 is therefore

                                                                    043835-8
LINEAR POLARIZABILITIES OF TWO- AND THREE- …                                                            PHYSICAL REVIEW A 77, 043835 共2008兲

                                                     2i⌫ 共−␻兲      2i⌫ 共␻兲   i⌫ 共−␻ −␻兲       i⌫ 共−␻ +␻兲    2i␻⌫ 共−␻ 兲
                         2d2 ␻32        1 + ␻3223+␻ − ␻3223−␻ + 12␻32+31␻ − 12␻32−31␻ + ␻212−␻2 21
                  ␣2共␻兲 = 23                                                              32
                                                                                                          .                                共78兲
                            ប ␻322
                                   − ␻2 − 2i␻␥23共␻兲 + i共␻32 − ␻兲⌫12共− ␻31 − ␻兲 − i共␻32 + ␻兲⌫12共− ␻31 + ␻兲




It is readily verified that this expression satisfies the crossing           cascade emission given in Eqs. 共C.44兲 and 共C.45兲 of 关22兴.
relation, and it shows the consequent property of a real value               The two terms in the first line of Eq. 共76兲 have the same
at ␻ = 0. The two terms in the product of square brackets on                 damping term or level width ␥23共␻兲 in respect of the 兩3典
the right in the first line of Eq. 共76兲 represent resonant and               → 兩2典 transition alone. The signs of these terms essentially
nonresonant contributions, respectively. Note the different                  follow the signs of ␻ in the two denominators. Equivalently,
structures of these terms with respect to the upper and lower                they have opposite signs relative to the transition frequency
transition functions. The latter results from the radiative cou-             ␻32, i.e., they follow the opposite-sign prescription.
pling jk between states 兩2典 and 兩1典 and makes only single                       However, any simple relation between the two terms is
contributions to the damping, as only state 兩2典 is affected by               destroyed by the contributions from the decay and shift pa-
spontaneous emission to state 兩1典. There is no simple relation               rameters appearing in the denominator of Eq. 共78兲 that are
between the ⌫12 magnitudes in the two terms, in contrast to                  associated with the 兩2典 → 兩1典 transition. In particular, the val-
the two upper-transition contributions contained in ␥23共␻兲.                  ues of the damping functions ⌫12共−␻31 − ␻兲 and
    The dominant feature in the polarizability is the resonance              ⌫12共−␻31 + ␻兲 are different except at ␻ = 0. As stated above,
of the first term in Eq. 共76兲 at ␻ = ␻32 and, for frequencies                ⌫12共−␻31 + ␻兲 is nonzero only for positive arguments while
close to resonance, it is usually a good approximation to                    ⌫12共−␻31 − ␻兲 is nonzero for all positive ␻. Both the simple
substitute ␻32 for ␻ in the expressions for the level widths                 forms of relation between the linewidths of the resonant and
that occur in the first term. Then                                           nonresonant terms, embodied in the opposite-sign and same-

                                冕
                                                                             sign rules, are therefore incorrect for transitions between
               ⌫23共− ␻32兲 = ␲       dkgk2 ␦共␻k − ␻32兲                        atomic excited states.
                                                                                If we bring the small terms in the numerator of Eq. 共78兲
                                                                             into the denominator in the manner of Eq. 共14兲, we obtain
and
                                                                                            2
                                                                                               ␻32
                                          冕
                                                                                          2d23
                                                                             ␣ 2共 ␻ 兲 ⬇
      ⌫12共− ␻31 + ␻兲 ⬇ ⌫12共− ␻21兲 = ␲         dkjk2 ␦共␻k − ␻21兲,                             ប
                                                                                                                    1
                                                                   共79兲                   ⫻                                              ,
                                                                                              ␻32
                                                                                               2                     ˜ 共␻兲 − 2i␻⌫ 共− ␻ 兲
                                                                                                  − ␻2 − 2i␻32 sgn共␻兲⌫ 23        12   21
in agreement with the usual expressions for the decay rates
of states 兩3典 and 兩2典.                                                                                                                     共81兲
                                                                             where we define, analogously to Eq. 共15兲,
                        IV. DISCUSSION
                                                                                                        ˜⌫ 共␻兲 = d23兩␻兩 .
                                                                                                                       2    3
   We note that the form 共78兲 of the polarizability when the                                              23                               共82兲
                                                                                                                6␲⑀0បc3
coupling jk of level 兩2典 to level 兩1典 is set equal to zero, given
by                                                                           We can use the simplification 共81兲 to verify that the optical
                                     2i⌫23共␻兲 2i⌫23共−␻兲                      theorem,
                          2
                        2d23 ␻32 1 − ␻32−␻ + ␻32+␻
           ␣ 2共 ␻ 兲 = −                                 ,          共80兲                                  ␻
                           ប ␻32  2
                                    − ␻2 − 2i␻␥23共␻兲                                       ␴ T共 ␻ 兲 =        Im ␣2共␻兲           共␻ ⬎ 0兲,   共83兲
                                                                                                        ⑀ 0c
agrees, apart from trivial changes in notation, with the two-
                                                                             is satisfied by the polarizability and the total cross section
level polarizability 共10兲 when radiative shifts are ignored.
                                                                             ␴T共␻兲 in our three-level model. We note first that, since we
   In our nonrelativistic approach without retardation or a
                                                                             have considered only the partial polarizability ␣2共␻兲, the
high-frequency cutoff, the radiative level shifts are divergent.
                                                                             兩2典 → 兩1典 transition in our model acts primarily as a decay
Nevertheless, whether they appear in a sum or a difference
                                                                             channel for level 兩2典. We have, from Eq. 共81兲,
helps to determine the plausibility of various expressions for
the polarizability, as discussed in Sec. II. In the three-level                                   ␻
                                                                                                      Im ␣2共␻兲 = ␴R共␻兲 + ␴A共␻兲,            共84兲
case the radiative level shifts of the states 兩2典 and 兩3典 appear,                                ⑀ 0c
as expected, as the difference ␦23共␻兲 determining a radiative
frequency shift.                                                             where
   For our purposes the radiative widths are of much greater
interest. Note that the widths of the upper and lower energy
levels in the transition add in the polarizability denominator,
                                                                                                  ␴ R共 ␻ 兲 =
                                                                                                                1
                                                                                                               6␲⑀20
                                                                                                                       冉冊
                                                                                                                       ␻ 4
                                                                                                                       c
                                                                                                                           兩␣2共␻兲兩2        共85兲

in agreement with the line shape of the 兩3典 → 兩2典 transition in              and

                                                                     043835-9
MILONNI et al.                                                                                          PHYSICAL REVIEW A 77, 043835 共2008兲


                ␻ 2d23
                    2
                       ␻32                                               Center Grant, and by the Michigan Center for Theoretical
  ␴ A共 ␻ 兲 =                                                             Physics. S.M.B. thanks the Royal Society and the Wolfson
               ⑀ 0c ប
                                                                         Foundation for financial support.
                                  2␻32⌫12共− ␻21兲
               ⫻                                               .
                   共␻32
                     2
                        − ␻2兲2 + 关2␻32˜⌫23共␻兲 + 2␻⌫12共− ␻21兲兴2                        APPENDIX: SCHRÖDINGER PICTURE

                                                              共86兲          Since we are working to first order in the applied field, it
                                                                         is practical to use the Schrödinger picture to obtain an ex-
If ␻ ⬇ ␻32                                                               pression for the polarizability. This will allow us to get the
                    ␻ d23
                       2
                                    ⌫12共− ␻21兲                           frequency dependence of the decay parameters in a rather
    ␴ A共 ␻ 兲 ⬇                                           .               simple manner. To illustrate the method, we carry out the
                   ⑀0c ប 共␻32 − ␻兲 + 关⌫
                                  2   ˜ 共␻兲 + ⌫ 共− ␻ 兲兴2
                                        23     12   21                   calculation in rotating wave approximation 共RWA兲 and ne-
                                                              共87兲       glect any level shifts. Both amplitude and density matrix
                                                                         approaches may be used. They lead to slightly different re-
It is possible to give a physical interpretation to these terms          sults that are, nevertheless, consistent within the limits of the
in the limit that ⌬ = ␻32 − ␻ Ⰷ ˜⌫23共␻兲, ⌫12共−␻21兲. To do so we          approximations. The results also agree with those of Sec. III,
first recall that light scattering from the ground state of an           in the appropriate limits.
atom is Rayleigh scattering, to lowest order in the incident                To proceed, we adopt a slightly different form for the
light intensity. That is, the scattering is elastic, with the fre-       Hamiltonian of our three-level system. Taking a classical,
quency of the scattered radiation equal to that of the incident          linearly polarized monochromatic field E共t兲 = E0d̂23 cos共␻t兲
field. The elastic nature of the scattering can be understood            to drive the 2–3 transition and setting the energy of level 2
in terms of a two-photon process in which a photon is scat-              equal to zero, we write the RWA Hamiltonian as
tered from the incident field into a previously unoccupied
vacuum field mode having the same frequency but a different
direction. Since the initial and final states of the atomic tran-
                                                                               Ĥ = − ប␻21兩1典具1兩 + ប␻32兩3典具3兩 +         冕    dkប␻kâk† âk
sition have zero width 共the transition is from the ground state
back to the ground state兲, the scattering is necessarily elastic.
On the other hand, when one scatters from an excited state,
                                                                                   + iប   冕   dk关gk共兩3典具2兩âk − 兩2典具3兩âk† 兲 + jk共兩2典具1兩âk − 兩1典
the initial and final state width is that of the excited state. In
                                                                                                    d23E0 i␻t
this limit, one can show that radiation scattered by the atoms                     ⫻具2兩âk† 兲兴 −         共e 兩2典具3兩 + 兩3典具2兩e−i␻t兲,            共A1兲
consists of two components, a component having width                                                  2
2⌫12共−␻21兲 centered at the field frequency ␻ and a compo-                where gk and jk are given in Eq. 共31兲.
nent having width 关⌫  ˜ 共␻兲 + ⌫ 共−␻ 兲兴 centered at the tran-                The state vector of the system is written in an interaction
                        23        12   21
sition frequency ␻32.                                                    representation as
    The radiation centered at the field frequency can be
viewed as the analog of Rayleigh scattering. On integrating                        兩␺共t兲典 = b20共t兲兩20典 + b30共t兲e−i␻t兩30典
over all scattered frequencies centered at ␻, one obtains the
cross section ␴R共␻兲 关Eq. 共85兲兴 corresponding to Rayleigh
scattering off an electric dipole scatterer having polarizabil-
                                                                                                +   冕   dk关b2k共t兲e−i␻t兩2,1k典 + b1k兩1,1k典兴,    共A2兲

ity ␣2共␻兲, although in this case the scattering, while centered          which are the only states needed to first order in the external
at ␻, is not totally elastic. On integrating the component               field. The first label in each state amplitude refers to the
centered at the transition frequency ␻32 over all scattered              atomic state and the second to the state of the field. We can
frequencies, one obtains the cross section ␴A共␻兲 关Eq. 共87兲兴              express the complex polarizability as
corresponding to absorption on the 2–3 transition. The ab-
sorption component occurs only if ⌫12共−␻21兲 ⫽ 0. In the limit
                                                                                                                  2 +
                                                                                                                 d23 ␳32
                                                                                                            ␣=           ,                    共A3兲
that ⌫12共−␻21兲 Ⰶ ˜⌫23共␻兲, the Rayleigh scattering is dominant.                                                   ប␹␳22
Thus the optical theorem is satisfied with a total optical cross         where ␳32
                                                                                 +
                                                                                   = ␳30,20ei␻t is a density matrix element in an inter-
section attributable to both Rayleigh scattering and absorp-             action representation and ␹ = d23E0 / 2ប. We must divide ␳32 +
tion, a result that is quite general when one considers scat-            by the steady-state population of level 2 to get a meaningful
tering from an excited state.                                            expression for the polarizability.

                        ACKNOWLEDGMENTS                                                             1. Amplitude approach
   We thank Professor G. W. Ford and Professor R. W. Boyd                   Since we use an amplitude approach and want a steady-
for helpful discussions and Professor I. Bialynicki-Birula and           state result, we use the trick of starting with the atom in state
Professor S. Mukamel for providing us with preprints of                  2 at t = t0, and eventually form density matrix elements which
their papers before they were submitted for publication. This            will depend on both t and t0. At that point, we assume a
research was supported in part by the National Science Foun-             共constant兲 pumping rate ⌳共t0兲 = ⌳ and integrate the results
dation through Grant No. PHY0244841 and the FOCUS                        from −⬁ to t. The equations for the amplitudes follow im-

                                                                   043835-10
LINEAR POLARIZABILITIES OF TWO- AND THREE- …                                                                       PHYSICAL REVIEW A 77, 043835 共2008兲

mediately from Schrödinger’s using the Hamiltonian 共A1兲 as                                                     2 +
                                                                                                              d23 ␳32           2
                                                                                                                              d23
                                                                                                         ␣=           =                                        共A11兲
                ḃ3 = − i共␻32 − ␻兲b3 + i␹b2 +                冕   dkgkb2k ,       共A4a兲
                                                                                                              ប␹␳22 ប关共␻32 − ␻兲 − i共␥3 + ␥2兲兴
                                                                                         and agrees with Eq. 共81兲 in RWA with the neglect of level
                                                                                         shifts.

                                     ḃ2 =   冕   dkjkb1k ,                       共A4b兲                         2. Density matrix approach
                                                                                               The appropriate density matrix equations are

                          ḃ1k = − i共␻k − ␻21兲b1k⬘ − jkb2 ,                      共A4c兲
                                                                                           ˙␳32
                                                                                             +
                                                                                                = i␹␳22 − i共␻32 − ␻兲␳32
                                                                                                                     +
                                                                                                                        +         冕   dkjk␳3,1k
                                                                                                                                           +
                                                                                                                                                +   冕   dkgk␳2k,2
                                                                                                                                                             +
                                                                                                                                                                  ,

                           ḃ2k = − i共␻k − ␻兲b2k − gkb3 ,                        共A4d兲                                                                         共A12a兲
where ␻k = kc and we have suppressed the “0”in labeling
amplitudes b3,0 and b2,0. By solving Eqs. 共A4c兲 and 共A4d兲                                       ˙␳3,1k
                                                                                                  +
                                                                                                       ⬇ 关− ⑀ + i共␻k + ␻ − ␻31兲兴␳3,1k
                                                                                                                                 +
                                                                                                                                      − jk␳32
                                                                                                                                           +
                                                                                                                                              + i␹␳2,1k
                                                                                                                                                   +
                                                                                                                                                        ,
for b1k and b2k and substituting the solutions into Eqs. 共A4a兲                                                                                               共A12b兲
and 共A4b兲 using

                    冕      dkgk2 e−i共␻k−␻兲共t−t⬘兲 = ⌫23共− ␻兲,
                                                                                                         ˙␳2,1k ⬇ 关i共␻k − ␻21兲 − ⑀⬘兴␳2,1k − jk␳22 ,

                                                                                                         ˙␳2k,2
                                                                                                           +
                                                                                                                ⬇ 关− i共␻k − ␻兲 − ⑀⬙兴␳2k,2
                                                                                                                                     +
                                                                                                                                          − gk␳32
                                                                                                                                               +
                                                                                                                                                  ,
                                                                                                                                                               共A12c兲

                                                                                                                                                             共A12d兲

                    冕       dkjk2 e−i共␻k−␻兲共t−t⬘兲 = ⌫12共− ␻兲                      共A5兲
                                                                                                            ˙␳22 = ⌳ +   冕   dkjk共␳1k,2 + ␳2,1k兲,              共A12e兲
关consistent with Eqs. 共69兲 and 共72兲, neglecting radiative
shifts兴, one finds                                                                       where
                                                                                                                             + −i␻t
                                                                                                                      ␳32 = ␳32 e ,                            共A13a兲
                  ḃ3 = − i共␻32 − ␻兲b3,0 + i␹b2 − ␥3b3 ,                         共A6a兲
                                                                                                                    ␳3,1k = ␳3,1k
                                                                                                                             +
                                                                                                                                  e−i␻t ,                    共A13b兲
                                        ḃ2 = − ␥2b2 ,                           共A6b兲
where                                                                                                               ␳2k,2 = ␳2k,2
                                                                                                                             +
                                                                                                                                  e−i␻t ,                      共A13c兲
                  ␥3 = ⌫23共− ␻兲;                   ␥2 = ⌫12共− ␻21兲.               共A7兲   and decay rates ⑀, ⑀⬘, and ⑀⬙ have been inserted into Eqs.
                                                                                         共A12b兲–共A12d兲 to account for the fact that ␳3,1k    +
                                                                                                                                                 , ␳2,1k, and
The solutions then follow immediately                                                    ␳2k,2 decay to states involving additional photons in the field
                                                                                           +

                                    b2共t,t0兲 = e−␥2共t−t0兲 ,                      共A8a兲   not contained in the basis states 共A2兲. The steady state solu-
                                                                                         tion of Eq. 共A12c兲, ␳2,1k = jk␳22 / 关i共␻k − ␻21兲 − ⑀兴, and its com-

                  冕   t                                                                  plex conjugate can be substituted into Eq. 共A12e兲, and Eq.
 b3共t,t0兲 = i␹            b2共t⬘兲e−关␥3+i共␻32−␻兲兴共t−t⬘兲dt⬘                                 共72兲 used to obtain the steady-state solution ␳22 = ⌳ / 共2␥2兲, in
                    t0                                                                   agreement with Eq. 共A9兲.
                         i␹                                                                  To obtain ␳32
                                                                                                         +
                                                                                                           , one solves Eqs. 共A12b兲 and 共A12d兲 in
            =                        关e−␥2共t−t0兲 − e−关␥3+i共␻32−␻兲兴共t−t0兲兴                steady state and substitutes the results in Eq. 共A12a兲 to ob-
                ␥3 − ␥2 + i共␻32 − ␻兲                                                     tain the steady state equation

                                                                                                                             冕                 冕
                                                                  共A8b兲
and the steady-state density matrix elements                                             0 = i␹␳22 − i共␻32 − ␻兲␳32
                                                                                                                +
                                                                                                                   +             dkjk␳3,1k
                                                                                                                                      +
                                                                                                                                           +       dkgk␳2k,2
                                                                                                                                                        +




                            冕                                                                      冉 冊                            冕 冋                                 册
                                t
                                                                    ⌳                               ⌳                                          − jk␳32
                                                                                                                                                    +
                                                                                                                                                       + i␹␳2,1k
                                                                                                                                                            +
                 ␳22 =               dt0⌳b2共t,t0兲bⴱ2共t,t0兲 =           ;          共A9兲     = i␹        − i共␻32 − ␻兲␳32
                                                                                                                    +
                                                                                                                       −              dkjk
                              −⬁                                   2␥2                             2␥2                                       i共␻k + ␻ − ␻31兲 − ⑀


 ␳32
  +
     =  冕   t
          dt0⌳b3共t,t0兲bⴱ2共t,t0兲 =
                                            i␹⌳              1
                                                                             冋                 −   冕dk
                                                                                                             gk2 ␳32
                                                                                                                  +

                                                                                                         i共␻k − ␻兲 + ⑀⬙
                                                                                                                        = i␹
                                                                                                                              ⌳
                                                                                                                             2␥2
                                                                                                                                 冉 冊
                                                                                                                                 − i共␻32 − ␻兲␳32
                                                                                                                                              +




                                                                                                   冕 冋                                                   册
       −⬁                         ␥ 3 − ␥ 2 + i共 ␻ 32 − ␻ 兲 2 ␥2

                                             册冉 冊
                                                                                                              gk2 ␳32
                                                                                                                   +
                                                                                                                                 jk2 ␳32
                                                                                                                                      +
                   1              ⌳           i␹                                               −    dk                  +
        −                      =                          .                                               i共␻k − ␻兲 + ⑀⬙ i共␻k + ␻ − ␻31兲 − ⑀⬘
          ␥3 + ␥2 + i共␻32 − ␻兲   2␥2 ␥3 + ␥2 + i共␻32 − ␻兲


The result is as expected; ⌫23 is evaluated at −␻ and ⌫12 at
                                                                                 共A10兲         −   冕dk
                                                                                                                         i␹ jk2 共 ⌫⌳2 兲
                                                                                                         关i共␻k + ␻ − ␻31兲 − ⑀兴关i共␻k − ␻21兲 − ⑀⬘兴
                                                                                                                                                         .     共A14兲

−␻21. The polarizability 共A3兲 is                                                         Using Eq. 共69兲 and 共72兲, one finds

                                                                                   043835-11
MILONNI et al.                                                                                             PHYSICAL REVIEW A 77, 043835 共2008兲


     0 = i␹   冉 冊⌳
                2␥2
                    + i共␻32 − ␻兲␳32
                                 +
                                    − ␥3␳32
                                         +
                                            − ␥2⬘␳32
                                                  +                                                   ␥2⬘ = ⌫12关− 共␻32 − ␻兲 − ␻21兴.               共A17兲


        − i␹    冕 冉 冊冋
                  dkjk2
                           ⌳
                          2␥22
                                           1
                                  i共␻32 − ␻兲 − ⑀⬘ + ⑀
                                                            册                      For overall consistency of the result to this order, we re-

            冋                                                   册
                                                                                   placed 关i共␻32 − ␻兲 − ⑀⬘ + ⑀兴−1 by 关i共␻32 − ␻兲兴−1 in the second
                          1                   1                                    line of Eq. 共A15兲.
        ⫻                            −
                关i共␻k + ␻ − ␻31兲 − ⑀兴 关i共␻k − ␻21兲 − ⑀⬘兴                              The polarizability

      ⬇ i␹    冉 冊⌳
                2␥2
                    − i共␻32 − ␻兲␳32
                                 +
                                    − ␥3␳32
                                         +
                                            − ␥2⬘␳32
                                                  +
                                                     + i␹
                                                           ⌳
                                                          2␥2
                                                                 冉 冊
        ⫻   冋
           共␥2⬘ − ␥2兲
          i共␻32 − ␻兲
                           册                                        共A15兲           ␣=
                                                                                          2 +
                                                                                         d23 ␳32 d23
                                                                                         ប␹␳22
                                                                                                =
                                                                                                  2
                                                                                                       冋      1
                                                                                                  ប 共␻32 − ␻兲 − i共␥2⬘ + ␥3兲
                                                                                                                                  册冋   1+
                                                                                                                                              ␥2⬘ − ␥2
                                                                                                                                            i共␻32 − ␻兲
                                                                                                                                                         册
or                                                                                                                                                共A18兲


     ␳32
      +
         = i␹   冉 冊冋
                   ⌳
                  2␥2
                                   1
                          i共␻32 − ␻兲 + ␥2⬘ + ␥3
                                                  册冋   1+
                                                              ␥2⬘ − ␥2
                                                            i共␻32 − ␻兲
                                                                         册         agrees with Eq. 共78兲 in RWA with the neglect of level shifts.
                                                                    共A16兲          If the second term in Eq. 共A18兲 is brought into the denomi-
where                                                                              nator, the result agrees with Eq. 共A11兲.




 关1兴 G. Placzek, in Handbuch der Radiologie, edited by G. Marx                     关12兴 L. N. Labzowsky, D. A. Solovyev, G. Plunien, and G. Soff,
     共Akademische Verlagsgesellschaft, Leipzig, 1934兲, Vol. 6, p.                       Phys. Rev. Lett. 87, 143003 共2001兲.
     247.                                                                          关13兴 In general, only one component of the dipole matrix element
 关2兴 S. Hassing and E. N. Svendsen, J. Raman Spectrosc. 35, 87                          can be taken as real—the phase of the other components is
     共2004兲.                                                                            then determined uniquely. To simplify matters, we have taken
 关3兴 See, for instance, S.-Y. Lee and K.-S. Chow, J. Raman Spec-                        all the components of dij to be real since this in no way
     trosc. 16, 386 共1985兲.                                                             changes the qualitative nature of the results.
 关4兴 D. L. Andrews, S. Naguleswaran, and G. E. Stedman, Phys.                      关14兴 We have dropped the factor of 共1/3兲 appearing in Eq. 共3兲. For
     Rev. A 57, 4925 共1998兲; G. E. Stedman, S. Naguleswaran, D.                         a true two level system, the polarizability must be represented
     L. Andrews, and L. C. Dávila Romero, ibid. 63, 047801                              as a tensor, since matrix elements of each component of d are
     共2001兲; D. L. Andrews, L. C. Dávila Romero, and G. E. Sted-                        not necessarily equal. The polarizabilities in this paper can be
     man, ibid. 67, 055801 共2003兲.                                                      viewed as the diagonal element of the polarizability tensor in
 关5兴 A. D. Buckingham and P. Fischer, Phys. Rev. A 61, 035801                           the direction of either d12 共two-level polarizabilty兲 or d23
     共2000兲; A. D. Buckingham and P. Fischer, ibid. 63, 047802                          共three-level polarizability兲. The factor of 1/3 is included in the
     共2001兲.                                                                            equations for the polarizability in Refs. 关6兴 and 关9兴, for in-
 关6兴 P. W. Milonni and R. W. Boyd, Phys. Rev. A 69, 023814                              stance. Here we omit that factor in comparing our results with
     共2004兲.                                                                            those of Ref. 关9兴. The factor of 共1/3兲 affects the expression for
 关7兴 R. Loudon and S. M. Barnett, J. Phys. B 39, S555 共2006兲.                           the optical theorem. Without it, the optical theorem takes the
 关8兴 P. R. Berman, R. W. Boyd, and P. W. Milonni, Phys. Rev. A                          form 共12兲. With it, the right-hand side of Eq. 共12兲 is multiplied
      74, 053816 共2006兲.                                                                by 3, as in Eq. 共5兲 of Ref. 关7兴.
 关9兴 I. Bialynicki-Birula and T. Sowiński, Phys. Rev. A 76, 062106                 关15兴 V. B. Berestetskii, E. M. Lifshitz, and L. P. Pitaevskii, Quan-
     共2007兲.                                                                            tum Electrodynamics 共Pergamon Press, Oxford, 1982兲.
关10兴 Other relevant literature has been mentioned in Refs. 关4兴 and                 关16兴 S. Mukamel, Phys. Rev. A 76, 021803共R兲 共2007兲.
     关6兴 and other papers cited herein. See also Ref. 关5兴 and R. W.                关17兴 We quote the remark following Eq. 共59.22兲, p. 227, of Ref.
     Boyd, J. E. Sipe, and P. W. Milonni, J. Opt. A, Pure Appl. Opt.                    关15兴.
      6, S14 共2004兲 for remarks on the relevance of the damping                    关18兴 L. Schiff, Quantum Mechanics 共McGraw-Hill, New York,
     terms to the question of the existence of a linear electro-optic                   1955兲, Sec. 25.
     effect in isotropic chiral media, and R. W. Boyd, Nonlinear                   关19兴 H. M. Nussenzveig, Causality and Dispersion Relations 共Aca-
     Optics, 2nd ed. 共Academic Press, San Diego, 2003兲, p. 158; D.                      demic Press, New York, 1972兲.
     A. Long, The Raman Effect 共Wiley, New York, 2001兲. Here we                    关20兴 D. N. Zubarev, Sov. Phys. Usp. 3, 320 共1960兲.
     are concerned primarily with the specific case of radiative                   关21兴 E. R. Pike and S. Swain, J. Phys. A 4, 555 共1971兲.
     damping.                                                                      关22兴 C. Cohen–Tannoudji, J. Dupont–Roc, and G. Grynberg, Atom–
关11兴 U. D. Jentschura and P. J. Mohr, Can. J. Phys. 80, 633 共2002兲.                     Photon Interactions 共Wiley, New York, 1992兲.


                                                                             043835-12
