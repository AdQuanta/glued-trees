# Quantum walks on trees with disorder: Decay, diffusion, and localization - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.86.022335
> Collected: 2026-09-20
> Published: 2012-08-27
> Zotero parent key: DVZGDRQV
> Evidence: Zotero indexed PDF text

Quantum Walks on Trees with Disorder: Decay, Diffusion, and Localization
Steven R. Jackson, Teng Jian Khoo, and Frederick W. Strauch∗
Williams College, Williamstown, Massachusetts 01267 (Dated: September 18, 2018)
Quantum walks have been shown to have impressive transport properties compared to classical random walks. However, imperfections in the quantum walk algorithm can destroy any quantum mechanical speed-up due to Anderson localization. We numerically study the effect of static disorder on a quantum walk on the glued trees graph. For small disorder, we find that the dominant effect is a type of quantum decay, and not quantum localization. For intermediate disorder, there is a crossover to diffusive transport, while a localization transition is observed at large disorder, in agreement with Anderson localization on the Cayley tree.
PACS numbers: 03.67.Lx, 03.65.Pm Keywords: Quantum walk, quantum computing, localization
I. INTRODUCTION
Quantum walks constitute a promising route to the development of algorithms for quantum information processing. Successful applications of quantum walks include a variety of search algorithms [1–4], graph hitting problems [5–7], Boolean function evaluation [8, 9], among others. Quantum walks are in fact a universal paradigm for quantum computation [10, 11]. The simplest and most dramatic improvement demonstrated by quantum walks, when compared with the corresponding classical random walks, is the hitting probability of a walk on certain graphs. Two graphs in particular have demonstrated an exponential separation between the quantum and classical walks: the glued binary trees [5] and the hypercube [7]. An example of the former is shown in Fig. 1; this graph is formed by connecting the leaves of two binary trees of depth d. Due to the graph’s symmetry, the quantum walk can be restricted to a subspace of the total (exponentially large) Hilbert space, known as the “column space” (also shown in Fig. 1). It has been argued that this symmetry is the heart of the quantum speed-up [12]. A quantum walk algorithm on a slight modification of this graph, to be described below, was proven to have an exponential speedup over any classical algorithm [6]. Keating et al. have argued that physical implementations of these walks will not be able to maintain this quantum speed-up for large graphs [13]. Indeed, one expects that physical systems will be subject to decoherence and disorder. While one can always argue that future quantum computers will be protected from these effects by error correction, it is more likely that near term demonstrations of quantum walks will use a physical network. In fact, many of the recent experiments on quantum walks involve an encoding of the degrees of freedom that is not, strictly speaking, computationally useful [14]. Nevertheless, these experiments demonstrate
∗Electronic address: Frederick.W.Strauch@williams.edu
the dynamical speed-up characteristic of quantum walks. Determining when disorder or decoherence will limit the observability of this speed-up is an important theoretical problem [15].
This problem may already have been encountered by nature. Recent evidence has shown that photosynthetic complexes operate using a type of quantum walk [16], where the interplay of decoherence with disorder plays a crucial role in their energy harvesting efficiency. This phenomenon, known as dephasing or environmentally assisted transport, has relations to earlier studies of phonon effects on electron transport in disordered solids [17]. Understanding and potentially reverse-engineering this efficiency is a topic of great scientific and practical importance. As the complexes and potential technologies under study can be far from the thermodynamic limit, examining quantum transport on graphs of modest size may reveal new surprises.
In this paper, we examine the continuous-time quantum walk on the glued trees graph with static disorder, corresponding to the usual Anderson model with disordered on-site energies [18]. Previous authors [13] introduced disorder through an effective one-dimensional representation (the column space). Using the fact that all eigenstates are localized in one-dimension with arbitrary disorder, they concluded that Anderson localization would cause an exponential suppression of the hitting probability. From a physical perspective, however, this model has some flaws. First, their model introduces a highly correlated form of disorder, in that all of the on-site energies on a given column are the same Second, the glued trees graph is quite similar to a Cayley tree, whose dimensionality is formally infinite, as far as Anderson localization is concerned [19]. The Cayley tree exhibits a localization transition at large disorder, and thus significant speed-up may still be possible for weak disorder.
We have performed a numerical study of this problem for the full Hilbert space of the glued trees graph and modifications thereof. Analysis of the eigenvalues and eigenvectors agree with previous studies of localization the Cayley tree. We pay special attention to the
arXiv:1206.3178v1 [quant-ph] 14 Jun 2012


 2
less well studied regime of weak disorder, using dynamical simulations to find a type of quantum decay of the quantum walk from the column space. The resulting hitting probability is well simulated by a model with local decay from each column state. We further consider the crossover from wavelike to diffusive transport for intermediate levels of disorder. A scattering theory analysis of this regime indicates a transition from the quantum walk to a classical random walk. Our results augment the many results for onedimensional quantum walks with disorder. These include theoretical studies for the continuous-time quantum walk [20] and the discrete-time quantum walk [21], and the many recent experiments on atoms [22], ions [23, 24], and photons [25, 26]. Higher-dimensional quantum walks could be realized in these or other systems, such as networks of superconducting circuits [27, 28]. In particular, our simulations show that the effects of disorder on quantum transport can be identified in systems of 10-100 lattice sites. This paper is organized as follows. In Section II we review the known results for Anderson localization on the Cayley tree, and in Section III numerically study the phase diagram for the two types of glued trees, and find evidence of the localization transition. In Section IV we study the time-dependence of the quantum walk with disorder, and introduce the local decay model for weak disorder. In Section V we consider a scattering theory model for transport through the glued trees graph, and find evidence for the transition to classical random walk. We conclude in Section VI, comparing our results with the hypercube and highlighting the major open questions. Results for the quantum scattering and (classical) diffusive transport through the glued trees are found in the Appendices.
II. LOCALIZATION AND DIFFUSION ON THE BINARY TREE
Anderson localization is the phenomenon that, for a sufficiently large amount of disorder, the eigenstates of a quantum system become exponentially localized about the nodes in a graph [18]. Localization transitions are a rich field of study [19], for which both symmetry and dimensionality play key roles. The quantum walk we consider corresponds to the simplest such model, a tightbinding Hamiltonian with random on-site energies
H = −γ ∑
〈j,k〉
(
c†
j ck + c†
k cj
)
+
∑
j
j c†
jcj, (1)
where γ is a hopping rate, j is a set of random variables, uniformly distributed in the range [−W/2, W/2], and c†
j
is the creation operator for an excitation at site j, and the sum is over neighboring sites. This model, originally inspired by electron transport in solids, can be used for many physical systems, such as quantum state transfer
!"#$$%&#"' (' (' (' ('
)'' )' )' )' )('' )('' )('' )(''
*+#,-+.'
!
2
!
2
!
2
!
2
!
2
!
2
!
2
!
2
!/"+.,''''''0''''''')''''''(''''''1'''''''2''''''3'''''''4''''''5'''''''6'
FIG. 1: Glued binary trees graph G4, showing the reduction to the column space for both the classical (top) and quantum (bottom) random walks.
of a single excitation on a qubit network [27, 29, 30] or exciton transfer in a photosynthetic complex [16]. Much is known about the Anderson model given by Eq. 1 [19]. For example, for a one-dimensional infinite lattice, localization occurs for arbitrarily small amounts of disorder [31]. It was argued that this property was generic to quantum walks [13]. However, it is known that for systems with dimension greater than two, localization requires a sufficiently large amount of disorder, i.e. there is a localization transition as the disorder is increased [32]. At first glance, the glued trees graph of Fig. 1 might appear to be a subset of a two-dimensional system, and thus one might expect localization for even small amounts of disorder. In fact, the infinite binary tree, or more generally the infinite Cayley tree (also known as the Bethe lattice [33]) has been used as a model for an infinite-dimensional system. This has been studied extensively, and exhibits a localization transition found numerically [17, 34–36] and by an analytical mean field calculation [37, 38]. For this system, there is a mobility edge in the energy spectrum, such that eigenstates inside the mobility edge are extended, while those outside are localized. For sufficiently large values of disorder, there is a localization transition beyond which all eigenstates are localized. For a binary tree (or Cayley tree with K = 1), this transition occurs for Wc ≈ 17 [17, 34–36, 38]. The description of localization given above, in which the eigenstates of the system exhibit a transition from extended to localized states, can be called eigenstate lo


 3
calization. There are two other ways to identify localization that we will encounter in this paper. The first is dynamical localization, in which the spreading of a wavepacket shows a saturation as a function of time. The second is spectral localization, in which the eigenvalues of the system move from an absolutely continuous spectrum (corresponding to extended states) to a pure point spectrum (corresponding to localized states). These other indicators of localization, which have also been studied extensively, we now briefly summarize. The spectral properties of the system were studied numerically [36, 39], and found to exhibit a transition in agreement with the self-consistent approaches described above. These numerical studies are sensitive to the handling of the boundary of the tree [40], a fact to which we will return in Section III. While there are some subtleties regarding the the phase diagram at weak disorder [41, 42], the existence of a localization transition for large disorder is well established. For small disorder, the existence of extended eigenstates has been proven [43]. It has also been proven that, for small disorder, states that are initially localized spread ballistically [44]. The ballistic spreading does not preclude classical behavior, however. The random walk on the Bethe lattice has been studied, and can be mapped onto an asymmetric random walk on a one-dimensional half-line [45], as indicated in Fig. 1 (e.g. the left half). A classical walker is twice as likely to move right as left, and this asymmetry leads to the peculiar fact that the classical walk also spreads ballistically. Exact results and limits have been established for this and other properties of the classical walk [46, 47]. Note that the asymmetry is linked to the exponential growth of sites away from the origin, such that one often calls the Bethe lattice a graph of infinite dimensionality.
III. QUANTUM WALK EIGENSTATES
The continuous-time quantum walk [48, 49] is precisely the quantum dynamics of a single particle moving on a graph. This is given by the Schr ̈odinger equation
i dψj
dt = −γ ∑
k
Ajkψk, (2)
where Ajk is the adjacency matrix for the graph and γ is hopping rate. One could also use the Laplacian matrix, or introduce potentials to implement search algorithms [2, 4], but here we consider the addition of static disorder, such that
i dψj
dt = −γ ∑
k
Ajkψk + j ψj , (3)
where the on-site energies j are i.i.d. random variables uniformly distributed in the range [−W/2, W/2]. In this section we consider the nature of the eigenstates of the Hamiltonian of the quantum walk with disorder,
namely H|Ψ〉 = E|Ψ〉, with H = H0 + H′, with the unperturbed Hamiltonian given by
H0 = −γ
Nd
∑
j,k=1
Ajk|j〉〈k|, (4)
and diagonal static disorder
H′ =
Nd
∑
j=1
j|j〉〈j|, (5)
where Nd = 3 × 2d − 2 is the number of vertices for the glued trees graph Gd. We begin by analyzing H0, and follow by studying the eigenvalues and eigenstates of H.
A. Eigenstates without disorder
As described above, there is a great deal of symmetry in the glued trees graph Gd, and a great deal of structure in the eigenstates and eigenvalues of the system. We begin by providing a notation for the graph. We consider a labeling along the “columns” and “rows” of the graph, of the form (j, n), where j = 0 → 2d indicates the distance from the left root along the graph, and n = 0 → Nj,d − 1 is the location within a given column. Here Nj,d is the number of sites in a given column j, given by Nj,d = 2j
for j ≤ d, and Nj,d = 22d−j for j > d. The coordinates (j, n) can be combined into a single coordinate v by the following rule
v=
{ 2j + n for 0 ≤ j ≤ d,
3 × 2d − 22d+1−j + n for d < j ≤ 2d. (6)
Note that v ranges from 1 → 3 × 2d − 2. The adjacency matrix elements Av,w are equal to one if vertices v and w are connected, and zero otherwise. This can be given in terms of the coordinates (j, n) by observing that (j, n) is connected to
(j − 1, bn/2c), (j + 1, 2n), (j + 1, 2n + 1) for j ≤ d, (7)
and
(j + 1, bn/2c), (j − 1, 2n), (j − 1, 2n + 1) for j > d. (8)
What is most important is that a given vertex is symmetrically coupled to those sites one step further from the left root (or closer to the right root). This allows us to express the eigenstates of the system in terms of “column-states” that are equal superpositions of states on a given column j. This column-space reduction is well-known for its utility in the analysis of the quantum walk [5, 6, 12]. Letting |j, n〉 denote the Hilbert-space vector associated with vertex (j, n), we define the column-space vector |col j〉 by
|col j〉 = 1
√Nj,d
Nj,d −1
∑
n=0
|j, n〉. (9)


 4
By the symmetry noted above, the Hamiltonian H0 = −γA acts on the column-space states as
H0|col j〉 = −√2γ|col j − 1〉 − √2γ|col j + 1〉, (10)
where one factor of √2 is due to the number of connections to a neighboring column, and the other due to the normalization of the column states. Hence, we can reduce the dynamics to a quantum walk on a finite line, whose eigenstates are equally well-known
| Ψk,d 〉 = 1
√d + 1
2d
∑
j=0
sin
( k (j + 1) π 2(d + 1)
)
| col j 〉, (11)
with energies
Ek,d = −2√2 γ cos
( kπ
2(d + 1)
)
, (12)
and k = 1 → 2d + 1. We have annotated the states by the depth of the graph, as there are in fact many more eigenstates for Gd, whose enumeration we now consider. The glued trees graph is self-similar, in that Gd contains 2ν subgraphs, each equivalent to Gd−ν. These sub
graphs can be grouped into 2ν−1 pairs, each pair formed by removing the roots of a larger graph equivalent to Gd−ν+1. That is, we can repeatedly split the glued trees graph by removing the left and right roots, such that Gd contains 2 copies of Gd−1, 4 copies of Gd−2, and so forth, formed by removing the roots until we are left with 2d copies of G0 (the isolated vertices at the center of the graph). Some representative subgraphs of G4 are shown in Fig. 2. On their own, each subgraph would have eigenstates of the form of Eq. (11). To find how these subgraphs contribute to the spectrum of Gd, we observe that an equal but opposite-signed superposition over two paired subgraph eigenstates is an eigenstate of Gd. This occurs because the components with opposite phase, when acted upon by H0, will interfere destructively on the two nodes to which they are connected on the larger graph. By this pairing, we can thus construct the complete set of eigenstates for Gd. To see this more clearly, we define a set of “subcolumn” states whose elements combine the paired subgraphs described above. These are given by
|scol j; α, ν〉 =
(2α+1)Nd−ν −1
∑
n=2αNd−ν
|j + ν, n〉 − |j + ν, n + Nj,d−ν 〉
√2Nj,d−ν
,
(13) where j = 0 → 2(d − ν) indicates the column in Gd−ν,
α = 0 → 2ν−1 − 1 labels the paired subgraphs, and ν = 1 → d indicates the depth of the subgraphs’ left root. Using these states, the remaining eigenstates of Gd can be obtained by using the eigenstates |Ψk,d−ν〉 from Eq. (11) with |col j〉 replaced by |scol j; α, ν〉 and eigenvalues Ek, d−ν from Eq. (12), where k = 1 → 2(d − ν) + 1. Defining
σd = {Ek,d, k = 1 → 2d}, (14)
!!"
!#"
!#"
FIG. 2: (Color online) Glued binary trees graph G4, with several highlighted subgraphs G3 (top, in gray) and two copies of G2 (middle, in red and bottom, in blue).
the total spectrum can then be written as
σ = σd +
d
∑
ν=1
2ν−1σd−ν . (15)
This spectrum exhibits a very large degeneracy, especially for E = 0, which has a multiplicity of 2d (one from each copy of σd−ν, and half from the σ0). This large degeneracy (also observed in [40]) occurs for trees that are both glued and unglued and can make numerical analysis of the disordered system problematic, as will be described below.
B. Eigenstates with disorder
The introduction of static disorder changes both the eigenvalues and eigenvectors of the system. For the Cayley tree, early studies used a self-consistent approach [34, 38] to find the localization transition and a phase diagram between extended and localized eigenstates. Recent numerical studies [35, 36] have confirmed these earlier results, which we now summarize. The eigenvalue spectrum has been studied for a single Cayley tree numerically by [39] through the use of spectral statistics. A transition of the distribution of the energy level spacings from Wigner to Poisson (indicative of a localization transition) was observed when the tree was modified so that the leaves are randomly connected to each other. This random connection presumably reduces the prevalence of the zero eigenvalue described above, which would otherwise lead to a Poisson distribution for the spectral statistics [40]. We performed a similar analysis for the glued trees graph, with the leaves connected


 5
as in Fig. 1, which we call a simple glued trees (SGT) graph, or interrupted by a random cycle (as in [6]), which we call a modified glued trees (MGT) graph. An example of the MGT (with a regular connection [50]) is shown in Fig. 9. A Wigner to Poisson transition was observed for the MGT, while the SGT exhibited a spectrum that was always far from Wigner. For the remainder of this section, our results were obtained using the MGT. The localization of the eigenstates and the localization transition can be found by studying a simple property of the eigenstates, namely the inverse participation ratio (IPR) I2:
I2(ψ) = ∑
j
|ψj|4, (16)
where we assume that the states are normalized with I1(ψ) = ∑
j |ψj|2 = 1. This quantity has the property that an eigenstate localized to a single site has I2(ψ) = 1, while an eigenstate extended over N sites has I2(ψ) = 1/N . We further define an averaged value of this quantity
I2(E) = 1
N (E; ∆E)
∑
|〈ψ| H |ψ〉−E|<∆E
I2(ψ), (17)
where N (E; ∆E) is the number of eigenstates found to have eigenvalue Ej with in the range E − ∆E < Ej < E +∆E, leaving the dependence on ∆E implicit.. By calculating I2(E) the eigenstates of the system as a function of energy and disorder, the phase diagram and localization transition can be visualized. For the SGT, we again encounter a difficulty in that there are a large number of states with an I2(ψ) = 1/2,
associated with the 2d−1 states in σ0 (with E = 0). However, by using the MGT, we can calculate meaningful results for I2(E) for various disorder strengths W to obtain the diagram in 3. Here we have let d = 8 and set ∆E = 0.15γ and averaged over 500 realizations of H. We observe a gradual movement of extended states (with small I2) to localized states (with I2 > 1/2) as disorder is increased. Also shown are the expected results for an infinite Bethe lattice, obtained using the self-consistent method of Miller and Derrida [34] To obtain an estimate of the localization transition, we fix our attention to states near E = 0, and repeat the calculation of the averaged IPR for graphs of various sizes. As expected, I2(0) exhibits a small size-dependent value for W = 0, which increases to approximately 0.5 for large W . At a certain value, the averaged IPRs for all of the graphs coalesce, from which we estimate Wc ≈ 17, in agreement with recent results for the Cayley tree [35, 36].
IV. QUANTUM WALK DYNAMICS
The dynamics of a quantum walk on the glued trees graph with disorder has been studied using the onedimensional column-space model by Keating et al. [13].
FIG. 3: Inverse participation ratio I2(E) as a function of energy and disorder, for d = 8. For each value of disorder the IPR was averaged over 500 realizations of H with ∆E = 0.15 (with γ = 1). Also shown is the mobility edge from the self-consistent theory, predicting a localization transition with Wc ≈ 17.
0 5 10 15 20
10−2
10−1
100
W
I2(E=0)
Depth 5 Depth 6 Depth 7 Depth 8
WC
FIG. 4: (Color online) Inverse participation ratio I2(E) at the band center (E = 0) as a function of disorder for various depths. For each value of disorder the IPR was averaged over the middle 100 eigenvalues and a number of realizations given by 500, 250, 125, and 50 for d = 5, 6, 7, and 8, respectively. The localization transition occurs when the curves collapse near W ≈ 17.
In the previous section, however, we have seen that the eigenstates of the MGT undergo a localization transition at large disorder. This leaves open the possibility that a dynamical speed-up can be observed for small disorder. To explore this possibility, we again turn to numerical studies. There are three issues to be studied: first, what is the probability to hit the right root should the quan


 6
tum walk begin at the left root? Second, how does this probability decay as a function of disorder and size, and by what mechanism? Finally, if the disorder quantum walk does not hit the right root, how far does it get?
The first question can be answered by calculating the average of
phit(t) = |〈col 2d|e−iHt|col 0〉|2 (18)
for instances of the SGT Hamiltonian with disorder strength W and for various sizes d. This corresponds to the single-shot measurement procedure [7] for the quantum walk, and a representative set of phit(t) as a function of time and values of W are shown in Fig. 5. The first thing to observe is the oscillatory structure, due to the Bessel function structure for phit(t) [5, 29], from which we can see that probability is maximized at the hitting time
thit ≈ 1
2√2γ
[
2d + 1 + 1.0188
(
d+ 1
2
)1/3]
, (19)
with a value pd ∼ d−2/3 for large d. Second, as disorder increases the maximum of the hitting probability is seen to decrease. This hitting probability can be approximated by
phit(thit) ≈ pd exp
[
−1
16 (d − 1
2 )W 2
]
, (20)
The exponential decay of phit/pd is shown in the inset to Fig. 5.
By what mechanism does this decay occur? It is not associated with eigenstate localization, as the eigenstates of the system are well within the extended regime in the phase diagram of Fig. 3. To understand this, we turn to another quantity of interest, the column-space probability
pcol(t) =
2d
∑
j=0
| 〈 col j | ψ(t) 〉 |2 . (21)
Quantum walks on the glued trees graph that are initially in a column space state |col j0〉 will remain in the column space in the absence of disorder. Once static disorder is introduced, the eigenstates lying within the column space become coupled to the other eigenstates of Gd. These are associated with the subgraphs of Gd, and have zero amplitude on the graph’s two roots. The resulting decay of pcol(t), shown in Fig. 6 leads to the decay of phit(t).
We can provide an analytical estimate of this decay through perturbation theory. Assuming the walk begins in a column state | col j0 〉, taking the second order ex
01234
0
0.1
0.2
0.3
0.4
0.5
t/thit
phit(t)
5 10 15
0
0.1
0.2
0.3
d
phit/pd
FIG. 5: (Color online) Hitting probability phit(t) as a function of time for the quantum walk on the glued trees graph with d = 15 and various values of disorder. The symbols were calculated using exact numerical simulations with (from top to bottom) W = 0, 0.2, 0.4, 0.6, 0.8, 1.0, and 1.2, with 10 realizations of H for each value of W . The solid curves were calculated using the locay decay model (see text). The inset shows the hitting probability phit(thit)/pd as a function of d with symbols from numerical simulations and the curve from the approximation of Eq. (20) (see text).
pansion of pcol(t) gives
pcol(t) =
2d
∑
j=0
| 〈 col j | exp(−i H t)| col j0 〉 |2
≈
2d
∑
j=0
|〈 col j | col j0 〉|2 + t2|〈 col j | H | col j0 〉|2
−t2 (〈 col j | col j0 〉〈 col j0 | H2 | col j 〉) , (22)
where the Hamiltonian is given by H = H0 + H′. It is straightforward to show that H0 contributes nothing to
the quadratic term, and for H′ given by Eq. (5) we find
pcol(t) = 1 − t2
Nj20,d

(Nj0,d − 1) ∑
i
i2 − ∑
i6=j
ij

.
(23) Averaging pcol(t) over the disorder we find
〈pcol(t)〉 = 1 − 1
12 t2W 2
(
1− 1
Nj0,d
)
, (24)
where we have used 〈 i j〉 = 1
12 W 2δij .
This result for the short time decay applies to any graph for which the quantum walk can be projected onto a column space. On longer timescales, we conjecture that


 7
the decay will have an exponential character, while retaining the position dependence. Hence, extrapolating from the short time result, we postulate a model of “local (exponential) decay”, in which the walk evolution is computed as in the ideal column space representation, but the probability at each site j is allowed to decay:
pj(t) = p0 exp
[
−t
12
W2
γ
(
1− 1
Nj,d
)]
. (25)
This is equivalent to applying the mapping
H 7→ Hcol − iΓ/2, (26)
where Hcol is the projection of the graph Hamiltonian onto the column space, and Γ is given by
Γ= 1
12
W2
γ
2d
∑
j=0
(
1− 1
Nj,d
)
| col j 〉〈 col j |, (27)
with γ denoting the unit time hopping probability from H0. This expression for Γ can be anticipated by applying
Fermi’s Golden Rule to H′ in the eigenstate basis, but the presence of a large discrete component to the spectrum (σ0) prevents us from making a precise derivation. Numerical evidence, however, suggests that this is in fact the correct mechanism. Along with the exact numerical results for phit and pcol in Figs. 5 and 6, we have included results from the localdecay model calculated in the (exponentially smaller)
01234
0
0.2
0.4
0.6
0.8
1
t/thit
pcol(t)
FIG. 6: (Color online) Column space probability pcol(t) as a function of time for the quantum walk on the glued trees graph with d = 15 and various values of disorder. The symbols were calculated using exact numerical simulations with (from top to bottom) W = 0, 0.2, 0.4, 0.6, 0.8, 1.0, and 1.2, with 10 realizations of H for each value of W . The error bars indicate the standard deviation of each average. The solid curves were calculated using the local decay model (see text).
column-space representation for H0. We observe that the local decay model predictions (solid lines) agree well with the results of simulations (points), to within one standard deviation. Our model accurately reproduces many features of the exact simulations, such as the variation in the decay rate of pcol and the oscillations in phit. Furthermore, if we use the column space probability to predict the hitting probability at the target node (opposite root), the agreement is quite good. This supports the claim that the disorder-induced reduction in quantum transport is primarily explained by decay from the column space. So far we have looked at the probability at the right root and the column space, but a more global characterization of the walk propagation can be found by analyzing the average depth reached by the quantum walk,
r(t) = 〈 ψ(t) | rˆ | ψ(t) 〉, (28)
where the column position operator rˆ is defined as
rˆ =
2d
∑
j=0
Nj,d −1
∑
n=0
j|j, n〉〈j, n| (29)
with the property rˆ| col j 〉 = j| col j 〉. The value of r(t) thus gives a snapshot of the expected position of the walk along the graph at any one time. This is displayed in Fig. 7 as a function of time and disorder. In the absence of disorder, the average depth shows an oscillatory character consistent with ballistic propagation of the wavepacket and reflections at the two ends of the graph. Disorder-induced decay from the column space causes the amplitude of the oscillations to decay faster than in the ideal case, ultimately causing a “damping” of the oscillations. Therefore, the walk has a reduced probability of traversing the graph, and substantial probability is instead deposited in the center of the graph, where the concentration of nodes is highest. In Fig. IV we plot the maximum value of r(t) in the range t < 3thit against the strength of disorder, illustrating the localization transition on the glued trees graph. We see that for small disorder (W < 2), the maximum value of r is high, corresponding to the quantum walk hitting the right root, for which r = 2d. As disorder increases, the curve falls, and begins to level off at the graph center (r ≈ d for 2 < W < 4). For larger amounts of disorder (W > 4), the curves continue to decrease, converging on a single value around W = 16, precisely when we expect all eigenstates to be localized. This analysis of the quantum walk dynamics strongly suggests a type of quantum-to-classical or “wavelike-todiffusive” crossover at weak disorder. Note that this not a “ballistic-to-diffusive” crossover, and does not conflict the ballistic spreading of wavepackets found by Klein [44] for the Bethe lattice at weak disorder, as classical diffusion also leads to ballistic spreading (r(t) ∼ t). It does, however, suggest that there may be a length scale (the mean-free-path) that limits the size of graphs for which


 8
01234
0 0.4 0.8 1.2 1.6 2
0
5
10
15
20
25
30
t/thit
W
r(t)
hit
FIG. 7: (Color online) Average distance r(t) for d = 15 as a function of time and disorder W . For each W , the simulations were averaged over 10 realizations of H. The quantum oscillations decay in time for small disorder, with a critical damping near W ≈ 2, indicating a type of quantum-to-classical transition.
0 5 10 15 20
0
5
10
15
20
25
30
W
rmax
d=5 d = 10 d = 15
FIG. 8: (Color online) Maximum average distance r(t) as a function of disorder W for various depths. For each value of disorder the maximum of r(t) was averaged over 1000, 100, and 10 realizations for d = 5, 10, and 15, respectively. For intermediate disorder (2 < W < 4), there is a quantumto-classical transition, while for large disorder (W > 15) a localization transition is observed.
a speedup could occur in the presence of disorder. That is, the exponential decay of the hitting probability (in d) seen in Fig. 5 may be interpreted as the classical probability for a walker to traverse d sites given a mean-freepath of order ` ∼ 1/W 2. To understand this crossover in more detail we extend our analysis of the quantum walk to a transport model.
!"#$%&"'()*+&(
,&-&#'&%()*+&(
./*"01$2&%()*+&(
FIG. 9: Scattering approach to the quantum walk, in which an incident wavepacket is transmitted and reflected along the “tails” connected to the modified glued trees graph.
V. QUANTUM WALK TRANSPORT
To identify the quantum-to-classical transition, we consider the quantum transmission through the glued trees graph, subject to disorder. To transform the quantum walk into a transmission problem, we attach “tails” to the input and output nodes, and look at the transmission coefficient through the graph for a wavefunction of the form
Ψ(n) =
{ eikn + Re−ikn for n < 0
T eikn for n > 2d + 1 (30)
This represents an ingoing wave that is reflected and transmitted through the graph, as illustrated in Fig. 9. This type of quantum walk was been used to develop a quantum algorithm for NAND-tree evaluation [8], and has been generally analyzed in [51]. We consider the transmission probability T = |T |2 as a function of depth and disorder. Using a standard analysis for transmission in tightbinding lattices [52], we find the transmission amplitude
T = 〈col 0| 2i sin k
H ̃ − 2 cos k |col 2d + 1〉 (31)
where
H ̃ = H + eik (|col 0〉〈col 0| + |col 2d + 1〉〈col 2d + 1|) (32) is an effective Hamiltonian for the MGT graph alone (note that this graph has 2d + 1 columns). This quantity can be calculated by diagonalizing the non-Hermitian
Hamiltonian H ̃, and forming the appropriate matrix elements in T . The resulting transmission probability T = |T |2 is shown as a function of momentum k and disorder W in Figs. 10 and 11, for depths d = 5 and d = 6, respectively. For small disorder, there is a size-dependent oscillatory


 9
T = |T |2
W
k/!
0 2 4 6 8 10
0
0.2
0.4
0.6
0.8
10
0.2
0.4
0.6
0.8
FIG. 10: Transmission probability T as a function of momentum k and disorder W for a modified glued trees graph of depth d = 5. For each value of momentum and disorder, the transmission was averaged over 250 realizations of H ̃.
T = |T |2
W
k/!
0 2 4 6 8 10
0
0.2
0.4
0.6
0.8
10
0.2
0.4
0.6
0.8
FIG. 11: Transmission probability T as a function of momentum k and disorder W for a modified glued trees graph of depth d = 6. For each value of momentum and disorder, the transmission was averaged over 100 realizations of H ̃.
structure as a function of k due to resonances, much like those found in [52] (and briefly described in Appendix A). These oscillations in T disappear when the disorder strength W ≈ 2, after which the transmission decays monotonically. Figure 12 shows T for k = π/2 as a function of disorder for many graph sizes, which all exhibit the same behavior for W > 2, indicative of a transition in T . The decay of the transmission probability with disor
0 2 4 6 8 10
0
0.2
0.4
0.6
0.8
1
W
T = |T |2
FIG. 12: (Color online) Transmission probability T for k = π/2 as function of disorder and for various depths. The various symbols are d = 7 (blue circles), d = 8 (red upward triangles), d = 9 (blue squares), and d = 10 (red downward triangles), averaged over 500, 200, 100, and 50 realizations of H ̃, respectively. The solid black curve is the transmission probability for the classical random walk Tc (see text).
der can be understood using a classical model, described in the Appendix B. This model uses a diffusion constant proportional to the mean-free-path λ ∼ ` ∼ W −2 and leads to a classical transmission probability of the form
Tc = T0
1 + c(W/γ)2 , (33)
where the coefficients T0 and c presumably depend on the exact mapping of the disordered quantum walk to the diffusion equation, such as the method of [53] or the results of [54]. This expression for Eq. (33), fit using T0 = 0.8 and c = 0.2, is shown in Fig. 12. This agreement, for intermediate values of disorder, provides confirmation of the quantum-to-classical crossover observed in the dynamical studies of the previous section.
VI. CONCLUSION
In this paper, we have carried out an investigation of the effects of diagonal disorder on quantum walks on the glued trees graph. While disorder does lead to localization in the strong disorder limit, we find the primary effect in the case of small disorder to be quantum decay out of the column space. The quantum decay can be accurately modeled in the column space by a non-unitary mapping that enforces position dependent decay of the probability. This local decay model is efficient to compute, owing to the exponential reduction in size of the representation, yet it allows prediction of the end-to-end hitting probability, and should be extendable to other graphs with similar symmetries.


 10
One such graph is the hypercube. This problem had been previously studied for quantum state transfer [27], where the effects of off-diagonal disorder were emphasized. Numerical simulations for diagonal disorder, however, provide very similar results to those found in Sec. IV, with one important difference. The hitting time for the hypercube is independent of the dimension d (which is analogous to the depth of the glued binary trees graph). The local decay model then predicts that the hitting probability should decay as e−W 2/12, a result borne out by simulations. Thus, for the hypercube, quantum transport outperforms classical transport for small W . Such a result is also possible for the glued trees graph. The exponential suppression of the hitting probability occurs for the specific case of a state initially localized to the left root of the graph. By using a graph with “tails”, the results of Sec. V show that appreciable transport is possible for W < 2, provided there is no disorder in the tails and an appropriate initial state can be found. In addition, alternative measurement strategies [55], or the inclusion of traps [49] could provide opportunities for speedup. Exploring this possibility could provide additional context for understanding environmentally assisted quantum transport [16]. In summary, we have performed an analysis of the effect of static disorder on a quantum walk on the glued trees graph. For small disorder, we find that the dominant effect is a type of quantum decay, and not quantum localization. For intermediate disorder, there is a crossover to diffusive transport, while a localization transition is observed at large disorder, in agreement with Anderson localization on the Cayley tree. Our results suggest that intermediate disorder will inhibit any quantum speedup, but also that large speedups are possible for quantum walks on complex networks with small disorder.
Acknowledgments
We thank A. Aspuru-Guzik, S. M. Girvin, T. Kottos, and S. Lloyd for helpful discussions. FWS was supported by the Research Corporation for Science Advancement.
Appendix A: Quantum Walk Transport
The transmission through the modified glued trees graph can be calculated by using the following ansatz for the column-space wavefunction
ΨMGT(n) =

  
  
eikn + Re−ikn for n < 0,
Aeik ̃n + Be−ik ̃n for 0 < n < d, Ceik ̃n + De−ik ̃n for d + 1 < n < 2d + 1, T eikn for n > 2d + 1. (A1) To determine T , one must use continuity of Ψ at n = 0 and 2d+1, and the Schr ̈odinger equation at n = 0, d, d+1,
and 2d + 1, with E = −2γ cos k = −2√2γ cos k ̃. These provide six equations for the six unknowns A, B, C, D, R, and T . For general k, these equations are most conveniently solved by computer, and have a rather complicated solution. For k = π/2, however, the solution for T is remarkably simple
T (k = π/2) = 8
9 + (−1)d . (A2)
This oscillation of T (k = π/2) as a function of d for the MGT facilitated the classical interpretation of Fig. 12. For comparison, the appropriate ansatz for the simple glued trees graph is
ΨSGT(n) =



eikn + Re−ikn for n < 0,
Aeik ̃n + Be−ik ̃n for 0 < n < 2d, T eikn for n > 2d,
(A3)
and the corresponding solution for the transmission coefficient is T (k = π/2) = 1, independent of d.
Appendix B: Classical Walk Transport
The scattering theory approach of Sec. IV can be modified to study classical diffusive transport through the modified glued trees graph. The model, depicted in Fig. 13, consists of an ingoing particle flux Γ to the left root. These particles then undergo a random walk in the interior of the graph, with diffusion rate λ, but can escape from either the left root (with rate λleft) or the right root (with rate λright). This is indicated by the directed paths on the left and right “tails” on the graph. In the steadystate, there is an outgoing flux to the left Γleft = pleftλleft and an outgoing flux to the right Γright = prightλright, with Γ = Γleft + Γright. The classical transmission coefficient introduced in the text is Tc = Γright/Γ. The calculation of Tc can be found by solving for the steady-state of the master equation
dpj
dt = ∑
k
Lj,kpk + bj , (B1)
where Lj,k is a matrix of rate constants, and bj is zero except for the input site (where it equals Γ). Due to the symmetry of the modified glued trees graph, we can write this equation in terms of the probabilities for the walker to be on each column, so that j = 0 → 2d + 1, pleft = p0, pright = p2d, and bj = Γδj,0. One can find the steady-state probability distribution from p~ss = −L−1~b. Here we provide an analytical calculation by solving for the steady state by recursion relations. In full, the master equation reads
dp0
dt = −(2λ + λleft)p0 + λp1 + Γ, (B2)


 11
!
"
!
"left
!
"right
FIG. 13: Transport approach to classical random walk on the modified glued trees graph. A steady-state flux is Γ introduced to the left root and carried away by the “tails” on the left and the right, with Γ = Γleft + Γright.
dpj
dt =



2λpj−1 − 3λpj + λpj+1 for 0 < j < d
2λpj−1 − 3λpj + 2λpj+1 for j = d and d + 1
λpj−1 − 3λpj + 2λpj+1 for d + 1 < j < 2d + 1 (B3) and
dp2d+1
dt = λp2d − (2λ + λright)p2d+1. (B4)
For the steady-state dp~/dt = 0, we can solve the reccurence relations
pj+1 = 3pj − 2pj−1 for j = 1 → d (B5) pj−1 = 3pj − 2pj+1 for j = 2d + 1 → d (B6)
in terms of p0 and p2d+1, respectively. We find
pj = 2j p0 + (2j − 1) λleft
λ p0 − (2j − 1) Γ
λ (B7)
p2d−j = 2j p2d+1 + (2j − 1) λright
λ p2d+1 (B8)
Requiring these two to solve dpd/dt = 0, we obtain one equation for p0 and p2d+1:
[
2d + (2d − 1) λleft
λ
]
p0 −
[
2d + (2d − 2−1) λright
λ
]
p2d+1
= (2d − 1) Γ
λ.
(B9) This can be combined with the conservation law
λleftp0 + λrightp2d+1 = Γ, (B10)
to solve for p0 and p2d+1. For the latter, we find
p2d+1 = Γ/λleft
1+
( λright λleft
)
+ 2(1 − 3 × 2−d−2)
( λright λ
).
(B11) Forming Tc = λrightp2d+1/Γ, and simplifying we find
Tc = 1 1+
( λleft λright
)
+ 2(1 − 3 × 2−d−2)
( λleft λ
) . (B12)
To complete our calculation, we estimate the diffusion rate λ as the product of the hopping rate (γ) and the transition probability between sites (γ2/W 2, for large W ). Finally, setting λleft = λright = γ and λ = γ3/W 2 yields
Tc = 1/2
1 + (1 − 3 × 2−d−2)(W/γ)2 , (B13)
a result very similar to that used in Sec. VI.
[1] N. Shenvi, J. Kempe, and K. B. Whaley, Phys. Rev. A 67, 052307 (2003). [2] A. M. Childs and J. Goldstone, Phys. Rev. A 70, 022314 (2004). [3] A. Ambainis, J. Kempe, and A. Rivosh, in Proceedings of the Sixteenth Annual ACM-SIAM Symposium on Discrete algorithms (Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2005), pp. 10991108. [4] A. M. Childs and J. Goldstone, Phys. Rev. A 70, 042312 (2004). [5] A. M. Childs, E. Farhi, and S. Gutmann, Quantum Inf. Process. 1, 35 (2002). [6] A. M. Childs, R. Cleve, E. Deotto, E. Farhi, S. Gutmann,
and D. A. Spielman, in Proceedings of the Thirty-fifth Annual ACM Symposium on Theory of Computing (ACM Press, New York, NY, USA, 2003), pp. 59–68. [7] J. Kempe, Approximation, Randomization, and Combinatorial Optimization 2764, 354 (2003). [8] E. Farhi, J. Goldstone, and S. Gutmann, Theory of Computing 4, 169 (2008). [9] A. M. Childs, R. Cleve, S. P. Jordan, and D. YongeMallo, Theory of Computing 5, 119 (2009). [10] A. M. Childs, Phys. Rev. Lett. 102, 180501 (2009). [11] N. B. Lovett, S. Cooper, M. Everitt, M. Trevers, and V. Kendon, Phys. Rev. A 81, 042330 (2010). [12] H. Krovi and T. A. Brun, Phys. Rev. A 75, 062332 (2007).


 12
[13] J. P. Keating, N. Linden, J. C. F. Matthews, and A. Winter, Physical Review A 76, 012315 (2007). [14] V. Kendon, eprint: arXiv: 1107.3795 (2011). [15] V. Kendon, Mathematical Structures in Comp. Sci. 17, 1169 (2007). [16] M. Mohseni, P. Rebentrost, S. Lloyd, and A. AspuruGuzik, Journal of Chemical Physics 129 (2008). [17] M. Jonson and S. M. Girvin, Physical Review Letters 43, 1447 (1979). [18] P. W. Anderson, Physical Review 109, 1492 (1958). [19] F. Evers and A. D. Mirlin, Rev. Mod. Phys. 80, 1355 (2008). [20] Y. Yin, D. E. Katsanos, and S. N. Evangelou, Phys. Rev. A 77, 022302 (2009). [21] A. Ahlbrecht, V. B. Scholz, and A. H. Werner, J. Math. Phys. 52, 102201 (2011). [22] M. Karski, L. Fo ̈rster, J.-M. Choi, A. Steffen, W. Alt, D. Meschede, and A. Widera, Science 325, 174 (2009). [23] H. Schmitz, R. Matjeschk, C. Scheider, J. Glueckert, M. Enderlein, T. Huber, and T. Schaetz, Phys. Rev. Lett. 103, 090504 (2009). [24] F. Za ̈hringer, G. Kirchmair, R. Gerritsma, E. Solano, R. Blatt, and C. F. Roos, Phys. Rev. Lett. 104, 100503 (2010). [25] M. A. Broome, A. Fedrizzi, B. P. Lanyon, I. Kassal, A. Aspuru-Guzik, and A. G. White, Phys. Rev. Lett. 104, 153602 (2010). [26] A. Schreiber, K. N. Cassemiro, V. Potocek, A. Gabris, I. Jex, and C. Silberhorn, Phys. Rev. Lett. 106, 180403 (2011). [27] F. W. Strauch and C. J. Williams, Phys. Rev. B 78, 094516 (2008). [28] C. Chudzicki and F. W. Strauch, Phys. Rev. Lett. 105, 260501 (2010). [29] S. Bose, Phys. Rev. Lett. 91, 207901 (2003). [30] S. Bose, Cont. Phys. 48, 13 (2008).
[31] R. E. Borland, in Proceedings of the Royal Society of London Series A (1963), vol. 274, pp. 529–545. [32] E. Abrahams, P. W. Anderson, D. C. Licciardello, and
T. V. Ramakrishnan, Physical Review Letters 42, 673 (1979). [33] M. Ostilli, Physica A 391, 3417 (2012). [34] J. D. Miller and B. Derrida, J. Stat. Phys. 74, 357 (1994). [35] C. Monthus and T. Garel, J. Phys. A. 42, 075002 (2009). [36] G. Biroli, G. Semerjian, and M. Tarzia, Prog. Theor. Phys. Suppl. 184, 187 (2010). [37] R. Abou-Chacra, D. J. Thouless, and P. W. Anderson, Journal of Physics C 6, 1734 (1973). [38] R. Abou-Chacra and D. J. Thouless, J. Phys. C 7, 65 (1974). [39] M. Sade and R. Berkovits, Phys. Rev. B 68, 193102 (2003). [40] M. Aizenman and S. Warzel, Math. Phys. Anal. Geom. 9, 291 (2006). [41] M. Aizenman and S. Warzel, Phys. Rev. Lett. 106, 136804 (2011). [42] M. Aizenman and S. Warzel, Europhys. Lett. 96, 37004 (2011). [43] A. Klein, Adv. in Math. 133, 163 (1998). [44] A. Klein, Commun. Math. Phys. 177, 755 (1996). [45] B. D. Hughes and M. Sahimi, J. Stat. Phys. 29, 781 (1982). [46] D. Cassi, Europhys. Lett. 9, 627 (1989). [47] C. Monthus and C. Texier, J. Phys. A 29, 2399 (1996). [48] E. Farhi and S. Gutmann, Phys. Rev. A 58, 915 (1998). [49] O. M ̈ulken and A. Blumen, Phys. Rep. 502, 37 (2011). [50] B. L. Douglas and J. B. Wang, Phys. Rev. A 79, 052335 (2009). [51] M. Varbanov and T. A. Brun, Phys. Rev. A 80, 052330 (2009). [52] A. F. Sadreev and I. Rotter, J. Phys. A 36, 11413 (2003). [53] A. Amir, Y. Lahini, and H. B. Perets, Phys. Rev. E 79, 050105(R) (2009). [54] L. Erdos, M. Salmhofer, and H.-T. Yau, eprint: arXiv: math-ph/0502025 (2005). [55] M. Varbanov and H. K. T. A. Brun, Phys. Rev. A 78, 022324 (2008).
