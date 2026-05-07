# BENCHMARK PLAN

## Objective

Build controlled, reproducible evidence for whether a quaternionic reconstruction
layer can improve coherence-sensitive MRI software outcomes relative to standard
complex baselines.

## Methods compared

1. Baseline: centered inverse FFT + root-sum-of-squares (RSS)
2. Baseline variant: sensitivity-informed fusion where sensitivity maps exist
3. Proposed: Quaternionic Coil-State Model (QCSM) placeholder fusion with
   coherence outputs

## Controlled scenarios

- Phantom baseline reconstruction
- Multicoil fusion under coil-state disagreement
- Artifact localization via coherence defect maps
- Undersampling stress tests
- Motion/orientation perturbation stress tests

## Primary metrics

- NMSE
- PSNR
- artifact energy
- coherence score / coherence defect summaries
- optional SSIM placeholder (documented as non-validated in current package)

## Research targets (not achieved results)

- Multicoil fusion: 5-15% relative error/coherence improvement target
- Artifact localization: 10-25% artifact-region detection improvement target
- Undersampling robustness: 5-12% relative NMSE reduction target
- Motion/orientation robustness: 10-20% ghosting/artifact reduction target

## Reproducibility requirements

- Deterministic seeds in config files
- Versioned simulation scripts and configs
- Saved `metrics.json`, `summary.md`, and maps per simulation run

## Reporting policy

- No clinical claims
- No regulatory claims
- No superiority claim without reproducible measured evidence
- Conclusions constrained to tested synthetic/offline conditions
