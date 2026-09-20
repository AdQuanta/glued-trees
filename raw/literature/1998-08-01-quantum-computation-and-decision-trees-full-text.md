# Quantum computation and decision trees - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.58.915
> Collected: 2026-09-20
> Published: 1998-08-01
> Zotero parent key: PUN6TIUF
> Evidence: Zotero indexed PDF text

Quantum computation and decision trees
Edward Farhi*
Center for Theoretical Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139
Sam Gutmann†
Department of Mathematics, Northeastern University, Boston, Massachusetts 02115 ~Received 11 July 1997!
Many interesting computational problems can be reformulated in terms of decision trees. A natural classical algorithm is to then run a random walk on the tree, starting at the root, to see if the tree contains a node n level from the root. We devise a quantum-mechanical algorithm that evolves a state, initially localized at the root, through the tree. We prove that if the classical strategy succeeds in reaching level n in time polynomial in n, then so does the quantum algorithm. Moreover, we find examples of trees for which the classical algorithm requires time exponential in n, but for which the quantum algorithm succeeds in polynomial time. The examples we have so far, however, could also be solved in polynomial time by different classical algorithms. @S1050-2947~98!01508-X#
PACS number~s!: 03.67.Lx, 03.65.Bz, 89.80.1h, 07.05.Tp
I. INTRODUCTION
Many of the problems of interest to computation experts are, or are reducible to, decision problems. These are problems that for a given input require the determination of a yes or no answer to a specified question about the input. For example the traveling salesman problem is ~polynomial time! equivalent to the decision problem that asks whether or not for a given set of intercity distances there is a route passing through all of the cities whose length is less than a given fixed length. Another example that we will later use for concreteness in this paper is the 0-1 integer programming problem called ‘‘exact cover’’ @1#. Here we are given an m by n matrix, A, all of whose entries are either 0 or 1. The number of columns m is <n. We are asked if there exists a solution to the m equations
(
k51
n
A jkxk51 for j51,m ~1.1!
with the xk restricted to be 0 or 1. The brute force approach to this problem is to try the 2n possible choices of xW
5(x1 , . . . ,xn). For each choice of xW, checking to see if Eq. ~1.1! is satisfied takes at most of order mn operations, which
is polynomial in the input size. However, checking all 2n
possible choices for xW is prohibitively time consuming even for moderately large values of n. For the exact cover problem, with a given instance of the
input matrix A, it is not actually necessary to check all 2n
values of xW to see if Eq. ~1.1! can be satisfied. Note that generically x1 can take the values 0 or 1 and (x1 ,x2) can have the values ~0,0!, ~0,1!, ~1,0!, or ~1,1!. However, suppose that for some j the matrix A has A j15A j251. In this case
the choice x15x251 is eliminated, and no xW of the form (1,1,x3 , . . . ,xn) need be tried. If we consider xW’s that begin with x1 ,x2 , . . . ,xl then if for some j we have (k51
l Ajkxk
>2, then any xW beginning with x1 ,x2 , . . . ,xl is eliminated.
We can picture this in terms of a decision tree as follows. Before imposing any constraints we construct an underlying branching tree. This tree starts at the top with one starting node that branches to two nodes corresponding to the two choices for x1 . This then branches to the four choices for
(x1 ,x2), and so on, until we have all 2n choices for (x1 ,...,xn) at the nth level. However if we impose the constraints and see that a particular node is eliminated, then we can also eliminate all nodes connected to that node that lie below it in the tree. The decision tree is the underlying branching tree that has been trimmed as a result of the constraints. Note that the exact cover problem has a solution if and only if the decision tree has one or more nodes left at the bottom ~nth! level. More generally we view decision problems as having an underlying bifurcating branching tree with n levels as in Fig. 1. The specific form ~or instance! of the problem imposes constraints that eliminates nodes from the tree as in Fig. 2. When a node is excluded the whole branch with that node as its topmost point is also cut from the tree. The decision question we wish to answer is ‘‘are there any nodes left at the nth level after all constraints have been imposed?’’
*Electronic address: farhi@mitlns.mit.edu †Electronic address: sgutm@nuhub.neu.edu
FIG. 1. The underlying branching tree. At level m there are 2m nodes.
PHYSICAL REVIEW A VOLUME 58, NUMBER 2 AUGUST 1998
1050-2947/98/58~2!/915~14!/$15.00 PRA 58 915 © 1998 The American Physical Society


 Consider a family of decision problems indexed by a size n. Particular instances of the problem of size n give rise to particular decision trees that either have or do not have nodes at the nth level. The computational concern is how much time, or how many algorithmic steps, are required to answer the decision question as n becomes large. Roughly speaking,
if the time grows like nA for fixed A.0, the problem is
considered easy; whereas, if the time grows like an with a .1, the problem requires an ‘‘exponential amount of time’’ and is considered computationally hard.
One approach to solving a decision problem is to check systematically every path that starts at the top of the tree and moves downward through the tree. If a path reaches a dead end you try the next path ~in some list of paths! until you find a path that has a node at the nth level, or else, after having checked all paths, you discover that the answer to the decision question is ‘‘no.’’ An alternative to systematically exploring the whole tree is to move through the tree with a probabilistic rule. For example you could use the rule that if you are at a given node you move to the other nodes that are connected to it with equal probability. Thus if you are at a
node that connects to two nodes below it, you have a 1
3
chance of moving back up the tree; if the node connects to
just one below, you have a 1
2 chance of moving back up; whereas if the node is a dead end, you definitely move back. If you start at the top of the tree and move with this probabilistic rule, you will eventually visit every node in the tree. Consider a family of decision trees that are associated with underlying branching trees that are n levels deep. An individual instance of the decision tree either has or does not have nodes at the nth level. If it does have nodes at the nth level and we use a probabilistic rule for moving through the tree, then we say that the tree is penetrable if there is a good chance of reaching the nth level in not too great a time. More precisely, we define the family of trees as penetrable if
There exist A,B.0 such that for those trees with a node ~or nodes! at the nth level there is a t,nA
with the probability of being at the nth level by time t greater than ~1/n !B. ~P!
This means that in polynomial time the probability of reaching the nth level is at worst polynomially small. If condition ~P! is met, then by running the process order nB times we achieve a probability of order 1 of reaching the nth level in time nA1B. If condition ~P! is not met, this means that it either takes more than polynomial time to reach the nth level or that the probability of reaching the nth level is always smaller than (1/n) to any power. Therefore if condition ~P! is not met, instances of the trees with nodes at the nth level cannot practically be distinguished from instances with no nodes at the nth level. In this case the corresponding decision problem is not solvable in polynomial time by this algorithm. We will divide families of decision trees indexed by n into two classes, those that satisfy condition ~P! and those that do not, which we call impenetrable. We are interested in using quantum mechanics to move through decision trees. We imagine that nodes of the decision tree correspond to quantum states, which give a basis for the Hilbert space. We further imagine constructing a
Hamiltonian ˆH with nonzero off-diagonal matrix elements only between states that are connected in the corresponding decision tree. ~We will be more specific about constructing
the Hilbert space and ˆH later.! We start the quantum system in the state corresponding to the topmost node, and let it
evolve with its time evolution determined by ˆH so that the unitary time evolution operator is
ˆU~t !5exp~2iHˆ t !. ~1.2!
At any time t we have a pure state that can be expressed as a ~complex! superposition of basis states corresponding to
the nodes. Given ˆH and the initial state, the probability ~the amplitude squared! of finding the system at the nth level at time t is determined. We then say that a family of trees indexed by size n is quantum penetrable if condition ~P! is met and it is quantum impenetrable if condition ~P! is not met. In Sec. II, we will give a specific form for the quantum
Hamiltonian ˆH, and then prove that any family of trees that is classically penetrable is associated with a closely related family of trees that is quantum penetrable. This will demonstrate that our model for quantum mechanically solving decision problems is at least as powerful as the classical probabilistic method. In Sec. III, we will go further and give an example of a family of decision trees that is classically impenetrable but which is quantum mechanically penetrable. This means that the quantum penetration is exponentially faster than the corresponding classical penetration for these trees. However, we have not yet identified general characteristics of a problem that guarantee that its associated decision trees are quantum penetrable. Furthermore, for the example considered, the problem associated with the classically impenetrable trees can be reformulated so that it is computationally simple to solve by an alternative classical method.
FIG. 2. An example of a decision tree Tn with one node at level n. For aesthetic reasons we will no longer put breaks in trees—they are still to be thought of as being many levels deep.
916 EDWARD FARHI AND SAM GUTMANN PRA 58


 In Sec. IV, we discuss the construction of the Hilbert
space and the Hamiltonian ˆH. The usual paradigm for quantum computation @2# envisages a string of, say, l spin- 1
2
particles that gives rise to a 2l -dimensional Hilbert space. Each elementary operation is a unitary transformation that acts on one or two spins at a time. We will show that the Hilbert space for our system can be constructed using l
spin- 1
2 particles just as in a conventional quantum computer. Furthermore, for a large class of problems, the Hamiltonian that we construct is a sum of Hamiltonians that act on a fixed number of spins. In this sense @3#, our quantum evolution through decision trees lies in the framework of conventional quantum computation.
II. CLASSICAL VS QUANTUM EVOLUTION THROUGH TREES
In Sec. I, we discussed a classical ~that is, nonquantum! probabilistic rule for moving through decision trees. Here we are going to be more specific and state the rule in a way that
gives rise to a continuous time Markov process. The rule is simply that if you are at a given node then you move to a connected node with a probability per unit time gwhere gis a fixed, time-independent, constant. This means that in a time e where ge!1, the probability of moving to a connected node is 'ge. Using a continuous time process, as opposed to saying that you move at discrete times, will make it easier when we compare with the continuous time evolution dictated by the unitary operator in Eq. ~1.2!. We are now going to introduce some formalism that looks quantum mechanical, but we are going to apply it to describe the classical Markov process. Suppose we are given a decision tree that has N nodes. ~N may be as large as 2n11, where n is the number of levels.! Index the nodes in some way by the integers a51, . . . ,N. Corresponding to the tree we construct an N-dimensional Hilbert space that has an orthonormal basis $ua&% with a51, . . . ,N and accordingly
^aub&5dab . Now we define a Hamiltonian ˆH through its matrix elements in this basis:
^bu ˆHua&5H 2g
0
for afib if node a is connected to node b for afib if node a is not connected to node b, ~2.1!
^au ˆHua&5H 3g
2g g
node a is connected to three other nodes node a is connected to two other nodes node a is connected to one other node.
Return to the classical probabilistic rule for moving through a fixed tree, and let
pba~ t !5Prob ~ go from a to b in time t !. ~2.2!
For a time e where ge!1, we have
pba~e!5 H 2e^bu ˆHua&1O~e2! for bfia
12e^au ˆHua&1O~e2! for b5a ~2.3!
as a consequence of the definition of ˆH. For a classical Markov process, the probability of moving depends only on current position, not on history, so we have, for any t1 and t2 ,
pba~ t11t2!5 (c pbc~ t2!pca~ t1!. ~2.4!
Therefore,
pba~ t1e!5 (c pbc~e!pca~ t !, ~2.5!
which for e small gives
pba~ t1e!5 pba~ t !2e(c ^bu ˆHuc&pca~ t !1O~e2!,
~2.6!
where we have used Eq. ~2.3!. We see therefore that pba(t) obeys the differential equation
d
dt pba~ t !52 (c ^bu ˆHuc&pca~ t !, ~2.7!
with the boundary condition pba(0)5dab . The solution to Eq. ~2.7! is
pba~ t !5^bue2Hˆ tua&. ~2.8!
Again, pba(t) given by Eq. ~2.8! is the classical probability of going from a to b in time t if you move through the tree with a probability per unit time g of moving to a connecting node. As a check we should have that
(
b pba~ t !51. ~2.9!
To see that this is the case, note that ˆH defined by Eq. ~2.1! has a zero eigenvector
uE50&5 1
AN b(51
N
ub&. ~2.10!
Therefore,
PRA 58 QUANTUM COMPUTATION AND DECISION TREES 917


 (b pba~ t !5AN^E50ue2Hˆ tua&5AN^E50ua&51.
~2.11!
We have constructed the Hamiltonian ˆH because of its utility in describing a classical Markov process. We now
propose using the same Hamiltonian ˆH to evolve quantum mechanically through the tree. Let
Aba~ t !5^bue2iHˆ tua& ~2.12!
be the quantum amplitude to be found at node b at time t given that you are at node a at time 0. In this case the
probability is uAba(t)u2, with
(
b uAba~ t !u251, ~2.13!
as a consequence of the fact that ˆH is Hermitian. With this quantum Hamiltonian we will now show that if a family of trees is classically penetrable, then there is a related family of trees that is also quantum mechanically penetrable. Imagine we are given a family of decision trees $Tn% where each Tn is n levels deep and does have nodes at the nth level. For simplicity we will take the worst case possible and assume that there is only one node at level n. In order to establish our result we are going to consider another family of trees $Tn8%, where each Tn8 is obtained from Tn by appending a semi-infinite line of nodes to the starting node of Tn . The rule for classically moving on the semi-infinite line is the same as the rule for moving on the rest of the tree: with a probability per unit time g, you move to an adjoining node ~see Fig. 3!. We can see that if $Tn% is classically penetrable, so is $Tn8%. Roughly speaking, starting at 0 on Tn8 , the probability
of reaching the nth level is not appreciably reduced because of the time some paths spend on the semi-infinite line. ~We now prove this statement, but the reader who is already convinced that it is true can skip to the next paragraph.! Suppose that for $Tn% we have condition ~P!, so that
Prob ~go from 0 to n in time t !> 1
nB ~2.14!
for some gt<nA. At level 1 of the decision tree only one of the two nodes is on the branch that contains n, the unique
node at level n. Denote this level 1 node by  ̄1. Now for each path ~on Tn! that reaches n from 0 in time t there is a time t2s at which the path last jumps from 0 to  ̄1. Thus
Prob ~go from 0 to n in time t!5 E0
t
ds Prob ~go from 0 to 0 in time t2s !3gds
3Prob ~go from  ̄1 to n without hitting 0 in time s !. ~2.15!
Using Eq. ~2.14!, it follows that for some gs<gt<nA,
Prob ~go from  ̄1 to n without hitting 0 in time s !> 1
gtnB > 1
nA1B . ~2.16!
However, this last probability is the same for Tn8 as for Tn . Turning to the trees Tn8 , we see that the node 0 is connected to three other nodes, the node at level 21 on the semiinfinite tree and the two nodes at level 1. In time 1/g there is an n-independent lower bound on the probability of going
from 0 to  ̄1. Combining this fact with Eq. ~2.16!, we see that in a time s1(1/g) there is a probability of going from 0 to n on Tn8 which is greater than 1/n to a power. Thus if $Tn% is
classically penetrable so is $Tn8%.
We are now going to compare the classical and quantum evolution through the family of trees $Tn8%. From this point on we set g51. We will return to finite trees later in this section, but for now the device of appending a semi-infinite line to the trees of interest actually makes the analysis simpler. Again call the starting node ~which is at level 0 of the tree Tn8! 0, and call the unique node at the nth level n. Then
p~ t !5^nue2Hˆ tu0& ~2.17!
FIG. 3. The tree Tn8 obtained from the tree Tn of Fig. 2 by appending a semi-infinite line of nodes at the starting node of Tn .
918 EDWARD FARHI AND SAM GUTMANN PRA 58


 is the probability to go from 0 to n in time t if you evolve with the classical rule. Similarly
A~ t !5^nue2iHˆ tu0& ~2.18!
is the quantum amplitude to be at n at time t if at t50 you are at 0, and you evolve with the quantum Hamiltonian ˆH. @Of course, ˆH, p(t) and A(t), are all sequences that depend on the sequence $Tn8%, but we will not bother to place an n label on these quantities.# The Hamiltonian ˆH is defined by Eq. ~2.1! for each tree Tn8 but now the number of nodes is infinite so the Hilbert space is infinite dimensional. Call the energy eigenvectors uE&, where
ˆH u E & 5 E u E &
and
^EuE8&5d~E2E8! ~2.19!
for the continuous part of the spectrum, and
^ E r u E s & 5dr s
for the bound states. Now for any Hermitian operator ˆH,
with matrix elements Hab , any eigenvalue E of ˆH must lie @4# in the union ~over a! of the intervals
uE2Haau<b(fia uHbau ~2.20!
which, given the form ~2.1!, implies that the eigenvalues lie in the interval @0,6#. Using the completeness of the uE&’s we can write Eq. ~2.17! as
p~t!5 E0
6
dE e2Et^nuE&^Eu0&, ~2.21!
and Eq. ~2.18! as
A~t!5 E0
6
dE e2iEt^nuE&^Eu0&, ~2.22!
where the integral dE is to be interpreted as a sum on the discrete part of the spectrum. From Eq. ~2.22!, we have
1
2p E2`
`
dt8eiwt8A~t8!5 E0
6
dE d~w2E !^nuE&^Eu0&.
~2.23!
Multiply both sides by e2wt and integrate dw from 0 to ` to obtain, for t.0,
1
2p E2`
`
dt8 A~t8!
t2it8 5p~t !, ~2.24!
which could have been obtained using the Cauchy integral
formula. Now in the ua& basis ˆH is real and symmetric, and from Eq. ~2.18! it then follows that A(t)5A*(2t). This allows us to write Eq. ~2.24! as
p~t!5 1
p Re E0
`
dt8 A~t8!
t2it8 . ~2.25!
We will now use Eq. ~2.25! to show that if a family of trees $Tn8% is classically penetrable it is also quantum penetrable. Pick some time T and let e be the maximum of uA(t8)u for 0<t8<T. Now
p~t!5 1
pReH E0
T
dt8 A~t8!
t2it8 1 ET
`
dt8 A~t8!
t2it8 J
<e
p E0
T
dt8 1
~ t21t82!1/2 1 1
pU ET
`
dt8 A~t8!
t2it8U
5e
plnF ~T21t2!1/21T
t G1 1
pU ET
`
dt8 A~t8!
t2it8U.
~2.26!
The magnitude of the last integral in Eq. ~2.26! is actually
less than C/T1/4 for large T, where C is an n-independent constant. We will show this shortly. With this result we then have that
p~t!< e
plnF ~T21t2!1/21T
t G1 C
T1/4 . ~2.27!
Now we are assuming that the family of trees is classically
penetrable. This means that for some t<nA we have p(t)
.1/nB for some A and B. For large n, this penetration time t is clearly >1. Since the ln term in Eq. ~2.27! is a decreasing function of t, we have
1
nB < e
pln@~ T211 !1/21T#1 C
T1/4 . ~2.28!
Now let T5nD for D.4B. We then have, for large enough n,
1
nB < e
pln~ nD! ~2.29!
which means that the maximum of uA(t)u for t,nD is larger
than a constant times 1/nB11. Thus we have the result that if a family of trees $Tn8% is classically penetrable, it is also quantum penetrable. Before verifying that the last integral in Eq. ~2.26! is actually bounded as claimed, we need to establish some facts about the eigenfunctions of ˆH. Label the nodes on the semiinfinite line of Tn8 by j with j50,21,22, . . . , so that j50 is the starting node of Tn . On the semi-infinite line,
ˆHu j&52u j&2u j11&2u j21& for j<21. ~2.30!
The state uu& with ^ juu& proportional to eiju is an eigenstate of Eq. ~2.30! with energy
E~u!5~222 cos u!54 sin2u/2. ~2.31!
PRA 58 QUANTUM COMPUTATION AND DECISION TREES 919


 Now ei ju and e2i ju correspond to the same energy, but because of the finite branching part of the tree ~Tn , which is connected at j50!, only one linear combination is an eigenfunction of the full ˆH,
^ juu&5 1
~ 2p!1/2 @ ei ju1R~u!e2i ju#, ~2.32!
with 0<u<p, and R(u) is determined by the structure of
Tn . Because ˆH in the node basis is real, Eq. ~2.32! must be real up to an overall j-independent phase. This implies that R(u) is of the form e22id(u), that is, uR(u)u51. @The form ~2.32! is an ‘‘in’’ state for scattering off of the tree Tn at the end of the semi-infinite line. The fact that uR(u)u51 is also a consequence of the unitarity of the S matrix.# We can rewrite Eq. ~2.32! as
^ juu&5e2id~u! 2
~ 2p!1/2cos@ ju1d~u!#, ~2.33!
and then absorb the phase in the definition of uu& to obtain
^ juu&5S 2
pD 1/2
cos@ ju1d~u!#. ~2.34!
The states uu& are a set of dfunction normalized eigenstates, i.e.,
^uuu8&5d~u2u8!. ~2.35!
We have introduced the states uu& because we could ~fairly! easily normalize them, that is, pick the coefficient in Eq. ~2.32! so that Eq. ~2.35! holds. The continuous energy eigenstates uE& given by Eq. ~2.19! are proportional to the uu&’s. To maintain both Eqs. ~2.19! and ~2.35!, we have
uE&5S dE
duD 21/2
uu&5~ 4E2E2!21/4uu&, ~2.36!
where again E54 sin2u/2. In the node basis on the semiinfinite line, we then have
^juE&5S 2
pD 1/2 1
~ 4E2E2!1/4cos@ ju1d~ E !#, 0<E<4.
~2.37!
We now describe the bound-state part of the spectrum.
Return to the form of ˆH, given by Eq. ~2.30! on the semiinfinite line, and consider the eigenfunctions
^ jua&5~ 21 ! jeaj, a.0
^ jub&5ebj, b.0 ~2.38!
with energies 212 cosh a and 222 cosh b, respectively.
Since we know that the eigenvalues of the full ˆH ~including the tree! lie in @0,6#, we see that there are no bound states of the form ub& and any bound states of the form ua& have energies in the interval @4,6#. We have now fully explored the
solutions to ˆHuE&5EuE& on the runway. Any additional solutions, which may be nonzero in the tree, will vanish identically on the runway and will play no role in any of our discussion. Next we prove the required bound for the last integral in Eq. ~2.26! The trusting reader is invited to skip beyond Eq. ~2.45!. First note that
A~t8!5^nue2iHˆ t8u0&5 E0
6
dE^nuE&^Eu0&e2iEt8,
~2.39!
where the integral in the range from 4 to 6 is actually a sum. The integral in Eq. ~2.26! we wish to bound is ~after dividing by i!
E
T
`
dt8 A~t8!
t81it 5 ET
`
dt8 E0
6
dE^nuE&^Eu0&e2iEt8 1
t81it 5 ET
`
dt8 E0
6
dE^nuE&^Eu0&e2iEt8 E0
`
dme 2m~t81it!
5 E0
6
dE E0
`
dm^nuE&^Eu0&e2imte2iETe2mT 1
m1iE . ~2.40!
Taking the absolute value, we obtain
U ET
`
dt8 A~t8!
t81itU< E0
`
dm e2mT E0
6
dEz^nuE&z z^Eu0&z
~m21E2!1/2 . ~2.41!
By the Cauchy-Schwarz inequality,
U ET
`
dt8 A~t8!
t81it U< E0
`
dm e2mTF E0
6
dE8z^nuE8&z2G1/2F E0
6
dE z^Eu0&z2
m21E2 G 1/2
5 E0
`
dm e2mTF E0
4
dE z^Eu0&z2
m21E2 1 (r
z^ E r u 0 & z2
m21Er2 G 1/2 ~2.42!
using ^nun&51. For 0<E<4, the matrix element ^Eu0& is given by Eq. ~2.37! so we have z^Eu0&z2<C1 /(4E2E2)1/2 where
Ci here and below are easily computable constants. Since (rz^Eru0&z2<1, and each Er>4, we have
920 EDWARD FARHI AND SAM GUTMANN PRA 58


 U ET
`
dt8 A~t8!
t81itU<C2 E0
`
dm e2mTF E0
4 dE
~ 4E2E2!1/2~m21E2! 1 1
m2142G 1/2
. ~2.43!
The integral dE in ~2.43! is
E
0
4
dE 1
~ 4E2E2!1/2
1
m21E2 5 E0
p
du 1
m21~ 4 sin2u/2!2
< E0
p
du 1
m21~ 2/p!4u4 < C3
m3/2 .
~2.44!
Now the inequality ~2.43! becomes
U ET
`
dt A~t8!
t81itU<C2 E0
`
dm e2mTF C3
m3/2 1 1
m2 1 4 2 G 1/2
<C4 E0
`
dme2mT 1
m3/4 < C5
T1/4 , ~2.45!
which is the desired result. This was the last step we needed in showing that if $Tn8% is classically penetrable then it is quantum penetrable. Of course we are not ultimately interested in quantum evolving on the family of infinite trees $Tn8%, because we only imagine building a quantum computer with a finite number of building blocks. However, we now argue that if the family $Tn8% is quantum penetrable there is a closely related family of finite trees $Tn
f % that is also quantum penetrable. In fact Tn
f is obtained from Tn8 by chopping off the semi-infinite line at some node that is far, but not exponentially far as a function of n, from the node 0. Alternatively we can view Tn
f as arising from Tn by appending to Tn at 0 a finite number of linearly connected nodes. To understand when ‘‘infinite’’ and ‘‘very long’’ give rise to the same quantum evolution, consider an infinite line of nodes by itself with the Hamiltonian given by Eq. ~2.30!. In this case it is possible to explicitly evaluate the amplitude to go from j to k in time t:
^kue2iHˆ tu j&5e22iti~k2 j!Jk2 j~ 2t !, ~2.46!
where Jk2j is a Bessel function of integer order. For fixed t this amplitude dies rapidly if uk2 ju is larger than 2t. Imagine starting at j50 at t50. The quantum amplitude spreads out with speed 2 ~recall that we have set g51!. Chopping off the infinite system at the nodes 6L will not affect the evolution from j50 as long as L@2t. Return to the family of quantum penetrable trees $Tn8%. These trees have the property that, starting at 0, which is at the end of the semi-infinite line, there is a substantial quantum amplitude for being at the node on the nth level of the
branching tree at a time t<n ̄A for a fixed  ̄A. Lopping off the
infinite tree at a node of order (n ̄A)2 down from 0 will not
affect this result. Thus the family of finite trees $T fn%, which
are obtained from the family of classically penetrable trees $Tn% by adding a finite number of linearly connected nodes, is quantum penetrable. It is reasonable to ask why we bother with the family of infinite trees $Tn8% when we are only actually interested in finite trees. Why did we not prove directly that the family of classically penetrable trees $Tn% is also quantum penetrable? Of course the answer is we would have if we could have. The difficulty lies in the fact that for an arbitrary finite tree with an exponential number of nodes there are an exponential number of energy eigenvalues falling in a fixed interval, and we were unable to establish the requisite facts about the density of states needed for a proof. Let us summarize the results of this section. We started with a given family of trees $Tn% that was assumed to be classically penetrable. We then constructed the closely related family of trees $Tn8% that has a semi-infinite line of nodes attached to the starting node of each Tn . The trees $Tn8% are also classically penetrable. Then, using the analytic relationship between the classical probabilities and quantum amplitudes of $Tn8%, we were able to prove that $Tn8% is quantum penetrable. We also argued that cutting the semi-infinite line at some node far from 0 cannot affect the quantum penetrability as long as the distance to the cut is much greater than the quantum penetration time. Therefore the family $Tn
f % of trees that is made from $Tn% by appending a long ~but finite! string of nodes to the starting node of each Tn is quantum penetrable if the original $Tn% is classically penetrable. Clearly $Tn% and $Tn
f % address precisely the same decision question. Therefore, any problem that can be solved by classically random walking through a decision tree can be solved by quantum evolving through a very closely related tree.
III. A FAMILY OF TREES THAT IS QUANTUM, BUT NOT CLASSICALLY, PENETRABLE
If we know enough about the structure of a family of trees we can decide if it is classically penetrable and if it is quantum penetrable. Here we will show examples of families of trees that are quantum but not classically penetrable. We begin by discussing the calculations in the quantum case. As in the last section we consider a family of trees $Tn% whose members have only one node at the nth level, called n. This time we construct the family $Tn9%, where each tree Tn9 has two semi-infinite lines of nodes, one connected to the starting node of Tn , and the other semi-infinite line of nodes attached to the node n of Tn . For calculational purposes we make these two extra lines of nodes semi-infinite, but ultimately we envisage making them of length n to a power. For convenience we redraw our trees so that the direct line of nodes from 0 to n lies along the base. In this way the tree depicted in Fig. 2, with two semi-infinite lines appended, becomes that of Fig. 4. We use ‘‘bush’’ to denote a group of nodes coming out of a node on the base. Here we label the
PRA 58 QUANTUM COMPUTATION AND DECISION TREES 921


 nodes on the base by j. The nodes j521,22,23,... are on the semi-infinite starting line. The nodes j5n11,n12,... are on the appended ending line. The nodes j50, . . . ,n are all on the original tree Tn and the nodes 0, . . . ,n22 may have bushes coming out them although the nodes n21 and n do not. ~If node n21 had a bush, then n would not be the unique level n node.! What we imagine doing is building a quantum state localized near 0 on the starting line, and then calculating the quantum amplitude for penetrating the tree and being on the ending line. To this end we now set up the formalism for calculating the energy-dependent transmission coefficient T(E), and then evaluate it in certain specific cases of families of trees. For the tree depicted in Fig. 4 with an infinite base, for each energy E with 0<E<4, there are two energy eigenstates. ~Here again we have set g equal to 1!. On the semi
infinite lines they are, in the node basis, of the form eiju and
e2i ju, where again E54 sin2u/2 and 0<u<p. Superposi
tions of the eiju are used to make right-moving packets,
whereas superpositions of e2i ju make left movers. Consider the state uE,1in& that on the starting and ending lines is of the form
^ juE,1in&5N~ E !@ei ju1R~ E !e2i ju#, j521,22, . . .
~3.1!
^ juE,1in&5N~ E !T~ E !ei ju, j5n21,n,n11, . . .
with
N~E!5 1
~ 2p!1/2
1
~ 4E2E2!1/4 .
At this point we say nothing about ^auE,1in& if a is a node on Tn . Superpositions of uE,1in& make states that at early times represent right-moving packets on the starting line headed towards the tree structure Tn . At late times the packet splits into a reflected piece, proportional to R, left moving on the starting line, and a transmitted piece, proportional to T, which is right moving on the ending line. Similarly we can define uE,2in&, which represents a state left moving on the ending line at early times that at late times is split into a right mover on the ending line and a transmitted part left moving on the starting line. For uE,2in&, we have
^ juE,2in&5N~ E !@e2i ju1 ̄R~ E !ei ju#,
j5n21,n,n11, . . . , ~3.2!
^ juE,2in&5N~ E ! ̄T~ E !e2i ju, j521,22, . . . .
The states uE,1in& and uE,2in& are a complete set of scattering states useful for discussing tree penetration. Equivalently there is the set uE,1out& and uE,2out& that at late times represents respectively a right mover on the ending line and a left mover on the starting line. From Eqs. ~3.1! and ~3.2!, we obtain
uE,1in&5R~E !uE,2out&1T~E !uE,1out&, ~3.3!
uE,2in&5 ̄R~E !uE,1out&1 ̄T~E !uE,2out&.
This transformation from the out states to the in states is called the S matrix,
S5SR T
 ̄T  ̄R D ~3.4!
which is necessarily unitary, so we have
uR~ E !u21uT~ E !u251,
u ̄R~ E !u21u ̄T~ E !u251, ~3.5!
R*~E !T~E !1 ̄T*~E ! ̄R~E !50.
The standard interpretation of T(E) is as follows. Suppose we build a state uc& completely on the starting line, that is, ^auc& is nonzero only for nodes a on the starting line. Furthermore, suppose that uc& expanded as a superposition of energy eigenstates is made only of states whose energy is close to some E0 . If we quantum mechanically evolve uc&
with the unitary operator e2iHˆ t, then at late times the prob
ability of being on the ending line is uT(E0)u2. Thus uT(E)u2 has a direct interpretation as the E-dependent transmission probability through the tree. Of course any state uc& that is highly localized in energy is necessarily highly delocalized in the node basis. ~This can be viewed as a consequence of the uncertainty principle.! We do not want our constructions to rely on building states that are very spread out on the starting line since we eventually do wish to chop it off not too far from the node 0. Suppose we start at a specific node, j on the starting line, and we want the amplitude for being at node k on the ending line at time t. This is given by
Ak j~ t !5^kue2iHˆ tu j&
5 E0
4
dE$^kuE,1in&^E,1inu j&
1^kuE,2in&^E,2inu j&%e2iEt
1 (r ^kuEr&^Eru j&e2iErt
5 E0
4
dEN2~ E !$T~ E !eiku@ e2i ju1R*~ E !ei ju#
1@ e2iku1 ̄R~ E !eiku# ̄T*~ E !ei ju%e2iEt
1 (r ^kuEr&^Eru j&e2iErt ~3.6!
FIG. 4. The tree Tn9 obtained from the tree Tn of Fig. 2 by appending two semi-infinite lines, one connected at the starting node and one connected to the node n. The tree is drawn with the direct line of nodes from 0 to n along the base.
922 EDWARD FARHI AND SAM GUTMANN PRA 58


 where we have used the explicit forms for uE,6in& on the starting and ending lines, and also included possible bound states. Now using the last equation in Eq. ~3.5!, with the further fact that ˆH being real in the node basis implies T(E)5 ̄T(E), we obtain
Akj~t!5 E0
4
dE N2~ E !$T~ E !ei~k2 j!u
1T*~ E !e2i~k2 j!u%e2iEt1 (r ^kuEr&^Eru j&e2iErt.
~3.7!
In order to obtain amplitudes Akj that are large enough to ensure penetrability, we will look for trees for which T(E) is large and nonoscillatory in some interval of E’s. This guarantees that the right-hand side of Eq. ~3.7! is large enough at some relevant time. We now turn to calculating T(E), which clearly depends on the structure of the tree to which we have added the semi-infinite starting and ending lines of nodes. For each of the nodes m50,1, . . . ,n22 along the base of the tree—see Fig. 4—that has a bush sprouting up from it, let us define
ym~E !5 ^node above muE,1in&
^muE,1in& , ~3.8!
where unode above m& is the state corresponding to the node one level up from the base above the node m. Now for fixed E, ym(E) is determined solely by the bush coming out of the node m; it does not depend on the other bushes. To see this suppose that the bush coming out of node m has N nodes above the base node m. Label these nodes by a51, . . . ,N.
Now ˆHua& gives a superposition of ua& and the states connected to a. Thus
^au ˆHuE,1in&5E^auE,1in& ~3.9!
is N equations for the N11 quantities ^auE,1in& and ^muE,1in&. Divide through by ^muE,1in& and we get N equations for the N ratios ^auE,1in&/^muE,1in& so we see that Eq. ~3.8! is determined by the bush alone. Furthermore the equations that were used to determine ym(E) are all real so ym(E) is also real. For any given bush ym(E) can be calculated recursively by looking at sub-bushes and it is not actually necessary to solve the N equations ~3.9!. Let m be a node on the base with a bush coming off. Now, from Eq. ~2.1!,
^mu ˆHuE,1in&53^muE,1in&2^m11uE,1in&
2 ^ m 2 1 u E , 1 in&
2^node above muE,1in&
5E^muE,1in&, ~3.10!
which implies that
^m11uE,1in&5@32E2ym~E !#^muE,1in&
2^m21uE,1in&, ~3.11!
where we have used Eq. ~3.8!. If m has no bush coming out of it, a parallel argument gives
^m11uE,1in&5~22E !^muE,1in&2^m21uE,1in&. ~3.12!
We can use ~3.11! for nodes with bushes as well as without if we define ym(E)51 for nodes on the base with no bushes above. Equation ~3.11! can be written as a matrix equation
F
^ m 1 1 u E , 1 in&
^muE,1in& G
5F@32E2ym~E!# 21
1 0 GF ^muE,1in&
^ m 2 1 u E , 1 in& G .
~3.13!
We then have
F
^ n u E , 1 in&
^n21uE,1in&G5MF ^0uE,1in&
^21uE,1in&G, ~3.14!
where
M 5 M n21M n22 ••• M 0 ~3.15!
and
Mm5F@32E2ym~E!# 21
1 0 G. ~3.16!
Substituting the explicit form for uE,1in& from Eq. ~3.1!, we get
F
T~ E !einu
T~E!ei~n21!uG5MF 11R~E!
e2iu1R~E !eiuG. ~3.17!
If we know the matrix M , T(E) is determined by these last two equations for T(E) and R(E). From Eq. ~3.16!, we see that M is the product of matrices of determinant 1, so det(M)51. We can write
M5Fa b
c dG, ~3.18!
with ad2bc51 and a, b, c, and d all real. Solving for T(E), we obtain
T~ E !5e2inu 2i sin u
c2b1~d2a !cos u1i~d1a !sin u.
~3.19!
It is interesting to note that if for some E we have ym(E)51 for all m, then T(E)51. To see this we construct M 5M (E) in this special case. From Eqs. ~3.15! and ~3.16!, we have
M~E!5F22E 21
1 0 Gn
51
sin~u! F sin@~n11!u# 2sin~nu!
sin~nu! 2sin@~n21!u#G.
~3.20!
PRA 58 QUANTUM COMPUTATION AND DECISION TREES 923


 Plugging into Eqs. ~3.18! and ~3.19!, we obtain T(E)51. To understand why this comes about, recall that a node with no bush is the same as a node with a bush for which ym(E) 51 as far as the calculation of T(E) is concerned. Therefore, if all bushes have ym(E)51 at some E, we have unimpeded transmission at that E. To recap, given a decision tree Tn with one node at level n, construct a new tree with semi-infinite lines attached to the starting node 0 and to the node at level n. Redraw the tree as in Fig. 4 with the direct line from 0 to n along the base. Suppose we can calculate the n21 functions y0(E),y1(E), . . . ,yn22(E). Substitute into Eqs. ~3.16! and ~3.15! to obtain the matrix M as a function of E. The transmission coefficient T(E) is then given by Eq. ~3.19!, where
E54 sin2u/2. In order for a family of trees to be quantum penetrable, the function uT(E)u must be not too small over a not too small range of E, as can be seen from Eq. ~3.7!. Furthermore, even if uT(E)u is not small, T(E) must not oscillate rapidly about zero or else the integral in Eq. ~3.7! may be small due to cancellations. It is interesting to note that for any tree T(E)→1 as E→0. To see this, note that the zero
energy eigenvector of ˆH,uE50,1in&, is constant in the node basis; that is, ^auE50,1in& is independent of a. Thus ym(0) defined by Eq. ~3.8! is 1 for all nodes on the base, and by the argument of the paragraph before last we have T(0)51. For trees that are not quantum penetrable, we will see that, although T(0)51, T(E) falls to near zero at an exponentially small value of E. Consider a decision tree that is perfectly bifurcating until
level n21 and then only one of the 2n21 nodes at level n 21 continues on to level n. The associated tree Tn is shown in Fig. 5. This decision tree could arise from the following
question. You are given a list of N52n21 items with the knowledge that a single unspecified item may or may not be marked. The question is, ‘‘Is there a marked item?’’ ~This is essentially the problem for which Grover @5# found a quan
tum algorithm requiring order AN steps.! Any classical algorithm for solving this problem requires of order N steps. In particular, the Markov process for moving through the decision tree gives a probability of being at the unique node at level n that is at most of order 1/N, so this family of trees is classically impenetrable. We now turn to quantum evolution through the same set of trees. Draw the tree in Fig. 5 with the direct line from 0 to n along the base, and add semi-infinite starting and ending lines; see Fig. 6. We see that each bush coming out of the base at node m is a perfectly bifurcating bush of length n212m for m50 to n21. The ratio ym(E) can be calcu
lated for each of these bushes. Consider one such bush of length k5n212m as depicted in Fig. 7. At height l , 1
<l <k, there are 2l 21 nodes. At each height we define the normalized state
ul ;pb&5 1
~ 2l 21!1/2 (
a at height l
ua&, ~3.21!
with u0;pb& being the state at the node on the bottom of the bush, that is, u0;pb&5um&. With these labels, for these bushes ym(E) defined by Eq. ~3.8! is
ym~E !5 ^1; pbuE,1in&
^0;pbuE,1in& . ~3.22!
Note that ˆH to any power acting on u0;pb& gives a linear superposition of states that only contains the states ul ;pb& on the bush. Further note that
^l ; pbu ˆHul 8; pb&53dl l 82&@dl ,l 8111dl ,l 821#
for 1<l , l 8<k21, ~3.23!
so the bush in Fig. 7 can be replaced by the effective linear bush given in Fig. 8, where the number next to the node on the right gives the diagonal element of the Hamiltonian and the number by the connecting edge on the left gives the off-diagonal element. Up to an overall constant that drops out of Eq. ~3.22!, for l 51 to k, we have
^l ;pbuE,1in&5cos~l u81a!
and
^0;pbuE,1in&5& cos a, ~3.24!
with
E5322& cos u8.
FIG. 5. The tree Tn , which is perfectly bifurcating for the first n21 levels, and then has only one node at level n.
FIG. 6. The tree Tn9 constructed from Tn of Fig. 5 by appending two semi-infinite lines of nodes, and drawing the direct line of nodes from 0 to n along the base.
FIG. 7. A perfectly bifurcating bush of height k coming out of the base of the tree in Fig. 6 at node m5n212k.
924 PRA 58
EDWARD FARHI AND SAM GUTMANN


 By applying ˆH to the l 5k node, we can determine a,
tan~ku81a!5 cos~u8!2&
sin u8 . ~3.25!
Going back to Eq. ~3.22!, we then have
ym~E!5 1
& H & sin@~k21!u8#2sin~ku8!
& sin~ku8!2sin@~k11!u8#J , ~3.26!
where again k5n212m. Of course the calculation of ym(E) in this example was greatly facilitated by the regularity of the bush. With ym(E) determined for each bush, we can evaluate T(E) by substituting into Eqs. ~3.16! and ~3.15!, and then into Eq. ~3.19!. In Fig. 9, we show uT(E)u for n526. At the
n21 level there are 2255107.5 nodes. Although T(0)51,
T(E) has fallen substantially by E510210. Most of the area
under the curve comes from E of order 1. We can evaluate T(E) explicitly at E53. Note from Eq. ~3.24! that u8 5p/2 at E53. In this case ym(3) is 1 if k5n212m is
even, and y m(3) is 2 1
2 if k is odd. Thus M (3) can be written as ~for n even!
M~3!5HF 1
2 21
1 0 GF21 21
1 0 GJ n/2
5~21!n/2F 3
2
1 2
1 1Gn/2
5~21!n/2F 1 2 1
3
12
3 GF2n/2 0
0 22n/2GF 2
3
1 3
21 1G, ~3.27!
from which we conclude that T(3);22n/2. The transmission
amplitude is of order 22n/2, so the transmission probability
goes like 22n. Here the quantum algorithm is doing no better than the classical algorithm. The alert reader may wonder whether any use can be made of the bound states which may exist for 4<E<6. The answer is no, at least in this case. To check this, we changed the Hamiltonian on the semi-infinite lines to have values 3 on the diagonal and 2 3
2 between neighbors. Now the continuum states uE,6in& are defined for 0<E<6, and are complete. We recalculated T(E) and looked for intervals of E’s where T(E) is large and nonoscillatory. Again, there are no values of T(E) which permit transmission with probabil
ity greater than ;22n. Now we make a seemingly small modification of the tree. We take all of the odd-height bushes coming out of the base line of Fig. 6, and trim back one layer so all bushes are of even height. The magnitude of the transmission coefficient is shown in Fig. 10, where we see that for a substantial range of E near 3, uT(E)u is very close to 1. In fact for all of these bushes, ym(3)51, which by the argument given above implies that T(3)51. We can also see that T(E) does not oscillate rapidly in this region by plotting the real part of T(E), which is shown in Fig. 11, confirming a more tedious analytic evaluation. Therefore, the family of trees is quantum penetrable.
FIG. 8. The effective bush of height k associated with the bush of Fig. 7. The number to the left of each edge gives the matrix element of Hˆ between the two states connected by the edge. The number next to the node gives the diagonal element of Hˆ for that state.
FIG. 9. The magnitude of T vs E for E between 0 and 4 for the perfectly bifurcating tree with one node at n526.
FIG. 10. The magnitude of T vs E for the same tree used in Fig. 9 after removing one layer of nodes from each odd-length bush.
PRA 58 QUANTUM COMPUTATION AND DECISION TREES 925


 It is easy to see that these trees with even-height bushes are not classically penetrable. Before trimming back the oddheight bushes, we had the n-level tree shown in Fig. 5, Tn , which is associated with the tree Tn9 shown in Fig. 6. These trees are not classically penetrable. Now, if we trim the oddheight bushes back one layer, the trimmed tree still contains all of the tree Tn21
9 , which has even- and odd-height bushes. Since Tn21
9 is not classically penetrable, the even-height bush family is also not classically penetrable, since, classically, any time you add nodes to bushes, you necessarily decrease the chances of getting to the node n. We have given a single example of a family of trees that is not classically penetrable but is quantum penetrable. Clearly there are many variants of this example using evenlength, perfectly bifurcating bushes in all sorts of combinations; we will not pursue these other examples here. However, we are faced with the question of what problem this family of trees corresponds to. We can think of decision trees as associated with functions that impose constraints. At each level i there is a function f i that depends on the first i bits. If f i(x1 ̄xi)51 then the ith-level node x1 ̄xi is connected to the (i21)th-level node x1 ̄xi21 . ~The zeroth-level node needs no bits to describe it.! If f i(x1 ̄xi)50, then x1 ̄xi is absent from the tree. In terms of the functions f i , the decision question is, ‘‘Is there an x1 ̄xn such that f i(x1 ̄xi)51 for all i51 to n ? ’’ For the tree depicted in Fig. 5, the functions f 1 , . . . , f n21 are all identically 1. This gives the perfectly bifurcating structure. Then there is a function f n(x1 ̄xn) that is guar
anteed to be 0 for all but one of the 2n values of x1 ̄xn . At one special, but unknown, value f n is either 0 or 1. ~We draw the decision tree assuming there is a value for which f n equals 1. Otherwise the transmission coefficient is 0 and there is nothing to calculate.! Without further information
about f n , any classical algorithm will need to search 2n values of x1 ̄xn to see if there is a value at which f n equals 1. Let us turn to the functions that determine the quantum penetrable tree just discussed. At the nth level there is the function f n(x1 ̄xn) which may take the value 1 on one
input, say w1 ̄wn . To arrange for the bushes to all have even height, the tree must be trimmed at level n21. For n even, the function f n21(x1 ̄xn21) is 0 if x1fiw1 or if x1 5w1 , x25w2 , and x3fiw3 or if x15w1 , x25w2 , x3 5w3 , x45w4 , and x5fiw5 , etc. If we are allowed to call the function f n21(x1 ̄xn21), which we know has this much structure, we can determine w1 ̄wn21 with far fewer than
order 2n function calls. First try various inputs until you find an example x1 ̄xn21 such that f n21 is 1 on this input. Then you know that w15x1 . Trying inputs of the form w1x2 ̄xn21 will allow you to find w2 , etc. Once w1 ̄wn21 is determined, two function evaluations of f n(w1 ̄wn21xn) with xn50 and 1 will answer the decision question. Of course what is occurring here is that the extreme regularity of the tree, which guarantees its quantum penetrability, is also structuring the decision problem so that it can be answered much more efficiently than by a classical random walk which is incapable of seeing larger structures.
IV. IMPLEMENTING THE QUANTUM SYSTEM
In this section, we show how to implement on a conventional quantum computer the quantum systems previously described. A conventional quantum computer consists of l
spin- 1
2 particles that give rise to a 2l dimensional complex Hilbert space with basis elements uz1z2 ̄zl & where we take each zi to be 0 or 1. The computer program can be thought of as a sequence of unitary operators ˆUa each of which acts on
~at most! B bits. That is, for each ˆUa in the sequence, there is a set Sa5$i1 ,i2 , . . . ,iB% that tells us which B bits are
being acted on and a 2B by 2B unitary matrix whose elements we write as Ua(w18 ̄w8B ;w1 ̄wB). We then have, for each ˆUa,
^z18z28 ̄zl8 u ˆUauz1z2 ̄zl &
5 jπ)Sa
I~ z j5z j8!Ua~ zi81 ̄zi8B ;zi1 ̄ziB!. ~4.1!
Here I(s) is the indicator function that is 1 if s is true and 0
if s is false. This formula is just a way of writing that ˆUa acts on B bits. In previous sections we described evolution through decision trees using the quantum Hamiltonian ˆH that gives rise to
the unitary time evolution operator e2itHˆ . To find a sequence of unitary operators, each of which acts on only several bits and whose product gives ~approximately! the same evolution
as e2itHˆ , we follow the procedure given in Ref. @3#. Suppose
ˆH 5 k(5 1
p
ˆHk ~4.2!
where, for each k, ˆHk and hence e2itHˆ k acts only on ~at most! B bits. The Trotter formula says
e 2itHˆ '@ e 2itHˆ 1 /me 2itHˆ 2 /m• • • e 2itHˆ p /m#m ~4.3!
for t/m small. Thus the evolution operator e2itHˆ can be approximated as a product of pm unitary operators each of
FIG. 11. The real part of T vs E showing that T does not oscillate rapidly about zero close to where T is 1, for the same tree as Fig. 10.
926 EDWARD FARHI AND SAM GUTMANN PRA 58


 which acts on a fixed number of bits. As a function of n the
largest times t that interest us are, say, nA. Taking m5n2A
allows us to obtain e2itHˆ with a number of elementary unitary operators that only grows polynomially with n, as long as p also grows only polynomially with n. We now show two cases where the Hamiltonian ˆH given
by Eq. ~2.1! can be written as a sum of ˆHk where each ˆHk acts on a fixed number of bits. Consider first the underlying
branching tree, Fig. 1 and its associated ˆH. Start with l 52n11 bits that we group for convenience as
~ y x !5~ y 0y 1 ̄y nx1 ̄xn!. ~4.4!
The y bits indicate the level of the node. The states we use will have a single yi51 and the rest 0 to indicate that the node is at level i. The x1 ̄xi will indicate the particular node at the ith level; these nodes will also have xi115xi12 5 ̄5xn50. We now define the following one bit operators through their action on the basis vectors uyx&:
yˆ juyx&5y juyx&,
ˆx juyx&5x juyx&, ~4.5!
ˆrjuy x&5 ˆrjuy 0 ̄y j ̄y nx&5 ̄y juy 0 ̄ ̄y j ̄y nx&,
ˆsjuy x&5 ˆsjuy x1 ̄x j ̄xn&5 ̄x juy x1 ̄ ̄x j ̄xn&,
where  ̄y j512y j and  ̄x j512x j . We see that ˆx j and yˆ j are diagonal in this basis. The operator ˆri
† ˆri11 acting on a state at level i brings it to level i11, whereas ˆri ˆri11
† moves from level i11 to level i. The Hamiltonian ~2.1!, defined on the underlying branching tree, is
ˆH52yˆ 013 i5 (1
n21
yˆ i1yˆ n2 i5 (0
n21
~ ˆri
† ˆri111 ˆri ˆri11
† !~ 12 ˆxi11!
2 i5 (0
n21
~ ˆri
† ˆri11 ˆsi111 ˆri ˆri11
† ˆsi11
† !. ~4.6!
The first three terms give the diagonal matrix elements. The fourth term connects the nodes x1 ̄xi at level i with the nodes x1 ̄xi0 at level i11, whereas the last term connects x1 ̄xi at level i with x1 ̄xi1 at level i11. Thus we see that
ˆH can be written as a sum of ˆHk , each of which acts on at most three bits.
We have built a Hilbert space with 22n11 states, whereas
the underlying branching tree has only 2n1121 nodes. However, if we start in the state corresponding to the topmost node, that is, y051 and all other bits 0, then if we act with
e2iHˆ t with ˆH given by Eq. ~4.6! we only ever reach states in the subspace corresponding to the underlying branching tree.
The 22n11-dimensional Hilbert space may not be the most economical choice to describe the tree, but it suffices for our
purpose of showing that ˆH can be built as a sum of local Hamiltonians.
Of course we also want to construct ˆH as a sum of Hamiltonians acting on a fixed number of bits for interesting
trimmed decision trees. There are families of trimmed trees whose Hamiltonians we cannot represent in this way. But for
many interesting problems we can write ˆH as a sum of Hamiltonians that act on at most B bits, where B does not grow with n. For example, we now show how to do this for a version of the exact cover problem discussed in Sec. I. We restrict the matrix A, which defines an instance of the exact cover problem, to have exactly three 1’s in any row and three or fewer 1’s in any column. Even with this restriction, the problem is N P complete. Consider first the question of whether the ith-level node x1 ̄xi connects to the (i11)th level node x1 ̄xi1. We assume that x1 ̄xi is in the tree, and we need to be consistent with Eq. ~1.1!, so we know that for each j, (k51
i A jkxk is 0 or 1. If for some j this sum is 1 and also A j,i1151, then x1 ̄xi1 is eliminated as a node. Consider the function
Ci1~ x1 ̄xi!5 j5 )1
m H F12k(51
i
AjkxkGAj,i111@12Aj,i11#J .
~4.7!
Given that x1 ̄xi is an allowed node, then this function is 1 if x1 ̄xi1 is allowed and 0 if x1 ̄xi1 is excluded. Furthermore, given the restriction that A has three 1’s in any row and three or fewer in any column, Ci
1 has at most six xk’s appearing. Now we ask if x1 ̄xi at level i connects to x1 ̄xi0 at level i11. This connection will be allowed unless for some j with A j,i1151, there is a k<i and a distinct k8<i such that A jk5A jk851 and xk5xk850. The reason the node x1 ̄xi0
would be eliminated in this case is that there are exactly three 1’s in any row, and Eq. ~1.1! could not be satisfied if the three bits xk , xk8 , and xi11 are all 0. Now consider the
function
di
j~ x1 ̄xi!5k(51
i
A jk~ 12xk!. ~4.8!
For any j with A j,i1151, di
j can be 0, 1, or 2. Only if di
j(x1 ̄xi)52 is x1 ̄xi0 eliminated. Let
Ci0~ x1 ̄xi!5 j5 )1
m HF1
2 dij~ 12dij!11G A j,i111~12A j,i11!J .
~4.9!
Then this function is 0 if x1 ̄xi0 excluded, and it is 1 if x1 ̄xi0 is allowed. Again because of the restrictions placed on A, this function has only six xk’s appearing.
The functions Ci0 and Ci1 can be promoted to operators simply by replacing their arguments by the bit operators ˆxk defined in Eq. ~4.5!; that is, we have Ci0( ˆx1 ̄ ˆxi) and Ci1( ˆx1 ̄ ˆxi). If we multiply the last term in Eq. ~4.6! by Ci1
and the fourth term by Ci0 , the Hamiltonian has off-diagonal elements only where the tree has connections. Similarly, we can write the diagonal term as
ˆHdiagonal52 yˆ 01 i5 (1
n21
yˆ i~ 11Ci01Ci1!1yˆ n . ~4.10!
PRA 58 QUANTUM COMPUTATION AND DECISION TREES 927


 Thus we have written the Hamiltonian for the trees trimmed by A in the form ~4.2! with B59. Generally, we think of decision trees as associated with functions f i that impose constraints: f i(x1 ̄xi)51 if the (i21)th level node x1 ̄xi21 is connected to the ith level node x1 ̄xi ; otherwise f i50. The exact cover example above makes clear that as long as there is a fixed B such that f i(x1 ̄xi) depends on only B bits for each i ~which bits can vary with i, of course! then the problem can be implemented within the usual quantum computing paradigm—we only need to replace Cix21( ˆx1 ̄ ˆxi21) in Eq. ~4.10! by f i( ˆx1 ̄ ˆxi21 ,x), and also to multiply the appropriate connec
tion terms in Eq. ~4.6! by f i( ˆx1 ̄ ˆxi21 ,x). Note that our example in Sec. III for which the quantum algorithm achieved exponential speed-up does not meet this fixed-B requirement. We do have, however, similar examples that achieve exponential speed-up and that do meet this requirement. These problems also rely on even-length, very structured bushes, and also can be solved quickly by other classical algorithms.
V. CONCLUSIONS
There is great interest in devising quantum algorithms that improve on classical algorithms, and there have been some notable successes. For example, the well-known Shor @6# and Grover @5# algorithms demonstrate remarkable ingenuity. Each uses quantum interference, the necessary ingredient for quantum speed-up, in what appears to be a problem-specific way. So far these methods have not been successfully applied to problems very different from the ones for which they were originally devised. In this paper, we have considered a single time-independent Hamiltonian that evolves a quantum state through the
nodes of a decision tree. ~For a related approach, see Ref. @7#.! This is in contrast to the usual setup consisting of a sequence of unitary operators each acting on a fixed number of bits. ~For many problems, including N P-complete ones, our algorithm can be rewritten in the conventional language of quantum computation.! Studying Hamiltonian evolution on decision trees is facilitated by the technique of calculating energy-dependent transmission coefficients. The example in Sec. III shows explicitly how interference allows a class of trees to be penetrated exponentially faster by quantum evolution than by a classical random walk. However, this example can be quickly solved by a different classical algorithm. The particular Hamiltonian we chose allowed us to prove, in Sec. II, that the quantum algorithm succeeded in polynomial time whenever the corresponding classical random walk on the decision trees succeeded in polynomial time. In searching for more examples where the quantum algorithm outperforms the classical algorithm, one is not restricted to this Hamiltonian. We can imagine trying any Hamiltonian with nonzero off-diagonal elements where there are links between the nodes on the decision tree. With this flexibility, we hope that the class of trees that can be penetrated quickly by the quantum algorithm is large enough to include classically difficult problems.
ACKNOWLEDGMENTS
We thank Francis Low and Mike Sipser for their help and insight. We also thank Rachel Cohen and Cindy Lewis for their LATEX assistance, and Martin Stock for creating Figs. 1–8 and for the final formatting. This work was supported in part by the U.S. Department of Energy under Contract No. DE-FC02-94ER40818.
@1# D. S. Johnson and C. H. Papadimitriou, in The Traveling Salesman Problem, edited by E. L. Lawler, J. K. Lenstra, A. H. G. Rinnooy Kan, and D. B. Shmoys ~Wiley, New York, 1985!, p. 37. @2# A. Barenco, C. H. Bennett, R. Cleve, D. P. DiVincenzo, N. Margolus, P. Shor, T. Sleator, J. A. Smolin, and H. Weinfurter, Phys. Rev. A 52, 3457 ~1995!, and references therein. @3# S. Lloyd, Science 273, 1073 ~1996!. @4# This is known as Gerschgorin’s theorem; c.f. C. G. Cullen,
Matrices and Linear Transformations, 2nd ed. ~AddisonWesley, Reading, MA, 1972!, p. 283.
@5# L. K. Grover, in Proceedings of the 28th Annual ACM Symposium on the Theory of Computing (STOC), Philadelphia, 1996 ~ACM Press, New York, 1996!, pp. 212–218; e-print quant-ph/9605043. @6# P. W. Shor, e-print quant-ph/9508027. @7# T. Hogg, e-print quant-ph/970113.
928 EDWARD FARHI AND SAM GUTMANN PRA 58
