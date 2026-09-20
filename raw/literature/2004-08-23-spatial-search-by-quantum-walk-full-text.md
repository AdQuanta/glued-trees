# Spatial search by quantum walk - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.70.022314
> Collected: 2026-09-20
> Published: 2004-08-23
> Zotero parent key: 97WB8NVD
> Evidence: Zotero indexed PDF text

Spatial search by quantum walk
Andrew M. Childs* and Jeffrey Goldstone†
Center for Theoretical Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA (Received 16 June 2003; revised manuscript received 27 January 2004; published 23 August 2004)
Grover’s quantum search algorithm provides a way to speed up combinatorial search, but is not directly applicable to searching a physical database. Nevertheless, Aaronson and Ambainis showed that a database of N
items laid out in d spatial dimensions can be searched in time of order ŒN for d . 2, and in time of order
ŒN polyslog Nd for d = 2. We consider an alternative search algorithm based on a continuous-time quantum walk on a graph. The case of the complete graph gives the continuous-time search algorithm of Farhi and
Gutmann, and other previously known results can be used to show that ŒN speedup can also be achieved on the
hypercube. We show that full ŒN speedup can be achieved on a d-dimensional periodic lattice for d . 4. In
d = 4, the quantum walk search algorithm takes time of order ŒN polyslog Nd, and in d , 4, the algorithm does not provide substantial speedup.
DOI: 10.1103/PhysRevA.70.022314 PACS number(s): 03.67.Lx
I. INTRODUCTION
Grover’s quantum search algorithm [1] is one of the main applications of quantum computation. Given a black-box function fsxd : h1 , . . . , Nj → h0 , 1j satisfying
fsxd = H0, x fi w
1, x = w, s1d
Grover’s algorithm can find the value of w using of order ŒN queries, which is optimal [2]. On the other hand, no classical algorithm can do better than exhaustive search, which takes of order N queries. Therefore Grover’s algorithm can be used to speed up brute force combinatorial search. It can also be used as a subroutine in a variety of other quantum algorithms. Grover’s algorithm is sometimes described as a way to
search an unsorted database of N items in time OsŒNd. But the algorithm as originally proposed is not designed to search a physical database. Suppose we had N items stored in a d-dimensional physical space, and that these items could be explored in superposition by a quantum computer making local moves (a “quantum robot” [3]). Naively, it would seem that each step of the Grover algorithm should take time of order N1/d, since this is the time required to cross the data
base. Performing ŒN iterations, we find that the search takes time of order Ns1/2d+s1/dd, so no speedup is achieved in d = 2, and full speedup is achieved only in the limit of large d. However, it is possible to do better than this naive approach suggests. In [4], Aaronson and Ambainis present a model of query complexity on graphs. Within this model, they give a recursive algorithm for the search problem that
achieves full ŒN speedup for a d  ̆ 3 dimensional lattice, and
runs in time ŒN log2 N in d = 2. (It is obvious that no algorithm can get speedup in d = 1.)
In this paper we approach the spatial search problem using quantum walks. Since random walks are commonly used in classical algorithms, it is natural to consider a quantum analog of a classical random walk as an algorithmic tool. Here we consider the continuous-time quantum walk [5]. On certain graphs, this quantum-walk can yield exponentially faster hitting times than its classical counterpart [5,6]. Indeed, a recent result shows that the continuous-time quantum walk can solve a certain black-box problem exponentially faster than any classical algorithm [7]. Quantum walks provide a natural framework for the spatial search problem because the graph can be used to model the locality of the database. We present a simple quantumwalk search algorithm that can be applied to any graph. Our algorithm could be implemented within the model of [4], but is actually much simpler because it uses no auxiliary storage space. For the case of the complete graph, the resulting algorithm is simply the continuous-time search algorithm of Farhi and Gutmann [8]. On the hypercube, previous results can be used to show that the algorithm also provides quadratic speedup [9,10]. However, in both of these cases, the graph is highly connected. Here, we consider the case of a d-dimensional cubic periodic lattice, where d is fixed inde
pendent of N. We find full ŒN speedup in d . 4 and running
time OsŒN log3/2 Nd in d = 4. In d , 4, we find that quadratic speedup is impossible, so the continuous-time quantum-walk algorithm is never faster than the Aaronson-Ambainis algorithm. We note that it is also possible to construct a quantum analog of a discrete-time random walk [11,12] (although the walk cannot take place directly on the vertices of the graph [13]). This type of walk has been used to construct a fast search algorithm on the hypercube [14], and more recently, on a d-dimensional lattice with d  ̆ 2 [15]. The latter result outperforms our continuous-time walk algorithm for d = 2 , 3 , 4. However, similar performance can be achieved by a modification of the continuous-time algorithm [16]. This paper is organized as follows. In Sec. II we review the continuous-time quantum walk and show how it can be used to approach the search problem. In Sec. III we review
*Electronic address: amchilds@mit.edu †Electronic address: goldston@mit.edu
PHYSICAL REVIEW A 70, 022314 (2004)
1050-2947/2004/70(2)/022314(11)/$22.50 70 022314-1 ©2004 The American Physical Society


 the results in the high-dimensional cases (the complete graph and the hypercube), casting them in the language of continuous-time quantum walks. In Sec. IV we present the results for finite dimensional lattices, and in Sec. V, we conclude with a discussion of our results.
II. QUANTUM WALK
The continuous-time quantum walk on a graph is defined in direct analogy to a continuous-time classical random walk [5]. Given an undirected graph G with N vertices and no self-loops, we define the adjacency matrix
Ajk = H1, sj,kd P G
0, otherwise, s2d
which describes the connectivity of G. In terms of this matrix, we can also define the Laplacian L = A − D, where D is the diagonal matrix with Djj = degsjd, the degree of vertex j. The continuous-time random walk on G is a Markov process with a fixed probability per unit time g of jumping to an adjacent vertex. In other words, the probability of jumping to any connected vertex in a time e is ge (in the limit e→ 0). This walk can be described by the first-order, linear differential equation
dpjstd
dt = gok
Ljk pkstd, s3d
where pjstd is the probability of being at vertex j at time t. Since the columns of L sum to zero, probability is conserved. The continuous-time quantum walk on a graph takes place in an N-dimensional Hilbert space spanned by states ujl, where j is a vertex in G. In terms of these basis states, we can write a general state ucstdl in terms of the N complex amplitudes qjstd = kj ucstdl. If the Hamiltonian is H, then the dynamics of the system are determined by the Schrödinger
equation,1
i dqjstd
dt = ok
Hjk qkstd. s4d
Note the similarity between Eqs. (3) and (4). The continuous-time quantum walk is defined by simply letting
H = −gL.2 Then the only difference between Eqs. (3) and (4) is a factor of i, which nevertheless can result in radically different behavior. As an aside, we note that the Laplacian does not provide the only possible Hamiltonian for a quantum walk. Whereas Eq. (3) requires oj Ljk = 0 to be a valid probability
conserving classical Markov process, Eq. (4) requires H
= H† to be a valid unitary quantum process. Therefore we could also choose, for example, H = −gA. All of the graphs
we consider in this paper are regular [i.e., degsjd is independent of j], so these two choices give rise to the same quantum dynamics. However, for nonregular graphs the two choices will give different results. To approach the Grover problem with a quantum walk, we need to modify the Hamiltonian so that the vertex w is
special. Following [8], we introduce the oracle Hamiltonian3
Hw = − uwlkwu, s5d
which has energy zero for all states except uwl, which is the ground state, with energy −1. Solving the Grover problem is equivalent to finding the ground state of this Hamiltonian. In this paper we assume that this Hamiltonian is given, and we want to use it for as little time as possible to find the value of w. Note that this Hamiltonian could be simulated in the circuit model using the standard Grover oracle
Uwujl = s− 1ddjwujl. s6d
However, in this paper we focus on the continuous-time description. To construct an algorithm with the locality of a particular graph G, we consider the time-independent Hamiltonian
H = − gL + Hw = − gL − uwlkwu, s7d
where L is the Laplacian of G. We begin in a uniform superposition over all vertices of the graph,
usl = 1
ŒN oj
ujl, s8d
and run the quantum walk for time T. We then measure in the vertex basis. Our objective is to choose the parameter g so that the success probability ukw ucsTdlu2 is as close to 1 as possible for as small a T as possible. Note that the coefficient of Hw is held fixed at 1 to make the problem fair [e.g., so that evolution for time T could be simulated with OsTd queries of the standard Grover oracle (6)]. One might ask why we should expect this algorithm to give a substantial success probability for some values of g, T. We motivate this possibility in terms of the spectrum of H. Note that regardless of the graph, usl is the ground state of the Laplacian, with Lusl = 0. As g→ `, the contribution of Hw to H is negligible, so the ground state of H is close to usl. On the other hand, as g→ 0, the contribution of L to H disappears, so the ground state of H is close to uwl. Furthermore, since usl is nearly orthogonal to uwl, degenerate perturbation theory shows that the first excited state of H will be close to usl as g→ 0 for large N. We might expect that over some intermediate range of g, the ground state will switch from uwl to usl, and could have substantial overlap on both for a certain range of g. If the first excited state also has substantial overlap on both uwl and usl at such values of g, then the Hamiltonian will drive transitions between the two states, and thus will rotate the state from usl to a state with substantial overlap with uwl in a time of order 1 / sE1 − E0d, where E0
1We have chosen units in which " = 1.
2Here the sign is chosen so that the Hamiltonian is positive semidefinite. We have defined L = A − D so that for a lattice, L is a discrete approximation to the continuum operator π2. A free particle in the continuum has the positive semidefinite Hamiltonian H = −π2 (in appropriate units).
3More precisely, we should use Hw = −vuwlkwu where v is a fixed parameter with units of inverse time. However, we choose units in which v= 1. In these units, g is a dimensionless parameter.
A. M. CHILDS AND J. GOLDSTONE PHYSICAL REVIEW A 70, 022314 (2004)
022314-2


 is the ground state energy and E1 is the first excited state energy. Indeed, we will see that this is a good description of the algorithm if the dimension of the graph is sufficiently high. The simplest example is the complete graph (the “analog analogue” of the Grover algorithm [8]), which can be thought of roughly as having dimension proportional to N. A similar picture holds for the slog Nd-dimensional hypercube. When we consider a d-dimensional lattice with d independent of N, we will see that the state usl still switches from ground state to first excited state at some critical value of g. However, the uwl state does not have substantial overlap on the ground and first excited states unless d . 4, so the algorithm will not work for d , 4 (and d = 4 will be a marginal case).
III. HIGH DIMENSIONS
In this section, we describe the quantum-walk algorithm on “high-dimensional” graphs, namely the complete graph and the hypercube. These cases have been analyzed in previous works [8–10]. Here, we reinterpret them as quantumwalk algorithms, which provides motivation for the case of a lattice in d spatial dimensions.
A. Complete graph
Letting L be the Laplacian of the complete graph, we find exactly the continuous-time search algorithm proposed in [8]. Adding a multiple of the identity matrix to the Laplacian gives
L + NI = Nuslksu = 11  ̄ 1
AA
1  ̄ 1 2. s9d
Therefore we consider the Hamiltonian
H = − gNuslksu − uwlkwu. s10d
Since this Hamiltonian acts nontrivially only on a twodimensional subspace, it is straightforward to compute its spectrum exactly for any value of g. For gN ! 1, the ground state is close to uwl, and for gN @ 1, the ground state is close to usl. In fact, for large N, there is a sharp change in the ground state from uwl to usl as gN is varied from slightly less than 1 to slightly greater than 1. Correspondingly, the gap between the ground and first excited state energies is smallest for gN , 1, as shown in Fig. 1. At gN = 1, for N large, the
eigenstates are suwl ± usld / Œ2 (up to terms of order N−1/2),
with a gap of 2 / ŒN. Thus the walk rotates the state from usl
to uwl in time pŒN / 2.
B. Hypercube
Now consider the n-dimensional hypercube with N = 2n vertices. The vertices of the graph are labeled by n-bit strings, and two vertices are connected if and only if they differ in a single bit. Therefore the adjacency matrix can be written as
A = j=o1
n
ssxjd, s11d
where sx
sjd is the Pauli sigma x operator on the jth bit. In this case, we again find a sharp transition in the eigenstates at a certain critical value of g, as shown in Fig. 2. The Hamiltonian can be analyzed using essentially the same method we will apply in the next section, together with facts about spin operators. The energy gap is analyzed in Sec. 4.2 of [9], and the energy eigenstates are analyzed in Appendix B of [10]. The critical value of g is
g= 1
2n r= o1
n Sn
r D1
r=2
n + Osn−2d, s12d
at which the energy gap is
FIG. 1. Energy gap and overlaps for the complete graph with N = 1024.
FIG. 2. Energy gap and overlaps for the hypercube with N = 210= 1024.
SPATIAL SEARCH BY QUANTUM WALK PHYSICAL REVIEW A 70, 022314 (2004)
022314-3


 2
ŒN f1 + Osn−1dg s13d
and the ground and first excited states are suwl ± usld / Œ2 up to terms of order 1 / n. Again, we find that after a time of order
ŒN, the probability of finding w is of order 1.
IV. FINITE DIMENSIONS
Having seen that the algorithm works in two cases where the dimension of the graph grows with N, we now consider the case of a d-dimensional cubic periodic lattice, where d is fixed independent of N. The minimum gap and overlaps of usl , uwl with the ground and first excited states are shown in Fig. 3 for d = 2 , 3 , 4 , 5 and N < 1000. In all of these plots, there is a critical value of g where the energy gap is a minimum, and in the vicinity of this value, the state usl changes from being the first excited state to being the ground state. In large enough d, the uwl state changes from being the ground state to having large overlap on the first excited state in the
same region of g. However, for smaller d, the range of g over which the change occurs is wider, and the overlap of the uwl state on the lowest two eigenstates is smaller. Note that in all cases, usl is supported almost entirely on the subspace of the two lowest energy states. Therefore, if the algorithm starting in the state usl is to work at all, it must work essentially in a two-dimensional subspace. In the rest of this section, we will make this picture quantitative. We begin with some general techniques for analyzing the spectrum of H using knowledge of the spectrum of the graph. We then show the existence of a phase transition in g, and we show that for any d, the algorithm fails if g is not close to a certain critical value. Next we consider what happens when g is close to its critical value. In d . 4, we show that the algorithm gives a success probability of order
1 in time of order ŒN, and in d = 4, we find a success prob
ability of order 1 / log N in time of order ŒN log N. Finally, we investigate the critical point in d , 4 and show that the algorithm does not provide substantial speedup.
FIG. 3. Energy gap and overlaps for d-dimensional lattices with N < 1000. (a) d = 5, N = 45 = 1024; (b) d = 4, N = 64 = 1296; (c) d = 3, N = 103 = 1000; (d) d = 2, N = 322 = 1024.
A. M. CHILDS AND J. GOLDSTONE PHYSICAL REVIEW A 70, 022314 (2004)
022314-4


 A. Preliminaries
In this section, we show how the spectrum of H can be understood in terms of the spectrum of L. An eigenvector of H, denoted ucal, with eigenvalue Ea, satisfies
Hucal = s− gL − uwlkwuducal = Eaucal, s14d
i.e.,
s− gL − Eaducal = uwlkwucal. s15d
The state ucal is normalized, so ukca ucalu2 = 1. Define
Ra = ukwucalu2 s16d
and choose the phase of ucal so that
kwucal = ŒRa. s17d
We wish to calculate the amplitude for success,
kwue−iHtusl = oa
kwucalkcausle−iEat, s18d
so we only need those ucal with Ra . 0. L is the Laplacian of a lattice in d dimensions, periodic in each direction with period N1/d, with a total of N vertices. Each vertex of the lattice corresponds to a basis state uxl, where x is a d-component vector with components xj
P h0 , 1 , . . . , N1/d − 1j. The eigenvectors of −L are ufskdl with
kxufskdl = 1
ŒN eik·x, s19d
where
kj = 2pmj
N1/d , s20d
mj = 50, ± 1, ... , ± 1
2 sN1/d − 1d, N1/d odd
0, ± 1, ... , ± 1
2 sN1/d − 2d, + 1
2 N1/d, N1/d even,
s21d
and the corresponding eigenvalues are
Eskd = 2Sd − j=o1
d
cosskjdD. s22d
Since kfskd u wl fi 0, from Eq. (15) we have
fgEskd − Eagkfskducal fi 0 s23d
for any k. We can therefore rewrite Eq. (15), using Eq. (17), as
ucal = ŒRa
− gL − Ea
uwl. s24d
Consistency with Eq. (17) then gives the eigenvalue condition
K
wU 1
− gL − EaUwL = 1. s25d
Using Eq. (19), this can be expressed as
FsEad = 1, FsEd = 1
N ok
1
gEskd − E . s26d
A typical function FsEd is shown in Fig. 4. This function has poles where E =gEskd. For E figEskd, Eq. (26) shows that F8sEd . 0, so there is an eigenvalue of H between every adjacent pair of eigenvalues of −gL. Since FsEd → 0 as E → ± `, there is also one negative eigenvalue of H (corresponding to the ground state). Note that in the case shown in Fig. 4, the eigenvalues E = 2 , 4 , 6 of −gL have degeneracies 4 , 6 , 4 because of the symmetry of the lattice. It follows that there are 3 , 5 , 3 eigenvectors of H with eigenvalues Ea = 2 , 4 , 6, all with kw ucal = 0 and thus not relevant to our purpose. These 11 eigenvectors, together with the 5 relevant ones, make up the necessary total of 16. The normalization condition on ucal gives
RaKwU 1
s− gL − Ead2UwL = 1, s27d
i.e.,
Ra = 1
F8sEad . s28d
We also need the overlap of ucal with usl. Since kL u sl = 0, from (24) we have
ksucal = − ŒRa
Ea
ksuwl, s29d
so that
zksucalz2 = 1
N
1
Ea
2F8sEad . s30d
Using Eqs. (18), (24), and (25),
FIG. 4. The function FsEd for a d = 2 dimensional periodic lattice with N = 16 vertices, at g= 1.
SPATIAL SEARCH BY QUANTUM WALK PHYSICAL REVIEW A 70, 022314 (2004)
022314-5


 kwue−iHtusl = − 1
ŒN oa
e−iEat
EaF8sEad . s31d
At t = 0, this gives the sum rule
o
a
1
EaF8sEad = − 1. s32d
We will see that the spectrum of H depends significantly on the behavior of the sums
Sj,d = 1
N kofi0
1
fEskdgj . s33d
If d . 2j, then Sj,d can be approximated by an integral as4
Sj,d = Ij,d + os1d, s34d
where
Ij,d = 1
s2pdd E−p
p ddk
fEskdgj . s35d
The condition d . 2j is necessary for Ij,d to converge at k = 0. The numerical values of I1,d and I2,d for d  ̄ 10 are given in Table I. Note that Ij,d can also be calculated using the
formula [17]
Ij,d = 1
s2ddj E0
`
daaj−1e−a
sj − 1d! fI0sa/ddgd, s36d
where I0 is a modified Bessel function of the first kind. On the other hand, if d , 2j, then Sj,d can be well approximated by the contribution from values of k small enough that Eskd is approximately
Eskd < k2 = s2pmd2
N2/d s37d
(where we have used the notation k2 = k12 +  ̄ + kd
2). Then
Sj,d , cj,d Ns2j/dd−1, s38d
where
cj,d = 1
s2pd2j mofi0
1
sm2dj . s39d
Here the sum is over all values of the d-component vector of integers m other than m = 0, and converges for large m2. Numerically, we find
c2,2 = 0.00664, c2,3 = 0.0265. s40d
In the borderline case d = 2j, Ij,d diverges logarithmically
at k2 small and cj,d diverges logarithmically at m2 large. In this case
Sj,2j = 1
s4pdj j! ln N + Os1d. s41d
We will need
S1,2 = 1
4pln N + A + OsN−1d, s42d
S2,4 = 1
32p2 ln N + Os1d, s43d
where A = 0.0488 (the case j = 1, d = 2 is treated in greater detail in [19]).
B. Phase transition
In this section, we show that the overlap of the state usl on the ground or first excited state of H exhibits a phase transition at a critical value of gfor any dimension d. In fact, away from the critical value, usl is approximately an eigenstate of H, so Schrödinger evolution according to H does not change the state very much. In the next section, we will show that the algorithm indeed fails away from the critical value of g, and in the following sections we will consider what happens near the critical point. For g larger than the critical value (which will be determined below), the ground state energy is very close to 0. This can be seen as follows. The eigenvalue condition (26) for the ground state energy E0, which is negative, gives
1 = FsE0d = 1
NuE0u + 1
N kofi0
1
gEskd + uE0u s44d
,1
NuE0u + 1
N kofi0
1
gEskd s45d
<1
NuE0u + I1,d
g , s46d
where in the last line we have assumed d . 2. In this case, for g. I1,d (which will turn out to be the critical value), up to small terms,
4The little-o notation fsNd = o(gsNd) means limN→`fsNd / gsNd = 0. In contrast, the more familiar big O-notation fsNd = O(gsNd) means there exist constants c, N0 such that for all N  ̆ N0 , ufsNd u  ̄ c u gsNdu.
TABLE I. Numerical values of the convergent integrals. The result for I1,3 is given exactly in [18]; the rest were computed numerically.
d I1,d I2,d
3 0.253 4 0.155 5 0.116 0.0184 6 0.0931 0.0105 7 0.0781 0.00697 8 0.0674 0.00504 9 0.0593 0.00383 10 0.0530 0.00301
A. M. CHILDS AND J. GOLDSTONE PHYSICAL REVIEW A 70, 022314 (2004)
022314-6


 uE0u , 1
N
g
g− I1,d
. s47d
Using Eq. (30), we have
zksuc0lz2 = f1 + E02kofi0
sgEskd + uE0ud−2g−1 s48d
.F1 + E02
g2 kofi0
1
fEskdg2 G−1
s49d
.1 − E02
g2 kofi0
1
fEskdg2 . s50d
Inserting the behavior of S2,d from Eqs. (33), (38), and (41)
and using the bound (47), we find
1 − zksuc0lz2 , 1
sg− I1,dd2 3 5OsN−1d, d . 4
OsN−1log Nd, d = 4
OsN−2/3d, d = 3.
s51d
This shows that if g= I1,d +e for any e. 0, then 1 − zks uc0lz2 approaches zero as N → `. If d = 2, then I1,2 is logarithmically divergent, but using
Eq. (42) in Eq. (45) we can apply a similar argument whenever g. s1 / 4pdln N + A, in which case we have
uE0u , 1
N
g
g− s1/4pdln N − A s52d
and
1 − zksuc0lz2 , 1
fg− s1/4pdln N − Ag2 Os1d. s53d
This shows that if g. fs1 / 4pd +egln N, then 1 − zks uc0lz2
 ̄ 1 / se ln Nd2, which approaches zero as N → `. Similarly, for d . 2 and for g, I1,d, the first excited state uc1l, with energy E1 . 0, is essentially usl. Here we find
1 = FsE1d = − 1
NE1
+1
N kofi0
1
gEskd − E1
s54d
.− 1
NE1
+1
N kofi0
1
gEskd s55d
<− 1
NE1
+ I1,d
g , s56d
so that, up to small terms,
E1 , 1
N
g
I1,d − g. s57d
Again applying Eq. (30), we find
1 − zksuc1lz2 , 1
sI1,d − gd2 3 5OsN−1d, d . 4
OsN−1log Nd, d = 4
OsN−2/3d, d = 3.
s58d
We see that g= I1,d is the critical point. In d = 2 we can apply similar reasoning to obtain that for g, s1 / 4pdln N + A,
1 − zksuc1lz2 , 1
fs1/4pdln N − gg2 Os1d. s59d
In this case g= s1 / 4pdln N + A is the critical point.
C. Failure of the algorithm away from the critical point
In this section we will show that the algorithm fails away from the critical point, regardless of dimension. The results (51) and (58) are actually sufficient to show that away from the critical point in d . 4, the algorithm can be no better than classical search, but we will give a different argument for consistency of presentation. First we consider the regime where g is larger than the critical value. In the previous section, we saw that in this case, the ground state energy E0 is small. This is sufficient to imply that the success probability is small at all times. Combining Eqs. (31) and (32), we see that the amplitude at an arbitrary time must satisfy
zkwue−iHtuslz  ̄ 1
ŒNS 2
uE0uF8sE0d − 1D s60d
 ̄2
ŒNuE0uF8sE0d . s61d
Furthermore it is clear from the definition of FsEd that
F8sE0d  ̆ 1
NE02 , s62d
so
zkwue−iHtuslz  ̄ 2ŒNuE0u. s63d
Using Eq. (47), we find that for d . 2,
zkwue−iHtuslz  ̄ 2
ŒN
g
g− I1,d
. s64d
This shows that if g= I1,d +e for any e. 0, the success probability is never more than a constant factor larger than its initial value, no matter how long we run the algorithm. If d = 2, then I1,2 is logarithmically divergent, but using Eq. (52) we find
zkwue−iHtuslz  ̄ 2
ŒN
g
g− s1/4pdln N − A . s65d
This shows that the algorithm fails if g. fs1 / 4pd +egln N for any e. 0. Now we consider the case where g is smaller than the critical value. For d . 4 and E , 0, we have
SPATIAL SEARCH BY QUANTUM WALK PHYSICAL REVIEW A 70, 022314 (2004)
022314-7


 FsEd < 1
s2pdd E ddk
gEskd + uEu s66d
=1
s2pdd E ddk
gEskd − uEu
s2pdd E ddk
gEskdfgEskd + uEug s67d
. I1,d
g − uEu
g2s2pdd E ddk
fEskdg2 s68d
= I1,d
g − I2,d
g2 uEu. s69d
Using the fact that FsE0d = 1, this shows that
uE0u . gsI1,d − gd
I2,d
. s70d
From Eqs (16) and (28), it is clear that F8sEd . 1, so using Eq. (61) gives
zkwue−iHtuslz , 1
ŒN
2I2,d
gsI1,d − gd . s71d
A similar argument can be used for d = 3 , 4. With d = 4, we have
FsEd < 1
s2pd4 E d4k
gEskd + uEu s72d
=1
s2pd4 E d4k
gEskd − uEu
s2pd4 E d4k
gEskdfgEskd + uEug s73d
. I1,4
g − uEu
32gE0
2p k dk 4g
p2 k2 + uEu
s74d
= I1,4
g − p2uEu
256g2lnS1 + 16g
uEu D, s75d
where the third line follows because cos k  ̄ 1 − 2sk /pd2 for uku  ̄p, which implies Eskd  ̆ s4 /p2dk2. We have also used the fact that k2  ̄ dp2 to place an upper limit on the integral. This shows that for any e. 0 (with e ̄ 1), there exists a c . 0 such that
FsEd . I1,4
g − cuEu1−e
g2−e , s76d
so that
uE0u . c8gsI1,d − gd1/s1−ed s77d
for some c8 . 0, and therefore
zkwue−iHtuslz , 1
ŒN
2
c8gsI1,4 − gd1/s1+ed . s78d
With d = 3, we have
FsEd < 1
s2pd3 E d3k
gEskd + uEu s79d
=1
s2pd3 E d3k
gEskd − uEu
s2pd3 E d3k
gEskdfgEskd + uEug s80d
. I1,3
g − uEu
8gE0
` dk 4g
p2 k2 + uEu
s81d
= I1,3
g − p2
32g3/2 ŒuEu, s82d
where in the third line we have again used Eskd  ̆ s4 /p2dk2. In this case we find
uE0u . 1024
p4 gsI1,3 − gd2, s83d
which shows that
zksue−iHtuwlz , 1
ŒN
2p4
1024gsI1,3 − gd2 . s84d
Finally, with d = 2 we use a different argument. Here we have
F8sEd < 1
s2pd2 E d2k
fgEskd + uEug2 s85d
.1
2pE0
p k dk
sgk2 + uEud2 s86d
=p
4uEusuEu + p2gd , s87d
where the second line follows since cos k  ̆ 1 − 1
2 k2, which
implies Eskd  ̄ k2. In the second line we have also used the fact that the entire disk uku  ̄p is included in the region of integration. Equation (87) shows that
uEuF8sEd . p
4suEu + p2gd , s88d
so that
ukwue−iHtuslu , 1
ŒN
8suE0u + p2gd
p , s89d
which is Os1 / ŒNd for g= Os1d, and O[sln Nd / ŒN] for any g, s1 / 4pdln N + A. The arguments for the case where g is smaller than the critical value can be made tighter by a more refined analysis. For example, by considering the behavior of F8sEd, one can give a bound whose dependence on I1,d −g is linear for all d . 2, not just for d . 4. Furthermore, the careful reader will note that our bounds for d . 2 all become useless as g→ 0, but it is easy to see that the algorithm cannot be successful for small values of g.
A. M. CHILDS AND J. GOLDSTONE PHYSICAL REVIEW A 70, 022314 (2004)
022314-8


 Altogether, we see that the algorithm cannot work any better than classical search if g is not chosen close to its critical value. It remains to investigate what happens near the critical point.
D. The critical point in d Ð 4
In this section we investigate the region of the critical point in the cases where the algorithm provides speedup. First we consider the case d . 4. Separating out the k = 0 term in (26), we have
FsEd = − 1
NE + 1
N kofi0
1
gEskd − E . s90d
If uEu !gEskd for all k fi 0, then for large N, we can Taylor expand the second term to obtain
FsEd < − 1
NE + 1
gI1,d + E
g2 I2,d, s91d
which gives
F8sEd < 1
NE2 + I2,d
g2 . s92d
The critical point corresponds to the condition g= I1,d. At this
point, setting Eq. (91) equal to 1 gives two eigenvalues,
E0 < − I1,d
ŒI2,dN , E1 < + I1,d
ŒI2,dN , s93d
which correspond to the ground and first excited state, with a gap of order N−1/2. Since Eskd < s2pd2N−2/d for m2 = 1, we see that the assumption E0 , E1 !gEskd holds for all k fi 0. Furthermore, for the ground and first excited states at g= II,d, Eq.
(92) gives
F8sE0d < F8sE1d < 2I2,d
I1,d
2 . s94d
Now we want to use Eq. (31) to compute the time evolution of the algorithm. The contribution from all states above the first excited state is small, since as can be seen using Eq. (32) we have
−1
ŒN Eao.E1
1
EaF8sEad = 1
ŒNS1 + 1
E0F8sE0d + 1
E1F8sE1d D .
s95d
Using Eqs. (93) and (94), we see that the OsŒNd contributions from 1 / E0F8sE0d and 1 / E1F8sE1d cancel, so the right
hand side of Eq. (95) is os1d. Thus, using Eq. (31), we find
zkwue−iHtuslz < I1,d
ŒI2,dUsinS I1,d t
ŒI2,dNDU. s96d
The success probability is of order 1 at t = ŒI2,dN / I1,d. Straightforward analysis shows that a similar condition holds as long as g= I1,d ± OsN−1/2d, exactly the width of the region that cannot be excluded based on the arguments of Sec. IV C.
In d = 4, I2,d does not converge, so the result is modified
slightly. In this case Eq. (91) holds with I2,d replaced by
s1 / 32p2dln N, so the ground and first excited state energies are given by
E0 < − I1,4
Œs1/32p2dN ln N , E1 < + I1,4
Œs1/32p2dN ln N ,
s97d
and we find
F8sE0d < F8sE1d < ln N
16p2I12,4 . s98d
Therefore
zkwue−iHtuslz < I1,4
Œs1/32p2dln NUsinS I1,4 t
Œs1/32p2dN ln NDU,
s99d
which shows that running for a time of order ŒN log N gives a success probability of order 1 / log N. Using Oslog Nd repetitions to boost the success probability close to 1, we find a
total run time OsŒN log3/2 Nd.5 One can show that similar
conditions hold as long as g= I1,4 ± O[Œslog Nd / N].
For d , 4, the expansion (91) fails to find states whose energies satisfy E !gEskd. Indeed, we will see in the next section that the algorithm provides no substantial speedup in these cases.
E. The critical point in d , 4
To handle the case d , 4, we rearrange the eigenvalue condition to extract the Os1d contribution to FsEd:
FsEd = − 1
NE + 1
N kofi0
1
gEskd + 1
N kofi0
E
gEskdfgEskd − Eg .
s100d
In d = 3, we can replace the middle term by I1,3 /gfor large N. To explore the neighborhood of the critical point in d = 3, we introduce rescaled variables a , x via
g= I1,3 + a
N1/3 , s101d
E = 4p2I1,3
N2/3 x. s102d
Since the sum in the third term of Eq. (100) only gets significant contributions from small energies, we use Eq. (37) to give the approximation
5In fact, we could improve the run time of the algorithm to
OsŒN log Nd using amplitude amplification [20].
SPATIAL SEARCH BY QUANTUM WALK PHYSICAL REVIEW A 70, 022314 (2004)
022314-9


 gEskd < 4p2I1,3m2
N2/3 , s103d
and we can analyze the sum using the same techniques we applied to calculate Sj,d in the case d , 2j. Then we have, for large N,
FsEd < 1 + G3sxd − a
I1,3N1/3 , s104d
where
G3sxd = 1
4p2 Smofi0
x
m2sm2 − xd − 1
xD. s105d
Here the sum is over all integer values of m, as in Eq. (39),
and similarly converges for large m2. The eigenvalue condition in terms of x is G3sxd = a, which has one negative solution x0. Since G3sxd is independent of N, x0 is independent of
N, and the ground-state energy E0 is proportional to N−2/3. As we saw in Sec. IV C, a very small ground-state energy implies that the success probability is small at all times. Using Eq. (63), we find
zkwue−iHtuslz  ̄ 8p2I1,3ux0u
N1/6 . s106d
Therefore the success probability is small no matter how long we run the algorithm. This fact is sufficient to imply that the algorithm cannot produce full square root speedup. Taking the time derivative of Eq. (31), we see that
d
dtzkwue−iHtuslz  ̄ U d
dtkwue−iHtuslU  ̄ 1
ŒN , s107d
which implies that
t  ̆ zkwue−iHtuslzŒN. s108d
Thus the time required to find w using classical repetition of the evolution for time t is of order
t
zkwue−iHtuslz2  ̆ ŒN
zkwue−iHtuslz s109d
 ̆ N2/3
8p2I1,3ux0u s110d
regardless of t. In other words, the algorithm cannot produce full speedup. Similar considerations hold in the case d = 2. In this case, the critical point is at g= s1 / 4pdln N + A, so we choose
g= 1
4pln N + A + a, s111d
E = 2p ln N
N x. s112d
In this case, we find
FsEd < 1 + G2sxd − a
s1/4pdln N , s113d
where G2sxd is defined as in Eq. (105), but with m having two components instead of three. Again we find a solution x0 , 0 that is independent of N, and applying Eq. (63) gives
zkwue−iHtuslz  ̄ 4pux0uln N
ŒN . s114d
[Note that we could have reached a similar conclusion using Eq. (89).] Using Eq. (109), we find
t
zkwue−iHtuslz2  ̆ N
4pux0uln N , s115d
so the algorithm also fails near the critical point in d = 2.
V. DISCUSSION
In this paper we have presented a general approach to the Grover problem using a continuous-time quantum walk on a graph. We showed that quadratic speedup can be achieved if the graph is a lattice of sufficiently high dimension sd . 4d. Although we had originally hoped to find a fast algorithm in d = 2, we found that our approach does not offer substantial speedup in this case. Our algorithm begins in the state usl, which is delocalized over the entire graph. One might demand instead that we start at a particular vertex of the graph. However, it is clear that usl can be prepared from a localized state using OsN1/dd local operations. In fact, we could also prepare usl by running the quantum-walk search algorithm backward from a known localized state for the same amount of time it would take to find uwl starting from usl. The quantum-walk search algorithm is related to a search algorithm using quantum computation by adiabatic evolution. Adiabatic quantum computation is a way of solving minimization problems by keeping the quantum computer near the ground state of a time-varying Hamiltonian [9]. In the adiabatic version of the search algorithm, the quantum computer is prepared in the state usl (the ground state of H with g large), and g is slowly lowered from a large value to 0. If gis changed sufficiently slowly, then the adiabatic theorem ensures that the quantum computer ends up near the final ground state uwl, thus solving the problem. The time required to achieve a success probability of order 1 is inversely proportional to the square of the gap between the ground and first excited state energies. On the complete graph, the fact that the gap is only small (of order N−1/2) for
a narrow range of g (of order N−1/2) means that g can be
changed in such a way that time OsŒNd is sufficient to solve the problem [21,22]. Since the gap has similar behavior for the hypercube and for d-dimensional lattices with d . 4, quadratic speedup can also be achieved adiabatically in these
cases. In d = 4 the gap is of order 1 / ŒN log N for a range of
g of order Œslog Nd / N, so the run time is again
OsŒN log 3/2 Nd. In d , 4, no speedup can be achieved adiabatically. Yet another way to solve the Grover problem uses a sequence of measurements of H. For any adiabatic algorithm,
A. M. CHILDS AND J. GOLDSTONE PHYSICAL REVIEW A 70, 022314 (2004)
022314-10


 there is a related algorithm that uses only a sequence of measurements to remain in the ground state of a slowly
changing Hamiltonian [10]. The case of a hypercube was
presented in [10], and our present results show that this algorithm can also be used when the graph is a lattice with d . 4. However, to realize the measurement dynamically, the Hamiltonian H must be coupled to a pointer variable, which must be represented using auxiliary space. Although the quantum-walk algorithm does not perform as well as the Aaronson-Ambainis algorithm in d = 2 , 3 , 4, it does have certain advantages. The quantum-walk algorithm uses simple, time-independent dynamics rather than a recursive procedure. Furthermore, the quantum-walk algorithm uses only a single basis state for each vertex of the graph, whereas the algorithm of [4] needs substantial auxiliary space. The actual complexity of the search problem in d = 2 remains an open question. It would be interesting either to
improve on the algorithms of [15,16] or to prove a lower bound showing that full speedup cannot be achieved.
ACKNOWLEDGMENTS
We thank Scott Aaronson for discussing his results on quantum search of spatial regions and for encouraging us to pursue a quantum-walk approach. We also thank Edward Farhi and Sam Gutmann for numerous helpful discussions. A.M.C. received support from the Fannie and John Hertz Foundation. This work was also supported in part by the Cambridge–MIT Institute, by the U.S. Department of Energy under cooperative research agreement DE-FC0294ER40818, and by the National Security Agency and Advanced Research and Development Activity under Army Research Office Contract No. DAAD19-01-1-0656.
[1] L. K. Grover, Phys. Rev. Lett. 79, 325 (1997). [2] C. H. Bennett, E. Bernstein, G. Brassard, and U. Vazirani, SIAM J. Comput. 26, 1510 (1997); e-print quant-ph/9701001. [3] P. Benioff, in Quantum Computation and Information, edited by S. J. Lomonaco and H. E. Brandt (AMS, Providence, 2002); e-print quant-ph/0003006. [4] S. Aaronson and A. Ambainis, in Proceedings of the 44th IEEE Symposium on Foundations of Computer Science (IEEE, Los Alamitos, 2003), p. 200. [5] E. Farhi and S. Gutmann, Phys. Rev. A 58, 915 (1998). [6] A. M. Childs, E. Farhi, and S. Gutmann, Quantum Inf. Process. 1, 35 (2002); e-print quant-ph/0103020. [7] A. M. Childs, R. Cleve, E. Deotto, E. Farhi, S. Gutmann, and D. A. Spielman, in Proceedings of the 35th ACM Symposium on Theory of Computing (ACM, New York, 2003), p. 59. [8] E. Farhi and S. Gutmann, Phys. Rev. A 57, 2403 (1998). [9] E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser, e-print quant-ph/0001106. [10] A. M. Childs, E. Deotto, E. Farhi, J. Goldstone, S. Gutmann, and A. J. Landahl, Phys. Rev. A 66, 032314 (2002). [11] D. Aharonov, A. Ambainis, J. Kempe, and U. Vazirani, in Proceedings of the 33rd ACM Symposium on Theory of Com
puting, (ACM, New York, 2001), p. 50; e-print quant-ph/ 0012090. [12] A. Ambainis, E. Bach, A. Nayak, A. Vishwanath, and J. Watrous, in Proceedings of the 33rd ACM Symposium on Theory of Computing (Ref. [11]), p. 37.
[13] D. A. Meyer, Phys. Lett. A 223, 337 (1996); e-print quant-ph/ 9604011. [14] N. Shenvi, J. Kempe, and K. B. Whaley, Phys. Rev. A 67, 052307 (2003). [15] A. Ambainis, J. Kempe, and A. Rivosh, e-print quant-ph/ 0402107. [16] A. M. Childs and J. Goldstone, Phys. Rev. A (to be published). [17] E. W. Montroll, J. Soc. Ind. Appl. Math. 4, 241 (1956). [18] G. N. Watson, Q. J. Math. 10, 266 (1939). [19] E. W. Montroll, J. Math. Phys. 10, 753 (1969). [20] G. Brassard, P. Høyer, M. Mosca, and A. Tapp, in Quantum Computation and Information, edited by S. J. Lomonaco and H. E. Brandt (AMS, Providence, 2002); e-print quant-ph/ 0005055. [21] J. Roland and N. J. Cerf, Phys. Rev. A 65, 042308 (2002). [22] W. van Dam, M. Mosca, and U. Vazirani, in Proceedings of the 42nd Symposium on Foundations of Computer Science (IEEE, Los Alamitos, 2001), p. 279; e-print quant-ph/0206003.
SPATIAL SEARCH BY QUANTUM WALK PHYSICAL REVIEW A 70, 022314 (2004)
022314-11
