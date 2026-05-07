# MRI-systems

Quaternion-native research software for MRI reconstruction, multicoil fusion, artifact analysis, and phase/coherence modeling.

MRI systems acquire complex-valued k-space data from phase-sensitive electromagnetic resonance measurements. Modern MRI reconstruction must also manage multichannel receiver coils, coil sensitivity maps, field variation, motion, undersampling, and artifact structure.

MRI-systems explores a quaternionic upgrade path: representing local MRI signal structure as a coherent geometric state rather than as disconnected complex channels and correction layers.

This repository is research software. It does not provide medical diagnosis, clinical recommendations, scanner control, or regulated medical-device functionality.

## Canonical model baseline

For coil \(c\), measured MRI k-space data is modeled as:

\[
y_c(k) = \int_\Omega \rho(r) s_c(r)e^{-i2\pi k\cdot r}\,dr + \epsilon_c(k)
\]

The practical reconstruction goal is still to recover image content from sampled complex k-space data. This project tests whether lifting internal reconstruction state into quaternionic form can improve coherence-sensitive failure modes while remaining compatible with existing scanners.

## Core thesis

- Complex numbers are sufficient for single-axis phase modeling.
- MRI errors are often coherence errors across phase, coil geometry, orientation, and motion.
- Quaternionic methods may help when those coupled coherence terms dominate quality loss.

## First MVP target

Quaternionic multicoil fusion for MRI reconstruction, benchmarked against:

- inverse FFT + root-sum-of-squares (RSS)
- sensitivity-map-informed baseline (SENSE-style where appropriate)
- Quaternionic Coil-State Model (QCSM) fusion
