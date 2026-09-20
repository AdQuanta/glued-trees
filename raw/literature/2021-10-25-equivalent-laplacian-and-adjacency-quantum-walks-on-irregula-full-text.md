# Equivalent Laplacian and adjacency quantum walks on irregular graphs - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.104.042221
> Collected: 2026-09-20
> Published: 2021-10-25
> Zotero parent key: I9NH4AWN
> Evidence: Zotero indexed PDF text

PHYSICAL REVIEW A 104, 042221 (2021)
Equivalent Laplacian and adjacency quantum walks on irregular graphs
Thomas G. Wong *
Department of Physics, Creighton University, 2500 California Plaza, Omaha, Nebraska 68178, USA
Joshua Lockhart†
Department of Computer Science, University College London, Gower Street, London WC1E 6BT, England, United Kingdom
(Received 12 July 2021; accepted 6 October 2021; published 25 October 2021)
The continuous-time quantum walk is a particle evolving by Schrödinger’s equation in discrete space. Encoding the space as a graph of vertices and edges, the Hamiltonian is proportional to the discrete Laplacian. In some physical systems, however, the Hamiltonian is proportional to the adjacency matrix instead. It is well known that these quantum walks are equivalent when the graph is regular, i.e., when each vertex has the same number of neighbors. If the graph is irregular, however, the quantum walks evolve differently. In this paper, we show that for some irregular graphs, if the particle is initially localized at a certain vertex, the probability distributions of the two quantum walks are identical, even though the amplitudes differ. We analytically prove this for a graph with five vertices and a graph with six vertices. By simulating the walks on all 1 018 689 568 simple, connected, irregular graphs with 11 vertices or less, we found 64 graphs with this notion of equivalence. We also give eight infinite families of graphs supporting these equivalent walks.
DOI: 10.1103/PhysRevA.104.042221
I. INTRODUCTION
A continuous-time quantum walk is simply the quantummechanical evolution of a particle in discrete space, where the space is encoded by a graph of vertices and edges. In general, the state of the particle |ψ〉 is a superposition over the vertices, and it evolves by Schrödinger’s equation
id
dt |ψ〉 = H|ψ〉,
where we have set h ̄ = 1. For a free particle, the Hamiltonian is the kinetic energy of the particle, so it is proportional to the negative of the discrete Laplacian:
H = −γ L,
where γ is the proportionality factor corresponding to the jumping rate (amplitude per time) of the walk and L = A − D is the discrete Laplacian. Here, A is the adjacency matrix of the graph (Ai j = 1 if vertices i and j are adjacent and Ai j = 0 otherwise), and D is the degree matrix of the graph, which is diagonal with Dii = deg(i) and zero on the off-diagonal. Note L is the discrete-space version of Laplace’s operator ∇2 = ∂2/∂x2 + ∂2/∂y2 + ∂2/∂z2. Setting γ = 1, the solution to Schrödinger’s equation is
|ψL (t )〉 = eiLt |ψ (0)〉. (1)
We will refer to this as a Laplacian quantum walk, and it was introduced by [1] to traverse decision trees. It has also been
*thomaswong@creighton.edu †joshualockhart@gmail.com
used for state transfer [2] and, with a suitable potential-energy term acting as a Hamiltonian oracle, for spatial searching [3]. In some physical systems, such as networks of interacting spins with XY interactions between nearest neighbors and single excitations, the Hamiltonian is instead proportional to the negative of the adjacency matrix A alone (without the degree matrix D) [4]. That is,
H = −γ A.
Then again with γ = 1, the solution to Schrödinger’s equation is
|ψA(t )〉 = eiAt |ψ (0)〉. (2)
We will refer to this as an adjacency quantum walk, and it yields an exponential speedup when traversing glued trees [5]. It is also the basis for quantum algorithms for solving boolean formulas [6], state transfer [7], and, with a suitable potentialenergy term acting as a Hamiltonian oracle, spatial searching [8]. It is well known that if the graph is regular, meaning each vertex has the same degree d, then the two quantum walks are equivalent because the states only differ by a global phase. As a proof, if the graph is regular, then D = dI, where I is the identity matrix, and, using (1),
|ψL (t )〉 = ei(A−dI)t |ψ (0)〉 = e−idt eiAt |ψ (0)〉
= e−idt |ψA(t )〉 = |ψA(t )〉.
In the third step, we used (2), and in the final step e−idt is an overall, global phase, which can be dropped because it does not affect the probability distribution of where the particle will be found when measured. In other words, there is no experiment that can distinguish a global phase. Thus, for
2469-9926/2021/104(4)/042221(13) 042221-1 ©2021 American Physical Society


 THOMAS G. WONG AND JOSHUA LOCKHART PHYSICAL REVIEW A 104, 042221 (2021)
FIG. 1. The simple, connected, irregular graph with N = 5 vertices where the Laplacian and adjacency quantum walks evolve with the same probability distribution when starting at a red vertex.
regular graphs, the Laplacian and adjacency quantum walks are exactly equivalent. In contrast, for an irregular graph, where vertices do not all have the same number of neighbors, the quantum walks generally evolve differently. For example, the Laplacian quantum walk only achieves perfect state transfer from one end of a path graph or chain to the other when the number of vertices is 2 [2,9], whereas the adjacency quantum walk achieves perfect state transfer when the number of vertices is 2 or 3 [10]. Or, for spatial search on complete bipartite graphs, different marked vertices are found depending on whether the Laplacian or adjacency matrix effect the quantum walk [11]. Despite the general difference between Laplacian and adjacency quantum walks on irregular graphs, in this paper, we present irregular graphs on which they are equivalent when the particle starts at a certain vertex. In the next section, we give a graph with five vertices that is the smallest simple, connected, irregular graph on which the Laplacian and adjacency quantum walks are equivalent, provided the walks start at a certain vertex. We analytically prove this equivalence by finding the amplitudes of the walks at time t, showing that some amplitudes differ by just a phase while others differ by both a phase and complex conjugation. We also prove this by comparing the mixing matrix [12] of each walk. In Sec. III, we present all 64 simple, connected, irregular graphs up to 11 vertices where the equivalence between the quantum walks holds out of a total of 1 018 689 568 simple, connected, irregular graphs. This indicates that the equivalence is rare. By observing patterns in these 64 graphs, we present in Sec. V eight infinite families of simple, connected, irregular graphs where the walks are equivalent when starting at a certain vertex, indicating that the equivalence is simultaneously abundant. This raises the question of whether all graphs with equivalent Laplacian and adjacency quantum walks can be found, so we conclude in Sec. VI with some open questions in this regard.
II. EXAMPLE WITH FIVE VERTICES
In Fig. 1, we present a graph with N = 5 vertices. Its adjacency matrix A and degree matrix D are
A=
⎛
⎜⎜⎜⎝
01100 10111 11011 01100 01100
⎞
⎟⎟⎟⎠, D =
⎛
⎜⎜⎜⎝
20000 04000 00400 00020 00002
⎞
⎟⎟⎟⎠,
FIG. 2. The simple, connected, irregular graph with N = 6 vertices where the Laplacian and adjacency quantum walks evolve with the same probability distribution when starting at a red vertex.
and so the graph Laplacian L = A − D is
L=
⎛
⎜⎜⎜⎝
−2 1 1 0 0 1 −4 1 1 1 1 1 −4 1 1 0 1 1 −2 0 0 1 1 0 −2
⎞
⎟⎟⎟⎠.
We claim that the Laplacian and adjacency quantum walks on this graph are equivalent when starting at one of the shaded red vertices in Fig. 1, i.e., at vertex 1, 4, or 5. We will first demonstrate this numerically, and then prove it analytically. First, note that in Fig. 1 vertices 2 and 3 are adjacent to each other, and vertices 1, 4, and 5 are each adjacent to both vertices 2 and 3. Thus, vertices 1, 4, and 5 have the same structure, so if the quantum walks are equivalent when starting at vertex 1 they are also equivalent when starting at vertex 4 or 5. Given this, let us take vertex 1 to be the initial state of the system, i.e.,
|ψ (0)〉 = (1 0 0 0 0)T. (3)
Using MATHEMATICA 12.0’s MatrixExp function, we can numerically find the state of the system for each walk at time t using (1) and (2). For example, at t = 7, we get
|ψL (7)〉 =
⎛
⎜⎜⎜⎜⎜⎝
0.1706660 − 0.6033140i 0.3807380 − 0.0856365i 0.3807380 − 0.0856365i 0.0339286 + 0.3872930i 0.0339286 + 0.3872930i
⎞
⎟⎟⎟⎟⎟⎠
,
|ψA(7)〉 =
⎛
⎜⎜⎜⎜⎜⎝
0.6209840 − 0.0865674i −0.136893 + 0.3654530i −0.136893 + 0.3654530i −0.379016 − 0.0865674i −0.379016 − 0.0865674i
⎞
⎟⎟⎟⎟⎟⎠
.
While the amplitudes of the two walks differ, if we take the norm square of each amplitude, the probability distribution of
FIG. 3. The simple, connected, irregular graph with N = 7 vertices where the Laplacian and adjacency quantum walks evolve with the same probability distribution when starting at a red vertex.
042221-2


 EQUIVALENT LAPLACIAN AND ADJACENCY QUANTUM ... PHYSICAL REVIEW A 104, 042221 (2021)
TABLE I. The number of simple, connected graphs up to 11 vertices, how many of them are regular and irregular, and how many of the irregular graphs have equivalent Laplacian and adjacency quantum walks when starting at a certain vertex.
Vertices Simple connected graphs Regular Irregular Irregular graphs with equivalent walks
1 1 10 0 2 1 10 0 3 2 11 0 4 6 24 0 5 21 2 19 1 6 112 5 107 1 7 853 4 849 1 8 11 117 17 11 100 4 9 261 080 22 261 058 6 10 11 716 571 167 11 716 404 23 11 1 006 700 565 539 1 006 700 026 28 Total 1 018 690 329 761 1 018 689 568 64
the two states at t = 7 is
pL (7) = pA(7) =
⎛
⎜⎜⎜⎜⎜⎝
0.393114 0.152295 0.152295 0.151147 0.151147
⎞
⎟⎟⎟⎟⎟⎠
. (4)
Thus, at t = 7, the probability distribution for the position of the particle is the same for both quantum walks, so the quantum walks are equivalent at this time. Using other small values of t, the probability distributions of the quantum walks are still equal. If we use a large value for time, however, a
FIG. 4. Connected, irregular graphs with N = 8 vertices where the Laplacian and adjacency quantum walks evolve with the same probability distribution when starting at a red vertex.
difference appears between the two probability distributions. For example, with t = 1012, MATHEMATICA 12.0 now yields
pL (1012 ) =
⎛
⎜⎜⎜⎝
0.447155 0.159125 0.159094 0.117237 0.117213
⎞
⎟⎟⎟⎠, (5)
pA(1012 ) =
⎛
⎜⎜⎜⎝
0.447352 0.159178 0.159178 0.117205 0.117180
⎞
⎟⎟⎟⎠. (6)
FIG. 5. Connected, irregular graphs with N = 9 vertices where the Laplacian and adjacency quantum walks evolve with the same probability distribution when starting at a red vertex.
042221-3


 THOMAS G. WONG AND JOSHUA LOCKHART PHYSICAL REVIEW A 104, 042221 (2021)
FIG. 6. Connected, irregular graphs with N = 10 vertices where the Laplacian and adjacency quantum walks evolve with the same probability distribution when starting at a red vertex. Continued on the next page.
Now, the probability distributions are slightly different. This raises the question of whether this discrepancy is due to numerical error, and the two quantum walks are actually equivalent, or if the disparity is genuine and the quantum walks are inequivalent. To resolve this, we next turn to an analytical proof showing that the quantum walks are, in fact, equivalent. Beginning with the Laplacian quantum walk, the (unnormalized) eigenvectors and eigenvalues of L are
ψL1 = (1 −3 0 1 1)T, λL1 = −5,
ψL2 = (0 −1 1 0 0)T, λL2 = −5,
FIG. 6. (Continued).
ψL3 = (−1 0 0 0 1)T, λL3 = −2,
ψL4 = (−1 0 0 1 0)T, λL4 = −2,
ψL5 = (1 1 1 1 1)T, λL5 = 0.
With the particle initially localized at vertex 1, we can express the initial state (3) as a linear combination of the eigenvectors of L:
|ψ (0)〉 = 2
15 ψL1 − 1
5 ψL2 − 1
3 ψL3 − 1
3 ψL4 + 1
5 ψL5.
Then, the state of the system at time t is obtained by multiplying each eigenvector ψLi with eiλLit :
|ψL (t )〉 = 2
15 eiλL1t ψL1 − 1
5 eiλL2t ψL2 − 1
3 eiλL3t ψL3
−1
3 eiλL4t ψL4 + 1
5 eiλL5t ψL5.
042221-4


 EQUIVALENT LAPLACIAN AND ADJACENCY QUANTUM ... PHYSICAL REVIEW A 104, 042221 (2021)
Plugging in for the eigenvectors and eigenvalues,
|ψL (t )〉 = 1
15
⎛
⎜⎜⎜⎜⎝
2e−5it + 10e−2it + 3 −3e−5it + 3 −3e−5it + 3
2e−5it − 5e−2it + 3
2e−5it − 5e−2it + 3
⎞
⎟⎟⎟⎟⎠.
Next, for the adjacency quantum walk, the (un-normalized) eigenvectors and eigenvalues of A are
ψA1 = (2 3 3 2 2)T, λA1 = 3,
ψA2 = (1 −1 −1 1 1)T, λA2 = −2,
ψA3 = (0 −1 1 0 0)T, λA3 = −1,
ψA4 = (−1 0 0 0 1)T, λA4 = 0,
ψA5 = (−1 0 0 1 0)T, λA5 = 0.
Again with the particle initially localized at vertex 1, the initial state (3) is
|ψ (0)〉 = 1
15 ψA1 + 1
5 ψA2 + 0ψA3 − 1
3 ψA4 − 1
3 ψA5
=1
15 ψA1 + 1
5 ψA2 − 1
3 ψA4 − 1
3 ψA5.
Evolving to time t,
|ψA(t )〉 = 1
15 eiλA1t ψA1 + 1
5 eiλA2t ψA2
−1
3 eiλA4t ψA4 − 1
3 eiλA5t ψA5
=1
15
⎛
⎜⎜⎜⎜⎝
2e3it + 3e−2it + 10
3e3it − 3e−2it
3e3it − 3e−2it
2e3it + 3e−2it − 5 2e3it + 3e−2it − 5
⎞
⎟⎟⎟⎟⎠
=1
15
⎛
⎜⎜⎜⎜⎝
e−2it (2e5it + 3 + 10e2it ) e3it (3 − 3e−5it ) e3it (3 − 3e−5it ) e−2it (2e5it + 3 − 5e2it ) e−2it (2e5it + 3 − 5e2it )
⎞
⎟⎟⎟⎟⎠
=1
15
⎛
⎜⎜⎜⎜⎝
e−2it (2e−5it + 10e−2it + 3)∗
e3it (−3e−5it + 3) e3it (−3e−5it + 3)
e−2it (2e−5it − 5e−2it + 3)∗
e−2it (2e−5it − 5e−2it + 3)∗
⎞
⎟⎟⎟⎟⎠.
We see that the second and third entries of |ψL(t )〉 and |ψA(t )〉 differ by an overall phase, and the first and last two entries differ by complex conjugation and an overall phase. Thus, if we take the norm square of each entry, we get the same probability distribution p(t ) for both quantum walks:
p(t ) = 1
225
⎛
⎜⎜⎜⎜⎜⎝
|2e−5it + 10e−2it + 3|2 |−3e−5it + 3|2 |−3e−5it + 3|2 |2e−5it − 5e−2it + 3|2
|2e−5it − 5e−2it + 3|2
⎞
⎟⎟⎟⎟⎟⎠
=1
225
⎛
⎜⎜⎜⎝
113 + 60 cos(2t ) + 40 cos(3t ) + 12 cos(5t ) 18 − 18 cos(5t ) 18 − 18 cos(5t ) 38 − 30 cos(2t ) − 20 cos(3t ) + 12 cos(5t ) 38 − 30 cos(2t ) − 20 cos(3t ) + 12 cos(5t )
⎞
⎟⎟⎟⎠.
This proves that the quantum walks are equivalent when they both start at vertex 1. For example, at t = 7, p(7) agrees with our previous numerical calculations of pL(7) and pA(7) in (4), and when t = 1012
p(1012 ) =
⎛
⎜⎜⎜⎝
0.447297 0.159143 0.159143 0.117209 0.117209
⎞
⎟⎟⎟⎠,
which differs from both of our earlier numerical calculations of pL (1012) in (5) and pA(1012) in (6), indicating that both of those calculations suffered from numerical error. Finally, since vertices 1, 4, and 5 have the same structure, this also proves that the quantum walks are equivalent when starting from vertex 4 or 5. Hence, vertices 1, 4, and 5 are all shaded red in Fig. 1. Another approach to proving the equivalence of the quantum walks is using the mixing matrix [12]. For the Laplacian walk, we can define the time-evolution operator
UL (t ) = eiLt .
Then using (1), the time evolution is
|ψL (t )〉 = UL (t )|ψ (0)〉.
Note the first column of UL(t ) is the state of the system at time t if the particle started localized at the first vertex, the second column of UL(t ) is the state of the system at time t if the particle started at the second vertex, and so forth. Then, if we multiply each entry of UL(t ) by its complex conjugate, we get a matrix of probabilities called the mixing matrix:
ML (t ) = UL (t ) ◦ U ∗
L (t ),
where ◦ denotes the elementwise product. Now, the first column of ML(t ) is the probability distribution of the particle at time t if it started localized at the first vertex, the second column of ML(t ) is the probability distribution of the particle at time t if it started localized at the second vertex, and so forth. In other words, (ML )ab is the probability of a particle initially at vertex b being measured at vertex a at time t. Finally, since, UL (t )∗ = UL (−t ), we can write the mixing matrix as
ML (t ) = UL (t ) ◦ UL (−t ).
For our example in Fig. 1, the mixing matrix of the Laplacian quantum walk is
ML (t ) = 1
225
⎛
⎜⎜⎜⎝
abbcc bd bbb bbd bb cbbac cbbca
⎞
⎟⎟⎟⎠,
where
a = 113 + 60 cos(2t ) + 40 cos(3t ) + 12 cos(5t ),
042221-5


 THOMAS G. WONG AND JOSHUA LOCKHART PHYSICAL REVIEW A 104, 042221 (2021)
FIG. 7. Continued from the previous page. Connected, irregular graphs with N = 11 vertices where the Laplacian and adjacency quantum walks evolve with the same probability distribution when starting at a red vertex. Continued on the next page.
b = 18 − 18 cos(5t ),
c = 38 − 30 cos(2t ) − 20 cos(3t ) + 12 cos(5t ),
d = 153 + 72 cos(5t ).
FIG. 7. (Continued).
Similarly, for the adjacency quantum walk, the time-evolution operator is
UA = eiAt ,
and its mixing matrix is
MA(t ) = UA(t ) ◦ UA(−t ).
042221-6


 EQUIVALENT LAPLACIAN AND ADJACENCY QUANTUM ... PHYSICAL REVIEW A 104, 042221 (2021)
It retains the same interpretation, where (MA)ab is the probability of a particle initially at vertex b being measured at vertex a, but with the adjacency quantum walk. Then, the Laplacian and adjacency quantum walks are equivalent when their mixing matrices have identical columns. For our example in Fig. 1,
MA(t ) = 1
225
⎛
⎜⎜⎜⎝
abbcc be f bb b f ebb c b bac c b bca
⎞
⎟⎟⎟⎠,
where a, b, and c are defined previously, and
e= 9
2 [19 + 10 cos(t ) + 15 cos(4t ) + 6 cos(5t )],
f=9
2 [19 − 10 cos(t ) − 15 cos(4t ) + 6 cos(5t )].
Since the first, fourth, and fifth columns of ML(t ) and MA(t ) are exactly the same, if the particle begins at vertex 1, 4, or 5, the two quantum walks have the same probability distributions at time t, and so they are equivalent. On the other hand, the second and third columns of ML(t ) and MA(t ) differ, so the quantum walks are not equivalent when the particle begins at vertex 2 or 3.
III. IRREGULAR GRAPHS UP TO 11 VERTICES
Given our analytical proof from the last section, we know it is possible for the Laplacian and adjacency quantum walks to evolve equivalently on an irregular graph. In this section, we numerically search for all such graphs up to 11 vertices. Note, throughout this paper, we only consider simple graphs, which are undirected, have unweighted edges, have at most one edge between each pair of vertices, and contain no self-loops. The graphs should also be connected, since if disconnected graphs are permitted one can trivially come up with additional graphs with equivalent quantum walks, such as taking the example in Fig. 1 and adding an isolated vertex, or taking two copies of the example in Fig. 1 and leaving them disconnected from each other. The adjacency matrices of all simple, connected graphs up to 11 vertices are available from [13]. Note the degree matrices and Laplacians can be determined from these data, since the diagonal elements of the degree matrix are given by summing the rows or columns of the adjacency matrix,
i.e., Dii = ∑
j Ai j = ∑
j A ji, and the graph Laplacian is then
L = A − D.
In Table I, we list how many simple, connected graphs of each size there are, along with how many of them are regular and irregular. In total, there are 1 018 690 329 simple, connected graphs up to 11 vertices, and 761 of them are regular, while 1 018 689 568 of them are irregular. This distinction is easy to detect, as a graph is regular if and only if the diagonal entries of the degree matrix are all the same value. Excluding these regular graphs on which the Laplacian and adjacency quantum walks are trivially equivalent (see our proof in the introduction), we can numerically simulate the Laplacian and adjacency quantum walks on each irregular graph, starting
from each vertex, using (1) and (2), at different values of t. Then, we can compute the norm square of each amplitude to see when the quantum walks have equivalent probability distributions. The last column of Table I shows how many irregular graphs of each size support equivalent quantum walks, and we found 64 graphs, which is just 6.28 × 10−6 percent of the 1 018 689 568 irregular graphs, suggesting that this equivalence is quite rare. Now, let us present all of them. The smallest irregular graph with equivalent quantum walks is Fig. 1 from the last section with N = 5 vertices. The next graph has N = 6 vertices, and it is shown in Fig. 2. In Appendix A, we analytically prove that the quantum walks are equivalent on this graph when starting at vertex 1 or 6, thus analytically proving that multiple graphs support equivalent quantum walks. The proof is very similar to our proof of Fig. 1 in the previous section, where we express the initial state in terms of the eigenvectors of the Laplacian and adjacency matrix and evolve by multiplying each eigenvector by the appropriate phase. The remaining graphs with N 7 are based on numerical simulations only. The quantum walks are equivalent on one irregular graph with N = 7 vertices, shown in Fig. 3. With N = 8 vertices, there are four irregular graphs, shown in Fig. 4, and with N = 9 vertices there are six irregular graphs, shown in Fig. 5. Next, there is a big jump in the number of irregular graphs with equivalent quantum walks. With N = 10 vertices, there are 23 of them, and they are shown in Fig. 6. Finally, with N = 11 vertices, there are 28 irregular graphs, shown in Fig. 7.
IV. FAMILIES OF GRAPHS
In this section, we identify patterns in the graphs from the previous section to determine eight families of graphs where the quantum walks are equivalent. For the first family, we point to five graphs from the previous section that follow a pattern. The first is Fig. 2, which consists of a complete graph of four vertices (K4) in the middle, and odd cycles of length 3 (C3’s) at the two ends. Next, growing a cycle, Fig. 4(a) has a C5 on one end and C3 on the other. Growing the cycle bigger still, Fig. 6(a) has C7 on one end and C3 on the other. Both cycles can grow as well. In Fig. 6(b), there are C5’s on each end. Finally, instead of growing the ends, we can grow the middle. In Fig. 6(c), there are two K4’s in the middle, and C3’s on each end. Generalizing this, we can have any number of K4’s in the middle, with any odd path at the two ends. A larger example is shown in Fig. 8, where there is a C9 on the left, three K4’s in the middle, and a C13 on the right. Since vertices 5, 6, 18, and 19 are double counted in both a cycle and a K4, there is a total of 30 vertices. Simulations show that graphs like this have equivalent Laplacian and adjacency quantum walks when starting at at either of the far ends of the graph. For the second family, we point to another five graphs from the previous section that follow a pattern. In Fig. 1, vertices 1, 2, and 3 can be identified as a cycle of three vertices C3. Then, vertices 4 and 5 stick out from vertices 2 and 3. Similarly, in Fig. 3, we now have a cycle of five vertices C5, with vertices 6 and 7 sticking out as before. Extending this further, in Fig. 5(a), the cycle has grown to C7, with vertices
042221-7


 THOMAS G. WONG AND JOSHUA LOCKHART PHYSICAL REVIEW A 104, 042221 (2021)
FIG. 8. An example of the first family of irregular graphs with equivalent quantum walks when starting at a red vertex. It consists of a C9 on the left, three K4’s in the middle, and a C15 on the right, for a total of 30 vertices.
8 and 9 sticking out. This is clearly a pattern, but we can go further. In Fig. 5(c), a complete graph of four vertices, K4, was inserted between the cycle C3 and the two “tail” vertices. In Fig. 7(c), the complete graph was inserted between C5 and the two tail vertices. We can insert any number of K4’s, as shown in Fig. 9. In this example of the family, the cycle has nine vertices, and there are two K4’s, and then the tail. Simulations show that graphs of this form have equivalent quantum walks when starting at the tip of the cyclic “head” or at either of the two tail vertices. Next, two graphs from the previous section follow a pattern that leads to the third family of graphs. In Fig. 4(b), two “tails” are joined together by two edges. In Fig. 6(e), the edges joining the tails now have an additional vertex in each of them. We can generalize this by adding any number of vertices to bridges between the tails, as long as they are the same length. An example is shown in Fig. 10. When the quantum walks start at any of the four tail vertices, they evolve with the same probability distributions, according to our simulations. For the fourth family, two graphs from the previous section follow a pattern. Figure 4(d) has eight vertices, five of which we arranged on the exterior (vertices 1, 2, 3, 4, and 5) and three of which we arranged in the interior (vertices 6, 7, and 8). Drawn this way, every exterior vertex is adjacent to every interior vertex, but the exterior vertices are not adjacent to each other. Furthermore, the interior vertices are adjacent to each other in a cycle C3. Enlarging this, Fig. 6(h) contains six exterior vertices and four interior vertices, and the four interior vertices form a cycle C4. This can be generalized to M exterior vertices and (M − 2) interior vertices, where M >= 5, with the interior vertices forming
FIG. 9. An example of the second family of irregular graphs with equivalent quantum walks when starting at a red vertex. It consists of a C9 on the left, two K4’s in the middle, and a tail on the right, for a total of 19 vertices.
FIG. 10. An example of the third family of irregular graphs with equivalent quantum walks when starting at a red vertex. It consists of two “tails,” connected through two paths of five vertices, for a total of 18 vertices.
CM−2. An example with 14 vertices is shown in Fig. 11, and our numerical simulations indicate that this family supports equivalent quantum walks when starting any of the exterior vertices. Six graphs from the previous section give rise to the fifth family of graphs with equivalent quantum walks. First, we can regard Fig. 1 as three C3’s that are joined together through two shared vertices. The first cycle consists of vertices 1, 2, and 3; the second consists of vertices 2, 3, and 4; and the last consists of vertices 2, 3, and 5, so they all share vertices 2 and 3. Next, Fig. 5(a) is one C7 and two C3’s, and they share vertices 4 and 5. Similarly, Fig. 5(b) is two C5’s and one C3, and they share vertices 3 and 4. In Fig. 7(a), there is one C9 and two C3’s, and they share vertices 5 and 6. In Fig. 7(b), there is one C3, one C5, and one C7, and they share vertices 4 and 5. Finally, in Fig. 7(z), there are three C5’s, and they share vertices 3 and 4. These reveal a family consisting of three odd cycles, each at least length 3, that all share two vertices. An example with C7, C9, and C11 is shown in Fig. 12, and our simulations show that the quantum walks are equivalent when starting at the vertex in any cycle that is furthest from the shared vertices. The sixth family arises from Figs. 1 and 6(o) by noting that the latter is two copies of the former, where each vertex from one copy is also adjacent to its corresponding vertex in the other copy. More formally, a graph G is doubled in this man
FIG. 11. An example of the fourth family of irregular graphs with equivalent quantum walks when starting at a red vertex. It consists of eight exterior vertices and six interior vertices, for a total of 14 vertices, with each exterior vertex adjacent to every interior vertex, and the interior vertices forming a cycle.
042221-8


 EQUIVALENT LAPLACIAN AND ADJACENCY QUANTUM ... PHYSICAL REVIEW A 104, 042221 (2021)
FIG. 12. An example of the fifth family of irregular graphs with equivalent quantum walks when starting at a red vertex. It consists of three cycles C7, C9, and C11, which share two vertices, for a total of 23 vertices.
ner by taking its Cartesian product with the complete graph of two vertices K2, and this is denoted G K2. More precisely, if we have two graphs with adjacency matrices A1 and A2 with respective dimensions n1 and n2, then the adjacency matrix of their Cartesian product is A1 ⊗ In2 + In1 ⊗ A2. Such doubled graphs, in the case where the original graph is a complete graph, were explored using quantum walks in the continuoustime setting in [14]. Here, our numerical simulations indicate that if a graph G supports equivalent Laplacian and adjacency quantum walks then so does G K2. An example is shown in Fig. 13. Since this new graph supports equivalent quantum walks, we can again double it, yielding G K2 K2, which also supports equivalent quantum walks. This can be repeated indefinitely, and it gives a family of graphs with equivalent quantum walks. Two graphs from the previous section motivate the seventh family. In Fig. 5(d), two C4’s are connected by a single edge. This bridge joining vertices 4 and 5 is then extended by vertex 9 into a C3. Next, in Fig. 7(w), we again have two C4’s joined by a single edge, and this edge is now extended into
FIG. 13. An example of the sixth family of irregular graphs with equivalent quantum walks when starting at a red vertex. It is the Cartesian product of Fig. 3 with K2, and it has 14 vertices.
FIG. 14. An example of the seventh family of irregular graphs with equivalent quantum walks when starting at a red vertex. It consists of two squares and a cycle of nine vertices, for a total of 15 vertices.
C5. This forms a family of graphs with equivalent quantum walks, where there are two C4’s joined by a single edge, which is extended into an odd cycle. For example, Fig. 14 shows two C4’s with the edge between them extended into C9. Our numerical simulations indicate that the quantum walks are equivalent when starting at the vertex in the odd cycle that is furthest from the C4’s. The eighth and final family stems from three graphs from the previous section. In Fig. 1, vertices 2 and 3 form a complete graph of two vertices K2. They are surrounded by three vertices (vertices 1, 4, and 5), which are each adjacent to both vertices 2 and 3. Next, in Fig. 4(d), vertices 6, 7, and 8 form K3. They are surrounded by five vertices (vertices 1, 2, 3, 4, and 5), which are adjacent to all three vertices 6, 7, and 8. Finally, in Fig. 7(aa), vertices 8, 9, 10, and 11 form K4, and they are surrounded by seven vertices (vertices 1 through 7), which are adjacent to all four vertices 8 through 11. This forms a family of graphs with Ki at the center, where i = 2, 3, . . . , surrounded by 2i − 1 vertices, each adjacent to the vertices in the central complete graph. An example is shown in Fig. 15. Our numerical simulations indicate that the quantum walks on this family are equivalent when starting at an exterior vertex. The existence of any one of these eight families means there is an infinite number of graphs on which the Laplacian and adjacency quantum walks yield the same probability distribution. This reveals that the number of irregular graphs that support equivalent quantum walks is plentiful, even though they are rare compared to the total number of irregular graphs.
V. CONCLUSION
In this paper, we have shown that the Laplacian and adjacency quantum walks can yield equivalent evolutions on irregular graphs, in the sense that they have the same probability distribution over the vertices. This requires that the
042221-9


 THOMAS G. WONG AND JOSHUA LOCKHART PHYSICAL REVIEW A 104, 042221 (2021)
FIG. 15. An example of the eighth family of irregular graphs with equivalent quantum walks when starting at a red vertex. It consists of K5 in the interior with nine vertices on the exterior that are adjacent to every vertex of the complete graph, for a total of 14 vertices.
walker starts at a certain vertex. We analytically proved this for the two smallest examples, which contain five and six vertices, and we numerically explored all 1 018 689 568 simple, connected, irregular graphs and found 64 that support equivalent quantum walks. Despite this rarity, we numerically
found eight infinite families of graphs supporting equivalent quantum walks. This paper raises several questions for further research. One is to find all families of graphs that support equivalent quantum walks. Related is to prove whether or not there exist graphs that support equivalent quantum walks outside of these families. From Table I, as the number of vertices increases, the number of irregular graphs supporting equivalent walks seems to be increasing. Another research question is whether this always increases and, more specifically, whether there is a way to find the number of graphs given N. Our results assumed the walker was initially localized at a single vertex, and further research could generalize this. Our preliminary numerical simulations where the initial state is a uniform superposition over two vertices suggest that the graphs with equivalent quantum walks may differ. Finally, throughout this paper, we assumed that the jumping rate γ = 1. The Laplacian and adjacency matrix can, however, have different spectral norms, meaning when γ = 1 the Hamiltonian H = −γ L or −γ A can have different norms. Then, the walks could be taking place at different rates, with one using more energy than the other. Scaling the quantum walks to account for this is further research.
ACKNOWLEDGMENT
J.L. thanks V. Kendon for helpful discussions.
APPENDIX: PROOF OF EXAMPLE WITH SIX VERTICES
In this Appendix, we prove that the graph with six vertices in Fig. 2 has equivalent quantum walks when the particle begins at vertex 1 or 6. Its adjacency matrix and degree matrix are
A=
⎛
⎜⎜⎜⎜⎜⎝
011000 101110 110110 011011 011101 000110
⎞
⎟⎟⎟⎟⎟⎠
, D=
⎛
⎜⎜⎜⎜⎜⎝
200000 040000 004000 000400 000040 000002
⎞
⎟⎟⎟⎟⎟⎠
.
Subtracting these, the Laplacian is
L=
⎛
⎜⎜⎜⎜⎜⎝
−2 1 1 0 0 0 1 −4 1 1 1 0 1 1 −4 1 1 0 0 1 1 −4 1 1 0 1 1 1 −4 1 0 0 0 1 1 −2
⎞
⎟⎟⎟⎟⎟⎠
.
Let us calculate the state of the Laplacian quantum walk. The (un-normalized) eigenvectors and eigenvalues of L are
ψL1 = (3 + √17 2 2 −2 −2 −3 − √17)T, λL1 = (−7 − √17)/2,
ψL2 = (0 0 0 −1 1 0)T, λL2 = −5,
ψL3 = (0 −1 1 0 0 0)T, λL3 = −5,
ψL4 = (2 −1 −1 −1 −1 2)T, λL4 = −3,
ψL5 = (3 − √17 2 2 −2 −2 −3 + √17)T, λL5 = (−7 + √17)/2,
ψL6 = (1 1 1 1 1 1)T, λL6 = 0.
042221-10


 EQUIVALENT LAPLACIAN AND ADJACENCY QUANTUM ... PHYSICAL REVIEW A 104, 042221 (2021)
Note that, due to the symmetry of the graph, vertices 1 and 6 have the same structure. So, if we prove the equivalence of the quantum walks starting at vertex 1, we have also proved it starting at vertex 6. So, we take the initial state to be vertex 1, i.e.,
|ψ (0)〉 = (1 0 0 0 0 0)T. Expressing this in terms of the eigenvectors of L,
|ψ (0)〉 = −1
4√17 ψL1 + 0ψL2 + 0ψL3 + 1
6 ψL4 + 1
4√17 ψL5 + 1
6 ψL6
= −1
4√17 ψL1 + 1
6 ψL4 + 1
4√17 ψL5 + 1
6 ψL6.
Then, the state of the system at time t is obtained by multiplying each eigenvector ψLi with eiλLit :
|ψL (t )〉 = −1
4√17 eiλL1t ψL1 + 1
6 eiλL4t ψL4 + 1
4√17 eiλL5t ψL5 + 1
6 eiλL6t ψL6.
Plugging in for the eigenvectors and eigenvalues, the state of the Laplacian quantum walk at time t is
|ψL (t )〉 = 1
204
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
3(17 − 3√17)ei(−7−√17)t/2 + 68e−3it + 3(17 + 3√17)ei(−7+√17)t/2 + 34
−6√17ei(−7−√17)t/2 − 34e−3it + 6√17ei(−7+√17)t/2 + 34
−6√17ei(−7−√17)t/2 − 34e−3it + 6√17ei(−7+√17)t/2 + 34
6√17ei(−7−√17)t/2 − 34e−3it − 6√17ei(−7+√17)t/2 + 34
6√17ei(−7−√17)t/2 − 34e−3it − 6√17ei(−7+√17)t/2 + 34
3(−17 + 3√17)ei(−7−√17)t/2 + 68e−3it − 3(17 + 3√17)ei(−7+√17)t/2 + 34
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
.
Next, let us consider the adjacency quantum walk. The (un-normalized) eigenvectors and eigenvalues of A are
ψA1 = (301 + 73√17 536 + 130√17 536 + 130√17 536 + 130√17 536 + 130√17 301 + 73√17)T,
λA1 = (3 + √17)/2,
ψA2 = (−1 1 1 −1 −1 1)T, λA2 = −2,
ψA3 = (0 0 0 −1 1 0)T, λA3 = −1,
ψA4 = (0 −1 1 0 0 0)T, λA4 = −1,
ψA5 = (−2 −1 −1 1 1 2)T, λA5 = 1,
ψA6 = (301 − 73√17 536 − 130√17 536 − 130√17 536 − 130√17 536 − 130√17 301 − 73√17)T,
λA1 = (3 − √17)/2.
Writing the initial state of the quantum walk, which is initially localized at vertex 1, as a linear combination of the eigenvectors of A, we get
|ψ (0)〉 = 1105 − 268√17
68 ψA1 − 1
6 ψA2 + 0ψA3 + 0ψA4 − 1
6 ψA5 + 1105 + 268√17
68 ψA6
= 1105 − 268√17
68 ψA1 − 1
6 ψA2 − 1
6 ψA5 + 1105 + 268√17
68 ψA6.
Multiplying each eigenvector ψAi with eiλAit , the state of the system at time t
|ψA(t )〉 = 1105 − 268√17
68 eiλA1t ψA1 − 1
6 eiλA2t ψA2 + 1105 + 268√17
68 eiλA6t 1
2√17 ψA6.
Plugging in for the eigenvectors and eigenvalues,
|ψA(t )〉 = 1
204
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
3(17 − 3√17)ei(3+√17)t/2 + 34e−2it + 68eit + 3(17 + 3√17)ei(3−√17)t/2
6√17ei(3+√17)t/2 − 34e−2it + 34eit − 6√17ei(3−√17)t/2
6√17ei(3+√17)t/2 − 34e−2it + 34eit − 6√17ei(3−√17)t/2
6√17ei(3+√17)t/2 + 34e−2it − 34eit − 6√17ei(3−√17)t/2
6√17ei(3+√17)t/2 + 34e−2it − 34eit − 6√17ei(3−√17)t/2
3(17 − 3√17)ei(3+√17)t/2 − 34e−2it − 68eit + 3(17 + 3√17)ei(3−√17)t/2
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
042221-11


 THOMAS G. WONG AND JOSHUA LOCKHART PHYSICAL REVIEW A 104, 042221 (2021)
=1
204
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
e−2it [3(17 − 3√17)ei(7+√17)t/2 + 34 + 68e3it + 3(17 + 3√17)ei(7−√17)t/2]
e−2it e−iπ [−6√17ei(7+√17)t/2 + 34 − 34e3it + 6√17ei(7−√17)t/2]
e−2it e−iπ [−6√17ei(7+√17)t/2 + 34 − 34e3it + 6√17ei(7−√17)t/2]
e−2it [6√17ei(7+√17)t/2 + 34 − 34e3it − 6√17ei(7−√17)t/2]
e−2it [6√17ei(7+√17)t/2 + 34 − 34e3it − 6√17ei(7−√17)t/2]
e−2it e−iπ [−3(17 − 3√17)ei(7+√17)t/2 + 34 + 68e3it − 3(17 + 3√17)ei(7−√17)t/2]
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
=1
204
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
e−2it [3(17 − 3√17)ei(−7−√17)t/2 + 68e−3it + 3(17 + 3√17)ei(−7+√17)t/2 + 34]∗
e−i(2t+π )[−6√17ei(−7−√17)t/2 − 34e−3it + 6√17ei(−7+√17)t/2 + 34]∗
e−i(2t+π )[−6√17ei(−7−√17)t/2 − 34e−3it + 6√17ei(−7+√17)t/2 + 34]∗
e−2it [6√17ei(−7−√17)t/2 − 34e−3it − 6√17ei(−7+√17)t/2 + 34]∗
e−2it [6√17ei(−7−√17)t/2 − 34e−3it − 6√17ei(−7+√17)t/2 + 34]∗
e−i(2t+π )[−3(17 − 3√17)ei(−7−√17)t/2 + 68e−3it − 3(17 + 3√17)ei(−7+√17)t/2 + 34]∗
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
.
Each of the terms of |ψL(t )〉 and |ψA(t )〉 differs by an overall phase and complex conjugation, so if we take the norm square of each entry we get the same probability distribution for both quantum walks:
p(t ) = 1
41 616
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
|3(17 − 3√17)ei(−7−√17)t/2 + 68e−3it + 3(17 + 3√17)ei(−7+√17)t/2 + 34|2
| − 6√17ei(−7−√17)t/2 − 34e−3it + 6√17ei(−7+√17)t/2 + 34|2
| − 6√17ei(−7−√17)t/2 − 34e−3it + 6√17ei(−7+√17)t/2 + 34|2
|6√17ei(−7−√17)t/2 − 34e−3it − 6√17ei(−7+√17)t/2 + 34|2
|6√17ei(−7−√17)t/2 − 34e−3it − 6√17ei(−7+√17)t/2 + 34|2
|3(−17 + 3√17)ei(−7−√17)t/2 + 68e−3it − 3(17 + 3√17)ei(−7+√17)t/2 + 34|2
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
=
⎛
⎜⎜⎜⎜⎜⎜⎜⎝
p1(t ) p2(t ) p3(t ) p4(t ) p5(t ) p6(t )
⎞
⎟⎟⎟⎟⎟⎟⎟⎠
,
where
p1(t ) = 1
41 616
[
13 736 + 4624 cos(3t ) + 2448 cos(√17t )
+ 408(17 − 3√17) cos
( 1 + √17
2t
)
+ 408(17 + 3√17) cos
( 1 − √17
2t
)
+ 204(17 − 3√17) cos
( 7 + √17
2t
)
+ 204(17 + 3√17) cos
( 7 − √17
2t
)]
,
p2(t ) = p3(t ) = 1
41 616
[
3536 − 2312 cos(3t ) − 1224 cos(√17t )
+ 408√17 cos
( 1 + √17
2t
)
− 408√17 cos
( 1 − √17
2t
)
− 408√17 cos
( 7 + √17
2t
)
+ 408√17 cos
( 7 − √17
2t
)]
,
p4(t ) = p5(t ) = 1
41 616
[
3536 − 2312 cos(3t ) − 1224 cos(√17t )
− 408√17 cos
( 1 + √17
2t
)
+ 408√17 cos
( 1 − √17
2t
)
+ 408√17 cos
( 7 + √17
2t
)
− 408√17 cos
( 7 − √17
2t
)]
,
042221-12


 EQUIVALENT LAPLACIAN AND ADJACENCY QUANTUM ... PHYSICAL REVIEW A 104, 042221 (2021)
p6(t ) = 1
41 616
[
13 736 + 4624 cos(3t ) + 2448 cos(√17t )
− 408(17 − 3√17) cos
( 1 + √17
2t
)
− 408(17 + 3√17) cos
( 1 − √17
2t
)
− 204(17 − 3√17) cos
( 7 + √17
2t
)
− 204(17 + 3√17) cos
( 7 − √17
2t
)]
.
Note p1(t ) and p6(t ) are the same, except the last two lines have opposite signs. Similarly p2,3(t ) and p4,5(t ) are the same, except the last two lines have opposite signs. This proves that the quantum walks in Fig. 2 are equivalent when starting at vertex 1 or, by symmetry, vertex 6.
[1] E. Farhi and S. Gutmann, Quantum computation and decision trees, Phys. Rev. A 58, 915 (1998). [2] R. Alvir, S. Dever, B. Lovitz, J. Myer, C. Tamon, Y. Xu, and H. Zhan, Perfect state transfer in Laplacian quantum walk, Journal of Algebraic Combinatorics 43, 801 (2016). [3] A. M. Childs and J. Goldstone, Spatial search by quantum walk, Phys. Rev. A 70, 022314 (2004). [4] S. Bose, A. Casaccino, S. Mancini, and S. Severini, Communication in XYZ all-to-all quantum networks with a missing link, Int. J. Quantum Inform. 07, 713 (2009). [5] A. M. Childs, R. Cleve, E. Deotto, E. Farhi, S. Gutmann, and D. A. Spielman, Exponential algorithmic speedup by a quantum walk, in Proceedings of the 35th Annual ACM Symposium on Theory of Computing, STOC ’03 (ACM, New York, 2003), pp. 59–68. [6] E. Farhi, J. Goldstone, and S. Gutmann, A quantum algorithm for the Hamiltonian NAND tree, Theory Comput. 4, 169 (2008). [7] C. Godsil, State transfer on graphs, Discrete Math. 312, 129 (2012).
[8] L. Novo, S. Chakraborty, M. Mohseni, H. Neven, and Y. Omar, Systematic dimensionality reduction for quantum walks: Optimal spatial search and transport on non-regular graphs, Sci. Rep. 5, 13304 (2015). [9] C. Godsil, Graph spectra and quantum walks, 2015 (unpublished). [10] M. Christandl, N. Datta, A. Ekert, and A. J. Landahl, Perfect State Transfer in Quantum Spin Networks, Phys. Rev. Lett. 92, 187902 (2004). [11] T. G. Wong, L. Tarrataca, and N. Nahimov, Laplacian versus adjacency matrix in quantum walk search, Quantum Inf. Process. 15, 4029 (2016). [12] G. Coutinho, C. Godsil, K. Guo, and H. Zhan, A new perspective on the average mixing matrix, The Electronic Journal of Combinatorics 25, 1 (2018). [13] B. D. McKay, Graphs, http://users.cecs.anu.edu.au/∼bdm/data/ graphs.html (accessed 30 Nov. 2020). [14] T. G. Wong and P. Philipp, Engineering the success of quantum walk search using weighted graphs, Phys. Rev. A 94, 022304 (2016).
042221-13
