# Continuous-time quantum walks: Models for coherent transport on complex networks - Full Text

> Source: https://linkinghub.elsevier.com/retrieve/pii/S0370157311000184
> Collected: 2026-09-20
> Published: Unknown
> Zotero parent key: BA8IKGFR
> Evidence: Publisher or author-preprint PDF

Continuous-Time Quantum Walks:
                                                                       Models for Coherent Transport on Complex Networks
                                                                                       Oliver Mülken and Alexander Blumen
                                                       Theoretical Polymer Physics, University of Freiburg, Hermann-Herder-Straße 3, 79104 Freiburg, Germany
                                                                                                 (Dated: June 2, 2018)
                                                         This paper reviews recent advances in continuous-time quantum walks (CTQW) and their application to
                                                      transport in various systems. The introduction gives a brief survey of the historical background of CTQW. After
                                                      a short outline of the theoretical ideas behind CTQW and of its relation to classical continuous-time random
                                                      walks (CTRW) in Sec. 2, implications for the efficiency of the transport are presented in Sec. 3. The fourth
                                                      section gives an overview of different types of networks on which CTQW have been studied so far. Extensions
                                                      of CTQW to systems with long-range interactions and with static disorder are discussed in section V. Systems




arXiv:1101.2572v1 [quant-ph] 12 Jan 2011
                                                      with traps, i.e., systems in which the walker’s probability to remain inside the system is not conserved, are
                                                      presented in section IV. Relations to similar approaches to the transport are studied in section VII. The paper
                                                      closes with an outlook on possible future directions.

                                                      PACS numbers: 05.60.Gg, 05.60.Cd, 71.35.-y


                                                                    Contents                                              2. Line with traps                                  26
                                                                                                                          3. Line with traps and long-range interactions      27
                                            I. Introduction                                              1             C. Fractals                                            28
                                               A. Quantum Walks                                          2                1. Hyperbranched fractals                           28
                                               B. Experimental implementations of CTQW                   2             D. Random networks                                     29
                                               C. Transport in complex systems                           2                1. Disordered system with one trap                  29

                                           II. Definitions and terminology of CTQW                       3       VII. Relations between CTRW/CTQW and other
                                               A. Connectivity of network                                3            approaches                                              30
                                               B. Transfer matrix for CTRW                               3            A. Phase space approaches                               30
                                               C. Hamiltonian for CTQW                                   4               1. WF for a ring                                     30
                                               D. Example: A discrete ring                               4               2. Rings with energetic disorder                     32
                                                                                                                         3. Long-range interaction cycles                     33
                                           III. Efficiency of CTQW and CTRW                              5               4. Disordered networks                               33
                                                A. Examples                                              6            B. Quantum master equations                             34
                                                                                                                         1. Decoherence on rings                              34
                                           IV. CTQW on networks                                          8               2. Dimer with traps                                  35
                                               A. Deterministic networks                                 8
                                                  1. Two dimensional regular networks                    8     VIII. Outlook                                                  36
                                                  2. Star-like networks                                  11
                                                  3. Complete graph                                      12            Acknowledgements                                       37
                                                  4. Dendrimers                                          12
                                                  5. Husimi-cacti                                        13            References                                             37
                                                  6. Glued Cayley trees                                  14
                                               B. Fractals                                               16
                                                  1. Sierpinski Gaskets                                  16                           I. INTRODUCTION
                                               C. Statistical networks                                   18
                                                  1. Small-world networks                                18       Transport of mass, charge or energy is the basis of many
                                                  2. Erdös-Rényi networks                              19    physical, chemical or biological processes. Such transfer
                                                  3. Scale-free networks                                 20    mechanisms and their efficiency depend on the underlying
                                                  4. Apollonian networks                                 20    structure of the system, range from polymer physics to solid
                                                                                                               state physics to biological physics to even quantum compu-
                                            V. Extensions                                                21    tation, see Refs. [1–6] for reviews. The underlying structures
                                               A. Systems with long-range interactions                   21    could be, for example, simple crystals, as in solid state physics
                                               B. Systems with disorder and localization                 22    [7], more complex molecular aggregates like polymers [8], or
                                                                                                               general network structures [2].
                                           VI. Systems with absorption                                   23       In quantum mechanics, the potential a particle is moving
                                               A. Average survival probability                           24    in specifies the Hamiltonian of the system, which determines
                                               B. Regular networks                                       24    the time evolution. For instance, the dynamics of electrons in
                                                  1. Ring with traps                                     24    a simple crystal is described by the Bloch ansatz [7, 9, 10],
                                                                                                                                 2

which mirrors their behavior in metals quite accurately. Over         CTQW are also in close relation to the so-called quantum
the years these models have been refined and extended to ad-       graphs (QG), see, e.g., [34–37]. However, unlike CTQW,
dress different phenomena, such as the dynamics of atoms           QG take into account detailed properties of each bond of the
in optical lattices and the Anderson localization in systems       graph explicitly; in QG, bonds may be directed and have dis-
with energetic disorder [11]. In quantum chemistry, Hückel’s      tinct lengths. The connections between discrete Laplacians on
molecular-orbital theory allows to define a Hamiltonian for        discrete QG and periodic orbits were recently investigated by
more complex structures, such as molecules [12]. This is also      Smilansky [38].
related to transport in polymers, where the connectivity of the
polymer plays a fundamental role in its dynamical and relax-
ational properties [13]. There, (classical) transport processes             B.   Experimental implementations of CTQW
can be modeled by continuous-time random walk (CTRW) ap-
proaches [5, 6, 8]. An important example is the motion of             Simple theoretical models have always been very useful
Frenkel excitons, whose high-temperature dynamics is often         for our understanding of physics. In quantum mechanics,
governed by a master equation with an appropriate (classical)      next to the harmonic oscillator, the particle in a box provides
transfer operator which determines the temporal evolution of       much insight into the quantum world (e.g. [39]). The problem
the system [14, 15]. CTRW have proven to be a very useful          of a quantum mechanical particle moving in an infinite box
and general tool in describing incoherent transport in various     has been reexamined in [40–42]: Remarkably, even this sim-
settings, ranging, for instance, from percolation on fractals      ple system shows complex but regular spacetime probability
[16] to electronic energy transfer in glassy systems [17, 18].     structures (so-called quantum carpets). In solid state physics
Also, anomalous diffusional behavior has been successfully         and quantum information theory, one of the most simple sys-
modeled by CTRW using suitable waiting time distributions          tems is associated with a particle moving in a regular periodic
[19, 20].                                                          potential.
                                                                      In recent years, arrangements close to ideal theoretical
                                                                   models have been tailored using, e.g., ultra-cold atoms in opti-
                     A.   Quantum Walks                            cal lattices, see [43] and references therein. For both quantum
                                                                   walk variants, experimental implementations have been pro-
   The tight-binding approximation used in sold state physics      posed, based on microwave cavities [44], on Rydberg atoms
as well as in Hückel’s theory is equivalent to the so-called      [45] or on ground state atoms [46] in optical lattices or in
quantum walks, which model purely coherent quantum dy-             optical cavities [47], or using the orbital angular momentum
namics of excitations on networks [4, 21–24]. What mat-            of photons [48]. Other experimental proposals connected to
ters is that the constituting elements (spins, atoms, molecules,   CTQW are based on waveguide arrays [49] or on structured
etc.) are of the same type, in the simplest cases acting as two-   clouds of Rydberg atoms [50].
level systems. Now, the extension of classical random walks
ideas to the quantum domain is not unique and allows vari-
ants, of which two types capture most of the interest: discrete-                  C. Transport in complex systems
time quantum (random) walks (introduced by Aharonov et al.,
using an additional internal “coin” degree of freedom [22]),          The range of systems where CTQW can be used to study
and continuous-time quantum walks (CTQW) (introduced by            transport is clearly not restricted to simple (symmetric) mod-
Farhi and Gutmann, where the connection to CTRW uses               els. In particular, CTQW have been proven to be very useful
the analogy between the quantum mechanical Hamiltonian             in describing the dynamics of excitations in various complex
and the classical transfer matrix [21]). Recently, Strauch has     systems, as will be shown throughout this review.
shown how these two versions are related [25]. Thus, CTQW             Since CTQW can be related to the tight-binding approxima-
and CTRW act as the two extreme cases of purely coherent           tion in solid state physics, CTQW are also related to chains of
and purely incoherent transport, respectively.                     coupled spin 1/2 particles. If all but one spins are prepared in
   In quantum information theory, quantum walks are used ex-       the same state, say, spin down, and a single spin in the spin
tensively as algorithmic tools for quantum computation [26].       up state, one can map this onto a chain of coupled two-level
Here, the most prominent examples are Shor’s algorithm [27]        systems with a single initial excitation at the node which is
and Grover’s algorithm [28]. The latter is a quantum algo-         identified with the spin up particle [24, 51, 52]. The essential
rithm for finding an item in an (unsorted) database of qubits.     dynamics is then equivalent to a CTQW on a linear network.
Such an algorithm can also be related to CTQW [29, 30]. The           However, also the dynamics in topological disordered sys-
idea of using computers built on quantum mechanical prin-          tems can be modeled by CTQW. Take for instance a gas of
ciples instead of classical computers goes back to Feynman,        highly excited ultra-cold Rydberg atoms. At ultra-low tem-
who already formulated an early version of quantum walks in        peratures the configuration of the atoms can be thought of as
1982 [31]. From a conceptual point of view, quantum walks          being frozen on the time-scale on which the following trans-
are closely related to quantum cellular automata, see, e.g.,       port process is taking place [53–55]: The dynamics is started
[32]. Using CTQW, the transfer of information in complex           by exciting one (or several) of the Rydberg atoms in a higher
systems was discussed by Christandl et al. in the context of       state which is resonantly coupled to a lower Rydberg state
perfect state transfer [33].                                       [45, 50]. Since essentially only two different Rydberg states
                                                                                                                                        3

are involved, one can map this again onto a network of cou-       stance, is given by
pled two-level systems.                                                         1                  0                     0
   Also biological systems share some properties of simple                        0                     1                       .
network models. Recent experiments on the light-harvesting               |1i =  .. ,         |2i =  .. ,   . . . , |N i =  ..    (2)
                                                                                  .                     .                       0
complexes of algae have renewed the interest in studying the                      0                     0                       1
dynamics of excitations in such systems [56, 57]. Here, an
initial excitation (a Frenkel exciton) is created by absorbing      Take as an example a ring-like network of N nodes, with
a solar photon. The exciton is then transfered along a net-       only nearest neighbor connections and |N + 1i ≡ |1i, then
work of (bacterio-) chlorophylls (BChl), the chromophores,        the matrix A reads:
to the reaction center, where the excitation energy is con-
                                                                                      2 −1 0 . . .     −1
                                                                                                         
verted into chemical energy. Now, the network of the BChls
can be considered to be static and stable with defined cou-                         −1 2 −1 0 . . . 0 
plings between the BChls, at all (even ambient) temperatures
                                                                                        .. .. .. ..    . 
                                                                                    0
                                                                                          .   .  .  . .. 
of interest. Moreover, the Frenkel exciton can be viewed as                   Aij =  .                                                (3)
                                                                                                          
                                                                                                          
                                                                                     .
a quasi particle moving along the network. Therefore, also                           .
                                                                                                          
                                                                                                          
here the transport can be modeled by CTQW, at least at (very)                                    −1 2 −1
                                                                                                         
low temperatures. The incoherent exciton transport in den-                            −1 0 . . .    −1 2
drimers can be efficiently modelled by random walks, see,
for instance, [58–61]. However, for certain systems there         Writing A in a quantum mechanical fashion using the projec-
is also experimental evidence for coherent interchromophore       tion operators |lihk|, leads to
transport processes [62, 63]. Recent investigations of biologi-                    X
cal light-harvesting systems range from the Fenna-Matthews-                  A=            2|lihl| − |l − 1ihl| − |l + 1ihl|           (4)
Olsen complex [56] to marine algae [57]. There have also                               l
been recent theoretical efforts to understand the coherent fea-
tures of exciton dynamics found in recent experiments, see,          Having now specified the network through the connectivity
e.g., [64–68].                                                    matrix A, one is interested in the dynamics over the network.
   Clearly, such biological systems cannot be thought of as be-   First, one distinguishes between purely classical, i.e., incoher-
ing isolated from their environment. Therefore, in these cases    ent dynamics and purely quantum-mechanical, i.e., coherent
the purely coherent description by CTQW is of limited value.      dynamics. The main question one wishes to answer is: What
However, it is also possible to extend the CTQW approach to       is the probability to be at node k after time t when starting at
take the coupling to the environment into account, which leads    node j? While here the focus is mainly on localized initial
to models related to quantum master equations [69], see also      conditions at a single node j, in general, the initial state can
Sec. VII B.                                                       be any distribution involving all the nodes.


   II.   DEFINITIONS AND TERMINOLOGY OF CTQW                                      B.       Transfer matrix for CTRW

                 A.   Connectivity of network                        We start by considering classical transport. Let the initial
                                                                  node be j, such that the initial state of the system is |ji, and
  Networks involved in the CTQW and CTRW dynamics are             denote the transition probability to go in time t from node j to
characterized by the form in which their sites are connected.     node k by pk,j (t). Therefore, the initial condition is hk|ji ≡
Starting point of a network is a collection of N nodes, which     pk,j (0) = δk,j , where δk,j = 1 for k = j and 0 otherwise.
are then joined by bonds, the connectivity matrix A mirroring     The state after time t is |j; ti, such that the overlap with node
the way in which the bonding occurs.                              k reads hk|j; ti ≡ pk,j (t).
  The N × N connectivity matrix A has the elements Akj ,             The dynamics resulting in the state |j; ti follows from the
where                                                             transition rates per unit time between two nodes. Those tran-
                                                                 sition rates are the elements of the so-called transfer matrix
               fj for k = j
                                                                 T , Tkj ≡ hk|T |ji, which is therefore related to the spatial
       Akj = −1 if k and j connected Akj = Ajk            (1)     gain or loss. One can now write the temporal change of the
                                                                  probability after time ǫ ≪ 1 as
               
               0      else,

where fj is the number of bonds emanating from node j. This                 pk,j (ǫ) = pk,j (0) + ǫTkj = δk,j + ǫTkj .                 (5)
matrix has interesting and useful properties: (a) A is real and
symmetric, (b) all its eigenvalues λn are real and λn ≥ 0, and    Assuming a Markovian process, the following master equa-
(c) A has a single smallest eigenvalue which is λ1 = 0.           tion can be shown to hold [5, 6]:
   One can associate with every node of the network a ba-
sis vector in an N -dimensional vector space. Now, these ba-                          d             X
                                                                                         pk,j (t) =   Tkl pl,j (t).                    (6)
sis vectors form a complete orthonormal basis, which, for in-                         dt
                                                                                                        l
                                                                                                                                     4

This equation defines the CTRW, which (depending on the               extremes of transport on the same topology. On the one hand
specific form of the transfer matrix) have been applied to var-       there is the purely incoherent CTRW, while on the other hand,
ious problems in physics, chemistry, biology, and also social         there is Schrödinger’s equation which now defines CTQW.
sciences.                                                             Assuming again that all transition rates between different con-
   In the simplest case, where the rates for all bonds are equal,     nected nodes are the same, the Hamiltonian can be directly
say, γ, the transfer matrix is related to the connectivity matrix     related to the connectivity, H = γA. Therefore, the underly-
through T = −γA. Then the master equation describes a                 ing topological network is determined both for CTRW and for
diffusive motion over the network.                                    CTQW by the connectivity matrix A. This allows to study the
   The formal solution of Eq.(6) is pk,j (t) = hk|eT t |ji =          role of the connectivity in parallel for CTRW and for CTQW.
hk|e−γAt |ji. Denoting the eigenstates of A by |qn i, one has            Let us donote the eigenvalues of H by En and the eigen-
                                 X                                    states of H by |Ψn i. Evidently, the eigenvalues and eigen-
     pk,j (t) = hk|e−γAt |ji =       e−λn γt hk|qn ihqn |ji.  (7)     states of H and T are practically the same; nonetheless, we
                                 n                                    will keep the distinction between H and T due to later pur-
                                                                      poses. Now, the quantum-mechanical transition probabilities
Since the eigenvalues are positive (λn > 0 for n > 1 and              read
λ1 = 0), the long-time limit follows directly: For t ≫ 1
in the sum of Eq.(7) all exponential terms but one decay                                      X                          2
quickly to zero. The only term which survives is the one                         πk,j (t) =        e−iEn t hk|Ψn ihΨn |ji .       (10)
                                                        P for                                  n
λ1 = 0, with the corresponding eigenstate |q1 i = N1        l |li.
Therefore, the long-time limit of all transition probabilities is     Unlike the situation for CTRW, for CTQW there is no unique
limt→∞ pk,j (t) = 1/N , which is independent of the connec-           long-time limit of πk,j (t) due to the unitary time evolution. In
tivity of the network. This means that every CTRW whose               order to compare to the long-time behavior of the CTRW one
transfer matrix follows directly from the connectivity matrix         uses the long time average [70, 71]
will eventually decay at long times to the equipartition value
1/N , a fact which is sometimes referred to as “ground state                              1 T
                                                                                             Z
dominance”.                                                                  χk,j ≡ lim          dt πk,j (t)
                                                                                    T →∞ T 0
                                                                               X
                                                                             =     δEn ,Em hk|Ψn ihΨn |jihj|Ψm ihΨm |ki,          (11)
                  C.   Hamiltonian for CTQW                                     n,m


   Turning now to the quantum-mechanical dynamics, one                where δEn ,Em = 1 if En = Em and 0 otherwise. The long-
faces the fact that the transport has to be formulated in Hilbert     time average χk,j still depends on the initial and final nodes j
space. For this one assumes that the states |ji representing the      and k.
nodes span the whole accessible Hilbert space. As before, it
is assumed that Pthe states are orthonormal and complete, i.e.,
hk|ji = δk,j , j |jihj| = 1. The dynamics is then governed                             D. Example: A discrete ring
by a specific Hamiltonian H, such that Schrödinger’s equa-
tion for the transition amplitudes αk,j (t) ≡ hk|j; ti reads             As an example which illustrates the differences and sim-
                                                                      ilarities between CTQW and CTRW we consider a discrete
               d                X
                                                                      ring of N nodes, whose connectivity matrix is given above
                  αk,j (t) = −i   Hk,l αl,j (t).               (8)
               dt                                                     in Eq.(3). This one-dimensional structure with the periodic
                                   l
                                                                      boundary conditions |N + 1i = |1i allows for a full analyti-
Similar to the CTRW, the formal solution for the transition           cal solution. When realizing that the matrix A is nothing but
amplitudes is given by                                                a tight-binding matrix for a particle moving in a regular one-
                                                                      dimensional crystal, one readily obtains the eigenvalues and
                    αk,j (t) = hk|e−iHt |ji,                   (9)    eigenstates from a Bloch ansatz [7, 10]. Namely, the Bloch
                                                                      states are linear combinations of the localized states |ji and
where e−iHt is the quantum-mechanical time-evolution oper-            are given by
ator. The transition probabilities follow as usual as πk,j (t) ≡
|αk,j (t)|2 .                                                                                           N
   Comparing Eq.(8) to Eq.(6) one immediatly notices the                                         1 X −iθj
                                                                                        |Ψθ i = √      e  |ji.                    (12)
very similar structure of the two equations, except for the                                      N j=1
imaginary unit i appearing in Eq.(8). However, while Eq.(6)
is an equation for the transition probabilities pk,j (t), Eq.(8) is   Now the energy is obtained as
an equation for the transition amplitudes αk,j (t).
   One can push the similarities further by identifying the                                   Eθ = 2 − 2 cos θ.                   (13)
quantum-mechanical Hamiltonian H with the classical trans-
fer matrix T , i.e., H ≡ −T . This approach, pioneered by             For small θ the energy is given by Eθ ≈ θ2 which resembles
Farhi and Gutmann in Ref. [21], allows to compare the two             the energy spectrum of a free particle.
                                                                                                                                                                              5

   By inverting Eq.(12) one may describe the state |ji local-                    (a) N=21                                       (a) N=20
                                                                                                      0                                                         0
ized at node j as a Wannier state [7, 10]
                           1 X iθj
                    |ji = √    e |Ψθ i.                     (14)                                      20                                                       20
                           N θ

Since the states |ji span the whole accessible Hilbert space,                                         40                                                       40

one has hk|ji = δkj and, via Eq.(12), also hΨθ′ |Φθ i = δθ′ θ .
Then the transition amplitude reads [72]
                     1 X                       ′
                                                                                                      60
                                                                                                           time t                                              60
                                                                                                                                                                     time t
        αkj (t) =         hΨθ′ |e−iθk e−iHt eiθ j |Ψθ i
                     N
                        θ,θ
                        ′
                                                                                                      80                                                       80
                   1 X −iEθ t −iθ(k−j)
                 =    e      e         .                    (15)
                   N
                         θ
                                                                                                  100                                                          100

In an analogous way one obtains the classical transition prob-
abilities [72]
                                                                                                  120                                                          120
                          1 X −λθ t −iθ(k−j)
               pk,j (t) =    e     e         ,              (16)             5     10
                                                                                   node k
                                                                                            15   20                 2   4   6    8    10
                                                                                                                                     node k
                                                                                                                                           12   14   16   18   20

                          N
                              θ
                                                                    FIG. 1: Contour plot of the probability for a CTQW on a circle of
because the Bloch states are also the eigenstates |qn i.            length (a) N = 21 and (b) N = 20 over long times t. Dark regions
  The periodic boundary condition for a 1d lattice of size N        denote high probabilities. From [72].
requires that θ = 2nπ/N with n ∈]0, N ]. Now Eq.(15) is
given by
                                                                    seen after a time t ≈ N/2. The first revival time has to
               e−i2t X i2t cos(2nπ/N ) −i2πn(k−j)/N
   αjk (t) =          e               e             .       (17)    be larger than this, because there cannot be any revival un-
                N n                                                 less the wave reaches its starting node again. Our calcula-
                                                                    tions [72] suggest that the first revival time will be of order
For small θ, this is directly related to the results obtained for   τ0 . From Fig. 1 one sees that the first (incomplete) revival oc-
a quantum particle in a box [40–42], because then En ∼ n2 .         curs for N = 20 at t ≈ 70 > 202 /2π and for N = 21 at
Indeed, some features found for the particle in a box can also      t ≈ 75 > 212 /2π.
be found in the case of a CTQW on a discrete ring. For the             Since the transition probabilities are easily obtained from
particle in a box the initial condition is restored after some      the Bloch ansatz, also the long-time averages can be estimated
revival time. In fact the probability to find the particle at a     analytically. Depending on the number of nodes in the net-
certain position in the box is a periodic function.                 work, the long-time averages are, [72], for even N :
   Analogously but not completely similarily, for the CTQW
on the ring, the initial (localized) condition is only partially
                                                                                      (
                                                                                        1/N 2 k 6= j
restored. Only small rings of sizes N = 1, 2, 3, 4, and 6                     χk,j =                                            (19)
lead to a full revival of the initial condition. All other sizes                        1/2N k = j and k = j + N/2
only lead to partial revivals. The revival time τ is given by
αk,j (τ ) = αk,j (0). Since the transition amplitudes are given     and for odd N :
as a sum over all modes n, see Eq.(17), one has for each mode                                  (
n its revival time [72]                                                                         1/N 2                       k 6= j
                                                                                        χk,j =                                                                            (20)
                                                                                                1/N                         k=j
                        rπ
                 τn =      [1 + cot2 (nπ/N )],              (18)
                         2                                          Thus, unlike in the classical CTRW case the long-time average
where r ∈ N (without any loss of generality one sets r = 1).        is not equipartitioned but “remembers” the initial condition.
From Eq.(18) one finds that τn > τn+1 for n ∈]0, N/2] and           Moreover, also the symmetry arising from the even or odd
τn < τn+1 for n ∈]N/2, N ]. For certain values of n, τn will        number N of nodes is reflected in the χk,j .
be of order unity, e.g. for n = N/2 τn = π/2. However, for
n << N , Eq.(18) yields τn = N 2 /2πn2 ≡ τ0 /n2 , which is
analogous to the particle in the box and where τ0 is a universal             III. EFFICIENCY OF CTQW AND CTRW
revival time.
   Because the revival times τn have large variations in value,        The performance of CTQW and CTRW depends to a large
one compares these times to the actual time needed by the           extent on the connectivity of the underlying network, i.e., on
CTQW for travelling through the lattice. As mentioned ear-          its topology. One focuses on the return probabilities πj,j (t)
lier, interference effects in the return probability π1,1 (t) are   and pj,j (t). Now, if these probabilities decay quickly with
                                                                                                                                    6

time, the probabilities 1 − πj,j (t) and 1 − pj,j (t), to be at any      As already discussed, for CTRW the long-time limit of the
but the initial node, increase quickly. This implies a fast trans-    transition probabilies reaches the equipartition value 1/N . In
port through the network. In order to make a global statement         the same way, the long-time limit of p(t) is given by 1/N . In
on the performance, one considers the average return proba-           contrast, for CTQW neither π(t) nor |α(t)|2 decay to a given
bilities [73]                                                         value at long times, but rather oscillate around the correspon-
                                                                      nding long-time average which for π̄(t) is given by [74]
                            1 X
            π(t) ≡              πj,j (t)      for CTQW        (21)
                            N j                                                           1 T
                                                                                            Z
                                                                                χ̄ ≡ lim        dt π̄(t)
                                                                                     T →∞ T 0
and                                                                                   1 X
                                                                                   =       δλ ,λ |hj|ψn i|2 |hj|ψm i|2 .         (26)
                    1 X                                                              N n,m n m
             p(t) ≡     pj,j (t)              for CTRW.       (22)
                    N j
                                                                      Again, on can obtain a lower bound which does not depend on
                                                                      the eigenvectors [74]:
Again, a quick decay of π(t) [p(t)] implies a fast propaga-
tion through the network, while a slow decay implies a slow                                     1 X
propagation.                                                                            χ̄ ≥          δλ ,λ ≡ χ̄lb .             (27)
                                                                                               N 2 n,m n m
   For CTRW the average return probabilities simplify consid-
erably; one has namely
                      1 X −λn t       X                                                            A. Examples
          p(t) =          e     hΨn |   |jihj|Ψn i
                      N n             j
                                                                         The difference in the global efficiencies of CTQW and
                      1 X −λn t                                       CTRW is illustrated by considering two distinct examples: the
                    =     e     ,                             (23)
                      N n                                             discrete ring of N nodes and the star with one core node and
                                                                      N − 1 nodes attached to it, see Fig. 2.
which only depends on the eigenvalues λn of the transfer                 The eigenvalues (and also eigenstates) of the discrete ring
matrix T but not on its eigenstates. By making use of the             have already been discussed. From these results it is straight-
Cauchy-Schwarz inequality one gets a similar expression for           forward to calculate the average return probabilities. Since the
CTQW. The average return probabily π(t) is related to the av-         ring’s eigenstates are Bloch states, one can easily verify that
erage return amplitude α(t) by [73]                                   the lower bound |α(t)|2 is exact, i.e., in this case also π(t)
                                                                      does not depend on the eigenstates. Therefore, the average
                             1 X          2
             π(t) =              αj,j (t)                             return probabilities are given by [73]
                             N j
                                                                                         N
                              1 X         2                                         1 X                             2
                        ≥         αj,j (t) ≡ |α(t)|2 .        (24)         π(t) =         exp[−i2t(1 − cos(2πn/N ))              (28)
                              N j                                                   N n=1

                                                                      for CTQW and
Similar to p(t) for CTRW, |α(t)|2 only depends on the eigen-
values En of the Hamiltonian H:                                                         1 X
                                                                                              N
                                                                               p(t) =         exp[−2t(1 − cos(2πn/N ))]          (29)
                2       1 X −iEn t       X            2                                 N n=1
       |α(t)|       =       e      hΨn |   |jihj|Ψn i
                        N n              j
                                                                      for CTRW. In the limit of large N , i.e., for continuous θ =
                        1 X −iEn t 2                                  2πn/N , one can replace the sums by integrals which leads to
                    =       e        .                        (25)
                        N n                                                                 Z
                                                                                   pγ (t) = dE ρ(E) exp(−Et),                  (30)
Having a quantity which only requires the calculation of the
eigenvalues considerably shortens the computation time, es-
                                                                      and to
pecially for very large systems.
   Clearly, due to the oscillating terms in Eq.(25), the lower                                                         2
                                                                                               Z
bound |α(t)|2 will oscillate in most cases. Thus, to compare                      π γ (t) =         dE ρ(E) exp(−iEt) ,          (31)
to the decay of the classical p(t) one uses the envelope of
|α(t)|2 . Note that when one identifies the Hamiltonian of the        where ρ(E) is the density of states (DOS). Then one obtains
CTQW with the transfer matrix of the CTRW, the eigenvalues            for CTQW π(t) ∼ |J0 (2t)|2 , which for t ≫ 1 can be ap-
of both are the same, i.e., En = λn . Thus, formally the differ-      proximated by π(t) ∼ sin2 (2t + π/4)/t [75]. Since the max-
ence in dynamics is only due to the different functional form         imum of the sine function is 1, the envelope of π(t) decays
of Eq.(23) and Eq.(25). Nonetheless, this can lead to drastic         as t−1 . For CTRW there is only a single sum and no ad-
effects.                                                              ditional quadrature, such that a similar calculation leads to
                                                                                                                                                                               7

p(t) ∼ t−1/2 . This temporal decay will also be present for
finite systems. The time-range over which it will be visible
depends on the value of N . Obviously, for small N the long-
time behavior will be reached faster than for larger N .
   Thus, we just established that for CTQW on a ring the ex-
ponent of the decay power-law is twice as large as the one for
CTRW. This fact holds for a wide class of systems. Namely,
                                                 PN
all networks whose density of states ρ(E) ≡ N1 n=1 δ(E −
En ) follows a power-law, ρ(E) ∼ (EEm − E 2 )ν , will show
this feature. Here, Em is the maximal eigenvalue (one as-                                                    FIG. 2: Star with N − 1 = 12 arms.
sumes the minimum eigenvalue to be zero). Since the in-
terest is in the large t behavior, p(t) will be mainly deter-         (a) Ring with N=1000
mined by the small eigenvalues, such that for t ≫ 1 one has                                        0                                                                 2
                                                                                              10                                                            |α(t)|
ρ(E) ∼ E ν . It is straighforward to show that for CTRW                                                                                                        -1
                                                                                                                                                            ~t
                                   −(1+ν)                                                          -1                                                       p(t)
                        p(t) ∼ t             .               (32)     2                       10
                                                                                                                                                               -1/2



                                                                           p(t) ; |α(t)|
                                                                                                                                                            ~t
This scaling feature at not too short times is well known, see,                                    -2
                                                                                              10
e.g., [76], where 2(1 + ν) ≡ ds is sometimes called the spec-
tral or fracton dimension. For CTQW, also |α(t)|2 will be in                                       -3
general determined by the small eigenvalues. For ρ(E) ∼ E ν                                   10
one obtains |α(t)| = p(t). Here, all quantum mechanical os-                                    -4
cillations vanish, because one considers only the leading term                                10             0      1           2        3         4    5                6
                                                                                                        10        10        10         10     10       10             10
of the DOS. Therefore, the envelope of the lower bound for                                                                          time t
CTQW scales as [73]                                                   (b) Star with N=51
                              2        −2(1+ν)                                                     0
                   env[|α(t)| ] ∼ t              .           (33)                             10
                                                                                                                                        1.0




                                                                       p(t) ; |α(t)| ; π(t)
   In other cases of interest (e.g., stars, see below) the DOS has
highly degenerate eigenvalues [74]. As an extreme case there          2
                                                                                                                  |α(t)|
                                                                                                                        2
                                                                                                                                        0.9
may exist a single eigenvalue El , whose degeneracy, Dl , is of                               10
                                                                                                   -1             π(t)
the order O(N ), whereas all others are of the order O(1) or                                                      p(t)
less. By writing
                  "                                     #
                1                    X
                                                                                              10
                                                                                                   -2
       α(t) =       Dl e−iEl t +             Dn e−iEn t       (34)                                 10
                                                                                                        -1                  0
                                                                                                                           10
                                                                                                                                               1
                                                                                                                                              10                      10
                                                                                                                                                                           2
               N
                                   En 6=El                                                                                          time t
                                   2
one obtains, up to order O(1/N ) [74]:
                 (                                 )                 FIG. 3: (Colour on-line). Panel (a): p(t) and |α(t)|2 with the
        2    Dl           X                                          appropriate scaling t−1/2 and t−1 , respectively, for a ring of size
  |α(t)| ≈ 2 Dl +             Dn 2 cos[(El − En )t] . (35)           N = 1000. Panel (b): p(t), π(t), and |α(t)|2 for a star with N = 51
             N
                         En 6=El                                     nodes. The inset shows a close-up of π(t) and |α(t)|2 in the same
                                                                     time interval. From [74].
The first term on the right-hand side of eq. (35) is of order
O(1), while the second term is of order O(1/N ). There-
fore, for few highly degenerate eigenvalues, the lower bound
       2                                                             Obviously, only the term |(N − 2) exp(−it)|2 /N 2 = (N −
|α(t)| will not show a decay to values which fluctuate about         2)2 /N 2 in Eq. (37) is of order O(1). All the other terms are of
1/N but will rather fluctuate around 1 − 1/N at all times.           order O(1/N ) or O(1/N 2 ) and, therefore, cause only small
Also, π(t) will not decay but will fluctuate around the same         oscillations (fluctuating terms) around or negligible shifts
                    2
value, since |α(t)| is a lower bound.                                (constant terms) from (N − 2)2 /N 2 ≈ 1 − 1/N .
   An example of a system with a single highly degenerate               Figure 3 shows the temporal behavior of π(t), |α(t)|2 , and
eigenvalue is the star, having one core node and N − 1 nodes         p(t) for a ring (uppper panel) and for a star (lower panel). The
directly connected to the core but not to each other, see Fig. 2.    difference, especially for CTQW, is dramatic. While in both
The eigenvalue spectrum has a very simple structure. There           cases the CTRW decay to the equipartition value 1/N , this is
are 3 distinct eigenvalues, namely E1 = 0, E2 = 1, and E3 =          not so for the CTQW. For the ring |α(t)|2 (thus also π(t)) fol-
N , with degeneracies D1 = 1, D2 = N − 2, and D3 = 1,                lows the t−1 decay at intermediate times and oscillates around
respectively. Therefore, one gets [74]                               the long-time average at long times. For the star, on the other
                   1 h                             i                 hand, there is no decay for both |α(t)|2 and π(t). There are
         p(t) =        1 + (N − 2)e−t + e−(N −2)t           (36)     only some oscillations around the value 1 − 1/N .
                  N
                   1                                   2                In the two examples above the efficiencies of the two pro-
     |α(t)|2 =       2
                        1 + (N − 2)e−it + e−i(N −2)t . (37)          cesses are vastly different. For the ring there is a considerable
                  N
                                                                                                                                       8

                                                                                 (1,1)                              (N,1)
                                                                          node 1




                                  g=1   g=2   g=3
                                                                                                      (j x ,j y )
                                                                                                                                2
                                                                                                                       node N
                                                                                 (1,N)                              (N,N)


                                                                  FIG. 5: Sketch of a square network arranged as a regular lattice with
                                                                  the appropriate numbering of the nodes. Note that the actual geomet-
 P 4: Spidernet graph of generation g = 3 with N = 53 = 1 +
FIG.                                                              rical realization can be much more flexible, see text for details. From
4 gk=1 3k−1 nodes.                                                [71].


increase in efficiency for CTQW, because for it the probabil-     tries observed in 1d are not always observed in 2d [71].
ity to return to the origin decays much faster than for CTRW.        Consider now 2d regular structures of side length N , thus,
The contrary is true for the star. Here, the CTRW still decay     they contain N 2 nodes giving rise to N 2 basis states [71]. In
while the CTQW remain close to unity. This implies that the       a pair notation one sets |ji = |jx , jy i, where jx and jy are
probability to visit other places than the initial node is - on   integer labels in the two directions, with jx , jy ∈ [1, N ], see
average - very low. Note that π(t), |α(t)|2 , and p(t) are av-    Fig.5. This labeling of the states is not to be confused with the
eraged over all nodes of the network. For the ring all nodes      labeling of the adjacency matrix. Note that capital bold letters
are equivalent, but the star has the core node which stands       denote matrices, while small bold letters denote the nodes and
out from the rest. Therefore, the temporal evolution is very      the states.
different when the CTQW starts at the core or at one of the          The focus in solid state physics is on systems where Born
peripheral nodes. When starting at the core, due to the rota-     - von Karman periodic boundary conditions (PBC) are as-
tional symmetry of the network, the walk can be mapped into       sumed. Now, for an internal site of the network (not on
a walk involving only two nodes. When starting at the periph-     an edge or in a corner), the Hamiltonian acting on a state
ery, there is no such simple mapping. Since all but one node      |ji = |jx , jy i reads
are at the periphery, they lead to the poor performance of the        H|jx , jy i = 2|jx , jy i − |jx + 1, jy i − |jx − 1, jy i
CTQW when compared to the CTRW.
   Salimi studied the situation over the semi-regular spider-                     + 2|jx , jy i − |jx , jy + 1i − |jx , jy − 1i.
net graph [77]. This graph is build in a hierarchical, radially                                                                 (38)
symmetric manner, i.e., one starts from a single core node and
                                                                  PBC extend this equation to all the sites of the network by
builds up the network generation after generation, as indicated
                                                                  interpreting every integer jx and jy to be taken modulus N .
in Fig. 4. The procedure used [73, 74, 77] also leads to power-
                                                                  With this generalization, the time independent SE
law behaviors for both CTQW and CTRW [77]. When one
starts at the core node, one can map the dynamics onto a line,                            H|Ψθ i = Eθ |Ψθ i                         (39)
where all the states corresponding to the nodes belonging to
the same generation are summed up to form a new state, rep-       admits (similar to the 1d case) the following Bloch eigenstates
resenting this generation. Salimi showed that in this case the                                     N
return to the origin (core node) follows a power-law which for                                1 X −i(θ·j)
                                                                                    |Ψθ i =             e |ji.                      (40)
CTRW goes as t−3/2 while for CTQW it goes as t−3 . There-                                     N j ,j =1
                                                                                                  x   y
fore, a behavior similar to that discussed around Eqs. (32) and
(33) is also found here, since the exponent of the CTQW de-       as solutions, where θ · j stands for the scalar product with
cay is twice as large as the exponent of the CTRW decay.          θ = (θx , θy ). The usual Bloch relation can be obtained by
                                                                  projecting |Ψθ i on the state |ji such that Ψθ (j) ≡ hj|Ψθ i =
                                                                  e−i(θ·j) /N , thus Ψθ (jx + 1, jy + 1) = e−i(θx +θy ) Ψθ (jx , jy ).
                  IV. CTQW ON NETWORKS                            The PBC restrict the allowed values of θ. In the present case
                                                                  [71] (side length N ), the PBC require that Ψθ (N + 1, jy ) =
                  A.   Deterministic networks                     Ψθ (1, jy ) and Ψθ (jx , N + 1) = Ψθ (jx , 1). It follows that
                                                                  one must have θx = 2nπ/N and θy = 2lπ/N , where n
             1.   Two dimensional regular networks
                                                                  and l are integers and n, l ∈ [1, N ]. It is now a simple mat-
                                                                  P to verify that the |Ψθ i also obey hΨθ |Ψθ ′ i = δθ,θ ′ and
                                                                  ter
                                                                     θ |Ψθ ihΨθ | = 1.
   CTQW on regular 2d structures carry over many of the              Furthermore, from Eqs.(39) and (40) the energy is obtained
properties of their 1d counterparts, since 2d regular networks    as
ca be envisaged to be the direct product of two 2d structures,
vide infra. However, some care is in order, since the symme-               Eθ = 4 − 2 cos θx − 2 cos θy = Eθx + Eθy ,               (41)
                                                                                                                                                                                                                                                                       9

                                                                                   χk,c                                                                                    χk,c
with Eθx = 2 − 2 cos θx and Eθy = 2 − 2 cos θy . Under                             0.12                              (a) N=5
                                                                                                                          (a)                                               0.02
                                                                                                                                                                                                                                  (b) (b)
                                                                                                                                                                                                                                     N=14
PBC the two-dimensional eigenvalue problem separates into
two one-dimensional problems.                                                      0.06                                                                                     0.01


   The transition amplitude at time t from state |ji to state |ki                     0
                                                                                                                                                                  5
                                                                                                                                                                                  0                                                                               12
                                                                                                                                                                                                                                                                       14
                                                                                                                                                         4                                                                                                   10
is now, using Eq.(40) twice, [71]:                                                        1
                                                                                                  2
                                                                                                                                                    3                                         2       4                                              6
                                                                                                                                                                                                                                                         8
                                                                                                            3
                                                                                                                     4
                                                                                                                                        2                    ky                                                6        8    10             2
                                                                                                                                                                                                                                                4             ky
                                                                                              kx                              5 1                                                                     kx                          12   14

                1 X              ′                                                 χk,c                                                                                    χk,c
    αk,j (t) =   2
                     hΨθ ′ |e−i(θ ·k) e−iHt ei(θ·j) |Ψθ i                          0.008                                 (c) (c)
                                                                                                                            N=23                                            0.002                                                      (d) (d)
                                                                                                                                                                                                                                           N=47
               N   ′    θ,θ
                                                                                   0.004                                                                                    0.001
                    1 X −iEθ t −iθ·(k−j)
                =      e      e                                             (42)
                    N2                                                                    0                                                                       20                  0                                                                                40
                         θ                                                                    5                                                     10
                                                                                                                                                         15
                                                                                                                                                                                                      10                                                 20
                                                                                                                                                                                                                                                              30
                                                                                                           10
                                                                                                                    15                      5                ky                                                    20
                                                                                                                                                                                                                             30                     10             ky
                                                                                              kx                             20                                                                            kx                      40
In the limit N → ∞, the sums in Eq.(42) may be changed to
integrals; by making use of Eq.(41) one obtains
                                                                                   FIG. 6: LPs χk,c to be at node k when starting at the corner node
                                   Zπ                                              c = (1, 1) for networks of sizes (a) N = 5, (b) N = 14, (c) N = 23,
                         e−i4t                                                     and (d) N = 47. From [71].
     lim αk,j (t) =                     dθx e−iθx (kx −jx ) ei2t cos θx
   N →∞                   4π 2
                                   −π                                               χk,c                                                                                   χk,c
                              Zπ                                                    0.1                              (a) N=6
                                                                                                                         (a)                                               0.02
                                                                                                                                                                                                                                  (b) N=15
                                                                                                                                                                                                                                       (b)
                                           −iθy (ky −jy ) i2t cos θy
                         ×         dθy e                 e             ,           0.05                                                                                    0.01

                             −π
                                                                                                                                                                      6                                                                                                14
                                                                                     0                                                                        5              0                                                                                    12
                                                                            (43)          1
                                                                                              2                                                 3
                                                                                                                                                         4                                2       4        6                                         6
                                                                                                                                                                                                                                                         8
                                                                                                                                                                                                                                                             10
                                                                                                       3                                2                                                                           8                           4
                                                                                                                4
                                                                                                  kx                     5
                                                                                                                                  6 1
                                                                                                                                                             ky                                            kx
                                                                                                                                                                                                                            10 12
                                                                                                                                                                                                                                  14        2                 ky
such that                                                                          χk,c                                                                                    χk,c
                                                                                   0.008                                 (c) (c)
                                                                                                                             N=24                                          0.002                                                       (d)(d)
                                                                                                                                                                                                                                           N=48
   lim αk,j (t) = ikx −jx iky −jy e−i4t Jkx −jx (2t)Jky −jy (2t)                   0.004
  N →∞                                                                                                                                                                     0.001

                                                             (44)
where Jn (x) is the Bessel function of the first kind [78]. Thus,                         0
                                                                                              5                                                         10
                                                                                                                                                             15
                                                                                                                                                                      20      0
                                                                                                                                                                                                  10                                                 20
                                                                                                                                                                                                                                                             30
                                                                                                                                                                                                                                                                  40

                                                                                                           10                                                                                                  20                                              ky
on a network topologically equivalent to a square lattice with                                        kx
                                                                                                                    15
                                                                                                                             20
                                                                                                                                                5                 ky                                      kx
                                                                                                                                                                                                                            30
                                                                                                                                                                                                                                  40
                                                                                                                                                                                                                                                10


PBC the transition amplitude between the nodes j and k is
given by                                                                           FIG. 7: LPs χk,c to be at node k when starting at the corner node
                                                                                   c = (1, 1) for networks of sizes (a) N = 6, (b) N = 15, (c) N = 24,
             lim πk,j (t) = [Jkx −jx (2t)Jky −jy (2t)]2 .                   (45)   and (d) N = 48. One may note the asymmetries by comparing to
            N →∞
                                                                                   Fig.6. From [71].
   Now, for finite networks the long-time average χk,j gives
more insight into the dynamics for different network sizes N .
In the 2d case one has [71]                                                           When starting at a corner node c = (1, 1), one often
                                                                                   finds that the LPs for the starting node and its “mirror” node
                  ZT                                 2
                                                                                   oc = (N, N ) are equal. Figure 6 shows the χk,c obtained by
                1          X
                                   −iHt
    χk,j = lim        dt      hk|e      |qn ihqn |ji                               going from the corner node c = (1, 1) to the other nodes for
           T →∞ T
                   0        n                                                      networks of sizes N = 5, N = 14, N = 23, and N = 47.
                                                                                      However, for some particular network sizes the distribu-
           X
         =    hk|qn ihqn |jihj|qm ihqm |ki
              n,m
                                                                                   tions of the LPs turn out to be asymmetric. For instance, for a
                                                                                   network of size N = 15 the LP χoc,c for the CTQW starting
                         ZT
                                              
                       1         −i(λ  −λ  )γt
                                                                                   at node c to be at the opposite corner node oc is less than the
            ×  lim         dt e     n   m                                (46a)   LP χc,c to be at the initial node. The same is true for the nodes
               T →∞ T
                         0                                                         along the edges of the network. Figure 7 shows that such
                                                                                   asymmetries occur for networks of sizes N = 6, N = 15,
              X
            =     δλn ,λm hk|qn ihqn |jihj|qm ihqm |ki.                    (46b)
              n,m
                                                                                   N = 24, and N = 48 (the asymmetries are best seen by look-
                                                                                   ing at χc,c and χoc,c ). The smallest network where asymme-
One notes that the integral in Eq.(46a) equals 1 if λn = λm                        tries in the distribution of the LPs are detected has N = 6. The
and 0 otherwise, i.e., it equals δλn ,λm . Given that some eigen-                  next ones are found for N = 12, 15, 18, 21, 24, 30, 36, · · ·.
values of H are degenerate, the sum in Eq.(46b) can contain                           An asymmetric LP distribution is particularly evident in the
terms belonging to different eigenstates |qn i and |qm i. Equa-                    difference between χc,c and χoc,c . Thus, as an overview
tion (46b) provides a numerically very efficient way of com-                       Fig.8 presents as a function of N a plot of the (χc,c −
puting the χk,j . Remarkably, one finds that the χk,j depend                       χoc,c )N 2 values obtained. Note that all N values in Fig.8
in an unexpected way on the exact value of the size N of the                       for which (χc,c − χoc,c ) 6= 0 are divisible by 3. However, the
finite network under study.                                                        converse is not true, one finds symmetric LP distributions for
                                                                                                                                             10

                                                                                 (a) Rectangle MxN with N=15




FIG. 8: Differences between the LPs for CTQW that start at c =                   (b) Cylinder MxN with N = 15
(1, 1) to be at c, χc,c , or to be at its “mirror” node oc = (N, N ),
χoc,c , as a function of the network size N , for 1 ≤ N ≤ 60. From
[71].




the networks with N = 3, 9, 27, 33, 39, · · · .

   The above effect is also observed for non-square networks,
where the number of nodes in the two directions are not equal
[79]. While for periodic boundary conditions in both direc-                      (c) Cylinder MxN with M=15
tions there is no asymmetry, there are observable asymmetries
both for periodic and for open boundary conditions in only
one direction as well as for open boundary conditions in both
directions.

   One now fixes N to be N = 15 and varies M , taking
4 ≤ M ≤ 30. Figure 9(a) shows for rectangles the differ-
ence between the LPs on the initial corner χc,c and on the
corner χoc,c . In the analysed range, 4 ≤ M ≤ 30, the value
χc,c − χoc,c displays varying patterns. For 4 ≤ M ≤ 13                  FIG. 9: (a) Rectangles M × N with N = 15 and varying M : Differ-
one can associate χc,c − χoc,c = 0 to odd values of M and               ences between the LPs for CTQW that start at c = (1, 1) to be at c,
χc,c − χoc,c 6= 0 to even values of M ; for larger M the                χc,c , and to be at oc = (M, N ), χoc,c . (b) Cylinders M × N with
situation becomes more complex. Figure 9(b) displays the sit-           N = 15 and varying M : Differences between the LPs for CTQW
uation for cylinders with N = 15 and 4 ≤ M ≤ 30. Here the               that start at c = (1, 1) to be at c, and to be at the node cy = (1, N ).
plot shows χc,c − χcy ,c , with cy ≡ (1, N ). Figure 9(c) shows         (c) Cylinders M × N with M = 15 and varying N : Differences
                                                                        between the LPs for CTQW that start at c = (1, 1) to be at c, and to
the situation for cylinders with M = 15 and 4 ≤ N ≤ 30.
                                                                        be at the node cy = (1, N ). From [79].
This last case looks quite regular, with non-vanishing values
only for N = 10, 15, and 30. Hence, Figs. 9(b) and 9(c)
(N < M ) show for cylinders that changes in radius lead to
                                                                        Now, according to Eq. (46a), the LPs are given by [79]
more asymmetric situations than changes in length.
                                                                                                    Z T
                                                                                           1
   An indication of the origin of the asymmetries is obtained                  χk,j = lim                    dt πkx ,jx (t) πky ,jy (t)
                                                                                      T →∞ T             0
by briefly reviewing some of the details of the calculations of                                                           Z T
the LPs. Since the Hamiltonian of the problem separates in the                           X                     1
two directions, it is easy to show that the transition probabili-                   =                 Fk,j lim                  dt
                                                                                                          T →∞ T           0
                                                                                          θx ,θx
                                                                                               ′ ,θ ,θ
                                                                                                    ′
ties πk,j (t) can be written as the product of the two separate                                h
                                                                                                   y y
                                                                                                                             i
probabilities for each direction [79], i.e.                                               × exp −it(λθx − λθx′ + λθy − λθy′ ) ,
                                                                                                                                           (48)

             πk,j (t) = πkx ,jx (t) πky ,jy (t)                         where Fk,j is a time independent function, which depends on
                                       2             2
                       = |αkx ,jx (t)| |αky ,jy (t)| ,          (47)    the eigenstates associated with θx , θx′ , θy , and θy′ . Because
                                                                        of the limit in the time integral in Eq. (48), there are only
                                                                        contributions to χk,j if a value (λθx − λθx′ ) for the x-direction
                                                                        has a counterpart −(λθy − λθy′ ) in the y-direction.
                    P
with αkx ,jx (t) = θx exp(−iλθx t)hkx |Ψθx ihΨθx |jx i , and              A careful analysis of the differences (λθx − λθx′ ) indicates
similarly for the y-direction.                                          where the asymmetries stem from. For finite chains one ob-
                                                                                                                                        11

tains (λθx − λθx′ ) = 2 cos θx′ − 2 cos θx . For simplicity one     (a) 6−fold finite path star graph    (b) 4−fold star square graph
considers now finite N × N networks with OBCs, see [71],
because then the eigenvalues are the same in both directions.
It turns out that for θx 6= θx′ the value (λθx − λθx′ ) appears
only once or twice for all symmetric cases. However, for the
asymmetric cases, some of the (λθx − λθx′ ) values (again for
θx 6= θx′ ) appear more than twice. Therefore, there are more                                       strata
contributions to χk,j in the asymmetric cases than in the sym-
metric cases.                                                      FIG. 10: (a) Star with 6 arms composed of finite segments of length
                                                                   4. (b) Star with 4 arms composed of circles of length 4. The dashed
                                                                   lines are guides to the eye, connecting all nodes belonging to given
                     2.   Star-like networks                       strata, see text.

   Networks which are not regular but, yet, have symmetry
properties which can be exploited, are star-like networks. As
already mentioned in Sec. III A and also discussed in [73, 74],    where, without loss of generality, the node 2 was chosen as
these networks consist of a central core node (with label 1)       initial node. One sees, especially for large N , that the prob-
to which each of the remaining N − 1 nodes is attached by          abilities are mainly localized on the initial node. For all ini-
an individual bond, see Fig. 2. The Hamiltonian has then the       tial conditions, the classical transition probabilities pk,j (t) ap-
following structure                                                proach the equipartition value 1/N .
                          N 
                          X                                          Having determined the probabilities to return or to still be
 H = (N − 1)|1ih1| +         |jihj| − |1ihj| − |jih1| . (49)       at the origin allows to calculate the average return probability
                          j=2                                      π(t), see Sec. III. One has thus
Using the Gram-Schmidt orthonormalization procedure, Xu
obtained the eigenstates of H [80]                                               N
                                                                             1 X                 1h                           i
                                          n+1                       π(t) =         πk,k (t) =      π1,1 (t) + (N − 1)π2,2 (t) ,
                1 √                  1 X         
                                                                            N                   N
           
            √            n|n + 2i −  √        |mi                              k=1
                n+1                     n m=2
           
           
           
           
                                                                                                                             (53)
           
           
                                    for n < N − 1                 which leads to the results given in Eq. (37).
           
                    N
           
            √1
           
                                                                     The strong dependence on the initial conditions also carries
           
                  X
                        |mi
  |Ψn i =       N m=1                                (50)          over to the long-time averages χk,j . One obtains namely
           
                                     for n = N − 1
           
           
           
           
                               N
           
           
                1       1              √       
                                                                     χ1,1 = (N 2 − 2N + 2)/N 2 ,
                             X
           
            √           √        |mi  −    N |1i
                N −1       N m=1
           
           
                                                                     χ2,1 = 2/N 2 ,
           
           
           
                                          for n = N
           
                                                                     χ2,2 = (N 4 − 4N 3 + 5N 2 − 2N + 2)/ N 2 (N − 1)2 ,
                                                                                                                     
   This yields analytic expressions for the transition probabil-     χ3,2 = 2(N 2 − N + 1)/ N 2 (N − 1)2 .
                                                                                                       
ities, e.g.,
                                                                                                                      (54)
                 N 2 − 2N + 2 2(N − 1)
    π1,1 (t) =               +         cos(N t).           (51)
                      N2        N2
                                                                   Thus, for large N the probability will be concentrated at the
One easily verifies that for cos(N t) = 1, i.e., t = 2πr/N         initial node.
(where r is an integer), there is a perfect revival. Moreover,
for t = (2r + 1)π/N all the probabilitiy is distributed over all     In a slightly more general setup, Salimi considered CTQW
but the core node. This is not true if one starts the CTQW at      on networks (called star graphs in [81]) with are built from
any of the other (N − 1) nodes, then one has                       several sub-networks such that all sub-networks share a single
                   h                                               node, see Fig. 10. The adjacency matrix is then a direct prod-
                      N 4 − 4N 3 + 5N 2 − 2N + 2
                                                      
        π2,2 (t) =                                                 uct of the separate adjacency matrices with additonal entries
                                                                   for the newly created bonds.
                 + 2N 3 − 6N 2 + 4N cos(t)
                                         
                                                                     By considering so-called strata, i.e., sets formed by all the
                 + 2N 2 − 4N cos((N − 1)t)
                                 
                                                                   nodes at the same chemical distance from the central node,
                                       i       1                   see the dashed lines in Fig. 10, Salimi calculated the transition
                 + (2N − 2) cos(N t)                    ,
                                         N (N − 1)2
                                           2
                                                                   probabilities to go from the central node to the different strata.
                                                           (52)    For a star with N arms each of which having 2 nodes, see
                                                                                                                                                                                    12

Fig. 2 in [81], he obtains for the transition probabilities           probabilities he then obtains
                                      √          2                                  2
                                                                                     N − 2N + 2 2(N − 1)
                            1 + N cos( N + 1t)                                                  +         cos(N t)
              π1,1 (t) =                           ,          (55)                 
                                                                                   
                                                                                          N2          N2
                                   N +1
                                                                                   
                                                                                   
                                                                                                          for k = j
                                                                                   
                            √       √        2                          πk,j (t) =                                                                                            (65)
                              N sin( N + 1t)                                          2     2
                                                                                         − 2 cos(N t)
                                                                                   
              π2,1 (t) =         √             ,              (56)                 
                                                                                       2
                                                                                   N      N
                                                                                   
                                   N +1
                                                                                   
                                                                                   
                                                                                                         for k 6= j.
                                       √          2
                            N (1 − cos( N + 1t)
          and π3,1 (t) =                √           .         (57)    Therefore, the transition probabilities have exactly the same
                                (N + 1) N
                                                                      form as the ones for the star graph, when the excitation starts
   In the case of a star made out of rings of length 4, such that     at the core.
all rings share a single node, there are again 2 strata and the
central node, see Fig. 10(b) and [81]. The transition probabil-
ities are given by                                                                                         4.    Dendrimers

                                                     2
                                                                         Star graphs of length 1 can also be viewed as being den-
                                      p
                           1 + N cos( 2(N + 1)t)
            π1,1 (t) =                                 ,      (58)    drimers (Cayley-trees) of first generation. The stucture of
                                    N +1
                                                                      dendrimers is exemplified in Fig. 11 for dendrimers of gen-
                           √       p             2                    erations G = 2 and G = 3, with functionality f = 3, see
                             N sin( 2(N + 1)t)
            π2,1 (t) =            √                ,          (59)    also [82]. In general, the functionality f gives the number of
                                    N +1                              bonds emanating from each node; the generation G refers to
                                        √          2                  all the nodes whose shortest distance (in bond units) from the
                           N (1 − 2 cos( N + 1t)
        and π3,1 (t) =                   √           ,        (60)    central node is not larger than G. Note that the number of
                                2(N + 1) N                            nodes belonging to the g-th generation (where G ≥ g ≥ 1)
                                                                      is 3 · 2g−1 and that it grows exponentially with g. Moreover,
results very similar to the above.                                    the total number of nodes in the dendrimer of generation G is
   For strata more distant from the core, one can still com-          N = 3 · 2G − 2.
pute the transition probabilities for different N . Evidently,           The connectivity matrix of these dendrimers has a very sim-
the N = 1 case corresponds to a semi-infinite line, while the         ple structure. One has Aii = 3 for all the nodes in the first
N = 2 case is equivalent to the infinite line, i.e., the transition   G − 1 generations and Aii = 1 for the nodes in generation
probabilities are given by Bessel functions.                          G. The bonds are represented by the off-diagonal matrix ele-
   Letting N go to infinity, Salimi showed that in all cases          ments Aij . Here, every node in generation g ≥ 1 is connected
considered above the transition probabilities reduce to               to two consecutively numbered nodes in generation g + 1 and
                                                                      to one node in generation g − 1.
                         π1,1 (t) = cos2 t,                   (61)       The eigenmodes of such dendrimers were studied in [83].
                                         2                            There, for the dendrimers of generations G = 1 and G = 2,
                        π2,1 (t) = sin t,                     (62)
                    and π3,1 (t) = 0,                         (63)    the eigenvalues and eigenvectors of A were explicitly calcu-
                                                                      lated. The eigenvectors determine the eigenmodes of the den-
which is equivalent to the result for a dimer, i.e., a complete       drimer, see e.g. Fig. 3 of [83]. It was further shown that there
graph consisting of two nodes.                                        are G + 1 nondegenerate eigenvalues, one of which is always
                                                                      λ0 = 0.


                       3. Complete graph                               (a) G=2                                      (b) G=3
                                                                                                                                            12           13
                                                                                                                                    11
                                                                                     5                                                                             14
                                                                                                 6
  The complete graph (for finite N ), where all nodes are mu-                                2
                                                                                                                                            5
                                                                                                                                                          6
tually connected with each other, shares some properties with                                                                                       2

the star graph. The Hamiltonian now reads                                                                                                               g=1            g=2    g=3

                                                                                         1                          22                          1
                                                                                                 g=1       g=2                 10
                                                                        10                                                                                                     15
                            N                                                                                        21                                                  7
                            X                X                                                              7                           4                     3
                                                                                 4                     3
            H = (N − 1)           |jihj| −          |jihk|.   (64)                                                                  9
                                                                                                                                                                              16
                                                                                                                                                              8
                            j=1              k6=j                            9
                                                                                                       8
                                                                                                                          20
                                                                                                                                                                         17
                                                                                                                               19
                                                                                                                                                                  18
The graph has two distinct eigenvalues EN = 0 and En = N
for n = 1, . . . , N − 1. Xu showed that, similar to the star
[73, 74, 80], one can calculate the eigenstates using the Gram-       FIG. 11: Dendrimers of functionality f = 3 and generation G = 2
Schmidt orthonormalization procedure [80]. For the transition         (left) and G = 3 (right). From [82].
                                                                                                                                            13

        (a)
   (a) G=3                                                                                                    initially
                                                                                                           excited node




                                                                                                                          Clusters

                                                                                 Clusters




                                                                         FIG. 13: (Color online). Clusters of the same limiting probability
                                                                         χk,j in the branch with the initial excitation for a dendrimer of gen-
        (b)
   (b) G=4                                              0.3              eration G. Nodes connected by thick (red) lines belong to the same
           40                                                 χ          cluster. From [82].
                                                        0.25   k,j

           30                                           0.2              i.e. limt→∞ pk,j (t) = 1/N for all nodes. Quantum mechan-
          k                                                              ically this is not the case. Figure 12 shows the LPs χk,j as a
                                                        0.15
           20                                                            contour plot [82]. Bright shadings correspond to high values
                                                        0.1              of the LP, whereas dark shadings correspond to low LPs. The
                                                                         diagonal has high values, meaning that an excitation starting
           10
                                                        0.05             at node j has a high LP to be found again at node j. The struc-
                                                                         tures of the LP distributions of dendrimers are self-similar,
              1                                         0                generation after generation.
                  1   10    20       30    40   46
                                 j                                          Furthermore, different nodes k and l may have the same LP,
                                                                         χk,j = χl,j . One hence combines all the nodes having (up to
FIG. 12: Limiting probabilities for dendrimers with (a) G = 3 and        our numerical precision, 10−10 ) the same LP into a cluster.
(b) G = 4. The white lines indicate the limiting distributions for the   Note, however, that the separation of the nodes into clusters
dendrimers of generations smaller than G. From [82].                     depends on the initially excited node, namely on j. For an ex-
                                                                         citation starting at the center (node 1), the clusters correspond
                                                                         exactly to the different generations of the dendrimer. In the
   When an excitation starts at the central node 1, the dynam-           general case, when starting from a non-central node, one still
ics of this excitation over the dendrimer can be mapped onto             finds from Fig. 12 that nodes belonging to the same cluster
a line. Remarkably, for the G = 2 dendrimer the transition               also belong to the same generation (the converse is not neces-
probabilities are fully periodic when the coherent excitation            sarily true).
starts from the central node 1 (the same holds for the G = 1                For larger dendrimers, while the general cluster pattern is
dendrimer, too). Note that due to rotational symmetry, the               preserved, some details change. Figure 13 shows the situation
transition probabilities from the central node to nodes belong-          for a dendrimer of dimension G = 5, for an excitation starting
ing to the same generation are equal. Because of this one                at a peripheral node. Again one indicates clusters by connect-
only has to list three different transition probabilities. It fol-       ing nodes by thick (red) lines. A change to be noticed is that
lows that there is a perfect revival of the initial state, which         for G ≥ 5 the initially excited node does not form anymore
resembles results obained for continuous [40, 41] and discrete           a cluster with its next-nearest node of the same generation. It
quantum carpets [72, 84].                                                appears as if such two nodes only belong to the same cluster
   If the initial excitation is placed at one of the nodes of the        when the dendrimer has G ≤ 4. Thus the total number of
outermost generation g = G of the dendrimer, the picture                 clusters is NC ≡ (G2 + G + 6)/2 for G ≥ 5 and NC − 1 for
changes. Classically, the propagation through the dendrimer              G ≤ 4.
gets to be much slower than in the previous case, see e.g.
[58, 85, 86]. Nevertheless, eventually the excitation will clas-
sically propagate through the whole graph and in the long time                                     5. Husimi-cacti
limit the probability will be equipartitioned among all nodes.
Quantum mechanically this effect is even more dramatic. The                 As shown in [87], it may happen that the excitation occu-
main fraction of πk,j (t) stays in a small region closely con-           pies preferentially the bonds between the branching points of
nected by bonds to the initial node j, and the transfer to other         the dendrimer. Then, the essential underlying structure is dif-
sites is highly unlikely. Also at long times the limiting prob-          ferent and is given by sites localized at the mid-points of the
ability for the excitation to reach the other branches of the            bonds. The situation is exemplified in Fig. 14(a), starting from
dendrimer stays very low.                                                a dendrimer of generation 2 (open circles) and indicating the
   Classically, the LP is equipartitioned among all the nodes,           mid-points of the bonds by filled circles. Connecting neigh-
                                                                                                                                                                                                                                                                                              14
                                                                                                                                             N=45
  (a)                        N=9               (b)                       N=21                              (c)                  24
                                                                                                                                      25
                                                                                                                                                        26
                                                                                                                                                               27
                                                                                                                                                                                                                                                                                        (b)
                                                                11                     12
                                                                                                                                 11                              12                                                                           1
                         4         5
                                                          10
                                                                         4        5                                    23 10                 4          5           13 28                                     (a)       2                                           3
                                                                                            13
                                                                                                                       45       22                                       29 31

                               1                                              1                  14              44                                 1                   30
                                                     21
                                                                                                                  21                                                              14                      4                         5                 6                  7
                     3                                               3                                          20                       3                                         15 32
                                                                                                                                                                                                     8          00
                                                                                                                                                                                                                119         00
                                                                                                                                                                                                                            11
                                                                                                                                                                                                                            10          111
                                                                                                                                                                                                                                        0       1
                                                                                                                                                                                                                                                0
                                                                                                                                                                                                                                              120             0
                                                                                                                                                                                                                                                              113   00
                                                                                                                                                                                                                                                                    11
                                                                                                                                                                                                                                                                    14        15       11
                                                                                                                                                                                                                                                                                       00
                                                                                                                                                                                                                00
                                                                                                                                                                                                                11          11
                                                                                                                                                                                                                            00          0
                                                                                                                                                                                                                                        1       1             0
                                                                                                                                                                                                                                                              1     11
                                                                                                                                                                                                                                                                    00                 11
                                                                                                                                                                                                                                                                                       00
                                                                                                                                                                                                                11
                                                                                                                                                                                                                00          00
                                                                                                                                                                                                                            11          0
                                                                                                                                                                                                                                        1         1
                                                                                                                                                                                                                                                  0           1
                                                                                                                                                                                                                                                              0     00
                                                                                                                                                                                                                                                                    11                 00
                                                                                                                                                                                                                                                                                       11
        9                          2       6   20     9                           2              6    15   43               9                           2                6
                                                                                                                 42                                                                    33
            8                                              8                                                                     8
                                       7                                                    7                                                                       7
                                                                                                                                                                                                         16                         17             18                    19
                                                                                                                                             38                              34
                                                      19                 18       17            16
                                                                                                                      41         19 18             37         17 16
                                                                                                                            40                   39         36               35
                                                                                                                                                                                                                    20                                              21

                                                                                                                                                                                                                                              22
FIG. 14: Finite Husimi cacti (filled circles) of size (a) N = 9, (b)
N = 21, and (c) N = 45. (a) also shows with dashed lines and open
circles the corresponding dendrimer. From [88].                                                                                                                                                (c)


        (a) N=21
                                                                                                                                                                                                                      G−1 G−1 G−2 G−3                                    G−3 G−2 G−1 G−1
                                                                                                                                                                                                           dk       2       2   2   2              2      2    2         2    2    2   2
                                                                                                                                                                                               (d)
                                                                                                                                                                                                         cluster 1          2   3 4                G G+1                               2G+1

                                                                                                                                                                                            FIG. 16: (a) Graph consisting of two Cayley trees of generation
                                                                                                                                                                                            G = 3. (b) horizontal projection of the graph following Ref. [89],
                                                                                                                                                                                            (c) vertical projection of the same graph. (d) Vertical projection of a
                                                                                                                                                                                            similar graph, obtained from two Cayley trees of general generation
                                                                                                                                                                                            G, indicating the new nodes (clusters) and the dk , see text for details.
                                                                                                                                                                                            From [23].


                                                                                                                                                                                            are obvious. Figure 15 presents the LPs for two sizes of
                                                                                                                                                                                            Husimi cacti, N = 21 and N = 45. The LP distributions
                                                                                                                                                                                            are self-similar generation after generation. Furthermore, for
                                                                                                                                                                                            each size there are LPs having the same value, i.e. χk,j = χl,j .
                                                                                                                                                                                            One collects LPs of the same value into clusters. Depending
        (b) N=45
                                                                                                                                                             0.35
                                                                                                                                                                                            on where the excitation starts, the clustering is different. This
                                                                                                                                                                                            in analogous to the previous results for dendrimers. Since both
            40
                                                                                                                                                                 χ
                                                                                                                                                                        k,j                 dendrimers and Husimi cacti lead to similar results, one can
                                                                                                                                                             0.3
                                                                                                                                                                                            conclude that here the loops have no significant effect on the
                                                                                                                                                             0.25                           transition probabilities.
            30

                                                                                                                                                             0.2
        k                                                                                                                                                                                                                        6. Glued Cayley trees
            20                                                                                                                                               0.15
                                                                                                                                                                                               One particular example which shares the properties of both
                                                                                                                                                             0.1                            regular and hyperbranched networks is a network which is
            10
                                                                                                                                                                                            composed of two Cayley-trees with the same number of gen-
                                                                                                                                                             0.05                           erations, where the nodes of the last generation are shared by
            1
                                                                                                                                                                                            both trees, see Fig. 16.
                                                                                                                                                             0
                 1                     10                  20                               30                  40                                                                             Now, depending on the initial condition, the dynamics of
                                                                     j
                                                                                                                                                                                            the CTQW over such a network can change dramatically.
                                                                                                                                                                                            While the transport from the top to the bottom node is very
FIG. 15: Limiting probabilites for finite Husimi cacti of sizes (a)
                                                                                                                                                                                            fast [89] and comparable to the dynamics on a finite regu-
N = 21 and (b) N = 45. From [88].
                                                                                                                                                                                            lar one-dimensional network, the transport from the left-most
                                                                                                                                                                                            node to the right-most node is very slow [23] compared to the
                                                                                                                                                                                            transport in dendrimers or Husimi cacti when the excitation
boring filled circles by new bonds, one is led to the so-called                                                                                                                             starts at a peripheral node [82, 88].
Husimi cactus. Figure 14 shows three finite Husimi cacti of                                                                                                                                    The authors of Refs. [21] and [89] have analyzed CTQW
sizes N = 9, 21, and 45.                                                                                                                                                                    over such networks, focussing on walks which start at the
   In the same way as for the dendrimer, one finds numerically                                                                                                                              top node, and looking for the amplitude of being at the bot-
that for the finite Husimi cactus consisting of 21 nodes, as                                                                                                                                tom node at time t. The problem can then be simplified by
depicted in Fig. 14, the TPs are nearly periodic when the initial                                                                                                                           considering only states which are totally symmetric superpo-
excitation is placed on one of the (symmetrically equivalent)                                                                                                                               sitions of states |ki, involving all the nodes k in each row of
nodes 1, 2, or 3 of the inner triangle [88].                                                                                                                                                Fig. 16(a), as indicated schematically in Fig. 16(b). The trans-
   Also in the long time limit, the similarities to the dendrimer                                                                                                                           port gets then mapped onto a one-dimensional CTQW [89].
                                                                                                                                                        15

   Other initial conditions for the CTQW are, indeed, possible,                                                   G=3 dendrimer
                                                                          (a)
especially when considering the high symmetry of the under-                                         0.8
                                                                                                                                       t=1
lying graphs. Note that, using for instance the site enumera-                                                                          t=5
tion of Fig. 16(a), a CTQW from node 8 to node 15 is equiv-                                         0.6                                t=10



                                                                               probability πj1(t)
                                                                                                                                       t=20
alent to a CTQW from, say, node 10 to node 14. The graph’s                    ~
                                                                                                                                       t=40
                                                                                                    0.4                                t=80
symmetry suggests to collect groups of such nodes into clus-                                                                           t=160
ters, while focussing on the transport from left to right. It is
                                                                                                    0.2
then natural to view the nodes 8, 9, 10, and 11 as belonging to
the first cluster. The second cluster consists then of the nodes                                     0
4, 5, 16, and 17, all of which are directly connected by one                                              1   2    3      4        5           6   7
bond to the nodes of the first cluster. The nodes 2 and 20 of             (b)                                          cluster j
the third cluster are all nodes directly connected by one bond                                0.16
to the nodes of the second cluster, while at the same time not

                                                                          lim. prob. χj1
                                                                          ~                   0.15
belonging to the first cluster. In general, all the nodes of the
(k + 1)st cluster are connected by one bond to nodes of the                                   0.14

kth cluster and at the same time do not belong to the (k − 1)st                               0.13
cluster.                                                                                      0.12
   Let us denote the number of nodes in cluster k by dk . The
                                                                                                          1   2    3      4        5           6   7
transport occurs now from a cluster to the next, by which the                                                          cluster j
original graph gets mapped onto a line in which one new node
corresponds to a group of original nodes of the graph. For a         FIG. 17: (a) Transition probability π̃j1 (t) for a CTQW between
new node at position k ∈ [2, G] one finds that dk = 2G−k+1 ,         different clusters j of the G = 3 graph. The CTQW starts at the first
the same being true for the mirror node value, i.e., dk =            cluster, presented is the situation at times t = 1, 5, 10, 20, 40, 80,
d2G+2−k . Note that for the end nodes d1 = d2G+1 = 2G−1 ,            and 160. (b) Limiting probability χ̃j1 for a CTQW starting at the
the same holds for the nodes next to them. Moreover, for the         first cluster. From [23].
middle node dG+1 = 2.
   One now focuses on the transport via the states which are
totally symmetric, normalized, linear state-combinations for         where bk is the number of bonds between the clusters k and
all the original nodes in each cluster. Thus, for the kth cluster,   k + 1.
whose sites are denoted by n, one has as a new state [23]               Now, except for the ends and the center of the graph, bk
                                                                     equals the maximum of the pair (dk , dk+1 ). Between the cen-
                              1 X
                     |ak i = √       |ni.                    (66)    tral node (dG+1 = 2) and its neighbors (dG = dG+2 = 2) the
                              dk n∈k                                 number of bonds is bG = bG+2 = 2. The number of bonds be-
                                                                     tween the end node and its neighbor is b1 = b2G+1 = 2d1 =
  The CTQW is now determined by the new Hamiltonian                  2G .
H̃ = γ Ã, where the matrix elements of Ã are obtained from
                                                                        For the graph consisting of 22 original nodes the new ma-
the new basis states |ak i and from the matrix A through
                                                                     trix Ã is a tridiagonal 7 × 7 matrix, which can be readily di-
                       Ãjk = haj |A|ak i.                   (67)    agonalized. The advantage of the procedure is clear: the new
                                                                     matrix Ã depends on the number of clusters and grows with
Given the properties of A and the construction of the |ak i,         (2G+1), whereas the full adjacency matrix, A, grows with the
Eq.(66), Ã is a real and symmetrical tridiagonal matrix, which      total number of nodes in the graph, namely with (3 · 2G − 2).
implies a CTQW on a line. The diagonal elements of Ã are               From Eq.(66) the transition amplitude between the state
given by                                                             |ak i at time 0 and the state |aj i at time t is given by [23]

            Ãkk = hak |A|ak i
                                                                        α̃jk (t) = haj |e−iH̃t |ak i = haj |Q̃e−iγ Λ̃t Q̃−1 |ak i,                     (70)
                    1 X ′
                 =         hn |A|ni = fn ≡ fk ,              (68)
                   dk n∈k
                          n′ ∈k
                                                                     where Λ̃ is the eigenvalue matrix and Q̃ the matrix con-
                                                                     structed from the orthonormalized eigenvectors of the new
where fk is the functionality of every node in the kth cluster.      matrix Ã.
For the sub- and super-diagonal elements of Ã one finds [23]           Now the quantum mechanical transition probabilities are
                                                                     given by π̃jk (t) = |α̃jk (t)|2 . Figure 17(a) shows the transi-
           Ãk,k+1 = Ãk+1,k = hak |A|ak+1 i
                                                                     tion probabilities for CTQW over clusters. Remarkably, now
                          1      X
                                                                     already during short periods of time, such CTQW move from
                   = p                hn′ |A|ni
                        dk dk+1 n∈k                                  one end cluster to the other one. The limiting probability dis-
                                     n′ ∈k+1
                                                                     tribution, χ̃jk , which is depicted in Fig. 17(b), also supports
                          bk                                         this finding. Note that Fig. 17(b) again reflects the symmetry
                     = −p        ,                           (69)
                         dk dk+1                                     of the original graph.
                                                                                                                                               16

                                                                                                 0
                                                                                                10

                                                 Dual
                                                 Sierpinski




                                                                         π(t), |α(t)|2 , p(t)
                                                 Gasket                                          −2
                                                                                                10
          Sierpinski
          Gasket

                                                                                                 −4
                                                                                                10
                                                                                                           exact value
                                                                                                           classical
                                                                                                           lower bound
                                                                                                 −6
                                                                                                10    −1       0             1       2    3
                                                                                                     10      10            10       10   10
                                                                                                                          time )t
                                                                                                                         t(γ −1



                                                                     FIG. 19: (Color online) Average return probability π̄(t) for the DSG
FIG. 18: Dual transformation from Sierpinski Gasket to Dual Sier-    of generation g = 5 on a log-log scale. The comparison with the
pinski Gasket of generation g = 3. From [90].                        classical p̄(t) evidences that the classical random walk spreads more
                                                                     efficiently than its quantum-mechanical counterpart. The dashed line
                                                                     represents the envelope of π̄(t). From [90].

                            B. Fractals
                                                                     ing to
                                                                                                                         p
                       1.   Sierpinski Gaskets                                                                  5±        25 − 4λg−1
                                                                                                           λ±
                                                                                                            g =                      ;        (71)
                                                                                                                            2
                                                                                      −
   Regular networks have integer dimensions, while some              both λ+ g and λg inherit the degeneracy of λg−1 . The eigen-
tree-like stuctures presented in the previous section, such          value spectrum is therefore bounded in [0, 5]. As explained
as the dendrimers, can be of “infinite fractal dimension”,           in [91], at any generation g, one can calculate the degeneracy
when the (fractal) dimension is taken to be given by df =            of each distinct eigenvalue: apart from λN whose degener-
limR→∞ ln N/ ln R, N being the number of nodes within                acy is 1, there are 2r distinct eigenvalues, each with degen-
a sphere of radius R.. In contrast, (deterministic) fractals         eracy (3g−r−1 + 3)/2, being r = 0, 1, ..., g − 1, and 2r dis-
have finite, in general, non-integer dimensions. One partic-         tinct eigenvalues, each with degeneracy (3g−r−1 −1)/2, being
ular example of a deterministic fractal is the dual Sierpinski       r = 0, 1, ..., g − 2. As can be easily verified, the degeneracies
gasket (DSG) for which the exact spectrum of the eigenval-           sum up to N = 3g .
ues of the connectivity matrix is known [90]. A DSG is an               For the DSG the CTRW average return probability p̄(t) is
exactly-decimable fractal which is directly related, through a       readily obtained without numerically diagonalizing the con-
dual transformation, to the Sierpinski gasket (SG). The DSG          nectivity matrix, since it only depends on the eigenvalues
of generation g can be constructed by replacing each small           which can be calculated iteratively. Figure 19 displays the
triangle belonging to the SG with a node and by connecting           averaged probabilities p̄(t), π̄(t) and |ᾱ(t)|2 as a function of
such nodes whenever the relevant triangles share a vertex in         time, obtained for g = 5. The classical p̄(t) decays mono-
the original gasket (see Fig. 18). It is straightforward to verify   tonically to the equipartition value 1/N , while the quantum-
that the number of nodes at any given generation g is N = 3g .       mechanical probabilities eventually oscillate around the value
                                                                     0.7, which is larger than 3−g . Although the amplitude of fluc-
   The dual transformation does not conserve the coordina-           tuations exhibited by the lower bound is larger than that of the
tion number (which decreases from 4 to 3, while the coordi-          exact value, the agreement between the two quantities is very
nation number of nodes corresponding to the vertices of the          good. In particular, the positions of the extremal points practi-
gasket remains 2), but it does conserve the fractal dimension        cally coincide and the maxima of π̄(t) are well reproduced by
df and the spectral dimension d, ˜ which are therefore the same      the lower bound. This is analogous to the behavior of walks
as for the original Sierpinski gasket, namely df = ln 3/ ln 2 =      on square lattices, Cayley trees, and stars, as described in the
1.58496... and d˜ = 2 ln 3/ ln 5 = 1.36521.... The eigenvalue        previous sections. Notice, however, that for the square lattices
spectrum of the DSG connectivity matrix can be determined            the lower bound turns out to be exact while for Cayley trees
at any generation through the following iterative procedure          and for stars it is only an approximation, which, moreover,
(for more details see [91, 92]): At any given generation g the       turns out to be less accurate than what is found for the DSG.
spectrum includes the non-degenerate eigenvalue λN = 0, the             At short times (t < 5γ −1 ) it is possible to construct the
eigenvalue 3 with degeneracy (3g−1 +3)/2 and the eigenvalue          envelope of π̄(t), which depends algebraically on t [90]. The
5 with degeneracy (3g−1 − 1)/2. Moreover, given the eigen-           exponent is ≈ −0.82, to be possibly compared with d/2     ˜ ≈
value spectrum at generation g −1, then to each non-vanishing        −0.68 which is the exponent expected classically for the in-
eigenvalue λg−1 correspond two new eigenvalues λ±    g accord-       finite DSG. The decay of the average return probability π̄(t)
                                                                                                                                                                                   17

                            0
                           10                                                                                   (a) g=3
                                                                                                                                                                    0.25
                            −1
                           10                                                                                       25




    π(t), |α(t)|2 , p(t)
                                                                                   π(t), g = 4
                                                                                                                                                                    0.2
                            −2                                                     |α(t)|2 , g = 4                  20
                           10
                                                                                   p(t), g = 4
                                                                                                                                                                    0.15
                                                                                   π(t), g = 5
                            −3
                           10
                                                                                   |α(t)|2 , g = 5
                                                                                                                k   15                                                     χk,j
                                                                                   p(t), g = 5                                                                      0.1
                            −4
                           10                                                                                       10

                                                                                                                                                                    0.05
                                                                                                                     5
                                0        10           20          30     40
                                                    time t)
                                                    t(γ −1
                                                                                                                            5        10    15        20   25
                                                                                                                                           j
FIG. 20: (Color online) Average return probability π̄(t) for the DSG
of generation g = 4 (bright colour) and g = 5 (dark colour). Its                                                (b) g=4
lower bound |ᾱ(t)|2 (dashed line) and the classical p̄(t) (dotted line)                                           80
are also depicted, as shown by the legend. From [90].                                                              70                                               0.2
                                                                                                                   60

                                                                                                                   50                                               0.15
for the ST can be estimated as well: its envelope goes like t−2                                                 k                                                         χk,j
                                                                                                                   40
(classically p̄(t) ∼ t−1 , see above), implying a faster delocal-                                                                                                   0.1
ization of the QW over the graph.                                                                                  30

   Interestingly, for the DSG, the overall shape of π̄(t) does                                                     20
                                                                                                                                                                    0.05
not depend significantly on the size of the gasket (see Fig. 20                                                    10
and [90]). In fact, the behaviour of π̄(t) is mainly controlled
                                                                                                                                20        40         60        80
by the most highly degenerate eigenvalues. These do not                                                                                    j
change when increasing the fractal size (i.e. its generation).
These values are: 3 with degeneracy mg (3) = (3√g−1 + 3)/2,
5 with degeneracy mg (5) = (3g−1 − 1)/2, (5 ± 13)/2 with                                                    FIG. 21: Limiting probabilities for the DSG of generation (a) g = 3
degeneracy mg−1 (3).                                                                                        and (b) g = 4, whose volumes are N = 27 and N = 81, respec-
                                                                                                            tively. The white lines enclose the limiting distributions for gaskets
   The inhomogeneity of the pattern of the long-time averages                                               of smaller generations. Notice that the global maxima lay on the
χk,j mirrors the lack of translation invariance of the DSG it-                                              main diagonal and correspond to j = 1, 14, 27 and to j = 1, 41, 81
self. For instance, being v the label assigned to any vertex                                                for g = 3 and for g = 4, respectively. From [90].
of the main triangle, χv,v is a global maximum; off-diagonal
local maxima correspond to couples of connected nodes be-
longing to different minor triangles of generation g − 1. This
                                                                                                            the final, explicit formula [90]
allows to establish a mapping between the pattern of χk,j and
the structure of the relevant DSG.
                                                                                                                                           2g
   Since the spectrum of the DSG is known, one can calculate                                                                           1 X
                                                                                                                        χ̄ ≥ χ̄lb =            [m(r)]2 ρ(m(r))
the lower bound of the long-time average of the average return                                                                        N 2 r=0
probability, χ̄lb , analytically. At generation g the spectrum of                                                                       g−1               2
the connectivity matrix displays Ñ distinct eigenvalues, where                                                                     1 n X 3g−r−1 + 3
                                                                                                                                = 2                           × 2r
                                                                                                                                   N    r=0
                                                                                                                                                   2
                                       g−1          g−2
                                       X            X                                                                             g−2
                                                                                                                                  X  3g−r−1 − 1 2
                                Ñ =         2r +          2r + 1 = 3 × 2g−1 − 1.                    (72)
                                                                                                                                                                 o
                                                                                                                                +                       × 2r + 1
                                       r=0          r=0
                                                                                                                                  r=0
                                                                                                                                             2
                                                                                                                                                 3g
                                                                                                                                                                  
                                                                                                                                    1                     10       3
Let us denote the set of distinct eigenvalues by {λ̃i }i=1,...,Ñ .                                                             = 2g 3g 1 +            + 2g −          ,          (74)
                                                                                                                                   3             14        7       2
Being m(λi ) the degeneracy of the eigenvalue λi , one can
write
                                                                                                            such that χ̄ > 1/3g . Interestingly, in the limit g → ∞, the
                                     N                      N                Ñ
                                                                                                            LTA χ̄ is finite [90]:
                                     X                      X                Xh            i2
  N 2 χ̄lb =                                 δλn ,λm =            m(λn ) =          m(λ̃i ) .
                                                                                                                                                            1
                                    n,m=1                   n=1              i=1                                                      χ̄ ≥ lim χ̄lb =         ,                   (75)
                                                          (73)                                                                                 g→∞         14
Now, one goes over to the space of distinct degeneracies, each
corresponding to a number ρ of distinct eigenvalues and gets                                                and χ̄lb reaches this asymptotic value from above.
                                                                                                                                  18

                                                     ring                         (a) B=1                         (b) B=2




                                                                                  (c) B=5                         (d) B=100

            additional
               bonds



FIG. 22: Sketch of a SWN of size N = 16 containing B = 11
additional bonds. From [93].                                       FIG. 23: Time dependence of the averaged transition probabilities
                                                                   hπkj (t)iR for SWN of size N = 100 with (a) B = 1, (b) B = 2, (c)
                                                                   B = 5, and (d) B = 100. The initial node is j = 50 and the number
                   C.    Statistical networks
                                                                   of realizations is R = 500. From [93].

                   1.    Small-world networks
                                                                   Fig. 23(c). This almost regular shape is reached very quickly
  The above examples dealt with deterministic networks.            when B gets to be comparable to N [Fig. 23(d)]. One notes,
However, many real systems have stochastic features; thus the      however, that particular realizations may still show (depend-
connectivity can be random. To model this, one can disrupt         ing on their actual additional bonds) strong interference pat-
the periodicity of regular patterns by randomly including B        terns. These features are washed out by the ensemble average,
additional bonds into the network [93]. In such a way one          so that only the dependence on the initial node stands out.
creates “shortcuts” and a walker can find shorter paths be-           Since CTQW on SWN always carry the information of their
tween pairs of sites than on the regular network. So-called        initial node j, the averaged probabilities to return to j are a
small-world-networks (SWN) are created by randomly adding          good measure to quantify the efficiency of the transport on
bonds to a regular one dimensional ring, see Fig. 22. Here we      such networks, see [73].
do not consider self-connections, i.e., bonds connecting one          Figure 24 shows in double-logarithmic scales the ensem-
node with itself.                                                  ble averages hp(t)iR , hπ(t)iR , and hα(t)iR for SWN with
  The general behavior of CTQW on SWN can be analyzed              N = 100 nodes and B = 1, 2, 5, and 100. For classical trans-
by averaging over distinct realizations R                          port [Fig. 24(a)] the initial decay of hp(t)iR occurs faster for
                                     R                             larger B. The decay at intermediate times follows a power-law
                                 1 X
                   h· · · iR ≡         [· · · ]r ,          (76)   (t−1/2 ) for the ring (as is clear from the linear behavior in the
                                 R r=1                             scales of the figure) and changes to a stretched exponential-
                                                                   type when B is large [94]. Thus, a classical excitation will
where the index r specifies the rth realization of the quan-
                                                                   quickly explore the whole SWN, so that it will occupy each
tity in question. In so doing one obtains statistical results
                                                                   site with equal probability of 1/N already after a relatively
which allow for a comparison with the deterministic situa-
                                                                   short time, see the final plateau in Fig. 24(a).
tion. In particular, we consider here the realization-averaged
transition probabilities hπkj (t)iR , the averaged probabilities      Quantum mechanically, however, the situation is more
hπ(t)iR , their lower bound hα(t)iR , and their classical analog   complex. Fig. 24(b) shows the ensemble average hπ(t)iR .
hp(t)iR . Furthermore, we also discuss the long time average       For a ring of N nodes and for times shorter than roughly
(LTA) of each of these quantities:                                 N/2 hπ(t)iR displays a quasiperiodic pattern (black curve),
                   *                        +                      the maxima of which decay as t−1 . At longer times interfer-
                           1 T                                     ence sets in and leads to an irregular behavior at times longer
                              Z
                      lim          dt · · ·   .             (77)   than N/2 [73]. Now, for SWN, as long as B is consider-
                     T →∞ T 0
                                                R                  ably less than N , the periodic pattern still remains visible; in
   In the absence of any additional bond, the excitations travel   Fig. 24(b) one can follow how an increase in B (red, green,
along the ring and interfere in a very regular manner, produc-     and blue curves) is smoothing out the curves, so that both the
ing discrete quantum carpets [72]. Typical for these carpets       heights of the first maxima and the depths of the minima de-
is that they show, depending on N , full or partial revivals at    crease. At longer times the SWN patterns are flattened out
specific times [72].                                               and hπ(t)iR tends towards a limiting value. With increasing
   For SWN the situation is quite different. Already a few         B this asymptotic domain is reached more quickly, such that
additional bonds obliterate the quantum carpets; the patterns      for larger B the crossover from the quasiperiodic behavior at
fade away [93]. By adding more bonds, only the initial node        short times to a smoothed out pattern at longer times is shifted
retains a significant value for hπjj (t)iR at all times t. Fur-    to smaller t.
thermore, already for SWN with as little as B = 5 the pat-            Figure 24(c) shows the lower bound of π(t), namely
tern of hπjj (t)iR becomes quite regular after a short time, see   h|α(t)|2 iR averaged over the realizations. One notices that
                                                                                                                                                           19

                        0
   (a) 10                                                                                      of course, not valid for the ring, see below). In Eq. (79) the
                                                                                0
                                                                               B=0             triple sum adds then to RN , so that the rhs equals 1/N . On
                                                                                1
                                                                               B=1
                                                                                               the other hand, Eq. (78) leads to [93]
     < p(t) >R
                        -1
                   10                                                           2
                                                                               B=2
                                                                                5
                                                                               B=5
                                                                               B=100
                                                                                100                                          1 X              4
                    -2
                   10
                                                                                                              hχiR =                 hj|Φn,r i .         (80)
                                                                                                                            RN r,j,n
                        -3
       10                                                                                      This expression depends on the eigenstates; in fact the rhs of
          0
   (b) 10                                                                                      Eq. (80) is the ensemble average of the average participation
                                                                                               ratio of the eigenstates |Φn,r i. Equation (80) is well known
                                                                                               in the theory of quantum localization, see, e.g., Sec. V. A. in
    < π(t) >R
                        -1
                   10
                                                                                               [95]. For the ring the eigenstates are Bloch states,
                    -2
                   10                                                                                                                N
                                                                                                                         1 X iEn j
                                                                                                                |Φn i = √      e   |ji,                  (81)
                        -3                                                                                               N j=1
                   10
         0
   (c) 10                                                                                                              4
                                                                                               from which hk|Φn i = 1/N 2 follows for all |Φn i.
                                                                                                  Now, increasing B results in an increase of hχiR , starting
     < |α(t)| >R
                        -1
                   10
   2                                                                                           from the corresponding value for the ring (B = 0, only one
                                                                                               realization, and N even)
                    -2
                   10
                                                                                                                                1 X       2N − 2
                                                                                                         hχring iR ≡ χ =            χjj =        ,       (82)
                        -3                                                                                                      N j        N2
                   10                 0              1            2        3            4
                                    10         10             10          10           10
                                                         time t                                where χjj = (2N − 2)/N 2 . Equation (79) yields a 1/N de-
                                                                                               pendence for the LTA of h|α(t)|2 iR , which by rescaling with
FIG. 24: (Color online) Time dependence of the averaged probabil-
                                                                                               hχring iR ∼ 1/N would result in a constant value for large
ities (a) hp(t)iR , (b) hπ(t)iR , and (c) h|α(t)|2 iR for SWN of size
N = 100 with B = 1, 2, 5, and 100. The number of realizations is
                                                                                               N [93]. However, rescaling hχiR with hχring iR shows an
R = 500. From [93]                                                                             increase with N of hχiR /hχring iR which is less than linear,
                                                                                               thus, hχiR depends on N as 1/N ν , with ν ∈ [1, 2].
                                                                                                  The fact that hχiR for SWN increases with increasing B
                                                                                                                                      4
the overall behavior of Figs. 24(b) and 24(c) is quite similar.                                points towards a change of hk|Φn i from the value 1/N 2 .
However, the limiting values at long times differ. For the LTA                                 The situation may be visualized as follows: For the ring all
of hπ(t)iR one has (see also Eq. (17) of Ref. [71])                                            eigenstates are Bloch states and hence are completely delo-
                                                                                               calized. Going over to SWN and increasing the number of
                                            1 T                                                additional bonds B leads to localized states at the band edges
                                         D   Z           E
                             hχiR ≡          lim  dt π(t)                                      and to fairly delocalized states well inside the band. The in-
                                       T →∞ T 0            R
                                       1 X                                                     crease of hχiR is thus mainly due to the localized band edge
                                    =           δ(En,r − En′ ,r )                              states.
                                      RN
                                              r,j,n,n
                                              ′

                                                                      2
                                         × hj|Φn,r ihj|Φn′ ,r i ,                       (78)                      2.       Erdös-Rényi networks
where δ(En,r − En′ ,r ) = 1 for En,r = En′ ,r and δ(En,r −
En′ ,r ) = 0 otherwise. For h|α(t)|2 iR the long-time values                                       Somewhat similar to the SWN is the Erdös-Rényi network
for different B collapse to one value. In fact, the LTA of                                     (ERN). One starts with N disconnected nodes, every pair of
h|α(t)|2 iR obeys                                                                              nodes is then connected with the probability p, where only
                                                                                               single connections between two nodes are allowed. One can
                                D      1 T
                                        Z              E                                       in turn associate to p an average degree k of the nodes, which
                                  lim       dt |α(t)|2                                         is related to p by k = p(N − 1). For large network sizes N ,
                                 T →∞ T 0                R
                                                                                               the degree distribution P (k) of the ERN is Poissonian peaked
                                    1   X
                                                                                               at k.
                                =           δ(En,r − En′ ,r ),                          (79)
                                  RN 2                                                             Xu and Liu showed in Ref. [96] that in the ensemble aver-
                                          ′  r,n,n
                                                                                               age, the average return probabilities display a behavior very
as can be immediately inferred from Eq. (24). Thus this quan-                                  similar to the SWN, see Sec. IV C 1 and [93]. Although the
tity is only a function of the eigenvalues En,r and does not                                   probabilities decay, they do so only until they reach a plateau
depend on the eigenstates |Φn,r i. In order to quantify the dif-                               (for N = 100), at a level considerably higher than the equipar-
ferences between Eqs. (78) and (79) for SWN, one assumes                                       tition value of 1/N . The behavior is only weakly affected by
that all the eigenvalues are nondegenerate (this assumption is,                                the value of the average degree k.
                                                                                                                                    20

                                                                                                        1




                                                                                              5      4       6



                                                                                                    7
                                                                            2                                               3

                                                                     FIG. 26: Example of an apollonian network of generation G = 2.

FIG. 25: Example of a scale-free network with N = 36 nodes and
φ = 5/2.                                                            have the largest symmetry), the larger is the stationary value.
                                                                    Large average return probablities are also found in the long-
                                                                    time averages χk,j , where in the ensemble average the values
   The height of the plateau is determined by the long-time         on the diagonal (for k = j) are much larger than the values
behavior of the transition probabilities. Due to the ensemble       for k 6= j.
average, all structure of the non-diagonal elements of hΞk,j i
disappears and only the main diagonal hΞj,j i remains.
                                                                                         4.   Apollonian networks

                     3.   Scale-free networks
                                                                       So-called Apollonian networks are models for networks
                                                                    which have small-world as well as scale-free properties.
   The distribution P (k) for the number k of bonds emanating       CTQW on such structures have been investigated by Xu et
from a node does not need to be Poissonian in general. Net-         al. [98]. The network is generated from a triangle (N = 3 at
works for which the distribution P (k) follows a power-law,         generation g = 0). In generation g = 1 a single node is added
i.e., P (k) ∼ k −φ , are called scale-free networks (SFN), see      which is connected with all three nodes of g = 0, this divides
Fig. 25. These have been proven useful in various fields of re-     the triangle of g = 0 into three distinct triangles. In g = 2
search from biology to social sciences. Xu and Liu have con-        three new noded are added which are placed at the center of
sidered CTQW over such structures [97]. They distinguish            each of the three triangles of g = 1, see Fig. 26. These three
between deterministic scale-free networks (DSFN) and ran-           nodes divide each triangle of g = 1 into three new triangles,
dom scale-free networks (RSFN): the latter may obey distinct        such that there are now nine new triangles in total. The iter-
building procedures which can lead to either tree-like struc-       ation proceeds in the same manner, such that in generation G
tures or structures containing loops.                               the total number of nodes is N = 3 + (3G − 1)/2.
   For the DSFN, Xu and Liu determined the return probabli-            For G = 1 the Apollonian network is identical to the com-
ties πj,j (t) and long-time averages χk,j . They find that there    plete graph of size N = 4, therefore the transition probabil-
is a strong dependence of πj,j (t) on the initial node j, which     ities for CTQW are fully periodic. It also turns out that for
can even result in (almost) complete revivals of the initial con-   G = 2 (N = 7), see Fig. 26, and when choosing as the ini-
dition. The transition probabilities translate directly into the    tial node the central, most symmetric node 4, the transition
long-time averages χk,j , where one can identify clusters of        probabilities are also fully periodic, being namely [97]
nodes having the same χk,j . However, the patterns obtained
are quite distinct from the previously found patterns for the                       (                  
dendrimers [82] or for the Husimi cacti [88]. As mentioned                              37 + 12 cos(7t) /49 for k = 4
                                                                          πk,4 (t) =                                        (83)
earlier, this is a direct consequence of the fact that the χk,j                         2 − 2 cos(7t) /49       for k 6= 4.
mirror the topology of the network.
   For RSFN, Xu and Liu calculated the ensemble average                However, also here Xu et al. observe a strong dependence
over many realizations of individual RSFN [97]. In the ensem-       on the initial condition. If the initial node is not a central node
ble average the return probabilities do not oscillate but rather    being, say, node 1, the transition probabilities π1,1 (t) are still
reach a stationary value, which differs for different initial       periodic, although there is no perfect revival. Enlarging the
nodes. In all cases, however, this stationary value is roughly      networks lets the strong dependence on the initial condition
one order of magnitude larger than the classical equipartition      be more pronounced. But, similar to the dendrimers [82], Xu
value 1/N obtained for CTRW. Moreover, the higher the sym-          et al. also identify clusters of nodes which, in the long-time
metry of the initial node (where on average the central nodes       average, have the same value for their probabilities χk,j .
                                                                                                                                        21

                        V.   EXTENSIONS                             ∞, which yields E2 (θ) = πθ − θ2 /2, and one obtains
                                                                                               √ p           −1
           A. Systems with long-range interactions                                   ρ2 (E) = π 2 π 2 /2 − E     .                     (87)

                                                                    In the intermediate range there is an analytic solution for γ =
   So far the Hamiltonian for CTQW and the transfer ma-
trix for CTRW have been directly related to the connectiv-          4, namely E4 (θ) = θ4 /24 − πθ3 /6 + π 2 θ2 /6 (see Eq. 1.443.6
ity matrix. However, this matrix is purely topological (in-         of [75]), which yields [100]
dicating whether or not two nodes are connected) and does                         h            q         √             i−1
not take metric (i.e., distance dependent) aspects into account.        ρ4 (E) = 2π(2/3)1/4 E(π 2 / 24) − E 3/2            . (88)
Some adjustment is thus necessary if one considers distance-
dependent interactions. As an example, consider the net-            One assumes the following general form for the DOS in order
work being embedded in the d-dimensional space; then to ev-         to interpolate between ρ2 (E) and ρ∞ (E) [99]:
ery node j one associates a vector j whose coordinates are
                                                                                                    hq             i−1
{xj1 , . . . , xjd }. The distance between two nodes j and k is                        ργ (E) ∼       cγ E α − E β                     (89)
then given by the euclidean norm R ≡ |k − j|. Consider
now systems in which the interaction between the two nodes
j and k decreases with increasing distance. An example for          with α ∈ [0, 1] and β ∈ [1, 2]; cγ is a constant related to the
such a system could be a collection of dipoles, interacting via     maximal energy, cγ ≡ (Eγ,max )β−α .
dipole-dipole forces, whose potential decreases, to a good ap-         Having the DOS at hand, the integrals in Eqs. (30) and (31)
proximation, as R−3 . Now, in terms of the connectivity ma-         can be calculated - at least asymptotically - for large t. In the
trix, a node j is not only connected to its nearest neighbors       classical case Eq. (30) will be dominated by small values of
but also to other nodes. Thus, due to the decaying interaction      E when t becomes large. The DOS yields
potential the transition rates are not the same for all bonds but                            (
they depend on the distance.                                                                   t−1/2    for α = 1
                                                                                    pγ (t) ∼ α/2−1                               (90)
   Take as a first example a one-dimensional network with pe-                                  t        for α < 1.
riodic boundary conditions (i.e., a discrete ring) [99]. Here,
when the interactions go as R−γ , the Hamiltonian has the fol-      Quantum mechanically one knows that for the NN-case
lowing structure:                                                   π ∞ (t) ∼ t−1 , see for instance [73]. Considering now the
                                                                    other limiting case, γ = 2, one has [99]
       N R
       X X max                                       
Hγ =             R−γ 2|nihn| − |n − Rihn| − |n + Rihn| ,                             Z π2 /2
                                                                                                      exp(−iEt)
                                                                                                                         2

       n=1 R=1                                                          π 2 (t) =              dE    √ p                     ∼ t−1 .   (91)
                                                            (84)                      0             π 2 π 2 /2 − E
where Rmax is a cut-off for finite systems. Note, that in the
infinite system limit one first takes N → ∞ before taking also      Thus, the behavior for long times is the same for π 2 (t) and
Rmax → ∞. For the cases considered here, namely γ ≥ 2 and           π ∞ (t), which suggests that for all one-dimensional lattices
N of the order of a few hundred nodes, a resonable cut-off is       with extensive (γ ≥ 2) interactions the long time dynamics of
Rmax = N/2, which is also the largest distance between two          the excitations is similar, no matter how long- or short-range
nodes on the discrete ring. In this way, to each pair of sites a    the step lengths are. This is in contrast to the classical case,
single (minimal) distance and a unique interaction is assigned.     where only CTRW with γ > 3 belong to the same universality
   For all γ, the eigenstates are again the Bloch states |Ψθ i      class.
given above. The fact that the eigenstates are not affected by         These results are corroborated by analytically evaluating
the long-range interactions is due to the translational invari-     π γ (t) using the stationary phase approximation (SPA) [101].
ance along the ring. For other systems without such an invari-      For large N , αγ (t) can be written in integral form
ance the eigenstates will also change depending on the type of                                      Z 2π
the interaction. From the eigenstates one obtains the eigenval-                                 1
                                                                                    αγ (t) =               dθ exp(iEγ (θ)t).           (92)
ues which now do depend on the interaction range [99]:                                         2π    0

                        R
                        X max                                       The SPA asserts now that the main contribution to this in-
                                R−γ 2 − 2 cos(θR) .
                                                
             Eγ (θ) =                                       (85)    tegral comes from those points where Eγ (θ) is stationary
                         R=1                                        [dEγ (θ)/dθ ≡ Eγ′ (θ) = 0]. For γ = 2, E2 (θ) has only
                                                                    one stationary point in θ ∈ [0, 2π[, namely θ0 = π, leading to
  The DOS ργ (E) is obtained by inverting Eq. (85) and tak-
ing the derivative with respect to Eγ . In the NN-case (γ = ∞)                                                 1
one gets the known DOS                                                         π 2 (t) = |α2 (t)|2 ≈                     ∼ t−1 ,       (93)
                                                                                                           2πt|E2′′ (π)|
                              p              −1
                 ρ∞ (E) = π 4E − E 2             .         (86)     which does not show any oscillations and coincides with the
                                                                    long time limit of Eq. (91). For γ > 2, Eγ (θ) has two sta-
For γ = 2 one can approximate the sum by letting Rmax →             tionary points in the interval θ ∈ [0, 2π[, namely θ0 = 0 and
                                                                                                                                                                                                                 22

    (a) 100                                                                 (b)107                                                               It turns out that the Bloch states are also the eigenstates of this
                                                                                                 6
                                                                                               10
                                                            -1/2                                                                                 Hamiltonian: their eigenvalues read [102]

                                                                               classical MSD
                     -1
                10                                         ~t                                    5
                                                                                               10                  ~t
 CTRW
                                                                                                 4
                 -2                                                                            10
        pγ(t)   10                    -1                                                         3                                                                                 m
                                      t ~                                                      10                                                                                  X
                 -3
                10                                                                             10
                                                                                                 2

                                                                                                    1
                                                                                                                                                                   En = 2m − 2           cos(jθn ).            (97)
                 -4                                                                            10
                10
                                                                                               10
                                                                                                 0                                                                                 j=1
                          -1      0         1          2         3      4                               -1    0     1       2      3         4
    (c)              10          10        10         10        10    10    (d) 10                           10   10     10       10     10
                                                                                                                                                 Inserting these values into Eqs. (10) and (7) allows to study
                10
                     0                                               γ=∞                       10
                                                                                                 7

                                                 -1                  γ=4                       10
                                                                                                  6
                                                                                                                                                 the dependence of CTQW and of CTRW on m. As has been


                                                                            quantum MSD
                10
                     -1
                                            ~t                       γ=3                       10
                                                                                                  5

                                                                                                                                                 shown by Xu [102], increasing m results (as intuitively ex-
  CTQW
                                                                                                  4
                 -2                                                  γ=2                       10
    πγ(t)
                                                                                                  3                           2
                10                                                                             10
                 -3
                                                                                               10
                                                                                                  2                      ~t                      pected) in a faster transport, both for CTQW and CTRW.
                10                                                                                 1
                                                                                                10
                                                                                               10
                                                                                                  0                                              Morevoer, when considering the long-time average χkj , Xu
                 -4
                10                                                                             10
                                                                                                  -1
                                                                                                 -2
                                                                                                                                                 finds characteristic peaks which depend on m. Especially for
                                                                                               10 -1
                     10
                          -1      0
                                 10
                                            1
                                           10
                                                       2
                                                      10
                                                                 3
                                                                10    10
                                                                        4
                                                                                                  10
                                                                                                              0
                                                                                                             10   10
                                                                                                                    1
                                                                                                                         10
                                                                                                                            2      3
                                                                                                                                  10     10
                                                                                                                                             4
                                                                                                                                                 even N , the probability to be at the initial node and the proba-
                                            time t                                                                 time t
                                                                                                                                                 bility to be at the exactly opposite node, i.e., the node j ±N/2,
FIG. 27: (Color online) (a) Classical pγ (t) and (b) quantum mechan-                                                                             are not necessary equal [102], as it is the case for only nearest-
ical πγ (t) for a discrete ring with N = 10000 nodes with γ = 2, 3,                                                                              neighbor couplings. Depending on m, these two values may
4, and ∞. From [99].                                                                                                                             differ [102]: an explanation of this effect is still lacking.


θ0 = π. Then αγ (t) is approximately given by the sum of the                                                                                               B. Systems with disorder and localization
contributions of the two stationary points. Consequently [99],
                                                                                                                                                    In real physical systems, under the influence of the sur-
                                     1                              1          1                                                                 roundings, the couplings between the nodes may differ. In
                          π γ (t) ≈                                       +
                                    2πt                         |Eγ′′ (0)| |Eγ′′ (π)|                                                            a static picture, one can introduce disorder by adding to the
                                                                                                                  !                              unperturbed Hamiltonian H0 a disorder operator ∆, i.e., by
                            2 cos{t[Eγ (0) − Eγ (π)] + π/2}                                                                                      setting H = H0 + ∆ [103]. The disorder matrix ∆ = (∆l,j )
                          +         q                                                                                   ∼ t−1 .         (94)
                                      |Eγ′′ (0)Eγ′′ (π)|                                                                                         is taken to have non-zero entries only at the positions for
                                                                                                                                                 which Hl,j 6= 0. For different strengths of disorder, the el-
  The classical and quantum mean square displacements                                                                                            ements ∆l,j = ∆j,l are chosen randomly (drawn from a nor-
(MSD) are in line with these findings. Now, the MSD for                                                                                          mal distribution with the zero mean and unit variance, and
CTRW/CTQW on the discrete ring with initial site j are given                                                                                     then multiplied by a factor of ∆ which takes values from the
by [99]                                                                                                                                          interval [0, 1/2]). Note that under these assumptions for the
                                                                                                                                                 (static) disorder the connectivity of the graph is essentially
                                                                           N                                                                     unchanged, i.e., there are no new connections created nor are
                                                                     1 X           (γ)
                               hRγ2 (t)icl; qm =                         |k − j|2 Pk,j (t),                                             (95)     existing connections destroyed. Therefore, the only non-zero
                                                                     N                                                                           matrix elements of H are those of the initial A. The action of
                                                                       k=1
                                                                                                                                                 the new Hamiltonian H on a state |ji reads then
                          (γ)                    (γ)                                                              (γ)                  (γ)
where Pk,j (t) = pk,j (t) for CTRW and Pk,j (t) = πk,j (t)                                                                                                                    
for CTQW. Figure 27 shows numerical calculations of pγ (t)                                                                                                 H|ji = H0 + ∆ |ji
and π γ (t) for different γ and a discrete ring of N = 10000                                                                                               = 2|ji − |j − 1i − |j + 1i
nodes. Clearly, pγ (t) changes when increasing the step width
from NN steps to long-range steps, see Fig. 27(a). While pγ (t)                                                                                            +2∆j,j |ji − ∆j,j−1 |j − 1i − ∆j,j+1 |j + 1i.
for γ > 3 decays as t−1/2 , the power law changes to t−1 for                                                                                                                                                   (98)
γ = 2. In contrast, the decay of the maxima of the quan-                                                                                            In the following two cases of disorder are considered:
tum return probability π γ (t) follows t−1 for all γ, Fig. 27(c).                                                                                   (A) Diagonal disorder (DD), where ∆j,j 6= 0 and ∆l,j = 0
Long-range steps lead only to a damping of the oscillations                                                                                      for l 6= j. Here, a random number is assigned to each ∆j,j , a
and to an earlier interference once the excitation has propa-                                                                                    procedure which leads to N random numbers.
gated around half of the ring.                                                                                                                      (B) Diagonal and off-diagonal disorder (DOD), where a
   As an extension of the ring topology just discussed [99],                                                                                     random number is chosen for each ∆j,j and for each ∆j,j−1 .
Xu considered networks where not only the nearest neighbors                                                                                      For this, 2N random numbers are needed.
are connected but in which each node is connected to its 2m                                                                                         Introducing disorder into the system in this way has conse-
nearest neighbors [102]. This model differs from the one with                                                                                    quences for the relation between the CTQW and the CTRW.
long-range interactions, where the interaction decreases with                                                                                    In CTRW the transition rates, given by the entries of the the
the distance |k − j| between the nodes k and j.                                                                                                  transfer matrix T , are correlated, i.e., for each site the sum of
   Now the action of the Hamiltonian on state |ji reads                                                                                          the non-diagonal rates for transmission from it and the diag-
                                                                                                    m
                                                                                                    X                                            onal rate of leaving it are the same. In the cases considered
                                H|ji = (2m + 1)|ji −                                                          |j + zi.                  (96)     here, a direct identification of the Hamiltonian H with a clas-
                                                                                                z=−m                                             sical transfer matrix is not possible anymore. However, the
                                                                                                                                   23

 (a) N=100                                                           diffusive behavior ∼ t [104].
                        0.4




 Σκ〈Wj(x,κ;t=100)〉R
                                  (a)
                        0.3
                                                      ∆=1/40                      VI. SYSTEMS WITH ABSORPTION
                        0.2                           ∆=1/10
                                                      ∆=1/4
                                                      ∆=1/2             In general, an excitation does not stay forever in the sys-
                        0.1
                                                                     tem in which it was created; the excitation either decays (ra-
                         0                                           diatively or by exciton recombination) or, e.g., in the case of
                              0         25     50     75       100
                                             node x                  biological light-harvesting systems, it gets absorbed at the re-
 (b) N=101                                                           action center, where it is transformed into chemical energy. In



 Σx〈Wj(x,κ;t=100)〉R
                      0.011
                                  (b)                                such cases, the total probability to find the excitation within
                                                                     the network is not conserved. Such loss processes can be mod-
                                                                     elled phenomenologically by changing the transfer matrix or
                       0.01
                                                                     the Hamiltonian [50, 105–107]. To fix the ideas, we consider
                                                                     networks in which the excitation can only vanish at certain
                                                                     nodes. These nodes will be called trap-nodes or traps. In the
                      0.009                                          absence of traps, let the transfer matrix and the Hamiltonian of
                              0         25     50     75       100
                                               κ                     the corresponding network be T0 and H0 , respectively. Take
                                                                     now M out to the N total nodes to be traps and denote them
FIG. 28: (Color online) Long-time average χk,j for different ∆ and   by m, so that m ∈ M, with M ⊂ {1, . . . , N }. The trapping
(a) N = 100 and (b) N = 101. From [103].                             process is now modelled by introducing a trapping matrix Γ
                                                                     which is given by a sum over all trap nodes; Γ has only diag-
                                                                     onal elements, i.e.,
DOD and DD Hamiltonians are widely used in quantum me-                                           X
chanical nearest-neighbor hopping models, to which also the                                 Γ≡       Γm |mihm|                   (99)
CTQW belong. Furthermore, we still consider transport pro-                                          m
cesses on graphs which have the connectivity matrix A, but
the direct connection between H and T is lost.                       (in the following one assumes that Γm = Γ > 0 for all m).
   Now, consider again rings of N nodes, where at time t =              CTRW with decreasing exciton probabilities due to trap-
0 the excitation is assumed to be localized at node j. The           ping are well described through the following transfer matrix:
above system is similar to the Anderson model [11], which
                                                                                                  T ≡ T0 − Γ.                    (100)
has been found to show (strong) localization around the initial
condition. The same happens here. In the ensemble average
                                                                     The total Hamiltonian H corresponding to trapping is then:
as well as for single realizations, an excitation starting at j
remains localized in the vicinity of j [103]. This effect is best                                 H ≡ H0 − iΓ.                   (101)
seen in the long-time average. Figure 28 shows χk,j for two
different ring sizes, N = 100 and N = 101, and varying               Note that the connection between CTRW and CTQW is now
∆. Clearly, the larger is ∆ the more is the long time average        less direct than before. For CTRW the term corresponding to
localized around the initial node j = 50.                            trapping has only real elements and the total transfer matrix
   Quantum walks in random linear environments were also             stays real. For CTQW, however, the trapping term has purely
studied by Yin et al. [104]. They calculated numerically             imaginary elements. As a result, H is non-hermitian and has
the quantum carpet structures for DD. It turns out that in the       N complex eigenvalues, El = ǫl −iγl (l = 1, . . . , N ). In gen-
course of time the excitation stays localized around its initial     eral, H has N left and N right eigenstates |Φl i and hΦ̃l |, re-
node; also depending on the strength of the disorder, some           spectively. It turns out that in most cases the eigenstates of H
structure of the original quantum carpets may still remain vis-      form a complete and biorthonormal set, see, e.g., Ref. [108],
ible.
   Yin et al. also studied dynamic diagonal disorder, where the           N
                                                                          X
diagonal elements of H are rapidly varying with time and the                    |Φl ihΦ̃l | = 1      and    hΦ̃l |Φl′ i = δll′   (102)
update of (H)jj is done at times comparable or much smaller               l=1
than the time step of the numerically determined dynamical
                                                                     Both, eigenvalues and eigenstates, will be different for CTRW
changes [104]. For dynamic disorder, the interference patterns
                                                                     and CTQW, because the incorporation of the trapping process
making up the quantum carpets are washed out. However, dis-
                                                                     is different.
tinct from the case of static disorder, no localization can be
                                                                        If the trapping strength Γ is small compared to the cou-
seen. Moreover, after the temporal range in which interfer-
                                                                     plings between neighboring nodes, perturbation theory allows
ence is lost, the dynamics becomes classical. This crossover
                                                                     to relate the real part of the eigenvalues to the eigenvalues of
behavior is also observed in the mean square displacement,                                                       (0)
which changes in a certain time range - depending on the             the unperturbed Hamiltonian H0 . Let |Ψl i be the lth eigen-
                                                                                   (0)
strength of disorder - from the ballistic behavior ∼ t2 to the       state and El ∈ R be the lth eigenvalue of the unperturbed
                                                                                                                                                  24

system with Hamiltonian H0 . Up to first-order, the eigenval-                        Such long times are not of much experimental relevance
ues of the perturbed system are given by [105]                                    (see also below), since most measurements highlight shorter
                                                                                  times, at which many γl contribute. In the corresponding en-
                                                                   2
          (0)         (1)      (0)                           (0)                  ergy range the γl often scale, so that in a large l range one finds
                                            X
  El = El         + El      = El     − iΓ           hm|Ψl i .             (103)
                                            m∈M
                                                                                  γl ∼ alµ . The prefactor a depends only on Γ and N [109].
                                                                                  For densely distributed γl and at intermediate times one has,
Therefore, the correction term determines the imaginary parts                     from Eq. (107), [50]
γl , while the unperturbed eigenvalues are the real parts ǫl =                                             Z
   (0)                                                                                                                    µ
El . Moreover, the imaginary parts are solely determined                                      ΠM (t) ≈       dx e−2atx
by the contribution of the eigenstates of the network without
                                                                                                                          µ
traps at the trap nodes m.                                                                                           e−y
                                                                                                           Z
                                                                                                       =     dy                ∼ t−1/µ .       (108)
                                                                                                                  (2at)−1/µ
                   A. Average survival probability                                  Analogously, the mean survival probability for CTRW is
                                                                                  given by
   In an ideal experiment one would excite exactly one node,
say j 6∈ M, and read out the outcome πkj (t), i.e., the proba-                                                   1  X X
                                                                                               PM (t) ≡                 pkj (t).               (109)
bility to be at node k 6∈ M at time t. However, it is easier to                                                N −M
                                                                                                                        j6∈M k6∈M
P track of the total outcome at all nodes k 6∈ M, namely of
keep
   k6∈M πkj (t). Since the
                        P
                           states |ki form a complete, orthonor-
                                               P                                  If the smallest eigenvalue, λ1 , is well separated from the rest,
mal basis set one has k6∈M |kihk| = 1 − m∈M |mihm|,                               PM (t) turns very quickly into a simple exponential decay.
which leads to [50]:                                                              Then, for not too small times, it can be shown that [105]
                                                                                                             1                  2
           X              X
                πkj (t) =      |αkj (t)|2
                                                                                                                       X
                                                                                              PM (t) ≈          e−λ1 t   hk|q1 i .             (110)
         k6∈M                k6∈M                                                                          N −M
                                                                                                                            k6∈M
             N                                  N
             X                                  X                  ∗
         =         e−2γl t hj|Φl ihΦ̃l |ji −             e−i(El −El′ )t
             l=1                               l,l′ =1                                                    B.   Regular networks
             X
         ×          hj|Φl′ ihΦ̃l′ |mihm|Φl ihΦ̃l |ji.                     (104)
             m∈M
                                                                                                           1. Ring with traps

   By averaging over all j 6∈ M, the mean survival probability                       Some of the nodes of a ring of N nodes are now taken to
is given by [50]                                                                  be traps. Depending on the particular choice of trap arrange-
                    1        X X                                                  ments, the average survival probability ΠM (t) shows different
      ΠM (t) ≡                        πkj (t)               (105)                 features [106].
                N −M                                                                 As already discussed, the eigenstates of the ring without
                            j6∈M k6∈M
                 ( N                                                              traps are Bloch states. Furthermore, if the trapping strength is
           1       X            h          X                 i
      =                  e−2γl t 1 − 2        hΦ̃l |mihm|Φl i                     small compared to the interaction strength between the nodes,
        N −M                                                                      the imaginary parts of the Hamiltonian of a network with traps
                    l=1                  m∈M
         N                    h X                    i2
                                                        )                         are given by the contributions of the eigenstates at the trap po-
               −i(El −El∗′ )t                                                     sitions, see Eq. (103). However, since all eigenvalues except
        X
      +      e                      hΦ̃l′ |mihm|Φl i      . (106)
        l,l′ =1                    m∈M
                                                                                  E1 = 0 (and for even N also except EN/2 = 4) are two-fold
                                                                                  degenerate, some care is in order when applying perturbation
   For long t and small M/N , Eq. (106) simplifies con-                           theory.
siderably: At long times the oscillating term on the                                 Take now N to be even. Then, for l = 1 and for l = N/2
right hand side drops out and for small M/N one has                               one has
  P
2 m∈M hΦ̃l |mihm|Φl i ≪ 1. Thus, ΠM (t) is mainly a sum                                                                               2
                                                                                                    (1)                         (0)
                                                                                                                  X
of exponentially decaying terms [50]:                                                             El      = −iΓ           hm|Φl i .            (111)
                                                                                                                  m∈M
                                        N
                               1  X
                ΠM (t) ≈            exp[−2γl t].                          (107)   Furthermore,
                             N −M
                                       l=1
                                                                                                          M                           M
   Asymptotically, Eq. (107) is dominated by the γl values                               E1 = 4 − iΓ            and EN/2 = −iΓ          .      (112)
                                                                                                          N                           N
closest to zero. If the smallest one, γmin , is well separated
from the other values, one is led for t ≫ 1/γmin to the expo-                     For l different from 1 and from N/2 one sets
nential decay found in earlier works, ΠM (t) = exp(−2γmint)
                                                                                                                  (0)          (0)
[109].                                                                                                 Vi,j ≡ hΦi | − iΓ|Φj i                  (113)
                                                                                                                                       25

and applies the expression valid for two-fold degenerate solu-         (a) periodic arrangement of traps
tions of H0 [106]:

            (1)1
          El = (Vl,l + VN −l,N −l )
               2
           1h                   2
                                                i1/2
          ± (Vl,l − VN −l,N −l ) + 4|Vl,N −l |2      , (114)
           2
where one takes the positive sign for l ∈ [1, N/2 − 1] and the
negative sign for l ∈ [N/2 + 1, N − 1]. Now one has
                                                                       (b) sequential arrangement of traps
                                            M
                  Vl,l ≡ VN −l,N −l = −iΓ     ,            (115)
                                            N
independently of the trap arrangement and
                         M
                      Γ X
       Vl,N −l = −i         exp{2iπmj [l − (N − l)]/N }
                      N j=1
                  M
               Γ X
       = −i          exp(4iπlmj /N ).                      (116)
               N j=1

Inserting the last results into Eq. (114) yields [106]              FIG. 29: Periodic (a) and sequential (b) arrangements of traps on a
                                                                  ring.
                                 M
          (1)    −iΓ           X
        El =             M±          e2iπ2lmj /N  .       (117)
                  N             j=1

                                                                                           0
                                                  (1)                                     10
Notice that for special trap arrangements the El can be cal-                                                               ΠM (t)
culated exactly: The most striking results are obtained when                                                               PM (t)
the exponential in the sum in Eq. (117) equals one of the val-
ues from the set {1, i, −1, −i}. Then the absolute value of the
                 PM                                                                        −1
sum reduces to | j=1 exp(i4πlmj /N )| = M .                                               10



                                                                         ΠM (t), PM (t)
                                                                                                                            M=10
   Now, for a single trap, which without loss of generality is
                                             (1)
placed at position mj = j = 1, one has El = −iΓ/N [1 ±
                                       (1)
exp(i4πl/N )]. Therefore, one has El = 0 for l = N and                                     −2
for l = N/2. As a consequence, ΠM (t) will not decay to zero                              10
but to a constant value given by 1/(N − 1).
   Another example is a periodic distribution of traps with                                              M=75
mj = jN/M , while N/M ∈ N, see Fig. 29(a). Then it is
straightforward to show that if 2l/M ∈ N the sum in Eq. (117)                              −3
                                                                                          10
equals one of the values from the set {1, i, −1, −i}. The total                                0   500              1000        1500
                                                                                                                t
number of such values is given by [106]                                                                   time t

                                                                    FIG. 30: Survival probabilities ΠM (t) (continuous line) and PM (t)
              
                  ⌊(N − 2)/M ⌋ for even M,
        |Υ| =                                            (118)      (dotted lines) on a ring of size N = 300 and Γ = 0.01 in the pres-
                 ⌊(N − 2)/2M ⌋ for odd M,
                                                                    ence of M = 10 and of M = 75 traps arranged periodically, i.e.
                                                                    mj = jN/M . Note the semilogarithmic scales. From [106].
where ⌊x⌋ denotes the largest integer less than or equal to x.
In particular, for both M = 1 and M = 2, |Υ| = N/2 − 1.
Hence, for large structures with M ≪ N , ΠM (t) decays
asymptotically to 1/M (even case) and to 1/(2M ) (odd case).
Figure 30 shows results obtained for a ring of size N = 300         they never “see” the traps. This genuine quantum-mechanical
with a periodic arrangement of M = 10 (|Υ| = 29) and                effect has no counterpart in the classical world where, for fi-
M = 75 (|Υ| = 1) traps. Consequently, the survival prob-            nite structures, the survival probability always decays to zero
ability ΠM (t) decays to the constant values 1/10 and 1/225,        in the presence of traps. In particular, as shown in Fig. 30,
respectively. From a physical point of view, the finite limit for   PM (t) decays exponentially, as expected.
the survival probability stems from the existence of station-
ary states to which the nodes in M do not contribute, so that         For a sequential arrangement of traps, such that mj = j
                                                                                                                                                            26

                                                                                                  -2
                                                     N = 32, Γ = 0.04                            10
                                                     N = 48, Γ = 0.01                                                                                   0.51
                                                                                                  -3
               −2
              10                                     N = 64, Γ = 0.01                            10                                                     0.5
                                                     N = 96, Γ = 0.004                                                                                  0.49
                                                                                                      10        label l             90
               −4                                                                     0.02
              10

    Π M (t)                                                                      γl
               −6                                                                     0.01
              10
                                                                                                                                              1.865
                                                                                                                                    γl ~ - l
               −8
                                                                                        0
              10                                                                             0             20   40             60        80           100
                                                                                                                     label l

               −10
              10                                                                 FIG. 32: (Color online) Imaginary parts γl (dots) in ascending order
                               1000         2000     3000    4000                for N = 100 and Γ = 1. Note the shortened y axis. The inset shows
                                            timett                               γl in log-log scale for l = 10, . . . , 90. From [50].

FIG. 31: Survival probability ΠM (t) on rings of size N = 32, 48, 64
and 96 with a sequential arrangement of M = N/2 traps for Γ =                    Without loss of generality, an eigenstate of the finite chain
0.04, 0.01, 0.004, as indicated.The straight lines represent Eq. (121).
                                                                                 without traps can be written as (l = 1, . . . , N ) [105]
From [106].
                                                                                          r    N
                                                                                             1 X
                                                                                                   |ji                   for l = N
                                                                                          
                                                                                          
and j = 1, ...., M , see Fig. 29(b), Eq. 116 can be written as                            
                                                                                           N
                                                                                          
                                                                                     (0)       j=1
                                      M                                            |Ψl i = r    N
                                      X                                                     2 X
        Vl,N −l = −iΓ/N                     exp(4iπlj/N )
                                                                                                                   
                                                                         (119)            
                                                                                          
                                                                                          
                                                                                           N      cos (2j − 1)θl /2 |ji else,
                                      j=1                                                      j=1
                 −iΓ exp(4iπlM/N ) − 1                                                                                                      (123)
               =                        exp(4πil/N )                             where for convenience one takes θl ≡ π(N − l)/N ∈ [0, π[;
                  N   exp(4πil/N ) − 1                                                                                    (0)
                 −iΓ sin(2πM l/N )                                               the corresponding eigenvalues are El = 2 − 2 cos θl (note
               =                   exp[2iπl(M + 1)/N ],                                                               (0)
                                                                                 that the smallest eigenvalue is EN = 0). Thus, first order
                  N   sin(2πl/N )
                                                                                 perturbation theory yields from Eqs. (103) and (123) as imag-
which yields                                                                     inary parts γN = 2Γ/N and γl = (4Γ/N ) cos2 θl /2 for
                                                                                                                                             

                                                                                 l = 1, . . . , N − 1. Indeed, for l ≪ N this means that γl ∼ l2 ,
                                                       
                     (1)       −iΓ        sin(2πM l/N )
                    El     =           M±                 .              (120)   so that the average survival probability scales in the corre-
                                N           sin(2πl/N )
                                                                                 sponding time interval as ΠM (t) ∼ t−1/2 , see Eq. (108).
Notice that since l 6= N/2 and l 6= N then 2l/N ∈   / N, while                      If the trapping stength increases, one cannot employ pertur-
                        (1)     (1)
for 2lM/N ∈ N then El = EN −l = −iΓM/N . In particu-                             bation theory anymore. Nevertheless, one can always calcu-
lar, when M = N/2, γl = M/N for each value of l ∈ [1, N ].                       late the eigenvalues of H numerically. As it will turn out, the
As a result, and by neglecting oscillations, one has [106]                       scaling γl ∼ lµ still holds in this case and extends even over
                         M                                                       a wider range of l-values. Figure 32 shows the spectrum of
                    ΠM (t) ≈  e−2ΓtM/N ∼ e−Γt ,         (121)                    γl for N = 100 and Γ = 1; the double logarithmic plot (see
                      N −M
                                                                                 inset) demonstrates that scaling holds for 10 ≤ l ≤ 60, where
which is independent of N . As shown in Fig. 31, the expo-                       the exponent µ is about µ = 1.865.
nential behaviour predicted by Eq. (121) holds also for inter-                      Figure 33 compares, for a linear system with N = 100 and
mediate times.                                                                   Γ = 1, the classical PM (t) to the quantum mechanical sur-
                                                                                 vival probability ΠM (t) [50]. Evidently, PM (t) and ΠM (t)
                                                                                 differ strongly: the PM (t) decay established for CTRW is
                                 2.    Line with traps
                                                                                 practically exponential. ΠM (t), on the other hand, shows two
                                                                                 regimes: a power-law decay at intermediate times (panel (a))
   An example of a network with traps which allows to study                      and an exponential decay (panel (b)) at very long times.
different time scales is a finite line of nodes with traps at each                  Turning now to the parameter dependences of ΠM (t),
end. The Hamiltonian is thus [50]                                                Fig. 34 shows the dependence of ΠM (t) on N [50]. Note that
                     N
                     X −1                                                      the scaling regime, where ΠM (t) ∼ t−1/µ holds, gets larger
       H =                     2|nihn| − |n − 1ihn| − |n + 1ihn|                 with increasing N . The cross-over to this scaling region from
                     n=2                                                         the domain of short times occurs around t ≈ N/2. For larger
                     +|1ih1| − |2ih1| + |N ihN | − |N − 1ihN |                   N and in the intermediate time domain, ΠM (t) scales nicely
                                                                               with N . In this case, the power-law approximation [Eq. (108)]
                     +iΓ |1ih1| + |N ihN | .                   (122)             holds and by rescaling l to l/N one has from Eq. (107) that
                                                                                                                                                                                                    27

 (a)               10
                        0                                                                                     (a)          0
                                                                                                                      10




   ΠM(t) ; PM(t)
                        -1
                   10
                                                     ΠM(t)                                                    ΠM(t)   10
                                                                                                                           -1
                                                                                                                                             -0.538
                    -2                               ~t
                                                       -0.538                                                                            ~t
                   10                                PM(t)                                                                               N = 20
                                                                                                                                         N = 100
                    -3                                                                                                 -2
                   10           0           1                2             3              4            5              10        0            1                2               3               4     5
                        10                 10           10                10            10           10                    10           10                   10              10              10   10
 (b)               10
                        0                                                                                                                                          time t
                                                                               ΠM(t)                           (b)         0




   ΠM(t) ; PM(t)
                                                                                               -5
                                                                                                                      10
                        -1                                                     ~ exp(-1.59*10 t)
                   10
                                                                               PM(t)


                                                                                                              ΠM(t)
                    -2                                                                                                     -1
                   10                                                                                                 10

                    -3
                   10
                            0           20000         40000            60000           80000        100000
                                                                 time t                                                -2
                                                                                                                      10        -2               -1                      0               1          2
                                                                                                                           10                10                10                       10        10
                                                                                                                                                                        3-µ
FIG. 33: (Color online) Temporal decay of ΠM (t) (solid black lines)                                                                                   rescaled time t/N
and PM (t) (short dashed green lines) for N = 100 and Γ = 1 in (a)
double logarithmic scales and in (b) logarithmic scales. Indicated are                                       FIG. 34: (Color online) Panel (a) shows the N -dependence of ΠM (t)
the fits to ΠM (t) (long dashed lines) in the intermediate (upper red)                                       for Γ = 1; N increases in steps of 10 from 20 (blue line) to
and the long (lower blue) time regime. From [50].                                                            100 (green line). Panel (b) shows ΠM (t) versus the rescaled time
                                                                                                             t/N 3−µ . From [50].

[50]
                                            X                −3 µ
                                                                                                             where Hν contains only the correction terms to the NNI case
                    ΠM (t) ∼                        e−2N         l t
                                                                                                             H0 . This allows one to calculate from the unperturbed states
                                                                                                                (0)
                                                l
                                                       h                     i                               |Ψl i the perturbed eigenstates |Ψl i up to first order. Taking
                                                                                                             the states |Ψl i to be the eigenstates of the LRI system with-
                                            X
                                       =            exp − 2(l/N )µ N −(3−µ) t ,
                                                l                                                            out traps, one readily obtains the imaginary parts γl for small
                                                                                                                                                                    2
                                                                                                     (124)   trapping strength from Eq. (103) as γl = 2Γ h1|Ψl i , where
                                                                                                             [105]
where it was assumed that a ∼ N −3 for a linear system [109].
Thus, when rescaling l to l/N , the time has to be rescaled by                                                                         (0)
                                                                                                                                                      X hΨ(0)
                                                                                                                                                          r |Hν |Ψ
                                                                                                                                                                   (0)
                                                                                                                                                                       i
the factor N −(3−µ) . Indeed, all curves for which a power-                                                    h1|Ψl i = h1|Ψl i +                                 (0)
                                                                                                                                                                                   l
                                                                                                                                                                                  (0)
                                                                                                                                                                                        h1|Ψ(0)
                                                                                                                                                                                            r i. (126)
                                                                                                                                                      r6=l        El     − Er
law behavior is visible fall on a master curve; see the inset in
Fig. 34.
                                                                                                                For large ν the coupling to the next-next-nearest neighbor is
                                                                                                             by a factor of (3/2)ν smaller, for ν = 10 this is about one and
                        3.          Line with traps and long-range interactions                              a half orders of magnitude. Taking, for fixed ν, only nearest
                                                                                                             and next-nearest neighbor couplings into account allows one
                                                                                                             to obtain simple analytic expressions. Thus, Eq. (126) yields
   As mentioned above, the interaction range does not need to
be restricted to nearest neighbor interactions (NNI). When the                                                                     r
                                                                                                                                       2      θ 
                                                                                                                                                 l
interactions between two nodes go as R−ν , the Hamiltonian of                                                          h1|Ψl i =         cos
the networks without traps has the following structure [105]:                                                                         N         2
                                                                                                                                          r                  θ 
                                                                                                                                       −ν    2                 l
                    N
                        " n−1                                                                                                      +2           sin 2θl sin        ,   (127)
                   X X                                                                                                                     N                 2
        H0 (ν) =              R−ν |nihn| − |n − Rihn|
                                         n=1        R=1                                                      (θl ≡ π(N − l)/N ∈ [0, π[) which results in [105]
                            N −n
                                                                #
                            X                                
                                        −ν
                   +                  R    |nihn| − |n + Rihn| .                                     (125)                           γl ≈ γl
                                                                                                                                             (0)
                                                                                                                                                      + 2−ν γl
                                                                                                                                                                   (1)
                                                                                                                                                                         + O(2−2ν ),              (128)
                             R=1
                                                                                                                           (0)
Note that in the case of a line, the states |ki with k ∈    /                                                where γl is the NNI expression, discussed in Sec. VI B 2,
                                                                                                                   (1)                                      
{1, . . . , N } are implicitly excluded from the summation.                                                  and γl = (8Γ/N ) cos θl /2 sin 2θl sin θl /2 is the cor-
  For large exponents ν the LRI can be regarded as a small                                                   rection due to the LRI. The smallest γl -values are those for
perturbation to the NNI, i.e., having H0 (ν) = H0 + Hν ,                                                     which l ≪ N , which leads to a decrease of the imaginary
                                                                                                                                                                                                       28

   (a) Γ=0.001
                                                                                                                    0
        (a)                                                                                                     10
                                                                                                          NNI
     5x10
                 4
                               6x10
                                      4
                                                7x10
                                                            4                                             ν=5
                                                                                                          ν=4
                                                                                                          ν=3

                                                                                                                        ΠM(t) ; PM(t)
                                                                                                                    -1
                                                                                                                10

                                                                          0.3
                                                            ΠM(t)                                     ΠM(t)         -2
                                                                                                                10
                                                                                PM(t)
                                                            PM(t)                                                                                                  trap nodes
                                                                          0.2
                                                                                                                    -3
                     1            2             3                4              5            6        7         10
                                                                                                                8
                 10            10             10                10            10           10     10          10
   (b) Γ =1
                                                                     time t
                     0                1                 2                 3              4        5             6                       FIG. 36: Examples of two regular hyperbranched fractals of genera-
        (b) 10                  10                 10                    10           10         10           10 0
                                                                                                                10                      tion g = 3 with functionalities f = 3 (left) and f = 4 (right).
                                                                                                          NNI
                                                                                                          ν=5
                                                                                                          ν=4


                                                                                                                        ΠM(t); PM(t)
    10
        0                                                                                                 ν=3   10
                                                                                                                    -1


                                                                                                                                        N = 100 five nodes randomly as trap nodes, Xu has shown
                                                   ~t
                                                        -1/µ
                                                                                                                    -2
                                                                                                                                        numerically that both the CTQW and the CTRW survival
                                                                                                                10
                                                                                                                                        probabilities decay with increasing m [110], thus showing an
                                                                                                      ΠM(t)
        -1
   10                     ΠM(t)
                                                                              PM(t)                                                     opposite effect to that mentioned above. However, an expla-
                                                                                                                10
                                                                                                                    -3                  nation was not given.
     -2
   10        1            2               3         4                5
                                                                                time t
         10              10         10          10              10


FIG. 35: (Color online) ν-dependence of the quantum mechanical                                                                                                    C. Fractals
ΠM (t) and the classical PM (t) decay behaviors for a chain of N =
100 sites; here (a) Γ = 0.001 and (b) Γ = 1. The inset in (a) shows
a close-up picture of the region where ΠM (t) and PM (t) cross. The                                                                                        1.   Hyperbranched fractals
inset in (b) shows power-law fits to ΠM (t) in the intermediate time
regime with exponents 1/µ, where the µ are taken from Fig. 3(b) of                                                                         Unlike the regular network discussed in the previous sec-
Ref. [105]. From [105].                                                                                                                 tions, hyperbranched fractals allow one to study the survival
                                                                                                                                        probability in the presence of highly degenerate eigenvalues.
                                          (1)                                                                                           Volta investigated so-called regular hyperbranched fractals,
parts γl because γl < 0 for l ≪ N . Here, one can approx-                                                                               see Fig. 36, for which the eigenvalue spectra of the connec-
imate the imaginary parts by a power-law, i.e., γl ∼ lµ . A                                                                             tivity matrices can be calculated recursively [111]. As shown
rough estimate of the scaling exponent µ, assuming ν ≫ 1,                                                                               previously [112], the eigenvalues of the (g + 1)st generation
can be readily given [105]:                                                                                                             can be obtained from the eigenvalues of the gth generation by
                               ln γl+1 − ln γl                                                                                          solving
                 µ≈                            ≈ µ(0) + 2−ν µ(1) .                                                        (129)
                              ln(l + 1) − ln l
                                                                                                                                                                P (λg+1 ) = λg ,                    (130)
                 (1)
Since µ is strictly positive for small l, the inclusion of LRI
leads to a decrease of γl when compared to the NNI case. In                                                                             where P (λ) = λ(λ − 3)(λ − f − 1), f being the functionality
turn, this results in a slower decay of ΠM (t).                                                                                         of the fractal. The three roots of the polynomial are given by
   Figure 35 displays for comparison the quantum mechanical                                                                             the Cardano solutions [112]
ΠM (t) and the classical PM (t) behaviors for different ν and
Γ; ΠM (t) and PM (t) were obtained by numerically diagonal-                                                                                     f +4 2
                                                                                                                                                    + |f (f − 1) + 7|1/2 cos (φ + 2πj)/3 , (131)
                                                                                                                                                                                       
                                                                                                                                         λj =
izing the corresponding Hamiltonian H(ν) and transfer ma-                                                                                         7  3
trix T (ν), respectively [105]. Clearly, for both Γ-values the
LRI lead to a slower decay of ΠM (t), i.e., to a slower trapping                                                                        with j = 1, 2, 3. Thus, each eigenvalue of the gth generation
of the excitation, which is somewhat counterintuitive since the                                                                         gives rise to three new eigenvalues, not all of which are dif-
opposite effect is observable for classical systems, where the                                                                          ferent from the previous ones. Therefore, there appear highly
decay of PM (t) becomes faster for decreasing ν, see below.                                                                             degenerate eigenvalues, e.g., the eigenvalue λ = 1 has in the
By increasing the trapping strength Γ, the difference between                                                                           gth generation the degeneracy ∆g = (f − 2)(f + 1)g−1 + 1.
the quantum and the classical behaviors become even more                                                                                   Placing now a trap node at the center of the fractal, Volta is
pronounced, compare Figs. 35(a) and 35(b). Generally, for                                                                               able to calculate the (complex) spectrum of the Hamiltonian
ΠM (t) a change in Γ leads mainly to in a rescaled time axis,                                                                           including the trap [111]. It turns out that only the nondegener-
since the imaginary parts γl turn out to be of the same order                                                                           ate eigenvalues depend on the trapping strength Γ. Thus, the
of magnitude when rescaled by Γ.                                                                                                        degenerate eigenvalues can be again calculated based on the
   Xu has studied a ring where the interaction strength does                                                                            Cardano solution. In particular, these eigenvalues are real and,
not decay with distance, as in [105], but ranges from a given                                                                           therefore, do not contribute to the decay of the survival prob-
node to the m nearest neighbors [110]. By choosing for                                                                                  ability. At generation g there are (3g − 1)/2 + (f + 1)g − 3g
                                                                                                                                  29

real degenerate eigenvalues, such that Eq. (107) yields
                     1 h g
       ΠM (t) ≈           (3 − 1)/2 + (f + 1)g − 3g
                   N −1                                                                                     position
                                                                                                            trap
                                                                                                               of trap
                     X               i
                   +     exp(−2γl t) .                  (132)
                     γl 6=0

Clearly, in the limit of t → ∞ this leads to a constant value.
As Volta also shows (extending the results for the line), in-
creasing the trapping strength above the value of Γ = V = 1
does not lead to a faster ΠM (t) decay.


                    D. Random networks

              1.   Disordered system with one trap
                                                                    FIG. 37: Random configuration of 99 nodes and a single trap. From
                                                                    [107].
  Introducing long-range interactions also allows one to study
topologically disordered systems. To illustrate this, take a ran-
dom configuration of (N − 1) identical nodes and one trap           cases were considered: (a) Γ = 10−6 , for which a perturba-
node [107], see Fig. 37. All N nodes are placed at random in        tion theoretical treatment can be justified, and (b) Γ = 1, such
a 3-dimensional box with Cartesian coordinates {x(i) }, with        that the average trapping strength is of the same order as the
i = 1, 2, 3. Then the distance between two nodes j and k is         diagonal elements of H0 at the node of the trap.
given by                                                               While each realization Π(t) r leads to a specific spectrum
                                                                             
                       " 3                      #1/2                of the γl r , the relation between hΠ(t)iR and the average
                        X         (i)  (i) 2
                                                                    hγl iR is not that straightforward. However, for all t, the func-
              Rj,k =             xj − xk               ,   (133)    tion exp(−2γl t) is convex, therefore, Jensen’s inequality ap-
                         i=1                                        plies, see paragraph 12.41 of [75], such that one obtains for a
                          (i)          (i)                          given l [107]
where the coordinates xj and xk are homogeneously dis-                                                                 
tributed random numbers in the interval [0, N ]. To relate this                    exp(−2γl t) R ≥ exp − 2thγl iR .             (136)
to the energy transfer dynamics within Rydberg gases one
                                     −3
considers interactions decaying as Rj,k . In the absence of         From this one gets a lower bound for Π(t) R :
traps the corresponding Hamiltonian H0 has the following                                         N
matrix elements                                                                              1 X               
                                                                                 Π(t) R ≥        exp − 2thγl iR .              (137)
                                                                                             N
                             −3                                                                 l=1
                         X−Rj,k     for k 6= j
             hk|H0 |ji =       R −3
                                     for k = j.          (134)         In Fig. 38 hΠ(t)iR is displayed for the two values Γ =
                                j,k
                         
                                k6=j
                                                                    10−6 and Γ = 1, for different N . In all cases the intermediate
                                                                    time decay can be fitted by a power-law [107]
Now, choose one of the N nodes to be a trap, i.e., for this
node the full Hamiltonian H has an additional purely imag-                                hΠ(t)iR ∼ t−η(N ) ,                  (138)
inary matrix element −iΓ. Since the configuration of nodes          where, different from the regular linear case [50, 105], the ex-
is random, one can (without any loss of generality) assume in       ponent η is now N -dependent. It turns out that approximating
the following that the node labeled 1 is the trap.                  the exponent by
   For disordered systems, one calculates averages over R dif-
ferent realizations following again, as for the SWN,                                        η(N ) = η0 N µ ,                   (139)
                                    R                               while keeping Γ fixed, reproduces the curves well. Note, how-
                                 1 X 
                       · R≡            · r,                (135)    ever, that η0 and also µ can still depend on Γ.
                                 R r=1                                Now, one can estimate µ based on the results of η for
                                                                  N1 = 100 and N2 = 1000. Based on η0 = η(N1 )/N1µ =
where · r denotes the realization r. In the calculations one
                                                                  η(N2 )/N2µ one has [107]
also assumes the trapping strength Γ r to be realization de-
                                                                                           ln η(N2 ) − ln η(N1 )
pendent, because it is required
                               that it be proportional to the                        µ=                         .             (140)
diagonal element h1|H0 |1i r in that particular realization,                                   ln N2 − ln N1
                            
namely Γ r ≡ Γ h1|H0 |1i r . As it turns out, the depen-            From the numerical values given in Fig. 38 one obtains ap-
dence of the decay on the value of Γ is quite weak - different      proximately µ ≈ −0.166 and η0 = 0.0349 for Γ = 10−6 and
Γ mainly rescale the time axis. In Ref. [107] only two extreme      µ ≈ −0.204 and η0 = 0.0313 for Γ = 1.
                                                                                                                                             30

 (a) 100                                                                     when integrating along the K-axis one has, [114, 115],
                                                                                           Z
                       -0.11                                                                 dK W (X, K; t) = |ψ(X; t)|2 .          (142)
                  ~t
 〈Π(t)〉R          N=100
                  N=200
                  N=500
                                                                                In the case of a discrete system, given, for instance, by N
                  ~t
                    -0.075                                                   discrete positions on a network (enumerated as 0, 1, . . . , N −
                  N=1000                                                     1) the functions ψ(x) are only defined for integer values of
     10
            -1                                                               x = 0, 1, . . . , N − 1, and the form of Eq.(141) has to be
         -3 -2   -1   0                 1        2    3    4    5        6   changed from an integral to a sum. There have been several
       10 10   10   10               10     10       10   10   10       10
 (b) 100                                    3                                attempts in doing so, see, for instance, [116, 117]. However,
                                       t Γ/N
                                                                             the definition of the discrete WFs might depend on whether
                                                                             the length N of the system is even or odd [118, 119].
                       -0.128
                  ~t                                                            For a one-dimensional system of length N with periodic
 〈Π(t)〉R          N=100
                  N=200
                                                                             boundary conditions (exemplified by a ring) one has ψ(x) ≡
                  N=500                                                      ψ(x ± rN ) for all r ∈ N. It follows that each and every
                  ~t
                    -0.08                                                    one of the products ψ ∗ (x − y ′ ; t)ψ(x + y ′ ; t) is identical to
                  N=1000                                                     (at least) one of the N forms ψ ∗ (x − y; t)ψ(x + y; t), where
            -1
           10                                                                y = 0, 1, . . . , N − 1.
                  0                                                 6
                 10                                            10               Now the WF has the form of a Fourier transform; a unique
                                                3
                           rescaled time t Γ/N                               transformation of these N products requires N different k-
                                                                             values. These k-values may evidently be chosen as k =
FIG. 38: (Color online) Ensemble averages hΠ(t)iR for different N :          2πκ/N , again having κ = 0, 1, . . . , N − 1. One is thus led to
(a) for Γ = 10−6 and (b) for Γ = 1. The scalings in the intermediate         propose for integer x and y the following discrete WF [120]
time regions for N = 100 and N = 1000 are shown as solid black
lines along with the appropriate scaling law. The arrows are guides                               N −1
                                                                                               1 X iky ∗
to the eye pointing at the bend of hΠ(t)iR for N = 1000. From                  W (x, k; t) =         e ψ (x − y; t)ψ(x + y; t). (143)
[107].                                                                                         N y=0


  From Fig. 38 as well as from Eq. (139) one sees that the                                           1.   WF for a ring
exponent η(N ) decreases with increasing N . Certainly, if N
becomes very large it becomes quite improbable (in the en-                     Since the eigenstates of the ring are Bloch states, the WF
semble average) for an exciton to encounter the single trap.                 for a CTQW on a ring of N nodes reads [120]
Therefore, the decay of hΠ(t)iR can only be observed at very
long times.                                                                                         N −1
                                                                                                 1 X                               
                                                                              Wj (x, κ; t) =      2
                                                                                                         exp − i2π(2n + κ)(x − j)/N
                                                                                                N n=0
                                                                                                      
VII. RELATIONS BETWEEN CTRW/CTQW AND OTHER                                                      × exp − i2t[cos(2π(κ + n)/N )
                 APPROACHES
                                                                                                − cos(2πn/N )] ,                          (144)
                      A.     Phase space approaches                          where it has been used that θ = 2πn/N and k = 2πκ/N .
                                                                             Furthermore, one may note from Eq.(143) that
   In order to obtain a unifying framework for describing both                      X
quantum mechanical and classical transport one introduces a                             Wj (x, κ; t) = |ψ(x; t)|2
quantum analog for the classical dynamics, see, e.g. [113].                           κ
One particular approach is attributed to Wigner and uses the                              1 X X −i2πκy/N ∗
so-called Wigner-function (WF) in the (quantum mechanical)                           =          e       ψ (x − y; t)ψ(x + y; t)
                                                                                          N κ y
2d phase space. If the phase space is spanned by the continu-
ous variables X and K, the WF is given by [114, 115]                                                                                      (145)

                  1
                     Z
                                                                                In general, the WFs have a very complex structure. Figure
  W (X, K; t) =          dY eiKY hX − Y /2|ρ̂(t)|X + Y /2i,                  39 shows a contour plot of the WF of a CTQW on a cycle of
                  π
                                                         (141)               length N = 101 at different times. Note that at t = 0 the WF
where ρ̂(t) is the density operator and thus for a pure state,               is localized on the strip at the initial point j. At t = 1, the
ρ̂(t) = |ψ(t)ihψ(t)|. Here, ψ(X; t) = hX|ψ(t)i is the wave                   WF is still mostly localized about j. As time increases other
function of the particle. The WF is a quasi-probability (in the              sites get populated. On short time scales, the WF develops a
sense that it can become negative). Integrating W (X, K; t)                  very regular structure in phase space, with “wavefronts” orig-
along lines in phase space gives marginal distributions, e.g.,               inating from the initial point j. Additionally, one also notes
                                                                                                                                                                                                                        31

                  x=50           initial node
   (a)                                     100
                                                     (b)                                    100
                                                                                                      (c)                                      100       tained from Eq.(144) as [120]
                                           80                                               80                                                 80



                                                                                                                                                                                         N −1
                                           60                                               60                                                 60
                                                 κ                                                κ                                                  κ
                                           40                                               40                                                 40                X                     1 X
                                           20                                               20                                                 20                     Wj (x, κ; t) =         exp[i2πn(x − j)/N ]
     100     80    60       40    20   0
                                           0
                                                       100     80    60       40   20   0
                                                                                            0
                                                                                                            100   80    60       40   20   0
                                                                                                                                               0

                                                                                                                                                                  κ
                                                                                                                                                                                       N n=0
                        x                                                 x                                                  x
   (d)                                               (e)                                              (f)
                                                                                                                                                                 × exp[−i2t cos(2πn/N )]
                                           100                                              100                                                100

                                           80                                               80                                                 80

                                           60
                                                 κ
                                                                                            60
                                                                                                  κ
                                                                                                                                               60
                                                                                                                                                     κ                    N −1
                                           40                                               40                                                 40
                                                                                                                                                                     1 X
                                           20                                               20                                                 20                ×         exp[i2π(κ + n)(x − j)/N ]
     100     80    60       40    20   0
                                           0
                                                       100     80    60       40   20   0
                                                                                            0
                                                                                                            100   80    60       40   20   0
                                                                                                                                               0                     N κ=0
                        x                                                 x                                                  x

                                                                                                                                                                 × exp[i2t cos(2π(κ + n)/N )].                        (146)
FIG. 39: (Color online) WFs of a CTQW on a cycle of length N =
101 at times t = 1, 10, 20, 40 [(a)-(d)] as well as t = 100, 500                                                                                         Since the system is periodic, the arguments (κ + n) in the
[(e),(f)]. The initial node is at j = 50. Red regions denote positive                                                                                    exponentials can be written as (κ + n) ≡ N − ν, where
values of Wj (x, κ; t), blue regions negative values and white regions                                                                                   ν = 0, 1, . . . , N − 1. This yields
values close to 0. From [120].
                                                                                                                                                                    X
                                                                                                                                                                           Wj (x, κ; t)
                                                                                                                                                                      κ
                  x=50           initial node                                                                                                                                N −1                             2
   (a)                                               (b)                                              (c)                                                            1 X i2πn(x−j)/N −i2t cos(2πn/N )
                                           90
                                           80
                                                                                            90
                                                                                            80
                                                                                                                                               90
                                                                                                                                               80                  =       e        e                             ,
                                           70
                                           60
                                           50    κ
                                                                                            70
                                                                                            60
                                                                                            50    κ
                                                                                                                                               70
                                                                                                                                               60
                                                                                                                                               50    κ
                                                                                                                                                                     N n=0
                                           40                                               40                                                 40
                                           30                                               30                                                 30
                                           20
                                           10
                                                                                            20
                                                                                            10
                                                                                                                                               20
                                                                                                                                               10
                                                                                                                                                                                                                      (147)
                                           0                                                0                                                  0
         90 80 70 60 50 40 30 20 10    0                   90 80 70 60 50 40 30 20 10   0                     90 80 70 60 50 40 30 20 10   0
                        x                                                 x                                                  x
   (d)                                               (e)                                              (f)
                                           90
                                           80
                                                                                            90
                                                                                            80
                                                                                                                                               90
                                                                                                                                               80
                                                                                                                                                         which is exactly what also follows, see Eq.(145), from calcu-
                                           70
                                           60
                                           50    κ
                                                                                            70
                                                                                            60
                                                                                            50    κ
                                                                                                                                               70
                                                                                                                                               60
                                                                                                                                               50    κ
                                                                                                                                                         lating |ψ(x; t)|2 directly from the Bloch ansatz, see Eq.(17)
                                           40
                                           30
                                           20
                                                                                            40
                                                                                            30
                                                                                            20
                                                                                                                                               40
                                                                                                                                               30
                                                                                                                                               20
                                                                                                                                                         and [72].                        P
         90 80 70 60 50 40 30 20 10
                        x
                                       0
                                           10
                                           0
                                                           90 80 70 60 50 40 30 20 10
                                                                          x
                                                                                        0
                                                                                            10
                                                                                            0
                                                                                                              90 80 70 60 50 40 30 20 10
                                                                                                                             x
                                                                                                                                           0
                                                                                                                                               10
                                                                                                                                               0            For the marginal distribution x Wj (x, κ; t) one also gets
                                                                                                                                                         from Eq.(144)
FIG. 40: (Color online) Same as Fig.39, for N = 100 and j = 50.
                                                                                                                                                                                     N −1
From [120].                                                                                                                                                    X                   1 X
                                                                                                                                                                   Wj (x, κ; t) = 2       N δ2n,−κ ei2π(2n+κ)j/N
                                                                                                                                                                x
                                                                                                                                                                                  N n=0
                                                                                                                                                                     
                                                                                                                                                               × exp − i2t[cos(2π(κ + n)/N ) − cos(2πn/N )]
                                                                                                                                                                  
“wavefronts” starting from the region opposite to the initial                                                                                                     1/N for N odd and all κ
                                                                                                                                                                  
point, which are much weaker in amplitude. As time pro-                                                                                                        = 2/N for N even and κ even                     (148)
                                                                                                                                                                  
                                                                                                                                                                  0
gresses, these two types of waves start interfering with each                                                                                                              for N even and κ odd,
other.
                                                                                                                                                         all of these expressions are independent of t. Eq.(148) can
   Figure 40 shows the WF of a CTQW for N = 100. At short                                                                                                be confirmed directly by taking the Fourier transform of
times, the structure of the WF is quite similar to the situation                                                                                         |ψ(x; t)|2 . The whole phase space volume is normalized to
for N = 101. Nonetheless, there are differences at larger                                                                                                unity, as can be seen by summing Eq.(148) over all κ, with
times, visible by comparing Figs.39(e) and 39(f) to Figs.40(e)                                                                                           κ = 0, 1, . . . , N − 1.
and 40(f).                                                                                                                                                  In the long-time average and for odd N (superscript o ) most
                                                                                                                                                         points in the quantum mechanical phase space have a weight
  However, although at long times the interference effects are                                                                                           of 1/N 2 , namely one has has [103]
quite intricate, typical patterns are still visible. At t = 500,                                                                                                               
one finds less regularities in phase space for N = 101 than                                                                                                                    1/N
                                                                                                                                                                                   2
                                                                                                                                                                                       for κ 6= 0 and any x
for N = 100, reflecting the higher symmetry of CTQW for                                                                                                            o
                                                                                                                                                                W j (x, κ) = 1/N       for κ = 0 and x = j         (149)
even N . One notes, moreover, that the phase space patterns                                                                                                                    
                                                                                                                                                                               0      else.
give a much richer picture of the underlying dynamics than
the transition probabilities |ψj (x; t)|2 alone.
                                                                                                                                                         For even N (superscript e ), the limiting WF reads
  Furthermore, one should remark that in an infinite system                                                                                                            
                                                                                                                                                                               2
the WFs have a much simpler structure, because there one                                                                                                               2/N
                                                                                                                                                                                   κ 6= 0, κ even and any x
                                                                                                                                                              e
does not face the problem of distinct wave fronts running into                                                                                             W j (x, κ) = 1/N         κ = 0 and x = j, j + N/2          (150)
                                                                                                                                                                       
                                                                                                                                                                       0
opposite directions and interfering with each other because of                                                                                                                      else.
the closure of the ring.
                                        P                                                                                                                The long time averages of the WFs for even N are somewhat
  In general, the marginal distribution κ Wj (x, κ; t) is ob-                                                                                            peculiar, since values different from zero appear only for even
                                                                                                                                                                     32

κ, whereas the WFs themselves have values different from                                                    x=50          initial node
                                                                             (1a)                (2a)                 (3a)               (4a)                   x 10
                                                                                                                                                                      −3


zero at arbitrary times for all κ. These stripes in the long-time     100                                                                                        5
                                                                     κ 80
average are due to the periodicity of the ring. For even N             60
                                                                       40
                                                                                                                                                                 0

one finds constructive interference patterns in the transition         20
                                                                        0                                                                                        −5
probabilities, since the number of steps in both directions is               (1b)                (2b)                 (3b)               (4b)                   x 10
                                                                                                                                                                      −3


the same, see also Ref. [72]. For a finite line with even N ,          100
                                                                     κ 80
                                                                                                                                                                 4
                                                                                                                                                                 2
there are no stripes in the long time average.                         60
                                                                        40
                                                                                                                                                                 0
                                                                                                                                                                 −2
                                                                        20
                                                                                                                                                                 −4
                                                                         0

                                                                             (1c)                (2c)                 (3c)               (4c)                   x 10
                                                                                                                                                                      −3

                                                                      100
                2.   Rings with energetic disorder                                                                                                               4
                                                                     κ 80
                                                                       60
                                                                                                                                                                 2
                                                                                                                                                                 0
                                                                       40
                                                                                                                                                                 −2
                                                                       20
   By introducing (static) disorder into the system, as in              0
                                                                                                                                                                 −4

Sec. V B, the Bloch property is lost [103]. In order to have          100
                                                                             (1d)                (2d)                 (3d)               (4d)                   x 10
                                                                                                                                                                      −3

                                                                                                                                                                 4
a global picture of the effect of the disorder on the dynam-         κ 80                                                                                        2
                                                                       60
                                                                                                                                                                 0
ics, one considers ensemble averages of the WFs. For this one          40
                                                                                                                                                                 −2
                                                                       20
calculates the WF for different realizations of H and averages          0                                                                                        −4

over all realizations, i.e., for R realizations:                      100
                                                                             (1e)                (2e)                 (3e)               (4e)                   x 10
                                                                                                                                                                      −3

                                                                                                                                                                 4
                                                                     κ 80
                                                                       60
                                                                                                                                                                 2
                               R                                                                                                                                 0
                            1 X                                      40
                                                                                                                                                                 −2
        hWj (x, κ; t)iR ≡         Wj (x, κ; t) r ,          (151)      20
                                                                                                                                                                 −4
                            R r=1                                       0

                                                                             (1f)                (2f)                 (3f)               (4f)                   x 10
                                                                                                                                                                      −3

                                                                       100                                                                                       4
                                                                   κ 80                                                                                        2
where Wj (x, κ; t) r is the WF of the rth realization of H.            60
                                                                        40
                                                                                                                                                                 0
                                                                                                                                                                 −2
   It turns out that the particular type of disorder, i.e., diago-      20
                                                                         0
                                                                                                                                                                 −4

nal or diagonal and off-diagonal, does not change the picture                0   20 40 60 80 100 0   20 40 60 80 100 0   20 40 60 80 100 0   20 40 60 80 100
                                                                                      x                     x                 x                  x
significantly. For diagonal and for off-diagonal disorder Fig-
ure 41 shows snapshots of hWj (x, κ; t)iR at different times         FIG. 41: (Color online) Ensemble average of WFs of the quantum
for N = 101 and for different values of ∆.                           dynamics on a ring of length N = 101 with diagonal and off-
   The first column shows hWj (x, κ; t)iR for ∆ = 1/40 at            diagonal disorder for ∆ = 1/40, 1/10, 1/4, and 1/2 [columns (1)-
times t = 1, 10, 20, 40, 100, and 500 [Fig. 41(1a)-(1f)]. For        (4)], each at times t = 1, 10, 20, 40, 100, and 500 [rows (a)-(f)]. The
this quite weak disorder, the patterns in phase space are sim-       initial node is always j = 50 and the average is over R = 1000 re-
ilar to the unperturbed case, where “waves” in phase space           alizations. Red regions denote positive values of the averaged WFs,
emanate from the initial site x = j = 50 and start to in-            blue regions negative values and white regions values close to 0. The
terfere after having reached the opposite site of the ring (see      colormaps are always chosen to be the same for each row but might
                                                                     differ in different rows. The maximal values of hWj (x, κ; t)iR are
Fig. 3 of [120]). However, at longer times differences become
                                                                     denoted by small black regions; these are highlighted and exempli-
visible, Fig 41(1f). The pattern for the unperturbed case is         fied by the arrows in panel (4f). From [103].
quite irregular but with alternating positive and negative re-
gions of the WF of approximately the same magnitude. For x
close to the initial site j = 50, the disorder causes a decrease     unity when integrated over the whole phase space. Having an
of hWj (x, κ; t)iR for κ-values in the middle of the interval        even number of nodes in the graph does not alter the picture
[0, N − 1] when compared to what is found for values of κ            significantly.
close to 0 or to N − 1.                                                 The ensemble average of the long-time averaged WF fol-
   Increasing the disorder parameter ∆, the patterns change          lows as [103]
profoundly. The wave structure gets suppressed and for all κ
a localized region forms about the initial site j = 50, already                                                               ZT
                                                                                                                D        1                        E
for small disorder (∆ = 1/10) and short times (t = 20), see                         hW j (x, κ)iR ≡                  lim           dt Wj (x, κ; t)
                                                                                                                    T →∞ T                                R
Fig. 41(2c).                                                                                                                  0
   For even larger values of ∆, for all κ the formation of a lo-                                      ZT
calized region about j = 50 becomes even more pronounced.                                 1
                                                                                    = lim                   dt hWj (x, κ; t)iR .                               (152)
Already for ∆ = 1/4 this localized region forms for times as                         T →∞ T
                                                                                                        0
short as t = 10, see Fig. 41(3b). At ∆ = 1/2, hWj (x, κ; t)iR
stays localized at all times [Fig. 41(4a)-(4f)]. Also here, the      Now, the disorder changes also the limiting WF quite drasti-
values of the WF at about κ ≈ N/2 are rather low, whereas            cally. Starting from high disorder of ∆ = 1/2, one expects
the values of the WF for κ close to the interval borders 0 and       from Figs. 41(4a)-(4f) that the long time average of the av-
N − 1 remain rather large for x ≈ j, as indicated by the thin        eraged WF will look basically the same. Figure 42 shows
black region (see also the arrows), e.g., in Fig. 41(4f). One        the limiting averaged WF for N = 101 and DOD accord-
further notes that at high disorder the localized averaged WF        ing to Eq. (152). Indeed, for large ∆, the limiting averaged
is always positive, i.e., all fluctuations, present for small dis-   WF is comparable to the corresponding averaged WF, com-
order, have vanished. One recalls that the WF is normalized to       pare Figs. 42(4). Close to the initial node x = j = 50 and
                                                                                                                                  33

       (1)       ∆ =1/40       (2)           ∆ =1/10       x 10
                                                                −3
                                                                     see Eq.(150). By switching on the disorder, these peculiar-
 100                                                                 ities vanish. Figure 43 shows the limiting averaged WF for
  80
                                                                     DOD and N = 100. Although for small ∆ there are some re-
κ 60                                                       3         mainders of stripes left, these disappear completely for higher
  40
  20                                                                 values of ∆, compare Figs. 43(1)-(4). Note further that the
                                                                                         e
   0                                                                 second peak of W j (x, κ) at x = j + N/2, see Eq.(150),
                                                           2         transforms for increasing disorder to an oscillatory line in the
       (3)       ∆ =1/4        (4)           ∆ =1/2
 100                                                                 κ-direction at x = j + N/2.
  80
                                                           1
κ 60
  40                                                                                3. Long-range interaction cycles
  20
   0                                                       0
       0 20 40 60 80 100 0 20 40 60 80 100                             Xu and Liu have considered the WF, defined in Eq. (143)
                x                        x                           and [120], for rings, where the m next nearest neighbors of a
                                                                     given node are connected to this node by bonds [121], see also
FIG. 42: (Color online) DOD: Limiting averaged WF, hW j (x, κ)iR ,   Sec. V A. The eigenstates of such a translationally invariant
for N = 101 and ∆ = 1/40, 1/10, 1/4, and 1/2 [panels (1) to (4),     system are still Bloch states. However, the eigenvalues read
respectively], according to Eq.(152). From [103].                    [121]
                                                                                                    m
       (1)       ∆ =1/40       (2)           ∆ =1/10            −3                                  X
                                                           x 10                     En = 2m − 2           cos 2njπ/N .         (153)
  80                                                       3                                        j=1

κ 60                                                       2         As in Eq. (144), the WF follows as
  40
  20                                                       1                                        N −1
   0                                                                                             1 X −it(En −EN +κ−n)
                                                                             Wj (x, κ : t) =             e
       (3)       ∆ =1/4        (4)           ∆ =1/2        0                                    N 2 n=0
  80                                                       −1                                   ×ei2π(2n−κ)(x−j)/N .           (154)
κ 60                                                       −2
  40                                                                 Thus, inserting the results for the eigenvalues one obtains the
  20                                                       −3        WF for this type of long-range interacting cycles.
   0                                                                    Now, while for m = 1 one recovers the results of the pre-
       0 20 40 60 80          0 20 40 60 80
                                                                     vious section, increasing m leads to more complex structures
                x                        x
                                                                     of the WF. The fronts emanating from the initial value x = j
FIG. 43: (Color online) Same as Fig. 42 but for N = 100. From        have, in the case of m = 1, only a single maximum value
[103].                                                               at about κ = N/2, see Figs. 39 and 40. For m > 1 there
                                                                     appear m front maxima at about κ = (2l − 1)N/2m with
                                                                     l = 1, . . . , m [121]. With increasing number m the structure
there along the κ-direction, hW j (x, κ)iR has large (positive)      of the WFs become more complex, but the resulting patterns
values for κ about 0 and N − 1 which decrease by going to-           can still be attributed to the interfering fronts emanating from
ward κ = N/2. Here, the decrease depends on the particular           x = j [121].
type of disorder involved.
   Also for small ∆ there are significant differences to the
case without disorder. From Fig. 42(1) one sees that the                                 4.   Disordered networks
disorder “smears out” the localized value W j (j, 0) = 1/N
in the absence of disorder, see Eq.(149). Specifically, the             Xu and Liu have also studied the WF for disordered sys-
(x = j, κ = 0)-value decreases, while the neighboring ones           tems, namely for the Watts-Strogatz (WS) small-world model
increase. For ∆ = 1/10, the onset of localization about              [121]. The WS model starts from an ordered ring with only
x = j = 50 can already be seen, e.g., Fig. 42(2), and becomes        nearest neighbor interactions. Now, every bond is rewired
more and more pronounced as ∆ increases, Fig. 42(3). Fur-            with probability p, implying that for p = 0 one retains the
thermore, all other values of hW j (x, κ)iR for x 6= j decrease      ordered ring and for p = 1 one has a completely disordered
with increasing disorder, as can be seen by the decreasing size      network of N nodes with N bonds. The WF for such systems
of the light pink region, which corresponds to values close to       shows essentially the same features as for rings with energetic
1/N 2 . In fact, the values of the limiting averaged WF for x        disorder, see above. In the ensemble average there is stronger
distant from x = j = 50 drop to zero, shown as white regions         and stronger localization with increasing p. Moreover, here
in Fig. 42.                                                          also the distinction between even and odd N remains, namely
   For even N one finds that without disorder the limiting WF        even N lead to a stripe-patterned WF caused by constructive
shows a peculiar “striped” distribution, caused by the PBCs,         interference while odd N do not show this behavior [121].
                                                                                                                               34

               B. Quantum master equations                                            1.    Decoherence on rings

   CTQW and CTRW are the two extreme cases of possi-                 Take now a ring of N nodes and N Lindblad operators
                                                                                                                    p        each
ble transport processes, i.e., a purely coherent transport for    of which projects onto a single node, i.e., Lj = λj |jihj| for
CTQW and a purely incoherent transport for CTRW. Now,             j = 1, . . . , N . The parameters λj specify the strength of the
if a quantum mechanical system cannot be regarded as being        coupling to the environment. If λj = λ for all j, Eq. (158)
isolated from its environment, this environment will influence    simplifies:
the dynamics of the system. Depending on the strength of the
coupling (where also the temperature is assumed to be con-                  ρ̇(t) = −i[HS , ρ(t)]
                                                                                        X
trolled by the environment), the dynamics may change from
                                                                                                           
                                                                                    −2λ      ρ(t) − ρjj (t) |jihj|,         (159)
quantal to classical. Since the total system (i.e., the system                                 j
S and the environment/reservoir R) resides in a Hilbert space
of huge dimension (this due to the many degrees of freedom        where ρkj (t) ≡ hk|ρ(t)|ji. The rate λ can be estimated from
(DOF) of the environment), one often considers the system         the spectral density J(ω) describing the environment within
only, where the environmental DOF have been traced out [69].      the Caldeira-Leggett model [122, 123] at a given temperature
   Let W (t) be the density operator of the total system, then    T . Taking J(ω) = 2παω exp(−ω/ωc ) and using the Markov
ρ(t) ≡ trR {W (t)} is called the reduced density operator.        approximation one arrives at λ = παkB T [69]. One has to
Then the dynamics of W (t) is still governed by Schrödinger’s    bear in mind that Eq. (159) is an approximation with a lim-
equation, which can be recast into the Liouville-von Neumann      ited range of validity: For a very large coupling strength λ,
(LvN) equation                                                    Eq. (170) leads to the quantum Zeno limit rather than to a clas-
                                                                  sical master/rate equation. In matrix form Eq. (159) is equiv-
                 Ẇ (t) = −i[Htot, W (t)],               (155)    alent to the so-called Gurvitz model, see for instance [124],
where Htot is the Hamiltonian of the total system. Htot usu-      considered in [125–127]
ally comprises three parts: the Hamiltonians HS for the sys-
tem, HR for the environemnt, and HSR for the coupling be-                        ρ̇kj (t) = −ihk|[HS , ρ(t)]|ji
tween system and environment:                                                               −2λ(1 − δkj )ρkj (t).           (160)
                Htot = HS + HR + HSR .                   (156)       Solenov and Fedichkin showed analytically that the prob-
  Inserting this into the LvN equation for W (t) and integrat-    ability distribution to be at node k, where for a ring one as-
ing out the environmental DOF one arrives at an equation for      sumes without loss of generality that the initial node is j = 0,
the reduced density operator (for details see [69]):              follows from the diagonal elements of the reduced density ma-
                                                                  trix [126, 127]
              ρ̇(t) = −i[HS , ρ(t)] + D[ρ(t)].           (157)
                                                                                        N −1
Here, D[ρ(t)] is called the dissipator. Note that in order to                       1   X    1 − δn+m,0 − δn+m,N
                                                                       ρk,k (t) =     +
arrive at Eq. (157) several assumptions, such as bilinear cou-                      N n,m=0          N2
plings between system and environment or the Markov ap-                  h                                                   i
proximation, have been used [69].                                      × δn,m e−2λ[(N −1)/N ]t + (1 − δn,m )e−2λ[(N −2)/N ]t
   Under certain conditons, such as a weak coupling between
the system and the environment, the dissipator can also be ex-
                                                                             h      π(n + m)       π(n − m)
                                                                       × exp it sin            cos
pressed by operators acting on the Hilbert space of the system                          N              N
S. In particular, Eq. (157) can be brought into the so-called            2πi          i
                                                                       +     (n + m)k .
Lindblad form [69]                                                        N
                                      2
                                                                                                                         (161)
                                    N 
                                          2Lj ρ(t)L†j
                                    X
         ρ̇(t) = −i[HS , ρ(t)] −                                  Clearly, Eq. (161) reduces to the results of Sec. IV A in the
                                    j=1                           limit of λ → 0. For λ 6= 0, due to the exponentially decaying
                                                                  factors, the probability distribution will eventually decay to
                                            
                   −L†j Lj ρ(t) − ρ(t)L†j Lj ,           (158)
                                                                  the classical equilibrium values, in this case the equipartition
where the operators Lj , the Lindblad operators, mimick the       value 1/N .
influence of the environemnt on the dynamics. Equation (158)         The so-called mixing time tm is used to compare the
is also called Lindblad quantum master equation (LQME).           spreading of CTQW to that of CTRW. It is implicitly defined
   Obviously, if the coupling to the environment vanishes, one    by looking at the deviation from the classical uniform distri-
arrives again at the LvN equation for the density operator ρ(t)   bution 1/N [125]. One gets thus
of the system S. Since the resulting LvN equation is equiv-                          N −1
alent to the Schrödinger equation of a closed system with                           X                     1
                                                                                            ρk,k (tm ) −     ≤ ε,           (162)
Hamiltonian H, it is also equivalent to the CTQW formula-                                                  N
                                                                                     k=0
tion of the previous sections. Now, when increasing the cou-
pling to the environment, Eq. (158) allows to study the onset     where ε is a small dimensionless constant representing the de-
of the quantum to classical cross-over.                           gree of mixing. By using Eq. (161), Solenov and Fedichkin
                                                                                                                               35

showed that the mixing time is bound from above by                                        2.   Dimer with traps
                                                  
                         N                  N +1                      Within the phenonmenological approach presented above,
      tmix ≡ min tm <           ln                     .   (163)
                      2λ(N − 2)               ε                    introducing traps into the system leads to non-Hermitian
                                                                   Hamiltonians. The LvN equation changes, therefore, to
   The same authors have generalized this approach to so-                                        
called hypercycles. A hypercycle of dimension d and size N                 Ẇ (t) = −i H0 , W (t) − Γ, W (t) ,           (169)
is build by considering N copies of the d − 1 dimensional hy-
percycle and connecting the corresponding nodes, see [125]         where {·, ·} is the anti-commutator and H0 the Hamiltonian
for details. Thereby, the total number of nodes is N d . The       without traps. Writing the Lindblad operators in the form
                                                                   √
corrsponding upper bound for the mixing time tm now fol-            λLj , the LQME reads [129]
lows as                                                                                             
                                                                               ρ̇(t) = −i H0 , ρ(t) − Γ, ρ(t)
                             d(N + 1)(1 + εN d )
                                                
       (d)     d N                                                                            X               
     tmix ≤             ln                         .    (164)                            −2λ     ρ(t) − ρjj (t) Lj .    (170)
              2λ N − 1                ε
                                                                                                 j

   Salimi and Radgohar have considered the long-range case            Now, consider a dimer which is coupled to an external bath.
of the single cycle, where a given node interacts with its 2m      This situation allows to solve Eq. (170) analytically and to
nearest neighbors (m to each side) [128], see also Sec. V A.       compare the LQME results to the numerically exact Path In-
The probability distribution to be at node k is then obtained      tegral Monte Carlo (PIMC) calculations. For details on PIMC
for even m as                                                      techniques see, e.g., [130, 131] and references therein. The
                       N −1
                                                                   Hamiltonian of the dimer without any coupling to the sur-
                1     X 1 − δn+l,0 − δn+l,N                        roundings can be expressed through the Pauli matrices σz and
      ρk,k (t) =   +
                N                   N2                             σx ,
                     n,l=0
           h                    i
      × exp − 2λ[(N − 1)/N ]t                                                                      Γ
                                                                                 H = E 1 − V σx − i (1 − σz ) ,              (171)
                                                                                                   2
           h       π(n + l)     π(n − l) 2πi            i
      × exp it sin          cos          +     (n + l)k            where E is the on-site energy, which is choosen to be the same
                      N             N       N
           h           πm(n  +  l)     πm(n − l) i                 for both nodes, and V is the coupling between the two nodes.
      × exp im+1 t sin             sin            .   (165)        It is easily verified that the eigenvalues are [129]
                           N              N
                                                                      E± = E ± V e±iφ = E ±
                                                                                                     p
and for odd m as                                                                                      V 2 − Γ2 /4 − iΓ/2,    (172)

                       N −1
                         X 1 − δn+l,0 − δn+l,N                     where φ = arcsin(Γ/2V ). For Γ → 0 (φ → 0) this yields
                  1
      ρk,k (t) =     +                                             the correct eigenvalues E ± V of H0 . Note that for Γ ≤
                 N                   N2
                        n,l=0                                      2V the negative imaginary part of E± is identical for both
                                                                   eigenvalues, i.e., γ+ = γ− = Γ/2. The bi-orthonormalized
        h                                                   i
      × δn,l e−2λ[(N −1)/N ]t + (1 − δn,l )e−2λ[(N −2)/N ]t
                                                                   eigenstates of H are of the form [129]
              h      π(n + l)     π(n − l) 2πi                i
      × exp it sin            cos           +      (n + l)k                                  1
                                                                                                        
                                                                                                            e±iφ/2
                                                                                                                     
                         N           N         N                                  |Φ± i ≡ √                                  (173)
              h
                m+1       πm(n + l)     πm(n − l) i                                        2 cos φ         ±e∓iφ/2
      × exp i       t sin           sin              .     (166)
                              N              N
                                                                   and
While the upper bounds of the mixing time turn out to be in-
                                                                                                         e∓iφ/2
                                                                                                                
dependent of m, they do differ for even and for odd m, one                                    1
                                                                                  |Φ̃± i ≡ √                       ,         (174)
has namely                                                                                  2 cos φ      ±e±iφ/2

                       N      N                                    where the phases φ depend on Γ, such that in the limit Γ → 0
             tmix ≤        ln          for even m          (167)   one recovers the eigenstates of H0 .
                      N −1    ε
                                                                      When the coupling to the environment vanishes (λ → 0),
and                                                                one obtains the survival probability directly from the eigen-
                                                                   states and eigenvalues of H. For Γ ≤ 2V one has [129]
                       N      N
             tmix ≤        ln          for odd m.          (168)                       cos2 (φ + tV cos φ)
                      N −2    ε                                          Π(t) = e−Γt                          (for λ = 0).   (175)
                                                                                              cos2 φ
Therefore, mixing turns out to be faster for even m than for
odd m.                                                             Note that for values Γ > 2V the dimer is overdamped.
                                                                                                                                           36

  When considering the dimer without traps (Γ = 0) but cou-                   1
                                                                      (a)
                                                                            0.8                                         Eq. (168)
pled to the environment, Eq. (170) simplifies and, from the                           α=0
solution for ρ, one obtains the transition probabilities [129]              0.6
                                      √                              Π(t)
                             "                                             0.4
       (0)        1 e−λt λ sin t 4V 2 − λ2
     π1,1 (t) =     +              √                                        0.2
                  2      2           4V 2 − λ2                               0
                                          #                                    0      1        2     3       4      5        6        7
                        p                                                   1
                  + cos t 4V 2 − λ2           (for Γ = 0).            (b)
                                                                            0.8                                         PIMC
                                                                                      α=1/10                            LQME
                                                                            0.6
                                                                     Π(t)
                                                          (176)                                                         Eq. (170)
                                                                            0.4
            (0)            (0)
Moreover, π2,1 (t) = 1−π1,1 (t). From Eq. (176) one recovers                0.2
for λ → 0 the simple oscillatory behavior of the transition                  0
                                    (0)                                        0      1        2     3       4      5        6        7
probabilities [namely, limλ→0 π1,1 (t) = cos2 (V t)]. When                    1
the coupling to the surroundings does not vanish, for λ > 0,          (c)
                                                                            0.8                                         PIMC
the transition probabilities still show oscillations, which are                       α=1/4                             LQME
                                                                            0.6
                                                                     Π(t)
superimposed on an exponential decay which tends for long                                                               Eq. (170)
times to the classical equipartition value of 1/2.                          0.4
   In order to combine the results of Eq. (175) – taking val-               0.2
ues Γ < 2V – and Eq. (176), one expands in both equations                    0
all terms except the exponentials to first order in Γ and λ, re-                  0   1        2     3        4     5        6        7
                                                                                                             -1
spectively. Note that for Eq. (175) one obtains a product of                                        time t [V ]
exp(−Γt) and cos2 V t, which is the simple oscillatory behav-         (d)
ior of the dimer in the absence of the trap. Now, the coupling              0.8                                              α=0
                                                                                                                             α=1/10
to the environment affects all transitions but still conserves              0.6                                              α=1/4
probabilities. Therefore, one replaces the term cos2 V t by the      Π(t)                                                    α=10
                                                                            0.4
expansion of Eq. (176), such that one obtains [129]
                                                                            0.2
                                                                             0
                    (0)                                                           0       10       20          30       40            50
   Π(t) ≈ e−Γt π1,1 (t)                                                                                      -1
                                                                                                    time t [V ]
               h 1 e−λt              λ         i
        ≈ e−Γt +          cos 2V t +    sin 2V t .                 FIG. 44: (Color online) PIMC results (circles) for a dimer with
                 2      2            2V
                                                 (177)             Γ = 0.1 and different system-bath couplings α = λ/π: (a) α = 0,
                                                                   (b) α = 1/10, and (c) α = 1/4. The solid lines represent the numer-
   Figure 44 compares the survival probabilities of a dissi-       ical solution of the LQME equation, the dashed lines show the corre-
pative dimer obtained from the approximative LQME ap-              sponding analytical results obtained from Eq. (175) for α = λ = 0
proach to the numerically exact PIMC calculations for a bath       and from Eq. (177) for α = 1/10 and α = 1/4. The dotted blue line
                                                                   shows the long time limit Π(t) ∼ exp(−Γt). Panel (d) shows the
with ohmic spectral density with exponential cutoff, J(ω) =
                                                                   corresponding long-time behavior of the numerical LQME solution
2παωe−ω/ωc . The initial condition is π1,1 (0) = 1, i.e., at       for the three different values of α and additionally the behavior for
t = 0 the system is localized in the non-trap node 1 of the        large couplings α = 10. From [129].
dimer. Here, the on-site energies E and the coupling elements
V have been taken to be equal, E = V = 1, one sets ωc = 5V
and the temperature is fixed to kB T = V .                         regime permits to compensate for this shortcoming; it allows
   For small trapping strength (Γ = 0.1) and vanishing cou-        namely to use for longer times the LQME procedure, see
pling to the environment (α = 0), Fig. 44(a), the PIMC cal-        Fig. 44(d).
culations coincide with the result of Eq. (175). A moderate
increase of the coupling (α = 1/10), Fig. 44(b), still leads
for Eqs. (170) (solid lines) and (177) (dashed lines) to re-
sults which are in excellent agreement with the findings of                                    VIII. OUTLOOK
the PIMC calculations (symbols). When increasing the cou-
pling further to α = 1/4, Fig. 44(c), however, the approxi-           The application of CTQW to transport for large classes of
mate solution, Eq. (177), begins to deviate from the LQME          (physical, chemical, and biological) phenomena involving dif-
and the PIMC calculations, which are still in very good agree-     ferent types of networks has turned out to be very successful
ment [129].                                                        in recent years. However, only little is known about the de-
   As the numerical effort of real-time PIMC simulations           tailed relations between topology, interaction ranges, dimen-
grows exponentially with time, they can cover only short-to-       sions and the transport efficiencies. While CTRW fall into dif-
intermediate time scales. However, the agreement between           ferent universality classes depending on the (fractal) dimen-
the LQME and the PIMC calculations in the weak coupling            sions and the interaction ranges, there are only few indica-
                                                                                                                                          37

tions on the analogous emergence of “quantum universality               the influence of the environment on the dynamics. Clearly,
classes”. Take as an example the dynamics on a chain with               the validity of both methods has to be checked. One option to
long-range interactions decaying as |k − j|−γ , see Sec. V A;           do so is to compare the results - for not too large systems - to
in this case the mean square displacement of CTQW increases             those of numerically exact PIMC simulations.
as t2 also for γ = 2. This is not the case for CTRW, where                 Such a comparison has several advantages. First, it sets the
only systems with γ > 3 lead to the same power-law behavior             range of validity of the phenomenological approaches. Sec-
of the mean square displacement.                                        ond, once this range is established, it allows to extend the
   Therefore, a thorough investigation of the influence of dif-         short-time PIMC results to (in principle) arbitrary long times.
ferent topological aspects on the dynamics is clearly neces-            Thus, joining different methods together may lead to a deeper
sary. Moreover, once a systematic classification of CTQW                understanding of the complex transport processes found in na-
gets established, one needs to examine the transition from the          ture.
quantum to the classical picture, in order to understand the
changes in the universality patterns. For this, the environ-
ment of each quantum system has to be properly taken into
account. In a phenomenological ansatz one can incorporate                                      Acknowledgements
this either by using the quantum master equation approach,
sketched in Sec. VII B, or by using so-called generalized mas-             Support from the Deutsche Forschungsgemeinschaft
ter equations (GME) [8]. Here, the Markovian master equa-               (DFG), the Fonds der Chemischen Industrie and the Ministry
tion (as used in CTRW) is extended by a memory-kernel (MK)              of Science, Research and the Arts of Baden-Württemberg
to account for non-Markovian effects. In the limit of a MK of           (AZ: 24-7532.23-11-11/1) is gratefully acknowledged. We
delta-type one recovers the CTRW, while in the limit of a con-          thank Elena Agliari, Veronika Bierbaum, Lothar Mühlbacher,
stant MK one arrives for CTQW at a wave equation similar                Volker Pernice, Tobias Schmid, and Antonio Volta for many
to the Schrödinger equation. Both approaches allow to study            fruitful discussions.




  [1] J.-P. Bouchaud, A. Georges, Phys. Rep. 195 (1990) 127.                  (1993) 1687.
  [2] R. Albert, A.-L. Barabási, Rev. Mod. Phys. 74 (2002) 47.          [23] O. Mülken, A. Blumen, Phys. Rev. E 71 (2005) 016101.
  [3] S. N. Dorogovtsev, J. F. F. Mendes, Adv. Phys. 51 (2002)           [24] S. Bose, Phys. Rev. Lett. 91 (2003) 207901.
      1079.                                                              [25] F. W. Strauch, Phys. Rev. A 74 (2006) 030301(R).
  [4] J. Kempe, Contemporary Physics 44 (2003) 307.                      [26] M. A. Nielsen, I. L. Chuang, Quantum Computation and
  [5] N. van Kampen, Stochastic Processes in Physics and Chem-                Quantum Information, Cambridge University Press, Cam-
      istry, North-Holland, Amsterdam, 1990.                                  bridge, England, 2000.
  [6] G. H. Weiss, Aspects and Applications of the Random Walk,          [27] P. W. Shor, in: 35th IEEE Symposium on Foundations of Com-
      North-Holland, Amsterdam, 1994.                                         puter Science, IEEE, Los Alamos, 1994, p. 124.
  [7] J. M. Ziman, Principles of the Theory of Solids, Cambridge         [28] L. K. Grover, Phys. Rev. Lett. 79 (2) (1997) 325.
      University Press, Cambridge, England, 1972.                        [29] A. M. Childs, J. Goldstone, Phys. Rev. A 70 (2004) 022314.
  [8] V. M. Kenkre, P. Reineker, Exciton Dynamics in Molecular           [30] E. Agliari, A. Blumen, O. Mülken, Phys. Rev. A 82 (2010)
      Crystals and Aggregates, Springer, Berlin, 1982.                        012305.
  [9] N. W. Ashcroft, N. D. Mermin, Solid State Physics, Saunders        [31] R. P. Feynman, Int. J. Theor. Phys. 21 (1982) 467.
      College Publishing, Philadelphia, 1976.                            [32] D. A. Meyer, J. Stat. Phys. 85 (1996) 551.
 [10] C. Kittel, Introduction to Solid State Physics, Wiley, New         [33] M. Christandl, N. Datta, A. Ekert, A. J. Landahl, Phys. Rev.
      York, 1986.                                                             Lett. 92 (2004) 187902.
 [11] P. W. Anderson, Phys. Rev. 109 (1958) 1492.                        [34] T. Kottos, U. Smilansky, Phys. Rev. Lett. 79 (1997) 4794.
 [12] D. A. McQuarrie, Quantum Chemistry, Oxford University              [35] H. Schanz, U. Smilansky, Phys. Rev. Lett. 84 (2000) 1427.
      Press, Oxford, 1983.                                               [36] T. Kottos, U. Smilansky, Phys. Rev. Lett. 85 (2000) 968.
 [13] M. Doi, S. F. Edwards, The Theory of Polymer Dynamics,             [37] T. Kottos, H. Schanz, Phys. Rev. Lett. 90 (2003) 234101.
      Oxford University Press, Oxford, 1998.                             [38] U. Smilansky, J. Phys. A 40 (2007) F621.
 [14] H. Scher, M. Lax, Phys. Rev. B 7 (1973) 4491.                      [39] J. Sakurai, Modern Quantum Mechanics, 2nd Edition,
 [15] H. Scher, E. W. Montroll, Phys. Rev. B 12 (1975) 2455.                  Addison-Wesley, Redwood City, CA, 1994.
 [16] S. Alexander, R. Orbach, J. Phys. (Paris) Lett. 43 (1982) L625.    [40] W. Kinzel, Phys. Bl. 51 (1995) 1190.
 [17] J. Klafter, A. Blumen, J. Chem. Phys. 80 (1984) 875.               [41] F. Grossmann, J.-M. Rost, W. P. Schleich, J. Phys. A 30 (1997)
 [18] U. Even, K. Rademann, J. Jortner, N. Manor, R. Reisfeld,                L277.
      Phys. Rev. Lett. 52 (1984) 2164.                                   [42] M. V. Berry, J. Phys. A 29 (1996) 6617.
 [19] J. Klafter, A. Blumen, M. F. Shlesinger, Phys. Rev. A 35           [43] I. Bloch, Nature Physics 1 (2005) 23.
      (1987) 3081.                                                       [44] B. C. Sanders, S. D. Bartlett, B. Fregenna, P. L. Knight, Phys.
 [20] G. Zumofen, A. Blumen, J. Klafter, M. Shlesinger, J. Stat.              Rev. A 67 (2003) 042305.
      Phys. 54 (1989) 1519.                                              [45] R. Côté, A. Russel, E. E. Eyler, P. L. Gould, New J. Phys. 8
 [21] E. Farhi, S. Gutmann, Phys. Rev. A 58 (1998) 915.                       (2006) 156.
 [22] Y. Aharonov, L. Davidovich, N. Zagury, Phys. Rev. A 48             [46] W. Dür, R. Raussendorf, V. M. Kendon, H.-J. Briegel, Phys.
                                                                                                                                         38

     Rev. A 66 (2002) 052319.                                           [80] X. P. Xu, J. Phys. A 42 (2009) 115205.
[47] P. L. Knight, E. Roldán, J. E. Sipe, Opt. Comm. 227 (2003)        [81] S. Salimi, Ann. Phys. 324 (2009) 1185.
     147.                                                               [82] O. Mülken, V. Bierbaum, A. Blumen, J. Chem. Phys. 124
[48] P. Zhang, X.-F. Ren, X.-B. Zou, B.-H. Liu, Y.-F. Huang, G.-C.           (2006) 124905.
     Guo, Phys. Rev. A 75 (2007) 052310.                                [83] C. Cai, Z. Y. Chen, Macromolecules 30 (1997) 5104.
[49] H. B. Perets, Y. Lahini, F. Pozzi, M. Sorel, R. Morandotti,        [84] R. Iwanow, D. A. May-Arrioja, D. N. Christodoulides, G. I.
     Y. Silberberg, Phys. Rev. Lett. 100 (2008) 170506.                      Stegeman, Y. Min, W. Sohler, Phys. Rev. Lett. 95 (2005)
[50] O. Mülken, A. Blumen, T. Amthor, C. Giese, M. Reetz-                   053902.
     Lamour, M. Weidemüller, Phys. Rev. Lett. 99 (2007) 090601.        [85] A. Bar-Haim, J. Klafter, R. Kopelman, J. Am. Chem. Soc. 119
[51] D. Burgarth, Quantum state transfer with spin chains, Ph.D.             (1997) 6197.
     thesis, University College London (2006).                          [86] D. Rana, G. Gangopadhyay, J. Chem. Phys. 118 (2003) 434.
[52] S. Bose, Contemp. Phys. 48 (2007) 13.                              [87] E. Y. Poliakov, V. Chernyak, S. Tretiak, S. Mukamel, J. Chem.
[53] W. R. Anderson, J. R. Veale, T. F. Gallagher, Phys. Rev. Lett.          Phys. 110 (1999) 8161.
     80 (1998) 249.                                                     [88] A. Blumen, V. Bierbaum, O. Mülken, Physica A 371 (2006)
[54] I. Mourachko, C. Comparat, F. de Tomasi, A. Fioretti, P. Nos-           10.
     baum, V. Akulin, P. Pillet, Phys. Rev. Lett. 80 (1998) 253.        [89] A. M. Childs, E. Farhi, S. Gutmann, Quantum Information
[55] S. Westermann, T. Amthor, A. L. de Oliveira, J. Deiglmayr,              Processing 1 (2002) 35.
     M. Reetz-Lamour, M. Weidemüller, Eur. Phys. J. D 40 (2006)        [90] E. Agliari, A. Blumen, O. Mülken, J. Phys. A 41 (2008)
     37.                                                                     445301.
[56] G. S. Engel, T. R. Calhoun, R. L. Read, T.-K. Ahn, T. Manal,       [91] M. G. Cosenza, R. Kapral, Phys. Rev. A 46 (1992) 1850.
     Y.-C. Cheng, R. E. Blankenship, G. R. Fleming, Nature 446          [92] A. Blumen, A. Jurjiu, J. Chem. Phys. 116 (2002) 2636.
     (2007) 782.                                                        [93] O. Mülken, V. Pernice, A. Blumen, Phys. Rev. E 76 (2007)
[57] E. Collini, C. Y. Wong, K. E. Wilk, P. M. G. Curmi, P. Brumer,          051125.
     G. D. Scholes, Nature 463 (2010) 644.                              [94] S. Jespersen, I. M. Sokolov, A. Blumen, Phys. Rev. E 62
[58] D.-J. Heijs, V. A. Malyshev, J. Knoester, J. Chem. Phys. 121            (2000) 4405.
     (2004) 4884.                                                       [95] E. J. Heller, Phys. Rev. A 35 (1987) 1360.
[59] S. M. Vlaming, D. J. Heijs, J. Knoester, J. Lumin. 111 (2005)      [96] X. P. Xu, F. Liu, Phys. Lett. A 372 (2008) 6727.
     349.                                                               [97] X. P. Xu, F. Liu, New J. Phys. 10 (2008) 123012.
[60] A. Blumen, A. Volta, A. Jurjiu, T. Koslowski, J. Lumin. 111        [98] X. P. Xu, W. Li, F. Liu, Phys. Rev. E 78 (2008) 052103.
     (2005) 327.                                                        [99] O. Mülken, V. Pernice, A. Blumen, Phys. Rev. E 77 (2008)
[61] M. R. Shortreed, S. F. Swallen, Z.-Y. Shi, W. Tan, Z. Xu,               021117.
     C. Devadoss, J. S. Moore, R. Kopelman, J. Phys. Chem. B           [100] M. Abramowitz, I. A. Stegun (Eds.), Handbook of Mathemat-
     101 (1997) 6318.                                                        ical Functions, Dover, New York, 1972.
[62] O. Varnavski, I. D. W. Samuel, L.-O. Palsson, R. Beavington,      [101] C. M. Bender, S. A. Orszag, Advanced Mathematical Methods
     P. L. Burn, T. G. III, J. Chem. Phys. 116 (2002) 8893.                  for Scientists and Engineers, McGraw-Hill, Inc., 1978.
[63] O. P. Varnavski, J. C. Ostrowski, L. Sukhomlinova, R. J.          [102] X. P. Xu, Phys. Rev. E 77 (2008) 061127.
     Twieg, G. C. Bazan, T. G. III, J. Am. Chem. Soc. 124 (2002)       [103] O. Mülken, V. Bierbaum, A. Blumen, Phys. Rev. E 75 (2007)
     1736.                                                                   031121.
[64] G. R. Fleming, G. D. Scholes, Nature 431 (2004) 256.              [104] Y. Yin, D. E. Katsanos, S. N. Evangelou, Phys. Rev. A 77
[65] Y. C. Cheng, R. J. Silbey, Phys. Rev. Lett. 96 (2006) 028103.           (2008) 022302.
[66] M. Mohseni, P. Rebentrost, S. Lloyd, A. Aspuru-Guzik, The         [105] O. Mülken, V. Pernice, A. Blumen, Phys. Rev. E 78 (2008)
     Journal of Chemical Physics 129 (2008) 174106.                          021115.
[67] F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, M. B. Plenio,      [106] E. Agliari, O. Mülken, A. Blumen, Int. J. Bif. Chaos 20 (2010)
     The Journal of Chemical Physics 131 (2009) 105106.                      271.
[68] A. Olaya-Castro, C. F. Lee, F. F. Olsen, N. F. Johnson, Phys.     [107] O. Mülken, A. Blumen, Physica E 42 (2010) 576.
     Rev. B 78 (2008) 085115.                                          [108] M. M. Sternheim, J. F. Walker, Phys. Rev. C 6 (1972) 114.
[69] H.-P. Breuer, F. Petruccione, The Theory of Open Quantum          [109] P. E. Parris, Phys. Rev. B 40 (1989) 4928.
     Systems, Oxford University Press, Oxford, England, 2006.          [110] X. P. Xu, Phys. Rev. E 79 (2009) 0n11117.
[70] D. Aharonov, A. Ambainis, J. Kempe, U. Vazirani, in: Pro-         [111] A. Volta, J. Phys. A 42 (2009) 225003.
     ceedings of ACM Symposium on Theory of Computation                [112] A. Blumen, C. von Ferber, A. Jurjiu, T. Koslowski, Macro-
     (STOC’01), ACM Press, New York, 2001, p. 50.                            molecules 37 (2004) 638.
[71] O. Mülken, A. Volta, A. Blumen, Phys. Rev. A 72 (2005)           [113] W. P. Schleich, Quantum Optics in Phase Space, Wiley-VCH,
     042334.                                                                 Berlin, 2001.
[72] O. Mülken, A. Blumen, Phys. Rev. E 71 (2005) 036128.             [114] E. P. Wigner, Phys. Rev. 40 (1932) 749.
[73] O. Mülken, A. Blumen, Phys. Rev. E 73 (2006) 066117.             [115] M. Hillery, R. F. O’Connell, M. O. Scully, E. P. Wigner, Phys.
[74] O. Mülken, Preprint (2007) arXiv:0710.3453.                            Rep. 106 (1984) 121.
[75] I. S. Gradshteyn, I. M. Ryzhik, Table of Integrals, Series, and   [116] W. K. Wootters, Ann. Phys. 176 (1987) 1.
     Products, Academic Press, 1980.                                   [117] O. Cohendet, P. Combe, M. Sirugeu, M. Sirugue-Collin, J.
[76] S. Alexander, J. Bernasconi, W. R. Schneider, R. Orbach, Rev.           Phys. A 21 (1988) 2875.
     Mod. Phys. 53 (1981) 175.                                         [118] U. Leonhardt, Phys. Rev. Lett. 74 (1995) 4101.
[77] S. Salimi, Quantum Inf. Process. 9 (2009) 75.                     [119] U. Leonhardt, Phys. Rev. A 53 (1996) 2998.
[78] K. Ito (Ed.), Encyclopedic Dictionary of Mathematics, MIT-        [120] O. Mülken, A. Blumen, Phys. Rev. A 73 (2006) 012105.
     Press, Cambridge, MA, 1987.                                       [121] X. P. Xu, F. Liu, Phys. Rev. A 77 (2008) 062318.
[79] A. Volta, O. Mülken, A. Blumen, J. Phys. A 39 (2006) 14997.      [122] A. O. Caldeira, A. J. Legget, Ann. Phys. 149 (1983) 374.
                                                                                                                                     39

[123] A. O. Caldeira, A. J. Legget, Ann. Phys. 153 (1984) 445(E).     [129] O. Mülken, L. Mühlbacher, T. Schmid, A. Blumen, Phys. Rev.
[124] S. A. Gurvitz, L. Fedichkin, D. Mozyrsky, G. P. Berman, Phys.         E 81 (2010) 041114.
      Rev. Lett. 91 (2003) 066801.                                    [130] L. Mühlbacher, J. Ankerhold, C. Escher, J. Chem. Phys. 121
[125] D. Solenov, L. Fedichkin, Phys. Rev. A 73 (2006) 012308.              (2004) 12696.
[126] D. Solenov, L. Fedichkin, Phys. Rev. A 73 (2006) 012313.        [131] L. Mühlbacher, J. Ankerhold, J. Chem. Phys. 122 (2005)
[127] L. Fedichkin, D. Solenov, C. Tamon, Q. Inf. Processing 6              184715.
      (2006) 263.
[128] S. Salimi, R. Radgohar, J. Phys. A 42 (2009) 475302.
