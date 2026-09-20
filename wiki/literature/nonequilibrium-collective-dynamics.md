# Nonequilibrium Collective Dynamics

> Sources: Richardson and Sherman, 1964; Yuzbashyan et al., 2005; Heyl et al., 2013; Marino et al., 2022
> Raw: [Richardson pairing solution](../../raw/literature/exact-eigenstates-of-the-pairing-force-hamiltonian-full-text.md); [BCS and central-spin dynamics](../../raw/literature/2005-09-09-solution-for-the-dynamics-of-the-bcs-and-central-spin-proble-full-text.md); [Ising DQPT](../../raw/literature/2013-03-28-dynamical-quantum-phase-transitions-in-the-transverse-field-full-text.md); [Collisionless dynamical phases](../../raw/literature/2022-11-01-dynamical-phase-transitions-in-the-collisionless-pre-thermal-full-text.md)
> Updated: 2026-09-20

## Papers in this route

| Paper | Year |
|---|---:|
| [Richardson1964 — Exact eigenstates of the pairing-force Hamiltonian](papers/richardson1964-45fgebgu.md) | 1964 |
| [Barankov2004 — Collective Rabi Oscillations and Solitons in a Time-Dependent BCS Pairing Problem](papers/barankov2004-svfhnszn.md) | 2004 |
| [Yuzbashyan2005 — Solution for the dynamics of the BCS and central spin problems](papers/yuzbashyan2005-7vi2mrkk.md) | 2005 |
| [Yuzbashyan2006 — Relaxation and Persistent Oscillations of the Order Parameter in Fermionic Condensates](papers/yuzbashyan2006-frcz4292.md) | 2006 |
| [Eckstein2010 — Interaction quench in the Hubbard model: Relaxation of the spectral function and the optical conductivity](papers/eckstein2010-y5n3ne3e.md) | 2010 |
| [Polkovnikov2011 — Colloquium : Nonequilibrium dynamics of closed interacting quantum systems](papers/polkovnikov2011-5re6s3c6.md) | 2011 |
| [Sciolla2011 — Dynamical transitions and quantum quenches in mean-field models](papers/sciolla2011-2n8jbrjz.md) | 2011 |
| [Heyl2013 — Dynamical Quantum Phase Transitions in the Transverse-Field Ising Model](papers/heyl2013-glanlrj2.md) | 2013 |
| [Eisert2015 — Quantum many-body systems out of equilibrium](papers/eisert2015-zuhxbjyu.md) | 2015 |
| [Yuzbashyan2015 — Quantum quench phase diagrams of an s -wave BCS-BEC condensate](papers/yuzbashyan2015-kc2s76ni.md) | 2015 |
| [Koller2016 — Dynamics of Interacting Fermions in Spin-Dependent Potentials](papers/koller2016-xhltvmea.md) | 2016 |
| [Žunkovič2018 — Dynamical Quantum Phase Transitions in Spin Chains with Long-Range Interactions: Merging Different Concepts of Nonequilibrium Criticality](papers/zunkovic2018-8zef3cj7.md) | 2018 |
| [Choi2019 — Emergent SU(2) Dynamics and Perfect Quantum Many-Body Scars](papers/choi2019-ar8ikbl8.md) | 2019 |
| [Kirton2019 — Introduction to the Dicke Model: From Equilibrium to Nonequilibrium, and Vice Versa](papers/kirton2019-gzc48ra3.md) | 2019 |
| [Scaramazza2019 — Consequences of integrability breaking in quench dynamics of pairing Hamiltonians](papers/scaramazza2019-ihdcttua.md) | 2019 |
| [Lewis-Swan2021 — Cavity-QED Quantum Simulator of Dynamical Phases of a Bardeen-Cooper-Schrieffer Superconductor](papers/lewis-swan2021-rv44b6is.md) | 2021 |
| [Marino2022 — Dynamical phase transitions in the collisionless pre-thermal states of isolated quantum systems: theory and experiments](papers/marino2022-272icr2x.md) | 2022 |
| [Li2024 — Emergent universal quench dynamics in randomly interacting spin models](papers/li2024-7r6zjnn7.md) | 2024 |

## Role in the paper

This route supplies language and diagnostics for collective sectors that persist, dephase, prethermalize, or undergo a true dynamical transition. Its central warning is that those outcomes must be operationally defined.

## Pairing dynamics

A reduced pairing Hamiltonian can be written

$$
H=\sum_j2\epsilon_jS_j^z-g\sum_{j,k}S_j^+S_k^- ,
\qquad
\Delta(t)=g\sum_j\langle S_j^-(t)\rangle.
$$

Richardson’s exact solution parameterizes eigenstates through coupled pair-energy equations. The time-dependent BCS and central-spin work turns the mean-field problem into integrable classical pseudospin dynamics. After a quench, the gap can decay, approach a constant, or oscillate persistently; isolated spectral roots distinguish those regimes.

## Dynamical-transition diagnostics

For a Loschmidt-amplitude definition, $\mathcal G(t)=\langle\psi_0|e^{-iHt}|\psi_0\rangle$ and the rate function is

$$
r(t)=-\lim_{N\to\infty}\frac1N\log|\mathcal G(t)|^2.
$$

Nonanalyticities in $r(t)$ define one class of DQPT. Order-parameter transitions and prethermal dynamical critical points are related but not identical notions. The project should reserve “transition” for an independently supported asymptotic distinction, not a finite-size transport crossover.

## See Also

- [Strategic Literature Map](organized-literature-map.md#nonequilibrium-collective-dynamics)
- [Coherence Protection Mechanisms](../concepts/coherence-protection-mechanisms.md)
- [Richardson1964](papers/richardson1964-45fgebgu.md)
- [Yuzbashyan2005](papers/yuzbashyan2005-7vi2mrkk.md)
- [Heyl2013](papers/heyl2013-glanlrj2.md)
