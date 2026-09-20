# Continuous-time quantum walks with defects and disorder - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.88.042334
> Collected: 2026-09-20
> Published: 2013-10-29
> Zotero parent key: 7B8G38RK
> Evidence: Publisher or author-preprint PDF

PHYSICAL REVIEW A 88, 042334 (2013)


                             Continuous-time quantum walks with defects and disorder

                                                  J. A. Izaac,* J. B. Wang,† and Z. J. Li
                            School of Physics, The University of Western Australia, Crawley WA 6009, Australia
                                          (Received 6 August 2013; published 29 October 2013)
                  With the advent of physical implementations of quantum walks, a general theoretical and efficient numerical
               framework is required for the study of their interactions with defects and disorder. In this paper, we derive
               analytic expressions for the eigenstates of a one-dimensional continuous-time quantum walk interacting with
               a single defect, before investigating the effects of multiple diagonal defects and disorder, with emphasis on its
               transmission and reflection properties. Complex resonance behavior is demonstrated, showing alternating bands
               of zero and perfect transmission for various defect parameters. Furthermore, we provide an efficient numerical
               method to characterize quantum walks in the presence of diagonal disorder, paving the way for selective control
               of quantum walks via the optimization of position-dependent defects. The numerical method can be readily
               extended to higher dimensions and multiple interacting walkers.

               DOI: 10.1103/PhysRevA.88.042334                                PACS number(s): 03.67.Lx, 05.40.Fb, 05.45.Mt


                      I. INTRODUCTION                                     in very effective exciton traps) [21]. Some earlier works by
                                                                          Dean [22] and Thouless [23] also looked at multiple defects
   Since the seminal paper by Aharonov et al. [1] establishing
                                                                          in relation to the density and distribution of eigenstates. Such
a quantum analogy of the classical walk, quantum walks
                                                                          a tight-binding lattice model has found applications in a wide
have constituted an important tool in quantum information
                                                                          variety of fields. For example, Avgin and Huber [24] applied
theory; for example, by motivating the creation of quantum
                                                                          the one-dimensional, single impurity model to study defects
algorithms that are faster and more efficient than their classical
                                                                          in polyfluorenes.
analogues [2–8] and by providing methods of universal
                                                                              More recently, the theoretical effects of random disorder
quantum computation [9–11]—a highly sought-after goal of
                                                                          in quantum walks have been considered by Yin et al. [25],
modern physics. This is a consequence of the markedly
                                                                          Schreiber et al. [26], and Mülken and Blumen [27] (the latter
different behavior exhibited by quantum walks: by taking into
                                                                          also considering the effects of nonunitary “traps”). Disorder
account superposition, interference, and quantum correlations,
                                                                          and decoherence, however, may provide additional tools in
the quantum walkers propagate quadratically faster than their
                                                                          constructing quantum walks for particular applications—for
classical counterpart and result in a probability distribution
                                                                          instance, Keating et al. [28] considered the application of
drastically different from the classically expected behavior [2].
                                                                          disorder-induced Anderson localization in quantum commu-
As with classical random walks, there are two related but
                                                                          nication. In this work, the point-defect model of diagonal
fundamentally different formulations of the quantum walk: the
                                                                          disorder, which is similar to that of Koster and Slater [20],
discrete-time quantum walk (DTQW) and the continuous-time
                                                                          will be used to derive expressions for the CTQW eigenstates
quantum walk (CTQW). While these are related through
                                                                          for transmission through a single defect. This will then
well-defined limits in the classical case, their relation in the
                                                                          be extended to provide transmission amplitudes through mul-
quantum realm is highly nontrivial, as shown by Strauch [12].
                                                                          tiple defects and, in particular, highlight resonant and bandlike
In this paper, we will focus on the continuous-time quantum
                                                                          structures. Furthermore, a general numerical method will be
walk, with emphasis on its scattering behavior in the presence
                                                                          developed that efficiently calculates transmission information
of disorder and defects.
                                                                          for an arbitrary distribution of diagonal defects, allowing
   Quantum walks have proven incredibly versatile in terms of
                                                                          a detailed study of defect-induced selective transmission of
theoretical applications, with uses ranging from implementing
                                                                          continuous-time quantum walkers.
quantum algorithms to modeling complex quantum systems.
                                                                              This paper is structured as follows. In Sec. II, we introduce
In order to benefit from these newfound ideas, physical
                                                                          the mathematical formalism behind continuous-time quantum
implementations are essential; some recent approaches include
                                                                          walks and, in particular, the diagonal point-defect model.
the use of waveguides and photonics [13–16] and ion lattices
                                                                          Analytic expressions for the single-defect eigenstates are
[17–19]. With physical implementations of quantum walks
                                                                          presented in Sec. III. Expressions for CTQW transmission
comes the issue of disorder and decoherence affecting the
                                                                          through multiple, equally spaced defects are then derived in
sought after quantum behavior. In a precursor to modern
                                                                          Sec. IV and used to verify the results of a general numerical
quantum walking systems, the limiting case of a single
                                                                          method for arbitrary defect distributions, which is detailed in
diagonal defect in a one-dimensional molecular crystal was
                                                                          Sec. V. Finally, our conclusions are provided in Sec. VI.
explored quantitatively by Koster and Slater [20] using tight-
binding methods and difference equations, and later extended
to take into account nearest-neighbor interactions (resulting                       II. CTQW DIAGONAL DEFECT MODEL
                                                                             Continuous-time quantum walks were first introduced by
                                                                          Farhi and Gutmann [29] in 1998 as an extension of the
 *
     josh.izaac@uwa.edu.au                                                classical theory of Markov processes. While research into
 †
     wang@physics.uwa.edu.au                                              continuous-time quantum walks has not been as extensive

1050-2947/2013/88(4)/042334(9)                                    042334-1                                  ©2013 American Physical Society
J. A. IZAAC, J. B. WANG, AND Z. J. LI                                                         PHYSICAL REVIEW A 88, 042334 (2013)

as the discrete-time case, some applications that have arisen             Symmetries that are present in continuous-space quantum
include efficient
             √ spatial search algorithms that achieve a               systems, for instance invariance under spatial translation
speedup of N over classical counterparts [4], exploring               for free particles, can also be formulated for discrete-space
topological structure [30], and modeling coherent transport           systems. This symmetry allows us to define the momen-
on complex networks [27] (such as mass and energy trans-              tum eigenstate |k: a complete orthonormal basis of the
port in complex molecular structures). Furthermore, recent            Hamiltonian, satisfying the eigenvalue equation H0 |k =
experimental evidence for energy transfer through quantum             2(1 − cos k)|k for −π ⩽ k < π . Analogous in function to
coherence in photosynthetic and other biochemical systems             the momentum eigenstates encountered in continuous-space
[31–34] suggests that continuous-time quantum walks can be            quantum mechanics, these are an important tool in studying
extended to model biological systems—potentially providing            scattering properties in discrete space and, as such, have been
new insights into the natural world.                                  described in detail by Childs et al. [3], Farhi et al. [10],
   The continuous-time quantum walk can be regarded as                Mülken and Blumen [27], Childs and Gosset [11], Mülken
a quantization of the corresponding classical continuous-             et al. [35], and Childs et al. [36] (albeit with slight variations in
time random walk, with the system now evolving as per                 definition). For example, consider a continuous-time quantum
the Schrödinger equation rather than the Markovian master            walk on an infinite line, scattering off a defect placed at node
equation. As a result, classical probabilities are replaced           |d. To account for these defects, the Hamiltonian matrix is
by quantum probability amplitudes. To illustrate, consider a          modified in the following way:
continuous-time random walk on the discrete graph G(V ,E),                                                  
composed of unordered vertices j ∈ V and edges ei = (j,k) ∈                         H = H0 + ,  =             m |mm|,             (5)
E connecting two vertices j and k. The transition rate matrix                                               m
H is defined as
       ⎧                                                              where we have introduced a real diagonal matrix , with
       ⎨−γj k for j = k if node j is connected to node k             m ∈ Z,m ∈ {d} representing the set of vertices associated
Hj k = 0        for j = k if node j is not connected to node k       with a defect of strength m . The probability of the walker
       ⎩S       for j = k,
           j                                                          being found at node |j  at time t can thus be given by
                                                               (1)    |j |e−iH t |ψ(0)|2 .
                                                                          Now, let the quantum walker be initialized in momentum
where γj k is the probability per unit time for making a              eigenstate |k incident from the left; this results in a time-
transition from node j to node k and for H to be conservative,        independent scattered state of the form
                               
                               N                                                                 
                     Sj =                  γj k .              (2)                                |k + r(k)| − k, j ⩽ d
                                                                                |ψs  = Û |k =                                 (6)
                            k = 1,k = j
                                                                                                  t(k)|k,          j >d

Classically, the state of the random walker is fully described by     (the Bethe ansatz), where t(k)|k and r(k)| − k are the trans-
the probability distribution vector P(t), with its time evolution     mitted and reflected components, respectively. It was shown
governed by the master equation                                       by Childs et al. [3] in the context of algorithmic speedup that,
                      dP(t)                                           given |ψs (k) remains an eigenstate of H = H0 + , a pair of
                             = H P(t),                                linearly independent equations are produced which uniquely
                        dt                                            determine t(k) and r(k). This was further extended by Farhi
which has the formal solution P(t) = exp(−H t)P(0).                   et al. [10] in order to calculate the transmission probability
   Extending the above description to the quantum realm               due to finite trees and semi-infinite lines attached at singular
involves replacing the real-valued probability distribution           nodes. Finally, it was demonstrated by Li et al. [37] that, in the
vector P(t) with a complex-valued wave function |ψ(t) and            presence of double diagonal defects, a CTQW system exhibits
adding the complex notation i to the evolution exponent, i.e.,        resonance behavior determined inherently by the nature of the
                 |ψ(t) = exp(−iH t)|ψ(0).                    (3)    discrete space. In successive sections, we will determine ana-
                                                                      lytic expressions for the complete set of eigenstates for a single
The quantum transition matrix H , often referred to as the            defect and relate this to group velocity. Moreover, we will show
system Hamiltonian, is required to be Hermitian and thus the          through analytical derivations that this previously established
above time evolution is unitary—guaranteeing that the norm of         resonant behavior exists in the case of multiple sets of defects,
|ψ(t) is conservedunder CTQWs. The complex-valued state             and describe an efficient numerical method for exploring
vector |ψ(t) = j aj (t)|j , where aj (t) = j |ψ(t) ∈ C,           systems with arbitrary distributions of diagonal defects.
represents the probability amplitude of the walker being found
at node |j  at time t, with |aj (t)|2 = |j |ψ(t)|2 the resulting
                                                                                   III. SINGLE-DEFECT EIGENSTATES
probability.
   For CTQWs on an infinite line, if each node is assumed                Using the diagonal defect model defined above for a
to be connected only to its neighboring nodes by a constant           CTQW containing a single-point defect on an infinite line,
transition rate γ = 1, then the action of the corresponding           the Hamiltonian can therefore be written as
Hamiltonian H0 on the state vector |ψ(t) leads to the inner                 
product relationship                                                    H =      (2|j j | − |j − 1j | − |j + 1j |) + α|dd|.
                                                                               j
      j |H0 |ψ = 2j |ψ − j + 1|ψ − j − 1|ψ.            (4)                                                                     (7)

                                                                042334-2
CONTINUOUS-TIME QUANTUM WALKS WITH DEFECTS . . .                                                                        PHYSICAL REVIEW A 88, 042334 (2013)


             0.03                                                     0.03                                                  0.03       0.0707
             0.02                                                     0.02
                                                                                                                                          α     1
             0.01                                                     0.01                                                                          α
                                                          j φeven k
                                                                                                                            0.02                            2
j φodd k                                                                                                        d φeven k
             0.00                                                     0.00
             0.01                                                     0.01                                                  0.01
             0.02                                                     0.02
             0.03                                                     0.03
                                                                                                                              0.
                 1000    500         0       500   1000                   1000     500     0      500    1000
                                                                                                                                   0    π4              π2         3π 4     π
                                     j                                                     j                                                            k

                                   (a)                                                   (b)                                                        (c)

    FIG. 1. (Color online) The numeric (orange solid line) and analytic (black dashed line) single-point-defect eigenstates are plotted for the
set of (a) odd continuous
                 √        eigenstates and (b) even continuous eigenstates. (c) The value of the even states at the defect location |0 for defect
strength α = 1/ 200,1,2.

For simplicity, and without loss of generality, choose d = 0.                             where tα (k) = 1/[1 + 12 iα csc k] is simply the transmission
Now let |φ denote the eigenstates of the Hamiltonian,                                    coefficient of the CTQW incident on a single defect. Also recall
with associated eigenvalues λ ∈ R; i.e., H |φ = λ|φ. Ex-                                that, by construction, both eigenstates satisfy the eigenvalue
panding j |H |φ explicitly using Eq. (7) and      the position                         equation
state decomposition of the eigenstates, |φ = j  |j  j  |φ =
                                                                                                H |φ(k) = λ(k)|k, λ(k) = 2(1 − cos k)|k                              (12)
   j  cj  |j , we arrive at the following recurrence relation:

 j |H |φ = 2cj − cj −1 − cj +1 + αc0 δj 0                                               (as is expected, the eigenvalues are of the same form as Koster
                                                                                          and Slater [20] and Merrifield [21] in the case where the lattice
           = λcj ⇒ (2 − λ)cj − cj −1 − cj +1 = αc0 δj 0 .                         (8)
                                                                                          parameter α → 1). Comparing these results to those obtained
We now have an inhomogeneous, linear recurrence equation                                  by numerical analysis (Fig. 1) verifies that these eigenstates do,
with constant coefficients—this equation fully determines the                             in fact, represent the complete set of continuous eigenstates.
eigenstates and eigenvalues of the system. By substituting                                Furthermore, it can be seen that setting α = 0 does, indeed,
in the ansatz cj = r j [20], we readily see that the general                              recover the free-space eigenstates |k, k ∈ [−π,π ].
homogeneous solution is
                               j         j
                    cj = Ar− + Br+                                                                                          B. Bound states
                                        √    √                                               For bound-state |φB  solutions to Eq. (8) to be physical,
                        = 2−j A(2 − λ − λ − 4 λ)j
                                          √    √                                          it is required that j |φB  → 0 as j → ±∞. Restricting
                          + 2−j B(2 − λ + λ − 4 λ)j ,                             (9)     our attention to λ < 0, λ > 4, the method of undetermined
where A and B are as yet undetermined functions of α and                                  coefficients is applied in the case of odd symmetry and even
λ. Using this result as a basis to calculate inhomogeneous                                symmetry (j → |j |). As in the continuous case, both odd and
solutions to Eq. (8), we must consider regimes where both                                 even bound states
                                                                                                        √ exist,
                                                                                                               √ with respective
                                                                                                                          √       √conditions A + B = 0
oscillatory and bound solutions exist.                                                    and A = B( λ − 4 λ − α)/( λ − 4 λ + α).
                                                                                             By taking into account the boundary condition, the odd
                                                                                          bound state turns out to be nonphysical [r− (j ) − r+ (j )
                          A. Continuous eigenstates
                                                                                          diverges as j → ±∞] and must be discarded. The even bound
   To determine the continuous eigenstates, consider oscillat-                            state, of the form
ing solutions of Eq. (9). It is clear that a necessary requirement
for oscillating solutions is |r± | ⩽ 1; this is satisfied only for                               j |φB  = Ar− (|j |) + Br+ (|j |)
                                                                                                                       √      √
0 ⩽ λ ⩽ 4. For convenience, the parametrization λ = 2(1 −                                                               λ−4 λ−α
cos k), 0 ⩽ k ⩽ π , can be used, resulting in a homogeneous                                               = Br− (|j |) √      √     + Br+ (|j |),                         (13)
                                                                                                                        λ−4 λ+α
solution of the form
                                                                                          contains only one divergent term [r− (|j |)] and thus represents
                           cj = Ae−ikj + Beikj .                                 (10)     a physical bound state when the coefficient of r− (|j |) is zero
The method of undetermined coefficients can now be used to                                for all values of α; thus, λ = 2 + α 1 + 4/α 2 . Substituting
calculate the inhomogeneous solutions to the system in this λ                             this back into Eq. (13) and normalizing, the bound state of the
regime. We find that two solutions exist, with odd and even                               system is therefore given by
symmetry around the defect, respectively:                                                                            √    
                                                                                                               2−|j | |α|                4 |j |
                              1                                                                    j |φB  = 2            α − α    1 +         ,     (14)
            j |φodd (k) = √ sin kj , 0 ⩽ k ⩽ π,                                                             (α + 4)1/4                 α2
                               π
                                                                                         satisfying the eigenvalue equation
                              1        1
           j |φeven (k) = √ tα (k)     α csc k sin k|j | + cos kj ,
                               π       2                                                                                                                        4
                        0 ⩽ k ⩽ π,                                  (11)                           H |φB  = λα |φB , λα = 2 + α 1 +                              .      (15)
                                                                                                                                                                α2

                                                                                   042334-3
J. A. IZAAC, J. B. WANG, AND Z. J. LI                                                                                      PHYSICAL REVIEW A 88, 042334 (2013)


                                                                                                              6
                                0.4                                                                                                              λ   0




                                                                                        Eigenvalue spectrum
                                                                                                              4
                                0.2
                    j φB                                                                                      2                      λk
                                0.0

                                0.2                                                                           0
                                                                                                                                                 λ   0
                                0.4                                                                           2
                                      10       5          0             5         10                              0   π4       π2         3π 4           π

                                                          j                                                                     k

    FIG. 2. (Color online) Left: The numeric and analytic single-point defect bound states are plotted and compared for the cases (i) α < 0
with the analytic result in long-dashed black lines and the numerical data points in red open circles, and (ii) α > 0 with the analytic result
in short-dashed black lines and the numerical data points in green dots. Right: The complete eigenvalue spectrum of the Hamiltonian with a
single-point defect.


Some properties of the single-defect bound state that can                              where
be ascertained from the analytic expression include (1) in
the limit |α| → ∞, j − d|φB  → δj d and λα → ∞ (i.e.,                                                                1 −2it  (1−cos k)
the contribution of the bound state to the time evolution of                           Gα,d (j  ,t  ; j ; k) =         e                  sin k(j  − d) sin k(j − d)
                                                                                                                       π
a CTQW outweighs that of the continuous eigenstates for                                                                                                    
large α) and (2) in the limit α → 0, j − d|φB  → 0 and                                                                 1                
limα→0− λα = 0, limα→0+ λα = 4 (i.e., the contribution of the                                                          + |tα (k)| (j − d) (j − d)
                                                                                                                                   2
                                                                                                                         4
bound state to the time evolution of a CTQW is approximately
the trivial solution for small α and can be neglected). It should                                                      + e−iλα t δ(k − 1)φB (j − d)φB (j  − d),
also be noted that for α > 0, the bound-state amplitude shows                                                                                                  (19)
damped oscillating behavior; this is not the case for α < 0
(Fig. 2). However, in both cases, the probability distributions
|vj |φB |2 are equal.                                                                with tα (k) = 1/[1 + (iα/2) csc k], (j ) = α csc k sin√
                                                                                                                                                k|j | +
                                                                                                                                       2−|j | |α|
                                                                                       2 cos kj ,  λα = 2 + α 1 + 4/α 2 ,    φB (j ) = (α 2 +4)1/4 (α −


           C. Eigenstate completeness and time evolution                               α 1 + 4/α 2 )|j | , |d the location of the defect, and α the
                                                                                       defect amplitude.
    Using the orthogonality relations of the sine and cosine                                                                         
                                                                                          Using this integral
                                                                                                      √        approach, j  |e−iH t |ψ is plotted in the
functions, it can be shown that the eigenstates calculated
above remain orthonormal with respect to each other; that                              case of α = 1/ 2, d = 5, |ψ = |v1 , and t  = 20 in Fig. 3. It
is, for all values of 0 ⩽ k ⩽ π and α ∈ R, φodd (k)|φB  =                            can be seen that the integral and the matrix exponential method
0,φeven (k)|φB  = 0, and φodd (k)|φeven (k) = 0. Coupling                          are in excellent agreement.
these results with the completeness of Hermitian eigenstates,                             The Green’s function offers other advantages compared to
the identity operator for the single defect containing discrete                        the previously considered one. For instance, it is now well
space can be written as                                                                defined in the case of the initial state being at the vertex
                                                                                       containing the defect, and the form of the expression is the
                π
                                                                                       same over all space (i.e., there are no piecewise components
    Iˆ =            dk (|φodd (k)φodd (k)| + |φeven (k)φeven (k)|)
            0                                                                          and no need to separate the position space into a “transmitted
           + |φB φB |,                                                      (16)     region,” “reflected region,” etc.). Numerous advantages also
                                                                                       exist compared to the matrix exponential method: the time
                                                                −iH t        −iH t ˆ
and thus the time-evolution operator Û (t) ≡ e                         =e        I    evolution can now be explored on a vertex by vertex basis
has the form                                                                           (reducing computation time as we no longer need to consider
                        π                                                              the entire discrete subspace), numerical integration is less
   Û (t) =                 dke−2it(1−cos k) [|φodd (k)φodd (k)|                     computationally expensive and easier to implement, and
                    0
                                                                                      asymptotic approximations of the integral can be used to
                + |φeven (k)φeven (k)|] + e−iλα t |φB φB |.               (17)     characterize behavior for large or small t and α, among others.
This integral form of the time-evolution operator now enables
us to construct an expression for the time evolution of an
arbitrary state |ψ from time t to t  ,                                                                              IV. MULTIPLE DEFECTS

               
                          π                                                              Using the same mathematical scaffolding discussed in
   j  |e−iH t |ψ(t) =       dkGα,d (j  ,t  ; j ; k)j |ψ(t),                     Sec. II and extending the work of Li et al. [37] to multiple
                                      j    0
                                                                                       defects, the transmission coefficient for N point defects,
                                                                              (18)     located at vertices d0 , . . . ,di , . . . ,dN−1 , can be calculated by

                                                                                 042334-4
CONTINUOUS-TIME QUANTUM WALKS WITH DEFECTS . . .                                                          PHYSICAL REVIEW A 88, 042334 (2013)


                            0.04                                                     2.0


                            0.03                                                     1.5
                     2                                                       10 16
                     j ψ    0.02                                                     1.0

                            0.01                                                     0.5

                            0.00                                                     0.0
                                             50    0            50                           40      20      0       20     40
                                                   j                                                          j

                                                  (a)                                                        (b)
                                                                                                                                               √
   FIG. 3. (Color online) (a) The time evolution of the initial state |1 for time t  = 20, with a defect placed at d = 5 with strength α = 1/ 2,
using the matrix exponential definition (blue line) and the integral approach (18) (red data points). (b) A plot of the absolute error between both
methods.


starting with the scattered state ansatz,                                            ω3 = − 18 iαe2ikL csc3 k[2 cos 2kL(α 2 − 2iα sin k − 3)
             ⎧
             ⎪  |k + r1 (k)| − k,      j < d0                                              + 4α sin k(i − 2 sin 2kL) − 3i sin 2k(L + 1)
             ⎪
             ⎪
             ⎪
             ⎪                ..                                                             + 6i sin 2kL − 3i sin 2k(L − 1) + 3 cos 2k(L − 1)
             ⎪
             ⎪
             ⎨                 .
                                                                                             + 3 cos 2k(L + 1) − 2α 2 ],                    (23b)
  |ψs (k) = ti (k)|k + ri+1 | − k, di−1 < j < di                   (20)
             ⎪
             ⎪
             ⎪
             ⎪                 ..                                              and thus
             ⎪
             ⎪                  .
             ⎪
             ⎩                                                                       2 = 4 α csc k(α sin kL + 2 sin k cos kL) ,
                                                                                         1 2    4                            2
                tN (k)|k,               dN−1 ⩽ j.                                                                                          (24a)
                                                                                     3 = 16 α csc k[(α − 2) cos 2kL − 4α sin k sin 2kL
                                                                                         1 2     6    2
The Hamiltonian of the system is now given by
                                                                                          + cos 2k(L − 1) + cos 2k(L + 1) + cos 2k − α 2 − 1]2 .
      H =       (2|j j | − |j − 1j | − |j + 1j |)
                                                                                                                                            (24b)
                 j

                     
                     N−1                                                       The analytic form of T (k) for the 5- and 8-point defect is too
                +           αi |di di |,                            (21)     long and complex to be reproduced here. The transmission
                      i=0                                                      coefficients for N = 2,3,5, and 8 are plotted and compared in
                                                                               Fig. 4 for barrier strength α = 1 and separations of L = 0,1,2,
and so the eigenvalue condition,                                               and 5. It can be seen that as N → ∞, the local minimums
                     j |H |ψs (k)                                            of T (k) approach zero, while the resonant peaks widen.
                                    = 2(1 − cos k)                             Furthermore, oscillation amplitudes appear to decrease, and
                       j |ψs (k)
                                                                               the transition between regions of perfect and zero transmission
(which must hold for all j ∈ Z and −π ⩽ k < π ), can then                      becomes much sharper. Qualitatively, this appears indicative
be applied to all possible regions described by Eq. (20). As                   of the electronic band structure observed in continuous-space
before, this produces a set of 2N linearly independent linear                  models of crystal lattices. The results are also visualized
equations relating t1 (k), . . . ,tN (k),r1 (k), . . . ,rN (k), which can      in Fig. 5, showing the effect of defect amplitude α on the
then be solved to calculate all the transmission and reflection                transmission coefficient for the case N = 8. It is easily seen
amplitudes. Note that there is the added caveat that as N                      that, by altering α, a method is provided to control the
increases, the complexity of the analytic form of ti (k) and                   placement and size of the unity transmission band.
ri (k) appears to drastically increase—suggesting that for                        Ultimately, however, this method of calculating the trans-
N significantly large, analytic approximations or numerical                    mission for N defects becomes unwieldy for large N , as
methods may be preferable.                                                     the increasing number of linearly independent equations
    Using this method, the transmission coefficient was calcu-                 required to calculate ri (k),ti (k) scales by O(2N ) and results in
lated in the case of the 2, 3, 5, and 8-point defects, respectively.           drastically larger computation times. Further, we are usually
For convenience, allowing di+1 − di = L and αi = α∀i (i.e.,                    only interested in calculating r1 (k) and tN (k); this motivates
all barriers have equal separation and amplitude), the trans-                  the creation of an algorithm to more efficiently characterize
mission amplitude is given by                                                  CTQW transmission through multiple arbitrary defects.
                1                            1
  tN (k) =          ⇒ TN (k) = |tN (k)|2 =      ,                     (22)                   V. A GENERAL NUMERICAL APPROACH
             1 + ωN                        1+ N
                                                                                                     FOR MULTIPLE DEFECTS
where
                                                                                 In the case of continuous-space quantum mechanics, the
  ω2 = iα csc k + 14 α 2 (e2ikL − 1) csc2 k,                         (23a)     Fourier method approach utilized by Yiu and Wang [38],

                                                                        042334-5
J. A. IZAAC, J. B. WANG, AND Z. J. LI                                                                               PHYSICAL REVIEW A 88, 042334 (2013)


                  1.0                                                                          1.0

                  0.8                                                                          0.8

                  0.6                                                                          0.6
            T k                                                                          T k
                  0.4                                                                          0.4

                  0.2                                                                          0.2

                  0.0                                                                          0.0
                        0.0        0.5        1.0     1.5     2.0           2.5    3.0               0.0   0.5   1.0     1.5    2.0     2.5         3.0
                                                          k                                                               k
                                              (a) L = 0                                                          (b) L = 1


                  1.0                                                                          1.0

                  0.8                                                                          0.8

                  0.6                                                                          0.6
            T k                                                                          T k
                  0.4                                                                          0.4

                  0.2                                                                          0.2

                  0.0                                                                          0.0
                        0.0        0.5        1.0     1.5     2.0           2.5    3.0               0.0   0.5   1.0     1.5    2.0     2.5         3.0
                                                          k                                                               k
                                              (c) L = 2                                                          (d) L = 5

   FIG. 4. (Color online) Transmission coefficient vs momentum for a CTQW momentum eigenstate incident on an N -point defect, where
N = 2 (blue dot-dashed line), N = 3 (red dashed line), N = 5 (black dotted line), and N = 8 (green solid line). The defect-induced barriers
are constructed with unity amplitude (α = 1) and equal separation L.

                                                                                                                                    
Falloon and Wang [39], and Manouchehri and Wang [40]                                      Using position space completeness (Iˆ = j |vj vj |) coupled
provides an efficient method of numerically calculating the                               with the inner product k|vj  = e−ikj , this expression can be
transmission coefficient T (k) over a wide range of k. In                                 evaluated explicitly in terms of probability amplitudes of the
this section, this method will be adapted for the CTQW on                                 walker at each vertex:
the infinite line and verified against the multibarrier analytic
                                                                                                                           −ikj             2
solution derived in the previous section.                                                                   |k|ψt |2   
                                                                                                                             j e      j |ψt 
   Consider an arbitrary initial state |ψ0  incident on a set of                                   T (k) =            =                     .    (28)
                                                                                                            |k|ψ0 |2          −ikj j |ψ 2
defects or barriers, with the transmitted component denoted                                                                  j e           0
|ψt  and produced as per the transmission amplitude t(k).
Using the completeness of the momentum eigenstates, these                                     The numerical calculation of the inner product j |ψt  =
can be written as                                                                         j |e−iH t |ψ0  is performed by expanding the matrix exponen-
          1     π
                                           1     π                                        tial via the Chebyshev expansion scheme, as detailed in Wang
|ψ0  =           dk|kk|ψ0 , |ψt  =            dk|kk|ψt .                          and Scholz [41]. This method is particularly beneficial for two
         2π −π                            2π −π
                                                                                          major reasons: first, since the coefficients of the expansion
                                                            (25a)                         are Bessel functions, they vanish after a finite number of
Evolving the state |ψ0  through time via the unitary operator                            terms, allowing for an exceptionally high level of accuracy
Ût , which acts to separate out the transmitted component,                               with a comparatively small number of terms. Second, this
                                                π                                         is an example of a global propagator, negating the need for
                                          1
           |ψt  = Ût |ψ0  =                      dk Ût |kk|ψ0                      iterative calculations at smaller time steps which can introduce
                                         2π    −π                                         accumulation error.
                              π
                       1                                                                      Briefly outlining the expansion, we have
                  =                dkt(k)|kk|ψ0 ,                              (26)
                      2π      −π
                                                                                          Ut ≡ e−iH t/h̄
and comparing this with Eq. (25a), it can be seen that we                                                                                   ∞
                                                                                                                                                                   
require                                                                                                                                      
                                                                                               = e−i(λmax +λmin )t/2 J0 (η)φ0 (−i H̃ ) + 2         Jn (η)φn (−i H̃ ) ,
                                          |k|ψt |                     2                                                                    n=1
 k|ψt  = t(k)k|ψ0  ⇒ T (k) = |t(k)| =            .2
                                                                                  (27)
                                          |k|ψ0 |2                                                                                                             (29)

                                                                                    042334-6
CONTINUOUS-TIME QUANTUM WALKS WITH DEFECTS . . .                                                                     PHYSICAL REVIEW A 88, 042334 (2013)


                   1.0                                                                   1.0

                   0.8                                                                   0.8

                   0.6                                                                   0.6
             T k                                                                  T k
                   0.4                                                                   0.4

                   0.2                                                                   0.2

                   0.0                                                                   0.0
                         0.0         0.5     1.0     1.5      2.0   2.5    3.0                 0.0       0.5    1.0      1.5           2.0         2.5     3.0
                                                          k                                                                  k
                                                 (a) L = 1                                                           (b) L = 2

    FIG. 5. (Color online) Transmission coefficient vs momentum for a CTQW momentum eigenstate incident on an evenly spaced 8-point
defect, with barrier amplitudes α = 0.1 (blue dot-dashed line), α = 0.5 (red dashed line), α = 1 (black dotted line), and α = 2 (green solid
line).


where λmax and λmin are maximum and minimum eigenvalues                            Noting that
of the Hamiltonian matrix H , η = (λmax − λmin )t/2, Jn (η) are                                              2                2
                                                                                                                            
the Bessel functions of the first kind, and φn are the Chebyshev                                                                       
                                                                                              e−ikj j |j   =   e−ikj δjj   = |e−ikj |2
polynomials. To ensure convergence, the Hamiltonian needs                                                                     
                                                                                                     j                            j
to be normalized as
                                                                                                                        = 1∀k ∈ [−π,π ),                          (32)
            =        1
           H                   [2H − λmax − λmin ].         (30)                   this allows the expression for the transmission coefficient give
                 λmax − λmin
                                                                                   by Eq. (28) to reduce to
   This method can now be used to investigate the behavior of a                                                         2
CTQW on an infinite line, incident on an arbitrary distribution                                                        
                                                                                                           −ikj         
of diagonal defects. However, for comparison purposes, we                                    T (k) =     e      j |ψt  ∀k ∈ [−π,π ).       (33)
                                                                                                                        
will restrict our attention to N equally spaced diagonal defects.                                                j
The Hamiltonian under investigation is therefore given by                                                         
                                                                                      Using Eq. (29), T (k) = | j e−ikj j |e−iH t |j  |2 is calcu-
                                                                                  lated for t = 300, chosen sufficiently large such that the
            H =        (2|j  − |j − 1 − |j + 1) j |
                                                                                   probability of the walker remaining located between the
                     j                                                                                    
                                                                                   defects is small, i.e., (N−1)L
                                                                                                            j =0  |d + j |ψ(t)|2 ≈ 0. The results
                         
                         N−1
                                                                                   are plotted in Fig. 6 for a variety of different values of L
                   +           αn |d + nLd + nL|,                       (31)
                                                                                   and compared to the analytic solution derived in Sec. IV.
                         n=0
                                                                                   It is observed that the numeric results closely match the
where αn ∈ R represents the amplitude of the nth defect, d ∈ Z                     analytic solutions, with an average absolute difference of
is the position of the first defect, and L ∈ N is the integer                      σT = 2.64 × 10−3 . As an aside, note the presence of Gibbs
spacing between defects. For convenience, the initial state is                     phenomenon at the boundaries of the domain due to the use of
chosen such that the walker is localized at a vertex to the left                   Fourier methods. By restricting the analysis to 0.5 < k < 2.5,
of the double reflecting barriers, i.e., |ψ(0) = |vj  , j  < 0.                the absolute difference between the numeric and analytic


                   1.0                                                                         0.010

                   0.8
                                                                                               0.005
                   0.6                                                             T k
             T k                                                                               0.000
                   0.4
                                                                                   T k
                                                                                               0.005
                   0.2

                   0.0                                                                         0.010
                               0.5         1.0      1.5       2.0   2.5     3.0                          0.0   0.5     1.0       1.5         2.0     2.5    3.0
                                                      k                                                                          k

    FIG. 6. (Color online) (a) Transmission coefficient vs momentum of a CTQW momentum eigenstate incident on two defects of unity
amplitude, separated by distances L = 0 (solid blue line), L = 1 (dashed red line), L = 2 (dotted black line), and L = 5 (dot-dashed green
line), and calculated via numerical Fourier methods. (b) Absolute difference between numeric and analytic results for the case L = 1.

                                                                            042334-7
J. A. IZAAC, J. B. WANG, AND Z. J. LI                                                             PHYSICAL REVIEW A 88, 042334 (2013)


results reduces to σT = 3.58 × 10−7 . This general numerical                  In this paper, a one-dimensional continuous-time quantum
approach can now be applied to situations where analytical                walk in the presence of multiple defects was explored
analysis becomes impossible, fine tuning the parameters to                analytically, with the results highlighting resonance behavior
increase accuracy.                                                        previously observed in the case of double diagonal defects. It
   It should be noted that a major source of error associated             was also demonstrated that by increasing the number of defects
with this method is due to a nonzero probability distribution             and by altering the defect amplitudes, “bands” of perfect
located between defects at measurement time. While this can               transmission (surrounded by regions of zero transmission)
be avoided by increasing the time step t, it requires that a              can be selectively placed in momentum space, allowing for
larger number of vertices be included in the propagation grid,            a high level of control of quantum walking characteristics.
as well as an increase in the number of Chebyshev summation               This provides a link between the tight-binding lattice models
terms required for significant accuracy, potentially increasing           widely used in condensed matter physics and the development
the computational time. The additional computational time                 of quantum information applications based on continuous-time
may prove insignificant with the accelerating availability of             quantum walks. Finally, we extended the Fourier-Chebychev
computational power. If not, further refinements (such as                 method utilized in the literature for continuous position
absorbing boundary conditions and multiple passes) may be                 space to the discrete space of CTQWs, which provides a
needed.                                                                   general numerical approach to situations where analytical
                                                                          analysis becomes impossible, such as multiple barriers, higher
                                                                          dimensions, and multiple interacting walkers.
                       VI. CONCLUSIONS
                                                                              Quantum walks remain an important field of study due to
    In the past two decades, quantum walks have played a                  their crucial role in both quantum information processing and
pivotal role in the field of quantum information theory and               the modeling of complex quantum systems. As a result of this
current research is suggesting potential applications across a            research, we hope to provide methods to selectively control and
whole range of different fields, making them an invaluable tool           efficiently characterize the time evolution of quantum walks
in the study of structured, discrete-space systems. Significant           by taking advantage of diagonal disorder that can sometimes
advances are also constantly being made in experimental                   be unavoidable in physical systems.
realizations of quantum walks, providing a means to fully
utilize the computational power of quantum walkers, while                                      ACKNOWLEDGMENT
simultaneously requiring an accurate theoretical and efficient
numerical framework to provide detailed information on the                  J.A.I. would like to thank the Hackett Foundation and the
effects of disorder and scattering on a quantum walk.                     University of Western Australia for financial support.




 [1] Y. Aharonov, L. Davidovich, and N. Zagury, Phys. Rev. A 48,          [15] L. Sansoni, F. Sciarrino, G. Vallone, P. Mataloni, A. Crespi,
     1687 (1993).                                                              R. Ramponi, and R. Osellame, Phys. Rev. Lett. 108, 010502
 [2] J. Kempe, Contemp. Phys. 44, 307 (2003).                                  (2012).
 [3] A. M. Childs, R. Cleve, E. Deotto, E. Farhi, S. Gutmann, and         [16] J. D. A. Meinecke, K. Poulios, A. Politi, J. C. F. Matthews,
     D. A. Spielman, Proceedings of the Thirty-Fifth Annual ACM                A. Peruzzo, N. Ismail, K. Wörhoff, J. L. O’Brien, and M. G.
     Symposium on Theory of Computing STOC ’03 (ACM, New                       Thompson, Phys. Rev. A 88, 012308 (2013).
     York, 2003), pp. 59–68.                                              [17] M. A. Broome, A. Fedrizzi, B. P. Lanyon, I. Kassal, A. Aspuru-
 [4] A. M. Childs and J. Goldstone, Phys. Rev. A 70, 022314                    Guzik, and A. G. White, Phys. Rev. Lett. 104, 153602 (2010).
     (2004).                                                              [18] M. Karski, L. Förster, J. Choi, A. Steffen, W. Alt, D. Meschede,
 [5] S. D. Berry and J. B. Wang, Phys. Rev. A 83, 042317 (2011).               and A. Widera, Science 325, 174 (2009).
 [6] S. D. Berry and J. B. Wang, Phys. Rev. A 82, 042333 (2010).          [19] H. Schmitz, R. Matjeschk, C. Schneider, J. Glueckert, M.
 [7] J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, and S. N.                    Enderlein, T. Huber, and T. Schaetz, Phys. Rev. Lett. 103, 090504
     Coppersmith, Phys. Rev. A 81, 052313 (2010).                              (2009).
 [8] B. L. Douglas and J. B. Wang, J. Phys. A: Math. Theor. 41,           [20] G. F. Koster and J. C. Slater, Phys. Rev. 95, 1167 (1954).
     075303 (2008).                                                       [21] R. E. Merrifield, J. Chem. Phys. 38, 920 (1963).
 [9] A. M. Childs, Phys. Rev. Lett. 102, 180501 (2009).                   [22] P. Dean, Proc. Phys. Soc. 73, 413 (1959).
[10] E.     Farhi,     J.    Goldstone,      and      S.     Gutmann,     [23] D. J. Thouless, J. Phys. C 5, 77 (1972).
     arXiv:quant-ph/0702144.                                              [24] I. Avgin and D. Huber, J. Lumin. 129, 1916 (2009).
[11] A. M. Childs and D. Gosset, J. Math. Phys. 53, 102207 (2012).        [25] Y. Yin, D. E. Katsanos, and S. N. Evangelou, Phys. Rev. A 77,
[12] F. W. Strauch, Phys. Rev. A 74, 030301(R) (2006).                         022302 (2008).
[13] Y. Bromberg, Y. Lahini, R. Morandotti, and Y. Silberberg,            [26] A. Schreiber, K. N. Cassemiro, V. Potoček, A. Gábris, I. Jex,
     Phys. Rev. Lett. 102, 253904 (2009).                                      and C. Silberhorn, Phys. Rev. Lett. 106, 180403 (2011).
[14] A. Peruzzo, M. Lobino, J. C. F. Matthews, N. Matsuda,                [27] O. Mülken and A. Blumen, Phys. Rep. 502, 37 (2011).
     A. Politi, K. Poulios, X. Zhou, Y. Lahini, N. Ismail, K. Wörhoff,   [28] J. P. Keating, N. Linden, J. C. F. Matthews, and A. Winter,
     Y. Bromberg, Y. Silberberg, M. G. Thompson, and J. L. O’Brien,            Phys. Rev. A 76, 012315 (2007).
     Science 329, 1500 (2010).                                            [29] E. Farhi and S. Gutmann, Phys. Rev. A 58, 915 (1998).


                                                                    042334-8
CONTINUOUS-TIME QUANTUM WALKS WITH DEFECTS . . .                                             PHYSICAL REVIEW A 88, 042334 (2013)

[30] E. Agliari, A. Blumen, and O. Mülken, Phys. Rev. A 82, 012305   [35] O. Mülken, A. Blumen, T. Amthor, C. Giese, M. Reetz-Lamour,
     (2010).                                                               and M. Weidemüller, Phys. Rev. Lett. 99, 090601 (2007).
[31] G. S. Engel, T. R. Calhoun, E. L. Read, T. Ahn, T. Mančal, Y.   [36] A. M. Childs, D. Gosset, and Z. Webb, Science 339, 791 (2013).
     Cheng, R. E. Blankenship, and G. R. Fleming, Nature (London)     [37] Z. J. Li, J. A. Izaac, and J. B. Wang, Phys. Rev. A 87, 012314
     446, 782 (2007).                                                      (2013).
[32] E. Collini, C. Y. Wong, K. E. Wilk, P. M. G. Curmi, P. Brumer,   [38] C. Yiu and J. Wang, J. Appl. Phys. 80, 4208 (1996).
     and G. D. Scholes, Nature (London) 463, 644 (2010).              [39] P. E. Falloon and J. B. Wang, Comput. Phys. Commun. 134, 167
[33] D. Mi, G. Liu, J. Wang, and Z. Li, J. Theor. Biol. 241, 152           (2001).
     (2006).                                                          [40] K. Manouchehri and J. B. Wang, J. Comput. Theor. Nanosci. 3,
[34] D. Mi, W. Q. Meng, and Y. Q. Sun, Phys. Rev. E 83, 041901             249 (2006).
     (2011).                                                          [41] J. B. Wang and T. T. Scholz, Phys. Rev. A 57, 3554 (1998).




                                                                042334-9
