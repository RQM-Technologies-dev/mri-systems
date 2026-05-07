# Claim 03: Undersampling robustness

## Plain-language claim

A coherence-aware candidate reconstruction path may reduce error concentration
under undersampling compared with standard complex-domain baselines.

## Why OEMs care

If reconstruction is more stable in undersampled conditions, teams may gain
flexibility in speed/quality tradeoff studies and workflow tuning.

## Technical mechanism being tested

The mechanism evaluates whether quaternionic/coherence-aware fusion better
handles coupled phase and multichannel behavior when sampling is incomplete.

## Baseline comparison

- Baseline: inverse FFT + RSS on undersampled k-space.
- Candidate: QCSM/coherence-aware placeholder reconstruction on same input.

## Required code path

- `src/qsg_mri/kspace.py`
- `src/qsg_mri/reconstruction.py`
- `src/qsg_mri/baselines.py`
- `src/qsg_mri/metrics.py`

## Required simulation

- `simulations/undersampling/run.py`
- Cartesian undersampling mask with configurable acceleration.
- Paired baseline/candidate outputs and error diagnostics.

## Required metrics

- NMSE (primary target metric)
- PSNR
- Artifact energy
- Mean coherence defect

## Current evidence maturity

Concept defined; code scaffolded; synthetic simulation scaffolded.
No achieved benchmark result is claimed unless measured artifacts are present.

## Limitations

- Limited mask family and acceleration settings.
- Synthetic-only benchmark conditions.
- Placeholder candidate method may not represent final algorithmic design.

## Next proof step

Evaluate multiple fixed undersampling factors with reproducible configs,
generate per-factor metrics artifacts, and compare against OEM baseline behavior
in offline deidentified replay.

## Technical basis

Measured complex k-space remains the data-fidelity target during candidate
representation testing.
