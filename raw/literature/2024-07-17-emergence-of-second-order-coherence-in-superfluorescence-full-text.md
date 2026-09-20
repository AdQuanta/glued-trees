# Emergence of second-order coherence in superfluorescence - Full Text

> Source: http://arxiv.org/abs/2407.12549
> Collected: 2026-09-20
> Published: 2024-07-17
> Zotero parent key: 644YRMSN
> Evidence: Zotero indexed PDF text

Emergence of second-order coherence in superfluorescence
Constanze Bach, Felix Tebbenjohanns, Christian Liedl, Philipp Schneeweiss, and Arno Rauschenbeutel Department of Physics, Humboldt-Universita ̈t zu Berlin, 10099 Berlin, Germany (Dated: July 18, 2024)
We experimentally investigate the second-order quantum coherence function of a superradiant burst in a cascaded quantum system. We chirally (i.e. direction-dependently) couple roughly 900 cesium atoms to the forward propagating mode of an optical nanofiber. We then prepare the ensemble in the maximally inverted state, where the subsequent collective emission of a burst is known as superfluorescence. Here, we observe that second-order coherence emerges in the course of the decay. This is a clear feature of the underlying collective dynamics that is also at the origin of the superradiant burst itself. We furthermore study the dynamics of the second-order coherence function of the emission in dependence on the initial average dipole moment of the ensemble. In addition, by correlating the detection of early and late photon emission events, we obtain evidence for fundamental shot-to-shot fluctuations in the delay of the start of the burst emission. Our findings reveal that, despite the fundamentally different coupling Hamiltonian, superradiance in cascaded and symmetrically coupled systems feature a strikingly large number of similarities.
Introduction. The collective emission of radiation is an ubiquitous physical process that underlies devices such as lasers and phased-array antennas, applications such as optical quantum memories, and even phenomena in space such as astrophysical cyclotron masers [13]. Already in 1954, R. H. Dicke studied the collective emission originating from a dense ensemble of two-level quantum emitters that are initially prepared in the maximally excited state [4–7]. In this system, superfluorescence occurs, where the radiated optical power first increases with time, then reaches a maximum and, eventually, decays. Such a superradiant burst of light is a hallmark effect in many-body quantum optics and qualitatively different from the exponential decay observed in the emission from independent atoms. Only recently, it was theoretically [8] and experimentally [9] shown that a burst also occurs for a cascaded interaction between emitters arranged in a chain. In this setting, a given atom i influences the decay of atoms j > i but not vice versa [10, 11]. Cascaded interactions between quantum emitters can be engineered, for example with Rydberg atoms [12], acousto-optic control techniques [13], spinorbit coupled Bose-Einstein condensates [14], and occur naturally for quantum emitters in optical near fields due to chiral light-matter interaction [15]. While superfluorescence and in general superradiant phenomena have been studied extensively [7, 16–25], important properties such as the coherence and the photon statistics of the burst emission have only been explored sparsely in the literature [9, 26–29].
Here, we experimentally study the two-time secondorder quantum coherence function [30], g(2)(t1, t2), of the superradiant burst emitted by a cascaded quantum system. Our system is realized with 900 cesium atoms chirally coupled to the guided mode of an optical nanofiber, i.e., a cylindrical dielectric waveguide with a diameter smaller than the wavelength of the guided light. From these second-order correlations, we discern the regimes
of superfluorescence and superradiance, we directly observe the spontaneous build-up of second-order coherence of the radiation emitted by an ensemble of initially independent atoms, and we infer shot-to-shot fluctuations of the delay between the excitation and the burst emission. We compare our data to the symmetric Dicke model as well as to a stochastic simulation of our system, which is based on the truncated Wigner approximation.
Setup and Measurement. Our experimental setup is sketched in Fig. 1. We realize an optical trapping potential in the evanescent field surrounding the nanofiberwaist of a tapered optical fiber (TOF), by sending running wave blue-detuned laser light (wavelength 760 nm, power 20.5 mW) and forward and backward propagating red-detuned laser light (wavelength 1064 nm, powers 1.3 mW and 1.1 mW, respectively) through the nanofiber. This creates two diametral arrays of trapping sites [31], which we probabilistically load with cold cesium atoms by overlapping the nanofiber with a molasses-cooled cloud of atoms from a magneto-optical trap (MOT). Due to the collisional blockade effect, each trapping site is filled with at most a single atom [32]. We prepare the atoms on only one side of the fiber in their motional ground state using side-selective degenerate Raman cooling (DRC) for 50 ms [33]. With this, we end up with a single one-dimensional array of trapped cesium atoms, which lies in the x − y-plane, see Fig. 1(a). Upon DRC, the internal state of the atoms is |g⟩ = |6S1/2, F = 4, mF = −4⟩, where the quantization axis is chosen along the z-direction. We control the number of atoms, N , via the MOT loading time and determine it by measuring the optical depth (OD) with transmission spectroscopy through the TOF. All the measurements shown here are performed at an OD of about 40, corresponding to N ≈ 900 [31].
Because of spin-momentum locking [34], the polarization of the waveguide mode at the position of the atoms depends strongly on its sense of propagation, for
arXiv:2407.12549v1 [quant-ph] 17 Jul 2024


 2
Detector 2
A=п
A>п
TOF with
nanofiber waist Fluorescence
A<п
BS
Time
Power
Detector 1
(a)
(d)
(b)
(c)
Bloch sphere
xy
Cesium atoms
z
FIG. 1. (a) Schematic of the experimental setup for measuring the second-order coherence function g(2)(t1, t2) of a superradiant burst. An ensemble of about 900 cesium atoms (red circles) are optically trapped near the surface of an optical nanofiber. A pulse of nanofiber-guided resonant light coherently excites the ensemble close to full inversion of a cycling transition which predominantly re-emits the light into the forward-propagating nanofiber mode, thereby realizing a cascaded quantum system. The optical power and its secondorder correlation are obtained using a Hanbury-Brown and Twiss-type detection setup. (b) Representation of the initial state, parameterized by the Rabi pulse area A on the Bloch sphere. (c) Measured two-photon coincidence rates within a 3 ns bin width. A maximum of roughly 250 two-photon coin
cidences occurs at t1 = t2 ≈ 7.5 ns for a total of 107 excitation pulses. (d) Sketch of the optical power on a single detector.
ward or backward. In particular, the radiation emitted on the σ−-polarized atomic D2-cycling transition |g⟩ → |e⟩ = |6P3/2, F = 5, mF = −5⟩ has an overlap with the forward-propagating mode of β ≈ 0.01, while its overlap with the backward-propagating mode is about ten times smaller. Thanks to this so-called chiral coupling, the nanofiber-coupled atoms thus realize a cascaded quantum system [10, 11, 15]. We coherently drive the |g⟩ → |e⟩ transition with a fiber-guided forward propagating resonant optical Rabi pulse of duration Tpulse = 4 ns, which is shorter than the excited-state lifetime of τ = 30.5 ns [35]. This prepares the ensemble close to the product state
|ψ0⟩ =
N ⊗
k=1
[
cos
(A
2
)
|gk⟩ − i sin
(A
2
)
|ek ⟩
]
, (1)
where the atomic index k = 1, . . . , N increases along the propagation direction of the light. This initial state is depicted on the Bloch sphere in Fig. 1(b). The Rabi pulse area A = ΩTpulse is defined by the Rabi frequency Ω applied to the first atom. In practice, because of absorption of the pulse upon propagation through the atomic en
semble and due to inhomogeneous atom-waveguide coupling, the atoms experience slightly different pulse areas Ak ≈ A, see discussions in Refs. [9, 35]. In each experimental run, we repeatedly excite the ensemble 400 times within 80 ms. During this probing, which would slightly heat the atoms, we continuously cool the ensemble by applying DRC on the D1 line (|6S1/2, F = 4⟩ → |6P1/2, F = 4⟩) with a free-space laser, achieving a survival of 75% of the atoms by the end of the probing period. Because the scattering rate of the D1 light is sufficiently small, this cooling does not alter the burst dynamics. A fully inverted and sufficiently large ensemble (for us N ≫ 100 and A ≈ π) then radiates a superradiant burst as sketched in Fig. 1(d) and experimentally investigated in detail in Ref. [9]. A hybrid photodetector (Hamamatsu, R10467, dead time < 2 ns) captures both this superradiant burst and the preceding transmitted excitation Rabi pulse. For the two-time correlation measurement of the burst, we split the light into two parts and delay one half by about 100 ns using a 20 m long optical fiber before both fractions reach the same detector. Since the decay dynamics is much faster than 100 ns, this allows us to measure the two-photon coincidence rate, nc(t1, t2). Here, t1 and t2 are measured from the end of the Rabi pulse. A sample measurement of nc(t1, t2) during the emission of a superradiant burst for a maximally inverted ensemble is shown in Fig. 1(c), with a binning of 3 ns. The normalized second-order coherence function is then given by
g(2)(t1, t2) = nc(t1, t2)
n1(t1)n2(t2) , (2)
where nj(tj) is the photon rate on detector j at the respective time tj with j = 1, 2.
Initial second-order coherence function. Let us first discuss the value of the second-order coherence function of the light that is emitted right after the excitation pulse, g(2)(0, 0), which is shown in Fig. 2(a) as a function of A (black circles). The data reaches a peak value of g(2)(0, 0) = 2 for A ≈ 1.1π, falls off over a range of about ±0.1π, and decreases to g(2)(0, 0) ≈ 1 for substantially smaller or larger pulse areas. This behavior can be understood in the following way. As discussed in Ref. [35], because of the absorption of the pulse along the ensemble, a pulse area at the first atom slightly larger than π (here, A ≈ 1.07π) maximizes the mean excitation stored in the ensemble. For this case of maximum inversion,
i.e. |ψ0⟩ ≈ ⊗
k |ek⟩, the ensemble-averaged dipole mo
ment vanishes, see also Bloch sphere representation in Fig. 1(b). Correspondingly, the fields radiated by the atoms do not have a fixed phase relationship. Thus, the initially emitted light features the statistics of independent atoms, yielding g(2)(0, 0) = 2. By contrast, when exciting the ensemble with a pulse area A below or above maximal inversion, a non-zero average dipole moment is imprinted on the ensemble by the excitation laser. Thus,


 3
0.8 0.9 1 1.1 1.2 1.3
A/π
0
1
2
g(2)(0, 0)
(a)
Analytical TWA
0
4
8
0
1
2
Power [nW]
0
4
8
0
1
2
A = 0.95 π
(b)
0
1
2
g(2)(t, t)
A = 1.10 π
(c)
0 5 10 15 20 25 30 Time t [ns]
0
1
2
A = 1.26 π
(d)
FIG. 2. (a) Experimentally measured second-order coherence function g(2)(0, 0) of the initial emission as a function of the excitation Rabi pulse area A (back circles with Poissonian error bars). The grey and purple theory lines are, respectively, an analytical prediction according to Eq. (3) and a numerical prediction of the TWA model for N = 900 atoms. (b)-(d) g(2)(t, t) as a function of time for three values of A, as indicated. For A = 1.10π, g(2)(t, t) develops from 2 to 1 during the burst. For A ̸= 1.10π, g(2)(t, t) = 1 is constant. The purple lines show TWA predictions with the one-sigma error due to a finite number of computed trajectories (shaded areas). The grey dashed line in panel (c) is the prediction by the symmetric Dicke model with NDicke = 9. The optical power P (t) is shown as the light blue area with the corresponding TWA prediction as the dark blue line. The oscillations on top of P (t) are quantum beats that originate from weak excitation of the hyperfine state |6P3/2, F = 4⟩. In (b) - (d) we omitted datapoints, where we did not observe a single coincidence.
the atoms radiate in phase and the statistics of the emitted light reproduces those of the excitation laser field, resulting in g(2)(0, 0) = 1. Let us now theoretically analyze g(2)(0, 0) when the atoms are prepared in |ψ0⟩ as defined in Eq. (1). The
total electric field Eˆ in the detected mode is given by
the sum over the contribution of all atomic dipoles σˆk =
|gk⟩ ⟨ek|, i.e., Eˆ ∝ ∑
k σˆk. As shown in the supplemen
tal material (SM), we find the following expression for second-order quantum coherence function
g(2)(0, 0) = ⟨ψ0| Eˆ†Eˆ†EˆEˆ |ψ0⟩
⟨ψ0| Eˆ†Eˆ |ψ0⟩2 ≈ 2 − 1
(1 + 1
N cos2(A/2) )2 ,
(3) where the right hand side is exact in the large-ensemble limit of N ≫ 1. We show this prediction as a grey line for N = 900 in Fig. 2(a). The width of the peak predicted
for g(2)(0, 0) as a function of A is approximately 2π/√N , which roughly matches our data. We can additionally model the absorption of the Rabi pulse along the ensemble by applying a stochastic numerical model based on the truncated Wigner approximation (TWA) [36, 37], see purple line in Fig. 2(a). It is apparent that this explains the shift of the peak by 0.07π. More details on the TWA follow below.
Dynamics of second-order coherence function. In Figs. 2(b)–(d), we show the measured optical power, which is averaged over more than 106 excitation pulses, as the blue shaded area, and the normalized secondorder coherence function at equal time, g(2)(t, t), during the burst as black circles for different initial atomic states characterized by the Rabi pulse area A. The characteristic feature of the superradiant decay of a maximally inverted atomic ensemble is the burst of the optical power [9]. It is most prominent in panel (c), where the initial state is close to maximal inversion. Notably, there we measure a decrease of g(2)(t, t) during the burst emission from its initial value of g(2)(0, 0) = 2 to g(2)(t, t) = 1 at t ≈ 19 ns. In stark contrast, we observe a constant g(2)(t, t) ≈ 1 for the entire duration of the burst emission in panels (b) and (d), where the ensemble’s average initial dipole moment is nonzero. The theoretical modelling of such second-order correlations for as many as one thousand atoms requires state-of-the-art approaches [8, 38–46]. Here, we apply an efficient, recently developed stochastic simulation tool, which is based on the truncated Wigner approximation for spins (TWA) [36, 47]. The latter can describe many emitters and many excitations. In our model, the system dynamics are mapped to a set of 2N coupled, nonlinear stochastic differential equations, which can be numerically solved for thousands of atoms, to accurately predict both the output power (blue lines in Fig. 2) and g(2)(t, t) (purple lines). For the details on the implementation of the TWA, see Ref. [37]. Our modelling includes the coherent Rabi excitation process, where we account for the absorption of the excitation pulse along the ensemble as well as for the inhomogeneous atom-waveguide coupling due to the atom’s thermal motion. In addition to predicting the system dynamics with the TWA model, we also numerically solve the symmetric Dicke model and present its prediction for g(2)(t, t) as the grey


 4
0 5 10 15 20 25 30 Time t [ns]
1.0
1.5
2.0
g(2)(t, t)
N 7 90 150 300 500 700 1000
FIG. 3. TWA simulation of g(2)(t, t) for different numbers of atoms. For N < Nthr ≈ 100 (blue) no burst occurs [9] and g(2)(t, t) = 2 is constant. For N > Nthr (red), g(2)(t, t) evolves towards 1, i.e., second-order coherence builds up during the collective emission.
dashed line in Fig. 2(c). Since this model assumes perfect atom-waveguide coupling (βDicke = 1), we use an atom number of NDicke = 9 ≈ βN [24] (see SM). This model shows qualitative agreement with our experimental data, particularly regarding the reduction of g(2)(t, t) from 2(1 − 1/NDicke) ≈ 2 to 1. However, it does not capture the experimentally observed time dynamics as accurately as the TWA. For maximal inversion, the ensemble has no dipole moment. Therefore the emission is seeded by vacuum fluctuations, a situation in which superradiance is also termed superfluorescence [48, 49]. Following the initially independent emission, second-order coherence builds up while the light is radiated. This characteristic dynamics of superfluorescence occurs because the atomic dipoles spontaneously synchronize via the shared mode. More in detail, we take the fact that we observe g(2)(t, t) < 2 as a signature of this synchronization, because it violates the Siegert relation [50], which holds for independent emitters and reads g(2)(t, t) = 1 + |g(1)(t, t)|2 = 2 [51]. Note that for an excitation Rabi pulse area sufficiently below and above maximal inversion [c.f. Fig. 2(a) and (c)], the Siegert relation is also broken. However, there the synchronization of the dipoles does not spontaneously build up, but is already present at t = 0 since the atomic dipoles are already synchronized to the excitation laser [9]. To further our understanding that the emergence of second-order coherence is a collective phenomenon, we now study g(2)(t, t) as a function of the number of atoms N . In a cascaded system with imperfect atom-mode coupling (β < 1), a burst only appears when N exceeds a threshold value, Nthr = 1+1/β, whereas the atoms decay independently for N ≪ Nthr [7, 8]. Here, Nthr is about 100. Due to low count rates, we cannot reliably measure g(2)(t, t) for small atom numbers in our experiment and therefore analyze this regime theoretically using the TWA model. In Fig. 3, we show the calculated g(2)(t, t) for an ensemble of homogeneously coupled atoms with
0 10 20 30
t2 [ns]
0
10
20
30
t1 [ns]
Power [arb.unit]
(a) Superradiant burst
0 10 20 30
t2 [ns]
0
10
20
30
(c)
Power [arb.unit]
Coherent pulse
0 10 20 30 |t2 − t1| [ns]
1
2
g(2)(t1 = 4 ns, t2 ≥ 4 ns)
(b)
0 10 20 30 |t2 − t1| [ns]
1
2
(d)
0.0
0.5
1.0
1.5
2.0
g(2)(t1, t2)
FIG. 4. (a) Color plot of g(2)(t1, t2) of the superradiant burst at detection times t1, t2. Red (blue) colors indicate g(2) > 1 (g(2) < 1). The trace of the average measured power (black line) is shown in the top panel for comparison. (b) A cut of g(2)(t1 = 4 ns, t2) as a function of |t2 − t1| (black circles with Poissonian error bars), reveals anti-correlations for delays above 20 ns. The grey solid line is a prediction based on the symmetric Dicke model for N = 9 and β = 1. (c), (d) Same analysis for a coherent laser pulse with similar shape
and duration as the burst in (a). Here, g(2)(t1, t2) = 1 within the error bars as the photons are uncorrelated.
β = 0.01, which is initialized in |ψ0⟩ = ⊗
k |ek⟩. The rate
at which the second-order coherence builds up decreases when N is reduced and, importantly, for N < Nthr (de
picted in blue), g(2)(t, t) is a constant. In that regime,
the ensemble remains in a product state ρˆ(t) = ⊗
k ρˆk(t),
where ρˆk(t) is the density matrix of the kth atom, yield
ing g(2)(t, t) = g(2)(0, 0) = 2. These simulation results further support the conclusion that a build-up of secondorder coherence in our experiment is a signature of a departure of the ensemble from the product state, i.e.
ρˆ(t) ̸= ⊗
k ρˆk(t).
Shot-to-shot variations. Finally, we turn to the statistical properties of the light emitted from a maximally inverted ensemble by considering g(2)(t1, t2) for unequal times t1 ̸= t2, depicted as a color plot in Fig. 4(a).
In Fig. 4(b), we show g(2)(t1 = 4 ns, t2) as a function of the time difference |t2 − t1|. This data thus quantifies the correlation between the burst light at early and late times. Interestingly, the detection events are correlated, g(2)(t1, t2) > 1, for small time differences and anti
correlated, g(2)(t1, t2) < 1, for larger time differences. These anti-correlations are also apparent as blue regions in the bottom right and top left corner of Fig. 4(a). For comparison, we present the results of the same correlation measurement performed with a coherent laser pulse


 5
of similar shape and duration in panels (c) and (d). Here, as expected, g(2)(t1, t2) = 1 is constant within the error bars for all combinations of t1 and t2 as there are no correlations between the detection of early and late photons. For the time being, the TWA cannot predict twotime correlators. In order to still compare our observations to a model prediction, we therefore apply the quantum regression theorem to the symmetric Dicke model for NDicke = 9 (see SM). The resulting prediction for
g(2)(t1 = 4 ns, t2) is shown as a grey solid line in panel (b) and features a qualitatively similar transition from g(2)(t1, t1) ≈ 2 to g(2)(t1 = 4 ns, t2) < 1 at a large time difference. To understand these anti-correlations, let us assume that individual bursts have a duration τs. Moreover, let us assume that, despite the identical preparation of the atoms, each burst occurs after a varying delay with respect to the excitation pulse [7]. When averaging over many realizations, the resulting power trace will have a duration that is longer than τs. At the same time, the probability of the detection of two photons separated by more that τs is smaller in a single shot than on average. We thus interpret the observed anti-correlations of g(2)(t1, t2) as a signature of these fluctuations. For the case of symmetric coupling, such shot-to-shot variations of the burst are a known feature of superfluorescence and originate from the fact that the burst is triggered by spontaneous emission [18, 52]. Conclusion and Outlook. In conclusion, we have measured and theoretically investigated the two-time secondorder quantum coherence function, g(2)(t1, t2), of a superradiant burst emitted by a cascaded quantum system. This allowed us to observe the emergence of second-order coherence in the light emitted by initially independent emitters. Remarkably, this occurs despite the absence of any feedback in a cascaded system. In particular, in conjunction with the results from Ref. [9], it becomes apparent that superradiance in a cascaded quantum system features surprisingly many similarities with the symmetric Dicke model. Further characterization of the photonic output state of cascaded quantum systems includes measurements of even higher-order correlations, such as g(3)(t1, t2, t3). Moreover, we would like to investigate the emission of coherently and incoherently driven cascaded quantum systems in the steady-state. From a theoretical standpoint, such experiments allow one to benchmark state-of-theart simulation methods of many-body quantum systems. From a conceptional point of view, they may shed light on, e.g., the physics underlying superradiant lasing [16]. We thank M. Fleischhauer, C. Mink, K. Mølmer, A. Poddubny, J. Volz, L. Yatsenko for fruitful discussions. We acknowledge funding by the Alexander von Humboldt Foundation in the framework of the Alexander von Humboldt Professorship endowed by the Federal Ministry of Education and Research.
[1] V. Letokhov and S. Johansson, Astrophysical lasers (Oxford University Press, 2009). [2] M. R. W. Guerin and R. Kaiser, Light interacting with atomic ensembles: collective, cooperative and mesoscopic effects, Journal of Modern Optics 64, 895 (2017). [3] A. S. Sheremet, M. I. Petrov, I. V. Iorsh, A. V. Poshakinskiy, and A. N. Poddubny, Waveguide quantum electrodynamics: Collective radiance and photon-photon correlations, Rev. Mod. Phys. 95, 015002 (2023). [4] R. H. Dicke, Coherence in spontaneous radiation processes, Phys. Rev. 93, 99 (1954). [5] N. Skribanowitz, I. Herman, J. MacGillivray, and M. Feld, Observation of Dicke superradiance in optically pumped HF gas, Phys. Rev. Lett. 30, 309 (1973). [6] M. Gross, C. Fabre, P. Pillet, and S. Haroche, Observation of near-infrared Dicke superradiance on cascading transitions in atomic sodium, Phys. Rev. Lett. 36, 1035 (1976). [7] M. Gross and S. Haroche, Superradiance: An essay on the theory of collective spontaneous emission, Phys. Rep. 93, 301 (1982). [8] S. Cardenas-Lopez, S. J. Masson, Z. Zager, and A. Asenjo-Garcia, Many-body superradiance and dynamical mirror symmetry breaking in waveguide qed, Phys. Rev. Lett. 131, 033605 (2023). [9] C. Liedl, F. Tebbenjohanns, C. Bach, S. Pucher, A. Rauschenbeutel, and P. Schneeweiss, Observation of superradiant bursts in a cascaded quantum system, Phys. Rev. X 14, 011020 (2024). [10] C. W. Gardiner, Driving a quantum system with the output field from another driven quantum system, Phys. Rev. Lett. 70, 2269 (1993). [11] H. J. Carmichael, Quantum trajectory theory for cascaded open systems, Phys. Rev. Lett 70, 2273 (1993). [12] N. Stiesdal, H. Busche, K. Kleinbeck, J. Kumlin, M. G. Hansen, H. P. B ̈uchler, and S. Hofferberth, Controlled multi-photon subtraction with cascaded rydberg superatoms as single-photon absorbers, Nat. Commun. 12, 4328 (2021). [13] G. Calajo ́, M. J. A. Schuetz, H. Pichler, M. D. Lukin, P. Schneeweiss, J. Volz, and P. Rabl, Quantum acoustooptic control of light-matter interactions in nanophotonic networks, Phys. Rev. A 99, 053852 (2019). [14] T. Ramos, H. Pichler, A. J. Daley, and P. Zoller, Quantum spin dimers from chiral dissipation in cold-atom chains, Phys. Rev. Lett. 113, 237203 (2014). [15] P. Lodahl, S. Mahmoodian, S. Stobbe, A. Rauschenbeutel, P. Schneeweiss, J. Volz, H. Pichler, and P. Zoller, Chiral quantum optics, Nature 541, 473 (2017). [16] J. G. Bohnet, Z. Chen, J. M. Weiner, D. Meiser, M. J. Holland, and J. K. Thompson, A steady-state superradiant laser with less than one intracavity photon, Nature 484, 78 (2012). [17] T. Bienaim ́e, R. Bachelard, N. Piovella, and R. Kaiser, Cooperativity in light scattering by cold atoms, Fortschritte der Physik 61, 377 (2013). [18] K. Cong, Q. Zhang, Y. Wang, G. T. Noe, A. Belyanin, and J. Kono, Dicke superradiance in solids [invited], J. Opt. Soc. Am. B 33, C80 (2016). [19] T. Laske, H. Winter, and A. Hemmerich, Pulse delay time statistics in a superradiant laser with calcium atoms,


 6
Phys. Rev. Lett. 123, 103601 (2019). [20] G. Ferioli, A. Glicenstein, F. Robicheaux, R. T. Sutherland, A. Browaeys, and I. Ferrier-Barbut, Laser-driven superradiant ensembles of two-level atoms near dicke regime, Phys. Rev. Lett. 127, 243602 (2021). [21] R. Pennetta, D. Lechner, M. Blaha, A. Rauschenbeutel, P. Schneeweiss, and J. Volz, Observation of coherent coupling between super- and subradiant states of an ensemble of cold atoms collectively coupled to a single propagating optical mode, Phys. Rev. Lett. 128, 203601 (2022). [22] M. Reitz, C. Sommer, and C. Genes, Cooperative quantum phenomena in light-matter platforms, PRX Quantum 3, 010201 (2022). [23] A. C. Santos and R. Bachelard, Generation of maximally entangled long-lived states with giant atoms in a waveguide, Phys. Rev. Lett. 130, 053601 (2023). [24] G. Ferioli, S. Pancaldi, A. Glicenstein, D. Cle ́ment, A. Browaeys, and I. Ferrier-Barbut, Non-gaussian correlations in the steady state of driven-dissipative clouds of two-level atoms, Phys. Rev. Lett. 132, 133601 (2024). [25] S. Ostermann, O. Rubies-Bigorda, V. Zhang, and S. F. Yelin, Breakdown of steady-state superradiance in extended driven atomic arrays, Phys. Rev. Res. 6, 023206 (2024). [26] F. Haake and R. J. Glauber, Quantum statistics of superradiant pulses, Phys. Rev. A 5, 1457 (1972). [27] R. Lopes, A. Imanaliev, M. Bonneau, J. Ruaudel, M. Cheneau, D. Boiron, and C. I. Westbrook, Second-order coherence of superradiance from a bose-einstein condensate, Phys. Rev. A 90, 013615 (2014). [28] F. Jahnke, C. Gies, M. Aßmann, M. Bayer, H. Leymann, A. Foerster, J. Wiersig, C. Schneider, M. Kamp, and S. Ho ̈fling, Giant photon bunching, superradiant pulse emission and excitation trapping in quantum-dot nanolasers, Nat. Commun. 7, 11540 (2016). [29] S. Stryzhenko, A. Bruns, and T. Peters, n scaling of large-sample collective decay in inhomogeneous ensembles, Phys. Rev. Res. 6, 013091 (2024). [30] R. J. Glauber, The quantum theory of optical coherence, Phys. Rev. 130, 2529 (1963). [31] E. Vetsch, D. Reitz, G. Sagu ́e, R. Schmidt, S. Dawkins, and A. Rauschenbeutel, Optical interface created by laser-cooled atoms trapped in the evanescent field surrounding an optical nanofiber, Phys. Rev. Lett. 104, 203603 (2010). [32] N. Schlosser, G. Reymond, and P. Grangier, Collisional blockade in microscopic optical dipole traps, Phys. Rev. Lett. 89, 023005 (2002). [33] Y. Meng, A. Dareau, P. Schneeweiss, and A. Rauschenbeutel, Near-ground-state cooling of atoms optically trapped 300 nm away from a hot surface, Phys. Rev. X 8, 031054 (2018). [34] R. Mitsch, C. Sayrin, B. Albrecht, P. Schneeweiss, and A. Rauschenbeutel, Quantum state-controlled directional spontaneous emission of photons into a nanophotonic waveguide, Nat. Commun. 5, 5713 (2014). [35] C. Liedl, S. Pucher, F. Tebbenjohanns, P. Schneeweiss, and A. Rauschenbeutel, Collective radiation of a cascaded quantum system: From timed Dicke states to inverted ensembles, Phys. Rev. Lett. 130, 163602 (2023). [36] C. D. Mink and M. Fleischhauer, Collective radiative interactions in the discrete truncated Wigner approximation, SciPost Phys. 15, 233 (2023).
[37] F. Tebbenjohanns, C. D. Mink, C. Bach, A. Rauschenbeutel, and M. Fleischhauer, Predicting correlations in superradiant emission from a cascaded quantum system (2024), arXiv:2407.02154. [38] L. Ostermann, H. Zoubi, and H. Ritsch, Cascaded collective decay in regular arrays of cold trapped atoms, Opt. Express 20, 29634 (2012). [39] T. Caneva, M. T. Manzoni, T. Shi, J. S. Douglas, J. I. Cirac, and D. E. Chang, Quantum dynamics of propagating photons with strong interactions: a generalized input–output formalism, New Journal of Physics 17, 113001 (2015). [40] S. Mahmoodian, G. Calajo ́, D. E. Chang, K. Hammerer, and A. S. Sørensen, Dynamics of many-body photon bound states in chiral waveguide QED, Phys. Rev. X 10, 031011 (2020). [41] F. Robicheaux and D. A. Suresh, Beyond lowest order mean-field theory for light interacting with atom arrays, Phys. Rev. A 104, 023702 (2021). [42] S. Arranz Regidor, G. Crowder, H. Carmichael, and S. Hughes, Modeling quantum light-matter interactions in waveguide qed with retardation, nonlinear interactions, and a time-delayed feedback: Matrix product states versus a space-discretized waveguide model, Phys. Rev. Res. 3, 023030 (2021). [43] K. J. Kusmierek, S. Mahmoodian, M. Cordier, J. Hinney, A. Rauschenbeutel, M. Schemmer, P. Schneeweiss, J. Volz, and K. Hammerer, Higher-order mean-field theory of chiral waveguide QED, SciPost Phys. Core 6, 041 (2023). [44] O. Rubies-Bigorda, S. Ostermann, and S. F. Yelin, Dynamic population of multiexcitation subradiant states in incoherently excited atomic arrays, Phys. Rev. A 107, L051701 (2023). [45] K. Kleinbeck, H. Busche, N. Stiesdal, S. Hofferberth, K. Mølmer, and H. P. Bu ̈chler, Creation of nonclassical states of light in a chiral waveguide, Phys. Rev. A 107, 013717 (2023). [46] E. Vlasiuk, A. V. Poshakinskiy, and A. N. Poddubny, Two-photon pulse-scattering spectroscopy for arrays of two-level atoms coupled to a waveguide, Phys. Rev. A 108, 033705 (2023). [47] J. Schachenmayer, A. Pikovski, and A. M. Rey, Manybody quantum spin dynamics with monte carlo trajectories on a discrete phase space, Phys. Rev. X 5, 011022 (2015). [48] Q. Vrehen, M. Schuurmans, and D. Polder, Superfluorescence: macroscopic quantum fluctuations in the time domain, Nature 285, 70 (1980). [49] R. Bonifacio and L. A. Lugiato, Cooperative radiation processes in two-level systems: Superfluorescence, Phys. Rev. A 11, 1507 (1975). [50] D. Ferreira, R. Bachelard, W. Guerin, R. Kaiser, and M. Fouch ́e, Connecting field and intensity correlations: The Siegert relation and how to test it, American Journal of Physics 88, 831 (2020). [51] The normalized, equal-time first-order coherence function is by definition equal to unity, g(1)(t, t) = 1 [30, 53]. [52] R. Florian, L. O. Schwan, and D. Schmid, Time-resolving
experiments on dicke superfluorescence of O2 − centers in kcl. two-color superfluorescence, Phys. Rev. A 29, 2709 (1984). [53] R. Loudon, The quantum theory of light, 3rd ed. (Oxford


 7
University Press, 2000).


 Supplemental Material for
Emergence of second-order coherence in superfluoresence
Constanze Bach, Felix Tebbenjohanns, Christian Liedl, Philipp Schneeweiss, and Arno Rauschenbeutel
Department of Physics, Humboldt-Universität zu Berlin, 10099 Berlin, Germany
SECOND-ORDER COHERENCE FUNCTION OF THE INITIAL PRODUCT STATE
As described in the main text, we initialize our atomic ensemble at t = 0 close to the product state given by Eq. (1),
|ψ0⟩ =
N ⊗
k=1
[
cos
(A
2
)
|gk⟩ − i sin
(A
2
)
|ek ⟩
]
, (S.1)
where |gk⟩ and |ek⟩ are the ground and excited state of the kth atom, and A is the Rabi pulse area. Here, we will compute the first
and second-order correlations of the symmetric lowering operator Sˆ = ∑N
k=1 σˆk, where σˆk = |gk⟩ ⟨ek| is the spin-lowering
operator of the kth atom. Since the detected mode Eˆ is proportional to Sˆ, the correlations will hold for Eˆ up to a prefactor. At
first, we define d as the imaginary part of the dipole moment,
d := i ⟨σˆ†
k − σˆk⟩ = i ⟨ψ0| σˆ†
k − σˆk |ψ0⟩ = −2 cos
(A
2
)
sin
(A
2
)
. (S.2)
Note that here, all atoms have the same dipole moment ⟨σˆk⟩ = id/2 and therefore we can omit an index k. Next, we define the
probability p that one particular atom is excited,
p := ⟨σˆ†
kσˆk⟩ = sin
(A
2
)2
. (S.3)
Since |ψ0⟩ is a product state, we make use of ⟨AˆBˆ⟩ = ⟨Aˆ⟩ ⟨Bˆ⟩ whenever Aˆ and Bˆ act on different atoms. With this and σˆk2 = 0
we find
⟨Sˆ⟩ =
N ∑
k=1
⟨σˆk⟩ = iN d
2 , (S.4a)
⟨Sˆ†Sˆ⟩ =
N ∑
k,l=1
⟨σˆ†
kσˆl⟩ =
N ∑
k,l=1
⟨σˆ†
k⟩ ⟨σˆl⟩ +
N ∑
k=1
(
⟨σˆ†
kσˆk⟩ − | ⟨σˆk⟩ |2)
= | ⟨Sˆ⟩ |2 + N
(
p − d2
4
)
=N
[
p + (N − 1) d2
4
]
N ≫1
−−−→ N
(
p + N d2
4
) (S.4b)
⟨Sˆ†Sˆ†SˆSˆ⟩ =
N ∑
k,l,m,n=1
⟨σˆ†
k σˆ †
l σˆmσˆn⟩ =
N ∑
k,l,m,n=1


d4
16 , k, l, m, n all different
p d2
4 , either k or l equals either m or n
p2, k = m ̸= l = n or k = n ̸= l = m
0, else
= N (N − 1)
[
(N − 2)(N − 3) d4
16 + 4(N − 2)p d2
4 + 2p2
]
N ≫1
−−−→ N 2
(
N 2 d4
16 + 4pN d2
4 + 2p2
)
. (S.4c)
Here, the final expressions are valid in the large-ensemble limit of N ≫ 1. In that limit, we can express the second-order
correlation function as
⟨Sˆ†Sˆ†SˆSˆ⟩ = ⟨Sˆ†Sˆ⟩2
(
2 − N 4d4
16 ⟨Sˆ†Sˆ⟩2
)
= ⟨Sˆ†Sˆ⟩2
(
2−
(
1 + 4p
N d2
)−2)
. (S.5)
arXiv:2407.12549v1 [quant-ph] 17 Jul 2024


 2
0.0 0.5 1.0 1.5
γt
0
10
P(t)/γ
N=9
0.0 0.5 1.0 1.5
γt
0.0
0.5
1.0
1.5
γt
0.00 0.04 0.08
γt
0
2500
5000
7500
P(t)/γ
N = 200
0.00 0.04 0.08
γt
0.00
0.04
0.08
γt
0.0
0.5
1.0
1.5
2.0
g(2)(t1, t2)
Figure S.1. Symmetric Dicke model predictions for N = 9 (left) and N = 200 (right) identical two-level atoms with excited state lifetime
τ = 1/γ. Top row: normalized photon flux P (t)/γ = ⟨Sˆ†(t)Sˆ(t)⟩ as a function of time. Bottom row: color plot of g(2)(t1, t2). Red (blue) colors indicate g(2) > 1 (g(2) < 1).
With the expressions for p and d, we thus find for the normalized second-order coherence function
g(2)(0, 0) = ⟨Sˆ†Sˆ†SˆSˆ⟩
⟨Sˆ†Sˆ⟩2 = 2 −
(
1+ 1
N cos2(A/2)
)−2
, (S.6)
which is Eq. (3) of the main text. Let us analyze this expression as a function of A. First note that it has a period of 2π in A.
Next, on the interval (0, 2π) the function has one maximum at A = π with g(2)(0, 0) = 2. Furthermore, for A ̸= π, the function approaches 1 as N becomes large, i.e. g(2)(0, 0) N→∞
−−−−→ 1. Thus, for a finite N ≫ 1, the function is similar to a Lorentzian with
a narrow peak at A = π, whose full-width at half-maximum (FWHM) w can be computed as follows. We set A = π ± w/2 and
have in close proximity to the maximum (i.e. for w ≪ π), g(2)(t, t) ≈ 2 − [1 + 16/(N w2)]−2. From this, we find the FWHM as
w=
√
16
√2 − 1
1
N ≈ 0.9892 × √2πN . (S.7)
TWO-TIME SECOND-ORDER CORRELATION FUNCTION IN THE DICKE MODEL
In this section, we consider the original Dicke model [1, 2]. There, a very dense ensemble of N two-level atoms with excited
state lifetime τ = 1/γ is initialized in the fully inverted state |N ⟩ = |e · · · e⟩. Upon decay, this ensemble always stays in its
symmetric Dicke states |k⟩, which can be written as [2]
|k⟩ =
√
k!
N !(N − k)! SˆN−k |N ⟩ , (S.8)


 3
where k = 0, 1, · · · , N counts the number of excitations in the ensemble and Sˆ = ∑N
k=1 σˆk is the symmetric lowering operator.
Our goal is to derive an expression for the second-order two-time correlation function G(2)(t1, t2) = ⟨Eˆ†(t1)Eˆ†(t2)Eˆ(t2)Eˆ(t1)⟩
of the field Eˆ ∝ √γSˆ, radiated by the Dicke ensemble.
For this, consider the vector of operators xˆ0, whose elements are the projection operators (xˆ0)k = |k⟩ ⟨k|. Note that the
expected value of xˆ0 are the diagonal entries of the density matrix with ρkk = ⟨k| ρˆ|k⟩ = (⟨xˆ0⟩)k. The equation of motion of
these diagonal entries reads [2]
d
dt ⟨xˆ0⟩ = γA0 ⟨xˆ0⟩ (S.9)
with the (N + 1)2 - matrix A0, whose components are given by (m, n = 0, . . . , N )
(A0)nm = −δnms2n + δn+1,ms2n+1. (S.10)
Here, sk = √k(N + 1 − k) are defined through Sˆ |k⟩ = sk |k − 1⟩ and Sˆ† |k⟩ = sk+1 |k + 1⟩. The time-dependent solution
of Eq. (S.9) reads ρkk(t) = ⟨xˆ0(t)⟩ = eA0γtρkk(0) with the initial value ρkk(0) = δk,N . Note that a numerical solution to
this matrix exponential can be found in a reasonable time, even when N exceeds 100. The off-diagonal elements are all zero,
ρk̸=n(t) = 0. The time-dependent radiated photon flux P (t) is then found by using Sˆ†Sˆ = ∑N
k=0 s2k(xˆ0)k as
P (t) = γ ⟨Sˆ†(t)Sˆ(t)⟩ = γTr [
ρˆ(t)Sˆ†Sˆ
]
=γ
N ∑
k,n=0
s2k ⟨n| ρˆ(t)(xˆ0)k |n⟩ = γ
N ∑
k=0
s2kρkk(t). (S.11)
We now consider the vector of two-time correlators ⟨Sˆ†(t1)xˆ0(t2)Sˆ(t1)⟩ with t2 > t1. Employing the quantum regression
theorem [3], we find an equation of motion for this vector of correlators from Eq. (S.9) as
d dt2
⟨Sˆ†(t1)xˆ0(t2)Sˆ(t1)⟩ = γA0 ⟨Sˆ†(t1)xˆ0(t2)Sˆ(t1)⟩ . (S.12)
The solution to this differential equation reads ⟨Sˆ†(t1)xˆ0(t2)Sˆ(t1)⟩ = eA0γ(t2−t1) ⟨Sˆ†(t1)xˆ0(t1)Sˆ(t1)⟩. From this, we finally
find the two-time second-order correlation function as
G(2)(t1, t2) = ⟨Sˆ†(t1)Sˆ†(t2)Sˆ(t2)Sˆ(t1)⟩ =
N ∑
k=0
s2k
(
⟨Sˆ†(t1)xˆ0(t2)Sˆ(t1)⟩
)
k
=
N ∑
k,n=0
s2k
(eA0γ(t2−t1))
k,n ⟨Sˆ† |n⟩ ⟨n| Sˆ⟩t1 =
N ∑
k,n=0
s2k s2n+1
(eA0γ(t2−t1))
k,n (ρ0(t1))n+1 .
(S.13)
For t2 < t1, we use the symmetry property G(2)(t1, t2) = G(2)(t2, t1). The normalized second-order coherence function is then
found by
g(2)(t1, t2) = G(2)(t1, t2)
P (t1)P (t2) . (S.14)
We show this quantity as a color plot for N = 9 and N = 200 in Fig. S.1.
[1] R. H. Dicke, Coherence in spontaneous radiation processes, Phys. Rev. 93, 99 (1954).
[2] M. Gross and S. Haroche, Superradiance: An essay on the theory of collective spontaneous emission, Phys. Rep. 93, 301 (1982).
[3] H. J. Carmichael, Statistical methods in quantum optics 1: master equations and Fokker-Planck equations, Vol. 1 (Springer Science &
Business Media, 1999).
