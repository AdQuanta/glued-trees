# An Example of the Difference Between Quantum and Classical Random Walks - Full Text

> Source: https://www.zotero.org/users/13148431/items/GUEJ9YVN
> Collected: 2026-09-20
> Published: Unknown
> Zotero parent key: GUEJ9YVN
> Evidence: Zotero indexed PDF text

An Example of the Difference Between Quantum and Classical Random Walks
Andrew M. Childs,1 Edward Farhi,1 and Sam Gutmann2
Received March 1, 2001; accepted May 16, 2002
In this note, we discuss a general definition of quantum random walks on graphs and illustrate with a simple graph the possibility of very different behavior between a classical random walkand its quantum analog. In this graph, propagation between a particular pair of nodes is exponentially faster in the quantum case.
KEY WORDS: quantum random walk; hitting times.
PACS: 03.67.Hk.
1. INTRODUCTION
Many classical algorithms are based on random walks, so it is natural to ask whether quantum random walks might be useful for quantum computation. Aframework for using quantum random walks to solve decision problems was investigated in Ref. 1. There also, an exponential separation was found between the classical and quantum times to propagate through a certain tree. In this note, we describe a general definition of continuous-time random walks on graphs and give a simpler example of a graph for which the quantum time to propagate between a particular pair of nodes is exponentially shorter than the analogous classical propagation time. We also discuss advantages of the continuous time formulation over discrete versions.
35
1570-0755/02/0400-0035/0 # 2002 Plenum Publishing Corporation
1 Center for Theoretical Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139. 2 Department of Mathematics, Northeastern University, Boston, Massachusetts 02115.
Quantum Information Processing, Vol. 1, Nos. 1/2, April 2002 (# 2002)


 2. RANDOM WALKS
Acontinuous time classical random walk on a graph is a Markov process. Agraph is a set of vertices f1; 2; . . . ; g and a set of edges that specifies which pairs of vertices are connected in the graph. Astep in a classical random walk on a graph only occurs between two vertices connected by an edge. Let denote the jumping rate. Starting at any vertex,the probability of jumping to any connected vertex in a time is (in the limit ! 0). This random walk can be described by the infinitesimal generator matrix M defined by
Mab 1⁄4
a 61⁄4 b; a and b connected by an edge
0 a 61⁄4 b; a and b not connected
k a 1⁄4 b; k is the valence of vertex a
8>><
>>:
ð1Þ
If paðtÞ denotes the probability of being at vertex a at time t, then
dpaðtÞ
dt 1⁄4
X
b
Mab pbðtÞ ð2Þ
Consider quantum evolution in a -dimensional Hilbert space according to a Hamiltonian H. In a basis j1i; j2i; . . . ; j i, the Schro ̈ dinger equation for j ðtÞi can be written
id
dt haj ðtÞi 1⁄4
X
b
hajHjbihbj ðtÞi ð3Þ
Note the similarity between (2) and (3). Whereas (2) conserves probability in the sense that
X
a
paðtÞ 1⁄4 1 ð4Þ
the Schr€odinger equation preserves probability as the sum of the amplitudes squared:
X
a
jhaj ðtÞij2 1⁄4 1 ð5Þ
In some sense, any evolution in a finite-dimensional Hilbert space can be thought of as a ‘‘quantum random walk.’’ However, the analogy is clearest when H has an obvious local structure. Aquantum random walk on a graph is naturally defined in a Hilbert space spanned by basis elements corresponding to the vertices. To respect
36 Childs, Farhi, and Gutmann


 the structure of the graph, we require that for a 61⁄4 b,
hajHjbi 61⁄4 0 iff a and b are connected by an edge ð6Þ
This is a very weak requirement, so we can impose more structure on H. A natural quantum analogue to the classical random walk described above is given by the quantum Hamiltonian with matrix elements(1)
hajHjbi 1⁄4 Mab ð7Þ
Note that on a one-dimensional lattice, this results in the Hamiltonian defined by
Hj ji 1⁄4 1
2 ðj j 1i 2j ji þ j j þ 1iÞ ð8Þ
which is just a discrete approximation to the operator d2=dx2 (where 1⁄4 1=2 is the lattice spacing). The difference between the quantum and classical evolution comes from the i which appears in (3) but not in (2). This can result in radically different behavior, as seen in Ref. 1. Asimpler example is given next.
3. AN EXAMPLE
Here we define a sequence of graphs Gn. The number of vertices in Gn is 2nþ1 þ 2n 2. In Fig. 1 we show G4. In general, Gn consists of two balanced binary trees of depth n with the 2n nth-level vertices of the two trees pairwise identified. For both the classical and quantum random walks, we start at the root of one tree and want the probability as a function of time of being at the other root. In other words, we are interested in how long it takes to propagate from the leftmost vertex to the rightmost vertex as a function of n. Consider the classical case first. The vertices of Gn can be grouped in columns indexed by j 2 f0; 1; . . . ; 2ng. Column 0 contains the root of the left tree, column 1 contains the two vertices connected to that root, etc. Note that column n contains the 2n vertices in the middle of the graph and column 2n is the root at the right. To analyze the classical walk from the left root to the right root, we need only keep track of the probabilities of being in the columns. In the left tree, for 0 < j < n, the probability of stepping from column j to column j þ 1 is twice as great as the probability of stepping from column j to column j 1. However, in the right tree, for n < j < 2n, the probability of stepping from column j to column j þ 1 is half as great as the probability of stepping from column j to column j 1. This means that if you start at the left root,
Example of the Difference Between Quantum and Classical Random Walks 37


 you quickly move to the middle of the graph, but then it takes a time exponential in n to reach your destination. More precisely, starting in column 0, the probability of being in column 2n after any number of steps is less than 2 n. This implies that the probability of reaching column 2n in a time that is polynomial in n must be exponentially small as a function of n. We now analyze the quantum walk on Gn starting in the state corresponding to the left root and evolving with the Hamiltonian given by (7). With this initial state, the symmetries of H keep the evolution in a ð2n þ 1Þdimensional subspace of the ð2nþ1 þ 2n 2Þ-dimensional Hilbert space. This subspace is spanned by states jcol ji (where 0 j 2n), the uniform superposition over all vertices in column j, that is,
jcol ji 1⁄4 1ffiffiNffiffijffi
pX
a2 column j
jai ð9Þ
where
Nj 1⁄4 2 j 0 j n
22n j n j 2n ð10Þ
Fig. 1. The graph G4.
38 Childs, Farhi, and Gutmann


 In this basis, the non-zero matrix elements of H are
hcol jjHjcol j 1i 1⁄4 ffi2ffiffi
p
ð11Þ
hcol jjHjcol ji 1⁄4
2 j 1⁄4 0; n; 2n
3 otherwise
(
ð12Þ
which is depicted in Fig. 2 (for n 1⁄4 4) as a quantum random walk on a line with 2n þ 1 vertices. Starting at the leftmost vertex of Fig. 2, there is an appreciable probability of being at the rightmost vertex after a time proportional to n. To see this, first consider quantum propagation on an infinite, translationally invariant line of vertices as depicted in Fig. 3. Here it is straightforward to compute the amplitude to go from vertex l to vertex m in a time t (for example, see Ref. 2):
hmje iHtjli 1⁄4 e i3 tim lJm lð2 ffi2ffiffi
p
tÞ ð13Þ
where Jm l is a Bessel function of order m l. This corresponds to propa
gation with speed 2pffi2ffiffi . More precisely, for any > 0 and jm lj 1, for
t < 1=ð2pffi2ffiffi Þ jm lj, the amplitude is exponentially small in jm lj,
whereas there are values of t between ð1=ð2pffi2ffiffi ÞÞjm lj and
ð1=ð2pffi2ffiffi Þ þ Þjm lj at which the amplitude is of order jm lj 1=2. In the limit of large n, the reduced version of Gn is nearly identical to the infinite, translationally invariant line, so it is plausible that propagation
on Gn will also occur with speed 2pffi2ffiffi . To verify this, we numerically compute the probability jhcol jj ðtÞij2 of being in column j at various times t, where j ð0Þi 1⁄4 jcol 0i and we choose 1⁄4 1. This is shown in Fig. 4 with n 1⁄4 500 for t 1⁄4 100, 250, and 400. These plots clearly show a wave packet
which propagates with speed 2pffi2ffiffi, with the amplitude near the wavefront decreasing like t 1=2. In the first plot, at t 1⁄4 100, the leading edge of the
Fig. 2. The reduction of G4 to a quantum random walk on a line. Vertices correspond to columns and are labeled with the diagonal matrix elements of H= , whereas edges are labeled with its matrix elements between adjacent columns.
Fig. 3. Quantum random walk on an infinite, translationally invariant line.
Example of the Difference Between Quantum and Classical Random Walks 39


 Fig. 4. Propagation in G500 starting at the left root. From top to bottom, the times are t 1⁄4 100; 250, and 400.
40 Childs, Farhi, and Gutmann


 distribution is at column 200pffi2ffiffi 283. The packet has not yet encountered the small defect at the center, so it has a relatively simple shape. At t 1⁄4 250, the wavefront has passed the center, and a small reflection can be seen propagating backward. However, the leading edge is relatively undisturbed,
having propagated to column 500pffi2ffiffi 707. The wavefront continues to
propagate with speed 2pffi2ffiffi until it reaches the right root, where the packet is reflected. The last plot, at t 1⁄4 400, shows the distribution shortly after this first reflection. Even after the reflection, there is still an appreciable probability of being at the right root.
4. THE LIMITING DISTRIBUTION
In this section, we consider the distribution over the vertices after a long time. We emphasize that although the mixing times (the characteristic times to reach the limiting distribution) may be similar in the classical and quantum cases,(3) this is in no way indicative of similar dynamics, as the limiting distributions may be radically different. In the classical case, the limiting distribution is defined as
b 1⁄4 Tli!m1 pbðTÞ ð14Þ
which is independent of the starting state. It is easy to see that the limiting distribution on Gn is uniform over the vertices: this distribution is the unique eigenvector of M with eigenvalue 0, so it is the only component that remains after a long time. Thus b 1⁄4 ð2nþ1 þ 2n 2Þ 1 for each vertex b, which is exponentially small. In the quantum case, unitarity prevents the walk from reaching a steady state. However, a sensible definition of the limiting distribution, which depends on the initial state jai, is given by(3)
b 1⁄4 Tli!m1
1 T
ðT
0
jhbje iHtjaij2 dt ð15Þ
This is the distribution resulting from a measurement done after a time chosen uniformly in 1⁄20; T , in the limit of large T. By expanding over the
Example of the Difference Between Quantum and Classical Random Walks 41


 energy eigenstates jEri, we find
b1⁄4
X
r;s
hbjErihErjaihajEsihEsjbi
Tli!m1
1 T
ðT
0
e iðEr EsÞt dt ð16Þ
1⁄4
X
r
jhajErij2 jhbjErij2 ð17Þ
(note that we have assumed Er 61⁄4 Es for r 61⁄4 s, which is true for Gn). In particular, consider the case where jai 1⁄4 jcol 0i corresponds to the left root and jbi 1⁄4 jcol 2ni corresponds to the right root. In this case, we may work in the reduced Hilbert space spanned by the columns, so the number of energy eigenstates is 2n þ 1. By symmetry, jh col 0jErij 1⁄4 jhcol 2njErij. The CauchySchwartz inequality gives
X
r
jhcol 0jErij4 X
s
1
X
r
jhcol 0jErij2
!2
1⁄4 1 ð18Þ
which implies
X
r
jhcol 0jErij4 1
2n þ 1 ð19Þ
Thus in the limiting distribution, the probability of being at the right root, starting at the left root, is
col 2n
1
2n þ 1 ð20Þ
which is much larger than in the classical case.
5. DISCUSSION
The model of quantum random walks used in this note applies automatically to any graph. In particular, the Hamiltonian is determined by the local structure of the graph and its definition does not require knowledge of any global properties. It is easy to imagine situations where the local structure of a graph is readily accessible, but determining some global property is difficult. For example, a computational problem may involve searching a graph for a node with a certain property whose presence or
42 Childs, Farhi, and Gutmann


 absence from the graph corresponds to the solution of an NP-complete problem.(1) The Hamiltonian-based approach to quantum random walks can be contrasted with discrete time models (for example, see Refs. 3–5) involving the extra state space of a ‘‘quantum coin.’’ This extra label seems to be necessary in discrete time formulations of quantum random walks (and is provably necessary for a lattice in any dimension(6)). However, for general graphs of mixed valence, it is not obvious how to define the discrete time unitary evolution operator without knowledge of global properties of the graph.
ACKNOWLEDGMENTS
This work was supported in part by the Department of Energy under cooperative agreement DE-FC02-94ER40818. A.M.C. is supported by the Fannie and John Hertz Foundation.
REFERENCES
1. E. Farhi and S. Gutmann, Phys. Rev. A 58, 915 (1998). 2. E. Farhi and S. Gutmann, Ann. Phys. 213, 182 (1992). 3. D. Aharonov, A. Ambainis, J. Kempe, and U. Vazirani, quant-ph/0012090. 4. Y. Aharonov, L. Davidovich, and N. Zagury, Phys. Rev. A 48, 1687 (1993). 5. A. Ambainis, E. Bach, A. Nayak, A. Vishwanath, and J. Watrous, in Proceedings of the 33rd Annual ACM Symposium on the Theory of Computing (ACM Press, New York, 2001), p. 37. 6. D. A. Meyer, Phys. Lett. A 223, 337 (1996).
Example of the Difference Between Quantum and Classical Random Walks 43
