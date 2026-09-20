# Experimental Implementations and Measurement Platforms

> Sources: Shi et al., 2020; Qu et al., 2022; Putz et al., 2014; Davis et al., 2023
> Raw: [Photonic glued trees](../../raw/literature/2020-06-20-quantum-fast-hitting-on-glued-trees-mapped-on-a-photonic-chi-full-text.md); [Irregular-graph experiment](../../raw/literature/2022-06-27-experimental-investigation-of-equivalent-laplacian-and-adjac-full-text.md); [Cavity spin-ensemble protection](../../raw/literature/protecting-a-spin-ensemble-against-decoherence-in-the-strong-full-text.md); [Dipolar-spin spectroscopy](../../raw/literature/probing-many-body-dynamics-in-a-two-dimensional-dipolar-spin-full-text.md)
> Updated: 2026-09-20

## Papers in this route

| Paper | Year |
|---|---:|
| [Allred2002 — High-Sensitivity Atomic Magnetometer Unaffected by Spin-Exchange Relaxation](papers/allred2002-dzbhrhdb.md) | 2002 |
| [Wei2005 — Realization of a Decoherence-Free Subspace Using Multiple Quantum Coherences](papers/wei2005-xx38angp.md) | 2005 |
| [Putz2014 — Protecting a spin ensemble against decoherence in the strong-coupling regime of cavity QED](papers/putz2014-jkuahfsn.md) | 2014 |
| [Zhang2017 — Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator](papers/zhang2017-aguew439.md) | 2017 |
| [Knüppel2019 — Nonlinear optics in the fractional quantum Hall regime](papers/knuppel2019-fxzgcbh3.md) | 2019 |
| [Smale2019 — Observation of a transition between dynamical phases in a quantum degenerate Fermi gas](papers/smale2019-mrn2jnmh.md) | 2019 |
| [Wang2019 — Evidence of high-temperature exciton condensation in two-dimensional atomic double layers](papers/wang2019-zuathaag.md) | 2019 |
| [Regan2020 — Mott and generalized Wigner crystal states in WSe2/WS2 moiré superlattices](papers/regan2020-ihu4vmja.md) | 2020 |
| [Shi2020 — Quantum fast hitting on glued trees mapped on a photonic chip](papers/shi2020-issp8hgc.md) | 2020 |
| [Shimazaki2020 — Strongly correlated electrons and hybrid excitons in a moiré heterostructure](papers/shimazaki2020-zqdtuhmy.md) | 2020 |
| [Tang2020 — Simulation of Hubbard model physics in WSe2/WS2 moiré superlattices](papers/tang2020-dennxzlr.md) | 2020 |
| [Xu2020 — Correlated insulating states at fractional fillings of moiré superlattices](papers/xu2020-d6weqxcx.md) | 2020 |
| [Shimazaki2021 — Optical Signatures of Periodic Charge Distribution in a Mott-like Correlated Insulator State](papers/shimazaki2021-z7y2gnyi.md) | 2021 |
| [Ballantine2022 — Optical magnetism and wavefront control by arrays of strontium atoms](papers/ballantine2022-77bmximb.md) | 2022 |
| [Ding2022 — Enhanced metrology at the critical point of a many-body Rydberg atomic system](papers/ding2022-gmrn2qp7.md) | 2022 |
| [Qu2022 — Experimental investigation of equivalent Laplacian and adjacency quantum walks on irregular graphs](papers/qu2022-fkckq2a4.md) | 2022 |
| [Davis2023 — Probing many-body dynamics in a two-dimensional dipolar spin ensemble](papers/davis2023-jm85xb6g.md) | 2023 |
| [Lei2023 — Many-body cavity quantum electrodynamics with driven inhomogeneous emitters](papers/lei2023-7lb2e9aq.md) | 2023 |
| [Bach2024 — Emergence of second-order coherence in superfluorescence](papers/bach2024-644yrmsn.md) | 2024 |

## Role in the paper

This route turns an abstract Hamiltonian into a measurement plan. It also marks the boundary between an experiment implementing the full graph and one implementing a symmetry-reduced effective model.

## Propagation as Schrödinger evolution

In a waveguide array, longitudinal distance $z$ plays the role of time and coupled-mode amplitudes obey

$$
i\frac{d}{dz}\mathbf a(z)=H_{\rm eff}\mathbf a(z).
$$

Shi et al. encode the glued-tree column Hamiltonian in this form. It is a faithful realization of the reduced chain and its interference pattern, but it does not carry the full exponentially large black-box structure. That difference must be stated in any proposed experimental framing.

## Observable design

The experimental papers show complementary readouts: output-port intensities for photonic transport, state-dependent evolution for adjacency–Laplacian equivalence, cavity transmission for bright/dark polaritons, and probe-spin coherence for interacting baths. For the project, the minimum stack is exit occupation, finite-time accessibility, symmetric-manifold occupation, intralayer coherence, and transverse spectrum. A single transmission maximum cannot identify protection.

## Calibration boundary

An implementation needs an explicit map from hardware controls to $J_{\rm GT}$, $J_{\rm LR}$, disorder $W$, biases $b_\ell$, and the selected Hamiltonian convention. Loss, drive, and preparation error belong in the model only if their effects are measured or bounded; otherwise the result is not a test of the closed static CTQW specified here.

## See Also

- [Strategic Literature Map](organized-literature-map.md#experimental-implementations-and-measurement-platforms)
- [Experimental Models and Observables](../concepts/experimental-models-and-observables.md)
- [Shi2020](papers/shi2020-issp8hgc.md)
- [Qu2022](papers/qu2022-fkckq2a4.md)
- [Putz2014](papers/putz2014-jkuahfsn.md)
