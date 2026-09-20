# Realization of a Decoherence-Free Subspace Using Multiple Quantum Coherences - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevLett.95.020501
> Collected: 2026-09-20
> Published: 2005-07-07
> Zotero parent key: XX38ANGP
> Evidence: Zotero indexed PDF text

arXiv:quant-ph/0410140v3 25 Oct 2004
Realization of decoherence-free subspace using Multiple-Quantum coherences
Daxiu Wei,∗ Jun Luo, Xianping Sun, Xizhi Zeng, Mingsheng Zhan, and Maili Liu† State Key Laboratory of Magnetic Resonance and Atomic and Molecular Physics, Wuhan Institute of Physics and Mathematics, Chinese Academy of Sciences, Wuhan 430071, P. R. China
This letter presents a two-dimensional nuclear magnetic resonance(NMR) approach for constructing a two-logical-qubit decoherence-free subspace (DFS) based on the fact that the three protons in a CH3 spin system can not be resolved in one-dimension NMR spectroscopy, but to a certain extent, can be distinguished by two-dimensional multiple-quantum NMR. We used four noisy physical nuclear spins, including three protons and one carbon in the CH3 spin system, to generate two decoherence-free logical qubits. It made full use of the unaddressed spins which could not be used in one-dimensional spectrum. Furthermore, we have experimentally demonstrated such an approach. Our experimental results have shown that our DFS can protect against far more types of decoherence than the one composed of four noisy physical qubits all with different chemical shifts. More importantly, this idea may provide new insights into extending qubit systems in the sense that it effectively utilizes the magnetically equivalent nuclei.
PACS numbers: 03.67.Lx. 76.60.-k. 75.10.Jm
Quantum computers could, in theory, be superior to classical computers when performing a number of computational tasks, such as factorizing a large number [1], searching unsorted database [2] and, especially, simulating quantum systems themselves [3]. Among various techniques, liquid nuclear magnetic resonance (NMR) approach is, currently, the most realistic tool [4]. If the chemical shift of a nuclear spin is well resolved and can be controlled by selective radiofrequency (RF) pulses without disturbing the other spins, the spin can be used as a qubit for quantum computing. Although NMR quantum computing has made the greatest progress towards QIP [4], it is very difficult to scale up current NMR quantum computers to large sizes (more than 10 qubits)[5]. There are many obstacles that limit wide applications of NMR in quantum computation. Firstly, in addition to the low signal-to-noise ratio (SNR) in NMR experiments, the SNR decreases exponentially with increasing of qubit numbers. Secondly, there are only few types of nuclear spins which might be used as qubits, such as 1H, 13C, 15N, 19F, and 31P etc. Thirdly, because of limitations in the number of the receive channels and the transmit channels in the commercial NMR spectrometers, one always had to employ homonuclear systems and selectively control each of the spins when implementing multi-qubit quantum computing. Finally, frequency dispersion limits the number of usable homonuclear spins or qubits. In the case of proton NMR at 500 MHz, the chemical shift range is generally less than 5000 Hz. This small spectral window restricts the number of qubits in a homonuclear system. In addition, it is extremely hard to select or design a special molecule whose protons all have well resolved chemical shifts and are coupled to each other. It is thus a great challenge for NMR spectroscopists to utilize all of the available spins in the real molecule. It has been noticed that magnetically equivalent spins, such as the three protons in a methyl, are used as a single physical qubit. One can wonder whether it is possible to use the equivalent spins as individual qubits. In this context, we will describe a two-dimensional (2D) NMR technique to implement logical qubit by making full use of the three protons in the methyl. The new concept of using 2D NMR to perform quantum computing was first proposed by Ma ́di and Ernst et al. in 1998[6]. The quantum logical gates and Deutsch-Jozsa quantum algorithm were also experimentally realized in 2D NMR with the help of spin- and transition- selective pulses[7, 8]. In these experiments, since single quantum transitions were used in both dimensions, the equivalent protons are indistinguishable and can only be utilized as one physical qubit. On the contrary, using 2D multiple-quantum NMR J-resolved spectroscopy (MQ-JRES) of the spins in alanine[9], we observed that the methyl has four resolved multi-quantum (MQ) coherences which have no interchange during the free evolution time. The 2D MQ-JRES spectrum can be explained in detail by a SI3-M spin system (for the 13CH3-12CH in alanine). After four spins are excited to their highest quantum state, the SI3 spin system will include four coherences (one quadruple quantum, two double quanta, and one zero quantum)[9]. Moreover, different multi-quantum coherences are modulated differently by their coupling constants to the remote spin M, and is distinguished by projecting the 2D multi-quantum onto the F1 dimension. In this case, the three protons in the methyl play the roles of three physical qubits. The following question arises: “can three physical qubits composed of three protons in a methyl be used to implement the 2D NMR quantum computing(QC)?” This topic will be discussed
∗Electronic address: dxwei@wipm.ac.cn †Electronic address: ml.liu@wipm.ac.cn


 2
and solved in the following context. Here, we will describe how to use three protons and a carbon in a methyl as four physical qubits to produce four multiple quantum coherences, and then utilize these multiple quantum coherences as logical qubits to construct an operator subspace DFS in a Liouville space[4, 6, 10] by virtue of the 2D multi-quantum J-resolved NMR spectrum (MQ-JRES). We also present experimental results in demonstrating this novel idea. There are two kinds of passive error control codes for counteracting the decoherence. One is decoherence-free subspace (DFS) [11, 12, 13] and the other is noiseless subsystems (NSs)[14, 15, 16, 17]. They had been widely studied in both theoretically and experimentally [11, 12, 13, 14, 15, 16, 18, 19]. Recently, the two-logic-qubit DFS composed of four physical qubits were demonstrated in NMR quantum computing[18]. All states in DFS are immune to the error operation Ed with the form Ed = αd,0E1E2E3E4 + αd,1X1X2E3E4 + αd,2E1E2X3X4 + αd,3X1X2X3X4, where E is the unit operator and X i (i=1, 2, 3, and 4) are operators which make the physical qubits flipped. Just as the other methods to avoid the decoherence problem, the construction of the DFS always needs at least two physical qubits to produce one logical qubit. In order to express a DFS as state vectors or density matrices, it is instructive to discuss the connection between logical-qubit state vectors and density matrices. For simplicity, we first consider a DFS with two physical qubits[20], which protects against the error set {E1E2, X1X2, Z1Z2} in the form of
|0〉0L = √12 (|01〉 + |10〉,
|1〉0L = √12 (|01〉 − |10〉. (1)
The above states can also be rewritten in the form of density operators and the state |0〉0L corresponds to the following expression,
ρL
(L0) = |0〉0L0L〈0|
=1
2(1
2 − 2Iz1Iz2 + 2Ix1Ix2 + 2Iy1Iy2). (2)
On the other hand, an experimental density matrix (ρ) could be separated into different orders p ( such as zero-, single-, two-, or quadruple-quantum coherence and so on)[21],
ρ=
+2l
∑
p=−2l
ρp,
where l is the maximum total spin quantum number. For example, we can decompose Eq. 2 into the superposition of zero quantum and double quantum,
ρL
(L0) = ρ0 + ρ2 + ρ−2 = 1
4 − Iz1Iz2
} {{ } ρ0
+ Ix1Ix2 + Iy1Iy2
} {{ } ρ2 +ρ−2
. (3)
where Iz, Ix, Iy are product operators with Iz= 1
2 σz= 1
2
[1 0 0 −1
]
, Ix= 1
2 σx= 1
2
[0 1 10
]
, Iy = 1
2σy= i
2
[ 0 −1 10
]
. In a
NMR experiment the different orders will evolve according to their own rules. Actually, the different orders are the elementary constituents of the density matrices. In this case, it is possible to create a DFS just by using the different orders as basis states in the density operator representation. Therefore, we should first find a group of logical orthonormal basis states which span a self-contained space. Such a group of basis states may be expressed in the form of density operators just as the four logical states proposed in Ref.[18]. But, on the other hand, it could also exist in an operator subspace and be presented in the fashion of density operators as long as one can find a group of logical orthonormal basis states. In looking for such an operator subspace DFS, we noted that there existed four MQ coherences in the spin system SI3 (such as the methyl 13CH3 where S denotes 13C and I stands for 1H), including one quadruple quantum (QQ), two double quantum (DQ1,DQ2) and one zero quantum (ZQ). More importantly, these four MQ coherences can be distinguished by applying Liu et al.’s pulse sequence[9]. Their product operator forms are


 3
ρ1(QQ) = 3IxIyIySy − 3IxIxIySx − IxIxIxSy + IyIyIySx, ρ2(DQ1) = 3IxIyIySy + 3IxIxIySx − IxIxIxSy − IyIyIySx,
ρ3(DQ2) = IxIyIy Sy + IxIxIy Sx + IxIxIxSy + Iy IyIySx, ρ4(ZQ) = IxIyIySy − IxIxIySx + IxIxIxSy − IyIyIySx. (4)
It is obvious that not all of the above four MQ coherences are orthogonal to each other, namely, they could not be used as orthonormal basis states for a four-dimension operator space. Nevertheless, if we slightly modify them to the following set of operators shown in Eq. 5, it is interesting to find that the four modified density operators (they also belong to multiple quantum coherences) span a two-logical-qubit DFS. We denote the four modified MQ coherences as ρ1, ρ2, ρ3, ρ4, which correspond to the logical states |00〉LL〈00|, |01〉LL〈01|, |10〉LL〈10|, |11〉LL〈11|, respectively. These states are written as
ρ1 = |00〉LL〈00| = IxIyIySy − IxIxIySx − IxIxIxSy + IyIyIySx,
ρ2 = |01〉LL〈01| = IxIyIySy + IxIxIySx − IxIxIxSy − IyIyIySx, ρ3 = |10〉LL〈10| = IxIyIySy + IxIxIySx + IxIxIxSy + IyIyIySx,
ρ4 = |11〉LL〈11| = IxIyIySy − IxIxIySx + IxIxIxSy − IyIyIySx, (5)
where the normalization constants have been omitted. Specifically, the states corresponding to these density operators are the eigenstates of the operator En,
En = αn,0E1E2E3E4+αn,1E1E2E3Z4+αn,2Z1Z2Z3E4+αn,3Z1Z2Z3Z4+
αn,4X 1X 2X 3X 4+αn,5X 1X 2X 3Y 4+αn,6Y 1Y 2Y 3X 4+αn,7Y 1Y 2Y 3Y 4. (6)
In a word, by using the spin system SI3 we have actually constructed a two-logical-qubit DFS which can resist the error En. Now the next work is to find an effective experimental technique of realizing the DFS with the above product operators. Our method to implement the above DFS is based on the idea in Ref.[9], in which the pulse sequence can be divided into three parts. The first part (the pulse sequences before the encoding gradient pulse Ge) is to generate the highest state 8IxIyIySy which consists of the above four coherences. In the second part (including the gradient pulse Ge, the evolution time t1 and the two 180◦ pulses on spins I and S ), each of the above four coherences evolves differently. At the end of the second part, the four coherences have the following forms
ρ ́1(QQ) = (3IxIyIySy − 3IxIxIySx − IxIxIxSy + IyIyIySx) cos[π(3JIM + JSM )t1] exp(−t1/T2QQ),
ρ ́2(DQ1) = (3IxIyIySy + 3IxIxIySx − IxIxIxSy − IyIyIySx)
cos[π(3JIM − JSM )t1] exp(−t1/T2DQ1),
ρ ́3(DQ2) = (IxIyIySy + IxIxIySx + IxIxIxSy + IyIyIySx)
cos[π(JIM + JSM )t1] exp(−t1/T2DQ2),
ρ ́4(ZQ) = (IxIyIySy − IxIxIySx + IxIxIxSy − IyIyIySx)
cos[π(JIM − JSM )t1] exp(−t1/T2ZQ). (7)
Therefore, the four MQ coherences can be distinguished by the remote J couplings of the spins I and S with the spin M, respectively, and the transverse relaxations. The third part is to transform the multiple-quantum coherences into the detectable signals. It should be noted that different multiple-quantum coherences have different projection onto the F1 dimension, which means that the resonances of the different multiple-quantum are resolved. In particular, the selectively detected MQ-JRES spectrum can be achieved by adjusting the strength ratio between the encoding and decoding gradient pulses(i.e. between Ge and Gd). One example is that when the gradient strength ratio Ge
Gd is -8:10, the double quantum coherence(DQ2) could be selectively detected. It is also worthwhile noting that there is no interchange between the multi-quantum coherences during the evolution period.


 4
Considering that product operators ρi in Eq. (4) and ρi(MQ) in Eq. (5) have the similar forms, the states ρ1, ρ2, ρ3, ρ4 could be obtained by using special pulse sequences similar to the one in Ref.[9]. That is, the method used to yield the states ρ3 and ρ4 is, respectively, the same as the one used to produce the multi-quantum coherences ρ3(DQ2) and ρ4(ZQ). The states ρ1 and ρ2 can also be created by applying the pulse sequences corresponding to the multi-quantum coherences ρ1(QQ) and ρ2(DQ1) apart from adding two special-angle pulses on spins C and H, respectively. Interestingly, due to the same chemical shift of the three protons in a methyl, error operators only affect them simultaneously, and the following error operator Em doesn’t exist:
Em = αm,0σ1E2E3E4+αm,1E1σ2E3E4+αm,2E1E2σ3E4+αm,3σ1σ ́2E3E4+ αm,4 σ 1 E 2 σ ́3 E 4 +αm,5 E 1 σ 2 σ ́3 E 4 +αm,6 σ 1 E 2 E 3 σ ́4 +αm,7 E 1 E 2 σ 3 σ ́4
+αm,8E1σ2E3σ ́4+αm,9σ1σ ́2E3σ ́4+αm,10σ1E2σ ́3σ ́4+αm,11E1σ2σ ́3σ ́ ́4, (8)
where σ, σ ́, σ ́ ∈ {X, Y, Z}. In other words, the DFS we constructed can avoid errors En and Em simultaneously. However, that one proposed by Ollerenshaw et al. based on four different physical qubits only protests against small parts of errors En and Em. It implies that it is more effective to adopt the SIn system to realize the DFS. On the other hand, in 1D NMR quantum computing, the spins In in SIn (n=2, 3) were always regarded as one qubit, so in a sense we actually implemented a DFS in a two-qubit physical quantum system, which has more advantages over the one constructed by four physical qubits. The experiment was carried out on a Varian INOVA 600 spectrometer. The sample was 20mg alanine in 0.5ml D2O, with one carbon in methyl labelled. The molecular structure is 13CH3-12CH(NH2)-12COOH. The spin system SI3M presents 13CH3-12CH in the alanine molecule. The coupling constants obtained from the high-resolution 1D NMR spectra, JSI, JSM and JIM are 129.8Hz, 4.5Hz and 7.3Hz, respectively. Using pulsed field gradients, which is similar to the method in Ref.[9], we can selectively obtain the states ρ1, ρ2, ρ3 or ρ4. For example, ρ3 can be selectively detected by applying the pulse sequences shown in Fig.1. Here, the required gradient strength ratio between the encoding gradient(Ge) and the decoding gradient (Gd) is -8:10. The delay △ is 3.88ms corresponding to the coupling constants JSI=129.8Hz. The spectral widths are 30 and 4000 Hz in the F1 and F2 dimensions, respectively. The data points in the F1 and F2 dimensions are 64 and 10000. In order to show that this DFS’ protection against the errors En and Em, we performed a series of errors belonging to En and Em at the position c in Fig.1. Whether the DFS constructed by two-dimensional MQ J-resolved spectrum protects against errors En and Em or not, is demonstrated by observing and comparing the 2D NMR spectra before and after applying the decoherence operators. Typical experimental results are shown in Fig.2, where (A), (B) correspond to the spectra of ρ3 before and after
one performs the error operator X1X2X3Y4, respectively. It is interesting to note that the spectrum in (A) is the same as the one in (B). This means that ρ3 is certainly not affected by this decoherence. Similar outcomes are also obtained when the other operators belonging to En or Em are applied to ρ1, ρ2, ρ3 or ρ4. Due to limitation in length, we do not reproduce the experimental results. Decoherence has been one of the severe impediments in quantum information processing. Many techniques have been widely studied. Therefore it is significative to experimentally and theoretically focus on the DFS that has been developed as a tool for protecting QIP. The idea for constructing the DFS provided in this paper shows new insights into effectively utilizing the spin system including CHn (n=2,3) to achieve quantum computing as well as extending the number of qubits. This process is impossible in 1D NMR, since the magnetically equivalent spins in CHn can not been fully used. But here we showed that 2D MQ-JRES could do it by using the MQ coherences which were modulated by the remote spin. In addition, a novel point is that since the n numbers of H have the same chemical shift, the errors only affect them together, so to this extent, this DFS may avoid more errors than others that were constructed by spins with different chemical shifts. Simultaneously, when one performs 1D NMR quantum computing with a sample containing the CHn group, all the protons in each CHn group which could only be used as one qubit, couple to the other spins. In this condition, the spectra of the other spins become more complex than those for which there are no magnetically equivalent spins in the sample, although their number of qubits is the same. So it seems that the CHn group just makes 1D NMR QC more complex. However, just as described above, the CHn group, in 2D MQJES, makes our DFS more powerful. Here, we merely performed a special DFS applying 2D MQJES. The demonstration of some quantum algorithms based on this DFS is under way. In summary, we have provided a new two-logical-qubit DFS with 2D MQ-JRES and the three magnetically equivalent spins in CH3. In a sense, the three protons are distinguishable. The corresponding experimental demonstration has been completed. Compared to the other schemes for implementing DFS, our method protected against more


 5
error operators just by employing a smaller nuclear system. Specifically, this idea can also be applied to implement other QIP tasks on NMR QC. It follows that when the selected spin system contains a methyl, we can implement an (n+2)-qubit quantum computing just using n qubits of one-dimensional NMR QC. Conclusively, the 2D NMR method presented in this letter may be helpful for developing the multi-qubit NMR QC. This work has been supported by the National Natural Science Foundation of China under Grant No. 10374103, the National Basic Research Programme of China under Grant No.2001CB309309, and the National Knowledge Innovation Program of the Chinese Academy of Sciences under Grant No: KJCX2-W1-3.
[1] P. Shor, in Proceedings of the 35th Annual Symposium on Foundations of Computer Science (IEEE Computer Society, Los Alamitos, CA, 1994), pp.124-134. [2] L. Grover, in Proceedings of the 28th Annual ACM Symposium on the Theory of Computing (Philadelphia, Pennsylvania, 22-24 May 1996), pp. 212-219. [3] S. Lloyd, Science 273, 1073(1996). [4] J. A. Jones, Prog. NMR. Spectrosc. 38, 325(2001). [5] W.S. Warren, Science 277, 1688(1997). [6] Z. L. M ́adi, R. Bru ̈chweiler, and R. R. Ernst, J. Chem. Phys. 109, 10 603(1998). [7] T. S. Mahesh, Kavita Dorai, Arvind and Anil Kumar, J. Magn. Reson. 148 95(2001). [8] T. S. Mahesh, Neeraj Sinha, K. V. Ramanathan, and Anil Kumar, Phys. Rev. A 65, 022312(2002). [9] Maili Liu and Xu Zhang, J. Magn. Reson. 146, 277(2000). [10] R. Bru ̈schweiler, Phys. Rev. Lett. 85, 4815(2000). [11] P. Zanardi and M. Rasetti, Phys. Rev. Lett. 79, 3306(1997); Paolo Zanardi, Mario Rasetti, Mod. Phys. Lett. B 11, 1085(1997); P. Zanardi, Phys. Rev. A 57, 3276(1998). [12] L. –M. Duan and G. –C. Guo, Phys. Rev. Lett. 79, 1953(1997); Lu-Ming Duan and Guang-Can Guo, Phys. Rev. A 57, 737(1998). [13] D. A. Lidar, I. L. Chuang, and K. B. Whaley, Phys. Rev. Lett. 81, 2594(1998). [14] L. Viola, E. Knill, and S. Lloyd, Phys. Rev. Lett. 85, 3520(2000). [15] S. De Filippo, Phys. Rev. A 62, 052307(2000). [16] E. Knill, R. Laflamme, and L. Viola, Phys. Rev. Lett. 84, 2525(2000). [17] P. Zanardi, Phys. Rev. A 63, 012301(2001). [18] J. E. Ollerenshaw, D. A. Lidar, and L. E. Kay, Phys. Rev. Lett. 91, 217904(2003). [19] Lorenza Viola, Evan M. Fortunato, Marco A. Pravia, Emanuel Knill, Raymond Laflamme, and David G. Cory, Science 293, 2059(2001). [20] WonYoung Hwang, Hyukjae Lee, Doyeol (David) Ahn and Sung Woo Hwang, Phys. Rev. A 62, 062305(2000). [21] R.R. Ernst, G. Bodenhausen, and A. Workaun, Principles of nuclear magnetic resonance in one and two dimensions, (Clarendon Press, Oxford, 1987).


 6
FIG. 1: Pulse sequence for multi-quantum J-resolved NMR spectroscopy showing ρ3 can protect against the error X1X2X3Y4, where a is the encoding process, b is the decoding process, and c is the position to perform errors.


 7
FIG. 2: Multi-quantum NMR spectra of ρ3 before (A) and after (B) performing the error X1X2X3Y4. The projection into F2 dimension presents the 1H NMR spectrum of the 13CH3 group protons with the signal from 12CH3 protons. The projection into F1 dimension shows the MQ spectrum, which is given at the right side of the 2D plot.


 t1
1H (I)
13C (S)
Gradient
Ge Gd
c t2
ab
