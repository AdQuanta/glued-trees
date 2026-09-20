# Polarizability and the optical theorem for a two-level atom with radiative broadening - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.74.053816
> Collected: 2026-09-20
> Published: 2006-11-21
> Zotero parent key: 8HDV27GR
> Evidence: Publisher or author-preprint PDF

PHYSICAL REVIEW A 74, 053816 共2006兲

        Polarizability and the optical theorem for a two-level atom with radiative broadening

                                                            Paul R. Berman
        Michigan Center for Theoretical Physics, FOCUS Center, and Physics Department, University of Michigan, Ann Arbor,
                                                   Michigan 48109-1040, USA

                                                            Robert W. Boyd
                           The Institute of Optics, University of Rochester, Rochester, New York 14627, USA

                                                            Peter W. Milonni
                                       104 Sierra Vista Dr., Los Alamos, New Mexico 87544, USA
                                        共Received 3 August 2006; published 21 November 2006兲
                The effect of spontaneous decay on the linear polarizability of an atom is typically included by adding
              imaginary parts to the frequency denominators that appear in the Kramers-Heisenberg formula. It has been
              shown for a two-level atom with radiative broadening that these 共frequency-dependent兲 imaginary parts must
              be included in both the resonant and antiresonant frequency denominators 关P. W. Milonni and R. W. Boyd,
              Phys. Rev. A 69, 023814 共2004兲兴; however, the expression obtained by Milonni and Boyd for the polarizability
              does not satisfy the optical theorem, if contributions from non-rotating-wave terms are included. In this paper,
              we derive a more accurate expression for the polarizability. The calculations are rather complicated and require
              that we go beyond the standard Weisskopf-Wigner approximation. We present calculations carried out in both
              the Heisenberg and Schrödinger pictures, since they offer complementary methods for understanding the
              dynamics of the Rayleigh scattering associated with the atomic polarizability. Moreover, it is shown that the
              shifts associated with the excited state are not the Lamb shifts of an isolated atom, but depend on the dynamics
              of the atom-field interaction. Our results for the polarizability are consistent with those obtained recently by
              Loudon and Barnett using a Green’s-function approach.

              DOI: 10.1103/PhysRevA.74.053816                      PACS number共s兲: 42.65.An, 32.10.Dk, 32.70.Jz, 32.80.⫺t


                     I. INTRODUCTION                                    ment is real. However, the situation is more complicated be-
                                                                        cause ␥ j is, in general, frequency dependent, as has been
   An atom in its ground state has a linear polarizability 关1兴

                                冉                   冊
                                                                        emphasized recently in the case of radiative damping, where
                      1             1      1                            ␥ j ⬀ ␻3 关6兴. In that work the radiative damping was found not
            ␣共␻兲 =      兺
                     3ប j
                          兩d j兩2       +
                                 ␻j − ␻ ␻j + ␻
                                                                共1兲
                                                                        to affect the antiresonant denominator. Of course, all these
                                                                        correction terms are small if ␥ j / 兩␻ j ± ␻ 兩 Ⰶ 1; moreover, in
if it is assumed that the field frequency ␻ is far removed              this limit, the underlying atom-field interaction is Rayleigh
from any absorption resonance. Here, d j and ␻ j are the elec-          scattering.
tric dipole matrix element and the angular transition fre-                  The question of the sign of the damping term in frequency
quency, respectively, connecting the excited state j to the             denominators arises also in the case of nonlinear susceptibili-
ground state. This 共Kramers-Heisenberg兲 关1兴 formula ignores             ties. Long 关7兴, for instance, discusses some historical aspects
the effects of collisions, spontaneous emission, and other line
                                                                        of this question in the case of Raman scattering and advo-
broadening phenomena that can be accounted for by adding
                                                                        cates the opposite-sign form.
imaginary parts to the frequency denominators in Eq. 共1兲, as
                                                                            The fact that antiresonant denominators are at issue in
well as self-energy corrections that appear as additional real
terms in both frequency denominators in Eq. 共1兲. Surpris-               these discussions means, of course, that derivations of the
ingly enough, however, this familiar procedure is not applied           polarizability, including relaxation processes, cannot be
uniformly in the literature. Some authors 关2兴 leave the                 based on the usual rotating-wave approximation 共RWA兲. The
“antiresonant” denominator ␻ j + ␻ unaltered while replacing            case of radiative damping is particularly complicated be-
the “resonant” denominator ␻ j − ␻ by ␻ j − ␻ − i␥ j, where             cause one must not only go beyond the RWA but must do so
␥ j 共⬎0兲 is the line width of the transition from the ground            within the Weisskopf-Wigner approximation or related ap-
state to state j. Others advocate a similar change in the               proximations that make the calculations tractable. On the
antiresonant denominator, but there have been lively debates            other hand, the case of radiative damping provides a simple
as to whether the modified denominator should be of the                 test of the accuracy of the calculation of ␣共␻兲, namely, that
“same-sign” form ␻ j + ␻ − i␥ j 关3兴 or the “opposite-sign” form         the polarizability satisfies the optical theorem.
␻ j + ␻ + i␥ j 关4,5兴. The causality requirement that ␣共␻兲 should            Let us briefly recall the form and physical significance of
be analytic in the upper half of the complex frequency                  the optical theorem in the context of an atom for which the
plane would appear to rule out the same-sign form, and simi-            only mechanism for energy loss in an isotropic environment
larly, this form does not satisfy the “crossing relation,”              is radiation. In this case, the optical theorem may be ex-
␣*共␻兲 = ␣共−␻兲, which guarantees that the induced dipole mo-             pressed in the form

1050-2947/2006/74共5兲/053816共11兲                                  053816-1                            ©2006 The American Physical Society
BERMAN, BOYD, AND MILONNI                                                                     PHYSICAL REVIEW A 74, 053816 共2006兲


                                    2␻3                                                     ␥共␻兲 = ⌫−共␻兲 + ⌫+共␻兲,                                 共9兲
                       ␣ I共 ␻ 兲 =       兩␣共␻兲兩2 ,             共2兲
                                    3c3                              P denotes principal part and
where ␣I共␻兲 is the imaginary part of the polarizability. This
expression follows from the condition that the rate of change
of the atomic 共or field兲 energy is zero. Physically, it simply
                                                                                     ⌫ ±共 ␻ 兲 =
                                                                                                   2d2
                                                                                                  3 ប c3
                                                                                                           冕
                                                                                                           0
                                                                                                               ⬁
                                                                                                                   d⍀⍀3␦共⍀ ± ␻兲               共10兲

states that the rate at which the atom’s energy increases due        such that
to absorption in the presence of a field of frequency ␻ must
exactly balance the rate at which the atom loses energy by                          ⌫+共␻兲 = 0;        ⌫−共␻兲 = 2d2␻3/3 ប c3
radiation, or, equivalently, the rate at which the field energy      for ␻ ⬎ 0. These results were obtained using the electric di-
decreases due to absorption must equal the rate of increase of       pole form of the atom interaction with the quantized field.
field energy due to scattering. Thus, the 共power兲 absorption         The divergent radiative level shifts ⌬±共␻兲 must obviously be
coefficient for the field in a dilute medium of N atoms per          renormalized, but this was not of direct concern in MB 关9兴
unit volume is a共␻兲 = 共4␲␻ / c兲N␣I共␻兲 and, equating this to          nor is it of concern here; the 共mass兲 renormalization process
N␴R共␻兲, where                                                        in any event cannot be correctly carried out in the two-level

                    ␴ R共 ␻ 兲 =                冉冊
                                  2 兩n − 1兩2 ␻ 4
                                 3␲ N2       c
                                                              共3兲
                                                                     approximation, since the dipole sum rule does not hold in the
                                                                     restricted Hilbert space of the TLA. We can write
                                                                                        ␦共␻兲 = − 关⌬E2共␻兲 − ⌬E1共␻兲兴/ ប ,                       共11兲
is the cross section for Rayleigh scattering 关8兴 and n − 1
⬵ 2␲N␣共␻兲 is the refractive index, we obtain Eq. 共2兲.                where ⌬E2共␻兲 = − ប ⌬−共␻兲 and ⌬E1共␻兲 = − ប ⌬+共␻兲 are the
   Let us recall also the familiar example of a classical elec-      level shifts of the upper 共兩2典兲 and lower 共兩1典兲 states, respec-
tron oscillator with resonance frequency ␻0. Including the           tively, of the TLA. ⌬E2共␻0兲 and ⌬E1共␻0兲, when modified to
radiation reaction force 2e2តx / 3c3 in the equation for the elec-   account for the fact that we have used the electric dipole
tron displacement x in the case of a driving field of amplitude      rather than minimal coupling form of the atom-field interac-
E0 and frequency ␻, we have                                          tion, are the nonrelativistic, unrenormalized “Lamb shifts” of
                                                                     the TLA in the absence of an applied field 关10兴. Note that
                                2e2      e                           both the transition width and shift in 共6兲 are evaluated at the
              mẍ + ␻20x −           ត
                                    3x =   E0 cos ␻t,         共4兲
                               3mc       m                           applied field frequency rather than the atomic transition fre-
                                                                     quency.
and, therefore,
                                                                        The purpose of MB 关9兴 was to address the question of the
                                       e2/m                          damping term in the antiresonant denominator in the specific
                  ␣共␻兲 =                            ,         共5兲    case of radiative broadening. The main conclusions to be
                           ␻20 − ␻2 − 2ie2␻3/3mc3
                                                                     drawn from the expression 共6兲 are that 共i兲 the radiative damp-
and the optical theorem 共2兲 is satisfied. Since a two-level          ing rate appears in both the resonant and the antiresonant
atom 共TLA兲 that remains with high probability in its ground          denominators, and 共ii兲 this damping rate is consistent with
state can for many purposes be approximated by such an               the opposite-sign convention, albeit the rate is, in fact, fre-
oscillator in which e2 / m is replaced by e2 f / m, where f is the   quency dependent. The expression 共6兲 can be rewritten, as-
oscillator strength of the transition, it might be expected that     suming ␥2共␻兲 Ⰶ 兩␻20 − ␻2兩 and ignoring for the moment the
the optical theorem for a TLA follows trivially from 共5兲. We         frequency shift ␦共␻兲, as 关11兴
show that things are not so simple.
   In light of the recent controversy concerning the same-                                2␻0d2/ប                         2␻0d2/ប
                                                                          ␣共␻兲 =                               =                              .
sign and opposite-sign forms, the polarizability for a two-                        ␻20 − ␻2 − 2i␻␥共␻兲              ␻20 − ␻2 − 2id2␻4/3 ប c3
level atom was recently revisited by Milonni and Boyd 关9兴,                                                                                    共12兲
hereafter referred to as MB, for the case of radiative damp-
ing. It was found that                                               The factor ␻ in the damping term in the denominator con-
                                                                                    4

                                                                     trasts with the ␻3 in the classical expression 共5兲. It follows
                   d2/ប                  d2/ប                        easily from Eq. 共2兲 that a consequence of this difference is
  ␣共␻兲 =                        +                      ,
           ␻0 − ␻ − ␦共␻兲 − i␥共␻兲 ␻0 + ␻ + ␦共␻兲 + i␥共␻兲               that 共12兲 does not satisfy the optical theorem.
                                                              共6兲       The major goal of this paper is to obtain a better approxi-
                                                                     mation than 共6兲 for the TLA polarizability in the case of
where d is the TLA transition dipole moment, which may be            radiative broadening. The results we obtain satisfy the opti-
taken to be real by an appropriate choice of the phases of the       cal theorem within the order of validity of the approxima-
lower- and upper-state wave functions, ␻0 is the TLA transi-         tion. Although the TLA polarizability of interest here can
tion frequency, and                                                  approximate that of a real atom in the case of a single
                     ␦共␻兲 = ⌬−共␻兲 − ⌬+共␻兲,                    共7兲    ground-to-excited-state transition with large oscillator
                                                                     strength, our primary interest here is in the calculation itself,

                                         冕
                                        ⬁                            which, as noted earlier, requires one to go beyond a
                                2d2       d⍀⍀3
                  ⌬ ±共 ␻ 兲 =          P        ,              共8兲    Weisskopf-Wigner-type approximation, which in its standard
                               3␲ ប c3 0 ⍀ ± ␻                       form involves the rotating-wave approximation as well as the

                                                               053816-2
POLARIZABILITY AND THE OPTICAL THEOREM FOR A…                                                           PHYSICAL REVIEW A 74, 053816 共2006兲

Markov approximation for which the line width and shift are                                        d
frequency dependent. To gain additional insight into the dy-             具 ˙␴共t兲典 = − i␻0具␴共t兲典 − i E0 cos ␻t具␴z共t兲典
                                                                                                   ប
namics responsible for the polarizability, we present calcula-
tions using both the Heisenberg and Schrödinger pictures.
This is a rare case in quantum optics in which a Schrödinger-                         + C2k   冕 ⬘
                                                                                              0
                                                                                               t
                                                                                                   dt 关具␴z共t兲␴共t⬘兲典 + 具␴z共t兲␴†共t⬘兲典兴ei␻k共t⬘−t兲
picture calculation is no more difficult than a Heisenberg-
picture one 关13兴; moreover, the Schrödinger-picture calcula-
tion is “exact” within certain limits, whereas the Heisenberg-                        − C2k   冕 ⬘
                                                                                              0
                                                                                               t
                                                                                                   dt 关具␴†共t⬘兲␴z共t兲典 + 具␴共t⬘兲␴z共t兲典兴e−i␻k共t⬘−t兲 .
picture approach is perturbative. It must be mentioned that a
different approach based on time-dependent Green’s func-                                                                                      共14兲
tions has been taken by Loudon and Barnett 关12兴, who first          Since the TLA is assumed to be initially in the lower state,
obtained corrections to 共6兲 that allow the optical theorem to       we approximate 具␴z共t兲典 in the second term on the right-hand
be satisfied. Following the calculations of the following three     side of 共14兲 by −1; this is the familiar approximation in
sections, we compare the assumptions and approximations             which the atom responds to the field as a classical Lorentz
made in these different approaches.                                 oscillator but with the factor e2 / m replaced by e2 f / m, where
   An important feature of the calculation is that it allows        f = 2m␻0d2 / e2ប is the oscillator strength. This approximation
one to investigate the origin of the level shifts that enter. The   assumes that the applied field frequency ␻ is far enough
Lamb shifts of the levels of an isolated atom can be calcu-         removed from the absorption resonance that the atom re-
lated in an unambiguous way; however, the level shifts that         mains with high probability in the lower state. This approxi-
appear in our calculation of the polarizability cannot be in-       mation is made in MB 关9兴, together with the “Markovian
terpreted solely in terms of these Lamb shifts, since the shifts    approximation” in the form
associated with the excited state that we find depend on the
dynamics of the atom-field interaction and are not the Lamb                            具␴z共t兲␴共t⬘兲典 ⬵ 具␴z共t⬘兲␴共t⬘兲典 = − 具␴共t⬘兲典               共15兲
shifts of an isolated atom 关14兴. This point is discussed in
more detail at the end of Sec. IV.                                  and likewise for the remaining three terms in the integrals on
                                                                    the right-hand side of 共14兲. These approximations lead
                                                                    straightforwardly to the polarizability 共6兲.
                II. HEISENBERG PICTURE I                               Here, we improve on the Markovian approximation 共15兲
                                                                    by using in 共14兲 the formal solution of the Heisenberg equa-
   We use essentially the same Hamiltonian and notation as          tion of motion for ␴z共t兲 that follows from the Hamiltonian
MB 关9兴 for the interaction of a two-level atom with the field       共13兲:

                                                                                                                        冕
in the electric dipole approximation, except that we treat the                                                          t
                                                                                                             dE0
applied field classically from the outset. For an applied field             ␴z共t兲 = ␴z共t⬘兲 + 2i                  cos ␻t dt⬙关␴共t⬙兲 − ␴†共t⬙兲兴
E0 cos ␻t polarized along the x direction, the Hamiltonian is                                                 ប        t⬘


                                                                                                   冕 ⬙
then                                                                                                   t
                                                                                        + 2Ck               dt 兵关␴共t⬙兲 − ␴†共t⬙兲兴ak共t⬙兲
                                                                                                       t⬘
        H = 21 ប ␻0␴z + ប ␻ka†k ak − dE0cos ␻t共␴ + ␴†兲
                                                                                         − a†k 共t⬙兲关␴共t⬙兲 − ␴†共t⬙兲兴其.                         共16兲
             − i ប Ck共␴ak + ␴†ak − a†k ␴ − a†k ␴†兲.         共13兲
                                                                       Consider the first term in the first integral on the right-
                                                                    hand side of 共14兲 when 共16兲 and the equal-time operator
ak and a†k are as usual the free-field photon annihilation and      identity ␴z共t⬘兲␴共t⬘兲 = −␴共t⬘兲 are used. We ignore terms of
creation operators for mode k, where k for brevity denotes          third- and higher-order in the atom field coupling Ck, which
the wave vector k and the polarization index ␭ 共=1 , 2兲 of a        amounts to dropping the third term in 共16兲 when 共16兲 is used
free-space, plane-wave field mode, and ␴, ␴†, and ␴z are,           in 共14兲. In this approximation, which we discuss in more
respectively, the TLA lowering, raising, and population dif-        detail later,

                                                                                  冕 ⬘
ference operators. We use a summation convention in which                          t
repeated field indices are to be summed over on the right-                  C2k        dt 具␴z共t兲␴共t⬘兲典ei␻k共t⬘−t兲
hand side of an equation unless they appear explicitly on the                     0


                                                                                              冕 ⬘ ⬘
left-hand side. The coupling constant Ck ⬅ 共d · ek␭兲                                               t
⫻共2␲␻k / ប V兲1/2, where ek␭ is the polarization unit vector for                   ⬵ − C2k              dt 具␴共t 兲典ei␻k共t⬘−t兲
the mode 共k , ␭兲 and V is the quantization volume. Without                                         0


                                                                                                冕 ⬘                        冕
loss of generality for our purposes, we take Ck to be real and                                        t            t
                                                                                            id
positive. As in MB 关9兴, we write the Heisenberg equation of                             −      E0C2k dt ei␻k共t⬘−t兲 dt⬙关e−i␻t⬙ + ei␻t⬙兴
motion for ␴共t兲 and take expectation values over an initial                                  ប       0            t⬘
state in which the initial TLA state is the lower state and the                         ⫻关具␴共t⬙兲␴共t⬘兲典 − 具␴†共t⬙兲␴共t⬘兲典兴.                      共17兲
initial field state is that in which all modes are unoccupied
except for that corresponding to the external, classically de-      To remain to second order in the atom-field coupling, we
scribed field                                                       make the replacements

                                                              053816-3
BERMAN, BOYD, AND MILONNI                                                                                                                   PHYSICAL REVIEW A 74, 053816 共2006兲


                      具␴共t⬙兲␴共t⬘兲典 → 具␴共0兲␴共0兲典e−i␻0共t⬙+t⬘兲 = 0,
                                                                                                                        C2k   冕 ⬘
                                                                                                                               0
                                                                                                                                  t
                                                                                                                                      dt ei共␻k±␻兲共t⬘−t兲 = ⌫±共␻兲 − i⌬±共␻兲.              共23兲

                     具␴†共t⬙兲␴共t⬘兲典 → 具␴†共0兲␴共0兲典ei␻0共t⬙−t⬘兲 = 0.                           共18兲        共We depart here from the notation in MB 关9兴 by using ⌫±共␻兲
The first expression is identically zero, whereas the second is                                        instead of ␥±共␻兲 and using ␥共␻兲 to denote ⌫+共␻兲 + ⌫−共␻兲
zero under the assumption that the initial TLA state is the                                            关Eq. 共9兲兴. Then, 共22兲 becomes
lower state 兩1典 共␴共0兲 兩 1典 = 0兲. Thus,
                                                                                                        C2k   冕 ⬘
                                                                                                               t
                                                                                                                   dt 具␴z共t兲␴†共t⬘兲典ei␻k共t⬘−t兲
  C2k   冕 ⬘  t
                  dt 具␴z共t兲␴共t⬘兲典ei␻k共t⬘−t兲 ⬵ − C2k                 冕 ⬘ ⬘
                                                                    t
                                                                        dt 具␴共t 兲典ei␻k共t⬘−t兲 ,
                                                                                                              0

             0                                                      0

                                                                                           共19兲
                                                                                                              ⬵ C2k     冕 ⬘
                                                                                                                         0
                                                                                                                          t
                                                                                                                              dt 具␴†共t⬘兲典ei␻k共t⬘−t兲 +
                                                                                                                                                              dE0 e−i␻t
                                                                                                                                                               ប ␻ + ␻0

which is equivalent to the approximation 共15兲 made in MB                                                            ⫻关⌫+共␻0兲 − ⌫−共␻兲 − i⌬+共␻0兲 + i⌬−共␻兲兴
关9兴 for the first term in the first integral on the right-hand side                                                     dE0 ei␻t
of 共14兲.                                                                                                            −             关⌫+共␻0兲 − ⌫+共␻兲 − i⌬+共␻0兲 + i⌬+共␻兲兴.
                                                                                                                         ប ␻ − ␻0
   Consider next the second term in the first integral on the
right-hand side of 共14兲 when 共16兲 and the identity                                                                                                                                     共24兲
␴z共t⬘兲␴†共t⬘兲 = ␴†共t⬘兲 are used. Following the same approxi-                                                We proceed in the same way to evaluate, approximately,
mation leading to 共17兲, we make the replacement                                                        the second integral on the right-hand side of 共14兲. Collecting

                  冕 ⬘ t                                                                                all the terms, we obtain the following approximate equation
            C2k           dt 具␴z共t兲␴†共t⬘兲典ei␻k共t⬘−t兲                                                   for 具␴共t兲典:
                     0
                                                                                                                                                      id
                     → 兺 C2k            冕 ⬘ ⬘
                                           t
                                               dt 具␴†共t 兲典ei␻k共t⬘−t兲
                                                                                                              具 ˙␴共t兲典 = − i␻0具␴共t兲典 +
                                                                                                                                                      2ប
                                                                                                                                                         E0关e−i␻t + ei␻t兴

                                   k      0
                                                                                                                                        冕 ⬘ t
                                                                                                                                                dt 关− 具␴共t⬘兲典 + 具␴†共t⬘兲典兴ei␻k共t⬘−t兲
                                          冕 ⬘ 冕 ⬙
                                           t            t                                                                     + C2k
                                   id
                                  − E0C2k dt ei␻k共t⬘−t兲 dt 关e−i␻t⬙ + ei␻t⬙兴                                                                 0


                                                                                                                                        冕 ⬘
                                    ប     0            t⬘                                                                                   t
                                                                                                                              − C2k             dt 关− 具␴†共t⬘兲典 + 具␴共t⬘兲典兴e−i␻k共t⬘−t兲
                              ⫻具关␴共t⬙兲␴ 共t⬘兲 − ␴ 共t⬙兲␴ 共t⬘兲兴典.
                                               †         †      †
                                                                                           共20兲                                             0

As in 共18兲, we take

            具␴共t⬙兲␴†共t⬘兲典 ⬵ 具␴共0兲␴†共0兲典e−i␻0共t⬙−t⬘兲 = e−i␻0共t⬙−t⬘兲 ,
                                                                                                                              +
                                                                                                                                   d
                                                                                                                                   ប
                                                                                                                                     E0e−i␻t      冋
                                                                                                                                             − ⌫−共␻兲 + i⌬−共␻兲 − i⌬+共␻0兲
                                                                                                                                                       ␻ + ␻0


                     具␴†共t⬙兲␴†共t⬘兲典 ⬵ 具␴†共0兲␴†共0兲典ei␻0共t⬙+t⬘兲 = 0                          共21兲
                                                                                                                              +
                                                                                                                                   − ⌫+共␻兲 + i⌬+共␻0兲 − i⌬+共␻兲
                                                                                                                                             ␻ − ␻0
                                                                                                                                                                        册
for the initial TLA state 兩1典. Then,                                                                                          −
                                                                                                                                   d
                                                                                                                                   ប
                                                                                                                                     E 0e i␻t    冋
                                                                                                                                              − ⌫−共␻兲 + i⌬+共␻0兲 − i⌬−共␻兲
                                                                                                                                                        ␻ + ␻0

C2k   冕 ⬘
       0
        t
            dt 具␴z共t兲␴†共t⬘兲典ei␻k共t⬘−t兲                                                                                        +
                                                                                                                                   − ⌫+共␻兲 + i⌬+共␻兲 − i⌬+共␻0兲
                                                                                                                                             ␻ − ␻0
                                                                                                                                                              ,         册              共25兲


       ⬵ C2k         冕 ⬘  0
                              t
                                  dt 具␴†共t⬘兲典ei␻k共t⬘−t兲 −
                                                             id
                                                              ប
                                                                       t
                                                                        冕           t
                                                                E0C2k dt⬘ei␻k共t⬘−t兲 dt⬙
                                                                      0            t⬘
                                                                                        冕              where we have used the fact that ⌫+共␻0兲 = 0.
                                                                                                          The solution of 共25兲 has the form 具␴共t兲典 = se−i␻t + rei␻t, and
                                                                                                       the induced dipole moment p = d具␴ + ␴†典 = 2d Re关共s
             ⫻关e−i␻t⬙ + ei␻t⬙兴e−i␻0共t⬙−t⬘兲                                                             + r*兲e−i␻t兴 ⬅ Re关␣共␻兲E0e−i␻t兴. Solving 共25兲 for s and r, we

                     冕 ⬘  t                                                                            obtain
                                                             d
       = C2k                  dt 具␴†共t⬘兲典ei␻k共t⬘−t兲 +          E0                                                                     2d2␻0           1
                         0                                   ប                                                      ␣共␻兲 ⬵
                                                                                                                                        ប ␻0 − ␻ − 2i␻关␥共␻兲 − i␦共␻兲兴
                                                                                                                                            2


                                                冕
                                                                                                                                                2



                                                                                                                                        冋
                                      t
                       1
             ⫻              e−i␻tC2k dt⬘关ei共␻k+␻0兲共t⬘−t兲 − ei共␻k−␻兲共t⬘−t兲兴                                                                           ⌬−共␻兲 + i⌫−共␻兲 − ⌬+共␻0兲
                     ␻ + ␻0          0                                                                                                ⫻ 1+2
                                                                                                                                                              ␻ + ␻0
                 −
                     d
                       E0
                          1
                     ប ␻ − ␻0
                                       t
                                                     冕
                              ei␻tC2k dt⬘关ei共␻k+␻0兲共t⬘−t兲 − ei共␻k+␻兲共t⬘−t兲兴.
                                      0                                                                                               +2
                                                                                                                                           ⌬+共␻0兲 − ⌬+共␻兲 + i⌫+共␻兲
                                                                                                                                                   ␻ − ␻0
                                                                                                                                                                         册             共26兲
                                                                                           共22兲
                                                                                                       for the TLA polarizability. This expression satisfies the cross-
      For the times t Ⰷ 1 / ␻ of interest, we use                                                      ing relation ␣*共−␻兲 = ␣共␻兲. If we retain only terms up to

                                                                                                 053816-4
POLARIZABILITY AND THE OPTICAL THEOREM FOR A…                                                   PHYSICAL REVIEW A 74, 053816 共2006兲

fourth order in d 共recall that all the widths and shifts are of              The total 共cycle-averaged兲 power radiated by the TLA is
order d2兲, consistent with the approximations used in our
derivation, then the optical theorem 共2兲 is also satisfied to                                  ␻4 2 2 4d2␻4␹2兩␤兩2
                                                                                          P=       兩␣兩 E0 =       ,                     共32兲
this order. We defer further discussion of this result to Sec. V.                              3c3          3c3
   In this section, we have shown how to generalize the re-
sults of MB 关9兴 to obtain an expression for the polarizability          and the rate at which energy is lost from the external field is
that is consistent with the optical theorem; however, it is             calculated straightforwardly to be
difficult to rigorously justify the factorization approxima-                                    P = 2 ប ␻␹2 Im关␤兴.                      共33兲
tions that were used in arriving at this result. We now give
alternative derivations based a Schrödinger-picture approach            The optical theorem is satisfied if these two expressions are
and a Heisenberg picture, in which the approximations intro-            equal
duced are more transparent. Moreover, these alternative deri-
                                                                                                   2 ␻ 3d 2 2
vations provide additional insight into the underlying physi-                            Im关␤兴 =           兩␤兩 = ⌫−共␻兲兩␤兩2 .            共34兲
cal processes contributing to the polarizability.                                                  3 ប c3

                III. SCHRÖDINGER PICTURE                                    In order to obtain ␤, one is faced with the task of calcu-
                                                                        lating
   In many cases, it is easier, computationally, to evaluate
expectation values of atomic Heisenberg operators, such as                           ␳21 = ␳2,0;1,0 + ␳2,k;1,k + ␳2,kk⬘;1,kk⬘ + ¯       共35兲
the polarizability, using a Heisenberg- rather than
Schrödinger-picture approach. In this case, however, since              and extracting ␳21
                                                                                         +
                                                                                           and ␳21−
                                                                                                    from this quantity. To first order in
we are working to first order in the external field amplitude,          ␹, it turns out that terms beyond the first two make contri-
the Schrödinger approach is no more difficult than the                  butions to ␳21
                                                                                     +
                                                                                       and ␳21
                                                                                             −
                                                                                                of order C2k / 共␻0 + ␻k兲2, that is, of order
Heisenberg approach. Moreover, it is a simple matter to keep            of the TLA “Lamb shift” divided by ␻0. Such terms, which
track of the amplitudes that contribute and no factorization            also determine the 共non-RWA兲 excited-state population in the
approximations are needed. Within certain approximations to             absence of any applied fields, are systematically neglected in
be specified below, this approach is exact.                             this work, as are terms of order C2k / 共␻0 + ␻k兲共␻ + ␻k兲:
   The state vector for the system can be written as
                                                                                                         C2k
兩␺典 = b1,0兩1,0典 + b2,0兩2,0典 + b1,k兩1,k典 + b2,k兩2,k典 + b1,kk⬘兩1,kk⬘典                                               Ⰶ 1,                 共36a兲
                                                                                                   共 ␻ 0 + ␻ k兲 2
      + b2,kk⬘兩2,kk⬘典 + ¯ .                                     共27兲
                                                                                                     C2k
The field states, which are specified by the second label in                                                    Ⰶ 1.                   共36b兲
each ket, refer to vacuum field modes; as before, the exter-                                  共␻0 + ␻k兲共␻ + ␻k兲
nally applied field is treated classically. Thus, 兩1 , 0典 and 兩2 , 0典
                                                                        As a consequence, the density matrix element 共35兲 can be
are, respectively, the states in which the TLA is in the lower
                                                                        approximated for our purposes as
state and the upper state and the field state is the vacuum.
兩1 , k典 and 兩2 , k典 are states in which the TLA is in the lower                                ␳21 ⬵ ␳2,0;1,0 + ␳2,k;1,k .              共37兲
state and the upper state, respectively, and there is a single
photon in the field mode denoted by k, as in the preceding                  Instead of directly calculating density matrix elements, we
section. Similarly, 兩1 , kk⬘典 and 兩2 , kk⬘典 are states in which the     calculate probability amplitudes and form density matrix el-
TLA is in the lower state and the upper state, respectively,            ements from these amplitudes. This simplifies the calculation
and there is a photon in mode k and a photon in mode k⬘.                considerably and enables us to obtain an expression for ␤共␻兲
     The expectation value of the electric dipole moment is             that is essentially exact to all orders in the vacuum coupling
                                                                        strength. An amplitude approach can be used in this problem
               p = p+e−i␻t + p−ei␻t = d共␳21 + ␳12兲,             共28兲    since the vacuum field states responsible for relaxation are
where ␳21 = ␳12
             *
                is an off-diagonal density matrix element.              included explicitly in the state amplitudes. Such a procedure
Writing                                                                 is practical in our case owing to the fact that the calculation
                            + −i␻t    − i␻t
                                                                        is perturbative in the applied field—for a strong external field
                     ␳21 = ␳21 e   + ␳21 e ,                    共29兲    共Rabi frequency greater than decay rates兲, the number of
we can express the complex polarizability as                            terms that enter would render the amplitude approach virtu-
                                                                        ally useless.
                               p + d 2␤                                     Owing to the definition 共31兲, we need only calculate ␳21 to
                          ␣=      =     ,                       共30兲
                               E+   ប                                   first order in ␹. The equations for the probability amplitudes
                                                                        are easily obtained from the Hamiltonian 共13兲 and the time-
where                                                                   dependent Schrödinger equation 关15兴:
                           lim 关␳21
                                 +
                                    + 共␳21
                                        − *
                                           兲兴
                      ␤=
                           ␹→0
                                                                共31兲                    ḃ1,0 = i␹共ei␻t + e−i␻t兲b2,0 − Ckb2,k ,        共38a兲
                                   ␹
and the Rabi frequency is defined by ␹ = dE0 / 2ប.                                 ḃ2,0 = i␹共ei␻t + e−i␻t兲b1,0 − i␻0b2,0 − Ckb1,k ,   共38b兲

                                                                  053816-5
BERMAN, BOYD, AND MILONNI                                                                                     PHYSICAL REVIEW A 74, 053816 共2006兲


    ḃ1,k = Ckb2,0 − Ck⬘b2,kk⬘ − i␻kb1,k + i␹共ei␻t + e−i␻t兲b2,k ,                                   0 = i␹ − i关⌬ + ⌬+共␻0兲兴b2,0
                                                                                                                           +        +
                                                                                                                               − Ckb1,k                 共42a兲
                                                                           共38c兲
                                                                                                   0 = i␹ − i关⌬共+兲 + ⌬+共␻0兲兴b2,0
                                                                                                                             −        −
                                                                                                                                 − Ckb1,k               共42b兲
                     i␻t        −i␻t
      ḃ2,k = i␹共e         +e          兲b1,k − i共␻0 + ␻k兲b2,k + Ckb1,0 ,
                                                                           共38d兲                                +
                                                                                                 +
                                                                                          0 = Ckb2,0 − Ck⬘b2,kk⬘ − i关␻k − ␻ + ⌬+共␻0兲 − i⑀兴b1,k
                                                                                                                                           +


      ḃ2,kk⬘ = − i共␻0 + ␻k + ␻k⬘兲b2,kk⬘ + Ck⬘b1,k + Ckb1,k⬘ .                                 + i␹b̃2,k 共no sum on k兲                                  共42c兲
                                                                           共38e兲
                                                                                                                    −
We neglect ground-state amplitudes involving two or more                                            −
                                                                                             0 = Ckb2,0 − Ck⬘b2,kk⬘ − i关␻k + ␻ + ⌬+共␻0兲兴b1,k
                                                                                                                                         −
free-field photons and excited-state amplitudes involving
three or more free-field photons, since they lead to correc-                                      + i␹b̃2,k 共no sum on k兲                               共42d兲
tions of order 共36兲; the probability amplitudes we retain are
the only ones that contribute to ␳21 to first order in the ex-
ternal field. These probability amplitudes satisfy Eqs. 共38兲,                                                                             +
                                                                                          0 = − i关␻0 − ␻ + ␻k + ␻k⬘ + ⌬+共␻0兲兴b2,kk⬘ + Ck⬘b1,k
                                                                                                                                          +
which are to be solved to first order in ␹ and to all orders in
                                                                                                      +
the vacuum coupling Ck.                                                                        + Ckb1,k⬘ 共no sum兲                                       共42e兲
   We are interested in steady-state solutions for the prob-
ability amplitudes. From the structure of Eqs. 共38兲, we de-
duce that b2,0, b1,k, and b2,kk⬘ oscillate as e±i␻t and depend                                                                            −
linearly on ␹, while b1,0 and b2,k have no linear dependence                              0 = − i关␻0 + ␻ + ␻k + ␻k⬘ + ⌬+共␻0兲兴b2,kk⬘ + Ck⬘b1,k
                                                                                                                                          −

on ␹. To first order in ␹, then, the solution of 共38d兲 is                                             −
                                                                                               + Ckb1,k⬘ 共no sum兲,                                      共42f兲
                                           − iCkb1,0
                                b2,k ⬵               ,                      共39兲
                                           ␻0 + ␻k                                  where
and, substituting this back into 共38a兲 共and neglecting the lead
term, which is of order ␹2兲, we obtain                                                                    ⌬ = ␻0 − ␻ ;        ⌬共+兲 = ␻0 + ␻ ,            共43兲

                            ḃ1,0 ⬵ i⌬+共␻0兲b1,0 .                           共40兲
                                                                                                                              − iCk
    In obtaining a solution to Eqs. 共38兲 and 共40兲 to first order                                                   b̃2,k ⬇           .                   共44兲
in ␹, we find that b2,0, b1,k, and b2,kk⬘ oscillate as e±i␻t+i⌬+共␻0兲t                                                        ␻0 + ␻k
while b1,0 and b2,k oscillate as ei⌬+共␻0兲t. Thus, we assume a
trial solution of the form                                                          The frequency ␻k has been replaced by ␻k − i⑀ in Eq. 共42c兲,
                                                                                    where ⑀ is a positive quantity that tends toward zero, to en-
                                  b1,0 = ei⌬+共␻0兲t                         共41a兲    sure that a steady-state solution for b1,k +
                                                                                                                                 exists. In terms of
                                                                                    these parameters, it follows from Eqs. 共29兲, 共31兲, 共37兲, and
                         + −i␻t    − i␻t i⌬+共␻0兲t
                b2,0 = 共b2,0 e  + b2,0 e 兲e                                共41b兲    共41兲, and the fact that ␳a,a⬘ = b␣b␣* , that
                                                                                                                         ⬘
                         + −i␻t    − i␻t i⌬+共␻0兲t
                b1,k = 共b1,k e  + b1,k e 兲e                                共41c兲                       +
                                                                                                      b2,0 + 共b2,0
                                                                                                               − *
                                                                                                                   兲 + b̃2,k共b1,k
                                                                                                                              − *
                                                                                                                                  兲 + b̃2,k
                                                                                                                                        * +
                                                                                                                                            b1,k
                                                                                                 ␤=                                              .       共45兲
                                       − iCk                                                                             ␹
        b2,k = b̃2,kei⌬+共␻0兲t =                    ei⌬+共␻0兲t 共41d兲
                                关␻0 + ␻k + ⌬+共␻0兲兴                                     Equations 共42兲 break up into two uncoupled sets of equa-
                                                                                                    +      +             +                         −      −
                                                                                    tions, one for b2,0 , b1,k , b̃2,k, b2,kk   and the other for b2,0 , b1,k ,
                                                                                                                              ⬘
             b2,kk⬘ = 共b2,kk⬘e−i␻t + b2,kk⬘ei␻t兲ei⌬+共␻0兲t .
                            +                  −
                                                                           共41e兲            −
                                                                                    b̃2,k, b2,kk   . However, it is sufficient to solve the first set only
                                                                                                 ⬘
                                                                                    since Eqs. 共42兲 imply that
Note that 兩b1,0 兩 = 1 and 兩b2,k 兩 = Ck / 关␻0 + ␻k + ⌬+共␻0兲兴 in the
approximations implicit in 共41兲; the fact that 兩b2,k 兩 ⫽ 0 results
                                                                                                               −               +
from fluctuations of the vacuum field that lead to a small                                                    ba,a⬘共␻兲 = ba,a⬘共− ␻兲
steady-state value for this amplitude 共but not to significant
population or to measurable radiation in the absence of any
applied field兲.
                                                                                                               b̃2,k共␻兲 = b̃2,k共− ␻兲                     共46兲
   When we substitute our trial solution into Eqs. 共38兲, and
keep terms only of first order in ␹, we obtain the steady-state
equations                                                                           for any 兵a , a⬘其. Therefore,

                                                                              053816-6
POLARIZABILITY AND THE OPTICAL THEOREM FOR A…                                                                     PHYSICAL REVIEW A 74, 053816 共2006兲

                                       +
                                      b2,0 共␻兲 + 关b2,0
                                                   −
                                                       共␻兲兴* + b̃2,k共␻兲关b1,k
                                                                         −
                                                                             共␻兲兴* + b̃2,k
                                                                                       *
                                                                                           共␻兲b1,k
                                                                                               +
                                                                                                   共␻兲
                         ␤共␻兲 =
                                                                     ␹
                                       −
                                      b2,0 共− ␻兲 + 关b2,0
                                                     +
                                                         共− ␻兲兴* + b̃2,k共− ␻兲关b1,k
                                                                               +
                                                                                   共− ␻兲兴* + b̃2,k
                                                                                               *
                                                                                                   共− ␻兲b1,k
                                                                                                         −
                                                                                                             共− ␻兲
                                  =                                                                                = ␤*共− ␻兲,
                                                                           ␹




i.e., the crossing relation is satisfied.
    We now solve Eqs. 共42兲 by eliminating b2,0   +
                                                   , b̃2,k, and
                                                                                            +
                                                                                           b2,0 =
                                                                                                             1
                                                                                                        ˜␥ + i⌬
                                                                                                                   冋   i␹ −
                                                                                                                              ˜␥␹
                                                                                                                              ⌬共+兲


                                                                                                                                                              册
  +
b2,kk to obtain an 共integral兲 equation for b1,k that is solved
                                            +
      ⬘                                                                                                                                  +
exactly using a Born series. We already have b̃2,k from 共44兲,                                                                  Ck⬘C2k b1,k⬘
                                    +                                                                   −i                                                        ,       共52兲
and we can use 共42e兲 to eliminate b2,kk                                                                      共␻0 − ␻ + ␻k + ␻k⬘兲共␻k − ␻ − i⑀兲
                                                    ⬘
                                  +                +
                     +
                              Ck⬘b1,k + Ckb1,k⬘                                  where
                   b2,kk⬘ =                             .              共47兲
                              ␻ 0 − ␻ + ␻ k + ␻ k⬘                                                 ⌬共+兲C2k
                                                                                   i˜␥ = lim                       = i⌫−共␻兲 + ⌬−共␻兲 − ⌬+共␻0兲.
关In writing 共44兲 and 共47兲, and in what follows, we neglect                              ⑀→0 共␻k − ␻ − i⑀兲共␻0 + ␻k兲
⌬+共␻0兲 in all frequency denominators except those involving                                                                                                               共53兲
⌬ and ␻k − ␻, since it represents a correction of order 共36兲.兴
Substituting this into 共42c兲, and using 共44兲, we obtain                          We have used

                       +
                0 = Ckb2,0 +i
                                      2
                                      +
                                  Ck⬘b1,k + Ck⬘Ckb1,k⬘
                                      ␻ 0 − ␻ + ␻ k + ␻ k⬘
                                                            +
                                                                                                            lim
                                                                                                                   1
                                                                                                            ⑀→0+ x − i⑀
                                                                                                                        = i␲␦共x兲 + P
                                                                                                                                     1
                                                                                                                                     x
                                                                                                                                       ,         冉冊                       共54兲


                    − i关␻k − ␻ + ⌬+共␻0兲 − i⑀兴b1,k
                                              +                                  where P again denotes the Cauchy principal part.
                                                                                   Using the approximation
                            Ck
                    +␹            共no sum on k兲.                       共48兲                                       +
                          ␻0 + ␻k                                                                                b1,k⬘
       +
Since b1,k is sharply peaked at ␻k = ␻, we make the approxi-                            共␻0 − ␻ + ␻k + ␻k⬘兲共␻k − ␻ − i⑀兲


                                                                                                                  冋                                                   册
mations                                                                                                 +
                                                                                                       b1,k⬘                1                1
                          +                 +                                                  =                                   −
                         b1,k              b1,k                                                    ␻ k⬘ + ␻ 0         ␻ k − ␻ − i ⑀ ␻ 0 − ␻ + ␻ k + ␻ k⬘
                                     ⬇

                                                                                                                  冋                                   册
                 ␻ 0 − ␻ + ␻ k + ␻ k⬘ 共 ␻ 0 + ␻ k⬘兲                                                      +
                                                                                                       b1,k⬘        1           1
                                                                                               ⬇                           −          ,                                   共55兲
                           +
                          b1,k⬘
                                                    +
                                                   b1,k⬘                                           ␻ k⬘ + ␻ 0 ␻ k − ␻ − i ⑀ ␻ 0 + ␻ k
                                            ⬇                          共49兲
                 ␻ 0 − ␻ + ␻ k + ␻ k⬘           共 ␻ 0 + ␻ k兲                     we rewrite Eq. 共52兲 as

with errors of order 共36兲. With this approximation, the term
involving Ck2 in Eq. 共48兲 is equal to i⌬+共␻0兲b1,k
             ⬘ +
                                              +
                                                  . This cancels
                                                                                                    +
                                                                                                   b2,0 =
                                                                                                                  1
                                                                                                               ˜␥ + i⌬
                                                                                                                         冋   i␹ −
                                                                                                                                    ˜␥␹
                                                                                                                                        − i
                                                                                                                                            ˜␥Ckb1,k
                                                                                                                                    ⌬共+兲 ␻k + ␻0
                                                                                                                                                 +
                                                                                                                                                     .    册               共56兲
the −i⌬+共␻0兲b1,k contribution from the second term on the
right-hand side, giving                                                          When Eq. 共56兲, in turn, is substituted back into Eq. 共50兲 and


                     冋                                                 册
                                                                                 共49兲 is used, we finally obtain the following 共integral兲 equa-
                                                                +                          +
                                   ␹          iCk⬘b1,k⬘                          tion for b1,k :


                                                                                                                  再冉
  +           iCk        +
 b1,k =               − b2,0 −          −                     .

                                                                                                                                                                          冊
          ␻k − ␻ − i⑀          ␻ 0 + ␻ k ␻ 0 − ␻ + ␻ k + ␻ k⬘
                                                                                       +           iCk                     − i␹     ␹         ˜␥␹
                                                                       共50兲           b1,k =                                    −       + 共+兲
                                                                                               ␻k − ␻ − i⑀               ˜␥ + i⌬ ␻0 + ␻k ⌬ 共˜␥ + i⌬兲
For future reference, we also note that

          1               1       1
                                ⬇ 共+兲
  共 ␻ k − ␻ − i ⑀ 兲 共 ␻ 0 + ␻ k兲 ⌬
                                           冋
                                           1
                                                 −
                                                     1
                                      ␻k − ␻ − i⑀ ␻0 + ␻k
                                                          .           册                            冉
                                                                                               −i 1−
                                                                                                                  ˜␥
                                                                                                                          冊
                                                                                                                                     +
                                                                                                                              Ck⬘b1,k⬘
                                                                                                             共˜␥ + i⌬兲 ␻0 + ␻k⬘
                                                                                                                                         冎   .                            共57兲

                                                                                 This equation can be solved iteratively to evaluate the sums
                                                                       共51兲
                                                                                 over k⬘ that occur in each iteration. In doing so, we can make
   When the solution 共50兲 is substituted into 共42a兲, we obtain                   the approximation

                                                                           053816-7
BERMAN, BOYD, AND MILONNI                                                                                        PHYSICAL REVIEW A 74, 053816 共2006兲


                C2k        1
                            冉
            ␻k − ␻ − i⑀ ␻0 + ␻k
                                2
                                        冊                                                                            −
                                                                                                                    b2,0 =
                                                                                                                              ␹
                                                                                                                             ⌬共+兲
                                                                                                                                  .                    共62兲


                  =
                      C2k
                           冋    1
                                      −
                                          1       1
                      ⌬共+兲 ␻k − ␻ − i⑀ ␻0 + ␻k ␻0 + ␻k
                                                             册                     All other amplitudes contribute to ␤ amounts that are smaller
                                                                                   by factors of order 共36兲. In this manner we obtain, to this
                                                                                   order, the combination 关b̃2,k共b1,k
                                                                                                                   − *
                                                                                                                      兲 + 共b2,0
                                                                                                                            − *
                                                                                                                                兲 兴 needed in the
                      C2k       1         1     i˜␥                                evaluation of ␤ as
                  ⬇                           =     ,
                      ⌬共+兲 ␻k − ␻ − i⑀ ␻0 + ␻k ⌬共+兲
                                                                                                                                           ␹
                                                                                                          关b̃2,k共b1,k
                                                                                                                  − *
                                                                                                                      兲 + 共b2,0
                                                                                                                            − *
                                                                                                                                兲 兴⬇           .       共63兲
the omitted term being of order 共36兲. In effect, we can re-                                                                               ⌬共+兲
place ␹ / 共␻0 + ␻k兲 in 共57兲 by ␹ / ⌬共+兲 since this leads only to
corrections of order 共36兲 in calculating ␤. Carrying out the                            Combining Eqs. 共63兲, 共39兲, 共60兲, 共61兲, and 共45兲, we arrive
iteration using these approximations, we have                                      at
                                                                                                          ⌬共+兲
                               i␹Ck
                                                         ⬁                              ␤共␻兲 =
                +
                                        共A + B兲 兺 关i˜␥B兴n ,                共58兲                  ⌬⌬共+兲 − 2i␻0˜␥

                                                                                                     冋冉                                            册
               b1,k =−

                                                                                                                                      冊
                            ␻k − ␻ − i⑀         n=0
                                                                                                                    C2k          *
                                                                                                                                     2␻0               *
                                                                                                 +                                 共+兲
where                                                                                                     共␻k − ␻ − i⑀兲共␻k + ␻0兲 ⌬⌬ + 2i␻0˜␥

                                            i                                                         1          ⌬共+兲     2i␻0˜␥/⌬共+兲    1
                                  A=                                                             +     共+兲 =            +              +
                                        ˜␥ + i⌬                                                      ⌬       ⌬⌬ − 2i␻0˜␥ ⌬⌬共+兲 − 2i␻0˜␥ ⌬共+兲
                                                                                                               共+兲


                                                                                                          2␻0
                  1
              B = 共+兲 1 −
                 ⌬
                           冉  ˜␥
                          共˜␥ + i⌬兲
                                    = 共+兲
                                          i⌬
                                     ⌬ 共˜␥ + i⌬兲
                                                冊.
                                                                                             =
                                                                                                 ⌬⌬共+兲 − 2i␻0˜␥
                                                                                                                  2␻0
                                                                                             =                                           .             共64兲
Since                                                                                            ⌬⌬共+兲 + 2␻0关⌬+共␻0兲 − ⌬−共␻兲兴 − 2i␻0⌫−共␻兲


    兩˜␥B兩 =   冏       i˜␥⌬
                   共+兲 ˜
                  ⌬ 共␥ + i⌬兲
                             ⱕ    冏 冑冏 冏 冑冏 冏    ˜␥
                                                ⌬共+兲
                                                     ⱕ
                                                                 ˜␥
                                                                 ␻0
                                                                    ⬍ 1,
                                                                                   This expression is exact, subject to the conditions 共36兲, and it
                                                                                   is easily verified that it satisfies the optical theorem 关Eq.
                                                                                   共34兲兴. The polarizability calculated in this Schrödinger-
                                                                           共59兲    picture approach is equivalent to that calculated in the
                                                                                   Heisenberg picture when 共36兲 holds and only contributions
we can carry out the summation in Eq. 共58兲 and obtain                              up to second order in d are retained. This can be seen by
                                                                                   writing the factor in large brackets in 共26兲 as 1 + x ⬵ 1 / 共1
    +         − i␹Ck 共A + B兲       − i␹Ck        2␻0                               − x兲, setting ⌫+共␻兲 = 0, and neglecting terms of order
   b1,k =                       =                           ,
            ␻k − ␻ − i⑀ 1 − i˜␥B ␻k − ␻ − i⑀ ⌬⌬共+兲 − 2i␻0˜␥                        关⌬+共␻兲 − ⌬+共␻0兲兴 / ⌬, consistent with condition 共36b兲. This
                                                                           共60兲    would imply that the condition x Ⰶ 1, along with 共36a兲, is
                                                                                   necessary for the validity of our factorization hypotheses. We
where the identity ⌬ + ⌬共+兲 = 2␻0 has been used. It then fol-                      now turn again to the Heisenberg picture, using an approxi-
lows from Eqs. 共52兲 and 共60兲 that                                                  mation scheme that further supports this contention and


                            冋
                                                                                   helps to elucidate some aspects of the TLA polarizability.
         +          −␹          ˜␥
        b2,0 =            − i + 共+兲                                                                   IV. HEISENBERG PICTURE II
                  ˜␥ + i⌬      ⌬

                                                                    册
                                                                                      From the Hamiltonian 共13兲 and the equal-time commuta-
                             ˜␥C2k             2␻0                                 tion relations, we obtain
                  +                          共+兲
                    共␻k − ␻ − i⑀兲共␻k + ␻0兲 ⌬⌬ − 2i␻0˜␥                                  具 ˙␴典 = − i␻0具␴典 − 2i␹ cos ␻t具␴z典 + Ck共具ak␴z典 − 具␴za†k 典兲,

              =
                      −␹
                  ˜␥ + i⌬
                            冋   −i+
                                      ⌬
                                       ˜␥    i␥
                                        共+兲 + 共+兲
                                                    2␻0
                                                    ˜2
                                                  共+兲
                                             ⌬ ⌬⌬ − 2i␻0˜␥
                                                                    册                                                                                  共65兲

                                                                                                      具ȧk典 = − i␻k具ak典 + Ck共具␴典 + 具␴†典兲.              共66兲
                   ␹⌬共+兲
              =                .                                           共61兲    Consistent with our previous approximations, we approxi-
                ⌬⌬共+兲 − 2i␻0˜␥
                                                                                   mate 具␴z典 in the second term on the right-hand side of 共65兲
This completes the calculation of the “+” terms.                                   by −1, since we are neglecting any excited-state population
   Although Eq. 共46兲 is exact, we cannot apply it directly to                      in the effect of the applied field on the atom. Thus, we work
                        −    −      −
obtain solutions for b2,0 , b1,k , b2,kk   since we have assumed                   with the approximate evolution equations
                                         ⬘
implicitly that ␻ ⬎ 0 in obtaining the solution 共61兲. On the                                 具 ˙␴典 = − i␻0具␴典 + 2i␹ cos ␻t − Ck共具ak典 − 具ak典*兲
other hand, it is easy to carry out an iterative solution to Eqs.
共42兲 to obtain, for instance,                                                                         + 2Ck共具ak␴22典 − 具a†k ␴22典兲,                  共67a兲

                                                                             053816-8
POLARIZABILITY AND THE OPTICAL THEOREM FOR A…                                                         PHYSICAL REVIEW A 74, 053816 共2006兲


                    具ȧk典 = − i␻k具ak典 + Ck共具␴典 + 具␴†典兲,            共67b兲                                             C*k
                                                                                                         ck = −            ,                        共70b兲
                                                                                                                   ␻0 + ␻k
                                     具␴ 典 = 具␴典 ,
                                        †           *
                                                                   共67c兲
                                                                            where the convergence parameter ⑀ has been reintroduced.
                                     具a†k 典 = 具ak典* ,              共67d兲      The key point now is to assume trial solutions of the form

where we have used ␴z = ␴22 − ␴11 = 2␴22 − 1.                                                         具␴典 = se−i␻t + rei␻t                          共71a兲
   It is now necessary to obtain equations of motion for
具ak␴22典 and its conjugate. This leads to an infinite set of                                          具␴†典 = r*e−i␻t + s*ei␻t                        共71b兲
coupled equations; however, since we are working to first
order in ␹, the equations can be truncated, just as in the                                           具ak典 = a+k e−i␻t + a−k ei␻t                    共71c兲
amplitude approach. In fact, we can be guided by the ampli-
tude approach in determining which operators must be re-                                              f k = f +k ei␻t + f −k e−i␻t .                共71d兲
tained. For example, 具ak␴22典 = ␳2k,2 = b2kb*2 and must be re-
tained, whereas 具a†k ␴典 = ␳2,1k = b2b1k
                                     *
                                        is of order ␹2 and can be           In terms of these variables, the polarizability ␣共␻兲 and ␤共␻兲,
neglected. In this way, we obtain a closed set of operator                  introduced in Secs. II and III, respectively, are given by
equations for the quantities                                                                        2d共s + r*兲                         共s + r*兲
                                                                                           ␣共␻兲 =              ;         ␤共␻兲 =                 .    共72兲
                                     f k = 具ak␴22典                 共68a兲                               E0                                 ␹
                                                †                              Using the trial solution in the original equations, one finds
                                 y kk⬘ = 具ak⬘ak␴典                  共68b兲
                                                                            steady-state equations
                                 zkk⬘ = 具ak⬘ak␴典                   共68c兲          0 = − i⌬s + i␹ − 关Cka+k − Ck共a−k 兲*兴 − 关Ck f +k − Ck共f −k 兲*兴
                                                                                                                                                    共73a兲
                                      ck = 具ak␴典                   共68d兲
                                            †
                                                                                  0 = i⌬共+兲r* − i␹ + 关Cka+k − Ck共a−k 兲*兴 + 关Ck f +k − Ck共f −k 兲*兴
                             xkk⬘k⬙ = 具ak⬙ak⬘ak␴22典                共68e兲
                                                                                                                                                    共73b兲
of the form
                                                                                             0 = − i共␻k − ␻ − i⑀兲a+k + Ck关s + r*兴                   共73c兲
                df k
                     = − i␻k f k + Ck⬘y k⬘k + Ck⬘zkk⬘ + Ck⬘y kk⬘
                dt
                                                                                               0 = i共␻k + ␻兲共a−k 兲* + Ck关s + r*兴                    共73d兲
                       − 2i␹ck cos ␻t + Ck具␴ 典          †
                                                                   共69a兲
                                                                                            0 = − i共␻k − ␻ − i⑀兲f +k − i␹ck + Ckr*                  共73e兲
       dy kk⬘                                               *
                = − i共␻0 + ␻k − ␻k⬘兲y kk⬘ + Ck⬙xkk⬙k⬘ − Ck⬙xk⬘k⬙k
         dt                                                                                    0 = i共␻k + ␻兲共f −k 兲* + i␹c*k + Cks                  共73f兲
                                   †
                   + Ck⬘ f k + Ck具ak⬘典                             共69b兲
                                                                                                                     iCk
                                                                                                         ck = −            .                        共73g兲
 dzkk⬘                                                                                                             ␻0 + ␻k
         = − i共␻0 + ␻k + ␻k⬘兲zkk⬘ − Ck具ak⬘典 + Ck⬘具ak典 − Ck⬙xkk⬘k⬙
  dt                                                                        The solution of these equations is now straightforward, with
                                                                   共69c兲                                       − iCk共s + r*兲
                                                                                                       a+k =                                        共74a兲
                                                                                                               ␻k − ␻ − i⑀
                                              Ck
                                ck = − i            ;              共69d兲
                                            ␻0 + ␻k                                                               iCk共s + r*兲
                                                                                                      共a−k 兲* =                                     共74b兲
                                                                                                                    ␻k + ␻
       dxkk⬘k⬙
                 = − i共␻k + ␻k⬘ − ␻k⬙兲xkk⬘k⬙ − Ck⬙zkk⬘ + Ck⬘y kk⬙           and
         dt
                    − C k y k⬘k⬙ ,                                 共69e兲            − i关Ck f +k − Ck共f −k 兲*兴 = ␹g共␻兲 − i␥−共␻兲r* − ⌬+共␻兲s, 共75兲

It can be shown that the contributions from the xkk⬘k⬙, zkk⬘,               where
and y kk⬙ terms are down by order of radiative shifts or widths                                   ␥ −共 ␻ 兲 ⌬ +共 ␻ 0兲 ⌬ +共 ␻ 0兲 − ⌬ +共 ␻ 兲
divided by ␻0, and therefore can be neglected, consistent                              g共␻兲 = i           −         −                                共76兲
with condition 共36a兲. Thus, the relevant equations are                                             ⌬共+兲     ⌬共+兲              ⌬

              df k                                                          and
                   = − i共␻k − i⑀兲f k − 2i␹ck cos ␻t + Ck具␴†典       共70a兲
              dt                                                                                   ␥−共␻兲 = ⌫−共␻兲 − i⌬−共␻兲.

                                                                      053816-9
BERMAN, BOYD, AND MILONNI                                                                       PHYSICAL REVIEW A 74, 053816 共2006兲

When these results are substituted into Eqs. 共73a兲 and 共73b兲,                        0 = i⌬共+兲r* − i␹ + g共␻兲共s + r*兲
one finds
                                                                                          − 2i关␹g共␻兲 − i␥−共␻兲r* − ⌬+共␻兲s兴,        共78兲
            0 = − i⌬s + i␹ − g共␻兲共s + r 兲
                                       *


                + 2i关␹g共␻兲 − i␥−共␻兲r* − ⌬+共␻兲s兴,             共77兲      which can be solved to give




                                ␤=
                                           冉
                                     2␻0 1 + 2
                                                 i⌫−共␻兲
                                                   ⌬ 共+兲 − 2
                                                             ⌬ +共 ␻ 0兲 − ⌬ −共 ␻ 兲
                                                                     ⌬ 共+兲        −2                    冊
                                                                                     ⌬ +共 ␻ 0兲 − ⌬ +共 ␻ 兲
                                                                                              ⌬
                                                                                                          .                       共79兲
                                                      共+兲
                                                  ⌬⌬ − 2␻关i⌫−共␻兲 + ⌬−共␻兲 − ⌬+共␻兲兴




Note that the last term in the numerator does not diverge as           nant and antiresonant components of the driving field, such
⌬ goes to zero owing to the definition 共8兲. Equation 共79兲              as that implied in an expression given by Sakurai 关2兴 共ne-
coincides exactly with the polarizability 共26兲 obtained in Sec.        glecting level shifts兲,
II, since ⌫+共␻兲 = 0 for ␻ ⬎ 0. Moreover, since all the fractions
                                                                                                          1      1
in the numerator are assumed to be small, we can move them                                    ␤1 =             + 共+兲              共81兲
to the denominator. In this way, using Eq. 共43兲, one obtains                                         ⌬ − i⌫−共␻兲 ⌬
                                                                       leads to a result,
                         2␻0
   ␤=   共+兲
      ⌬⌬ + 2␻0关− i⌫−共␻兲 − ⌬−共␻兲 − ⌬+共␻兲 + 2⌬+共␻0兲兴
                                                             共80兲
                                                                                                Im ␤1
                                                                                              ⌫−共␻兲兩␤1兩2
                                                                                                         ⬇     冉 冊
                                                                                                           2␻0 2
                                                                                                           ⌬共+兲
                                                                                                                 ,

                                                                       which is consistent with the optical theorem 关Im关␤兴
in agreement with the result of the amplitude approach 共64兲                                                                   2␻
if one sets 关⌬+共␻兲 − ⌬+共␻0兲兴 / ⌬ ⬇ 0, consistent with condi-           = ⌫−共␻兲 兩 ␤兩2兴 only near resonance, when 2␻0 / ⌬共+兲 = ␻0+0␻ ⬇ 1.
tions 共36b兲.                                                           In contrast, our expression 关Eq. 共80兲兴 共neglecting level shifts兲
    Thus, it appears that the validity conditions for the                                               2␻0/⌬共+兲
Heisenberg approach are that 共36a兲 holds and that the ratios                                 ␤=
in the numerator of Eq. 共79兲 are much less than unity. On the                                     ⌬ − i共2␻0/⌬+兲⌫−共␻兲
other hand, the Schrödinger approach is valid provided both            is consistent with the optical theorem for any atom-field de-
conditions 共36a兲 and 共36b兲 are satisfied. It can be shown that         tuning. Clearly, if one uses Eq. 共33兲 兵P = 2 ប ␻␹2 Im关␤兴其, for
Eq. 共80兲 agrees exactly with a perturbative solution of Eqs.           the energy absorbed from the field, the use of Eq. 共81兲 leads
共38兲 carried out to second order in the vacuum coupling.               to considerable errors for large detunings. For example, if
    There are two features of Eq. 共80兲 that merit some discus-         ⌬ / ␻0 = 1 / 2, ⌬共+兲 / ␻0 = 3 / 2, then
sion. First, we see that the excited state Lamb shift,
− ប ⌬−共␻0兲, that would enter the calculation is replaced by a                                                 ⌫ −共 ␻ 兲
                                                                                                   Im ␤1 ⬇
“Lamb shift” evaluated at ␻ rather than ␻0. In fact, ⌬−共␻兲                                                      ⌬2
must be viewed as a level shift resulting from the combined
dynamics of the applied and vacuum field. This result im-              while
plies that Lamb shifts associated with excited states must be
calculated within the context of a given problem. For ex-
ample, in spontaneous emission from an atom prepared in
                                                                                       Im ␤ ⬇            冉 冊
                                                                                                  ⌫ −共 ␻ 兲 2 ␻ 0 2 9 ⌫ −共 ␻ 兲
                                                                                                    ⌬2 ⌬共+兲
                                                                                                                  =
                                                                                                                    4 ⌬2
                                                                                                                              .

the excited state, ⌬−共␻0兲 is the relevant shift parameter asso-
ciated with the excited state 关16兴; however, in the case we
                                                                                          V. CONCLUDING REMARKS
consider here of an atom driven by an external field the rel-
evant parameter is ⌬−共␻兲. The frequency denominator in Eq.                The expression 共26兲 关or 共80兲兴 for the polarizability coin-
共80兲 contains the differences 关⌬−共␻兲 − ⌬+共␻0兲兴 and 关⌬−共−␻兲             cides, with one small difference, with that derived by Lou-
− ⌬+共␻0兲兴, which can be interpreted as the differences be-             don and Barnett 关12兴. The difference is that the factor in
tween the excited state level shifts associated with the reso-         large brackets in 共26兲 is missing a term −2C2k / 共␻k + ␻0兲2 that
nant and antiresonant components of the driving field, minus           appears in the Loudon-Barnett expression. In our approach,
the ground state Lamb shift. The ground state Lamb shift is            we have ignored terms of this order by consistently invoking
the only shift that is independent of the atom-field dynamics.         共36a兲 关17兴.
    The second point to note is that the use of an “intuitive”-           As noted in the Introduction, a TLA that remains with
type expression for the polarizability resulting from the reso-        high probability in its ground state is often approximated by

                                                               053816-10
POLARIZABILITY AND THE OPTICAL THEOREM FOR A…                                                     PHYSICAL REVIEW A 74, 053816 共2006兲

a harmonic, Lorentzian oscillator obtained by replacing ␴z                proximate 具␴22共t兲典 by 0 in the interaction of the atom with
everywhere by −1. The polarizability for this model is then               the applied field, but we cannot replace the operator ␴22共t兲
obtained using Eq. 共14兲, replacing ␴z by −1, and following                by 0 when it appears in operator-product expectation values,
exactly the same approach as in Sec. II except that no “fac-              such as 具ak共t兲␴22共t兲典. To first order in the external field am-
torization” approximations, such as 共15兲 or 共18兲, are needed              plitude, corrections to 具␴22共t兲典 = 0 are of order 共36a兲 共the ex-
because the model is now linear in 具␴共t兲典. One easily obtains             cited state population in the absence of any applied fields,
               2d2␻0             1                                        resulting solely from the vacuum field兲, whereas contribu-
      ␣共␻兲 =                                         , 共82兲               tions arising from f k = 具ak共t兲␴z共t兲典 关Eq. 共75兲兴 are of order
                 ប ␻0 − ␻ − 2i␻0关␥共−兲共␻兲 − i␦共+兲共␻兲兴
                     2   2
                                                                          ␥共␻兲 / ⌬共+兲共␻兲 and must be included. As noted previously,
with ␥共−兲共␻兲 = ⌫−共␻兲 − ⌫+共␻兲 and ␦共+兲共␻兲 = ⌬−共␻兲 + ⌬+共␻兲. Al-             具ak␴22典 = ␳2k,2 = b2kb*2; this expectation value arises from in-
though this expression satisfies the optical theorem, it has the          terference between processes associated with the excitation
unphysical feature that the radiative frequency shift ␦共+兲共␻兲             of the atom by the external field and the antiresonant com-
involves the sum of the radiative level shifts. The radiative             ponent of the vacuum field.
frequency shift ␦共␻兲 in the polarizability 共26兲, on the other
hand, involves the expected difference in the two radiative                                     ACKNOWLEDGMENTS
level shifts. This point explains one of the reasons for includ-
ing the radiative shifts in our calculations, even though, as                We thank S. M. Barnett and R. Loudon for sharing their
noted earlier, these shifts cannot be properly renormalized in            insights on this problem and for providing us with a preprint
a two-level model to obtain physically meaningful Lamb                    of their paper. We also thank G. W. Ford and J. E. Sipe for
shifts.                                                                   brief but helpful remarks relating to this work. This research
    The familiar Lorentzian oscillator approximation to a                 is supported in part by the National Science Foundation
TLA therefore fails to provide a physically satisfactory ex-              through Grants No. PHY0244841 and No. ECS-0355206,
pression for the polarizability, even when the TLA has neg-               and the FOCUS Grant, and by the US Army Research Office
ligible excitation probability. The reason for this is clear              through a MURI grant, and by the Michigan Center for The-
from Eq. 共14兲: for a TLA near its ground state, we can ap-                oretical Physics.




 关1兴 H. A. Kramers and W. Heisenberg, Zeits. f. Physik. 31, 681            关9兴 P. W. Milonni and R. W. Boyd, Phys. Rev. A 69, 023814
     共1925兲. An English translation of this paper, and a discussion            共2004兲. There is a typographical error in Eq. 共25兲: V in that
     of its importance in the development of quantum theory, may               equation should be replaced by −V.
     be found in B. L. van der Waerden, Sources of Quantum Me-            关10兴 See, for instance, P. W. Milonni, The Quantum Vacuum: An
     chanics 共Dover, New York, 1968兲.                                          Introduction to Quantum Electrodynamics 共Academic, San Di-
 关2兴 See, for instance, J. J. Sakurai, Advanced Quantum Mechanics
                                                                               ego, 1994兲.
     共Addison-Wesley, Reading, MA, 1976兲, Eq. 共2.188兲. Sakurai
                                                                          关11兴 Equation 共12兲 follows directly from Eqs. 共25兲 and 共26兲 of MB
     notes that the optical theorem is exact, but that his expression
     for the scattering amplitude is perturbative and satisfies the            when the approximation noted after Eq. 共26兲 is not made.
     optical theorem only in the vicinity of resonance.                   关12兴 R. Loudon and S. M. Barnett, J. Phys. B 39, S555 共2006兲.
 关3兴 See, for instance, D. L. Andrews, S. Naguleswaran, and G. E.         关13兴 See, for example, P. R. Berman and B. Dubetsky, Phys. Rev. A
     Stedman, Phys. Rev. A 57, 4925 共1998兲; G. E. Stedman, S.                   55, 4060 共1997兲, and references therein.
     Naguleswaran, D. L. Andrews, and L. C. Dávila Romero, ibid.          关14兴 The level shifts do not include light shifts, proportional to the
      63, 047801 共2001兲; D. L. Andrews, L. C. Dávila Romero, and               intensity of the external field, which are neglected in this work.
     G. E. Stedman, ibid. 67, 055801 共2003兲.                              关15兴 The upper- and lower-state energy levels are now taken to be
                                                                                                                         1
 关4兴 See for instance, A. D. Buckingham and P. Fischer, Phys. Rev.             ប␻0 and 0, respectively, rather than ± 2 ប ␻0 as implied by the
     A 61, 035801 共2000兲; Phys. Rev. A 63, 047802 共 c4 c4a c4b                 Hamiltonian 共13兲.
     c4cR. W. Boyd, Nonlinear Optics, 2nd ed. 共Academic Press,            关16兴 G. S. Agarwal, Phys. Rev. A 7, 1195 共1973兲.
     New York, 158.                                                       关17兴 It might be worth noting, however, that we can obtain a result
 关5兴 The relevance of the damping terms to the question of the                 in exact agreement with Loudon and Barnett Ref. 关12兴 关an
     existence of a linear electro-optic effect in isotropic chiral me-        extra term equal to −2C2k / 共␻k + ␻0兲2 in the bracketed factor of
     dia is discussed by R. W. Boyd, J. E. Sipe, and P. W. Milonni,            共26兲兴, if we turn on the vacuum field adiabatically and keep
     J. Opt. A, Pure Appl. Opt. 6, S14 共2004兲.                                 terms of this order. In effect, this extra term would correspond
 关6兴 G. S. Agarwal and R. W. Boyd, Phys. Rev. A 67, 043821                     to the fact that there is a population difference between the
     共2003兲.                                                                   “bare” ground and excited states when these states are dressed
 关7兴 D. A. Long, The Raman Effect 共Wiley, New York, 2001兲.                     by the vacuum field. By neglecting terms of this order, we
 关8兴 See, for instance, J. D. Jackson, Classical Electrodynamics               avoid corrections related to nonvanishing excited state popula-
     共Wiley, New York, 1975兲, p. 423.                                          tions in the absence of any external field.



                                                                   053816-11
