# Colloquium : Protecting quantum information against environmental noise - Full Text

> Source: https://link.aps.org/doi/10.1103/RevModPhys.88.041001
> Collected: 2026-09-20
> Published: 2016-10-10
> Zotero parent key: WAG7DUIW
> Evidence: Publisher or author-preprint PDF

REVIEWS OF MODERN PHYSICS, VOLUME 88, OCTOBER–DECEMBER 2016

Colloquium: Protecting quantum information against
environmental noise
         Dieter Suter
         Fakultät Physik, TU Dortmund, 44221 Dortmund, Germany


         Gonzalo A. Álvarez
         Weizmann Institute of Science, 76100 Rehovot, Israel,
         and Centro Atómico Bariloche, CNEA, CONICET, 8400 S. C. de Bariloche, Argentina
         (published 10 October 2016)

         Quantum technologies represent a rapidly evolving field in which the specific properties of quantum
         mechanical systems are exploited to enhance the performance of various applications such as sensing,
         transmission, and processing of information. Such devices can be useful only if the quantum systems
         also interact with their environment. However, the interactions with the environment can degrade the
         specific quantum properties of these systems, such as coherence and entanglement. It is therefore
         essential that the interaction between a quantum system and the environment is controlled in such a
         way that the unwanted effects of the environment are suppressed while the necessary interactions are
         retained. This Colloquium gives an overview, aimed at newcomers to this field, of some of the
         challenges that need to be overcome to achieve this goal. A number of techniques have been
         developed for this purpose in different areas of physics including magnetic resonance, optics, and
         quantum information. They include the application of static or time-dependent fields to the quantum
         system, which are designed to average the effect of the environmental interactions to zero. Quantum
         error correction schemes were developed to detect and eliminate certain errors that occur during the
         storage and processing of quantum information. In many physical systems, it is useful to use specific
         quantum states that are intrinsically less susceptible to environmental noise for encoding the quantum
         information. The dominant contribution to the loss of information is pure dephasing, i.e., through the
         loss of coherence in quantum mechanical superposition states. Accordingly, most schemes for
         reducing loss of information focus on dephasing processes. This is also the focus of this Colloquium.

         DOI: 10.1103/RevModPhys.88.041001



CONTENTS                                                                      B. Dynamical decoupling                                      12
                                                                              C. Imperfect and robust rotations                            12
I. Introduction                                                    1          D. Robustness of decoupling sequences                        13
      A. Quantum information                                       1          E. Quantum error correction                                  15
      B. Environment, dephasing, and errors                        2     VI. Protecting Unitary Evolutions                                 16
      C. The threshold theorem                                     2          A. Combining decoupling with other control operations        16
      D. A counterstrategy                                         3          B. Examples                                                  17
      E. Historical background                                     3     VII. Environmental Noise and Sensing                              18
II. Characterization of Quantum States                             4          A. Sensing                                                   18
      A. Pure and mixed states                                     4          B. Examples                                                  19
      B. Errors and fidelity                                       5     VIII. Conclusions and Outlook                                     19
III. Dephasing and Rephasing in a Static Environment               5     Acknowledgments                                                   20
      A. Dephasing models                                          5     References                                                        20
           1. Classical environment                                5
           2. Quantum mechanical environment                       6
           3. Symmetry of dephasing interactions                   7     I. INTRODUCTION
      B. Rephasing: Echoes                                         7
      C. Protected subspaces and subsystems                        7     A. Quantum information
           1. Clock transitions                                    7
           2. Decoherence-free subspaces and noiseless                     Since the time of its foundation, quantum mechanics has
              subsystems                                          8      been understood as one of the basic pillars on which physics is
IV. Fluctuating Environments                                      8      built. Many fields of research are based on quantum mechani-
      A. Classical environments                                   8      cal laws such as Heisenberg’s uncertainty relation and
      B. Quantum mechanical environments                          9      Schrödinger’s equation of motion. However, until a few
      C. Interference of fluctuations with refocusing             9      decades ago these fundamental laws were rarely connected
V. Active Protection Against Noise                               11      to directly observable phenomena, and even today, direct
      A. The Carr-Purcell solution                               11      observations of “quantum phenomena” are still considered

0034-6861=2016=88(4)=041001(23)                                   041001-1                                    © 2016 American Physical Society
                                Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


striking. Nevertheless, a scientific community has recently                ideal (targeted) result. The main causes that lead to deviations
developed, whose members concentrate on designing and                      between the actual and the targeted result are as follows:
controlling physical systems whose behavior directly follows                   • The isolation between the quantum mechanical system
Schrödinger’s equation. Accordingly, the state and the evo-                      and the environment is not perfect. The spurious inter-
lution of these systems have to be described by the laws of                      actions with the environment cause unwanted transitions
quantum mechanics. Of particular interest is the possibility of                  (relaxation) and decay of the phase coherence (dephas-
storing information in these systems in the form of quantum                      ing or decoherence) (Zurek, 2003).
mechanical superposition states, and in controlling its evolu-                 • The control fields are not perfect, thus generating
tion in such a way that the information stored in the system                     imperfect gate operations (Levitt, 1986; Souza, Álvarez,
evolves along a specific path in Hilbert space. This general                     and Suter, 2012c).
goal has motivated many researchers with different back-                       • The quantum system itself differs from the idealized
grounds and resulted in a new field of research commonly                         model system considered in the design of the informa-
known as quantum information. Applications of quantum                            tion processing protocol. This includes coupling con-
information include quantum computing, the simulation of                         stants that are slightly different from the ideal ones and
other quantum systems, or quantum sensing, where quantum                         quantum states that are not included in the computational
systems serve as small but sensitive probes of the environ-                      Hilbert space (De Chiara et al., 2005; Hauke et al., 2012;
ment, e.g., for measuring electric or magnetic fields, temper-                   Stolze et al., 2014).
ature, or pressure.                                                        The evolution of quantum mechanical systems is typically
   All these techniques use some set of simple quantum                     characterized by the Schrödinger equation—to some degree
systems, typically two-level systems referred to as qubits, to             the successor of Newton’s second law. Since it is a linear
store the information in a superposition of the available basis            equation, all possible solutions can be written as linear
states. In the simplest case, the system consists of a single qubit,       combinations of a basis set. This is also the basis of quantum
but in the more general case, an array of qubits is used, which is         information, where the information is stored in the coefficients
often called “quantum register.” This register is the main system          of a superposition state (Stolze and Suter, 2008; Nielsen and
of interest: it contains the information that is processed and that        Chuang, 2010). The description of the system in terms of
requires protection against unwanted modifications.                        superposition states is exact only for isolated systems. Every
   Information stored and processed in a quantum system                    real system, however, exists in an environment that consists of
undergoes different life cycles. The simplest and most com-                the rest of the Universe. The notion of an isolated system is
monly used model is the network model represented in                       convenient, but only an approximation whose validity must be
Fig. 1. Here the information is initially written into the quantum         verified in every specific situation. If the isolation is not
system by initializing it into a well-defined state. The infor-            perfect (i.e., always), there is an interaction between the
mation is then subjected to a series of unitary transformations            quantum system and its environment, and this interaction
defined by a recipe (algorithm) designed to implement a sensor             modifies the evolution of the system.
or an information processor. In the simplest case, it implements              We can distinguish between two types of interactions:
a quantum memory, where the sequence of control operations                 external control fields (usually electric and/or magnetic
is equal to the unit operation. Finally, the result is read out, i.e.,     fields) drive the evolution of the quantum system, particularly
the quantum state is converted into classical information by               to generate unitary operations. Uncontrolled interactions
performing a projective measurement.                                       between system and environment, such as thermal motion
                                                                           of charge carriers or stray magnetic fields, lead to deviations
                                                                           between the targeted and the actual evolution and to a loss
B. Environment, dephasing, and errors                                      of coherence in the system. As discussed in Sec. II.A, this
                                                                           corresponds to a transition from pure to mixed states and an
   The main challenge for implementing this scheme is that
                                                                           associated increase in the entropy of the system, in close
quantum systems are too sensitive to perturbations, which
                                                                           analogy to the second law of thermodynamics. These uncon-
affect the evolution of the system in such a way that it deviates          trolled degrees of freedom can include quantum mechanical
from the wanted evolution (Peres, 1984; Goussev et al., 2012;              as well as classical degrees of freedom.
Hauke et al., 2012). As a consequence, the implementation                     Control operations are unitary transformations that change
always generates a result that differs to some degree from the             the state of the quantum system. They form the elementary
                                                                           operations for manipulating the quantum information. An
                                                                           experimental implementation must generate operations that
                                                                           are as close as possible to the operations that the processing
                                                                           protocol requires. Deviations between the targeted and actual
                                                                           fields cause additional errors in the evolution of the system.

                                                                           C. The threshold theorem

FIG. 1. Initialization, processing, and detection (readout) of                Any such system must maintain the integrity of the
quantum information in the network model. The processing of                information until the relevant tasks (e.g., sensing or process-
information is performed by unitary transformations. Their                 ing) and the readout have completed. While this is the case for
sequence is determined by the algorithm.                                   classical as well as for quantum information, the challenge is

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016              041001-2
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


significantly larger for quantum information than for classical                 subspaces (DFS) (Lidar, Chuang, and Whaley, 1998);
information, essentially for two reasons: (i) quantum infor-                    see Sec. III.C.
mation is more fragile, since even infinitesimal perturbations                • Use active schemes for decoupling the system from
can change it (Peres, 1984; Jalabert and Pastawski, 2001;                       the environment, such as dynamical decoupling (DD)
Goussev et al., 2012); and (ii) the no-cloning theorem (Dieks,                  (Viola, Knill, and Lloyd, 1999; Zanardi, 1999); see
1982; Wootters and Zurek, 1982), which states that unknown                      Sec. V.B.
quantum information cannot be duplicated, implies that                        • Use robust control operations, which are designed such
classical error correction schemes, which typically use dupli-                  that errors in experimental parameters tend to cancel
cation of information, cannot be used. The rate at which                        rather than amplify. A typical example for this approach
the information decays becomes even faster as the number                        is the use of composite pulses in nuclear magnetic
of degrees of freedom of the quantum system increases                           resonance (NMR) (Levitt, 1986); see Sec. V.C.
(Pastawski et al., 2000; Krojanski and Suter, 2004; Cho et al.,               • Use error correction schemes (Shor, 1995; Chuang and
2006; Sánchez, Pastawski, and Levstein, 2007; Álvarez and                       Yamamoto, 1996; Laflamme et al., 1996; Steane, 1996);
Suter, 2010). These known facts appeared to prevent the                         see Sec. V.E.
implementation of quantum information processing (QIP) on                 The combination of these techniques has allowed a number of
a scale that could make it useful until methods for quantum               groups to extend the coherence times of different quantum
error correction (QEC) became available (Shor, 1995; Chuang               systems by many orders of magnitude, in some cases to times
and Yamamoto, 1996; Laflamme et al., 1996; Steane, 1996).                 as long as several hours (Zhong et al., 2015). It appears likely
QEC techniques require a significant overhead in terms of                 that any useful implementation of a quantum computer will
additional (ancilla) qubits, as well as in terms of computa-              require the implementation of all of these principles (and
tional steps. It therefore remained unclear if the additional             more) into its design. Sections III, IV, V, and VI contain more
(imperfect) gate operations would result in execution times               details on these approaches.
that scale qualitatively worse than without QEC. Such an                     All these countermeasures contribute to the implementation
algorithm would no longer have any advantage over classical               of quantum information devices. However, they also add
algorithms. This question was finally resolved by the thresh-             different types and different amounts of overhead to any
old theorem (Knill, Laflamme, and Zurek, 1998; Preskill,                  quantum device that uses them. The overhead may consist of
1998), which essentially states that                                      additional qubits (particularly in QEC) or additional controls
                                                                          or gate operations (particularly in DD, but also in QEC). Since
     An arbitrarily long quantum computation can be                       these additional gates also are faulty (to some degree), it is of
     executed reliably, provided that the noise is weaker                 utmost importance to keep their precision as high as possible.
     than a certain critical value, the accuracy threshold.               If their precision is not high enough, applying a large number
                                                                          of these operations can result in destruction of the information.
   The main significance of this theorem is that reliable                 Furthermore, since they are designed to decouple the system
quantum information is possible. However, reaching the                    from its environment, they also eliminate the effect of the
required threshold for the error per computational step is                control fields that should drive the evolution of the system.
very challenging. The precise values depend on various                    The first issue can be resolved by designing the decoupling
parameters, in particular, on the error correction scheme.                sequences in a robust manner, such that their performance
Under optimal conditions, it is of the order of 10−2 –10−4                remains very close to that of the ideal sequence, even if the
(Lidar and Brun, 2013; Terhal, 2015). Reaching this degree of             control fields deviate from the ideal ones (see Sec. V.C). To
precision is hard in all physical implementations of QIP and              resolve the second issue, the gate operations must be adapted
requires a range of protection schemes (Souza et al., 2015). In           to take the effect of the DD control operations into account
the following, we summarize some of the available options.                (see Sec. VI).

D. A counterstrategy                                                      E. Historical background

   While one can (and should) try to minimize errors, both                   The development of protection schemes for quantum states
from experimental imperfections and from environmental                    started well before the field of quantum information was
noise, it is important to realize that there are technical,               established. Perhaps the main pioneering work was the
financial, and fundamental limits to the precision that can               discovery of the spin echo by Hahn (1950). In its original
be achieved. It is not possible to shield gravitational inter-            form, an ensemble of nuclear spins loses its phase coherence
actions between the system and the environment, or the                    as it undergoes Larmor precession in an inhomogeneous field.
quantum fluctuations in the apparatus that drives the control             The coherence can be regenerated by a suitable refocusing
operations and reads out the result. It is therefore essential not        pulse, which eliminates the dephasing and brings back a
only to minimize the environmental noise, but also to mitigate            macroscopic signal—the spin echo. Closely related echo
the effects that it has on the system. Several options have               phenomena, such as the photon echo (Kurnit, Abella, and
been explored for this secondary line of defense. The most                Hartmann, 1964), were later observed in many different fields.
important ones are as follows:                                            In many cases, the refocusing can be understood as an
   • Store the information in those subspaces of Hilbert space            evolution backward in time. These refocusing effects occur
     that are least affected by the interaction between the               only under very specific conditions: it must be possible to
     system and its environment, such as in decoherence-free              completely invert the Hamiltonian, which may be challenging

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016             041001-3
                                  Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


in systems with many degrees of freedom. A pioneering                          system state vectors of wave functions appears much
example was demonstrated in nuclear spin systems where the                     more natural. Nevertheless, even there, data are obtained by
Hamiltonian is dominated by magnetic-dipole interactions                       repeatedly preparing the same experiment in a given initial
between equivalent spins (Rhim, Pines, and Waugh, 1970,                        state, applying the required operations to it and performing
1971). This example was compared to a “Loschmidt daemon,”                      some measurement on it. This is a direct consequence of the
which reverses the time evolution (Loschmidt, 1876;                            probabilistic nature of processes occurring at the quantum
Boltzmann, 1877). The Loschmidt echo was defined as a                          level: The complete information about the state of the system
general measure of the efficiency of a time-reversal pro-                      is not sufficient for predicting the outcome of a measurement.
cedure, which is in general imperfect (Peres, 1984; Jalabert                   The actual results are then obtained as averages over many
and Pastawski, 2001; Goussev et al., 2012).                                    repetitions of the same experiment.
   Formation of an echo generally requires that the evolution                     In most cases, measurements therefore work with ensem-
of the system before and after the refocusing pulse is the same                bles, averaging either over many systems or over repeated
and thus that the environment does not change. This condition                  experiments. The states of all members of these ensembles are
is violated in many cases. For those situations, Carr and                      in general not exactly identical. Furthermore, every individual
Purcell (1954) introduced a modification of the spin-echo                      system may become entangled with environmental degrees of
experiment that improves refocusing in a time-dependent                        freedom. Such systems cannot be represented in terms of a
environment. The result of this was the CPMG sequence,                         single state vector. Instead, a density operator is a suitable
involving a series of π pulses with a constant delay between                   representation (Blum, 2012). For a pure state, it can be defined
them (Carr and Purcell, 1954; Meiboom and Gill, 1958).                         as ρ ¼ jΨihΨj. A generalization for the case of an ensemble is
These sequences now form the basis for active protection of
quantum systems against a noisy environment known as                                                        X
                                                                                                          1 N
dynamical decoupling (Viola and Lloyd, 1998; Viola, Knill,                                           ρ¼        jΨ ihΨi j;                     ð1Þ
                                                                                                          N i¼1 i
and Lloyd, 1999; Zanardi, 1999; Kofman and Kurizki, 2001,
2004; Khodjasteh and Lidar, 2005; Uhrig, 2007).
   This Colloquium is structured as follows: Sec. II defines                   where jΨi i represents the state of the ith member of
some basic tools that are generally used to characterize                       the ensemble and the index runs over all N members. The
quantum information, such as purity and fidelity of quantum                    normalization of the state vectors jΨi i implies that Trfρg ¼ 1.
states. Section III introduces the loss of coherence in static                 If all members of the ensemble are in the same state, Eq. (1)
environments and possible countermeasures. Section IV deals                    implies ρ2 ¼ ρ and therefore Trfρ2 g ¼ 1. This is the signature
with the additional complications that arise when the                          of a “pure state.” In all other cases, Trfρ2 g < 1 and the state is
environment fluctuates in time. Section V introduces pro-                      called a mixed state.
tection techniques that were developed specifically for time-                     By definition, the purity of a system Trfρ2 g is positive
dependent environments. In Sec. VI we discuss how these                        and its lowest value is for the maximally mixed state
protection techniques can be adapted to make them com-                         ρ ¼ 1=Trf1g. In almost all experimentally relevant situations,
patible with active controls of the system that drive the                      the interaction with the environment leads to a process known
execution of a quantum task, e.g., a computational algorithm.                  as decoherence, which drives the system from a pure state to a
Section VII considers how the same control operations can                      mixed state (Zurek, 2003; Schlosshauer, 2005). Decoherence
be used to characterize the noisy environment and extract                      does not exist if a closed system is considered that undergoes
information about it.                                                          a unitary evolution. It arises when we are interested in a
                                                                               particular part of the system leading to the consideration of a
II. CHARACTERIZATION OF QUANTUM STATES                                         system plus an environment. The reduced density operator is a
                                                                               tool to mathematically describe the system of interest. If the
A. Pure and mixed states                                                       state of the combined system A þ B is the pure state jΨihΨj,
                                                                               the reduced density operator of system A is obtained as
   The state vector jΨi is a convenient way of representing the
state of an individual quantum system. However, for many                                             ρA ¼ TrB fjΨihΨjg;                       ð2Þ
years after the introduction of the state vector, experiments
with single quantum systems were considered to be impos-                       where TrB ð⋅Þ denotes the trace in the Hilbert space of B. Its
sible1 and the state vector was therefore considered a tool that               definition comes from the fact that if an observable O operates
was only loosely related to the system under study. However,                   only on the system A, i.e., O ¼ OA ⊗ 1B , then its expectation
the situation changed completely when the specific properties                  value can be determined from the reduced density matrix as
of laser light made it possible to observe individual ions                     hOiΨ ¼ TrfjΨihΨjOg ¼ TrA fρA OA g. The generalization to
(Sauter et al., 1986) or electrons (Dehmelt, 1990). Since then,                the case where the state of the full system is itself mixed is
the number of quantum systems that can be controlled and                       ρA ¼ TrB fρAþB g. We identify subsystem A with the quantum
observed at the individual system level has grown signifi-                     system of interest and B with the environment (or vice versa).
cantly (Ladd et al., 2010). In those cases, describing the                     If the two subsystems become entangled with each other,
                                                                               e.g., by undergoing evolutions under a suitable coupling
   1
    In 1952, Schrödinger wrote “In the first place it is fair to state that    Hamiltonian, the subsystem observation destroys their quan-
we are not experimenting with single particles, any more than we can           tum superposition and drives the system toward a state that is
raise Ichthyosauria in the zoo” (Schrödinger, 1952).                           indistinguishable from a statistical mixture of states. This

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016                   041001-4
                                   Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


decoherence process has many implications in the foundations                     In many cases, one wants to quantify the agreement not
of quantum mechanics such as the problem of quantum                           between states, but between two evolutions. The evolutions
measurements, the quantum to classical transition, and irre-                  may be described by two propagators U1 and U2 , where one
versibility (Zurek and Paz, 1994; Paz and Zurek, 2002; Zurek,                 might be a target operator, such as a quantum gate operation,
2003; Schlosshauer, 2005; Goussev et al., 2012). It is the                    and the other the actual propagator implemented in an
purpose of this Colloquium to discuss causes of decoherence,                  experiment. The corresponding process fidelity can be defined
its consequences, and to show how its effects can be sup-                     in close analogy to the state fidelity (Wang, Yu, and Yi, 2008):
pressed or even exploited for specific tasks.
                                                                                                                   jTrfU †1 U 2 gj
B. Errors and fidelity                                                                   FðU 1 ; U 2 Þ ¼ qﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃqﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ :   ð3Þ
                                                                                                          TrfU†1 U 1 g TrfU†2 U 2 g
   In order to assess the effects of decoherence and the need
for countermeasures and their efficiency, it is necessary to                  Again, this fidelity measure satisfies FðU; UÞ ¼ 1. It corre-
quantify deviations between the actual and the ideal informa-                 sponds to the cosine of a generalized angle between the two
tion. Such distance measures correspond to the establishment                  propagators.
of a metric.
   Measures of distance between different states also exist in                III. DEPHASING AND REPHASING IN A STATIC
classical information theory. A widely used measure is the                    ENVIRONMENT
Hamming distance between two bit strings, which is defined
by the number of bits that must be flipped to transform one                   A. Dephasing models
into the other. As an example, the Hamming distance between
the strings “00110” and “00101” is 2. In the case of sensing,                    Environmental effects can be classified into two types:
accuracy and precision quantify the distance between the                      transitions between quantum states and loss of phase coher-
measurement and the true value.                                               ence. This Colloquium concentrates on the loss of coherence,
   A distance metric for quantum states should specify how                    which does not change the populations and is known as
well a state jΨ1 i agrees with the reference state jΨ2 i. In the              pure dephasing. This is in most cases the dominant process and
case of pure states, it is possible to measure this by the scalar             more options exist for fighting it. In the case of pure dephasing,
product hΨ1 jΨ2 i, which corresponds to the overlap between                   the system qubit couples to the environment through the
the two states. The scalar product has many useful properties,                operator Sz, which defines the quantization axis of the system.
such as being independent of the coordinate system and                        In systems with multiple qubits, the coupling operator com-
invariant under unitary transformations hUΨ1 jUΨ2 i ¼                         mutes with the system operator HS. Early discussions of
hΨ1 jΨ2 i. It corresponds to an inverse distance in the sense                 decoherence processes were given by Bloembergen, Purcell,
that it is maximized if the two states are identical and it                   and Pound (1947) for spins and by Feynman and Vernon
vanishes for orthogonal states.                                               (1963) for a general system coupled to an environment of
   In the case of mixed states, which have to be described by                 harmonic oscillators. In later work, Hepp and Lieb (1973) and
density operators, several distance measures are in use. One                  Zurek (1981, 1982) suggested the universality of the effect and
possible measure of the distance between two states (and thus                 made connections to the theory of quantum mechanical
of the error) is the trace-norm distance (Nielsen and Chuang,                 measurements. A very thorough investigation of the environ-
                                                         pﬃﬃﬃﬃﬃﬃﬃﬃ            mental effects on a two-level system was given by Caldeira and
2010) Dðρ1 ; ρ2 Þ ¼ ð1=2Þ‖ρ1 − ρ2 ‖, where ‖A‖ ¼ Trf A† Ag.
Clearly, the trace-norm distance between identical states                     Leggett (1983a, 1983b).
vanishes Dðρ; ρÞ ¼ 0, and for two pure orthogonal states
ρ1 , ρ2 , the distance Dðρ1 ; ρ2 Þ ¼ 1 reaches the maximum                    1. Classical environment
possible value. It is equal to the sum of the singular values                    The simplest description of the spurious interaction
of the difference of the operators. If the two operators                      between system and environment uses a single spin 1=2 to
commute, the trace distance becomes equal to the sum over                     describe the quantum system and a magnetic field that
the differences between the eigenvalues.                                      summaries the effect of many degrees of freedom of the
   Instead of measuring the distance, it is possible to measure               environment. Since we discuss errors, we may restrict
how closely two states agree. The corresponding quantity is                   the analysis to the case when this field is weak compared
generally called the state fidelity (Jozsa, 1994), and it can be              to the static field that defines the energy of the basis states j↑i
considered as a generalization of the scalar product. It is 1                 and j↓i. In this limit, the most important effect of the error
for identical states and 0 for orthogonal states. Different                   field is due to the component along the static field, which is
definitions of the state fidelity are used, including                         conventionally chosen to be oriented along the z axis.
                                                                                 To illustrate its effect, we consider a system that is initially
                                  jTrfρ1 ρ2 gj                                in a superposition state
                Fðρ1 ; ρ2 Þ ¼ pﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ pﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ :
                               Trfρ21 g Trfρ22 g
                                                                                                      jΨð0Þi ¼ aj↑i þ bj↓i;                               ð4Þ
Compared to some other measures, this specific measure
(Wang, Yu, and Yi, 2008) has the advantage that it does not                   where the two states j↑i and j↓i are the eigenstates of
require the evaluation of square roots of operators.                          the system Hamiltonian HS ¼ ℏωz Sz with eigenvalues

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016                 041001-5
                                 Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …

                                                                                                           X
ð1=2Þℏωz and Sz is the z component of the spin operator S.
                                                         ~                                       HSE ¼ ℏ         dβ Sz ⊗ Eβ ;            ð9Þ
An ideal evolution transforms the state jΨð0Þi into                                                          β


                                                                            where Sz represents the system operator, Eβ the bath oper-
            jΨðtÞi ¼ aj↑ie−ið1=2Þωz t þ bj↓ieið1=2Þωz t :            ð5Þ
                                                                            ators, and the index β runs over the relevant degrees of
                                                                            freedom of the bath. The coupling constants dβ here corre-
Dephasing is due to additional (uncontrollable) interactions,
                                                                            spond directly to the energy shift δE in Sec. III.A.1 but
which shift the energy of these eigenstates by a small amount
                                                                            describe the strength of the interaction between two quantum
ℏδE , i.e., the perturbation Hamiltonian or in general terms the
                                                                            mechanical degrees of freedom. An even simpler quantum
system-environment (SE) interaction is HSE ¼ ℏδE Sz . This
                                                                            mechanical model is the spin-spin model, where the environ-
additional energy level difference changes the relative phase
                                                                            ment is reduced to a single spin 1=2 or the central-spin model,
between the states by an angle ϕðtÞ ¼ δE t. The state then
                                                                            where the environment is represented by several spins
becomes
                                                                            (Gaudin, 1976; Prokof’ev and Stamp, 2000; Bortz and
                                                                            Stolze, 2007).
jψðtÞi ¼ aj↑ie−ði=2Þωz t e−ði=2ÞϕðtÞ þ bj↓ieði=2Þωz t eði=2ÞϕðtÞ :   ð6Þ       Here we discuss the simplest case of two interacting qubits:
                                                                            A (the system) and B (the environment). Each qubit is
If we now consider an ensemble in which the perturbation δE                 represented by a spin 1=2, and we assume that the two spins
varies for the individual members, they undergo different                   are coupled by an Ising interaction
evolutions and the average spin vector differs from that of the
individual spins. The same result is obtained if a single                                           HSE ¼ ℏdSA;z SB;z                   ð10Þ
quantum system is used in repetitive experiments and the
overall result corresponds to an average over realizations and              and that the system is initially in the product state
the perturbation δE varies for the different realizations. This             jΨð0Þi ¼ ð1=2Þðj↑i þ j↓iÞA ⊗ ðj↑i þ j↓iÞB . The evolution
effect can best be seen in the rotating frame at the Larmor                 under the operator (10) entangles the two systems with each
frequency ωz. The transformation to this reference frame is                 other. For the individual subsystems, this means that they are
described by the rotation operator Rz ðtÞ ¼ e−iHS t=ℏ ¼ e−iωz tSz           no longer pure states, but they must be described by density
(Abragam, 1961; Slichter, 1990).                                            operators. If we concentrate on the first (the “system” A),
   In this rotating frame, the dephasing can be obtained by                 while leaving the other (the “environment” B) unobserved, its
calculating the averaged scalar product as a fidelity measure               reduced density operator becomes, according to Eq. (2),
                                                                                                               
                      hψðtÞjψð0Þi ¼ cos ϕðtÞ;                        ð7Þ             1                   1     dt
                                                                                 ρA ¼ ðj↑ih↑j þ j↓ih↓jÞ þ cos     ðj↑ih↓j þ j↓ih↑jÞ:
                                                                                     2                   2     2
where the overbar represents
                      pﬃﬃ       the ensemble average, and we
assumed a ¼ b ¼ 1= 2. The cos ϕðtÞ term can be evaluated                       The purity of this state is 1=2 þ ð1=2Þcos2 ðdt=2Þ, which is
                                                                            lower than 1 for dt=2 ≠ nπ and n integer. At time dt=2 ¼ π=2,
by writing it as cos ϕðtÞ ¼ ðeiϕðtÞ þ e−iϕðtÞ Þ=2. For a Gaussian
                                                                            the total wave function is the maximally entangled state
random variable ϕðtÞ with vanishing mean, one obtains
                                                                                               eiπ=4
                                   2            2 2
                  cos ϕðtÞ ¼ e−ϕ ðtÞ=2 ¼ e−δE t =2 :                 ð8Þ               jΨi ¼         ðj↑↑i þ j↓↓i−ij↑↓i − ij↓↑iÞ;
                                                                                                 2

Therefore the average scalar product decreases as a Gaussian                but the reduced density operator of the system A is the
with a rate proportional to the second moment of the                        maximally mixed state
perturbation δ2E . For the off-diagonal elements (coherence
elements) of the density matrix, also in the rotating frame of                               ρA ¼ 12½ðj↑ih↑jÞA þ ðj↓ih↓jÞA ;
                                                  2
reference, one writes ρij ðtÞ ¼ ρij ð0Þe−ðt=T 2 Þ , where the
                                                                            whose purity is minimal Trfρ2A g ¼ 1=2. The reduced density
dephasing time or decoherence time T 2 is related to the root
                                       qﬃﬃﬃﬃﬃﬃﬃﬃﬃ                           matrix of this model system evolves strictly periodically
mean square of the perturbation T 2 ¼ 2=δ2E (Anderson and                   because the extremely simple model contains only a single
Weiss, 1953; Abragam, 1961; Kachru, Mossberg, and                           energy or frequency scale d=2. More complicated models of a
Hartmann, 1980). Different random processes give rise to                    system coupled to an environment show more complex
different decay laws. The states may then decay exponentially,              behavior; if the bath is sufficiently large, the typical behavior
as a power law, or as a combination of them.                                is a monotonous decrease of the purity. The time scale of
                                                                            most decoherence phenomena is inversely proportional to the
                                                                            square of the coupling between system and environment, as
2. Quantum mechanical environment                                           long as the different bath degrees of freedom interact inde-
  If the environment is not a classical field, but must also be             pendently with the system. If this is no longer the case, the
described as a quantum mechanical subsystem, the interaction                system-bath interaction becomes effectively time dependent.
between system and environment can be written as (Breuer                    This changes the effective strength as well as the characteristic
and Petruccione, 2007)                                                      behavior of the decoherence process (see Sec. IV).

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016                041001-6
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


3. Symmetry of dephasing interactions                                     where τþ is the time at which the pulse ends. The relative
   The best strategy for reducing the effect of environmental noise       phase between the two components has thus been inverted
depends on many details of the interaction, in particular, also on        from ϕ1 ¼ ωz τ to ϕ01 ¼ −ωz τ. Depending on the factor in ωz τ
the symmetry properties of the interaction Hamiltonian. The               to which we associate this sign change, it appears as an
following listcovers someimportant casesthatmay be considered             inversion of the Hamiltonian (ωz → −ωz ) for the period
prototypes and the appropriate countermeasures for those cases.           before the pulse, or to a reversal of the time evolution
    (i) Total decoherence: This is the most general case.                 τ → −τ. As the evolution continues, the phase accumulation
        Essentially there are no restrictions on the operators            continues, ϕ ¼ −ωz τ þ ωz ðt − τÞ. After another period τ, the
                                                                          additional phase ϕ2 ¼ ωz τ exactly cancels the phase ϕ01 and
        that generate the decoherence. The suitable counter-
                                                                          the sum of the two phases vanishes, ϕ01 þ ϕ2 ¼ 0. It therefore
        measure depends strongly on the specifications of
                                                                          appears as if the system had never undergone an evolution.
        the particular system. There is not a general rule.
                                                                          Since this is true for all spins, independent of the interaction
   (ii) Independent qubit decoherence: If the coupling oper-
                                                                          with the environment, the dephasing due to an inhomo-
        ator contains only operators that couple individual
                                                                          geneous interaction is exactly canceled by this refocusing
        spins to different degrees of freedom of the environ-             pulse and the second free precession period. All phases vanish
        ment, errors of individual qubits are independent. This           and the qubits get back into phase, forming an echo at time τ
        is the case typically considered in QEC and DD.                   after the refocusing pulse. The overall evolution is then the
  (iii) Collective decoherence: Here the coupling operators               unit operator. Since the same evolution would be generated by
        act in the same way on allPqubits. They can thus be               a Hamiltonian H ¼ 0, one says that the effective or average
        written in the form Fα ¼ i Siz , where i is the index             Hamiltonian vanishes (Haeberlen and Waugh, 1968). Echoes
        of the qubit. Clearly this interaction has full permu-            are also generated for other rotation axes and angles. If the
        tation symmetry on the system spins. This symmetry                rotations are π rotations around an axis in the x-y plane, the
        is exploited in the clock transitions and DFS                     refocusing is complete for a static environment.
        counterstrategies discussed in Sec. III.C.                           This time-reversal picture appears naturally if the evolution
  (iv) Cluster decoherence: This is an intermediate case,                 is written in the toggling frame (Slichter, 1990), an interaction
        where clusters of qubits decohere collectively, while             representation that follows the system state and the corre-
        the different clusters decay independently.                       sponding Hamiltonian is the one seen effectively by the spins.
The cases discussed are idealized situations. Real systems may            The propagator U ¼ e−iHðt−τÞ=ℏ Rx ðπÞe−iHτ=ℏ describing the
                                                                                                                            ~
be close to one of them or intermediate between several limit-            evolution can be rewritten as U ¼ Rx ðπÞe−iHðt−τÞ=ℏ e−iHτ=ℏ ,
ing cases.                                                                where H ~ ¼ R−x ðπÞHRx ðπÞ is the toggling frame Hamiltonian
                                                                          that describes the evolution after the refocusing pulse. In this
B. Rephasing: Echoes                                                      case H ¼ ℏωz Sz and H   ~ ¼ −ℏωz Sz which shows the change in
                                                                          the sign of the interaction. The probability of returning back to
   In those cases where the system is not sufficiently isolated,          the initial condition is then
environmental perturbations can cause unwanted time evolu-
tions. In many cases, these contributions to the evolution of                                                      ~
                                                                          jhΨð0ÞjΨðtÞij2 ¼ jhΨð0ÞjRx ðπÞe−iHðt−τÞ=ℏ e−iHτ=ℏ jΨð0Þij2
the system can be undone, in a process that can be compared
to time reversal. The most important preconditions for such                                ¼ jhΨð0ÞjeiHðt−τÞ=ℏ e−iHτ=ℏ jΨð0Þij2 ;      ð11Þ
time-reversal experiments are that the system operator that
couples to the environment is known, that suitable control                where we used Rx ðπÞjΨð0Þi ¼ jΨð0Þi for the present initial
operations exist that can invert it, and that the environment             condition. When t ¼ 2τ, Eq. (11) gives a perfect time reversal.
does not change too rapidly. The prototypical example                     If the reversal procedure contains imperfections, i.e., the
corresponds to the case where the system is a two-level                   forward Hamiltonian H and its backward counterpart H     ~ are
quantum system (e.g., a spin 1=2) that couples to a static                                                   i~
                                                                                                              Hτ −iHτ
                                                                          different, the probability jhΨð0Þje e
                                                                                                                             2
                                                                                                                      jΨð0Þij defines the
environment through the z component of the spin operator.                 Loschmidt echo that quantifies the efficiency of a time-
   This approach to reducing decoherence was originally                   reversal procedure (Peres, 1984; Jalabert and Pastawski,
introduced in NMR by Hahn (1950), who showed that a                       2001; Goussev et al., 2012).
π rotation (a NOT gate) applied to a spin-1=2 system (a qubit)
generates a time reversal of the corresponding evolution                  C. Protected subspaces and subsystems
(Fig. 2). This principle can be understood by considering a
                                           pﬃﬃ
superposition state (4) with a ¼ b ¼ 1= 2 in an external field               The basic idea of passive protection of quantum states,
that splits the eigenstates of the Hamiltonian by ℏωz as in the           using subspaces of the Hilbert space that are less sensitive to
example of Sec. III.A.1. The superposition state then evolves             environmental perturbations than others, has been exploited in
according to Eq. (5), i.e., the relative phase ϕ of the coherence         different fields for a long time. A prominent example is that of
increases linearly with time ϕ ¼ ωz t. The π rotation, which is           clock transitions (Essen and Parry, 1955).
applied at time τ, therefore changes the state to
                                                                          1. Clock transitions
                       1
           jΨðτþ Þi ¼ pﬃﬃ ðj↑ieiωz τ=2 þ j↓ie−iωz τ=2 Þ;                     Atomic clocks use the evolution of coherence in a chosen
                        2                                                 transition ðjiihkjÞðtÞ ¼ ðjiihkjÞð0Þe−iωik t as a measure of time.

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016             041001-7
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


Clearly, a variation of the level splitting ℏωik causes the clock         information or sensing, it is therefore necessary to extend the
to run too fast or too slow. Our time or frequency standard               concept to higher-dimensional subspaces. These are known as
defines 1 s as the duration of 9 192 631 770 periods of the               decoherence-free subspaces (Lidar, Chuang, and Whaley,
radiation corresponding to the transition between the two                 1998). The ideal situation is reached when the system-
hyperfine levels of the ground state of the cesium-133 atom               environment coupling HSE is degenerate for this subspace,
(Essen and Parry, 1955).                                                  i.e., it is a multiple of the unit operator. By a suitable choice
   A closer look at the level scheme of the cesium ground state           of the origin of the energy axis, it can be made to vanish for
(see Fig. 3) shows that the state splits not only into two                                    ðDFSÞ
                                                                          this subspace HSE ¼ 0. The simplest example of such a
hyperfine substates, but they again consist of a total of 16              subspace is that of a singlet state discussed earlier. A two-
Zeeman sublevels, which are shifted by the magnetic field by              dimensional DFS is used in the singlet-triplet qubit (Levy,
δE ¼ mF gF μB Bz , where gF is the Landé factor and μB is the             2002; Weiss et al., 2012). For QIP, this type of protection is
Bohr magneton. The z axis is chosen along the magnetic field              useful only if the dimension of the subspace is sufficiently
~ Accordingly, any perturbing magnetic field causes devia-
B.                                                                        large. The highest-dimensional subspaces exist in systems
tions of the atomic clock. The main exception from this rule is           undergoing “collective decoherence” (see Sec. III.A.3). This
the mF ¼ 0 ↔ mF0 ¼ 0 transition, since these two energies,                protection scheme remains useful even in a fluctuating
and therefore their difference, does not depend on the                    environment, which is discussed in the next section. It can
magnetic field strength Bz . Actual measurements therefore                be generalized to noiseless subsystems, where the symmetry
use this particular transition, and it is known as the “clock             of the system-bath interaction determines what quantum states
transition.” Similar transitions exist in other systems, and they         are conserved (Zanardi and Rasetti, 1997; Lidar, Chuang, and
are also referred to as clock transitions. The design and                 Whaley, 1998; Knill, Laflamme, and Viola, 2000; Kempe
engineering of quantum hardware can be improved by using                  et al., 2001).
an electronic structure of magnetic molecules if they are
tailored to give the desired clock transitions for enhancing the
                                                                          IV. FLUCTUATING ENVIRONMENTS
coherence times (Shiddiq et al., 2016).
                                                                             As discussed in Sec. III.B, a refocusing pulse reverts the
2. Decoherence-free subspaces and noiseless subsystems                    dephasing due to an inhomogeneous field by inverting the
   Another example
                 pﬃﬃ is found in a pair of spins: The singlet             accumulated phase and then by the subsequent evolution this
state jΨs i ¼ ð1= 2Þðj↑↓i − j↓↑iÞ has the special property in             phase is canceled. The dephasing is fully reverted only if the
which the expectation value of the magnetic-dipole operator μ~            effective strength of the system-environment interaction
vanishes, hΨs jμα jΨs i ¼ 0 for α ¼ ðx; y; zÞ. As a result, this          remains constant over the whole period. If this condition is
state is not affected by any type of magnetic fluctuations                not fulfilled, i.e., if either the strength of the system-environment
that can dephase the other states and its lifetime can be                 interaction or the state of the environment is time dependent, the
orders of magnitude longer than that of the other states                  evolution of the quantum system after the refocusing pulse
(Carravetta, Johannessen, and Levitt, 2004; Levitt, 2012).                differs from that before the pulse. In this case, the phase
Such long-lived singlet states are useful for storing population,         acquired by the spin due to the environmental interaction does
but they cannot store information. For applications in quantum            not cancel and some destructive interference remains. For
                                                                          longer evolution times, the probability that the environment
                                                                          is modified increases and the amplitude of the generated echo
                                                                          decreases as a function of the refocusing time (Hahn, 1950; Carr
                                                                          and Purcell, 1954). This decay contains information about the
                                                                          time dependence of the environment which can be exploited for
                                                                          sensing applications as discussed in Sec. VII.

                                                                          A. Classical environments

                                                                             We consider again the example of Sec. III.A.1, where the
                                                                          system Hamiltonian is HS ¼ ℏωz Sz and  pﬃﬃ the initial state is the
                                                                          superposition jΨð0Þi ¼ ðj↑i þ j↓iÞ= 2 of the eigenstates of
                                                                          the system. A fluctuating classical interaction can be described
                                                                          by the time-dependent coupling Hamiltonian

                                                                                                 HSE ðtÞ ¼ ℏδE ðtÞSz :                   ð12Þ
FIG. 2.  Phase reversal and echo formation by an inversion (π)
pulse applied to the qubit. The upper trace shows the pulses
(rectangles) driving the evolution of the system as well as the           This corresponds to a time dependence of the energy differ-
average signal of an ensemble of spins as a function of time (solid       ence ℏδE ðtÞ between the two spin states. The state of the
green line). The middle part shows the orientation of two of the          system is still given by the superposition of Eq. (6), but the
individual spin vectors at specific times, while the bottom trace         relative phase ϕ betweenR the eigenstates is now the integrated
shows their phase as a continuous function of time (dashed red vs         frequency shift ϕðtÞ ¼ 0t δE ðt0 Þdt0 . The resulting precession
solid blue lines).                                                        angle differs between members of an ensemble or between

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016             041001-8
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


                                                                            If the environmental Hamiltonian HE does not commute
                                                                          with Eβ , HSE also undergoes a time evolution induced by HE
                                                                          and the coupling between system and environment is no
                                                                          longer static. This is best seen by using an interaction
                                                                          representation defined by the Hamiltonian of the isolated
                                                                          environment HE . The system-environment interaction then
                                                                          becomes
FIG. 3. Ground state sublevels of atomic cesium. The hyperfine
structure as a function of magnetic field is shown, where F and                               ðEÞ
                                                                                           HSE ðtÞ ¼ e−iHE t=ℏ HSE eiHE t=ℏ :         ð13Þ
mF are the magnetic quantum numbers of the total spin operator
and its z component. The frequency of the clock transition
(mF ¼ 0 ↔ mF0 ¼ 0) is independent of the magnetic field (to               The system operators are not affected by this transformation,
first order).                                                             since they commute with HE .
                                                                             This quantum mechanical model can often be reduced to
independent runs of a single system. The phase acquired                   one that is formally equivalent to the classical model of
during a single run corresponds to a random process, as shown             Eq. (12) by tracing over the environmental degrees of freedom
in the left-hand part of Fig. 4.                                          (Abragam, 1961; Breuer and Petruccione, 2007). However, in
   Considering an ensemble instead of a single quantum                    some cases, classical and quantum environments generate
system, the random evolution of the individual members                    different effects. In the semiclassical regime, the thermal or
means that the average magnetization vector differs from that             quantum fluctuations of the environment induce random
of the individual spins. Since the orientation of the individual          phase accumulation to the system (Abragam, 1961; Breuer
spins (qubits) is progressively randomized as a function of               and Petruccione, 2007). In a regime that can only be described
time, the average magnetization vector, which is given by the             quantum mechanically, the interaction between the system’s
coherence ρij , becomes smaller, as shown in the right-hand               qubits and the environment can produce entanglement induc-
part of Fig. 4. If the perturbation corresponds to a Gaussian             ing feedback or backaction between the system and environ-
random variable with zero mean, as considered in Eq. (7) the              ment. A typical example of these quantum signatures is
                                                     2                    quantum beats and mesoscopic echoes (Müller et al., 1974;
average magnetization decays as cos ϕðtÞ ¼ e−ϕ ðtÞ=2 (Klauder             Pastawski, Levstein, and Usaj, 1995; Pastawski, Usaj, and
and Anderson, 1962). For a random walk of the phase, ϕ2 ðtÞ is            Levstein, 1996; Mádi et al., 1997; Levstein, Usaj, and
a linear function of time and the coherence decreases                     Pastawski, 1998; Altshuler, Lee, and Webb, 2012).
exponentially, as shown in the right-hand part of Fig. 4.
This simplified description becomes exact if the interaction              C. Interference of fluctuations with refocusing
that generates the random kicks does not have a memory
(Markovian limit) (Breuer and Petruccione, 2007).                            Figure 5 shows an example for the interference of fluctua-
                                                                          tions in the environment with refocusing. In this case, the
B. Quantum mechanical environments                                        system consists of an ensemble of 13 C nuclear spins in the
                                                                          molecular crystal adamantane,
                                                                                                      pﬃﬃ which are initially prepared in
  Time-dependent interactions between system and environ-
                                                                          a superposition state ð1= 2Þðj↑i þ j↓iÞ. This state dephases
ment exist also when the environment is a quantum system,
even if the Hamiltonian describing it has no explicit time                under the influence of a noisy environment consisting of 1 H
dependence. To show how this happens, we introduce a simple               nuclear spins coupled by magnetic dipole-dipole couplings
model Hamiltonian H ¼ HSE þ HP                                            between each other and to the system qubits. In the figure, the
                                   E , where HE is the envi-
ronment Hamiltonian, HSE ¼ ℏSz β dβ Eβ is the interaction                 black squares mark the decay of 13 C nuclear spin coherence. If
between the system and the environment described by Eq. (9),              a refocusing pulse is applied in the middle of the evolution
and the system Hamiltonian vanishes. As in the classical                  time, the spins can be rephased, but the dephasing time is
environment, this interaction describes only the dephasing,               increased only by approximately a factor of 2 (red circles).
not the energy relaxation.                                                The relatively low refocusing efficiency can be traced to the
                                                                          homonuclear dipole-dipole couplings between the 1 H nuclear
                                                                          spins of the environment, which correspond to HE in Eq. (13).
                                                                          The resulting mutual spin flips generate a rapidly fluctuating
                                                                          interaction for the 13 C nuclear spin (Álvarez et al., 2010).
                                                                             To discuss the interference between environmental fluctua-
                                                                          tions and refocusing, it is useful to consider a simple model for
                                                                          the fluctuations, such as the random telegraph noise model. In
                                                                          this model, the interaction strength δE ðtÞ of the dephasing
                                                                          Hamiltonian (12) makes random jumps between the two
FIG. 4. The left-hand part shows the evolution of the phase due           values δ0 . It describes a situation where a particle jumps
to a randomly fluctuating transition frequency, which corre-              randomly between two positions in a molecule or a solid
sponds effectively to a diffusion process. The right-hand part            and was studied in detail by Anderson (1954), Efros and
shows the decay of the coherence ρij of an ensemble of two-level          Rosen (1997), Falci et al. (2004), Bergli and Faoro (2007),
systems suffering this random process.                                    Cywinski et al. (2008), and Smith et al. (2012). Figure 6

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016             041001-9
                                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


                         1.0             1.0         S(ω)
                                                     FID filter
                                                     Hahn Filter

                                         0.5
                         0.8




     Normalized signal
                                         0.0
                         0.6                   -6      -4       -2   0   2    4   6
                                                                Frequency ω

                         0.4                        Hahn-echo

                                   FID
                         0.2


                         0.0
                               0                            1                         2
                                         Evolution time (ms)

FIG. 5. Decays of the freely precessing magnetization and the
Hahn echo of 13 C nuclear spins in solid adamantane as a function
of the evolution time. Both are proportional to the coherence ρ12
of the spin density operator. The decay of the Hahn echo indicates
that the environment that causes the dephasing is time dependent.
The inset shows a Lorentzian-shaped environmental noise spec-
trum SðωÞ (solid green line) together with the filter functions of
the free (shaded gray curve) and the Hahn (transparent red shaded
curve) evolution. In contrast to the free evolution, the Hahn filter
vanishes at the origin jFð0; 2τÞj2 ¼ 0. From Álvarez et al., 2010.

illustrates the interference of the fluctuations with the refocus-
ing by comparing a static environment and a single random                                       FIG. 6.     Interference of telegraph noise with the refocusing
jump. Two different spins are considered, whose coupling to                                     process. (a) The Hahn spin-echo sequence. (b), (c) The phase
the environment is initially δE ðt ¼ 0Þ ¼ δ0 (solid blue curves)                                accumulation of the spins without and with a random single jump
and δE ðt ¼ 0Þ ¼ −δ0 (dashed red curves). If δE ðtÞ is static,                                  of the precession frequency of the spin, respectively. fðtÞ gives
as assumed in Sec. III.B, the phase acquired by the spin during                                 the effective sign of the SE interaction during the sequence and
a time τ, ϕ1 ¼ δ0 τ, is fully refocused by a Hahn echo                                         δE ðtÞ is the instantaneous coupling with the environment of two
[Fig. 6(b)], where the phase ϕ2 ¼ ∓δ0 τ acquired during the                                     spins whose coupling to the environment is initially þδ0 (solid
second period cancels ϕ1 ¼ δ0 τ. However, if a jump                                            blue lines) and −δ0 (dashed red lines). The accumulated phase is
                                                                                                shown to be fully refocused for the static case (b), but it is not
between the values δ0 occurs at time Δτ after the π pulse,
                                                                                                refocused when a single jump occurs (c).
the accumulated phase becomes ϕ2 ¼ ∓δ0 Δτ  δ0 ðτ − ΔτÞ ¼
δ0 ðτ − 2ΔτÞ, which can cancel only ϕ1 if Δτ ¼ τ, i.e., the
                                                                                                with ϕð2τÞ ¼ 0, then according to Eq. (7), the averaged
jump does not occur during the considered evolution time.
                                                                                                fidelity of the spin state is
   In general the interference of environmental fluctuations
can be much more complex, e.g., if the random fluctuations                                                                                       2
                                                                                                                       hψð2τÞjψð0Þi ¼ e−ϕ ð2τÞ=2 ;
are between more than two values or the noise must be treated
quantum mechanically. However, a universal picture still                                         where
exists for weakly coupled environments, where the system                                                          Z 2τ Z 2τ
negligibly influences the environment. In this case, the                                              ϕ2 ð2τÞ ¼               fðt0 Þfðt00 ÞδE ðt0 ÞδE ðt00 Þdt0 dt00 :   ð15Þ
second-order approximation for the total evolution operator                                                        0      0
of the SE interaction can be used (Abragam, 1961; Breuer and                                       If the average of the fluctuating δE ðt0 Þ is independent of
Petruccione, 2007), where the SE interaction Hamiltonian can
                                                                                                time, i.e., δE ðt0 Þ ¼ const, then also ϕ2 ð2τÞ ¼ 0 for DD sequen-
be described by Eq. (12), HSER ¼ ℏδE ðtÞSz , and the phase
acquired by the spins is ϕðtÞ ¼ 0t δE ðt0 Þdt0 . In the Hahn echo                               ces. However, the term ϕ2 ð2τÞ does not vanish in general and
sequence, the π pulse inverts the sign of the effective SE                                      can be evaluated by its Fourier transform representation:
interaction and the accumulated phase becomes                                                                            pﬃﬃﬃﬃﬃ Z ∞
                                                                                                               2
                             Z 2τ                                                                            ϕ ð2τÞ ¼ 2π            jFðω; 2τÞj2 SðωÞdω;       ð16Þ
                                                                                                                                  −∞
                   ϕð2τÞ ¼        fðt0 ÞδE ðt0 Þdt0 ;         ð14Þ                                                    pﬃﬃﬃﬃﬃ R
                                               0                                                where SðωÞ ¼ ð1= 2π Þ ∞        −∞ gðΔtÞe
                                                                                                                                         −iωΔt
                                                                                                                                               dΔt is the spectral
where fðt0 Þ is a modulating function that tracks the effective                                 density of the environmental fluctuations, which is
sign of the SE interaction due to the pulses, i.e., fðt0 Þ ¼ 1 for                              given by the Fourier transform of the environmental correla-
0 ≤ t0 < τ and fðt0 Þ ¼ −1 for τ < t0 ≤ 2τ for the Hahn echo                                    tion function gðΔtÞ ¼ δE ðt0 ÞδE ðt0 þ ΔtÞ, and Fðω; 2τÞ ¼
                                                                                                    pﬃﬃﬃﬃﬃ R      0 −iωt0 0
sequence. If the phase ϕð2τÞ is a Gaussian random variable                                      ð1= 2π Þ 2τ  0 fðt Þe     dt is the finite time Fourier transform

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016                                    041001-10
                                  Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


of the sign modulating function. Fðω; 2τÞ can be understood as               quadratically in time. In a rapidly fluctuating environment
a filter function, since it reduces the respective frequency                 where the correlation time goes to zero (a Markovian bath),
component of the noise spectrum (Kofman and Kurizki, 2001;                   the decay is ∝ e−t=T 2 and the derivative at t ¼ 0 is nonzero.
Kofman and Kurizki, 2004; Cywinski et al., 2008).                               The distinction between these two cases with vanishing or
   In general the decay of a Hahn echo is slower than the decay              nonzero derivative at t ¼ 0 is not as technical as it may appear:
during free evolution, as seen in Fig. 5. As shown in the inset              Only if the experimental control of the system is sufficiently
of Fig. 5, if SðωÞ has a maximum at ω ¼ 0, and it decays for                 fast that manipulation can occur during the quadratic initial
larger frequencies, the integral of Eq. (16) is lower than for               phase, it remains possible to undo the effects of dephasing.
free evolution, because jFð0; 2τÞj2 ¼ 0 for a Hahn sequence,                 This is used in the quantum Zeno effect, where a measurement
but not for free evolution. If the environment is Markovian,                 “projects” the state back to the initial state. If the initial
i.e.,
pﬃﬃﬃﬃﬃ the noise spectrum is white,p  ﬃﬃﬃﬃﬃ SðωÞ ¼ const, ϕ2 ð2τÞ ¼          evolution is quadratic in time and the projection sufficiently
           R∞                                                                frequent, this scheme can stop the evolution of the system
   2π Sð0Þ −∞ jFðω; 2τÞj2 dω ¼ 2π Sð0Þt. The signal decays
then exponentially with a rate that depends purely on Sð0Þ                   (Misra and Sudarshan, 1977; Pascazio, 2014). A number of
independently of the shape of Fðω; 2τÞ. Refocusing pulses                    schemes based on this effect have been proposed and
therefore do not affect the decay. The width of the spectral                 implemented. They may be distinguished from refocusing
density is related to the inverse of the correlation time 1=τc               schemes, which reverse the evolution, rather than arresting
which defines the decay of the correlation function gðΔtÞ. For               it, but the two approaches can also be unified in a single
example, if SðωÞ is a Lorentzian function whose width is 1=τc ,              framework (Kofman and Kurizki, 2001, 2004; Facchi, Lidar,
                                                                             and Pascazio, 2004; Facchi et al., 2005). These dynamical
then its correlation function is gðΔtÞ ∝ e−t=τc . The refocusing
                                                                             control approaches are usually referred to as DD or quantum
works well only when the delay between adjacent pulses is
                                                                             bang bang (Viola, Knill, and Lloyd, 1999; Viola, Lloyd, and
shorter than the correlation time. In the frequency domain, this
                                                                             Knill, 1999; Zanardi, 1999) and are the main focus of the
corresponds to the requirement that the filter function must
                                                                             present section. A common assumption for these schemes is
remain small for frequencies where the spectral density SðωÞ
                                                                             that control operations can only be applied to the system,
is significant.
                                                                             while the environment is not only randomly fluctuating, but
   A simple example of a time-dependent interaction that
                                                                             also uncontrollable.
generates Gaussian noise is that of an ensemble of particles
undergoing Brownian motion in an inhomogeneous field
(Hahn, 1950; Carr and Purcell, 1954; Klauder and Anderson,                   A. The Carr-Purcell solution
1962; Stepisnik, 1999; Grebenkov, 2007). Assuming for                           The first experiment of this type was described by Carr and
simplicity that the field has a uniform gradient ~             G, the        Purcell (1954) (CP). It can be described using the Hamiltonian
resonance frequency of the spins depends on their position                   (12) discussed in Sec. IV. The basic idea is to modify Hahn’s
as δE ð~rÞ ¼ δE ð0Þ þ γ G
                        ~ · ~r. The phase acquired by these                  echo experiment: Instead of applying a single pulse in the
particles during a spin-echo sequence is                                     middle of the period, CP applied a sequence of pulses, with
                           Z τ                 Z 2τ                          separations between them that were short compared to the
          ϕð2τÞ ¼ ϕð0Þ −        δE ð~rÞdt þ         δE ð~rÞdt;               time scale on which the environment changes.
                              0                 τ                               As shown in Fig. 7, each pulse generates a new echo. In the
where ~r ¼ ~rðtÞ is in general time dependent. The two integrals             case of diffusion, the decay of the echo envelope slows down
cancel as long as G  ~ · ~r is constant. This happens if the field is        ∝ 1=N 2 as the number N of pulses is increased. If the pulse
                                                                             spacing becomes short compared to the environmental fluc-
homogeneous (G ¼ 0) or if the position of the particle is
                   ~
                                                                             tuations, they become unimportant and refocusing is reestab-
independent of time ~rðtÞ ¼ ~rð0Þ. However, for a general                    lished. A modification of the Carr-Purcell experiment due to
diffusive motion in an inhomogeneous field, this condition                   Meiboom and Gill (1958) reduced the effect of experimental
is not fulfilled, the two integrals differ, and the refocusing is            imperfections for initial conditions that are invariant under the
incomplete. Accordingly, the Hahn echo is not effective in                   effect of the refocusing pulse. The same idea was adapted in
systems with fluctuating environments. For this situation,
additional techniques are required, which we discuss in the
following section.

V. ACTIVE PROTECTION AGAINST NOISE

   As discussed in Sec. III, static environmental perturbations
can generally be refocused by techniques such as the Hahn
echo. However, as shown in Sec. IV, the environment is
generally not static, and fluctuations in the interaction between
system and environment severely degrade the refocusing
efforts. The difference between a static and a rapidly fluctuat-
ing environment can be summarized as follows: In a static                    FIG. 7. The sequence of π rotations shown on top generates the
environment, the correlation function of a superposition state               echo train shown in the bottom trace. From Ali Ahmed, Álvarez,
decays as 1 − at2 for short times, i.e., the decay occurs                    and Suter, 2013.

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016               041001-11
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


the context of QIP under the name of DD (Viola and Lloyd,                 unavoidable imperfections of the refocusing pulses. In QIP
1998; Viola, Knill, and Lloyd, 1999; Zanardi, 1999; Kofman                applications, where the initial condition is in general not
and Kurizki, 2001, 2004; Khodjasteh and Lidar, 2005;                      known, a simple phase shift is not sufficient to make the
Uhrig, 2007).                                                             sequences robust for arbitrary initial conditions (Álvarez et al.,
   Figure 8 shows that refocusing pulses effectively decouples            2010; Ryan, Hodges, and Cory, 2010; de Lange et al., 2010;
the qubit from the environment. The more pulses are applied               Souza, Álvarez, and Suter, 2011, 2012c).
(and thus the shorter the delay between the pulses), the longer              Dhar, Grover, and Roy (2006) and Uhrig (2007) added
the survival time of the coherence (Álvarez et al., 2010; Ryan,           another important degree of freedom to the scheme: they
Hodges, and Cory, 2010; de Lange et al., 2010; Ajoy, Álvarez,             introduced sequences with nonequidistant pulses, while all
and Suter, 2011). For the conditions shown here (a single                 earlier sequences were based on equidistant pulses. The effect
electron spin in a diamond nitrogen vacancy (NV) center), the             of the nonequidistant pulses can be understood in the context
coherence time increases by roughly 1 order of magnitude as               of filter theory: DD inserts a filter between system and
the number of refocusing pulses increases from 1 to 64 (Shim              environment, and the pulse spacing determines the character-
et al., 2012).                                                            istics of this filter. This type of picture was discussed by
                                                                          Kofman and Kurizki (2001, 2004) as a general framework for
B. Dynamical decoupling                                                   dynamically controlling the decoherence rates. According to
                                                                          Eq. (16), they are proportional to the overlap of a filter
   Dynamical decoupling can be seen as a generalization of                function with the spectral density of the environmental noise.
the Carr-Purcell experiment to situations where general                   Well-designed DD sequences minimize this overlap and
(unknown) quantum states must be protected against noise.                 therefore the decoherence rate (Kofman and Kurizki, 2001,
The basic idea of active techniques is to use unitary control             2004; Gordon, Kurizki, and Lidar, 2008; Biercuk et al.,
operations that impose a time dependence on the system-bath               2009a; Uys, Biercuk, and Bollinger, 2009; Clausen,
interaction in such a way that hHSE it ¼ 0, where h⋅it stands             Bensky, and Kurizki, 2010; Pasini and Uhrig, 2010; Ajoy,
for the time average. In the simplest case, this is achieved by a         Álvarez, and Suter, 2011). In particular, the Uhrig DD (UDD)
sequence of π pulses (Viola and Lloyd, 1998; Viola, Knill, and            sequence generates a high pass filter that has the flattest stop
Lloyd, 1999; Viola, Lloyd, and Knill, 1999; Zanardi, 1999;                band around zero frequency (Uhrig, 2007, 2008; Cywinski
Kofman and Kurizki, 2001, 2004). The main parameters for                  et al., 2008). This predicted behavior was confirmed exper-
optimizing the design of DD sequences are the delays between              imentally by Biercuk et al. (2009b) and Du et al. (2009).
the pulses and their phases (i.e., the rotation axes). In many            However, the UDD scheme requires increasing the number of
cases, it is also possible to use continuous control fields               pulses per cycle, while the delays between them are not
instead of discrete inversion pulses (Kofman and Kurizki,                 identical. As the duration of one UDD cycle increases with N,
2001; 2004; Viola and Knill, 2003; Gordon, Kurizki, and                   the first transmission peaks appear at lower frequencies than
Lidar, 2008; Timoney et al., 2011).                                       in sequences built from short cycles, such as CPMG (Ajoy,
   The CP and CPMG sequences discussed in Sec. V.A consist                Álvarez, and Suter, 2011). Therefore the UDD protocol does
of a series of identical π pulses. The only difference between            not perform well when the noise contains frequency compo-
CP (Carr and Purcell, 1954) and CPMG (Meiboom and Gill,                   nents in the range of the transmission peaks (Biercuk et al.,
1958) is the orientation of the rotation axis of the pulses with          2009b; Álvarez et al., 2010; Barthel et al., 2010; Ryan,
respect to the initial condition: CPMG aligned it with the                Hodges, and Cory, 2010; de Lange et al., 2010; Ajoy, Álvarez,
initial condition to minimize the effect of experimentally                and Suter, 2011; Green et al., 2013). Nevertheless, choosing
                                                                          the delays between the pulses in an optimal way for designing
                                                                          the best filter function for a given environmental spectral
                                                                          density can be generally useful (Kofman and Kurizki, 2001,
                                                                          2004; Gordon, Kurizki, and Lidar, 2008; Biercuk et al.,
                                                                          2009a; Uys, Biercuk, and Bollinger, 2009; Clausen,
                                                                          Bensky, and Kurizki, 2010; Pasini and Uhrig, 2010; Ajoy,
                                                                          Álvarez, and Suter, 2011).
                                                                             These refocusing techniques are useful for the reversal of
                                                                          dephasing processes. In the case of energy relaxation, the
                                                                          fluctuations of the environmental perturbations occur on a
                                                                          time scale of the order of 1=ωz or faster. Resonant pulses are
                                                                          necessarily slower than this; thus they cannot undo energy
                                                                          relaxation and we therefore do not consider this case.

FIG. 8.  Decay of the coherence of a single electron spin in the          C. Imperfect and robust rotations
NV center of a diamond for different numbers of refocusing
pulses. The different curves are displaced vertically to avoid               As discussed earlier, applying multiple refocusing pulses
overlap. Each data point represents the number of photons                 with short delays compared to the correlation time of the
counted at the position of the last echo. As the number of pulses         environmental fluctuations increases the coherence time of the
increases and the delay between the pulses decreases, the signal          system. This is the theoretical expectation and experimental
can be preserved for a longer time. From Shim et al., 2012.               results support this in many cases.

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-12
                                                         Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


   However, as shown in Fig. 9, there are also cases where                                              Freeman, 1979; Tycko, 1983; Tycko and Pines, 1984; Tycko,
experimental observations differ qualitatively (Álvarez et al.,                                         Pines, and Guckenheimer, 1985; Levitt, 1986; Brown,
2010). In this example, a train of refocusing pulses is applied,                                        Harrow, and Chuang, 2004). When electronic signal gener-
which rotate the nuclear spins around the same axis. If the                                             ators became more flexible, it was generalized to (almost)
initial condition is perpendicular to the rotation axis of the                                          continuous modulation of amplitude and phase of the pulse.
pulses, reducing the delay between the pulses actually leads to                                         The shapes can be optimized using tools from optimal control
a faster decay of the coherence. The reason is that in this case                                        theory, and the design goal is the same as for composite pulses
the accumulation of pulse imperfections destroys the coher-                                             (Warren and Silver, 1988; Khaneja et al., 2005; Nielsen et al.,
ence. Shorter delays mean more pulses during a given interval                                           2008; Koch, 2016). In both approaches, it is possible to design
and therefore more rapid accumulation of pulse errors. These                                            the gates in such a way that they take a specific initial state to a
effects of pulse imperfections were noticed by Meiboom and                                              chosen final state. The more general scheme, which is usually
Gill (1958) who proposed to shift the phases of the π pulses to                                         required in quantum information, implements specific unitary
reduce the flip-angle error effects in the CP sequence (Carr                                            transformations, which can be applied to arbitrary initial
and Purcell, 1954). The effect of pulse imperfections in the                                            conditions (Levitt, 1986; Warren and Silver, 1988; Merrill
CPMG sequence depends therefore strongly on the initial                                                 and Brown, 2014).
condition. If the spins are initially oriented along the rotation                                          Using such robust gate operations can almost completely
axis of the pulses, flip-angle errors have essentially no effect                                        eliminate some of the most important experimental imperfec-
(longitudinal initial condition). However, if the spins are                                             tions. A comparison of DD with robust pulses versus standard
oriented perpendicular to the pulse rotation axis (transverse                                           pulses (Souza, Álvarez, and Suter, 2011) showed that robust
initial condition), the pulse errors add up and cause a rapid                                           pulses improve the performance at high duty cycles,2 where
decay of the coherence. This type of asymmetries between                                                the effect of pulse errors is largest. However, for a given duty
input states has been observed in different systems. Apart                                              cycle, sequences with robust (and thus longer) pulses must
from the decay, the pulse imperfections induce a number of                                              use longer delays between the pulses, which may result in a
interesting effects such as stimulated echoes (Franzoni and                                             lower performance than sequences with short pulses and short
Levstein, 2005; Franzoni et al., 2008, 2012) or effective spin-                                         delays (Souza, Álvarez, and Suter, 2011). The refocusing
lock effects (Álvarez et al., 2010; Ridge, O’Donnell, and                                               schemes discussed previously are designed mostly to elimi-
Walls, 2014). Average Hamiltonian theory can be used to                                                 nate static field inhomogeneities. Similar techniques can be
describe the combined effect of the pulse imperfection and the                                          used to eliminate inhomogeneities of the control fields
environment dynamics over the pulse sequence (Dementyev                                                 (Solomon, 1959; Levitt and Freeman, 1979).
et al., 2003; Li et al., 2007, 2008; Dong et al., 2008).
   A straightforward approach for reducing the effect of pulse                                          D. Robustness of decoupling sequences
imperfections is to use robust pulses instead of the normal
pulses. Robust pulses are designed such that their performance                                             Robust gate operations perform well even if the control
is close to the targeted operation even if the control field                                            fields deviate from their ideal values. However, the associated
deviates from its ideal value. Two approaches are used for this                                         overhead makes this approach less attractive when a large
purpose. The older one concatenates a series of rotations in                                            number of pulses is required. Instead, it is better to design the
such a way that their errors cancel over the sequence. These                                            sequences in such a way that the errors of one operation are
types of pulses are known as composite pulses (Levitt and                                               compensated by the imperfections of the others. In this way,
                                                                                                        the overall sequence can achieve virtually perfect fidelity at
                                                                                                        the same cost, e.g., in terms of power requirements, as simple,
                                                                               Longitudinal
                                                                                  initial               uncompensated sequences like CPMG. Clearly, for this
                                                                                condition               approach it is easier to correct known errors than completely




      Relaxation time T2 (ms)
                                100                   En
                                                         v                                              random ones. In the following, we generally assume the errors
                                                           nm                                           of subsequent operations are correlated.
                                                        iro
                                                                 om                                        As an example of the cumulative effect of experimental
                                         Pulse                 td
                                10                           en
                                      imperfections               in
                                                                         e           Transverse         imperfections, consider the cumulative effect of N successive
                                        dominate                      ats               initial         rotations by a nominal angle π around the x axis, such as in a
                                                                                      condition
                                                                                                        CPMG sequence. Under ideal conditions, this corresponds to
                                 1
                                                                                                        the operation NOTN ¼ ðe−iπSx ÞN ¼ 1 ¼ NOOP if the number N
                                                                                                        of pulses is even. If the actual rotation angle of each pulse
                                      10                          100                                   differs by πδ (e.g., δ ¼ 1=N, which can be very small for
                                      Delay between pulses                   ( s)                       large N), the error accumulates over the N pulses and the
                                                                                                        total propagator becomes ðe−iπð1þδÞSx ÞN ¼ e−iπSx ¼ NOT. This
FIG. 9. Dephasing time of 13 C nuclear spins in adamantane as a                                         actual propagator is generated by an effective magnetic field in
function of the delay between the pulses for two different initial
conditions (parallel and perpendicular to the rotation axis of the
                                                                                                              2
refocusing pulses). The number of refocusing pulses per unit of                                             The duty cycle is the sum of the pulse durations divided by the
time increases then from right to left. The square symbols                                              total duration of the sequence. Experimental constraints, such as
represent experimental data points and the curves are guides to                                         maximum power deposition, often limit the possible duty cycle to
the eye. From Álvarez et al., 2010.                                                                     values ≪ 1.

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016                                            041001-13
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …




                                                                          FIG. 11. Fidelity of a DD sequence of 100π pulses as a function
                                                                          of two types of errors (offset, flip-angle). The resulting fidelity is
                                                                          color coded, with fidelities below 0.95 in white. For details see
                                                                          the text.
FIG. 10. Fidelity of different pulse sequences after N ¼ 20
π pulses as a function of the flip-angle error of the individual          on the qubit energy) whose effect is equivalent to an error in
pulses. The different curves correspond to the CPMG, XY-4, and            the orientation of the rotation axis. The dephasing inter-
KDD sequences (Souza, Álvarez, and Suter, 2011).
                                                                          actions discussed in Sec. III.A can also be considered as
                                                                          offset errors; therefore robust sequences have to be robust
the x direction (Álvarez et al., 2010; Ridge, O’Donnell, and              against flip-angle and offset errors. Figure 11 shows the
Walls, 2014) and has vanishing overlap with the target                    performance of the sequences of Fig. 10 as a function of
propagator; the fidelity of the operation is zero. This is the            simultaneous flip-angle and offset errors. These sequences
reason that the dashed blue curve in Fig. 10 tends to zero for            were found to be useful for QIP in several systems, including
flip-angle errors of 5% and N ¼ 20.                                      electron spins in diamond (Ryan, Hodges, and Cory, 2010; de
   The simple example of a sequence of two π rotations                    Lange et al., 2010; Shim et al., 2012; Wang, de Lange et al.,
discussed earlier is useful for illustrating some of the most             2012) or silicon (Wang, Zhang et al., 2012), and nuclear spins
useful schemes for avoiding errors. Instead of applying the N             in solids (Álvarez et al., 2010; Souza, Álvarez, and Suter,
successive rotations around the same axis, one applies                    2011; Álvarez, Souza, and Suter, 2012; Lovric et al., 2013;
rotations around a series of different axes. Consider the case            Zhong et al., 2015) or liquids (Ali Ahmed, Álvarez, and
in which the rotations are applied alternating between the x              Suter, 2013).
and −x axes (Álvarez et al., 2010). In this case, the overall                Sequences whose performance is robust against experi-
operation is                                                              mental imperfections have been developed by many different
                                                                          approaches. One possible approach is based on evaluating
         NOTN ¼ ðe−ið1þδÞπSx eið1þδÞπSx Þ
                                            N=2
                                                  ¼ 1 ¼ NOOP;             the average Hamiltonian of a DD sequence using a series
                                                                          expansion, such as the Magnus expansion (Magnus, 1954).
                                                                          The DD sequence is designed such that the lowest-order term
independent of the error δ. This simple “trick” of alternating
                                                                          is the identity operator. The higher-order terms are imperfec-
the rotation axis thus turns the highly error-prone sequence
                                                                          tions that reduce the sequence performance and must therefore
into a completely robust one, and this is achieved with zero
                                                                          be minimized. This usually defines the decoupling order of
overhead: the duration of the sequence and the amount of
                                                                          the sequences and was also the general approach for devel-
energy deposited remains the same.
                                                                          oping better decoupling sequences for NMR (Waugh, 1968,
   This principle can be extended: switching not only between
                                                                          1982a, 1982b; Levitt and Freeman, 1981; Levitt, Freeman,
two possible orientations of the rotation axis, it is possible
                                                                          and Frenkiel, 1982). Two general strategies for canceling or
to find sequences that are much more robust against different
                                                                          reducing higher-order terms are to either sequentially con-
types of experimental imperfections. This is illustrated in
                                                                          catenate symmetry-related versions of the basic cycles into so-
Fig. 10 by the two curves labeled XY-4 and KDD. In the
                                                                          called supercycles (Haeberlen and Waugh, 1968; Mansfield,
case of XY-4,3 the rotation axis alternates between the x and y
                                                                          1971; Rhim, Elleman, and Vaughan, 1973; Burum and Rhim,
axes (Maudsley, 1986; Gullion, Baker, and Conradi, 1990). In
                                                                          1979) or by nested iteration schemes (Khodjasteh and Lidar,
the KDD sequence the rotation axis alternates between five
                                                                          2005, 2007; Álvarez, Souza, and Suter, 2012). The sequential
different orientations during a 10-step cycle (Souza, Álvarez,
                                                                          approach led to the XY family of sequences like XY-4, XY-8,
and Suter, 2011; Álvarez, Souza, and Suter, 2012) chosen
                                                                          and XY-16 (Maudsley, 1986; Gullion, Baker, and Conradi,
with a numerical optimization procedure for the minimum
                                                                          1990) or Eulerian DD (Viola and Knill, 2003). The nested
error of the cycle (Tycko, Pines, and Guckenheimer, 1985). In
                                                                          approach includes concatenated DD (CDD), which initially
all three cases, the error of the individual pulses is the same,
                                                                          used the XY-4 sequence as the basic building block. The
but the compensated sequences XY-4 and KDD perform
                                                                          CDD evolution operator for a recursion order N is given
almost flawlessly, even if the flip angle deviates by as much
                                                                          by CDDN ¼ CN ¼ Y-CN−1 -X-CN−1 -Y-CN−1 X-CN−1, where
as 15% (XY-4) or 30% (KDD) from its nominal value.
                                                                          C0 ¼ 1 and CDD1 ¼ XY-4. With this approach, each level of
   Besides reducing the effect of flip-angle errors, these
                                                                          concatenation reduces the norm of the first nonvanishing order
sequences must also be robust against offset errors (a shift
                                                                          term of the Magnus expansion of the previous level, provided
                                                                          that the norm was small enough to begin with (Khodjasteh and
  3
      In the context of QIP, XY-4 is also known as PDD.                   Lidar, 2005, 2007). CDD sequences were tested in solid-state

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-14
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


NMR demonstrating the performance improvement by                          allows one not only to detect errors, but also correct them, is
increasing the concatenation level (Álvarez et al., 2010;                 the generation of copies of a bit, independent processing, and
Álvarez, Souza, and Suter, 2012). In cases where the                      comparison of the results. Of course in today’s mature
composite pulse consists of a sequence of N π rotations, it               information and communication technology, far more sophis-
is also possible to improve the overall sequence by separating            ticated error correction schemes are used, but they all rely on
the segments of the composite pulse and distributing the free             checking for damage and reconstructing the original informa-
precession period equally between them. Instead of a                      tion with the help of redundancy. Since duplicating unknown
composite refocusing pulse followed by a delay τ, the basic               quantum information is not possible (Dieks, 1982; Wootters
element consists then of N refocusing pulses separated by N               and Zurek, 1982), a direct transfer of these techniques to the
delays of duration τ=N. This basic element can be extended                realm of quantum information is not possible. Nevertheless,
into supercycles by concatenating different phase-shifted                 schemes that implement error correction for quantum infor-
versions. The resulting sequence combines the robustness                  mation have been developed (Lidar and Brun, 2013; Terhal,
of composite pulses with good low-power decoupling per-                   2015). On the basis of these schemes, it was finally shown that
formance (Souza, Álvarez, and Suter, 2011; Álvarez, Souza,                reliable quantum computation is feasible (Preskill, 1998),
and Suter, 2012).                                                         provided the fidelity of the individual gate operations exceeds
   Under ideal conditions the delays between the pulses can be            the threshold for the corresponding scheme.
reduced indefinitely, and the performance of the sequences                   As in the classical case, QEC relies on encoding informa-
improves monotonically. However, this is not the case for real            tion to be protected in a larger number of physical qubits
pulses, whose amplitudes and durations are finite and contain             than the minimum required by the amount of information.
imperfections, as shown in Fig. 9. Under these conditions the             Figure 12 shows the principle of this approach, using the
optimal performance is obtained for a finite cycle time. In the           example of a three-qubit code. In this simplest case, a single
case of CDD, it was predicted (Khodjasteh and Lidar, 2007)                logical qubit is encoded in three physical qubits, using for the
and experimentally demonstrated (Álvarez et al., 2010;                    logical state 0L the code word j000i and for 1L the code word
Álvarez, Souza, and Suter, 2012) that an optimal concatena-               j111i. Thus j000i and j111i are the only two legal code words
tion order exists for a given delay between pulses, and beyond            of this coding scheme. If the bit-flip error probabilities p for
that order the decoupling becomes less efficient. This behavior           the 3 bits are identical and independent of each other, the
can be understood by considering that the compensation of                 probability for error-free transmission of the logical bit is
the pulse imperfections is designed to happen at the end of the           ð1 − pÞ3 , the probability that one of the three physical bits
cycle. If the average delay between the pulses is fixed, then             has flipped is 3pð1 − pÞ2 , and so on. After transmission one
the CDD cycle time increases with the concatenation order.                checks if all 3 bits of the code word are equal, and if they are
Therefore, when the cycle time exceeds the correlation time               not, one flips the 1 bit which does not conform to the other
of the environmental fluctuations, the compensation of the                two. This leads to a wrong result if 2 bits were flipped during
imperfections becomes inefficient and the DD performance                  transmission, and the total probability for this to happen is
decreases. This kind of behavior is general for DD sequences
                                                                          p2 ð3 − 2pÞ, which is much smaller than p for sufficiently
and in practice, higher-order sequences do not always perform
                                                                          small p.
better. Numerous studies addressed this issue from the
                                                                             Usually the bit-flip probability p grows with the distance
theoretical (Viola and Knill, 2003; Khodjasteh and Lidar,
                                                                          (in space or time) of transmission, so that error correction must
2007; Hodgson, Viola, and D’Amico, 2010; Uhrig and Lidar,
                                                                          be repeated sufficiently frequently (but not too frequently,
2010; Khodjasteh, Erdélyi, and Viola, 2011; Ng, Lidar, and
                                                                          since encoding and decoding operations may themselves
Preskill, 2011) and experimental side (Álvarez et al., 2010;
                                                                          introduce additional errors, which we have neglected here
Ajoy, Álvarez, and Suter, 2011; Souza, Álvarez, and Suter,
                                                                          for simplicity). A larger number of physical bits per logical bit
2011; Álvarez, Souza, and Suter, 2012) for different types of
                                                                          can be employed, increasing the probability of success, but
errors and DD sequences.
                                                                          also increasing the cost in terms of storage space or trans-
                                                                          mission time, as well as the complexity of the encoding and
E. Quantum error correction
                                                                          decoding schemes.
   The protective measures discussed earlier can reduce the
error rate, but not eliminate errors completely. Reliable storage
and processing of information requires therefore a scheme for
correcting errors. In classical information processing, error
correction schemes are used extensively, but they cannot be
applied directly to quantum information. As a specific
example, in every step of a classical computation, the bits               FIG. 12. Quantum error correction scheme based on a three-
are renormalized, i.e., they may only assume values in specific           qubit code. On input, the first (uppermost) physical qubit contains
ranges that are identified with the logical values 0 or 1.                the logical information, while the ancilla qubits are initialized into
Clearly, this is a nonlinear process, which is not compatible             the state j0i. The input information is then encoded into the
with the basic operations of QIP. Renormalization is the first            logical qubit and the gate operation is performed. If a bit-flip
(and possibly most important) step in a chain of measures                 error occurs, it can be corrected during the decoding process. At
designed to maintain the integrity of the information. Another            the end, the first physical qubit contains again the logical
step is error detection and correction. A simple scheme that              information.

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-15
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


   Of specific interest are perfect codes: They can protect a             describes the evolution of a quantum system under a time-
qubit of information against general one qubit errors                     dependent Hamiltonian by an effective or averaged, time-
(Laflamme et al., 1996). For a single qubit, the possible                 independent Hamiltonian for times tk ¼ kτ0 , where τ0 is the
operations can be expanded in terms of the three Pauli                    duration of a cycle and k ≥ 0 is an integer. Several sequences
matrices and the unit operator. The last one corresponds to               of control pulses were developed for characterizing molecules,
perfect transmission (NOERR), the three Pauli matrices to                 quantum simulations, and similar tasks.
flips around the corresponding axes. For a system of N qubits,               As an example for the interference between DD and
the number of possible independent qubit error conditions is              controlled evolution, consider a NOT operation, which is
4N . Detecting these conditions requires extracting the infor-            applied in parallel to a minimal DD sequence consisting of
mation from the N −1 ancilla qubits. These N − 1 qubits form              two identical π pulses. The DD pulses are assumed to be short
a ðN − 1Þ2 -dimensional subspace, which must be at least 4N to            compared to the NOT operation, so the overall sequence can be
allow unequivocal distinction of all possible error conditions.           written as
The smallest number N of qubits that fulfills this condition is
N ¼ 5 and QEC codes realizing this minimum have indeed                          U NOTDD ¼ e−iðπ=4ÞI x e−iπI y e−iðπ=2ÞIx eþiπIy e−iðπ=4ÞI x
been proposed (Bennett et al., 1996; Laflamme et al., 1996) and
experimentally implemented (Knill et al., 2001; Zhang,                                   ¼ e−iðπ=4ÞI x eþiðπ=2ÞIx e−iðπ=4ÞI x ¼ 1;
Laflamme, and Suter, 2012; Kelly et al., 2015; Riste et al., 2015).
   So far, most implementations of QEC have concentrated on               where we assumed that the NOT gate rotates the qubit around
the elimination of single-qubit errors, i.e., errors that affect only     the x axis and the DD pulses around the y axis in the first
a single qubit. While this is often the dominant error mecha-             row of the equation. The result shows that the DD pulses have
nism, some types of environmental noise also act in a correlated          decoupled the qubit from the control field and the resulting
way on more than one qubit. A simple example is a magnetic                operation is not the intended one.
field acting on spin qubits if the source of the field is farther            It is therefore necessary to take the interaction between the
away from the qubits than the separation between them. This is            control gates and the decoupling operations into account.
the normal situation and in this case, it acts collectively on all        Basically, two solutions exist for this: (i) separating DD
the qubits as type (iii) in Sec. III.A.3. This situation is easier to     operations and gate operations in time or (ii) to apply the
correct by using decoherence-free subspaces than by using                 gate operations in the so-called “toggling frame,” which takes
error correction. The intermediate situation, where some qubits           the effect of the decoupling pulses into account.
are affected and others are not (or more weakly), can also be                For this toggling frame description, consider a system
tackled by QEC. In this case, more advanced QEC codes are                 governed by the Hamiltonian
required, which can detect and correct also errors that affect
more than one qubit (Lidar and Brun, 2013; Terhal, 2015).                                HðtÞ ¼ HS þ HC ðtÞ þ HSE þ HE ;                      ð17Þ

VI. PROTECTING UNITARY EVOLUTIONS                                         where HS describes the internal Hamiltonian of the qubit,
                                                                          HC ðtÞ is a time-dependent control Hamiltonian driving the
   The preceding section considered the preservation of a                 logical gates, HSE is the interaction of the qubit with the
quantum state (of one qubit) in the presence of environmental             environment, and HE describes the environmental degrees of
noise. The result is essentially a protected quantum memory: a            freedom. The goal is to implement gate operations protected
quantum state can be stored for a longer time. The present                against environmental noise.
                                                                                                R      The target operation is a unitary
                                                                                                       τ
section goes one step beyond this: it considers the evolution of          gate Uτ ¼ U g ⊗ T e−i 0 dtHE =ℏ that is not affected by the
a quantum state that is subject to a driving field (control
                                                                          system-environment interaction HSE . Here the gate operation
Hamiltonian) and environmental noise. The targeted evolution
                                                                          U g is a pure system operator, T is the Dyson time ordering
may implement a task in sensing or computing whose fidelity
                                                                          operator, and τ is the duration of the gate operation. The
decays over the task’s duration (Khodjasteh, Lidar, and Viola,
                                                                          second factor, which describes the effect of the environmental
2010; Souza, Álvarez, and Suter, 2012b) or as a function of
the task’s spatial extent (De Chiara et al., 2005; Álvarez and            Hamiltonian HE , does not affect the evolution of the system.
Suter, 2010; Zwick et al., 2012; Álvarez, Suter, and Kaiser,                 Protecting the system from the environmental noise while
2015) due to the environmental noise and imperfections of the             simultaneously driving logical gate operations can be
control Hamiltonians. The goal of mitigating the effect of the            achieved by using a standard DD sequence and inserting a
noisy environment remains, but in this case, care must be                 suitably adapted gate operation in short increments in the free
taken that the protection scheme does not interfere with the              precession periods of the DD sequence. Figure 13 illustrates
control field that drives the system to achieve the targeted              this for the XY-4 DD sequence: in the delays between the
evolution. The main problem is that the decoupling operations             DD pulses, the control Hamiltonian HCn is applied, where
introduced above decouple the qubit not only from the noise,              ðn ¼ 1; …; 5Þ indicates the period for which this Hamiltonian
but equally from all gate operations.                                     is active. The evolution of the system can then be written as

A. Combining decoupling with other control operations                             U ¼ U Nþ1 PN U N    P1 U 1 ¼ U Nþ1 ΠNn¼1 Pn U n ;        ð18Þ

  This task can be tackled by average Hamiltonian theory                  where N is the number of pulses of the DD sequence (N ¼ 4
(Haeberlen and Waugh, 1968; Blanes et al., 2009), which                   in the case of XY-4), Pn ¼ e−iπIα is the propagator describing

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-16
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


                                                                             Figure 14 shows the resulting protected gate, combining the
                                                                          gate operation and the DD cycle. While we discussed the
                                                                          example of the XY-4 sequence, the scheme is equally
                                                                          applicable to other DD schemes, provided the decomposition
                                                                          is adapted to that scheme.
                                                                             Other possible schemes for maintaining DD protection
FIG. 13. Pulse sequence for a protected single-qubit gate. A              during the gate operation were suggested by Viola, Lloyd,
single cycle of an XY-4 DD sequence is used to protect the gate           and Knill (1999), Cappellaro et al. (2009), Khodjasteh and
operation. The labels x and y mark the rotation axes of the DD            Viola (2009a, 2009b), Khodjasteh, Lidar, and Viola (2010),
pulses and HCn the gate operations.
                                                                          Ng, Lidar, and Preskill (2011), Khodjasteh, Bluhm, and Viola
                                                                          (2012), and Souza, Álvarez, and Suter (2012b). These
the nth DD inversion pulse, I α is the Cartesian component of             schemes can be considered as dynamically corrected gates,
the spin operator, and Un ¼ e−iHCn τn =ℏ is the evolution                 where the gate is built up along with the DD sequence
between two DD pulses. We assume that these periods are                   (Khodjasteh and Viola, 2009a, 2009b; Souza, Álvarez, and
short and the control Hamiltonians are time independent                   Suter, 2012b). Alternatively, one can define logical qubits,
within each period. We treat the DD pulses Pn as ideal                    where gates are designed to commute with the DD operations
rotations.                                                                (Viola, Lloyd, and Knill, 1999; Byrd and Lidar, 2002; Lidar,
   To find the required control Hamiltonians HCn , we rewrite             2008; West et al., 2010; Quiroz and Lidar, 2012). As in
Eq. (18) in the form                                                      protecting quantum memories, the control operations used for
                                                   ~                      DD can also introduce additional errors. A general scheme for
                         ~ n ¼ U Nþ1 ΠNn¼1 e−iHCn τn =ℏ ;
          U ¼ UNþ1 ΠNn¼1 U                                     ð19Þ       protecting gate operations against a fluctuating environment
                             ~ Cn ¼ T −1                                  and that is robust against experimental errors can be based on
where the Hamiltonians H              n HCn T n describe the con-         a suitable hybridization of DD with robust pulses for gen-
trol fields in the toggling frame (Haeberlen, 1976) of the
                                                                          erating the protected gates (Souza, Álvarez, and Suter, 2012b).
DD sequence, which are defined by the transformations
T n ¼ Pn−1 Pn−2    P1 , and include the limiting cases T 1 ¼
                                                                          B. Examples
T Nþ1 ¼ 1 (identity). This approach guarantees first order
protection of any operation interlaced with a suitable DD                    As an example of a protected one-qubit operation, we
sequence.                                                                 consider the NOT gate protected with an XY-4 sequence shown
   As a specific example, we choose the XY-4 DD sequence to               in Fig. 14. The pulse sequence consists of the four DD pulses
protect the gate operations NOOP (no operation, i.e., identity),          shown as wide green rectangles and the five partial gate
NOT, Hadamard, and phase gates, which can be represented as               operations shown as narrow red rectangles. The gate pulses
                                                                  add up to the π pulse of the NOT operation. For the data shown
      1 0          0 1          1 1 1              1 0
            ;              ; pﬃﬃ            ;            ; ð20Þ           as green diamonds, eight refocusing pulses, according to the
      0 1          1 0            2 1 −1           0 i                    XY-8 sequence (Gullion, Baker, and Conradi, 1990), and nine
                                                                          delays were used. The experimental data show that the
respectively. To protect these gates, we first split them into            combination with the DD operations is very effective in
segments that can be interleaved with the DD sequence. A
possible decomposition is
                                                                                                         1

  NOT∶ ðπ=8Þ0 − ðπ=4Þ0 − ðπ=4Þ0 − ðπ=4Þ0 − ðπ=8Þ0 ;                                                                     XY4




                                                                               Quantum gate fidelity
                                                                                                                   te
                                                                                                             unpro
    H∶ ðπ=4Þ3π=2 − ðπ=2Þ0 − ð0Þ0 − ðπ=2Þ0 − ðπ=4Þπ=2 ;
Phase∶ ð0Þ0 − ðπ=2Þ0 − ðπ=2Þπ=2 − ðπ=2Þ0 − ð0Þ0 ;              ð21Þ                                             cted              x 135                      XY8
                                                                                                       0.9
                                                                                                                                    x 270

                                                                                                                                                 protected
with time running from left to right. Here ðθÞϕ ¼
e−iθðIx cos ϕ−Iy sin ϕÞ denotes a pulse with flip angle θ and phase
ϕ. The short line between the pulses denotes a variable
delay for adjusting the overall gate duration. ð0Þ0 denotes a                                          0.8
“pulse” with zero amplitude but nonzero duration for
                                                                                                               0.1            1             10
balancing the delays in the DD sequence: the duration of
                                                                                                                        Gate duration ( s)
ð0Þ0 in the Hadamard gate, e.g., is the same as that of the
ðπ=2Þ pulse. The decomposition of the gates is not unique.                FIG. 14. Effect of protecting a NOT gate by DD with a single
An optimal decomposition uses all delays. We choose a                     XY-4 cycle (red squares) or an XY-8 cycle (green diamonds).
decomposition that is sufficiently symmetric to eliminate                 The unprotected counterpart is represented by blue circles. The
odd order terms in the Magnus expansion (Burum, 1981;                     process fidelity of the gate operation is shown as a function of
Souza, Álvarez, and Suter, 2012a). The transformation into                the gate duration. The results show that the dephasing due to the
the toggling frame changes the phases to 0 − 0 − π − π − 0,               fluctuating environment is slowed down by several orders of
3π=2 − 0 − 0 − π − π=2, and 0 − π − π=2 − π − 0 for the                   magnitude by the combination of DD with the gate operation as
NOT, Hadamard, and phase gates, respectively.                             shown in the inset. From Zhang et al., 2014.

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-17
                                                    Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


arresting the dephasing process due to the fluctuating envi-                                        match the inverse of the coupling constant that was used for
ronment (Zhang et al., 2014). The dephasing time is roughly                                         the two-qubits gates. A similar example was also performed
proportional to the number of refocusing pulses. In this                                            on an effective qubit in a semiconductor quantum dot (Barthel
example, the fluctuations are caused by nuclear spins under-                                        et al., 2010).
going mutual spin flips, together with more remote spins of
the spin bath. These dynamically corrected gates were also                                          VII. ENVIRONMENTAL NOISE AND SENSING
implemented on other NV center experiments (Rong et al.,
2014) and on nuclear spins in NMR (Souza, Álvarez, and                                              A. Sensing
Suter, 2012b). The operation can be made robust against
imperfections of the control fields by implementing the gate                                           Quantum systems can be sensitive probes of the environ-
as a robust pulse known as BB1 (Wimperis, 1994), which is                                           ment at molecular or atomic scales. Novel quantum technol-
less sensitive to flip-angle errors (Souza, Álvarez, and                                            ogies achieving high sensitivity at the nanoscale are based on
Suter, 2012b).                                                                                      spin probes serving as magnetometers (Balasubramanian et al.,
   The approach can be generalized to systems with multiple                                         2008; Taylor et al., 2008; de Lange et al., 2011), thermom-
qubits, where the need to protect unitary transformations is                                        eters (Kucsko et al., 2013; Neumann et al., 2013; Toyli et al.,
actually more evident, particularly in hybrid systems combin-                                       2013), sensors for imaging (Shemesh, Álvarez, and Frydman,
ing different types of qubits. A good example is NV centers in                                      2013; Steinert et al., 2013; Grinolds et al., 2014), or
                                                                                                    monitoring biological, chemical, or physical processes
diamond (Doherty et al., 2013), where electron spins are
                                                                                                    (Mittermaier and Kay, 2006; Smith et al., 2012; Álvarez,
coupled to nuclear spins. Since the magnetic moment of the
                                                                                                    Shemesh, and Frydman, 2013; Zwick, Álvarez, and Kurizki,
electron spin is more than 3 orders of magnitude larger than
                                                                                                    2016). The protection schemes that have been discussed can
that of the nuclear spins, gate operations on the nuclear spins
                                                                                                    contribute in two ways to improving such sensors: they can
tend to last much longer than those for the electron and also
                                                                                                    (i) suppress the effect of noise that interferes with the targeted
longer than the dephasing time of the electron spin. As shown
                                                                                                    measurement, e.g., suppress magnetic noise that disturbs the
in Fig. 15, an attempt to implement a controlled rotation
                                                                                                    measurement of a temperature, and (ii) the protection schemes
(CROT) gate with the electron spin as the control qubit and the
                                                                                                    can be used to filter the environmental interaction to select
nuclear spin as the target qubit results in a decay rather than an
                                                                                                    components at specific frequencies (zero or nonzero).
oscillation. The corresponding data are represented by the thin
                                                                                                       The effect of an increased coherence time can be seen in the
line. If a protection scheme is implemented for the electron
                                                                                                    example of a magnetic field measurement, using a spin as
spin by a sequence of inversion pulses, the dephasing is
                                                                                                    the probe. If the magnetic field is static, the spin precesses at
canceled and the experimental data, represented by the red
                                                                                                    the Larmor frequency ωz ¼ ℏγB0, acquiring a phase propor-
spheres, follow almost perfectly the behavior predicted for an
                                                                                                    tional to the magnetic field B0 and the interaction time t. This
ideal gate (thick red solid curve). Other examples of two-qubit
                                                                                                    interaction time is limited by the dephasing time τϕ . Extending
gates were also implemented with NV centers (Sar et al.,
                                                                                                    the dephasing time therefore increases the sensitivity.
2012) by applying DD to the control qubit (the electron spin).
                                                                                                       If the magnetic field oscillates, DD sequences are useful not
In this case, the delay between the DD pulses was adjusted to
                                                                                                    only to prolong the coherence time, but also to select the
                                                                                                    specific frequency component that the sensor measures. This
                          excitation                                        detection
                                                                                                    frequency is given by the inverse of the cycle time, where a
    Laser
                                                                                                    cycle consists of two inversion pulses (Taylor et al., 2008;
    Microwave                       excitation
                                                        DD
                                                     protection      detection
                                                                                                    Hall et al., 2010; de Lange et al., 2011; Pham et al., 2012).
                                                                                                    Composite pulses generating “rotary echoes” (Solomon,
    Radiofrequency                        protected CROT                                            1959) have also been applied to eliminate pulse inhomoge-
                                                                                                    neities during continuous driving for high-sensitivity sensing
                          1.0                                                                       applications (Gustavsson et al., 2012; Aiello, Hirose, and
                                                       ideal                                        Cappellaro, 2013).
                          0.9


              PL signal
                                                                                                       An important application of this approach is the determi-
                          0.8                                                                       nation of the spectrum of the environmental noise. As
                          0.7                                                                       discussed in Sec. IV.C, DD sequences generate filter functions
                                                 unprotected            protected                   that allow only specific frequency components to act on the
                                0                              200                      400         system. The width of these pass bands can be made arbitrarily
                                                                       Time t ( s)
                                                                                                    narrow by repeating DD cycles. The spectral density of the
                                                                                                    environmental noise can thus be determined by performing a
FIG. 15. Protected CROT gate in a single NV center in diamond.
The refocusing pulses are applied to the electron spin qubits as                                    series of measurements with different frequencies of the filter
microwave pulses, while the nuclear spin qubit is rotated condi-                                    function peak, using either continuous fields (Slichter and
tional on the electron spin qubits being initially in state j1i by the                              Ailion, 1964; Ailion and Slichter, 1965; Look and Lowe,
radio-frequency pulses. The bottom part shows the measured                                          1966; Almog et al., 2011; Loretz, Rosskopf, and Degen, 2013;
population of the initial state with and without protection. In the                                 Yan et al., 2013) or sequences of pulses (Meriles et al., 2010;
absence of protection, it dephases rapidly, while the evolution in                                  Álvarez and Suter, 2011; Bylander et al., 2011). More
the presence of protection remains close to the ideal evolution.                                    advanced methods were developed for scenarios where a
From Zhang and Suter, 2015.                                                                         single delta filter function approximation is not sufficient for

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016                                        041001-18
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


                                                                          instrumental for monitoring molecular motion (Kimmich,
                                                                          1997) or finding and characterizing phase transitions
                                                                          (Borsa and Rigamonti, 1991). Techniques for scanning the
                                                                          noise spectrum based on dynamical control by CPMG
                                                                          sequences or continuous wave irradiation are building blocks
                                                                          of modern magnetic resonance applications. They are widely
                                                                          used for distinguishing between different sources of noise that
                                                                          have different correlation times, for measuring diffusion rates
                                                                          (Carr and Purcell, 1954; Stejskal, 1965; Stejskal and Tanner,
                                                                          1965; Packer, 1973), and for measuring protein dynamics
                                                                          (Mittermaier and Kay, 2006). In most of these studies, some
                                                                          assumptions have been made about the shape of the noise
                                                                          spectrum and then determined the free parameters of their
                                                                          model from experimental data. Noise spectroscopy may be
FIG. 16. Example of environmental noise spectra determined by
                                                                          considered to go beyond this, as its focus is the determination
DD noise spectroscopy. A narrow-band filter function scans the
                                                                          of the full noise spectrum, with no prior assumptions (Meriles
noise spectra (shaded curve). The reconstructed noise spectra are
shown by the blue triangles and red circles for an unmodulated            et al., 2010; Almog et al., 2011; Álvarez and Suter, 2011;
and a modulated environment, respectively. From Álvarez and               Bylander et al., 2011). Besides being useful for characterizing
Suter, 2011.                                                              the environment and then designing optimal decoupling
                                                                          methods, it has been shown to be important for determining
                                                                          pore structures of biological systems that are characterized by
the filter shape (Álvarez and Suter, 2011; Bar-Gill et al., 2012;         multiple noise correlation times (Stepisnik, 1993; Callaghan
Kotler et al., 2013).                                                     and Stepisnik, 1995; Lasic, Stepisnik, and Mohoric, 2006;
   Figure 16 shows, as an example, the noise spectrum                     Stepisnik et al., 2006; Álvarez, Shemesh, and Frydman, 2013;
generated by 1 H nuclear spins. It was determined by using                Shemesh, Álvarez, and Frydman, 2013) and it is being
13
   C nuclear spins as probes and applying different DD                    exploited for magnetic resonance spectroscopy and imaging
sequences to generate suitable filter functions (Álvarez and              at the nanoscale, based on sensing noise fluctuations gen-
Suter, 2011). The blue triangles represent the data points of the         erated by a host system on single spins in diamonds (Mamin
noise spectrum. The 1 H nuclear spins are coupled by magnetic             et al., 2013; McGuinness et al., 2013; Shi et al., 2013;
dipole-dipole interactions, which generate energy-preserving              Staudacher et al., 2013; Steinert et al., 2013; Grinolds et al.,
flip-flops where two coupled spins with antiparallel orientation          2014; Loretz et al., 2014).
simultaneously change their orientation, e.g., ↑↓ ↔ ↓↑. With                 Most of these approaches rely on a single frequency
no additional interaction, the noise spectrum of this system has a        component of the filter function for probing the environmental
maximum at zero frequency and decreases monotonously with                 noise. However, the nonequidistant sequence proposed by
increasing frequency, as shown by the blue triangles. A different         (Uhrig (2007) has motivated the exploration of filter functions
spectral distribution can be obtained by applying a control field         with multiple frequency components. In particular nonequi-
to the 1 H nuclear spins that forces a coherent rotation around an        distant sequences have been useful for filtering out intrinsic
axis in the x-y plane. As shown by the red circles, the spectral          decoherence effects and pulse imperfections in probing
density of the spin noise is then no longer monotonously                  targeted noise spectra by changing the pulse distribution
decreasing, but reaches a maximum at a frequency of 3.85 kHz,             while keeping the total duration of the sequence and the
the frequency at which the spins are rotated.                             number of pulses constant. This has been put forward as a new
   If the noise does not follow Gaussian statistics, the second           magnetic resonance imaging (MRI) source of contrast (Jenista
order approximation of Eq. (16) is not exact. The telegraph               et al., 2009) and has led to the design of sequences for
noise (Anderson, 1954; Efros and Rosen, 1997; Falci et al.,               selective probing of specific parameters of the noise spectrum
2004; Bergli and Faoro, 2007; Cywinski et al., 2008; Smith                by generating incoherent modulations of the spin signal for
et al., 2012) represented in Fig. 6 is a typical example of non-          determining chemical identities derived from chemical shifts
Gaussian noise. In these cases, higher-order terms must be                (Smith et al., 2012) or restricted diffusion lengths in pore
considered to describe the dephasing, but usually they become             structures with higher sensitivity (Álvarez, Shemesh, and
small for large numbers of pulses (Cywinski et al., 2008).                Frydman, 2013; Shemesh, Álvarez, and Frydman, 2013).

B. Examples                                                               VIII. CONCLUSIONS AND OUTLOOK

   Probing the spectrum of environmental noise has been used                 This Colloquium gives an introduction into some of the
extensively in the field of relaxometry (Redfield, 1957;                  strategies that were developed for preventing superpositions of
Abragam, 1961; Kimmich, 1997). It uses the fact that the                  quantum states from losing their phase coherence due to pure
relaxation rate of nuclear and electronic spins is most sensitive         dephasing noise from environmental perturbations. The goal
to frequency components of the environmental noise at nωz ,               of these techniques is to control the evolution of the target
where ωz is the Larmor frequency of the spins and n takes                 system in such a way that it remains as close as possible to the
the values 0, 1, and 2, depending on the type of interaction              ideal evolution, without being affected by unwanted and
that drives the process. Measurements based on this are                   uncontrolled interactions with other degrees of freedom.

Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-19
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


Some of the techniques discussed here, in particular, dynami-             Altshuler, B. L., P. A. Lee, and W. R. Webb, 2012, Mesoscopic
cal decoupling, require near-perfect suppression of experi-                Phenomena in Solids (Elsevier, New York).
mental imperfections by robust design of the sequence. A                  Álvarez, G. A., A. Ajoy, X. Peng, and D. Suter, 2010, Phys. Rev. A
number of approaches for solving this challenging task have                82, 042306.
been proposed, but this remains an active field of research.              Álvarez, G. A., N. Shemesh, and L. Frydman, 2013, Phys. Rev. Lett.
   Similar techniques had previously been developed in                     111, 080404.
specific communities such as in magnetic resonance, atomic                Álvarez, G. A., A. M. Souza, and D. Suter, 2012, Phys. Rev. A 85,
                                                                           052324.
and molecular physics, or in QIP. The different methods
                                                                          Álvarez, G. A., and D. Suter, 2010, Phys. Rev. Lett. 104, 230403.
discussed here have different requirements as well as different
                                                                          Álvarez, G. A., and D. Suter, 2011, Phys. Rev. Lett. 107, 230501.
advantages and disadvantages, e.g., in terms of the type of               Álvarez, G. A., D. Suter, and R. Kaiser, 2015, Science 349, 846.
errors they can catch or they require different overhead in               Anderson, P. W., 1954, J. Phys. Soc. Jpn. 9, 316.
terms of additional qubits and additional gate operations.                Anderson, P. W., and P. R. Weiss, 1953, Rev. Mod. Phys. 25,
Achieving the goal of an unperturbed evolution in a specific               269.
system and application normally requires a combination of                 Balasubramanian, G., et al., 2008, Nature (London) 455, 648.
several of those approaches.                                              Bar-Gill, N., L. M. Pham, C. Belthangady, D. L. Sage, P. Cappellaro,
   The implementation of suitable protection schemes is one                J. R. Maze, M. D. Lukin, A. Yacoby, and R. Walsworth, 2012,
of the most important prerequisites for making quantum                     Nat. Commun. 3, 858.
simulations and computations scalable and reliable, as well               Barthel, C., J. Medford, C. M. Marcus, M. P. Hanson, and A. C.
as for improving the sensitivity of various type of quantum                Gossard, 2010, Phys. Rev. Lett. 105, 266808.
sensors. In the case of sensing applications, the protection              Bennett, C. H., D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters,
scheme itself must be fully integrated with the control                    1996, Phys. Rev. A 54, 3824.
operations that drive the system in probing the environment.              Bergli, J., and L. Faoro, 2007, Phys. Rev. B 75, 054515.
Such schemes are currently developed in various fields to                 Biercuk, M. J., H. Uys, A. P. VanDevender, N. Shiga, W. M. Itano,
optimize quantum mechanical sensors for combining high                     and J. J. Bollinger, 2009a, Phys. Rev. A 79, 062324.
                                                                          Biercuk, M. J., H. Uys, A. P. VanDevender, N. Shiga, W. M. Itano,
sensitivity with high spatial resolution as well as for analyzing
                                                                           and J. J. Bollinger, 2009b, Nature (London) 458, 996.
environmental noise at the nanometer scale.
                                                                          Blanes, S., F. Casas, J. Oteo, and J. Ros, 2009, Phys. Rep. 470, 151.
                                                                          Bloembergen, N., E. Purcell, and R. Pound, 1947, Nature (London)
ACKNOWLEDGMENTS                                                            160, 475.
                                                                          Blum, K., 2012, Density Matrix Theory and Applications (Springer-
   We gratefully acknowledge useful discussions with                       Verlag, Berlin/Heidelberg).
Christiane Koch, who suggested that we write this review                  Boltzmann, L., 1877, in Über die Beziehung eines allgemeinen
and provided advice throughout the project, and J. Stolze and              mechanischen Satzes zum zweiten Hauptsatze der Wärmetheorie,
G. Uhrig for careful reading of the manuscript and many useful             Vol. II 75 (Sitzungsberichte der Akademie der Wissenschaften,
suggestions. During the past years, we were fortunate enough               Wien), pp. 67–73.
to work on these subjects with many gifted and dedicated                  Borsa, F., and A. Rigamonti, 1991, “Topics in current physics,”
researchers, including M. A. Ali Ahmed, A. Ajoy, G. Bensky,                in Structural Phase Transitions II, Vol. 45 (Springer, Berlin/
L. Frydman, G. Kurizki, P. R. Levstein, D. A Lidar, S. Pasini,             Heidelberg), pp. 83–175.
H. M. Pastawski, X. Peng, G. Quiroz, N. Shemesh, P. E. S.                 Bortz, M., and J. Stolze, 2007, Phys. Rev. B 76, 014304.
Smith, A. M. Souza, G. Uhrig, J. Zhang, and A. Zwick. Many                Breuer, H.-P., and F. Petruccione, 2007, The Theory of Open
useful discussions took place during the meetings organized by             Quantum Systems (Oxford University Press, New York).
the European Quantum Control Network Quaint. This work                    Brown, K. R., A. W. Harrow, and I. L. Chuang, 2004, Phys. Rev. A
                                                                           70, 052318.
was supported by the DFG through Grants No. Su 192/24-1 and
                                                                          Burum, D., 1981, Phys. Rev. B 24, 3684.
No. Su 192/31-1. G. A. A. acknowledges the support of the
                                                                          Burum, D. P., and W. K. Rhim, 1979, J. Chem. Phys. 71, 944.
European Commission under the Marie Curie Intra-European
                                                                          Bylander, J., S. Gustavsson, F. Yan, F. Yoshihara, K. Harrabi, G.
Fellowship for career Development Grant No. PIEF-GA-2012-                  Fitch, D. G. Cory, Y. Nakamura, J. Tsai, and W. D. Oliver, 2011,
328605.                                                                    Nat. Phys. 7, 565.
                                                                          Byrd, M. S., and D. A. Lidar, 2002, Phys. Rev. Lett. 89, 047901.
                                                                          Caldeira, A. O., and A. J. Leggett, 1983a, Physica A (Amsterdam)
REFERENCES                                                                 121, 587.
Abragam, A., 1961, The Principles of Nuclear Magnetism (Oxford            Caldeira, A. O., and A. J. Leggett, 1983b, Ann. Phys. (N.Y.) 149,
 University Press, Oxford).                                                374; 153, 445(E) (1984).
Aiello, C. D., M. Hirose, and P. Cappellaro, 2013, Nat. Commun. 4,        Callaghan, P. T., and J. Stepisnik, 1995, J. Magn. Reson. 117, 118.
 1419.                                                                    Cappellaro, P., L. Jiang, J. S. Hodges, and M. D. Lukin, 2009, Phys.
Ailion, D. C., and C. P. Slichter, 1965, Phys. Rev. 137, A235.             Rev. Lett. 102, 210502.
Ajoy, A., G. A. Álvarez, and D. Suter, 2011, Phys. Rev. A 83,             Carr, H., and E. Purcell, 1954, Phys. Rev. 94, 630.
 032303.                                                                  Carravetta, M., O. G. Johannessen, and M. H. Levitt, 2004, Phys.
Ali Ahmed, M. A., G. A. Álvarez, and D. Suter, 2013, Phys. Rev. A          Rev. Lett. 92, 153003.
 87, 042309.                                                              Cho, H., P. Cappellaro, D. G. Cory, and C. Ramanathan, 2006, Phys.
Almog, I., Y. Sagi, G. Gordon, G. Bensky, G. Kurizki, and N.               Rev. B 74, 224434.
 Davidson, 2011, J. Phys. B 44, 154006.                                   Chuang, I. L., and Y. Yamamoto, 1996, Phys. Rev. Lett. 76, 4281.


Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-20
                               Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


Clausen, J., G. Bensky, and G. Kurizki, 2010, Phys. Rev. Lett. 104,       Jalabert, R. A., and H. M. Pastawski, 2001, Phys. Rev. Lett. 86,
  040401.                                                                   2490.
Cywinski, L., R. M. Lutchyn, C. P. Nave, and S. DasSarma, 2008,           Jenista, E. R., A. M. Stokes, R. T. Branca, and W. S. Warren, 2009,
  Phys. Rev. B 77, 174509.                                                  J. Chem. Phys. 131, 204510.
De Chiara, G., D. Rossini, S. Montangero, and R. Fazio, 2005, Phys.       Jozsa, R., 1994, J. Mod. Opt. 41, 2315.
  Rev. A 72, 012323.                                                      Kachru, R., T. Mossberg, and S. Hartmann, 1980, J. Phys. B 13,
Dehmelt, H., 1990, Rev. Mod. Phys. 62, 525.                                 L363.
de Lange, G., D. Ristè, V. V. Dobrovitski, and R. Hanson, 2011,           Kelly, J., et al., 2015, Nature (London) 519, 66.
  Phys. Rev. Lett. 106, 080802.                                           Kempe, J., D. Bacon, D. A. Lidar, and K. B. Whaley, 2001, Phys.
de Lange, G., Z. H. Wang, D. Ristè, V. V. Dobrovitski, and R.               Rev. A 63, 042307.
  Hanson, 2010, Science 330, 60.                                          Khaneja, N., T. Reiss, C. Kehlet, T. Schulte-Herbrüggen, and S.
Dementyev, A. E., D. Li, K. MacLean, and S. E. Barrett, 2003, Phys.         Glaser, 2005, J. Magn. Reson. 172, 296.
  Rev. B 68, 153302.                                                      Khodjasteh, K., H. Bluhm, and L. Viola, 2012, Phys. Rev. A 86,
Dhar, D., L. K. Grover, and S. M. Roy, 2006, Phys. Rev. Lett. 96,           042329.
  100405.                                                                 Khodjasteh, K., T. Erdélyi, and L. Viola, 2011, Phys. Rev. A 83,
Dieks, D., 1982, Phys. Lett. A 92, 271.                                     020305.
Doherty, M. W., N. B. Manson, P. Delaney, F. Jelezko, J. Wrachtrup,       Khodjasteh, K., and D. Lidar, 2005, Phys. Rev. Lett. 95, 180501.
  and L. C. L. Hollenberg, 2013, Phys. Rep. 528, 1.                       Khodjasteh, K., and D. A. Lidar, 2007, Phys. Rev. A 75, 062310.
Dong, Y., R. G. Ramos, D. Li, and S. E. Barrett, 2008, Phys. Rev.         Khodjasteh, K., D. A. Lidar, and L. Viola, 2010, Phys. Rev. Lett. 104,
  Lett. 100, 247601.                                                        090501.
Du, J., X. Rong, N. Zhao, Y. Wang, J. Yang, and R. B. Liu, 2009,          Khodjasteh, K., and L. Viola, 2009a, Phys. Rev. A 80, 032314.
  Nature (London) 461, 1265.                                              Khodjasteh, K., and L. Viola, 2009b, Phys. Rev. Lett. 102, 080501.
Efros, A., and M. Rosen, 1997, Phys. Rev. Lett. 78, 1110.                 Kimmich, R., 1997, NMR Tomography, Diffusometry, Relaxometry
Essen, L., and J. V. L. Parry, 1955, Nature (London) 176, 280.              (Springer, Berlin).
Facchi, P., D. A. Lidar, and S. Pascazio, 2004, Phys. Rev. A 69,          Klauder, J. R., and P. W. Anderson, 1962, Phys. Rev. 125, 912.
  032314.                                                                 Knill, E., R. Laflamme, R. Martinez, and C. Negrevergne, 2001,
Facchi, P., S. Tasaki, S. Pascazio, H. Nakazato, A. Tokuse, and D.          Phys. Rev. Lett. 86, 5811.
  Lidar, 2005, Phys. Rev. A 71, 022302.                                   Knill, E., R. Laflamme, and L. Viola, 2000, Phys. Rev. Lett. 84,
Falci, G., A. D’Arrigo, A. Mastellone, and E. Paladino, 2004, Phys.         2525.
  Rev. A 70, 040101.                                                      Knill, E., R. Laflamme, and W. H. Zurek, 1998, Science 279, 342.
Feynman, R. P., and F. L. Vernon, Jr., 1963, Ann. Phys. (N.Y.) 24,        Koch, C. P., 2016, arXiv:1603.04417.
  118.                                                                    Kofman, A. G., and G. Kurizki, 2001, Phys. Rev. Lett. 87, 270405.
Franzoni, M. B., R. H. Acosta, H. M. Pastawski, and P. R. Levstein,       Kofman, A. G., and G. Kurizki, 2004, Phys. Rev. Lett. 93, 130406.
  2012, Phil. Trans. R. Soc. A 370, 4713.                                 Kotler, S., N. Akerman, Y. Glickman, and R. Ozeri, 2013, Phys. Rev.
Franzoni, M. B., and P. R. Levstein, 2005, Phys. Rev. B 72, 235410.         Lett. 110, 110503.
Franzoni, M. B., P. R. Levstein, J. Raya, and J. Hirschinger, 2008,       Krojanski, H. G., and D. Suter, 2004, Phys. Rev. Lett. 93, 090501.
  Phys. Rev. B 78, 115407.                                                Kucsko, G., P. C. Maurer, N. Y. Yao, M. Kubo, H. J. Noh, P. K. Lo,
Gaudin, M., 1976, J. Phys. France 37, 1087.                                 H. Park, and M. D. Lukin, 2013, Nature (London) 500, 54.
Gordon, G., G. Kurizki, and D. A. Lidar, 2008, Phys. Rev. Lett. 101,      Kurnit, N., I. Abella, and S. Hartmann, 1964, Phys. Rev. Lett. 13,
  010403.                                                                   567.
Goussev, A., R. A. Jalabert, H. M. Pastawski, and D. A. Wisniacki,        Ladd, T. D., F. Jelezko, R. Laflamme, Y. Nakamura, C. Monroe, and
  2012, Scholarpedia 7, 11687.                                              J. L. O’Brien, 2010, Nature (London) 464, 45.
Grebenkov, D. S., 2007, Rev. Mod. Phys. 79, 1077.                         Laflamme, R., C. Miquel, J. P. Paz, and W. H. Zurek, 1996, Phys.
Green, T. J., J. Sastrawan, H. Uys, and M. J. Biercuk, 2013, New J.         Rev. Lett. 77, 198.
  Phys. 15, 095004.                                                       Lasic, S., J. Stepisnik, and A. Mohoric, 2006, J. Magn. Reson. 182,
Grinolds, M. S., M. Warner, K. D. Greve, Y. Dovzhenko, L. Thiel,            208.
  R. L. Walsworth, S. Hong, P. Maletinsky, and A. Yacoby, 2014,           Levitt, M., and R. Freeman, 1979, J. Magn. Reson. 33, 473.
  Nat. Nanotechnol. 9, 279.                                               Levitt, M. H., 1986, in Encyclopedia of Magnetic Resonance
Gullion, T., D. B. Baker, and M. S. Conradi, 1990, J. Magn. Reson.          (Wiley Online Library).
  89, 479.                                                                Levitt, M. H., 2012, Annu. Rev. Phys. Chem. 63, 89.
Gustavsson, S., et al., 2012, Phys. Rev. Lett. 108, 170503.               Levitt, M. H., and R. Freeman, 1981, J. Magn. Reson. 43, 502.
Haeberlen, U., 1976, in Advances in Magnetic Resonance, Advances          Levitt, M. H., R. Freeman, and T. Frenkiel, 1982, J. Magn. Reson. 47,
  in magnetic resonance, Vol. 1, edited by J. Waugh, Chap. 1                328.
  (Academic Press, New York).                                             Levstein, P. R., G. Usaj, and H. M. Pastawski, 1998, J. Chem. Phys.
Haeberlen, U., and J. S. Waugh, 1968, Phys. Rev. 175, 453.                  108, 2718.
Hahn, E., 1950, Phys. Rev. 80, 580.                                       Levy, J., 2002, Phys. Rev. Lett. 89, 147902.
Hall, L. T., C. D. Hill, J. H. Cole, and L. C. L. Hollenberg, 2010,       Li, D., A. E. Dementyev, Y. Dong, R. G. Ramos, and S. E. Barrett,
  Phys. Rev. B 82, 045208.                                                  2007, Phys. Rev. Lett. 98, 190401.
Hauke, P., F. M. Cucchietti, L. Tagliacozzo, I. Deutsch, and M.           Li, D., Y. Dong, R. G. Ramos, J. D. Murray, K. MacLean, A. E.
  Lewenstein, 2012, Rep. Prog. Phys. 75, 082401.                            Dementyev, and S. E. Barrett, 2008, Phys. Rev. B 77, 214306.
Hepp, K., and E. H. Lieb, 1973, Helv. Phys. Acta 46, 573.                 Lidar, D. A., 2008, Phys. Rev. Lett. 100, 160506.
Hodgson, T. E., L. Viola, and I. D’Amico, 2010, Phys. Rev. A 81,          Lidar, D. A., and T. A. Brun, 2013, Eds., Quantum Error Correction
  062321.                                                                   (Cambridge University Press, Cambridge, England).


Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016            041001-21
                                Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


Lidar, D. A., I. L. Chuang, and K. B. Whaley, 1998, Phys. Rev. Lett.       Rhim, W.-K., D. D. Elleman, and R. W. Vaughan, 1973, J. Chem.
  81, 2594.                                                                  Phys. 59, 3740.
Look, D. C., and I. J. Lowe, 1966, J. Chem. Phys. 44, 2995.                Rhim, W. K., A. Pines, and J. S. Waugh, 1970, Phys. Rev. Lett. 25, 218.
Loretz, M., S. Pezzagna, J. Meijer, and C. L. Degen, 2014, Appl.           Ridge, C. D., L. F. O’Donnell, and J. D. Walls, 2014, Phys. Rev. B
  Phys. Lett. 104, 033102.                                                   89, 024404.
Loretz, M., T. Rosskopf, and C. L. Degen, 2013, Phys. Rev. Lett. 110,      Riste, D., S. Poletto, M. Z. Huang, A. Bruno, V. Vesterinen, O. P.
  017602.                                                                    Saira, and L. DiCarlo, 2015, Nat. Commun. 6, 6983.
Loschmidt, J., 1876, in Über den Zustand des Wärmegleichgewichts           Rong, X., J. Geng, Z. Wang, Q. Zhang, C. Ju, F. Shi, C.-K. Duan, and
  eines Systems von Körpern mit Rücksicht auf die Schwerkraft,               J. Du, 2014, Phys. Rev. Lett. 112, 050503.
  Vol. II 73 (Sitzungsberichte der Akademie der Wissenschaften,            Ryan, C. A., J. S. Hodges, and D. G. Cory, 2010, Phys. Rev. Lett.
  Wien), pp. 128–142.                                                        105, 200402.
Lovric, M., D. Suter, A. Ferrier, and P. Goldner, 2013, Phys. Rev.         Sánchez, C. M., H. M. Pastawski, and P. R. Levstein, 2007, Physica B
  Lett. 111, 020503.                                                         (Amsterdam) 398, 472.
Mádi, Z. L., B. Brutscher, T. Schulte-Herbrüggen, R. Brüschweiler,         Sar, T. v. d., Z. H. Wang, M. S. Blok, H. Bernien, T. H. Taminiau,
  and R. R. Ernst, 1997, Chem. Phys. Lett. 268, 300.                         D. M. Toyli, D. A. Lidar, D. D. Awschalom, R. Hanson, and V. V.
Magnus, W., 1954, Commun. Pure Appl. Math. 7, 649.                           Dobrovitski, 2012, Nature (London) 484, 82.
Mamin, H. J., M. Kim, M. H. Sherwood, C. T. Rettner, K. Ohno,              Sauter, T., R. Blatt, W. Neuhauser, and P. Toschek, 1986, Opt.
  D. D. Awschalom, and D. Rugar, 2013, Science 339, 557.                     Commun. 60, 287.
Mansfield, P., 1971, J. Phys. C 4, 1444.                                   Schlosshauer, M., 2005, Rev. Mod. Phys. 76, 1267.
Maudsley, A. A., 1986, J. Magn. Reson. 69, 488.                            Schrödinger, E., 1952, Brit. J. Philos. Sci. III, 233.
McGuinness, L. P., et al., 2013, New J. Phys. 15, 073042.                  Shemesh, N., G. A. Álvarez, and L. Frydman, 2013, J. Magn. Reson.
Meiboom, S., and D. Gill, 1958, Rev. Sci. Instrum. 29, 688.                  237, 49.
Meriles, C. A., L. Jiang, G. Goldstein, J. S. Hodges, J. Maze, M. D.       Shi, F., X. Kong, P. Wang, F. Kong, N. Zhao, R.-B. Liu, and J. Du,
  Lukin, and P. Cappellaro, 2010, J. Chem. Phys. 133, 124105.                2013, Nat. Phys. 10, 21.
Merrill, J. T., and K. R. Brown, 2014, “Progress in compensating           Shiddiq, M., D. Komijani, Y. Duan, A. Gaita-Ariño, E. Coronado,
  pulse sequences for quantum computation,” in Quantum Informa-              and S. Hill, 2016, Nature (London) 531, 348.
  tion and Computation for Chemistry (John Wiley & Sons, Inc.,             Shim, J. H., I. Niemeyer, J. Zhang, and D. Suter, 2012, Europhys.
  New York), pp. 241–294.                                                    Lett. 99, 40004.
Misra, B., and E. C. G. Sudarshan, 1977, J. Math. Phys. (N.Y.) 18,         Shor, P. W., 1995, Phys. Rev. A 52, R2493.
  756.                                                                     Slichter, C. P., 1990, Principles of Magnetic Resonance (Springer,
Mittermaier, A., and L. Kay, 2006, Science 312, 224.                         Berlin, Heidelberg).
Müller, L., A. Kumar, T. Baumann, and R. R. Ernst, 1974, Phys. Rev.        Slichter, C. P., and D. Ailion, 1964, Phys. Rev. 135, A1099.
  Lett. 32, 1402.                                                          Smith, P. E. S., G. Bensky, G. A. Álvarez, G. Kurizki, and L.
Neumann, P., et al., 2013, Nano Lett. 13, 2738.                              Frydman, 2012, Proc. Natl. Acad. Sci. U.S.A. 109, 5958.
Ng, H. K., D. A. Lidar, and J. Preskill, 2011, Phys. Rev. A 84,            Solomon, I., 1959, Phys. Rev. Lett. 2, 301.
  012305.                                                                  Souza, A. M., G. A. Álvarez, and D. Suter, 2011, Phys. Rev. Lett.
Nielsen, M. A., and I. L. Chuang, 2010, Quantum Computation and              106, 240501.
  Quantum Information: 10th Anniversary Edition (Cambridge                 Souza, A. M., G. A. Álvarez, and D. Suter, 2012a, Phys. Rev. A 85,
  University Press, Cambridge, England).                                     032306.
Nielsen, N. C., C. Kehlet, S. J. Glaser, and N. Khaneja, 2010,             Souza, A. M., G. A. Álvarez, and D. Suter, 2012b, Phys. Rev. A 86,
  eMagRes (John Wiley & Sons, Ltd), doi:10.1002/9780470034590                050301(R).
  .emrstm1043.                                                             Souza, A. M., G. A. Álvarez, and D. Suter, 2012c, Phil. Trans. R.
Packer, K. J., 1973, J. Magn. Reson. 9, 438.                                 Soc. A 370, 4748.
Pascazio, S., 2014, Open Syst. Inf. Dyn. 21, 1440007.                      Souza, A. M., R. S. Sarthour, I. S. Oliveira, and D. Suter, 2015, Phys.
Pasini, S., and G. S. Uhrig, 2010, Phys. Rev. A 81, 012309.                  Rev. A 92, 062332.
Pastawski, H. M., P. R. Levstein, and G. Usaj, 1995, Phys. Rev. Lett.      Staudacher, T., F. Shi, S. Pezzagna, J. Meijer, J. Du, C. A. Meriles, F.
  75, 4310.                                                                  Reinhard, and J. Wrachtrup, 2013, Science 339, 561.
Pastawski, H. M., P. R. Levstein, G. Usaj, J. Raya, and J. Hirschinger,    Steane, A. M., 1996, Phys. Rev. Lett. 77, 793.
  2000, Physica A (Amsterdam) 283, 166.                                    Steinert, S., F. Ziem, L. T. Hall, A. Zappe, M. Schweikert, N. Götz,
Pastawski, H. M., G. Usaj, and P. R. Levstein, 1996, Chem. Phys.             A. Aird, G. Balasubramanian, L. Hollenberg, and J. Wrachtrup,
  Lett. 261, 329.                                                            2013, Nat. Commun. 4, 1607.
Paz, J. P., and W. H. Zurek, 2002, in Fundamentals of Quantum              Stejskal, E. O., 1965, J. Chem. Phys. 43, 3597.
  Information, Lecture Notes in Physics Vol. 587, edited by D. Heiss       Stejskal, E. O., and J. E. Tanner, 1965, J. Chem. Phys. 42, 288.
  (Springer, Berlin/Heidelberg), pp. 77–148.                               Stepisnik, J., 1993, Physica B (Amsterdam) 183, 343.
Peres, A., 1984, Phys. Rev. A 30, 1610.                                    Stepisnik, J., 1999, Physica B (Amsterdam) 270, 110.
Pham, L. M., N. Bar-Gill, C. Belthangady, D. Le Sage, P. Cappellaro,       Stepisnik, J., S. Lasic, A. Mohoric, I. Sersa, and A. Sepe, 2006,
  M. D. Lukin, A. Yacoby, and R. L. Walsworth, 2012, Phys. Rev. B            J. Magn. Reson. 182, 195.
  86, 045214.                                                              Stolze, J., G. A. Álvarez, O. Osenda, and A. Zwick, 2014, in
Preskill, J., 1998, Proc. R. Soc. A 454, 385.                                Quantum State Transfer and Network Engineering, Quantum
Prokof’ev, N. V., and P. C. E. Stamp, 2000, Rep. Prog. Phys. 63, 669.        Science and Technology, edited by G. M. Nikolopoulos and I.
Quiroz, G., and D. A. Lidar, 2012, Phys. Rev. A 86, 042333.                  Jex (Springer, Berlin/Heidelberg), pp. 149–182.
Redfield, A., 1957, IBM J. Res. Dev. 1, 19.                                Stolze, J., and D. Suter, 2008, Quantum Computing: A Short Course
Rhim, W., A. Pines, and J. Waugh, 1971, Phys. Rev. B 3, 684.                 from Theory to Experiment (Wiley-VCH, Berlin), 2nd ed.


Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016              041001-22
                                Dieter Suter and Gonzalo A. Álvarez: Colloquium: Protecting quantum information …


Taylor, J. M., P. Cappellaro, L. Childress, L. Jiang, D. Budker, P. R.     Waugh, J. S., 1982a, J. Magn. Reson. 49, 517.
  Hemmer, A. Yacoby, R. Walsworth, and M. D. Lukin, 2008, Nat.             Waugh, J. S., 1982b, J. Magn. Reson. 50, 30.
  Phys. 4, 810.                                                            Weiss, K. M., J. M. Elzerman, Y. L. Delley, J. Miguel-Sanchez, and
Terhal, B. M., 2015, Rev. Mod. Phys. 87, 307.                               A. Imamoğlu, 2012, Phys. Rev. Lett. 109, 107401.
Timoney, N., I. Baumgart, M. Johanning, A. F. Varon, M. B. Plenio,         West, J. R., D. A. Lidar, B. H. Fong, and M. F. Gyure, 2010, Phys.
  A. Retzker, and C. Wunderlich, 2011, Nature (London) 476, 185.            Rev. Lett. 105, 230503.
Toyli, D. M., C. F. d. l. Casas, D. J. Christle, V. V. Dobrovitski, and    Wimperis, S., 1994, J. Magn. Reson., Ser. A 109, 221.
  D. D. Awschalom, 2013, Proc. Natl. Acad. Sci. U.S.A. 110, 8417.          Wootters, W., and W. Zurek, 1982, Nature (London) 299, 802.
Tycko, R., 1983, Phys. Rev. Lett. 51, 775.                                 Yan, F., S. Gustavsson, J. Bylander, X. Jin, F. Yoshihara, D. G. Cory,
Tycko, R., and A. Pines, 1984, Chem. Phys. Lett. 111, 462.                  Y. Nakamura, T. P. Orlando, and W. D. Oliver, 2013, Nat. Commun.
Tycko, R., A. Pines, and J. Guckenheimer, 1985, J. Chem. Phys. 83,          4, 2337.
  2775.                                                                    Zanardi, P., 1999, Phys. Lett. A 258, 77.
Uhrig, G. S., 2007, Phys. Rev. Lett. 98, 100504.                           Zanardi, P., and M. Rasetti, 1997, Phys. Rev. Lett. 79, 3306.
Uhrig, G. S., 2008, New J. Phys. 10, 083024.                               Zhang, J., R. Laflamme, and D. Suter, 2012, Phys. Rev. Lett. 109,
Uhrig, G. S., and D. A. Lidar, 2010, Phys. Rev. A 82, 012301.               100503.
Uys, H., M. J. Biercuk, and J. J. Bollinger, 2009, Phys. Rev. Lett.        Zhang, J., A. M. Souza, F. D. Brandao, and D. Suter, 2014, Phys.
  103, 040501.                                                              Rev. Lett. 112, 050502.
Viola, L., and E. Knill, 2003, Phys. Rev. Lett. 90, 037901.                Zhang, J., and D. Suter, 2015, Phys. Rev. Lett. 115, 110502.
Viola, L., E. Knill, and S. Lloyd, 1999, Phys. Rev. Lett. 82, 2417.        Zhong, M., M. P. Hedges, R. L. Ahlefeldt, J. G. Bartholomew, S. E.
Viola, L., and S. Lloyd, 1998, Phys. Rev. A 58, 2733.                       Beavan, S. M. Wittig, J. J. Longdell, and M. J. Sellars, 2015, Nature
Viola, L., S. Lloyd, and E. Knill, 1999, Phys. Rev. Lett. 83,               (London) 517, 177.
  4888.                                                                    Zurek, W., 2003, Rev. Mod. Phys. 75, 715.
Wang, X., C.-S. Yu, and X. Yi, 2008, Phys. Lett. A 373, 58.                Zurek, W. H., 1981, Phys. Rev. D 24, 1516.
Wang, Z.-H., G. de Lange, D. Ristè, R. Hanson, and V. V.                   Zurek, W. H., 1982, Phys. Rev. D 26, 1862.
  Dobrovitski, 2012, Phys. Rev. B 85, 155204.                              Zurek, W. H., and J. P. Paz, 1994, Phys. Rev. Lett. 72, 2508.
Wang, Z.-H., W. Zhang, A. M. Tyryshkin, S. A. Lyon, J. W. Ager,            Zwick, A., G. A. Álvarez, and G. Kurizki, 2016, Phys. Rev. Applied
  E. E. Haller, and V. V. Dobrovitski, 2012, Phys. Rev. B 85, 085206.       5, 014007.
Warren, W. S., and M. Silver, 1988, Adv. Magn. Reson. 12, 247.             Zwick, A., G. A. Álvarez, J. Stolze, and O. Osenda, 2012, Phys. Rev.
Waugh, J. S., 1968, J. Chem. Phys. 48, 662.                                 A 85, 012318.




Rev. Mod. Phys., Vol. 88, No. 4, October–December 2016              041001-23
