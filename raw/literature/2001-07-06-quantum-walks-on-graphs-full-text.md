# Quantum walks on graphs - Full Text

> Source: https://dl.acm.org/doi/10.1145/380752.380758
> Collected: 2026-09-20
> Published: 2001-07-06
> Zotero parent key: Q6AXAXZQ
> Evidence: Zotero indexed PDF text

Quantum Walks on Graphs
Dorit Aharonov Andris Ambainisy Julia Kempez Umesh Vazirani x
ABSTRACT
We set the ground for a theory of quantum walks on graphsthe generalization of random walks on nite graphs to the quantum world. Such quantum walks do not converge to any stationary distribution, as they are unitary and reversible. However, by suitably relaxing the de nition, we can obtain a measure of how fast the quantum walk spreads or how con ned the quantum walk stays in a small neighborhood. We give de nitions of mixing time, lling time, dispersion time. We show that in all these measures, the quantum walk on the cycle is almost quadratically faster then its classical correspondent. On the other hand, we give a lower bound on the possible speed up by quantum walks for general graphs, showing that quantum walks can be at most polynomially faster than their classical counterparts.
1. INTRODUCTION
Markov chains or random walks on graphs have proved to be a fundamental tool, with broad applications in various elds of mathematics, computer science and the natural sciences, such as mathematical modeling of physical systems, simulated annealing, and the Markov Chain Monte Carlo method. In the physical sciences they provide a fundamental model for the emergence of global properties from local interactions. In the algorithmic context, they provide a general paradigm for sampling and exploring an exponentially large set of combinatorial structures (such as matchings in a graph), by using a sequence of simple, local transitions.
E-mail: doria@cs.berkeley.edu, Computer Science Division,
U.C. Berkeley, Berkeley, California, USA, supported by U.C.
President's postdoctoral fellowship and NSF grant CCR
9800024
yE-mail: ambainis@cs.berkeley.edu, Computer Science Di
vision, U.C. Berkeley, Berkeley, California, USA,supported
by Microsoft Graduate Fellowship and NSF grant CCR9800024
zE-mail: kempe@math.berkeley.edu, Departments of Math
ematics and Chemistry, U.C. Berkeley, Berkeley, California,
USA, supported by the Center for Pure and Applied Mathe
matics, U.C. Berkeley, and by NSA and ARDA under ARO
xE-mail: vazirani@cs.berkeley.edu, Computer Science Divi
sion, U.C. Berkeley, Berkeley, California, USA, supported
by NSF grant CCR-9800024
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. STOC’01, July 6-8, 2001, Hersonissos, Crete, Greece. Copyright 2001 ACM 1-58113-349-9/01/0007 ...$5.00.
In this paper, we initiate a study of the theory of quantum walks on graphs | the motivation, as in the case of Markov chains, is to study global properties of a certain structured set, using repeated application of local transition rules. In the quantum setting, though, the local transition rule is dened to be unitary, rather than probabilistic. A classical Markov chain is said to be a random walk on an underlying graph, if the nodes of the graph are the states in S, and a state s has non zero probability to go to t if and only if the edge (s; t) exists in the graph. To de ne a quantum random walk, in addition to the Hilbert space spanned by the nodes of the graph, we must explicitly introduce the Hilbert space spanned by the outcomes of the coin that control the process. Thus, the quantum walk is allowed to use an auxiliary Hilbert space. Now, the quantum walk on a graph is naturally de ned to be a unitary transformation on the tensor product of the Hilbert space of the graph and the auxiliary Hilbert space, and with the property that the probability amplitude (rather than the probability) is non zero only on edges of the graph. How do the basic de nitions of Markov chains carry over to quantum walks? The most fundamental property of Markov chains is the fact that they converge to a stationary distribution, independent of the initial state. However, by their very de nition, quantum walks do not converge to any stationary state. This is due to the fact that unitary matrices preserve the norm of vectors, and hence the distance between the vectors describing the system at subsequent times does not converge to 0. One can ask whether the probability distribution induced on the nodes of the graph converges in time, but it turns out that it does not converge either. Yet we can obtain a natural notion of convergence in the quantum case, if we de ne the limiting distribution as the limit of the average of the probability distributions over time. This de nition captures the amount of time the walk spends in each subset of the nodes, and moreover, it corresponds to the natural concept of sampling from the graph, since if one measures the state at a random time chosen from the interval f1; ::; tg, the resulting distribution is exactly the average
distribution. We show that although in general, the limiting distribution is a function of the initial state of the quantum walk, for Cayley graphs of Abelian groups it is independent of the initial state, and is uniform over the group elements. The rate of convergence, called the mixing time, is of crucial importance to algorithmic applications of classical Markov chains. Given the notion of limiting distribution in the quantum case, we can now talk about mixing times of a quantum walk. A natural de nition for mixing time is the time it takes for the average probability distribution to get close to the limiting distribution. We can also talk about measures for how fast the quantum walk spreads or how long it takes the quantum walk to escape from a small neighborhood. We give de nitions of quantum mixing time,
50


 sampling time, lling time, and dispersion time. How do the various mixing times of quantum walks compare with their classical counterparts? We show that the quantum walk on a cycle converges in time O(n log n), giving a nearly quadratic speedup over the classical walk. For the cycle this quadratic speed up is the best possible, since the diameter of the graph is clearly a lower bound for the mixing time. How large can the quantum speed up be, for other graphs? We give a general lower bound on the various measures for the quantum mixing time, in terms of the conductance of the underlying graph. Our main result is that quantum random walks on graphs can be at most polynomially faster than their classical counterparts, and in fact, for bounded degree graphs, the gap is at most quadratic. It is still an open question whether quantum walks can be used to obtain a quadratic speed up for certain randomized algorithms | such as 2-SAT. Indeed, all quantum algorithms from the last decade | including Shor's celebrated factorization algorithm[9] and Grover's search algorithm[6] | use only quantum Fourier transforms and classical computation. Is it possible to use other types of unitary transformations to design new quantum algorithms? One constraint that must be met is that the unitary transformations must be poly-local | they must be a product of a polynomial number of local unitary transformations. Quantum walks on graphs might provide a good starting point to explore the e ects of a sequence of local unitary transformations. The paper is organized as follows. We rst give some background regarding classical Markov chains and the quantum model. We proceed to de ne quantum Markov chains, and prove various general results about the limiting distribution. We then prove the speed up for the quantum walk on the cycle, which is followed by an upper bound on the mixing time for general graphs. Finally we prove the polynomial lower bound on the speed up for any graph, and conclude with a list of open questions. Related Work: Various researchers studied special cases of quantum walks on graphs. Feynman studied quantum walks on a line; Farhi and Gutmann[5] and Childs, Farhi and Gutmann[4] studied quantum walks on various graphs and gave examples of graphs on which the quantum walk hits a particular node exponentially faster than a classical walk. (Note that this is a di erent task from the convergence to the stationary distribution, which we consider in this paper.) Ambainis, Bach, Nayak, Vishvanath and Watrous[2] studied various properties of the discrete-time quantum walk on the line. In particular, they have calculated the the asymptotic behavior of the probability distributions for the walk on the in nite line, and shown that the probability distribution at time t is within a constant in total variation distance from the uniform distribution over an interval which is of length linear in t.
2. BACKGROUND
2.1 Random Walks
A simple random walk on an undirected graph G(V; E), is described by repeated applications of a stochastic matrix
P , where Pu;v = 1
du if (u; v) is an edge in G and du the
degree of u. If G is connected and non-bipartite, then the
distribution of the random walk, Dt = P tD0 converges to a stationary distribution which is independent of the initial distribution D0. For G which is d regular, i.e. if all nodes
have the same degree, the limiting probability distribution is uniform over the nodes of the graph. There are many de nitions which capture the rate of the convergence to the limiting distribution. A survey can be found in [7].
Definition 2.1. Mixing Time:
M = minfT j 8t T; D0 : jjDt jj g;
where here and throughout the paper, we use the total variation distance to measure the distance between two distributions d1; d2: kd1 d2k = Pi jd1(i) d2(i)j.
Definition 2.2. Filling Time:
= minfT j 8t T; D0; X V : Dt(X) (1 ) (X)g:
Definition 2.3. Dispersion Time:
= minfT j 8t T; D0; X V : Dt(X) (1 + ) (X)g:
The mixing time is related to the gap between the (unique) largest eigenvalue 1 = 1 of the stochastic matrix P , and the second largest eigenvalue 2.
Theorem 2.4. Mixing time and spectral gap: [10]
2
(1 2) log 2 M 1
(1 2) (miax log i 1 + log 1)
(1)
The mixing time of a random walk on a graph is strongly related to a geometric property of the graph, the conductance, denoted by .
Definition 2.5. Let the capacity CX and the ow FX of a subset X G of the graph G be de ned as
CX = u2XX
u FX = X
u2X;v62X
pu;v u: (2)
where is the stationary distribution, and pu;v is the transition probability. Then the conductance is
= min
0<jX j<jGj CX 1=2
FX CX
(3)
Theorem 2.6. Conductance and spectral gap:[Jerrum, Sinclair[11]]
2
2 (1 2) 2 (4)
Theorems 2.4 and 2.6 together imply that the mixing time
of a Markov chain is bounded between (1= ) and O(1= 2). Example It is well known that for the simple random walk on an n cycle, the mixing time is quadratic, M =
(n2 log(1= )), and so are the lling time and the dispersion time. The conductance of this chain is 1=n, which gives a lower bound of (n) time steps for convergence, and an
upper bound of O(n2).
2.2 Quantum Computation
The model. Consider a nite Hilbert space H with an or
thonormal set of basis states fjsig for s 2 . The states
s 2 may be interpreted as the possible classical states of
the system described by H. In general, the state of the sys
tem, j i, is a unit vector in the Hilbert space H, and can
be written as j i = Ps2 asjsi, where Ps2 jasj2 = 1. h j
denotes the conjugate transpose of j i. h j i denotes the in
ner product of j i and j i. A quantum system can undergo
two basic operations: unitary evolution and measurement.
51


 Unitary evolution : Quantum physics requires that the evolution of quantum states is unitary, that is the state
j i is mapped to Uj i, where U satis es U Uy = I,
and U y denotes the transpose complex conjugate of U . Unitary transformations preserve norms, can be diagonalized with an orthonormal set of eigenvectors, and the corresponding eigenvalues are all of absolute value 1.
Measurement : We will describe here only a measurement in the orthonormal basis jsi: The output of the mea
surement of the state j i is an element s 2 , with
probability jhsj ij2. Moreover, the new state of the
system after the measurement is jsi.
Combining two quantum systems : If HA and HB are
the Hilbert spaces of two systems, A and B, then the joint system is described by the tensor product of the Hilbert spaces, HA HB. If the basis states for HA,
H
B are fjaig; fjvig, respectively, then the basis states
of HA HB are fjai jvig. We use the abbreviated
notation ja; vi for the state jai jvi. This coincides
with the interpretation by which the set of basis states of the combined system A; B is spanned by all possible classical con gurations of the two classical systems A and B.
Non-unitary evolution The unitary model of quantum computation is not the most general model possible. In fact, the most general quantum state is a semi definite positive trace one matrix, , called the density matrix. The density matrix of j i is j ih j. evolves
by a unitary operator U to U U y. In general, the evolution of the density matrix is not necessarily unitary; evolves to E , where E is a completely positive linear operator, or a super operator. Another way to think of non unitary evolution is by adding qubits to the system, applying unitary transformation on the entire system and then throwing the extra qubits away. For more details see [1, 8].
3. QUANTUM MARKOV CHAINS
3.1 Definitions
Let G(V; E) be a graph, and let HV be the Hilbert space
spanned by states jvi where v 2 V . We denote by n, or
jV j the number of vertices in G. First assume that G is d
regular. Let HA be an auxiliary Hilbert space of dimension
d spanned by the states j1i through jdi (we think of this
auxiliary Hilbert space as the \coin space"). Let C be a unitary transformation on HA (which we think of as the
\coin-tossing operator"). Label each directed edge with a number between 1 and d, such that for each a, the directed edges labeled a form a permutation. For Cayley graphs the labeling of a directed edge is simply the generator associated with the edge. Now we can de ne a shift operator S on HA
HV such that Sja; vi = ja; ui where u is the a-th neighbor
of v. Note that since the edge labeling is a permutation, S is unitary. One step of the quantum walk is given by U = S (C I). We call this walk a coined quantum walk. Example: Coined Quantum Walk on the Cycle Consider the graph G which is a cycle with n nodes. This 2regular graph can be viewed as the Cayley graph of the
Abelian group Zn with the generators +1 (denoted by R for right) and 1 (denoted by L for left). The Hilbert space of
the walk would then be C2 Cn. We choose the coin tossing
operator to be the Hadamard transform,
H = p12
11
1 1 (5)
and the shift S is de ned by
SjR; ii = jR; i + 1 mod ni (6)
SjL; ii = jL; i 1 mod ni
The quantum walk is then de ned to be repeated applications of the Hadamard matrix operating on the rst register, followed by the shift S. Note that the coin we use corresponds to a classical \ unbiased" walk, in the sense that if measured, the walk has an equal chance of moving left or right. In our more general de nition, the general quantum walk, we relax our restriction on the exact form of U , and require only that U respects the structure of the graph. In other words, we require that, for any v and a, the su
perposition Uja; vi only contains basis states ja0; v0i with
v0 2 Q(v) [ fvg, where Q(v) is the set of adjacent nodes to
v. This means that the quantum walk only moves to neighbors of v or stays at v. More formally, let X be a set of vertices, and B the set of vertices which are neighbors of vertices in X (but that are not in X.) We denote by PX; PB the probability to measure a vertex in X; B respectively.
Claim 3.1. For any state j i,
PX(Uj i) PX(j i) + PB(j i):
Proof: Let j i = j 1i + j 2i, with j 1i being a superposi
tion over vertices in X [ B and j 2i being a superposition
over X B. Then, PXUj 2i = 0 because ja; vi components of j 2i get
mapped to components corresponding to neighbors of v and no vertex in X B is connected by an edge to a vertex in X. Therefore, PXU j i = PX U j 1i. Since PX is a
projection (and can only decrease norm) and U is unitary,
PXUj 1i kUj 1ik2 = k 1k2. Since j 1i is a superposition
over vertices in X [B, k 1k2 = kPXj 1ik2 +kPBj 1ik2. 2
In our most general de nition, the Non Unitary Quantum Walk, we allow the quantum operation representing one time step of the Markov chain to be non-unitary, i.e. the unitary matrix U is replaced by a completely positive linear operator E (a super-operator) operating on the state of the system, represented by the density matrix on the Hilbert space H = HG HA. We say that the walk de ned
by E respects the graph G if for any density matrix on H
and all subsets X of the vertices,
PX (E ) PX( ) + PB( ):
In the rest of the paper we use the unitary de nition, but all de nitions extend in a natural way to the non-unitary case.
3.2 Limiting Distribution
We now discuss the evolution of a quantum walk as a function of time. Starting with an initial state j 0i, the
state of the quantum walk at time t is j ti = U tj 0i: In
general the limit limt7!1 j ti does not exist. The reason
being that U , as a unitary transformation, preserves the
52


 norm of j ti U j ti. Consider instead the probability
distribution on the nodes of the graph induced by j ti,
Definition 3.2. Pt(vj 0) = Pa2A jha; vj tij2.
We will sometimes denote this probability by Pt (v). One might ask whether this probability distribution converges to a limit. However, Pt does not converge either. To see this,
rst observe that the eigenvalues of U are of the form ei ,
and therefore after a nite number of steps, t, ei t is arbitrarily close to 1 simultaneously for all eigenvalues. Hence the evolution of the state is quasi periodic | the state of the
system U tj 0i is arbitrarily close to j 0i (and U t+1j 0i is
arbitrarily close to j 1i) for in nitely many times t. As long
as the probability distributions at time 0 and 1 are di erent, P0 6= P1, this implies that Pt does not converge.
Despite the fact that the actual distribution does not converge, its average over time does. We de ne:
Definition 3.3. PT (vj 0) = 1
T PT 1
t=0 Pt(vj 0)
It turns out, as we will see soon, that for any initial state this quantity always has a limit as T grows to in nity, which we denote by (v) (and sometimes write (vj 0) if we wish
to stress its dependence on the initial vector). Intuitively, this quantity captures the proportion of time which the walk \spends" in any given node. Note that it is easy to sample according to this distribution PT using the following process: Uniformly pick a random time t between 0 and T 1, let the process evolve for t time steps and then measure to see which node it is at. The node will then be distributed according to PT . We now prove a general statement about the convergence of PT . The algebra used to prove this theorem will be useful in the rest of the paper. Let j ji, j denote the eigenvectors
and corresponding eigenvalues of U , respectively.
Theorem 3.4. For an initial state j 0i = Pj aj j ji,
Tl7i!m1 PT (vj 0) = i;j X;a
aiaj ha; vj iih jja; vi
where the sum is only on pairs i; j such that i = j.
Proof: We start by writing down the probability to measure the basis state ja; vi in j ti, for a xed t.
jha; vj tij2 = j Xi
ai t
iha; vj iij2
= i; Xj
aiaj ( i j )tha; vj iih jja; vi (7)
We now take the average over time of (7), from t = 0 to T 1. The only time dependent term in the above expression
is ( i j )t. Hence, we are interested in
1 T
T1
X
t=0
( i j )t (8)
We separate into two cases: One in which i j = 1, or equivalently i = j. In this case, we have that the average in Eq. (8) is equal to 1. In all other cases, we can write
j1
T
T1
X
t=0
( i j )tj = j1 ( i j )T j
j1 i j j j 2
T j i jj (9)
The latter term converges to zero, therefore the contribution to the limiting distribution comes solely from terms with i = j . Thus, the limiting distribution can be derived from the expression in equation 7 by summing only over pairs which correspond to equal eigenvalues. This yields the desired claim, using the fact that the probability to measure a node v is a sum over the probabilities to measure ja; vi,
and so we can let each term converge separately. 2 In the case in which all eigenvalues of U are distinct, the limiting distribution takes a very simple form. Denote by pi(v) the probability to measure the node v in the eigenstate
j
ii, so pi(v) = Pa jha; vj iij2.
Corollary 3.5. If all eigenvalues of U are distinct, then for an initial state j 0i = Pj ajj ji,
Tl7i!m1 PT (vj 0) = Xi jaij2pi(v):
By corollary 3.5, the limiting distribution depends on the initial state. However, if all eigenvectors induce a uniform distribution over the nodes of the graph, the limiting distribution is uniform, as is easily implied by the theorem. We show:
Theorem 3.6. Let U be a coined quantum walk on the Cayley graph of an Abelian group, such that all eigenvalues of U are distinct. Then the limiting distribution is uniform over the nodes of the graph, independent of the initial state
j
0i.
Proof: We derive an explicit expression for the eigenvectors of U , which, for a coined quantum walk, is of the form U = S (C I). We note that S is a matrix of dimension dn, for n = jV j. S is composed of d blocks, each of dimension
n. The a th block corresponds to applying the a-th generator ga on the group. We note that the characters of the
group, j ki = p1n Pv k(v)jvi, are simultaneous eigenvec
tors of all the blocks. The eigenvalue associated with apply
ing the a-th block on j ki is k(ga 1). Since the application
of the coin applies an identity on HV , a natural guess for the
form of the eigenvectors is (Pd
a=1 cajai) j ki. Applying
C and then S on this vector, we nd that this vector is an eigenvector of U if Pa cajai is an eigenvector of the d d
matrix Hk = k C, where k is a diagonal matrix, with
k(a; a) = k(ga 1). Since Hk, as a product of two unitary matrices, has d orthogonal eigenstates, the tensor products of these eigenstates (which depend on k) with j ki give d
orthonormal eigenstates for U . Running over k, this gives an orthonormal set of nd eigenstates for U . It is easy to see that the probability distribution that these eigenstates induce on the group elements is uniform, since the characters
j
ki are uniformly distributed over the group, and since the
eigenstates are of the form of a tensor product, the proba
bility to measure a; v in (Pd
a=1 cajai) j ki summed over a
is just the probability to measure v in j ki. This proves the
theorem, using corollary 3.5. 2 We claim that for any quantum walk, if the limiting distribution is independent of the initial node and state of the auxiliary space, then it must be uniform over the nodes.
Claim 3.7. Consider a quantum walk such that for any initial basis state of the form ja; vi, for v 2 V , the limiting
distribution over the nodes of the graph is equal to . Then is uniform over the nodes of the graph.
53


 Proof: If the initial state is chosen randomly from a uniform distribution over all basis states, then the limiting distribution is equal to the average over the limiting distributions for each initial state, but since they are all equal to , the limiting distribution for the uniform mixture is . However, the density matrix which represents a complete mixture, i.e. a uniformly random basis state of the space spanned by ja; vi is preserved under unitary transformation,
since the unitary matrix maps this space into itself. Hence for any time t it induces a uniform probability distribution over the nodes in the graph, because the initial density matrix induces this distribution. This means that the limiting probability distribution starting from the complete mixture is uniform. Combining the two facts together, we get that is uniform. 2
3.3 Mixing Times
We rst de ne the analogue of the classical notion of mixing time:
Definition 3.8. Mixing time:The mixing time M , of a quantum Markov chain is
M = minfT j 8t T; ja; vi : k ( ja; v) Pt( ja; v)k g:
where by the notation P ( ja; v) we mean the probability dis
tribution conditioned on the initial state being ja; vi. This
quantity measures the number of time steps required for the average distribution to be -close to the limiting distribution, starting from a basis state. We next de ne a closely related quantity which we call sampling time:
Definition 3.9. Sampling time:The Sampling time S , of a quantum Markov chain is
S = minfT j 8t T; ja; vi; X V :
j (Xja; v) Pt(Xja; v)j (Xja; v)g:
This is the time it takes for the walk to approximate the limiting distribution point-wise. Sampling at a random time between 0 and S 1 results in a distribution which is -close point-wise to the limiting distribution, justifying the term sampling time. In the same sense, sampling at a random time between 0 and M 1 results in a distribution which is close to the limiting distribution in total variation distance. The third quantity, namely the lling time of the quantum Markov chain is de ned as the rst time at which the walk can claim to have visited all sets with at least (1 ) the correct proportion:
Definition 3.10. Filling time: The lling time, , of a quantum Markov chain is
= minfT j 8X V; ja; vi 9t T :
Pt(Xja; v) (1 ) (Xja; v)g:
We also de ne the dispersion time, which is in some sense the opposite de nition to lling time:
Definition 3.11. Dispersion time: The dispersion time, , of a quantum Markov chain is
= minfT j 8X V; ja; vi 9t T :
Pt(Xja; v) (1 + ) (Xja; v)g:
This quantity measures how fast the quantum walk escapes any subset of the nodes. Remark: We note that one could consider all the above de nitions of mixing times with an arbitrary initial state,
j
0i, and not restrict the initial state to be a basis state of
the form ja; vi. However, the mixing time could change sig
ni cantly. We will see in the cycle example that the mixing time is almost linear for initial basis states of the form ja; vi,
but it is actually quadratic for general initial states.
The above de nitions can be related one to another in various ways. First, it turns out that the sampling time is an upper bound on the mixing time, the lling time and the dispersion time:
Theorem 3.12. M ; ; S :
Proof: Fix a subset of the nodes X, and an initial state ja; vi. Suppose at all times before S , Pt(Xja; v) < (1
) (Xja; v). Then the average at time S of the probability
to measure X is less than (1 ) (Xja; v). But by de nition
of the sampling time this is a contradiction. Hence there exists some time before S at which the probability for the measurement outcome to be a node in X is Pt(Xja; v)
(1 ) (Xja; v), and since this is true for all X, we have
S . We argue in exactly the same way to prove S . The statement M S follows trivially from the de nition of total variation distance. 2 We will later de ne ampli ed versions of these quantities, and nd more relations between them. Let us rst proceed to give an upper bound on the mixing time M for the quantum walk on the cycle.
4. QUANTUM WALK ON THE CYCLE
In subsection 3.1, we have de ned the coined quantum walk on the cycle. We restrict the discussion to cycles of an odd number of nodes n. We rst show that the limiting distribution for this walk is uniform.
Theorem 4.1. The limiting distribution for the coined quantum walk on the n-cycle, with n odd, and with the Hadamard transform as the coin, is uniform on the nodes, independent of the initial state j 0i.
Proof: To prove that the limiting distribution is uniform, by theorem 3.6 it suÆces to show that all eigenvalues of U are di erent. By the proof of theorem 3.6, the set of eigenvalues of U consists of all eigenvalues of the matrices:
Hk = !k 0
0 !k
p12
p12
p12
p12 ! =
!pk2
!pk2
!p2k
!p2k !
(10) where ! = e 2 i
n . We now show that the eigenvalues of Hk are distinct. The eigenvalues of Hk are the roots of the following quadratic equation:
2 ip2 sin( 2 k
n ) 1 = 0 (11)
The two solutions to this equation are of the form ei k , with k being one of the two solutions for the following equation:
sin( k) = sin( 2 k
n)
p2 : (12)
54


 In particular, j sin( k)j p12 which means that the roots of
the quadratic equation 11 are con ned to two regions of the unit circle, k 2 [ =4; =4] and k 2 [3 =4; 3 =4]. There
are two solutions for equation 12, k;1 and k;2 where k;1 = k;2, so they lie in di erent regions, and in particular, they are distinct. To get equality between eigenvalues coming from di erent k's, we have to have sin( 2 k
n ) = sin( 2 k0
n ),
which implies that either k = k0 or k + k0 = n=2. The latter equation has no solutions for odd n, which implies the theorem. 2
Theorem 4.2. For the quantum walk on the n-cycle, with n odd, with the Hadamard coin, we have
M O( n log n
3 ):
Proof: We prove an upper bound on the mixing time M , i.e. we give an upper bound on the total variation distance between the average distribution PT and the limiting distribution . This is done using the following lemma which holds for any quantum walk.
Lemma 4.3. Consider a general quantum walk speci ed by the unitary matrix U , and let i; i be the eigenvectors and corresponding eigenvalues of U , respectively. For any initial state j 0i = Pi aij ii, the total variation distance
between the average probability distribution and the limiting probability distribution satis es
kPT ( j 0) ( j 0)k 2 i;j;Xi6= j jaij2 1
Tj i jj
Proof: We recall that in the proof of lemma 3.4 we have already bounded the time dependent term in the average probability distribution. From equations (7) and (9) we have that jPT (v) (v)j
X
a;i;j; i6= j jaij jaj j jha; vj iij jh jja; vij 2
T j i jj (13)
We now use j2abj jaj2 + jbj2 twice, and summing over v
we get that kPT k is at most
X
v;a;i;j; i 6= j
jaij2 + jaj j2
2 jha; vj iij2 + jh jja; vij2
2
2
Tj i jj
(14) Summing rst over all v and a we get the desired bound. 2 We observe that in that lemma, the distances j i j j are
of crucial importance, and they need to be large for the convergence time to be small. By the proof of theorem 4.1, the eigenvalues are distributed in two regimes (which we will call
R and R0) of the complex unit circle, k;1 2 [ =4; =4] = R
and k;2 2 [3 =4; 3 =4] = R0. Near the boundaries of
these regimes, i.e. for those 's coming from k's in the vicinity of n=4; 3n=4 modulo n, the distance between two adja
cent eigenvalues can be of the order of 1=n2. However, we claim that the contribution of these problematic eigenvalues is small, and that for the rest of the eigenvalues, the distance is of order 1=n. We x 0 < Æ < 1 (which will later be related to ) and de ne
RÆ = [0; (1 Æ) 2 ] [ [(1 + Æ) 3
2 ; 2 ] (15)
R0Æ = [(1 + Æ) 2 ; (1 Æ) 3
2]
These two regimes together cover the entire interval [0; 2 ]
except for a 2Æ portion of it. We refer to k such that 2 k
n is in
one of these regimes as \Æ-good", and other k0s are \Æ-bad". We also refer to eigenvectors and eigenvalues associated with \Æ-good" k's as \Æ-good", and similarly for \Æ-bad". We will later show that if the initial state for the walk is a basis state, the contribution of the bad eigenvectors is small, because the projection of basis states on bad eigenvectors is small. But rst, let us restrict our attention to an initial state which is a superposition of good eigenvectors, and consider the convergence to limiting distribution in this case. We rst give a lower bound on the spacing between good eigenvalues.
Definition 4.4.
Æ = mi;ijnfj i jj s:t: i 6= jg
where i; j run only on Æ-good eigenvalues.
Claim 4.5. For the quantum walk on the odd n cycle with
the Hadamard coin, Æ p2Æn .
Proof: First observe that if i; j originate from the same
k, then they lie in two di erent regimes R and R0, which
means that j i j j is at least p2. Hence, we can restrict
our attention to eigenvalues coming from di erent k's. Let
i, j originate from k; k0, respectively. Then using equation 12 we have
j
i jj j sin( i) sin( j)j = p12 j sin( 2 k
n ) sin( 2 k0
n )j
(16)
We separate the proof to two cases. In the rst case, k; k0 lie
in the same regime, RÆ or R0Æ. Recall the intermediate value theorem, which states that for a continuous function, for any x y, there exists x z y such that jf (x) f (y)j =
jf 0(z)(x y)j: Applying this theorem with f (x) = sin(x), we
get
j sin( 2 k
n ) sin( 2 k0
n )j = j cos( )( 2 (k k0)
n )j j cos( ) 2
nj
(17) for some 2 k
n
2 k0
n . Since k; k0 are in the same regime,
then 2 RÆ or 2 R0Æ, and by monotonicity of the cos
function, we have:
j cos( )j j cos( (1 Æ)
2 )j = j sin( Æ
2 )j Æ (18)
where the last equality follows from the fact that sin(0) = 0; sin( =2) = 1, and sin is convex in the regime [0; =2]. If
k; k0 belong to di erent regimes, then we can no longer claim that cos( ) is large. Instead, we write
j sin( 2 k
n ) sin( 2 k0
n )j = j sin( 2 k
n ) sin( 2 k0
n )j (19)
j cos( 0)( 2 (k + k0)
n )j j cos( 0) n j
for some 0, between 2 k
n and 2 k0
n . Now, 2 k
n and 2 k0
n
lie in the same regime, and so using the same argument as before, the lemma follows. 2 We can now use claim 4.5 to give a better lower bound on the distance between two eigenvalues.
55


 Claim 4.6. Let us order the eigenvalues such that 0 Arg( 1 ) Arg( 2):::: Arg( 2n ) 2 . Consider i and
j which lie in the same regime, RÆ or R0Æ. Then
j
i jj 2p2 ji jj Æ
Proof: Consider i; j as in the requirements of the claim. Let Li;j be the length of the shorter arc on the unit circle that
connects j to i. We rst claim that j i jj 2p2 Li;j
in our regime. This is true since the ratio j i j j=Li;j
is monotonically decreasing in i j in the regime i j 2 [0; =2], and so we can bound j i j j=Li;j from below
by its value on the boundary, j i jj = =2, which gives
j
i j j=Li;j = 2p2 . Hence, to bound j i j j we give
a lower bound on Li;j . We have Li;j = ji jjLi;i+1, so it
suÆces to bound Li;i+1. This is done by noticing that Li;j 2j sin Li;j =2j = j i jj Æ, where the rst inequality uses
sin(x) x, the second equality uses simple trigonometry, and the last inequality uses claim 4.5. Hence, Li;j = ji
jjLi;i+1 ji jj Æ which combined with j i jj 2p2 Li;j
gives the claim. 2
Claim 4.7. Let j i = Pi aij ii such that all coeÆcients
of Æ bad eigenvectors are zero. Then
kPT k 2n(ln(n) + 2)
TÆ
Proof: Using lemma 4.3 we write
kPT k 2 k X
0X
i;j;ji jj=k jaij2
T k2p2 Æ
+2
00
X
i;j jaij2 1
T p2
(20) where in the rst sum the prime indicates the fact that we
sum over pairs i; j in the same regime RÆ or R0Æ, such that i 6= j, and in the second sum the double prime indicates
that the sum is over pairs i; j such that i; j are in the di erent regimes. We have used claim 4.6 in the rst sum,
and the fact that j i jj p2 for eigenvalues from di erent
regimes in the second sum. To bound the rst term, we observe that for each i there are at most two eigenvalues j such that ji jj = k. We rst
sum over i; j. Then, summing over k, we use the fact that the sum of the rst n terms of the harmonic series is less
than ln(n) + 1. Thus, the rst term is at most p2 (ln(n)+1)
TÆ .
For the second term we get an upper bound p2n
T . Using
claim 4.5 to bound Æ in the rst term we get the desired claim. 2 We now prove that the contribution of the Æ-bad vectors is small. This follows from the following two claims.
Claim 4.8. The projection of any basis state on the bad eigenvectors is of norm squared at most 2Æ.
Proof: The 2n dimensional Hilbert space of the quantum walk can be viewed as a direct sum of the two dimensional subspaces Lk, where Lk is the space spanned by the two eigenvectors originating from k. The projection of a basis
state on Lk is of norm squared exactly 1
n . The claim follows
from the fact that there are 2Æn bad k0s. 2
Claim 4.9. Consider two initial states, j 0i; j 0i. De
note by PT ,PT the average distributions in the quantum
walk starting with j 0i; j 0i, respectively. Then for all T ,
the total variation distance between the average distribution is bounded by the distance between the initial states:
kPT PT k 2kj 0i j 0ik
Proof: Denote by j ti; j ti the states at time t starting with
j
0i; j 0i as initial states. Denote by Pt ; Pt the induced
distributions of j ti; j ti on the nodes of the graph. Clearly,
kPT PT k maxt T kPt Pt k. Due to unitarity of the
walk, the distance is preserved: kj ti j tik = kj 0i j 0ik.
By lemma 11 in [1], the total variation distance between the two probability distributions resulting from a measurement on two states which are apart, is at most 2 . This proves the claim. 2
Claim 4.10. Let j 0i be the initial basis state, and j 0i be
the initial basis state projected on the Æ good eigenvectors, and renormalized. Then
kPT k 8p2Æ + kPT k
Proof: We write
kPT k kPT PT k + kPT k + k k: (21)
The rst term, by claim 4.9 is smaller than 2kj 0i j 0ik.
The last term is also smaller than 2kj 0i j 0ik, since it
is the limit of distances which are smaller than this term.
We claim that kj 0i j 0ik 2p2Æ. This is true since by
claim 4.8 we can write j 0i = aj 0i + jvi, where jvi is a
vector of norm at most p2Æ and a is larger than p1 2Æ.
kj 0i j 0ik j1 aj + p2Æ 2p2Æ. 2
We can now combine claim 4.10 and claim 4.7 to nish
the proof of the Theorem. If we now pick Æ = 1
2 ( =16)2, and
T 4n(ln(n) + 2)= Æ, we get that
kPT k 8p2Æ + 2n(ln(n) + 2)
T Æ 2 + 2 = : 2 (22)
Remark In the theory of classical Markov chains, the distance between the rst and second eigenvalues plays a crucial role in mixing time analysis. In the quantum case, we see that the distances between eigenvalues play a similarly important role; However, unlike in the classical case, since all eigenvalues of a unitary matrix are of absolute value 1, there is no special eigenvector which plays the role of the xed state, and all eigenvalues play are equally important.
5. AMPLIFICATION
In classical Markov chains, after approaching a certain closeness to the limiting distribution, the distance to the limiting distribution starts to drop exponentially. Theorem 4.2 gives only polynomial dependence on 1= in the quantum case. However, one can amplify the closeness in a very simple way. Suppose the limiting distribution ( ja; v) is in
dependent of the initial node v and the state a, and is equal to . (Recall that by claim 3.7 is uniform.) In this case, the closeness to can be ampli ed in a standard way to get logarithmic dependence on 1= . This is done by running the walk for M steps (i.e. for a random time between 0 and M 1) and then measuring the node. If the measured node is v, we then initialize the state to be ja; vi with a random
auxiliary state a, and start the walk again for one more stage of M steps, and so on for k times. We claim:
56


 Lemma 5.1. Ampli cation lemma Running the quantum walk for k ampli cation steps, each lasting M time
steps, results in a distribution which is k close to .
Proof: De ne Pv;u to be the probability to measure the node u starting from a random initial basis state ja; vi, in
one ampli cation step, where a is randomly chosen from all basis states of the auxiliary space. The matrix P dened by these transition probabilities is a stochastic matrix. We claim that applying one ampli cation step starting from the uniform distribution one gets the distribution again. The reason is that a uniformly random state ja; vi (which in
duces a uniform distribution over the nodes v) is a complete mixture of the Hilbert space in which the walk evolves. The unitary transformation associated with the walk is a map from this space to itself, therefore, starting from a complete mixture of this space, the state of the system remains a complete mixture, i.e. is preserved. We now claim that the L1 norm of any vector orthogonal to is shrunk by a factor of by the matrix P . To prove that k P k k k for ? , observe that by de nition of M , for
any distribution = + , k P k . This means that
for any vector for which the sum of elements is zero, and each coordinate is at least 1=n, we have k P k . We
can de ne a basis for the subspace orthogonal to , which is composed of such vectors: These will be the vectors vi,
where vi has (n 1)=n on its ith coordinate and the rest are all equal to 1=n. Any ? can be written as a sum of vi
and : = Pi i(vi+ ) = Pi ivi. k P k Pi j ijkviP k
P
i j ij = k k .
We can now prove the claim by induction. Starting from a distribution which is within Æ total variation distance from , we can write = + where ? , and k k Æ.
Then, k P k = k P + P k = k P k k k Æ : 2
For the cases in which the limiting distribution is independent of the initial state, we can now generalize our measures of convergence to allow the possibility of ampli cation. This means that in all de nitions we allow a warm start, i.e. we rst amplify for several ampli cation steps, which all together last TA time steps, to get an initial \warm" node (the exact times at which one measures are chosen so that TA is minimized, and the times at which the node is measured during TA are referred to as the \ampli cation scheme"). Then we apply the various de nitions of mixing times with the \warm start" node as the initial node. However, to account for the initial ampli cation stage, we add TA to the mixing times. We denote those ampli ed versions of convergence
with primes. M 0, S0 , and so on. We have:
Theorem 5.2. 0; 0 S0 log(1= minvf (v)g)
log(1= ) M
Proof: We rst prove the right inequality. Closeness to within point wise will be guaranteed if the total variation distance is at most minvf (v)g. For that, by the ampli 
cation lemma, it suÆces to apply log(1= min (v))=log(1= ) ampli cation steps, each of length M . The proof of the left
inequality is as follows. Let S0 be achieved with a certain ampli cation scheme. We then use the same ampli cation scheme for the dispersion time and the lling time, so that we start with the same distribution over initial nodes. Now, the remaining of the proof is exactly as the proof of theorem 3.12, referring only to the time interval starting at the end of the ampli cation stage. 2
Theorem 5.3. For the quantum walk on the n-cycle, with n odd, with the Hadamard coin, we have
M 0 O n log nlog 1 ; S0 ; 0 ; 0 O n log2 n log 1
proof: The upper bound on S0 ; 0 and 0 follows from theorems 5.2 and 4.2, and the fact that minf (v)g = 1=n. 2
6. GENERAL GRAPHS
We now prove a general upper bound on M for any quantum walk. This will imply upper bounds on the other mixing times by theorem 5.2. Let j ii be the eigenvectors of U with eigenvalues i. The
upper bound will be given in terms of , which is de ned to be the minimal spacing between the eigenvalues.
Theorem 6.1. Consider a general quantum walk on a graph G with n nodes, with an auxiliary space of dimension d. Then, for an initial state j i, the total variation distance
from its limiting distribution is
kPT ( j ) ( j )k (ln(nd=2) + 1)
T
Proof: The proof follows approximately the same lines as the proof for the upper bound for the cycle, except that the complications due to throwing away part of the system disappear. More precisely, the proof goes along the lines of the proof of claim 4.7. The main di erence is that we do not have a partition of the eigenvalues into two regimes. For this reason, in the counterpart of claim 4.6, we can have
j
i jj 2 [0; ] (instead of [0; =2]). Then, j i j j=Li;j
is minimized by j i j j = (instead of =2) and we get
j
i jj 2 ji jj . Also, the counterpart of equation
20 has just one summation (over all eigenvalues) instead of two (over eigenvalues in the same regime and eigenvalues in di erent regimes). After that, we just notice that in the general case there are nd eigenvalues, which implies that k = ji jj runs up to nd=2: 2.
Just like we did in the cycle case, one can separate the eigenvectors to \good" and \bad" vectors, where the proportion of the \bad" vectors is Æ, to get a better estimation of the mixing time.
7. THE LOWER BOUND
Here we are going to prove a lower bound on the various mixing measures of a general quantum random walk. In analogy to the classical case this bound will be stated in terms of the conductance of the underlying graph G (cf. Chapter 2).
We will de ne a slightly di erent quantity 0 rst: Let (X; X) be a cut in the graph G (i.e., a partition of vertices into two sets). De ne BX , the boundary of X, as the set of vertices in X that have an edge going to X. Let
0 = min0<jXj 1
2 jV j jBX j
jXj .
Theorem 7.1. The lling, dispersion, mixing and sampling times of a general quantum walk with a uniform limit
ing distribution are (1= 0).
Proof: Let (X; X) be the cut that achieves the minimum (jBX j=jXj). To simplify the notation, let B = BX .
Let HX be the Hilbert space supported by nodes in X, i.e.
the subspace spanned by fja; vig for all v 2 X and all basis
57


 states a of the auxiliary space. Let HX and HB be Hilbert
spaces supported by nodes in X and B (de ned similarly). We show a lower bound on lling and dispersion times by taking a random state j i of form ja; vi, v 2 X and showing
that the projection of U tj i onto HX is small for all t
(1= 0). For any state j i, let PXj i and PBj i be the projections of
j i onto HX and HB, respectively.
Let j i be a uniformly random basis state ja; vi, v 2 X. We
bound the expected projection of j i onto the boundary HB
and then use that to bound the expected projection of U tj i
onto HX. (This works because the only way to go from X
to X is through the boundary B.)
Claim 7.2. For any t, the expected value of kPBU tj ik2
is at most jBj=jXj.
Proof: j i is a uniformly random state in jXjd dimensions.
Since U is unitary, U tj i is a uniformly random state in
some jXjd-dimensional subspace of H. The projection of
this state to the jBjd-dimensional subspace HB is at most
jBjd
jXjd = jjBXjj (with equality if and only if HB U t(HX)). 2
By applying Claim 3.1 to PX U kj i, we get
kPXUkj ik2 kPXUk 1j ik2 + kPBUk 1j ik2:
By applying Claim 3.1 k 1 more times (to kPX U k 1j ik2,
then kPXU k 2j ik2 and so on), we get
kPXUkj ik2 kPBUk 1j ik2+: : :+kPBUj ik2+kPBj ik2:
By claim 7.2, the expected value of each term on the righthand side (for a random j i = ja; vi, v 2 X) is at most
jBj=jXj. Therefore, the expected value of the sum on the
right hand side is at most k(jBj=jXj). For some j i = ja; vi,
the sum Pk 1
i=0 kPBU ij ik2 is at most its expectation. For
this j i, we have
kPXUjj ik2
j1
X
i=0 kPBUij ik2
k1
X
i=0 kPBUij ik2 k jBj
jXj
for all j < k. For k to be the lling time, one of kPXU j j ik2
should be at least (1 ) jjVXjj . Then, k jjXBjj (1 ) jjVXjj
and k (1 ) jXjjXj
jBjjV j . Since jXj 1
2 jV j, jXj 1
2 jV j and
k = ( jjBXjj ) = (1= 0). A similar argument applies to dis
persion time and sampling time. The bound on mixing time is implied by theorem 3.12 2
The quantity 0 (which we call boundary) is similar but not identical to the conductance.
Lemma 7.3. For a graph with maximal degree d,
0 d;
where is the conductance of a simple random walk on the graph.
Proof: For a simple random walk on G, the limiting distribution is v = dv= Pv dv = dv=2jEj. Fix a cut X; X,
and denote the conductance of this cut by X . The capacity of X is CX = Pv2X dv
2jEj
djXj
2jEj . Let E(X : X) be the
set of edges going between X and X. The ow FX satis es
FX = jE(X:X)j
2jEj jBX j
2jEj . Therefore, X = FX
CX
2jBX jjEj
2djEjjXj
jBX j
djXj = 0X
d . This is true for any cut X, which implies the lemma. 2
Therefore, ( 10 ) = ( 1
d ) and theorem 7.1 implies an
(1
d ) lower bound on For constant degree d graphs, this
lower bound is ( 1 ), the same as the classical lower bound on lling, dispersion and sampling times. Since a classical
random walk converges in O( 1
2 ) steps, this means that a quantum walk can be at most quadratically faster.
Corollary 7.4. For a general quantum walk on a bounded degree graph, the lling, dispersion, sampling and mixing times are at most quadratically faster than the mixing time of the simple classical random walk on that graph.
For unbounded d, the factor-d gap between the two lower bounds (quantum and classical) is important. This gap can be quite large: we did not rule out the case in which the
quantum lling time is O(logc n) but d is (n). We suspect that the bound can be improved and quantum walks are at most quadratically faster on any graph. We can prove that for the special case of coined quantum walks.
Theorem 7.5. For a coined quantum walk, the lling, dispersion and sampling times are (1= ).
Proof: To simplify the proof, we assume that the unitary transformation U is of form C Æ S, not S Æ C (i.e. we rst do
the shift S and then the coin ip C). This assumption can
be removed by replacing the starting state j i by C 1j i
and adding an extra C at the end. The proof is similar to Theorem 7.1. We take the set X
which achieves the conductance, = FX
CX . Let HX and
H
X be similar to the proof of Theorem 7.1 and HC be the
Hilbert space spanned by edges in the cut (i.e., the space spanned by jb; vi, v 2 X, b Æ v 2 X). Let PX and PC be the
projections onto HX and HC, respectively.
Claim 7.6. For any t, the expected value of kPCU tj ik2
(for a uniformly random j i = ja; vi, v 2 X) is at most
jE(X:X )j
jXjd .
Proof: j i is a uniformly random state in jXjd dimensions.
Since U is unitary, U tj i is a uniformly random state in
some jXjd-dimensional subspace of H. The projection of
this state to the jE(X : X)j-dimensional subspace HC is at
most jE(X:X)j
jXjd . 2
Claim 7.7. For any state j i and any k 2 N,
kPXUkj ik2 kPXUk 1j ik2 + kPCUk 1j ik2:
Proof: De ne j 0i = Uk 1j i. Let j 0i = j 01i + j 02i, with
j 01i being a superposition over jb; vi with v 2 X or bÆv 2 X
and j 02i being a superposition over all other jb; vi.
Then, Sj 02i 2 HX because b Æ v 2= X for all jb; vi that
appear in j 02i. Since the coin ip C does not change v,
this also means that Uj 02i = C Sj 02i 2 HX. Therefore,
PXUj 0i = PXUj 01i.
Similarly to the proof of claim 3.1, kPXUj 01ik2 kj 01ik2 =
kPXj 01ik2 + kPCj 01ik2 = kPXj 0ik2 + kPCj 0ik2: 2
The rest of proof is identical to Theorem 7.1. 2
58


 7.1 Lower bound for non-unitary walks
We rst deal with a special case of non-unitary walks. In this case, instead of U , we have a set of possible unitary matrices Ui, and we choose one of them randomly to apply at time t. The lower bounds extend trivially to this case. We now give a simple lower bound on the sampling time of a general non-unitary walk in terms of the boundary.
Theorem 7.8. The sampling time of a general non-unitary
quantum walk with a uniform limiting distribution are ( 10 ).
Proof: Fix a cut, X; X. Suppose we start with a state concentrated on X. By applying the de nition of a nonunitary quantum walk that respects the structure of the graph (section 3.1) several times we get
PX Ek PBEk 1 + : : : + PBE + PB (23)
For S to be the sampling time, there must be some S k 2S such that PXEk (1 3 ) jjXGjj . On the other
hand, the sum at the right hand side of the above equation is exactly kPk(Bj ), which, for k > S , must satisfy
Pk(Bj ) (1 + )jBj=jGj (24)
This means that (1 3 ) jjXGjj k(1 + )jBj=jGj or
(1 3 )jXj
2(1 + )jBj S (25)
for all X. If we pick X to be the set which achieves the minimum boundary jBj=jXj, we get the desired result. 2
We leave it as an open question to generalize the lower bound for non-unitary walks to other mixing measures.
8. CONCLUDING REMARKS
In this paper we have set up the basic de nitions for quantum walks on graphs. However, the foundations of the theory of quantum walks on graphs still await discovery. We list here a few selected open problems. The rst open question is for which graphs quantum speed up is achievable. More generally, can the 1= lower bound always be achieved quantumly? In [3] it was shown that for any Markov chain, there exists a lifted version of it which achieves this bound, but no lifting can give better than 1= convergence. To achieve the lower bound of 1= by lifting, one has to be able to solve the multi-commodity ow on the graph, a task which is in general extremely hard. Therefore the lifting speed-up is an existence proof, rather than an algorithmic one. It would therefore be very interesting to know whether convergence in time 1= can be achieved by quantum walks for graphs other than the cycle in an eÆciently constructible way. An open question is to make our two bounds tight. We have shown how to improve the factor of 1=d in the lower bound for coined quantum walks, and this needs to be generalized to general quantum walks, or else nd a counter example. One possible candidate is the graph consisting of two complete graphs connected by one edge. It is not clear that quantumly one cannot achieve convergence in time O(n) which matches the 1=d = 1=n lower bound. The limiting distribution for general quantum walks still needs to be understood. For Abelian groups, we have shown that coined quantum walks converge to the uniform distribution. On the other hand, we know one example in which
a quantum walk does not converge to the same limiting distribution as the classical simple random walk. This is a quantum walk on the Cayley graph of the symmetric group S3. Is there a simple description, perhaps via representation theory, of the limiting distribution for quantum walks on Cayley graphs of non-Abelian groups? A very interesting question is how to use quantum walks in order to speed up algorithms. One way to do that is via speeding up the convergence time, however it is still an open question to give an example in which fast sampling cannot be done in an easy way classically. Another direction to pursue is to nd other ways of using the various curious features of quantum walks, rather than speeding up the convergence time. For example, one might try to use quantum walks which converge to limiting distributions which are di erent than those of the corresponding classical walks. Another way might be to investigate which quantum states can be generated using quantum walks. Generating interesting quantum states is an important primitive for quantum algorithms. A well known example is the graph isomorphism problem which can be reduced to the problem of generating a certain quantum state eÆciently.
9. ACKNOWLEDGEMENTS
We wish to thank John Watrous for introducing us to his model of a quantum walk on a line. We are grateful to Barbara Terhal for useful discussions. We are most grateful to Alesha Kitaev for pointing out to us an error in a previous version of this paper.
10. REFERENCES
[1] D. Aharonov, A. Kitaev, and N. Nisan. Quantum circuits with mixed states. Proceedings of STOC'98, pp. 20{30. [2] A. Ambainis, E. Bach, A. Nayak, A. Vishwanath, J. Watrous, One-dimensional quantum walks. Proceedings of STOC'01. [3] F. Chen, L. Lovasz and I. Pak, Lifting Markov chains to speed up mixing, Proceedings of STOC'99, pp. 275-281. [4] A. Childs, E. Farhi, S. Gutmann, An example of a di erence between quantum and classical random walks. LANL preprint http://www.arxiv.org/abs/quant-ph/0103020. [5] E. Farhi, S. Gutmann, Quantum computation and decision trees, Physical Review A, 58 : 915-928, 1998. [6] L. Grover, A fast quantum mechanical algorithm for database search Proceedings of STOC'96, pp. 212{219. [7] L. Lovasz and P. Winkler, Mixing times, in Microsurveys in Discrete Probability, Dimacs Series in Discrete Mathematics and Theoretical Computer Science, 41, eds. D. Aldous and J. Propp. [8] M. Nielsen, I. Chuang, Quantum Computation and Quantum Information. Cambridge University Press, 2000. [9] P. Shor, Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer, SIAM J. Comp., 26 : 1484{1509, 1997. [10] A. Sinclair, Algorithms for Random Generation and Counting, a Markov Chain Approach, Birkhauser, 1993. [11] A. Sinclair and M. Jerrum, Approximate counting, generation, and rapidly mixing Markov chains, Information and Computation, 82 : 93-133, 1989.
59
