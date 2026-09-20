# Dynamical Quantum Phase Transitions in Spin Chains with Long-Range Interactions: Merging Different Concepts of Nonequilibrium Criticality - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevLett.120.130601
> Collected: 2026-09-20
> Published: 2018-03-27
> Zotero parent key: 8ZEF3CJ7
> Evidence: Publisher or author-preprint PDF

PHYSICAL REVIEW LETTERS 120, 130601 (2018)



     Dynamical Quantum Phase Transitions in Spin Chains with Long-Range Interactions:
                 Merging Different Concepts of Nonequilibrium Criticality
                        Bojan Žunkovič,1 Markus Heyl,2,3 Michael Knap,2 and Alessandro Silva1
                   1
                    SISSA—International School for Advanced Studies, via Bonomea 265, 34136 Trieste, Italy
                       2
                        Department of Physics, Walter Schottky Institute, and Institute for Advanced Study,
                                  Technical University of Munich, 85748 Garching, Germany
                         3
                           Max-Planck-Institut für Physik komplexer Systeme, 01187 Dresden, Germany

                 (Received 27 September 2016; revised manuscript received 8 May 2017; published 27 March 2018)

                We theoretically study the dynamics of a transverse-field Ising chain with power-law decaying
             interactions characterized by an exponent α, which can be experimentally realized in ion traps. We focus on
             two classes of emergent dynamical critical phenomena following a quantum quench from a ferromagnetic
             initial state: The first one manifests in the time-averaged order parameter, which vanishes at a critical
             transverse field. We argue that such a transition occurs only for long-range interactions α ≤ 2. The second
             class corresponds to the emergence of time-periodic singularities in the return probability to the ground-
             state manifold which is obtained for all values of α and agrees with the order parameter transition for
             α ≤ 2. We characterize how the two classes of nonequilibrium criticality correspond to each other and give
             a physical interpretation based on the symmetry of the time-evolved quantum states.

             DOI: 10.1103/PhysRevLett.120.130601



   Recent experiments with cold atoms [1–9] and trapped             state only when crossing the DQPT-LO but ceases to do so
ions [10–13] have realized nonequilibrium quantum states            for quenches within the same dynamical phase.
with exotic properties that cannot be captured by a                    Model and protocol.—Long-range systems exhibit many
thermodynamic equilibrium description. This includes                interesting properties that have been extensively studied in
the observation of prethermalization [1–3,11] and many-
body localization [5–10]. Despite these remarkable
discoveries, it is still a major challenge to reveal universal
properties of nonequilibrium quantum states. One possible
approach for developing a general understanding of
far-from-equilibrium dynamics is to explore concepts of
nonequilibrium critical phenomena. However, due to the
lack of clear generic principles, different concepts of
dynamical criticality have been introduced [14–22].
   In this work, we show that two seemingly unrelated
nonequilibrium critical phenomena are actually intimately
connected. In particular, the first class of nonequilibrium
criticality describes dynamical quantum phase transitions           FIG. 1. wDynamical phase diagram. We study the quantum
(DQPTs) in the asymptotic late-time steady state of an              dynamics of an Ising chain with power-law decaying interactions
order parameter (DQPT-OP) that is finite in one dynamical           by preparing the system in a fully polarized state and abruptly
phase but vanishes in the other [14,19]. The second class is        switching on a finite transverse field hf . We identify the DQPT
DQPTs associated with singular behavior in the transient            through two mechanisms: One introduces an order parameter
real-time evolution of Loschmidt echoes (DQPT-LO)                   (DQPT-OP) that is finite only in the dynamical ferromagnetic
[22,23]. By studying the quantum dynamics of an initially           phase, whereas the other is based on nonanalytic kinks in the
fully polarized state in a transverse-field Ising chain with        Loschmidt rate function (DQPT-LO) that only arise for quenches
                                                                    across the transition. When the interaction exponent α < 2, the
power-law decaying interactions, we show that these two
                                                                    DQPT occurs simultaneously for both cases along the red line,
types of DQPTs are related in several ways: First, they             separating the dynamical ferromagnetic (I) and the dynamical
predict consistent values for the dynamical critical point;         paramagnetic (III) phase. We argue that for α > 2 the system does
see Fig. 1. Second, the singularities in the Loschmidt echo         not establish a finite order parameter and thus the DQPT-OP ends
are related to 0’s in the time evolution of the order               at α ¼ 2. Yet, the DQPT-LO persists for arbitrarily large α (dashed
parameter. Third, we argue that the dynamics restores               line) separating two dynamical phases characterized by a mono-
the symmetry breaking imprinted by the initial polarized            tonic decay (II) and an oscillating decay (III) of the magnetization.


0031-9007=18=120(13)=130601(6)                               130601-1                         © 2018 American Physical Society
                                      PHYSICAL REVIEW LETTERS 120, 130601 (2018)

the past [24–31]. Experimentally, the real-time dynamics of                  For α > 0 the dynamics is not exactly solvable.
long-range interacting spin chains in a transverse field can              Therefore, we compute the time evolution numerically
be explored with trapped ions [10,12,32–35] where power-                  using a recently developed algorithm based on a time-
law decaying interactions between the effective spins with                dependent variational principle applied to matrix product
exponents 0 ≤ α ≤ 3 are mediated by collective vibrations                 states [47,48]. All presented data are evaluated for bond
of the underlying ionic crystal [36]. The corresponding                   dimension 100 and time step 0.02=J. We demonstrate the
Hamiltonian is                                                            convergence of our data with the bond dimension in
                                                                          Supplemental Material [49].
                     X
                     N                               X
                                                     N
                                                                             For sufficiently small exponent α, we find that the order
         ĤðhÞ ¼ −           Vði − jÞσ xi σ xj − h         σ zj ;   ð1Þ   parameter σ x ðtÞ remains finite within the dynamical ferro-
                     i≠j¼1                           j¼1
                                                                          magnetic phase hf < hc , whereas it approaches 0 with
with the transverse field h and the interaction potential                 damped oscillations within the dynamical paramagnetic
VðxÞ ¼ JvðxÞ=NðαÞ. Here, vðxÞ ¼ jxj−α describes the                       phase hf > hc ; see Fig. 2(a) for α ¼ 1.5. In this regime,
power-law decaying interactions and J sets the interaction                we find that the order parameter increases with system size
strength. We added a normalization constant NðαÞ ¼                        for hf < hc supporting its robustness in the thermodynamic
             P                                                            limit. When increasing α further σ x ðtÞ relaxes to 0 regardless
½1=ðN − 1Þ Ni≠j¼1 vði − jÞ that ensures the intensive scal-
                                                                          of the final transverse field hf ; see Fig. 2(b) for α ¼ 3. In that
ing of the energy density for any α. For all values of α, this
model is known to display an equilibrium quantum phase                    regime the order parameter decays with increasing system
transition from a ferromagnet to a paramagnet. At finite                  size, indicating its approach to 0 in the thermodynamic limit.
temperatures, the equilibrium ferromagnetic phase is in one                  Dynamical transition in the order parameter.—In the
dimension only stable for α ≤ 2 [37,38].                                  following we focus on the order parameter σ x obtained
   We are studying the quantum dynamics following a
global quantum quench in the transverse field h. To this
end, we initially prepare the system in the fully polarized                          (a)
state jþi ¼ j → … →i and then monitor the ensuing
real-time dynamics governed by the Hamiltonian Ĥðhf Þ.
   Time evolution of the order parameter.—The first class
of dynamical criticality, DQPT-OP, occurs in the long-time
asymptotics of a dynamical order parameter, which is finite
for quenches within the ordered phase hf < hc and 0 for
quenches across the dynamical transition hf > hc . For our
model the order parameter is the time-averaged longi-
tudinal magnetization
                                Z                                                    (b)
                               1 T
                 σ x ¼ lim          dtσ x ðtÞ;             ð2Þ
                        T→þ∞ T 0

                                                       P
with σ β ðtÞ ¼ hSβ ðtÞi (β ¼ x, y, z) and Sβ ¼ 1=N i σ βi
denoting the collective spin operators.
   DQPT-OPs have been studied extensively in various
integrable quantum many-body systems displaying non-
thermal long-time dynamics, such as BCS models [14],
models with infinite-range interactions [19,39–44], and
field theories in high dimensions [44,45]. An analytically
tractable regime of our model is the infinite-range limit,
α ¼ 0. There, the dynamics of the order parameter corre-                  FIG. 2. Time evolving the order parameter. (a) For α ¼ 1.5 and
sponds to the precession of a single collective spin Sβ ,                 hf ¼ 0.7J the order parameter σ x ðtÞ approaches a finite value,
implying that σ x ðtÞ oscillates persistently in time with a              describing a dynamical symmetry-broken state with ferromag-
                                                                          netic order, whereas it decays to 0 with strong oscillations for
single frequency around a mean value set by σ x. Initializing             quenches to hf ¼ 1.5J. (b) Even though for shorter-ranged
the system in the ferromagnetic ground state, hi < hc , a                 interactions α ¼ 3 the order parameter reaches 0 for all values
DQPT-OP can occur, characterized by an order parameter                    of hf , the nature of the decay is very different: For small fields
σ x that remains finite for hf < hc but is 0 for hf > hc. For             hf ¼ 0.7J it decays with a timescale much longer than the
α ¼ 0, the critical value of the field h can be computed                  microscopic scales, whereas for large fields hf ¼ 1.5J it oscil-
analytically, hc ¼ J þ hi =2 [43,46].                                     lates around 0 and decays rapidly.


                                                                    130601-2
                                       PHYSICAL REVIEW LETTERS 120, 130601 (2018)

from our numerical data by integrating σ x ðtÞ over a time                 In the limit of the nearest-neighbor Ising model, α ¼ ∞,
window of 5=J around half of the first finite-size recurrence           it is well established that σ x ¼ 0 for all hf > 0 [50].
time, which scales approximately linearly with system size              Constructing perturbatively a generalized Gibbs ensemble
[49]. The order parameter σ x displays the same qualitative             around this point [51] suggests the absence of a steady-state
crossover in finite-size systems: a monotonic decrease of σ x           transition also in the vicinity of α ¼ ∞ [49]. Our numerics
from 1 to 0 as the final transverse field hf is increased; see          provides strong evidence that the dynamical phase tran-
Fig. 3. Analyzing the finite-size flow we, however, observe             sition is absent for all α > 2. We estimate α ¼ 2 as an upper
a markedly different behavior when tuning the value of α.               bound for the DQPT-OP, in analogy to the equilibrium
At small α and moderate fields hf ≲ J, Figs. 3(a) and 3(b),             finite-temperature transition that can only occur for α < 2.
our numerics indicate that σ x increases with system size N             However, we also find a crossover region 2 ≤ α ≲ 2.4
and the finite-size flow suggests a critical point close to             where the finite-size flow of our simulations is not fully
hc ≈ J in the thermodynamic limit. By contrast, for large α,            indicative [49].
Fig. 3(c), the order parameter σ x rapidly vanishes with                   In a recent work, a different interpretation has been
increasing system size, suggesting the absence of a tran-               proposed for α > 2: Based on extrapolating transient
sition. A finite-size scaling analysis of the dynamical                 dynamics (tJ < 10) of the order parameter to infinite times,
transition would require a two-parameter scaling, which                 a prethermal ordered phase has been conjectured to exist for
depends both on the system size and on time. In addition                all values of α [52]. This approach is, however, inconsistent
the dynamical critical point is not known for our system.               with the arguments for the absence of a DPQT-OP near
Because of our limited amount of data, such an analysis is              α ¼ ∞ and might be explained by the fact that the error of
therefore not feasible. However, it would be a direction for            the extrapolation procedure cannot be estimated in an
future research.                                                        unbiased way, unless the functional form of the decay
   One might expect that our model is not integrable and                (or at least the timescales involved) is known.
hence thermalizes for any α ∈ ð0; ∞Þ, which would turn the                 Dynamical transition in the Loschmidt echo.—The
                                                                        second class of dynamical transitions we consider is
DQPT-OP into a conventional thermal transition. We argue
                                                                        DQPT-LOs, which arise as singularities in Loschmidt
that this is not the case. To this end, we first consider the           amplitudes GðtÞ ¼ hΨj exp½−iHðhf ÞtjΨi as a function of
integrable point α ¼ 0. In that limit, we find that the
                                      pﬃﬃ                               time [22], where jΨi denotes the initial state. Formally,
thermal transition occurs at hthc ¼     2J, which is signifi-           Loschmidt amplitudes at imaginary times resemble equi-
cantly larger than the critical field of the dynamical                  librium boundary partition functions [22,53,54]. Therefore,
transition hc ¼ J [49]. For small α ¼ 0.1 our numerical                 it is suitable to introduce a dynamical counterpart of the
data suggest that the DQPT is also located at hc ≈ J; see               free energy density, which is the Loschmidt rate function
Fig. 3(a). Assuming now that the critical field of the thermal          (or large deviation function [54]) gðtÞ ¼ −N −1 log½GðtÞ.
transition changes only perturbatively for weak α, our                  Similarly to equilibrium free energies being nonanalytic at
numerical evidence for hc ≈ J is inconsistent with the                  conventional phase transitions, the Loschmidt rate function
transition being thermal also for α ¼ 0.1. Determining                  gðtÞ can display nonanalyticities, which define the DQPT-
the value of α at which the system starts to thermalize                 LO. Such DQPT-LOs have been studied in different models
remains a challenging open question.                                    [22,23,55–70] and measured in recent experiments [67,71].


                                 (a)                                            (b)                                              (c)




FIG. 3. Dynamical phase diagram of the order parameter. We estimate the asymptotic value of the order parameter σ¯x as a function of
the quenched transverse field hf for different system sizes N and interaction exponents (a) α ¼ 0.1, (b) α ¼ 1.5, and (c) α ¼ 3. For both
values of α < 2 we find that the finite-size flow of the order parameter indicates a DQPT-OP with the critical point hc ∼ J. For very long-
ranged interactions, (a), the order parameter σ x approaches the mean-field predictions, α ¼ 0 (dashed lines), with increasing system size.
By contrast, for relatively short-ranged interactions (c) α ¼ 3, the finite-size flow suggests that the order parameter σ¯x flows toward 0 in
the thermodynamic limit for all values of the transverse field.


                                                                130601-3
                                     PHYSICAL REVIEW LETTERS 120, 130601 (2018)

   The Loschmidt amplitude is not uniquely defined when              (a)
the ground-state manifold of the initial Hamiltonian is
degenerate. In order to maintain the connection of DQPT-
LOs to macroscopic observables and therefore potentially
to DQPT-OPs, the proper generalization is the probability
to stay in the ground-state manifold [23],
                  X
          PðtÞ ¼     jhΨn ðhi Þje−iHðhf Þt jΨ0 ðhi Þij2 ; ð3Þ
                    n                                                (b)

which reduces to the Loschmidt echo LðtÞ ¼ jGðtÞj2 in the
limit of a single ground state. Here, fjΨn ðhi Þig denotes the
degenerate states at hi and jΨ0 ðhi Þi is the chosen initial
condition. In our case we have that jΨ0 ðhi Þi ¼ jþi and
jΨ1 ðhi Þi ¼ j−i ¼ j ← … ←i. Consequently, we obtain
PðtÞ ¼ Pþ ðtÞ þ P− ðtÞ with Pþ ðtÞ ¼ jhþj þ ðtÞij2 and
P− ðtÞ ¼ jh−j þ ðtÞij2 . After our work appeared, the
Loschmidt echo LðtÞ itself was also computed for the
long-range Ising model [72–74].                                      FIG. 4. Dynamical quantum phase transitions in the Loschmidt
                                                                     echo. We compute an extension of the Loschmidt echo, which is
    Merging the different concepts of DQPT.—Let us now
                                                                     the return probability to the degenerate ground-state manifold,
establish the connection between the two concepts of                 Eq. (3), for different values of the transverse field hf and
dynamical criticality. For this purpose we first consider            interaction exponent (a) α ¼ 1.8 and (b) α ¼ 2.5. We observe
the limit of α ¼ 0 where the dynamics is described by                nonanalyticities in the associated rate function λðtÞ for arbitrary
semiclassical Bloch equations for the collective spin                values of the interaction exponent α, provided the final transverse
⃗σ ðtÞ ¼ fσ x ðtÞ; σ y ðtÞ; σ z ðtÞg. In that case, the individual   field hf is sufficiently large. The insets compare the typical rate of
probabilities P ðtÞ ¼ exp½−Nλ ðtÞ with λ ðtÞ ¼                   kinks in λðtÞ, solid line, with the zero crossings of the order
− log½ð1  ⃗σ ðtÞ · ⃗σ ð0ÞÞ=2 exhibit a particularly illustrative   parameter σ x ðtÞ. The right panels show the evolution of the
form: for the fully polarized state, ⃗σ ðtÞ · ⃗σ ð0Þ measures the    magnetization ⃗σ ðtÞ projected onto the xy plane of the Bloch
projection of ⃗σ ðtÞ onto the x axis [75].                           sphere. When quenching across the dynamical transition, the
    DQPT-LOs can occur in PðtÞ because the individual                magnetization spreads over both hemispheres (black curves)
                                                                     whereas it remains located on one hemisphere for quenches
probabilities P ðtÞ ¼ exp½−Nλ ðtÞ show an exponential
                                                                     within the same dynamical phase (blue and red curves), indicating
dependence on system size N. Therefore, in the thermo-               a bifurcation of the dynamics.
dynamic limit only one of the two dominates such that
PðtÞ ¼ exp½−NλðtÞ with λðtÞ ¼ minη¼ λη ðtÞ [23]. While
at short times λðtÞ ¼ λþ ðtÞ due to the initial condition,           successive kinks in λðtÞ and successive 0’s in σ x ðtÞ,
λ− ðtÞ can take over at a critical time, which leads to a kink       respectively. Specifically, we plot in the insets of Fig. 4
in λðtÞ. For the concrete case of α ¼ 0 this can be traced           the inverse of this timescale and find within the error bars,
back to ⃗σ ðtÞ crossing the equator of the Bloch sphere,             which denote the standard error of the mean, good agree-
σ x ¼ 0, because then λþ ¼ λ− . As we have seen in Fig. 2,           ment over a wide range of hf , supporting the close
this can happen only when the DQPT-OP is crossed, i.e.,              connection of σ x ðtÞ and DQPT-LOs for generic values of
for hf > hc. Therefore, a DQPT-LO occurs only when                   α. The precise location of the 0’s in σ x ðtÞ exhibits a small,
crossing the DQPT-OP, which manifests itself in a vanish-            essentially constant shift compared to the kinks in λðtÞ
ing long-time magnetization σ¯x ¼ 0. In this way the Z2              [22,23]. This is illustrated in the Bloch spheres of Fig. 4,
symmetry, broken explicitly by the initial state, is restored        where the kinks (black dots) appear slightly later in time
in the long-time limit as well as at the critical times at which     than the zero crossings of the order parameter σ x ¼ 0.
the DQPT-LO occur.                                                   Moreover, we emphasize that the connection between
    Although these considerations address a fine-tuned limit         DQPT-LOs and the 0’s of σ x ðtÞ is also valid for α > 2
of α ¼ 0, we show in Fig. 4 based on our numerical data              where no DQPT-OP occurs. The field hc marking the
that the relation between DQPT-LO and DQPT-OP is                     appearance of DQPT-LOs for hf > hc then separates a
robust and extends to α > 0. DQPT-LOs in the form of                 regime of monotonic decay of σ x for hf < hc from
kinks occur whenever the system is quenched sufficiently             oscillatory decay for hf > hc ; see Fig. 4(b).
strongly such that hf > hc whereas for hf < hc the rate                 Conclusions and outlook.—We have studied dynamical
function λðtÞ stays smooth. In addition we compare the               quantum phase transition in a transverse-field Ising chain
period of the kinks ðτLE Þ with the period of the 0’s of σ x ðtÞ     with power-law decaying interactions. We have argued that
(τOP ), which are obtained by the distance between                   two seemingly different concepts of nonequilibrium


                                                               130601-4
                                    PHYSICAL REVIEW LETTERS 120, 130601 (2018)

criticality, specifically dynamical transitions in the order         [9] P. Bordia, H. Lüschen, S. Scherg, S. Gopalakrishnan, M.
parameter and dynamical transitions in the Loschmidt echo,               Knap, U. Schneider, and I. Bloch, Phys. Rev. X 7, 041047
are actually intimately related in the following ways. (i) We            (2017).
find that both of them predict consistent values for the            [10] J. Smith, A. Lee, P. Richerme, B. Neyenhuis, P. W. Hess,
dynamical critical point for interaction exponent α < 2.                 P. Hauke, M. Heyl, D. A. Huse, and C. Monroe, Nat. Phys.
                                                                         12, 907 (2016).
(ii) For generic values of α, the period of kinks in the
                                                                    [11] B. Neyenhuis, J. Zhang, P. W. Hess, J. Smith, A. C. Lee, P.
Loschmidt rate function agrees with the period of 0’s in the             Richerme, Z.-X. Gong, A. V. Gorshkov, and C. Monroe, Sci.
order parameter. (iii) The order parameter restores sym-                 Adv. 3, e1700672 (2017).
metry imprinted by the initial polarized state, only for            [12] E. A. Martinez, C. A. Muschik, P. Schindler, D. Nigg, A.
quenches across the dynamical quantum phase transition,                  Erhard, M. Heyl, P. Hauke, M. Dalmonte, T. Monz, P. Zoller
but ceases to do so for quenches within the same dynami-                 et al., Nature (London) 534, 516 (2016).
cal phase.                                                          [13] J. Zhang, G. Pagano, P. W. Hess, A. Kyprianidis, P. Becker,
   In future studies, it would be interesting to extract the             H. Kaplan, A. V. Gorshkov, Z.-X. Gong, and C. Monroe,
dynamical critical exponents of the order parameter.                     Nature (London) 551, 601 (2017).
Furthermore, studying in detail the scaling of order                [14] E. A. Yuzbashyan, O. Tsyplyatyev, and B. L. Altshuler,
parameter fluctuations with system size could establish                  Phys. Rev. Lett. 96, 097005 (2006).
for which values of the interaction exponent our system is          [15] S. Diehl, A. Micheli, A. Kantian, B. Kraus, H. P. Buechler,
                                                                         and P. Zoller, Nat. Phys. 4, 878 (2008).
thermalizing according to the eigenstate thermalization
                                                                    [16] P. Barmettler, M. Punk, V. Gritsev, E. Demler, and E.
hypothesis.
                                                                         Altman, Phys. Rev. Lett. 102, 130603 (2009).
   We acknowledge support from the Technical University             [17] M. Eckstein, M. Kollar, and P. Werner, Phys. Rev. Lett. 103,
of Munich—Institute for Advanced Study, funded by the                    056403 (2009).
German Excellence Initiative and the European Union FP7             [18] S. Diehl, A. Tomadin, A. Micheli, R. Fazio, and P. Zoller,
                                                                         Phys. Rev. Lett. 105, 015702 (2010).
under Grant No. 291763, the Deutsche Akademie der
                                                                    [19] B. Sciolla and G. Biroli, Phys. Rev. Lett. 105, 220401
Naturforscher Leopoldina under Grant No. LPDR 2015-                      (2010).
01, and by the Deutsche Forschungsgemeinschaft via                  [20] J. P. Garrahan and I. Lesanovsky, Phys. Rev. Lett. 104,
the Gottfried Wilhelm Leibniz Prize program. B. Z.                       160601 (2010).
was supported by the ERC under starting Grant                       [21] A. Mitra, Phys. Rev. Lett. 109, 260601 (2012).
No. 279391 EDEQS.                                                   [22] M. Heyl, A. Polkovnikov, and S. Kehrein, Phys. Rev. Lett.
                                                                         110, 135704 (2013).
Note added.—During the review process of our work,                  [23] M. Heyl, Phys. Rev. Lett. 113, 205701 (2014).
recent experiments observed some of our findings on                 [24] F. J. Dyson, Commun. Math. Phys. 12, 91 (1969).
DQPT in the order parameter [13] and the Loschmidt                  [25] F. J. Dyson, E. H. Lieb, and B. Simon, in Statistical
                                                                         Mechanics (Springer, New York, 1978), pp. 163–211.
echo [71].
                                                                    [26] M. E. Fisher, S.-k. Ma, and B. G. Nickel, Phys. Rev. Lett.
                                                                         29, 917 (1972).
                                                                    [27] E. Luijten and H. W. J. Blöte, Phys. Rev. B 56, 8945 (1997).
 [1] S. Hofferberth, I. Lesanovsky, B. Fischer, T. Schumm, and J.   [28] D. Mukamel, S. Ruffo, and N. Schreiber, Phys. Rev. Lett.
     Schmiedmayer, Nature (London) 449, 324 (2007).                      95, 240604 (2005).
 [2] M. Gring, M. Kuhnert, T. Langen, T. Kitagawa, B. Rauer,        [29] J. Barré, D. Mukamel, and S. Ruffo, Phys. Rev. Lett. 87,
     M. Schreitl, I. Mazets, D. A. Smith, E. Demler, and                 030601 (2001).
     J. Schmiedmayer, Science 337, 1318 (2012).                     [30] T. Dauxois, S. Ruffo, E. Arimondo, and M. Wilkens,
 [3] T. Langen, R. Geiger, M. Kuhnert, B. Rauer, and                     Lecture Notes in Physics (Springer, New York, Berlin,
     J. Schmiedmayer, Nat. Phys. 9, 640 (2013).                          2002), pp. 1–22.
 [4] S. Hild, T. Fukuhara, P. Schauss, J. Zeiher, M. Knap, E.       [31] A. Campa, T. Dauxois, D. Fanelli, and S. Ruffo, Physics of
     Demler, I. Bloch, and C. Gross, Phys. Rev. Lett. 113,               Long-Range Interacting Systems (Oxford University Press,
     147205 (2014).                                                      Oxford, 2014).
 [5] M. Schreiber, S. S. Hodgman, P. Bordia, H. P. Lschen, M. H.    [32] B. P. Lanyon, C. Hempel, D. Nigg, M. Mueller, R.
     Fischer, R. Vosk, E. Altman, U. Schneider, and I. Bloch,            Gerritsma, F. Zaehringer, P. Schindler, J. T. Barreiro, M.
     Science 349, 842 (2015).                                            Rambach, G. Kirchmair et al., Science 334, 57 (2011).
 [6] P. Bordia, H. P. Luschen, S. S. Hodgman, M. Schreiber, I.      [33] J. W. Britton, B. C. Sawyer, A. C. Keith, C. C. J. Wang, J. K.
     Bloch, and U. Schneider, Phys. Rev. Lett. 116, 140401               Freericks, H. Uys, M. J. Biercuk, and J. J. Bollinger, Nature
     (2016).                                                             (London) 484, 489 (2012).
 [7] J. yoon Choi, S. Hild, J. Zeiher, P. Schau, A. Rubio-Abadal,   [34] P. Jurcevic, B. P. Lanyon, P. Hauke, C. Hempel, P. Zoller, R.
     T. Yefsah, V. Khemani, D. A. Huse, I. Bloch, and C. Gross,          Blatt, and C. F. Roos, Nature (London) 511, 202 (2014).
     Science 352, 1547 (2016).                                      [35] P. Richerme, Z.-X. Gong, A. Lee, C. Senko, J. Smith, M.
 [8] P. Bordia, H. Lüschen, U. Schneider, M. Knap, and I. Bloch,         Foss-Feig, S. Michalakis, A. V. Gorshkov, and C. Monroe,
     Nat. Phys. 13, 460 (2017).                                          Nature (London) 511, 198 (2014).


                                                              130601-5
                                      PHYSICAL REVIEW LETTERS 120, 130601 (2018)

[36] R. Islam, C. Senko, W. C. Campbell, S. Korenblit, J. Smith,       [54] A. Gambassi and A. Silva, Phys. Rev. Lett. 109, 250602
     A. Lee, E. E. Edwards, C. C. J. Wang, J. K. Freericks, and             (2012).
     C. Monroe, Science 340, 583 (2013).                               [55] F. Pollmann, S. Mukerjee, A. G. Green, and J. E. Moore,
[37] A. Dutta and J. K. Bhattacharjee, Phys. Rev. B 64, 184106              Phys. Rev. E 81, 020101 (2010).
     (2001).                                                           [56] C. Karrasch and D. Schuricht, Phys. Rev. B 87, 195104
[38] M. Knap, A. Kantian, T. Giamarchi, I. Bloch, M. D. Lukin,              (2013).
     and E. Demler, Phys. Rev. Lett. 111, 147205 (2013).               [57] F. Andraschko and J. Sirker, Phys. Rev. B 89, 125120
[39] M. Eckstein, M. Kollar, and P. Werner, Phys. Rev. B 81,                (2014).
     115131 (2010).                                                    [58] J. N. Kriel, C. Karrasch, and S. Kehrein, Phys. Rev. B 90,
[40] S. A. Hamerla and G. S. Uhrig, Phys. Rev. B 87, 064304                 125106 (2014).
     (2013).                                                           [59] E. Canovi, P. Werner, and M. Eckstein, Phys. Rev. Lett. 113,
[41] M. Schiro and M. Fabrizio, Phys. Rev. Lett. 105, 076401                265702 (2014).
     (2010).                                                           [60] M. Schmitt and S. Kehrein, Phys. Rev. B 92, 075114 (2015).
[42] A. Gambassi and P. Calabrese, Europhys. Lett. 95, 6 (2010).       [61] S. Vajna and B. Dora, Phys. Rev. B 89, 161105 (2014).
[43] B. Sciolla and G. Biroli, J. Stat. Mech. Theor. Exper. 11,        [62] S. Vajna and B. Dora, Phys. Rev. B 91, 155127 (2015).
     P11003 (2011).                                                    [63] N. O. Abeling and S. Kehrein, Phys. Rev. B 93, 104302
[44] B. Sciolla and G. Biroli, Phys. Rev. B 88, 201110                      (2016).
     (2013).                                                           [64] J. C. Budich and M. Heyl, Phys. Rev. B 93, 085416 (2016).
[45] P. Smacchia, M. Knap, E. Demler, and A. Silva, Phys. Rev.         [65] S. Sharma, S. Suzuki, and A. Dutta, Phys. Rev. B 92,
     B 91, 205136 (2015).                                                   104306 (2015).
[46] B. Žunkovič, A. Silva, and M. Fabrizio, Phil. Trans. R. Soc.      [66] Z. Huang and A. V. Balatsky, Phys. Rev. Lett. 117, 086802
     A 374, 20150160 (2016).                                                (2016).
[47] J. Haegeman, J. I. Cirac, T. J. Osborne, I. Pizorn, H.            [67] F. N., V. D., T. M., R. B. S., L. D.-S., H. M., B. J. C., M. L.,
     Verschelde, and F. Verstraete, Phys. Rev. Lett. 107,                   S. K., and W. C., Nat. Phys. 1 (2017).
     070601 (2011).                                                    [68] M. Heyl, Phys. Rev. Lett. 115, 140602 (2015).
[48] J. Haegeman, C. Lubich, I. Oseledets, B. Vandereycken, and        [69] M. Heyl, Phys. Rev. B 95, 060504 (2017).
     F. Verstraete, Phys. Rev. B 94, 165116 (2016).                    [70] S. A. Weidinger, M. Heyl, A. Silva, and M. Knap, Phys.
[49] See Supplemental Material at http://link.aps.org/                      Rev. B 96, 134313 (2017).
     supplemental/10.1103/PhysRevLett.120.130601 for details           [71] P. Jurcevic, H. Shen, P. Hauke, C. Maier, T. Brydges, C.
     about numerical simulations.                                           Hempel, B. P. Lanyon, M. Heyl, R. Blatt, and C. F. Roos,
[50] P. Calabrese, F. H. L. Essler, and M. Fagotti, Phys. Rev. Lett.        Phys. Rev. Lett. 119, 080501 (2017).
     106, 227203 (2011).                                               [72] J. C. Halimeh and V. Zauner-Stauber, Phys. Rev. B 96,
[51] M. Kollar, F. A. Wolf, and M. Eckstein, Phys. Rev. B 84,               134427 (2017).
     054304 (2011).                                                    [73] I. Homrighausen, N. O. Abeling, V. Zauner-Stauber, and
[52] J. C. Halimeh, V. Zauner-Stauber, I. P. McCulloch, I. de               J. C. Halimeh, Phys. Rev. B 96, 104436 (2017).
     Vega, U. Schollwock, and M. Kastner, Phys. Rev. B 95,             [74] V. Zauner-Stauber and J. C. Halimeh, Phys. Rev. E 96,
     024302 (2017).                                                         062118 (2017).
[53] A. Gambassi and A. Silva, arXiv:1106.2671.                        [75] B. Žunkovič and A. Silva (to be published).




                                                                130601-6
