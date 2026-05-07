# 06 - Software package

Python package: `qsg_mri`

This package is the proof engine for the repository. Claims are meant to become
testable through code paths, reproducible simulations, and metrics artifacts.

## What the package is for

- Build controlled benchmark comparisons.
- Keep baseline and candidate reconstruction paths auditable.
- Generate reproducible research metrics and diagnostics.
- Support offline evaluation before any workflow integration decision.

## Module map and what each module proves

- `quaternion.py` proves the representation is implementable in software.
- `kspace.py` preserves standard Fourier-space interpretation and handling.
- `coil_state.py` implements QCSM construction and channel packing/fusion paths.
- `coherence.py` makes coil agreement/disagreement measurable.
- `baselines.py` keeps comparison honest against standard methods.
- `reconstruction.py` holds first-pass research candidate reconstruction/fusion execution paths.
- `metrics.py` converts outputs into auditable evidence artifacts.
- `phantoms.py` enables controlled, repeatable synthetic input cases.
- `simulations/` turns modules into reproducible benchmark runs.

## Proof burden by code path

### `claim_01_multicoil_fusion`

- `coil_state.py`
- `baselines.py`
- `simulations/multicoil_fusion`
- `metrics.json`

### `claim_02_artifact_coherence_mapping`

- `coherence.py`
- `simulations/artifact_localization`
- `coherence_defect_map`
- artifact localization metrics

### `claim_03_undersampling_robustness`

- `kspace.py`
- `reconstruction.py`
- `simulations/undersampling`
- NMSE/PSNR comparison

### `claim_04_motion_orientation_correction`

- `coil_state.py`
- `coherence.py`
- `simulations/motion_artifacts`
- artifact_energy / ghosting proxy

## Scope guardrail

The package outputs research metrics only. It is not clinical reconstruction
software, is not medical-device software, and does not provide scanner control.
