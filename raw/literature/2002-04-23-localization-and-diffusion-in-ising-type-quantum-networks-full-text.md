# Localization and diffusion in Ising-type quantum networks - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.65.052110
> Collected: 2026-09-20
> Published: 2002-04-23
> Zotero parent key: BBN4UNYD
> Evidence: Zotero indexed PDF text

arXiv:quant-ph/0103169v1 30 Mar 2001
Localization and diffusion in Ising-type quantum networks
P. T ̈orm ̈a(a), I. Jex(b), and W.P. Schleich(c)
(August 1, 2021)
(a) Laboratory of Computational Engineering, P.O.B. 9400, FIN-02015 Helsinki University of Technol
ogy, Finland
(b) Department of Physics, FNSPE, Czech Technical University Prague, Bˇrehov ́a 7, 115 19 Praha 1,
Czech Republic
(c) Abteilung f ̈ur Quantenphysik, Universit ̈at Ulm, Albert-Einstein Allee 15, D-89081 Ulm, Germany
PACS numbers: 42.50.-p, 05.45.-a, 05.50.+q
We investigate the effect of phase randomness in Ising-type quantum networks. These
networks model a large class of physical systems. They describe micro- and nanostruc
tures or arrays of optical elements such as beam splitters (interferometers) or parameteric
amplifiers. Most of these stuctures are promising candidates for quantum information pro
cessing networks. We demonstrate that such systems exhibit two very distinct types of
behaviour. For certain network configurations (parameters), they show quantum local
ization similar to Anderson localization whereas classical stochastic behaviour is observed
in other cases. We relate these findings to the standard theory of quantum localization.
I. INTRODUCTION
Maturing of the techniques for controlling single quantum systems such as atoms, photons, or quantum
dots has made it possible to design more complicated structures of these basic elements: quantum net
works. Interesting examples of such micro- and nanostructures are for instance thin wires used as atom
guides [1], trapped chains of atoms and ions [2], or structures grown on a substrate such as quantum
dots [3] or arrays of nanomagnets. These are among the first steps of laboratory demonstrations leading
to quantum network engineering and finally to matured and scalable quantum technology. Due to these
possible applications investigations of quantum networks have become topical.
In this paper we consider a quantum network configuration which is perhaps the simplest non-trivial
one: a network which realizes nearest-neighbour interactions by coupling the individual quantum systems
pairwise. As a possible implementation one can think of light modes coupled together by an optical
element, for example a beam splitter or a mode coupler. The network is schematically presented in
Fig.1. Another common form of nearest neighbour interaction is simulataneous interaction with many
neighbours, like electrons interacting with Coulomb interaction. Here we, however, consider pairwise
interaction which is typical for light modes, and for many quantum networks in general.
1


 A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
U motif
FIG. 1. A schematic presentation of the considered quantum network. The nodes are connected to their nearest
neighbours. The boxes A and B denote the transformations performed at the nodes; they could correspond
for instance to beam splitters in case of an optical realization.
The network in Fig.1 has an interesting and potentially useful connection to the Ising-model [4,5].
Interference effects are typical in this kind of networks and have been investigated by many authors [6–9].
The Hamiltonian structure of the network was studied in [10]. In this paper we consider the effect of
randomness in such a network. Randomness in certain quantum systems is know to lead to intriguing
effects such as Anderson localization and dynamical localization [11–13]. Also classical wave behaviour
combined with randomness can lead to localization, c.f. localization of light [14,15]
We can view the considered network also as a interferometer. The effects demonstrated can be under
stood as the result of interferences between paths available for the excitations in the network. However,
interferences are known to be very fragile towards phase perturbations. We show that the typical inter
ference effects are modified or completely destroyed as randomness is introduced in the network.
The way in which the randomness enters the network has a profound effect on the behaviour. Therefore
we consider two basic variants of the network. First, a 2-D network of the type shown in Fig.1, with
randomness all over the network. This means that along each connecting line between two interaction
nodes, the phase (free time evolution) is changed randomly within the possible range of 〈0, 2π〉. A
corresponding physical system could be for example a network of optical elements with phase fluctuations
arising from different optical lengths between the elements. The fluctuations could be produced at will
with phase shifters to make systematic studies of the effect of randomness. Alternatively, our calculations
can model undesired phase fluctuations in optical networks and can be used to study the stability of
interference effects in a complicated interferometer. We show that in the random 2-D network classical
stochastic diffusion is typical.
In the second configuration considered, the network models a 1-D system. Now the basic unit of the
network contains fixed randomness. The basic unit is formed by the two columns of A and B (”the motif”
element for building the network) in Fig.1, and along the connecting lines between the columns the phase
is adjusted arbitrarily, i.e., within the range of 〈0, 2π〉. In such a way we define a random motif matrix.
Then this very same basic unit is precisely repeated M times. The horizontal dimension of the network
can now be understood as time and the network actually models time evolution in one dimension (the
2


 vertical dimension is the real space or a mode space). Note that the configuration also corresponds to
a thin layer of material inside a cavity, with a light pulse crossing it several times: the 1-D propagation
is now the spreading of the light along the material layer after many cavity crossings. We show that
randomness in the 1-D type configuration leads to quantum localization.
We explain the different behaviour of the two configurations by relating our observations to the stan
dard theory of localization. The theory of Anderson localization and dynamical localization is formulated
considering the properties of the Hamiltonian for the system of interest. This is not always the best possi
ble approach in the quantum engineering context, where the individual components of a more complicated
network are described by a unitary transform. The transfer matrix for the total network is easily obtained
by simple multiplications of the transfer matrices corresponding to the individual elements, but to find
out the Hamiltonian corresponding to the complex system is non-trivial if not impossible [10]. Therefore
we find it of interest to consider here, for the first time to our knowledge, the quantum localization
problem by starting the theoretical description from the transfer matrices of the system.
Note that in the mathematical level, the unitary transforms describing the network can also be under
stood as operations performed in the computational space of a quantum computer. Thus our investiga
tions also relate to decoherence affecting certain types of computational operations. Nearest-neighbour
coupling configurations have been considered in the quantum information context recently [16,17].
In section 2 we introduce the transfer matrix which is the common starting point for both network
configurations of interest. The first configuration, leading to classical diffusion, is considered in section
3, the second, showing localization, in section 4. Differences in the quantum behaviour in these two
cases are explained with the theory of Anderson/dynamical localization in section 5. The conclusions are
presented in section 6.
II. THE TRANSFER MATRIX
The network we consider realizes the nearest-neighbour structure given in Fig.1. Each element (box in
the figure) represents a 2 × 2 coupler, e.g. a beam-splitter in case of optical networks. The whole network
is build up by repeating the motif structure consisting of a row of components A and B , i.e., we use
the outputs of the motif as the input for the next layer. We assume periodic boundary conditions [4,5].
The transfer matrix describing the motif unit has the form
U=

            
A 00
00
···
···
00
00 A
... ... . . .
A

            

            
B22 0 0 · · · B21
0
0B
... B
...
B12 B11

            
, (1)
where
A=


cos θ sin θ
− sin θ cos θ

; B =


cos φ sin φ
− sin φ cos φ

 . (2)
3


 When the parameters θ and φ are real, (2) describes a SU(2) network. Purely imaginary θ and φ
correspond to a SU(1,1) network. Above, sin2 x (x is θ or φ) gives the coupling strengths of the elementary
units used and N is the number of the units in one layer. We will consider only the case cos2 x = 0.5. In
optics, this corresponds to so called balanced beam splitters (or 3-dB couplers).
The transfer matrix W of the whole network, in the case all motif sturctures are the same, is given as
a power of U :
W (M ) = U M . (3)
The other possibility is that all the motif structures Ui, i ∈ [1, M ] are different due to overall randomness,
then
W (M ) = U1D1U2D2...UM . (4)
The matrices Di represent diagonal matrices giving the phase uncertainities between the random motifs.
Here M can be understood as the size (2N × M ) of the network in the case of a 2-D network, or as time
when the network models 1-D propagation.
An example of the typical interference behaviour in complete absence of randomness is presented in
Fig.2
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
UU
A
0 10 20 30 40
n
-12
-10
-8
-6
-4
-20
FIG. 2. A typical interference pattern in the case of no randomness in the network. The left picture shows the
repetition of the motif structure of the network, the right the logarithm of the probability P to find the photon
at a particular output n. We used 40 inputs and outputs. The vertical axis shows the labels of the outputs, the
horizontal one the logarithm of the probability.
In the following we will show how this interference pattern is modified by different forms of randomness.
III. RANDOM 2-D NETWORK
We consider first a two-dimensional quantum network with randomness. This corresponds to the total
transfer matrix
W (M ) = U1D1U2D2...UM , (5)
4


 where Ui, Di are all different. The randomness enters the motif stuctures either via the individual
quantum components A and B, or by having an extra random phase shift matrix between the matrices
containing the N components A and B. For optical systems, the first case would correspond to having
fluctuations in the transmittivities of the beam splitters, the latter to random phase shifts occuring in the
optical paths. Here we have analyzed phase randomness. The phases between all the connecting points
change randomly within the 〈0, 2π〉 interval.
We study the behaviour of the network by following the propagation of an input state initially located
at the input port which is at the center of the network. To illustrate our results we fixed the number of
network input ports to 40 which corresponds to 20 elements in one layer. As the initial state we consider
a single photon guided into the network from the 20-th input port
|ψ(0)〉 = |0〉1...|0〉19|1〉20...|0〉40. (6)
The spread of a photon given by this initial state in the network is shown in Fig.3
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
U DUD
1 12 2
10 20 30 40
n
-11
-9
-7
-5
-3
10 20 30 40
n
-7
-5
-3
-1
ln P
M=4
10 20 30 40
n
-10
-8
-6
-4
-2
ln P
M=7
10 20 30 40
n
-11
-9
-7
-5
-3
ln P
M=10
FIG. 3. The left picture shows the considered network structure. All Ui are random because of random phases
introduced inside each motif structure, in the figure these phases are represented by the dotted arrows connecting
the two columns of the elements A. Additional random phases are introduced in the layers Di between each two
motifs. The output distribution after ten layers is shown on the right. The dots represent the actual output
probabilities, the solid line shows the least square fit. The bottom plot shows the evolution of the distribution
after four, seven and ten layers traversed. Note the change in the logarithmic (vertical) scale.
The plot shows the logarithm of the probability for the photon to appear at the given output (given
5


 by the dots). Three choices for M are shown to illustrate how the distribution changes when the photon
propagates in the network. The largest value of M equals ten; after ten layers the photon hits the border
of the network, then traversing just another motif layer the photon would be recycled back into the
system due to periodic boundary conditions. In calculating the probability we have averaged over 1000
runs. The solid line gives the least square fit to the calculated values to show that the distribution follows
a quadratic dependence.
As shown in Fig.3, the quantum state in this network behaves like a classical distribution, i.e. it spreads
into a broad Gaussian at the outputs. Classical and quantum behaviour in this kind of networks, in the
absence of randomness, is studied in [6–9]. Gaussian outputs were found in the classical case [8] whereas
complicated interference and recurrence phenomena are typical in the quantum case. Our results show
that introducing randomness acts as decoherence which reduces the quantum behaviour to the classical
one. In section 5 we explain the results further in the light of random matrix theory of localization.
IV. PROPAGATION IN 1-D; A THIN LAYER OF MATERIAL
Next we consider the situation where the transfer matrix of one motif structure of the network has the
form U D, where D is a diagonal matrix with fixed randomness, and the total transfer matrix is simply
W (M ) = (U D)M . (7)
Physically this corresponds to quantum propagation in one dimension, or for example a thin layer of
material inside a cavity through which light makes several passages. The situation is illustrated in Fig.4
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
U DUD
10 20 30 40
n
-12
-10
-8
-6
-4
-2
0
6


 10 20 30 40
n
-10
-8
-6
-4
-2
ln P
M=15
10 20 30 40
n
-6
-4
-2
0
ln P
M=80
10 20 30 40
n
-12
-10
-8
-6
-4
-2
0
ln P
M=10
10 20 30 40
n
-8
-6
-4
-2
0
ln P
M=40
10 20 30 40
n
-7
-5
-3
-1
ln P
M=5
10 20 30 40
n
-9
-7
-5
-3
-1
ln P
M=20
FIG. 4. The evolution of the output probability distribution for a network configuration formed by repeating a
fixed random motif. The top right plot shows the distribution after 10 traversed motifs (dots), compared to the
corresponding least square fit. The evolution for different numbers of motifs is given by the three lower pairs of
plots. They are for M = 5, 10, M = 15, 20 and M = 40, 80.
7


 We consider the behaviour of the same input as given in the previous section. Fig.4 shows that
the distribution becomes exponentialy peaked at the input position 20. To see the emergence of this
exponential localization we present the evolution of the initial photon distribution in dependence on the
number of motifs traversed (M ).
We have found that the complicated interference pattern typical for the ideal network turns gradually
into quantum localization when the amount of randomness is increased. This is demonstrated in Fig.5.
10 20 30 40
n
− 12
− 10
−8
−6
−4
−2
0
ln P
<0,π/4>
10 20 30 40
n
− 12
− 10
−8
−6
−4
−2
0
ln P
<0,2π>
10 20 30 40
n
− 12
− 10
−8
−6
−4
−2
0
ln P
<0,π/8>
10 20 30 40
n
− 12
− 10
−8
−6
−4
−2
0
ln P
<0,π>
10 20 30 40
n
− 12
− 10
−8
−6
−4
−2
0
ln P
<0,π/16>
10 20 30 40
n
− 12
− 10
−8
−6
−4
−2
0
ln P
<0,π/2>
8


 FIG. 5. The emergence of localization when the amount of randomness in the network is increased. The
number of motifs is M = 10. The interval of random phases changes from top to bottom and left to right as
〈0, π/16〉, 〈0, π/8〉, 〈0, π/4〉, 〈0, π/2〉, 〈0, π〉, 〈0, 2π〉. The upper left picture shows the almost unperturbed interfer
ence pattern appearing for very weak randomness, the lower right picture the localized distribution in the case of
strong randomness.
We compare the distributions at M = 10 for weak and strong randomness. The strength of randomness
is controlled by the extend to which the phases in the random diagonal matrices can change, for instance
for weak randomness only within the interval 〈0, π/16〉 and for moderate randomness the interval would be
larger 〈0, π/4〉. The main result is that we observe exponential localization for strong enough randomness.
This remarkable quantum feature will be explained in section 5 by making a connection to the standard
theory of Anderson and dynamical localization.
A. Intermediate case: extra noise in 1-D propagation or semi-random 2-D network
As an intermediate case we consider a network with the transfer matrix
W (M ) = U DD1U DD2U DD3..., (8)
where Di are random and different from each other. The matrix D is also random. Note that with all
Di = 1, W (M ) would be the same as in the previous section, that is, expected to lead to localization. This
intermediate case models a network with phase fluctuations inbetween exactly similar motif structures.
Examples of this are an optical network where the nearest neighbour coupling could be essentially perfect
but the path lengths inbetween two nearest neighbour coupling layers fluctuate, or fluctuating cavity
length in the 1-D case of a layer of material in a cavity. In modelling 1-D propagation, this is also a test
of numerical stability of the localization phenomenon when very small extra randomness is introduced.
We now fix the amount of randomness in the matrix D that appears repeatedly in W (M ) (phases chosen
between 〈0, 2π〉), and vary the amount of randomness in Di. We observe that for weak randomness in
Di (phases chosen between 〈0, 0.1π〉), the localization is preserved (note that in this case we probably
have approximately the situation W ∼ (U D)M ). For strong randomness (phases chosen between 〈0, 2π〉)
Gaussian diffusion is observed. This transition from localization into diffusion is illustrated in Fig.6.
10 20 30 40
n
-12
-----108642
ln P
M=10
10 20 30 40
n
-----1864200
ln P
M=10
10 20 30 40
n
-10
-8
-6
-4
-2
ln P
M=10
9


 10 20 30 40
n
-8
-6
-4
-2
ln P
M=20
10 20 30 40
n
-6
-4
-2
ln P
M=20
10 20 30 40
n
-6
-4
-2
ln P
M=20
FIG. 6. The transition from localization into diffusion. The number of traversed motifs is M = 10 (top) and
M = 20 (bottom). The left column represents weak extra randomization (interval of the Di phases only 〈0, 0.1π〉).
The middle is an intermediate regime with phases varying 〈0, 0.1π〉. The right column was calculated for phases
randomly chosen from the interval 〈0, 2π〉. In this case no localization is observed.
V. LOCALIZATION — HAMILTONIAN VERSUS TRANSFER MATRIX APPROACH
The theory of Anderson and dynamical localization tells that exponential localization of the system
eigenvectors, and consequently, of quantum wave packets, occurs when the system Hamiltonian is a
random band-diagonal matrix [12]. Band-diagonality means that only a few neighbouring sites (thinking
in terms of a lattice) are coupled — in the Lloyd model [12], which is the simplest model showing
localization, only the nearest neighbours are connected. Randomness usually means that the energies
of the sites, that is, the diagonal terms of the Hamiltonian, are randomly chosen according to a certain
distribution. But randomness can equally well appear in the off-diagonal couplings.
We describe the network of interest by a transfer matrix rather than a Hamiltonian. Connection
between these two is non-trivial to obtain for large networks, c.f [10]. But some overall characteristics are
easy to sketch. One motif structure of our network clearly couples nearest neighbours, which corresponds
to a Hamiltonian Hmotif with only nearest neighbour coupling. In the case of 1-D propagation, or a thin
layer of material in a cavity, the total transfer matrix is
W (M ) = U M = eiHmotif M . (9)
The network size M can be interpreted as time, and the Hamiltonian of the system is the one describing
one motif structure: random and band diagonal. Therefore it is in accordance with the theory of localiza
tion to observe an exponentially localized distribution at the output. The case with overall randomness
in a 2-D network is completely different. The total transfer matrix
W (M ) = U1D1U2D2...UM (10)
can no longer be expressed as an M th power of a certain band-diagonal Hamiltonian. By diagonalizing
W (M ) one can obtain the corresponding Hamiltonian, but it is clear that it will not any more be band
diagonal, but instead couples M neighbours. For large M , the Hamiltonian approaches a full random
matrix. It is known that for full random matrices there is no localization [12]. Instead, we observe
classical-type diffusion.
10


 VI. CONCLUSIONS
We have considered randomness and localization in a specific quantum network which is character
ized by nearest-neighbour structure and has a relation to models of statistical mechanics with nearest
neighbour interaction. The physical systems that can be modelled by such a network are for instance
beam splitter networks [18], micro- and nanostructures and networks of intersecting energy levels [9,19].
We showed that in a 2-D network with overall randomness, the quantum behaviour was reduced to the
classical one. In contrast, in 1-D propagation, or a system like a layer of material in a cavity, we ob
serve exponential localization. An intermediate case was showing a smooth transition between these two
completely different behaviours.
We relate our findings to the standard theory of localization. Our discussion emphasises the new
features which arise when the systems of interest are described by transfer matrices rather than Hamil
tonians. This would be the natural approach in case of engineered quantum networks.
Acknowledgements
P.T. acknowledges the support by the Academy of Finland (projects 42588, 47140 and 48845 and
Research Centre for Computational Science and Engineering, project 44892, Finnish Centre of Excel
lence Programme 2000-2005). The financial support by the Alexander von Humboldt foundation, MSM
210000018 (Czech Republic), GACR 202/01/0318 and EU IST-1999-13021 for I.J. is greatefully acknowl
edged.
[1] J. Denschlag, D. Cassettari, and J. Schmiedmayer, Phys. Rev. Lett. 82, 2014 (1999); R. Folman, P. Kru ̈ger,
D. Cassettari, B. Hessmo, T. Maier, and J. Schmiedmayer, Phys. Rev. Lett. 84, 4749 (2000).
[2] D. Kielpinki, V. Meyer, M.A. Rowe, C.A. Sackett, W.M. Itano, C. Monroe, and D.J. Wineland, Science 291,
1013 (2001).
[3] G. Mahler and V. A. Weberruß, Quantum networks, Dynamics of open nanostructures, (Springer-Verlag,
Berlin, 1995).
[4] P. T ̈orma ̈, Phys. Rev. Lett. 81, 2185 (1998).
[5] B. Kraus and P. T ̈orma ̈, in Quantum Communication, Computing and Measurement 2, eds. P. Kumar, G.
M. D’Ariano, and O. Hirota (Kluwer Academic/Plenum Publishers, New York, 2000).
[6] P. T ̈orma ̈ and I. Jex, J. Opt. B: Quantum Semiclass. Opt. 1, 8 (1999).
[7] D. Bouwmeester, I. Marzoli, G. Karman, W.P. Schleich, and J.P. Woerdman, Phys. Rev. A 61, 013410 (2000);
see also D. Bouwmeester, Quantum mechanics and classical optics, PhD thesis, Leiden 1996.
[8] D.A. Harmin, Phys. Rev. A 56, 232 (1997).
[9] D.A. Harmin and P.N. Price, Phys. Rev. A 49, 1933 (1994); Yu.N. Demkov, P.B. Kurasov, and V.N. Ostro
11


 vsky, J. Phys. A: Math. Gen. 28, 4361 (1995); V.N. Ostrovsky and H. Nakamura, Phys. Rev. A 58, 4293
(1998); Yu.N. Demkov and V.N. Ostrovsky, Phys. Rev. A 61, 032705 (2000);
[10] P. T ̈orma ̈ and I. Jex, J. Mod. Opt. 47, 1 (2000).
[11] P.W. Anderson, Phys. Rev. 109, 1492 (1958).
[12] F. Haake, Quantum Signatures of Chaos (Springer-Verlag, Berlin, 1992).
[13] Quantum Chaos, eds. G. Casati and B. Chirikov (Cambridge University Press, Cambridge, 1995).
[14] M.V. Berry and S. Klein, Eur. J.Phys. 18, 222 (1997); M. Born and E. Wolf, Principles of Optics (Pergamon,
London, 1959).
[15] See e.g. T. Jonckheere, C.A. Mu ̈ller, R. Kaiser, C. Miniatura, and D. Delande, Phys. Rev. Lett. 85, 4269
(2000) and references therein.
[16] W.K. Wootters, quant-ph/0006105, K.M. O’Connor and W.K. Wootters, quant-ph/0009041.
[17] H.J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).
[18] A. Zeilinger, H.J. Bernstein, D.M. Greenberger, M.A. Horne, and M. Zukowski, Quantum Control and Mea
surement (North Holland) 1993; A. Zeilinger, M. Zukowski, M.A. Horne, H.J. Bernstein, and D.M. Green
berger, in Fundamental Aspects of Quantum Theory, eds. J. Anandan and J.L. Safko, (World Scientific,
Singapore, 1994).
[19] Rydberg States of Atoms and Molecules, eds. by R. F. Stebbing and F. B. Dunning (Cambridge University
Press, 1993).
12
