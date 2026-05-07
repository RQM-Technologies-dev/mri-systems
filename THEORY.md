# THEORY

> This file is for technical reviewers. The main README and OEM_BRIEF
> intentionally present the upgrade path before the equations.

## 1) Standard complex MRI measurement model

For coil \(c\), measured complex k-space is:

\[
y_c(k) = \int_\Omega \rho(r) s_c(r) \exp(-i 2\pi k\cdot r) dr + \epsilon_c(k)
\]

Definitions:

- \(y_c(k)\): measured k-space data for coil \(c\)
- \(k\): Fourier-space / spatial-frequency coordinate
- \(r\): image-space coordinate
- \(\rho(r)\): underlying image / tissue magnetization
- \(s_c(r)\): coil sensitivity map
- \(\epsilon_c(k)\): noise

The model and data fidelity remain complex-valued at measurement level.

## 2) k-space interpretation

\(k\) is not an anatomical radius.

- \(k=0\): low spatial frequency content (global contrast)
- larger \(|k|\): finer spatial detail
- direction in \(k\)-space: direction of spatial variation

## 3) Quaternionic lift

Standard local signal:

\[
z(r) = A(r)\exp(i \phi(r))
\]

Quaternionic state:

\[
q(r) = A(r)\left[\cos \phi(r) + u(r)\sin \phi(r)\right]
\]

where:

- \(A(r)\): local magnitude
- \(\phi(r)\): local phase
- \(u(r)\): local unit imaginary quaternion axis
- \(q(r)\): local quaternionic resonance state

Credibility bridge:

\[
u(r)=i \Rightarrow q(r)\ \text{reduces to the standard complex model}
\]

Standard complex MRI is therefore a fixed-axis special case.

## 4) Quaternionic Coil-State Model (QCSM)

Per-coil local state:

\[
q_c(r) = A_c(r)\left[\cos \phi_c(r) + u_c(r)\sin \phi_c(r)\right]
\]

QCSM represents multicoil structure as a set of coupled quaternionic states with
explicit projection back to measured complex data.

## 5) Coherence metric

Define weighted local coherence:

\[
C_{MRI}(r) =
\frac{\left\|\sum_c \alpha_c(r) q_c(r)\right\|}
{\sum_c |\alpha_c(r)|\|q_c(r)\| + \epsilon}
\]

Coherence defect:

\[
D_{coh}(r) = 1 - C_{MRI}(r)
\]

\(D_{coh}\) is a research metric for local coil-state disagreement and potential
artifact-prone instability.

## 6) Data-fidelity requirement

Measured complex k-space remains the target. Quaternionic internal states must
project to complex measurements for fidelity checks. This repository does not
replace measured data with synthetic quaternion-only observations.

## 7) Scope

This is software research only. It does not provide clinical diagnosis, scanner
control, or regulatory-cleared medical-device functionality.
