# MRI-systems

Quaternion-native software methods for MRI reconstruction, calibration, and multichannel signal representation.

MRI systems acquire phase-sensitive resonance data across receiver coils, gradients, and spatial frequency domains. Standard pipelines represent this data primarily through complex-valued k-space and then manage coil geometry, phase drift, motion, and reconstruction artifacts through separate correction layers.

MRI-systems explores a quaternionic upgrade path: representing MRI signal structure as a coherent geometric object rather than a collection of loosely coupled complex channels.

This repository is research software. It does not provide medical diagnosis, clinical recommendations, scanner control, or regulated medical-device functionality.

## Scope

RQM Technologies develops quaternion-native software methods for MRI reconstruction, calibration, artifact reduction, and multichannel signal representation.

## Central thesis

Standard MRI reconstruction is fundamentally complex-valued, but modern MRI systems are multichannel, orientation-dependent, and phase-sensitive. Quaternionic representations can encode one scalar and three coupled directional or phase components in a single object.

## MVP focus

The first MVP in this repository is quaternionic multicoil fusion for MRI reconstruction, benchmarked against baseline inverse FFT + root-sum-of-squares coil combination.
