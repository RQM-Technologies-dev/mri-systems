# 06 - Software package

Python package: `qsg_mri`

This package is the proof engine for the repository. Claims are meant to become
testable through code paths, reproducible simulations, and metrics artifacts.

## What the package is for

- Build controlled benchmark comparisons.
- Keep baseline and candidate reconstruction paths auditable.
- Generate reproducible research metrics and diagnostics.
- Support offline evaluation before any workflow integration decision.

## Module map in practical terms

- `quaternion.py`: representation utilities for quaternionic state operations.
- `kspace.py`: spatial-frequency helpers for centered frequency-domain handling.
- `coil_state.py`: QCSM state construction and multicoil packing/fusion helpers.
- `coherence.py`: coherence score and defect metrics for disagreement analysis.
- `baselines.py`: RSS/FFT reference methods for standard complex pipelines.
- `reconstruction.py`: baseline reconstruction and candidate coherence-aware
  placeholder path.
- `metrics.py`: NMSE/PSNR/artifact-energy metrics for controlled benchmark
  reporting.
- `phantoms.py`: synthetic data generators used by reproducible simulation runs.
- `simulations/`: reproducible evidence generation scripts and output artifacts.

## Scope guardrail

The package outputs research metrics only. It is not clinical reconstruction
software and is not a medical-device product.
