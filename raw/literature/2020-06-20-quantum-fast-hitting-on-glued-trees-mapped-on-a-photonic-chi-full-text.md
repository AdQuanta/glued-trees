# Quantum fast hitting on glued trees mapped on a photonic chip - Full Text

> Source: https://opg.optica.org/abstract.cfm?URI=optica-7-6-613
> Collected: 2026-09-20
> Published: 2020-06-20
> Zotero parent key: ISSP8HGC
> Evidence: Zotero indexed PDF text

Research Article Vol. 7, No. 6 / June 2020 / Optica 613
Quantum fast hitting on glued trees mapped on a photonic chip
Zi-Yu Shi,1,2 Hao Tang,1,2 Zhen Feng,1,2 Yao Wang,1,3 Zhan-Ming Li,1,2 Jun Gao,1,3 Yi-Jun Chang,1,2 Tian-Yu Wang,1,2 Jian-Peng Dou,1,2 Zhe-Yong Zhang,1,2 Zhi-Qiang Jiao,1,2 Wen-Hao Zhou,1,2 AND Xian-Min Jin1,3,*
1Center for Integrated Quantum Information Technologies (IQIT), School of Physics and Astronomy and State Key Laboratory of Advanced Optical Communication Systems and Networks, Shanghai Jiao Tong University, Shanghai 200240, China 2CAS Center for Excellence and Synergetic Innovation Center in Quantum Information and Quantum Physics, University of Science and Technology of China, Hefei, Anhui 230026, China 3Shenzhen Institute for Quantum Science and Engineering and Department of Physics, Southern University of Science and Technology, Shenzhen 518055, China *Corresponding author: xianmin.jin@sjtu.edu.cn
Received 17 January 2020; revised 28 April 2020; accepted 30 April 2020 (Doc. ID 388451); published 27 May 2020
Quantum walks on graphs play an important role in the field of quantum algorithms. Fast hitting is one of the properties that quantum walk algorithms can utilize to outperform classical random walk algorithms. Fast hitting refers to a particle starting from the entrance node on a graph and trying to hit the exit node quickly. Especially, continuous-time quantum walks on random glued binary trees have been investigated in theories extensively for their exponentially faster hitting speed over classical random walks. Here, using heralded single photons to represent quantum walkers and laserwritten waveguide arrays to simulate the theoretical graph, we are able to demonstrate the hitting efficiency of quantum walks with tree depth as high as 16 layers for the first time. Furthermore, we expand the graph’s branching rate from 2 to 5, revealing that quantum walks can exhibit more superiority over classical random walks as the branching rate increases. Our results may shed light on the physical implementation of quantum walk algorithms as well as quantum computation and quantum simulation. © 2020 Optical Society of America under the terms of the OSA Open Access Publishing Agreement
https://doi.org/10.1364/OPTICA.388451
1. INTRODUCTION
Due to unique features like superposition and entanglement, introducing quantum mechanical effects into classical algorithms has shown great speed advantage [1–8]. Classical random walks (CRWs) on graphs have become a powerful tool for designing classical algorithms. As its counterpart in quantum field, quantum walks [9] (QWs) also find wide applications in not only quantum algorithms [10–16] but also quantum computation [17,18] and quantum simulation [19–22]. Fast hitting [23–25] is one of the properties [26,27] of QWs on graphs that quantum algorithms can take advantage of to demonstrate remarkable quantum speedup, which focuses on the time that a particle needs to reach the exit node as a function of the size of a graph. On random glued binary trees, using QWs to traverse is exponentially faster than not only CRWs but also any classical algorithms people can come up with [25]. This structure originates from the regular glued binary trees [28], i.e., two identical binary trees glued with each other at the end regularly. On random glued binary trees, each end of the left tree has two branches that are randomly glued to two different ends of the right one, and vice versa [Fig. 1(a)]. The left root is the entrance node, and the right root is
the exit node. The size of the whole graph is usually described by the depth n of one of its two binary trees. The probability of a particle hitting the exit node is called hitting efficiency. The hitting efficiency of CRW is less than 2−n [28]. Due to the unitarity, the hitting efficiency of QWs always changes with evolving time [28], and the first peak occurs in O(n) time and is polynomial with n, meaning a QW can almost certainly hit the exit in polynomial time [25,29]. Furthermore, each node on the graph (including the glued part) can be extended to B branches rather than just two branches, exhibiting higher complexity [Fig. 1(b)] [29]. Unfortunately, mapping the full random glued trees into a physical system is impossible under existing studies, as the node number grows exponentially with n. There has yet been no experimental demonstration of QW’s hitting efficiency on this graph, not to mention the expansion to higher branching rates. Even exploiting a deformation [30] or simplified structure [31] is already of great interest. On the other hand, on account of the coherent superposition of quantum particles as well as the symmetrical shape of these glued trees, the analysis of the QW traversing the graph can be reduced to only being concerned with the graph’s column positions (see
2334-2536/20/060613-06 Journal © 2020 Optical Society of America


 Research Article Vol. 7, No. 6 / June 2020 / Optica 614
(a)
(b)
n=2
n=3
n=4
B=3
B=2
B=4 entrance exit
branching rate B, tree depth n
entrance exit
B B BB B B B
(c)
inject single photons
hitting efficiency
Fig. 1. Schematic diagram of random glued trees. (a), Random glued trees with an increasing n (in row) and B (in column). (b), Generalized random glued trees and their one-dimensional equivalence for QWs. The hopping rate between any adjacent nodes of the two-dimensional graph is γ , while on the one-dimensional chain, the hopping rate is
√
Bγ except for the two adjacent nodes at the center, which becomes Bγ . (c), Experimental implementation of the mapped one-dimensional chain on a photonic chip using femtosecond laser direct writing technique. The cross section of the waveguide array is consistent with the theoretical one-dimensional chain, and the longitudinal direction of the waveguide corresponds to the evolving time. Since the hopping rate of the two adjacent waveguides at the center is greater than others, the spacing between the two waveguides is reduced accordingly.
Supplement 1). The complex two-dimensional graph can be simplified to a one-dimensional chain with nonuniform hopping rates [25] [Fig. 1(b)]. Nonetheless, the physical implementation is still a big challenge compared with those reported structures [20,32–37], for the experimental results are highly sensitive to the coupling strength between waveguides (see Supplement 1 for the sensitivity analysis). Fortunately, after plenty of time and effort, we have conquered the difficulties. For the first time, we not only experimentally investigate the variation of QW’s optimal hitting efficiency with n ranging from 2 to 16, which demonstrates that a quantum walker can hit the exit in polynomial time, but also its variation with B going from 2 to 5, revealing that the branching rate can also contribute to the speed advantage of QWs. Our work will inspire the experimental realization of fast hitting as well as the other properties of QWs [10,11,26,27] in more scenarios, further facilitating the physical realization of QW algorithms.
2. METHODS
The row of Fig. 1(a) shows the changing of tree depth, while the column exhibits the variation of the branching rate. As shown in Fig. 1(c), in borosilicate chip substrate, we use femtosecond laser direct writing technique [38–42] to fabricate an array of waveguides, the cross section of which is a strict mapping of the theoretical one-dimensional chain [Fig. 1(b)]. Each waveguide represents a node in the theoretical graph, and the longitudinal direction of the waveguides is for the evolving process in time. As evolving length z of photons is proportional to evolving time
t for z = vt, in which v is the propagation speed of photons in waveguides, we use length z to replace time t in the following description. We prepare and inject single photons into the entrance waveguide, and observe the spatial photon number distribution when the waveguide lengths change. When propagating along the waveguides, a single photon will be coupled evanescently to the other waveguides [33,43]. It is worth noting that, since the coupling coefficient decreases exponentially with waveguide spacing, we only consider the coupling effects between the nearest waveguides [33,44]. The evolving process of a continuous-time QW can be described by the wave function of photons according to
|9(z)〉 = e −i Hz |9(0)〉 , (1)
where |9(0)〉 is the initial state and H is the Hamiltonian. The equation can be calculated by matrix exponential methods [45]. The Hamiltonian of photons propagating through a waveguide system can be described by [20,32]
H=
N
∑
i
βi a †
i ai +
N
∑
i
6= j
Ci,j a†
i a j , (2)
where a †
i , ai are the creation and annihilation operator for wave
guide i. βi = β is the propagation constant. Ci, j is the coupling coefficient between waveguide i and j , which is mainly determined by waveguide spacing. For random glued trees with depth n, its one-dimensional equivalence has 2n + 2 nodes, and the probabilities of a walker


 Research Article Vol. 7, No. 6 / June 2020 / Optica 615
n=4
n=6
n=8
n=10
n=12
n=14
n=16
(a) (b)
Hitting Efficiency
Evolving Length(mm)
Fig. 2. Spatial photon number distributions and hitting efficiencies for trees at B = 2. (a), Variation of hitting efficiency with evolving length with n = 2. Several pictures of spatial photon number distributions for samples of different evolving lengths are also shown as insets. The injecting waveguide is marked by a white circle, and corresponding hitting efficiencies of CRWs on random glued trees are also plotted. (b), Spatial photon number distributions that show optimal hitting efficiencies at different n.
moving right or left (hopping rate) on the chain are the same on all the nodes except the two nearest nodes at the center. As Fig. 1(c) shows, on the chain, the hopping rate, which corresponds to the coupling coefficient in experiments, of a quantum walker between the two nearest central nodes is
√
B times of that between the other nearest nodes, where γ is the hopping rate on the trees. The value γ is does not affect the optimal hitting efficiency, but the ratio of the hopping rate at the center to that at the noncenter position, i.e.,
√
B, on the chain does; therefore, precisely mapping this ratio to waveguide arrays is essential to simulate glued trees with different branching rates. If j represents column positions, then the nonzero elements of the Hamiltonian of the one-dimensional chain are [29]
〈 j | H | j + 1〉 =
{√
Bγ 0 ≤ j < n, n < j ≤ 2n
Bγ j = n . (3)
The rest of the nonzero elements can be deduced by the Hermiticity. The probability distribution of a CRW is uniform and stationary as long as the evolving time is long enough [11], whereas the probability distribution of a continuous-time QW is always changing [29,30,46]. Several peaks of hitting efficiency, which we term as optimal hitting efficiency, will appear as the evolving length of photons increases. Here, we only study the first peak of the hitting efficiency and calculate the corresponding evolving length where such first peak occurs. We will term such evolving length as optimal evolving length in the following description. On the basis of coupled mode theory [44], every time before we fabricate experimental chips, we will fabricate C -measurement chips to calibrate the function of coupling coefficients with waveguide spacings in advance. Hence, we can determine the waveguide spacings of the experimental chips according to the coupling coefficients used in the theoretical calculation (see Supplement 1 for the fabrication details). Each waveguide is uniform, and the distance between any two nearest waveguides is identical except the two waveguides at the center. With these waveguide arrays in hand, we study the transporting property of QWs by injecting vertically polarized single photons with a wavelength of 810 nm into the entrance waveguide and monitoring the intensity pattern exiting the photonic chip with an intensified charge-coupled device (ICCD) (see Supplement 1 for details on single-photon imaging). The experimental hitting efficiency is obtained by calculating the
ratio of the intensity in the exit waveguide to the total intensity (see Supplement 1 for details on data processing).
3. RESULTS
For trees with n ranging from 2 to 16, and B ranging from 2 to 5, we first work out the variation of hitting efficiency against evolving length from the experimental patterns. Figure 2(a) exhibits the results of a two-layer tree at a branching rate of 2. The experimental optimal hitting efficiency is 0.76, and corresponding evolving length is 15.5 mm, agreeing very well with theoretical calculation, which suggests an optimal value of 0.82 at 15 mm. However, the theoretical hitting efficiency of CRW [25] at 15 mm is only 0.044, which is lower than QW by more than 1 order. Some QW spatial photon number distributions are also added into Fig. 2(a) to visually show the change of hitting efficiency. The left-most light spot in each subpicture corresponds to the entrance waveguide, which is marked by a white circle, and the right-most light spot corresponds to the exit waveguide. It can be seen that variation of the ratio of photons reaching the exit waveguide in the spatial photon number distributions is consistent with our calculated experimental curve. Then, applying the method of finding experimental optimal hitting efficiency as shown in Fig. 2(a), we investigate the change of optimal hitting efficiency with n. Figure 2(b) shows spatial photon number distribution of optimal hitting efficiency with n going from 2 to 16 at B = 2. It is obvious that, despite the number of waveguides increasing with n, most of the photons gather at the exit waveguide rather than the other waveguides, which represents the positions of the other columns of the tree. All spatial photon number distributions that show optimal hitting efficiency for graphs of different sizes as well as the linearly increasing optimal evolving lengths are presented in supplementary material (see Supplement 1, Figs. S4–S7). The optimal hitting efficiencies calculated from theoretical models and experimental evolution results are plotted in Fig. 3(a), and the ultimate steady hitting efficiency of CRW when evolving length is long enough is added in Fig. 3(b) as a comparison. We emphasize that this way of reducing to a one-dimensional chain is derived for QWs (as shown in Supplement 1), but is not suitable for CRWs; therefore, all theoretical results about CRWs are based on random glued trees. Figure 3(a) exhibits that, for each B, QW’s optimal hitting efficiency decays polynomially with the increase of n. In contrast, for CRW, when evolving length is infinitely long,


 Research Article Vol. 7, No. 6 / June 2020 / Optica 616
Optimal Hitting Efficiency
Tree Depth Tree Depth
Optimal Hitting Efficiency
(a) (b)
B=2
B=3
B=5
B=5
B=4
B=2
B=3 B=5
B=4
Fig. 3. Experimental optimal hitting efficiencies for different branching rates. (a), Variation of optimal hitting efficiencies with n for B = 2, 3, 4, 5, respectively. As B increases, the optimal hitting efficiencies decrease slightly. (b), Comparison between CRWs and QWs in a half logarithmic coordinate. The ultimate steady hitting efficiencies of CRWs on random blued trees decrease exponentially with n, in contrast with the polynomially decreasing trend of QWs. Though data of B = 5 for QWs is the smallest among the four groups, it still outperforms CRWs.
the hitting efficiency will increase monotonously to an asymptotic value, which is the inverse of the number of nodes on the trees [25], and the scaling can be expressed as PCRW ∼ B−n, meaning its optimal hitting efficiency decays exponentially with n [29] [Fig. 3(b)]. It can be seen from Fig. 3(b) that though the hitting efficiency of QW at B = 5 is the smallest among the four kinds of branches, it is still exponentially higher than CRW. Finally, we investigate the variation of optimal hitting efficiency with B. As B increases, the complexity of graphs rises dramatically, and the increasing branches at each node provide ever more challenges for CRW particles to choose from. On the other hand, a quantum walker is able to explore the landscape it traverses with superposition, and hence has even more evident superiority over CRW at a higher branching rate. From Fig. 3(a), the QW’s optimal hitting efficiency for n = 16 at B = 5 is still more than 50% of that at B = 2, while the ratio for the same pair drops to approximately (2/5)16 = 4.29 × 10−7 for CRW [see Fig. 3(b)], as PCRW ∼ B−n. In Fig. 4, we plot the QW’s optimal hitting efficiency (left y axis) and the enhancement ratio over CRW’s optimal hitting efficiency (right y axis) for different branching rates from 2 up to 10. The results all come from four-layer glued trees. Even for the shallow glued tree without pursuing a large tree depth, the enhancement of optimal hitting efficiency by QW over CRW is impressive at a high branching rate. It has been suggested in theory [29] that when B is considerably large, QW’s optimal hitting efficiency scales with B by PQW ∼ 1/B, and then the enhancement ratio would scale as r = PQW/PCRW ∼ Bn−1 for a certain n. We have observed the increasing enhancement ratio for a few branching rates, and provided the first experiment demonstration of random glued trees of high branching rates. The experimental results prove that branching rate can be another useful resource besides the more commonly discussed tree depth, to increase the complexity of random glued trees for strengthening the quantum superiority. The second-order anticorrelation parameters [47] α of the waveguide arrays used in Fig. 4, which tend to be 0 for ideal single photons and 1 for classical coherent light, are shown in Table 1,
Optimal Hitting Efficiency
Branching rate
Enhancement Ratio
Fig. 4. Variation of experimental optimal hitting efficiencies with branching rate for n = 4. Scatter plots correspond to the left y axis, representing optimal hitting efficiencies of QWs in theory and experiment, respectively. Column plots correspond to the right y axis, representing the enhancement rate, i.e., optimal hitting efficiency ratio of the QW against the CRW. The tree depth remains to be 4 when this measurement is taken.
Table 1. Measured α of the Single Photons Existing from the Exit Waveguide for Graphs with B = 2, 3, 4, 5 at n = 4
B 2345 α 0.086 0.114 0.091 0.093 error bar 0.001 0.001 0.001 0.003
exhibiting excellent quality of our single-photon source during the whole transporting process. (See Supplement 1 for details.) We further demonstrate the nonclassical property of our designed hitting process by fabricating waveguide arrays with two input ports for trees at n = 4 and B = 3. As shown in Fig. 5, the idler photons and signal photons, which are generated via the type-II spontaneous parametric downconversion (SPDC) process on PPKTP crystal with an average pumping power of 3.8 mW are injected into the right-most and left-most waveguides, respectively. The waveguide arrays are fabricated at the optimal evolving length;


 Research Article Vol. 7, No. 6 / June 2020 / Optica 617
signal idler
(a) (b)
0.1
1
2
10
100 before chip
after chip
(2) (2) (2) (2) (2) (2)
Fig. 5. Measurement of the cross correlation g (2)
si and autocorrelation
g (2)
ss , g (2)
ii for trees at n = 4 and B = 3. (a), The idler photons and the signal photons are injected into the two ends of the waveguide array, respectively. The waveguide arrays are fabricated at the optimal evolving length; hence, most of the photons from each input waveguide will hit the opposite end at the exiting side of the waveguide array and will be detected by two avalanche photodiodes (APDs), respectively. Cross correlation g (2)
si
is obtained by measuring the coincidence of the two APDs. (b), g (2)
si , g (2)
ss ,
g (2)
ii before the chip and after the chip.
hence, most of the photons from the two input ports will hit the opposite end at the exiting side of the chip and be detected by two avalanche photodiodes (APDs), respectively. The cross correlation
g (2)
si is obtained by measuring the coincidence of the two paths
of photons after the chip. The g s(s2) (g (2)
ii ) is measured by passing the exiting signal (idler) photons through a balanced fiber beam splitter (BS) and measuring the coincidence of the two paths of the output photons, with the idler (signal) photons ignored. For classical fields, the Cauchy–Schwarz inequality,
(g (2)
si )2 ≤ g s(s2) · g (2)
ii , must be satisfied. The g (2)
si and g s(s2) (g (2)
ii )
can be calculated by
g (2)
xy =
Nxy Np
Nx Ny
, (4)
where Nx (Nxy) refers to single (coincidence) detection events and Np refers to the number of trials [47]. For the photon source, the g (2)
si is 149.62 ± 0.42, and the g s(s2) (g (2)
ii ) is 1.89 ± 0.05
(2.03 ± 0.05). For the photons exiting the chip, the g (2)
si is
123.87 ± 0.66, and the g s(s2) (g (2)
ii ) is 2.10 ± 0.15 (1.54 ± 0.10), with the Cauchy–Schwarz inequality violated by 94 standard deviations, demonstrating a nonclassical property of our designed hitting process.
4. CONCLUSIONS
In summary, we demonstrate the fast-hitting property of QWs on random glued trees in a single-photon regime. Harnessing the femtosecond laser direct writing technique, we precisely control the coupling coefficient between waveguides and fabricate waveguide arrays with high tree depths and branching rates. We employ ultra-low-noise single-photon imaging techniques to measure the probability of heralded single photons reaching the exit waveguides. Using single photons instead of classical coherent light, we manage to observe the accumulated process from the individual single photons to the eventual spatial photon number distribution, realizing a true sense of quantum-particle experiment instead of the simulation results by laser beams. Besides, using single photons also
gives a possible direction for the experimental expansion to a bigger Hilbert space, i.e., increasing the number of particles walking on the graph, which classical coherent light cannot achieve. We experimentally demonstrate that the optimal hitting efficiency of a quantum walker hitting the exit only decays polynomially as tree depth increases, which is in contrast with CRW’s exponentially decreasing trend. We further demonstrate that the enhancement ratio of the QW’s optimal hitting efficiency over CRW becomes higher when branching rate increases, suggesting the branching rate as another useful approach besides the tree depth to introduce more evident quantum advantages. In fabricating high-branched glued trees, we manage to precisely set coupling coefficients as
√
Bγ or Bγ using the advanced waveguide writing techniques, without which it is impossible to implement such glued trees on photonic chips. These precise writing techniques can be further utilized for richer explorations of on-chip quantum algorithms and quantum simulation. Another inspiring point from this work is the idea of reducing a complex graph to a simpler equivalence that can be mapped in the physical systems. For many complex graphs such as hypercubes and other high-dimensional structures, this may shed light upon the experimental implementation in a highly feasible way. Further, it would also be interesting to map the structure of high branching rates and tree depths to optimization problems in different fields [24,48], and bring up quantum advantages by these hitting protocols into real-life applications.
Funding. National Key Research and Development Program of China (2019YFA0308700, 2017YFA0303700); National Natural Science Foundation of China (11904229, 11761141014, 61734005, 11690033); Science and Technology Commission of Shanghai Municipality (17JC1400403); Shanghai Municipal Education Commission (2017-01-07-00-02-E00049); China Postdoctoral Science Foundation (2019T120334).
Acknowledgment. The authors thank Andrew Childs and Jian-Wei Pan for helpful discussions. X.-M. J. acknowledges additional support from a Shanghai talent program.
Disclosures. The authors declare no conflicts of interest.
See Supplement 1 for supporting content.
REFERENCES
1. A. Montanaro, “Quantum algorithms: an overview,” NPJ Quantum Inform. 2, 15023 (2016). 2. P. W. Shor, “Algorithms for quantum computation: discrete logarithms and factoring,” in 35th Annual Symposium on Foundations of Computer Science, 1994 Proceedings (IEEE, 1994), pp. 124–134.
3. B. P. Lanyon, T. J. Weinhold, N. K. Langford, M. Barbieri, D. F. James, A. Gilchrist, and A. G. White, “Experimental demonstration of a compiled version of Shor’s algorithm with quantum entanglement,” Phys. Rev. Lett. 99, 250505 (2007). 4. L. K. Grover, “A fast quantum mechanical algorithm for database search,” in Proceedings of the 28th Annual ACM Symposium on Theory of Computing (ACM, 1996), pp. 212–219. 5. L. K. Grover, “Quantum mechanics helps in searching for a needle in a haystack,” Phys. Rev. Lett. 79, 325–328 (1997). 6. J. A. Jones, M. Mosca, and R. H. Hansen, “Implementation of a quantum search algorithm on a quantum computer,” Nature 393, 344–346 (1998). 7. E. Farhi, J. Goldstone, S. Gutmann, J. Lapan, A. Lundgren, and D. Preda, “A quantum adiabatic evolution algorithm applied to random instances of an NP-complete problem,” Science 292, 472–475 (2001).


 Research Article Vol. 7, No. 6 / June 2020 / Optica 618
8. S. Aaronson and Y. Shi, “Quantum lower bounds for the collision and the element distinctness problems,” J. ACM 51, 595–605 (2004). 9. Y. Aharonov, L. Davidovich, and N. Zagury, “Quantum random walks,” Phys. Rev. A 48, 1687–1690 (1993). 10. A. Ambainis, “Quantum walks and their algorithmic applications,” Int. J. Quantum Inform. 1, 507–518 (2003). 11. J. Kempe, “Quantum random walks: an introductory overview,” Contemp. Phys. 44, 307–327 (2003). 12. A. Ambainis, “Quantum walk algorithm for element distinctness,” SIAM J. Comput. 37, 210–239 (2007). 13. B. L. Douglas and J. B. Wang, “A classical approach to the graph isomorphism problem using quantum walks,” J. Phys. A 41, 075303 (2008). 14. A. M. Childs and J. Goldstone, “Spatial search by quantum walk,” Phys. Rev. A 70, 022314 (2004). 15. N. Shenvi, J. Kempe, and K. B. Whaley, “Quantum random-walk search algorithm,” Phys. Rev. A 67, 052307 (2003). 16. A. Tulsi, “Faster quantum-walk algorithm for the two-dimensional spatial search,” Phys. Rev. A 78, 012310 (2008). 17. A. M. Childs, “Universal computation by quantum walk,” Phys. Rev. Lett. 102, 180501 (2009). 18. A. M. Childs, D. Gosset, and Z. Webb, “Universal computation by multiparticle quantum walk,” Science 339, 791–794 (2013). 19. A. Schreiber, A. Gábris, P. P. Rohde, K. Laiho, M. Štefanˇ ák, V. Potocˇ ek, C. Hamilton, I. Jex, and C. Silberhorn, “A 2D quantum walk simulation of two-particle dynamics,” Science 336, 55–58 (2012). 20. A. Peruzzo, M. Lobino, J. C. Matthews, N. Matsuda, A. Politi, K. Poulios, X.-Q. Zhou, Y. Lahini, N. Ismail, K. Wörhoff, and Y. Bromberg, “Quantum walks of correlated photons,” Science 329, 1500–1503 (2010). 21. L. Sansoni, F. Sciarrino, G. Vallone, P. Mataloni, A. Crespi, R. Ramponi, and R. Osellame, “Two-particle bosonic-fermionic quantum walk via integrated photonics,” Phys. Rev. Lett. 108, 010502 (2012). 22. A. Crespi, R. Osellame, R. Ramponi, V. Giovannetti, R. Fazio, L. Sansoni, F. De Nicola, F. Sciarrino, and P. Mataloni, “Anderson localization of entangled photons in an integrated quantum walk,” Nat. Photonics 7, 322–328 (2013). 23. J. Kempe, “Discrete quantum walks hit exponentially faster,” Probability Theory Relat. Fields 133, 215–235 (2005). 24. E. Farhi and S. Gutmann, “Quantum computation and decision trees,” Phys. Rev. A 58, 915–928 (1998). 25. A. M. Childs, R. Cleve, E. Deotto, E. Farhi, S. Gutmann, and D. A. Spielman, “Exponential algorithmic speedup by a quantum walk,” in Proceedings of the 35th Annual ACM Symposium on Theory of Computing (STOC ’03) (ACM, 2003), pp. 59–68. 26. D. Aharonov, A. Ambainis, J. Kempe, and U. Vazirani, “Quantum walks on graphs,” in Proceedings of the 33rd Annual ACM Symposium on Theory of Computing (ACM, 2001), pp. 50–59. 27. C. Moore and A. Russell, “Quantum walks on the hypercube,” in International Workshop on Randomization and Approximation Techniques in Computer Science (Springer, 2002), pp. 164–178.
28. A. M. Childs, E. Farhi, and S. Gutmann, “An example of the difference between quantum and classical random walks,” Quantum Inform. Process. 1, 35–43 (2002). 29. I. Carneiro, M. Loo, X. Xu, M. Girerd, V. Kendon, and P. L. Knight, “Entanglement in coined quantum walks on regular graphs,” New J. Phys. 7, 156 (2005). 30. H. Tang, C. Di Franco, Z.-Y. Shi, T.-S. He, Z. Feng, J. Gao, K. Sun, Z.-M. Li, Z.-Q. Jiao, T.-Y. Wang, and M. S. Kim, “Experimental quantum fast hitting on hexagonal graphs,” Nat. Photonics 12, 754–758 (2018).
31. F. Qi, Q. Ma, Y. Wang, and W. Zheng, “Silicon photonic chips for search on improved-glued-binary-tree based on continuous-time quantum walk,” Proc. SPIE 10029, 100291C (2016). 32. H. B. Perets, Y. Lahini, F. Pozzi, M. Sorel, R. Morandotti, and Y. Silberberg, “Realization of quantum walks with negligible decoherence in waveguide lattices,” Phys. Rev. Lett. 100, 170506 (2008). 33. H. Tang, X.-F. Lin, Z. Feng, J.-Y. Chen, J. Gao, K. Sun, C.-Y. Wang, P.-C. Lai, X.-Y. Xu, Y. Wang, L.-F. Qiao, A.-L. Yang, and X.-M. Jin, “Experimental two-dimensional quantum walk on a photonic chip,” Sci. Adv. 4, eaat3174 (2018). 34. D. N. Biggerstaff, R. Heilmann, A. A. Zecevik, M. Gräfe, M. A. Broome, A. Fedrizzi, S. Nolte, A. Szameit, A. G. White, and I. Kassal, “Enhancing coherent transport in a photonic network using controllable decoherence,” Nat. Commun. 7, 11282 (2016). 35. A. Perez-Leija, R. Keil, A. Kay, H. Moya-Cessa, S. Nolte, L.-C. Kwek, B. M. Rodrguez-Lara, A. Szameit, and D. N. Christodoulides, “Coherent quantum transport in photonic lattices,” Phys. Rev. A 87, 012309 (2013). 36. M. A. Broome, A. Fedrizzi, B. P. Lanyon, I. Kassal, A. Aspuru-Guzik, and A. G. White, “Discrete single-photon quantum walks with tunable decoherence,” Phys. Rev. Lett. 104, 153602 (2010). 37. F. Caruso, A. Crespi, A. G. Ciriolo, F. Sciarrino, and R. Osellame, “Fast escape of a quantum walker from an integrated photonic maze,” Nat. Commun. 7, 11682 (2016). 38. K. M. Davis, K. Miura, N. Sugimoto, and K. Hirao, “Writing waveguides in glass with a femtosecond laser,” Opt. Lett. 21, 1729–1731 (1996). 39. R. R. Thomson, T. A. Birks, S. Leon-Saval, A. K. Kar, and J. BlandHawthorn, “Ultrafast laser inscription of an integrated photonic lantern,” Opt. Express 19, 5698–5705 (2011). 40. A. Crespi, R. Osellame, R. Ramponi, D. J. Brod, E. F. Galvao, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, “Integrated multimode interferometers with arbitrary designs for photonic boson sampling,” Nat. Photonics 7, 545–549 (2013). 41. Z. Chaboyer, T. Meany, L. Helt, M. J. Withford, and M. Steel, “Tunable quantum interference in a 3D integrated circuit,” Sci. Rep. 5, 9601 (2015). 42. Z. Feng, B.-H. Wu, Y.-X. Zhao, J. Gao, L.-F. Qiao, A.-L. Yang, X.-F. Lin, and X.-M. Jin, “Invisibility cloak printed on a photonic chip,” Sci. Rep. 6, 28527 (2016). 43. J. Gao, L.-F. Qiao, X.-F. Lin, Z.-Q. Jiao, Z. Feng, Z. Zhou, Z.-W. Gao, X.-Y. Xu, Y. Chen, H. Tang, and X.-M. Jin, “Non-classical photon correlation in a two-dimensional photonic lattice,” Opt. Express 24, 12607–12616 (2016). 44. A. Szameit, F. Dreisow, T. Pertsch, S. Nolte, and A. Tünnermann, “Control of directional evanescent coupling in fs laser written waveguides,” Opt. Express 15, 1579–1587 (2007). 45. J. A. Izaac and J. B. Wang, “pyCTQW: a continuous-time quantum walk simulator on distributed memory computers,” Comput. Phys. Commun. 186, 81–92 (2015). 46. E. Sánchez-Burillo, J. Duch, J. Gómez-Gardenes, and D. Zueco, “Quantum navigation and ranking in complex networks,” Sci. Rep. 2, 605 (2012). 47. J. B. Spring, P. S. Salter, B. J. Metcalf, P. C. Humphreys, M. Moore, N. Thomas-Peter, M. Barbieri, X.-M. Jin, N. K. Langford, W. S. Kolthammer, and M. J. Booth, “On-chip low loss heralded source of pure single photons,” Opt. Express 21, 13522–13532 (2013). 48. N. Bao, V. P. Su, and M. Usatyuk, “Wormhole traversability via quantum random walks,” arXiv:1906.01672 (2019).
