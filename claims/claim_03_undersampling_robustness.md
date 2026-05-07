# Claim 03: Undersampling robustness

## Plain-language claim

A coherence-aware candidate reconstruction path may reduce error concentration
under undersampling compared with standard complex-domain baselines.

## Why an OEM would care

If reconstruction is more stable in undersampled conditions, teams may gain
flexibility in speed/quality tradeoff studies and workflow tuning.

## Mechanism being tested

The mechanism evaluates whether quaternionic/coherence-aware fusion better
handles coupled phase and multichannel behavior when sampling is incomplete.

## Baseline comparison

- Baseline: inverse FFT + RSS on undersampled k-space.
- Candidate: QCSM/coherence-aware placeholder reconstruction on same input.

## Required simulation

- `simulations/undersampling/run.py`
- Cartesian undersampling mask with configurable acceleration.
- Paired baseline/candidate outputs and error diagnostics.

## Metrics

- NMSE (primary target metric)
- PSNR
- Artifact energy
- Mean coherence defect

## Current status

Scaffolded research workflow. No achieved benchmark result is claimed.

## Limitations

- Limited mask family and acceleration settings.
- Synthetic-only benchmark conditions.
- Placeholder candidate method may not represent final algorithmic design.

## Technical basis

Measured complex k-space remains the data-fidelity target during candidate
representation testing.
