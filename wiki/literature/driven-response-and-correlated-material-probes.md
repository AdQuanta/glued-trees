# Driven Response and Correlated-Material Probes

> Sources: Rudner and Lindner, 2020; Wackerl et al., 2020; Eckstein and Kollar, 2008; Mukamel, 2004
> Raw: [Floquet topological systems](../../raw/literature/2020-05-04-band-structure-engineering-and-non-equilibrium-dynamics-in-f-full-text.md); [Floquet-Drude conductivity](../../raw/literature/2020-05-26-floquet-drude-conductivity-full-text.md); [Time-resolved spectroscopy](../../raw/literature/2008-11-25-theory-of-time-resolved-optical-spectroscopy-on-correlated-e-full-text.md); [Nonlinear spectroscopy methods](../../raw/literature/2004-04-01-many-body-approaches-for-simulating-coherent-nonlinear-spect-full-text.md)
> Updated: 2026-09-20

## Papers in this route

| Paper | Year |
|---|---:|
| [Inagaki2000 — Many-body theory of pump-probe spectra for highly excited semiconductors](papers/inagaki2000-55epgt7v.md) | 2000 |
| [Mukamel2004 — Many-Body Approaches for Simulating Coherent Nonlinear Spectroscopies of Electronic and Vibrational Excitons](papers/mukamel2004-42yx2izq.md) | 2004 |
| [Eckstein2008 — Theory of time-resolved optical spectroscopy on correlated electron systems](papers/eckstein2008-5hvv7wqb.md) | 2008 |
| [Koch2009 — Pump-Probe Spectroscopy of Two-Body Correlations in Ultracold Gases](papers/koch2009-yt3zu32d.md) | 2009 |
| [Giannetti2016 — New perspectives in the ultrafast spectroscopy of many-body excitations in correlated materials](papers/giannetti2016-mmupante.md) | 2016 |
| [Giannetti2016 — Ultrafast optical spectroscopy of strongly correlated materials and high-temperature superconductors: a non-equilibrium approach](papers/giannetti2016-rn3b4vft.md) | 2016 |
| [Chang2019 — Many-body theory of optical absorption in doped two-dimensional semiconductors](papers/chang2019-uplcy5ln.md) | 2019 |
| [Rudner2020 — Band structure engineering and non-equilibrium dynamics in Floquet topological insulators](papers/rudner2020-dxfkqu3t.md) | 2020 |
| [Wackerl2020 — Floquet-Drude conductivity](papers/wackerl2020-q5c8cddv.md) | 2020 |
| [Sloan2024 — Optical Properties of Dispersive Time-Dependent Materials](papers/sloan2024-a2zjlm5i.md) | 2024 |

## Role in the paper

These papers are primarily a guide to measurement logic: a response function is a two-time or multi-time object tied to a probe protocol, not a direct photograph of an instantaneous material property.

## Floquet and two-time mathematics

For a periodic Hamiltonian $H(t+T)=H(t)$, Floquet states satisfy

$$
\bigl[H(t)-i\partial_t\bigr]|u_\alpha(t)\rangle
=\varepsilon_\alpha|u_\alpha(t)\rangle,
\qquad |u_\alpha(t+T)\rangle=|u_\alpha(t)\rangle.
$$

The quasienergy $\varepsilon_\alpha$ alone does not determine a measured conductivity: occupations, micromotion, disorder scattering, and the weak-probe protocol enter the response. In time-resolved spectroscopy, $\sigma(t,t')$ depends independently on probe and observation times; a finite pulse mixes temporal and spectral resolution.

## Transferable lesson

The glued-tree project is static, but it needs the same discipline: define preparation, observable, averaging, and time window before interpreting a curve as protection. Multidimensional spectroscopy work offers an additional model for separating observables sensitive to different correlation functions rather than relying on a single aggregate signal.

## See Also

- [Strategic Literature Map](organized-literature-map.md#driven-response-and-correlated-material-probes)
- [Experimental Models and Observables](../concepts/experimental-models-and-observables.md)
- [Rudner2020](papers/rudner2020-dxfkqu3t.md)
- [Wackerl2020](papers/wackerl2020-q5c8cddv.md)
- [Eckstein2008](papers/eckstein2008-5hvv7wqb.md)
