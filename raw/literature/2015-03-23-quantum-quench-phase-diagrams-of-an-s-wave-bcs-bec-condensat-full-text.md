# Quantum quench phase diagrams of an s -wave BCS-BEC condensate - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.91.033628
> Collected: 2026-09-20
> Published: 2015-03-23
> Zotero parent key: KC2S76NI
> Evidence: Publisher or author-preprint PDF

PHYSICAL REVIEW A 91, 033628 (2015)


                    Quantum quench phase diagrams of an s-wave BCS-BEC condensate

                                    E. A. Yuzbashyan,1 M. Dzero,2 V. Gurarie,3 and M. S. Foster1,4
                          1
                              Center for Materials Theory, Rutgers University, Piscataway, New Jersey 08854, USA
                                     2
                                       Department of Physics, Kent State University, Kent, Ohio 44240, USA
                                3
                                  Department of Physics, University of Colorado, Boulder, Colorado 80309, USA
                              4
                                Department of Physics and Astronomy, Rice University, Houston, Texas 7700, USA
                                             (Received 9 January 2015; published 23 March 2015)

                 We study the dynamic response of an s-wave BCS-BEC (atomic-molecular) condensate to detuning quenches
              within the two-channel model beyond the weak-coupling BCS limit. At long times after the quench, the condensate
              ends up in one of three main asymptotic states (nonequilibrium phases), which are qualitatively similar to those
              in other fermionic condensates defined by a global complex order parameter. In phase I the amplitude of the
              order parameter vanishes as a power law, in phase II it goes to a nonzero constant, and in phase III it oscillates
              persistently. We construct exact quench phase diagrams that predict the asymptotic state (including the many-body
              wave function) depending on the initial and final detunings and on the Feshbach resonance width. Outside of
              the weak-coupling regime, both the mechanism and the time dependence of the relaxation of the amplitude of
              the order parameter in phases I and II are modified. Also, quenches from arbitrarily weak initial to sufficiently
              strong final coupling do not produce persistent oscillations in contrast to the behavior in the BCS regime. The
              most remarkable feature of coherent condensate dynamics in various fermion superfluids is an effective reduction
              in the number of dynamic degrees of freedom as the evolution time goes to infinity. As a result, the long-time
              dynamics can be fully described in terms of just a few new collective dynamical variables governed by the
              same Hamiltonian only with “renormalized” parameters. Combining this feature with the integrability of the
              underlying (e.g., the two-channel) model, we develop and consistently present a general method that explicitly
              obtains the exact asymptotic state of the system.

              DOI: 10.1103/PhysRevA.91.033628                                PACS number(s): 67.85.De, 34.90.+q, 74.40.Gh


                     I. INTRODUCTION                                     strength of the quench: Volkov-and-Kogan-like behavior,
                                                                         persistent oscillations, and exponential vanishing of the order
    The problem of a superconductor driven out of equilibrium
                                                                         parameter. Most recent research [27–30] fueled by exper-
by a sudden perturbation goes back many decades. Early
                                                                         imental breakthroughs [25,31,32] investigates nonadiabatic
studies [1–6] addressed small deviations from equilibrium
                                                                         dynamics of s-wave BCS superconductors in response to fast
using linearized equations of motion. An important result was
                                                                         electromagnetic perturbations. Closely related subjects devel-
obtained by Volkov and Kogan [3], who discovered a power                 oping in parallel are exciton dynamics [33], collective neutrino
law oscillatory attenuation of the Bardeen-Cooper-Schriffer              oscillations [34,35], quenched p-wave superfluids [36,37], etc.
(BCS) order parameter for nonequilibrium initial conditions                 Most existing work addressed the dynamics in the BCS
close to the superconducting ground state.                               regime and, in particular, quenches such that the interaction
    In the past decade it was realized that even large deviations        strength is weak both before and after the quench. This was
from equilibrium are within the reach of appropriate theo-               so that the system always remains in the BCS regime, since
retical methods. Recent studies, motivated by experiments                the physics of the condensate beyond this regime was not
in cold atomic fermions, focused on quantum quenches,                    sufficiently well understood. However, a superfluid made up
nonequilibrium conditions created by a sudden change in                  of cold atoms can be as well quenched from the BCS to
the superconducting coupling strength. Barankov et al. [7],              the Bose-Einstein condensation (BEC) regime or within the
in a paper that set off a surge of modern research in this               BEC regime. With few exceptions [23,36,37], these types of
long-standing problem [8–24] in the context of quantum gases,            quenches are not adequately studied in the existing literature.
found that for initial conditions close to the unstable normal              Our paper aims to close this gap and analyze all possible
state, the order parameter exhibits large anharmonic periodic            interaction quenches throughout the BCS-BEC crossover in a
oscillations.                                                            paired superfluid, including BCS-to-BEC, BEC-to-BCS, and
    Subsequently, Yuzbashyan et al. [16] developed an ana-               BEC-to-BEC quenches. We fully determine the steady state of
lytical method to predict the state of the system at large               the system at large times after the quench: the asymptote of the
times based on the integrability of the underlying BCS model.            order parameter, as well as the approach to the asymptote; the
This work extended Volkov and Kogan’s result to large                    many-body wave function; and certain observables, such as
deviations from equilibrium and showed that the oscillation              the radio-frequency absorption spectrum and the momentum
frequency is twice the nonequilibrium asymptotic value of the            distribution. In the BCS limit, we recover previous results.
order parameter, a conclusion confirmed by recent terahertz              Beyond this limit the dynamics is quantitatively and some-
pump pulse experiments in Nb1-x Tix N films [25,26]. Later               times qualitatively different. For example, the power law in
studies [17,18] mapped out the full quantum quench “phase                the Volkov-and-Kogan-like attenuation changes in the BEC
diagram” for weakly coupled s-wave BCS superconductors                   regime, exponential vanishing is replaced with a power law,
finding that three distinct regimes occur depending on the               and persistent oscillations first change their form and then

1050-2947/2015/91(3)/033628(43)                                   033628-1                                 ©2015 American Physical Society
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                        PHYSICAL REVIEW A 91, 033628 (2015)

disappear altogether after a certain threshold for quenches        effective interaction (coupling) between fermions increases
from any initial (e.g., arbitrarily weak) to sufficiently strong   from weak to strong and the system undergoes a BCS-BEC
final coupling. We believe an experimental verification of         crossover. At ω  2εF , where εF is the Fermi energy, the
the predictions of this work is within a reach of current          system is deep in the BCS regime, while at large negative ω
experiments in cold atomic systems.                                it is deep in the BEC regime. It is not known how to recreate
    The long-time dynamics can be determined explicitly due        such a crossover in a conventional solid-state superconductor
to a remarkable reduction mechanism at work, so that at large      since the interaction strength cannot be easily adjusted.
times the system is governed by an effective interacting Hamil-        In a quantum quench setup the system is prepared in the
tonian with just a few classical collective spin or oscillator     ground state at a detuning ωi . At t = 0 the detuning is suddenly
degrees of freedom. In a sense, the system “flows in time” to a    changed, ωi → ωf . At t > 0 the system evolves with a new
much simpler Hamiltonian. This observation, combined with          Hamiltonian H (ωf ). The main goal is to determine the state
the integrability of the original Hamiltonian (see below), lead    of the system at large times, t → ∞.
to a method originally proposed in Ref. [16] for obtaining the
long-time asymptote (steady state) of integrable Hamiltonian
dynamics in the continuum (thermodynamic) limit. Here we                             A. Models and approximations
improve this method as well as provide its comprehensive and          We consider two closely related models in this paper in both
self-contained review including many previously unpublished        two and three dimensions. The first one is the well-known
results and steps. We do so in the context of the s-wave           two-channel model that describes two species of fermionic
BCS (one channel) and inhomogeneous Dicke (two-channel)            atoms interacting via an s-wave Feshbach resonance
models, but with some modifications the same method also
applies to all known integrable pairing models [38–44], such                                                q2
                                                                                                                  
                                                                                              †
as p + ip superfluids [36,37], integrable fermion or boson          Ĥ2ch =              p âpσ âpσ +     ω+     b̂q† b̂q
                                                                              p,σ =↑,↓                    q
                                                                                                               4m
pairing models with nonuniform interactions [45,46], Gaudin
magnets (central spin models), and potentially can be extended                                                        †         †      
                                                                              +g     b̂q† â q2 +p,↑ â q2 −p,↓ + b̂q â q −p,↓ â q +p,↑ . (1.1)
to a much broader class of integrable nonlinear equations.                                                            2        2
                                                                                    pq
    The purpose of this paper is therefore twofold. First, it
serves as an encyclopedia of quantitatively exact predictions,
                                                                   It is convenient to think of the two types of fermions of mass
new and old, for the quench dynamics of real s-wave BCS-BEC
                                                                   m and energy p = p2 /2m as spin-up and spin-down, created
condensates in two and three spatial dimensions. Readers                                            †
primarily interested in this aspect of our work will find most     and annihilated by operators âpσ and âpσ . The interaction term
of the relevant information in the Introduction, Sec. VII,         converts two fermions into a bosonic molecule and vice versa
and Conclusion. In particular, Sec. I D concisely summarizes       at a rate controlled by the parameter g. Molecules are created
                                                                                          †
our main results and provides a guide to other sections that       and annihilated by b̂q and b̂q and have a binding energy ω.
contain further results and details. Our second goal is to         The parameter g is set by the type of atoms and the specifics
develop and thoroughly review a method for determining the         of a particular Feshbach resonance and cannot be changed
far-from-equilibrium dynamics in a certain class of integrable     in a single experiment; ω can be varied at will by varying the
models. We refer readers interested in learning about the          magnitude of the magnetic field applied during the experiment.
method to Sec. II. Also, from this viewpoint, Secs. III and IV     This model describes atoms in the BCS regime when ω is
should be considered as applications of our approach and           large, which undergo a crossover to the BEC regime as ω is
Sec. V as a related development.                                   decreased.
    A major experimental breakthrough with ultracold atoms             A parameter with dimensions of energy important for our
was achieved in 2004, when they were used to emulate s-wave        analysis of this model is g 2 νF , where νF is the bulk density of
superconductors with an interaction strength that can be varied    states (proportional to the total volume) at the Fermi energy
at will [47,48]. The experimental control parameter is the         F . A well-known parameter,
detuning ω, the binding energy of a two-fermion bound state
(molecule). This parameter determines the strength of the                                                 g 2 νF
                                                                                                  γ =            ,                        (1.2)
effective interaction between fermions and can be varied both                                              F
slowly and abruptly with the help of a Feshbach resonance.
Moreover, it is straightforward to make time-resolved mea-         controls whether the resonance is narrow γ  1 or broad
surements of the subsequent evolution of the system. Thus,         γ  1. This parameter is the dimensionless atom-molecule
cold atoms provide a natural platform to study quenches in         interaction strength or, equivalently, the resonance width.
superfluids and in a variety of other setups [49,50].                 A very convenient feature of the narrow resonance is that,
    At large ω we have fermionic atoms with weak effective         regardless of the regime of the system, controlled by ω, the
attraction that form a paired superfluid, an analog of the         system is adequately described with mean-field theory [53].
superconducting state of electrons in a metal. As ω is             This is already clear from the form of the Hamiltonian: Small
decreased, the atoms pair up into bosonic molecules which          γ implies that interaction g is small.
then Bose condense. It was argued for a long time that both           Broad resonances, on the other hand, correspond to large
the paired superfluid and the Bose-condensed molecules are in      g. Under those conditions it is possible to integrate out the
the same phase of the fermionic gas, named the BCS-BEC             molecules b̂q to arrive at a simpler Hamiltonian [53] describing
condensate [51,52]. As ω decreases, the strength of the            fermions interacting via a short-range attractive interaction

                                                             033628-2
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                          PHYSICAL REVIEW A 91, 033628 (2015)

with variable strength,                                                        therefore becomes
                                                                                                                    
                                                                                  Ĥ2ch =    2p ŝpz + ωb̂† b̂ + g  (b̂† ŝp− + ŝp+ b̂),      (1.5)
                                  †
        Ĥ1ch =              p âpσ âpσ                                                      p                            p
                  p,σ =↑,↓
                                                                               where
                     λ  †           †                                                                            †                         
                  −         â q   â q   â q +p ,↑ â q2 −p ,↓ ,   (1.3)                                                    †
                                                                                    ŝp− = âp↑ â−p↓ , ŝpz = 12 âp↑ âp↑ + â−p↓ â−p↓ − 1    (1.6)
                    νF pp q 2 −p,↓ 2 +p,↑ 2
                                                                               are Anderson pseudospin- 12 operators [1] and
where
                                                                                                             b̂ = b̂q=0 .
                            g 2 νF   γ εF
                         λ=        =      .                            (1.4)   Hamiltonian (1.5) is also known as inhomogeneous Dicke
                              ω       ω                                        or Tavis-Cummings model. In a quantum quench problem
                                                                               we need to solve Heisenberg equations of motion for this
This is the single (one)-channel, or BCS, model, which is
                                                                               Hamiltonian for given initial conditions
the second model we analyze in this paper. It also describes
the BCS-BEC crossover as ω is decreased (λ is increased).                                   d sˆp                   d b̂
However, while in the BCS and (to some extent) in the BEC                                          = Bˆ p × sˆp ,        = −iωb̂ − ig Jˆ− ,
                                                                                            dt                      dt
regimes corresponding to large and small λ, respectively,                                                                                       (1.7)
mean-field theory holds in equilibrium, for the intermediate                                    Jˆ =      sˆp , Bˆ p = 2g bˆ + 2p ẑ,
values of λ (neither large nor small) the mean-field theory                                           p
is known to break down. A special value of λ in the middle
of the regime unaccessible to the mean-field theory already                    where bˆ = b̂x x̂ + b̂y ŷ, b̂x , and −b̂y are Hermitian and anti-
in equilibrium is called the unitary point. It corresponds to                  Hermitian parts of the operator b̂ = b̂x − i b̂y , and x̂,ŷ,ẑ are
the interaction strength where molecules are about to be                       coordinate unit vectors.
formed. Noncondensed molecules play an important role in                           The second step in the mean-field treatment of the two-
the description of the unitary point and its special properties                channel model is to replace Heisenberg operator b̂(t) in the
are a subject of many studies in the literature [52,54].                       first equation of motion in Eq. (1.7) with its time-dependent
    Just as in earlier work on the far-from-equilibrium su-                    quantum-mechanical average, b̂(t) → b̂(t) ≡ b(t), which is
perconductivity, we analyze the quench dynamics in the                         expected to be exact in thermodynamic limit as long as the
mean-field approximation where no molecules are transferred                    q = 0 state is macroscopically occupied at all times. This
into or out of the BCS-BEC condensate after the quench;                        replacement can be shown to be exact in equilibrium using
i.e., the dynamics of the condensate is decoupled from                         the exact solution for the spectrum of the inhomogeneous
the noncondensed modes. We analyze the validity of this                        Dicke model [38,57] and numerically for the time-dependent
approximation for nonequilibrium steady states produced by                     problem [58]. Upon this replacement equations of motion be-
quenches in the two-channel model in Appendix A. We find                       come linear in operators and taking their quantum-mechanical
that the situation is similar to that in equilibrium [53]. In the              average, we obtain
case of a broad Feshbach resonance, mean field is expected
to hold for quenches where both initial and final detunings                                   s˙p = Bp × sp , ḃ = −iωb − igJ− ,
are far from the unitary point. A quench into the unitary point                                                                                 (1.8)
is a very interesting problem addressed by some publications                                   J =     sp , Bp = 2g b + 2p ẑ,
before [55], but the method we employ here is not applicable                                          p

to this case.                                                                  where sp = sˆp . These are Hamiltonian equations of motion
    Nevertheless, a variety of quenches are still accessible to                for a classical Hamiltonian,
our description even when the resonance is broad, includ-                                                          
ing BCS → BCS, BCS → BEC, BEC → BCS, and BEC →                                       H2ch =      2p spz + ωb̄b + g  (b̄sp− + bsp+ ), (1.9)
BEC, where BCS and BEC stand for the value of the interaction                                   p                           p
strength far weaker or far stronger than that at the unitary point.
                                                                               which describes a set of angular momenta (classical spins or
In the case of BCS-BEC superfluids formed with interactions
                                                                               vectors) coupled to a harmonic oscillator. Here, b̄ denotes the
generated by narrow Feshbach resonances, the mean-field
                                                                               complex conjugate of b. These dynamical variables obey the
theory treatment is valid even at the threshold of the formation
                                                                               Poisson brackets
of the bound state and throughout the BCS-BEC crossover.                                     a b
Here we consider quenches of the detuning ω for both narrow                                  sp ,sk = −εabc δpk spc , {b,b̄} = i,       (1.10)
and broad resonances within the mean field. Note that in the
                                                                               where a, b, and c stand for spatial indicies x, y, and z.
case of the one-channel model we expect the mean field on the
                                                                                  Similar steps in the case of the single-channel model (1.3)
BEC side to be valid only in the far BEC limit where the ground
                                                                               lead to a classical spin Hamiltonian,
state essentially consists of noninteracting Bose-condensed
molecules [56].                                                                                                     λ  − +
                                                                                              H1ch =      2p spz −        s s ,        (1.11)
    In the mean-field treatment the condensate is described by
                                                                                                        p
                                                                                                                    νF p,p p p
the q = 0 part of the Hamiltonian (1.1), which is decoupled
from q = 0 terms in this approximation. The Hamiltonian                        together with the corresponding equations of motion.

                                                                         033628-3
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                        PHYSICAL REVIEW A 91, 033628 (2015)

   An important characteristic of the system both in and out                              Further, the Hamiltonian (1.9) conserves
of equilibrium is the superfluid order parameter or the gap                                                                 1
                                                                                                                                
function defined in the two-channel model as                                                             n = bb +        sp +
                                                                                                                          z
                                                                                                                                 ,                                (1.19)
                                                                                                                              2
        (t) = −g b̂(t) = −gb(t) ≡                x (t) − i
                                                                                                                    p
                                                                   y (t).   (1.12)
In the one-channel limit, this expression turns into                                 which is the average total number of bosons and fermion pairs.
                                                                                     This number is related to 0 and the chemical potential μ as
                  λ                       λ  −
       1ch (t) =      âp↑ (t)â−p↓ (t) =         s .                       (1.13)                    2 20        εp − μ
                 νF p                     νF p p                                               2n =       +   1−              .                                   (1.20)
                                                                                                       g2   p
                                                                                                                 E(εp ; 0 ,μ)
The magnitude | (t)| of the order parameter is known as
the Higgs or amplitude mode for its similarity with the                                 The Fermi energy εF is the chemical potential of the
Higgs boson [20,59] and its time-dependent phase represents                          fermionic atoms at zero temperature in the absence of any
a Goldstone mode. Note, however, that out of equilibrium                             interaction, when only fermions are present. It provides an
the gap function does not entirely determine the state of the                        overall energy scale and it is convenient to measure all energies
system. It specifies the effective magnetic field acting on each                     in units of the Fermi energy. Thus, from now on, we set
spin according to Eq. (1.8), but there is still a certain freedom                    everywhere below
in how the spin moves in this field. For example, even for
a constant field the spin can precess around it, making an                                                                 εF = 1.                                (1.21)
arbitrary constant angle with its direction.                                            Below we often switch from discrete to continuum (ther-
    In the above models we took a free single-particle spectrum,                     modynamic limit) formulations. In the former version, there
εp = p2 /2m, and labeled states with momenta p. This choice                          are N discrete single-particle energy levels εp with certain
is not essential for our analysis. We can as well consider an ar-                    degeneracy each. Any quantity Ap we consider in this paper
bitrary spectrum εi . The pairing is then between pairs of time-                     depends on p only through εp , Ap = A(εp ). For example, all
reversed states [60,61]; see also the first two pages in Ref. [13]                   spins sp on a degenerate level εp are parallel at all times
for more details. For example, in Hamiltonian (1.5) this results                     and effectively merge into a single vector. There are N such
                                                     †           †
in relabeling sˆp → sˆi , âp↑ â−p↓ → âi↑ âi↓ , âp↑ âp↑ → âi↑ âi↑ ,           vectors, so we count N distinct classical spins.
etc., where the state |i ↓ is the time-reversed counterpart of                          In thermodynamic limit, energies εp form a continuum
|i ↑ . Our results below depend only on the density of the                           on the positive real axis, i.e., are described by a continuous
single-particle states ν(ε) in the continuum limit regardless of                     variable ε with a density of states ν(ε) that depends on the
whether these states are characterized by momenta p or any                           dimensionality of the problem
other set of quantum numbers i.
                                                                                                                  ν(ε) = νF f (ε),                                (1.22)
                               B. Ground state                                       where νF is the bulk density of states (proportional to
   In the ground state                                                                                           √ energy, f (ε) = 1 in two
                                                                                     the system volume) at the Fermi
                                              −2iμt
                                                                                     dimensions (2D), and f (ε) = ε in 3D. Summations over
                                (t) =    0e           ,                     (1.14)   p turn into integrations,
where the magnitude 0 is time independent. Apart from                                                                                 ∞
an overall rotation about the z axis with frequency 2μ, the                                                 Ap → νF                        A(ε)f (ε)dε.           (1.23)
                                                                                                                                   0
ground state is a static solution of the equations of motion that                                      p
minimizes H2ch . The minimum is achieved when each spin is                                With only fermions present, the total particle number is
directed against its effective magnetic field, i.e.,
                                                                                                                       1
                       −2iμt                                                                                                                   4
                  0e                              εp − μ                                                   2n =            2ν(ε)dε =             νF ,             (1.24)
     sp− =                        ,   spz = −                 ,             (1.15)                                 0                           d
             2E(εp ;      0 ,μ)                 2E(εp ; 0 ,μ)
                                                                                     where d = 2,3 is the number of spatial dimensions. Interaction
where
                                                                                     redistributes this number between fermions and bosons as in
                  E(ε;         ,μ) ≡    (ε − μ)2 +            2.            (1.16)   Eq. (1.20). Combining Eqs. (1.20) and (1.24) and taking the
                                                                                     continuum limit, we obtain
Note that the length of the spin sp = 1/2. This is because the                                             ⎡                    ⎤
ground state is a tensor product of single spin- 12 wave functions                                       ∞
                                                                                                           ⎣1 −  ε − μ
                                                                                                2
                                                                                       4     2 0
and sp = sˆp .                                                                            =       +                             ⎦ f (ε)dε, (1.25)
                                                                                       d      γ        0         (ε − μ)2 + 2
   The equation of motion (1.8) for b yields                                                                                                      0

                                      (ω − 2μ)        0                              where γ is the dimensionless resonance width defined in
                         |J− | =                          ,                 (1.17)
                                          g2                                         Eq. (1.2).
which implies a self-consistency equation for 0                                        Similarly, Eq. (1.18) becomes in the thermodynamic limit

              (ω − 2μ)               1                                                             2ω − 4μ                    ε
                                                                                                                                            f (ε)dε
                         =                    .                             (1.18)                          =                                                ,   (1.26)
                  g 2           2E(εp ; 0 ,μ)                                                          γ                   0           (ε − μ)2 +         2
                             p                                                                                                                            0


                                                                               033628-4
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                       PHYSICAL REVIEW A 91, 033628 (2015)

                                                                              Bogoliubov amplitudes up (t),vp (t) obey the Bogoliubov de
                                                                              Gennes (BdG) equations
           0
                                                                                                                       
                                                                                      ∂ up (t)       p        (t)   up (t)
                                                                                    i            = ¯                          ,    (1.31)
                                                                                      ∂t vp (t)       (t) −p        vp (t)
       F -4
                                                                              with the normalization condition |up |2 + |vp |2 = 1. Apart
                                                                              from an overall time-dependent phase (which is important
                                                                              for certain observables), these equations are equivalent to the
         -8
                                                                              classical spin equations of motion (1.8) and spins are related
                                                                              to the amplitudes as

        -12                                                                                 sp−                 spz
           0         0.2      0.4          0.6             0.8   1                                = 2up v p ,         = |vp |2 − |up |2 ,   (1.32)
                                                                                            sp                  sp
                                         max
                                                                              where sp is the length of the spin. For quench initial conditions
    FIG. 1. (Color online) Ground-state chemical potential μ for the          sp = 1/2, as explained below Eq. (1.16).
two-channel model in 3D in units of the Fermi energy εF as a function            Each quench is uniquely characterized by three parameters:
of the ground-state gap 0 for various resonance width γ . μ( 0 ) is           the resonance width γ = g 2 νF and the initial ωi and final ωf
calculated from Eqs. (1.25) and (1.26). Note that in the two-channel          values of the detuning in units of the Fermi energy. Indeed,
model 0 is bounded from above by max .                                        ωi and γ determine 0i and μi and thus the initial condition,
                                                                              while the equations of motion (1.7) in the thermodynamic limit
where ε is the high-energy cutoff. In 3D it can be eliminated                 depend only on ωf and γ . To see the latter, note that model
by an additive renormalization of the detuning ω; see, e.g.,                  parameters enter the equation of motion for spin sp ≡ s(εp )
Ref. [53]. This, however, does not affect our results for the                 only through = −gb, while the equation of motion for the
quench dynamics as they depend on the difference between                      bosonic field b can be equivalently written as
the initial and final values of the detuning.                                                                       ∞
   Equations (1.25) and (1.26) contain two independent                                  ˙ = −iωf        + iγ            s − (ε)f (ε)dε.     (1.33)
parameters not counting the cutoff. For example, we can                                                         0

choose γ and ω and determine μ and 0 from these equations,                        Instead of ωi ,ωf we find it more convenient to characterize
or choose γ and 0 and determine μ and ω etc.; see Fig. 1 for a                the quench by 0i , 0f , the ground-state gaps corresponding
plot of μ( 0 ) for various γ in 3D. Note also that 20 = g 2 b̄b is            to these values of the detuning. As discussed below Eq. (1.26),
proportional to the number of bosons and is therefore limited                 for a given γ , the detuning ω uniquely determines 0 and
by the total number of particles. Equation (1.25) implies                     vice versa. Note that 0f has nothing to do with the time-
                                                                             dependent gap function (t) and in particular with the large-
                                2γ                                            time asymptote (t → ∞). Whenever (t) goes to a constant
                         0 ⩽        = max .              (1.27)
                                 d                                            at large times, we denote this constant ∞ .

               C. Quench setup and initial conditions
                                                                                                         D. Main results
   In a quantum quench setup we prepare the system in a
                                                                                 Our main result is a complete description of the long-time
ground state at a certain detuning ωi ; i.e., the initial state is
                                                                              dynamics of two- and one-channel models (1.9) and (1.11)
                                                                              in two and three spatial dimensions following a quench of
                 sp− (t = 0) =
                                           0i
                                                           ,
                                 2E(εp ;        0i ,μi )                      the detuning ωi → ωf (coupling λi → λf in the one-channel
                                                                     (1.28)   model) in the thermodynamic limit. A key effect that makes
                                       εp − μi                                such a description possible is a drastic reduction in the number
                  spz (t = 0) = −                    ,
                                    2E(εp ; 0i ,μi )                          of effective degrees of freedom as t → ∞. It turns out that the
where 0i ,μi are the ground-state values determined by                        large-time dynamics can be expressed in terms of just a few
Eqs. (1.25) and (1.26) with ω = ωi . We then quench the                       new collective spins plus the oscillator in the two-channel case
detuning ωi → ωf and evolve the system with the two-channel                   that are governed by the same Hamiltonians (1.9) and (1.11)
Hamiltonian (1.9) starting from the initial state (1.28) at t = 0.            only with new effective parameters replacing εp and ω. The
   The state of the system is fully determined by the many-                   number of collective spins is m = 0, 1, or 2 and m = −1, 0,
body wave function, which in the mean-field treatment is at all               or 2 for one- and two-channel models, respectively, depending
times a product state of the form                                             on the quench. The difference is due to the presence of the
                                                                              oscillator degree of freedom in the latter case. For example,
                   | (t) = |ψ(t) ⊗ (b̂† )n(t) |0 ,                   (1.29)   m = −1 means that the effective large-time Hamiltonian Hred
                                                                              not only has no spins, but also the oscillator b is absent; i.e.,
where n(t) = |b(t)|2 and |ψ(t) is the fermionic part of the
                                                                              Hred = 0. This reduction effect combined with integrability of
wave function:
                                                                             classical Hamiltonians (1.9) and (1.11) allows us to determine
                                       †    †
       |ψ(t) =      [up (t) + v p (t)âp↑ â−p↓ ]|0 . (1.30)                  the state of the system (its many-body wave function) at t →
                     p                                                        ∞. We explain this method in detail in Sec. II. This section

                                                                        033628-5
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                                         PHYSICAL REVIEW A 91, 033628 (2015)

provides a summary of main results obtained with the help of                          (a)                                                                                           0x
this method.                                                                                       1

   In Secs. III and IV, we construct exact quench phase                                                                                                                                      0x
diagrams shown in Figs. 2–5. Depending on the values of                                         0.8
ωi and ωf either system reaches one of three distinct steady                                                                                                                        II′
states labeled by I, II (including subregion II ), and III that can                        max 0.6
be thought about as nonequilibrium phases with second-order                                                                                      II
phase transition lines between them [t → ∞ limit of the order                               /
                                                                                            0i  0.4
parameter (t) is continuous along lines separating different
regions]. These steady states correspond to m = 0, 1, or 2                                                   I
                                                                                                0.2
collective spins, respectively, for the one-channel model and
to m = −1, 0, or 2 in the case of two channels.                                                                                                                  III
   Each point in the quench phase diagrams represents a                                            0
                                                                                                    0                    0.2            0.4           0.6              0.8               1
particular quench specified by a pair of values ( 0i , 0f ).
                                                                                                                                              0f
                                                                                                                                                 /        max
Here 0 is the gap that the system would have in the
ground state at detuning ω, which is a known function of                              (b)          1
                                                                                                                                                                        0x
ω. Values 0i and 0f —ground-state gaps for ω = ωi and
ωf , respectively—uniquely determine ωi and ωf at fixed
                                                                                                0.8
resonance width γ . Note that 0f is not the magnitude of the                                               0.86
                                                                                                                                                                                             0x
actual steady-state gap function | (t)|. Each quench ωi → ωf                                max
                                                                                                                                                                              II′
(or λi → λf ) therefore maps to a single point ( 0i , 0f ) and                                  0.6
                                                                                                           0.85

vise versa.                                                                                 /
                                                                                                                  0   0.03                       II
   Steady states I, II, and III reached by the system at t → ∞                              0i  0.4          I
can be described in terms of the superfluid order parameter
  (t). In region I of phase diagrams in Figs. 2–5 the gap                                       0.2
function vanishes at large times, (t) → 0; see Fig. 6.
                                                                                                                                                                III
   In region II (including subregion II ) the magnitude of                                        0
                                                                                                       0                 0.2            0.4           0.6              0.8               1
the order parameter asymptotes to a nonzero constant ∞
as illustrated in Fig. 7,                                                                                                                     0f
                                                                                                                                                 /        max
                                      −2iμ∞ t−2iϕ
                      (t) →      ∞e                 ,                   (1.34)        (c)           1                                                0x

where ∞ ,μ∞ are functions of ωi , ωf (or, equivalently, of 0i
and 0f ), and γ to be determined below, and ϕ is a constant                                       0.8
phase. Plots of ∞ and μ∞ as functions of 0f for fixed 0i
                                                                                                                                                                      II′
are shown in Figs. 9, 18, and 19. The quantity μ∞ plays the                                 max   0.6        I
role of the out-of-equilibrium chemical potential. Subregions                                                                                                                                    0x
II and II of region II correspond to μ∞ > 0 and μ∞ < 0,                                    /
                                                                                            0i    0.4
respectively.                                                                                                                      II
   In region III of quench phase diagrams the amplitude of the
                                                                                                  0.2
order parameter oscillates persistently at large times, as shown                                                                                                III
in Fig. 8,
                                                                                                   0
                                2 (t) + h e−i(t) ,                                                    0                     0.2        0.4               0.6           0.8                  1
                    (t) →                                               (1.35)
                                         1
                                                                                                                                              0f
                                                                                                                                                 /         max
where
                                                               −                    FIG. 2. (Color online) Detuning quench phase diagrams for the
         (t) =    + dn[   + (t − t0 ),k ],    k =                  ,   (1.36)   two-channel model (1.1) in 2D for an assortment of resonance widths
                                                                +
                                                                                 γ . Each point represents a single quench labeled by 0i (vertical
where dn is the Jacobi elliptic function and t0 is an integration                axis) and 0f (horizonal axis), pairing gaps the system would have
constant. The magnitude of the order parameter oscillates                        in the ground state for initial and final detunings. At large times the
periodically between b = ( 2− + h1 )1/2 and a = ( 2+ +                           system ends up in one of three steady states shown as regions I, II
h1 )1/2 . The phase contains linear and periodic parts [62],                     (including II ), and III. For quenches in region I the order parameter
                                             κdt                                 vanishes, (t) → 0. In II (t) → ∞ e−2iμ∞ t−2iϕ and in III | (t)|
                 (t) = 2μt −            2 (t) + h
                                                            .           (1.37)   oscillates persistently. Subregions II and II differ in the sign of μ∞
                                                        1                        (out of equilibrium analog of the chemical potential): μ∞ > 0 in
Constants h1 , + , − , μ, and κ are known functions of                           II and μ∞ < 0 in II . The diagonal, 0i = 0f , is the no-quench
  0i , 0f (or ωi ,ωf ), and γ to be specified below; see also                    line. To the left of it are strong-to-weak-coupling quenches; to the
                                                                                                                                             √
Figs. 9 and 10 and refer to Sec. II D 2 for more information                     right are weak- to strong-coupling quenches. max = εF γ in 2D is
about the periodic solution.                                                     the maximum possible ground-state gap and 0× is the ground-state
   Previous studies of the BCS dynamics [3,7,16–19] were                         gap corresponding to zero chemical potential; i.e., 0× is given by
performed in the weak-coupling regime when both 0i and                           Eq. (1.25) for μ = 0.

                                                                           033628-6
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                                                                          PHYSICAL REVIEW A 91, 033628 (2015)


       (a)                                                                                            0x
                      1
                                                                                                               0x
                 0.8


                                                                                                      II′
             / max
                 0.6
                                                                       II
               0i0.4

                               I
                 0.2

                                                                              III
                      0
                       0               0.2                 0.4              0.6          0.8               1

                                                                      0f
                                                                         / max
       (b)             1
                                                                                         0x
                                                                                                                                 FIG. 4. (Color online) Interaction (λ) quench phase diagram for
                                                                                                                              the one-channel model (1.11) in 2D. Otherwise same as Fig. 2.
                 0.8

               max
                                                                                                               0x
                                   I                                                                                              There are several qualitatively new effects beyond the
                 0.6
                                                                                                II′                           weak-coupling regime. At smaller resonance width γ < γc =
             /                                                   II                                                           16/π 2 , gapless region I terminates below max at 0i = γ π/4
               0i0.4
                                                                                                                              along the vertical axis in 2D. This means that as initial coupling
                                                                                                                              gets stronger ( 0i increases), even quenches to arbitrarily weak
                     0.2                                                                                                      final coupling (small 0f ) do not result in vanishing (t) at
                                                                                  III                                         large times, in contrast to the weak-coupling regime, where
                      0
                          0                0.2             0.4              0.6          0.8            1                     quenches with sufficiently large 0f / 0i always do. The I-II
                                                                     /                                                        critical line also displays an interesting backwards bending
                                                                  0f          max                                             behavior for γ < γc = 16/π 2 ; see the inset in Fig. 2(b) and
       (c)             1                                     0x                                                               Eqs. (3.38) and (3.34).
                                                                                                                                  Region III of persistent oscillations terminates at a threshold
                                                                                                                              value of 0f < max in 3D, see Figs. 3 and 5. This means that
                     0.8
                                       I                                                                                      even quenches from an infinitesimally weak initial coupling
                                                                                        II′
                                                                                                                              (λi = 0+ in the one-channel model, which corresponds to
               max
                     0.6
                                                                                                                              a vicinity of the normal state) to final couplings stronger
                                                                                                                              than a certain threshold value produce no oscillations and
             /       0.4
                                                                                                                   0x         | (t)| instead goes to a constant. At finite but small initial
               0i
                                                 II                                                                           gap 0i (e.g., along the dashed line in Fig. 3) there is a
                     0.2


                       0                                     III                                                                                                        0x
                           0               0.2             0.4               0.6              0.8              1

                                                                  0f
                                                                        /     max
                                                                                                                                           2



   FIG. 3. (Color online) Same as Fig. 2 but in three spatial
                                                                                                                                        1.6     I                                  II′
dimensions.
                                                                                                                                    / F 1.2

                                                                                                                                                                                              0x
  0f   are much smaller than a characteristic high-energy                                                                             0i0.8
scale (Fermi energy for cold gases and Debye energy for                                                                                                    II
conventional superconductors). This limit corresponds to an                                                                             0.4
infinitesimal vicinity of the origin 0i = 0f = 0 in our
quench phase diagrams in Figs. 2–5. The weak-coupling limit                                                                                0
                                                                                                                                                                      III
                                                                                                                                           0        0.4         0.8          1.2    1.6   2
is universal in that it is independent of the resonance width and                                                                                                          / F
dimensionality and thus is the same in all diagrams. Critical                                                                                                           0f
lines separating regions I from II and II from III are straight
                                                                                                                                  FIG. 5. (Color online) Interaction quench phase diagram for the
lines in this case coming out of the origin with slopes                                                                       one-channel model (1.11) in 3D (otherwise the same as Fig. 2).
                                                                                                                              Consider, e.g., quenches from fixed infinitesimal coupling λi (small
                                                            = e±π/2 .
                                                      0i
                                                                                                                   (1.38)       0i ) to various final couplings λf . Increasing λf ( 0f ) we move
                                                  0f
                                                                                                                              through gapless (I), gapped (II), then oscillating (III) steady states.
Further, h1 = 0 in Eq. (1.35) and ∞ , ± take a simpler form                                                                   As λf increases, further oscillations disappear and we again end up
given by Eqs. (3.27)–(3.29), and (3.31).                                                                                      in a steady state characterized by constant asymptotic | (t)| (II ).

                                                                                                                        033628-7
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                                   PHYSICAL REVIEW A 91, 033628 (2015)

                        1                                                                                          60
                                                                                                     (a)
                                                                                                                                                 numerics
                                                                                                                                                 analytics
                      0.8                                                                                          50




      |Δ(t)| / Δ0i
                                                                                                                   40


                                                                                                       Φ(t)/2π
                      0.6

                                                                                                                   30
                      0.4
                                                                                                                   20

                      0.2
                                                                                                                   10

                        0                                                                                           0
                         0             2                  4          6             8                                        40           60                  80
                                                     Δ0i t                                                                       Δ0f t

    FIG. 6. (Color online) | (t)| in region I for a 3D two-channel                                   (b)             1
                                                                                                                                                numerics
model, γ = 1, obtained from numerical evolution of N = 5024 spins                                                                               analytics
following a detuning quench ωi → ωf . Here 0i = 0.27 max , 0f =                                                    0.8
4.30 × 10−2 max [cf. Fig. 3(b)]. From these two values all other
parameters obtain, e.g. μi = 0.90εF and ωf − ωi = 1.97εF .

                                                                                                      |Δ(t)|/Δ0f
                                                                                                                   0.6


reentrant behavior in both 2D and 3D as the final coupling                                                         0.4
( 0f ) increases when first there are no oscillations, then
they appear, and then they disappear again. The threshold                                                          0.2
value of 0f where the critical line separating regions II and
                                                                                                                    0
                                                                                                                            40           60                  80

                            1
                                                                                                                                 Δ0f t
      (a)
                        0.9                                                                       FIG. 8. (Color online) Amplitude (Higgs mode) and phase (t)
                                                                                              of the order parameter (t) in region III of Fig. 3(c) after detuning
                        0.8                                                                   quench from deep BCS to BEC in a 3D two-channel model for γ =


         |Δ(t)| / Δ0f
                                                                                              10. Numerical evolution with 5024 spins vs Eqs. (1.35) and (1.37).
                                                                                                               −3
                        0.7                                                                     0i = 3.20 × 10     max ,  0f = 0.45 max , and δω = −5.86γ .


                        0.6
                                                                                              III terminates is given by Eq. (3.47) (plotted as a function
                                                                                              of the resonance width in Fig. 22) and Eq. (4.18) for one-
                        0.5
                                                                                              and two-channel models, respectively. For more details about
                        0.4
                                                                                              quench diagrams, such as the shape of the critical lines, various
                             0   10        20        30        40   50   60        70
                                                          Δ0f t                               thresholds and termination points, and values of parameters
                                                                                              (e.g., ∞ , μ∞ , + , and − ) characterizing asymptotic (t),
                        0.7
      (b)                                                                                     see Secs. III and IV.
                                                                                                 The large-time asymptote of (t) does not fully specify
                        0.6                                                                   the steady state. One also needs to know the Bogoliubov
                                                                                              amplitudes up (t → ∞),vp (t → ∞). We calculate them in

       |Δ(t)| / Δ0f
                        0.5                                                                   Sec. II D in all three steady states. In terms of spin vectors, this
                                                                                              translates into steady-state spin distribution. Even in regions I
                        0.4                                                                   and II where | (t)| goes to a constant, the steady state of the
                                                                                              system is far from any equilibrium state. Time-independent
                        0.3                                                                   | (t)| means that in a frame that rotates around the z axis
                                                                                              with frequency 2μ∞ the magnetic field Bp that acts on spin
                        0.2                                                                   sp in Eq. (1.7) is constant. In equilibrium sp aligns with Bp
                           0      10            20            30    40        50
                                                      Δ0f t                                   or −Bp (ground state). In steady states I and II it instead
                                                                                              rotates around Bp , making a constant angle with it. Let θp
    FIG. 7. (Color online) | (t)| in regions II (top) and II (bottom)                        be the angle between sp and −Bp (negative z axis in steady
for a 3D two-channel model, γ = 1, obtained from numerical                                    state I), so that in the ground state θp = 0. Out-of-equilibrium
evolution of N = 5024 spins after quenching the detuning ω. 0i =                              θp determines the steady-state spin distribution function and is
0.27 max , μi = 0.90εF in both panels (same as in Fig. 6). The                                given by Eq. (3.11). This expression for cos θ (εp ) applies in all
final detuning corresponds to (a) 0f = 0.56 max = 2.07 0i and                                 three steady states, but its interpretation in region III is slightly
(b) 0f = 0.97 max = 3.59 0i . See also Fig. 3(b).                                             different and is explained below. A plot of the distribution

                                                                                        033628-8
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                               PHYSICAL REVIEW A 91, 033628 (2015)


        (a) 0.5                     γ = 0.1                                          (a)                                     γ = 0.1
                                                                                             0.1
                                                                 3D                                                                                             3D
                                                Δa
               0.4                                                                         0.05



                                                                                      h1 / Δ _
       Δ /Δmax
                                                                                     2
               0.3                                                                               0


          8 0.2                                                                            -0.05
                                               Δb

                 0.1                                                                        -0.1


                  0
                   0   0.2         0.4         0.6         0.8                                   0.2             0.4             0.6                      0.8
                                         Δ0f /Δmax                                                                             Δ0f /Δmax
        (b)                         γ = 10                                           (b)                                     γ = 10
                                                                                                 0
                                                                 3D                                                                                             3D
              0.25       Δa                                                                 -0.2


                                                                                      h1 / Δ _
                                                                                     2


       Δ /Δmax
               0.2
                                                                                            -0.4

              0.15
          8                                                                                 -0.6
                 0.1


              0.05            Δb                                                            -0.8


                  0                                                                              -1
                   0    0.2              0.4         0.6         0.8                                     0.1           0.2             0.3                0.4
                                         Δ0f /Δmax                                                                             Δ0f /Δmax
     FIG. 9. (Color online) Limiting values of | (t)| for a 3D two-             FIG. 10. (Color online) Parameter h1 in Eq. (1.35) for asymptotic
channel model at large times after a detuning quench as functions            | (t)| in phase III as a function of 0f at fixed small 0i = 0.05 max
of 0f (or, equivalently, of final detuning ωf ) at fixed small               (same as in Fig. 9). For quenches within the weak-coupling limit
   0i = 0.05 max (fixed initial detuning deep in the BCS regime).            h1 = 0, so nonzero h1 quantifies deviations from this limit. Note that
This corresponds to moving along a horizontal line (not shown)               one must have h1 ⩾ − 2− , so that the expression under the square
in Figs. 3(a) and 3(c) going through regions I, where | (t)| → 0,            root in Eq. (1.35) is non-negative.
II, where | (t)| → ∞ > 0, III, where | (t)| oscillates periodically
between a and b , and into region II , where again | (t)| → ∞ >             coupling regime we find
0. Note that persistent oscillations appear and then disappear again
                                                                                                                                              2
as we decrease ωf − ωi (i.e., increase 0f at fixed 0i ). The same                                                                (δ      0)
behavior is observed in the 3D one-channel model; see Fig. 5.                                                  ∞ =      0f −                      .                  (1.39)
                                                                                                                                  6      0f

                                                                                We obtain an exact expression for (t)—Eqs. (5.35)–
                                                                             (5.37)—valid at all times and arbitrary coupling strength for
function cos θp is shown in Fig. 11. We explore the asymptotic
                                                                             both one- and two-channel models. In the weak-coupling
states produced by detuning or interaction quenches in detail
                                                                             regime this expression simplifies so that
in Sec. II D. In Sec. VII we provide further insight into their
                                                                                                                        ∞
physical nature and discuss their experimental signatures.                                                 dx cos[2 0 t cosh(π x/2)]
                                                                                  | (t)| =            0f − 2δ    0                      .
   We perform detailed analysis of linearized equations of                                              0   π          1 + x2
motion that goes much beyond previous work even in the                                                                                (1.40)
weak-coupling regime and yields a range of new results. Small                From here short- and long-time asymptotes follow. At short
quenches of the detuning correspond to a small neighborhood                  times the order parameter amplitude rises or falls sharply as
of the diagonal in quench diagrams in Figs. 2–5; i.e., they fall                                                                    δ        0
within region II, where | (t)| → ∞ and Eq. (1.34) applies.                                              | (t)| =         0i +                         .              (1.41)
We show that within linear approximation ∞ = 0f and                                                                              |ln(        0 t)|

μ∞ = μf ; i.e., there are no corrections to these equations                  The long-time behavior in the weak-coupling limit is
linear in the change of detuning or, equivalently, in δ 0 =                                                      2δ 0 cos(2 0 t + π/4)
  0f − 0i . This is, in fact, a general result that has been                         | (t)| =            0f −              √           .                             (1.42)
                                                                                                                 π 3/2          0t
overlooked by previous work; to first order in deviations from
the ground state (t) always asymptotes to its ground-state                      At stronger coupling in region II (but not II ) the long-time
form for the Hamiltonian with which the system evolves at                    asymptote is still given by Eq. (1.42); only the coefficient
t > 0. Note, however, that when quadratic correction is taken                in front of the second term on the right-hand side is more
into account one gets ∞ < 0f . For example, in the weak-                     involved.

                                                                       033628-9
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                PHYSICAL REVIEW A 91, 033628 (2015)


        (a)        1
                                                                              ε =√0, E(0) = Emin , and the density of states in 3D vanishes
                                                                              as ε at small ε.
                                                                                 In 2D linear analysis yields a different approach to the
                 0.5                                                          asymptote in region II

        cos θp
                                                                                                                  δω sin(2Emin t)
                                                                                           | (t)| =    0f   1−                    ,           (1.44)
                  0
                                                                                                                   γ |μ|t ln2 t
                                                                              because of a constant density of states and ln ε divergence
              -0.5
                                                                              of the Fourier amplitude of | (t)| at small ε (see below).
                                                                              We also determine the time-dependent phase of the order
                  -1
                                                                              parameter (t) in all cases corresponding to Eqs. (1.40)–
                   0             0.5          1
                                                  εp
                                                       1.5       2
                                                                              (1.44), asymptotes of individual spins sp (t) as t → ∞, and
                                                                              many other new results for the linearized dynamics in Sec. V.
        (b)
                                                                                 Finally, we extend some of the above results for the long-
                                                                              time behavior of | (t)| to the nonlinear regime, though, unlike
                                                                              the linear analysis, these results are not rigorous. In region II
                 0.8

                                                                                                             cos(2   ∞ t + π/4)
                 0.6
                                                                                       | (t)| =    ∞+c                √            ,          (1.45)
                                                                                                                          ∞t

        cos θp   0.4                                                          where c is a dimensionless coefficient. This answer holds for
                                                                              both one- and two-channel models in either dimension.
                 0.2                                                             For region II we argue that the answer depends on
                                                                              dimensionality similarly to the linear analysis and
                  0                                                                                           min 
                                                                                                         sin 2E∞     t
              -0.2                                                                 | (t)| = ∞ 1 − c1                       in 2D,     (1.46)
                   0         1            2       3          4   5                                           t ln2 t
                                                  εp
                                                                                                         min         
                                                                                                     cos 2E∞   t + π/4
    FIG. 11. (Color online) Spin distribution cos θp as a function of           | (t)| =    ∞ 1 − c2                                   in 3D, (1.47)
εp (in units of Fermi energy) at large times after the quench in a 3D
                                                                                                           t 3/2
two-channel model. In phases I and II, − cos θp /2 is the projection of       where E∞  min
                                                                                            = μ2∞ + 2∞ .
the spin sp onto its effective magnetic field (z axis in phase I) around         The approach to the gapless steady state (region I) is
which it precesses. In equilibrium cos θp = ±1 (1 in the ground               expected to be
state) for all momenta and in phase I cos θp = −1 and 1 correspond
                                                                                                             c4
to doubly occupied and unoccupied states, respectively. Quench                                   | (t)| =         in 2D,         (1.48)
parameters are γ = 1 and (a) 0i = 0.05 max , 0f = 0.002 max                                               t lnr t
(BCS to deep BCS quench in phase I); (b) 0i = 0.78 max , 0f =                 where r = 1 or r = 2, and
0.001 max (BEC to deep BCS quench in phase I). In both cases                                                 c3
μ∞ ≈ εF . Note the Fermi-like shape of the distribution function in                               | (t)| = 3/2 in 3D.            (1.49)
(a). Note that cos θp → 1 as εp → ∞, as it should, indicating that                                         t
states at very high energies are empty.                                       We discuss these nonlinear large-time asymptotes in more
                                                                              detail in Sec. VI.

    Regions II and II differ in the sign of the phase frequency                                       II. METHOD
μ∞ , μ∞ > 0 in II and μ∞ < 0 in II . We see below that
frequency (Fourier) spectrum of quench dynamics in regions                       Here we describe a method that allows one to determine
II and II is E∞ (εp ) = (εp − μ∞ )2 + 2∞ , so that the Fourier              the asymptotic state of the system at long times. Both
                                             ∞
transform of a dynamical quantity reads 0 A(ε)e−2iE∞ (ε)t dε.                 the quantum (1.5) and classical (1.9) two-channel models
For μ∞ > 0 the phase has a stationary point on the integration                are integrable meaning that there are as many nontrivial
path at ε = μ∞ , while for μ∞ < 0 it is absent. As a result, the              conservation laws as there are degrees of freedom. There
long-time behavior in 3D in region II changes,                               is an exact Bethe ansatz-type solution for the quantum
                                                                              spectrum [38]. In the classical case integrability implies a
                                       δω cos(2Emin t + π/4)                  formal inexplicit solution of the equations of motion in terms of
     | (t)| =          0f   1−c                              ,       (1.43)
                                        γ     (2|μ|t)3/2                      certain multivariable special (hyperelliptic) functions [15] that
                  √                                                           can be helpful for understanding certain general features of the
where Emin = μ2 + 20 , c is of order one, and δω = ωf −                       dynamics. Evaluating specific dynamical quantities of interest
ωi . The same expression holds for the one-channel model after                for realistic initial conditions with this solution is, however,
a replacement δω/γ → 1/λf − 1/λi . Oscillation frequency                      roughly equivalent to just solving the equations of motion
Emin and 1/t 3/2 decay are in agreement with Ref. [23] and                    numerically. However, the latter could be as well done directly
reflect the fact that in the absence of a stationary point, the long-         without the formal exact solution. This is a typical situation in
time asymptote is dominated by the end point of integration at                the standard theory of nonlinear integrable systems.

                                                                        033628-10
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                   PHYSICAL REVIEW A 91, 033628 (2015)

    Fortunately, it was realized that, at least for the BCS-type       Explicit evaluation of L2 (u) yields
models, the large-time dynamics dramatically simplifies in the
thermodynamic limit, so that the number of evolving degrees                        (2u − ω) 4Hb           2Hp         sp2
of freedom effectively drops to just a few spins. Building on          L2 (u) =            +      +                +           ,
                                                                                      g4     ωg 2     g 2 (u − εp ) (u − εp )2
this insight, Yuzbashyan et al. [16] were able to develop a                                         p
method that goes beyond the standard theory and explicitly                                                                           (2.4)
predicts the long-time dynamics in the thermodynamic limit.
    The main idea of this method is as follows. First, we              where
construct a special class of reduced solutions of the classical
equations of motion for the two-channel model such that the                          sp · sq
                                                                             Hp = g 2                  + (2p − ω)spz + g(bsp− + bsp+ ),
dynamics reduces to that of just few effective spins. Then we
                                                                                     q=p
                                                                                         (εp  −   εq )
choose a suitable reduced solution and fix its parameters so                           
that its integrals of motion match those for a given quench                  Hb = bb +      spz .                                    (2.5)
in the thermodynamic limit. Reduced solutions have only few                                p
additional arbitrary constants and cannot generally satisfy all
of the quench initial conditions (1.28). There are 2N + 2 initial      It follows from Eq. (2.3) that these spin Hamiltonians mutually
conditions (two angles per spin plus two initial conditions            Poisson commute, i.e.,
for the oscillator mode b) and only N + 1 correspond to the
integrals of motion.                                                                       {Hp ,Hp } = {Hp ,Hb } = 0.               (2.6)
    Next, exploiting the fact that for fixed (t) BdG equa-
tions (1.31) are linear in the amplitudes up and vp , we derive        Moreover, the two-channel Hamiltonian (1.9) is
the most general t → ∞ asymptotic solution that has the                                                
same (t) as the reduced one. It has the same integrals as                                H2ch = ωHb +      Hp .                      (2.7)
the quench dynamics by construction and, in addition, N + 1                                                           p
arbitrary independent constants to match the remaining initial
conditions. We conjecture that the so-constructed asymptotic           This implies that Hp and Hb are conserved by H2ch and
solution is the true large-time asymptote of the actual quench         establishes the integrability of the two-channel Hamiltonian.
dynamics. To verify this few spin conjecture it is sufficient to       Note that L2 (u) is also conserved for any value of u and serves
show that the large-time asymptote of the actual (t) matches           as a generator of the integrals of motion for the two-channel
that of the reduced (and therefore general asymptotic) solution.       model. The same construction works in the quantum case as
We do so numerically in the nonlinear case and analytically for        well; one only needs to promote classical dynamical variables
infinitesimal quenches when the dynamics can be linearized.            to corresponding quantum operators and replace Poisson
    We consider the two-channel model in this and the                  brackets with commutators.
following sections and then obtain similar results for the                Equations of motion can be conveniently and compactly
one-channel (BCS) model in Sec. IV by taking the broad                 written in terms of the Lax vector as
resonance, γ → ∞, limit.
                                                                                                L˙ = (−2       + 2uẑ) × L.          (2.8)

         A. Integrability and Lax vector construction                  Comparing the residues at the poles at both sides of this
    An object called Lax vector plays a key role in our approach.      equation, we see that it is equivalent to the equations of motion
It encodes all the information about the integrals of motion           for spins (1.8).
and turns out to be especially useful in analyzing the quench             The square of the Lax vector is of the form
dynamics in the thermodynamic limit. The Lax vector is                                                         Q2N+2 (u)
defined as                                                                                     L2 (u) =                       ,     (2.9)
                                                                                                          g4    εp (u − εp )
                                                                                                                             2
                 sp     (ω − 2μ)      2
  L(u) =               −          ẑ + 2 [(u − μ)ẑ −       ],         where N is the total number of distinct single-particle energies
            p
                u − εp      g 2       g
                                                                       εp , the product is similarly over nondegenerate values of εp ,
                                                           (2.1)       and Q2N+2 (u) is a polynomial in u of degree 2N + 2. The
                                                                       roots of this spectral polynomial [or equivalently of L2 (u)]
where u is an auxiliary complex variable and ≡ x x̂ + y ŷ.            play an important role in the further analysis of the asymptotic
Poisson brackets of components of L(u) satisfy the following           behavior. Note that since L2 (u) is conserved, so are its roots.
Gaudin algebra:                                                        They thus constitute a set of integrals of motion alternative to
                                                                       Eq. (2.5). Since L2 (u) ⩾ 0 for real u, its roots come in complex
                                     Lc (u) − Lc (v)                   conjugate pairs.
            {La (u),Lb (v)} = εabc                   .     (2.2)
                                          u−v

This implies an important equality,                                                              B. Reduced solutions
                                                                          Let us look for special solutions of equations of motion (2.8)
                      {L2 (u),L2 (v)} = 0.                 (2.3)       such that the Lax vector factorizes into time-dependent

                                                                 033628-11
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                     PHYSICAL REVIEW A 91, 033628 (2015)

and -independent parts,                                                       Equations (2.15) constrain the coefficients of the spectral
                                                                              polynomial
               σp       (ω − 2μ)       2
  Lred (u) =          −            ẑ + 2 [(u − μ)ẑ − ]                                                         
                                                                                                                 m−1
              u −  εp       g 2        g
            p                                                                       Q2m+2 (u) = g L2m (u)
                                                                                                       4
                                                                                                                       (u − ηk )2 , m ⩾ 0,             (2.16)
                           
                 dp                                                                                             k=0
          = 1+                Lm (u),                 (2.10)                  of the m-spin system. Indeed, using Eq. (2.14), we can cast
                 p
                     u − p
                                                                              these constraints into the following form:
where σp (not to be confused with Pauli matrices) denote spins                        σp εpr−1               δrm
in this solution that can have arbitrary length to distinguish                                         =−         ,    r = 1, . . . ,m,
                                                                                      Q2m+2 (εp )             g2
them from spins sp for the quench dynamics that have                            p
                                                                                                                                                       (2.17)
length 1/2. Further, dp are time-independent constants to be                                                      
                                                                                                                  m−1               2σp g 2 εpm
                                                                                                   
determined later and Lm (u) is the Lax vector for an effective                                    ω = ω+2               ηk +                           .
m-spin system,                                                                                                    k=0          p
                                                                                                                                     Q2m+2 (εp )

                                                                              Here m ⩾ 0. These equations can be viewed as equations for
            
            m−1
                 tj     (ω − 2μ)      2
 Lm (u) =             −           ẑ + 2 [(u − μ)ẑ −                  ].     determining the lengths of the collective spins tj .
          j =0
               u − ηj       g 2       g                                          We thus constructed a class of solutions such that the
                                                                              dynamics reduces to that of a smaller number of spins. These
                                                                     (2.11)   few-spin solutions, however, do not match the quench initial
Here tj are new collective spin variables placed at new arbitrary             conditions, but, as we will see, the long-time asymptote of (t)
                                                                              after the quench coincides with (t) of an appropriately chosen
“energy levels” ηj . Note that the bosonic field b and therefore              few-spin solution. Specifically, m = −1, 0, and 1 are realized
   are the same in the original and reduced models.                           depending on the magnitude and the sign of the change in the
   Substituting Eq. (2.10) into the equations of motion (2.8),                detuning ω. Let us therefore consider these particular cases.
we see that Lm (u) satisfies the same equation of motion.
This means that variables tj obey Bloch equations (1.8) with                                           1. m = −1 spin solutions
εp → ηj and ω → ω , and are therefore governed by the same
                                                                                  m = −1 refers to the case when there are no collective
Hamiltonian,
                                                                              spins and b = 0; i.e., the oscillator (which can be viewed as an
               
               m−1                          
                                            m−1                               infinite length limit of a spin) is effectively absent as well. In
                      2ηj tjz + ω bb + g          (btj− + btj+ ).
                                                                                                                            
     red
    H2ch =                                                           (2.12)   other words, Hred = 0 and Lm (u) = 2u−ω    g2
                                                                                                                              ẑ. Equation (2.13)
               j =0                         j =0                              then implies that all spins in the reduced solution are along the
                                                                              z axis pointing in either a positive or a negative direction. It is
We need at most m = 1 for analyzing the quench dynamics,
                                                                              convenient to redefine the sign of σp (only for m = −1) so that
so we are able solve the equations of motions for tj directly.
                                                                              σp = −σp ẑ. We see directly from the equations of motion (1.8)
   Matching the residues at u = εp on both sides of Eq. (2.10),
                                                                              that this configuration together with b = 0 is indeed a solution,
we express original spins in terms of tj
                                                                              a stationary one in the present case.
                              σp = dp Lm (εj ).                      (2.13)
                                                                                                       2. m = 0 spin solutions
Constants dp are determined from the above equation using                        In this case the reduced problem consists of a free classical
σp2 = σp2 , where |σp | is the length of spin σp . Note that σp can           oscillator as there are no collective spins; i.e., Hred = ω b̄b.
be of either sign (for future convenience). We have                           Equations of motion reduce to ḃ = −iω b. Therefore,

                              dp = − 
                                          σp
                                                     .               (2.14)                                (t) = −gb = ce−2iμt ,                       (2.18)
                                                                                                                                                   
                                         L2m (εp )                            where c is a complex constant and we defined μ = ω /2.
                                                                                Expressions for the original spins follow from the reduced
It is important to note that σp are arbitrary constants at this               Lax vector
point. We determine them later so that the integrals of motion
                                                                                                         2
for the reduced solution match those for quench dynamics.                                    Lm (u) = − 2 [ − (u − μ)ẑ].            (2.19)
    To satisfy Eq. (2.10), we also need to match the residues at                                        g
u = ηk and the u → ∞ asymptotic. This leads to the following                  Equations (2.13) and (2.14) imply
m + 1 equations:                                                                                     σp
                                                                                           σp =             [ − (εp − μ)ẑ],                           (2.20)
                     dp                                                                         E(εp ; ,μ)
       1+                  = 0 k = 0, . . . ,m − 1,
               p
                   ηk − εp                                                    where E(εp ; ,μ) = (εp − μ)2 + | |2 . We see that the
                                                                    (2.15)   ground state (1.15) is a one-spin solution with c = 0 and
       ω = ω − 2             dp .                                            σp = 1/2 (to minimize the energy). Excited states are also
                          p                                                   one-spin solutions with different parameters.


                                                                        033628-12
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                       PHYSICAL REVIEW A 91, 033628 (2015)

   There is only one (last) constraint among Eqs. (2.17) for             equation for 
m = 0, which we recognize as a generalization of the gap
                                                                               (ap 2 + bp )2 + (2ap εp  − ap A + cp )2 + ap2 ˙
                                                                                                                              2 = σp2 .
equation (1.18).
                                                                                                                                                       (2.29)
                      3. m = 1 spin solutions                            Dividing the last equation by ap2 and rearranging, we obtain
   This example is substantially more involved than the                                                       
previous two. Now there is one collective spin t coupled to                                         bp
                                                                                  +  +  2 + 4εp − 4εp A + A2
                                                                                  ˙ 2     4     2            2
an oscillator,                                                                                      ap

          Hred = 2ηt z + ω bb + g(bt − + bt + ),              (2.21)                         bp2 − σp2
                                                                                          +               = 0.                                         (2.30)
                                                                                                 ap2
making the dynamics rather nontrivial. Our main goal
presently is to derive a differential equation for | (t)| =              It turns out that A is a certain function
                                                                                                                  of . To see this, let xp
g|b(t)| and to relate its coefficients to the spectral polynomial        be a set of numbers such that p xp = 0, multiply Eq. (2.30)
Q4 (u) of the reduced m = 1 problem given, in general, by                by xp , and sum over p. This yields
Eq. (2.16).                                                                                                      κ
   Hred conserves b̄b + t z . It follows that t z can be expressed                                A = 2μ + ,                        (2.31)
                                                                                                                
through |b|2 as t z = c1 2 + c2 , where c1,2 are constants and
we introduced a notation                                                 where μ and κ are arbitrary real constants. Substituting
                                                                         Eq. (2.31) into Eq. (2.30), we obtain
                              = e−i .                        (2.22)                                2 b2 − σp2
                                                                         ˙ 2 + 4 + 22 bp + 2ξp2 + κ + p
                                                                                                               − 4κξp = 0,
Equation (2.13) then implies that the z component of the orig-                          ap          2    ap2
inal spins in the reduced solution can be similarly expressed
through | | as                                                                                                                                         (2.32)
                                                                         where ξp = εp − μ. Note that the same equation obtains in the
                         σpz = ap 2 + bp .                    (2.23)
                                                                         reduced problem with ap → c1 , bp → c2 , etc. It follows that
Note that constants ap and bp are inversely proportional to              coefficients must be p independent; i.e.,
   L2m (εp ) and therefore to Q4 (εp ). It turns out that an efficient             bp                       bp2 − σp2
strategy to derive an equation for  and relate its coefficients                      + 2ξp2 = 2ρ,                              − 4κξp = 4χ ,          (2.33)
                                                                                   ap                            ap2
to those of Q4 (u) is somewhat indirect. First, we use equations
of motion for σp together with Eq. (2.23) to obtain an equation          where ρ and χ are p-independent constants. We find
for  and expressions for ap and bp . Identifying Q4 (εp ) in                                        
                                                                                      bp = −2 ξp2 − ρ ap ,
the latter with the help of Eq. (2.14), we relate the coefficients.                                                                                    (2.34)
    Bloch equations (1.8) for spins in the reduced solution,                                              −σp
                                                                                              ap =       2         .
spred ≡ σp , can be written as
                                                                                                  2 ξp2 − ρ − κξp − χ
   σ̇pz = −i(σp− ¯ − σp+ ), σ̇p− = −2iσpz           − 2iεp σp− .               As mentioned above ap and bp are inversely proportional
                                                               (2.24)    to     Q4 (εp ). Equation (2.34) therefore implies
Substituting σpz from Eq. (2.23) into the first equation, we                      Q4 (u) = [(u − μ)2 − ρ]2 − κ(u − μ) − χ ,                            (2.35)
obtain
                                                                         while the differential Eq. (2.32) for  reads
                    σp− ei − σp+ e−i = 2iap .
                                              ˙                (2.25)                                                           2
                                                                                     ˙ 2 + 4 + 4ρ2 + κ + 4χ = 0.              (2.36)
Multiplying the second equation in Eq. (2.24) by ei and                                                   2
adding the resulting equation to its complex conjugate, we               This equation can be solved in terms of elliptic function. Let
get                                                                      w = 2 . We have
      d                                                                   ẇ 2 + 4w 3 + 16ρw 2 + 16χ w + 4κ 2 ≡ ẇ 2 + 4P3 (w) = 0.
        (σ − ei + σp+ e−i ) = 4ap εp 
                                       ˙ − 2ap 
                                               ˙ ,
                                                 ˙             (2.26)
      dt p                                                                                                                       (2.37)
where we also used Eq. (2.25). Integrating this and adding the           Further, let P3 (w) = (w − h1 )(w − h2 )(w − h3 ), where h3 ⩾
result to Eq. (2.25), we obtain                                          h2 ⩾ h1 , and define
                                                                               ω=     2
                                                                                          + h1 ,       + = h3 − h1 ,
                                                                                                       2
                                                                                                                                      − = h2 − h1 .
                                                                                                                                      2
                                                                                                                                                       (2.38)
                 σp− ei = 2ap εp  − ap A + iap ,
                                                 ˙             (2.27)
                                                                        We get
where A =        dt ˙
                   ˙ . Equation (2.27) implies
                                                                                                ˙2 =(      +−
                                                                                                           2           2
                                                                                                                           )(    2
                                                                                                                                     −      2
                                                                                                                                            − ),       (2.39)
              |σp− |2 = (2ap εp  − ap A)2 + ap2 
                                                 ˙ 2.          (2.28)    with the solution
Equations (2.28) and (2.23) combined with the conservation of                                                                                 −
                                                                                       =       + dn[   + (t − t0 ),k ],              k =          ,   (2.40)
the length of the spin, (σpz )2 + |σp− |2 = σp2 , yield a differential                                                                         +

                                                                   033628-13
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                            PHYSICAL REVIEW A 91, 033628 (2015)

where dn is the Jacobi elliptic function and t0 is an arbitrary         |σ (εp )|, in the few-spin solution so that
integration constant.
                                                                                                                 
   It also follows from Eq. (2.31) and the definition of A below
Eq. (2.27) that the phase of the order parameter is determined                                          L2 (ε− ) − L2 (ε+ )
                                                                                      σ (ε) = z(ε)                               .     (2.44)
as                                                                                                           2iπ ν(ε)

 ˙ = dA = 2μ −             κ                   2 + h e−i .
                                  ,   =            1         (2.41)       Thus, the few-spin solution with this σ (ε) and L2m (u), whose
     d                  2+h
                               1                                        roots are the same as the isolated roots of L2 (u), has the same
                                                                        integrals of motion as the quench problem.
                C. Matching integrals of motion
   Given the quench initial conditions, we can evaluate all
                                                                                D. Asymptotic solution for the quench dynamics
integrals of motion. This is equivalent to evaluating L2 (u) in
the initial state as it is conserved and contains all the integrals         There are altogether 2(N + 1) initial conditions: two angles
as residues at u = εp . It turns out that in the thermodynamic          for each classical spin and two initial conditions for the
limit it is possible to find a reduced (few-spin) solution that has     oscillator. So far, we constructed a reduced m-spin solution that
the same L2 (u), i.e., exactly the same integrals as the quench         matches N + 1 integrals of motion. This satisfies N + 1 initial
dynamics.                                                               conditions. The dynamics of the reduced m-spin Hamiltonian
   In the thermodynamic limit single-particle energies εp form          contains 2(m + 1) constants, m + 1 of which (integrals of
a continuum on the positive real axis and L2 (u), therefore, has        motion for Hred ) are already fixed since we fixed L2m (u).
a continuum of poles at u > 0. Additionally, L2 (u) also has a          The remaining m + 1 constants are not sufficient to match the
continuum of roots along the u > 0 half line, as we show in             remaining N → ∞ initial conditions for the quench dynamics
                                                                        at finite m. This is resolved as follows. We use the known
Appendix B. Thus, L2 (u) has a branch cut along u > 0 in the
                                                                        m-spin solution to derive a general asymptotic (i.e., valid
continuum limit. There can also be several isolated roots whose
                                                                        at t → ∞) solution of the equations of motion for spins
imaginary parts remain finite in this limit. Isolated roots play
                                                                        sp with the same (t) and the same integrals of motion as
an important role in the dynamics; we determine them below
                                                                        the m-spin solution. Integrals of motion therefore are those
and see that there are at most four such roots (two pairs of
                                                                        for the quench dynamics. In addition, this general solution
complex conjugate roots) for our quench problem.
                                                                        contains the correct number N + 1 of independent constants.
   Equation (2.10) implies
                                                                        We therefore conjecture that this is the true solution for
                                                                       the quench dynamics at large times after the quench. By
                       
              d(ε )ν(ε )            L2 (u)                             construction, to verify this few-spin conjecture, it is sufficient
 1 + dε               
                          = −z(u)            , z(u) = ±1, (2.42)
                u−ε                  L2m (u)                            to show that the true asymptote of (t) coincides with (t)
                                                                        in the m-spin solution because given (t) we obtain the most
where L2 (u) is evaluated for the quench initial conditions. Our        general asymptotic solution of equations of motion.
task is to find the parameters for the reduced problem—d(ε)                 As discussed above Eq. (1.33), each quench is characterized
and L2m (u)—so that this equation holds. Then the reduced               by three parameters: the resonance width γ and the final ωf
problem has the same integrals of motion as the quench                  and initial ωi values of the detuning. We determine in the next
dynamics.                                                               section that L2 (u) for the quench dynamics can have zero, one,
   Both sides of Eq. (2.42) have a branch cut along the positive        or two pairs of isolated complex roots for any γ depending on
real axis and tend to 1 as u → ∞ for an appropriate choice              ωi and ωf . These, by construction, must also be all the roots
of the sign z(∞). Further, provided that the isolated roots of          of L2m (u), which has m + 1 pairs of complex conjugate roots
L2 (u) coincide with the roots of L2m (u), there are no more            according to Eq. (2.16). Cases relevant for the quench phase
branching points and both sides are analytic away from the              diagram are therefore m = −1, 0, and 1.
shared branch cut at u > 0. If we further ensure that the left-             It is worthwhile to consider the m = −1 case separately
and the right-hand sides of Eq. (2.42) have the same jump               in some detail to illustrate this procedure. Suppose L2 (u)
across the branch cut, then their difference is an entire function      evaluated for the quench initial condition has no complex
that vanishes at infinity. It is therefore identically zero by          (isolated) roots away from the real axis. Then there is an
Liouville’s theorem from complex analysis, and Eq. (2.42)               m = −1 spin solution constructed above that in the N → ∞
holds.                                                                  limit has the same values of the integrals of motion as the
   To equate jumps across the branch cut, we take u →                   spin dynamics. Spins in this solution are all along the z axis,
ε ± i0, apply the well-known formula 1/(x ± i0) = P(1/x) ∓              σp = −σp ẑ, and (t) = −gb(t) = 0. It is a particular solution
iπ δ(x), and subtract one result from another. This fixes d(ε),         of the equations of motion (1.8) such that b(t) = 0.
                                                                          The general solution of the spin part of the equations of
                              L2 (ε− ) − L2 (ε+ )                       motion in Eq. (1.8) with b(t) = 0 is as follows: spins sp precess
                     z(ε)
        d(ε) = −                                  ,        (2.43)      around the z axis (or equivalently around the reduced spins σp )
                   2iπ ν(ε)                                             with frequencies 2εp , i.e.,
                                     L2m (ε)

where ε± = ε ± i0. According to expression (2.14) for dp ≡                                   σpz cos θp             sin θp iαp (t)
                                                                                     spz =                , sp− =         e        ,   (2.45)
d(εp ) this is equivalent to fixing the lengths of the spins, |σp | ≡                        σp    2                  2

                                                                  033628-14
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                       PHYSICAL REVIEW A 91, 033628 (2015)

where θp is the angle sp makes with −ẑ and αp = −2εp t + δp .             (a)
Equivalently, this can be expressed as
                                                                                     0.4                                                Im[cm]/0.1 0i
                            σp cos θp
                       sp =           + sp⊥ ,               (2.46)                   0.2
                            σp 2
where sp⊥ is the component transverse to σp , which rotates                               0
around σp with frequency 2εp . Note that the length of spin sp
is 1/2, as it should be for the quench initial conditions.                          -0.2
    This spin configuration has N additional constants δp , but
                                                                                    -0.4
it does not satisfy the equation of 
                                    motion forb(t) in Eq. (1.8)
because b(t) = 0, while J− (t) = p sp− = p fp e−2εp t = 0,
where 2fp = sin θp eiδp . However, in the thermodynamic limit                                 0.4   0.6       0.8      1             1.2   1.4       1.6
                                                                                                                     Re[c] / F
J− (t) = f (ε)ν(ε)e−2εt → 0 as t → ∞ and this solution
becomes self-consistent.                                                                   1
                                                                           (b)
    Next we set 2σp = cos θp and substitute sp = σp + sp⊥ into
the Lax vector,                                                                      0.8

                                            sp⊥
                  L(u) = Lred (u) +
                                                                            | (t)|/ 0i
                                                    .       (2.47)                   0.6
                                       p
                                           u − εp

The second term vanishes by the Riemann-Lebesgue lemma                                   0.4
(dephases) as t → ∞ in the thermodynamic limit for u away
from the real axis similarly to J− (t) and therefore L(u) →                              0.2
Lred (u). Constants σp are given by Eq. (2.44) to match the
integrals of motion. Then the solution given by Eq. (2.45) with                           0
2σp = cos θp has the same integrals of motion as the quench                                0               2                      4               6
                                                                                                                         0i
                                                                                                                              t
dynamics and the right number of additional constants to match
the remaining initial conditions. As explained above, to verify
                                                                         FIG. 12. (Color online) Order parameter (t) vanishes whenever
that this is indeed the true asymptote of the quench dynamics,
                                                                     the square of the Lax vector L2 (u) has no isolated roots. Panel
we only need to show that asymptotic (t) coincides with (t)
                                                                     (a) shows real, Re[c], and imaginary, Im[cm ], parts of the roots
of the m = −1 spin solution, i.e., that (t) → 0 at large times       cm , and panel (b) shows the corresponding | (t)| for a detuning
after the quench whenever L2 (u) has no isolated complex roots       quench in a 3D two-channel model with γ = 0.1 and N = 1024
(region I in quench phase diagrams above). We confirm this           spins. There are N + 1 pairs of complex conjugate continual roots
numerically; see, e.g., Figs. 5 and 12 and Refs. [16,18]. There      whose imaginary parts scale as 1/N so that in the N → ∞ limit they
is also a justification of this statement based on the general       form a continuum on the real axis. Here 0i = 0.34 max , 0f =
theory of integrable Hamiltonian dynamics. It works for both         8.1 × 10−3 max , μi = 0.91εF , and δω = 3.45γ .
m = −1 and m = 0 and we present at the end of the m = 0
case below Eq. (2.65).
    To summarize, if L2 (u) has no isolated complex roots            and Bogoliubov amplitudes it reads
for given (quench) initial conditions, then (t) → 0 at large                                          
                                                                                    ˙ = −iω + ig 2      2sp up v̄p .                                        (2.50)
times in the thermodynamic limit and the steady-state spin
                                                                                                                              p
configuration is
                  cos θp         sin θp −2iεp t+iδp                  The reduced m-spin solution is a particular solution (Up ,Vp ) of
        spz = −          , sp− =       e            ,       (2.48)   the BdG equations that also satisfies the above self-consistency
                    2              2
                                                                     condition (with sp → σp ). It is straightforward to check that
where                                                                (V̄p , −Up ) is also a solution of the BdG equations with the
                                      
                                                                     same (t). Since for any fixed (t) these equations are linear
                             L2 (ε− ) − L2 (ε+ )                     in the amplitudes, their most general normalized solution with
         cos θ (ε) = z(ε)                               ,   (2.49)
                                   iπ ν(ε)                           this (t) is a linear combination of these two independent
and θp ≡ θ (εp ). This expression evaluates explicitly for quench    solutions,
initial conditions; the answer is given by Eq. (3.11). The sign                                                 
                                                                               up           θp Up           θp V̄p
z(ε) = ±1 is fixed by requiring that cos θ (ε) be smooth and                         = cos           + sin             .       (2.51)
                                                                                vp           2 Vp           2 −Ūp
spins sp point in the negative z direction at εp → ∞ (so that
corresponding single-particles states be empty).                     The coefficients are made real by dropping an unimportant
    The logic for m ⩾ 0 is similar, but the calculation is a         overall time-independent phase and including the relative
bit more involved. To derive the analog of Eq. (2.45), it is         phase into the common phase of Up and Vp . At this point θp
convenient to work with the BdG equations (1.31). In addition,       is an arbitrary angle. This solution does not generally satisfy
there is an equation of motion for b in Eq. (1.8), which can be      the self-consistency condition (2.50) at finite t, but, as we see
viewed as a self-consistency condition. In terms of = −gb            below, becomes self-consistent as t → ∞.

                                                               033628-15
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                   PHYSICAL REVIEW A 91, 033628 (2015)

   Let us now determine the spins corresponding to this                       Lred (u), (t) is described by this m-spin solution at large times
solution. Equation (2.51) implies                                             and satisfies the self-consistency condition (2.50), and the
    |vp |2 − |up |2 = (|Vp |2 − |Up |2 ) cos θp                               asymptotic spin configuration (2.55) and the m-spin problem
                                                                              have the same integrals of motion as the quench dynamics.
                       − sin θp (Ūp V̄p + Up Vp ),                (2.52)     The remaining N + 1 constants required to match the initial
                                         sin θp  2                          conditions are in αp (see below) and in the phase of (t).
              up v̄p = Up V̄p cos θp +           V̄p − Up2 .                     To determine αp , rewrite the BdG equations as
                                           2
True spins sp are related to up , vp through Eq. (1.32) with                                                 Vp                   Up
                                                                                    i∂t (ln Up ) = εp +         ,     i∂t (ln Vp ) = −εp + ¯
                                                                                                                                     .
sp = 1/2. Spins σp are similarly related to Up ,Vp . Let                                                     Up                   Vp
                                                                                                                                   (2.58)
                                             αp − φp
                      Up = |Up | exp i               ,                        Adding these equations and using Eqs. (2.53) and (2.54), we
                                                2                             get, after some algebra,
                                                                   (2.53)
                                       αp + φp                                                                σp ( ¯ σp− +      σp+ )
                      Vp = |Vp | exp i         .                                                   α̇p = −                                 .   (2.59)
                                          2                                                                           |σp− |2
We can express the absolute values of the amplitudes and their
relative phase through the spin components                                                                       1. m = 0
                                                                                              2
                 σpz              σpz                             σp−           Suppose L (u) has a single pair of isolated complex roots at
             1                 1
  |Vp |2 =     +     , |Up |2 = −     ,                ,e−iφp =               u = μ∞ ± i ∞ . The 0-spin expression (2.18) for (t) reads
             2 2σp             2 2σp            |σp− |
                                                                                                                         −2iμ∞ t−2iϕ
                                                  (2.54)                                                 (t) =      ∞e                 .       (2.60)
while their common phase αp needs to be determined sepa-
rately from the BdG equations.                                                The notation ∞ and μ∞ anticipates that this is also the
   We obtain in this notation                                                 long-time asymptote for the quench dynamics. Equation (2.20)
                                                                              implies
            σpz cos θp       |σp− | sin θp
    spz =                −                   cos αp ,                                             σp−         (t)        σpz        ξp
            σp    2           σp     2                                                                   =        ,            =−       ,      (2.61)
                                    z                  (2.55)
                                                                                                 σp         Ep∞         σp         Ep∞
          −
    −
        σp  cos θp   sin θp   −iφp
                                    σp
   sp =            +        e          cos αp − i sin αp .                    where Ep∞ = E(εp ; ∞ ,μ∞ ) = (εp − μ∞ )2 + 2∞ and
        σp 2           2            σp
                                                                              ξp = εp − μ∞ .
Note that σpz /σp and σp− /σp are components of the unit vector                  Equation (2.59) obtains α̇p = −2Ep∞ . We see that αp is of
along the spin in the reduced solution σp . Geometrically,                    the form (2.57) and therefore the large-time asymptote of (t)
Eq. (2.55) says that sp makes a constant angle θp (or π − θp                  according to the few-spin conjecture is given by Eq. (2.60). The
for negative σp ) with σp and rotates around it with an angular               asymptotic spin configuration is then Eq. (2.55) with cos θp ≡
velocity α̇p ,                                                                cos θ (εp ) given by Eq. (2.49). Explicitly, using Eq. (2.61) and
                                                                              αp = −2Ep∞ t − δp , we obtain
                                 σp cos θp
                         sp =              + sp⊥ .                 (2.56)
                                 σp 2                                                                 ξp             ∞
                                                                                           spz = −        cos θp −      sin θp cos(2Ep∞ t+δp ),
To see this, consider a body set of axis for σp . Take z along                                      2Ep∞          2Ep∞
σp , x  axis along the intersection of the zz plane with the                                      ∞          sin θp 2iEp∞ t+iδp
plane perpendicular to σp , and y  normal to x  z to form a                sp− e2iμ∞ t+2iϕ =     ∞
                                                                                                      cos θp −       e                         (2.62)
                                                                                                  2Ep            2
right-handed coordinate system as usual. Then αp is the angle                                            
between sp⊥ and the x  axis and Eq. (2.55) follows.                                              −
                                                                                                    ξp
                                                                                                        −1
                                                                                                            sin θp
                                                                                                                   cos(2Ep∞ t + δp ).
    The contribution of the second terms on the right-hand side                                     Ep∞       2
of Eqs. (2.55) and (2.56) (terms containing αp ) to L(u) at u
away from the real axis and to J− (t) vanishes (dephases) at                  In a reference frame rotating with frequency 2μ∞ around z
large times at least for m = 0 and 1 in the thermodynamic                     axis, (t) → ∞ meaning that magnetic field acting on spin
limit, the same as in the m = −1 case considered above. For                   sp is time independent. In this frame sp rotates around the field
this to be true it is sufficient that αp contain a dispersing linear          or, equivalently, around the reduced spin σp with frequency
in t term, i.e.,                                                              2Ep∞ as described by Eq. (2.62).
                                                                                  We can also determine the Bogoliubov amplitudes corre-
                         αp = −2ep t + Fp (t),                     (2.57)     sponding to the 0-spin solution from Eqs. (2.53) and (2.54),
                                                                                                  
where ep is a continuous nonconstant function of εp and Fp (t)                                      1       ξp −iEp∞ t−iμ∞ t−iϕ
is a bounded function of t. Note that for m = −1, ep = εp and                               Up =       +         e              ,
Fp (t) = δp = const.                                                                                2 2Ep∞
    To derive the asymptotic state, we follow the same pro-                                                                            (2.63)
cedure as for m = −1 above. We set 2σp = cos θp , where                                      Vp =
                                                                                                    1
                                                                                                       −
                                                                                                            ξp −iEp∞ t+iμ∞ t+iϕ
                                                                                                                 e              .
cos θp ≡ cos θ (εp ) is given by Eq. (2.49). Then L(u) →                                            2 2Ep∞

                                                                        033628-16
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                                    PHYSICAL REVIEW A 91, 033628 (2015)


     (a)              1                                                                        (t). In this frame, the effective magnetic field acting on
                                                                                             each spin sp in Eq. (1.8) is Bp = −2 ˜ ∞ x̂ + 2(p − μ̃∞ )ẑ
                                                           Im[c _ ]/ 0f
                                                                +
                                                                                             and is time independent. The spin therefore rotates around
                                                           Im[cm]/0.1 0f
                    0.5
                                                                                             the field, making a constant angle (call it π − θp ) with it. It is
                                                                                             straightforward to determine spin components in this situation.
                                                                                             They are given by Eq. (2.62) with μ∞ → μ̃∞ , ∞ → ˜ ∞ ,
                     0
                                                                                             and absent e2iμ∞ t+2iϕ on the left-hand side in the rotating
                                                                                             frame.
                -0.5                                                                            Next we evaluate Lax vector (2.1) for this spin configura-
                                                                                             tion. For u away from the real axis, summations over p can be
                                                                                             safely replaced with integrations in the continuum limit and
                     -1
                           0.4    0.6        0.8            1         1.2
                                                                                             contributions from oscillating terms on the right-hand side of
                                        Re[c] / F                                            Eqs. (2.62) vanish at t → ∞. The same cancellation occurs in
                                                                                             the gap equation of motion (1.33), so that it becomes Eq. (5.4)
                      1
     (b)                                                                                     that we will later also need in a different context. Using this
                    0.9                                             8                        gap equation to simplify the expression for L(u), we obtain
                                                                            0f
                    0.8
                                                                                                          L(u) = [ ˜ ∞ x̂ − (u − μ̃∞ )ẑ]L∞ (u),         (2.64)
                    0.7

       | (t)|/ 0f
                                                                                             where
                    0.6                                                                                               2           1
                                                                                                           L∞ (u) =       −                 .            (2.65)
                    0.5                                                                                               g 2
                                                                                                                            p
                                                                                                                              2(u − εp )Ep∞
                    0.4
                                                                                             We see that L2 (u) = [ ˜ 2∞ − (u − μ̃∞ )2 ]L2∞ (u) has a pair of
                    0.3                                                                      isolated roots at u = μ̃∞ ± i ˜ ∞ ; i.e., the parameters of the
                    0.2                                                                      asymptotic (t) must coincide with those of an isolated root.
                       0     20         40            60         80              100
                                                  t                                             Finally, there is a general argument explaining why the
                                             0f                                              actual quench dynamics at t → ∞ should be described by
    FIG. 13. (Color online) Roots of L2 (u) (top) and | (t)| for a
                                                                                             the above asymptotic solutions derived from −1 and 0
detuning quench in a 3D two-channel model for N = 1024 spins,                                spin solutions at least when L2 (u) has none or only one
γ = 1.0. There is one pair of isolated roots c± = μ∞ ± i ∞ whose                             isolated root pair (m = −1 and 0). The general motion of
imaginary part remains finite in the large N limit and N − 1 continual                       a classical Hamiltonian integrable model with N degrees of
roots cm close to the real axis (Im[cm ] is magnified by 10). Observe                        freedom is quasiperiodic with N independent frequencies,
| (t)| → ∞ in agreement with the few-spin conjecture. Here                                   ω = (ω1 , . . . ,ωN ), which are determined solely by the values
  0i = 0.18 max ,   0f = 0.78 max , and δω = −2.26γ .                                        of its integrals of motion [63,64]. There are two types of
                                                                                             (quasi)periodic motion: libration and rotation [65]. Let us
                                                                                             explain this terminology with a 1D example. In libration, the
These in turn determine the “real” asymptotic amplitudes                                     coordinate returns to its initial value after each period, such
according to Eq. (2.51) and therefore the many-body wave                                     as, e.g., the coordinate of a harmonic oscillator. In rotation, it
function (1.29), which allows one to calculate various few-                                  increases each time by a fixed amount, such as, e.g., the angle
particle Green’s functions.                                                                  of a rotating pendulum. Dynamical variables of libration type
    As before, to verify the few-spin conjecture in the present                              can be decomposed in a multidimensional Fourier series as
case it is enough to check that the large-time asymptote of (t)                                                             
                                                                                                                     Q(t) =     cm ei ω·mt ,            (2.66)
after the quench is given by Eq. (2.60) as long as L2 (u) has
                                                                                                                            m
one pair of isolated complex conjugate roots (regions II and
II in quench phase diagrams above). We do so numerically;                                   where m = (m1 , . . . ,mN ) is a vector with integer components.
see, e.g., Figs. 7 and 13 and Refs. [16,18]. The large-time                                  Dynamical variables of rotation type contain an additional
asymptote of | (t)| is in excellent agreement with ∞ derived                                 linear term, i.e.,
as the imaginary part of the isolated root; see, e.g., Fig. 2 in                                                               
                                                                                                                Q(t) = c0 t +      cm ei ω·mt ;        (2.67)
Ref. [18]. This is, however, guaranteed by conservation laws
                                                                                                                                m
without reliance on the few-spin conjecture. Indeed, suppose
we find (t) → ˜ ∞ e−2i μ̃∞ t−2i ϕ̃ . Starting with this, one can                             see, e.g., Ref. [65] for further details. In our case, the absolute
retrace the steps that lead to Eq. (2.62) backwards and show                                 value of the order parameter, | (t)| is of libration type, while
that L2 (u) has a single pair of isolated complex conjugate roots                            its phase is of rotation type.
at μ̃∞ ± i ˜ ∞ . In other words, μ̃∞ = μ∞ , ˜ ∞ = ∞ , and the                                    The frequency spectra of asymptotic solutions con-
constant ϕ is arbitrary in the 0-spin solution, so we can always                             structed above are ω(εp ) = 2εp for m = −1 and ω(εp ) =
set ϕ̃ = ϕ. Let us prove this somewhat differently using Bloch                               2 (εp − μ∞ )2 + 2∞ for m = 0. Important for us is that
rather than BdG equations.                                                                   the spectra are continuous with no isolated frequencies in
    Going to a reference frame rotating around the z axis with                               the thermodynamic limit. Since setting 2σp = cos θp ensures
frequency 2μ̃∞ eliminates time dependence in the asymptotic                                  that the quench dynamics has the same integrals as this

                                                                                       033628-17
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                              PHYSICAL REVIEW A 91, 033628 (2015)

solution (lives on the same invariant torus), it also must                 The general expression for the reduced spins obtain from
have an identical frequency spectrum. Assuming | (t)| is                 Eqs. (2.23), (2.27), and (2.34),
continuously distributed over the spectrum as a collective
variable, i.e., the discrete summation in Eq. (2.66) turns into a                             σpz         | |2 − 2ξp2 + 2ρ
continuous Fourier transform, it must dephase at large times,                                       =−                           ,
                                                                                              σp                2 Q4 (εp )
| (t)| → const. Under the same assumption, the phase of                                                                                         (2.72)
the order parameter according to Eq. (2.67) must tend to a                                 σp−            2ξp     − 2μ + i ˙
linear-in-time function as t → ∞. Therefore, (t) at large                                           =−                       ,
                                                                                           σp                    2 Q4 (εp )
times is of the form ∞ e−2iμ∞ t−2iϕ . Since finite ∞ also
implies an isolated root at μ∞ ± i ∞ , while for m = −1 there            where ξp = εp − μ and is given by Eq. (2.68). Bogoliubov
are no isolated roots by definition, we must have ∞ = 0, i.e.,           amplitudes corresponding to the 1-spin solution can now be
  (t) → 0 in this case.                                                  derived from Eq. (2.58). The imaginary and real parts of
   We also prove the few-spin conjecture for infinitesimal               the right-hand sides determine the absolute values of the
quenches in Sec. V D independently of above arguments and                amplitudes and their phases, respectively,
numerics.
                                                                                                                                                 
                            2. m = 1                                                  2cp+ − | |2                                κ − 4ξp cp+
                                                                                                         −iμt+iξp t
                                                                           Up =                      e                exp i                    dt ,
    Suppose we found that for some initial condition (quench                             1/4
                                                                                    2Q4 (εp )                                    2cp+ − | |2
parameters) L2 (u) has two pairs of isolated complex conjugate
                                                                                                                                             
roots c,c̄,c ,c̄ . Given c and c , the above method allows us to
                                                                                      2cp− + | |2                               κ + 4ξp cp−
determine the long-time asymptote of (t), asymptotic spin                  Vp =                     e   iμt−iξp t
                                                                                                                    exp i                     dt ,
configuration, and time-dependent Bogoliubov amplitudes                                 1/4
                                                                                    2Q4 (εp )                                   2cp− + | |2
up (t),vp (t) for the dynamics of the two-channel model (1.9)                                                                (2.73)
starting from this initial condition at t = 0.                           where cp± = Q4 (εp ) ± (ξp2 − ρ).
    By construction, c,c are also the roots of L2m (u) furnishing         The common phase of the amplitudes αp is the sum of their
the spectral polynomial for the reduced problem Q4 (u) =                 phases in the above equations; i.e.,
(u − c)(u − c̄)(u − c )(u − c̄ ) and therefore the parameters
μ,ρ,κ,χ through Eq. (2.35). We further obtain from Eq. (2.41)                                  κ − 4ξp cp+            κ + 4ξp cp−
                                                                              αp =                           +                     dt.        (2.74)
                                                 κdt                                           2cp+ − | |    2        2cp− + | |2
     (t) =          2 + h exp −2iμt − i                   , (2.68)
                         1                       2+h
                                                      1
                                                                         The integrand is a periodic function of time. Therefore, αp
where     is the Jacobi elliptic function dn,                            is of the form (2.57), which is seen, e.g., by expanding the
                                                                        expression under the integral in Fourier series. The linear
                                                  h3 − h2                part ep t comes from the zeroth harmonics. We only need to
     =     h3 − h1 dn     h3 − h1 (t − t0 ),              ,     (2.69)
                                                  h3 − h1                show that ep is a nonconstant (dispersing) function of εp . For
                                                                         this, we expand the integrand for large εp , ep = εp + O(1).
t0 is a constant, and h3 ⩾ h2 ⩾ h1 are the roots of the third-
                                                                         Therefore, ep is indeed dispersing and the contribution of
order polynomial P3 (w) = w 3 + 4ρw 2 + 4χ w + κ 2 .√  The am-
plitude | (t)| oscillates between   a minimum       =    h2 and          second terms on the right-hand sides of Eq. (2.55) to L(u)
                    √                             b
                                                                         and J− (t) dephases similarly to m = −1,0 cases. By few-
a maximum a = h1 . Plots of a , b , and h1 for various
quenches are shown in Figs. 9 and 10. As we now see, the                 spin conjecture the asymptotic behavior of (t) is then
parameter h1 also quantifies the deviation from the weak-                given by Eqs. (2.68). The asymptotic spin configuration
coupling limit, where h1 = 0.                                            obtain by substituting Eqs. (2.74) and (2.72) into Eq. (2.55),
    Of interest is the particular case when the parameter                where cos θp ≡ cos(εp ) is given by Eq. (2.49) and e−iφp =
κ = 0. As we see below, this is realized for quenches deep               σp− /|σp− | straightforwardly derives from the second equation
within the weak-coupling BCS regime in the broad resonance               in Eq. (2.72).
limit when the two-channel model is equivalent to the                       As before, to verify the few-spin conjecture, it is sufficient
BCS Hamiltonian (1.11). κ = 0 implies h1 = 0, 4χ = h2 h3 ,               to check that (t) at large times after the quench is described
4ρ = −h2 − h3 , and Q4 (u) = [(u − μ)2 − ρ]2 − χ . Let h3 =              by Eq. (2.68) whenever L2 (u) has two pairs of isolated roots.
                                                                         We do this numerically; see Figs. 8 and 14–16. In these plots
  + ,h2 =
  2          2
             − in accordance with the notation of Eq. (2.38).
The roots of Q4 (u) in this case take a simple form with shared          we compare (t) from direct numerical evolution of 5024
real part. Namely, they are                                              spins to Eq. (2.68), where parameters h1 ,h2 ,h3 , and μ obtain
                                                                         from the isolated roots of L2 (u). Note that there are no fitting
                                 +±      −                               parameters apart from an overall shift t0 along the time axis.
                        μ±i            ,                        (2.70)
                                 2
and the expression (2.68) simplifies as well,
                                                                         III. QUENCH PHASE DIAGRAM AND ASYMPTOTIC SPIN
                                                −2iμt−2iϕ
               (t) =    + dn[   + (t − t0 )]e               .   (2.71)       DISTRIBUTION FOR THE TWO-CHANNEL MODEL
This expression for (t) and the corresponding m = 1 spin                   We established in the previous section that the long-time
solution were constructed in Ref. [7].                                   dynamics of the system after a quench are determined by

                                                                   033628-18
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                                     PHYSICAL REVIEW A 91, 033628 (2015)


       (a)           0.5                                                                   (a)
                                                                                                                                                     numerics
                                                                                                                                                     analytics
                                                            Im[c,c’]/ 0f
               0.25                                         Im[cm]/0.1 0f                                20



                      0                                                                      Φ(t)/2π
                                                                                                         10

              -0.25


                                                                                                          0
                 -0.5                                                                                          20             40            60                 80
                           0.4    0.6   0.8    1       1.2       1.4    1.6                                                        Δ0f t
                                          Re[c] / F
                     0.9                                                                   (b)             1
       (b)                                                                                                                                         numerics
                                                                  numerics                                                                         analytics
                     0.8                                          analytics
                                                                                                         0.8
                     0.7

                     0.6

                                                                                            |Δ(t)|/Δ0f
                                                                                                         0.6

        | (t)|/ 0f
                     0.5

                     0.4                                                                                 0.4
                     0.3

                     0.2                                                                                 0.2

                     0.1

                      0                                                                                   0
                                 110     120          130         140                                                    40                60                  80
                                                  t                                                                                Δ0f t
                                               0f

    FIG. 14. (Color online) Roots of L2 (u) (top) and | (t)| for a                     FIG. 15. (Color online) Magnitude and phase of (t) in region III
detuning quench in a 3D two-channel model with N = 1024 spins                       (two pairs of isolated roots) after detuning quench from deep BCS to
and γ = 1.0. There are two pairs of isolated roots (c,c̄) and (c ,c̄ ) and        BEC in a 3D two-channel model for γ = 1. Numerical evolution with
N − 2 continual roots close to the real axis. The large-time asymptote              5024 spins against Eq. (2.68). Parameters h1 ,h2 , etc., are obtained
of | (t)| is described by Eq. (2.68), where parameters hi are extracted             from isolated roots of L2 (u) as described in the text. 0i = 2.65 ×
from the isolated roots, in agreement with the few-spin conjecture.                 10−2 max , 0f = 0.80 max , μi = 1.00εF , δω = −4.59γ .
The phase of (t) is also in excellent agreement; see, e.g., Figs. 8
and 15. Quench parameters are 0i = 2.68 max , 0f = 0.76 max ,                       initial condition into the definition (2.1)
and δω = −4.13γ .
                                                                                                                                                   δω
                                                                                          L(u)|t=0 = [              0i x̂ − (u − μi )ẑ]L0 (u) −      ẑ,           (3.1)
                                                                                                                                                   g2
the isolated complex roots of L2 (u). We now proceed to                             where δω = ωf − ωi and
evaluate the roots and thus construct the quench phase diagram:                                                   
identify all possible steady states for quenches throughout the                                               2              1
                                                                                                L0 (u) = − 2 +                           ,    (3.2)
BCS-BEC crossover. We find that, depending on the quench                                                     g     p
                                                                                                                      2(u − εp )Ei (εp )
parameters, L2 (u) has zero, one, or two pairs of complex                                                       
conjugate roots and the long-time behavior is therefore that                        Ei (εp ) = E(εp ; 0i ,μi ) = (εp − μi )2 + 20i and we also
described in Secs. II D, II D 1, or II D 2, respectively. Imaginary                 used the gap equation (1.18).
and real parts of the roots determine the parameters of the                             Taking the square of the above expression for L(u) and
asymptotic behavior. For example, in the Volkov and Kogan                           equating it to zero, we obtain an equation for the roots
regime (region II in our quench phase diagrams) where                                                                               
   (t → ∞) → ∞ e−2iμ∞ t−2iϕ , the roots are μ∞ ± i ∞ . We                                                 2              1                δω
first derive general equations for the roots, lines separating                       (u − μi ∓ i 0i ) 2 −                               = 2 . (3.3)
                                                                                                         g      p
                                                                                                                   2(u − εp )E  (ε
                                                                                                                              i p  )       g
distinct regimes, and the asymptotic distribution function
and then consider various cases, such as 2D and 3D, wide                            Suppose first that the single-particle levels εp are discrete and
(one-channel) and narrow resonance limits, and deep BCS and                         there are N  1 distinct εp . Then this is a polynomial equation
BEC regimes.                                                                        with N + 1 pairs of complex conjugate roots. Most of the
    After the quench the system evolves with the Hamilto-                           pairs are close to the real axis, at distances of the order of
nian (1.9), where ω = ωf starting from the spin configura-                          the spacing between εp , which is inversely proportional to N
tion (1.28), which is the ground state for ω = ωi . Since L2 (u)                    (system volume) and goes to zero in the thermodynamic limit.
is conserved, we can evaluate it at any t. It is convenient to do                   In the thermodynamic limit most of the roots of L2 (u) coalesce
so at t = 0. The Lax vector at t = 0 obtains by plugging the                        to the real axis merging with its poles to form a branch cut along

                                                                              033628-19
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                         PHYSICAL REVIEW A 91, 033628 (2015)

                    0.6
                                                                                                 1
                          (a)                          analytics
                                                                                                                                    Re[cm] / F
                                                       numerics
                    0.5                                                                                                             Re[cm] / F
                                                                                               0.5                                  Im[c+_ ] / 0i


       |Δ(t)|/Δ0f
                    0.4
                                                                                                0

                    0.3
                                                                                            -0.5

                    0.2
                                                                                                                                    5    6    7     8
                                                                                                -1

                          180     200          220          240                                  0      0.5       1       1.5       2        2.5        3
                                        Δ0f t                                                                             m
                                                                                                                              / F

                    0.3                                                              FIG. 17. (Color online) Roots of L2 (u) for the ground state of a
                          (b)                           analytics
                                                        numerics                 3D two-channel model for N = 54 spins and γ = 1.0. There are N
                                                                                 doubly degenerate real roots cm (shown as circles and squares), N − 1
                                                                                 of them located between discretized energy levels εp → εm , and two
                    0.2                                                          isolated complex roots c± = μi ± 0i . Here 0i = 0.1εF .
       |Δ(t)|/Δ0f
                                                                                 limit, spacings between εp ’s vanish and real zeros and poles
                    0.1                                                          merge into a continuous line. For δω = 0 the real roots acquire
                                                                                 imaginary parts, each degenerate root splitting into a complex
                                                                                 conjugate pair, as shown in Figs. 12–14. The imaginary parts,
                                                                                 however, scale as 1/N .
                     800        850      900         950            1000            We first take the continuum limit in Eq. (3.3) for u away
                                        Δ0f t                                    from the real axis. Then only isolated complex roots remain
               0.08                                                              and we find that there are only zero, one, or two pairs of
                          (c)                           analytics                such roots depending on δω. At δω = 0 there are two isolated
                                                        numerics
                                                                                 complex conjugate roots at u = μi ± i 0i . One pair of roots
               0.06                                                              persists for sufficiently small |δω|, but beyond a certain
                                                                                 threshold the number of isolated roots changes, as we now
       |Δ(t)|/Δ0f                                                                demonstrate. The continuum limit of Eq. (3.3) reads
               0.04                                                                                                       ∞
                                                                                                 2           δω                  f (ε)dε     4
                                                                                                                +                           = ,             (3.4)
                                                                                           u − μi ∓ i     0i γ        0       (u − ε)Ei (ε)  γ
               0.02                                                              where, as always, we measure energies in units of εF and f (ε)
                                                                                 is the dimensionless density of states defined in Eq. (1.22).
                     2000       2200    2400         2600           2800             As δω is decreased or increased, the single pair of roots
                                        Δ0f t                                    can collapse to the real axis or a new pair of isolated roots
                                                                                 can emerge from it. The threshold (critical) value of δω when
    FIG. 16. (Color online) Postquench | (t)| for a 3D two-channel               this occurs is determined by looking for roots of Eq. (3.4)
model in region III, where L2 (u) has two pairs isolated roots.
                                                                                 with an infinitesimal imaginary part. Replace u → u ± iδ in
Numerical evolution with 5024 spins against Eq. (2.68). γ = 0.1,
                                                                                 Eq. (3.4) and use (u − ε ± iδ)−1 = P (u − ε)−1 ∓ iπ δ(u − ε)
  0i = 0.035 max in all three panels.   0f / max = 0.54,0.67, and
                                                                                 to separate its real and imaginary parts. The latter yields critical
0.85 in (a)–(c), respectively.
                                                                                 values of δω when the number of roots changes
                                                                                                              |δω|   πf (u)Ei (u)
the real axis. We fully verify this picture in this section and in                                                 =              ,                         (3.5)
                                                                                                                γ       2 0i
Appendix B. Here we consider the roots whose imaginary part
remains finite as N → ∞ and in Appendix B we evaluate the                        where u is real positive and obtains from the real part of
roots with vanishing imaginary parts to order 1/N.                               Eq. (3.4),
   Consider first the ground state. This corresponds to δω = 0                             ∞
                                                                                               f (ε)dε              π (u − μi )f (u)  4
in Eq. (3.3) and L2 (u) = [(u − μ)2 + 20 ]L20 (u). There is a                          −                  + sgn(δω)                  = ,                    (3.6)
pair of complex roots at c± = μ ± i 0 . The remaining 2N                               0    (u − ε)Ei (ε)              Ei (u) 0i      γ
roots solve L0 (u) = 0 and are double degenerate and real;                       where the dashed integral indicates principal value.
see Fig. 17. This is because L0 (u) goes from +∞ to −∞                              The last two equations determine critical lines in quench
as u goes from the left vicinity of one pole at u = εp to                        phase diagrams shown in Figs. 2, 3, 20, and 21. We construct
the right vicinity of the next one along the real axis, always                   the diagrams in the ( 0f , 0i ) plane, ground-state gaps at
crossing zero between consecutive εp ’s. In the thermodynamic                    final and initial detunings ωi and ωf . The resonance width

                                                                           033628-20
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                       PHYSICAL REVIEW A 91, 033628 (2015)

(dimensionless interaction strength) γ is fixed throughout the                   (a)
diagram. 0i , 0f , and γ uniquely determine μi , ωi , and                                                                              γ = 0.1
ωf through ground-state Eqs. (1.25) and (1.26). Each point                                  1
in this plane represents a particular quench of the detuning
ωi → ωf . We choose 0i (or, equivalently, the ratio μi / 0i )

                                                                                  Δ /Δmax
and the sign of δω and solve Eq. (3.6) for real u. Equation (3.5)
then yields the final detuning ωf and therefore 0f . We thus                           8 0.5
obtain a critical line, 0f as a function of 0i , in the ( 0f , 0i )
plane. The number of isolated root pairs changes by one as one                                                          Δ0i = 0.99Δmax
crosses this line.                                                                                                      Δ0i = 0.28Δmax
    It turns out there is one critical line for either sign
of δω. There are therefore three nonequilibrium phases or                                   0
                                                                                             0       0.2        0.4       0.6         0.8
regimes, qualitatively different long-time behaviors, indicated                                                 Δ0f /Δmax
as regions I, II (including subregion II ), and III in Figs. 2, 3, 20,
and 21. Region II contains the 0f = 0i or, equivalently,                         (b)
ωf = ωi line, which corresponds to no quench, i.e., to the                                                                             γ = 10
                                                                                            1               Δ0i = 0.89Δmax
system remaining in the ground state at all times. Therefore,                                               Δ0i = 0.03Δmax
in region II Eq. (3.4) yields a single pair of isolated complex
roots u = μ∞ ± i ∞ . This, in turn, implies that (t) →
                                                                                  Δ /Δmax
      −2iμ∞ t−2iϕ
  ∞e                as t → ∞. For all quenches in region II
the system thus goes into the asymptotic state described in                            8 0.5
Sec. II D 1.
    Negative δω corresponds to 0f > 0i . As we cross the
critical line going from region II into region III the number
of isolated root pairs changes by one. It can be shown
both analytically and numerically by analyzing Eq. (3.4) that                               0
                                                                                             0        0.2         0.4           0.6         0.8
this number increases; i.e., there are two pairs of complex                                                     Δ0f /Δmax
conjugate isolated roots in region III. For quenches in this
part of the diagram the large-time asymptote of (t) is given                  FIG. 18. (Color online) (t) → ∞ e−2iμ∞ t−2iϕ as t → ∞ after
by Eq. (2.68) and the large-time state of the system is that              a detuning quench ωi → ωf in a 3D two-channel model in region II
obtained in Sec. II D 2. Plots of ∞ and μ∞ as functions of                of the quench phase diagram in Fig. 3. ∞ extracted from the single
  0f at two fixed values of         0i are shown in Figs. 18 and 19.      isolated root pair of the Lax vector norm is shown as a function of 0f
    Similarly, as we enter region I from region II, ∞ → 0 and             (ground-state gap for ωf ) at two fixed values of 0i (ground-state gap
the single pair of isolated roots collapses to the real axis at the       for the initial detuning ωi ). Note that ∞ > 0f for BEC to BCS
critical line. There are hence no isolated roots in region I and          quenches 0i = 0.99 max for γ = 0.1.
therefore (t) → 0 for quenches in this regime and the system
goes into the gapless steady state detailed at the beginning of
Sec. II D.                                                                Equation (3.7) determines the μ∞ = 0 line via a procedure
    Of interest is the line along which the real part of the root         similar to that for critical lines separating region I from II and
pair μ∞ ± i ∞ in region II vanishes, i.e., μ∞ = 0 (the line               II from III. For a given 0i , the first equation yields ∞ . We
separating subregions II and II in quench phase diagrams).               then find δω and consequently ωf and 0f from the second
This can be thought of as a nonequilibrium extension of                   equation.
the BCS-BEC crossover going from a positive to a negative                     Note the intersection of the μ∞ = 0 line with the 0i =
chemical potential. Out of equilibrium, as we see below, the                 0f (no-quench) line. Along the latter line we also have ∞ =
change of sign of μ∞ affects the approach of (t) to its                      0i and, therefore, at the intersection point μi = μf = 0 or
asymptote. For example, in 3D the approach changes from                   the first term in the first equation in Eq. (3.7) would blow up.
1/t 1/2 in II to 1/t 3/2 in II . Setting u = ±i ∞ in Eq. (3.4) and       In equilibrium μ = 0 corresponds to a certain ground-state
separating the real and imaginary parts, we obtain equations              gap 0 = 0× , which obtains from Eq. (1.25) and provides a
determining this line,                                                    characteristic energy scale for the crossover from the BCS to
                                                                          BEC regime. Vanishing of μi and μf at the intersection point
                     μi                          4                        implies that straight lines 0i = 0× , 0f = 0× , and 0i =
                               Im F + Re F =       ,                         0f and the μ∞ = 0 line must cross at the same point, which
                  0i −    ∞                      γ
                                                                 (3.7)    is indeed seen in all quench phase diagrams in Figs. 2, 3, 20,
                 δω 2( ∞ − 0i )                                           and 21.
                                      = Im F,                                 Let us also obtain an explicit expression for the asymptotic
                  γ μ2i + ( ∞ − 0i )2
                                                                          spin distribution function Eq. (2.49) in all three regimes.
where                                                                     Equation (3.1) implies

                               ∞                                                                                                      δω 2
                                      f (ε)dε
                   F=                              .             (3.8)         L2 (u) =          0i L0 (u) +
                                                                                                 2 2
                                                                                                               (u − μi )L0 (u) +           .      (3.9)
                           0       (i ∞ − ε)Ei (ε)                                                                                    g2

                                                                   033628-21
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                                          PHYSICAL REVIEW A 91, 033628 (2015)


        (a)      2                                                                         (a)                                                                                 0x
                                                              γ = 0.1                                     1
                                                                                                                                                                                     0x

                 0                                                                                   0.8
                                                                                                                                                                               II′

        μ /εF
                                                                                                 / max
                                                                                                     0.6
              8 -2                                                                                                                                   II
                                 Δ0i = 0.99Δmax                                                    0i0.4
                                 Δ0i = 0.28Δmax
                -4
                                                                                                     0.2
                                                                                                                  I
                                                                                                                                                            III
                         0.2      0.4              0.6      0.8         1                                 0
                                                                                                           0              0.2            0.4              0.6           0.8      1
                                    Δ0f /Δmax                                                                                                           / max
                                                                                                                                                     0f
        (b)      0
                                                              γ = 10                       (b)            1
                                                                                                                                                     0x


               -25                                                                                   0.8
                                                                                                                          I                                       II′
                                                                                                   max
        μ /εF
                                                                                                     0.6
              8 -50
                                 Δ0i = 0.89Δmax
                                                                                                 /                                                                                   0x
                                                                                                   0i0.4
                                 Δ0i = 0.03Δmax
               -75                                                                                                                  II
                                                                                                     0.2


              -100                                                                                        0
                                                                                                                                               III
                  0        0.2     0.4              0.6     0.8         1                                     0               0.2        0.4              0.6       0.8          1
                                    Δ0f /Δmax                                                                                                      /
                                                                                                                                                0f          max
    FIG. 19. (Color online) (t) → ∞ e−2iμ∞ t−2iϕ as t → ∞ after                            (c)                                      0x
                                                                                                           1
a detuning quench ωi → ωf in a 3D two-channel model in region II
of the quench phase diagram in Fig. 3, where μ∞ plays the role of
                                                                                                         0.8
the out-of-equilibrium analog of the chemical potential. Here μ∞ is
extracted from the single isolated root pair of the Lax vector norm                                                                                                II′
and is shown as a function of 0f (ground-state gap for ωf ) at two                                 max
                                                                                                         0.6

fixed values of 0i (ground-state gap for the initial detuning ωi ). Note
that μ∞ behaves similarly to the ground-state chemical potential in                                                   I   II
                                                                                                 /       0.4
Fig. 1.                                                                                            0i
                                                                                                                                                                                         0x
                                                                                                         0.2

In the thermodynamic limit,                                                                                                                      III
                                                                                                          0
                                             ∞                                                                0               0.2        0.4               0.6           0.8         1
                             2                      f (ε)dε                                                                                        /
                  L0 (u) = − 2 +                                .           (3.10)                                                              0f          max
                            g            0       2(u − ε)Ei (ε)
                                                                                          FIG. 20. (Color online) Detuning quench phase diagrams for
We evaluate L0 (ε± ) using (ε − ε ± iδ)−1 = P (ε − ε )−1 ∓
                                                                                     two-channel model in 2D for various resonance widths γ obtained
iπ δ(ε − ε ). This results in
                                                                                     from Eqs. (3.16) and (3.17). Each point represents a single quench
                                                                                    labeled by 0i and 0f , pairing gaps the system would have in the
                  z(ε)                             δω 2                              ground state for initial and final detunings. At large times the system
   cos θ (ε) =             A2− 20i + (ε − μi )A− +
                iπf (ε)                             γ                                ends up in one of three steady states shown as regions I, II (including
                                                                                    II ), and III. For quenches in region I the order parameter vanishes.
                     z(ε)                             δω 2                           In II (t) → ∞ e−2iμ∞ t−2iϕ and III | (t)| oscillates persistently.
                −            A2+ 20i + (ε − μi )A+ +       ,                         Subregions II and II differ in the sign of μ∞ (out-of-equilibrium
                   iπf (ε)                             γ
                                                                                     analog of the chemical potential): μ∞ > 0 in II and μ∞ < 0 in II . The
                                                                            (3.11)   diagonal, 0i = 0f , is the no-quench line. 0× is the ground-state
                                                                                     gap corresponding to zero chemical potential; i.e., 0× is given by
where                                                                                Eq. (1.25) for μ = 0.
                                     ∞
                      2   iπf (ε)        f (ε )dε
      A∓ = −            ±         +−               
                                                       .                    (3.12)
                      γ   2Ei (ε)   0 2(ε − ε )Ei (ε )
                                                                                     regime, and in BEC regime in Secs. III A and III B below;
The integral here is the same as in Eq. (3.6). We evaluate                           see also Eqs. (B4) through (B7) for explicit expressions.
it in elementary functions in 2D, in the weak-coupling BCS                           Note cos θ (ε) = 1 for δω = 0 (no quench) as it should.

                                                                               033628-22
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                                                       PHYSICAL REVIEW A 91, 033628 (2015)


    (a)                                                                                                                                        A. 2D
                                                                                          0x
                   1
                                                                                               0x                 In 2D the dimensionless density of states f (ε) = 1 and all
                                                                                                               integrals above in this section can be evaluated in terms of
              0.8
                                                                                              II′              elementary functions. It is convenient to introduce a notation:

          / max
              0.6                                                                                                                x=
                                                                                                                                       μi
                                                                                                                                           , v=
                                                                                                                                                   u − μi
                                                                                                                                                           .            (3.14)
                                                                 II                                                                       0i              0i
            0i0.4                                                                                              Equation (3.4) reads
                                                                                                                                                √
                                                                                                                                    (v + x)(v + 1 + v 2 )
              0.2                                                                                                            ln − √        √
                        I                                                                                                           1 + x 2 1 + v 2 − xv + 1
                   0
                                                                  III                                                              2δω(v ∓ i) 4 0i
                    0           0.2                  0.4                0.6         0.8   1                                    =− √           +         1 + v2.             (3.15)
                                                                    / max                                                          γ 1 + v2        γ
                                                                 0f
                                                                                                               The critical lines separating the three asymptotic regimes are
    (b)             1
                                                                 0x
                                                                                                               determined by Eqs. (3.6) and (3.5), which become
                                                                                                                                      |δω|   π
              0.8
                                I                                                                                                          =       1 + v2,                  (3.16)
                                                                              II′                                                       γ    2
            max                                                                                                                                √
              0.6                                                                                                                  (v + x)(v + 1 + v 2 )
                                                                                                                             ln √         √
          /                                                                                    0x                                  1 + x 2 1 + v 2 − xv + 1
            0i0.4
                                                                                                                                                  4 0i
                                                II                                                                              = −sgn(δω)π v +         1 + v2,             (3.17)
                  0.2
                                                                                                                                                    γ
                                                                                                               where v is real and v > −x. It is straightforward to analyze
                   0
                                                           III                                                 Eq. (3.17) graphically and to find v and thus the critical lines
                       0            0.2              0.4                0.6      0.8      1
                                                               /                                               numerically.
                                                            0f            max                                     Positive δω mean 0f > 0i and the corresponding v
    (c)                                                           0x
                                                                                                               determine the critical line separating regions I and II. In this
                  0.4
                                                                                                               case, for γ above a certain threshold γc to be determined below,
                                                                                                               there is a single root for any 0i . This means that a horizontal
                            I                                                                                    0i = const line intersects the I-II line once for any value of the
                                                                                II′                            const and region I therefore extends all the way up to 0i =
                                                                                                               √
            max                                                                                                  γ = max as seen in Figs. 2(c), 20(b), and 20(c). When
                  0.2
                                                                                                    0x         γ < γc , the number of roots for positive δω changes from one
          /                                                                                                    to two and then to zero as 0i increases. The I-II line then
            0i                                                                                                 displays peculiar reentrant behavior; see the inset in Fig. 2(b).
                                            II
                                                                                                                  Negative δω means 0f < 0i . The roots v in this case
                                                                                                               yield the II-III critical line. There are two roots for 0i below
                    0
                                                             III                                               a certain threshold and no roots above it, implying that a
                        0                 0.1                    0.2            0.3       0.4
                                                                   /                                           horizontal 0i = const line intersects the II-III critical line
                                                            0f            max                                  twice for a sufficiently small value of the const.
                                                                                                                  The shape of the critical lines as well as the complex roots
   FIG. 21. (Color online) Detuning quench phase diagrams for a
                                                                                                               of Eq. (3.15) can be determined analytically when the initial
two-channel model in 3D for various resonance widths γ obtained
from Eqs. (3.40) and (3.41) (otherwise, the same as Fig. 20).
                                                                                                               and/or final value of the detuning ω is deep in the BCS or BEC
                                                                                                               regime. The BCS limit corresponds to detuning ω → +∞.
                                                                                                               For the ground state this implies μ → εF = 1, 0 → 0. The
Representative plots of the spin distribution function for two
                                                                                                               gap equation (1.26) then yields
quenches appear in Fig. 11. For future use we also write the
first two terms in large ε expansion of Eq. (3.11),                                                                                        4ε      2ω − 4
                                                                                                                                       ln 2 =              .                (3.18)
                                                                                                                                                      γ
                                          2                                                                                                 0
                                    δω                       2 20i                                             The deep BEC regime obtains when ω → −∞. In this case
  cos θ (ε) ≈ 1 −                                                               ,                   (3.13)
                                     γ           Ei2 (ε)[H 2 (ε) + π 2 f 2 (ε)]                                μ → −∞ in the ground state. The gap and chemical potential
                                                                                                               equations switch roles in the sense that the former determines
which are also independently the first two terms in its small                                                  the chemical potential and the latter the ground-state gap.
δω expansion. The function H (ε) is defined in Eq. (B8).                                                       Equation (1.26) becomes
   Next, we consider 2D and 3D separately, as well as various                                                                          ε      2ω + 4|μ|
special cases such as wide (single-channel limit) and narrow                                                                       ln      =                            (3.19)
                                                                                                                                       |μ|        γ
resonance and deep BCS and BEC regimes.


                                                                                                         033628-23
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                          PHYSICAL REVIEW A 91, 033628 (2015)

and Eq. (1.25) reads in this limit                                       the asymptotic value of order-parameter amplitude, which is
                                                                       much smaller than εF . Equation (3.15) becomes
                            1      1 −1/2                                                √
                    0 =        +          .                    (3.20)               v + 1 + v2             v ∓ i 2δω
                            γ    4|μ|                                            ln      √          = −√             .        (3.26)
   First, we consider quenches originating deep in the BCS                          v − 1 + v2             1 + v2 γ
regime; i.e., ωi → +∞ and, therefore, 0i → 0, μi → 1.                    This equation is symmetric with respect to complex conjuga-
Such initial states correspond to x → +∞. Equation (3.17)                tion and with respect to v → −v. The latter symmetry reflects
becomes                                                                  emergence of the particle-hole symmetry in the BCS limit.
                  √                                                      Note that when there is only one root, these two symmetries
          (v + x)( 1 + v 2 + v)
     ln        √                  = −sgn(δω)π v.      (3.21)             together require that it be purely imaginary.
             x( 1 + v 2 − v)                                                Let v = −i cosh φ in Eq. (3.26), where φ is either purely
The roots are v → 0 for either sign of δω and v → −x + 0                 real or purely imaginary, so that v is purely imaginary.
for δω < 0. This translates into                                         Equation (3.26) yields, depending on the sign choice on the
                                                                        right-hand side,
                       μi ,        δω > 0,
                u≈                                 (3.22)
                       μi or +0, δω < 0.                                                             δω
                                                                                             φ=−        coth(φ/2),                       (3.27)
                                                                                                      γ
For v → 0 Eq. (3.16) yields δω/γ = ±π/2. Therefore, both
  0f and    0i are deep in the BCS regime. The gap equation                                          δω
Eq. (3.18) implies 0 ∝ exp(−ω/γ ) and, hence,                                                φ=−        tanh(φ/2).                       (3.28)
                                                                                                      γ
                                  0i
                                       = e±π/2 .               (3.23)    Note that in this regime δω/γ = ln( 0i / 0f ). It is straightfor-
                              0f                                         ward to analyze these equations graphically and to determine
This result has been already obtained in Refs. [17,18], which            when they have solutions. We summarize the results.
studied quenches within the single-channel model in the weak-               Region I: 0i / 0f > eπ/2 . There are no isolated roots and,
coupling (BCS) limit. Weak coupling means small 0i and                   hence, (t) → 0 at large times.
                                                                            Region II: e−π/2 < 0i / 0f < eπ/2 . There is a single pair
  0f , which corresponds to a vicinity of the origin,            0i =
                                                                         of isolated roots at μ∞ ± i ∞ ,
  0f = 0, in our phase diagrams. Equation (3.23) is the slope
of the I-II and II-III critical lines at the origin in Figs. 2, 3, 20,                   μ∞ = εF ,       ∞ =        0i cosh φ,           (3.29)
and 21.
   As we see below, Eq. (3.23) also holds in 3D. This is                 where φ is real for δω < 0 and imaginary for δω > 0 and is the
expected on general grounds because, in the BCS limit,                   solution of Eq. (3.27). One can show ∞ ⩽ 0f for any δω,
superconducting correlations come from a narrow energy                   where the equality is achieved only at δω = 0. The long-time
window around the Fermi energy. The main contribution to                 dynamics is that described in Sec. II D 1.
integrals determining the roots comes from these energies.                  It is instructive to evaluate ∞ , the asymptotic value of
The density of states is then well approximated by a constant            the magnitude of the gap, for infinitesimal quenches, when
rendering the 2D and 3D cases equivalent.                                | 0f − 0i |  0i . Expanding Eqs. (3.27) and (3.29) in small
   The second root at δω < 0, v → −x + 0, yields δω/γ ≈                  φ, we obtain, after some calculation,
−π x/2. This means that the initial state is deep in the BCS
                                                                                                               0f −
                                                                                                                                 2
                                                                                                           (              0i )
regime, while ωf → −∞ and the ground state at ωf is in the                                  ∞ =     0f −                             .   (3.30)
BEC limit. Further, μi → εF = 1, so x ≈ 1/ 0i . Subtracting                                                     6    0f

Eq. (3.18) from Eq. (3.19), we obtain                                    Note that within linear analysis ∞ = 0f . As we show
                       2
                                       π         4|μf |  4               in Sec. V, this is a general feature of linearized dynamics
               ln      0i
                             =−              +          + .    (3.24)    around the ground state regardless of coupling strength
                    4|μf |              0i         γ     γ               or initial conditions: | (t)| tends to its ground-state value
Here we assume that γ is finite and treat the single-channel             corresponding to the Hamiltonian with which the system
limit γ → ∞ separately below. Since the 1/ 0i term diverges              evolves at t > 0.
much faster than the logarithm in the above equation, we get                Region III: 0i / 0f < e−π/2 . There are two pairs of
4|μf | ≈ π γ / 0i . Equation (3.20) now obtains                          complex conjugate roots,
                             0f                   0i                            εF ± i    0i cosh φ1 ,   εF ± i     0i cosh φ2 ,         (3.31)
                                       =1−             .       (3.25)
                             max                 2π                      where φ1 is the solution of Eq. (3.27) and φ2 is the solution of
This equation shows that the II-III critical line terminates             Eq. (3.28); φ2 is real when δω/γ = ln( 0i / 0f ) ⩽ −2 and
at ( 0f , 0i ) = ( max ,0) linearly with a slope 0i /( 0f −              imaginary otherwise. We see that the roots are indeed of the
                √
  max ) = −2π/ γ .                                                       form Eq. (2.70). The asymptotic state is that of Sec. II D 2,
   Simpler expressions can also be derived for complex roots             while (t) takes the simplified form Eq. (2.71).
for quenches within the BCS regime, i.e., in the vicinity of                Just as in Eq. (3.23), the above results starting with
the of the origin in the phase diagrams. By Eq. (3.22) the real          Eq. (3.26) are universal in that they hold for quenches within
parts of the roots in this regime Re[u] ≈ μi ≈ εF . Then v is            the BCS regime independent of the dimensionality and also
purely imaginary and also |v|  x because Im[u] is related to            hold for the single-channel model.

                                                                   033628-24
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                       PHYSICAL REVIEW A 91, 033628 (2015)

   Next, consider quenches originating deep in the BEC,                and using           0i ≈     th = π γ /4, we get
                                           √
which corresponds to μi → −∞, 0i → γ , and x → −∞.                                                                     
Since v > −x in Eq. (3.17), we also have v → ∞ provided a                                                  1     γc − γ
real root exists. Equation (3.17) for δω > 0 simplifies to                                   0f = C exp  −    ln         ,                 (3.38)
                                                                                                           2ε      γε
                                            
                     v+x           4 0i
                 ln          =v          −π .            (3.32)        where C is independent of ε.
                      |x|            γ
                                                                          The I-II critical line for γ < γc is shown in Figs. 2(a), 2(b),
For 4 0i /γ < π , there is a single root at v → −x, which              and 20(a), which correspond to th / max ≈ 0.25,0.78, and
                                     √
corresponds to u ≈ 0. Since 0i ⩽ γ = max , the condition               0.18, respectively. th appears somewhat larger in these plots
  0i < π γ /4 can be fulfilled only if γ > γc , where                  since exponentially small, but finite, 0f in Eq. (3.38) is not
                                                                       noticeable; the critical line effectively goes down along the 0i
                                   16                                  axis. In the same way, the I-II critical line appears to terminate
                            γc =      .                      (3.33)
                                   π2                                  below max in Fig. 20 for γ = 50 due to exponential smallness
For γ ⩾ γc Eq. (3.17) at δω > 0 has a single root for any 0i           of 0f in Eq. (3.34).
and, in particular, for 0i → max . This means that the I-II
critical line extends all the way up to 0i = max , terminating
                                                                                                               B. 3D
at ( 0i , 0f ) = ( max ,0).
    It is interesting to work out the shape of the I-II critical           Three-dimensional diagrams for various values of reso-
line near its termination point. First, let γ > γc . Since v ≈         nance width γ are shown in Figs. 3 and 21. Overall, they are
−x, Eq. (3.16) implies δω/γ ≈ π |x|/2. Using Eqs. (3.19)               qualitatively similar to 2D diagrams. A notable difference is
and (3.20) to determine 0i and μi and Eq. (3.18) for 0f , we           that, in 3D, region III of the oscillating order parameter
                                                                                                                               √    (t) for
get                                                                    sufficiently large γ terminates at 0f < max = 2γ /3. This
                                                                     means that quenches from infinitesimally weak to sufficiently
                0f       1           α                                 strong coupling produce no oscillations. Also, in contrast to
                    = √ exp −           ,
               max       2ε         2ε                                 the 2D case, the critical line separating the gapless region I,
                                                        (3.34)        in principle, always extends all the way up to 0i = max and
                         max − 0i            γ
                  ε=               , α=         − 1.                   terminates at 0f = I-II   0f > 0. This is, however, not noticeable
                             max             γc
                                                                       at small γ because in this case the value of I-II0f is exponentially
This behavior is seen in Figs. 2(c), 20(b), and 20(c). Note the        small.                                                      √
difference between γ = 5 and γ = 50 in Figs. 20(b) and 20(c)               In 3D the dimensionless density of states f (ε) = ε and
that correspond to α ≈ 0.8 and α ≈ 4.6, respectively.                  Eq. (3.4) becomes
    Next, let γ < γc . In this case, the I-II critical line goes up,                        √
                                                                                   ∞
then bends backward, reaching a maximum, goes down, and                                dy         0i (x + y)           2δω      4 0i
terminates on the 0i axis below max ; see, e.g., the inset in                                                  =−             +      ,     (3.39)
                                                                                  −x   (v − y) y 2 + 1              γ (v ± i)    γ
Fig. 2(b). Near the termination point μi and ωi are finite since
  0i <     max , while ωf → ∞ since 0f → 0. Equation (3.16)            where y = ε/ 0i − x, and x and v are defined in Eq. (3.14).
implies v → ∞ and δω/γ ≈ π v/2. In this limit, Eq. (3.17)              Similarly, Eqs. (3.6) and (3.5) determining critical lines read
becomes
                                                                                           |δω|   π
                     2v                 4 0i                                                      =             0i (x + v)(v
                                                                                                                               2 + 1),     (3.40)
          ln √                   =v           −π .            (3.35)                           γ    2
                  1 + x2 − x              γ
                                                                                       √                                  √
                                                     √                        ∞
                                                                               dy          0i (x + y)                πv      0i (x + v)   4 0i
We see that v diverges as 0i → π γ /4 = π γ max /4 ≡                     −                               + sgn(δω)        √             =      ,
  th . Therefore, the I-II critical line terminates at ( 0i , 0f ) =         −x (v − y)         y2 + 1                      v2 + 1         γ
( th ,0). For 0i above th and below a certain upper value,                                                                                 (3.41)
which we do not determine explicitly, Eq. (3.17) has two roots.
For 0i below th there is one root.                                     The integral here is a complete elliptic integral. Substitution
    The shape of the I-II critical line as it approaches the           y = 1/t − x reduces it to one of the Carlson elliptic integrals
termination point for γ < γc obtains from Eq. (3.35). Let              with known asymptotic behaviors in various regimes [66,67].
ε = ( 0i − th )/ th  1. Equation (3.35) implies                       We, however, find it more convenient to evaluate the limiting
                                   √                                   behaviors by a direct analysis of the integral.
                        1       2( 1 + x 2 + x)                            First, we consider initial states deep in the BCS regime,
                  v≈       ln                      .          (3.36)
                       πε               πε                             i.e., ωi → +∞, which implies 0i → 0, μi → 1, and x →
                                                                       1/ 0i → +∞. To evaluate the integral in Eqs. (3.39)
The gap equation (1.26) yields in 2D                                   and (3.41) in this regime, we split the integration range into
                                                                     three intervals—(−x, −y ),(−y ,y ), and (y ,∞)—where
                                 2 γ − 20i
                 1+x +x =
                       2                     .               (3.37)    y is such that 1  y  x. Let the corresponding integrals
                                    γ 0i                               be I1 , I2 , and I3 . To the leading order in 1/y and y /x
Since ωf → ∞ corresponds to the BCS limit, we have 0f ∝                we
                                                                       √ can replace √       y 2 + 1 → |y| in I1 and I3 and replace
e−ωf /γ ∝ e−πv/2 . Combining this with the last two equations             x + y → x in I2 . The resulting integrals evaluate in terms

                                                                 033628-25
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                           PHYSICAL REVIEW A 91, 033628 (2015)

of elementary functions                                                     6
            √                                                                                  II-III
           2 x 4x                                                           5                  0f
 I1 + I3 =       ln
             v      y                                                                          max
              √                 √          √                                4
                x+v          4x( x + v + x)2
           −            ln 2       √         √ ,
                 v        y − 4x( x + v − x)2                               3
                          √       
              √          ( 1 + v 2 1 + y 2 + vy )(v + y )
                x                                                           2
      I2 = √          ln √                               ,
             1 + v 2 ( 1 + v 2 1 + y 2 − vy )(v − y )
                                                                             1

where we used 1  y  x to simplify expressions. The                        0
dependence on y should, of course, cancel from I1 + I2 + I3                  0         10               20    30          40          50
to the leading order in 1/y and y /x.
    The gap equation (1.26) in the BCS regime is handled                 FIG. 22. (Color online) Termination point of the II-III critical
similarly by splitting the integral into three, resulting in         line as a function of resonance width γ in units of Fermi energy for
                                                                     a 3D two-channel model. This line encloses region III of persistent
                 ω  2 √           8
                   − = ε − 2 + ln    .                     (3.42)    oscillations in Figs. 3 and 21. It starts at the origin and ends at
                 γ  γ              0                                   II-III
                                                                              along the 0f axis. This reflects an interesting phenomenon:
                                                                       0f
                                                                     There are no persistent oscillations for quenches to couplings stronger
Suppose the final detuning is also in the BCS regime. The
                                                                     than a certain threshold (i.e., quenches to detunings ωf such that the
above equation then implies
                                                                     corresponding ground-state gaps 0f ⩾ II-III  0f ) no matter how weak

                         δω                                          the initial coupling is (i.e., for any initial detuning). At γ → ∞
                                     0i
                            = ln          ,                (3.43)    (one-channel limit) II-III
                                                                                             0f   saturates at 1.49εF , in agreement with
                          γ          0f                              Eq. (4.19).
the same as in 2D. Because δω/γ must remain of order one
as x → +∞, it follows from Eq. (3.40) that v is also of order        Combining this with Eq. (3.42), taking the limit 0i → 0, and
one for quenches within the BCS regime. Therefore, |v|              plugging into the gap equation (1.26), we obtain
y in the above expressions for I1 + I2 and I3 . We obtain
                                                                                           ∞                                   √
|I1 + I2 |  1 and                                                          4μf                 1          1
                                                                       4+       =                 −                               εdε, (3.47)
                                       √                                     γ         0        ε    (ε − μ )2 +          2
                          1       v + 1 + v2                                                                   f          0f
    I1 + I2 + I3 ≈ I3 ≈        ln      √          . (3.44)
                        1 + v2    v − 1 + v2                         where we sent the cutoff ε to infinity. Equation (3.47),
    Equation (3.39) now turns into the 2D Eq. (3.26), and            together with the chemical potential equation (1.25), determine
Eq. (3.40) yields |δω|/γ = π/2 and therefore Eq. (3.23). Thus,       the value of II-III
                                                                                    0f , where the II-III critical line terminates on
quenches within the BCS regime in 3D are identical to those          the 0f axis. II-III
                                                                                      0f is a function of γ only; see Fig. 22.
in 2D and all results from Eq. (3.26) to Eq. (3.31) also hold in        We also note that it follows from the above analysis that,
3D. As we already commented above, this is expected since            just as in 2D, for initial states deep in the BCS regime, there
in the BCS regime superconductivity comes from the vicinity          are three roots: v → 0 for either sign of δω and v → −x + 0
of the Fermi energy, making the dependence of the density of         for δω < 0. Therefore, Eq. (3.22) holds in 3D as well.
states on the energy and thus the dimensionality inessential.           Second, consider quenches from deep BEC to larger
    The horizontal 0i = const line for infinitesimal values of       detuning ωf > ωi , i.e., ωi → −∞,δω > 0,μi → −∞,x →
the const intersects the II-III critical line twice, once near the   −∞, 0i → max . Since y ⩾ |x|  1 in Eq. (3.41), we can
origin and the second time near the termination point of the         replace√ y 2 + 1 → y. The principal value integral evaluates
II-III critical line. The former intersection corresponds to small   to −π |x|/v and Eq. (3.41) becomes
v, as we saw above, and the latter to v of order x. To determine                        √                        √
the termination point, we therefore take |v|  y in the above                         π |x|                     4     0i
                                                                                   −          + π v − |x| =              ,     (3.48)
expressions for I1 + I3 and I2 . Equation (3.39) becomes                                 v                         γ
            √              √          √
              x+v         ( x + v + x)2                              where we also took into account that we need v ⩾ |x| so that
              √       ln √             √                             Eq. (3.40) yields real δω. The solution for large |x| is
                  x      −( x + v − x)2
                                                                                                    √
                    δω      8     2v 0i   2iδω                                                    4     0i     1
            = −2       + ln     −       ±      . (3.45)                                 v − |x| ≈          +√ .               (3.49)
                     γ       0i     γ      vγ                                                       πγ          |x|

The real root of this equation is v ≈ −x ≈ −1/       0i , yielding   Equation (3.40) now yields

                     δω        8    2                                               δω   2|μi | π                      32 2max
                        = − ln     − .                     (3.46)                      ≈       +             |μi | +           ,           (3.50)
                      γ         0i  γ                                                γ     γ     2                      π 2γ 3

                                                               033628-26
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                        PHYSICAL REVIEW A 91, 033628 (2015)


          1                                                                     We see from Fig. 23 that I-II  0f becomes noticeable for γ 
                       Δ0f : Eq. (3.52)
                         I-II                                                   0.45. For smaller γ the gapless region I appears to close at
        0.8            Δmax                                                     smaller 0i and zero 0f . Figure 23 also shows that Eq. (3.52)
                       ΔI-II
                        0f
                                                                                provides a reasonable estimate of I-II
                                                                                                                     0f even for large γ , which
                       ΔI-II
                        0f
                            : Eq. (3.51)                                        is useful in our analysis of the one-channel model below.
        0.6

                                                                                                IV. ONE-CHANNEL MODEL
        0.4
                                                                                    In this section we collect for reference purposes analogous
        0.2                                                                     results for the asymptotic steady state after a quench λi → λf
                                                                                in the one-channel model given by Eqs. (1.3) and (1.5).
                                                                                    As explained in Sec. I A, the one-channel model obtains in
          0
           0         0.2        0.4        0.6        0.8          1            the broad resonance limit via replacements,
                                      γ
                                                                                            ω   ω    1
                                                                                              = 2   → , γ = g 2 νF → ∞                               (4.1)
    FIG. 23. (Color online) Unlike 2D, in 3D 0f tends to a finite                           γ  g νF  λ
         0f along the I-II critical line as the initial detuning ωi → −∞
value I-II
( 0i → max ) for quenched two-channel model; see, e.g., Fig. 21.                (in units of εF ). Our task is to go over equations of
The gapless regime thus persists even for quenches from arbitrarily             previous sections performing these replacements. All essential
large negative ωi to finite ωf . Here we compare I-II                           reasoning and methods are the same.
                                                          0f (in units of the
Fermi energy) as a function of the resonance width γ extrapolated                  Chemical potential and gap Eqs. (1.25) and (1.26) now read
from actual phase diagrams with that obtained from Eqs. (3.51)                                   ⎡                      ⎤
                                                                                               ∞
and (3.52). Note that I-II 0f is exponentially small at small γ , so that             4          ⎣1 −      ε − μ       ⎦ f (ε)dε,
the I-II critical line appears to close earlier at zero 0f in Fig. 21(a).                =                                               (4.2)
                                                                                      d      0           (ε − μ)2 + 2            0


where we replaced 20i → 2max = 2γ /3 up to terms of order                       and
|μi |−1/2 . The overall correction to this expression is also                                    2            ε
                                                                                                                           f (ε)dε
proportional to |μi |−1/2 at large |μi |.                                                          =                                        ,       (4.3)
                                                                                                 λ        0           (ε − μ)2 +         2
   Similar simplifications occur in the gap equation (1.26). We                                                                          0
replace the square root with ε − μi to obtain
                                                                                respectively.
                 ωi  √    2|μi | π                                                 The Lax vector becomes
                    ≈ ε −       −                  |μi |.                                              
                 γ          γ     2                                                                                     sp      ẑ
                                                                                                L(u) =                       −     .                 (4.4)
The last two equations determine ωf and from the gap                                                              p
                                                                                                                      u − εp   λνF
equation (1.26) for ω = ωf we obtain
                                                                                Gaudin algebra, i.e., Eqs. (2.2) and (2.3), as well as the Lax
                         ⎡                     ⎤
                       ∞          √                                             equation of motion (2.8) are the same. The numerator of the
  128       4μf          ⎣        ε        1                                   conserved L2 (u) is now a polynomial of degree 2N ,
          −      =                        − √ ⎦ dε,
 3π 2 γ 2    γ       0      (ε − μ )2 + 2    ε
                                            f         0f                                                            Q2N (u)
                                                                                                L2 (u) =                           ,                (4.5)
                                                                                                                      p (u − εp )
                                                                                                                      )2
                                                                                                               (λνF               2
                                                                       (3.51)

where we eliminated the cutoff similar to Eq. (3.47). This                      where N is the number of nondegenerate εp .
equation combined with Eq. (1.25) determines the termination                       Reduced solutions are constructed in the same way with
point ( 0i , 0f ) = ( max , I-II                                                minor modifications. Specifically, the expressions for Lred (u)
                               0f ) of the I-II critical line. The
plot of I-II as a function  of γ is shown in Fig. 23.                           in terms of σp and Lm (u) in terms of tj are replaced in
          0f
   Note that, in contrast to the 2D case, this critical line                    Eqs. (2.10) and (2.11) with the corresponding one-channel Lax
formally always extends up to 0i = max and I-II                                 vectors according to Eq. (4.4). The Hamiltonian governing the
                                                      0f does not
vanish as 0i → max . This means that the gapless regime                         collective spin variables tj is
persists even for quenches to finite final detunings from initial                                       
                                                                                                        m−1                      
                                                                                                                                 m−1
states lying arbitrarily deep in the BEC regime. But for small                                red
                                                                                             H1ch =            2ηj tjz − λνF             tj− tk+ .   (4.6)
γ the value of I-II 0f is exponentially small and the critical                                          j =0                     j,k=0
line appears to have closed at smaller 0i ; see Figs. 3(a)
and 21(a). Small γ implies a large left-hand side in Eq. (3.51)                 Equations (2.13) and (2.14) as well as constraints (2.15) are
and therefore the final state deep in the BCS regime. In this                   the same, except that the last equation relating ω and ω is
regime μf → 1 and the integral in √      Eq. (3.51) is twice the                absent. In terms of the m-spin spectral polynomial Q2m (u) the
right-hand side of Eq. (3.42) without ε resulting in                            constraints become
                                                                                           σp εpr−1                δrm
                                     64  2
                                  − 2 2 + −2 .                                                          =−                , r = 1, . . . ,m.         (4.7)
                  0f = 8 exp
                  I-II
                                                                       (3.52)               Q2m (εp )             (λνF )2
                                   3π γ  γ                                             p


                                                                          033628-27
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                             PHYSICAL REVIEW A 91, 033628 (2015)

Further, since the degree of the m-spin spectral polynomial is      δβ. The two roots u ≈ μi for either sign of δβ correspond
2m rather than 2(m + 1), an m-spin solution of the two-channel      to quenches also terminating in deep BCS, so they are in the
model becomes an (m + 1)-spin solution of the one-channel           universal regime given by Eqs. (3.26) through (3.31), which is
model. This name change reflects the fact that the oscillator       shared by both models regardless of the dimensionality.
mode b in the two-channel model is effectively an additional           The analysis for the root u ≈ +0 at δβ < 0 leading to
spin, which was not counted as such.                                Eq. (3.25) requires some modifications. The γ → ∞ limit
   All remaining equations in Sec. II, i.e., Eqs. (2.18)            in Eqs. (3.24) and (3.20) yields 4|μf | = 20i eπ/ 0i , 0f =
through (2.74), are identical for the one-channel model, except       4|μf |, and finally
Eq. (2.21) is replaced with Eq. (4.6) for m = 2 and the
                                                                                                0f =                               0i → 0.
                                                                                                                π/2
self-consistency condition (2.50) is now given by Eq. (1.13).                                            0i e
                                                                                                                          0i
                                                                                                                               ,                       (4.13)
   Equations determining isolated roots, critical lines, and        This equation gives the asymptotic form of the II-III critical
μ∞ = 0 line for the one-channel model are Eq. (3.4), Eqs. (3.6)     line in the ( 0i , 0f ) plane in Fig. 4. We see that this line never
and (3.5), and Eq. (3.7), respectively, with replacements           terminates in the 2D one-channel model.
               δω    1   1               1                             Finally, let us work out the shape of the I-II critical line
                  →    −    ≡ β,           → 0.            (4.8)    for large 0i , i.e., for quenches originating deep in the BEC
                γ   λf   λi              γ
                                                                    regime. Equation (3.32) becomes
Asymptotic spin distribution—the constant angle the spin
s(ε) makes with the spin σ (ε) in the corresponding m-spin                                              v+x
                                                                                                  ln                       = −π v.                     (4.14)
solution—is                                                                                              |x|
                     
              z(ε)                                                  Now there is always a single root v → −x (u ≈ 0). Equa-
 cos θ (ε) =           A2− 20i + [(ε − μi )A− + δβ]2
             iπf (ε)                                                tion (4.11) implies
                       
                z(ε)                                                                               1   1    π |x|   π |μi |
             −           A2+ 20i + [(ε − μi )A+ + δβ]2 , (4.9)                           δβ =        −    =       =         .                          (4.15)
               iπf (ε)                                                                            λf   λi     2     2 0i
where                                                               We also need the gap equation in BCS and BEC limits and
                          ∞
               iπf (ε)        f (ε )dε                            the chemical potential equation in the BEC limit. Sending γ
        A± = ±         +−               
                                            .             (4.10)    to infinity in Eqs. (3.18)–(3.20), we obtain
               2Ei (ε)   0 2(ε − ε )Ei (ε )
Equation (4.9) is in excellent agreement with the actual                       4ε        2              ε       2
                                                                          ln         =      ,     ln         =    ,                0i =      4|μi |.   (4.16)
spin distribution obtained from direct simulation of spin                       2
                                                                                0i       λi            |μf |   λf
dynamics [18]; see Fig. 3 therein.
                                                                    Combining these equations with Eq. (4.15), we get
                                                                                                              −π
                                                                                           0f =                                    0i → ∞.
                                                                                                                   0i /8
                  A. Quench phase diagram                                                              0i e                    ,                       (4.17)
    Quench phase diagrams for one-channel model in 2D and           We see that 0f exponentially vanishes along the I-II critical
3D are shown in Figs. 4 and 5. There is only one diagram in         line (gapless regime closes) as 0i increases. The vertical
each case extending to positive infinity in both 0i and 0f          range of Fig. 4 is not enough to fully display this behavior,
directions because γ → ∞ and therefore max → ∞.                     though we see that I-II line does incline towards the 0i axis
    As we commented below Eqs. (3.23) and (3.31), the weak-         at large 0i .
coupling part of the diagrams (the region of small 0i and
   0f near the origin) is independent of the dimensionality and                                                 2. 3D
is exactly the same for the one-channel model. In other words,
                                                                        In addition to quenches that fall within the universal weak-
all results contained in Eqs. (3.26) through (3.31) and the
                                                                    coupling regime described in Eqs. (3.26) to (3.31) and the
surrounding text apply to the one-channel model in both 2D
                                                                    corresponding text, let us derive the termination point of the
and 3D; one only needs to replace δω/γ → δβ.
                                                                    II-III critical line and analyze the I-II line at large 0i .
    When either the initial or final coupling is outside the deep
                                                                        First, we consider the II-III line. The termination point is
BCS regime, we need to treat 2D and 3D cases separately.
                                                                    given by Eq. (3.47). In the γ → ∞ limit we have
                                                                                      ⎡                           ⎤
                             1. 2D                                                 ∞
                                                                                        1             1              √
    It is straightforward to take the broad resonance limit               4=          ⎣ −                        ⎦ εdε.         (4.18)
                                                                                 0      ε      (ε − μ )2 + 2
in Eqs. (3.15) to (3.21). In particular, the critical lines are                                                       f            0f
determined by taking this limit in Eqs. (3.16) and (3.17),
                                                                    Chemical potential equation (4.2) provides another relation
                              π                                     between μf and 0f . Numerical solution of these two
                      |δβ| =      1 + v2,                 (4.11)
                              2                                     equations is
                      √
          (v + x)(v + 1 + v 2 )                                                μII-III
                                                                                f      ≈ −1.4602εF ,                      0f ≈ 1.4875εF .
                                                                                                                          II-III
                                                                                                                                                       (4.19)
  ln √          √                   = −sgn(δβ)π v.        (4.12)
         1 + x 2 1 + v 2 − xv + 1                                   This value of II-III  agrees with Fig. 22. Unlike 2D, in 3D
                                                                                     0f
Equation (3.22), describing quenches originating in deep BCS,       region III encloses a finite area, resembling a dome between
remains as is, except the sign of δω translates into the sign of    the origin and the point ( 0i , 0f ) = (0, II-III
                                                                                                                0f ).


                                                              033628-28
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                PHYSICAL REVIEW A 91, 033628 (2015)

    Next we turn to the critical line separating the gapless region    that transformation to the rotating frame results in shifts to εp
I from region II. For finite γ we analyzed the termination point       and ωf . Then the spin rotates around Bp , making a constant
( 0i , 0f ) = ( max , I-II
                         0f ) of this line at the end of Sec. III B.   angle π − θp with it. This is, in fact, the asymptotic solution
In the single-channel case, max → ∞, so the I-II line does             described in Sec. II D 1,
not close. As 0i → ∞, the value of 0f for a point on this
                                                                                                     np
                0f , which is determined by the γ → ∞ limit
line tends to I-II                                                                        sp (t) =      cos θp + sp⊥ (t),            (5.2)
of Eq. (3.51),                                                                                       2
                ⎡                              ⎤                       where np is a unit vector along −Bp ,
              ∞                                  √
                ⎣           1               1
      0=                                  − ⎦ εdε,           (4.20)                       ∞                            εp − μ∞
            0        (ε − μ )2 +       2     ε                                   nxp =         , nyp = 0,    nzp = −           .     (5.3)
                            f         0f                                                 Ep∞                              Ep∞
together with Eq. (4.2). The solution of these equations is            Equation (1.8) with ḃ = 0 further implies ∞ = −gb =
             μf ≈ 0.5906εF ,                                           g 2 J− /(ωf − 2μ∞ ). The contribution of sp⊥ to J− dephases
                                     0f ≈ 0.6864εF .
                                     I-II
                                                             (4.21)                                          x
                                                                       as t → ∞. The latter is therefore       p np /2, the sum of

     V. TRANSIENT DYNAMICS: LINEAR ANALYSIS                            components of sp along Bp projected onto the xy plane,

    Here we solve the dynamics for small deviations from the                           g2           ∞ cos θp
                                                                              ∞ =                                                .   (5.4)
ground state. Linear analysis for the one-channel model in                          ωf − 2μ∞ p 2 (εp − μ∞ )2 +               2
                                                                                                                             ∞
the weak-coupling BCS regime was performed by Volkov and
Kogan [3]; see also Ref. [18]. Gurarie [23] extended this study        In the ground state sp is aligned with −Bp ; i.e., θp = 0. This
to strongly coupled superconductors. Both these studies of the         implies that θp must be proportional to δω and therefore
linearized dynamics conclude that                                      corrections to cos θp = 1 are second order in δω. However, for
                                     −2iμ∞ t−2iϕ                       cos θp = 1, Eq. (5.4) is the ground-state gap equation (1.18)
                      (t) →     ∞e                            (5.1)
                                                                       for ω = ωf . Moreover, applying the same argument to Jz
as t → ∞, but the approach to this asymptote is different.             and Eq. (1.19), we find that ∞ and μ∞ also satisfy the
Our analysis adds several new results to this prior work.              ground-state chemical potential equation (1.20). It follows that
We demonstrate that within linear analysis the amplitude               for small oscillations around the ground state one always has
of the order parameter asymptotes to its ground-state value
                                                                                               ∞ =    0f ,   μ∞ = μf .               (5.5)
for the Hamiltonian with which the system evolves after
nonequilibrium conditions are created, i.e., ∞ = 0f , a point          For the same reason the nonoscillatory part of sp (zeroth
that seems to have been missed by the earlier work. Also,              harmonic) in the steady state is the same as in the ground
μ∞ = μf , the ground-state chemical potential. In other words,         state at ω = ωf , i.e., is given by Eq. (1.15) with 0 → 0f
  ∞ − 0 and μ∞ − μf are second order in the deviation. This            and μ → μf .
is a general result that holds for both one- and two-channel              The same is true for the one-channel model. Note also
models and is independent of the type of perturbation that             that infinitesimal quenches in the BCS regime conform to this
drives the system out of equilibrium.                                  conclusion; see Eq. (3.30). Moreover, this result generalizes
   Further, we solve linearized equations of motion using the          to finite spin dynamics, where, as we show below, zeroth
machinery of the exact solution [13,15], which provides much           harmonics of (t) and sp to linear order in δω coincide with
more detailed information. For example, we also determine              the ω = ωf ground-state values.
the short-time behavior, normal modes, full explicit long-time
form (t), and individual spins with all prefactors and phases,                   B. Normal modes and finite-size dynamics
etc., unavailable to conventional linear analysis. Note that
in quench phase diagrams constructed above small quenches                  Now we turn to the linear analysis per se. At this point
correspond to the vicinity of the diagonal 0i = 0f ; see, e.g.,        it is convenient to rewrite summations over p as summations
Figs. 20 and 21.                                                       over single-particle energies. We adopt the following model
                                                                       of discrete spectrum. Let us discretize the magnitude of
                                                                       the momentum, p → pk . The corresponding energies are
                  A. Asymptotic (t) and spins
                                                                       εk = pk2 /2m with degeneracy Nk = N (εk ), the number of
    Consider an infinitesimal quench of the detuning δω =              states in a momentum shell between pk and pk+1 , which is
ωf − ωi . More generally, δω can be any small parameter                a smooth function of εk . The level spacing δk = εk+1 − εk
that measures the deviation from the ground state in the               is also assumed to depend on εk smoothly. We include this
two- or one-channel model. We work to linear order in                  dependence in Nk , so without loss of generality we take
δω. Suppose (t) → ∞ e−2iμ∞ t−2iϕ . For the detuning or                 it to be constant, δk = δ. Our final results depend only on
interaction quenches, this follows from the few-spin conjecture        the density of states ν(εk ) = Nk /δ, the number of states per
and quench phase diagrams derived above and we also verify             unit energy. Equivalently, εi can represent levels of some
it independently below. Let us go to a reference frame that            other single-particle potential, e.g., a 3D harmonic oscillator
rotates with frequency 2μ∞ around the z axis. In this frame            potential; see the discussion at the end of Sec. I A. All
   (t) = ∞ and the magnetic field Bp = (−2 ∞ ,0,2εp −                  quantities and equations, including spins sp , Hamiltonians,
2μ∞ ) acting on spin sp in Eq. (1.8) is time-independent. Note         equations of motion, and initial conditions, considered in this

                                                                 033628-29
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                           PHYSICAL REVIEW A 91, 033628 (2015)

paper depend on p only through εp . For any such quantity               A plot of L0 (x) reveals that xk are located between consecutive
Ap = A(εp ),                                                            εk , i.e., εk < xk < εk+1 .
                                                                            Since L2 (xk ) = L2x (xk ) + L2y (xk ) + L2z (xk ) = 0 in the
                         
                          N
                   Ap =         Nk Ak →     ν(ε)dε,          (5.6)      ground state and xk is real, all components of L(xk ) must van-
               p          k=1                                           ish, Lx (xk ) = Ly (xk ) = Lz (xk ) = 0. It follows that L− (xk ) =
                                                                        0, meaning that the separation variables are frozen in the real
where Ak = A(εk ). In particular, the Lax vector (2.1) reads            double roots, uk = xk . After a quench they start to move from
           
           N                                                            these initial positions, uk (t) = xk + δuk , where δuk vanishes
             Nk sk           (ω − 2μ)      2
  L(u) =                 −            ẑ + 2 [(u − μ)ẑ −    ].         at t = 0 and is proportional to δω for an infinitesimal quench.
           k=1
               u − εk           g2        g                             For δω = 0 real double roots of Q2N+2 (u) split into pairs
                                                             (5.7)      of complex conjugate roots ck = xk + δck and c̄k = xk + δ c̄k .
                                                                        Therefore, the expression for Q2N+2 (uk ),
   A convenient tool for linear analysis of the dynamics are
the separation variables introduced in Refs. [13,15] for the                  Q2N+2 (uk ) = (uk − ck )(uk − c̄k )(uk − c+ )(uk − c− )
                                                                                              
one- and two-channel models, respectively. As we will see,                                  ×    (uk − cm )(uk − c̄m ),            (5.15)
in linearized dynamics these variables are simply the normal                                     m=k
modes. Separation variables uj are defined as the solutions of
L− (uj ) ≡ Lx (uj ) − iLy (uj ) = 0; i.e.,                              to lowest nonzero order in δω becomes

                        2b  Nk sk−
                             N                                                      Q2N+2 (uk ) = (δuk − δck )(δuk − δ c̄k )2k
               L− (u) =   +            = 0.                  (5.8)                                  
                        g   k=1
                                u − εk                                                            ×     (xk − xm )2 ,               (5.16)
                                                                                                           m=k
Because u = uj are the zeros of the rational function L− (u)                       √
and u = εk are its poles, we can also write it as                       with k = (xk − μ)2 + 20 , not to be confused with function
                                                                       (t) in Sec. II B 3. Similarly, the denominator
                            2b j (u − uj )                                                                           of the equation
                  L− (u) =                   .        (5.9)            of motion (5.12) for uk to the lowest order m=k (uk − um ) =
                                                                        
                             g    k (u − εk )
                                                                          m=k (xk − xm ), so this equation reads
Matching the residues at u = εk and u = ∞ in Eqs. (5.8)
and (5.9), we express the spins in terms of uj ,                                 δ u̇k = ±2ik (δuk − δck )(δuk − δ c̄k ).          (5.17)
                              
                                 j (εk − uj )
                          2b                                               Corrections to the roots due to the quench obtain by setting
                    −
                Nk sk =                      ,  (5.10)                 u = xk + δck in Eq. (5.13) and linearizing in δck . Separating
                          g m=k (εk − εm )
                                                                        real and imaginary parts, δck = ak + ibk , we have
                                   2b 
             J− =        Nk sk− =        (εk − uk ).        (5.11)                           δω(xk − μ)         δω 0
                                    g k                                               ak =               , bk = 2 2 ,               (5.18)
                     k                                                                        g 2 2k Fk       g k Fk
Equations of motion in terms of new variables are                       where
                        √                                                                            
                      2i Q2N+2 (uk )                                                                             Nk
             u̇k = −                  ,                                                  Fk =                                .     (5.19)
                        m=k (uk − um )                                                               m
                                                                                                          2(xk − εm )2 E(εm )
                                                          (5.12)
                           ω                                              Let us also evaluate the correction to the complex root pair
               ḃ = −2ib      +    (εk − uk ) ;
                           2                                            c± = μi ± i 0i . Writing the perturbed roots as μ ± i  , we
                                 k
                                                                        obtain from Eq. (5.13) to linear order in δω
see Ref. [15] for a detailed derivation. Here Q2N+2 (u) is the
                                                                                                             δω βk
spectral polynomial defined in Eq. (2.9).                                                    μ − μi =                     ,
    Roots of Q2N+2 (u) are the same as roots of L2 (u)                                                       g 2 αk2 + βk2
                                                                                                                                    (5.20)
determined by Eq. (3.3). In our new notation,                                                                     δω αk
                                                                                             
                                                                                               −       0i = −                 ,
                2                 Nk              δω                                                           g 2 αk2 + βk2
   u−μ∓i 0             −                           = 2 , (5.13)
                    g2      k
                               2(u − ε k )E(εk )     g                  where αk and βk are defined in Eq. (C5). Comparing this
                √                                                       with first-order shifts in the ground-state gap and chemical
where E(εk ) = (εk − μ)2 + 20 . Here and everywhere be-                 potentials that readily derive from Eqs. (C7), we conclude that
low in this section μ and 0 without a subscript indicate
ground-state values μi and 0i for the initial detuning ω = ωi .                              μ = μf ,             
                                                                                                                       =   0f ,     (5.21)
In the ground state L2 (u) = [(u − μi )2 + 20i ]L20 (u). There is       as it should be according to Sec. II D 1; see the text following
a pair of complex roots c± = μi ± i 0i and 2N real double               Eq. (2.65) and also below.
degenerate roots xk that solve                                             Equation (5.17) is a harmonic oscillator equation, which
                   2               Nk                                  yields
       L0 (x) = − 2 +                           = 0,      (5.14)
                  g       k
                              2(x − εk )E(εk )                                  δuk (t) = ak (1 − cos 2k t) + ilk sin 2k t,       (5.22)

                                                                  033628-30
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                     PHYSICAL REVIEW A 91, 033628 (2015)

           1                                                              ω = ωf , yields
                                             Im[cm]/0.1 0f                      (t)           1 − cos 2k t              
                                                                                      = 1−     lk            − iδωt + 2it   ak
        0.5                                  Im[c _ ]/ 0f
                                                  +                              0           k
                                                                                                    k                    k
                                                                                             ak sin 2k t
                                                                                       −i                             ,            (5.26)
          0                                                                                  k
                                                                                                        k

                                                                          where we took into account (t) = −gb(t), (0) = 0 and
        -0.5                                                              expressions (5.22). The iδωt appears because for unperturbed
                                                                          uk the bracketed term in the second equation in Eq. (5.12)
                                                                          vanishes for ω = ωi , while after the quench ω = ωf .
          -1
                     1                   2                   3
                                                                             Linearizing spin equations of motion (1.8) directly and
                              Re[c] / F                                   plugging expressions (5.25) and (5.26), one can verify that the
                                                                          correct sign in the last equation in Eq. (5.23) is indeed plus,
   FIG. 24. (Color online) As a result of a quench, doubly degen-         even though there is probably a simpler way to show this.
erate roots of L2 (u) in Fig. 17 split into pairs of complex conjugate       The imaginary part in Eq. (5.26) comes from the phase of
roots cm (not all N = 54 pairs of roots are shown). In linear analysis,   the order parameter, so we write
separation variables move periodically on ellipses around the brunch                                               
                                                                                                 1 − cos 2k t
cuts of [L2 (u)]−1/2 connecting complex conjugate cm without crossing         (t) =     0− 0        lk
any of the brunch cuts. Each separation variable has its own distinct                            k
                                                                                                           k
frequency and corresponds to a normal mode of small oscillations                                                                   
around the ground state. Here 0f = 0.12εF , δω/γ = −0.1, and                                                         ak sin 2k t
other parameters are the same as in Fig. 17.
                                                                                    × exp −iδωt + 2it         ak − i                   .
                                                                                                           k          k
                                                                                                                              k
                                                                                                                                   (5.27)
where
                                                                         This coincides with Eq. (5.26) to first order in δω. Moreover,
                                             δω
                  lk = ± ak2 + bk2 =                  .          (5.23)   we know from Eq. (5.5) that the linear part of the phase
                                          g 2 k Fk
                                                                          (zeroth harmonic in the derivative of the phase) is −2μf t
In deriving Eq. (5.22) we took into account the initial condition         in the continuum limit, where μf is the ground-state chemical
δuk (0) = 0 and used expressions (5.18). We set the sign in the           potential at detuning ωf . Similarly, the zeroth harmonic in the
last equation in Eq. (5.23) to be plus, which we justify later in         amplitude of (t) is equal to 0f . It turns out that this is true
this section.                                                             even in the discrete case, i.e.,
    Equation (5.22) shows that uk (t) are the normal modes of                                              lk
small oscillations around √the ground state and that the normal                                 0− 0              = 0f ,
                                                                                                             k
frequencies are 2k = 2 (xk − μ)2 + 20 , where xk are the                                                  k
                                                                                                                                  (5.28)
roots of Eq. (5.14). Equation (5.22) also shows that in linear                             2μ + δω − 2        ak = 2μf ,
                  √ variable uk (t) moves on an ellipse with
analysis separation                                                                                               k
semiaxes ak and ak2 + bk2 around the roots ck ,c̄k√  . The latter
are the focal points of the ellipse. The function Q2N+2 (u)               where we restored the phase of (t) to the original reference
entering equations of motion for separation variables has                 frame according to Eq. (5.24). Recall that in this section μ and
branch cuts connecting pairs of conjugate roots ck and c̄k ,                0 without a subscript indicate ground-state values μi and 0i
so one can also say that separation variables move on ellipses            for the initial detuning ω = ωi . With the help of Eqs. (5.18)
around brunch cuts without crossing any of them; see Fig. 24.             and (5.23) these relations become
    Next, we determine deviations of the spins δ sk (t) and the                               xk − μ                 g2     δμ
order parameter δ (t) from their initial ground-state configu-                                                =          − g2 ,
                                                                                                     2k Fk           2      δω
ration (1.14) and (1.15). We go to a rotating reference frame,                               k
                                                                                                                                   (5.29)
                                                                                                                         δ 0
                sk− → sk− e−2iμt , b → be−2iμt ,
                                                                                                         0
                                                                 (5.24)                                       = −g 2          ,
                                                                                                 k
                                                                                                     2k Fk                δω
to get rid of the time dependence in the unperturbed dynam-
ical variables. This shifts ω → ω − 2μ in the equation of                 where δμ = μf − μ and δ 0 = 0f − 0 . These are in fact
motion (5.12) and now ḃ = 0 in the ground state before the               identities, as we prove in Appendix C. Thus,
quench, i.e., for ω = ωi . Linearizing Eq. (5.10), we obtain a                                                     
                                                                                                       cos 2k t
decomposition of spin deviations in terms of the normal modes,                      (t) =     0f + 0      lk
                                                                                                              k
                 δsk− (t)   δ (t)  δuj                                                          
                                                                                                       k
                                                                                                                             
                  −       =      −           .                   (5.25)                                        ak sin 2k t
                 sk (0)       0      εk − xj
                                   j                                                      × exp −2iμf t − i                    , (5.30)
                                                                                                               k
                                                                                                                     k
Similarly, the second equation in Eq. (5.12) linearized and
integrated in the rotating frame after the quench, i.e., with             in the original reference frame.

                                                                    033628-31
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                         PHYSICAL REVIEW A 91, 033628 (2015)


   An expression for sk− (t) obtains similarly from Eqs. (5.25)                        1.02
and (5.26) with the help of identity (C8),                                                                                          numerics
                  ⎛                                                                                                                 analytics, Eq. (5.35)
                        lj cos 2j t
               − ⎝
    sk− (t) = skf   1+

                                                                                    | (t)|/ 0f
                         j
                                j                                                               1

                                                     ⎞
                   aj cos 2j t       lj sin 2j t
              +                   −i                 ⎠
                  j
                       εk − xj         j
                                            εk − xj
                                                                                       0.98
                     ⎡                             ⎤
                                    aj sin 2j t
              × exp ⎣−2iμf t − i                   ⎦ , (5.31)
                                                                                                 0            20              40            60              80
                                             j
                                    j                                                                                        t 0f
where
                                                                                FIG. 25. (Color online) Comparison of Eq. (5.35) with | (t)|
          −                                                                 computed by numerically evolving N = 5024 spins in a 3D two-
             ≡ sf− (εk ) =
                                            0f
         skf                                              .       (5.32)
                                                                            channel model after a detuning quench. Here γ = 1.0, 0i =
                                2 (εk − μf )2 +       2
                                                      0f                    0.122 max , 0f = 0.126 max , and both Eq. (5.35) and the spin chain
                                                                            in the numerics are cut off at ε = 10εF .
The last term in round brackets in Eq. (5.31) can be as well
included into the phase; to linear order the two versions are
equivalent. The present form is more convenient for the long-               tion (5.35) is in excellent agreement with numerical results;
time analysis below. We see that again nonoscillatory parts of              see, e.g., Fig. 25.
the magnitude and phase of sk− (t) and magnitude of skz are the                Expressions (5.33) and (5.31) for sk− (t) and skz (t) contain
same as in the ground state for final detuning ω = ωf .                     two extra summations as compared to (t). These are handled
    Finally, the expression
                       √      for skz (t) follows the conservation of       as in Appendix C by splitting each sum into two parts, over
|sk | = 1/2, sk = ± 1/4 − |sk− |2 expanded to the linear order
                 z                                                          xj inside and outside a small interval around εk . The same
in δω,                                                                      method works for summations over xj because according to
                        ⎡                                                   Eq. (B8) (ε) is a smooth function and therefore xj are locally
                                     2        lj cos 2j t                 equally spaced with spacing δ just as εk . The second and the
                    z ⎣              0f
         skz (t) = skf    1−                                                third sums in round brackets in Eq. (5.31) are
                              (εk − μf ) j 2         j
                                                       ⎤                                               δω ∞ 2(ε − μ) cos[2E(ε )t]f (ε )dε
                                                                                   Y1 (ε,t) =              −
                            2
                            0f
                                         aj cos 2j t ⎦                                                γ 0 (ε − ε )E(ε )[π 2 f 2 (ε ) + H 2 (ε )]
                   −                                     ,     (5.33)
                       (εk − μf )2 j         εk − xj                                                     δω 2(ε − μ)H (ε) cos[2E(ε)t]
                                                                                                       −                                   ,         (5.38)
                                                                                                          γ E(ε)[π 2 f 2 (ε) + H 2 (ε)]
where
                                                                                                          δω ∞ 2 sin[2E(ε )t]f (ε )dε
                                         εk − μf                                         Y2 (ε,t) =           −
          z
         skf ≡ sfz (εk ) = −                                  .   (5.34)                                  γ 0 (ε − ε )[π 2 f 2 (ε ) + H 2 (ε )]
                                 2 (εk − μf )2 +       2
                                                       0f                                                   δω 2H (ε) sin[2E(ε)t]
                                                                                                          −                          ,              (5.39)
                                                                                                             γ π 2 f 2 (ε) + H 2 (ε)
                        C. Continuum limit
                                                                            respectively. Thus,
   In N → ∞ limit, xk → εk and summations in the above
expressions for skz (t), sk− (t), and (t) turn into integrations.                                s − (ε,t)
                                                                                                           = [1 + X1 (t) + Y1 (ε,t) − iY2 (ε,t)]
With the help of Eqs. (5.18), (5.23), (5.6), and (B9), Eq. (5.30)                                 sf− (ε)
obtains (as always in units of the Fermi energy εF )
                                                                                                              × exp[−2iμf t − iX2 (t)],                      (5.40)
         (t)
               = [1 + X1 (t)] exp[−2iμf t − iX2 (t)],              (5.35)
                                                                                                                   2
         0f                                                                           s z (ε,t)          0f
                                                                                                =1−            [X1 (t) + Y1 (ε,t)].                          (5.41)
where                                                                                  sfz (ε)      (ε − μf )2
                            ∞
                   δω            2 cos[2E(ε)t]f (ε)dε                             Functions X1 and X2 are related via differentiation. Define
        X1 (t) =                                            ,      (5.36)
                    γ   0       E(ε)[π 2 f 2 (ε) + H 2 (ε)]                                                             ∞
                                                                                                                                    !
                                                                                                        !1 (t) =
                                                                                                        X                   K(ε)e2i E(ε)t dε,                (5.42)
              δω ∞ 2(ε − μ) sin[2E(ε)t]f (ε)dε
    X2 (t) =                                            , (5.37)                                                    0
               γ 0       E 2 (ε)[π 2 f 2 (ε) + H 2 (ε)]                                                √
                √                                                           where !
                                                                                  E(ε) =                (ε − μ
                                                                                                             !)2 +          2
                                                                                                                            0 and
where E(ε) = (ε − μ)2 + 20 and H (ε) is defined in
Eq. (B8). In deriving this expression, we also used, k →                                                     δω           2f (ε)
                                                                                                     K(ε) =                                  .               (5.43)
E(εk ), ν(ε) = νF f (ε), g 2 νF = γ , and δ = Nk /ν(εk ). Equa-                                                γ E(ε)[π 2 f 2 (ε) + H 2 (ε)]

                                                                      033628-32
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                             PHYSICAL REVIEW A 91, 033628 (2015)

Then                                                                                    The phase of the order parameter defined through
                                !1 (t)|μ!=μ ,
                     X1 (t) = ReX                                        (5.44)                               (t) = | (t)|e−i(t)                    (5.49)

                                      "                                           is simply (t) = 2εF t. Let us also note that in terms of ξ =
                          1    !1 (t) "
                              ∂X                                                    0 sinh(π x/2) Eq. (5.47) reads
                  X2 (t) = Re         " .                                (5.45)
                          2t    μ "μ!=μ
                               ∂!                                                                                     ∞
                                                                                                                          dx cos[2τ cosh(π x/2)]
                                                                                    | (t)| =       0f − 2δ    0                                  , (5.50)
                                                                                                                  0       π        1 + x2
A similar relationship holds for Y1 and Y2 .
                                                                                  where τ =        0 t.

             D. Validity of the few-spin conjecture
                                                                                                 F. Long-time behavior of (t): BCS side
   We are now in the position to prove the few-spin conjecture
                                                                                     Integrands in Eqs. (5.36) and (5.37) are highly oscillatory.
for infinitesimal quenches independently of either numerics
                                                                                  The argument of the cosine is stationary at ε = μ, E  (μ) = 0.
or arguments of Sec. II. At t → ∞ integrals in Eqs. (5.36)
                                                                                  For μ > 0 the stationary point is inside the integration range.
and (5.37) vanish by the Riemann-Lebesgue lemma. There-
                                                                                  For μ < 0 there are no stationary points on the integration
fore,
                                                                                  path. This leads to qualitatively different behavior of (t) on
                        (t) →                   −2iμf t
                                                                         (5.46)   the BCS (μ > 0) and BEC (μ < 0) sides.
                                         0f e             .
                                                                                     Consider first the BCS regime. We evaluate X        !1 (t) in
According to the few-spin conjecture this asymptotic behavior                     Eq. (5.42) in stationary-phase approximation
of (t) occurs when there is a single isolated root pair at                                              
                                                                                        !                 π 0 2i 0 t+iπ/4
μf ± i 0f . Equation (5.21) shows that our L2 (u) does have                             X1 (t) = K(! μ)        e           + O(1/t),       (5.51)
this pair of roots. Moreover, the remaining 2N roots are given                                              t
by Eq. (5.18) and we explicitly see from Appendix B that their                    where we used E(!! μ) = 0 , E ! (!
                                                                                                                     μ) = 1/ 0 . With the help of
imaginary parts scale as 1/N at large N and that they merge                       Eq. (5.44) we obtain from Eq. (5.35) for the order parameter
into a continuum of roots on the real axis in the N → ∞ limit.                    amplitude
Thus, there is indeed a single isolated root pair at μf ± i 0f                                              √               2 cos(2 0 t + π/4)
in the thermodynamic limit.                                                             | (t)| =     0f +    π K(μ)         0      √           .     (5.52)
                                                                                                                                        0t

                                                                                  The phase of the order parameter obtains with the help of
                     E. Weak-coupling limit
                                                                                  Eq. (5.45),
    Simpler expressions obtain in the weak-coupling (BCS)
                                                                                                            √               2 cos(2   0 t + π/4)
limit when 0 is much smaller than other energy scales (Fermi                            (t) = 2μf t +       π K  (μ)      0               3/2
                                                                                                                                                 .   (5.53)
energy in gases and Debye energy in metals). This limit                                                                          2(    0 t)
describes superconductivity in metals and applies to recent                       Coefficients K(μ),K  (μ) are given by Eqs. (5.43), (B8),
experiments on nonadiabatic BCS dynamics [25,31]. In our                          and (B4). Simpler expressions for G(ε) are available in 2D
quench phase diagrams (Figs. 2–4, etc.) the weak-coupling                         and in the weak-coupling (BCS) limit; see Eqs. (B5) and (B6).
regime corresponds to a small neighborhood of the origin.                         For example, in the BCS limit ( 0 /εF → 0),
    At weak coupling μ ≈ εF = 1. Integrals (5.36) and (5.37)
are dominated by energies close to the Fermi energy, |ε −                                                  2δ 0 cos(2 0 t + π/4) −2iμf t
                                                                                         (t) =      0f −             √           e       ,           (5.54)
μ| ∼ 0 , where f (ε) ≈ 1 independent of dimensionality. It                                                 π 3/2          0t
is convenient to change the integration variable to ξ = ε − μ                     where δ 0 = 0f − 0i and we additionally used 0 ∝
and extend the integration to the entire real axis. X2 (t) vanishes               exp(−ω/γ ). Note that the second term in Eq. (5.53) is
by particle-hole symmetry (integrand is odd in ξ ). The error                     proportional to 0 /εF . This expression for (t) holds in the
due to these approximations is proportional to 0 /εF , which                      BCS limit for both one- and two-channel models in 2D and
vanishes in the weak-coupling limit. Equation (5.35) implies                      3D. Equation (5.54) for μf = 0 appeared in Ref. [18] without
                                     ∞                                            derivation.
                                          cos[2E(ξ )t]dξ
    | (t)| =    0f − 4δ    0                                   ,         (5.47)       Let us also mention that long times for which asymptotes
                                 0       E(ξ )[π 2 + H 2 (ξ )]                    of the order parameter derived in this section apply in practice
                √                                                                 (e.g., in numerical simulations) mean t such that 1/ 0  t 
where E(ξ ) =    ξ2 +     2
                          0, δ       0 =          0f −        0i , and            1/δ. At times of order of the inverse level spacing 1/δ partial
                                                                                  recurrences √ occur; see Fig. 26. Oscillations with frequency
                                         E(ξ ) − ξ
                    H (ε) = ln                     .                     (5.48)   2 0 and 1/ t decay in the weak-coupling limit of the one-
                                         E(ξ ) + ξ                                channel model were identified by Volkov and Kogan [3].
In deriving Eq. (5.47) we used the weak-coupling gap formula
                                                                                                 G. Long-time behavior of (t): BEC side
  0 ∝ exp(−ω/γ ) and Eqs. (B6) and (B8). [Note that at
relevant energies 4E(ε)/γ ∝ 0 /εF → 0.] We also used the                             In the absence of stationary points, integrals of the type
fact that the integrand is even in ξ to convert the integration                   of Eq. (5.42) are dominated by the end point, ε = 0 here.
range from (−∞,∞) to (0,∞).                                                       Normally, they vanish as 1/t at large t, but in the present case

                                                                            033628-33
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                         PHYSICAL REVIEW A 91, 033628 (2015)


     (a)              1                                                            The other two integrals vanish as 1/t ln3 t and are therefore
                                                                                   negligible. Equations (5.35), (5.44), and (5.45) yield the
                    0.8                                                            amplitude and the phase of the order parameter,
                                                                                                                           δω sin(2Emin t)
                                                                                                    | (t)| =          1−
       | (t)|/ 0i
                    0.6                                                                                         0f                         ,    (5.57)
                                                                                                                            γ |μ|t ln2 t
                    0.4                                                                                                   δω cos(2Emin t)
                                                                                                      (t) = 2μf t −                      ,     (5.58)
                                                                                                                           γ Emin t ln2 t
                    0.2                                                                            √
                                                                                   where Emin = μ√2 + 20 .            √
                     0
                                                                                      In 3D f (ε) = ε and K(ε) ∝ ε at small ε. This follows
                      0       0.5             1       1.5   2      2.5
                                                                                   from Eqs. (5.43), (B8), and (B4) and is, for example, readily
                                                  t
     (b)                                                                           verified in the strong-coupling limit with the help of the last
         0.9805                                                                    expression in Eq. (B7). We split the integration range in
                                                                                   Eq. (5.55) into two, (0,1/ ) and (1/ ,∞), where t   1.
                                                                                   In the first integral we can expand in small
                                                                                                                              √ t, which results
                                                                                   in a Gaussian integral that behaves as 1/ t at large t. The
                                                                                   second integral vanishes faster as t → ∞. We thus determine

       | (t)|/ 0f
                                                                                   the following (exact) large-time asymptote:
               0.98
                                                                                                        1/2                   !
                                                                                           !1 (t) = − π      δω     e2i E(0)t+iπ/4
                                                                                           X                                            .       (5.59)
                                                                                                                 ! (0)]3/2 E(0)H 2 (0)
                                                                                                     (2t)3/2 γ [−E
                                                                                   With the help of Eqs. (5.44) and (5.45) we finally derive
         0.9795                                                                                                      δω cos(2Emin t + π/4)
               0                    0.5           1         1.5          2
                                                                                           | (t)| =    0f   1−c                            ,    (5.60)
                                                  t                                                                   γ     (2|μ|t)3/2
    FIG. 26. (Color online) Finite-size effects, such as partial                                               |μ| δω sin(2Emin t + π/4)
recurrences in | (t)|, develop at times of order of the inverse
                                                                                           (t) = 2μf t − c                              .      (5.61)
                                                                                                               Emin γ      (2|μ|t)3/2
level spacing δ ∝ 1/N between discretized single-particle energy
levels εk . Long-time behaviors derived in our paper apply at                      The coefficient c depends on μ, 0 , and γ . It is known exactly
times tδ  1. In other words, we take the thermodynamic limit                      from Eq. (5.59), but involves G(0), which in 3D is an elliptic
first and large-time limit second. Two detuning quenches in a 3D                   integral according to Eq. (B4). In the strong-coupling BEC
two-channel model are shown for N = 5024 and (a) γ = 0.5, 0i =                     limit, μ → −∞, G(ε) is independent of ε and takes a simple
3.0 × 10−2 max , 0f = 2.9 × 10−4 max , δ = 3.4 × 10−3 max , and                    form (B7). In this case,
(b)          γ = 0.1, 0i = 0.97 max , 0f = 0.99 max , δ = 8.0 ×                                                         
                                                                                                             
10−3 max .                                                                                              π |μ| 4|μ|        |μ| −2
                                                                                                 c=                 +π               ,      (5.62)
                                                                                                         εF    γ εF          0

K(0) = 0 in both 2D and 3D, so they vanish faster. Unlike                          where we restored the original energy units.
the BCS side, the long-time behavior on the BEC side is not
universal in that it depends on the form of K(ε) at small ε, i.e.,
on the density of states and on the asymptotic spin distribution.                                      H. Long-time behavior of spins
As a result, for example, it is different in 2D and 3D.                               Let us also work out the long-time behavior of individual
   We first integrate by parts to obtain                                           spins given by Eqs. (5.40) and (5.41) and compare it to the
                                                                                   asymptotic spin distribution, Eqs. (2.62) and (3.11), obtained
           !1 (t) = − 1
                                          ∞
                                              K(ε)  2i !                          earlier. The latter result is based on the few-spin conjecture,
           X                                         e E(ε)t dε.         (5.55)
                     2it              0       ! (ε)
                                              E                                    so the agreement with linear analysis provides yet another
                                                                                   (though redundant because we already proved the few-spin
In 2D the dimensionless density of states f (ε) = 1 and it                         conjecture for infinitesimal quenches in Sec. V D) check.
follows from Eqs. (5.43), (B8), and (B5) that K(ε) ∝ 1/ ln2 ε.                        Functions X1,2 vanish as t → ∞, while the large-time limit
We evaluate the large t asymptote of this integral by splitting                    of Y1,2 derives from the identity
the integration range into three, (0,1/ t),(1/ t, /t), and                                      ∞                     
( /t,∞), where is such that 1  ln  ln t. In the first                                         dε F (ε )e±2iE(ε )t
                                                                                          lim −                       = ±iπ αF (ε)e±2iE(ε)t ,   (5.63)
integral we expand the integrand in small ε, which leads to an                           t→∞ 0         ε − ε
          1/ t
integral 0      d(ln ε)/ ln3 ε and                                                 where α is the sign of tdE(ε )/dε at ε = ε and F (ε ) is an
                                                                                   arbitrary bounded continuous function.
                                          2i E(0)t!
                          !1 (t) = δω ie            1                                 Applying this identity to Eqs. (5.38) and (5.39) and
                          X                              .               (5.56)
                                      ! (0)E(0) t ln2 t
                                    γ E                                            substituting resulting expressions into Eqs. (5.40) and (5.41),

                                                                             033628-34
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                    PHYSICAL REVIEW A 91, 033628 (2015)

we obtain                                                                   In I2 we replace x 2 + 1 → x02 up to terms of order a/x0 . After
   −
  s∞ (ε,t)e2iμf t      2δω exp[−2iE(ε)t − iφ]                               this, a substitution
                                                                                                y = exp π x/2 transforms it into the cosine
       −          = 1−                                                      integral dy cos y/y with known behavior, leading to
      sf (ε)            γ    π 2 f 2 (ε) + H 2 (ε)
                                                                                                             a           
                      2δω ξ                  cos[2E(ε)t + φ]                                     I2 =          2
                                                                                                                 + o a/x02 .                    (5.69)
                    −         −1                                      ,                                     π x0
                       γ E(ε)                 π 2 f 2 (ε) + H 2 (ε)
                                                                            Integrating by parts in I3 , we see that it is proportional to
                                                               (5.64)       e−πa/2 /x02 , which is negligibly small. Thus,

     z
    s∞  (ε,t)
                              2
                  2δω 0f cos[2E(ε)t + φ]                                                            1     1             1
              =1+                                 ,            (5.65)              I1 + I2 + I3 =     −          +o           .                 (5.70)
       z
     sf (ε)        γ ξ E(ε) π 2 f 2 (ε) + H 2 (ε)                                                   2 2| ln(τ )|    | ln(τ )|
                                                                            Note the cancellation of the auxiliary parameter a. Finally,
where ξ = ε − μ and φ is defined through
                                                                            plugging this into Eq. (5.50), we derive the short-time behavior
                                    H (ε)                                   of the gap function amplitude
                 cos φ =                              ,
                              π 2 f 2 (ε) + H 2 (ε)                                                                      0f −      0i
                                                               (5.66)                         | (t)| =        0i +                      .       (5.71)
                               πf (ε) sgn(tξ )                                                                          |ln(   0 t)|
                 sin φ =                              .
                              π 2 f 2 (ε) + H 2 (ε)
                                                                                   VI. APPROACH TO THE ASYMPTOTE IN THE
In our case t > 0, but we still kept it under the sign function                               NONLINEAR CASE
to ensure proper behavior under time reversal; see Eq. (6.2).
                                                                                Here we discuss the approach of (t) to its large-time
Equations (5.64) and (5.65) match Eq. (2.62) with
                                                                            asymptote in the nonlinear case. We consider regimes I
                         2δω             0                                  and II, the gapless phase and the phase where (t) →
   θ (ε) ≈ sin θ (ε) =                                 .       (5.67)             −2iμ∞ t−2iϕ
                                                                                              . Rather than rigorously deriving the t → ∞
                          γ E(ε) π 2 f 2 (ε) + H 2 (ε)                        ∞e
                                                                            asymptote in its entirety as we did for the linearized dynamics,
(Not that in the present case ∞ = 0f and μ∞ = μf .) This                    we present an argument based only on our knowledge of
indeed agrees with Eq. (3.13) obtained from the few-spin                    the frequency spectrum that works under certain general
conjecture.                                                                 assumptions about relevant Fourier amplitudes.
                                                                                As t → ∞ spins tend to their steady-state form, s(ε,t) →
                                                                            s∞ (ε,t), where s∞ (ε,t) is given by Eqs. (2.45) and (2.62) in
                     I. Short-time behavior
                                                                            regimes I and II, respectively. In phase II, in a reference frame
    Here we analyze the short-time behavior of | (t)| for                   rotating with frequency 2μ∞ around the z axis, s∞ (ε) rotates
quenches within the universal weak-coupling regime. For                     with a constant frequency 2E∞ (ε) = 2 (ε − μ∞ )2 + 2∞ . As
large quenches from weaker to stronger coupling, when                       mentioned above, an integrable model with N degrees of free-
   0f / 0i  1, or from the normal state (zero initial coupling)            dom is characterized by N incommensurate frequencies [63]
in this regime | (t)| grows as e 0f t . This exponential growth             that are determined by the integrals of motion and are fixed
reflects the instability of the normal state in the presence of             throughout its time evolution. The Fourier decomposition of
superconducting interactions [7,16]. At the same time, even for             any dynamical quantity can have only these basic frequencies
small quenches | (t)| rises or falls sharply at short times; see            in its spectrum. In particular,
Figs. 7 and 25. Sharp growth is seen in experiment, too, though
                                                                                                        ∞
most of it is probably due to a different mechanism [31].                         | (t)| =   ∞+             F (ε) cos[2E∞ (ε)t]f (ε)dε,          (6.1)
    A direct small t expansion of the cosine in Eq. (5.36)                                          0
diverges at high energies. Cutting off the integral at ε
(Debye energy in the case of metals), one obtains [12]                      with some unknown function F (ε).
δ| (t)| ∝ δ 0 (ε t)2 . This is cutoff dependent and applies                    Terms containing sin[2E∞ (ε)t] are absent by time-reversal
only to ultrashort times t  1/ε that vanish as the cutoff is               symmetry [cf. Eq. (5.35)] of the equations of motion (1.8)
sent to infinity. We are interested in times 1/ε  t  1/ 0 .               and (1.33) [see also Eq. (2.24)]
    Consider Eq. (5.50). The argument of the cosine is small
                                             πx0                              s z (−t) = s z (t), s + (−t) = s − (t),           ¯ (−t) =    (t), (6.2)
for x  x0 , where x0 is determined by e 2 = 1/τ , i.e., x0 =
 2                                                                          where we suppressed ε dependence of spins for compactness.
π
   ln(1/τ ). Let us divide the domain of the integration into three
intervals: [0,x0 − a], [x0 − a,x0 + a], and [x0 + a,∞) and let              These relations hold at all times as long as the initial condition
the corresponding integrals be I1 , I2 , and I3 , respectively.             at t = 0 satisfies them, which our initial state (1.28) does.
The auxiliary parameter a, 1  a  x0 , is such that 1/a      √→
                                                                                A common practice in previous work is to attempt to deter-
0,a/x0 → 0 as x0 → ∞. For example, one can take a = x0 .                    mine the approach of | (t)| to its asymptotic value ∞ from
Expanding the cosine in small τ in I1 and integrating, we                   the steady-state spins s∞ (ε,t). Consider the one-channel case
obtain                                                                      for simplicity. Continuum version of Eq. (1.13) at t = ∞ is
                      1      1      a                                                                           ∞
               I1 = −           −     2
                                        + o a/x02 .          (5.68)                           ∞ (t) = λ
                                                                                                                       −
                                                                                                                      s∞ (ε,t)f (ε)dε.           (6.3)
                      2 π x0      π x0                                                                        0

                                                                      033628-35
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                     PHYSICAL REVIEW A 91, 033628 (2015)

                       −                                                       method [cf. Eq. (5.52)]
The constant part of s∞   (ε,t) yields ∞ , while the contribution
of the oscillating part integrated over ε vanishes (dephases) as                                      √
t → ∞. One can further determine the large-time asymptote                                                                2 cos(2 ∞ t + π/4)
                                                                                     | (t)| =    ∞+       π F (μ∞ )      ∞      √           .     (6.5)
of Eq. (6.3) similarly to how we evaluated the large-time                                                                           ∞t
behavior of Eq. (5.35). This is, however, not the correct                      The only assumption about F (ε) here is that it is smooth.
asymptote of the actual (t). Not only does it not yield the                    This is an extension of Eq. (5.52) to the nonlinear regime.
correct coefficient of the time-dependent part of (t) [such                    In the weak-coupling BCS limit this result was published
as the coefficient c in Eq. (5.60)], but also the actual time                  in Ref. [16]. In this limit ∞ is given by Eq. (3.29) and
dependence can be different.                                                   generally it obtains from Eqs. (3.15) and (3.39) in 2D and
   At finite t there is a correction to the steady-state value of              3D, respectively, and Eq. (3.14) as the imaginary part of u.
the spin, s(ε,t) = s∞ (ε,t) + δ s(ε,t), so that the actual order               Here we see that expression (6.5) holds throughout the entire
parameter is                                                                   region II for both one- and two-channel models.
                  ∞                             ∞
                       −
    (t) = λ           s∞ (ε,t)f (ε)dε + λ           δs − (ε,t)f (ε)dε.
              0                             0                                                                B. Regime II
                                                                     (6.4)         Regime II has the same asymptotic (t) as II by definition
                                                                               only with μ∞ < 0. There are now no stationary points on the
Even though δs − (ε,t) is small as compared to the oscillating
           −                                                                   integration path. The approach to the asymptote is therefore
part of s∞   (ε,t) at large times, this is no longer true after
                                                                               determined by the behavior of F (ε)f (ε) near the end points,
integrating these quantities over ε. Consider, for example,
                                              −                                ε = 0 in this case. We assume this behavior is the same as
Eq. (5.40). We showed in Sec. V H that s∞        (ε,t) comes from
                                                                               in linear analysis, since we expect the time dependence to
functions Y1,2 (ε,t). However, we see from Eq. (5.35) that the
                                                                               have the same functional form throughout a given regime.
integral of these functions over ε vanishes and, as a result,
                                                                               According to Sec. V G, this means finite nonzero F (0) in 3D
they do not contribute to (t). The correction δs − (ε,t), on the
                                                                               and F (ε) ∝ 1/ ln2 ε for ε  1 in 2D.
other hand, comes from both X1,2 (t) and Y1,2 (ε,t). It is this
                                                                                   Expanding Eq. (3.11) in small ε and using Eq. (2.62), we
contribution from X1,2 (t) to δs − (ε,t) that actually determines
                                                                               see that the spin components at t → ∞ do behave the same
   (t). Thus, there is a partial cancellation between the two
                                                                               as in linear analysis, though this in itself does not prove our
integrals in Eq. (6.4) and the true large-time behavior of (t)
                                                                               assumption. Moreover, the asymptotic spin distribution (3.11)
can only be determined by keeping both.
                                                                               is continuous across critical lines separating various regimes,
    Nevertheless, ∞ (t) being a legitimate dynamical quantity
                                                                               so the same small ε form holds in gapless region I as well.
has the right frequency spectrum and also contains the
                                                                                   As long as our assumptions about F (ε) are correct, the
dimensionless density of states f (ε). So, it still produces a
                                                                               analysis of the integral in Eq. (6.3) is the same as that in
correct large-time dependence when, for example, the latter is
                                                                               Sec. V G, resulting in
set by a stationary point as in Eq. (5.52) or by the behavior of
                                                                                                                 min 
f (ε) at small ε as in Eq. (5.60). The situation on the BEC side                                            sin 2E∞    t
in 2D is different. The ln2 t dependence in the denominator                           | (t)| = ∞ 1 − c1             2
                                                                                                                              in 2D       (6.6)
                                                                                                                t ln t
of Eq. (5.57) comes from K(ε) ∝ 1/ ln2 ε behavior of the
Fourier amplitude at small ε; see Eq. (5.42) and the text                      and
below Eq. (5.55). This is, in turn, a consequence of K(ε) ∝                                                  min         
                                                                                                         cos 2E∞   t + π/4
H −2 (ε) and H (ε) ∝ ln ε, which follow from Eqs. (5.43), (B8),                  | (t)| =       ∞ 1 − c2                                 in 3D,   (6.7)
and (B5). Were we to evaluate the large-time asymptote of                                                      t 3/2
| (t)| using Eq. (6.3), we would obtain 1/(t ln t) instead of
                                                                               at large times, where E∞  min
                                                                                                             = μ2∞ + 2∞ and c1 and c2 are
1/(t ln2 t). To see this, note that Eq. (5.64) implies that the
                       −                                                       real coefficients that depend on 0i , 0f , and γ .
oscillating part of s∞   (ε,t) is proportional to H −1 (ε), i.e., to
1/ ln ε, at small ε and apply the same steps as in the text below
Eq. (5.55). The 1/ ln ε dependence cancels in Eq. (6.4) due                                                C. Gapless regime
to the second term on the right-hand side. We note also that                      Finally, we turn to regime I. Now (t) → 0 at t → ∞.
                                  −
Eqs. (2.62) and (3.11) imply s∞     (ε,t) ∝ 1/ ln ε in all of region           Spins s∞ (ε) rotate with frequencies 2ε around the z axis, so
II in 2D, not just in the linear approximation.                                that the Fourier transform of the order parameter magnitude is
    Similar considerations apply in analyzing Eq. (6.1). Let us                of the form
work out the large-time behavior of | (t)| in steady states I,                                                  ∞
II, and II separately.                                                                         | (t)| =            F (ε) cos(2εt)f (ε)dε,        (6.8)
                                                                                                            0
                             A. Regime II                                      and the sin(2εt) term vanishes by time-reversal symme-
   In steady states II and II (t) → ∞ e−2iμ∞ t−2iϕ . For                      try (6.2).
quenches in region II μ∞ > 0, so it can be viewed as a nonequi-                   In 3D we similarly assume finite and nonzero F (0). Steps
librium extension of the BCS regime. The frequency spectrum                    outlined below Eq. (5.58) in Sec. V G now lead to the following
                                                                              large-time behavior:
2E∞ (ε) has a stationary point at ε = μ∞ , E∞  (μ∞ ) = 0, which
in regime II lies within the integration range. The large-time                                                             c3
behavior of Eq. (6.1) obtains with the help of stationary point                                             | (t)| =              .               (6.9)
                                                                                                                          t 3/2

                                                                         033628-36
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                             PHYSICAL REVIEW A 91, 033628 (2015)

    In 2D we speculate that F (ε) ∝ 1/ lnr ε at small ε, where r    ing superfluidity in these systems include measurements of
                                                        −
is either 1 or 2. As discussed before in this section, s∞ (ε,t) ∝   the molecular condensate fraction [47,48], radio-frequency
1/ ln ε in 2D, so that ∞ (t) ∝ 1/(t ln t). The 1/ ln ε term,        absorption spectra [68], and observation of vortices [69].
however, cancels from F (ε) at least in linear analysis and it      Signatures of “far-from-equilibrium phases” I, II, and III—
ends up being proportional to 1/ ln2 ε instead. In the gapless      gapless, gapped (Volkov-Kogan), and oscillatory—in these
case we allow for a possibility that such a cancellation does       experiments can be derived from the many-body wave function
not occur. The analysis of the integral in Eq. (6.8), analogous       (t) determined above.
to that leading to Eq. (5.60), then yields                             The pseudospin (fermionic) part     of (t) is a direct
                                      c4                            product of spin- 12 wave functions p (ūp |↓ + v̄p |↑ ) found
                       | (t)| =            .              (6.10)    in Sec. II D. In the gapless steady state
                                   t lnr t                                                                 
   The gapless regime contains the 0i = 0f = 0 point, the                 up           θp 1 −iεp t         θp 0 iεp t−iδp
                                                                                = cos         e      + sin       e        ,  (7.1)
origin of quench phase diagrams. It therefore includes the                 vp           2 0                 2 1
weak-coupling limit 0i /εF → 0 and 0f /εF → 0. Equa-
                                                                    where cos θp ≡ cos θ (εp ) is given by Eq. (3.11) in all three
tion (6.8) becomes in this limit [see Sec. V E]
                                                                    phases. The second term represents an occupied pair of states
                            ∞                                       ±p (pseudospin up); the first represents an empty pair of
               | (t)| =         F (ξ ) cos(2ξ t)dξ,       (6.11)    states (pseudospin down). (t) in the gapless phase is a
                          −∞
                                                                    coherent superposition of eigenstates of a free Fermi gas with
where F (ξ ) is even in ξ . Now there can be no power law           different energies reflecting the fact that (t) → 0 implies
in t contribution at large t coming from integration limits.        vanishing of interactions between fermions on the mean-field
Instead, | (t)| vanishes exponentially [17,18] as A(t)e−2α 0i t     level. Effectively, the system is governed by a noninteracting
independent of dimensionality, where α ∼ 1 and A(t) is a            Hamiltonian at t → ∞. It nevertheless retains superconduct-
decreasing power law, A(t) ∼ 0i at t ∼ 1/ 0i . Recall that          ing correlations. For example, in the weak-coupling regime
throughout this paper we have been using units where εF = 1.        its superfluid density is half that in the ground state and in
To convert to arbitrary units in Eqs. (6.9) and (6.10), one         phase II [18]. Phase I is therefore a nonequilibrium gapless
needs to replace t → εF t. Guided by linear analysis, we            superfluid.
further assume that coefficients c4 and c5 are of order 0f ,            In the gapped steady state Eqs. (2.51) and (2.63) imply
which we take to be comparable to 0i . It is clear that at any
finite 0i /εF  1 power laws in Eqs. (6.9) and (6.10) coming                                             #
                                                                                                           ground-state pair
                                                                                                               $%    &
                                                                                                             
from the lower integration limit will eventually win over the                   up e ∞  iμ t           θp |Up | −iEp∞ t
exponential decay. The comparison of e−2α 0i t with (εF t)−1                                     = cos          e
                                                                                vp e−iμ∞ t             2 |Vp |
shows that the weak-coupling result is valid at times such that
                                                                                                                   excited pair
ln(εF / 0i )  0i t  1, while for 0i t  ln(εF / 0i ) it has                                                 #        $%     &
                                                                                                              
to be replaced with Eqs. (6.9) and (6.10).                                                               θp        |Vp |     ∞
                                                                                                   + sin                  eiEp t ,   (7.2)
                                                                                                         2        −|Up |
            VII. EXPERIMENTAL SIGNATURES
                                                                    where
    Far-from-equilibrium states of fermionic superfluids de-                                                     
scribed in this paper can be observed in different systems with                         1   ξp                        1   ξp
                                                                          |Up | =         +    ,       |Vp | =          −    ,       (7.3)
various experimental techniques.                                                        2 2Ep∞                        2 2Ep∞
    Matsunaga et al. [25,26] directly measured the time-
dependent amplitude | (t)| induced by an ultrafast electro-         ξp = εp − μ∞ , and we dropped the nonessential constant
magnetic perturbation in Nb1-x Tix N films using terahertz-         phase ϕ. Bogoliubov amplitudes |Up | and |Vp | are the same
pump–terahertz-probe spectroscopy. The underlying system            as in the BCS ground state [70] with gap ∞ and chemical
is a BCS superconductor [weak-coupling regime of the one-           potential μ∞ . The two wave functions on the right-hand side
channel model (1.3)] and for perturbation strength below            of Eq. (7.2) are the two orthonormal eigenstates of the BdG
certain threshold its nonadiabatic dynamics falls within region     Hamiltonian,
II of our quench phase diagrams. Even though we considered                                                
                                                                                                  ξp     ∞
BCS interaction quenches in the one-channel model in this                              HBdG =                .              (7.4)
                                                                                                   ∞   −ξp
paper, it is clear from our arguments that our results apply
more generally to any kind of nonadiabatic global perturbation.     The first one is a Cooper pair wave function in the BCS ground
Therefore, we expect | (t)| to be described by Eq. (6.5) de-        state and corresponds to an alignment of the pseudospin sp
rived originally in nonlinear regime by Yuzbashyan et al. [16].     antiparallel to the effective magnetic field. The second one is
These experiments indeed measure damped oscillations with           an excited state of the Cooper pair (sp parallel to the effective
frequency 2 ∞ , where ∞ is the asymptotic value of | (t)|           magnetic field) termed an excited pair in the original BCS
even when the system is deep in the nonlinear regime and ∞          work [71]. It is interesting to note that these excitations of
is much different from the ground-state gap. The power-law          the condensate in superconducting metals carry no charge and
approach, however, appears to be faster than 1/t 1/2 .              spin, so nonadiabatic dynamics considered here provides a
    In this paper we primarily focused on detuning or in-           unique venue for creating and measuring them [19]. The steady
teraction quenches in cold fermions. Experiments address-           state in phase II therefore is a coherent mixture of ground-state

                                                              033628-37
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                                     PHYSICAL REVIEW A 91, 033628 (2015)

and excited pairs, a superposition of eigenstates of the BCS                        a process in which an RF photon breaks a ground-state pair; the
Hamiltonian with gap ∞ and chemical potential μ∞ .                                  second peak corresponds to a process in which an RF photon
   A similar interpretation of the oscillatory state obtains by                     breaks an excited pair. The RF response of phase III similarly
Fourier transforming the amplitudes (2.73),                                         reflects the structure of the corresponding steady-state wave
                       ∞                                                      function (7.5). There are two series of peaks spaced by ω ,
          up ei μ̃t                θp apn −i(ep −nω )t                              the frequency of oscillations of | (t)|, coming from processes
                      =        cos           e
         vp e−i μ̃t                2 bpn                                            where an RF photon breaks a ground-state (excited) pair and
                        n=−∞
                                                   '                              absorbs or emits several quanta of the amplitude (Higgs) mode
                              θp b̄pn
                        + sin            ei(ep −nω )t ,    (7.5)                    | (t)|.
                              2 −āpn
where ω is the oscillation frequency of | (t)|, μ̃ and −2ep                                              VIII. CONCLUSION
are the zeroth harmonics of the phase of (t) and the common
phase of the amplitudes [see Eqs. (2.53) and (2.57)], and we                            In this paper we studied the coherent dynamics of an
again dropped the constant phase ϕ. This expression derives by                      isolated BCS-BEC condensate in two- and one-channel (BCS)
first going to a frame rotating with frequency 2μ̃ to get rid of                    models in two and three spatial dimensions. Our main focus
the linear term in the phase of (t). This makes e−iφp , the term                    was on detuning quenches ωi → ωf (interaction quenches
involving the relative phase, periodic according to Eq. (2.54)                      λi → λf in the one-channel model). We constructed exact
and it does not contribute to the momentum-dependent phases                         quench phase diagrams and predicted the order parameter
on the right-hand side. Phase III, therefore, can be understood                     dynamics (t) and the full time-dependent wave function (t)
as a superposition of generalized excited- and ground-state                         of the system at large times for any pair of values (ωi ,ωf ).
pairs with dispersions ±ep and quanta of the amplitude (Higgs)                      In contrast to most previous work, we considered quenches
mode | (t)|. As noted in Sec. II D 2, ep → εp at large εp .                         beyond the weak-coupling limit of BCS-to-BCS quenches. We
    The knowledge of the steady state allows us to compute                          add to this BCS-to-BEC and BEC-to-BCS quenches across the
far-from-equilibrium correlation and Green’s functions in all                       Feshbach resonance, as well as quenches on the BEC side. We
three phases. For example [72],                                                     showed that the weak-coupling limit is universal in that it is
                                         †
                                                                                    model and dimension independent. Outside of this limit, there
          iGp,> (t,t  ) = âp↑ (t) âp↑ (t  ) = ūp (t)up (t  ),                 are several qualitatively different features, the two-channel
                               †                                                    model having richer quench phase diagram as it contains an
        −iGp,< (t,t  ) = âp↑ (t  ) âp↑ (t) = v̄p (t  )vp (t),          (7.6)
                                                                                    extra parameter: dimensionless resonance width γ . All results
                                †         †
             Gp+ (t,t  ) =   â−p↓ (t) âp↑ (t  )   = vp (t)ūp (t  ).           for the one-channel model obtain from the two-channel ones
                                                                                    by taking the broad resonance, γ → ∞, limit.
With these we can evaluate various observables such as the                              We find the same three main nonequilibrium phases
superfluid density mentioned earlier in this section. Note also                     (asymptotic states) as in the weak-coupling regime. Inter-
that the steady-state momentum distribution n∞ p (t)dp is simply                    estingly, this seems to be a universal, model-independent
related to the z component of the pseudospin according to                           feature of quench dynamics of fermionic condensates, at least
Eq. (1.6). Taking into account that p and −p are both included                      when there is a global complex order parameter, so that the
in spz and integrating over the angles, we have                                     Cooper pairs interact only through this collective mode. The
                                    z                                             same three phases occur, for example, in p-wave supercon-
                     n∞
                      p (t) = 2p 2sp + 1 .
                                 2
                                                            (7.7)
                                                                                    ductors [36,37], spin-orbit coupled superfluids [81], and s-
Expressions for spz in phases I, II, and III appear in Eq. (2.48),                  wave superconductors with energy-dependent interaction [20].
Eq. (2.62), and Eqs. (2.55) and (2.72), respectively.                               One can speculate that similar universality according to the
    Finally, let us discuss the signatures of nonequilibrium                        order parameter type exists among quench phase diagrams
phases in radio-frequency (RF) spectroscopy [73–79]. Recall                         of multicomponent superfluids, such as three fermion species
that in an atomic Fermi gas the pairing occurs between atoms                        with pairing interactions or multiband superconductors.
in two different hyperfine states, |↑ ≡ |1 and |↓ ≡ |2 . The                            The above three main phases are phase I, where (t)
RF photon transfers atoms from one of these states, say |2 , to                     vanishes; phase II, where (t) → ∞ e−2iμ∞ t up to a constant
the third hyperfine state |3 that does not interact with |1 and                     phase factor; and phase III, where | (t)| oscillates persistently.
|2 . In an unpaired Fermi gas where atoms |2 are free, the RF                       It turns out that μ∞ plays the role of a nonequilibrium analog
absorption spectrum has a peak at the atomic transition energy                      of the chemical potential. For quenches within the weak-
ω = E23 . In the paired ground state, the peak shifts to ω > E23                    coupling regime μ∞ ≈ εF , while for quenches to deep BEC
by an amount equal to the minimum binding energy of Cooper                          μ∞ → −∞. Some of the new effects as one moves beyond
pairs [73].                                                                         the weak-coupling regime are as follows. The oscillatory
    The RF response of steady states I, II, and III was calculated                  approach of | (t)|√ to a constant (Volkov-Kogan behavior)
in Ref. [19] for quenches within the BCS regime and in                              changes from 1/ t for μ∞ > 0 to 1/t 3/2 in 3D and 1/(t ln2 t)
Ref. [36] for quenched p-wave superfluids. The calculation in                       in 2D for μ∞ < 0, and the oscillation frequency changes
the present case is identical [80], so we do not reproduce it here.                 from 2 ∞ to 2 μ2∞ + 2∞ . For resonance width below a
The RF spectrum of phase I is similar to that of the normal state,                  certain threshold, the asymptotic gap amplitude ∞ can be
a peak at ω = E23 . In phase II there are two peaks—at ω > E23                      much larger than 0f , the ground-state gap at final detuning
and ω < E23 —which come from the ground-state and excited                           ωf . Similarly, exponential vanishing of | (t)| in phase I
pairs, respectively; see Eq. (7.2). The first peak corresponds to                   gives way to a power-law behavior. Persistent oscillations

                                                                              033628-38
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                           PHYSICAL REVIEW A 91, 033628 (2015)

in phase III are first suppressed for stronger quenches and              It is this feature of the dynamics together with the inte-
then disappear altogether. For example, in 3D one-channel            grability of the underlying model that allowed us to explicitly
model there is a critical coupling λc , such that even quenches      determine the exact postquench asymptotic state of the system.
from an infinitesimally small λi to λf > λc produce no such          In this paper we presented for the first time a comprehensive,
oscillations. As λf approaches λc from below, the oscillation        consistent overview of a general method to explicitly evaluate
amplitude first increases, then decreases, and finally vanishes      the large-time asymptotic solution in classical integrable
at λf = λc .                                                         systems that support this kind of reduction. We are not aware
    The postquench asymptotic state of the condensate is a           of any similar method for other integrable nonlinear models,
coherent superposition of ground-state and excited pairs at          the rather different soliton resolution conjecture [82] being the
each momentum [multiple bands of such pairs shifted by the           closest analog we were able to identify.
oscillation frequency of | (t)| in phase III]. These are two             An interesting open question is whether a similar reduction
orthogonal eigenstates of a Cooper pair in the self-consistent       in the number of degrees of freedom in the course of time
field, and, for instance, the BCS ground state is a direct           evolution occurs also in nonintegrable pairing models. This
product of ground-state pair wave functions. Our steady state        can explain the aforementioned universality of the quench
in phases I and II is a direct product of such time-dependent        phase diagrams among systems characterized by a global
superpositions. In the Anderson pseudospin language, ground-         complex order parameter. It seems nonaccidental indeed that
state (excited) pairs correspond to the alignment of pseudospin      the nonintegrable spin-orbit coupled superfluid [81] has the
antiparallel (parallel) to the magnetic field. Even though we        same three main postquench phases and that, moreover, (t)
refer to these states as ground-state or excited pairs, we should    in phase III is given by an elliptic function dn. Presumably, a
stress that they are not the same as similar states of Cooper        generalization of this method to nonintegrable models would
pairs in the ground or excited states of the BCS Hamiltonian         rely on more general considerations without recourse to
since the self-consistent field is different. Excited pairs are      integrability-specific techniques and thus would clarify the
elusive excitations in superconductors; it is difficult to couple    underlying physical mechanism. It would also make a number
to them as they carry no charge or spin. Nonadiabatic dynamics       of interesting problems, such as, e.g., the competition between
of the BCS-BEC condensate provides an opportunity to access          chiral and antichiral components in p-wave superconductors
them, e.g., in the RF absorption spectrum.                           upon switching on superconducting interactions and, more
    Our treatment of the dynamics of the BCS-BEC condensate          generally, the dynamical interplay among various components
neglects the coupling to the noncondensed modes (mean-               in a multicomponent superfluid, potentially amenable to in-
field approximation), molecules with nonzero momenta q               depth analysis.
in the two-channel model. We check the validity of this
approximation for the two-channel model by estimating the
rates of the decoherence processes due to these terms for                               ACKNOWLEDGMENTS
postquench steady states in phase II and comparing them to the
                                                                       This work was supported in part by the David and Lucile
typical time scale on which the quench dynamics occurs. Our
                                                                     Packard Foundation (M.S.F. and E.A.Y.), by the Welch
preliminary results indicate that the mean-field approach is
                                                                     Foundation under Grant No. C-1809, and by an Alfred P. Sloan
justified for quenches sufficiently far from the μ∞ = 0 line in
                                                                     Research Fellowship (Grant No. BR2014-035) (M.S.F.).
the quench phase diagrams, e.g., quenches within deep BEC,
deep BCS, or across the resonance from deep BCS to deep
BEC and vice versa. A more thorough study of these effects is
                                                                               APPENDIX A: PAIR-BREAKING RATES
necessary to fully clarify the situation.
    In mean-field various pairing Hamiltonians, e.g., one- and          In this Appendix, we perform a preliminary analysis of
two-channel models considered here, chiral p-wave BCS, a             the validity of neglecting q = 0 terms far from equilibrium
certain class of d-wave BCS models [39], is equivalent to            in the Hamiltonian (1.1). So far, we have studied the quench
integrable classical spin (or spin-oscillator) chains with long-     dynamics of the condensate decoupled from these noncon-
range interactions. The most remarkable general feature of           densed modes. There are two kinds of relevant processes
their dynamics is a reduction in the number of effective degrees     due to the q = 0 terms: (i) excitation of molecules out of
of freedom as t → ∞. Consider, e.g., the one-channel model.          the condensate and (ii) excitation of fermionic quasiparticles
As explained above, its dynamics in the thermodynamic limit          through two-particle collisions. We estimate characteristic
at long times after the quench can be described in terms of          time scales of both processes in the postquench steady state.
just a few—zero (phase I), one (phase II), or two (phase III)—       We find that sufficiently far from the μ∞ = 0 line in our quench
collective classical spin variables. In other words, the number      phase diagrams (see Figs. 3 and 21) these time scales are much
of spins at long times reduces from infinity to zero, one, or two.   larger than the characteristic time of the quench dynamics. This
Moreover, the spin times evolve with the same Hamiltonian            means that dropping q = 0 terms is indeed justified at times it
only with “renormalized” parameters. For example, in phase           takes for the quench dynamics to develop and reach the steady
I the effective Hamiltonian at large times is simply H = 0,          state. At much later times, after the quench dynamics plays
and in phase II it is H = 2μ∞ Sz − gS− S+ , where S is the           out, these terms set in, presumably leading to decoherence
collective spin of length |S| = ∞ /g and g is the original           and eventual thermalization of our (isolated) system. We note
BCS coupling constant. The order parameter (t) coincides             also that the μ∞ = 0 line can be very roughly interpreted as
with that of the few-spin problem, while the original spins          a far-from-equilibrium generalization of the unitarity point.
relate to the collective ones in a more involved fashion.            Quenches away from this line are from BCS or BEC initial

                                                               033628-39
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                              PHYSICAL REVIEW A 91, 033628 (2015)

detuning to the far BCS and BEC side, including quenches                       Let us specialize to quenches into either deep BCS (ωf →
across the resonance.                                                       +∞) or deep BEC (ωf → −∞). We expect a much higher
   In what follows we consider a 3D condensate and, for                     rate in the latter case, because in the BCS regime ζq → +∞,
simplicity, we content ourselves with steady states in phase                requiring excited pairs of extremely high energy to create a
II (including II ), where pairing amplitude asymptotes to a                molecule. For quenches to the far BEC side μ∞ → −∞, while
constant, | (t → ∞)| = ∞ .                                                    ∞ remains finite regardless of the initial detuning; see, e.g.,
                                                                            Figs. 18 and 19. It follows that Ep∞ ≈ ξp = |μ∞ | + p2 /2m and
             1. Steady-state molecular production                           Eq. (5.4) implies ωf ≈ 2μ∞ . For α = β = −1 the argument
                                                                            of the δ function in Eq. (A6) is always positive; i.e., energy
   Here we compute the rate at which molecules with nonzero
                                                                            conservation cannot be satisfied, meaning that the ground-state
momentum are produced in steady state II, where initially all
                                                                            pairs do not contribute to the rate. Similarly, if α = β = 1 (two
molecules have zero momentum. To the lowest order in the
                                                                            excited pairs),
interaction, the corresponding scattering amplitudes are [83]
                                      ∞                                                                 (p1 + p2 )2           p2 + p22
   Ab (p1 ,p2 )δ(Efin − Ein ) =                                                   ζp1 +p2 − Ep∞1 − Ep∞2 ≈           + ωf − 1
                                             fin |V̂ (t)|   in dt,   (A1)                                   4m                   2m
                                    −∞
                                                                                                              (p1 − p2 ) 2
where | in and Ein are the steady-state wave function and                                            = ωf −                < 0.        (A7)
energy. | fin obtains from | in by destroying two pairs and                                                       4m
creating a molecule with momentum q = p1 + p2 and two                          Therefore, only scattering processes involving one fermion
unpaired atoms with momenta p1 and p2 . The energy of the                   from an excited pair and another from a ground-state pair
final state is                                                              contribute. Expression (A6) for the rate in this case is
                Efin = Ein + ζq ± Ep∞1 ± Ep∞2 ,                      (A2)                    4πg 2  2 θp2          θp " "2 " "2
                                                                                     −1
                                                                                    τmol ≈              sin     cos2 1 "Up2 " "Vp1 "
where plus (minus) corresponds to a ground (excited) pair and                                 Nf p ,p         2      2
                                                                                                    1 2

                           q2                                                                    2                    
                    ζq =      + ωf − 2μ∞                             (A3)                         3p1 + 2p1 · p2 − p22
                           4m                                                                ×δ                          .                 (A8)
                                                                                                            4m
is the energy of the molecule. The interaction V̂ (t) is described          Next we go from summations to integrations, integrate over
by the last term in Eq. (1.1),                                              the angle between p1 and p2 , and change integration variables
                        ( †
             V̂ (t) = g      b̂p1 +p2 (t)âp1 ↑ (t)âp2 ↓ (t)               from momenta to energies, which results in
                       p1 ,p2                                                                              ∞
                                                                                         −1      3γ                  θ (ε2 )
                                     †         †       )                                τmol ≈                 dε2 sin2      |U (ε2 )|2
                     + b̂p1 +p2 (t)âp2 ↓ (t)âp1 ↑ (t) .            (A4)                        2εF   0                2
                                                                                                     ε2
   Since our initial state does not contain molecules with                                                        θ (ε1 )
                                                                                                 ×       dε1 cos2         |V (ε1 )|2 .     (A9)
nonzero momentum, only the first term in Eq. (A4) contributes                                      ε2 /9             2
to the matrix element (A1). One also needs to keep in mind
                                                                            We replace the cosine with one, use |V (ε1 )|2 ≈ 2∞ /4(ε1 +
that our steady state contains superpositions of a ground-state
                                                                            |μ∞ |)2 , which follows from Eq. (7.3) together with |U (ε1 )|2 ≈
pair with energy −Ep∞ and an excited pair with energy +Ep∞
                                                                            1, and integrate over ε1 . According to Eq. (3.13), the
for each p. Equations (7.2) and (A1) then yield four scattering
                                                                            probability of finding an excited pair is
amplitudes [72],
                                           θp " "" "
                                                                                                       2
                                    θp                                                      θ (ε2 )      (δω)2
         A(−−)
           b    (p1 ,p2 ) = g cos 2 cos 1 "Vp2 ""Vp1 ",                              sin2           → 0i 4            as ε2 → ∞.          (A10)
                                      2     2                                                  2     16Ei (ε2 )
                                    θ     θ p "    "" "
                (p1 ,p2 ) = g sin 2 cos 1 "Up2 ""Vp1 ",                     A larger rate obtains for finite ωi than for ωi close to ωf .
                                      p
         A(+−)
           b                                              (A5)
                                     2     2                                In this case, δω ≈ 2μ∞ and√sin2 [θ (ε2 )/2] appreciably differs
                                    θp    θp " "" "                         from zero at energies about     0i |μ∞ |. We obtain
         A(++)
           b    (p1 ,p2 ) = g sin 2 sin 1 "Up2 ""Up1 ",
                                     2     2                                                               γ 2∞ 0i
                                                                                                   −1
where − (+) describes breaking a ground-state (excited) pair                                      τmol ∼             → 0.                 (A11)
                                                                                                            εF |μ∞ |
and A(−+)
      b    (p1 ,p2 ) = A(+−)
                          b    (p2 ,p1 ).
   Molecular production rate per atom at zero temperature                   In deriving Eq. (A10) we assumed finite resonance width γ . A
obtains from these amplitudes and Fermi’s golden rule [83],                 separate estimate for the broad resonance limit for quenches to
                                                                            deep BEC finds a rate that also vanishes, but as γ −1/3 |μ∞ |−1/2 .
                      2π  "" (αβ)              "2
               −1
             τmol   =               Ab (p1 ,p2 )"                              This result for the molecular production rate should be
                      Nf p p αβ                                             compared with the typical time scale τdyn of the quench
                             1 2
                                                                          dynamics for quenches to the far BEC side. Equations (5.60)
                      × δ ζp1 +p2 − αEp∞2 − βEp∞1 .       (A6)              and (6.7) imply
In this expression Nf is the total number of fermions in the                                            −1
                                                                                                       τdyn ∼ |μ∞ |.                      (A12)
absence of molecules and we took into account that there are
no molecules with nonzero momentum in our steady state.                     We see that indeed τdyn  τmol .

                                                                      033628-40
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                           PHYSICAL REVIEW A 91, 033628 (2015)

                   2. Two-particle collisions                       contains many εk . Specifically, ε → 0, but ε/δ√ → ∞ in
    Next we estimate the relaxation rate due to two-particle        the thermodynamic limit. For example, ε = δ N fulfills
collisions. In contrast to the molecular production, we find        these conditions. The latter summation becomes a principal
that here the contribution coming from just the ground-state        value integral in the N → ∞ limit, while the former one to
pairs is of the same order of magnitude or larger than that from    leading order in 1/N reads
                                                                               ∞
collisions that involve excited pairs. We therefore consider          N (εm )      1          1        π ν(εm )
ground-state pairs only and take the probability of finding                              −            =          cot π ςm .
                                                                     2E(εm )δ p=0 p + ςm   p + 1 − ςm   2E(εm )
such a pair at a given momentum p to be cos2 (θp /2) ≈ 1.
Let us analyze quenches to the far BCS side of the Feshbach                                                                    (B1)
resonance from any initial detuning. In this case, ωf  μ∞ ≈
F ; see, e.g., Fig. 19. The total scattering amplitude for this    The first sum is from εk < εm , the second sum is from εk > εm .
case has been studied in Ref. [2] [see Eq. (71) therein], which     Here it is important that the degeneracy Nk ≡ N (εk ) and the
also estimates the corresponding rate as                            spacing between εk vary smoothly with εk . As long as this is
                  2 2 2                     2                   the case, we can include any variation of the spacing into Nk .
           −1      g νF      ∞               ∞                         Thus, Eq. (5.13) to leading order in 1/N becomes
         τin ∼                  = γ F
                                     2
                                                  .       (A13)
                                                                                     ∞
                    ωf      F             ωf                                2           ν(ε )dε        ν(εm )
                                                                                 −−                 
                                                                                                       −         cot π ςm
                                                                                    0 2(εm − ε )E(ε )
                                                                             g 2                         2E(εm )
In fact, this is the well-known Fermi liquid result for the
quasiparticle lifetime. Indeed, λ = g 2 νF /ωf is the strength of                 δω εm − μ ± i 0
the effective interaction between fermions [see Eq. (1.4)] and                  = 2                .                           (B2)
                                                                                  g     E 2 (εm )
  ∞ is the typical excitation energy, the energy scale at which
spins deviate appreciably from their ground-state positions.        Recalling that ν(ε) = νF f (ε) and g 2 νF = γ in units of Fermi
   Equation (A13) has to be compared with the characteristic        energy, we obtain
time scale of the dynamics for quenches to the far BCS side.                           4E(ε) G(ε) 2δω ε − μ ± i 0
According to Eq. (6.5) this time scale is                            π cot π ς (ε) =          −       −             ,          (B3)
                                                                                       γf (ε)   f (ε)   γ E(ε)f (ε)
                                   1
                         τdyn ∼        .                  (A14)     where
                                   ∞                                                                    ∞
                                                                                                           f (ε )dε
We see that τdyn  τin for any finite resonance width γ since                      G(ε) = E(ε) −                        .      (B4)
                                                                                                    0   (ε − ε )E(ε )
ωf → ∞ in deep BCS. In the broad resonance limit, too,
τdyn /τin = λ2 ∞ /εF  1. This is because at large γ quenches       This principal value integral is the same as in Eq. (3.6).
to the far BCS in phase II are only possible from initial           We evaluated it in elementary functions for various cases in
detunings also on the far BCS side; see, e.g., Figs. 3(c) and 5.    Secs. III A and III B. Specifically, in 2D,
                                                                                    ⎧                                 ⎫
It then follows from Eq. (3.29) that ∞ ⩽ 0f  εF .                                  ⎨                                 ⎬
                                                                                               ε[ε − μ + E(ε)]
    A preliminary analysis for quenches to the far BEC                G2d (ε) = ln                                     ; (B5)
                                                                                    ⎩                                 ⎭
side shows that, at least for a finite resonance width γ                              E(ε) μ2 + 20 + μ2 + 20 − με
and sufficiently large |ωf |, one still has τdyn  τin . Thus,
neglecting two-particle collisions is justified at the times it     in the weak-coupling (BCS) limit, μ ≈ εF  0 , for energies
takes the quench dynamics to fully develop and reach its            not too far from the Fermi energy, in both 2D and 3D,
asymptote.                                                                                          E(ε) + ε − μ
                                                                                    Gwc (ε) = ln                 ;             (B6)
                                                                                                    E(ε) − ε + μ
       APPENDIX B: FINITE-SIZE CORRECTIONS
                  TO THE ROOTS                                      in the strong-coupling (BEC) limit in 2D and 3D,
                                                                                                                
    As mentioned in Sec. III, in the thermodynamic limit L2 (u)                               ε                   |μ|
                                                                                Gsc (ε) = ln
                                                                                 2d
                                                                                                 , Gsc (ε) = −π
                                                                                                    3d
                                                                                                                      .        (B7)
for quench initial conditions has a continuum of roots along the                             |μ|                    0
positive real axis. Here we verify this and determine finite-size
corrections to these roots.                                            Ground-state continual roots xk = εk + k δ obtain by
    Roots of L2 (u) are determined by Eq. (3.3) or, equivalently,   setting δω = 0 in Eq. (B3); i.e.,
by Eq. (5.13) in notation explained in the beginning Sec. V B,                                  4E(ε) G(ε)       H (ε)
which we employ here as well. The level spacing δ is of order                  π cot π (ε) =          −       ≡       .       (B8)
                                                                                                γf (ε)   f (ε)   f (ε)
1/N. Thermodynamic limit means N → ∞, so εk become
continuous with density ν(ε).                                       The quantity Fk ≡ F (εk ) defined in Eq. (5.19) evaluates
    Let us look for a pair of complex conjugate roots close to      similarly to Eq. (B1),
εm , writing it as cm = εm + ςm δ. We take ςm ≡ ς (εm ) to be                                    ∞
                                                                                     N (ε) ∂           1       1
of order 1, to be confirmed below. Note that ςm is generally              F (ε) = −                          −
complex. Our goal is to evaluate cm to first order in 1/N.                          2E(ε)δ 2 ∂ p=0 p + 1 −  p + 
We split the summation in Eq. (5.13) into two parts: over εk
in a small interval (εm − ε,εm + ε) and over remaining                              ν(ε) π 2 f 2 (ε) + H 2 (ε)
                                                                               =                               .               (B9)
εk . The interval is, however, sufficiently large so that it                       2E(ε)δ         f 2 (ε)

                                                              033628-41
YUZBASHYAN, DZERO, GURARIE, AND FOSTER                                                              PHYSICAL REVIEW A 91, 033628 (2015)

                  APPENDIX C: IDENTITIES                                    The leading term in 1/u expansion of 1/R(u) according
                                                                         to Eq. (C2) is −2/(g 2 u2 ). Therefore, the coefficient at 1/u in
   In this Appendix we prove Eq. (5.29). To this end, consider
                                                                         Eq. (C3) vanishes and that at 1/u2 is −2/g 2 . This yields
a function
                            (                )
               R(u) = L0 (u) (u − μ)2 + 20 ,             (C1)                                         0               αk
                                                                                                               =             ,
where L0 (u) is given by Eq. (5.14). Since zeros of L0 (u) are                                 k
                                                                                                   Fk 2k          αk2 + βk2
xk and its poles are εk it alternatively can be written                                                                                    (C6)
                                                                                         xk − μ                g2     βk
                  2 N      (u − xk ) (               )                                                         =    − 2       .
     R(u) = − 2 k=1                  (u − μ)2 + 20 .    (C2)                              k
                                                                                                   Fk 2k        2   αk + βk2
                       N
                       k=1 (u − εk )
                 g
Equation (5.29) follows by matching two leading terms in 1/u                Gap and chemical potential equations (1.18) and (1.20) in
expansions of function 1/R(u) obtained with the help of these            the notation of Sec. V B read
two alternative forms.
   Because 1/R(u) is a rational function with poles at u = xk                       ω − 2μ    Nk
and μ ± i 0 , we have                                                                   2
                                                                                           =           ,
                                                                                      g        2E(εk )
    1                    1                     1
                                                                                             k
                                                                                                                                           (C7)
         =                           +
   R(u)          (u − x  )L 
                              (x )2   2i   (u − c+ )L0 (c+ )                                2 2           εk − μ
             k         k    0 k    k      0
                                                                                         2n = 20 +   Nk 1 −         .
                                                                                              g              E(εk )
                            1                                                                      k
             −                            ,                     (C3)
                 2i   0 (u − c− )L0 (c− )
                                                                         Differentiation of these equations with respect to ω obtains
where c± = μ ± i 0 and we took into account that the square              δμ/δω and δ 0 /δω and comparison of the resulting quantities
bracket in Eq. (C1) evaluated at u = xk is equal to 2k . Note also      with the right-hand side of Eq. (C6) proves Eq. (5.29).
that L0 (xk ) = −Fk ; see Eq. (5.19). Equation (5.14) implies              Another identity used in Sec. V B derives by noting
                       L0 (c± ) = −βk ∓ iαk ,                   (C4)     that, according to Eq. (C2), 1/R(εk ) = 0. Setting u = εk in
                                                                         Eq. (C3), we obtain after some algebra
where
              Nk 0               2    Nk (εk − μ)                            
 αk =                      , βk = 2 +                . (C5)                               1                     αk (εk − μ) − 0 βk
             2[E(εk )] 3/2       g      2[E(εk )]3/2                                                       =                         .   (C8)
         k                            k
                                                                               j
                                                                                   (εk − xm )Fm 2m            2 0 αk2 + βk2 [E(εk )]2




 [1] P. W. Anderson, Phys. Rev. 112, 1900 (1958).                        [15] E. A. Yuzbashyan, V. B. Kuznetsov, and B. L. Altshuler, Phys.
 [2] V. P. Galaiko, Sov. Phys. JETP 34, 203 (1972).                           Rev. B 72, 144524 (2005).
 [3] A. F. Volkov and S. M. Kogan, Zh. Eksp. Teor. Fiz 65, 2038          [16] E. A. Yuzbashyan, O. Tsyplyatyev, and B. L. Altshuler, Phys.
     (1974) [,English translation: Sov. Phys. JETP, 38, 1018 (1974)].         Rev. Lett. 96, 097005 (2006); ,96, 179905(E) (2006).
 [4] Y. M. Galperin, V. I. Kozub, and B. Z. Spivak, Sov. Phys. JETP      [17] R. A. Barankov and L. S. Levitov, Phys. Rev. Lett. 96, 230403
     54, 1126 (1981).                                                         (2006).
 [5] P. B. Littlewood and C. M. Varma, Phys. Rev. B 26, 4883 (1982).     [18] E. A. Yuzbashyan and M. Dzero, Phys. Rev. Lett. 96, 230404
 [6] V. S. Shumeiko, Ph.D. thesis, Institute for Low Temperature              (2006).
     Physics and Engineering, Kharkov, Ukraine, 1990.                    [19] M. Dzero, E. A. Yuzbashyan, B. L. Altshuler, and P. Coleman,
 [7] R. A. Barankov, L. S. Levitov, and B. Z. Spivak, Phys. Rev. Lett.        Phys. Rev. Lett. 99, 160402 (2007).
     93, 160401 (2004).                                                  [20] R. A. Barankov and L. S. Levitov, arXiv:0704.1292.
 [8] M. Amin, E. Bezuglyi, A. Kijko, and A. Omelyanchouk, Low            [21] A. Tomadin, M. Polini, M. P. Tosi, and R. Fazio, Phys. Rev. A
     Temp. Phys. 30, 661 (2004).                                              77, 033605 (2008).
 [9] A. V. Andreev, V. Gurarie, and L. Radzihovsky, Phys. Rev. Lett.     [22] A. Nahum and E. Bettelheim, Phys. Rev. B 78, 184510 (2008).
     93, 130402 (2004).                                                  [23] V. Gurarie, Phys. Rev. Lett. 103, 075301 (2009).
[10] R. A. Barankov and L. S. Levitov, Phys. Rev. Lett. 93, 130403       [24] A. Faribault, P. Calabrese, and J.-S. Caux, J. Math. Phys. 50,
     (2004).                                                                  095212 (2009).
[11] M. H. Szymanska, B. D. Simons, and K. Burnett, Phys. Rev.           [25] R. Matsunaga, Y. I. Hamada, K. Makise, Y. Uzawa, H. Terai, Z.
     Lett. 94, 170402 (2005).                                                 Wang, and R. Shimano, Phys. Rev. Lett. 111, 057002 (2013).
[12] G. L. Warner and A. J. Leggett, Phys. Rev. B 71, 134514 (2005).     [26] R. Matsunaga, N. Tsuji, H. Fujita, A. Sugioka, K. Makise, Y.
[13] E. A. Yuzbashyan, B. L. Altshuler, V. B. Kuznetsov, and V. Z.            Uzawa, H. Terai, Z. Wang, H. Aoki, and R. Shimano, Science
     Enolskii, J. Phys. A 38, 7831 (2005).                                    345, 1145 (2014).
[14] E. A. Yuzbashyan, B. L. Altshuler, V. B. Kuznetsov, and V. Z.       [27] T. Papenkort, V. M. Axt, and T. Kuhn, Phys. Rev. B 76, 224522
     Enolskii, Phys. Rev. B 72, 220503(R) (2005).                             (2007).


                                                                   033628-42
QUANTUM QUENCH PHASE DIAGRAMS OF AN s-WAVE . . .                                                    PHYSICAL REVIEW A 91, 033628 (2015)

[28] T. Papenkort, T. Kuhn, and V. M. Axt, J. Phys. 193, 012050           [58] C. Sträter, O. Tsyplyatyev, and A. Faribault, Phys. Rev. B 86,
     (2009).                                                                   195101 (2012).
[29] H. Krull, D. Manske, G. S. Uhrig, and A. P. Schnyder, Phys.          [59] D. Pekker and C. M. Varma, Rev. Condens. Matter Phys. 6, 269
     Rev. B 90, 014515 (2014).                                                 (2015).
[30] N. Tsuji and H.Aoki, arXiv:1404.2711.                                [60] P. W. Anderson, J. Phys. Chem. Solids 11, 26 (1959).
[31] R. Matsunaga and R. Shimano, Phys. Rev. Lett. 109, 187002            [61] I. L. Kurland, I. L. Aleiner, and B. L. Altshuler, Phys. Rev. B
     (2012).                                                                   62, 14886 (2000).
[32] M. Beck, I. Rousseau, M. Klammer, P. Leiderer, M. Mittendorff,       [62] The integrand in Eq. (1.37) generally has a nonvanishing zeroth
     S. Winnerl, M. Helm, G. N. Gol’tsman, and J. Demsar, Phys.                Fourier mode; i.e., it contributes to both linear and periodic parts.
     Rev. Lett. 110, 267003 (2013).                                       [63] V. I. Arnold, Mathematical Methods of Classical Mechanics
[33] R. T. Brierley, P. B. Littlewood, and P. R. Eastham, Phys. Rev.           (Springer-Verlag, New York, 1978).
     Lett. 107, 040401 (2011).                                            [64] M. Tabor, Chaos and Integrability in Nonlinear Dynamics
[34] Y. Pehlivan, T. Balantekin, A. B., Kajino, and T. Yoshida, Phys.          (Wiley, New York, 1989).
     Rev. D 84, 065008 (2011).                                            [65] J. S. H. Goldstein, C. Poole, Classical Mechanics, 3rd ed.
[35] G. Raffelt, S. Sarikas, and D. d. S. Seixas, Phys. Rev. Lett. 111,        (Addison Wesley, Boston, 2002), Chap. 10.
     091101 (2013).                                                       [66] B. C. Carlson and J. L. Gustafson, SIAM J. Math. Anal. 25(2),
[36] M. S. Foster, M. Dzero, V. Gurarie, and E. A. Yuzbashyan, Phys.           288 (1994).
     Rev. B 88, 104511 (2013).                                            [67] DLMF, NIST Digital Library of Mathematical Functions, Chap.
[37] M. S. Foster, V. Gurarie, M. Dzero, and E. A. Yuzbashyan, Phys.           19, Release date 2014-04-25, http://dlmf.nist.gov/.
     Rev. Lett. 113, 076403 (2014).                                       [68] C. Chin, M. Bartenstein, A. Altmeyer, S. Riedl, S. Jochim, J. H.
[38] M. Gaudin, La fonction d’onde de Bethe (Masson, Paris, 1983).             Denschlag, and R. Grimm, Science 305, 1128 (2004).
[39] R. W. Richardson, arXiv:cond-mat/0203512.                            [69] M. W. Zwierlein, A. S. J. R. Abo-Shaeer, C. H. Schunck, and
[40] M. Ibanez, J. Links, G. Sierra, and S.-Y. Zhao, Phys. Rev. B 79,          W. Ketterle, Nature (London) 435, 1047 (2005).
     180501(R) (2009).                                                    [70] R. Schrieffer, Theory of Superconductivity (Perseus, New York,
[41] C. Dunning, M. Ibanez, J. Links, G. Sierra, and S.-Y. Zhao,               1989).
     J. Stat. Mech. (2010) P08025.                                        [71] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, Phys. Rev. 108,
[42] S. M. A. Rombouts, J. Dukelsky, and G. Ortiz, Phys. Rev. B 82,            1175 (1957).
     224510 (2010).                                                       [72] See Ref. [36] for a detailed calculation of analogous Green’s
[43] J. Dukelsky, S. Pittel, and G. Sierra, Rev. Mod. Phys. 76, 643            functions and expectation values.
     (2004).                                                              [73] P. Törmä and P. Zoller, Phys. Rev. Lett. 85, 487 (2000).
[44] G. Ortiz, R. Somma, J. Dukelsky, and S. Rombouts, Nucl. Phys.        [74] C. A. Regal and D. S. Jin, Phys. Rev. Lett. 90, 230404 (2003).
     B 707, 421 (2005).                                                   [75] S. Gupta, Z. Hadzibabic, M. W. Zwierlein, C. A. Stan, K.
[45] J. Dukelsky, C. Esebbag, and P. Schuck, Phys. Rev. Lett. 87,              Dieckmann, C. H. Schunck, E. G. M. van Kempen, B. J. Verhaar,
     066403 (2001).                                                            and W. Ketterle, Science 300, 1723 (2003).
[46] L. Amico, A. Di Lorenzo, and A. Osterloh, Phys. Rev. Lett. 86,       [76] J. Kinnunen, M. Rodriguez, and P. Törmä, Science 305, 1131
     5759 (2001).                                                              (2004).
[47] C. A. Regal, M. Greiner, and D. S. Jin, Phys. Rev. Lett. 92,         [77] C. H. Schunk, Y. Shin, A. Schirotzek, and W. Ketterle, Nature
     040403 (2004).                                                            (London) 454, 739 (2008).
[48] M. W. Zwierlein, C. A. Stan, C. H. Schunck, S. M. F. Raupach,        [78] S. Basu and E. J. Mueller, Phys. Rev. Lett. 101, 060405 (2008).
     A. J. Kerman, and W. Ketterle, Phys. Rev. Lett. 92, 120403           [79] A. Schirotzek, Y. I. Shin, C. H. Schunck, and W. Ketterle, Phys.
     (2004).                                                                   Rev. Lett. 101, 140403 (2008).
[49] P. Calabrese and J. Cardy, Phys. Rev. Lett. 96, 136801 (2006).       [80] We note that the contribution of stimulated emission processes is
[50] C. Kollath, A. M. Läuchli, and E. Altman, Phys. Rev. Lett. 98,           missing in Ref. [19]. This mistake is fixed in Ref. [36]. Moreover,
     180601 (2007).                                                            we computed the RF response for the two-channel model taking
[51] A. Leggett, in Modern Trends in the Theory of Condensed Matter            this term into account and we find that the absorbed intensity is
     (Springer-Verlag, Berlin, 1980), pp. 13–27.                               not significantly affected by this term for quenches to both BCS
[52] P. Nozières and S. Schmitt-Rink, J. Low Temp. Phys. 59, 195              and BEC final detunings at least for the values of the relevant
     (1985).                                                                   parameters considered.
[53] V. Gurarie and L. Radzihovsky, Ann. Phys. 322, 2 (2007).             [81] Y. Dong, L. Dong, M. Gong, and H. Pu, Nat. Commun. 6, 6103
[54] E. Burovski, N. Prokof’ev, B. Svistunov, and M. Troyer, New               (2015).
     J. Phys. 8, 153 (2006).                                              [82] T. Duyckaerts, C. Keni, and F. Merle, Cambridge J. Math. 1, 75
[55] A. Bulgac and S. Yoon, Phys. Rev. Lett. 102, 085302 (2009).               (2013).
[56] J. Levinsen and V. Gurarie, Phys. Rev. A 73, 053607 (2006).          [83] P. Phillips, Advanced Solid State Physics (Westview, Boulder,
[57] R. Richardson, J. Math. Phys. 18, 1802 (1977).                            CO, 2003).




                                                                   033628-43
