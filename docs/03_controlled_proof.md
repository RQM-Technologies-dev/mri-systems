# 03 - Controlled proof

This repository includes explicit proof notes to keep the model testable and
falsifiable.

## Proof obligations

1. Complex MRI is a fixed-axis quaternionic special case.
2. Two complex coil channels can be packed into one quaternionic state.
3. Measured complex k-space remains the data-fidelity target.
4. Quaternionic latent states must project back to complex measurements.
5. Coherence defect can be defined as local coil-state disagreement.

## Quaternionic Coil-State Model

\[
q_c(r) = A_c(r)\left[\cos \phi_c(r) + u_c(r)\sin \phi_c(r)\right]
\]

## Coherence score and defect

\[
C_{MRI}(r) =
\frac{\left\|\sum_c \alpha_c(r) q_c(r)\right\|}
{\sum_c |\alpha_c(r)|\|q_c(r)\| + \epsilon}
\]

\[
D_{coh}(r) = 1 - C_{MRI}(r)
\]

\(D_{coh}\) is evaluated as a software-side indicator of local disagreement that
may align with artifact-prone or reconstruction-unstable regions in controlled
experiments.
