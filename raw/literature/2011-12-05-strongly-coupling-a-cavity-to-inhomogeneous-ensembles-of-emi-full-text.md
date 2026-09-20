# Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for long-lived solid-state quantum memories - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.84.063810
> Collected: 2026-09-20
> Published: 2011-12-05
> Zotero parent key: JENG5KGV
> Evidence: Local Zotero PDF

PHYSICAL REVIEW A 84, 063810 (2011)


        Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for long-lived
                                       solid-state quantum memories
                           I. Diniz,1 S. Portolan,1 R. Ferreira,2 J. M. Gérard,3 P. Bertet,4 and A. Auffèves1,*
          1
          CEA/CNRS/UJF Joint team “Nanophysics and semiconductors,” Institut Néel-CNRS, Boı̂te Postale 166, 25 rue des Martyrs,
                                                     F-38042 Grenoble Cedex 9, France
                             2
                               Laboratoire Pierre Aigrain, ENS/CNRS, 24 rue Lhomond, F-75005 Paris, France
      3
        CEA/CNRS/UJF Joint team “Nanophysics and semiconductors,” CEA/INAC/SP2M, 17 rue des Martyrs, F-38054 Grenoble, France
                   4
                     Quantronics group, SPEC (CNRS URA 2464), IRAMIS, DSM, CEA, F-91191 Gif-sur-Yvette, France
                 (Received 10 January 2011; revised manuscript received 1 September 2011; published 5 December 2011)
                   We investigate theoretically the coupling of a cavity mode to a continuous distribution of emitters. We discuss
                the influence of the emitters’ inhomogeneous broadening on the existence and on the coherence properties of the
                polaritonic peaks. We find that their coherence depends crucially on the shape of the distribution and not only on
                its width. Under certain conditions the coupling to the cavity protects the polaritonic states from inhomogeneous
                broadening, resulting in a longer storage time for a quantum memory based on emitter ensembles. When two
                different ensembles of emitters are coupled to the resonator, they support a peculiar collective dark state, which
                is also very attractive for the storage of quantum information.

                DOI: 10.1103/PhysRevA.84.063810                      PACS number(s): 42.50.Pq, 42.50.Ct, 42.50.Gy, 42.65.Hw


                        I. INTRODUCTION                                    broadening, we also find polaritonic peaks. Surprisingly, their
                                                                           relaxation properties are affected not only by the width of
    Understanding the coupling between a cavity and an ensem-
                                                                           the emitters distribution but also by its shape. We derive
ble of emitters was motivated in the early 1980s by seminal
                                                                           explicit formulas for the polaritonic linewidths, showing in
demonstrations of cavity quantum electrodynamics (CQED)
                                                                           particular that, provided the spectral density of emitters in the
effects [1]. First performed with atoms, these experiments were
                                                                           wings of the distribution decays faster than a Lorentzian, the
further developed in solid-state systems, starting with a few
                                                                           spectral width will be dominated by the emitter’s homogeneous
semiconductor quantum wells coupled to planar cavities [2].
                                                                           linewidth. We call this effect cavity protection. We solve
The interest for this topic has been renewed in the framework
                                                                           exactly the dynamics of the coupled system, showing that, in
of quantum information, with proposals to use collections
                                                                           this regime, the two polariton states are well decoupled from
of emitters as quantum memories for individual excitations.
                                                                           the other emitters states. As a consequence, cavity protection
Indeed, ensembles of microscopic degrees of freedom benefit
                                                                           reduces very significantly the relaxation of an excitation when
from the collective enhancement of the interaction strength [1],
                                                                           stored in one of the polariton states, which opens a promising
while possibly keeping the relaxation properties of a single
                                                                           path toward solid-state quantum memories [12,13]. We finally
emitter [3]. This led to a series of recent proposals where
                                                                           propose another potential application of cavity protection
cold atoms [4], polar molecules [5], or electronic spins [3,6]
                                                                           by considering a cavity coupled to two inhomogeneously
coupled to a superconducting cavity have been suggested
                                                                           broadened ensembles of emitters. Indeed, this system supports
as long-storage quantum memories and optical interfaces.
                                                                           a collective dark state, which is particularly attractive for the
This problem also bears some analogy to the situation where
                                                                           storage of quantum information.
a nuclear-spin ensemble is coupled to a single electronic
                                                                              The paper is organized as follows. In Sec. II we present the
spin [7]. Following these proposals, recent experiments have
                                                                           model leading to Heisenberg equations in the low-excitation
demonstrated the strong coupling of a resonator to a collection
                                                                           regime and obtain an expression for the complex transmis-
of electronic spins in a crystal [8,9]. However, inhomogeneous
                                                                           sion of the cavity. This expression is analyzed in detail in
broadening is always present in the solid state and may
                                                                           Sec. III, where we explore criteria for the strong-coupling
eventually limit the performance of such a quantum memory.
                                                                           regime, taking into account inhomogeneous broadening. The
    In this paper, we study theoretically a cavity coupled to a
                                                                           transmission pattern allows us to introduce the notion of
continuous distribution of inhomogeneously broadened emit-
                                                                           cavity protection, whose physical origin is analyzed from two
ters in the low excitation regime. In the ideal case where all the
                                                                           different perspectives in Secs. IV and V. Finally, in Sec.VI,
emitters have the same frequency, strong light-matter coupling
                                                                           we study the potential of cavity protection in the framework of
leads to the formation of two polaritonic modes separated by
                                                                           quantum memories. In particular, we discuss the possibility of
the so-called vacuum Rabi splitting [10]. In the situation we
                                                                           exploiting a collective dark state to store and retrieve quantum
aim to describe, the emitters’ bare frequencies are spread over
                                                                           information with high fidelity.
a range that can be larger than the cavity linewidth. Our goal
is to clarify the effect of inhomogeneous broadening on the
former simple picture in the ideal case, building on an early
                                                                                                       II. MODEL
work by Houdré et al. [11]. In the presence of inhomogeneous
                                                                              The system under study is pictured in Fig. 1. It consists in
                                                                           a cavity mode a of frequency ω0 , which we shall define as the
 *
     alexia.auffeves@grenoble.cnrs.fr                                      origin of frequencies, linearly coupled with a strength gk to

1050-2947/2011/84(6)/063810(9)                                      063810-1                                 ©2011 American Physical Society
I. DINIZ et al.                                                                                  PHYSICAL REVIEW A 84, 063810 (2011)

                                                                                                                     
                                                                         ρ(ω) = k gk2 δ(ω − ωk )/ 2 , where 2 = k gk2 . Introduc-
                                                                         ing this definition
                                                                                            in Eq. (2) and using the identity 1/(ωk −
                                                                         ω − iγ ) = dω δ(ω − ωk )/(ω − ω − iγ ), we obtain
                                                                                                        κ/2i
                                                                                       t(ω) =                         ,                  (3)
                                                                                                ω − ω0 + iκ/2 − W (ω)
                                                                         with
                                                                                                         ∞
                                                                                                             ρ(ω )dω
                                                                                       W (ω) =     2
                                                                                                                
                                                                                                                                         (4)
                                                                                                        −∞ ω − ω + iγ /2

                                                                            In the following we consider three different continua,
   FIG. 1. Scheme of the emitters-cavity coupled system. The cavity      namely, a Gaussian, a Lorentzian, and a rectangular distri-
frequency is ω0 . The cavity mode is coupled to the outside world via    bution. Gaussian broadening is quite common in nature, from
two ports labeled 1 and 2, and the kth two-level system has frequency
                                                                         Doppler-broadened lines in gases to, e.g., size distributions
ωk and interacts with the cavity mode with coupling constant gk .
                                                                         in ensembles of semiconductor nanocrystals [16] and self-
a distribution of N two-level systems of frequencies ωk and              assembled quantum dots [17]. Lorentzian distributions can be
damping rates γ . In the regime where the number of excitations          found in certain solid-state systems, such as spin ensembles in
is small compared to the total number of emitters, each                  dipolar interaction [18] or dilute optically active impurities
two-level emitter is properly modeled by a bosonic mode bk               in crystals [19]. Finally, the rectangular distribution is a
(Holstein-Primakoff approximation). The total Hamiltonian is             prototypical example of finite bandwidth distribution. The
written   H = Hcav + Hem +       Hint , with Hcav = h̄ω0 a † a, Hem =   results obtained in this case can, for instance, qualitatively
           †                               †      †                     be applied to dilute ensembles of fluorescent molecules in
    k h̄ωk bk bk , and Hint = ih̄   k gk (a bk − bk a).
    Using well-known input-output formalism [14], we define              organic crystals [20]. For these three distributions, we have
the external fields cin (injected or pumping field), cr (reflected       obtained analytical expressions for the function W (ω), which
field), and ct (transmitted field) that lead to the damping κ of         are detailed in Appendix B.
the intracavity field. We also consider atomic losses γ , i.e.,
atomic emission in modes other than the cavity mode. The                  III. PROPERTIES OF THE TRANSMISSION FUNCTION
Heisenberg equations are written in the frame rotating at the               In this section we discuss the properties of the transmission
frequency ω of the probe, yielding                                       function [Eq. (3)] in the resonant case. First, we recall
                                                 
  ȧ = −[κ/2 + i(ω0 − ω)]a − κ/2cin +                 gk bk + fa (t),    some well-known results in the absence of inhomogeneous
                                                 k
                                                                         broadening ( = 0). In that case, the distribution ρ(ω) is
                                                                         well described by a Dirac δ function, leading to W (ω) =
          b˙k = −[γ /2 + i(ωk − ω)]sk − gk a + fk (t),
                                                                 (1)    2 /(ω +iγ /2), and the transmission function has two poles,
                      cr = cin + κ/2a,                                   λ± = ± 2 − [(κ − γ )/4]2 + i κ+γ     4
                                                                                                                  [21]. Strong coupling is
                                                                        reached if   κ,γ and is manifested by the appearance of a
                         ct = κ/2a,
                                                                         doublet in the transmission pattern located at ± (at first order
where fa (t) and fk (t) are noise operators allowing the                 in κ/ ,γ / ). These two peaks are the spectral counterpart of
preservation of the commutation relations. From this set of              the coherent and reversible exchange of a quantum of energy
equations and as demonstrated in Appendix A, it comes out that           between the cavity field and the symmetrical state |S of
                                                                                                                                 †
the evolution of the system can be modeled with a generalized            the emitters ensemble, defined as |S = −1 gk bk |0. The
Hamiltonian Heff involving the respective complex emitters               transmission coefficient t(ω) is proportional to the Fourier-
and cavity frequencies ω̃k = ωk − iγ /2 and ω̃0 = ω0 − iκ/2.             Laplace transform of the field’s amplitude in the cavity initially
Consequently, the system made of N atoms coupled to a cavity             fed with a single excitation 1,G|e−iHeff t/h̄ |1,G (this result is
appears to be equivalent to an ensemble of N + 1 coupled                 demonstrated in Appendix A, generalizing Ref. [22], and is
leaky cavities, and the problem reduces to the study of the              also valid in the case where  > 0). The so-called collective
classical evolution of the field in each cavity. This exact              Rabi oscillation takes place at the frequency
                                                                                                                     √  defined above,
analogy is the basis of the model. Taking the average value              which in that case simply equals  = g0 N , and is damped
and solving analytically the set of equations in the steady-state        on a time scale given by the finite linewidth of the peaks.
regime, we get the following expression for the complex                  In that temporal picture, strong coupling is reached when the
transmission of the cavity:                                              excitation is exchanged several times before being lost in the
                  ct              −κ/2i                                environment.
        t(ω) =           =                         .            (2)       We now study how the strong coupling features are
                  cin    ω̃0 − ω − k gk2 (ω̃k − ω)
                                                                         modified by inhomogeneous broadening. We have plotted the
    We are interested in the very large number of emitters N ,           transmission in energy |t(ω)|2 for / ranging from 0 to 3.5 in
so we describe the emitters as a continuous distribution with            Fig. 2. To be only sensitive to the influence of inhomogeneous
spectral density ρ(ω) spread around its central frequency ωc             broadening, we have kept κ and γ negligible with respect to .
and normalized to 1. The full width at half maximum (FWHM)               We have considered the three types of distributions introduced
is denoted  and is used to parametrize each distribution. As            in Sec. II, namely, Lorentzian [Fig. 2(a)], Gaussian [Fig. 2(b)],
in Ref. [15], we define the spectral density distribution as             and rectangular [Fig. 2(c)]. Whatever the distribution, two

                                                                   063810-2
STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . .                                               PHYSICAL REVIEW A 84, 063810 (2011)

                                                                       Looking at Eq. (7), it appears that in the strong-coupling
                                                                       regime, the polaritonic peaks remain located at ± but
                                                                       that inhomogeneous broadening adds a contribution to their
                                                                       linewidth. This contribution writes 2π 2 ρ() and scales like
                                                                       the density of emitters at the real frequency of the poles. This
                                                                       feature explains the sensitivity to the distribution shape that
                                                                       clearly appears in Fig. 2. The polaritonic linewidth decreases
                                                                       upon increasing , provided the distribution ρ(ω) decays
                                                                       faster than 1/ω2 . The Lorentzian distribution is the limiting
                                                                       case for which the linewidth tends toward a constant :
                                                                       whatever the coupling, the polaritonic linewidth is governed
                                                                       by inhomogeneous broadening. On the other hand, in the
                                                                       Gaussian and rectangular cases, increasing the ratio /
                                                                       allows to get rid of the influence of the parameter , so that
    FIG. 2. (Color online) Transmission of a cavity resonantly
                                                                       the width of the peaks only depends on the losses of the cavity
coupled to a broad distribution of emitters. (a,d) Lorentzian,
(b,e) Gaussian, and (c,f) rectangular. We took  = 1 MHz, κ =
                                                                       and of individual emitters. In the rectangular case, this ideal
0.1 MHz, γ = 10−4 MHz. In (d)–(f)  = 3.5 MHz. These values            behavior is even reached for finite values of the collective
are typical of nitrogen-vacancy centers coupled to a superconducting   coupling strength  (while it remains a limit in the Gaussian
resonator.                                                             case). This effect, which we call cavity protection, leads to an
                                                                       enhanced lifetime of the Rabi oscillation and has interesting
peaks appear in the transmission pattern when  > , a                 consequences for quantum information storage, as we show in
signature of Rabi oscillation in the temporal domain. A first          Sec. VI.
rough interpretation is that strong coupling is reached when
dephasing processes, which take place on a time scale −1 , are                   IV. ORIGIN OF PEAK BROADENING
slower than energy exchanges, whose period still scales like
−1 . Note that the Rabi period is a collective quantity involving        Before focusing on applications opened by cavity pro-
all the emitters, even emitters that are not spectrally matched to     tection, we give an interpretation of peak broadening. This
the cavity mode. This apparently puzzling feature had already          amounts to understanding the damping of Rabi oscillations,
been evidenced in Ref. [11] and is due to the fact that the mode       which occurs even in the absence of any radiative losses
interacts with a collective state of the matter field.                 κ = γ = 0. Our approach is based on the seminal paper of
    Inhomogeneous broadening does more than state a novel              Fano [23] and consists in the diagonalization of the total
condition to fulfill to ensure strong light-matter coupling. As it     Hamiltonian of the system H = Hcav + Hem + Hint .
eventually accelerates the damping of Rabi oscillations, it also          In the absence of inhomogeneous broadening, preparing
leads to the broadening of the polaritonic peaks, as clearly seen      the system in the initial state |1,G gives rise to Rabi
in Fig. 2. In particular, the shape of the emitters distribution       oscillations between the atoms and the field. This state is
has a dramatic influence. An analytical expression for this            a coherent superposition of two eigenstates of the Hamil-
width can be derived in perturbation with respect to the small         tonian, namely, the polaritons |ψ±0  = √12 |0,S ± i √12 |1,G
parameter / : namely, departing from the strong-coupling             of energies ±h̄, where |S is the symmetrical matter state
case in the absence of inhomogeneous broadening, we evaluate           defined in Sec. III. Rabi oscillation is a quantum beat between
how the poles of the transmission function are modified when           these two components. In particular, all other emitter states,
0 <   . For the sake of simplicity we consider the limit            which do not interact with the electromagnetic field and are
γ = 0. The case of finite γ is studied in Appendix C in the limit      usually called “dark states,” remain uncoupled. The presence
γ  , which corresponds to the experimental situations we             of inhomogeneous broadening strongly modifies the features
aim to describe. Using the Sokhatsky-Weierstrass formula in            of the emitters-cavity coupling. Introducing the continuous
Eq. (4) we have                                                        basis of bare emitter states |ω of energy h̄ω, we write the
                           ∞                                          matrix elements of H as
             W (ω)             ρ(ω )dω
                     =  P                 − iπρ(ω).            (5)
              2           −∞ ω − ω
                                                                                          1,G|H |1,G = h̄ω0 ,
                                                                                                           
   The modified poles of the transmission function are ex-                               ω |H |1,G = h̄ ρ(ω ),                (8)
pected in the vicinity of ±, so that we develop the expression                             
                                                                                         ω |H |ω = h̄δ(ω − ω )ω

of W (ω) for ω ∼   :
                                                                       where the coupling is normalized per unit frequency. An
                   2                                                  eigenvector |ψω  of H with energy h̄ω is searched under the
         W (ω) =       [1 + O(2 /ω2 )] − iπ 2 ρ(ω),           (6)
                   ω                                                   form
                                                                                                       
yielding for the poles of the transmission function (at first order
                                                              2                   |ψω  = a(ω)|1,G + dω b(ω,ω ),             (9)
in κ/  and second order in / ) λ± = ± + i κ+2π4 ρ() .
Finally, keeping a finite γ leads to the modified expression for
the full width at half maximum of the peaks:                           where the quantity |a(ω)|2 is normalized with respect to ω. For
                                                                       distributions whose support is not bounded, as is the case for
                   = [κ + γ + 2πρ()2 ]/2.                     (7)    the Lorentzian and Gaussian, the solution of the eigenvalue

                                                                 063810-3
I. DINIZ et al.                                                                                 PHYSICAL REVIEW A 84, 063810 (2011)

equation has been carried out by Fano [23], yielding the
normalized eigenvectors:
        √                      √
                                   ρ(ω )
          ρ(ω) |1,G + P dω ω−ω            
                                         |ω  + C(ω)|ω
|ψω  =                                                 ,
                       C(ω)2 + [πρ(ω)2 ]2
                                                       (10)
        
where P stands for principal value and
                                 
                                           ρ(ω )
          C(ω) = ω − ω0 − 2 P dω                     (11)
                                           ω − ω
                                                                           FIG. 3. (Color online) Schematic diagram of the open-system
The amplitude of probability to find the excitation in the cavity      approach to inhomogeneous broadening. (a)  = 0, the states |ψ± 
mode can finally be written                                            are isolated from the degenerate dark states |ω. (b)  = 0, the states
                                                                      |ψ±  are coupled to the |ω states, which are nondegenerate in this
          −iH t/h̄                −iH t/h̄
   1,G|e          |1,G = 1,G|e            dω a ∗ (ω )|ψω        case, with a coupling strength proportional to .
                           
                                               
                         = dω |a(ω )|2 e−iω t .               (12)   The second type, related to πρ()2 , is Hamiltonian and thus
                                                                       reversible, in principle, with spin-echo experiments. It is due
    It can easily be shown that |a(ω)|2 is proportional to the         to the interaction of the cavity with a continuum of emitters,
transmission coefficient in energy |t(ω)|2 [namely, |a(ω)|2 =          leading to progressive dephasing of Rabi oscillations.
2 ρ(ω)| t(ω)
          κ/2
              |2 for γ ,κ → 0], so that |t(ω)|2 corresponds to
the Fourier transform of the occupation amplitude of the
                                                                                       V. OPEN-SYSTEM APPROACH
cavity mode. As we have checked in Appendix D, this result
is completely consistent with the formalism of the Laplace                 The approach developed in Sec. IV gives an interpretation
transform used in Sec. III in the absence of external sources of       of the peaks broadening within a Hamiltonian formalism. In
losses.                                                                this part, we adopt another point of view based on quantum
    This approach sheds new light on the transmission function         open systems. As shown above and pictured in Fig. 3, in
studied in Sec. III, which directly reflects the overlap between       the absence of inhomogeneous broadening, the symmetrical
the initial state |1,G and the continuum of eigenstates               state |S is decoupled from the dark states. The excitation
|ψω  of the Hamiltonian. The two-peak characteristics of              initially injected in the cavity mode remains thus trapped in
the strong-coupling regime show that this initial state is a           the “small system” consisting of the two polaritons |ψ+0  and
coherent superposition of two wave packets, reminiscent of             |ψ−0 . When inhomogeneous broadening is switched on, the
the polaritons obtained when  = 0. As the eigenstates of the          symmetrical state couples to the dark states, which act as an
Hamiltonian form an infinite continuum, these wave packets             environment in which the excitation can decay. Broadening
always have a finite width, which is responsible for the               of the polaritonic peaks can be attributed to the decoherence
damping of Rabi oscillations. Nevertheless, as shown above,            induced by the bath of dark states. This picture is corroborated
increasing the collective coupling  may drastically change            by the computed, expression for the width of the transmission
the shape of this overlap and eventually lead to the narrowing         peaks, = 2π 2 ρ(), which could be interpreted as a natural
of the peaks for distributions ρ(ω) decaying faster than ω−2 , a       linewidth for polaritons “dressed” by the environment of
phenomenon that was defined above as cavity protection.                dark states. Nevertheless, the analogy should be used with
    Distributions with a bounded support of width  (rectan-           caution, as the coupling with the bath is not Markovian.
gular, for example) provide an interesting limiting case where         This naive picture still has the advantage of giving intuitive
cavity protection is almost perfect. As a matter of fact, if  >       insight on cavity protection, which is nothing but energetically
, the Hamiltonian eigenstates consist not only in a continuum         decoupling the polaritons from the bath of dark states, as
ψω lying within the support of the distribution but also in two        initially suggested in Ref. [13].
discrete states |ψ+  and |ψ− , located around ω = ± (at                 To study the dynamics of the polaritonic relaxation, we
first order in /), corresponding to the polaritons |ψ+0  and        have exactly computed the evolution of the state of the system
|ψ−0  when  = 0. The initial state |1,G mostly overlaps with        initially prepared in |ψ+0  for different values of the collective
these two eigenstates, making the problem similar to the case          coupling strength  and for the three types of distribution,
of standard Rabi oscillations in the absence of inhomogeneous          keeping the same FWHM  = 1 MHz. We have plotted
broadening. In particular, if ρ(ω) is rectangular, the overlap of      in Fig. 4 the probability |ψ+0 |e−iHeff t/h̄ |ψ+0 |2 of finding the
|1,G with the discrete states is C = 1 − (1/8)(/ )2 , giving        excitation in the polariton as a function of time. For the sake of
rise to Rabi oscillations of infinite duration characterized by a      clarity, we have neglected again the losses κ = γ = 0 (realistic
contrast C.                                                            values are considered below). As can be seen in Fig. 4, if the
    To conclude this part, we emphasize that the total damping         distribution is Lorentzian, the excitation exponentially decays
rate = [κ + γ + 2πρ()2 ]/2 evidenced in Sec. III shows               in the environment, whatever the coupling , on a typical time
contributions of essentially a different nature. The first type,       scale −1 . This is consistent with the spectral study performed
related to κ and γ , is due to the irreversible loss of the            in Sec. III, where the width of the polaritonic peaks does not
excitation in the environment of the cavity or the emitters.           depend on the coupling with the cavity. On the contrary, the

                                                                 063810-4
STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . .                                                                        PHYSICAL REVIEW A 84, 063810 (2011)


                                           (a)               (b)                 (c)




| < ψ+0 | Uef f (t) |ψ+0 > |2
                                 1                    1                  1

                                0.8                  0.8                0.8

                                0.6                  0.6                0.6

                                0.4                  0.4                0.4

                                0.2                  0.2                0.2

                                 0                    0                   0
                                          5        10         5        10         5        10
                                 Time (units of 1/Δ) Time (units of 1/Δ) Time (units of 1/Δ)

    FIG. 4. (Color online) Probability to recover an excitation ini-
tially stored in the state |ψ+0  after a time t. We took  = 1 MHz,
κ = γ = 0. (a) Lorentzian, (b) Gaussian, and (c) rectangular. Red
dashed line,  = 1 MHz; green dotted line,  = 2 MHz; blue solid                                     FIG. 5. (Color online) Maximized fidelity F of regaining the
line,  = 4 MHz.                                                                                 excitation initially stored in the state |ψ+  after τ = 10 cavity
                                                                                                 lifetimes as a function of /. We took  = 1 MHz, κ = 0.1 MHz,
effect of cavity protection can be observed on the two other                                     γ = 10−4 MHz. The inset shows the same quantity L as a function of
distributions. Damping is strongly inhibited as soon as  >                                     detuning δ after τ . Green dotted line,  = 40 MHz; black solid line,
if the distribution is Gaussian but is always present whatever                                    = 20 MHz; blue dashed line,  = 10 MHz; red dash-dotted line,
                                                                                                  = 5 MHz.
the coupling, which is the counterpart of the finite linewidth
of the transmission peaks. Finally, in the case of a rectangular
distribution, two time scales are visible. The initial state |ψ+0 
mostly overlaps with the discrete state |ψ+  defined above                                      contrary, are all weaker as the atoms-cavity detuning is smaller.
but also overlaps with the continuum of eigenstates |ψω .                                       The atoms-cavity detuning is thus the result of a trade-off and
The coherent superposition of the continuum of frequencies                                       can be optimized with our modeling, as we show below.
is damped on a short time scale −1 , so that the probability                                        The protocol of the quantum memory is the following.
quickly converges toward the quantity |ψ+0 |ψ+ |2 , which also                                 First, the detuning δ between the mode and the center of
scales like (/)2 .                                                                             the distribution is slowly swept from −∞ to a finite positive
                                                                                                 value, thus adiabatically mapping the quantum state of the
                                                                                                 cavity mode onto the emitters ensemble: (α|0 + β|1)|G →
                                      VI. APPLICATION TO QUANTUM MEMORIES                        |0[α|G + β|ψ+0 (δ)]. We have introduced the dressed state
    The previous sections establish that, for distributions                                      |ψ+0 (δ) = cos(θ/2)|0,S + i sin(θ/2)|1,G and the mixing
allowing cavity protection, increasing the collective coupling                                   angle cot(θ ) = δ/(2). The transfer of the excitation should be
 dramatically increases the potential storage time of one                                       realized on a time scale longer than the Rabi period but shorter
excitation in the polaritonic states, as energetic decoupling                                    than −1 so that no dephasing mechanism affects the process;
from the dark states is more pronounced. In particular, this                                     this can be achieved under strong coupling, as in this case
storage time becomes insensitive to dephasing processes                                            . The expected fidelity F(t) of such a quantum memory
induced by inhomogeneous broadening. This allows to treat                                        can be exactly computed with the present model; in particular,
an inhomogeneous distribution as an effective oscillator with                                    in the case where a single photon state is stored (β = 1),
ground state |G and first excited state |S, which benefits from                                we get the simple expression F = |ψ+0 (δ)|e−iHeff t/h̄ |ψ+0 (δ)|2 .
the collective coupling  to the cavity and whose relaxation                                     We have plotted this quantity in Fig. 5. As explained above,
properties are solely governed by individual emitter properties                                  F must be optimized by properly choosing the detuning δ,
γ . As a consequence, cavity protection opens the path to the                                    which should be low enough to maintain cavity protection and
implementation of long-lived solid-state quantum memories                                        high enough to reduce the sensitivity to cavity losses, which
by exploiting ensembles of microscopic degrees of freedom,                                       typically scale like κ(/δ)2 . The maximal detuning δM leading
whose coherence times are remarkable. In this section we use                                     to an efficient protective energy gap is 2 /δM ∼  [12]. This
our modeling to estimate the performances of two such types                                      condition induces an optimal reduction of the cavity losses by
of quantum memories.                                                                             a factor of (/)2 .
                                                                                                     The trade-off in the detuning clearly appears in the inset of
                                                                                                 Fig. 5, where we have plotted F as a function of the detuning δ
                                      A. Quantum memory based on dispersive coupling             after ten cavity lifetimes for different values of the ratio /.
   Here we evaluate the potential of a broad ensemble of                                         We have used standard parameters for circuit QED technology
emitters dressed by a cavity mode for quantum information                                        [8]. As it appears in Fig. 5, a quantum memory based on a
storage. The coupling should be dispersive to freeze Rabi                                        Gaussian distribution of emitters of linewidth  = 1 MHz
oscillations between the mode and the atoms. This system                                         strongly coupled to a cavity of width κ = 0.1 MHz with a
offers an interesting situation where information has to be                                      strength  = 40 MHz would yield a typical fidelity of 90%
protected against two types of losses: the cavity losses, which                                  after 100 μs, a remarkable storage time compared to the
are more critical when the mode and the distribution of emitters                                 lifetime of the cavity mode (10 μs) and the typical dephasing
are on resonance, and the losses in the dark states, which, on the                               time of the ensemble (1 μs).

                                                                                           063810-5
I. DINIZ et al.                                                                                                                     PHYSICAL REVIEW A 84, 063810 (2011)

                                                                                                                                                  √
                        B. Quantum memory based on two emitter distributions                                  state |A = (|G1 ,S2  − |S1 ,G2 )/
                                                                                                                                               √ 2, with√its expression be-
    We focus now on a second type of quantum memory based                                                     ing |ψd  = (iδ|1,G1 ,G2  +  2|0,A)/ δ 2 + 22 . When
on two distributions of emitters allowing cavity protection,                                                  δ  , the excitation is mostly in the cavity and is mostly
respectively detuned by +δ and −δ with respect to a cavity.                                                   in the matter field in the opposite case. This change of nature
Note that the case of a mode coupled to two such discrete                                                     clearly appears in the narrowing of the peak while decreasing
emitters of ground and excited states |gi  and |ei  is exactly                                              δ, as can be seen in Fig. 6 and confirmed by the expression
solvable, with the poles of the transmission revealing the                                                    for its linewidth d = (δ 2 κ + 22 γ )/(δ 2 + 22 ). Note that
complex eigenfrequencies of the system [24]. In particular,                                                   this modeling might explain some recent experimental results
when the emitters are on resonance with the   √ mode (δ = 0), the                                             [8], in which a superconducting cavity is strongly coupled
antisymmetrical state (|e1 ,g2  − |g1 ,e2 )/ 2 is not coupled to                                            to a inhomogeneous ensemble of nitrogen-vacancy centers
the electromagnetic field. This dark state is naturally protected                                             of spin 1. Because of the geometrical strain, the transitions
against spontaneous emission in the cavity, a property that                                                   |mS = 0 → |mS = 1 and |mS = 0 → |mS = −1 are non-
can be used to store quantum information during a typical                                                     degenerate, which can be modeled by two ensembles of
time scale given by the atomic dephasing time. Note that                                                      emitters of different central frequencies. The visible presence
for artificial atoms like superconducting qubits or quantum                                                   of a narrow peak at the cavity frequency explains qualitatively
dots this time can be quite short, which is a severe drawback                                                 the effect discussed above.
for quantum computation on a chip. Here we suggest an                                                             Coming back to the general case of two distinct ensembles,
experiment to prepare and exploit this dark state as a quantum                                                the state |ψd  could provide a new type of quantum memory,
memory in the case where the discrete emitters are replaced                                                   as mentioned in the beginning of this section. The protocol
by broad assemblies of atoms. This proposal allows us                                                         consists in feeding the cavity mode with a single photon while
to benefit from the collective atoms-cavity coupling, while                                                   the ensembles are largely detuned, thus preparing the state
the storage time now corresponds to the dephasing time                                                        |1,G1 ,G2 , and then adiabatically transferring the excitation
of individual emitters and is thus potentially quite long.                                                    to |ψd  by slowly lowering δ. Yet the ensembles cannot be
Note that this idea is typical of the so-called hybrid-circuit                                                brought to resonance with the mode as would be the case for
technology [3–6].                                                                                             two discrete emitters. As seen in Fig. 6(c), the effective model
    First, we have checked the validity of the effective model                                                breaks down when δ ∼ . At this point, indeed, the dis-
if two ensembles are coupled to the cavity. We have plotted                                                   tributions of emitters start to spectrally overlap with the
in Fig. 6(a) the exact transmission |t(ω)|2 of a cavity coupled                                               central peak, leading to its broadening. This yields a minimal
to two Gaussian ensembles and have verified that the position                                                 linewidth d ∼ γ + (2 /22 )κ, allowing us to typically
of the peaks are fitted by the eigenenergies computed in the                                                  reduce the cavity losses by (/)2 . Here again the ratio
discrete case. Moreover, we have superimposed the transmis-                                                   (/)2 appears as a major figure of merit for devices based
sion resulting from the exact calculation and from the discrete                                               on inhomogeneous ensembles strongly coupled to cavities.
model, as can be seen in Fig. 6(b) after focusing on the central
peak of the transmission pattern: the excellent agreement be-                                                                      VII. CONCLUSION
tween the two plots fully validates the effective approach. This
central peak corresponds to the eigenstate |ψd  resulting from                                                  We have shown that if an inhomogeneous distribution of
the coupling between the cavity mode and the antisymmetric                                                    emitters is strongly coupled to a cavity, the ensemble can be
                                                                                                              treated as a single effective emitter collectively coupled to the
                                                                                                              mode, whose relaxation is governed by the single emitter’s
                                                                                                              properties, provided that their spectral distribution decreases




Frequency(units of Δ)
                        100
                                                                                                              faster than 1/ω2 . This effect, called “cavity protection,”
                                                                                                 (a)          offers promising perspectives in the framework of quantum
                          0                                                                                   information with solid-state integrable devices, particularly
                                                                                                              regarding the implementation of long-lived high-fidelity
                   −100
                       0           10       20         30       40          50     60       70         80
                                                                                                              quantum memories. These results are quite general and can
                                                               δ/Δ                                            fruitfully be applied to numerous important physical systems,
                          1                                            1                                      ranging from semiconductor emitters coupled to optical
                                                       (b)                                         (c)
2                                                            2                                                cavities to ensembles of spins in circuit QED.
 |t(ω)|                                                       |t(ω)|
                        0.5                                          0.5
                                                                                                                                 ACKNOWLEDGMENTS
                         0                                             0
                         −0.4 −0.2      0        0.2    0.4            −0.4 −0.2        0   0.2        0.4       The authors gratefully thank Z. Kurucz, K. Mølmer,
                              Frequency (units of Δ)                       Frequency (units of Δ)
                                                                                                              G. Nogues, J. Claudon, M. F. Santos, and D. Estève for
    FIG. 6. (Color online) (a) Transmission of a cavity coupled to                                            all the fruitful exchanges. This work was supported by
two Gaussian distributions of emitters, each detuned by +δ and −δ                                             the NanoSci-ERA consortium, by the EU under ERANET
from the cavity frequency; δ is swept from 0 to 8 MHz. We took  =                                            project LECSIN, by the European project SOLID, by the
1 MHz,  = 0.1 MHz, κ = 0.5 MHz, γ = 10−4 MHz. (b) Focus on                                                   Nanosciences Foundation of Grenoble, and by ANR projects
the central peak with δ = 0.5 MHz. Solid red line, Gaussian profile;                                          CAFE and QINVC. I.D. acknowledges the CAPES. I.D.,
blue dashed line, two emitters of homogeneous linewidth γ . (c) As                                            S.P., and A.A. thank the Center for Quantum Technologies
in (b) for δ = 0.15 MHz.                                                                                      of Singapore.

                                                                                                        063810-6
STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . .                                                     PHYSICAL REVIEW A 84, 063810 (2011)

                   APPENDIX A: DYNAMICS                                      This establishes the relation between the amplitude α1 (t) =
                                                                             1,G|e−iHeff t/h̄ |1,G and the transmission t(ω) as
    In this appendix, we establish the link between the complex                                   ∞
transmission of the cavity and the evolution of the system if                                                         2
the mode a is initially fed with a single photon. This evolution                                     α1 (t)eiωt dt = − t(ω).         (A6)
                                                                                                  0                   κ
is governed by the set of equations (1) written in the free frame
(ω = 0). The input fields are in vacuum, and the state of the                   One can use the method exposed above to compute the
system is |1,G = a † (0)|0, where |0 is the ground state of the           expression of the probability amplitude for a state initially
total system. We are interested in the quantities a(t)a † (0) and          prepared in |ψ+0 (δ), namely, ψ+0 (δ)|e−iHeff t/h̄ |ψ+0 (δ) studied
bk (t)a † (0), which represent the probability amplitudes of the           in Sec. VI. In general, we can decompose it as
excitation in the cavity mode and in each emitter, respectively,
                                                                             ψ+0 (δ)|Ueff (t)|ψ+0 (δ)
as will be shown later. The average values are taken in state
|0. We get                                                                       = cos2 (θ/2)1,G|Ueff |1,G + sin2 (θ/2)0,S|Ueff |0,S
                                                                                   + i sin(θ/2) cos(θ/2)(0,S|Ueff |1,G − 1,G|Ueff |0,S)
ȧ(t)a † (0) = −(κ/2 + iω0 )a(t)a † (0) +     gk bk (t)a † (0),
                                                                                  = cos2 (θ/2)α1 (t) + sin2 (θ/2)α2 (t)
                                                       k

 b˙k (t)a (0) = −(γ /2 + iωk )bk (t)a (0) − gk a(t)a † (0).
         †                                    †                                     + i sin(θ/2) cos(θ/2)[α3 (t) − α4 (t)],                  (A7)
                                                                     (A1)    where Ueff (t) ≡ e−iHeff t/h̄ .
                                                                                 We need only to calculate the four matrix elements
   The vector |ψ, defined as (a(t)a † (0), . . . ,                        αi (t). Defining ti (s) = L(αi (t)), we obtain, in the case of a
bk (t)a † (0), . . .), evolves in time following the                       continuous distribution,
Schrödinger-like equation h̄ dtd |ψ(t) = −iHeff |ψ(t), with
                                                                                                           W (is)
                                                                                              t2 (s) = −          t1 (s)(s + i ω˜o ),
                        ⎛                                       ⎞                                            2
                          ω̃0       ig1   ig2          ...                                                          iW (is)
                        ⎜−ig                                    ⎟                                   t3 (s) = t1 (s)         ,                (A8)
                        ⎜     1     ω̃1                         ⎟                                                      
             Heff /h̄ = ⎜                                       ⎟.   (A2)                               t4 (s) = −t3 (s).
                        ⎜−ig2                 ω̃2               ⎟
                        ⎝                                       ⎠
                           ..                          ..
                            .                               .
                                                                                  APPENDIX B: W (ω) FOR SPECIFIC DISTRIBUTIONS
We have used the complex frequencies for the cavity ω̃0 and
for the emitters ω̃k defined above. Note that these results                     We now evaluate the function W (ω) for all the specific
are in full agreement with the ones obtained in the Green                    continua analyzed in this paper. This function allows the eval-
function formalism by Kurucz et al. [12]. It appears that                    uation of the complex transmission using t(ω) = (κ/2i)[ω −
the dynamics of the problem can be modeled with the                          ω0 + iκ/2 − W (ω)]−1 but also appears in other formulas.
effective Hamiltonian Heff . In particular, one can define an
effective evolution operator O(t) = eiHeff t/h̄ Oe−iHeff t/h̄ , such                               1. Gaussian distribution
that a(t)a † (0) = 0|a(0)e−iHeff t/h̄ a † (0)|0. This quantity can            The    Gaussian         distribution    is     written   ρ(ω) =
be rewritten 1,G|e−iHeff t/h̄ |1,G, justifying that we talk of the         √
                                                                               ln 2 −(ω2 ln 2)/2
                                                                              √    e              . W (ω) is thus
probability amplitude of the excitation in the cavity mode,                   π
starting from the initial state |1,G. The problem is solved                                √              ⎡                  ⎤
                                                                                                                          2
using, e.g., the standard
                      ∞ Laplace transform method. Defining                           1         ln 2 2 √ ⎣ i ∞    dω e−ω    ⎦ . (B1)
L(f (t)) = F (s) = 0 exp(st)f (t)dt, we have                                 WG (ω) =                    π       
                                                                                      i                            √ /2 − ω
                                                                                                             π −∞ ω+iγ
                                                                                                                          / ln 2
                         −1                       −1
             |ψ(t) = L ((s + iHeff /h̄) |ψ(0)),                    (A3)    Remembering that
                                                                                                      2
where we have used the Laplace transform property                                      i ∞         e−ω
                                                                                              dω         = e−z erfc(−iz),
                                                                                                               2

L{ dtd |ψ(t)} = s|(s) − |ψ(0). We finally define t1 (s) =                                                                                (B2)
                                                                                      π −∞        z − ω
1,G|(s + iHeff /h̄)−1 |1,G. Inverse Laplace transform of this
coefficient gives back the quantity 1,G|e−iHeff /h̄t |1,G. We              where erfc is the complex complementary error function, it
easily get                                                                   becomes
                                                                                           √                                         
                                                                                             ln 2 2 √ −( /
                                                                                                          ω+iγ
                                                                                                            √ /2 )2         ω + iγ /2
                 t1 (s) =
                                      1
                                                           .         (A4)     WG (ω) = −i             πe      ln 2 erfc  −i    √        .
                                                 gk2                                                                      / ln 2
                            s + i ω̃0 +       k s+i ω̃k
                                                                                                                                      (B3)
From Eqs. (3) and (A4), we finally write the link between the
transmission coefficient in amplitude t(ω) and the coefficient
t1 (s) characterizing the dynamics of the system,                                                 2. Rectangular distribution
                              κ                                                In the case of a rectangular distribution, the density of
                      t(ω) = − t1 (−iω).                             (A5)    emitter is ρ(ω) = 1 [(ω − /2) − (ω + /2)], and we
                              2

                                                                       063810-7
I. DINIZ et al.                                                                              PHYSICAL REVIEW A 84, 063810 (2011)

have                                                                 where we have used   γ . One easily infers the modifi-
                             2                                     cations to the transmission poles induced by inhomogeneous
                         2            
              WR (ω) =       arctan         .             (B4)       broadening. They are located at
                          i        γ − 2iω                                      
                                                                                                                     
                                                                                                   κ + 2πρ()2 − γ 2
                                                                      ω± = ± 1 + μ2 / 2 −                             . (C6)
                    3. Lorentzian distribution                                                             4
   The density of the emitter is ρ(ω) = /2    1
                                                      ; thus
                                         π (/2)2 +ω2
                                                                        Their width check = κ+γ +2π
                                                                                                                2
                                                                                                            ρ()
                                                                                                         2
                                                                                                                 , in correspondence
                                    2                               with what was stated in Sec. III. Note that this procedure
                  WL (ω) =                    .           (B5)       is only valid for a distribution with well-defined moments.
                             ω + iγ /2 + i/2
                                                                     This is not the case of the Lorentzian; nevertheless, W (ω) can
From the equation above we see that for the Lorentzian               be exactly evaluated in this case. The exact calculations for
distribution we do not achieve cavity protection; i.e., the          the three cases taken under consideration are the subject of
inhomogeneous broadening always contributes as if it were            Appendix B.
homogeneous.
                                                                      APPENDIX D: TWO WAYS TO OBTAIN THE TEMPORAL
       APPENDIX C: DEVELOPMENT WITH FINITE γ
                                                                                       EVOLUTION
   We start by rewriting W (ω) from Eq. (4) as                          We have found two ways to evaluate α1 (t) =
                 ∞
                            ω2 ρ(ω + ω)                            1,G|e−iHeff t/h̄ |1,G; the first, in Appendix A, uses a Laplace-
   W (ω) =   2
                     dω 2                                          Fourier transform of −t(ω)/(κ/2), and the second uses the
                 −∞      ω + γ2       ω
                      ∞                                             standard Fourier transform of 2π 2 ρ(ω)|t(ω)/(κ/2)|2 for
                                    γ                                κ,γ → 0 as in Sec. IV. The first way is more general in the
            − iπ 2       dω     2
                                           ρ(ω + ω ).    (C1)
                      −∞      π (ω + γ 2 )                           sense that it can include emitter and cavity radiative losses;
The integrands contain products of a function of width γ and         the second describes a reversible process that originates in a
another with width . If γ  , the integrals take the form          Hamiltonian evolution. We now show that both ways coincide
                   ∞                                                when we disregard losses.
                       ρ(ω )dω                                        From Appendix A we have
    W (ω) = 2 P              
                    −∞ ω − ω                                                              ∞
                                    ∞              
                               γ         ρ(ω )dω                                           α1 (t)eiωt dt = t1 (−iω),            (D1)
             − i πρ(ω) + P
                  2
                                                  2
                                                       . (C2)                            0
                                2    −∞ (ω − ω )
                                                                     where, if γ ,κ → 0,
   We are interested in the development of W (ω) near the poles
of the transmission function in the absence of inhomogeneous                                                i
broadening,          ω ∼ . Denoting r = ω /ω and using the              t1 (−iω) =                      ρ(ω )dω                  .   (D2)
          namely,                                                                     ω − ω0   − 2 P        ω−ω
                                                                                                                       + iπ 2 ρ(ω)
identity r = 1/(1 − r), we find
             k
                               ∞
                                                                         We now take the real part of Eqs. (D1) and (D2), yielding
                    2          μk
           W (ω) =         1+         − iπρ(ω)                                  ∞                
                     ω         k=1
                                   ωk                                       Re       α1 (t)eiωt dt
                                                                                0
                        2 γ        ∞
                                               μk                                                                              
                    −i 2        1+      (k + 1) k ,        (C3)                                          i
                        ω 2                    ω                              = Re                          )dω
                                    k=1                                               ω − ω0 − 2 P ρ(ω   ω−ω
                                                                                                                   + iπ 2 ρ(ω)
where μk is the kth moment of the distribution ρ(ω) about its
                                                                               = π 2 ρ(ω)|t1 |2 ;                                        (D3)
origin,
                         ∞                                          if we consider time reversibility of the lossless dynamics, we
                   μk ≡     dωρ(ω)ωk .                 (C4)          have α1 (−t) = [α1 (t)]∗ and thus
                             −∞                                              ∞                 ∞
    Note that this development is only valid if ω  ω , which          2Re       α1 (t)eiωt dt =      [α1 (t)eiωt + α1∗ (t)e−iωt ]dt
is the case in the present study as ω ∼    > ω . From the                 0                     0
                                                                                                    ∞
normalization and considering only symmetric distributions,
we have μ0 = 1 and μ1 = 0. μ2 gives the first nonzero                                           =       α1 (t)eiωt dt.             (D4)
                                                                                                         −∞
correction, and it is typically proportional to the square of
the FWHM [as an example, μ2 = 2 /(2 ln 2) in the case of a          Equations (D3) and (D4) together give
Gaussian distribution]. To first nonzero correction we have                      ∞
                                                                                   α1 (t)eiωt dt = 2π 2 ρ(ω)|t1 |2 ,                   (D5)
                 2                     γ 2                                        −∞
      W (ω) =       (1 + μ2 /ω2 ) − i        + π 2
                                                    ρ(ω)
                 ω                      2 ω2                         which is precisely what we find by applying the inverse Fourier
               2 (1 + μ2 /ω2 )                                      transform in Eq. (12). Note we had to use the time reversibility,
             =                  − iπ 2 ρ(ω),             (C5)
                  ω + iγ /2                                          which is only valid in the lossless case.

                                                               063810-8
STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . .                                                  PHYSICAL REVIEW A 84, 063810 (2011)

 [1] Y. Kaluzny, P. Goy, M. Gross, J. M. Raimond, and S. Haroche,         [13] Z. Kurucz, M. W. Sorensen, J. M. Taylor, M. D.
     Phys. Rev. Lett. 51, 1175 (1983).                                         Lukin, and M. Fleischhauer, Phys. Rev. Lett. 103, 010502
 [2] C. Weisbuch, M. Nishioka, A. Ishikawa, and Y. Arakawa, Phys.              (2009).
     Rev. Lett. 69, 3314 (1992).                                          [14] C. W. Gardiner and M. J. Collett, Phys. Rev. A 31, 3761
 [3] A. Imamoglu, Phys. Rev. Lett. 102, 083602 (2009).                         (1985).
 [4] J. Verdu, H. Zoubi, C. Koller, J. Majer, H. Ritsch, and              [15] X.-H. Wang, R. Wang, B. Y. Gu, and G. Z. Yang, Phys. Rev.
     J. Schmiedmayer, Phys. Rev. Lett. 103, 043603 (2009).                     Lett. 88, 093902 (2002).
 [5] P. Rabl, D. DeMille, J. M. Doyle, M. D. Lukin, R. J. Schoelkopf,     [16] C. B. Murray et al., Science 270, 1335 (1995).
     and P. Zoller, Phys. Rev. Lett. 97, 033003 (2006).                   [17] J. Y. Marzin, J.-M. Gérard, A. Izrael, D. Barrier, and G. Bastard,
 [6] J. H. Wesenberg, A. Ardavan, G. A. D. Briggs, J. J. L. Morton,            Phys. Rev. Lett. 73, 716 (1994).
     R. J. Schoelkopf, and D. I. Schuster, Phys. Rev. Lett. 103, 070502   [18] D. Hone et al., Phys. Rev. 186, 291 (1969).
     (2009).                                                              [19] D. L. Orth et al., J. Phys. Condens. Matter 5, 2533 (1993).
 [7] J. M. Taylor, C. M. Marcus, and M. D. Lukin, Phys. Rev. Lett.        [20] A. A. L. Nicolet et al., Chem. Phys. Chem. 8, 1215 (2007).
     90, 206803 (2003).                                                   [21] L. C. Andreani, G. Panzarini, and J.-M. Gérard, Phys. Rev. B
 [8] Y. Kubo et al., Phys. Rev. Lett. 105, 140502 (2010).                      60, 13276 (1999).
 [9] D. I. Schuster et al., Phys. Rev. Lett. 105, 140501 (2010).          [22] A. Auffèves, B. Besga, J.-M. Gérard, and J. P. Poizat, Phys. Rev.
[10] M. Gross and S. Haroche, Phys. Rep. 93, 301 (1982).                       A 77, 063833 (2008).
[11] R. Houdré, R. P. Stanley, and M. Ilegems, Phys. Rev. A 53, 2711     [23] U. Fano, Phys. Rev. 124, 1866 (1961).
     (1996).                                                              [24] J. M. Fink, R. Bianchetti, M. Baur, M. Goppl, L. Steffen,
[12] Z. Kurucz, J. H. Wesenberg, and K. Molmer, Phys. Rev. A 83,               S. Filipp, P. J. Leek, A. Blais, and A. Walraff, Phys. Rev. Lett.
     053852 (2011).                                                            103, 083601 (2009).




                                                                    063810-9
