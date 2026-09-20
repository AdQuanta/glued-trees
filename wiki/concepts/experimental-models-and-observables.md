# Experimental Models and Observables

> Sources: Shi et al., 2020; Qu et al., 2022; Davis et al., 2023; project specification, 2026-09-20
> Raw: [Photonic glued trees](../../raw/literature/2020-06-20-quantum-fast-hitting-on-glued-trees-mapped-on-a-photonic-chi-full-text.md); [Irregular-graph equivalence experiment](../../raw/literature/2022-06-27-experimental-investigation-of-equivalent-laplacian-and-adjac-full-text.md); [Dipolar-spin noise spectroscopy](../../raw/literature/probing-many-body-dynamics-in-a-two-dimensional-dipolar-spin-full-text.md); [Project snapshot](../../raw/project/2026-09-20-project-snapshot.md)
> Updated: 2026-09-20

## Reduced models are useful but have a boundary

The photonic glued-tree experiment realizes the column-reduced chain in a waveguide array. That demonstrates coherent transport associated with the symmetry reduction, but it does not instantiate the exponentially large random oracle graph. Similarly, irregular-graph quantum-walk experiments can demonstrate state-dependent adjacency–Laplacian equivalence without proving that the equivalence survives arbitrary initial states, degree patterns, or disorder.

## What should be measured

The project needs an observable stack rather than one headline curve: infinite-time exit occupation, a finite-time windowed exit signal, symmetric-manifold occupation, intralayer coherence, relevant transverse spectral separation, and distributional disorder statistics. If an experimental analogue is pursued, the preparation map and readout map must be specified: which graph state represents $|\mathrm{IN}\rangle$, which ports represent the exit, how disorder is realized, and how the target quantities are reconstructed.

## Hamiltonian identification

Waveguide propagation, coupled oscillators, cavity modes, and spin ensembles each implement an effective Hamiltonian under a convention. The adjacency and Laplacian forms can match only under stated conditions. A credible implementation must report its effective couplings, onsite terms, unwanted loss or drive, calibration uncertainty, and whether the target result is a full graph or a symmetry-reduced analogue.

## See Also

- [Symbols and Conventions](symbols-and-conventions.md)
- [Glued-Trees Walk and Problem Formulation](glued-trees-walk-and-problem-formulation.md)
- [Shi2020](../literature/papers/shi2020-issp8hgc.md)
- [Qu2022](../literature/papers/qu2022-fkckq2a4.md)
- [Davis2023](../literature/papers/davis2023-jm85xb6g.md)
