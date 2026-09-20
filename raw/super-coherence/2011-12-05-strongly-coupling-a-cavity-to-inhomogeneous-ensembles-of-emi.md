# Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for long-lived solid-state quantum memories

> Source: https://link.aps.org/doi/10.1103/PhysRevA.84.063810
> Collected: 2026-09-20
> Published: 2011-12-05

## Zotero record

- Parent item key: JENG5KGV
- Collections: Super-Coherence
- Item type: journalArticle
- Authors: I. Diniz; S. Portolan; R. Ferreira; J. M. Gérard; P. Bertet; A. Auffèves
- Original date field: 2011-12-5
- Publication: Physical Review A
- DOI: 10.1103/PhysRevA.84.063810
- URL: https://link.aps.org/doi/10.1103/PhysRevA.84.063810
- Citation key: dinizStronglyCouplingCavity2011
- PDF attachment keys: 7SMUYE9E
- Evidence captured: Zotero indexed PDF text (7SMUYE9E)

## Full text

PHYSICAL REVIEW A 84, 063810 (2011)
Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for long-lived solid-state quantum memories
I. Diniz,1 S. Portolan,1 R. Ferreira,2 J. M. G ́erard,3 P. Bertet,4 and A. Auff`eves1,*
1CEA/CNRS/UJF Joint team “Nanophysics and semiconductors,” Institut Ne ́el-CNRS, Boıˆte Postale 166, 25 rue des Martyrs, F-38042 Grenoble Cedex 9, France 2Laboratoire Pierre Aigrain, ENS/CNRS, 24 rue Lhomond, F-75005 Paris, France 3CEA/CNRS/UJF Joint team “Nanophysics and semiconductors,” CEA/INAC/SP2M, 17 rue des Martyrs, F-38054 Grenoble, France 4Quantronics group, SPEC (CNRS URA 2464), IRAMIS, DSM, CEA, F-91191 Gif-sur-Yvette, France (Received 10 January 2011; revised manuscript received 1 September 2011; published 5 December 2011)
We investigate theoretically the coupling of a cavity mode to a continuous distribution of emitters. We discuss the influence of the emitters’ inhomogeneous broadening on the existence and on the coherence properties of the polaritonic peaks. We find that their coherence depends crucially on the shape of the distribution and not only on its width. Under certain conditions the coupling to the cavity protects the polaritonic states from inhomogeneous broadening, resulting in a longer storage time for a quantum memory based on emitter ensembles. When two different ensembles of emitters are coupled to the resonator, they support a peculiar collective dark state, which is also very attractive for the storage of quantum information.
DOI: 10.1103/PhysRevA.84.063810 PACS number(s): 42.50.Pq, 42.50.Ct, 42.50.Gy, 42.65.Hw
I. INTRODUCTION
Understanding the coupling between a cavity and an ensemble of emitters was motivated in the early 1980s by seminal demonstrations of cavity quantum electrodynamics (CQED) effects [1]. First performed with atoms, these experiments were further developed in solid-state systems, starting with a few semiconductor quantum wells coupled to planar cavities [2]. The interest for this topic has been renewed in the framework of quantum information, with proposals to use collections of emitters as quantum memories for individual excitations. Indeed, ensembles of microscopic degrees of freedom benefit from the collective enhancement of the interaction strength [1], while possibly keeping the relaxation properties of a single emitter [3]. This led to a series of recent proposals where cold atoms [4], polar molecules [5], or electronic spins [3,6] coupled to a superconducting cavity have been suggested as long-storage quantum memories and optical interfaces. This problem also bears some analogy to the situation where a nuclear-spin ensemble is coupled to a single electronic spin [7]. Following these proposals, recent experiments have demonstrated the strong coupling of a resonator to a collection of electronic spins in a crystal [8,9]. However, inhomogeneous broadening is always present in the solid state and may eventually limit the performance of such a quantum memory. In this paper, we study theoretically a cavity coupled to a continuous distribution of inhomogeneously broadened emitters in the low excitation regime. In the ideal case where all the emitters have the same frequency, strong light-matter coupling leads to the formation of two polaritonic modes separated by the so-called vacuum Rabi splitting [10]. In the situation we aim to describe, the emitters’ bare frequencies are spread over a range that can be larger than the cavity linewidth. Our goal is to clarify the effect of inhomogeneous broadening on the former simple picture in the ideal case, building on an early work by Houdr ́e et al. [11]. In the presence of inhomogeneous
*alexia.auffeves@grenoble.cnrs.fr
broadening, we also find polaritonic peaks. Surprisingly, their relaxation properties are affected not only by the width of the emitters distribution but also by its shape. We derive explicit formulas for the polaritonic linewidths, showing in particular that, provided the spectral density of emitters in the wings of the distribution decays faster than a Lorentzian, the spectral width will be dominated by the emitter’s homogeneous linewidth. We call this effect cavity protection. We solve exactly the dynamics of the coupled system, showing that, in this regime, the two polariton states are well decoupled from the other emitters states. As a consequence, cavity protection reduces very significantly the relaxation of an excitation when stored in one of the polariton states, which opens a promising path toward solid-state quantum memories [12,13]. We finally propose another potential application of cavity protection by considering a cavity coupled to two inhomogeneously broadened ensembles of emitters. Indeed, this system supports a collective dark state, which is particularly attractive for the storage of quantum information. The paper is organized as follows. In Sec. II we present the model leading to Heisenberg equations in the low-excitation regime and obtain an expression for the complex transmission of the cavity. This expression is analyzed in detail in Sec. III, where we explore criteria for the strong-coupling regime, taking into account inhomogeneous broadening. The transmission pattern allows us to introduce the notion of cavity protection, whose physical origin is analyzed from two different perspectives in Secs. IV and V. Finally, in Sec.VI, we study the potential of cavity protection in the framework of quantum memories. In particular, we discuss the possibility of exploiting a collective dark state to store and retrieve quantum information with high fidelity.
II. MODEL
The system under study is pictured in Fig. 1. It consists in a cavity mode a of frequency ω0, which we shall define as the origin of frequencies, linearly coupled with a strength gk to
063810-1
1050-2947/2011/84(6)/063810(9) ©2011 American Physical Society


 I. DINIZ et al. PHYSICAL REVIEW A 84, 063810 (2011)
FIG. 1. Scheme of the emitters-cavity coupled system. The cavity frequency is ω0. The cavity mode is coupled to the outside world via two ports labeled 1 and 2, and the kth two-level system has frequency ωk and interacts with the cavity mode with coupling constant gk.
a distribution of N two-level systems of frequencies ωk and damping rates γ . In the regime where the number of excitations is small compared to the total number of emitters, each two-level emitter is properly modeled by a bosonic mode bk (Holstein-Primakoff approximation). The total Hamiltonian is written H = Hcav + Hem + Hint, with Hcav =  ̄hω0a†a, Hem =
∑
k  ̄hωkb†
kbk, and Hint = i ̄h ∑
k gk(a†bk − b†
k a ).
Using well-known input-output formalism [14], we define the external fields cin (injected or pumping field), cr (reflected field), and ct (transmitted field) that lead to the damping κ of the intracavity field. We also consider atomic losses γ , i.e., atomic emission in modes other than the cavity mode. The Heisenberg equations are written in the frame rotating at the frequency ω of the probe, yielding
a ̇ = −[κ/2 + i(ω0 − ω)]a − √κ/2cin + ∑
k
gkbk + fa(t),
b ̇k = −[γ /2 + i(ωk − ω)]sk − gka + fk(t),
(1)
cr = cin + √κ/2a,
ct = √κ/2a,
where fa(t) and fk(t) are noise operators allowing the preservation of the commutation relations. From this set of equations and as demonstrated in Appendix A, it comes out that the evolution of the system can be modeled with a generalized Hamiltonian Heff involving the respective complex emitters and cavity frequencies ω ̃ k = ωk − iγ /2 and ω ̃ 0 = ω0 − iκ/2. Consequently, the system made of N atoms coupled to a cavity appears to be equivalent to an ensemble of N + 1 coupled leaky cavities, and the problem reduces to the study of the classical evolution of the field in each cavity. This exact analogy is the basis of the model. Taking the average value and solving analytically the set of equations in the steady-state regime, we get the following expression for the complex transmission of the cavity:
t(ω) = 〈ct 〉
〈cin〉 = −κ/2i
ω ̃ 0 − ω − ∑
k g2
k
/(ω ̃ k − ω) . (2)
We are interested in the very large number of emitters N , so we describe the emitters as a continuous distribution with spectral density ρ(ω) spread around its central frequency ωc and normalized to 1. The full width at half maximum (FWHM) is denoted   and is used to parametrize each distribution. As in Ref. [15], we define the spectral density distribution as
ρ(ω) = ∑
k g2
k δ(ω − ωk)/  2, where  2 = ∑
k g2
k . Introduc
ing this definition in Eq. (2) and using the identity 1/(ωk −
ω − iγ ) = ∫ dω′δ(ω′ − ωk)/(ω′ − ω − iγ ), we obtain
t(ω) = κ/2i
ω − ω0 + iκ/2 − W (ω) , (3)
with
W (ω) =  2
∫∞
−∞
ρ (ω′ )d ω′
ω − ω′ + iγ /2 (4)
In the following we consider three different continua, namely, a Gaussian, a Lorentzian, and a rectangular distribution. Gaussian broadening is quite common in nature, from Doppler-broadened lines in gases to, e.g., size distributions in ensembles of semiconductor nanocrystals [16] and selfassembled quantum dots [17]. Lorentzian distributions can be found in certain solid-state systems, such as spin ensembles in dipolar interaction [18] or dilute optically active impurities in crystals [19]. Finally, the rectangular distribution is a prototypical example of finite bandwidth distribution. The results obtained in this case can, for instance, qualitatively be applied to dilute ensembles of fluorescent molecules in organic crystals [20]. For these three distributions, we have obtained analytical expressions for the function W (ω), which are detailed in Appendix B.
III. PROPERTIES OF THE TRANSMISSION FUNCTION
In this section we discuss the properties of the transmission function [Eq. (3)] in the resonant case. First, we recall some well-known results in the absence of inhomogeneous broadening (  = 0). In that case, the distribution ρ(ω) is well described by a Dirac δ function, leading to W (ω) =  2/(ω + iγ /2), and the transmission function has two poles,
λ± = ±√ 2 − [(κ − γ )/4]2 + i κ+γ
4 [21]. Strong coupling is
reached if     κ,γ and is manifested by the appearance of a doublet in the transmission pattern located at ±  (at first order in κ/  ,γ /  ). These two peaks are the spectral counterpart of the coherent and reversible exchange of a quantum of energy between the cavity field and the symmetrical state |S〉 of
the emitters ensemble, defined as |S〉 =  −1 ∑ gkb†
k|0〉. The transmission coefficient t(ω) is proportional to the FourierLaplace transform of the field’s amplitude in the cavity initially fed with a single excitation 〈1,G|e−iHefft/ ̄h|1,G〉 (this result is demonstrated in Appendix A, generalizing Ref. [22], and is also valid in the case where   > 0). The so-called collective Rabi oscillation takes place at the frequency   defined above, which in that case simply equals   = g0
√N , and is damped on a time scale given by the finite linewidth of the peaks. In that temporal picture, strong coupling is reached when the excitation is exchanged several times before being lost in the environment. We now study how the strong coupling features are modified by inhomogeneous broadening. We have plotted the transmission in energy |t(ω)|2 for  /  ranging from 0 to 3.5 in Fig. 2. To be only sensitive to the influence of inhomogeneous broadening, we have kept κ and γ negligible with respect to  . We have considered the three types of distributions introduced in Sec. II, namely, Lorentzian [Fig. 2(a)], Gaussian [Fig. 2(b)], and rectangular [Fig. 2(c)]. Whatever the distribution, two
063810-2


 STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . . PHYSICAL REVIEW A 84, 063810 (2011)
FIG. 2. (Color online) Transmission of a cavity resonantly coupled to a broad distribution of emitters. (a,d) Lorentzian, (b,e) Gaussian, and (c,f) rectangular. We took   = 1 MHz, κ = 0.1 MHz, γ = 10−4 MHz. In (d)–(f)   = 3.5 MHz. These values are typical of nitrogen-vacancy centers coupled to a superconducting resonator.
peaks appear in the transmission pattern when   >  , a signature of Rabi oscillation in the temporal domain. A first rough interpretation is that strong coupling is reached when dephasing processes, which take place on a time scale  −1, are slower than energy exchanges, whose period still scales like  −1. Note that the Rabi period is a collective quantity involving all the emitters, even emitters that are not spectrally matched to the cavity mode. This apparently puzzling feature had already been evidenced in Ref. [11] and is due to the fact that the mode interacts with a collective state of the matter field. Inhomogeneous broadening does more than state a novel condition to fulfill to ensure strong light-matter coupling. As it eventually accelerates the damping of Rabi oscillations, it also leads to the broadening of the polaritonic peaks, as clearly seen in Fig. 2. In particular, the shape of the emitters distribution has a dramatic influence. An analytical expression for this width can be derived in perturbation with respect to the small parameter  /   : namely, departing from the strong-coupling case in the absence of inhomogeneous broadening, we evaluate how the poles of the transmission function are modified when 0 <      . For the sake of simplicity we consider the limit γ = 0. The case of finite γ is studied in Appendix C in the limit γ    , which corresponds to the experimental situations we aim to describe. Using the Sokhatsky-Weierstrass formula in Eq. (4) we have
W (ω)
 2 = P
∫∞
−∞
ρ (ω′ )d ω′
ω − ω′ − iπρ(ω). (5)
The modified poles of the transmission function are expected in the vicinity of ± , so that we develop the expression of W (ω) for ω ∼      :
W (ω) =  2
ω [1 + O( 2/ω2)] − iπ  2ρ(ω), (6)
yielding for the poles of the transmission function (at first order in κ/   and second order in  /  ) λ± = ±  + i κ+2π 2ρ( )
4.
Finally, keeping a finite γ leads to the modified expression for the full width at half maximum of the peaks:
= [κ + γ + 2πρ( ) 2]/2. (7)
Looking at Eq. (7), it appears that in the strong-coupling regime, the polaritonic peaks remain located at ±  but that inhomogeneous broadening adds a contribution to their linewidth. This contribution writes 2π  2ρ( ) and scales like the density of emitters at the real frequency of the poles. This feature explains the sensitivity to the distribution shape that clearly appears in Fig. 2. The polaritonic linewidth decreases upon increasing  , provided the distribution ρ(ω) decays faster than 1/ω2. The Lorentzian distribution is the limiting case for which the linewidth tends toward a constant  : whatever the coupling, the polaritonic linewidth is governed by inhomogeneous broadening. On the other hand, in the Gaussian and rectangular cases, increasing the ratio  /  allows to get rid of the influence of the parameter  , so that the width of the peaks only depends on the losses of the cavity and of individual emitters. In the rectangular case, this ideal behavior is even reached for finite values of the collective coupling strength   (while it remains a limit in the Gaussian case). This effect, which we call cavity protection, leads to an enhanced lifetime of the Rabi oscillation and has interesting consequences for quantum information storage, as we show in Sec. VI.
IV. ORIGIN OF PEAK BROADENING
Before focusing on applications opened by cavity protection, we give an interpretation of peak broadening. This amounts to understanding the damping of Rabi oscillations, which occurs even in the absence of any radiative losses κ = γ = 0. Our approach is based on the seminal paper of Fano [23] and consists in the diagonalization of the total Hamiltonian of the system H = Hcav + Hem + Hint. In the absence of inhomogeneous broadening, preparing the system in the initial state |1,G〉 gives rise to Rabi oscillations between the atoms and the field. This state is a coherent superposition of two eigenstates of the Hamiltonian, namely, the polaritons |ψ0±〉 = √12 |0,S〉 ± i √12 |1,G〉
of energies ± ̄h , where |S〉 is the symmetrical matter state defined in Sec. III. Rabi oscillation is a quantum beat between these two components. In particular, all other emitter states, which do not interact with the electromagnetic field and are usually called “dark states,” remain uncoupled. The presence of inhomogeneous broadening strongly modifies the features of the emitters-cavity coupling. Introducing the continuous basis of bare emitter states |ω〉 of energy  ̄hω, we write the matrix elements of H as
〈1,G|H |1,G〉 =  ̄hω0,
〈ω′|H |1,G〉 =  ̄h √ρ(ω′), (8)
〈ω′|H |ω〉 =  ̄hδ(ω − ω′)ω
where the coupling is normalized per unit frequency. An eigenvector |ψω〉 of H with energy  ̄hω is searched under the form
|ψω〉 = a(ω)|1,G〉 +
∫
dω′b(ω,ω′), (9)
where the quantity |a(ω)|2 is normalized with respect to ω. For distributions whose support is not bounded, as is the case for the Lorentzian and Gaussian, the solution of the eigenvalue
063810-3


 I. DINIZ et al. PHYSICAL REVIEW A 84, 063810 (2011)
equation has been carried out by Fano [23], yielding the normalized eigenvectors:
|ψω〉 =
√ρ(ω) (|1,G〉 + P ∫ dω′ √ρ(ω′)
ω−ω′ |ω′〉) + C(ω)|ω〉
√C(ω)2 + [πρ(ω) 2]2 ,
(10)
where P ∫ stands for principal value and
C(ω) = ω − ω0 −  2 P
∫
dω′ ρ(ω′)
ω − ω′ (11)
The amplitude of probability to find the excitation in the cavity mode can finally be written
〈1,G|e−iH t/ ̄h|1,G〉 = 〈1,G|e−iH t/ ̄h
∫
dω′a∗(ω′)|ψω′ 〉
=
∫
dω′|a(ω′)|2e−iω′t . (12)
It can easily be shown that |a(ω)|2 is proportional to the transmission coefficient in energy |t(ω)|2 [namely, |a(ω)|2 =
 2ρ(ω)| t(ω)
κ/2 |2 for γ ,κ → 0], so that |t(ω)|2 corresponds to the Fourier transform of the occupation amplitude of the cavity mode. As we have checked in Appendix D, this result is completely consistent with the formalism of the Laplace transform used in Sec. III in the absence of external sources of losses. This approach sheds new light on the transmission function studied in Sec. III, which directly reflects the overlap between the initial state |1,G〉 and the continuum of eigenstates |ψω〉 of the Hamiltonian. The two-peak characteristics of the strong-coupling regime show that this initial state is a coherent superposition of two wave packets, reminiscent of the polaritons obtained when   = 0. As the eigenstates of the Hamiltonian form an infinite continuum, these wave packets always have a finite width, which is responsible for the damping of Rabi oscillations. Nevertheless, as shown above, increasing the collective coupling   may drastically change the shape of this overlap and eventually lead to the narrowing of the peaks for distributions ρ(ω) decaying faster than ω−2, a phenomenon that was defined above as cavity protection. Distributions with a bounded support of width   (rectangular, for example) provide an interesting limiting case where cavity protection is almost perfect. As a matter of fact, if   >  , the Hamiltonian eigenstates consist not only in a continuum ψω lying within the support of the distribution but also in two discrete states |ψ+〉 and |ψ−〉, located around ω = ±  (at
first order in  /  ), corresponding to the polaritons |ψ0+〉 and
|ψ0−〉 when   = 0. The initial state |1,G〉 mostly overlaps with these two eigenstates, making the problem similar to the case of standard Rabi oscillations in the absence of inhomogeneous broadening. In particular, if ρ(ω) is rectangular, the overlap of |1,G〉 with the discrete states is C = 1 − (1/8)( /  )2, giving rise to Rabi oscillations of infinite duration characterized by a contrast C. To conclude this part, we emphasize that the total damping rate = [κ + γ + 2πρ( ) 2]/2 evidenced in Sec. III shows contributions of essentially a different nature. The first type, related to κ and γ , is due to the irreversible loss of the excitation in the environment of the cavity or the emitters.
FIG. 3. (Color online) Schematic diagram of the open-system approach to inhomogeneous broadening. (a)   = 0, the states |ψ±〉 are isolated from the degenerate dark states |ω〉. (b)   = 0, the states |ψ±〉 are coupled to the |ω〉 states, which are nondegenerate in this case, with a coupling strength proportional to  .
The second type, related to πρ( ) 2, is Hamiltonian and thus reversible, in principle, with spin-echo experiments. It is due to the interaction of the cavity with a continuum of emitters, leading to progressive dephasing of Rabi oscillations.
V. OPEN-SYSTEM APPROACH
The approach developed in Sec. IV gives an interpretation of the peaks broadening within a Hamiltonian formalism. In this part, we adopt another point of view based on quantum open systems. As shown above and pictured in Fig. 3, in the absence of inhomogeneous broadening, the symmetrical state |S〉 is decoupled from the dark states. The excitation initially injected in the cavity mode remains thus trapped in the “small system” consisting of the two polaritons |ψ0+〉 and
|ψ0−〉. When inhomogeneous broadening is switched on, the symmetrical state couples to the dark states, which act as an environment in which the excitation can decay. Broadening of the polaritonic peaks can be attributed to the decoherence induced by the bath of dark states. This picture is corroborated by the computed, expression for the width of the transmission peaks, = 2π  2ρ( ), which could be interpreted as a natural linewidth for polaritons “dressed” by the environment of dark states. Nevertheless, the analogy should be used with caution, as the coupling with the bath is not Markovian. This naive picture still has the advantage of giving intuitive insight on cavity protection, which is nothing but energetically decoupling the polaritons from the bath of dark states, as initially suggested in Ref. [13]. To study the dynamics of the polaritonic relaxation, we have exactly computed the evolution of the state of the system initially prepared in |ψ0+〉 for different values of the collective coupling strength   and for the three types of distribution, keeping the same FWHM   = 1 MHz. We have plotted in Fig. 4 the probability |〈ψ0+|e−iHefft/ ̄h|ψ0+〉|2 of finding the excitation in the polariton as a function of time. For the sake of clarity, we have neglected again the losses κ = γ = 0 (realistic values are considered below). As can be seen in Fig. 4, if the distribution is Lorentzian, the excitation exponentially decays in the environment, whatever the coupling  , on a typical time scale  −1. This is consistent with the spectral study performed in Sec. III, where the width of the polaritonic peaks does not depend on the coupling with the cavity. On the contrary, the
063810-4


 STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . . PHYSICAL REVIEW A 84, 063810 (2011)
5 10
0
0.2
0.4
0.6
0.8
1
Time (units of 1/Δ) 5 10
0
0.2
0.4
0.6
0.8
1
Time (units of 1/Δ)
5 10
0
0.2
0.4
0.6
0.8
1
Time (units of 1/Δ)
| < ψ+0| Ueff (t) |ψ+0 > |2
(c)
(b)
(a)
FIG. 4. (Color online) Probability to recover an excitation initially stored in the state |ψ0+〉 after a time t. We took   = 1 MHz, κ = γ = 0. (a) Lorentzian, (b) Gaussian, and (c) rectangular. Red dashed line,   = 1 MHz; green dotted line,   = 2 MHz; blue solid line,   = 4 MHz.
effect of cavity protection can be observed on the two other distributions. Damping is strongly inhibited as soon as   >   if the distribution is Gaussian but is always present whatever the coupling, which is the counterpart of the finite linewidth of the transmission peaks. Finally, in the case of a rectangular distribution, two time scales are visible. The initial state |ψ0+〉
mostly overlaps with the discrete state |ψ+〉 defined above but also overlaps with the continuum of eigenstates |ψω〉. The coherent superposition of the continuum of frequencies is damped on a short time scale  −1, so that the probability quickly converges toward the quantity |〈ψ0+|ψ+〉|2, which also
scales like ( /  )2.
VI. APPLICATION TO QUANTUM MEMORIES
The previous sections establish that, for distributions allowing cavity protection, increasing the collective coupling   dramatically increases the potential storage time of one excitation in the polaritonic states, as energetic decoupling from the dark states is more pronounced. In particular, this storage time becomes insensitive to dephasing processes induced by inhomogeneous broadening. This allows to treat an inhomogeneous distribution as an effective oscillator with ground state |G〉 and first excited state |S〉, which benefits from the collective coupling   to the cavity and whose relaxation properties are solely governed by individual emitter properties γ . As a consequence, cavity protection opens the path to the implementation of long-lived solid-state quantum memories by exploiting ensembles of microscopic degrees of freedom, whose coherence times are remarkable. In this section we use our modeling to estimate the performances of two such types of quantum memories.
A. Quantum memory based on dispersive coupling
Here we evaluate the potential of a broad ensemble of emitters dressed by a cavity mode for quantum information storage. The coupling should be dispersive to freeze Rabi oscillations between the mode and the atoms. This system offers an interesting situation where information has to be protected against two types of losses: the cavity losses, which are more critical when the mode and the distribution of emitters are on resonance, and the losses in the dark states, which, on the
FIG. 5. (Color online) Maximized fidelity F of regaining the excitation initially stored in the state |ψ+〉 after τ = 10 cavity lifetimes as a function of  / . We took   = 1 MHz, κ = 0.1 MHz, γ = 10−4 MHz. The inset shows the same quantity L as a function of detuning δ after τ . Green dotted line,   = 40 MHz; black solid line,   = 20 MHz; blue dashed line,   = 10 MHz; red dash-dotted line,   = 5 MHz.
contrary, are all weaker as the atoms-cavity detuning is smaller. The atoms-cavity detuning is thus the result of a trade-off and can be optimized with our modeling, as we show below. The protocol of the quantum memory is the following. First, the detuning δ between the mode and the center of the distribution is slowly swept from −∞ to a finite positive value, thus adiabatically mapping the quantum state of the cavity mode onto the emitters ensemble: (α|0〉 + β|1〉)|G〉 → |0〉[α|G〉 + β|ψ0+(δ)〉]. We have introduced the dressed state
|ψ0+(δ)〉 = cos(θ/2)|0,S〉 + i sin(θ/2)|1,G〉 and the mixing
angle cot(θ ) = δ/(2 ). The transfer of the excitation should be realized on a time scale longer than the Rabi period but shorter than  −1 so that no dephasing mechanism affects the process; this can be achieved under strong coupling, as in this case      . The expected fidelity F(t) of such a quantum memory can be exactly computed with the present model; in particular, in the case where a single photon state is stored (β = 1), we get the simple expression F = |〈ψ0+(δ)|e−iHefft/ ̄h|ψ0+(δ)〉|2. We have plotted this quantity in Fig. 5. As explained above, F must be optimized by properly choosing the detuning δ, which should be low enough to maintain cavity protection and high enough to reduce the sensitivity to cavity losses, which typically scale like κ( /δ)2. The maximal detuning δM leading to an efficient protective energy gap is  2/δM ∼   [12]. This condition induces an optimal reduction of the cavity losses by a factor of ( / )2. The trade-off in the detuning clearly appears in the inset of Fig. 5, where we have plotted F as a function of the detuning δ after ten cavity lifetimes for different values of the ratio  / . We have used standard parameters for circuit QED technology [8]. As it appears in Fig. 5, a quantum memory based on a Gaussian distribution of emitters of linewidth   = 1 MHz strongly coupled to a cavity of width κ = 0.1 MHz with a strength   = 40 MHz would yield a typical fidelity of 90% after 100 μs, a remarkable storage time compared to the lifetime of the cavity mode (10 μs) and the typical dephasing time of the ensemble (1 μs).
063810-5


 I. DINIZ et al. PHYSICAL REVIEW A 84, 063810 (2011)
B. Quantum memory based on two emitter distributions
We focus now on a second type of quantum memory based on two distributions of emitters allowing cavity protection, respectively detuned by +δ and −δ with respect to a cavity. Note that the case of a mode coupled to two such discrete emitters of ground and excited states |gi〉 and |ei〉 is exactly solvable, with the poles of the transmission revealing the complex eigenfrequencies of the system [24]. In particular, when the emitters are on resonance with the mode (δ = 0), the
antisymmetrical state (|e1,g2〉 − |g1,e2〉)/√2 is not coupled to the electromagnetic field. This dark state is naturally protected against spontaneous emission in the cavity, a property that can be used to store quantum information during a typical time scale given by the atomic dephasing time. Note that for artificial atoms like superconducting qubits or quantum dots this time can be quite short, which is a severe drawback for quantum computation on a chip. Here we suggest an experiment to prepare and exploit this dark state as a quantum memory in the case where the discrete emitters are replaced by broad assemblies of atoms. This proposal allows us to benefit from the collective atoms-cavity coupling, while the storage time now corresponds to the dephasing time of individual emitters and is thus potentially quite long. Note that this idea is typical of the so-called hybrid-circuit technology [3–6]. First, we have checked the validity of the effective model if two ensembles are coupled to the cavity. We have plotted in Fig. 6(a) the exact transmission |t(ω)|2 of a cavity coupled to two Gaussian ensembles and have verified that the position of the peaks are fitted by the eigenenergies computed in the discrete case. Moreover, we have superimposed the transmission resulting from the exact calculation and from the discrete model, as can be seen in Fig. 6(b) after focusing on the central peak of the transmission pattern: the excellent agreement between the two plots fully validates the effective approach. This central peak corresponds to the eigenstate |ψd 〉 resulting from the coupling between the cavity mode and the antisymmetric
δ/Δ
Frequency(units of Δ)
(a)
0 10 20 30 40 50 60 70 80
−100
0
100
−0.4 −0.2 0 0.2 0.4
0
0.5
1
Frequency (units of Δ)
|t(ω)|2
(b)
−0.4 −0.2 0 0.2 0.4
0
0.5
1
Frequency (units of Δ)
|t(ω)|2
(c)
FIG. 6. (Color online) (a) Transmission of a cavity coupled to two Gaussian distributions of emitters, each detuned by +δ and −δ from the cavity frequency; δ is swept from 0 to 8 MHz. We took   = 1 MHz,   = 0.1 MHz, κ = 0.5 MHz, γ = 10−4 MHz. (b) Focus on the central peak with δ = 0.5 MHz. Solid red line, Gaussian profile; blue dashed line, two emitters of homogeneous linewidth γ . (c) As in (b) for δ = 0.15 MHz.
state |A〉 = (|G1,S2〉 − |S1,G2〉)/√2, with its expression be
ing |ψd 〉 = (iδ|1,G1,G2〉 +  √2|0,A〉)/√δ2 + 2 2. When δ    , the excitation is mostly in the cavity and is mostly in the matter field in the opposite case. This change of nature clearly appears in the narrowing of the peak while decreasing δ, as can be seen in Fig. 6 and confirmed by the expression for its linewidth d = (δ2κ + 2 2γ )/(δ2 + 2 2). Note that this modeling might explain some recent experimental results [8], in which a superconducting cavity is strongly coupled to a inhomogeneous ensemble of nitrogen-vacancy centers of spin 1. Because of the geometrical strain, the transitions |mS = 0〉 → |mS = 1〉 and |mS = 0〉 → |mS = −1〉 are nondegenerate, which can be modeled by two ensembles of emitters of different central frequencies. The visible presence of a narrow peak at the cavity frequency explains qualitatively the effect discussed above. Coming back to the general case of two distinct ensembles, the state |ψd 〉 could provide a new type of quantum memory, as mentioned in the beginning of this section. The protocol consists in feeding the cavity mode with a single photon while the ensembles are largely detuned, thus preparing the state |1,G1,G2〉, and then adiabatically transferring the excitation to |ψd 〉 by slowly lowering δ. Yet the ensembles cannot be brought to resonance with the mode as would be the case for two discrete emitters. As seen in Fig. 6(c), the effective model breaks down when δ ∼  . At this point, indeed, the distributions of emitters start to spectrally overlap with the central peak, leading to its broadening. This yields a minimal linewidth d ∼ γ + ( 2/2 2)κ, allowing us to typically reduce the cavity losses by ( / )2. Here again the ratio ( / )2 appears as a major figure of merit for devices based on inhomogeneous ensembles strongly coupled to cavities.
VII. CONCLUSION
We have shown that if an inhomogeneous distribution of emitters is strongly coupled to a cavity, the ensemble can be treated as a single effective emitter collectively coupled to the mode, whose relaxation is governed by the single emitter’s properties, provided that their spectral distribution decreases faster than 1/ω2. This effect, called “cavity protection,” offers promising perspectives in the framework of quantum information with solid-state integrable devices, particularly regarding the implementation of long-lived high-fidelity quantum memories. These results are quite general and can fruitfully be applied to numerous important physical systems, ranging from semiconductor emitters coupled to optical cavities to ensembles of spins in circuit QED.
ACKNOWLEDGMENTS
The authors gratefully thank Z. Kurucz, K. Mølmer, G. Nogues, J. Claudon, M. F. Santos, and D. Est`eve for all the fruitful exchanges. This work was supported by the NanoSci-ERA consortium, by the EU under ERANET project LECSIN, by the European project SOLID, by the Nanosciences Foundation of Grenoble, and by ANR projects CAFE and QINVC. I.D. acknowledges the CAPES. I.D., S.P., and A.A. thank the Center for Quantum Technologies of Singapore.
063810-6


 STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . . PHYSICAL REVIEW A 84, 063810 (2011)
APPENDIX A: DYNAMICS
In this appendix, we establish the link between the complex transmission of the cavity and the evolution of the system if the mode a is initially fed with a single photon. This evolution is governed by the set of equations (1) written in the free frame (ω = 0). The input fields are in vacuum, and the state of the system is |1,G〉 = a†(0)|0〉, where |0〉 is the ground state of the total system. We are interested in the quantities 〈a(t)a†(0)〉 and 〈bk(t)a†(0)〉, which represent the probability amplitudes of the excitation in the cavity mode and in each emitter, respectively, as will be shown later. The average values are taken in state |0〉. We get
〈a ̇(t)a†(0)〉 = −(κ/2 + iω0)〈a(t)a†(0)〉 + ∑
k
gk 〈bk (t )a† (0)〉,
〈b ̇k(t)a†(0)〉 = −(γ /2 + iωk)〈bk(t)a†(0)〉 − gk〈a(t)a†(0)〉.
(A1)
The vector |ψ〉, defined as (〈a(t)a†(0)〉, . . . , 〈bk(t)a†(0)〉, . . .), evolves in time following the
Schr ̈odinger-like equation  ̄h d
dt |ψ〉(t) = −iHeff|ψ〉(t), with
Heff/ ̄h =
⎛
⎜⎜⎜⎜⎝
ω ̃ 0 ig1 ig2 . . .
−ig1 ω ̃ 1
−ig2 ω ̃ 2
... . . .
⎞
⎟⎟⎟⎟⎠
. (A2)
We have used the complex frequencies for the cavity ω ̃ 0 and for the emitters ω ̃ k defined above. Note that these results are in full agreement with the ones obtained in the Green function formalism by Kurucz et al. [12]. It appears that the dynamics of the problem can be modeled with the effective Hamiltonian Heff. In particular, one can define an
effective evolution operator O(t ) = eiHefft/ ̄hOe−iHefft/ ̄h, such that 〈a(t)a†(0)〉 = 〈0|a(0)e−iHefft/ ̄ha†(0)|0〉. This quantity can be rewritten 〈1,G|e−iHefft/ ̄h|1,G〉, justifying that we talk of the probability amplitude of the excitation in the cavity mode, starting from the initial state |1,G〉. The problem is solved using, e.g., the standard Laplace transform method. Defining
L(f (t)) = F (s) = ∫ ∞
0 exp(st)f (t)dt, we have
|ψ(t)〉 = L−1((s + iHeff/ ̄h)−1|ψ(0)〉), (A3)
where we have used the Laplace transform property L{ d
dt |ψ(t)〉} = s| (s)〉 − |ψ(0)〉. We finally define t1(s) =
〈1,G|(s + iHeff/ ̄h)−1|1,G〉. Inverse Laplace transform of this
coefficient gives back the quantity 〈1,G|e−iHeff/ ̄ht |1,G〉. We easily get
t1(s) = 1
s + iω ̃ 0 + ∑
k
g2
k s+iω ̃ k
. (A4)
From Eqs. (3) and (A4), we finally write the link between the transmission coefficient in amplitude t(ω) and the coefficient t1(s) characterizing the dynamics of the system,
t(ω) = − κ
2 t1(−iω). (A5)
This establishes the relation between the amplitude α1(t) =
〈1,G|e−iHefft/ ̄h|1,G〉 and the transmission t(ω) as ∫∞
0
α1(t)eiωt dt = − 2
κ t(ω). (A6)
One can use the method exposed above to compute the expression of the probability amplitude for a state initially prepared in |ψ0+(δ)〉, namely, 〈ψ0+(δ)|e−iHefft/ ̄h|ψ0+(δ)〉 studied in Sec. VI. In general, we can decompose it as
〈ψ 0
+(δ)|Ueff(t )|ψ 0
+(δ)〉
= cos2(θ/2)〈1,G|Ueff|1,G〉 + sin2(θ/2)〈0,S|Ueff|0,S〉
+ i sin(θ/2) cos(θ/2)(〈0,S|Ueff|1,G〉 − 〈1,G|Ueff|0,S〉)
= cos2(θ/2)α1(t) + sin2(θ/2)α2(t)
+ i sin(θ/2) cos(θ/2)[α3(t) − α4(t)], (A7)
where Ueff (t ) ≡ e−iHefft/ ̄h. We need only to calculate the four matrix elements αi(t). Defining ti(s) = L(αi(t)), we obtain, in the case of a continuous distribution,
t2(s) = − W (is)
 2 t1(s)(s + iω ̃o),
t3(s) = t1(s) iW (is)
  , (A8)
t4(s) = −t3(s).
APPENDIX B: W (ω) FOR SPECIFIC DISTRIBUTIONS
We now evaluate the function W (ω) for all the specific continua analyzed in this paper. This function allows the evaluation of the complex transmission using t(ω) = (κ/2i)[ω − ω0 + iκ/2 − W (ω)]−1 but also appears in other formulas.
1. Gaussian distribution
The Gaussian distribution is written ρ(ω) =
√ln 2
 √π e−(ω2 ln 2)/ 2 . W (ω) is thus
WG(ω) = 1
i
√ln 2  2

√π
⎡
⎣i π
∫∞
−∞
d ω′ e−ω′2
( ω+iγ /2
 /√ln 2 − ω′)
⎤
⎦ . (B1)
Remembering that
i
π
∫∞
−∞
dω′ e−ω′2
z − ω′ = e−z2 erfc(−iz), (B2)
where erfc is the complex complementary error function, it becomes
WG(ω) = −i
√ln 2  2

√π e−( ω+iγ /2
 /√ln 2 )2
erfc
(
−i ω + iγ /2
 /√ln 2
) .
(B3)
2. Rectangular distribution
In the case of a rectangular distribution, the density of emitter is ρ(ω) = 1
  [ (ω −  /2) −  (ω +  /2)], and we
063810-7


 I. DINIZ et al. PHYSICAL REVIEW A 84, 063810 (2011)
have
WR(ω) = 2 2
i  arctan
(
γ − 2iω
)
. (B4)
3. Lorentzian distribution
The density of the emitter is ρ(ω) =  /2
π
1
( /2)2+ω2 ; thus
WL(ω) =  2
ω + iγ /2 + i /2 . (B5)
From the equation above we see that for the Lorentzian distribution we do not achieve cavity protection; i.e., the inhomogeneous broadening always contributes as if it were homogeneous.
APPENDIX C: DEVELOPMENT WITH FINITE γ
We start by rewriting W (ω) from Eq. (4) as
W (ω) =  2
∫∞
−∞
dω′ ω′2
ω′2 + γ 2
ρ(ω′ + ω) ω′
− iπ  2
∫∞
−∞
dω′ γ
π (ω′2 + γ 2) ρ(ω + ω′). (C1)
The integrands contain products of a function of width γ and another with width  . If γ    , the integrals take the form
W (ω) =  2P
∫∞
−∞
ρ (ω′ )d ω′ ω − ω′
− i 2
(
πρ(ω) + γ
2P
∫∞
−∞
ρ (ω′ )d ω′
(ω − ω′)2
)
. (C2)
We are interested in the development of W (ω) near the poles of the transmission function in the absence of inhomogeneous broadening, namely, ω ∼  . Denoting r = ω′/ω and using the
identity ∑ rk = 1/(1 − r), we find
W (ω) =  2
ω
[
1+
∞ ∑
k=1
μk
ωk − iπρ(ω)
]
− i  2
ω2
γ
2
[
1+
∑ ∞
k=1
(k + 1) μk
ωk
]
, (C3)
where μk is the kth moment of the distribution ρ(ω) about its origin,
μk ≡
∫∞
−∞
dωρ(ω)ωk. (C4)
Note that this development is only valid if ω   ω′, which is the case in the present study as ω ∼       > ω′. From the normalization and considering only symmetric distributions, we have μ0 = 1 and μ1 = 0. μ2 gives the first nonzero correction, and it is typically proportional to the square of the FWHM [as an example, μ2 =  2/(2 ln 2) in the case of a Gaussian distribution]. To first nonzero correction we have
W (ω) =  2
ω (1 + μ2/ω2) − i
[γ
2
 2
ω2 + π  2ρ(ω)
]
=  2(1 + μ2/ω2)
ω + iγ /2 − iπ  2ρ(ω), (C5)
where we have used     γ . One easily infers the modifications to the transmission poles induced by inhomogeneous broadening. They are located at
ω± = ±
√
1 + μ2/  2 −
( κ + 2πρ( ) 2 − γ
4
)2
. (C6)
Their width check = κ+γ +2π 2ρ( )
2 , in correspondence
with what was stated in Sec. III. Note that this procedure is only valid for a distribution with well-defined moments. This is not the case of the Lorentzian; nevertheless, W (ω) can be exactly evaluated in this case. The exact calculations for the three cases taken under consideration are the subject of Appendix B.
APPENDIX D: TWO WAYS TO OBTAIN THE TEMPORAL EVOLUTION
We have found two ways to evaluate α1(t) =
〈1,G|e−iHefft/ ̄h|1,G〉; the first, in Appendix A, uses a LaplaceFourier transform of −t(ω)/(κ/2), and the second uses the standard Fourier transform of 2π  2 ρ(ω)|t(ω)/(κ/2)|2 for κ,γ → 0 as in Sec. IV. The first way is more general in the sense that it can include emitter and cavity radiative losses; the second describes a reversible process that originates in a Hamiltonian evolution. We now show that both ways coincide when we disregard losses. From Appendix A we have ∫∞
0
α1(t)eiωt dt = t1(−iω), (D1)
where, if γ ,κ → 0,
t1(−iω) = i
ω − ω0 −  2P ∫ ρ(ω′)dω′
ω−ω′ + iπ  2ρ(ω) . (D2)
We now take the real part of Eqs. (D1) and (D2), yielding
Re
{∫ ∞
0
α1(t )eiωt dt
}
= Re
{ i
ω − ω0 −  2P ∫ ρ(ω′)dω′
ω−ω′ + iπ  2ρ(ω)
}
= π  2ρ(ω)|t1|2 ; (D3)
if we consider time reversibility of the lossless dynamics, we have α1(−t) = [α1(t)]∗ and thus
2Re
{∫ ∞
0
α1(t )eiωt dt
} =
∫∞
0
[α1(t )eiωt + α∗
1 (t )e−iωt ]dt
=
∫∞
−∞
α1(t)eiωt dt. (D4)
Equations (D3) and (D4) together give ∫∞
−∞
α1(t)eiωt dt = 2π  2 ρ(ω)|t1|2, (D5)
which is precisely what we find by applying the inverse Fourier transform in Eq. (12). Note we had to use the time reversibility, which is only valid in the lossless case.
063810-8


 STRONGLY COUPLING A CAVITY TO INHOMOGENEOUS . . . PHYSICAL REVIEW A 84, 063810 (2011)
[1] Y. Kaluzny, P. Goy, M. Gross, J. M. Raimond, and S. Haroche, Phys. Rev. Lett. 51, 1175 (1983). [2] C. Weisbuch, M. Nishioka, A. Ishikawa, and Y. Arakawa, Phys. Rev. Lett. 69, 3314 (1992). [3] A. Imamoglu, Phys. Rev. Lett. 102, 083602 (2009). [4] J. Verdu, H. Zoubi, C. Koller, J. Majer, H. Ritsch, and J. Schmiedmayer, Phys. Rev. Lett. 103, 043603 (2009). [5] P. Rabl, D. DeMille, J. M. Doyle, M. D. Lukin, R. J. Schoelkopf, and P. Zoller, Phys. Rev. Lett. 97, 033003 (2006). [6] J. H. Wesenberg, A. Ardavan, G. A. D. Briggs, J. J. L. Morton, R. J. Schoelkopf, and D. I. Schuster, Phys. Rev. Lett. 103, 070502 (2009). [7] J. M. Taylor, C. M. Marcus, and M. D. Lukin, Phys. Rev. Lett. 90, 206803 (2003). [8] Y. Kubo et al., Phys. Rev. Lett. 105, 140502 (2010). [9] D. I. Schuster et al., Phys. Rev. Lett. 105, 140501 (2010). [10] M. Gross and S. Haroche, Phys. Rep. 93, 301 (1982). [11] R. Houdr ́e, R. P. Stanley, and M. Ilegems, Phys. Rev. A 53, 2711 (1996). [12] Z. Kurucz, J. H. Wesenberg, and K. Molmer, Phys. Rev. A 83, 053852 (2011).
[13] Z. Kurucz, M. W. Sorensen, J. M. Taylor, M. D. Lukin, and M. Fleischhauer, Phys. Rev. Lett. 103, 010502 (2009). [14] C. W. Gardiner and M. J. Collett, Phys. Rev. A 31, 3761 (1985). [15] X.-H. Wang, R. Wang, B. Y. Gu, and G. Z. Yang, Phys. Rev. Lett. 88, 093902 (2002). [16] C. B. Murray et al., Science 270, 1335 (1995). [17] J. Y. Marzin, J.-M. G ́erard, A. Izrael, D. Barrier, and G. Bastard, Phys. Rev. Lett. 73, 716 (1994). [18] D. Hone et al., Phys. Rev. 186, 291 (1969). [19] D. L. Orth et al., J. Phys. Condens. Matter 5, 2533 (1993). [20] A. A. L. Nicolet et al., Chem. Phys. Chem. 8, 1215 (2007). [21] L. C. Andreani, G. Panzarini, and J.-M. G ́erard, Phys. Rev. B 60, 13276 (1999). [22] A. Auff`eves, B. Besga, J.-M. G ́erard, and J. P. Poizat, Phys. Rev. A 77, 063833 (2008). [23] U. Fano, Phys. Rev. 124, 1866 (1961). [24] J. M. Fink, R. Bianchetti, M. Baur, M. Goppl, L. Steffen, S. Filipp, P. J. Leek, A. Blais, and A. Walraff, Phys. Rev. Lett. 103, 083601 (2009).
063810-9
