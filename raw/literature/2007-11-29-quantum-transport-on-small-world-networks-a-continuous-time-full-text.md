# Quantum transport on small-world networks: A continuous-time quantum walk approach - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevE.76.051125
> Collected: 2026-09-20
> Published: 2007-11-29
> Zotero parent key: K2539M6F
> Evidence: Zotero indexed PDF text

Quantum transport on small-world networks: A continuous-time quantum walk approach
Oliver Mülken,* Volker Pernice, and Alexander Blumen
Theoretische Polymerphysik, Universität Freiburg, Hermann-Herder-Straße 3, 79104 Freiburg, Germany Received 11 May 2007; revised manuscript received 31 July 2007; published 29 November 2007
We consider the quantum mechanical transport of coherent excitons on small-world networks SWNs . The SWNs are built from a one-dimensional ring of N nodes by randomly introducing B additional bonds between them. The exciton dynamics is modeled by continuous-time quantum walks, and we evaluate numerically the ensemble-averaged transition probability to reach any node of the network from the initially excited one. For sufficiently large B we find that the quantum mechanical transport through the SWNs is, first, very fast, given that the limiting value of the transition probability is reached very quickly, and second, that the transport does not lead to equipartition, given that on average the exciton is most likely to be found at the initial node.
DOI: 10.1103/PhysRevE.76.051125 PACS number s : 05.60.Gg, 05.60.Cd, 03.67. a, 71.35. y
I. INTRODUCTION
Many systems encountered in nature cannot be described by simple lattice models. In general such systems are characterized by graphs whose bonds connect sites with a wide distribution of mutual distances. Examples can be found in various fields, ranging from physics or biology to social studies or computer science; see 1–3 and references therein. More specifically, some of these systems can be described by small-world networks SWNs , which have large clustering coefficients but short characteristic path lengths 2 . The statistical properties of SWN have been studied to a great extent and are now well understood. A large variety of dynamical processes on graphs are related to the spectrum of the discrete Laplacian of the underlying topological network 4–6 . For classical diffusion on SWNs, which has been modeled, for instance, by random walks 7,8 , it was found that the probability to be still or again at the initial site has a complex dependence on the number n of steps; i.e., at short times it decays as a power law of n, whereas at longer times it has a stretched exponential dependence on n. The quantum dynamics on SWNs has been studied mainly in the framework of the localizationdelocalization transition 9,10 , where one has also assumed an additional on-site disorder. Here, the transition depends on the complexity of the SWNs. A comparison between classical and quantum diffusion was given in 11 , where a quantum diffusion time defined as the time where the participation ratio of the time-dependent wave function has dropped to a certain value was shown to be faster than its classical counterpart. However, even here little consideration has been given to the full set of eigenvectors of such systems, which become important in the quantum mechanical extension of the classical diffusion process. To be specific, a quantum mechanical analog of continuous-time random walks CTRWs can be defined by identifying the Laplacian or connectivity matrix A of the network with the Hamiltonian H. For simple lattices this corresponds, in fact, to a nearest-neighbor hopping model 12–16 . The transformation replaces the classical diffusion
process by a quantal propagation of the excitation through the network. Due to its formal similarity to CTRWs, the procedure was dubbed a continuous-time quantum walk CTQW . In fact, it is known in other branches of physics under different names, such as the tight-binding model in solid-state physics 17 or the Hückel linear combination of molecular orbitals, LCMO model in physical chemistry 18 . CTQWs are also closely related to so-called quantum graphs QGs —see, for instance, 19–22 —whose connectivity matrix is defined in a similar way. However, QGs explicitly consider the bond between two nodes in the sense that bonds may be directed and are given a varying length. Thus, CTQWs are, to some extent, a simplified version of QGs. Quite recently, Smilansky discussed the connections between discrete Laplacians equivalently, between the connectivity matrices on discrete QG and periodic orbits 23 . There is certainly a large mathematical backbone on which to establish further connections; see, for instance, 24 .
II. QUANTUM WALKS ON NETWORKS
Here, we consider transport processes CTQWs and CTRWs on networks, which allows us to study the two extreme cases of transport processes on such structures: namely, purely quantum mechanical CTQWs and purely classical CTRWs processes. Networks are a collection of N connected nodes. The periodicity of regular networks can be destroyed by randomly including B additional bonds into the network. In such a way one creates “shortcuts” and a walker can find shorter paths between pairs of sites than on the regular network. In the following we create the SWNs by randomly adding bonds to a regular one-dimensional ring; see Fig. 1. However, we forbid self-connections—i.e., bonds connecting one node with itself. We denote by j a state associated with a localized excitation at node j and take the set j to be orthonormal. For CTRWs on undirected and unweighted networks the transfer matrix is given by the discrete Laplacian A of the network, by which we assume equal transition rates 1 between all nodes. The matrix A has as nondiagonal elements Ak,j the values −1 if nodes k and j of the network are connected by a bond and 0 otherwise. The diagonal elements Aj,j of A equal the number of bonds f j which exit from node j. Quantum
*muelken@physik.uni-freiburg.de
PHYSICAL REVIEW E 76, 051125 2007
1539-3755/2007/76 5 /051125 8 051125-1 ©2007 The American Physical Society


 mechanically, the states j span the whole accessible Hilbert space; the time evolution of an excitation initially placed at node j is determined by the systems’ Hamiltonian H = A and reads exp −iHt j , where we set 1. The classical and quantum mechanical transition probabilities to go from the state j at time 0 to the state k in time t are given by pk,j t k exp −At j and by k,j t k,j t 2 k exp −iHt j 2, respectively. By fixing the coupling strength between two nodes Hj,j±1 = 1, the time unit / Hj,j±1 for the transfer between two nodes is set to unity. From the eigenvalues En of the Hamiltonian H or Laplacian A follows the density of states DOS or spectral density of the given system of size N,
E =1
N n=1
N
E − En . 1
The DOS contains the essential information about the system and shows distinct features which depend on the network’s topology. These features also carry over to dynamical properties, which in some cases depend only on the En. For example, the average classical probability to be still or again at the initially excited node,
 ̄p t = 1
N n=1
N
e−Ent, 2
depends solely on the En of A, but not on the eigenstates n 4,5 . In the quantum case, we find a lower bound to
 ̄t 1
N j=1
N
j,j t , which also depends only on the En 15,25 ,
 ̄ t  ̄ t 2= 1
N n=1
N
e−iEnt
2
,3
where  ̄ t 1
N j=1
N
j,j t . We hasten to note that the lower bound is exact for regular networks 15,16 . The quantity  ̄ t 2 given in Eq. 3 has also been derived in a different context as being the form factor of QG 19 .
III. CTQWs ON SWNs
We will analyze the general behavior of CTQWs on SWNs by averaging over distinct realizations R:
 ̄R
1
R r=1
R
 ̄ r, 4
where the index r specifies the rth realization of the quantity in question. In so doing we obtain statistical results which allow for a comparison with the classical ones. In particular, we will consider the realization-averaged transition probabilities kj t R, the averaged probabilities  ̄ t R, their lower bound  ̄ t R, and their classical analog  ̄p t R. Furthermore, we also calculate the long time average LTA of each quantity:
lim
T→
1
T0
T
dt  ̄
R
.5
For the numerical evaluation we make use of the standard software package MATLAB. Specifically, we focus on SWNs of size N = 100 with B = 1, 2, 5, and 100 additional bonds; the ensemble average is, in general, performed over R = 500 realizations, which guarantees a sufficiently large number of samples under manageable computing times.
A. Random matrix theory
Before going into the details of our analysis, we like to point to the differences and similarities of SWNs with other approaches to study quantum transport processes. Classical transport over SWNs differs from that over other systems, such as regular lattices or fractal networks, in that the transport becomes faster: While the probability to return to the origin decays as t−1/2 for regular networks, it decays as a stretched exponential for SWNs 7,8 , vide infra Fig. 5 a . While the classical dynamics over SWNs is by now well understood, little is known about the quantum dynamics on such networks. In general, several dynamical properties of networks depend only on the DOS of the system’s Hamiltonian 26 . We choose the additional bonds of our SWNs randomly; thus, the corresponding Hamiltonian will have entries at random positions in the matrix. This has to be distinguished to some extent from random matrix theory RMT 27 . However, there are also similarities between RMT and SWNs. The DOS of SWNs have been compared to RMT in 28 , where it was found that the level spacing E En+1 − En of the DOS of SWNs can be fitted by the so-called Brody distribution, which interpolates between Poissonian and Wigner-Dyson
FIG. 1. Sketch of a SWN of size N = 16 containing B = 11 additional bonds.
MÜLKEN, PERNICE, AND BLUMEN PHYSICAL REVIEW E 76, 051125 2007
051125-2


 level spacings statistics; see 28 for details. The SWN considered in Ref. 28 is a Watts-Strogatz network, obtained by randomly permuting the bonds of a regular one-dimensional network. The eigenvalue statistics of random networks have been studied in Ref. 29 and in the works referenced therein; the quantum dynamics on regular disordered networks has been considered in 30 . Now, the DOS of a SWN differs from that of networks whose sites have been totally randomly connected; the DOS of the latter networks follow Wigner’s semicircle law. Figure 2 shows for SWNs with N = 100 nodes and B = 1, 2, 5, and 100 additional bonds histograms of the average DOS E and of the level spacing distribution P E , where E is normalized in such a way that the average E = 1. While for small B the DOS barely changes, the level spacing distribution shows more drastic changes; see Figs. 2 a –2 c and 2 e –2 g . The appearance of large isolated eigenvalues results in a nonvanishing P E for large E. In Figs. 2 e –2 h plots of P E we also show the Poissonian exp − E , dashed line and Wigner-Dyson ( E / 2 exp − E / 2 2 , dash-dotted line) statistics. While P E roughly follows the Poissonian statistics for B = 1 Fig. 2 e , this is not the case when increasing B. Especially the tail of the distribution P E is better fitted by the Wigner-Dyson statistics Figs. 2 f and 2 g . However, when increasing B to the order of N Fig. 2 h , the tail of P E decays neither as exp − E dashed line nor as exp − E2 dash-dotted line , but rather as exp − E , with 1.2 solid line .
Thus, the complexity of the DOS of SWNs compared, e.g., to the semicircle law leads to dynamical properties of the SWNs not all of which can be captured by RMT.
B. Transition probabilities
The ensemble average of the transition probabilities kj t R allows a first glimpse at the behavior of CTQWs on SWNs. Figure 3 shows kj t R for several SWNs with N = 100 nodes and different B. Note that due to the ensemble average we can choose the initial node j freely, and we thus take j = 50. In the absence of any additional bond, the excitations travel along the ring and interfere in a very regular manner, producing discrete quantum carpets 14 . Typical for these carpets is that they show, depending on N, full or partial revivals at specific times 14 . For SWNs the situation is quite different. Already a few additional bonds obliterate the quantum carpets; the patterns fade away. By adding more bonds, only the initial node retains a significant value for jj t R at all times t. Furthermore, already for SWNs with as little as B = 5 the pattern of jj t R becomes quite regular after a short time; see Fig. 3 c . This almost regular shape is reached very quickly when B gets to be comparable to N Fig. 3 d . We note, however, that particular realizations may still show depending on their actual additional bonds strong interference patterns. These features are washed out by the ensemble average, so that only the dependence on the initial node stands out. We
0 123456 E
0
1
2
3
4
5
6
7
ρ(E)
0 123456 E
0
1
2
3
4
5
6
7
0 123456 E
0
1
2
3
4
5
6
0 2 4 6 8 10 12 14 E
0
0.5
1
1.5
2
0 1234 ∆E
0
0.2
0.4
0.6
0.8
1
P(∆E)
0 1234 ∆E
0
0.2
0.4
0.6
0.8
1 Poissonian
Wigner-Dyson
0 123456 ∆E
0
0.2
0.4
0.6
0.8
1
0 123456 ∆E
0
0.2
0.4
0.6
0.8
1
05
exp(-∆E1.2) exp(-∆E)
exp(-∆E2)
(a) (b) (c) (d)
(e)
(f)
(g)
(h)
FIG. 2. Color online DOS E a – d and level spacing distribution P E e – f of SWNs with N = 100 nodes and B = 1 a , e , 2 b , f , 5 c , g , and 100 d , h additional bonds. The lower panels e – g show also the Poissonian dashed line and Wigner-Dyson dash-dotted line statistics; panel h shows fits of the tails of P E with different exponentials.
QUANTUM TRANSPORT ON SMALL-WORLD NETWORKS: ... PHYSICAL REVIEW E 76, 051125 2007
051125-3


 will return to the discussion of the transition probabilities kj t R in Sec. III D. For the ring the LTA can be calculated analytically. Depending on whether N is even or odd, the LTAs are slightly different 14 . For even N superscript e there are two maxima at k = j and at k = j + N / 2, both having the value
k,j
e limT→
1 T0
Tdt k,j t = 2N − 2 / N2; this is due to the fact that the number of nodes from j to j + N / 2 is the same in both directions, which leads to constructive interference. On the other hand, for odd N superscript o there is only one maximum at k = j, k,j
o = 2N − 1 / N2. Figure 4 shows k,j R for SWNs of size N = 100 with B = 1, 2, 5, and 100. For B = 1 and fixed j, the two peaks of the regular network turn into a main peak and into a much
weaker side peak at k = j + N / 2. This structure is still barely visible for B = 2. Already for B = 5 the side peak has practically vanished; see Fig. 4 c . While for B = 1, 2, and 5 also structure around the main peak is visible, for B = 100, the k,j R are sharply peaked at k = j. We stress that this should not be confused with the Anderson localization, since there is a nonvanishing probability to go from node j to all other nodes k j. The sharp peak of jj t R at the initial node j is only the result of ensemble averaging.
C. Return probabilities
Since CTQWs on SWNs always carry information of their initial node j, the averaged probabilities to return to j are a
FIG. 3. Time dependence of the averaged transition probabilities kj t R for SWNs of size N = 100 with a B = 1, b B = 2, c B = 5, and d B = 100. The initial node is j = 50 and the number of realizations is R = 500.
10 20 30 40 50 60 70 80 90
100
10 20 30 40 50 60 70 80 90 100
10 20 30 40 50 60 70 80 90
100
10 20 30 40 50 60 70 80 90 100
10 20 30 40 50 60 70 80 90
100
10 20 30 40 50 60 70 80 90 100
10 20 30 40 50 60 70 80 90
100
10 20 30 40 50 60 70 80 90 100
node k node k
node j node j
(a) (b)
(c) (d)
FIG. 4. Long-time average k,j R for SWNs of size N = 100 with a B = 1, b B = 2, c B = 5, and d B = 100. The number of realizations is R = 500. Dark regions denote large values of k,j R and bright regions low values of k,j R.
MÜLKEN, PERNICE, AND BLUMEN PHYSICAL REVIEW E 76, 051125 2007
051125-4


 good measure to quantify the efficiency of the transport on such networks 25 . Figure 5 shows in double-logarithmic scales the ensemble averages  ̄p t R,  ̄ t R, and  ̄ t R for SWNs with N = 100 nodes and B = 1, 2, 5, and 100. For classical transport Fig. 5 a the initial decay of  ̄p t R occurs faster for larger B. The decay at intermediate times follows a power law t−1/2 for the ring as is clear from the linear behavior in the scales of the figure and changes to a stretched exponential type when B is large 7 . Thus, a classical excitation will quickly explore the whole SWN, so that it will occupy each site with equal probability of 1 / N already after a relatively short time, see the final plateau in Fig. 5 a . Quantum mechanically, however, the situation is more complex. Let us start with the ensemble average  ̄ t R, shown in Fig. 5 b . For a ring of N nodes B = 0 and for times smaller than roughly N / 2,  ̄ t R displays a quasiperiodic pattern, the maxima of which decay as t−1. At longer times interference sets in and leads to an irregular behavior at times larger than N / 2 25 . Now, for SWNs, as long as B is considerably less than N, the periodic pattern still remains visible; in Fig. 5 b , one can follow how an increase in B is smoothing out the curves, so that both the heights of the first maxima and the depths of the minima decrease. At longer times the SWN patterns are flattened out and  ̄ t R tends towards a limiting value. With increasing B this asymptotic domain is reached more quickly. To emphasize this point we display in Fig. 6 in an enlarged scale the data of Fig. 5 b in
the time interval 1,100 . Clearly, for larger B the crossover from the quasiperiodic behavior at short times to a smoothed out pattern at longer times is shifted to smaller t. In Fig. 5 c we plot the lower bound of  ̄ t , namely  ̄ t 2 R averaged over the realizations. We note that the overall behavior of Figs. 5 b and 5 c is quite similar. However, the limiting values at long times differ. For the LTA of  ̄ t R we have see also Eq. 17 of Ref. 31
 ̄ R lim
T→
1
T0
T
dt ̄ t
R
=1
RN r,j,n,n
En,r − En ,r j n,r j n ,r 2, 6
where En,r − En ,r = 1 for En,r = En ,r and En,r − En ,r = 0 otherwise. For  ̄ t 2 R the long-time values for different B collapse to one value. In fact, the LTA of  ̄ t 2 R obeys
lim
T→
1
T0
T
dt  ̄ t 2
R
=1
RN2
r,n,n
En,r − En ,r , 7
as can be immediately inferred from Eq. 3 . Thus this quantity is only a function of the eigenvalues En,r and does not depend on the eigenstates n,r . In order to quantify the differences between Eqs. 6 and 7 for SWNs, we will assume that all the eigenvalues are nondegenerate this assumption is, of course, not valid for the ring; see below . In Eq. 7 the triple sum adds then to RN, so that the right-hand side rhs equals 1 / N. On the other hand, Eq. 6 leads to
 ̄ R= 1
RN r,j,n
j n,r 4. 8
This expression depends on the eigenstates; in fact, the rhs of Eq. 8 is the ensemble average of the averaged participation ratio of the eigenstates n,r . Equation 8 is well known in the theory of quantum localization; see, e.g., Sec. V A. in 32 . Now, Fig. 7 shows the behavior of  ̄ R, according to Eq. 6 , for a SWN with N = 100, 500, and 1000 nodes as a function of B / N we restrict ourselves to even N; the case of odd N is similar . Increasing B results in an increase of  ̄ R, starting from the corresponding value for the ring B = 0, only one realization, and N even ,
10-3
10-2
10-1
100
< p(t) >R
0 1 2 5 100
10-3
10-2
10-1
100
< π(t) >R
100 101 102 103 104 time t
10-3
10-2
10-1
100
< |α(t)|2>R
(a)
(b)
(c)
FIG. 5. Color online Time dependence of the averaged probabilities a  ̄p t R, b  ̄ t R, and c  ̄ t 2 R for SWNs of size N = 100 with B = 1, 2, 5, and 100. The number of realizations is R = 500.
1 10 100 time t
10-2
10-1
< π(t) >R
0 12
5 100
FIG. 6. Color online Close-up of Fig. 5 b for short times t = 1 , . . . , 100.
QUANTUM TRANSPORT ON SMALL-WORLD NETWORKS: ... PHYSICAL REVIEW E 76, 051125 2007
051125-5


  ̄ ring R  ̄ = 1
Nj
jj = 2N − 2
N2 , 9
where jj = 2N − 2 / N2. From Eq. 7 we obtain a 1 / N dependence for the LTA of  ̄ t 2 R, which by rescaling with  ̄ ring R 1 / N would result in a constant value for large N. However, rescaling  ̄ R with  ̄ ring R shows an increase with N of  ̄ R /  ̄ ring R which is less than linear; thus,  ̄ R depends on N as 1 / N , with 1 , 2 . Additionally, for larger N see N = 500 and 1000 ,  ̄ R has a maximum value at B / N 0.14, which is not present for smaller N see N = 100 , meaning that for this ratio of B / N the transport from the initial node to all others is least probable, a fact which remains unclear. A detailed study of the N dependence will be given elsewhere. When increasing B to the order of N,  ̄ R saturates to a plateau which increases monotonically with N. Thus, an increase in the number of nodes leads to a less probable transport from the initial node to all others. We further note that with increasing B the structures of  ̄ t 2 R and  ̄ t R differ even at short times, while for the ring the relation  ̄ t =  ̄ t 2 holds exactly. In Ref. 25 we showed that  ̄p t R and  ̄ t R or  ̄ t 2 R can be regarded as measures for the efficiency of the excitonic transport. When increasing B, the initial quantum transport through the SWN takes place—on averageduring a very short time scale see Fig. 3 compared to the
ring, where an excitation takes about t = N / 2 to travel around the ring 14 . Additionally and in contrast to the classical case, where the limiting value is always given by the equipartition value 1 / N, for CTQWs the limiting probability to be still or again at the initial node increases with B. Thus, an exciton is on average more likely to be found at the initial node, a feature which is not captured by the lower bound  ̄ t 2 R. Therefore,  ̄ t 2 R as, for instance, shown in Fig. 5 c does not capture fine details of the transport, which the full expression  ̄ t R does.
D. Participation ratio of eigenstates
For the ring the eigenstates are Bloch states,
n= 1
N j=1
N
eiEnj j , 10
from which k n 4 = 1 / N2 follows for all n . By naively inserting this result into Eq. 8 one obtains  ̄ R = 1 / N, which differs from the exact result, Eq. 9 , by a factor of 2. The reason for this difference is that for a ring most of the eigenvalues are doubly degenerate. For SWNs, on the other hand, most eigenvalues are nondegenerate. The fact that, as is evident from Fig. 7,  ̄ R for SWNs increases with increasing B points towards a change of the k n 4 from the value 1 / N2. In order to quantify the difference to the ring case we plot in Fig. 8 the average distribution of eigenstates,
n,j R
1
RN r
j n,r 4, 11
for SWNs with N = 100 with B = 1, 2, 5, and 100. From Fig. 8 we remark that the n,j R increase with increasing B. Additionally, the fluctuations between different values of n,j R become larger, too. This results in a substantial increase of  ̄ R for larger B. We stress the particular role played by the eigenstate 0 = N−1/2 j j , which corresponds to the eigen
value E0 = 0 and for which 0,j R = 1 / N3. Most of the other states contribute more to  ̄ R. In particular for SWNs with large B, Fig. 8 d , one finds large values for n,j R close to
0 0.2 0.4 0.6 0.8 1 B/N
0
1
2
3
4
5
6
7
< χ >R / [(2N-2)/N2]
N = 100 N = 500 N = 1000
FIG. 7. Color online The LTA of  ̄ t R,  ̄ R, for SWNs with N = 100, 500, and 1000 nodes as a function of B / N.
FIG. 8. The function n,j R, Eq. 11 , for SWNs of size N = 100 with a B = 1, b B = 2, c B = 5, and d B = 100. Note the different scaling of the z axis in d . The number of realizations is R = 500.
MÜLKEN, PERNICE, AND BLUMEN PHYSICAL REVIEW E 76, 051125 2007
051125-6


 the band edges of En i.e., for n close to 0 and close to N , in accordance with previous work; see, for instance, Ref. 33 . The situation may be visualized as follows: For the ring all eigenstates are Bloch states and hence are completely delocalized. Going over to SWNs and increasing the number of additional bonds B leads to localized states at the band edges and to fairly delocalized states well inside the band. The increase of  ̄ R shown in Fig. 6 is thus mainly due to the localized band edge states. The participation ratio also dominates the transition probabilities kj t R, which were presented in Fig. 3 in Sec. III B. In general, the kj t = k exp −iHt j 2 averaged over the distinct realizations read
kj t R = 1
Rr n
e−iEn,rt k n,r n,r j 2. 12
Under the assumption that the eigenvalues of SWNs are nondegenerate, we obtain for the initial node j
jj t R = 1
Rr n
j n,r 4
+
n n ,n
e−i En,r−En ,r t j n,r 2 j n ,r 2 .
13
The fluctuations for larger t t-dependent sum in Eq. 13 become suppressed due to the ensemble average. As can be inferred from Figs. 3 a –3 c , when increasing B from B = 0 only slightly up to B / N = 0.05, the fluctuations are already strongly suppressed. Larger values of B see Fig. 3 d for B / N = 1 result in a very strong peak at the initial node j. Hence, the fluctuations at the other nodes k j become more and more suppressed in the ensemble average when increasing B. Now, averaging the time-independent term of Eq. 13 over all nodes j one recovers the LTA of  ̄ t R see Eqs. 6 and 8 :
1
Nj
1
Rr n
j n,r 4 =  ̄ R. 14
In the ensemble average, all nodes j can be considered roughly equal; thus, every node j gives approximately the same contribution to the sum over j and we get therefore
 ̄R
1
R rn j n,r 4 jj t R. Figure 7 shows that for in
creasing B the LTA  ̄ R is always larger than 2N − 2 / N2 the corresponding value for the ring , also leading to the almost regular shape of the transition probabilities kj t R shown in Fig. 3. As noted earlier, single realizations may still show strong interference patterns. For QGs, Kottos and Schanz have given conditions for finding almost scarred eigenfunctions states with excess density near unstable periodic orbits of the corresponding classical chaotic system 22 . In combination with Smilansky’s work on discrete QGs 23 , it might be possible in the future to obtain similar conditions for the networks considered here. We stress again that there is no Anderson localization in our system. Although the states are localized for large B, there is still a nonvanishing transition probability to go from the initial node j to all other nodes. Thus, the additional bonds in the SWN do not prohibit the transport through the network completely, but just hinder it. Adding disorder to our system will essentially result in the model considered in Ref. 10 . In this work, the Anderson model was augmented by additional bonds, such that a SWN develops, which lead to the localization-delocalization transition.
IV. CONCLUSION
We modeled the quantum mechanical transport of coherent excitons on small-world networks by continuous-time quantum walks and computed the ensemble average of the transition probability to go from one node of the network to any other node. The transport through the network turns out to become faster with increasing the number of additional bonds. Distinct from the classical case, however, where the information of the initial node is quickly lost, quantum mechanically this information is preserved. During its time development the exciton is on average most likely to be found at the initial node. The reason for this is to be found in the network’s eigenstates, which are localized at the band edges, whereas they are quite delocalized inside the band.
ACKNOWLEDGMENTS
Support from the Deutsche Forschungsgemeinschaft DFG , the Fonds der Chemischen Industrie, and the Ministry of Science, Research and the Arts of Baden-Württemberg Grant No. 24-7532.23-11-11/1 is gratefully acknowledged.
1 D. J. Watts and S. H. Strogatz, Nature London 393, 440 1998 . 2 R. Albert and A.-L. Barabási, Rev. Mod. Phys. 74, 47 2002 . 3 S. N. Dorogovtsev and J. F. F. Mendes, Adv. Phys. 51, 1079 2002 . 4 S. Alexander and R. Orbach, J. Phys. France Lett. 43, L625 1982 . 5 A. J. Bray and G. J. Rodgers, Phys. Rev. B 38, 11461 1988 . 6 R. Monasson, Eur. Phys. J. B 12, 555 1999 .
7 S. Jespersen, I. M. Sokolov, and A. Blumen, Phys. Rev. E 62, 4405 2000 . 8 S. Jespersen and A. Blumen, Phys. Rev. E 62, 6270 2000 . 9 C. P. Zhu and S.-J. Xiong, Phys. Rev. B 62, 14780 2000 . 10 O. Giraud, B. Georgeot, and D. L. Shepelyansky, Phys. Rev. E 72, 036203 2005 . 11 B. J. Kim, H. Hong, and M. Y. Choi, Phys. Rev. B 68, 014304 2003 . 12 E. Farhi and S. Gutmann, Phys. Rev. A 58, 915 1998 .
QUANTUM TRANSPORT ON SMALL-WORLD NETWORKS: ... PHYSICAL REVIEW E 76, 051125 2007
051125-7


 13 A. M. Childs, E. Farhi, and S. Gutmann, Quantum Inf. Process. 1, 35 2002 . 14 O. Mülken and A. Blumen, Phys. Rev. E 71, 036128 2005 . 15 O. Mülken, V. Bierbaum, and A. Blumen, J. Chem. Phys. 124, 124905 2006 . 16 A. Blumen, V. Bierbaum, and O. Mülken, Physica A 371, 10 2006 .
17 J. M. Ziman, Principles of the Theory of Solids Cambridge University Press, Cambridge, England, 1972 . 18 D. A. McQuarrie, Quantum Chemistry Oxford University Press, Oxford, 1983 . 19 T. Kottos and U. Smilansky, Phys. Rev. Lett. 79, 4794 1997 . 20 H. Schanz and U. Smilansky, Phys. Rev. Lett. 84, 1427 2000 . 21 T. Kottos and U. Smilansky, Phys. Rev. Lett. 85, 968 2000 . 22 H. Schanz and T. Kottos, Phys. Rev. Lett. 90, 234101 2003 . 23 U. Smilansky, J. Phys. A 40, F621 2007 . 24 P. Kuchment, Waves Random Media 14, S107 2004 ; J. Phys.
A 38, 4887 2005 . 25 O. Mülken and A. Blumen, Phys. Rev. E 73, 066117 2006 . 26 D. M. Cvetković, M. Doob, and H. Sachs, Spectra of Graphs: Theory and Applications, 3rd ed. Academic Press, New York, 1997 . 27 M. L. Mehta, Random Matrices Academic Press, San Diego, 1991 . 28 J. N. Bandyopadhyay and S. Jalan, Phys. Rev. E 76, 026109 2007 . 29 A. D. Mirlin, Phys. Rep. 326, 259 2000 . 30 R. Klesse and M. Metzler, Int. J. Mod. Phys. C 10, 577 1999 . 31 O. Mülken, A. Volta, and A. Blumen, Phys. Rev. A 72, 042334 2005 . 32 E. J. Heller, Phys. Rev. A 35, 1360 1987 . 33 I. J. Farkas, I. Derényi, A.-L. Barabási, and T. Vicsek, Phys. Rev. E 64, 026704 2001 .
MÜLKEN, PERNICE, AND BLUMEN PHYSICAL REVIEW E 76, 051125 2007
051125-8
