# THEORY

## 1) Standard complex MRI measurement model

For receiver coil \(c\), MRI measurements are complex-valued k-space samples:

\[
y_c(k) = \int_\Omega \rho(r) s_c(r)e^{-i2\pi k\cdot r}\,dr + \epsilon_c(k)
\]

- \(y_c(k)\): measured k-space data for coil \(c\)
- \(k\): spatial-frequency coordinate
- \(r\): image-space coordinate
- \(\rho(r)\): underlying magnetization image
- \(s_c(r)\): coil sensitivity map
- \(\epsilon_c(k)\): noise term

The baseline inverse problem is to recover image-space structure from sampled complex k-space data.

## 2) Clarifying k-space coordinates

The coordinate \(k\) is Fourier-space, not anatomical radius.

- \(k=0\): low spatial frequencies (broad contrast, smooth structure)
- Large \(|k|\): high spatial frequencies (edges, fine detail)
- Direction of \(k\): direction of spatial variation

Moving outward in k-space means moving toward finer spatial detail, not moving outward in the body.

## 3) Quaternionic lift

Standard local complex representation:

\[
z(r)=A(r)e^{i\phi(r)}
\]

Quaternionic lift:

\[
q(r)=A(r)[\cos\phi(r)+u(r)\sin\phi(r)]
\]

- \(A(r)\): local magnitude
- \(\phi(r)\): local phase
- \(u(r)\): local unit imaginary quaternion axis

The standard complex model is the fixed-axis special case \(u(r)=i\). This project treats quaternionic MRI as a testable generalization that contains conventional complex MRI.

## 4) Quaternionic Coil-State Model (QCSM)

Define each coil-local state as:

\[
q_c(r)=A_c(r)[\cos\phi_c(r)+u_c(r)\sin\phi_c(r)]
\]

Reconstruction seeks a coherent quaternionic field whose projections remain consistent with measured complex k-space data.

## 5) Data-fidelity framing

Scanners still measure complex RF/k-space data; they do not directly measure full quaternion states.

High-level objective:

\[
\hat q = \arg\min_q\,[\text{data fidelity} + \text{quaternionic regularity} + \text{coil-state coherence}]
\]

The data-fidelity term enforces agreement with measured complex data after projection from quaternionic state space.

## 6) Why this might help

Standard pipelines often separate phase handling, coil combination, orientation effects, and motion correction into independent modules. QCSM aims to model these coupled effects in one state representation. Expected value is strongest where reconstruction failure is driven by coherence errors across phase, coil geometry, orientation, and motion.

## 7) Research status

This repository is a research program and hypothesis test, not proven clinical superiority. Current targets are controlled benchmarks for multicoil fusion, artifact localization, undersampling robustness, and motion sensitivity.
