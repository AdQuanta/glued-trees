# Dynamical Quantum Phase Transitions in the Transverse-Field Ising Model - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevLett.110.135704
> Collected: 2026-09-20
> Published: 2013-03-28
> Zotero parent key: GLANLRJ2
> Evidence: Publisher or author-preprint PDF

week ending
PRL 110, 135704 (2013)                  PHYSICAL REVIEW LETTERS                                                      29 MARCH 2013



             Dynamical Quantum Phase Transitions in the Transverse-Field Ising Model
                                                             M. Heyl
            Department of Physics, Arnold Sommerfeld Center for Theoretical Physics and Center for NanoScience,
                  Ludwig-Maximilians-Universität München, Theresienstrasse 37, 80333 Munich, Germany
               and Institut für Theoretische Physik, Technische Universität Dresden, 01062 Dresden, Germany

                                                         A. Polkovnikov
           Department of Physics, Boston University, 590 Commonwealth Avenue, Boston, Massachusetts 02215, USA

                                                            S. Kehrein
        Department of Physics, Georg-August-Universität Göttingen, Friedrich-Hund-Platz 1, 37077 Göttingen, Germany
              (Received 28 June 2012; revised manuscript received 29 January 2013; published 28 March 2013)
                A phase transition indicates a sudden change in the properties of a large system. For temperature-driven
             phase transitions this is related to nonanalytic behavior of the free energy density at the critical
             temperature: The knowledge of the free energy density in one phase is insufficient to predict the
             properties of the other phase. In this Letter we show that a close analogue of this behavior can occur
             in the real time evolution of quantum systems, namely nonanalytic behavior at a critical time. We denote
             such behavior a dynamical phase transition and explore its properties in the transverse-field Ising model.
             Specifically, we show that the equilibrium quantum phase transition and the dynamical phase transition in
             this model are intimately related.

             DOI: 10.1103/PhysRevLett.110.135704                                       PACS numbers: 64.70.Tg, 05.30.Rt



   Phase transitions are one of the most remarkable phe-              From a formal point of view, there is a very suggestive
nomena occurring in many-particle systems. At a phase               similarity between the canonical partition function of an
transition a system undergoes a nonanalytic change of its           equilibrium system
properties, for example the density at a temperature driven
liquid-gas transition, or the magnetization at a paramagnet-                                ZðÞ ¼ TreH                      (1)
ferromagnet transition. What makes the theory of such
                                                                    and the overlap amplitude of some time-evolved initial
equilibrium phase transitions particularly fascinating is
                                                                    quantum state ji i with itself,
the observation that a perfectly well-behaved microscopic
Hamiltonian without any singular interactions can lead to                                GðtÞ ¼ hi jeiHt ji i:              (2)
nonanalytic behavior in the thermodynamic limit of the
many-particle system. In fact, the occurrence of equilibrium        This leads to the question of whether some analogue of
phase transitions was initially a puzzling problem because          temperature ()-driven equilibrium phase transitions in (1)
one can easily verify no-go theorems for finite systems;            exists in real time evolution problems. In the theory of
therefore, the thermodynamic limit is essential [1].                equilibrium phase transitions it is well established that the
   Today the theory of equilibrium phase transitions is well        breakdown of the high-temperature (small ) expansion
established, especially for classical systems undergoing            indicates a temperature-driven phase transition. Likewise,
continuous transitions, where the powerful tool of renor-           we propose the term dynamical phase transition for non-
malization theory bridges the gap from microscopic                  analytic behavior in time, that is the breakdown of a short
Hamiltonian to universal macroscopic behavior. On the               time expansion in the thermodynamic limit at a critical
other hand, the behavior of nonequilibrium quantum                  time. In this Letter we study this notion of dynamical phase
many-body systems is by far less well understood.                   transition in the one-dimensional transverse-field Ising
Recent experimental advances have triggered a lot of                model, which serves as a paradigm for one-dimensional
activity in this field [2], like the experiments on the real        quantum phase transitions [5]. It can be solved exactly,
time evolution of essentially closed quantum systems in             which permits us to establish the existence of dynamical
cold atomic gases [3,4]. The experimental setup is typi-            phase transitions that are intimately related to the equilib-
cally a quantum quench, that is a sudden change of some             rium quantum phase transition in this model.
parameter in the Hamiltonian. Therefore the system is                  Our key quantity of interest is the boundary partition
initially prepared in a nonthermal superposition of the             function
eigenstates of the Hamiltonian which drives its time
evolution.                                                                               ZðzÞ ¼ hi jezH ji i                (3)


0031-9007=13=110(13)=135704(5)                               135704-1                         Ó 2013 American Physical Society
                                                                                                                                   week ending
PRL 110, 135704 (2013)                                  PHYSICAL REVIEW LETTERS                                                  29 MARCH 2013

in the complex plane z 2 C. For imaginary z ¼ it this just                        In a quantum quench experiment the system is prepared
describes the overlap amplitude (2). For real z ¼ R it can                     in the ground state for parameter g0 , ji i ¼ jGS ðg0 Þi,
be interpreted as the partition function of the field theory                   while its time evolution is driven with a Hamiltonian Hðg1 Þ
described by H with boundaries described by boundary                           with a different parameter g1 . In the sequel we will first
states ji i separated by R [6]. In the thermodynamic limit                    analyze quench experiments in the setting of the fermionic
one defines the free energy density (apart from a different                    model (8). A subtle difference occurs when thinking in
normalization)                                                                 terms of the spin model (7) since in the ferromagnetic
                                                                               phase the ground state of the spin model is twofold degen-
                                                  1
                           fðzÞ ¼  lim               lnZðzÞ            (4)    erate, while the fermionic model always has a unique
                                          N!1 N
                                                                               ground state. We will say more about this later. Taking
where N is the number of degrees of freedom. Now subject                       the ground state of the fermionic model in Eq. (8) as the
to a few technical conditions [1] one can show that for                        initial state ji i, the free energy density (4) describing this
finite N the partition function (3) is an entire function of z                 sudden quench g0 ! g1 can be calculated analytically [13]
since inserting an eigenbasis of H yields sums of terms                        yielding
ezEj , which are entire functions of z. According to the                                         Z  dk
Weierstrass factorization theorem [7] an entire function                         fg0 ;g1 ðzÞ ¼            lnðcos2 k þ sin2 k e2zk ðg1 Þ Þ: (9)
                                                                                                    0 2
with zeros zj 2 C can be written as
                                                                                                                                         def
                                                                               Here k ¼ k ðg0 Þ  k ðg1 Þ, and tan½2k ðgÞ ¼ sink=
                                Y       z
                                            
                   ZðzÞ ¼ ehðzÞ     1                     (5)                 ðg  coskÞ, k ðgÞ 2 ½0; =2. In (9) we have ignored an
                                j        zj                                    uninteresting additive contribution zEGS ðg1 Þ=N that
                                                                               depends on the ground state energy of Hðg1 Þ.
with an entire function hðzÞ. Thus                                                In the thermodynamic limit the zeros of the partition
                                  X                                        function in the complex plane coalesce to a family of lines
                        1                   z
        fðzÞ ¼  lim        hðzÞ þ   ln 1                              (6)    labeled by a number n 2 Z
                  N!1 N                     zj
                                   j
                                                                                                    1
                                                                                      zn ðkÞ ¼             ½lntan2 k þ ið2n þ 1Þ:           (10)
and the nonanalytic part of the free energy density is solely                                    2k ðg1 Þ
determined by the zeros zj . A similar observation was
originally made by M. E. Fisher [1], who pointed out that                      The limiting infrared and ultraviolet behavior of the
the partition function (1) is an entire function in the com-                   Bogoliubov angles,
                                                                                       8
plex temperature plane. This observation is analogous to                               >
                                                                                       > 0     quench in same phase
the Lee-Yang analysis of equilibrium phase transitions in                              <
                                                                               k¼0 ¼ =4 quench to or from quantum critical point
the complex magnetic field plane [8]. For example in the                               >
                                                                                       >
                                                                                       : =2 quench across quantum critical point
2D Ising model the Fisher zeros in the complex tempera-
ture plane approach the real axis at the critical temperature                  k¼ ¼ 0;                                                       (11)
z ¼ c in the thermodynamic limit, indicating its phase
transition [9].                                                                immediately shows that the lines of Fisher zeros cut the time
   We now work out these analytic properties explicitly for                    axis for a quench across the quantum critical point (Fig. 1)
the one-dimensional transverse-field Ising model (with                         since then limk!0 Re zn ðkÞ ¼ 1, limk! Re zn ðkÞ ¼ 1.
periodic boundary conditions)                                                  In fact, the limiting behavior (11) remains unchanged for
                                                                               general ramping protocols [14].
                                  1 X
                                    N1               X
                                                    g N                           The free energy density (4) is just the rate function of the
                 HðgÞ ¼                zi ziþ1 þ      x :           (7)
                                  2 i¼1             2 i¼1 i                    return amplitude GðtÞ ¼ exp½NfðitÞ. Likewise for the
                                                                               return probability (Loschmidt echo) LðtÞ ¼def jGðtÞj2 ¼
For magnetic field g < 1 the system is ferromagnetically                       exp½NlðtÞ one has lðtÞ ¼ fðitÞ þ fðitÞ. The behavior
ordered at zero temperature, and a paramagnet for g > 1                        of the Fisher zeros for quenches across the quantum critical
[5]. These two phases are separated by a quantum critical                      point therefore translates into nonanalytic behavior of the
point at g ¼ gc ¼ 1. The Hamiltonian (7) can be mapped                         rate functions for return amplitude and probability at cer-
to a quadratic fermionic model [10–12]                                         tain times tn . For sudden quenches one can work out these
                                                                               times easily,
                     X y
                   1 N1                                 XN
  HðgÞ ¼                ðci ciþ1 þ cyi cyiþ1 þ H:c:Þ þ g cyi ci :                                        
                                                                                                          1
                   2 i¼1                                 i¼1                                tn ¼ t n þ ;        n ¼ 0; 1; 2; . . .     (12)
                                                                                                          2
                                                                        (8)
                                                                               with t ¼ =k ðg1 Þ and k determined by cosk ¼
Diagonalization             yields              the    dispersion   relation   ð1 þ g0 g1 Þ=ðg0 þ g1 Þ. We conclude that for any quench
        pﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
k ðgÞ ¼ ðg  coskÞ þ sin k.   2             2                                 across the quantum critical point the short time expansion

                                                                         135704-2
                                                                                                                           week ending
PRL 110, 135704 (2013)                      PHYSICAL REVIEW LETTERS                                                      29 MARCH 2013

                                                                        Hðg0 Þ, then quench to Hðg1 Þ at time t ¼ 0, and then
                                                                        quench back to Hðg0 Þ at time t. The amount of work W
                                                                        performed follows from the distribution function
                                                                                   X
                                                                        PðW; tÞ ¼ ½W  ðEj  EGS ðg0 ÞÞjhEj ji ðtÞij2  (13)
                                                                                      j

                                                                        where the sum runs over all eigenstates jEj i of the initial
                                                                        Hamiltonian Hðg0 Þ. It obeys a large deviation form
                                                                        PðW; tÞ  eNrðw;tÞ with a rate function rðw; tÞ  0
                                                                        depending on the work density w ¼ W=N. In the thermo-
                                                                        dynamic limit one can derive an exact result for rðw; tÞ:
                                                                        According to the Gärtner-Ellis theorem [17] it is just the
                                                                        Legendre transform

FIG. 1 (color online). Lines of Fisher zeros for a quench within                          rðw; tÞ ¼ inf ½wR  cðR; tÞ             (14)
                                                                                                     R2R
the same phase g0 ¼ 0:4 ! g1 ¼ 0:8 (left) and across the quan-
tum critical point g0 ¼ 0:4 ! g1 ¼ 1:3 (right). Notice that the         where
Fisher zeros cut the time axis for the quench across the quantum
critical point, giving rise to nonanalytic behavior at tn (the times                 Z  dk
tn are marked with dots in the plot).
                                                                        cðR; tÞ ¼             ln½1 þ sin2 ð2k Þsin2 ðk ðg1 ÞtÞ
                                                                                      0 2
                                                                                   ðeð2k ðg0 ÞRÞ  1Þ                           (15)
for the rate function of the return amplitude and probability
breaks down in the thermodynamic limit, analogous to the                is the rate function for the cumulant generating func-
breakdown of the high-temperature expansion at an equi-                 tion of the work distribution function, CðR; tÞ ¼
librium phase transition. In fact, the nonanalytic behavior             R
                                                                          dWPðW; tÞeRW ¼ eNcðR;tÞ . In Fig. 2 we show rðw; tÞ
of lðtÞ at the times tn has already been derived by Pollmann            for a quench across the quantum critical point. For w ¼ 0 it
et al. Reference [15] for slow ramping across the quantum               just gives the return probability to the ground state,
critical point. For a slow ramping, protocol k ðg1 Þ                  rðw ¼ 0; tÞ ¼ lðtÞ; therefore, the nonanalytic behavior at
becomes the mass gap mðg1 Þ ¼ jg1  1j of the final                     the Fisher zeros shows up as nonanalytic behavior in the
Hamiltonian, but in general it is a new energy scale gen-               work distribution function. However, from Fig. 2 one can
erated by the quench and depending on the ramping pro-                  see that these nonanalyticities at w ¼ 0 also dominate the
tocol. In the universal limit for a quench across but very              behavior for w > 0 at tn , corresponding to more likely
close to the quantum critical point, g1 ¼ 1pþ   ﬃﬃﬃﬃﬃﬃ, jj  1        values of the performed work. The suggestive similarity
and fixed g0 , one finds k ðg1 Þ=mðg1 Þ / 1= jj. Hence in            to the phase diagram of a quantum critical point, with
this limit the nonequilibrium energy scale k becomes                  temperature being replaced by the work density w, moti-
very different from the mass gap, which is the only equi-               vates us to call this behavior dynamical quantum phase
librium energy scale of the final Hamiltonian.                          transitions. Notice that experimentally the work density
   The interpretation of the mode k follows from the obser-            can be lowered by postselection [18].
vation nðk Þ ¼ 1=2, where nðkÞ is the occupation of the                   So far we have analyzed the quench dynamics in terms
excited state in the momentum k-mode in the eigenbasis of               of the fermionic model (8). When thinking in terms of the
the final Hamiltonian Hf ðg1 Þ. Modes k > k have thermal               transverse-field Ising model (7), all results carry over for
occupation nðkÞ < 1=2, while modes k < k have inverted                 quenches starting in the paramagnetic phase since then
population nðkÞ > 1=2 and therefore formally negative                   the spin ground state is unique. Specifically, one finds the
effective temperature. The mode k corresponds to infinite              nonanalytic behavior in the Loschmidt echo and the work
temperature. In fact, the existence of this infinite tempera-           distribution function for quenches from the paramagnetic
ture mode and thus of the Fisher zeros cutting the time axis            to the ferromagnetic phase. For quenches originating in the
periodically is guaranteed for arbitrary ramping protocols              ferromagnetic phase, the Loschmidt echo calculated above
across the quantum critical point. For example, for slow                corresponds to working in the Neveu-Schwarz sector [19],
ramping across the quantum critical point the existence of              which amounts to an unphysical superposition of spin-up
this mode and the negative temperature region in relation to            and spin-down ground states in the spin language.
spatial correlations was discussed in Ref. [16].                        However, looking at the experimentally relevant quantity
   One measurable quantity in which the nonanalytic                     work distribution function, one derives the same result in
behavior generated by the Fisher zeros appears naturally                the thermodynamic limit as above when starting from
is the work distribution function of a double quench ex-                either of the two degenerate ferromagnetic ground states.
periment: We prepare the system in the ground state of                  Specifically, one obtains the nonanalytic behavior in

                                                                 135704-3
                                                                                                                         week ending
PRL 110, 135704 (2013)                   PHYSICAL REVIEW LETTERS                                                       29 MARCH 2013




FIG. 2 (color online). The bottom plot shows the work distri-
bution function rðw; tÞ for a double quench across the quantum
critical point (g0 ¼ 0:5, g1 ¼ 2:0). The dashed line depicts the
expectation value of the performed work, rðw; tÞ ¼ 0. The top
plot shows various cuts for fixed values of the work density w.    FIG. 3 (color online). Dynamics of the magnetization after the
The line w ¼ 0 is just the Loschmidt echo: Its nonanalytic         quench. The bottom plot shows the longitudinal magnetization
behavior at tn becomes smooth for w > 0, but traces of the        for various quenches across the quantum critical point. The time
nonanalytic behavior extend into the work density plane. In this   axis is shifted by a fit parameter t’ and one can see that the
respect work density plays a similar role to temperature in the
                                                                   period of the oscillations is the time scale t (12). The upper
phase diagram of an equilibrium quantum phase transition.
                                                                   plots show the magnetization dynamics in the y  z plane for a
                                                                   quench across the quantum critical point g0 ¼ 0:3 ! g1 ¼ 1:4
Pðw ¼ 0; tÞ at the critical times (12) for quenches from the       (left) and a quench in the ordered phase g0 ¼ 0:3 ! g1 ¼ 0:8
ferromagnetic to the paramagnetic phase [18].                      (right). For better visibility the  magnetization is normalized to
                                                                                                     qﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
     Interestingly, the nonequilibrium time scale (12) also        unit length: s^y;z ðtÞ ¼ sy;z ðtÞ= s2y ðtÞ þ s2z ðtÞ. Notice the Larmor
                                                                                           def

plays a role in the dynamics of a local observable after           precession for the quench across the quantum critical point,
the quench. We have calculated the longitudinal magneti-           while the dynamics for the quench in the ordered phase is
zation by numerical evaluation of Pfaffians [20]. For              asymptotically just an exponential decay [21].
quenches within the ordered phase it is known analytically
[21,22] that the order parameter decays exponentially as a         transition. Very recent numerical results in Ref. [23]
function of time, which is expected since in equilibrium           show that the dynamical phase transitions in the Ising
one only finds long range order at zero temperature (g < 1).       model are stable against weak integrability breaking per-
For a quench across the quantum critical point an addi-            turbations and indicate that the appearance of the real-time
tional oscillatory behavior is superimposed on this                nonanalyticities seem to be a generic feature also in other
exponential decay, see Fig. 3. Notice that the behavior of         systems as long as the respective quenches cross the equi-
the magnetization remains perfectly analytic, but the pe-          librium critical points. Notice that there are other related
riod of its oscillations agrees exactly (within numerical          but not identical notions of dynamical phase transitions, for
accuracy) with the period t of Fisher times. A conjecture         example, a sudden change of the dynamical behavior of an
consistent with our observation was also formulated in             observable as a function of some control parameter
Ref. [19]. A better understanding of this observation will         [24,25], or qualitative changes in the ensemble of trajecto-
be the topic of future work. At low energies the oscillatory       ries as a function of the conjugate field of a dynamical
decay transforms into real-time nonanalyticities at the            order parameter [26].
Fisher times using the concept of postselection, allowing             For quenches within the same phase (including to or
us to observe the dynamical phase transitions in local             from the quantum critical point) the lines of Fisher zeros lie
observables [18].                                                  in the negative half plane, Re zj ðkÞ  0 (Fig. 1). Hence the
     Summing up, we have shown that ramping across the             knowledge of the equilibrium free energy fðRÞ on the
quantum critical point of the transverse-field Ising model         positive real axis completely determines the time evolution
generates periodic nonanalytic behavior at certain times           by a simple Wick rotation. This is no longer true for a
tn . This breakdown of the short time expansion is reminis-       quench or ramping protocol across the quantum critical
cent of the breakdown of a high temperature expansion              point since then the lines of Fisher zeros cut the complex
for the free energy at an equilibrium phase transition. We         plane into disconnected stripes, Fig. 1: Knowing fðRÞ for
have therefore denoted this behavior dynamical phase               R  0 does not determine the time evolution for t > t0 .

                                                             135704-4
                                                                                                                  week ending
PRL 110, 135704 (2013)                 PHYSICAL REVIEW LETTERS                                                  29 MARCH 2013

In this sense nonequilibrium time evolution is no longer         [9] W. van Saarloos and D. Kurtze, J. Phys. A 17, 1301 (1984).
described by equilibrium properties.                            [10] E. Lieb, T. Schultz, and D. Mattis, Ann. Phys. (N.Y.) 16,
   The authors thank L. D’Alessio, M. Kolodrubetz, and D.            407 (1961).
Huse for valuable discussions. The authors also acknowl-        [11] P. Pfeuty, Ann. Phys. (N.Y.) 57, 79 (1970).
                                                                [12] E. Barouch, B. McCoy, and M. Dresden, Phys. Rev. A 2,
edge the support of the Deutsche Forschungsgemeinschaft
                                                                     1075 (1970).
via SFB-TR 12, the German Excellence Initiative via the         [13] A. Silva, Phys. Rev. Lett. 101, 120603 (2008).
Nanosystems Initiative Munich (M. H. and S. K.), the NSF        [14] For a general ramping protocol gðtÞ with gðt ¼ 0Þ ¼ g0 ,
under Grants No. DMR-0907039, No. PHY11-25915, the                   gðt ¼ Þ ¼ g1 we define ji i ¼ j c ðÞi and j c ðtÞi is the
AFOSR under Grant No. FA9550-10-1-0110, the Sloan                    solution of the Schrödinger equation: i@t j c ðtÞi ¼
and Simons Foundations (A. P.). S. K. thanks the Boston              H½gðtÞj c ðtÞi, j c ðt ¼ 0Þi ¼ jGS ðg0 Þi.
University visitors program, A. P. and S. K. thank the Kavli    [15] F. Pollmann, S. Mukerjee, A. G. Green, and J. E. Moore,
Institute for Theoretical Physics at UCSB for their hospi-           Phys. Rev. E 81, 020101(R) (2010).
tality and NSF PHY11-25915.                                     [16] M. Kolodrubetz, B. K. Clark, and D. A. Huse, Phys. Rev.
                                                                     Lett. 109, 015701 (2012).
                                                                [17] H. Touchette, Phys. Rep. 478, 1 (2009).
                                                                [18] See Supplemental Material at http://link.aps.org/
 [1] M. E. Fisher, in Boulder Lectures in Theoretical Physics        supplemental/10.1103/PhysRevLett.110.135704              for
     (University of Colorado, Boulder, 1965), Vol. 7.                details about Loschmidt echoes for symmetry broken
 [2] A. Polkovnikov, K. Sengupta, A. Silva, and M.                   initial states and postselection.
     Vengalattore, Rev. Mod. Phys. 83, 863 (2011).              [19] P. Calabrese, F. Essler, and M. Fagotti, J. Stat. Mech.
 [3] M. Greiner, O. Mandel, T. Esslinger, T. Hänsch, and I.         (2012) P07016.
     Bloch, Nature (London) 419, 51 (2002).                     [20] E. Barouch and B. McCoy, Phys. Rev. A 3, 786 (1971).
 [4] T. Kinoshita, T. Wenger, and D. Weiss, Nature (London)     [21] P. Calabrese, F. H. L. Essler, and M. Fagotti, Phys. Rev.
     440, 900 (2006).                                                Lett. 106, 227203 (2011).
 [5] S. Sachdev, Quantum Phase Transitions (Cambridge           [22] D. Schuricht and F. Essler, J. Stat. Mech. (2012) P04017.
     University Press, Cambridge, England, 2011).               [23] C. Karrasch and D. Schuricht, arXiv:1302.3893.
 [6] A. LeClair, G. Mussardo, H. Saleur, and S. Skorik, Nucl.   [24] M. Eckstein, M. Kollar, and P. Werner, Phys. Rev. Lett.
     Phys. B453, 581 (1995).                                         103, 056403 (2009).
 [7] J. B. Conway, Functions of One Complex Variable            [25] B. Sciolla and G. Biroli, J. Stat. Mech. (2011) P11003.
     (Springer, New York, 1995).                                [26] J. P. Garrahan and I. Lesanovsky, Phys. Rev. Lett. 104,
 [8] C. Yang and T. Lee, Phys. Rev. 87, 404 (1952).                  160601 (2010).




                                                          135704-5
