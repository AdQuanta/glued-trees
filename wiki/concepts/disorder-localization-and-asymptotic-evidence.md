# Disorder, Localization, and Asymptotic Evidence

> Sources: Jackson et al., 2012; Izaac et al., 2013; project specification, 2026-09-20
> Raw: [Disordered trees](../../raw/literature/2012-08-27-quantum-walks-on-trees-with-disorder-decay-diffusion-and-loc-full-text.md); [Defects and disorder](../../raw/literature/2013-10-29-continuous-time-quantum-walks-with-defects-and-disorder-full-text.md); [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## Disorder does two different things

Within a layer, disorder separates into a layer mean and a zero-mean fluctuation. The layer mean directly disorders the reduced one-dimensional channel, while the fluctuation couples its symmetric state to the vast nonsymmetric sector. For iid uniform disorder,

$$
\operatorname{Var}(\bar\epsilon_\ell)=\frac{W^2}{3n_\ell},
$$

so the mean self-averages at large layer size. In contrast, the total fluctuation coupling out of $|S_\ell\rangle$ remains order $W$ rather than vanishing with $n_\ell$. Layer averaging alone is not protection.

## Localization and competing explanations

Tree and network transport studies show that disorder can produce localized, diffusive, and extended regimes depending on graph architecture and energy. Defects can create trapped modes; long-range shortcuts can change spreading without producing monotonic transport enhancement. Therefore an improved exit signal can arise from a larger localization length, shifted resonance, altered density of states, rare high-transmission samples, or endpoint detuning. Each is a competing explanation for the proposed spectral-protection mechanism.

## What constitutes a scaling result

The desired distinction is between exponential, stretched-exponential, and power-law large-$L$ behavior. A fit must report uncertainty, fit-window sensitivity, inclusion of the largest available sizes, and comparison against competing models. The ensemble mean alone is not enough: its distribution, median, and typical value are needed to detect rare-event domination. Independent leaf-gluing realizations are required at paper level.

## Accessibility is separate

The infinite-time average is a spectral quantity. It does not establish that a usable exit probability occurs at an accessible time. If the later paper claims operational or algorithmic benefit, it must exhibit a polynomial $T(L)$ with a corresponding finite-time exit diagnostic. Otherwise the claim must stay at the level of asymptotic long-time occupation.

## See Also

- [Glued-Trees Walk and Problem Formulation](glued-trees-walk-and-problem-formulation.md)
- [Coherence Protection Mechanisms](coherence-protection-mechanisms.md)
- [Paper-Readiness Criteria](../project/paper-readiness-criteria.md)
- [Jackson2012](../literature/papers/jackson2012-dvzgdrqv.md)
- [Izaac2013](../literature/papers/izaac2013-7b8g38rk.md)
