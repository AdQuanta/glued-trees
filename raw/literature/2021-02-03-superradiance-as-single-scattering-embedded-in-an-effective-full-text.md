# Superradiance as single scattering embedded in an effective medium - Full Text

> Source: https://link.aps.org/doi/10.1103/PhysRevA.103.023702
> Collected: 2026-09-20
> Published: 2021-02-03
> Zotero parent key: 4SC89EYI
> Evidence: Zotero indexed PDF text

PHYSICAL REVIEW A 103, 023702 (2021)
Superradiance as single scattering embedded in an effective medium
P. Weiss ,1,* A. Cipris ,1 R. Kaiser ,1 I. M. Sokolov ,2,3 and W. Guerin 1 1Université Côte d’Azur, CNRS, Institut de Physique de Nice, 06560 Valbonne, France 2Department of Theoretical Physics, Peter the Great St. Petersburg Polytechnic University, 195251 St. Petersburg, Russia 3Institute for Analytical Instrumentation, Russian Academy of Sciences, 198103 St. Petersburg, Russia
(Received 10 November 2020; accepted 11 January 2021; published 3 February 2021)
We present an optical picture of linear-optics superradiance, based on a single scattering event embedded in a dispersive effective medium composed by the other atoms. This linear-dispersion theory is valid at low density and in the single-scattering regime, i.e., when the exciting field is largely detuned. The comparison with the coupled-dipole model shows a perfect agreement for the superradiant decay rate. Then we use two advantages of this approach. First we make a direct comparison with experimental data, without any free parameter, and show a good quantitative agreement. Second, we address the problem of moving atoms, which can be efficiently simulated by adding the Doppler broadening to the theory. In particular, we discuss how to recover superradiance at high temperature.
DOI: 10.1103/PhysRevA.103.023702
I. INTRODUCTION
Superradiance generally refers to the accelerated radiation rate of excited atoms due to the collective interaction of the sample with light and the vacuum reservoir. It has been originally introduced by Dicke for a collection of excited atoms in a small volume [1], and experimentally studied with large-size, low-density samples [2,3]. Although Dicke’s approach is based on collective atomic states, it is also interesting to develop an optical picture of the superradiance (or superfluorescence [4]) phenomenon, in particular to understand propagation effects associated to the size and shape of the sample. In the case of many excited atoms, one may consider superradiance as the transient form of stimulated emission [2]. More recently the subject of “single-photon superradiance” has been brought up by Scully et al. [5,6] and experimentally observed using weak continuous excitation of large-size and dilute samples [7,8]. In this linear-optics regime the picture of stimulated emission obviously cannot apply. Is it still possible, then, to use an optical picture of superradiance in that case? In this article we present such an optical picture, which is based on a single scattering event embedded in the effective medium built by the whole atomic sample. The effective medium has a complex refractive index that introduces attenuation and dispersion. In this picture, the physics of linear-optics superradiance appears to be very close to the one of optical precursors and flash effects [9–13], the only supplementary ingredient being the scattering event, which does modify the decay rate. Linear-optics superradiance is thus mainly a dispersion effect. Besides providing a nice physical description, this picture also allows us to derive a simple equation to compute the early
*Present address: Physikalisches Institut, Eberhard Karls Universität Tübingen, Tübingen, Germany.
decay of scattered light. This “linear-dispersion” (LD) theory, first introduced in [14] and recently used to simulate the excitation dynamics at the switch-on [15,16], is very efficient from the computing point of view. We can then apply it to a direct quantitative comparison with experimental data and to the problem of moving atoms [17,18]. The paper is organized as follows. In the next section we describe the LD theory of superradiance in a very simple way and benchmark it against the more commonly used coupleddipole (CD) model. In Sec. III we compare its results with experimental data from [7]. In its limit of validity, which is that multiple scattering should be negligible, the agreement is very good. Finally in Sec. IV we address the case of thermal motion and show that, in principle, superradiance can be observed with room-temperature vapors.
II. LINEAR-DISPERSION THEORY OF SUPERRADIANCE
The main physical ingredient of the LD theory is to consider the different frequency components of the field that drives the atoms. These frequency components are due to the switch-on and -off of the field. The LD theory is thus relevant to study nonstationary effects in light-atom interactions, such as the transient behavior at the switch-on [15,16] and the superradiant decay at the switch-off.
A. Simple version of the linear-dispersion theory
For pedagogical purposes, we only present here the result of the LD theory without derivation and in its simplest version, which corresponds to the case of motionless atoms and a scalar model for light. We also do not bother with numerical prefactors. A more sophisticated version, accounting for the polarization, Zeeman states, and a velocity distribution, is given in the Appendix A, along with the main ideas and approximations for its derivation. Let us start from the result and explain its meaning. The
intensity Ik′ (t ) detected in the direction k′ as a function of time
2469-9926/2021/103(2)/023702(8) 023702-1 ©2021 American Physical Society


 P. WEISS et al. PHYSICAL REVIEW A 103, 023702 (2021)
t is given by
Ik′ (t ) ∝
∫
d 3 rρ (r)
∣∣∣∣
∫∞
−∞
d ωE0 (ω )e−iωt
× exp
[
i b0(r, k′ )
2 α ̃ (ω)
]
α ̃ (ω) exp
[
i b0(r, k)
2 α ̃ (ω)
]∣∣∣∣
2
.
(1)
In this equation, ρ(r) is the atomic density distribution, E0(ω) is the Fourier transform of the incident field,
α ̃ (ω) = −1
i + 2(ω − ωat )/ 0
(2)
is the dimensionless atomic polarizability with 0 the natural linewidth, and the b0(r, k) terms denote the resonant optical thickness through a part of the cloud, from the position r
into the direction k′, and from the incident direction k to the position r. In the case of a Gaussian cloud of rms size R, and taking the incident wave vector along the z axis and putting the origin of coordinates at the center of the cloud, one can easily compute
b0(r, k′ ) = b0
2 exp
[ −r2 + (r · k′ )2
2R2
][
1 − erf
( r · k′
√2R
)] ,
b0(r, k) = b0
2 exp
[
− x2 + y2
2R2
][
1 + erf
( √z2R
)]
, (3)
where b0 = √2π ρ0σ0R is the resonant optical thickness through the center of the cloud, with ρ0 the peak atomic density and σ0 the resonant scattering cross section. The meaning of Eq. (1) is clear: each Fourier component of the initial field propagates through the cloud until the scattering position r, propagation during which it undergoes attenuation and dephasing following Beer’s law. Then it is scattered at position r with some probability and associated dephasing given by the atomic polarizability (2). Finally it propagates again through the atomic cloud until it escapes the sample. The whole process acts as a linear transfer function, which applies to the frequency components of the incident field. The temporal dependence is recovered by a Fourier transform and the intensity is computed by taking the squared modulus. Then all possible scattering positions are summed up. This equation is valid for single-scattering only, since there is only one scattering term. Note also that the average over the scattering positions is done on the intensity: the random phase associated with incoherent scattering and the associated speckle pattern are averaged out. Indeed, what is computed is formally a quantum-mechanical average, i.e., an average over the disorder configurations (see Appendix A). Still, since this model describes superradiance, as we show below, it means that superradiance is not related to the interference between light scattered by different atoms. It is actually related to the interference between the different Fourier components of the incident field scattered by the atoms and attenuated or dephased by the surrounding effective medium. It is thus mainly a dispersion effect. Of course, the complex refractive index of the effective medium can also be considered as an interference effect between light coherently scattered by all atoms.
This calculation is very similar to what is done to explain the transient effects observed in the coherently transmitted beam, the so-called optical precursors and flash effects [9–13], except for the extra scattering term. In this case, though, this approach is more natural because there is no random phase associated with any scattering. The extra scattering term introduces a quantitative difference between superradiance off-axis, as observed in [7], and superradiance of the forward scattering lobe, as studied in [5,8,19,20]. In this approach, one can understand the occurrence of a superradiant decay rate ( sup > 0) for large b0 by the spectral broadening of the transfer function induced by the larger value of b0: if the transfer function becomes broader in Fourier space, the temporal response becomes faster. This is also the intuitive picture given for the flash effect, which can also have a decay rate faster than 0 [13].
B. Benchmark against the coupled-dipole model
In Fig. 1 we compare the results of the decay rate fitted at very early time on temporal traces computed from the CD model and the linear-dispersion (LD) model [Eq. (1)], at large detuning ( = −10 0). The agreement is excellent. Note that several densities are used in the CD simulations, from ρ0λ3 = 1.5 to 25 (with an exclusion volume k0ri j > 0.5), while the density is not a parameter in the LD model. This shows that, in this range of parameters, the density does not plays any role. We also show an analytical result that can be computed from Eq. (1) using the residue theorem. For a squared pulse of duration T −1
0 , in the limit t → 0, i.e., right after the
switch-off, and under the condition b0 0/ 1, we obtain (see [14])
sup =
(
1 + b0
4
)
0. (4)
Note that for isotropic samples, this does not depend on the observing direction, and that the model only contains
50
0
2
4
6
8
10
12
14
1+b0/4
LCDD
0 10 20 30 40 b0
Γsup/ Γ0
FIG. 1. Comparison between the coupled-dipole (CD) model and the linear-dispersion (LD) theory for the superradiant decay rate sup. Also shown is the analytical result for the large-detuning limit. The detuning is = −10 0; the observation direction is θ = 45◦. The fitting range is 0 < t < 0.02 −1
0.
023702-2


 SUPERRADIANCE AS SINGLE SCATTERING EMBEDDED ... PHYSICAL REVIEW A 103, 023702 (2021)
superradiance off-axis, i.e., with a true scattering event; it does not include the forward lobe of the timed-Dicke (TD) state [5,8,19–21]. As a consequence the decay rate is different, even in the forward direction, than for the TD state. The extra α ̃ (ω) term (scattering) is responsible for a factor 2 in the superradiant enhancement factor. It emphasizes the different nature of the forward lobe, which is, in a photon picture, diffracted or refracted light by the effective medium, without any true scattering. The different superradiant decay rates between on-axis and off-axis scattering was already numerically observed in [7]. A deviation from this analytical limit can be seen for the largest b0’s. This is the first sign of the suppression of superradiance as soon as b0 0/ is not small. A systematic numerical study shows that the superradiant decay rate reaches it maximum at b0 8 / 0 and decays beyond this value. Then, for very large b0, it slowly tends toward 0, but the LD model is not valid in that regime because the actual optical thickness b( ) = b0/(1 + 4 2/ 2
0 ) is not small and thus multiple scattering is not negligible any more. A possible interpretation for the decrease of sup is that the initial detuning must be much larger than the width of the transfer function. Then the incident spectrum E0(ω) is almost constant at the scale of the transfer function and thus does not narrow the transferred spectrum, yielding the fastest dynamics. This leads to the condition sup/2, which corresponds well to b0 8 / 0. Note that another, but consistent, interpretation of the reduction of superradiance close to resonance has already been discussed in the framework of the CD model [22]. Of course, the LD theory is extremely efficient from a computing point of view. Moreover there is no limitation for the atom number or b0 (contrary to the CD model), and we can also include the Zeeman structure. It is thus possible to make a direct comparison with experimental data without any free parameter. Another possible extension is to include the effect of atomic motion, which can be done by a simple Doppler broadening of the atomic polarizability and a Doppler shift at the scattering (see Appendix A). Whereas the CD simulations with moving atoms are extremely time demanding [17,18], the LD theory allows fast computing. We address those two problems in the following.
III. COMPARISON WITH EXPERIMENTAL DATA
To perform such a comparison we can use the experimental results of Ref. [7] on off-axis superradiance [23]. For the linear-dispersion modeling, we have simulated as closely as possible the experimental switch-off profile of the laser, which has been measured independently [24]. About the multilevel aspect of the rubidium atoms used in the experiment, it actually does not change the modeling. Indeed, we suppose that all Zeeman states are equipopulated and, in addition, the total light intensity was measured without any polarization selection [25]. Under these conditions, one can show that the complete multilevel equation (A4) is equivalent to Eq. (1), where b0 is the resonant optical thickness measured in the experiment, which includes a degeneracy factor in the scattering cross section. The result of the LD theory is reported in Fig. 2 along with the data points. The decay rates are determined by exponential
Δ=-4Γ0
Δ=-5Γ0
Δ=-6Γ0
Δ=-7Γ0
Γsup/ Γ0
b0
0 20 30 40 50 60 70
0
1
2
3
4
5
6
7
8
9
FIG. 2. Ab initio comparison between the experimental data (symbols) from [7] and the linear-dispersion theory (solid lines) for the superradiant decay rate sup as a function of the resonant optical thickness b0 for different detunings. Here the fitting range starts as t > 0.1 −1
0 (to wait for the laser switch-off) until the detected light intensity decreases to 20% from its steady-state value (before the switch-off).
fits using the same fitting window for both (see caption). Except for the lowest part of the = −7 0 data set, where there is a small discrepancy that is not understood, the agreement is very good for large detunings, without any free parameter. Yet a discrepancy appears at large b0 for the lowest detuning = −4 . Other data sets at even lower detuning (not shown for clarity) are also not in agreement with the LD theory. We attribute this discrepancy to multiple scattering, which is neglected in the LD theory: as soon as the condition b( ) 1 is not fulfilled any more, deviations from the LD theory start to appear. For = −4 0, the discrepancy starts at b0 > 20, corresponding to b( ) > 0.3. We note, however, that for data at larger , the agreement seems to go beyond this limit. Interestingly, one can also notice that some of the measured and computed decay rates are larger than the prediction of Eq. (4). Using different switch-off profiles in the LD theory, we have checked that an instantaneous switch-off, which leads to Eq. (4), does not produce the fastest decay rate, which is somewhat counterintuitive. One possible explanation is that resonant photons produce longer-lived excitations [26,27]. For an initially detuned field, a large broadening (fast extinction) is thus not favorable for superradiance. This effect will be the subject of further investigations. Finally, the large-b0 limit is not visible in Fig. 2 but we have checked that the LD theory predicts a decay rate slowly reaching the single-atom one (e.g., sup 1.14 0 for = −4 0 and b0 = 200), although the experiment yields lower values due to multiple scattering [7].
IV. SUPERRADIANCE WITH THERMAL MOTION
One can easily include the effect of atomic motion in the LD theory by convoluting the atomic polarizability with the detuning distribution corresponding to the Doppler broadening [Eq. (A4)] The Doppler broadening also acts on the
023702-3


 P. WEISS et al. PHYSICAL REVIEW A 103, 023702 (2021)
10-2 10-1 100 101
1
1.5
2
2.5
Δ=-4 Γ0
Δ=-10 Γ0
Γsup/ Γ0
k0σv/Γ0
102
FIG. 3. Comparison between the coupled-dipole model (symbols) and the linear-dispersion theory (solid lines) for the superradiant decay rate sup as a function of the normalized Doppler width k0σv/ 0 (σv is the rms width of the velocity distribution), for two detunings, = −4 (blue) and = −10 (red). The parameters are N = 1500, ρ0λ3 = 2, b0 = 5.78, θ = π /2, averaged over φ and over ∼200 realizations, and the fitting range is 0 < t < 0.15 −1
0.
propagation part [Eq. (A6)] and one should also take into account the Doppler shift between the incident light and the scattered light. For the computing time, it is tremendously more efficient than solving the CD equations with moving atoms, as done in [17,18] for subradiance.
A. Benchmark against the coupled-dipole model
We use the same CD simulation method as in [17], with moving atoms. The comparison between the two models is shown in Fig. 3 for a fixed b0 and two different detunings. The agreement is good, with only a slight discrepancy in the T = 0 limit. This discrepancy was absent in Fig. 1 computed with motionless atoms. In that case we used an exclusion volume to suppress the influence of strong superradiant pairs, while we removed the exclusion volume for the case of moving atoms. These superradiant pairs (with at most = 2) contribute to a slight decrease of the superradiant decay rate in the CD model. The two models agree well in predicting a certain robustness of superradiance: the superradiant decay rate is unaffected until a Doppler broadening on the order of 0.
For 87Rb, it corresponds to T ∼ 235 mK, well above standard temperatures of cold-atom experiments. In Appendix B we show experimental data that confirms this robustness until T ∼ 11 mK. The two models also agree in their prediction of suppressed superradiance at higher temperature, with a critical temperature that clearly depends on the detuning: a larger detuning allows one to observe superradiance at larger temperature. We interpret this behavior by the reduction and suppression of superradiance when the driving field is close to resonance, as discussed in the previous sections (and in [7,22]). Here, the same effect occurs with the Doppler-broadened resonance. This raises the question of the possibility of observing superradiance at higher temperature, even at room temperature, by using very large detunings. When solving the CD
Γsup/ Γ0
Δ/Γ0
k0σv = 0.2Γ0
k0σv = 5Γ0
k0σv = 10Γ0
k0σv = 20Γ0
k0σv = 30Γ0
k0σv = 40Γ0
1+b0/4
0 50 100 150 200 250 300
1
2
3
4
5
6
7
FIG. 4. Superradiant decay rate computed from the LD theory as a function of the detuning for different values of the Doppler broadening, with b0 = 20. The decay rate is determined in the range 0 < t < 0.02 −1
0 . At large detuning k0σv, superradiance is recovered.
equations, larger detunings need finer time sampling, which increases the computation time. Detunings larger than the Doppler broadening are thus very difficult to explore with the CD model at large temperature.
B. Room-temperature superradiance
In Fig. 4 we show the superradiant decay rate computed from the LD theory as a function of the detuning for several values of the Doppler broadening, up to k0σv = 40 0, corresponding to T ≈ 400 K for Rb. Correspondingly, the detuning goes up to = 300 0. The resonant optical thickness is fixed, b0 = 20 (defined for motionless atoms). As expected, superradiance is suppressed near resonance. At very large detuning, however, superradiance is recovered. With some algebra, it is actually possible to analytically show, starting from Eq. (A4), which includes the atomic velocity distribution, that one should recover the motionless superradiant decay rate in the limit k0σv. Numerically we obtain a slight discrepancy, which is due to the fitting range (see caption): the maximum decay rate is only visible for a very short time after t = 0, beyond our numerical resolution. Note also that the decay rate is overestimated for the lowest temperatures on resonance because multiple scattering should be significant there. From these results, it seems possible to observe superradiance in the linear-optics regime using room-temperature vapor at moderate optical thickness. Since the driving field must be largely detuned, it interacts only very weakly with the atomic vapor: therefore the experimental difficulty is to collect enough scattered light (compared to spurious light).
V. CONCLUSION
We have presented a linear-dispersion model for off-axis superradiance in the linear-optics regime for disordered dilute samples. This approach is very useful from a computational point of view, as it provides a fast method of calculating the
023702-4


 SUPERRADIANCE AS SINGLE SCATTERING EMBEDDED ... PHYSICAL REVIEW A 103, 023702 (2021)
superradiant dynamics. It also gives a nice description of the physics from the point of view of light. Superradiance appears as a dispersion effect, similar to optical precursors, without involving interference between light scattered by different atoms. If one uses Eq. (1) to compute the decay at all time, one can check that after the fast superradiant part, the following of the decay tends to a single exponential of rate 0: the LD theory does not describe subradiance. This means that linear-optics subradiance cannot be understood as a dispersion effect, contrary to linear-optics superradiance. An optical description of subradiance in disordered samples is therefore still an open problem. It should rely on mechanisms not included in the LD approach, such as multiple scattering [28,29], recurrent scattering, or refractive-index-gradient trapping [30,31]. Which of these mechanisms is the dominant one probably depends on the parameters of the experiment, such as the detuning of the excitation and the density of the sample [32,33]. Note that in multiple-scattering approaches the effective medium between scattering events also plays an important role [28,29,34]. Another open problem is the extension of this model to the case of dense samples. At high density other phenomena occur, such as collective shifts and recurrent scattering [35], which are not included in the present model. However it might be possible to keep the essential ingredients of the lineardispersion theory and include the high-density effects through a renormalization of the atomic susceptibility, following the method recently presented in [36].
ACKNOWLEDGMENTS
W.G. thanks Romain Pierrat for initial help. Part of this work was performed in the framework of the European Training Network ColOpt, which is funded by the European Union (EU) Horizon 2020 program under the Marie Sklodowska-Curie action, Grant Agreement No. 721465, and of the project ANDLICA, ERC Advanced Grant No. 832219. We also acknowledge funding from the French National Research Agency (Projects PACE-IN ANR19-QUAN-003 and QuaCor ANR19-CE47-0014). P.W. received support from the Deutsche Forschungsgemeinschaft (Grant No. WE 6356/1-1). I.M.S. thanks the Ministry of Science and Higher Education of the Russian Federation for financial support (the State Program for Fundamental Research, theme code FSEG2020-0024).
APPENDIX A: MAIN STEPS FOR THE DERIVATION OF THE LINEAR-DISPERSION THEORY
The intensity Iν ( , t ) of the light polarization component ν that the atomic ensemble scatters in a unit solid angle around an arbitrary direction given by the vector R [ = (θ , φ)] is determined by the electric field second-order correlation function D(ν1Eν)2 (r1, t1; r2, t2 ) via [37]
Iν ( , t ) = c
2π
∫
Su
d2rD(E )
νν (r, t ; r, t ). (A1)
Here the integral is calculated over a spherical surface Su corresponding to a unit spherical angle and located far from the considered atomic ensemble. The center of the sphere is
assumed to be in this ensemble and c is the speed of light in vacuum. In order to theoretically describe the effect of superradiance, we have to be able to calculate the correlation function D(νEν)(r, t ; r, t ). In the general case this function is expressed in
terms of negative-frequency Eν(1−)(r, t ) and positive-frequency
Eν(1+)(r, t ) components of the Heisenberg electric field opera
tors:
D(E )
ν1 ν2 (r1, t1; r2, t2 ) = 〈E (−)
ν2 (r2, t2 )E (+)
ν1 (r1, t1 )〉. (A2)
The brackets in this expression correspond to quantummechanical statistical averaging over the density operator of the entire system under investigation. The correlation function (A2) can be calculated by the diagram technique for nonequilibrium systems (see for example [38–42]). This technique is based on a perturbation-theory expansion. The field correlation function is expanded into series over interaction between atoms and light. Each item in this expansion is represented by a diagram. Part of the diagrams can be summed up. In this paper we consider only the case of side scattering, when the mean values of the field operators are equal to zero, 〈Eν(±)(r,t )〉 = 0, in the region of the photodetector. In addition, when calculating the correlation function (A2), we assume the following typical experimental conditions: The initial states of the atomic ensemble and light are uncorrelated; the atomic ensemble is dilute, which means that the average interatomic distance is much larger than the wavelength of the resonant radiation. The exciting light is assumed to be a long pulse and the time profile of its positive frequency component can be determined by the following superposition of monochromatic waves:
E (+)
μ (r, t ) = uμ
∫∞
0
dω
2π E (ω) exp(ikr − iωt ), (A3)
where the unit vector uμ determines the polarization of the incident light. This light is weak and all nonlinear optical phenomena can be neglected. Under such assumptions we can get an expansion of the correlation function (A2) as a series over the number of events of incoherent scattering of a photon in the medium. By incoherent, in contrast to coherent forward scattering, we mean an act of scattering of a photon by an atom in which the direction of the wave vector changes. Coherent forward scattering can be taken into account at all orders by introducing the exact advanced and retarded Green’s functions of the electromagnetic field in the considered medium. They can be found analytically as solutions of the corresponding Dyson equation (see for example [41,42]). In a similar way we can sum up all diagrams responsible for the interaction of excited atoms with the vacuum reservoir and introduce “dressed” atomic Green’s functions. They also can be found analytically [41,42]. Every event of incoherent scattering leads to a delay of the secondary photon caused by the so-called dwell or Wigner time [26,27]. For this reason, to describe the process of superradiance, which takes place just after the exciting pulse is switched off, we can consider only the contribution of a single incoherent scattering event.
023702-5


 P. WEISS et al. PHYSICAL REVIEW A 103, 023702 (2021)
FIG. 5. Experimental superradiance data for = −4 0. (a) Decay curves for light scattered off axis with b0 = 35. The amplitude is normalized to 1 for the steady-state level, right before the switch-off at t = 0. The dashed line is the single-atom decay and the temperature is encoded in the color. The two horizontal dashed lines indicate the range used for fitting the decay rates. (b) Fitted decay rates as a function of b( ) for different temperatures (same color code). For clarity, statistical error bars are shown for one data set only.
Omitting all calculations, which can be found in [41,42], we reproduce here the final result for the single scattering contribution Iνs( , t ) in the light intensity Iν ( , t ). This contribution is
Is
ν( ,t) =
∫
d3r
∫ d3p
(2π h ̄ )3
c
4π h ̄2
∑
m
ρmm(p, r)
×
∣∣∣∣∣∣
∑
μ′ ,ν ′ ,m′
∫∞
0
k2dω
2π E (ω) exp(−iωt )u′ν Xνν′
×(R, r, ω′ )α(m′m)
ν′μ′ (ω − kv)Xμ′μ(r, r0, ω)uμ
∣∣2.
(A4)
This is valid even for anisotropic media when the populations of the different Zeeman sublevels are different. Here the unit vectors u′ correspond to the two possible orthogonal polarizations of scattered light; the function Xμ′μ(r, r0, ω) describes the propagation of light from the source r0 to the point r, where a single incoherent scattering event takes place. The function Xνν′ (R, r, ω′) describes the propagation of a sec
ondary photon with frequency ω′ toward the photodetector. The frequency ω′ = ω + (k′ − k) · v differs from ω due to a Doppler shift. In the typical case of isotropic media, when all Zeeman sublevels of the ground state are uniformly populated and the single atom density matrix ρmm(p, r) does not depend on the magnetic quantum number m, the function Xμ1 μ2 (r1, r2; ω)
can be calculated as follows:
Xμ1 μ2 (r1, r2; ω) = exp[−b(r1, r2, ω)/2]δμ1 μ2 , (A5)
where the “complex optical thickness” (accounting for attenuation and dephasing) of the inhomogeneous cloud between points r1 and r2 for the considered case is
b(r1, r2, ω) = 4π k′‖d j0 j‖2
3h ̄
∫ r1
r2
n(r )d s
×
∫ d3p
(2π h ̄ )3
f (p)
−i(ω − ω j j0 − k′v) + 0/2 . (A6)
Here n(r) and f (p) are the spatial and momentum distributions of atoms in the considered ensemble, ‖d j0 j‖ is the reduced matrix element of the dipole operator for the transition between the ground and excited states of total angular momentum j0 and j respectively, and 0 is the natural
linewidth. The wave vector k′ is directed along r1 − r2.
The matrix α(m′m)
νμ (ω) is a scattering amplitude of the probe photon on an atom:
α(m′m)
νμ (ω) = − ∑
n
(dν )m′m (dμ )nm
h ̄ (ω − ωnm ) + ih ̄ 0/2 . (A7)
Note that expression (A4) describes only the contribution of single incoherent scattering. It can be used for the description of superradiance when the average optical thickness of the cloud is small. Another restriction is that Eq. (A4) can be used for all directions except in the zones of backward and forward scattering. For forward scattering the main contribution comes from the coherent component of the scattered light, and for backward direction, one of the polarization components is absent for single scattering and scattering of higher order should be taken into account. Equation (A4) is also not valid for a cloud with a large aspect ratio. In such a case diffraction and refraction effects play essential roles [43–45] and the propagation function X cannot be described by Eq. (A5).
APPENDIX B: EXPERIMENTAL DATA ON SUPERRADIANCE AS A FUNCTION OF THE TEMPERATURE
In this Appendix we show some experimental data on the superradiant decay as a function of the temperature of the sample. The experimental setup and procedure are the same as in Ref. [17] devoted to the influence of atomic motion on subradiance. Here we analyze the temporal dynamics of the decay of scattered light at early time. Several decay curves are shown in Fig. 5(a) for fixed optical thickness and detuning and for temperatures between 110 μK and 11 mK, corresponding to normalized Doppler broadening k0σv/ 0 between 0.022 and 0.22. All curves exhibit a superradiant behavior, with an early decay significantly faster than the single-atom decay. There is no visible difference between the data acquired at different temperatures,
023702-6


 SUPERRADIANCE AS SINGLE SCATTERING EMBEDDED ... PHYSICAL REVIEW A 103, 023702 (2021)
which demonstrate the robustness of superradiance in this temperature range. This is confirmed in Fig. 5(b), where we show the fitted superradiant decay rate as a function of the optical thickness for the same temperatures. At the precision of the experiment and in this limited range of temperature, we do not observer any influence of the temperature. The behav
ior is the one observed in Fig. 1 for motionless atoms, i.e., an increase with the optical thickness as long as b( ) 1, and then a decrease. Note also that superradiance is more limited than in the data of Fig. 2 because the switch-off of the laser was significantly slower (∼15 ns instead of ∼3 ns).
[1] R. H. Dicke, Coherence in spontaneous radiation processes, Phys. Rev. 93, 99 (1954). [2] M. S. Feld and J. C. MacGillivray, Coherent Nonlinear Optics: Recent Advances (Springer, Berlin, 1980), pp. 7–57. [3] M. Gross and S. Haroche, Superradiance: An essay on the theory of collective spontaneous emission, Phys. Rep. 93, 301 (1982). [4] R. Bonifacio and L. A. Lugiato, Cooperative radiation processes in two-level systems: Superfluorescence, Phys. Rev. A 11, 1507 (1975). [5] M. O. Scully, E. S. Fry, C. H. Raymond Ooi, and K. Wódkiewicz, Directed Spontaneous Emission from an Extended Ensemble of N Atoms: Timing is Everything, Phys. Rev. Lett. 96, 010501 (2006). [6] M. O. Scully and A. A. Svidzinsky, The super of superradiance, Science 325, 1510 (2009). [7] M. O. Araújo, I. Kreši ́c, R. Kaiser, and W. Guerin, Superradiance in a Large Cloud of Cold Atoms in the Linear-Optics Regime, Phys. Rev. Lett. 117, 073002 (2016). [8] S. J. Roof, K. J. Kemp, M. D. Havey, and I. M. Sokolov, Observation of Single-Photon Superradiance and the Cooperative Lamb Shift in an Extended Sample of Cold Atoms, Phys. Rev. Lett. 117, 073003 (2016). [9] H. Jeong, A. M. C. Dawes, and D. J. Gauthier, Direct Observation of Optical Precursors in a Region of Anomalous Dispersion, Phys. Rev. Lett. 96, 143901 (2006). [10] J. F. Chen, S. Wang, D. Wei, M. M. T. Loy, G. K. L. Wong, and S. Du, Optical coherent transients in cold atoms: From freeinduction decay to optical precursors, Phys. Rev. A 81, 033844 (2010). [11] M. Chalony, R. Pierrat, D. Delande, and D. Wilkowski, Coherent flash of light emitted by a cold atomic cloud, Phys. Rev. A 84, 011401(R) (2011). [12] C. C. Kwong, T. Yang, M. S. Pramod, K. Pandey, D. Delande, R. Pierrat, and D. Wilkowski, Cooperative Emission of a Coherent Superflash of Light, Phys. Rev. Lett. 113, 223601 (2014). [13] C. C. Kwong, T. Yang„ D. Delande, R. Pierrat, and D. Wilkowski, Cooperative Emission of a Pulse Train in an Optically Thick Scattering Medium, Phys. Rev. Lett. 115, 223601 (2015). [14] A. S. Kuraptsev, I. Sokolov, and M. D. Havey, Angular distribution of single photon superradiance in a dilute and cold atomic ensemble, Phys. Rev. A 96, 023830 (2017). [15] W. Guerin, T. S. do Espirito Santo, P. Weiss, A. Cipris, J. Schachenmayer, R. Kaiser, and R. Bachelard, Collective MultiMode Vacuum Rabi Splitting, Phys. Rev. Lett. 123, 243401 (2019). [16] T. S. do Espirito Santo, P. Weiss, A. Cipris, R. Kaiser, W. Guerin, R. Bachelard, and J. Schachenmayer, Collective excita
tion dynamics of a cold-atom cloud, Phys. Rev. A 101, 013617 (2020). [17] P. Weiss, A. Cipris, M. O. Araújo, R. Kaiser, and W. Guerin, Robustness of Dicke subradiance against thermal decoherence, Phys. Rev. A 100, 033833 (2019). [18] A. S. Kuraptsev and I. M. Sokolov, Influence of atomic motion on the collective effects in dense and cold atomic ensembles, Phys. Rev. A 101, 033602 (2020). [19] A. A. Svidzinsky, J.-T. Chang, and M. O. Scully, Dynamical Evolution of Correlated Spontaneous Emission of a Single Photon from a Uniformly Excited Cloud of N Atoms, Phys. Rev. Lett. 100, 160504 (2008). [20] Ph. W. Courteille, S. Bux, E. Lucioni, K. Lauber, T. Bienaimé, R. Kaiser, and N. Piovella, Modification of radiation pressure due to cooperative scattering of light, Eur. Phys. J. D 58, 69 (2010). [21] S. L. Bromley, B. Zhu, M. Bishof, X. Zhang, T. Bothwell, J. Schachenmayer, T. L. Nicholson, R. Kaiser, S. F. Yelin, M. D. Lukin, A. M. Rey, and J. Ye, Collective atomic scattering and motional effects in a dense coherent medium, Nat. Commun. 7, 11039 (2016). [22] W. Guerin and R. Kaiser, Population of collective modes in light scattering by many atoms, Phys. Rev. A 95, 053865 (2017). [23] Note that in [7], the decay rates were slightly underestimated by the fact that a portion of the detected scattered light was coming from a hot-vapor background. We have refined the analysis to remove this systematic effect in the decay rates reported in Fig. 2. [24] Since the pulse profile is different, a direct comparison with the results of the previous section is not possible. [25] There might be some spurious polarization selection introduced by the optical elements between the atoms and the detector but we suppose here that this is negligible. [26] A. Lagendijk and B. A. van Tiggelen, Resonant multiple scattering of light, Phys. Rep. 270, 143 (1996). [27] R. Bourgain, J. Pellegrino, S. Jennewein, Y. R. P. Sortais, and A. Browaeys, Direct measurement of the Wigner time delay for the scattering of light by a single atom, Opt. Lett. 38, 1963 (2013). [28] G. Labeyrie, E. Vaujour, C. A. Müller, D. Delande, C. Miniatura, D. Wilkowski, and R. Kaiser, Slow Diffusion of Light in a Cold Atomic Cloud, Phys. Rev. Lett. 91, 223904 (2003). [29] P. Weiss, M. O. Araújo, R. Kaiser, and W. Guerin, Subradiance and radiation trapping in cold atoms, New. J. Phys. 20, 063024 (2018). [30] N. J. Schilder, C. Sauvan, J.-P. Hugonin, S. Jennewein, Y. R. P. Sortais, A. Browaeys, and J.-J. Greffet, Role of polaritonic modes on light scattering from a dense cloud of atoms, Phys. Rev. A 93, 063835 (2016).
023702-7


 P. WEISS et al. PHYSICAL REVIEW A 103, 023702 (2021)
[31] F. Cottier, R. Kaiser, and R. Bachelard, Rode of disorder in super- and subradiance of cold atomic clouds, Phys. Rev. A 98, 013622 (2018). [32] Y. A. Fofanov, I. M. Sokolov, R. Kaiser, and W. Guerin, Subradiance in dilute atomic ensembles excited by nonresonant radiation, arXiv:2012.10659. [33] A. Cipris, R. Bachelard, R. Kaiser, and W. Guerin, van der Waals dephasing for Dicke subradiance in cold atomic clouds, arXiv:2012.06248. [34] G. Labeyrie, C. Miniatura, C. A. Müller, O. Sigwarth, D. Delande, and R. Kaiser, Hanle Effect in Coherent Backscattering, Phys. Rev. Lett. 89, 163901 (2002). [35] J. Javanainen and J. Ruostekoski, Light propagation beyond the mean-field theory of standard optics, Opt. Express 24, 993 (2016). [36] F. Andreoli, M. J. Gullans, A. A. High, A. Browaeys, and D. E. Chang, The maximum refractive index of an atomic medium, arXiv:2006.01680. [37] R. J. Glauber, Optical coherence and photon statistics, in Quantum Optics and Electronics, edited by C. de Witt, A. Blandin, and C. Cohen-Tannoudji (Gordon & Breach, New York, 1965), pp. 65–185.
[38] E. M. Lifshitz and L. P. Pitaevskii, Course of Theoretical Physics: Physical Kinetics (Pergamon, Oxford, 1981).
[39] O. V. Konstantinov and V. I. Perel’, A diagram technique for evaluating transport quantities, Zh. Eksp. Teor. Fiz. 39, 197 (1961) [Sov. Phys. JETP 12, 142 (1961)]. [40] L. V. Keldysh, Diagram technique for nonequilibrium processes, Zh. Eksp. Teor. Fiz. 47, 1515 (1965) [Sov. Phys. JETP 20, 1018 (1965)]. [41] V. M. Datsyuk and I. M. Sokolov, Coherent backscattering under conditions of pulsed radiation trapping, JETP 102, 724 (2006). [42] D. V. Kupriyanov, I. M. Sokolov, and M. D. Havey, Mesoscopic coherence in light scattering from cold, optically dense, and disordered atomic systems, Phys. Rep. 671, 1 (2017). [43] S. Roof, K. Kemp, M. D. Havey, I. M. Sokolov, and D. V. Kupriyanov, Microscopic lensing by a dense, cold atomic sample, Opt. Lett. 40, 1137 (2015). [44] R. T. Sutherland and F. Robicheaux, Coherent forward broadening in cold atom clouds, Phys. Rev. A 93, 023407 (2016). [45] R. Saint-Jalm, M. Aidelsburger, J. L. Ville, L. Corman, Z. Hadzibabic, D. Delande, S. Nascimbène, N. Cherroret, J. Dalibard, and J. Beugnon, Resonant-light diffusion in a disordered atomic layer, Phys. Rev. A 97, 061801(R) (2018).
023702-8
