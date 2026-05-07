# BENCHMARK PLAN

## Objective

Test whether quaternionic coil-state modeling can produce a **5-15% relative improvement** in reconstruction error, artifact localization, or phase/coherence stability on controlled multicoil MRI datasets versus standard complex baselines.

## Methods compared

1. Baseline: inverse FFT + RSS coil combination
2. Sensitivity-informed baseline: SENSE-style reconstruction where maps are available
3. Proposed: Quaternionic Coil-State Model (QCSM) fusion

## Primary metrics

- NMSE
- PSNR
- SSIM
- Artifact energy
- Phase consistency
- Coil-combination stability
- Motion-corrupted reconstruction error

## Evaluation policy

- Report per-dataset and aggregated statistics
- No clinical efficacy claims
- No guaranteed superiority claims
- Conclusions limited to tested acquisition settings
