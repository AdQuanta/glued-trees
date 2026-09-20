# Experimental investigation of equivalent Laplacian and adjacency quantum walks on irregular graphs - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.105.062448
> Collected: 2026-09-20
> Published: 2022-06-27
> Zotero parent key: FKCKQ2A4
> Evidence: Publisher or author-preprint PDF

PHYSICAL REVIEW A 105, 062448 (2022)



                        Experimental investigation of equivalent Laplacian and adjacency
                                      quantum walks on irregular graphs

                          Dengke Qu ,1,2,* Lei Xiao,2 Kunkun Wang,3 Xiang Zhan ,4,5 and Peng Xue                   2,†
                                   1
                                      Department of Physics, Southeast University, Nanjing 211189, China
                                   2
                                     Beijing Computational Science Research Center, Beijing 100084, China
                        3
                          School of Physics and Optoelectronics Engineering, Anhui University, Hefei 230601, China
                          4
                            School of Science, Nanjing University of Science and Technology, Nanjing 210094, China
                                5
                                  MIIT Key Laboratory of Semiconductor Microstructure and Quantum Sensing,
                                     Nanjing University of Science and Technology, Nanjing 210094, China

                                   (Received 27 February 2022; accepted 9 June 2022; published 27 June 2022)

                 The continuous-time quantum walk denotes the evolution of a particle on a given graph governed by
               Schrödinger’s equation. For different applications, the corresponding Hamiltonian is proportional to either the
               Laplacian or the adjacency matrix of the graph. The two quantum walks are equivalent on regular graphs, since
               each vertex has the same degree. However, for irregular graphs, the evolutions of the two quantum walks are
               generally different. In this paper, we report an experimental investigation of the two quantum walks on irregular
               graphs with single photons and interferometric networks. We demonstrate that it is possible to obtain equivalent
               probability distributions with the two quantum walks on specific irregular graphs, where the particle is initially
               localized at a vertex or uniformly distributed at multiple vertices. Our results not only deepen the understanding
               of the equivalence between the two quantum walks, but also extend the application of the continuous-time
               quantum walk.

               DOI: 10.1103/PhysRevA.105.062448



                       I. INTRODUCTION                                    and the adjacency matrix is used for quantum computation
                                                                          [8,14,37–41]. We refer to the two QWs as the Laplacian QW
    The main pursuit of quantum information is to design
                                                                          and the adjacency QW. The distinction between the Laplacian
large-scale general-purpose quantum computers [1,2]. An
                                                                          QW and the adjacency QW has been explored in terms of
effective platform to develop quantum algorithms is the quan-
                                                                          search algorithms [42] and perfect state transfer [20,43].
tum walk (QW) [3], which is the quantum analog of a classical
                                                                             For the CTQW on a regular graph, where vertices have the
random walk. In QW, a walker can be in superposition of mul-
                                                                          same number of neighbors, the evolutions of the two QWs are
tiple states so that it propagates in superposition of possible
                                                                          equivalent [27,30,44–46]. Thus, the probability distributions
paths. Therefore, QW spreads quadratically faster through the
                                                                          of particles are identical in position space. From a conceptual
interference between paths and entanglement between differ-
                                                                          point of view, an irregular graph has vertices with different
ent degrees of freedom [4,5]. It is useful for a wide range
                                                                          degrees, so the probability distributions of the two QWs gen-
of applications including search algorithms [6–10], quan-
                                                                          erally show differences. However, Wong and Lockhart have
tum simulation [11–13], and universal quantum computation
                                                                          shown that the probability distributions of the two QWs are
[14–16].
                                                                          identical on some specific irregular graphs when the walker
    Similar to a classical random walk, QW has two forms
                                                                          starts from a certain vertex [46]. The equivalence of the two
[17]: the discrete-time quantum walk, which uses a quantum
                                                                          CTQWs has the potential to realize some practical applica-
coin to govern the direction of walk; and the continuous-time
                                                                          tions. For specific physical systems, the way to experimentally
quantum walk (CTQW) [18], which directly defines the walk
                                                                          realize two models of QWs might be different. That is, the
in discrete position space through a time-varying unitary ma-
                                                                          resources or complexity required to realize the Laplacian and
trix that depends on the Hamiltonian of the physical system.
                                                                          adjacency QWs might be different. In that case, we can choose
Traditionally, for the CTQW, the space is represented by a
                                                                          the model at low cost or low complexity to achieve the ap-
graph, which gives its discrete Laplacian as the Hamiltonian
                                                                          plication as the two models are proven to be equal for some
[7,18–22]. Another kind of Hamiltonian is provided by the
                                                                          certain applications.
adjacency matrix [9,23–28].
                                                                             In this paper, we report an experimental simulation of
    The Laplacian is usually used for discrete approximation
                                                                          the Laplacian and the adjacency QWs on irregular graphs
to the kinetic energy operator of quantum mechanics [29–36],
                                                                          with single photons and interferometric networks. Our results
                                                                          demonstrate the equivalence of two QWs on five-vertex and
                                                                          six-vertex irregular graphs with the walker initially localized
 *
     dkqu@seu.edu.cn                                                      at a certain vertex, which support the prediction in Ref. [46].
 †
     gnep.eux@gmail.com                                                   In addition, we confirm that such equivalence depends on the

2469-9926/2022/105(6)/062448(7)                                    062448-1                                 ©2022 American Physical Society
QU, XIAO, WANG, ZHAN, AND XUE                                                                   PHYSICAL REVIEW A 105, 062448 (2022)

                                                                           irregular graphs and analytically prove that the two QWs on
                                                                           these graphs are equivalent when starting at a certain vertex.
                                                                               In this paper, we consider two examples of irregular graphs
                                                                           proposed by Wong and Lockhart [46]. One is an irregular
                                                                           graph with five vertices as shown in Fig. 1. Its adjacency
                                                                           matrix A and the Laplacian L are
    FIG. 1. (a) Irregular graphs with (a) five and (b) six vertices. The                      ⎛                  ⎞
                                                                                                0 1 1 0 0
probability distributions of the two QWs are equivalent, if the particle
                                                                                              ⎜1 0 1 1 1⎟
is initially localized at one of the green vertices.                                          ⎜                  ⎟
                                                                                         A = ⎜ 1 1 0 1 1 ⎟,
                                                                                              ⎝0 1 1 0 0⎠
initial state. Interestingly, we show that equivalence can also                                 0 1 1 0 0
exist even when the walker is initially distributed at multiple                               ⎛                             ⎞
vertices.                                                                                       −2     1     1    0     0
                                                                                              ⎜1      −4     1    1     1⎟
    This paper is organized as follows. In Sec. II, we give a                                 ⎜                             ⎟
                                                                                         L=⎜ 1         1    −4    1     1 ⎟,
                                                                                              ⎝0                        0⎠
brief introduction to the CTQW and illustrate it with irregular
graphs. In Sec. III, we experimentally demonstrate the Lapla-                                          1     1   −2
cian QW and the adjacency QW on the five-vertex irregular                                        0     1     1    0    −2
graph and the six-vertex irregular graph. Section IV contains              respectively. For this graph, the two QWs will have the same
the experimental results of the equivalence of the two QWs.                probability distribution when the initial state is localized at
We conclude with a summary of our observations in Sec. V.                  one of the green vertices, as shown in Fig. 1(a). Moreover,
                                                                           when the initial state is a uniform superposition over vertices
            II. CTQWs ON IRREGULAR GRAPHS                                  2 and 3, and vertices 1, 4, and 5, the probability distributions
  The CTQW is the evolution of a particle in discrete space                of the two QW are also identical. In Sec. III, we elaborate on
governed by Schrödinger’s equation                                         the formula for the superposition states.
                                                                               The other irregular graph has six vertices as shown in
                           d
                             |ψ = H|ψ,                                   Fig. 1(b), which has the adjacency matrix A and the Laplacian
                         i                                        (1)
                          dt                                               L  as
where we set h̄ = 1. The state of the walker at time t is                                 ⎛                        ⎞
                                                                                            0 1 0 1 0 0
|ψ (t ) = e−iHt |ψ (0) and the probability that it is localized                         ⎜1 0 1 1 1 0 ⎟
at vertex x is P(x, t ) = |x|ψ (t )|2 , where {|x} constitutes the                     ⎜                        ⎟
                                                                                         ⎜0 1 0 1 1 1⎟
orthonormal basis spanning the space of the vertices.                               A =⎜                           ⎟,
                                                                                          ⎜1 1 1 0 1 0 ⎟
    As shown in Fig. 1, the discrete space can be represented by                          ⎝0 1 1 1 0 1⎠
a graph G(V, E ) composed of vertices i ∈ V and edges (i, j) ∈                              0 0 1 0 1 0
E . The adjacency matrix A of a graph is defined as                                       ⎛                                    ⎞
                                                                                           −2      1     0     1     0      0
                              1, (i, j) ∈ E ,                                             ⎜1       −4     1     1     1      0⎟
                     Ai j =                                       (2)                     ⎜                                    ⎟
                              0, (i, j) ∈   / E.                                          ⎜  0      1    −4     1     1      1⎟
                                                                                    L = ⎜                                     ⎟,
                                                                                          ⎜1        1     1    −4     1      0⎟
    For a free particle, the Hamiltonian is the kinetic energy of                         ⎝0        1     1     1    −4      1⎠
the particle H = −γ L, which is proportional to the negative                                 0      0     1     0     1     −2
of the Laplacian L = A − D. Here, γ is the jumping rate of the
walk and D is the diagonal matrix, where the diagonal entries              respectively. For the irregular graph with six vertices, the two
Dii = deg(i) represent the degree of vertex i. In some ap-                 QWs have the same probability distribution, where the walker
plications, e.g., search algorithms [9] and PageRank [28,47],              is initially localized at one of the green vertices 1 and 6.
the corresponding Hamiltonian is instead proportional to the               Moreover, the equivalence of the probability distributions of
negative of the adjacency matrix A, H = −γ A. In this paper,               the two QWs is also satisfied for the initial state with equal
we choose γ = 1.                                                           weights at vertices 2 and 4 or equal weights at vertices 3
    For a regular graph, each vertex has the same de-                      and 5.
gree d, so D = dI, where I is the identity matrix. In
this case, the state of the Laplacian QW |ψL (t ) differs
                                                                                      III. EXPERIMENT DEMONSTRATION
from that of the adjacency QW |ψA (t ) by a global phase,
|ψL (t ) = eiLt |ψ (0) = e−idt |ψA (t ). Therefore, the probabil-          We first demonstrate the experimental test of the identical
ity distributions of the two QWs are equivalent, PL (x, t ) =              probability distributions of the two QWs on the irregular
|x|ψL (t )|2 = |x|ψA (t )|2 = PA (x, t ).                              graph with five vertices. As shown in Fig. 2(a), the
    For an irregular graph, some vertices have different de-               experimental setup consists of three stages: the initial-state
grees, and the probability distributions of the two QWs                    preparation, the time evolution of the Laplacian or adjacency
are generally different. However, for some specific irregular              QW, and project measurements. The basis states of the
graphs and localized initial states, equivalence can still be              five-dimensional qudit are encoded as {|1 = |V1 , |2 =
obtained. Wong and Lockhart [46] present eight families of                 |H2 , |3 = |V2 , |4 = |H3 , |5 = |V3 }, where H (V )

                                                                     062448-2
EXPERIMENTAL INVESTIGATION OF EQUIVALENT …                                                         PHYSICAL REVIEW A 105, 062448 (2022)




    FIG. 2. (a) Experimental setup. The heralded single photons are generated and are injected into the optical network to simulate the CTQW
on irregular graphs. The first polarizing beam splitter (PBS), half-wave plates (HWPs), and two beam displacers (BDs) are used to prepare the
initial states. The Laplacian and adjacency QWs can be simulated by an interferometric network, consisting of WPs and BDs. The probability
distributions are obtained by projecting the final state into the basis states via a PBS. The photons are detected by APDs. (b) The 5 × 5
unitary matrix is decomposed into a product of ten two-level unitary matrices. The green nodes represent the two-level unitary operators. The
connection between two matrices indicates that they can be realized at the same time.

denotes the horizontal (vertical) polarizations with the                   m ∈ {2, . . . , 5} and n ∈ {1, . . . , 4}. Here, Um,n denotes the
subscript k (k = 1, 2, 3) denoting the spatial mode.                       two-level unitary matrix that acts only on two vector com-
    In the preparation stage, a pair of photons are generated              ponents, m and n, in five-dimensional Hilbert space with the
via spontaneous parametric down-conversion (SPDC) using                    complementary vector components unchanged. For example,
a β-barium-borate (BBO) crystal. As one trigger photon is                  U4,2 means that the two-level unitary matrix acts only on
detected by a single-photon avalanche photodiode (APD), the                the fourth and second vector components in five-dimensional
signal photon is heralded and injected into the interferomet-              Hilbert space. The decomposition of a unitary operator is
ric network. A polarization beam splitter (PBS), two beam
                                                                                         U = U5,4 · · · U5,1U4,3 · · · U4,1 · · · U2,1 .       (4)
displacers (BDs), and two half-wave plates (HWPs) are used
to prepare the state of the photonic five-dimensional system                   Through this decomposition, the two-level unitary matri-
in different initial states. In the experiment, we prepare four             ces Um,n and Um−1,n+1 can be implemented simultaneously
initial states, which are                                                   in the interferometric networks, thus reducing the number
           ⎧                                                               of optical elements as shown in Fig. 2(b). To realize Um,n ,
           ⎪
           ⎪  (1 0 0 0 0) ,                 vertex 1,                       we first combine the corresponding spatial modes using a
           ⎨(0 1 0 0 0) ,                  vertex 2,
|ψ (0) =                            √
                                                                            BD, and then realize the 2 × 2 unitary matrices using the
           ⎪
           ⎪  (0   1   1    0    0)   / 2,  vertices 2 and 3,               array of wave plates (WPs). Therefore, in the experimental
           ⎩                        √
              (1 0 0 1 1) / 3, vertices 1, 4, and 5.                        simulation, the difference between the unitary operators of the
                                                              (3)           two QWs, UL and UA , lies in the parameters of the ten sets of
                                                                            WPs. We realize unitary operators UL = eiLt and UA = eiAt for
   In order to demonstrate the dynamics of CTQWs’ e−iHt                     t = {10, 102 , 103 , 104 } in the experiment. Experimentally, we
conveniently and flexibly, the evolution time can be regard as a            can adjust the time parameters using the wave-plate angles.
parameter of the unitary operation. Different time parameters                  In the measurement stage, the probability of the final state
correspond to different unitary matrices. To implement the                  distributed at every vertex is obtained by a projective mea-
unitary operations, we decompose the matrix into a prod-                    surement. A PBS projects the final state into the basis states
uct of ten two-level unitary matrices Um,n [9,48,49], where                 |x (x = 1, . . . , 5). The output photons are finally detected




    FIG. 3. Experimental results of the probability distributions of two QWs at time t = {10, 102 , 103 , 104 } for the irregular graph with five
vertices. The blue and green hatched bars represent the experimental results of the Laplacian and adjacency QWs, respectively. The open bars
correspond to the theoretical predictions of the probability distributions of the two QWs. (a)–(d) indicate the results for QW starting at vertex
1, vertex 2, vertices 2 and 3, and vertices 1, 4, and 5, respectively. Error bars indicate the statistical uncertainty, which are obtained based on
assuming Poissonian statistics.

                                                                    062448-3
QU, XIAO, WANG, ZHAN, AND XUE                                                                          PHYSICAL REVIEW A 105, 062448 (2022)




    FIG. 4. Experimental results of the probability distributions of two QWs at time t = {10, 102 , 103 , 104 } for the irregular graph with six
vertices. The red and green hatched bars represent the experimental results of the Laplacian and adjacency QWs, respectively. The open bars
correspond to the theoretical predictions of the probability distributions of the two QWs. (a)–(d) indicate the results of the two QWs when
starting at vertex 1, vertex 2, vertices 2 and 4, and vertices 3 and 5, respectively. Error bars indicate the statistical uncertainty, which is obtained
based on assuming Poissonian statistics.

by APDs, in coincidence with the trigger photon. For each                         We also measure the probability distributions where the
setup, we record clicks for 1 s and register about 8000 single                initial state is in a uniform superposition over multiple ver-
photons. For the Laplacian (adjacency) QW at time t, we                       tices. In Figs. 3(c) and 3(d), our experimental results show that
can obtain the number of photons at vertex x, NL(A) (x, t ).                  the two QWs on the irregular graph with five vertices evolve
Therefore, the probability of the final state localized at vertex             with the same probability distribution when the initial state is
x can be evaluated as PL(A) (x, t ) = NL(A) (x, t )/ x NL(A) (x, t ).         distributed in either the equal superposition of vertices 2 and
    For the irregular graph with six vertices, the exper-                     3, or that of vertices 1, 4, and 5. The probability distributions
imental simulation is similar to that with five vertices.                     of the two QWs on the irregular graph with six vertices are
In this case, the basis states of the six-dimensional qu-                     still equal when the initial state is distributed in the equal
dit are encoded as {|1 = |H1 , |2 = |V1 , |3 = |H2 , |4 =              superposition of vertices 2 and 4, or that of vertices 3 and 5 as
|V2 , |5 = |H3 , |6 = |V3 }. We prepare the initial states of            shown in Figs. 4(c) and 4(d).
the system as                                                                     To quantify the equivalence between the probability distri-
           ⎧                                                                 butions of the two QWs, we calculate the similarity between
           ⎪
           ⎪ (1 0 0 0 0 0) ,                       vertex 1,
           ⎨(0 1 0 0 0 0) ,                       vertex 2,
                                                                              the measured probability distributions of the two QWs at time
 |ψ (0) =                               √                                   t [12,50–53],
           ⎪
           ⎪ (0    1    0   1     0  0)   /  2,   vertices 2 and 4,
           ⎩                             √                                                                                      2
             (0 0 1 0 1 0) / 2, vertices 3 and 5.                                                      
                                                                 (5)                          S(t ) =         PL (x, t )PA (x, t ) .        (6)
                                                                                                           x
   The six-dimensional evolution operator can be decom-
posed into a product of 15 two-level unitary matrices Um ,n ,               The similarity varies between 0 for completely different
where m ∈ {2, . . . , 6} and n ∈ {1, . . . , 5}. We realize the             distributions and 1 for identical distributions. The results
6 × 6 unitary operators by using 15 sets of WPs and a complex                 of the similarities are presented in Table I. For the
interferometric network. There are at most three two-level
unitary matrices that can be realized simultaneously, i.e., U6,1 ,
U5,2 , and U4,3 . Through this approach, our experiment can also                  TABLE I. The similarities between the measured probability dis-
be generalized to simulations of CTQWs for graphs with more                   tributions of the Laplacian and adjacency QWs.
vertices [9].
                                                                                                 Irregular graph with five vertices
                                                                                                    t = 10      t = 102       t = 103        t = 104
                   IV. EXPERIMENT RESULTS
                                                                              From 1              0.9976(8)     0.9959(10)    0.9977(7)     0.9950(11)
    For each experiment, we evaluate the probability distri-                  From 2              0.1612(58)    0.9768(23)    0.7877(63)    0.7454(69)
butions of the two QWs. The experiment results for the five                   From 2 and 3        0.9836(20)    0.9949(11)    0.9968(9)     0.9824(21)
(six)-vertex graph are shown in Fig. 3 (Fig. 4).                              From 1, 4, and 5    0.9975(8)     0.9988(5)     0.9859(19)    0.9982(6)
    For both graphs, the Laplacian and adjacency QWs have
the same probability distribution when the initial state is local-                                Irregular graph with six vertices
ized in vertex 1 as shown in Figs. 3(a) and 4(a), which verifies                                  t = 10        t = 102      t = 103         t = 104
the equivalence as predicted by Wong and Lockhart [46].                       From 1           0.9684(27)      0.9923(13)    0.9853(19)     0.9860(18)
Moreover, the probability distributions are different when the                From 2           0.6664(73)      0.9866(18)    0.7346(70)     0.9848(19)
initial state is localized at vertex 2, as shown in Figs. 3(b) and            From 2 and 4     0.9885(17)      0.9875(17)    0.9677(28)     0.9649(29)
4(b). Therefore, the equivalence of the probability distribu-                 From 3 and 5     0.9916(14)      0.9946(12)    0.9830(20)     0.9949(11)
tions is state dependent.

                                                                      062448-4
EXPERIMENTAL INVESTIGATION OF EQUIVALENT …                                                  PHYSICAL REVIEW A 105, 062448 (2022)

irregular graph with five vertices, we get the minimum                    The significance of our experiments is the experimental
similarity of the two QWs when starting at vertices 2 and 3,          verification and demonstration of the existence of this equiv-
S(104 ) = 0.9824 ± 0.0021. For the irregular graph with six           alence. For large-scale irregular graphs, the number of spatial
vertices, the minimum similarity of probability distributions         modes Ns and the number of bulk optical elements (BDs) NBD
of the two QWs measured in the experiment when starting               increase with the number of vertices n, i.e., Ns ∼ n/2 and
at vertices 2 and 4 is S(104 ) = 0.9649 ± 0.0029. The                 NBD ∼ 2n − 4. Moreover, our method can be applied to the
reason for the larger uncertainty is that the experimental            recently developed waveguide technology, which promises
implementation of the 6 × 6 unitary matrix requires more              breakthroughs in stability and scalability.
complex interferometric networks.                                         The Laplacian and adjacency QWs are preferred for certain
    The experimental results agree with the theoretical predic-       applications. The choice of the Laplacian and the adjacency
tion very well. The imperfection of the experiment is mainly          matrix affects the efficiency of quantum search algorithms
caused by the accuracy of the WPs and the dephasing in-               [42]. In the case of searching on such an irregular graph,
troduced via the misalignment of the BDs, two of which                there may be equivalence in the search efficiencies of the two
form a Mach-Zehnder interferometer. Thus, we experimen-               QWs. Furthermore, there are some potential applications of
tally demonstrate that on irregular graphs, there is equivalence      our work, i.e., the equivalence of the two QWs on irregular
between Laplacian and adjacency QWs, which depends on                 graphs. For specific physical systems, the way to experimen-
both the graphs and the initial states.                               tally realize two models of QWs might be different. That is,
                                                                      the resources or complexity required to realize the Laplacian
            V. DISCUSSION AND CONCLUSIONS                             and adjacency QWs might be different. In that case, we can
                                                                      choose the model at low cost or low complexity to achieve
    In summary, we have investigated the probability distri-          the application as the two models are proven to be equal for
butions of the Laplacian and adjacency QWs on irregular               some certain applications. There is still a great deal we need
graphs with five and six vertices using single photons and in-        to learn about the Laplacian and the adjacency matrix. For the
terferometric networks. We can decompose an arbitrary n × n           two QWs, the evolution on more complex irregular graphs is a
unitary matrix into n(n − 1)/2 two-level unitary matrices. Our        possible area of research. Whether there are more initial states
experimental setup directly implements the two-level unitary          can still satisfy the equivalence of the two QWs. Our work
matrices in a bulk optical system, the advantage of which is          deepens the understanding of the Laplacian and the adjacency
the flexibility to demonstrate the dynamics of CTQWs [9].             matrix and sheds light on accelerating the development of
The experimental results agree with the prediction proposed           quantum computation.
by Wong et al. [46], i.e., they have the same probability
distribution over the vertices when the walker is initially at
                                                                                          ACKNOWLEDGMENTS
a certain vertex. Our experiments also show that this equiv-
alence depends on the initial state. However, we find and                This work has been supported by the National Natural
experimentally show that the equivalence between the proba-           Science Foundation of China (Grants No. 12025401, No.
bility distributions of the two QWs can also be observed even         U1930402, No. 12004184, No. 12104036, No. 12104009, and
when the walker starts from an equal superposition of specific        No. 12088101). X.Z. is supported by the Natural Science
multiple vertices.                                                    Foundation of Jiangsu Province (Grant No. BK20190428).




 [1] A. Montanaro, Quantum algorithms: An overview, npj                [9] D. Qu, S. Marsh, K. Wang, L. Xiao, J. Wang, and P. Xue,
     Quantum Inf. 2, 15023 (2016).                                         Deterministic Search on Star Graphs via Quantum Walks, Phys.
 [2] A. W. Harrow and A. Montanaro, Quantum computational                  Rev. Lett. 128, 050501 (2022).
     supremacy, Nature (London) 549, 203 (2017).                      [10] N. Pan, T. Chen, H. Sun, and X. Zhang, Electric-circuit re-
 [3] Y. Aharonov, L. Davidovich, and N. Zagury, Quantum random             alization of fast quantum search, Research 2021, 9793071
     walks, Phys. Rev. A 48, 1687 (1993).                                  (2021).
 [4] S. Dadras, A. Gresch, C. Groiseau, S. Wimberger, and G. S.       [11] L. Xiao, X. Zhan, Z. H. Bian, K. K. Wang, X. Zhang, X. P.
     Summy, Quantum Walk in Momentum Space with a Bose-                    Wang, J. Li, K. Mochizuki, D. Kim, N. Kawakami, W. Yi, H.
     Einstein Condensate, Phys. Rev. Lett. 121, 070402 (2018).             Obuse, B. C. Sanders, and P. Xue, Observation of topologi-
 [5] P. Xue, B. C. Sanders, and D. Leibfried, Quantum Walk on a            cal edge states in parity–time-symmetric quantum walks, Nat.
     Line for a Trapped Ion, Phys. Rev. Lett. 103, 183602 (2009).          Phys. 13, 1117 (2017).
 [6] N. Shenvi, J. Kempe, and K. B. Whaley, Quantum random-walk       [12] X. Zhan, L. Xiao, Z. Bian, K. Wang, X. Qiu, B. C. Sanders, W.
     search algorithm, Phys. Rev. A 67, 052307 (2003).                     Yi, and P. Xue, Detecting Topological Invariants in Nonunitary
 [7] A. M. Childs and J. Goldstone, Spatial search by quantum walk,        Discrete-Time Quantum Walks, Phys. Rev. Lett. 119, 130501
     Phys. Rev. A 70, 022314 (2004).                                       (2017).
 [8] S. Chakraborty, L. Novo, A. Ambainis, and Y. Omar, Spatial       [13] K. Wang, X. Qiu, L. Xiao, X. Zhan, Z. Bian, W. Yi, and P. Xue,
     Search by Quantum Walk is Optimal for Almost all Graphs,              Simulating Dynamic Quantum Phase Transitions in Photonic
     Phys. Rev. Lett. 116, 100501 (2016).                                  Quantum Walks, Phys. Rev. Lett. 122, 020501 (2019).



                                                                062448-5
QU, XIAO, WANG, ZHAN, AND XUE                                                                 PHYSICAL REVIEW A 105, 062448 (2022)

[14] A. M. Childs, Universal Computation by Quantum Walk, Phys.        [35] J. R. McClean, M. P. Harrigan, M. Mohseni, N. C. Rubin,
     Rev. Lett. 102, 180501 (2009).                                         Z. Jiang, S. Boixo, V. N. Smelyanskiy, R. Babbush, and H.
[15] N. B. Lovett, S. Cooper, M. Everitt, M. Trevers, and V. Kendon,        Neven, Low-depth mechanisms for quantum optimization, PRX
     Universal quantum computation using the discrete-time quan-            Quantum 2, 030312 (2021).
     tum walk, Phys. Rev. A 81, 042330 (2010).                         [36] A. Candeloro, L. Razzoli, P. Bordone, and M. G. A. Paris, Role
[16] A. M. Childs, D. Gosset, and Z. Webb, Universal computation            of topology in determining the precision of a finite thermometer,
     by multiparticle quantum walk, Science 339, 791 (2013).                Phys. Rev. E 104, 014136 (2021).
[17] F. W. Strauch, Connecting the discrete- and continuous-time       [37] M. Santha, Quantum walk based search algorithms, in Theory
     quantum walks, Phys. Rev. A 74, 030301(R) (2006).                      and Applications of Models of Computation (Springer, Berlin,
[18] E. Farhi and S. Gutmann, Quantum computation and decision              2008), pp. 31–46
     trees, Phys. Rev. A 58, 915 (1998).                               [38] D. Gosset, B. M. Terhal, and A. Vershynina, Universal
[19] E. Agliari, A. Blumen, and O. Mülken, Quantum-walk approach            Adiabatic Quantum Computation via the Space-Time Circuit-
     to searching on fractal structures, Phys. Rev. A 82, 012305            to-Hamiltonian Construction, Phys. Rev. Lett. 114, 140501
     (2010).                                                                (2015).
[20] R. Alvir, S. Dever, B. Lovitz, J. Myer, C. Tamon, Y. Xu, and      [39] X. Qiang, T. Loke, A. Montanaro, K. Aungskunsiri, X. Zhou,
     H. Zhan, Perfect state transfer in Laplacian quantum walk,             J. L. O’Brien, J. B. Wang, and J. C. F. Matthews, Efficient
     J. Algebr. Comb. 43, 801 (2016).                                       quantum walk on a quantum processor, Nat. Commun. 7, 11511
[21] P. Chawla, C. V. Ambarish, and C. M. Chandrashekar, Quantum            (2016).
     percolation in quasicrystals using continuous-time quantum        [40] T. Osada, B. Coutinho, Y. Omar, K. Sanaka, W. J. Munro, and
     walk, J. Phys. Commun. 3, 125004 (2019).                               K. Nemoto, Continuous-time quantum-walk spatial search on
[22] T. Wu, J. A. Izaac, Z.-X. Li, K. Wang, Z.-Z. Chen, S. Zhu,             the Bollobás scale-free network, Phys. Rev. A 101, 022310
     J. B. Wang, and X.-S. Ma, Experimental Parity-Time Symmet-             (2020).
     ric Quantum Walks for Centrality Ranking on Directed Graphs,      [41] X. Qiang, Y. Wang, S. Xue, R. Ge, L. Chen, Y. Liu, A. Huang,
     Phys. Rev. Lett. 125, 240501 (2020).                                   X. Fu, P. Xu, T. Yi, F. Xu, M. Deng, J. B. Wang, J. D. A.
[23] E. Farhi, J. Goldstone, and S. Gutmann, A quantum algorithm            Meinecke, J. C. F. Matthews, X. Cai, X. Yang, and J. Wu,
     for the Hamiltonian NAND tree, Theory Comput. 4, 169 (2008).           Implementing graph-theoretic quantum algorithms on a sili-
[24] S. Bose, A. Casaccino, S. Mancini, and S. Severini, Communi-           con photonic quantum walk processor, Sci. Adv. 7, eabb8375
     cation in XYZ all-to-all quantum networks with a missing link,         (2021).
     Int. J. Quantum Inf. 07, 713 (2009).                              [42] T. G. Wong, L. Tarrataca, and N. Nahimov, Laplacian versus ad-
[25] C. Godsil, State transfer on graphs, Discrete Math. 312, 129           jacency matrix in quantum walk search, Quantum Inf. Process.
     (2012).                                                                15, 4029 (2016).
[26] L. Novo, S. Chakraborty, M. Mohseni, H. Neven, and Y. Omar,       [43] M. Christandl, N. Datta, A. Ekert, and A. J. Landahl, Perfect
     Systematic dimensionality reduction for quantum walks: Op-             State Transfer in Quantum Spin Networks, Phys. Rev. Lett. 92,
     timal spatial search and transport on non-regular graphs, Sci.         187902 (2004).
     Rep. 5, 13304 (2015).                                             [44] Y. Elon, Eigenvectors of the discrete Laplacian on regular
[27] J. A. Izaac, X. Zhan, Z. Bian, K. Wang, J. Li, J. B. Wang, and         graphs—a statistical approach, J. Phys. A: Math. Theor. 41,
     P. Xue, Centrality measure based on continuous-time quantum            435203 (2008).
     walks and experimental realization, Phys. Rev. A 95, 032318       [45] A. Abiad, B. Brimkov, A. Erey, L. Leshock, X. Martínez-
     (2017).                                                                Rivera, S. O, S.-Y. Song, and J. Williford, On the Wiener index,
[28] K. Wang, Y. Shi, L. Xiao, J. Wang, Y. N. Joglekar, and P. Xue,         distance cospectrality and transmission-regular graphs, Discrete
     Experimental realization of continuous-time quantum walks on           Appl. Math. 230, 1 (2017).
     directed graphs and their application in PageRank, Optica 7,      [46] T. G. Wong and J. Lockhart, Equivalent Laplacian and adja-
     1524 (2020).                                                           cency quantum walks on irregular graphs, Phys. Rev. A 104,
[29] R. Guantes and S. C. Farantos, High order finite difference            042221 (2021).
     algorithms for solving the Schrödinger equation in molecular      [47] Y. Wang, S. Xue, J. Wu, and P. Xu, Continuous-time quantum
     dynamics, J. Chem. Phys. 111, 10827 (1999).                            walk based centrality testing on weighted graphs, Sci. Rep. 12,
[30] P. Kurzyński and A. Wójcik, Discrete-time quantum walk ap-            6001 (2022).
     proach to state transfer, Phys. Rev. A 83, 062315 (2011).         [48] M. A. Nielsen and I. L. Chuang, Quantum Computation and
[31] T. G. Wong and P. Philipp, Engineering the success of quantum          Quantum Information: 10th Anniversary Edition (Cambridge
     walk search using weighted graphs, Phys. Rev. A 94, 022304             University Press, Cambridge, UK, 2010).
     (2016).                                                           [49] K. Wang, G. C. Knee, X. Zhan, Z. Bian, J. Li, and
[32] J. A. Izaac and J. B. Wang, Systematic dimensionality reduction        P. Xue, Optimal experimental demonstration of error-
     for continuous-time quantum walks of interacting fermions,             tolerant quantum witnesses, Phys. Rev. A 95, 032122
     Phys. Rev. E 96, 032136 (2017).                                        (2017).
[33] R. Babbush, N. Wiebe, J. McClean, J. McClain, H. Neven, and       [50] A. Schreiber, A. Gábris, P. P. Rohde, K. Laiho, M. Štefaňák,
     G. K.-L. Chan, Low-Depth Quantum Simulation of Materials,              V. Potoček, C. Hamilton, I. Jex, and C. Silberhorn, A 2D quan-
     Phys. Rev. X 8, 011044 (2018).                                         tum walk simulation of two-particle dynamics, Science 336, 55
[34] L. Razzoli, M. G. A. Paris, and P. Bordone, Continuous-time            (2012).
     quantum walks on planar lattices and the role of the magnetic     [51] A. Crespi, R. Osellame, R. Ramponi, V. Giovannetti, R. Fazio,
     field, Phys. Rev. A 101, 032336 (2020).                                L. Sansoni, F. De Nicola, F. Sciarrino, and P. Mataloni,

                                                                 062448-6
EXPERIMENTAL INVESTIGATION OF EQUIVALENT …                                                PHYSICAL REVIEW A 105, 062448 (2022)

     Anderson localization of entangled photons in an integrated         Numbers in a Two-Dimensional Quantum Walk, Phys. Rev.
     quantum walk, Nat. Photonics 7, 322 (2013).                         Lett. 121, 100501 (2018).
[52] B. Wang, T. Chen, and X. Zhang, Experimental Observation       [53] Y. F. Peng, W. Wang, and X. X. Yi, Discrete-time quantum walk
     of Topologically Protected Bound States with Vanishing Chern        with time-correlated noise, Phys. Rev. A 103, 032205 (2021).




                                                              062448-7
