# Exponential Quantum Speedup in Simulating Coupled Classical Oscillators - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevX.13.041041
> Collected: 2026-09-20
> Published: 2023-12-04
> Zotero parent key: FNYHLMCU
> Evidence: Zotero indexed PDF text

Exponential Quantum Speedup in Simulating Coupled Classical Oscillators
Ryan Babbush ,1,* Dominic W. Berry ,2 Robin Kothari ,1 Rolando D. Somma ,1 and Nathan Wiebe3,4,5 1Google Quantum AI, Venice, California, USA 2School of Mathematical and Physical Sciences, Macquarie University, Sydney, New South Wales, Australia 3Department of Computer Science, University of Toronto, Toronto, Ontario, Canada 4Pacific Northwest National Laboratory, Richland, Washington, USA 5Canadian Institute for Advanced Research, Toronto, Ontario, Canada
(Received 20 April 2023; revised 29 August 2023; accepted 9 October 2023; published 4 December 2023)
We present a quantum algorithm for simulating the classical dynamics of 2n coupled oscillators (e.g., 2n masses coupled by springs). Our approach leverages a mapping between the Schrödinger equation and Newton’s equation for harmonic potentials such that the amplitudes of the evolved quantum state encode the momenta and displacements of the classical oscillators. When individual masses and spring constants can be efficiently queried, and when the initial state can be efficiently prepared, the complexity of our quantum algorithm is polynomial in n, almost linear in the evolution time, and sublinear in the sparsity. As an example application, we apply our quantum algorithm to efficiently estimate the kinetic energy of an oscillator at any time. We show that any classical algorithm solving this same problem is inefficient and must make 2ΩðnÞ queries to the oracle, and when the oracles are instantiated by efficient quantum circuits, the problem is bounded-error quantum polynomial time complete. Thus, our approach solves a potentially practical application with an exponential speedup over classical computers. Finally, we show that under similar conditions our approach can efficiently simulate more general classical harmonic systems with 2n modes.
DOI: 10.1103/PhysRevX.13.041041 Subject Areas: Quantum Information
I. INTRODUCTION
The efficient simulation of quantum dynamics is among the most promising areas of quantum computing [1]. This is due to having practical applications as well as universality providing strong complexity theoretic evidence for exponential quantum advantage [2,3]. Several other applications with similarly favorable qualities are known (e.g., factoring [4]), but the discovery of more compelling use cases remains critical for understanding and motivating the value proposition of quantum computers. One approach for leveraging the power of Hamiltonian simulation would be to consider the space of problems that reduces to it. Hamiltonian dynamics is an example of a homogeneous, first-order partial differential equation that gives rise to unitary evolutions. Thus, it is natural to explore whether other differential equations can be mapped to Hamiltonian simulation. The goal would be a more natural (albeit perhaps more narrow) alternative to solving differential equations compared with methods [5–7] leveraging
quantum linear systems algorithms [8–10]. Past work has sought to develop Hamiltonian simulation approaches for a limited set of other differential equations but thus far has only succeeded in obtaining polynomial speedups [11–13]. In this paper, we discuss a rich set of problems in classical dynamics that can be mapped to Hamiltonian simulation and solved with exponential quantum advantage. As a prominent example, our approach can simulate the dynamics of exponentially many coupled classical oscillators in polynomial time. Such systems describe a variety of physical phenomena including networks of masses and springs [14], circuits with capacitors and inductors [15], models of neuron activity [16], and vibrations in molecules [17], materials, and mechanical structures. More generally, the harmonic approximation (defined by a quadratic potential) arises as the first-order correction to equilibrium in bound systems. That the dynamics of coupled classical oscillators can be studied via Hamiltonian simulation is perhaps not too surprising. Solutions to the Schrödinger equation contain oscillatory terms and interference, and we are effectively using these properties to simulate the same phenomena in the classical system. This correspondence was also presaged by the finding that Grover search can be implemented (in the absence of errors) using mechanical wave interference [18]. Similarly, the problem of simulating the
*Corresponding author: ryanbabbush@gmail.com
Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article’s title, journal citation, and DOI.
PHYSICAL REVIEW X 13, 041041 (2023)
2160-3308=23=13(4)=041041(34) 041041-1 Published by the American Physical Society


 (discrete) classical wave equation is a special case of the oscillator dynamics problem considered here, and a quantum algorithm to solve the classical wave equation via Hamiltonian simulation has been studied in Ref. [11]. However, despite the seemingly natural connection, our mapping involves a number of subtle technical features, and modern quantum algorithms are required to efficiently simulate the resultant Hamiltonians. Besides providing a classical-to-quantum reduction, another key to obtain exponential quantum advantage for this problem is the way we encode physical quantities in quantum states. In our case, this encoding is motivated by energy conservation (being different from the one in Ref. [11]). Specifically, we encode quantities related to the displacements and momenta of the classical system in the amplitudes of a quantum state. Thus, extracting the full configuration of the classical system would scale polynomially in the Hilbert space dimension, precluding a large quantum speedup. Nevertheless, interesting global properties, like estimating the kinetic or potential energies at any time, can still be computed efficiently. Likewise, our methods only provide an exponential speedup for the dynamics of sparsely coupled oscillator networks when masses, spring constants, and initial states can be efficiently computed. Fortunately, many interesting systems meet those conditions. Finally, we provide strong evidence that such simulations cannot also be performed efficiently on a classical computer. In particular, we are able to show that estimating the kinetic energy of simple instances of these systems at any time that is polyðnÞ requires 2ΩðnÞ queries to the oracles in the worst case and, when the oracles are instantiated by quantum circuits of polyðnÞ size, the problem is bounded-error quantum polynomial time BQP-complete. Thus, all problems efficiently solved by a quantum computer can be reduced to an instance of simulating exponentially many coupled classical oscillators, which can also be solved efficiently by our approach. The rest of the paper is organized as follows. In Sec. II we describe classical systems of oscillators, define the associated simulation problems of interest, and state our main results. In Sec. III we show how these problems reduce to instances of Hamiltonian simulation, giving rise to an efficient quantum algorithm. We discuss some applications of this algorithm in Sec. V, emphasizing the problem of estimating the time-dependent kinetic (or potential) energies of the oscillators. In Sec. VI A we show the exponential lower bound for classical algorithms for this problem in the oracle setting, and in Sec. VI B we show that this problem is BQP-complete when the oracles can be accessed via efficient quantum circuits. Finally, in Sec. VII we generalize our approach to efficiently simulating classical systems under the harmonic approximation. Detailed proofs of our claims are provided in the Appendixes. We also provide a comparison of our results
with those of related work on quantum algorithms for differential equations in Appendix G.
II. SIMULATING COUPLED OSCILLATORS: MAIN RESULTS
We consider a classical system of coupled harmonic oscillators, i.e., N 1⁄4 2n point (positive) masses m1; ...; mN that are coupled with each other by springs. At any time t ≥ 0, the displacements (with respect to their rest position) and velocities of the masses are given by ⃗xðtÞ1⁄4 (x1ðtÞ;...;xNðtÞ)T ∈RN and ⃗x ̇ðtÞ1⁄4( ̇x1ðtÞ;...;x ̇NðtÞ)T ∈RN, respectively, where  ̇aðtÞ 1⁄4 ðd=dtÞaðtÞ and ̈aðtÞ 1⁄4 ðd2=dt2ÞaðtÞ. We let κjk 1⁄4 κkj ≥ 0 be the spring constants that couple the jth and kth oscillator, and κjj ≥ 0 is the spring constant that connects the jth oscillator to a “wall.” We have described it for dimension D 1⁄4 1 for simplicity, i.e., we assigned one coordinate to each oscillator, but the same formulation holds for arbitrary dimension D by using D coordinates to represent the position of a single oscillator (see Fig. 1 for an example). In the harmonic approximation, the dynamics of the oscillators can be determined from the initial values ⃗xð0Þ and ⃗ ̇xð0Þ and Newton’s equation (for all j ∈ 1⁄2N ≔ f1; ...; Ng):
mj̈xjðtÞ 1⁄4 X
k≠j
κjk(xkðtÞ − xjðtÞ) − κjjxjðtÞ: ð1Þ
In matrix form, this is M̈⃗xðtÞ 1⁄4 −F⃗xðtÞ, where M is a N × N diagonal matrix with entries mj > 0 and F is the N × N matrix whose diagonal and off-diagonal entries are fjj 1⁄4
P
k κjk and fjk 1⁄4 −κjk, respectively. (Observe that F is the discrete Laplacian of a weighted graph.) Solutions to Eq. (1) are well understood and can be expressed in terms of normal modes [14], which is essentially a way of describing the system as N uncoupled harmonic oscillators in a different basis. Classical algorithms that compute ⃗xðtÞ and ⃗ ̇xðtÞ have
FIG. 1. An example system of N=2 oscillators in D 1⁄4 2 dimensions. We use x1ðtÞ for the first coordinate of the first mass and x2ðtÞ for the second coordinate of the first mass, and so on. Since the first and second mass now correspond to the same original mass, m1 1⁄4 m2.
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-2


 complexity polyðNÞ or, equivalently, expðnÞ. [In this paper we use expðmÞ, polyðmÞ, and polylogðmÞ to mean Oðk
m
Þ, Oðm
k
Þ, and Oðlog
k
mÞ, respectively, for some constant k. We use “log” to mean logarithm to base 2.] Our goal is to provide a quantum algorithm for simulating the dynamics of the classical oscillators efficiently, in time polyðnÞ. Doing so requires a particular notion of “simulation,” since any algorithm that outputs the full vectors
⃗
xðtÞ or
 ̇
⃗
xðtÞ would necessarily have complexity at least linear in N. Specifically, we consider a problem formulation where the output is a quantum state with some amplitudes proportional to
ffiffiffiffiffiffi
m
j
p
 ̇
x
j
ðtÞ and others to
ffiffiffiffiffiffi
κ
jk
p
(x
j
ðtÞ − x
k
ðtÞ) or
ffiffiffiffiffiffi
κ
jj
p
x
j
ðtÞ, and the input masses and spring constants are provided through oracles in the usual way; see Appendix A. (Here and throughout this paper,
ffiffiffi
x
p
is the principal square root of x ≥ 0 and
ffiffiffiffi
X
p
is the principal square root of a positive semidefinite matrix X ≽ 0.) The formal problem is as follows: Problem 1. Let K be the N × N symmetric matrix of spring constants κ
jk
≥ 0 and assume it is d-sparse (i.e., there are at most d nonzero entries in each row). Let M be the N × N diagonal matrix of masses m
j
> 0 and define the normalized state
jψðtÞi ≔
1
ffiffiffiffiffiffi
2E
p
ffiffiffiffiffi
M
p
 ̇
⃗
xðtÞ
i⃗μðtÞ
; ð2Þ
where E>0 is a constant, and ⃗μðtÞ∈R
M
[M ≔ NðN þ 1Þ=2] is a vector with N entries
ffiffiffiffiffiffi
κ
jj
p
x
j
ðtÞ and NðN − 1Þ=2 entries
ffiffiffiffiffiffi
κ
jk
p
(x
j
ðtÞ − x
k
ðtÞ), with k > j. Assume we are given oracle access to K and M, and oracle access to a unitary W that prepares the initial state, i.e., Wj0i ↦ jψð0Þi. Given t ≥ 0 and ε > 0, the goal is to output a state that is ε-close to jψðtÞi in Euclidean norm. Our main result is a quantum algorithm that prepares jψðtÞi efficiently. Theorem 1. Problem 1 can be solved with a quantum algorithm that makes Q 1⁄4 O(τ þ logð1=εÞ) queries to the oracles for K and M, uses
G1⁄4O
(
Q × log
2
Nτ ε
m
max
m
min
)
ð3Þ
2-qubit gates, and uses W once, where τ ≔ t
ffiffiffiffiffiffi
d א
p
≥ 1, ≔ κ א
max
=m
min
,m
max
≥m
j
≥m
min
> 0, and κ
max
≥κ
jk
for all j; k ∈ 1⁄2N are known quantities. In the O notation above, the asymptotically large parameters are N, τ, 1=ε, and m
max
=m
min
. This complexity has explicit dependence on n 1⁄4 logðNÞ that is polynomial. If τ, logð1=εÞ, and logðm
max
=m
min
Þ are polyðnÞ, and all oracles (including W) can be performed with cost polyðnÞ, then the entire algorithm has complexity polyðnÞ. An interesting feature of this complexity is that it scales as the square root of the sparsity d, whereas Hamiltonian
simulation complexities are usually linear in d. The complexity is also linear in τ, which bounds the maximum number of oscillations of the normal modes after time t. Our algorithm can be used to determine properties of the system at time t. For example, the state jψðtÞi encodes the velocities and displacements of the oscillators in a way that makes it easy for the estimation of the kinetic or potential energies, as we discuss below. We discuss in Appendix F that other encodings are also possible, and the choice of encoding may determine which initial states and properties (observables) are efficient to prepare and measure. Nevertheless, our main goal is to establish results for this particular encoding. The constant in Eq. (2) is E 1⁄4 KðtÞ þ UðtÞ, where KðtÞ 1⁄4
1 2
 ̇
⃗
xðtÞ
T
M
 ̇
⃗
xðtÞ is the kinetic energy, i.e.,
KðtÞ 1⁄4
1 2
X
j
m
j
 ̇
x
j
ðtÞ
2
; ð4Þ
and UðtÞ 1⁄4
1 2
⃗μðtÞ
T
⃗μðtÞ is the potential energy, i.e.,
UðtÞ 1⁄4
1 2
X
j
κ
jj
x
j
ðtÞ
2
þ
X
k>j
κ
jk
(x
j
ðtÞ − x
k
ðtÞ)
2
: ð5Þ
Hence, E is the total energy of the system, which is time independent as the system is closed. The support of jψðtÞi on the subspace spanned by the first N basis vectors is KðtÞ=E, which can be estimated via a simple measurement on jψðtÞi; see Sec. V. The support on the other subspace is UðtÞ=E. As an example of the type of problem that can be solved by preparing jψðtÞi, consider the following. Problem 2. Given the same inputs as Problem 1 and an oracle for V ⊆ 1⁄2N , which is a subset of the oscillators, output an estimate
ˆ
k
V
ðtÞ ∈ R such that
j
ˆ
k
V
ðtÞ − K
V
ðtÞ=Ej ≤ ε; ð6Þ
where K
V
ðtÞ ≔
1 2
P
j∈V
m
j
 ̇
x
j
ðtÞ
2
is the kinetic energy of V at time t. In Sec. V, we prove that our quantum algorithm solves this problem with high probability with Oð1=εÞ uses of the quantum algorithm from Theorem. 1. We also show a related result for the estimation of the potential energy stored on a subset V ⊆ 1⁄2N × 1⁄2N of springs at time t. Problems 1 and 2 are formulated using a specific input and output format, and one might wonder if a classical algorithm could also solve these problems efficiently. The answer is no: we show that any classical algorithm solving Problem 2 must make polyðNÞ or expðnÞ queries to the oracles in general. Theorem 2. Any classical algorithm that solves Problem 2 with high probability must make 2
ΩðnÞ
queries to the oracle for K. This lower bound holds even if we further require that all m
j
1⁄4 1, all κ
jk
∈ f0; 1g, d ≤ 3, and the
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-3


 initial state is jψð0Þi 1⁄4 j0i⊗q for some q 1⁄4 polyðnÞ, which corresponds to ⃗xð0Þ1⁄4ð0;0;...;0ÞT and ⃗x ̇ð0Þ 1⁄4 ð1;0;...;0ÞT. To provide more evidence of the impossibility of efficient classical simulations and prove a stronger hardness result, we define a nonoracular version of Problem 2 and show that it is BQP-complete. Thus, no classical algorithm can solve this nonoracular problem efficiently [in time polyðnÞ unless it can also solve every problem solved by quantum computers in polynomial time. The same observation essentially applies to Problem 2 as a result. Formally, to be BQP-complete a problem must be a decision problem (i.e., a problem where there are only two possible answers), so we define a decision version of Problem 2 with jVj 1⁄4 1 and a sparse initial state. Problem 3. The setup is as in Problem 2, but we are given efficient quantum circuits [i.e., circuits with polyðnÞ gates] to implement the oracles for K and M, an explicit description of jψð0Þi, which is required to have a constant number of nonzero entries, and a label v ∈ 1⁄2N of a single oscillator. We additionally require that τ, 1=ε, and mmax=mmin are bounded by polyðnÞ. The problem is to decide if KvðtÞ=E, the kinetic energy of oscillator v as a fraction of total energy, is at least 1=polyðnÞ or at most
1= expðpffinffiffiÞ, promised that one of these holds. Note that this problem has an input of size polyðnÞ and our algorithm for Problem 1 will solve this on a quantum computer in time polyðnÞ. We then show this problem is BQP-complete in Sec. VI B. Theorem 3. Problem 3 is BQP-complete. The problem remains BQP-complete even if we further require that all κjk ≤ 4, mj 1⁄4 1, d ≤ 4, and the initial state is jψð0Þi 1⁄4 j0i⊗q ⊗ j−i for some q 1⁄4 polyðnÞ, which corresponds to ⃗xð0Þ 1⁄4 ð0; 0; ...; 0ÞT and ⃗ ̇xð0Þ 1⁄4 ðþ1; −1; 0; ...; 0ÞT.
Finally, we show that our results can be extended to address more general classical systems that arise naturally under the harmonic approximation [14]. In these cases, for example, the matrix M resulting from Eq. (1) is not necessarily diagonal and the off-diagonal entries of F are not necessarily nonpositive. A simple change of variables takes Eq. (1) to the standard form ̈⃗yðtÞ 1⁄4 −A⃗yðtÞ, where
⃗yðtÞ 1⁄4 pffiffiMffiffiffi⃗qðtÞ, and ⃗qðtÞ ∈ RN are the generalized displacements. We then consider the following generalization of Problem 1. Problem 4. Let A ≽ 0 be an N × N real-symmetric, positive semidefinite, d-sparse matrix. Define the normalized state,
jψðtÞi ≔ ffi12ffiffiffiEffiffi
p ⃗y ̇ðtÞ
i⃗μðtÞ ; ð7Þ
where E > 0 is a constant and ⃗μðtÞ ≔ pffiffiAffiffi⃗yðtÞ ∈ CN. Assume we are given oracle access to A and oracle access to a unitary W that prepares the initial state jψð0Þi. Given t
and ε, the goal is to output a state that is ε-close to jψðtÞi in Euclidean norm. The constant E in Eq. (7) is also the energy of the system. The encoding is different from the one used for Problem 1;
for example, pffiffiAffiffi is of dimension N × N and might not be sparse even if A is. However, the support of jψðtÞi on the subspace spanned by the first N basis states is still KðtÞ=E, where KðtÞ is the kinetic energy. We then show the following result. Theorem 4. Problem 4 can be solved with a quantum algorithm that makes
Q 1⁄4 O(kAkmaxd logð1=εÞ min t ffiffiffiffiffiffiffiffiffiffiffiffiffi
kA−1k
p
ε ; t2
ε2 ) ð8Þ
queries to the oracles, uses  ̃O(Q × polylogðN=εÞ) 2-qubit gates, and uses W once.
The  ̃O notation hides logarithmic factors in several parameters that specify the input.
III. REDUCTION TO QUANTUM EVOLUTION
We show how to reduce Problem 1 to time evolution of a quantum system. A change of variables where ⃗yðtÞ ≔
pffiffiMffiffiffi⃗xðtÞ allows us to write Eq. (1) as
̈⃗yðtÞ 1⁄4 −A⃗yðtÞ; ð9Þ
where A ≔ pffiffiMffiffiffi−1FpffiffiMffiffiffi−1 ≽ 0 is positive semidefinite and real symmetric, and M≻0 is the diagonal matrix with entries mj. Any solution to Eq. (9) satisfies
̈⃗yðtÞ þ ipffiffiAffiffi⃗ ̇yðtÞ 1⁄4 ipffiffiAffiffi1⁄2⃗y ̇ðtÞ þ ipffiffiAffiffi⃗yðtÞ : ð10Þ
This is simply Schrödinger’s equation induced by the
Hamiltonian −pffiffiAffiffi. Hence its solution is
⃗y ̇ðtÞ þ ipffiffiAffiffi⃗yðtÞ 1⁄4 eitpffiAffiffi
1⁄2⃗ ̇yð0Þ þ ipffiffiAffiffi⃗yð0Þ : ð11Þ
Unfortunately, we do not have direct access to −pffiffiAffiffi, and casting the problem as quantum evolution with simpler Hamiltonians requires additional steps. It is possible,
however, to do Hamiltonian simulation with −pffiffiAffiffi given oracle access to A using quantum phase estimation, as we describe in Sec. VII, but that is less efficient than what we describe here. The phase estimation approach also gives rise to a different encoding, and some properties of the system are not as easy to access. For example, in the encoding used in Problem 1, the support of jψðtÞi in a basis state is either proportional to the kinetic energy of an oscillator or to the potential energy stored in a spring, but this might not be the case in other encodings. Let B be any N × M matrix that satisfies BB† 1⁄4 A and H be the block Hamiltonian:
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-4


 H≔−
0B
B
†
0
; ð12Þ
where 0 are matrices of all zeros. (The dimension of each 0 is clear from context.) Note that H acts on the space C
NþM
and functions as the “square root” of A, since the first block of H
2
is A. Schrödinger’s equation induced by H is
j
 ̇
ψðtÞi 1⁄4 −iHjψðtÞi; ð13Þ
where jψðtÞi ∈ C
NþM
is the state of a quantum system at time t. It can be verified by direct substitution that
jψðtÞi ∝
 ̇
⃗
yðtÞ
iB
†
⃗
yðtÞ
ð14Þ
is a valid solution to Eq. (13). Hence, we have
 ̇
⃗
yðtÞ
iB
†
⃗
yðtÞ
1⁄4e
−itH
 ̇
⃗
yð0Þ
iB
†
⃗
yð0Þ
; ð15Þ
which lets us compute
 ̇
⃗
yðtÞ and B
†
⃗
yðtÞ using Hamiltonian simulation. This generalizes Eq. (11) since B is not necessarily −
ffiffiffiffi
A
p
. (This formulation also stores the positions and velocities in different components of the vector, but this is a minor difference.) To match the state representation of Problem 1, we need to choose B such that ⃗μðtÞ 1⁄4 B
†
⃗
yðtÞ 1⁄4 B
†
ffiffiffiffiffi
M
p
⃗
xðtÞ, where ⃗μðtÞ ∈ C
M
[for M 1⁄4 NðN þ 1Þ=2]. We can express ⃗μðtÞ in the basis fjj; ki∶j ≤ k ∈ 1⁄2N g, which is of size M. Since F is a graph Laplacian, we can obtain B from the incidence matrix of F given by
ffiffiffiffiffi
M
p
Bjj; ki 1⁄4
ffiffiffiffiffiffi
κ
jj
p
jji if j 1⁄4 k ffiffiffiffiffiffi
κ
jk
p
ðjji − jkiÞ if j < k:
ð16Þ
This choice satisfies
ffiffiffiffiffi
M
p
Bð
ffiffiffiffiffi
M
p
BÞ
†
1⁄4F, and hence BB
†
1⁄4 A, because we can write F1⁄4
ffiffiffiffiffi
M
p
ð
P
j≤k
Bjj;kihj;kjB
†
Þ
ffiffiffiffiffi
M
p
and each term in this sum describes the interaction between the jth and kth oscillators,
ffiffiffiffiffi
M
p
Bjj; jihj; jjB
†
ffiffiffiffiffi
M
p
1⁄4κ
jj
jjihjj; ð17Þ
and for j < k,
ffiffiffiffiffi
M
p
Bjj; kihj; kjB
†
ffiffiffiffiffi
M
p
1⁄4κ
jk
ðjjihjj þ jkihkj
− jjihkj − jkihjjÞ: ð18Þ
These reproduce F once we perform the sum. To obtain the action of B we apply
ffiffiffiffiffi
M
p
−1
to Eq. (16).
Note that a similar approach based on the incidence matrix was taken in Ref. [11] to provide a quantum algorithm that simulates the wave equation. The setting considered in that paper corresponds to the special case of our problem where the graph is spatially local, and the masses and spring constants are uniform.
IV. QUANTUM ALGORITHM
Our quantum algorithm solves Problem 1 by preparing jψð0Þi and simulating H for time t. Access model. The Hamiltonian H is built from the matrix of spring constants K (or F) and M. As we wish to avoid complexities that are polynomial in N, we require succinct representations of these matrices. For maximum generality, we assume that access to M and the d-sparse K is provided by a black box, similar to that used in prior quantum algorithms [19,20]. The black box is a unitary S that computes the masses m
j
on input j and the nonzero entries of K, i.e., κ
jk
, on input ðj; kÞ, as well as their locations. This black box readily gives query access to H in Eq. (12), which is also d-sparse. Its entries are
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
κ
jk
=m
j
p
, and these factors can be applied using the values of m
j
and κ
jk
; see Appendix A. Simulation of H. Time evolution with the sparse H can be simulated using one of the methods in Refs. [21–24], which apply an approximation of the exponential e
−itH
. Such methods are tailored to our access model and achieve almost optimal scaling in the parameters ε, d, t, and kHk
max
, the largest entry of H in absolute value. Here kHk
max
is at most
ffiffiffiffi
א
p
, which is defined in Theorem 1. Complexity. The complexity of our approach is determined by the simulation of H for time t from the initial state. We consider the query complexity Q of the number of calls to S, and we allow inverses and controlled forms of these oracles. This query complexity can also be taken to include the unitary for preparing the initial state, but only one call to that preparation is needed. We also consider the gate complexity G, which is the number of additional elementary gates, which could, for example, be single-qubit gates and CNOT gates. We describe these as “2-qubit gates” in Theorem 1 for simplicity. Using Ref. [23], the Hamiltonian evolution may be simulated with
O(tΛ þ logð1=εÞ) ð19Þ
calls to a block encoding of H, where the block encoding gives a factor of 1=Λ. In Appendix A we show how to block encode H with Λ 1⁄4
ffiffiffiffiffiffiffiffiffi
d א 2
p
using Oð1Þ calls to S, and so Eq. (19) gives the total query complexity Q given in Theorem 1 since τ ≔ t
ffiffiffiffiffiffi
d א
p
. The reason for the square root dependence on the sparsity is then because the algorithm involves simulation of H, which is effectively the square root of the d-sparse operator A. Note that אd is an upper
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-5


 bound on kAk, implying that
ffiffiffiffiffiffi
d א
p
is an upper bound on the largest frequency of the normal modes. See Appendix A for a more technical explanation. To achieve final error ε, each block encoding should be given within error
ε
0
1⁄4 O(ε=1⁄2τ þ logð1=εÞ ); ð20Þ
which will determine the gate complexity. In Lemmas 8 and 9 of Appendix A we also show that it suffices to represent the relevant inputs, i.e., masses and spring constants, with a number of bits, that is, r
m
1⁄4 O( logðm
max
=ðm
min
ε
0
Þ) and r
κ
1⁄4 O( logð1=ε
0
Þ), respectively, to achieve error ε
0
in the block encoding. The gate complexity for the arithmetic is essentially Oðr
m
r
κ
Þ, and there is also another contribution OðnÞ to the gate complexity for other operations in the block encoding (e.g., for inequality tests and other state preparations). Hence, we can bound the overall gate complexity as G 1⁄4 O(Qlog
2
ðNm
max
=ðm
min
ε
0
ÞÞ). Substituting the value of ε
0
from Eq. (20), this gives
G1⁄4O
(
Qlog
2
Nτ ε
m
max
m
min
)
; ð21Þ
which is the expression provided in Theorem 1. To simplify this expression we used the fact that log (ðτ þ logð1=εÞÞ=ε) ≤ log (ðτ þ ð1=εÞÞ=ε). Because we consider complexity for large τ and 1=ε, we can upper bound that by logðτ=ε
2
Þ 1⁄4 O( logðτ=εÞ).
In Theorem 1 we have not quantified the state preparation complexity (i.e., the complexity of W), since Problem 1 assumes W is given as an input. However, in many situations this preparation can often be performed efficiently. One example is when we have oracles to separately prepare states with amplitudes proportional to ⃗
xð0Þ and
 ̇
⃗
xð0Þ. In Appendix E, we show the query complexity to prepare jψð0Þi is Q
ini
1⁄4 Oð
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
E
max
d=E
p
Þ, where
E
max
1⁄4
m
max
2
k
 ̇
⃗
xð0Þk
2
þ
κ
max
2
k
⃗
xð0Þk
2
ð22Þ
is the energy of N uncoupled oscillators of mass m
max
and spring constants κ
max
with similar initial conditions. We also establish the gate complexity G
ini
1⁄4 O(Q
ini
log
2
ðNE
max
=ðEεÞÞ).
V. EXAMPLE APPLICATION
Our quantum algorithm can simulate classical oscillators in time polynomial in n under some assumptions. As we are concerned with dynamics and seek to preserve the speedup, we focus on computing certain time-dependent properties of the system. In particular, we explain how to use the quantum algorithm to solve Problem 2, i.e., to estimate the
kinetic energy of all or some oscillators V ⊆ 1⁄2N at any time. Theorem 5. Let V be an oracle for V, i.e., a unitary that performs the map Vjji 1⁄4 −jji if j ∈ V and Vjji 1⁄4 jji otherwise, and δ > 0. Then Problem 2 can be solved with probability at least 1 − δ by a quantum algorithm that makes O( logð1=δÞ=ε) uses of V and the quantum circuit that prepares jψðtÞi (along with its inverse and controlled version). When V 1⁄4 1⁄2N , the potential energy is UðtÞ 1⁄4 E−K
V
ðtÞ, and a solution to Problem 2 provides an estimate of UðtÞ=E as well. As usual, we include controlled applications of the oracle V, which means that the global phase is distinguishable (this way we have that V 1⁄4 1⁄2N is distinct from V 1⁄4 fg). Although here we focus on estimating kinetic energies, a similar idea can be used to estimate the potential energies stored on a subset of springs at any time, as we discuss below. To prove Theorem 5, we note that K
V
ðtÞ=E 1⁄4 hψ ðtÞjP
V
jψðtÞi, where P
V
1⁄4 ð1 − VÞ=2 is the projector onto V. This expectation, which is the support of jψðtÞi on the subspace spanned by the basis states whose labels correspond to V (i.e., a subspace of that spanned by the first N basis states), can be obtained by making measurements on many copies of jψðtÞi, but that approach is not optimal (i.e., the scaling is quadratic in 1=ε). The problem reduces to estimating hψðtÞjVjψðtÞi with additive error at most 2ε and error probability δ. A method based on high-confidence amplitude estimation [25] then provides the result in Theorem 5. Hence, when jψðtÞi can be efficiently prepared and V can be efficiently implemented, we can obtain an estimate of K
V
ðtÞ=E with error ε and high probability in time polynomial in n. If in addition E is known or is efficiently computed, this translates to an efficient estimation of K
V
ðtÞ with error εE. A related result shows that our quantum algorithm can be applied to estimate the potential energy of a subset of oscillators. Problem 5. Given the same inputs as Problem 1 and an oracle for V ⊂ 1⁄2N × 1⁄2N , which is now a subset of springs (edges) labeled as ðj; kÞ with k ≥ j, output an estimate ˆ
u
V
ðtÞ ∈ R such that
j
ˆ
u
V
ðtÞ − U
V
ðtÞ=Ej ≤ ε; ð23Þ
where
U
V
ðtÞ ≔
1 2
X
j∶ðj;jÞ ∈ V
κ
jj
x
j
ðtÞ
2
þ
1 2
X
k>j∶ðj;kÞ ∈ V
κ
jk
(x
j
ðtÞ − x
k
ðtÞ)
2
ð24Þ
is the potential energy of the springs in V at time t.
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-6


 By noting that UVðtÞ=E is the support of jψðtÞi on the subspace spanned by the basis states jj; ki such that ðj; kÞ ∈ V, the problem reduces to estimating the expectation of another unitary V on jψðtÞi. Like in the prior example for the kinetic energy, this can be done efficiently using our quantum algorithm as follows. Theorem 6. Let V be an oracle for V, i.e., a unitary that performs the map Vjj; ki 1⁄4 −jj; ki if ðj; kÞ ∈ V and Vjj; ki 1⁄4 jj; ki otherwise, and δ > 0. Then, Problem 5 can be solved with probability at least 1 − δ by a quantum algorithm that makes O( logð1=δÞ=ε) uses of W and the quantum circuit that prepares jψðtÞi (along with its inverse and controlled version).
VI. IMPOSSIBILITY OF EFFICIENT CLASSICAL SIMULATIONS
An important question is whether our quantum algorithm results in an exponential quantum speedup, or whether it can be efficiently simulated by classical algorithms. We address this question in two ways: (i) by showing that our approach can solve an oracular problem—the “glued-trees” problem of Ref. [26]—in polyðnÞ time, while Theorem 2 is implied by Ref. [26], and (ii) by showing that our approach can simulate any quantum circuit of size L acting on q qubits in polyðL; qÞ time. More precisely, we show that Problem 3 is BQPcomplete, thereby proving Theorem 3. Although our results use physical systems that may seem artificial (e.g., resulting interactions between oscillators are not spatially local), they are strong evidence that no polynomial-time (in n) classical algorithm for simulating systems of coupled classical oscillators exists. Our results also add a new problem to the list of “natural” BQP-complete problems [27].
A. Oracle lower bound
At a high level, in the glued-trees problem of Ref. [26], we are given oracle access to the adjacency matrix of a sparse graph with an ENTRANCE vertex, and the goal is to find the EXIT vertex. We map this problem to a system of masses and springs by putting a unit mass at each vertex and a spring of unit spring constant at every edge. Then we show that if the system starts at rest except with the ENTRANCE vertex having unit velocity, after polynomial time, the EXIT vertex will have inverse polynomial velocity, and thus it is a special case of Problem 2. Formally, we study the following problem. Problem 6. Consider a network of N 1⁄4 2nþ1 − 2 masses coupled by springs, where M 1⁄4 1N and K coincides with the adjacency matrix of a graph consisting of two balanced binary trees of depth n “glued” randomly as in Fig. 2 [i.e., the spring constants are κjk 1⁄4 1 if ðj; kÞ is an edge of the graph or κjk 1⁄4 0 otherwise]. Each mass (vertex) of the network is labeled randomly with a bit string of size 2n. The network contains two special and verifiable masses, ENTRANCE and EXIT, which correspond to the roots of
both trees. Given oracle access to K and the label of the ENTRANCE mass, the problem is to find the label of the EXIT mass. This problem is equivalent to that studied in Ref. [26] where the authors presented an efficient quantum walk based algorithm while showing that no classical algorithm can solve the problem efficiently in this oracular setting. In that work the root vertices do not have the extra edge that connects them to a wall, so they can be easily verified as they are the only vertices of degree two. We add these extra edges to simplify the analysis below; this small change allows us to use some results on the spectral properties of the adjacency matrix already studied in Ref. [26]. With this change, the oracle to access K allows us to verify whether a certain vertex is a root or not, since they are the only vertices (or masses) with nonzero diagonal spring constants; i.e., κjj 1⁄4 1 only if j corresponds to ENTRANCE or EXIT and κjj 1⁄4 0 otherwise. Since our problem is a minor modification of the glued-trees problem, and any oracle query to our problem can be answered using a single oracle query to the glued-trees problem, the original classical lower bound of Ref. [26] implies that our problem requires 2ΩðnÞ queries to solve classically. We then show that our quantum algorithm for simulating coupled classical oscillators can also be used to solve Problem 6 efficiently. This is a different approach from that of Ref. [26] as we are not simulating the quantum walk but rather the classical dynamics obtained from Newton’s equation with a quantum algorithm. This shows that our quantum algorithm cannot be simulated classically efficiently in the oracular setting in general. Our main claim is the following lemma, which we prove in Appendix B.
Lemma 7. Let ⃗xð0Þ1⁄4ð0;0;...;0ÞT and ⃗x ̇ð0Þ1⁄4ð1;0;...;0ÞT, where the first and last components refer to the initial conditions of the ENTRANCE and EXIT masses in the network of Fig. 2, respectively. Then, there exists a time
FIG. 2. A network of N 1⁄4 2nþ1 − 2 coupled oscillators obtained by randomly gluing two binary trees. Each mass is mj 1⁄4 1 for all j ∈ 1⁄2N and is labeled by a random bit string of size 2n. Edges denote springs of constant κjk 1⁄4 1. The goal is to find the label of the EXIT mass given the label of the ENTRANCE mass and given oracle access to the network.
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-7


 t 1⁄4 O(polyðnÞ) at which the kinetic energy of the EXIT mass is KμðtÞ ≔ 1
2 ( ̇xEXITðtÞ)2 1⁄4 Ω(1=polyðnÞ). Given this lemma, it is easy to see that Problem 6 is a special case of the problem of estimating the kinetic energy, Problem 2. The quantum algorithm can prepare jψðtÞi efficiently under the conditions of Lemma 7. Because Lemma 7 proves that the kinetic energy of the EXIT mass will be inverse polynomially large after time t 1⁄4 O(polyðnÞ), a projective measurement on jψðtÞi will return the label of the EXIT with probability KEXITðtÞ=E 1⁄4 Ω(1=polyðnÞ), where the energy
is E 1⁄4 1
2 (x ̇ ENTRANCEð0Þ)2 1⁄4 1
2 in this case. Since the EXIT mass can be verified with the oracle by assumption, the probability of finding the label of EXIT can be made a constant close to 1 after O(polyðnÞ) repetitions of the previous procedure, giving an overall query and gate complexity O(polyðnÞ). Since Problem 6 requires 2ΩðnÞ queries to solve classically, this yields the exponential lower bound in Theorem 2.
B. BQP-completeness
To prove this, we start from the standard BQP-complete problem of simulating universal quantum circuits, i.e., the problem of determining some property of the output state jφi 1⁄4 UL...U1j0i⊗q, where L 1⁄4 polyðqÞ. The unitary gates Ul belong to a universal set such as fH; X; Toffg, where H and X are single-qubit Hadamard and Pauli X (bit flip) gates, and Toff is the 3-qubit Toffoli gate. (Without loss of generality, all Hadamard gates can act on the last qubit, a property that is not necessary, but we use it to simplify the presentation of the proof.) The specific problem is that of deciding if jφi is essentially the allzero state or has almost no overlap on it; see Problem 7. In Appendix C we show that this problem reduces to one in which the kinetic energy of a specific oscillator is either exponentially close to zero or at least 1=polyðqÞ large. This is essentially Problem 3 for n 1⁄4 OðqÞ. We use the standard Feynman-Kitaev construction [28,29] to encode the Ul’s into a Hamiltonian with an extra “clock” register. One property of this construction is that evolution under the Hamiltonian is known to apply the sequence of gates UL...U1 on a given initial state [with 1=polyðqÞ amplitude]. We want this Hamiltonian to be the matrix A of a corresponding system of coupled oscillators. This way we could use the connection between classical and quantum systems discussed in Sec. III, which suggests that the evolved state of the oscillators encodes the amplitudes of jφi. However, this has two problems. (1) The off-diagonal entries of the Hamiltonian would not be real negative numbers; i.e., they cannot be related to spring constants. (2) The evolution of the oscillators is induced by the
pffiffiAffiffi rather than A, so the evolution property of the Hamiltonian does not apply.
The first problem is due to the fact that Hadamard gates have negative matrix entries. To fix this, we observe that the same effect can be obtained using an operator with non-negative entries and an ancilla in the j−i ≔
ð1=pffi2ffiffiÞðj0i − j1iÞ state [30,31]. This operator is no longer unitary, but this poses no additional problems as it is only being encoded in a Hamiltonian that, at this stage, corresponds to a system of oscillators coupled by springs. The second problem is addressed by showing that the
spectral properties of pffiffiAffiffi are such that there is an appropriate evolution time t 1⁄4 polyðqÞ after which the evolved state of the oscillators indeed encodes the output of the quantum circuit with 1=polyðqÞ amplitude. Formally, we consider problem instances, i.e., systems of coupled oscillators, where N 1⁄4 ðL þ 1Þ2qþ1, M 1⁄4 1N, and A 1⁄4 F is
A 1⁄4 41N − L X
l1⁄41
ðjlihl þ 1j þ jl þ 1ihljÞ ⊗ Wl: ð25Þ
The matrix 1N is the N × N identity matrix. The 2qþ1 ×
2qþ1 matrices Wl are real symmetric and act on one more qubit than do the Ul matrices. We define them as Wl 1⁄4 Ul ⊗ 12 if Ul is the X or Toff gate acting on the space of q qubits. When Ul is a Hadamard gate, which acts on the last qubit (the qth qubit), we replace it by the following 4 × 4 matrix acting on qubits q and q þ 1:
p1ffi2ffiffi
0
BBB@
1010
0101
1001
0110
1
CCCA: ð26Þ
This matrix acts like Hadamard on qubit q when qubit q þ 1 is set to j−i. Thus the entries of Wl are non-negative in this case as well, the off-diagonal entries of A are
f0; −1=pffi2ffiffi; −1g, and all diagonal entries are 4. Hence, the
off-diagonal entries of the matrix K are f0; 1=pffi2ffiffi; 1g and one can show that κjj ≥ 0 for all j ∈ 1⁄2N . These spring constants can be efficiently accessed using Eq. (25). The gates Ul are 2-sparse, implying that the Wl’s are also 2-sparse, and A and K are 4-sparse. These properties are outlined in Theorem 3. For our proof, we consider the initial condition
for the N oscillators where ⃗xð0Þ 1⁄4 ð0; 0; ...; 0ÞT, ⃗ ̇xð0Þ 1⁄4 ðþ1; −1; 0; ...; 0ÞT, so that the energy is E 1⁄4 1. Labeling each oscillator j ∈ 1⁄2N by ðl; rÞ, where l ∈ 1⁄2L þ 1 and r ∈ 1⁄22qþ1 , the oscillator under consideration is the one with l 1⁄4 L þ 1 and r 1⁄4 1. In Appendix C we show that computing the kinetic energy of this oscillator after time t 1⁄4 polyðqÞ 1⁄4 polylogðNÞ solves the above BQP-complete problem. In addition, this classical system satisfies all of
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-8


 our conditions for the quantum algorithm to be efficient (i.e., the problem is in BQP).
VII. GENERALIZED COORDINATES
In general, when modeling a classical system using the harmonic approximation, Newton’s equation can be simply written as ̈⃗yðtÞ 1⁄4 −A⃗yðtÞ, where ⃗yðtÞ ∈ RN encodes the generalized coordinates and A ≽ 0 is of dimension N × N. To prove Theorem 4 we use a standard approach based on quantum phase estimation [32–34] to first estimate the eigenvalues of Hð2Þ ≔ −X ⊗ A, which are γη;j ≔ ð−1Þηλj, within certain precision that gives the eigenvalues of H within precision Oðε=tÞ. Here, λj ≥ 0 are the eigenvalues of A, and η ∈ f0; 1g determine the eigenvalues of −X as ð−1Þη, with eigenstates j0Xi 1⁄4 j−i and j1Xi 1⁄4 jþi. We specifically use a standard QFT-based approach to phase estimation (PE), where QFT stands for quantum Fourier transform. This eschews the need for measurement and in turn maps (within small error) each eigenvector of Hð2Þ via
jηX; λji ↦ jηX; λji ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
pX
x∶jx−γ η;j j≤εPE
bxjxi
þ ffiffiffiffiffiffiffi
δη;j
p jφη;ji ; ð27Þ
where jφη;ji is some unspecified error state of the ancillas
of unit norm, P
x jbxj2 1⁄4 1, δη;j ≤ δPE, and εPE and δPE need to be set according to the error requirements. The states jxi encode the eigenvalue estimates of Hð2Þ. From each estimate x, we obtain the eigenvalue estimate of H by taking its sign and computing a square root, i.e.,
sgnðxÞ ffijffixffiffijffi
p . Then we apply a phase factor yielding
jηX; λji ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
pX
x∶jx−γ η;j j≤εPE
e−itsgnðxÞ jffiffixffiffij
p
bxjxi
þ ffiffiffiffiffiffiffi
δη;j
p jφ0η;ji : ð28Þ
Last, we invert quantum phase estimation and other operations to (approximately) uncompute the estimated eigenvalues. The result is, for a value of the error tolerances where δPE 1⁄4 Oðε2Þ and
εPE 1⁄4 O( max ε
t ffiffiffiffiffiffiffiffiffiffiffiffiffi
kA−1k
p ; ε2
t2 ); ð29Þ
a unitary approximating e−itH within error ε. The result is implied by the complexity of quantum phase estimation that requires O(kAkmaxd logð1=δPEÞ=εPE) queries to the oracle. See Appendix D for details.
VIII. CONCLUSION
We introduced an approach to simulating systems of coupled classical oscillators using a quantum computer. We showed how to map Newton’s equations for these dynamics (coupled second-order ordinary differential equations) to the Schrödinger equation (a first-order partial differential equation), with polylogarithmic overhead in the number of oscillators under certain assumptions. Using this mapping, we demonstrated that any classical algorithm that simulates these classical dynamics requires at least 2ΩðnÞ queries to the oracle, and that they can provide solutions to BQPcomplete problems, and would thus require exponential time to solve classically under reasonable complexity theoretic assumptions. We also generalized our approach to the simulation of other classical harmonic systems. While providing a large quantum advantage in certain contexts, these techniques also have significant limitations. For example, the approach is only efficient for computing particularly large or global properties and when masses and spring constants can be computed in time polylogarithmic in system size. Another feature of our algorithm is that its complexity is (almost) linear in the evolution time t, a scaling that might not be avoided in general [19,35,36], being efficient only if t is also polylogarithmic in system size. This would discourage applications where, for example, N 1⁄4 polyðtÞ (and when fast forwarding is not possible). This feature is expected to arise when simulating physical systems with geometrically local interactions, and for initial states that are locally supported. In these examples, the relevant system size is determined by the “light cone,” whose size in D spatial dimensions would scale as N ∼ tD. Nevertheless, even for these examples our quantum algorithm would still result in significant quantum speedups (e.g., superquadratic), suggesting a new application area for quantum computers [37]. As many systems from molecular vibrations, to structural mechanics, to electrical grids, to neuronal activation can be modeled within the harmonic approximation, and since interesting dynamical features can appear at relatively short times (e.g., t independent of N), we expect that there exist specific applications that meet all the requirements for our quantum algorithm to be efficient. Such applications will then benefit from this speedup with appreciable realworld impact; identifying them is one important next step in this line of research. Last, we note that our classical-to-quantum reduction provides yet another way to think about quantum algorithms. For example, once mapped to a one-dimensional system, the glued-trees problem of masses and springs becomes a simple wave propagation problem. Since waves propagate ballistically, it is now clear why our quantum algorithm, whose complexity is mainly dominated by evolution time but not by the number of masses, works in this case. Another example results from Grover’s classical system of coupled pendulums [18] that, after using our
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-9


 reduction, provides another way to solve the unstructured search problem with OðtÞ queries, where t 1⁄4 Oð
ffiffiffiffi
N
p
Þ.
ACKNOWLEDGMENTS
The authors thank Amira Abbas, Sergio Boixo, Pedro Costa, Eddie Farhi, Bill Huggins, Marika Kieferova, Jarrod McClean, Hartmut Neven, Philipp Schleich, and Alexander Schmidhuber for helpful discussions. D. W. B. and N. W. were funded to work on this project by grants from Google Quantum AI. D. W. B. is also supported by Australian Research Council Discovery Projects No. DP190102633, No. DP210101367, and No. DP220101602. The work of N. W. was also supported by the U.S. Department of Energy, Office of Science, National Quantum Information Science Research Centers, Co-design Center for Quantum Advantage under Contract No. DE-SC0012704.
APPENDIX A: ACCESS MODELS AND BLOCK ENCODING OF B AND H
We provide more details on the access model used for our quantum algorithm, which is similar to that used in prior quantum algorithms [19,20]. The black box or oracle S allows us to perform the map
jj; li → jj; aðj; lÞi; ðA1Þ
for any j ∈ 1⁄2N ≔ f1; ...; Ng and l ∈ 1⁄2d , where d is the maximum number of nonzero entries in any row of K (i.e., the sparsity), and aðj; lÞ is the column index of the lth nonzero entry in the jth row of K. The same black box allows us to perform the maps jj; k; zi → jj; k; z ⊕
 ̄
κ
jk
i and jj; zi → jj; z ⊕
 ̄
m
j
i, for any j; k ∈ 1⁄2N , where z,
 ̄
κ
jk
, and
 ̄
m
j
are assumed to be given as bit strings. (One could use three different oracles for these maps, but we combine them into one that we call S.) Specifically, if m
max
≥m
j
for all j ∈ 1⁄2N , then j
 ̄
m
j
i denotes a basis state determined from the bits in the binary fraction m
j
1⁄4m
max
1⁄2:b
j;1
b
j;2
... , where b
j;i
∈ f0; 1g. Similarly, if κ
max
≥κ
jk
for all j; k ∈ 1⁄2N , then j
 ̄
κ
jk
i denotes a basis state determined from the bits in the binary fraction κ
jk
1⁄4κ
max
1⁄2:c
jk;1
c
jk;2
... , where c
jk;i
∈ f0; 1g. This access model simplifies some calculations and does not require knowing the important quantities in any specific units. Similar to Refs. [19,20], we assume that any number of bits can be given as the output of S, with it still being accounted for as a single oracle call. However, for computations with this output, we will only use a limited number of bits, the choice of which is governed by the parameters of the problem, particularly the approximation errors. In particular, we denote by r
m
and r
κ
the number of bits used to represent m
j
and κ
jk
. Then m
j
1⁄4m
max
 ̄
m
j
=2
r
m
and κ
jk
1⁄4κ
max
 ̄
κ
jk
=2
r
κ
. These approximations as well as the choices for r
m
and r
κ
are discussed below, where we show how to use S to gain access to B or H.
1. Access to B and H
We explain how to use S and other gates to access H, the Hamiltonian in Eq. (12). This access is required by Hamiltonian simulation methods in Refs. [21–24]. We do this by showing a block encoding of the relevant matrices using known methods for state preparation via inequality testing [38], i.e., by constructing a unitary such that one of its blocks approximates H=Λ, where Λ is needed for normalization reasons and given below. We explain how to implement that unitary operation using elementary gates. In our construction, we start by providing a block encoding of B (and B
†
). This is the N × M matrix discussed in Sec. III. Because M 1⁄4 NðN þ 1Þ=2 is not a power of two in general (N 1⁄4 2
n
), it is convenient to pad B with zeros so that its dimension is N × N
2
, instead. That is, here we consider and describe the simulation of H in a larger-dimensional space, where many amplitudes of the evolved state will be zero and the others will coincide with those of jψðtÞi in Eq. (2). With this padding, the matrices B and H will then be of dimension N × N
2
and 2N
2
× 2N
2
, respectively, in the following analyses. First we prove the following.
Lemma 8. Let ε
0
> 0, m
max
≥m
j
≥m
min
and κ
max
≥κ
jk
for all j; k ∈ 1⁄2N , and א ≔ κ
max
=m
min
. Consider the d-sparse N×N
2
matrix B obtained from Sec. III (with the padding). Then, there exists a unitary U
B
acting on 2n þ r þ 2 qubits with r 1⁄4 O( logð1=ε
0
Þ) that provides a block encoding of B to within additive error ε
0
as follows:
ð1
N
⊗ h0j
⊗n
⊗ h0j
⊗rþ2
ÞU
B
ð1
N
⊗1
N
⊗ j0i
⊗rþ2
Þ
−
1
ffiffiffiffiffiffiffiffiffi
d א 2
p
B ≤ε
0
: ðA2Þ
The quantum circuit that implements U
B
makes Oð1Þ uses of S and its inverse, in addition to O(n þ log
2
ðm
max
= ðm
min
ε
0
ÞÞ) 2-qubit gates. Next, we use this result to provide a block encoding for the 2N
2
× 2N
2
matrix H. Lemma 9. Let ε
0
> 0, m
j
≥m
min
and κ
max
≥κ
jk
for all j; k ∈ 1⁄2N , and א ≔ κ
max
=m
min
. Consider the d-sparse 2N
2
× 2N
2
matrix H obtained from Sec. III (with the padding). Then, there exists a unitary U
H
acting on 2n þ r þ 4 qubits with r 1⁄4 O( logð1=ε
0
Þ) that provides a block encoding of H to within additive error ε
0
as follows:
h0j
⊗rþ3
U
H
j0i
⊗rþ3
−
1
ffiffiffiffiffiffiffiffiffi
d א 2
p
H ≤ε
0
: ðA3Þ
The quantum circuit that implements U
H
uses a controlled version of U
B
and its inverse once, and additional OðnÞ 2-qubit gates (e.g., CNOT gates and singlequbit gates).
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-10


 Combining Lemmas 8 and 9, a block encoding for H=Λ, where Λ ≔
ffiffiffiffiffiffiffiffiffi
d א 2
p
, can be implemented within additive error Oðε
0
Þ in spectral norm using the oracles S, together with its inverse and controlled versions, Oð1Þ times, in addition to O(n þ log
2
ðm
max
=ðm
min
ε
0
ÞÞ) 2-qubit gates.
2. State preparation using inequality testing
Before presenting the proofs of the lemmas, we revisit how inequality testing can be used for state preparation [38], since our constructions use this approach, which is more efficient than controlled rotation of an ancilla qubit as in Ref. [8]. Let fβ
1
; ...; β
N
g be such that β
j
≥ 0 can be expressed using r bits (see below) and β ≥ β
j
for all j ∈ 1⁄2N . Assume we have access to an oracle that, on input jj; zi outputs jj; z ⊕
 ̄
β
j
i, where z and
 ̄
β
j
∈ 1⁄22
r
are given as bit strings of size r (we will fix z 1⁄4 0...0). That is, in this notation, j
 ̄
β
j
i is a basis state, and the bits are obtained from the binary fraction β
j
1⁄4 β1⁄2:b
1
...b
r
. The method in Ref. [38] can be used to perform the following:
jjij0i → jji
β
j
β
j0i
⊗r
j0i þ jω
j
i ; ðA4Þ
where jω
j
i is a state orthogonal to j0i
⊗r
j0i. The basic steps of the method are as follows. (1) Apply the oracle to compute
 ̄
β
j
; i.e., perform the map jji ↦ jj;
 ̄
β
j
i.
(2) Prepare the equal superposition state of r ancilla qubits, i.e., ð1=2
r=2
Þ
P
2
r
x1⁄41
jxi.
(3) Apply inequality testing to prepare jj;
 ̄
β
j
ið1=2
r=2
Þ×
ð
P
 ̄
β
j
x1⁄41
jxij0i þ
P
2
r
 ̄
β
j
þ1
jxij1iÞ.
(4) Apply Hadamard gates on the r ancilla qubits. (5) Apply the inverse of the oracle to reverse the computation of
 ̄
β
j
; i.e., perform the map jj;
 ̄
β
j
i↦ jj; 0i.
After these operations there will be amplitude
 ̄
β
j
=2
r
1⁄4 β
j
=β on j0i
⊗r
j0i. This is because the amplitude can be found by taking the inner product of the state in step 3 with ð1=2
r=2
Þ
P
2
r
x1⁄41
jxij0i. The method requires one use of the oracle and its inverse, in addition to OðrÞ Hadamard gates for steps 1 and 4, and OðrÞ gates for the inequality test in step 3. It is also possible to compute more complicated functions of the oracle by rearranging the inequality in step 3, which is the method we will use here.
3. Proof of Lemma 8
We consider a block encoding of B
†
for simplicity, and later use it to provide a block encoding of B by taking the conjugate transpose. Using the padding described above, the dimension of B
†
is N
2
× N and its entries are of the form
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
κ
jk
=m
j
p
or zero; specifically, the definition of B in Sec. III [obtained from Eq. (16)] implies
B
†
jji 1⁄4
X
k≥j
ffiffiffiffiffiffi
κ
jk
m
j
r
jjijki −
X
k<j
ffiffiffiffiffiffi
κ
jk
m
j
r
jkijji : ðA5Þ
We will construct a unitary U
† B
that is a block encoding of B
†
following simple steps and then explain how these can be simulated with quantum circuits. The steps require using a work register of qubits for some computations that we discard at the end. (1) Apply a unitary that performs the map
j0i
⊗n
↦
1
ffiffiffi
d
p
X
d
l1⁄41
jli: ðA6Þ
(2) Apply the oracle S for the positions of nonzero entries of K to map jli to jaðj; lÞi according to Eq. (A1). (3) Apply the oracle S two more times to compute
 ̄
m
j
and
 ̄
κ
jk
; i.e., perform the map jj; 0i ↦ jj;
 ̄
m
j
i and jj; k; 0i ↦ jj; k;
 ̄
κ
jk
i.
(4) Prepare the equal superposition state of r ancilla qubits, i.e., ð1=2
r=2
Þ
P
2
r
x1⁄41
jxi, where r is given below. (5) Using coherent arithmetic, compute the square of x and multiplications needed for the inequality test,
κ
max
 ̄
κ
jk
2
r
κ
≤
x
2
2
2r
א
m
max
 ̄
m
j
2
r
m
; ðA7Þ
where r
κ
and r
m
are the numbers of bits of
 ̄
κ
jk
and
 ̄
m
j
, respectively, also determined below. This gives the factor in the amplitude approximately
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
κ
jk
=ðm
j
Þ א
p
.
(6) Reverse the computation of the arithmetic for Eq. (A7) and the oracles for
 ̄
m
j
and
 ̄
κ
jk
. This transforms the working registers back to an all-zero state. (7) Apply inequality testing (outputting the result in an ancilla qubit) and a controlled-SWAP operation to perform the map jjijkij0i ↦ jkijjij1i if k < j or leave the state jjijkij0i invariant otherwise. (8) Apply HZ on the ancilla qubit of the previous step to implement j0i↦ð1=
ffiffiffi
2
p
Þðj0iþj1iÞ and j1i↦ ð1=
ffiffiffi
2
p
Þð−j0iþj1iÞ.
The previous sequence of unitaries define U
† B
. To show that the method is correct, consider steps 1–6. If we discard the working registers (used to store
 ̄
m
j
;
 ̄
κ
jk
and perform the arithmetic), these steps combined implement approximately
jjij0i
⊗nþr
j0i ↦ jji
1
ffiffiffiffiffiffi
d א
p
X
k
jki
ffiffiffiffiffiffi
κ
jk
m
j
r
j0i
⊗r
j0i þ jω
j
i;
ðA8Þ
for some state jω
j
i that is orthogonal to j0i
⊗r
j0i on the ancilla qubits. We want the error in this approximation to be
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-11


 Oðε
0
Þ, and we show how to achieve this below. Step 7 is then needed to rearrange the sum depending on whether k < j or k ≥ j, according to Eq. (A5). This step transforms Eq. (A8) to
1
ffiffiffiffiffiffi
d א
p
X
k≥j
jjijkij0i
ffiffiffiffiffiffi
κ
jk
m
j
r
j0i
⊗r
j0i
þ
1
ffiffiffiffiffiffi
d א
p
X
k<j
jkijjij1i
ffiffiffiffiffiffi
κ
jk
m
j
r
j0i
⊗r
j0i þ jω
0
j
i; ðA9Þ
where jω
0
j
i is still orthogonal to j0i
⊗r
j0i on the ancilla qubits. Applying step 8 to Eq. (A9), and considering the part of the state where the ancillas are in j0ij0i
⊗r
j0i only, we obtain
1
ffiffiffiffiffiffiffiffiffi
d א 2
p
X
k≥j
ffiffiffiffiffiffi
κ
jk
m
j
r
jjijki −
X
k<j
ffiffiffiffiffiffi
κ
jk
m
j
r
jkijji j0ij0i
⊗r
j0i:
ðA10Þ
This coincides with Eq. (A5) if we drop the normalization factor and project onto the subspace specified by j0ij0i
⊗r
j0i of the ancillas. Hence, the sequence of steps defines the desired unitary U
† B
that satisfies, for all j ∈ 1⁄2N ,
h0j
⊗rþ2
U
† B
jjij0i
⊗n
j0i
⊗rþ2
≈
ε
0
1
ffiffiffiffiffiffiffiffiffi
d א 2
p
B
†
jji: ðA11Þ
Equivalently, ð1
N
⊗ h0j
⊗n
⊗ h0j
⊗rþ2
ÞU
B
ð1
N
⊗1
N
⊗ j0i
⊗rþ2
Þ≈
ε
0
ð1=
ffiffiffiffiffiffiffiffiffi
d א 2
p
ÞB. Note that the factor of 1=
ffiffiffi
d
p
comes from a single sparse state preparation (with amplitudes
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
κ
jk
=m
j
p
). In contrast, the block encoding based on Ref. [20] involves a matched preparation and inverse preparation, each of which gives a factor of 1=
ffiffiffi
d
p
for an overall factor of 1=d for Hamiltonian simulation. In particular, the state preparation as in Lemma 4 of Ref. [20] gives a factor of 1=
ffiffiffi
d
p
, then the step of the walk as in Eq. (23) of Ref. [20] involves a matched preparation and inverse preparation to implement the reflection. The above steps can be implemented with a quantum circuit as follows. The unitary in step 1 [Eq. (A6)] is simply obtained from the action of logðdÞ Hadamard gates if d is a power of 2, or otherwise can be performed with high precision by amplitude amplification (see Appendix E.2 of Ref. [34]). The gate complexity is Oðlog dÞ 1⁄4 OðnÞ, with an amplitude for success that is very close to 1. When allowing arbitrary qubit rotations in the gate set, as we do here, then the amplitude for success can be made exactly one, so we need no correction here. The gate complexity in step 4 depends on the number of bits needed to represent m
j
,κ
jk
, and x with sufficient accuracy. The leading-order gate complexity is Oðr
2
þ rr
m
Þ for computing x
2
and x
2
×
 ̄
m
j
. We also need to multiply by אm
max
=κ
max
1⁄4
m
max
=m
min
. The number of bits needed is no more than that in x
2
×
 ̄
m
j
, which is Oðr þ r
m
Þ, giving gate complexity O(ðr þ r
m
Þ
2
). The divisions by powers of 2 just involve bit shifts with no gate cost. The gate complexity for the inequality test is linear in the number of bits, so is smaller than the multiplication cost. It suffices to set r 1⁄4 O( logð1=ε
0
Þ) for overall precision Oðε
0
Þ, since this choice would imply that the coefficients in Eq. (A8) are given with that precision. To choose r
m
,r
κ
, we note that our computations of m
j
and κ
jk
are effectively done within additive error δ
m
1⁄4 Oðm
max
=2
r
m
Þ and δ
κ
1⁄4 Oðκ
max
=2
r
κ
Þ, respectively, since
 ̄
m
j
and
 ̄
κ
jk
give m
j
and κ
jk
relative to m
max
and κ
max
. That is, we are effectively giving the factor in the amplitude:
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi κ
jk
þδ
κ
ðm
j
þδ
m
א Þ
s
: ðA12Þ
For additive error Oðε
0
Þ in the above, we can let δ
m
1⁄4 Oðm
j
ε
0
Þ; i.e., m
j
is computed within multiplicative error Oðε
0
Þ. This choice would imply r
m
1⁄4 O( logðm
max
= ðm
min
ε
0
ÞÞ). Similarly using the error propagation formula for κ
jk
indicates that the error is largest for small κ
jk
, so the choice of r
κ
would depend on κ
min
. However, the worst the error can be is rounding down a value by δ
κ
to zero, which would imply an error Oð
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
δ
κ
=κ
max
p
Þ. That implies we can choose δ
κ
1⁄4 O(κ
max
ðε
0
Þ
2
) and, therefore, r
κ
1⁄4 O( logð1=ε
0
Þ).
These choices of numbers of bits imply the complexity of the squaring and multiplications at most O(log
2
1⁄2m
max
= ðm
min
ε
0
Þ ). Last, all unitaries in steps 7 and 8 can be implemented with gate complexity OðnÞ using standard techniques. These imply the gate complexities stated in Lemma 8. ▪
4. Proof of Lemma 9
The result of Lemma 9 is a direct consequence of Lemma 8. Recall that
H1⁄4−
0B
B
†
0
; ðA13Þ
where we use 0 to denote all-zero matrices whose dimensions are clear from context. Assuming that B is of dimension N × N
2
following Lemma 8, then H would be of dimension ðN þ N
2
Þ × ðN þ N
2
Þ. However, because it is easier to work with square matrices, we will further pad B and B
†
with more zeros, to make them of dimension N
2
×N
2
, implying that the dimension of H is now ð2N
2
Þ × ð2N
2
Þ. That is, H acts on a space of 2n þ 1 qubits. [The evolved state will have nonzero amplitude on a subspace of dimension N þ M only, where M 1⁄4 NðN þ 1Þ=2.] The previous padding is equivalent to replacing Bjj; ki → ðBjj; kiÞ ⊗ j0i
⊗n
and hj; kjB
†
→ ðhj; kjB
†
Þ ⊗ h0j
⊗n
.
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-12


 With this small modification, Lemma 8 implies
H
ffiffiffiffiffiffiffiffiffi
d א 2
p
1⁄4−
0 ð1
N
⊗ j0ih0j
⊗n
⊗ h0j
⊗rþ2
ÞU
B
ð1
N
⊗1
N
⊗ j0i
⊗rþ2
Þ
ð1
N
⊗1
N
⊗ h0j
⊗rþ2
ÞU
† B
ð1
N
⊗ j0ih0j
⊗n
⊗ j0i
⊗rþ2
Þ0
!
;
ðA14Þ
or, equivalently, ðH=
ffiffiffiffiffiffiffiffiffi
d א 2
p
Þ 1⁄4 h0j
⊗rþ2
 ̃
U
H
j0i
⊗rþ2
, where
 ̃
U
H
≔ −j0ih1j ⊗ 1⁄2ð1
N
⊗ j0ih0j
⊗n
⊗1
⊗rþ2 2
ÞU
B
þ H:c: ðA15Þ
Here, H.c. denotes the conjugate transpose of the first term. This operator is not yet unitary because j0ih0j
⊗n
is not unitary (it is a projector). However, it is simple to construct a block encoding for a projector as follows. We bring one additional ancilla and implement a conditional unitary operation on the state of the ancilla that is
jþihþj ⊗ ð2j0ih0j
⊗n
−1
N
Þ þ j−ih−j ⊗ 1
N
: ðA16Þ
Applying h0j j0i to this operator gives the block encoding,
h0jðjþihþj ⊗ ð2j0ih0j
⊗n
−1
N
Þ þ j−ih−j ⊗ 1
N
Þj0i 1⁄4 j0ih0j
⊗n
; ðA17Þ
which implements the desired projector. We write U
cond
for this unitary when acting on the system of 2n þ 1 qubits (the space associated with H) plus r þ 3 ancilla qubits. Hence, our block encoding for H is
1
ffiffiffiffiffiffiffiffiffi
d א 2
p
H 1⁄4 h0j
⊗rþ3
U
H
j0i
⊗rþ3
; ðA18Þ
where
U
H
≔ −U
cond
ðj0ih1j ⊗ 1
2
⊗U
B
Þ þ H:c: ðA19Þ
Here 1
2
acts on the extra qubit used for block encoding the projector. Simulating U
H
with a quantum circuit requires applying a controlled version of U
B
and U
† B
once, in addition to a simple X gate on the controlled qubit. Simulating U
cond
can be done with gate complexity OðnÞ, since it requires applying a conditional phase on j0i
⊗n
.▪
APPENDIX B: ORACLE LOWER BOUND AND PROOF OF LEMMA 7
Consider the glued-trees oscillator network in Fig. 2. Let any node represent a unit mass (i.e., m
j
1⁄4m
max
1⁄4m
min
1⁄41 for all j ∈ 1⁄2N ) and each edge represent a spring of constant 1 [i.e., κ
jk
1⁄4κ
max
1⁄4 1 if ðj; kÞ is an edge and κ
jk
1⁄40 otherwise]. The ENTRANCE and EXIT masses are additionally connected to a wall each with a spring of constant
also 1. We write
⃗
xðtÞ ∈ R
N
and
 ̇
⃗
xðtÞ ∈ R
N
for the positions and velocities of the masses, where we assume their motion is constrained to one spatial dimension, such as the “horizontal” direction. Although we do not know the actual names of the masses a priori, our labels are such that j 1⁄4 1 refers to the ENTRANCE, j 1⁄4 2, 3 refer to the masses in the second column, and so on, until j 1⁄4 N 1⁄4 2
nþ1
−2 represents the EXIT mass. The energy of the system is E 1⁄4 TðtÞ þ UðtÞ, where
TðtÞ 1⁄4
1 2
X
N
j1⁄41
(
 ̇
x
j
ðtÞ)
2
; ðB1Þ
UðtÞ 1⁄4
1 2
X
j;k>j
κ
jk
(x
j
ðtÞ − x
k
ðtÞ)
2
þ
1 2
κ
11
(x
1
ðtÞ)
2
þ
1 2
κ
NN
(x
N
ðtÞ)
2
ðB2Þ
are the kinetic and potential energies, respectively. Newton’s equation gives then a set of N coupled secondorder differential equations:
̈
⃗
xðtÞ 1⁄4 −A
⃗
xðtÞ; ðB3Þ
where A is the (N × N)-dimensional symmetric matrix:
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-13


 A1⁄4
0
BBBBBBBBBBBBBBBBBBBBB@
3 −1 −1 0 0
−1 3 0 −1 0
−1 0 3 0 0
0 −1 0 3 0
... ... ... ... . . . ... ... ... ...
... ... ... ... ... 3 0 −1 0
... ... ... ... ... 0 3 0 −1
... ... ... ... ... −1 0 3 −1
0 0 0 0 0 −1 −1 3
1
CCCCCCCCCCCCCCCCCCCCCA
:
ðB4Þ
Note that A 1⁄4 31N − A, where A is the adjacency matrix of the graph constructed from the two binary trees randomly glued, if we disregard the edges that connect the roots to their respective walls, and 1N is the N × N identity matrix. Also, A is positive semidefinite because it is symmetric and diagonally dominant. This property also follows from the potential being UðtÞ 1⁄4 1
2 ⃗xðtÞTA⃗xðtÞ ≥ 0 for all ⃗xðtÞ ∈ RN,
which implies A ≽ 0. In fact, A is positive definite: The matrix A0 1⁄4 A − j1ih1j − jNihNj represents the above network of oscillators where the masses at the roots are not connected to any wall. Hence, A0 contains a nondegenerate eigenvector of eigenvalue zero corresponding to the translations of the system, i.e., the eigenvector
ju1i ≔ ð1=pffiffiNffiffiÞ P
j jji. The only way for A to contain an eigenvalue zero is if this eigenvector ju1i was also an eigenvector of j1ih1j þ jNihNj, which is not the case. Nevertheless, while A≻0, its smallest eigenvalue is exponentially small in n since the expectation hu1jAju1i 1⁄4 2=N is an upper bound on the smallest eigenvalue. We would like to show the following property. If ⃗xð0Þ 1⁄4 ð0; 0; ...; 0ÞT and ⃗ ̇xð0Þ 1⁄4 ð1; 0; ...; 0ÞT, then ⃗x ̇ðtÞ is such that the magnitude of its Nth entry, corresponding to EXIT, is at least polynomially small in n for a time t that is at most polynomial in n [i.e., the kinetic energy of the Nth oscillator is Ω(1=polyðnÞ)]. For these initial conditions, the solution to Eq. (B3) implies
⃗ ̇xðtÞ 1⁄4 cos tpffiffiAffiffi ⃗ ̇xð0Þ: ðB5Þ
The matrix A, and hence pffiffiAffiffi, possesses a symmetry that allows one to simulate the dynamics of the N oscillators by considering that of 2n oscillators in one spatial dimension,
instead. (A similar idea was used in Ref. [26] to prove that the quantum algorithm solves the problem efficiently.) To show this, we define 2n real components:
zlðtÞ 1⁄4 ffi1ffiNffiffilffi
pX
j ∈ lth column
xjðtÞ; ðB6Þ
where Nl is the number of masses in the lth column and
l ∈ 1⁄22n ; that is, Nl 1⁄4 2l−1 if l ≤ n and Nl 1⁄4 22n−l if l ≥ n þ 1. Then, for the masses in any column that is not the ENTRANCE (l 1⁄4 1), EXIT (l 1⁄4 2n), or the randomly glued masses where l 1⁄4 n and l 1⁄4 n þ 1, simple manipulations of Eq. (B3) give
̈zlðtÞ 1⁄4 pffi2ffiffizl−1ðtÞ − 3zlðtÞ þ pffi2ffiffizlþ1ðtÞ: ðB7Þ
For the masses in the remaining columns, Eq. (B3) gives
̈z1ðtÞ 1⁄4 −3z1ðtÞ þ pffi2ffiffiz2ðtÞ; ðB8Þ
̈znðtÞ 1⁄4 pffi2ffiffizn−1ðtÞ − 3znðtÞ þ 2znþ1ðtÞ; ðB9Þ
̈znþ1ðtÞ 1⁄4 2znðtÞ − 3znþ1ðtÞ þ pffi2ffiffiznþ2ðtÞ; ðB10Þ
̈z2nðtÞ 1⁄4 pffi2ffiffiz2n−1ðtÞ − 3z2nðtÞ: ðB11Þ
Then, if ⃗zðtÞ ≔ 1⁄2z1ðtÞ; ...; z2nðtÞ T ∈ R2n, Eq. (B3) implies
̈⃗zðtÞ 1⁄4 −  ̃A ⃗zðtÞ; ðB12Þ
where  ̃A is a ð2nÞ × ð2nÞ real-symmetric and tridiagonal matrix that, in bra-ket notation, can be written as
 ̃A 1⁄4 3 2 Xn
l1⁄41
jlihlj − pffi2ffiffi nX−1
l1⁄41
ðjlihl þ 1j þ jl þ 1ihljÞ
þ 2nX−1
l1⁄4nþ1
ðjlihl þ 1j þ jl þ 1ihljÞ
− 2ðjnihn þ 1j þ jn þ 1ihnjÞ: ðB13Þ
Hence, we have effectively reduced the dimension of the system from N to 2n when symmetries are considered. The matrix  ̃A is 312n − A ̃ , where A ̃ is the 2n × 2n adjacency matrix of the graph constructed from the glued binary trees in the new coordinate system defined above (see Fig. 3). The matrix  ̃A is also positive, with its smallest eigenvalue being exponentially small in n, and any two eigenvalues separated by a gap that is at least Δ0 1⁄4 Ωð1=n3Þ. In
FIG. 3. The 2n × 2n matrix  ̃A 1⁄4 312n − A ̃ viewed as the adjacency matrix of a weighted graph.
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-14


 particular, if ⃗zð0Þ 1⁄4 ð0; 0; ...; 0ÞT, the solution to Eq. (B12) implies
⃗z ̇ðtÞ 1⁄4 cos t
ffiffi ̃Affiffi
p ⃗z ̇ð0Þ: ðB14Þ
We are interested in the magnitude of  ̇z2nðtÞ ≡  ̇xNðtÞ or, more specifically, the kinetic energy of the Nth oscillator. Similar to Ref. [26], rather than considering a fixed t, we will consider an average over t as follows:
PEXITðTÞ ≔ 1
T
ZT
0
dtjx ̇NðtÞj2 1⁄4 1
T
ZT
0
dtjz ̇2nðtÞj2: ðB15Þ
Here, T > 0 is set below and PEXITðTÞ is the average kinetic energy of the Nth oscillator from time t 1⁄4 0 to t 1⁄4 T renormalized by the energy E 1⁄4 1=2 for the above initial conditions; for our algorithm, PEXITðTÞ coincides with the
average probability of projecting jψðtÞi into a basis state that corresponds to the EXIT mass. Thus, the goal reduces to showing that there exists T 1⁄4 O(polyðnÞ) such that PEXITðTÞ 1⁄4 Ω(1=polyðnÞ). If we prove this, then Eq. (B15) automatically implies the existence of t 1⁄4 O(polyðnÞ) such that KNðtÞ 1⁄4 Ω(1=polyðnÞ), which is our main goal. Finding such t can be done classically by simulating Eq. (B12) in time polynomial in n. We can write
 ̇z2nðtÞ 1⁄4 h2nj 1
2 ðeit
ffi ̃Affiffi
p
þ e−it
ffi ̃Affiffi
p
Þj1i: ðB16Þ
Let fjλ1i; ...; jλ2nig be the 2n eigenvectors of the adjacency
matrix  ̃A of eigenvalues λ1 < λ2 < < λ2n. These are
also eigenvectors of
pffiffi ̃Affiffi
of eigenvalues γl ≔ ffiffiffiffiffiffiffiffiffiffiffiffi
3 − λl
p > 0. This implies
PEXITð∞Þ ≔ Tli→m∞PEXITðTÞ
1⁄4 Tli→m∞
1 T
ZT
0
dth2nj 1
2 ðeit
ffi ̃Affiffi
p
þ e−it
ffi ̃Affiffi
p
Þj1ih1j 1
2 ðeit
ffi ̃Affiffi
p
þ e−it
ffi ̃Affiffi
p
Þj2ni
1⁄4 2 Xn
l;l0 1⁄41
h2njλlihλlj1ih1jλl0 ihλl0 j2niTli→m∞
1 T
ZT
0
dt cosðtγlÞ cosðtγl0Þ
1⁄41
2
2 Xn
l1⁄41
h2njλlihλlij1ih1jλlihλlj2ni
1⁄41
2
2 Xn
l1⁄41
jhλlj1ij2jhλlj2nij2
1⁄41
2
2 Xn
l1⁄41
jhλlj1ij4
≥1
2
1 2n
2 Xn
l1⁄41
jhλlj1ij2
1⁄41
4n : ðB17Þ
To obtain this we used limT→∞ð1=TÞ R0T dt eitðγl−γl0 Þ 1⁄4 δl;l0 , limT→∞ð1=TÞ R0T dt eitðγlþγl0 Þ 1⁄4 0 since the eigenvalues are
positive, jhλlj1ij 1⁄4 jhλlj2nij for all l ∈ 1⁄22n due to a reflection symmetry of the network (i.e., the adjacency matrix of the graph in the line is invariant under the transformation l ↔ 2n − l þ 1), and also the Cauchy-Schwarz inequality for the last line as there are 2n different eigenvectors. This would already prove the desired result, but we are interested in finite times T < ∞ and, more precisely, showing a similar bound for T 1⁄4 O(polyðnÞ). Using again the reflection symmetry of the network, for T < ∞ the average success probability can be written as
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-15


 PEXITðTÞ 1⁄4 X
l;l0
h2njλlihλlj1ih1jλl0ihλl0 j2ni 1
T
ZT
0
dt cosðtγlÞ cosðtγl0Þ
1⁄4X
l;l0
jh1jλlij2jh1jλl0 ij2 1
T
ZT
0
dt cosðtγlÞ cosðtγl0 Þ
1⁄41
2
X
l
jh1jλlij4 1
T
ZT
0
dt1⁄21 þ cosð2tγlÞ þ X
l≠l0
jh1jλlij2jh1jλl0 ij2 1
T
ZT
0
dt cosðtγlÞ cosðtγl0Þ
1⁄41
2
X
l
jh1jλlij4 þ 1
2
X
l
jh1jλlij4 1
T
ZT
0
dt cosð2tγlÞ þ X
l≠l0
jh1jλlij2jh1jλl0 ij2 1
T
ZT
0
dt cosðtγlÞ cosðtγl0Þ
1⁄4 PEXITð∞Þ þ 1
2
X
l
jh1jλlij4 1
T
ZT
0
dt cosð2tγlÞ þ X
l≠l0
jh1jλlij2jh1jλl0 ij2 1
T
ZT
0
dt cosðtγlÞ cosðtγl0 Þ; ðB18Þ
where we used the identity cos2ðαÞ 1⁄4 1
2 1⁄21 þ cosð2αÞ . Then, the correction to PEXITð∞Þ for T < ∞ is such that
jPEXITðTÞ − PEXITð∞Þj 1⁄4 X
l≠l0
jh1jλlij2jh1jλl0 ij2 1
T
ZT
0
dt cosðtγlÞ cosðtγl0 Þþ 1
2
X
l
jh1jλlij4 1
T
ZT
0
dt cosð2tγlÞ : ðB19Þ
Note that, for l ≠ l0,
1 T
ZT
0
dt cosðtγlÞ cosðtγl0Þ 1⁄4 1
T
1 2
sin1⁄2Tðγl þ γl0 Þ
γl þ γl0
þ sin1⁄2Tðγl − γl0Þ
γl − γl0
≤1
TΔ ðB20Þ
where Δ is the minimum spectral gap between any pair of eigenvalues γl, that is, Δ ≔ minl jγlþ1 − γlj.
(Also, jγl þ γl0j > Δ if l ≠ l0.) Also, if we order the eigenvalues so that γlþ1 > γl for all l 1⁄4 1⁄22n − 1 , for l ≥ 2 we have γl ≥ Δ and
1 T
ZT
0
dt cosð2tγlÞ 1⁄4 1
T
sinð2tγlÞ 2γl
≤1
2TΔ : ðB21Þ
For l 1⁄4 1, the eigenvalue γl is exponentially small in n and the corresponding average can be Oð1Þ. Combining these equations and using the reflection symmetry of the network, we obtain
jPEXITðTÞ − PEXITð∞Þj ≤ 1
TΔ
X
l≠l0
jhλlj1ij2jhλl0 j1ij2 þ 1
4TΔ
X
l≥2
jhλlj1ij4 þ 1
2 jhλ1j1ij4
≤1
TΔ
X
l;l0
jhλlj1ij2jhλl0 j1ij2 þ 1
2 jh1jλ1ij4
≤1
TΔ þ 1
2 jh1jλ1ij4; ðB22Þ
where we also used P
l jh1jλlij2 1⁄4 1. We need to show that both these terms are small. In Ref. [26] it has been shown that the eigenvalues λl’s are separated by spectral gaps bounded by Δ0 1⁄4 Ωð1=n3Þ. The
same follows for the γl’s. More precisely, suppose that the two closest eigenvalues of  ̃A are 3 − λ ≤ 6 and 3 − ðλ þ Δ0Þ.
Then, the two closest eigenvalues of
pffiffiA ̃ffiffi
are separated as
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-16


 Δ 1⁄4 ffiffiffiffiffiffiffiffiffiffi
3−λ
p − ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
3 − ðλ þ Δ0Þ
p
1⁄4 ffiffiffiffiffiffiffiffiffiffi
3−λ
p 1−
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − Δ0
3−λ
r
≥ ffiffiffiffiffiffiffiffiffiffi
3−λ
p 1 − 1 − Δ0
3−λ
≥ Δ0
ffiffiffiffiffiffiffiffiffiffi
3−λ
p
≥ Δ0
pffi6ffiffi : ðB23Þ
Then, since Δ0 1⁄4 Ωð1=n3Þ, we have Δ 1⁄4 Ωð1=n3Þ. This implies that we can choose T 1⁄4 Oðn4Þ so that, for example,
1
TΔ ≤ 1
8n : ðB24Þ
It is also possible to show that jh1jλ1ij4 is exponentially small in n. Consider the vector
jv1i ≔ n X
l1⁄41
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
22þn−l
p jli þ 2 Xn
l1⁄4nþ1
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
21þl−n
p jli: ðB25Þ
The length of this vector is
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Pln1⁄41ð1=21þn−lÞ
q
1⁄4
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − 1=2n
p being exponentially close to 1. In addition,
 ̃Ajv1i 1⁄4 3jv1i − pffi2ffiffi nX−1
l1⁄41
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
22þn−l
p jl þ 1i þ n X
l1⁄42
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
22þn−l
p jl − 1i þ 2nX−1
l1⁄4nþ1
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
21þl−n
p jl þ 1i þ 2 Xn
l1⁄4nþ2
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
21þl−n
p jl − 1i
−21
2 ðjn þ 1i þ jniÞ
1⁄4 3jv1i − pffi2ffiffi n X
l1⁄42
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
23þn−l
p jli þ nX−1
l1⁄41
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
21þn−l
p jli þ 2 Xn
l1⁄4nþ2
ffiffi1ffiffiffiffiffiffi
2l−n
p jli þ 2nX−1
l1⁄4nþ1
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
22þl−n
p jli − 2 1
2 ðjn þ 1i þ jniÞ
1⁄4 3jv1i − 3 nX−1
l1⁄42
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
22þn−l
p jli − 1
2 jni − ffiffi1ffiffiffiffiffiffiffi
2n−1
p j1i − 3 2nX−1
l1⁄4nþ2
ffiffiffiffi1ffiffiffiffiffiffiffiffiffi
21þl−n
p jli − ffiffi1ffiffiffiffiffiffiffi
2n−1
p j2ni − 1
2 jn þ 1i − 2 1
2 ðjn þ 1i þ jniÞ
1⁄4 3jv1i − 3jv1i þ 1
2 ffiffiffiffiffiffiffiffiffi
2n−1
p j1i þ 1
2 ffiffiffiffiffiffiffiffiffi
2n−1
p j2ni
1⁄41
2 ffiffiffiffiffiffiffiffiffi
2n−1
p j1i þ 1
2 ffiffiffiffiffiffiffiffiffi
2n−1
p j2ni: ðB26Þ
This implies k  ̃Aðjv1i=kjv1ikÞk 1⁄4 Oð1= ffi2ffiffinffiffi
p Þ and that jv1i=kjv1ik is exponentially close to the normalized eigenvector of lowest eigenvalue as the spectral gaps are at least Δ 1⁄4 Ωð1=n3Þ; that is, kðjv1i=kjv1ikÞ − jλ1ik 1⁄4 O(1= expðnÞ). Since the first entry of jv1i=kjv1ik is O(1=expðnÞ), these results imply jh1jλ1ij1⁄4O(1=expðnÞ). Combining these bounds, and for the choice of T above, we obtain
jPEXITðTÞ − PEXITð∞Þj ≤ 1
8n þ O(1= expðnÞ): ðB27Þ
Together with Eq. (B17), this gives
PEXITðTÞ ≥ 1
8n − O(1= expðnÞ); ðB28Þ
which is the desired result: we can choose T 1⁄4 Oðn4Þ so that the average probability PEXITðTÞ is Ωð1=nÞ, implying the existence of t ∈ 1⁄20; T with the desired property j ̇xNðtÞj 1⁄4 Ω(1=polyðnÞ). ▪
We note that numerical solutions show a stronger result, where t ∝ n suffices. See Fig. 4 for an example.
FIG. 4. Numerical simulation of the network in Fig. 2 for n 1⁄4 20 (N 1⁄4 221 − 2). Initially ⃗xð0Þ 1⁄4 ð0; 0; ...; 0ÞT and ⃗ ̇xð0Þ 1⁄4 ð1; 0; ...; 0ÞT. At time t ≈ 2n, j ̇xNðtÞj becomes significant. Similar behavior is observed for larger values of n.
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-17


 APPENDIX C: BQP-COMPLETENESS AND PROOF OF THEOREM 3
In this appendix our goal is to show Theorem 3, which establishes that Problem 3 is BQP-complete. A problem is BQP-complete if it is in BQP and if it is BQP-hard, which means that every problem in BQP can be reduced to it by classical polynomial-time reductions. Since we have already established that Problem 3 is in BQP (a consequence of Theorem 1), we only need to show it is BQP-hard. To show our problem is BQP-hard, we start the reduction from the following BQP-complete problem: Problem 7. Given a quantum circuit on q qubits with L 1⁄4 polyðqÞ gates over the gate set of Hadamard, Pauli X, and Toffoli acting on the initial state j0i⊗q, decide if the
output state has overlap at least 1 − 1= expðpffiqffiffiÞ with j0i⊗q
or has overlap at most 1= expðpffiqffiffiÞ with j0i⊗q, promised that one of these is the case. This problem is easily seen to be in BQP. It is BQP-hard by reduction from the standard BQP-complete problem, which has a similar input, but the goal is to decide a different property of the output state: Upon measuring the first qubit of the output state, we have to decide if it is 1 with probability at least 2=3 or 1 with probability at most 1=3, promised that one of these is the case. By known results, we can assume our gate set is real and contains only Hadamard and Toffoli, since this is a universal gate set for real quantum computation, which is computationally as powerful as complex quantum computation [39,40]. We also add the single-qubit Pauli X gate so that we can create the state j1i from j0i, as we want the computation to start with all qubits in state j0i. Also, the X and Toffoli gates generate SWAP gates, and we can then assume that all Hadamard gates act on the same qubit. This property will be useful to simplify the presentation of the proof, but it is not necessary, and one could in principle allow Hadamard gates to act on any qubit. Given such a circuit, we can amplify the constants 2=3 and 1=3 to 1 − 1= expðqÞ and 1= expðqÞ by running OðqÞ copies of the circuit in parallel and taking the majority vote of the first output qubits of all circuits. Now we have a new circuit on Oðq2Þ qubits whose first qubit is almost certainly [with probability 1 − 1= expðqÞ] j1i when the answer is yes and almost certainly j0i when the answer is no. We then use an additional qubit and copy this answer to that qubit. Since the qubit we are copying is exponentially close to being j0i or j1i, let us assume it is one of these, and this will only introduce an error of 1= expðqÞ. We then run the circuit’s inverse on the remaining qubits to restore them to the all-zero state. The resulting output state is now exponentially close to all zeros if the additional qubit was also zero, which happens when the input was a no instance. If it was a yes instance, the additional qubit we added will be exponentially close to j1i, and hence the overall state will have almost no amplitude on the all-zeros state.
Thus deciding if the output state of a Oðq2Þ qubit circuit of size polyðqÞ is 1 − 1= expðqÞ close to the all-zeros state or has at most 1= expðqÞ overlap on the all-zeros state is BQP-complete. This yields the stated result by renaming q to q2. (Our proof below does not require the closeness to be exponentially small, and it would suffice to have inverse polynomial closeness, as long as this polynomial was smaller than all the other polynomials appearing in the problem.)
1. From a circuit to a network of oscillators
We now show that our quantum algorithm for simulating coupled classical oscillators allows us to solve the BQPcomplete problem above. We begin with the given quantum circuit on q qubits with L 1⁄4 polyðqÞ gates. If the gates are U1 to UL, the output of this circuit is UL...U1j0i⊗q. Our
goal is to decide if this state is essentially j0i⊗q or has essentially no overlap with j0i⊗q. The unitaries U1 to UL are either the single-qubit gates Hadamard H or Pauli X (tensored with identity on all other qubits) or the 3-qubit Toffoli gate Toff (tensored with identity on all other qubits). These gates are
H1⁄4
p1ffi2ffi p1ffi2ffi
p1ffi2ffi − p1ffi2ffi ; X 1⁄4 0 1
1 0 ; and
Toff 1⁄4
0
BBBBBBBBBBBBBBB@
10000000
01000000
00100000
00010000
00001000
00000100
00000001
00000010
1
CCCCCCCCCCCCCCCA
ðC1Þ
in the corresponding 1-qubit and 3-qubit subspaces. It will be very useful in our context that these are real as the resulting Hamiltonian will have real entries, which we require because the κjk are real. From this circuit we will create a network of N oscillators, where N 1⁄4 ðL þ 1Þ2qþ1. It is convenient to label each oscillator j ∈ 1⁄2N using two indexes j → ðl; rÞ, where l ∈ 1⁄2L þ 1 , r ∈ 1⁄22qþ1 , and j 1⁄4 ðl − 1Þ2qþ1 þ r. We will call the oscillator with l 1⁄4 L þ 1 and r 1⁄4 1 the output oscillator. In our construction, the N × N matrix of spring constants K that describes the couplings between oscillators, which depends on the Ul’s, is 4-sparse and each entry is bounded as κjk ≤ 4. We will have all masses be
mj 1⁄4 1. Note that A 1⁄4 pffiffiMffiffiffi−1FpffiffiMffiffiffi−1 1⁄4 F and ⃗yðtÞ 1⁄4
pffiffiMffiffiffi⃗xðtÞ 1⁄4 ⃗xðtÞ in this case. This simplifies our analysis.
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-18


 In the following, we show that for our oscillator network, there exists a time t 1⁄4 polylogðNÞ such that, for the initial conditions where ⃗xð0Þ1⁄4ð0;...;0ÞT, x ̇1ð0Þ 1⁄4 1, x ̇2ð0Þ 1⁄4 −1, and x ̇jð0Þ 1⁄4 0 for all j > 2, the kinetic energy of the output oscillator is either exponentially close to 0 (when the original circuit had almost no overlap with j0i⊗q) or 1=polylogðNÞ (when the original circuit’s output is very close to j0i⊗q). Since our algorithm allows us to estimate the kinetic energy of a given oscillator to additive 1=polylogðNÞ precision, we can distinguish these two cases with complexity O(polylogðNÞ). The initial quantum state jψð0Þi is simply j−i tensored with the all-zeros state, and hence easy to prepare. This proves that Problem 2 is BQP-complete even with these constraints on the initial conditions, t, ε, M, and K, which is the desired result. We now provide the details of this construction. We use the bra-ket notation for specifying vectors and matrices, which is convenient for relating properties of the classical system with properties of quantum states. We will specify our oscillator network using the A matrix, instead of the K matrix. This real matrix is positive semidefinite and has non-negative entries on the diagonal and nonpositive entries on the off diagonal. The standard FeynmanKitaev [28,29] circuit-to-Hamiltonian construction gives us a Hamiltonian of the form
L X
l1⁄41
ðjlihl þ 1j þ jl þ 1ihljÞ ⊗ Wl; ðC2Þ
where Wl is the lth gate in the circuit, i.e., Ul. We cannot let A equal this Hamiltonian, since the matrix is not positive semidefinite and there are off-diagonal entries of both signs. The first issue is easily fixed by adding a multiple of the identity, but it will require some work to fix the second issue. We will adjoin an additional qubit to work in a slightly larger space. Formally, we consider the following Hilbert space:
H 1⁄4 Hclock ⊗ Hcomp ⊗ H2: ðC3Þ
Here, Hclock is the (L þ 1)-dimensional Hilbert space that is used to describe the state of the clock [i.e., corresponding to the first register in Eq. (C2)], which is used to track the progress of a simulated quantum computation on a state in Hcomp ⊗ H2, where Hcomp is 2q dimensional and H2 is two dimensional. The purpose of Hcomp is to store the state of the given quantum circuit at a time given by the clock. The purpose of H2 is to address the issue on the off-diagonal entries raised above. The off-diagonal entries of A need to have the same sign, but our gate set includes a gate H with entries of both signs. We address this by providing a
resource state j−i 1⁄4 ð1=pffi2ffiffiÞðj0i − j1iÞ in the last register which we use to effectively create negative signs in a subspace although the operators will only have positive
entries. Similar constructions that create Hamiltonians with non-negative entries have been used within the context of Hamiltonian complexity; see Refs. [30,31], for example. We will map our circuit to a system of oscillators that satisfy the assumptions made in Problem 1 by choosing the couplings to implement an “encoded” sequence of gates fWlgl as
A 1⁄4 41N − L X
l1⁄41
ðjlihl þ 1j þ jl þ 1ihljÞ ⊗ Wl; ðC4Þ
where each Wl corresponds to an encoded version of the lth gate in the original circuit, which is either a Hadamard, X, or a Toffoli, and 1N is the identity matrix on the system of dimension N. Notice that Wl lives in Hcomp ⊗ H2, whereas the original unitaries Ul lived in Hcomp. So we encode each gate into a larger space with 1 additional qubit. We want all the entries in the encoded versions of Hadamard, X, and Toffoli to be non-negative, which will make the off-diagonal entries nonpositive in A due to Eq. (C4). Let us start with the Hadamard matrix. Without loss of generality, because we can swap qubits, we assume the Hadamard always acts on qubit q, the last qubit of Hcomp. We describe our encoded Hadamard gate via the following positive-valued real-symmetric block matrix acting on the last qubit of Hcomp and H2:
Henc 1⁄4 p1ffi2ffiffi 12 12
12 X : ðC5Þ
This can be seen to act as a logical Hadamard when acting on a state of the form jψij−i because of the following block-encoding result:
ð12 ⊗ h−jÞHencð12 ⊗ j−iÞ
1⁄4 p1ffi2ffiffi ð12 ⊗ h−jÞ 12 12
12 X ð12 ⊗ j−iÞ
1⁄4 p1ffi2ffiffi 1 1
1 −1
1⁄4 H: ðC6Þ
Note here that unlike a conventional block encoding, the encoded Hadamard gate Henc is not a unitary operation. However, it block encodes a unitary operation within the logical subspace where the Hilbert space H2 contains the state j−i, which is sufficient for our purposes as it represents the Hadamard gate as a real-symmetric matrix with positive entries. The Toffoli and X gates have non-negative entries and so we define the encoded Toffoli and X gates on Hcomp ⊗ H2 as simply Ul ⊗ 12. The action of this matrix on the first register (Hcomp) is a Toffoli gate or X gate, independent
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-19


 of the second register (H2). Finally, as in the standard circuit-to-Hamiltonian construction, the initial state that we use is jl 1⁄4 1i ⊗ j0i⊗q on the first two spaces, and j−i on the last space, as discussed. As mentioned above, the Wl’s, which are not necessarily unitary on the entire Hilbert space (but act as unitaries on the subspace where the last register
is j−i), have non-negative entries ∈ f0; 1=pffi2ffiffi; 1g and are of sparsity at most 2. The matrix F 1⁄4 A contains all the desired properties to describe N coupled oscillators. Its off-diagonal entries are
ajk ∈ f0; −1; −1=pffi2ffiffig, for j; k ∈ 1⁄2N , j ≠ k. This agrees with the assumptions that the off-diagonal elements in F are negative given in Sec. III. All diagonal entries are ajj 1⁄4 4, which similarly agrees with the requirement in Sec. III that the diagonal elements of F are positive. The spring constants of the system are such that κjk 1⁄4 −ajk for j ≠ k
and then κjk ∈ f0; 1=pffi2ffiffi; 1g. Also, κjj 1⁄4 ajj − P
k≠j κjk 1⁄4
4−P
k≠j ajk. The matrix K has a nonzero diagonal entry and it can have at most 3 nonzero off-diagonal entries. For example, if Wl 1⁄4 Henc and Wlþ1 1⁄4 Toff or Wlþ1 1⁄4 X, then the corresponding row will have at most 3 nonzero
matrix elements off the diagonal with coefficients 1=pffi2ffiffi for two and 1 for the remainder. Maximizing over all such
possibilities P
k≠j ajk ≤ 1 þ 2=pffi2ffiffi in our construction, we obtain κjj > 0. (Since the Hadamard gates act on the same qubit, we do not have two consecutive Hadamard gates in our circuit.) The matrix of spring constants K is then 4-sparse and each entry satisfies κjk ≤ 4. Given j ∈ 1⁄2N , it is possible to compute all neighbors aðj; lÞ of j, where l ∈ 1⁄24 , and the corresponding nonzero spring constants, in polynomial time from the polynomial-sized representation in Eq. (C4). This gives an efficient circuit to query the matrix K as in Sec. IV. Now that we have established that a query to the elements of the oscillator can be efficiently simulated, we will now turn to showing that the classical dynamics under an exponentially large A can implement an arbitrary quantum computation.
2. Solving the original problem using the dynamics of oscillators
As discussed above, the initial state we want to use is jl 1⁄4 1i ⊗ j0i⊗q ⊗ j−i. As a vector, this is a vector with the
first entry equal to þ1=pffi2ffiffi, the second entry equal to
−1=pffi2ffiffi, and the remaining entries zero. Using our problem’s encoding in Eq. (2), this corresponds to the initial state where y ̇1ð0Þ 1⁄4 1, y ̇2ð0Þ 1⁄4 −1,  ̇yjð0Þ 1⁄4 0 for all j > 2, ⃗xð0Þ 1⁄4 0, and E 1⁄4 1. This corresponds to all the oscillators starting at their rest positions, with the first oscillator having velocity þ1, the second one having velocity −1, and the remaining oscillators being stationary. When the initial conditions are such that ⃗xð0Þ 1⁄4 ð0; ...; 0ÞT, the solution to Newton’s equations is even easier to describe, and Eq. (11) implies
⃗ ̇xðtÞ 1⁄4 ⃗ ̇yðtÞ 1⁄4 Re
n
eipffiAffiffit ⃗ ̇yð0Þ
o
1⁄4 cos pffiffiAffiffit ⃗ ̇yð0Þ: ðC7Þ
In the rest of this section we want to understand the
behavior of ⃗ ̇yðtÞ for our initial conditions. We start by defining an N × N matrix A0, which is obtained from A in Eq. (C4) by replacing Wl → Ul ⊗ 12
when Ul is a Hadamard gate (i.e., A0 is allowed to have offdiagonal entries of both signs). We do this for simplicity to remove the dependence on the j−i state in the ancilla. Specifically, let Ul ∈ fH; X; Toffg and
A0 1⁄4 41N − L X
l1⁄41
ðjlihl þ 1j þ jl þ 1ihljÞ ⊗ Ul ⊗ 12: ðC8Þ
The block-encoding property of Eq. (C6) implies
⃗y ̇ðtÞ 1⁄4 cos pffiffiAffiffit ⃗y ̇ð0Þ
1⁄4 cos pffiffiAffiffit jl 1⁄4 1i ⊗ j0i⊗q ⊗ j−i
1⁄4 cos
ffiffiAffiffi0ffi
p
t jl 1⁄4 1i ⊗ j0i⊗q ⊗ j−i: ðC9Þ
That is, Wl and Ul ⊗ 12 act identically on the subspace specified by j−i. As a corollary, the velocities of the oscillators are such that the last register remains in j−i. The matrix A0 is also 4-sparse and satisfies A0 ≽ 0,
implying that ffiffiAffiffi0ffi
p is a well-defined N × N Hermitian matrix that is row computable. We define the N × N select unitary (U0 ≔ 12q),
S ≔ L X
l1⁄40
jl þ 1ihl þ 1j ⊗ Ul...U0 ⊗ 12; ðC10Þ
which implements the unitary in the circuit up to Ul when
the first register is jl þ 1i, i.e., a vector in RLþ1 with entry 1 in position l þ 1 and zeros elsewhere. Note that S and S† leave any vector represented as jl 1⁄4 1i ⊗ jψi, jψi ∈ C2qþ1, invariant. We also define the N × N Hermitian matrix:
X ≔ 41N − L X
l1⁄41
ðjlihl þ 1j þ jl þ 1ihljÞ ⊗ 12qþ1 : ðC11Þ
Then, by inspection of Eq. (C8), we obtain from the fact that each Ul in our gate set is Hermitian and unitary
A0 1⁄4 SXS†: ðC12Þ
Since U0 1⁄4 12q, for our initial conditions ⃗y ̇ð0Þ 1⁄4 jl 1⁄4
1i ⊗ j0i⊗q ⊗ j−i,
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-20


 ⃗ ̇yðtÞ 1⁄4 cos
ffiffiAffiffi0ffi
p
t jl 1⁄4 1i ⊗ j0i⊗q ⊗ j−i
1⁄4 S cos pffiffiXffiffit S†jl 1⁄4 1i ⊗ j0i⊗q ⊗ j−i
1⁄4 S cos pffiffiXffiffit jl 1⁄4 1i ⊗ j0i⊗q ⊗ j−i: ðC13Þ
Since X acts trivially on Hcomp ⊗ H2, it is useful to define
X0 ≔ 41Lþ1 − L X
l1⁄41
ðjlihl þ 1j þ jl þ 1ihljÞ; ðC14Þ
implying
⃗ ̇yðtÞ 1⁄4 S cos pffiffiXffiffit jl 1⁄4 1i ⊗ j0i⊗q ⊗ j−i
1⁄4S
h
cosð ffiffiXffiffi0ffiffi
p
tÞjl 1⁄4 1i
i
⊗ j0i⊗q ⊗ j−i: ðC15Þ
This compact expression for the vector of velocities is useful to show the desired result. In general, we can write
cos
ffiffiXffiffi0ffiffi
p
t jl 1⁄4 1i 1⁄4 LXþ1
l1⁄41
αlðtÞjli; ðC16Þ
with αlðtÞ ∈ R, because the Taylor expansion of the cosine
function has only even powers of ffiffiXffiffi0ffiffi
p . Then
⃗ ̇yðtÞ 1⁄4 S
h
cos
ffiffiXffiffi0ffiffi
p
t jl 1⁄4 1i
i
⊗ j0i⊗q ⊗ j−i
1⁄4 LXþ1
l1⁄41
αlðtÞjli ⊗ ðUl−1...U0j0i⊗qÞ ⊗ j−i: ðC17Þ
Hence, when the first register in the tensor product is l 1⁄4 L þ 1, the second register is UL...U1j0i⊗q, and recall that our goal was to decide if this state was close to or far from j0i⊗q. So if we measure the output state, in the case where the circuit’s output was close to j0i⊗q, we will see jL þ 1ij0i⊗q
with probability 1⁄21 − 1=expðpffiqffiffiÞ jαLþ1ðtÞj2 ≥ 1
2 jαLþ1ðtÞj2,
and if the circuit’s output had 1= expðpffiqffiffiÞ overlap with j0i⊗q, then we will see jL þ 1ij0i⊗q with at most
1= expðpffiqffiffiÞ probability. So all we have to show is that there exists a t 1⁄4 polylogðNÞ such that jαLþ1ðtÞj2 1⁄4 Ω(1=polylogðNÞ) 1⁄4 Ω(1=polyðqÞ), which will allow us to distinguish the two cases by using our algorithm O(polylogðNÞ) 1⁄4 polyðqÞ times.
3. Establishing inverse polynomial overlap
It is not too hard to establish inverse polynomial overlap jαLþ1ðtÞj2 1⁄4 Ω(1=polylogðNÞ) for t 1⁄4 polylogðNÞ. (In fact, it is possible to get perfect overlap as we discuss in the next section.) To prove this result, we use some
known results on the spectral properties of X0. Its eigenvectors are
jφli 1⁄4
ffiffiffiffiffiffiffiffiffiffiffiffi
2 Lþ2
r LXþ1
l0 1⁄41
sin πll0
L þ 2 jl0i; ðC18Þ
and the eigenvalues are
γl 1⁄4 4 − 2 cos πl
L þ 2 ; ðC19Þ
where l ∈ 1⁄2L þ 1 . Note that 6 > γl > 2. The jφli’s are also
the eigenvectors of ffiffiXffiffi0ffiffi
p , whose eigenvalues are γ0
l ≔ ffiγffiffilffi
p
and pffi6ffiffi > γ0
l > pffi2ffiffi. Let Δl 1⁄4 γlþ1 − γl be the spectral gaps
of X0 and note that Δl > 0 and Δl=γl > 0. The spectral
gaps of ffiffiXffiffi0ffiffi
p satisfy (for l ∈ 1⁄2L )
γ0lþ1 − γ0l ≥ π
L þ 2 min
x ∈ 1⁄2lπ=ðLþ2Þ;ðlþ1Þπ=ðLþ2Þ
d dx
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
4 − 2 cosðxÞ
p
1⁄4π
L þ 2 min
x ∈ 1⁄2lπ=ðLþ2Þ;ðlþ1Þπ=ðLþ2Þ
sinðxÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
4 − 2 cosðxÞ
p
≥π
L þ 2 min
x ∈ 1⁄2lπ=ðLþ2Þ;ðlþ1Þπ=ðLþ2Þ
sinpðffi2ffiffixÞ : ðC20Þ
This derivative is zero at x 1⁄4 0 and π, which is outside the region of values of x. The derivative will therefore take its smallest (nonzero) values at the nearest allowed values of x:
x1⁄4 π
L þ 2 and x 1⁄4 πðL þ 1Þ
L þ 2 : ðC21Þ
We have (L ≥ 1)
sin π
L þ 2 1⁄4 sin πðL þ 1Þ
L þ 2 ≥ p1ffi2ffiffi π
L þ 2 : ðC22Þ
Thus we have
γ0
lþ1 − γ0
l≥1
2
π Lþ2
2
: ðC23Þ
Hence, the smallest spectral gap of ffiffiXffiffi0ffiffi
p , Δ0 1⁄4 minlðγ0lþ1−
γ0lÞ, satisfies Δ0 1⁄4 Ωð1=L2Þ.
The amplitude αLþ1ðtÞ that we are interested in can be written as
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-21


 αLþ1ðtÞ 1⁄4 hL þ 1j cos
ffiffiXffiffi0ffiffi
p
t j1i
1⁄4
ffiffiffiffiffiffiffiffiffiffiffi
2 Lþ2
r
hL þ 1j cosð ffiffiXffiffi0ffiffi
p
tÞ LXþ1
l1⁄41
sin πl
L þ 2 jφli
1⁄42
Lþ2
LXþ1
l1⁄41
cosðγ0ltÞ sin πlðL þ 1Þ
L þ 2 sin πl
Lþ2
1⁄42
Lþ2
LXþ1
l1⁄41
ð−1Þl−1sin2 πl
L þ 2 cosðγ0ltÞ: ðC24Þ
Recall that the probability of measuring jL þ 1i after
evolving with ffiffiXffiffi0ffiffi
p for time t, when the initial state is j1i, is
jαLþ1ðtÞj2 1⁄4 2
Lþ2
2 LXþ1
l;l0 1⁄41
ð−1Þlþl0 sin2 πl
Lþ2 sin2 πl0
Lþ2
×1
4ðeitðγ0
l þγ 0
l0 Þ þeitðγ0
l −γ 0
l0 Þ þeitð−γ0
l þγ 0
l0 Þ þeitð−γ0
l −γ0
l0 ÞÞ;
ðC25Þ
where we used that cosðθÞ 1⁄4 1
2 ðeiθ þ e−iθÞ.
If l ≠ l0, Eq. (C23) implies jγ0
l −γ0
l0 j≥π2=1⁄22ðLþ2Þ2 ≥Δ0,
and jγ0l þ γ0
l0j ≥ 2pffi2ffiffi for all l, l0. Then, for any ε > 0, there
exists a probability distribution fðtÞ, where t ∈ f0; 1; ...; Tg and T 1⁄4 O(ðL þ 2Þ2 logð1=εÞ), such that fðtÞ ≥ 0,
PtT1⁄40 fðtÞ 1⁄4 1, and
T X
t1⁄40
fðtÞeitðγ0
l −γ 0
l0 Þ ≤ ε; ∀ l ≠ l0; ðC26Þ
T X
t1⁄40
fðtÞeitðγ0
l þγ 0
l0 Þ ≤ ε; ∀ l; l0: ðC27Þ
In other words, the absolute value of the Fourier transform of fðtÞ for frequencies ω such that jωj ≥ Δ0 is upper bounded by ε. One choice for fðtÞ is the probability distribution obtained by taking m 1⁄4 O(logð1=εÞ) samples ft1; ...; tmg from a uniform distribution where ti ∈ f0; 1; ...;
T0g, T0 1⁄4 OðL2Þ, and outputting t 1⁄4 P
i ti. Other choices can be found in Ref. [41]. This also implies
T X
t1⁄40
fðtÞX
l≠l0
ð−1Þlþl0 sin2 πl
L þ 2 sin2 πl0
L þ 2 eitðγ0
l −γ 0
l0 Þ ≤ εX
l≠l0
sin2 πl
L þ 2 sin2 πl0
Lþ2
1⁄4 ε ðL þ 2Þ2
4 − 3ðL þ 2Þ
8
≤ ε ðL þ 2Þ2
4 ; ðC28Þ
and
T X
t1⁄40
fðtÞX
l;l0
ð−1Þlþl0 sin2 πl
L þ 2 sin2 πl0
L þ 2 eitðγ0
l þγ 0
l0 Þ ≤ εX
l;l0
sin2 πl
L þ 2 sin2 πl0
Lþ2
1⁄4 ε ðL þ 2Þ2
4 : ðC29Þ
Hence, when we analyze PtT1⁄40 fðtÞjαLþ1ðtÞj2, the terms that dominate the sum are those that correspond to l 1⁄4 l0 in
Eq. (C25) and where the phases are e itðγ0
l −γ 0
l0Þ. That is, the above equations give
T X
t1⁄40
fðtÞjαLþ1ðtÞj2 − 1
2
T X
t1⁄40
fðtÞ 2
Lþ2
2 LXþ1
l1⁄41
sin4 πl
Lþ2 ≤2 2
Lþ2
2
ε ðL þ 2Þ2
4
≤ 2ε: ðC30Þ
The second term on the left-hand side can be computed and is 3=4ðL þ 2Þ, which gives
T X
t1⁄40
fðtÞjαLþ1ðtÞj2 − 3
4ðL þ 2Þ ≤ 2ε: ðC31Þ
Let us choose ε 1⁄4 1=1⁄24ðL þ 2Þ . This implies that the average PtT1⁄40 fðtÞjαLþ1ðtÞj2 is Ωð1=LÞ and recall that T 1⁄4 O ̃ ðL2Þ.
Then, there must exist a t 1⁄4  ̃OðL2Þ such that jαLþ1ðtÞj2 1⁄4 Ωð1=LÞ.
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-22


 Now we are done, since we can run the algorithm for all t 1⁄4 1; ...; T, since there are only polyðLÞ 1⁄4 polylogðNÞ values. Alternatively, we can find the desired t by simulat
ing ffiffiXffiffi0ffiffi
p for all times t 1⁄4 1; 2; ...; T on a classical computer at cost that is also polynomial in L or polylogðNÞ. Note that although our proof does not pin down a specific t for which this works, numerical simulations show that a fixed time t 1⁄4 OðLÞ suffices for any L.
4. Bonus: Establishing perfect overlap
While the argument above completes the proof of BQPcompleteness, we observe that it is also possible to obtain jαLþ1ðtÞj 1⁄4 1 in the proof above, which is equivalent to perfect transmission of a disturbance down a spin chain, which was solved in Refs. [42–44]. The principle is to adjust the weights of the operator X0 as
X0 1⁄4 L X
l1⁄40
bljl þ 1ihl þ 1j − L X
l1⁄41
ffiuffiffilffi
p ðjlihl þ 1j þ jl þ 1ihljÞ;
ðC32Þ
where we have adjusted the first sum to be consistent with the notation in Ref. [44]. The weights bl and ul are adjusted so that the eigenvalues are proportional to the squares of a sequence of integers. Provided the matrix is persymmetric
(so bl 1⁄4 bL−l and ul 1⁄4 uLþ1−l), then ei ffiXffiffi0ffi
p tj1i gives exactly jL þ 1i for some t. In particular, in Ref. [42], X0 has the eigenvalues 2k2 for k 1⁄4 0 to L, which gives the perfect
transfer for t 1⁄4 π=pffi2ffiffi. Here we cannot use that exact result, because that would imply certain values for the diagonal entries of X0 (and hence A) for which the Hamiltonian would not correspond to a system of coupled oscillators. For our case, it will suffice if the diagonal entries are at
least 2pffi2ffiffi times the off-diagonal entries. To obtain the larger on-diagonal entries we can use the analysis in terms of para-Racah polynominals in Ref. [44]. For odd L 1⁄4 2j þ 1, one takes [from Eq. (2.9) of Ref. [44], and using α 1⁄4 1=2]
bl 1⁄4
(1
2 1⁄2aða þ jÞ þ cðc þ jÞ þ lðL − lÞ if l ≠ j; j þ 1
a2 þ 1
2 jð1 þ a − cÞð1 þ a þ c þ jÞ − 1
2 ða − cÞð1 þ jÞða þ c þ jÞ if l 1⁄4 j; j þ 1; ðC33Þ
ul 1⁄4
8<
:
lðLþ1−lÞðL−lþaþcÞðl−1þaþcÞððl−j−1Þ2−ða−cÞ2Þ
4ðL−2lÞðL−2lþ2Þ if l ≠ j þ 1 1
4 ða − cÞ2ð1 þ jÞ2ða þ c þ jÞ2 if l 1⁄4 j þ 1:
ðC34Þ
We have flipped the sign of the matrix in Ref. [44] to be consistent with our usage here. The eigenvalues as per Eq. (3.11) of Ref. [44] are (again flipping the sign from that work)
λ2s 1⁄4 ðs þ aÞ2; s 1⁄4 0; ...; j;
λ2sþ1 1⁄4 ðs þ cÞ2; s 1⁄4 0; ...; j: ðC35Þ
We then get the appropriate set of eigenvalues if a − c 1⁄4 1=2. The matrix is persymmetric if α 1⁄4 1=2. We will also use Lþ 1⁄4 L þ 1 in the notation to simplify the form of the expressions. Taking a 1⁄4 Lþ=2 þ 1=4 and c 1⁄4 Lþ=2 þ 3=4, we obtain
4bl 1⁄4 5L2þ=2 − 1=4 − 2ðl − L=2Þ2; ðC36Þ
16ul 1⁄4 lð2Lþ − lÞðL2þ − l2Þ: ðC37Þ
Exactly the same result is obtained for odd L 1⁄4 2j using the expressions in Eq. (4.4) of Ref. [44]. In either case it is found that the eigenvalues are 1
4 ðL þ k þ 1=2Þ2 for k 1⁄4 0
to L. Then one can evolve directly to l 1⁄4 L þ 1 for t 1⁄4 2π, so that jαLþ1ð2πÞj 1⁄4 1. Alternatively, one can divide the X0
given here by L2 so the coefficients are Oð1Þ, and evolve for time 2πL. For the relative values of bl and ul, we need to show
bl ≥ pffi2ffiffið ffiuffiffilffi
p þ ffiffiffiffiffiffiffiffiffi
ulþ1
p Þ; ðC38Þ
for l 1⁄4 0 to L. Here we use the convention that u0 1⁄4 0,
which is given by the formula above. For l 1⁄4 0 we
want b0 ≥ ffiffiffiffiffiffiffi
2u1
p , so Eq. (C38) can still be used with the convention u0 1⁄4 0. Note that both bl and ul take their maximum values in the center, but bl is nonzero at the boundaries whereas ul is close to zero. This
means that bl= ffiuffiffilffi
p is smallest for l 1⁄4 L=2, and there the ratio is approximately 10=3, which is significantly
larger than 2pffi2ffiffi. To show this inequality more rigorously, we can use the concavity of ul as a function of l and the concavity of the square root function to give
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-23


 ffiffiffiffiffiffiffiffiffiffiffiffiffiffi 8u
lþ1=2
q ≥
ffiffiffi
2
p
ð
ffiffiffiffi
u
l
p
þ
ffiffiffiffiffiffiffiffiffi
u
lþ1
p
Þ; ðC39Þ
where u
lþ1=2
is using the same function of l (even though it is only meaningful to give coefficients for integer l). We find that
b
2
l
− 8u
lþ1=2
1⁄4 1 þ 16ðL
4
þ
−L
2
þ
Þ1⁄21 þ ð1 − βÞβ
þ 16L
4
þ
(3 − βf9 − β1⁄25 þ 4ð2 − βÞβ g);
ðC40Þ
with β 1⁄4 ðl þ 1=2Þ=L
þ
. Because we consider values of l ∈ 1⁄20; L , we need only consider β ∈ 1⁄20; 1 . The expression (3 − βf9 − β1⁄25 þ 4ð2 − βÞβ g) is positive; it has its minimum of 1=2 at β 1⁄4 1=2. The expression L
4
þ
−L
2
þ
is nonnegative, and 1 þ ð1 − βÞβ is positive for β ∈ 1⁄20; 1 . As a result,
b
2
l
≥ 8u
lþ1=2
⇒b
l
≥
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi 8u
lþ1=2
q ≥
ffiffiffi
2
p
ð
ffiffiffiffi
u
l
p
þ
ffiffiffiffiffiffiffiffiffi
u
lþ1
p
Þ; ðC41Þ
as required.
APPENDIX D: PHASE ESTIMATION APPROACH AND PROOF OF THEOREM 4
We provide proof of Theorem 4, which provides a method for simulating the dynamics of a broader family of classical systems under the harmonic approximation than the previous method described in Theorem 1, at the price of reduced scaling with the desired error tolerance ε. Proof of Theorem 4. We describe the simulation of H 1⁄4 −X ⊗
ffiffiffiffi
A
p
, where X is the single-qubit Pauli bit flip operator and
ffiffiffiffi
A
p
is the principal square root of A, using a standard quantum phase estimation (QPE) approach. In this approach, we run QPE with a unitary that is a walk operator built from a block encoding of H
ð2Þ
≔ −X ⊗ A, i.e., a unitary that contains H
ð2Þ
=Λ in a block, where Λ > 0 is due to normalization reasons. This QPE provides estimates of the eigenvalues of the walk operator, which can be converted into estimates of the eigenvalues of H
ð2Þ
and ultimately of H. Once these estimates are obtained, simulation of H is simply applying a phase that is a product of the eigenvalue estimate and t. Last, we reverse QPE and other calculations to uncompute the estimated eigenvalues. In the case where we have oracle access to K, then A 1⁄4 BB
†
and we can obtain a block encoding of A—and hence of H
ð2Þ
—from the block encodings of B and B
†
. These were given in Appendix A. This approach would imply Λ 1⁄4 2אd. In the case of generalized coordinates described in Sec. VII, where we assume oracle access to d-sparse A but not K, then H
ð2Þ
can be block encoded using standard methods with Λ 1⁄4 OðkH
ð2Þ
k
max
dÞ 1⁄4 OðkAk
max
dÞ [24]. Let jλ
j
i denote the eigenvectors of A of eigenvalue
λ
j
≥ 0. Then, we can write jη
X
ijλ
j
i 1⁄4 jη
X
;λ
j
i for the
eigenvectors of H
ð2Þ
, where η ∈ f0; 1g, and j0
X
i 1⁄4 j−i and j1
X
i 1⁄4 jþi are the eigenvectors of X. The corresponding eigenvalues of H
ð2Þ
are γ
η;j
≔ ð−1Þ
η
λ
j
. Our first step is to estimate the eigenvalue γ
η;j
within fixed error, and then propagate that error into the maximum error that can be observed in ð−1Þ
η
ffiffiffiffi
λ
j
p
, which is the corresponding eigenvalue of H, using an arithmetic circuit on the outputs of the QPE routine. Phase estimation can be used to provide a confidence interval S
η;j
for the eigenvalue estimates of H
ð2Þ
, which we call x. That is, for all x ∈ S
η;j
that are estimates of γ
η;j
, and for a given ε
PE
, we define ε
η;j
ðxÞ ≔ x−γ
η;j
and S
η;j
≔ fx∶ε
η;j
ðxÞ ∈ 1⁄2−ε
PE
;ε
PE
g. To describe the contribution to estimates outside the confidence interval, we use a state jφ
η;j
i of unit norm and an amplitude
ffiffiffiffiffiffiffi
δ
η;j
p
, where δ
η;j
> 0 depends on η and j, and 1 − δ
η;j
is the confidence level when the input state is jη
X
;λ
j
i. Eventually, we will set δ
η;j
≤δ
PE
for all η and j, where δ
PE
> 0 is determined below. Then, when implementing QPE on input eigenstate jη
X
;λ
j
i and using a unitary that provides
eigenvalue estimates of H
ð2Þ
(e.g., a walk operator), the state is approximately transformed as
jη
X
;λ
j
i ↦ jη
X
;λ
j
i
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1−δ
η;j
p
X
x∈S
η;j
b
x
jxi þ
ffiffiffiffiffiffiffi
δ
η;j
p
jφ
η;j
i;
ðD1Þ
for some unit vector
⃗
b that gives the probability distribution jb
x
j
2
for phase estimates within the confidence interval (the states jxi can be basis states that encode the estimates of γ
η;j
). When performing QPE using Kaiser windows [34], the number of invocations of the walk operator (i.e., the query complexity) built from the block encoding of H
ð2Þ
is then [45]
O(Λ logð1=δ
PE
Þ=ε
PE
) 1⁄4 O(kAk
max
d logð1=δ
PE
Þ=ε
PE
):
ðD2Þ
The walk operator we use in QPE combines the block encoding of H
ð2Þ
with other 2-qubit gates, including a reflection on some ancilla qubits [46]. That is, each use of the walk operator requires Oð1Þ uses of the oracle to access A. The eigenvalues of the walk operator are then ∓e
i arcsinðλ
j
=ΛÞ
. The actual eigenvalues of H
ð2Þ
, which are γ
η;j
, can be estimated by QPE using the walk operator, then taking the sine of the result to give an estimate of γ
η;j
=Λ. Note that jγ
η;j
j=Λ ≤ 1 for all η ∈ f0; 1g and j ∈ 1⁄2N . Aiming for ε
PE
=Λ uncertainty in the phase estimation of arcsinðλ
j
=ΛÞ yields the following estimate in γ
η;j
=Λ:
jγ
η;j
=Λ − sin1⁄2arcsinðγ
η;j
=ΛÞ þ ε
PE
=Λ j ≤ ε
PE
=Λ: ðD3Þ
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-24


 Then, in QPE we are first obtaining an estimate x 1⁄4 γη;jþ εη;jðxÞ, where the error εη;jðxÞ satisfies jεη;jðxÞj ≤ εPE within a ð1 − δPEÞ confidence level. We want to convert this estimate into an estimate of an eigenvalue of H, i.e., an
estimate of ð−1Þη ffiλffiffijffi
p 1⁄4 sgnðγη;jÞ ffiffiffiffiffiffiffiffiffi
jγη;jj
p , which is obtained
by computing sgnðxÞ ffijffixffiffijffi
p . This gives the error
Δη;jðxÞ ≔ sgnðxÞ ffijffixffiffijffi
p − sgnðγη;jÞ
ffiffiffiffiffiffiffiffiffi jγη;jj
q
1⁄4 sgn1⁄2γη;j þ εη;jðxÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi jγη;j þ εη;jðxÞj
q
− sgnðγη;jÞ
ffiffiffiffiffiffiffiffiffi jγη;jj
q
; ðD4Þ
which we seek to bound. In the case where γη;j ≥ 0 (i.e., η 1⁄4 0 and γη;j 1⁄4 λj), we have
jΔη;jðxÞj 1⁄4 sgn1⁄2λj þ εη;jðxÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi jλj þ εη;jðxÞj
q −
ffiffiffiffi λj
q
; ðD5Þ
and in the case where γη;j ≤ 0 (i.e., η 1⁄4 1 and γη;j 1⁄4 −λj), we have
jΔη;jðxÞj 1⁄4 sgn1⁄2−λj þ εη;jðxÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi j − λj þ εη;jðxÞj
q þ
ffiffiffiffi λj
q :
ðD6Þ
If we replace εη;jðxÞ with −εη;jðxÞ this becomes
sgn1⁄2λj þ εη;jðxÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi jλj þ εη;jðxÞj
q −
ffiffiffiffi λj
q
; ðD7Þ
and so bounding the expression for the case η 1⁄4 0 will be sufficient to account for all cases. To find the bound for this case we will show that for any a ∈ R,
sgnð1 þ aÞ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p − 1 ≤ pffi2ffiffi minðjaj;
ffijffiffiaffiffijffi
p Þ: ðD8Þ
There are four cases to consider to prove this expression.
(1) For a ≥ 1, we can prove the inequality by using
1 þ a ≤ 1 þ a þ 2pffiaffiffi ⇒ ffiffiffiffiffiffiffiffiffiffiffi
1þa
p ≤ 1 þ pffiaffiffi
⇒ ffiffiffiffiffiffiffiffiffiffiffi
1þa
p − 1 ≤ pffiaffiffi
⇒ sgnð1 þ aÞ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p − 1 ≤ ffijffiffiaffiffijffi
p
: ðD9Þ
Since ffijffiffiaffiffijffi
p ≤ jaj for a ≥ 1, this proves the inequality. (2) For a ∈ 1⁄20; 1 , we can use
ffiffiffiffiffiffiffiffiffiffiffi
1þa
p ≤ 1 þ a ⇒ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p − 1 ≤ jaj
⇒ sgnð1 þ aÞ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p − 1 ≤ jaj: ðD10Þ
Since jaj ≤ ffijffiffiaffiffijffi
p for a ∈ 1⁄20; 1 , this proves the inequality.
(3) For a ∈ 1⁄2−1; 0 ,
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p ≥ j1 þ aj ⇒ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p −1≥a
⇒ 1 − ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p ≤ −a ⇒ sgnð1 þ aÞ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p − 1 ≤ jaj: ðD11Þ
Again for a ∈ 1⁄2−1; 0 we can use jaj ≤ ffijffiffiaffiffijffi
p . This time we need to take the absolute value because ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p ≤ 1. (4) For a ≤ −1, we can use
0 ≤ ðjaj − 2Þ2 ⇒ 4ðjaj − 1Þ ≤ a2
⇒ 2 ffiffiffiffiffiffiffiffiffiffiffiffiffi
jaj − 1
p ≤ jaj
⇒ ðjaj − 1Þ þ 2 ffiffiffiffiffiffiffiffiffiffiffiffiffi
jaj − 1
p þ 1 ≤ 2jaj
⇒ ffiffiffiffiffiffiffiffiffiffiffiffiffi
jaj − 1
p þ 1 ≤ ffiffiffiffiffiffiffiffi
2jaj
p
⇒ sgnð1 þ aÞ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
j1 þ aj
p − 1 ≤ ffiffiffiffiffiffiffiffi
2jaj
p : ðD12Þ
That also implies that it is upper bounded by pffi2ffiffijaj.
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-25


 The result gives us the bound on the error in the signed square root as follows:
Δη;j ≔ max
x∶jx−γ η;j j≤εPE
jΔη;jðxÞj ≤ min εPE
ffiffiffiffiffiffiffiffiffi 2=λj
q
; ffiffiffiffiffiffiffiffiffi
2εPE
p:
ðD13Þ
Hence, from the estimate x of γη;j within error at most εPE,
we can compute an estimate of ð−1Þη ffiλffiffijffi
p , the eigenvalue of H, within error at most Δη;j as above.
To implement eitX⊗pffiAffiffi
, we apply a phase factor proportional to the estimated eigenvalue from QPE. Then the state after applying the phase factor is transformed as
jηX; λji ↦ jηX; λji ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
pX
x ∈ Sη;j
bxe−itsgnðxÞ jffiffixffiffij
p
jxi þ ffiffiffiffiffiffiffi
δη;j
p jφη;j0i
1⁄4 e−itð−1Þη ffiλffijffi
p
jηX; λji ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
pX
x ∈ Sη;j
bxe−itΔη;jðxÞjxi þ ffiffiffiffiffiffiffi
δη;j
p jφη;j0i
1⁄4 e−itð−1Þη ffiλffijffi
p
jηX; λji ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
pX
x ∈ Sη;j
bxjxi þ ffiffiffiffiffiffiffi
δη;j
p jφη;ji
þ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
pX
x ∈ Sη;j
bxðe−itΔη;jðxÞ − 1Þjxi þ ffiffiffiffiffiffiffi
δη;j
p ðjφη;j0i − jφη;jiÞ : ðD14Þ
The states jφη;ji and jφ0η;ji are states of the ancillas of unit
norm, supported in the space orthogonal to fjxi∶x ∈ Sη;jg. After the phase was applied, we need to invert QPE. The inverse phase estimation and projection onto the zero state of the ancillas that were used to estimate the eigenvalues corresponds to applying
hλ ̃η;jj 1⁄4 X
x ∈ Sη;j
bxhxj; ðD15Þ
to give
e−itð−1Þη ffiλffijffi
p
jηX; λji ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
p þ ffiffiffiffiffiffiffi
δη;j
p hλ ̃η;jjφη;ji
þ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δη;j
pX
x ∈ Sη;j
jbxj2ðe−itΔη;jðxÞ − 1Þ
þ ffiffiffiffiffiffiffi
δη;j
p ðhλ ̃η;jjφ0η;ji − hλ ̃η;jjφη;jiÞ : ðD16Þ
The error can be bounded from the Euclidean distance between the above state and the correct state
e−itð−1Þη ffiλffijffi
p
jηX; λji. Using δη;j ≤ δPE, this distance is upper bounded by
1 − ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δPE
p þ 3 ffiffiffiffiffiffiffi
δPE
p þ ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 − δPE
p he−itΔη;jðxÞ − 1i; ðD17Þ
where the expectation value is on the probability distribution given by jbxj2. This can be further upper bounded by
mη;ajxΔη;jt þ 4 ffiffiffiffiffiffiffi
δPE
p : ðD18Þ
To appropriately bound the error by ε as required by Problem 4 we can take
4 ffiffiffiffiffiffiffi
δPE
p 1⁄4 ε=2; ðD19Þ
so δPE 1⁄4 ε2=64. Because measurement of the phase with this confidence level has a factor O( logð1=δPEÞ) in the complexity in Eq. (D2), it corresponds to a factor of O( logð1=εÞ). Then for
mη;ajxΔη;j ≤ mη;ajx min εPE
ffiffiffiffiffiffiffiffiffi 2=λj
q
; ffiffiffiffiffiffiffiffiffi
2εPE
p
1⁄4 min εPE
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2=mjinλj
q ; ffiffiffiffiffiffiffiffiffi
2εPE
p ; ðD20Þ
to satisfy maxη;j Δη;jt ≤ ε=2, we can take
εPE 1⁄4 max ε ffiffiffiffiffiffiffiffiffiffiffiffiffi
minjλj
p
2tpffi2ffiffi ; ε2
8t2 : ðD21Þ
Using these expressions in Eq. (D2) gives us an overall query complexity,
O(kAkmaxd logð1=εÞ min t ffiffiffiffiffiffiffiffiffiffiffiffiffi
kA−1k
p
ε ; t2
ε2 ); ðD22Þ
for the phase estimation approach. This is the stated result. There are further elementary 2-qubit gates arising from three main areas.
(1) Computing sgnðxÞ ffijffixffiffijffi
p , the estimate of the eigenvalue of H, multiplying by t, and then applying the phase factor. The dominant complexity is that from
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-26


 computing the square root, which scales using Newton iteration and textbook multiplication as  ̃O(log2ð1=εÞ). The phase rotation then requires a linear number of controlled rotation gates based on the target, which in turn requires at most O( logð1=εÞ) 2-qubit gates to implement. Thus the former cost dominates. (2) The gates for the implementation of the block encoding will be logarithmic in N and the allowable error of the block encoding. Because the allowable error in the block encoding needs to be ε divided by the number of block encodings in the phase estimation, there will be logarithmic factors in many of the parameters here. (3) The gate complexity of preparing the control states for phase estimation with optimal confidence intervals is at most linear in the dimension of this control register [47], which is the same as the number of oracle calls. This is the least significant contribution to the complexity and gives no logarithmic factors. In quoting the complexity we give the logarithmic factor in N coming from implementing the block encoding, but for simplicity use  ̃O and do not explicitly give the logarithmic factors in other parameters. ▪
APPENDIX E: INITIAL STATE PREPARATION
Our algorithm for solving Problem 1 accepts as input a circuit W that prepares an initial state of the form in Eq. (2) for t 1⁄4 0. In this appendix we explain how we might create such a circuit given only the ability to separately create superpositions over the initial positions and initial velocities. Our construction is related to that in Lemma 8 of Appendix A. As in Sec. IV, we consider a setting where the N × N matrices M and K can be queried through the use of a unitary S that gives the positions and nonzero entries of these matrices. Lemma 10. Let K be the N × N symmetric and d-sparse matrix of spring constants, κmax ≥ κjk ≥ 0, M≻0 be the N × N diagonal matrix of masses, and mmax ≥ mj > 0, where κmax and mmax are known. Assume we are given access to K and M through an oracle S, and access to a unitary U that performs the map
αj0i ↦ j0ij⃗x ̇ð0Þi; βj1i ↦ j1ij⃗xð0Þi;
where
j⃗x ̇ð0Þi 1⁄4 N X
j1⁄41
 ̇xjð0Þjji; j⃗xð0Þi 1⁄4 N X
j1⁄41
xjð0Þjji
are normalized states that encode the initial states of the oscillators in their amplitudes, and α and β are known norms of the vectors ⃗ ̇xð0Þ and ⃗xð0Þ, respectively. Then,
there exists a quantum algorithm that prepares a state that is ε-close in Euclidian norm to
jψð0Þi 1⁄4 ffi12ffiffiffiEffiffi
p
pffiffiMffiffiffi⃗ ̇xð0Þ
i⃗μð0Þ ; ðE1Þ
where E > 0 is a known constant (the energy of the classical oscillators) and ⃗μð0Þ ∈ RM for M 1⁄4 NðN þ 1Þ=2 is a vector
whose entries are ffiκffiffijffijffiffi
p xjð0Þ or ffiκffiffijffikffiffi
p (xjð0Þ − xkð0Þ), k > j.
The quantum circuit makes Qini 1⁄4 Oð ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Emaxd=E
p Þ uses of U, S, and its inverses, in addition to
Gini 1⁄4 O( ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Emaxd=E
p × polylogðNEmax=ðEεÞÞ) ðE2Þ
2-qubit gates. Here Emax 1⁄4 ðmmax=2Þ P
j (x ̇jð0Þ)2þ
ðκmax=2Þ P
j (xjð0Þ)2 is the energy of a system of N uncoupled oscillators where all masses are mmax and all individual spring constants are κmax, and for the same initial conditions. Proof. For ease of implementation, we can encode the state on 2n þ 1 qubits, where n 1⁄4 logðNÞ. In this space, the initial state is represented as
jψð0Þi 1⁄4 ffi12ffiffiffiEffiffi
pX
j
ffiffimffiffijffiffi
p  ̇xjð0Þjjij0i þ i
X
j
ffiκffiffijffijffiffi
p xjð0Þjjijji
þi
X
j<k
ffiκffiffijffikffiffi
p (xjð0Þ − xkð0Þ)jjijki : ðE3Þ
First we rotate a qubit and apply the state preparation oracle as
j0i ↦ 1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
p ð ffiffiffiffiffiffiffiffiffiffi
mmax
p αj0i þ i ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2κmaxd
p βj1iÞ
↦1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
p 1⁄2 ffiffiffiffiffiffiffiffiffiffi
mmax
p αj0ij ⃗ ̇xð0Þi
þ i ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2κmaxd
p βj1ij ⃗xð0Þi : ðE4Þ
The way we have described the oracle for ⃗ ̇xð0Þ and ⃗xð0Þ allows for the case where α or β may be zero, in which case U can be arbitrary on that subspace because it has no effect
on the state above. Then our goal is to apply pffiffiMffiffiffi to the
j⃗ ̇xð0Þi portion, and B†pffiffiMffiffiffi to the j⃗xð0Þi portion.
The most challenging part is for applying B†pffiffiMffiffiffi. To do this, we essentially apply the same construction in Lemma
8 in Appendix A, but for block encoding B†pffiffiMffiffiffi rather than B†. First consider the operation where we prepare a superposition over d values in an ancilla to give
j⃗xð0Þi p1ffidffiffi Xd
l1⁄41
jli: ðE5Þ
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-27


 This preparation is simple if d is a power of 2, and otherwise can be performed using Oðlog dÞ 1⁄4 OðnÞ gates via amplitude amplification (see Appendix E.2 of Ref. [34]). We can then apply the oracle for the positions of nonzero entries of K to map k to the nonzero entry in row j, and obtain
p1ffidffiffi N X
j1⁄41
xjð0Þjji X
k ∈ 1⁄2N ∶κjk≠0
jki: ðE6Þ
There may be less than d values of k for each j such that κjk ≠ 0, but the oracle may be chosen to give dummy values of k to pad it out to d. These will later be eliminated because κjk is actually zero for those values of j, k.
In the usual way, we can use the oracle for the matrix entries of κjk to output its value, and perform an inequality test with an ancilla in an equal superposition to apply a
factor corresponding to ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
κjk=κmax
p (which is no greater than 1) [38]. This will give us, with an amplitude corresponding to the amplitude for success,
ffiffiffi1ffiffiffiffiffiffiffiffi
κmaxd
pX
j;k
ffiκffiffijffikffiffi
p xjð0Þjjijki: ðE7Þ
We then perform an inequality test, and perform a controlled swap based on the result of the inequality test. This gives the state
ffiffiffi1ffiffiffiffiffiffiffiffi
κmaxd
p N X
j1⁄41
ffiκffiffijffijffiffi
p xjð0Þjjijjij0i þ X
k>j
ffiκffiffijffikffiffi
p xjð0Þjjijkij0i þ X
k<j
ffiκffiffijffikffiffi
p xjð0Þjjijkij1i ; ðE8Þ
where the third register is the qubit flagging the result of the inequality test. Then we perform a Z gate on that qubit and relabel the third sum to give
ffiffiffi1ffiffiffiffiffiffiffiffi
κmaxd
p N X
j1⁄41
ffiκffiffijffijffiffi
p xjð0Þjjijjij0i þ X
j<k
ffiκffiffijffikffiffi
p jjijki(xjð0Þj0i − xkð0Þj1i) : ðE9Þ
Projecting onto the jþi state on the ancilla qubit then gives
ffiffiffiffiffi1ffiffiffiffiffiffiffiffiffi
2κmaxd
p N X
j1⁄41
ffiκffiffijffijffiffi
p xjð0Þjjijji þ X
j<k
ffiκffiffijffikffiffi
p (xjð0Þ − xkð0Þ)jjijki ; ðE10Þ
where the amplitude is indicating the amplitude for success.
To apply pffiffiMffiffiffi to the j⃗ ̇xð0Þi portion, we can simply perform the same inequality testing procedure from Ref. [38] to apply
a factor of ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mj=mmax
p , and give
j⃗ ̇xð0Þi ↦ ffiffiffi1ffiffiffiffiffiffiffi
mmax
p
N X
j1⁄41
ffiffimffiffijffiffi
p  ̇xjð0Þjji: ðE11Þ
Combined, the preparation on these two parts of the state gives
1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
p ( ffiffiffiffiffiffiffiffiffiffi
mmax
p αj0ij⃗ ̇xð0Þi þ i2 ffiffiffiffiffiffiffiffiffiffiffi
κmaxd
p βj1ij⃗xð0Þi)
↦1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
p N X
j1⁄41
ffiffimffiffijffiffi
p x ̇jð0Þj0ijjij0iþi
N X
j1⁄41
ffiκffiffijffijffiffi
p xjð0Þj1ijjijji þ i
X
j<k
ffiκffiffijffikffiffi
p (xjð0Þ − xkð0Þ)j1ijjijki ;
ðE12Þ
which is the correct state [Eq. (E3)], but subnormalized indicating that it is not produced deterministically and we need to use amplitude amplification. The number of amplitude amplification rounds scales as the inverse of the amplitude, so the complexity in terms of α, β, E is
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-28


 O
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2 2E
r
: ðE13Þ
We assume we know the constants for this lemma to simplify the amplitude amplification. It is also possible to perform amplitude amplification when the amplitude is unknown but bounded [48]. Note that
1
2 mmaxα2 1⁄4 1
2
N X
j1⁄41
mmax( ̇xjð0Þ)2 ðE14Þ
≕ Kmax; ðE15Þ
which is the kinetic energy of the system of oscillators at t 1⁄4 0 if all masses were mj 1⁄4 mmax. Also,
1
2 κmaxβ2 1⁄4 1
2
N X
j1⁄41
κmax(xjð0Þ)2 ðE16Þ
≕ Umax ðE17Þ
is the potential energy of a system of N uncoupled oscillators at t 1⁄4 0 if all spring constants were κjj 1⁄4 κmax and κjk 1⁄4 0
if j ≠ k. If Emax 1⁄4 Kmax þ Umax 1⁄4 ðmmax=2Þk⃗x ̇ð0Þk2 þ
ðκmax=2Þk⃗xð0Þk2 is the total energy of such a system, it satisfies
mmaxα2 þ 2κmaxdβ2 ≤ 4Emaxd: ðE18Þ
The number of amplitude amplification rounds is then
Oð ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Emaxd=E
p Þ. Each amplitude amplification round makes two uses of S, S†, and also one use of U and U†. Hence, the overall query complexity of our algorithm that prepares jψð0Þi is
Qini 1⁄4 O
ffiffiffiffiffiffiffiffiffiffiffiffi
Emaxd
E
r
: ðE19Þ
To find the accuracy of the block encoding we need to account for the error due to applying the factors of
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
κjk=κmax
p and ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mj=mmax
p by inequality testing. If we give the maximum errors in these factors as δ [corresponding to logð1=δÞ bits in the inequality testing], then the error in Eq. (E12) is upper bounded as
1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
pX
j
δ ffiffiffiffiffiffiffiffiffiffi
mmax
p x ̇jð0Þj0ijjij0i þ X
j
δ ffiffiffiffiffiffiffiffiffi
κmax
p xjð0Þj1ijjijji þ X
j<k κjk ≠0
δ ffiffiffiffiffiffiffiffiffi
κmax
p (xjð0Þ − xkð0Þ)j1ijjijki
≤1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
p mmax
N X
j1⁄41
δx ̇ j ð0Þjji
2
þ κmax
X
j≤k κjk ≠0
δxjð0Þjjijki − X
j>k κjk ≠0
δxjð0Þjkijji
2 1=2
≤δ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
p mmax ⃗x ̇jð0Þ
2
þ κmax
pffi2ffiffi X
j;k;κjk ≠0
xjð0Þjjijki
2 1=2
≤δ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
mmaxα2 þ 2κmaxdβ2
p mmax ⃗x ̇ð0Þ
2
þ 2κmaxd ⃗xð0Þ
2 1=2
1⁄4 δ: ðE20Þ
The inequality on the third line is obtained by noting that we can move from the state on the third line to that on the second line by the procedure described above, with an inequality test between j and k, a controlled swap and phase, then projection onto jþi on the ancilla. Thus, δ corresponds to the error before amplitude amplification,
and it is amplified by a factor of Oð ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Emaxd=E
p Þ.
If we are aiming for error ε in the state preparation, we should therefore take
δ1⁄4O ε
ffiffiffiffiffiffiffiffiffiffiffiffi E
Emaxd
s
: ðE21Þ
Because the state preparation by inequality testing uses squares, we have a gate complexity that is the square of
logð1=δÞ for each step of amplitude amplification, and therefore the gate complexity from this source is
O(
ffiffiffiffiffiffiffiffiffiffiffiffi
Emaxd
E
r
log2 Emaxd
Eε ): ðE22Þ
Moreover, there are O( logðNÞ) gates needed to implement an inequality test and controlled swap for each step of amplitude amplification. Using d ≤ N, we can give the overall gate complexity as
O(
ffiffiffiffiffiffiffiffiffiffiffiffi
Emaxd
E
r
log2 EmaxN
Eε ); ðE23Þ
which are the stated results. ▪
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-29


 The factor Emax=E in the complexity can become large when the masses mj or spring constants κjk lack uniformity. In this case, the state jψð0Þi is more complicated, and one has to “pay extra” for its preparation. In addition, the query complexity in Lemma 10 matches a lower bound for some instances. For example, consider the case where xjð0Þ 1⁄4 0
for all j ∈ 1⁄2N , which implies β2 1⁄4 0, and x ̇jð0Þ 1⁄4 1=pffiffiNffiffi for all j ∈ 1⁄2N , which implies α2 1⁄4 1. Let the masses be mj 1⁄4 1, for some unknown j, and mj0 1⁄4 0 otherwise. Then, jψð0Þi is simply a state jji in a computational basis, and our state preparation algorithm would output the unknown j with high probability, as in the unstructured search problem [49]. A lower bound on the query complex
ity for this case is ΩðpffiffiNffiffiÞ [50]. Since Emax 1⁄4 1
2 mmaxα2 1⁄4 1
2,
E1⁄41
2 1⁄2 ̇xjð0Þ 2 1⁄4 1
2N, and d 1⁄4 1 for this instance, the query
complexity of our approach is OðpffiffiNffiffiÞ, matching the lower bound.
APPENDIX F: OTHER ENCODINGS
In Sec. III, we choose a specific encoding for the position and velocities as a quantum state jψi in Eq. (14), which satisfies Eq. (13). Let jψðtÞi ∈ CNþM be written as
jψðtÞi 1⁄4 ⃗νðtÞ
i⃗μðtÞ ; ðF1Þ
where ⃗νðtÞ ∈ CN and i⃗μðtÞ ∈ CM. We made the choice of ⃗νðtÞ 1⁄4 ⃗ ̇yðtÞ and ⃗μðtÞ 1⁄4 B†⃗yðtÞ to present our main results. Nevertheless, other choices also work, and we now discuss another solution (and problem). This provides us with a new encoding that is different from the one we used in Problem 1, and is closely related to the encoding used in Ref. [11]. Let ⃗νðtÞ 1⁄4 P⃗yðtÞ, where P projects out the components of ⃗yðtÞ corresponding to the null space of A (or B†). Let ⃗μðtÞ1⁄4−BþP ⃗y ̇ðtÞ, where Bþ is the Moore-Penrose pseudoinverse of B. This is an M × N matrix that satisfies BBþB 1⁄4 B and Bþ 1⁄4 B†ðBB†Þþ 1⁄4 B†Aþ. We claim that
this choice also satisfies Eq. (13). Specifically, we want it to satisfy
⃗ ̇νðtÞ
i⃗ ̇μðtÞ 1⁄4 −iH ⃗νðtÞ
i⃗μðtÞ 1⁄4 −B⃗μðtÞ
iB†⃗νðtÞ : ðF2Þ
We then have
⃗ ̇νðtÞ 1⁄4 P ⃗y ̇ðtÞ 1⁄4 AAþP ⃗ ̇yðtÞ 1⁄4 BBþP ⃗ ̇yðtÞ 1⁄4 −B ⃗μðtÞ; ðF3Þ
which establishes the first component of Eq. (F2). Note that AAþP 1⁄4 P, since Aþ does not act on eigenvectors of A of eigenvalue zero. Using Newton’s equations [Eq. (9)], we have
i⃗μ ̇ ðtÞ 1⁄4 −iBþP̈⃗yðtÞ 1⁄4 iBþPA⃗yðtÞ 1⁄4 iBþAP⃗yðtÞ
1⁄4 iB†AþAP⃗yðtÞ 1⁄4 iB†P⃗yðtÞ 1⁄4 iB†⃗νðtÞ; ðF4Þ
which establishes the second component in Eq. (F2). Hence, evolution under H also allows us to solve the following variation of Problems 1 and 4. Problem 8. Let A ≽ 0 be an N × N real-symmetric, positive semidefinite, and d-sparse matrix, and B an N × M matrix that satisfies BB† 1⁄4 A. Define the normalized state,
jψðtÞi ≔ ffi1ffiffiffiffiffi
2F
p P⃗yðtÞ
−iBþP⃗ ̇yðtÞ ; ðF5Þ
where F > 0 is a constant, P is the projector onto the subspace orthogonal to the null space of A, and Bþ is the Moore-Penrose pseudo-inverse of B. Assume we are given oracle access to A and to a unitary W that prepares the initial state jψð0Þi. Given t and ε, the goal is to output a state that is ε-close to jψðtÞi in Euclidean norm. Note that the normalizing constant is
F1⁄41
2 ⃗yðtÞTP⃗yðtÞ þ 1
2
⃗ ̇yðtÞTPðBþÞ†BþP⃗y ̇ðtÞ; ðF6Þ
which satisfies
2F ̇ 1⁄4 ⃗y ̇ðtÞTP⃗yðtÞ þ ⃗yðtÞTP⃗ ̇yðtÞ þ ̈⃗yðtÞTPðBþÞ†BþP⃗ ̇yðtÞ þ ⃗y ̇ðtÞTPðBþÞ†BþP̈⃗yðtÞ
1⁄4 ⃗y ̇ðtÞTP⃗yðtÞ þ ⃗yðtÞTP⃗ ̇yðtÞ − ⃗yðtÞTAPðBþÞ†BþP⃗ ̇yðtÞ − ⃗ ̇yðtÞTPðBþÞ†BþPA⃗yðtÞ
1⁄4 ⃗y ̇ðtÞTP⃗yðtÞ þ ⃗yðtÞTP⃗ ̇yðtÞ − ⃗yðtÞTPAðBþÞ†BþP⃗ ̇yðtÞ − ⃗ ̇yðtÞTPðBþÞ†BþAP⃗yðtÞ
1⁄4 ⃗y ̇ðtÞTP⃗yðtÞ þ ⃗yðtÞTP⃗ ̇yðtÞ − ⃗yðtÞTPAðAþÞ†BBþP⃗ ̇yðtÞ − ⃗ ̇yðtÞTPðBþÞ†B†AþAP⃗yðtÞ
1⁄4 ⃗y ̇ðtÞTP⃗yðtÞ þ ⃗yðtÞTP⃗ ̇yðtÞ − ⃗yðtÞTPBBþP⃗y ̇ðtÞ − ⃗y ̇ðtÞTPðBþÞ†B†P⃗yðtÞ
1⁄4 ⃗y ̇ðtÞTP⃗yðtÞ þ ⃗yðtÞTP⃗ ̇yðtÞ − ⃗yðtÞTP⃗ ̇yðtÞ − ⃗ ̇yðtÞTP⃗yðtÞ
1⁄4 0; ðF7Þ
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-30


 where we used BBþP 1⁄4 AAþP 1⁄4 P. Then, F is independent of t and refers to another conserved quantity different from E. We can use our quantum algorithm to prepare jψðtÞi in Eq. (F5) by simulating H in Eq. (12). The complexity of Hamiltonian simulation is the same as that in Theorem 1. In the encoding used for Problem 8, some amplitudes are proportional to P⃗yðtÞ, and we have more direct access to the displacements of the oscillators than that using the encoding in Problem 1. However, preparing jψð0Þi in this case is expected to be more costly as it involves the action of Bþ. This is the reason why the complexity in the quantum algorithm of Ref. [11] for simulating the wave equation can be dominated by that of the initial state preparation. That case is a special instance of Problem 8 where A corresponds to the (discretized) Laplacian.
APPENDIX G: RELATED WORK AND OPTIMALITY OF OUR APPROACH
Our quantum algorithm provides the solution to a
second-order differential equation, i.e., ̈⃗yðtÞ 1⁄4 −A⃗yðtÞ, encoded in the amplitudes of a quantum state jψðtÞi defined in Problems 1 and 4. We do this via the classical-to-quantum reduction given in Sec. III, which results in a first-order differential equation, corresponding to a Schrödinger equation with a time-independent Hamiltonian H that depends on B, where A 1⁄4 BB†. Prior works have also considered quantum algorithms for solving first-order differential equations using a variety of approaches. A prominent example is Ref. [5] and related results (cf. Refs. [51,52]) that use the quantum algorithm for linear systems of equations [8,9,53]. Here we argue that those approaches, while possibly applicable to our problem, generally yield inefficient quantum algorithms for Problems 1, 2, 4, and 5 due to issues arising from the encoding. Indeed, by formulating the problem as a Hamiltonian simulation problem, and using optimal methods for the latter, we argue that our approach is the optimal one for solving these problems. Among other useful features, our approach does not necessitate a clock register to encode the solution at all times as in Ref. [5]. More details follow. One standard approach to formulate the second-order differential equation as a first-order one in our case would be to consider
⃗ ̇vðtÞ 1⁄4 0 −A
1N 0 ⃗vðtÞ; ðG1Þ
where
⃗vðtÞ ≔ ⃗ ̇yðtÞ
⃗yðtÞ ðG2Þ
is a vector in R2N that encodes the coordinates of all oscillators. (We assume that the choice of units is set from the beginning so that calculations are done with real numbers.) Another standard approach would be to consider
⃗w ̇ ðtÞ 1⁄4 0 −1N
A 0 ⃗wðtÞ; ðG3Þ
where
⃗wðtÞ ≔ ⃗y ̇ðtÞ
A⃗yðtÞ ðG4Þ
is also a vector in R2N. Equations (G1) and (G3) are also homogeneous first-order differential equations, whose solutions can be obtained by applying an exponential operator to ⃗vð0Þ or ⃗wð0Þ. Note that ðd=dtÞk⃗vðtÞk ≠ 0 and ðd=dtÞk ⃗wðtÞk ≠ 0 in general, so we cannot directly apply Hamiltonian simulation methods using these encodings, as the evolution of these vectors is not unitary. To solve differential equations that do not conserve the norm, Refs. [5,51,52] propose a range of quantum algorithms that, for this application, would output (normalized) quantum states:
j⃗vðtÞi ≔ 1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
k⃗ ̇yðtÞk2 þ k⃗yðtÞk2
q ⃗ ̇yðtÞ
⃗yðtÞ ðG5Þ
or
j ⃗wðtÞi ≔ 1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
k⃗ ̇yðtÞk2 þ kA⃗yðtÞk2
q ⃗y ̇ðtÞ
A⃗yðtÞ : ðG6Þ
In Refs. [5,51,52] this is done by approximating the solutions to the differential equations as solutions to systems of linear equations. The complexity of this approach depends on several parameters, in particular the condition number of the matrix to be inverted. In Ref. [13] a solution is found by giving the solution to the differential equation in exponential form, and then using the linear combination of unitaries (LCU) approach to approximate the exponential; a related approach that approximates the exponential operator is given in Ref. [54]. That approach is not applicable here, because it requires the matrix to be normal. Here the matrices—the 2 × 2 block matrices including A—are not normal, so the approach cannot be used. Nevertheless, even disregarding such difficulties, we show that this way of encoding the coordinates of the oscillators as in Eq. (G1) or (G3) is readily problematic. To observe this, it suffices to consider the evolution of a single normal mode of frequency ωk, i.e., the eigenvector of
A of eigenvalue ðωkÞ2. We obtain
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-31


 ⃗yðtÞ 1⁄4 ⃗ak cosðtωk þ φkÞ; ðG7Þ
where φk ∈ R is the initial phase and ⃗ak ∈ RN is the eigenvector of A. Computing the time average we obtain
hk⃗yðtÞk2i 1⁄4 1
2 k⃗akk2 ðG8Þ
and
hk⃗ ̇yðtÞk2i 1⁄4 1
2 jωkj2k⃗akk2
1⁄4 jωkj2hk⃗yðtÞk2i: ðG9Þ
(The latter is also the time average of the kinetic energy.) In a case where A gives rise to normal modes of low frequency, we have jωkj ≪ 1 (in the corresponding units), and then
hk⃗ ̇yðtÞk2i ≪ hk⃗yðtÞk2i: ðG10Þ
The implication is that the support of j⃗vðtÞi is, on average, mostly concentrated on the subspace spanned by basis vectors that encode ⃗yðtÞ. These do not encode the terms appearing in the kinetic energy or ⃗ ̇yðtÞ. Hence, the complexity of solving Problem 2 using this encoding, where j⃗vðtÞi is prepared rather than jψðtÞi, is at least linear in 1=jωkj, which is the factor needed to increase the desired amplitudes to a constant. This can become unbounded if jωkj → 0. In the second case we note that the support of j ⃗wðtÞi is, on average, mostly concentrated on the subspace spanned by basis vectors that encode ⃗ ̇yðtÞ instead. That is, the case hkA⃗yðtÞk2i ≪ hk⃗y ̇ðtÞk2i can occur when there are normal modes of low frequency. To solve Problem 1 or Problem 4, and especially Problem 5, the second component of the
state must be proportional to B†⃗yðtÞ or pffiffiAffiffi⃗yðtÞ, which
requires the application of the pseudo-inverse of B or pffiffiAffiffi to j ⃗wðtÞi. The condition number of these pseudo-inverses is also polynomial in 1=jωkj; for example, kð⃗akÞTBk 1⁄4 jωkj ≪ 1 for low frequencies. This implies that the complexity of solving Problem 1, Problem 4, or Problem 5 using this encoding, where j ⃗wðtÞi is prepared rather than jψðtÞi, is at least linear in 1=jωkj, which is the complexity of the most efficient methods to implement the pseudoinverse [9]. As in the previous case, this can also become unbounded if jωkj → 0. Similar observations follow directly from the results for the complexity in Refs. [5,51]. There the complexity is polynomial in the condition number of the matrix that diagonalizes the matrix appearing in the differential equations, which is here that with the blocks −A and 1N in Eq. (G1), or the negative of these for ⃗wðtÞ in Eq. (G3). The matrix that diagonalizes this matrix has condition number
maxðjωkj; jωkj−1Þ: ðG11Þ
Thus it will become unbounded when jωkj → 0, as described above. Technically, we cannot use the result as given in Ref. [5] directly, because the stability condition it uses requires the matrices appearing in the differential equations to not have eigenvalues exactly on the imaginary axis, as is the case here. An alternative approach to avoid dependence on the condition number of the diagonalizing matrix is that using the log-norm [52]. There we would need to subtract the identity times the log-norm from the original matrix. Here, the log-norm is
max j1 − ω2
kj=2: ðG12Þ
This means it is always positive, and so subtracting a multiple of the identity would result in a norm that exponentially decreases. Hence, the approach of Ref. [52] would yield a complexity that is exponential in time. At a high level, our encoding is motivated by the conservation of energy in time, and places equal emphasis
on those terms that encode the kinetic energy [⃗ ̇yðtÞ] and the potential energy [B†⃗yðtÞ] of the oscillators. The other two encodings do not have this feature: j⃗vðtÞi underrepresents the kinetic energy terms and j ⃗wðtÞi underrepresents the potential energy terms, bringing the issues discussed above. Last, we provide a comment on the relation between our results and a closely related result in Ref. [11] for simulating the wave equation. In Ref. [11] it is shown that the wave equation, a second-order and homogeneous differential equation, can also be mapped to a Schrödinger equation. Their construction is related to ours in that it uses a factorization of the (discrete) Laplacian as L 1⁄4 BB†, and indeed it is well known that the wave equation is one example of a classical system of coupled oscillators where all masses and springs are uniform, and where the couplings between oscillators are geometrically local (e.g., on the square grid). However, the encoding used in Ref. [11] is different from ours; for example, N amplitudes are reserved to encode the intensity of the wave, which corresponds to ⃗yðtÞ in our case. [The component of ⃗yðtÞ on the eigenvector of eigenvalue 0 of L is projected out.] The other amplitudes
are proportional to Bþ⃗ ̇yðtÞ, where Bþ is the pseudo-inverse of B. That is, the state prepared by the algorithm of Ref. [11] is of the form
jφðtÞi ∝ ⃗yðtÞ
Bþ⃗y ̇ðtÞ ; ðG13Þ
where the constant of proportionality is also time independent. This is essentially the same encoding as the one discussed in Appendix F, since P⃗yðtÞ 1⁄4 ⃗yðtÞ by assumption. The length of this vector is preserved in time since the evolution is unitary. Nevertheless, one implication
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-32


 of using this encoding to solve Problem 1 or Problem 2 for this example is the need to invert Bþ initially, to obtain amplitudes proportional to Bþ⃗y ̇ð0Þ. The condition number can be large, i.e., it is O(polyðNÞ) for the example of the wave equation, and hence the initial state preparation step (t 1⁄4 0) can be inefficient. Indeed, Ref. [11] manages to give evidence of a polynomial quantum speedup only. In addition, when considering the wave equation, the system is geometrically local and implies that N is polynomial in the evolution time t (i.e., t is exponential in n). In our problem, however, we can treat a significantly larger set of instances: we do not impose uniform masses, uniform spring constants, or even geometrically local interactions, and we can allow for times t 1⁄4 O(polyðNÞ). This generality together with our improved encoding are key to obtaining our claimed exponential quantum speedups for the problems defined.
[1] Richard P. Feynman, Simulating physics with computers, Int. J. Theor. Phys. 21, 467 (1982).
[2] Seth Lloyd, Universal quantum simulators, Science 273, 1073 (1996). [3] Leonard M. Adleman, Jonathan DeMarrais, and Ming-Deh A. Huang, Quantum computability, SIAM J. Comput. 26, 1524 (1997).
[4] P. W. Shor, Algorithms for quantum computation: Discrete logarithms and factoring, in Proceedings of the 35th Annual Symposium on Foundations of Computer Science, Santa Fe, NM, USA, 1994 (IEEE, 1994), pp. 124–134.
[5] Dominic W. Berry, High-order quantum algorithm for solving linear differential equations, J. Phys. A 47, 105301 (2014). [6] B. D. Clader, B. C. Jacobs, and C. R. Sprouse, Preconditioned quantum linear system algorithm, Phys. Rev. Lett. 110, 250504 (2013). [7] B. D. Clader, B. C. Jacobs, and C. R. Sprouse, Publisher’s Note: Preconditioned quantum linear system algorithm Phys. Rev. Lett. 110, 250504 (2013); 111, 049903(E) (2013). [8] Aram W. Harrow, Avinatan Hassidim, and Seth Lloyd, Quantum algorithm for linear systems of equations, Phys. Rev. Lett. 103, 150502 (2009). [9] Andrew M. Childs, Robin Kothari, and Rolando D. Somma, Quantum algorithm for systems of linear equations with exponentially improved dependence on precision, SIAM J. Comput. 46, 1920 (2017). [10] Yiğit Subaşı, Rolando D. Somma, and Davide Orsucci, Quantum algorithms for systems of linear equations inspired by adiabatic quantum computing, Phys. Rev. Lett. 122, 060504 (2019). [11] Pedro C. S. Costa, Stephen Jordan, and Aaron Ostrander, Quantum algorithm for simulating the wave equation, Phys. Rev. A 99, 012323 (2019). [12] Shi Jin, Nana Liu, and Yue Yu, Quantum simulation of partial differential equations via Schrodingerisation, arXiv: 2212.13969.
[13] Dong An, Jin-Peng Liu, Daochen Wang, and Qi Zhao, A theory of quantum differential equation solvers: Limitations and fast-forwarding, arXiv:2211.05246.
[14] Lev D. Landau and Evgeny M. Lifshitz, Mechanics, 3rd ed., Vol. 1 (Butterworth-Heinemann, Oxford, 2010). [15] John David Jackson, Classical Electrodynamics, 3rd ed., Vol. 1 (Wiley, New York, 1998). [16] Hartmut Neven and Ad Aertsen, Rate coherence and event coherence in the visual cortex: A neuronal model of object recognition, Biol. Cybern. 67, 309 (1992). [17] E. Bright Wilson, J. C. Decius, and P. C. Cross, Molecular Vibrations: The Theory of Infrared and Raman Vibrational Spectra (Courier Corporation, New York, 1980). [18] Lov K. Grover and Anirvan M. Sengupta, Classical analog of quantum search, Phys. Rev. A 65, 032319 (2002). [19] Dominic W. Berry, Graeme Ahokas, Richard Cleve, and Barry C. Sanders, Efficient quantum algorithms for simulating sparse Hamiltonians, Commun. Math. Phys. 270, 359 (2007). [20] Dominic W. Berry and Andrew M. Childs, Black-box Hamiltonian simulation and unitary implementation, Quantum Inf. Comput. 12, 29 (2012). [21] Dominic W. Berry, Andrew M. Childs, Richard Cleve, Robin Kothari, and Rolando D. Somma, Simulating Hamiltonian dynamics with a truncated Taylor series, Phys. Rev. Lett. 114, 090502 (2015). [22] Dominic W. Berry, Andrew M. Childs, and Robin Kothari, Hamiltonian simulation with nearly optimal dependence on all parameters, in Proceedings of the 2015 IEEE 56th Annual Symposium on Foundations of Computer Science, Berkeley, CA, USA, 2015 (IEEE, 2015), pp. 792–809. [23] Guang Hao Low and Isaac L. Chuang, Optimal Hamiltonian simulation by quantum signal processing, Phys. Rev. Lett. 118, 010501 (2017). [24] Guang Hao Low and Isaac L. Chuang, Hamiltonian simulation by qubitization, Quantum 3, 163 (2019).
[25] Emanuel Knill, Gerardo Ortiz, and Rolando D. Somma, Optimal quantum measurements of expectation values of observables, Phys. Rev. A 75, 012328 (2007). [26] Andrew M. Childs, Richard Cleve, Enrico Deotto, Edward Farhi, Sam Gutmann, and Daniel A. Spielman, Exponential algorithmic speedup by a quantum walk, in Proceedings of the Thirty-Fifth Annual ACM Symposium on Theory of Computing, San Diego, CA, USA, 2003 (Association for Computing Machinery, New York, 2003), pp. 59–68. [27] Pawel Wocjan and Shengyu Zhang, Several natural BQPcomplete problems, arXiv:quant-ph/0606179.
[28] Richard P. Feynman, Quantum mechanical computers, Found. Phys. 16, 507 (1986). [29] A. Yu. Kitaev, A. H. Shen, and M. N. Vyalyi, Graduate Studies in Mathematics, Vol. 47 (American Mathematical Society, Providence, 2002), p. 257. [30] Stephen P. Jordan, David Gosset, and Peter J. Love, Quantum-Merlin-Arthur–complete problems for stoquastic Hamiltonians and Markov matrices, Phys. Rev. A 81, 032331 (2010). [31] Andrew M. Childs, David Gosset, and Zak Webb, The BoseHubbard model is QMA-complete, Theory Comput. 11, 491 (2015).
[32] A. Kitaev, Quantum measurements and the Abelian stabilizer problem, arXiv:quant-ph/9511026.
EXPONENTIAL QUANTUM SPEEDUP IN SIMULATING COUPLED ... PHYS. REV. X 13, 041041 (2023)
041041-33


 [33] R. Cleve, A. Ekert, C. Macchiavello, and M. Mosca, Quantum algorithms revisited, Proc. R. Soc. A 454, 339 (1998). [34] Yuval R. Sanders, Dominic W. Berry, Pedro C. S. Costa, Louis W. Tessler, Nathan Wiebe, Craig Gidney, Hartmut Neven, and Ryan Babbush, Compilation of fault-tolerant quantum heuristics for combinatorial optimization, PRX Quantum 1, 020312 (2020).
[35] Y. Atia and D. Aharonov, Fast-forwarding of Hamiltonians and exponentially precise measurements, Nat. Commun. 8, 1572 (2017). [36] Jeongwan Haah, Matthew B. Hastings, Robin Kothari, and Guang Hao Low, Quantum algorithm for simulating real time evolution of lattice Hamiltonians, in Proceedings of the IEEE 59th Symposium on Foundations of Computer Science, Paris, France, 2018 (IEEE Computer Society, 2018), p. 350. [37] Ryan Babbush, Jarrod R. McClean, Michael Newman, Craig Gidney, Sergio Boixo, and Hartmut Neven, Focus beyond quadratic speedups for error-corrected quantum advantage, PRX Quantum 2, 010103 (2021). [38] Yuval R. Sanders, Guang Hao Low, Artur Scherer, and Dominic W. Berry, Black-box quantum state preparation without arithmetic, Phys. Rev. Lett. 122, 020502 (2019). [39] Yaoyun Shi, Both Toffoli and controlled-NOT need little help to do universal quantum computation, arXiv:quant-ph/ 0205115.
[40] Dorit Aharonov, A simple proof that Toffoli and Hadamard are quantum universal, arXiv:quant-ph/0301040. [41] Sergio Boixo, Emanuel Knill, and Rolando Somma, Eigenpath traversal by phase randomization, Quantum Inf. Comput. 9, 0833 (2009). [42] Ruggero Vaia and Lidia Spadini, Persymmetric Jacobi matrices with square-integer eigenvalues and dispersionless mass-spring chains, Linear Algebra Appl. 585, 164 (2020). [43] Hugo Sche ́rer, Luc Vinet, and Alexei Zhedanov, Analytic “Newton’s cradles” with perfect transfer and fractional revival, Ann. Phys. (Amsterdam) 439, 168790 (2022). [44] Jean-Michel Lemay, Luc Vinet, and Alexei Zhedanov, The para-Racah polynomials, J. Math. Anal. Appl. 438, 565 (2016).
[45] Dominic W. Berry, Yuan Su, Casper Gyurik, Robbie King, Joao Basso, Alexander Del Toro Barba, Abhishek Rajput, Nathan Wiebe, Vedran Dunjko, and Ryan Babbush, Quantifying quantum advantage in topological data analysis, arXiv:2209.13581. [46] Dominic W. Berry, Mária Kieferová, Artur Scherer, Yuval R. Sanders, Guang Hao Low, Nathan Wiebe, Craig Gidney, and Ryan Babbush, Improved techniques for preparing eigenstates of fermionic Hamiltonians, npj Quantum Inf. 4, 22 (2018). [47] Mikko Möttönen, Juha J. Vartiainen, Ville Bergholm, and Martti M. Salomaa, Transformation of quantum states using uniformly controlled rotations, Quantum Inf. Comput. 5, 467 (2005). [48] Theodore J. Yoder, Guang Hao Low, and Isaac L. Chuang, Fixed-point quantum search with an optimal number of queries, Phys. Rev. Lett. 113, 210501 (2014).
[49] Lov K. Grover, A fast quantum mechanical algorithm for database search, in Proceedings of the 28th ACM Symposium on Theory of Computing, Philadelphia, PA, USA, 1996 (Association for Computing Machinery, New York, 1996), pp. 212–219. [50] Charles H. Bennett, Ethan Bernstein, Gilles Brassard, and Umesh Vazirani, Strengths and weaknesses of quantum computing, SIAM J. Comput. 26, 1510 (1997). [51] Andrew M. Childs, Jin-Peng Liu, and Aaron Ostrander, High-precision quantum algorithms for partial differential equations, Quantum 5, 574 (2021).
[52] Hari Krovi, Improved quantum algorithms for linear and nonlinear differential equations, Quantum 7, 913 (2023). [53] Pedro C. S. Costa, Dong An, Yuval R. Sanders, Yuan Su, Ryan Babbush, and Dominic W. Berry, Optimal scaling quantum linear-systems solver via discrete adiabatic theorem, PRX Quantum 3, 040303 (2022). [54] Anirban N. Chowdhury and Rolando D. Somma, Quantum algorithms for Gibbs sampling and hitting-time estimation, Quantum Inf. Comput. 17, 0041 (2017).
BABBUSH, BERRY, KOTHARI, SOMMA, and WIEBE PHYS. REV. X 13, 041041 (2023)
041041-34
