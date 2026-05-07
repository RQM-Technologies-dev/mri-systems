# Claim 01: Multicoil fusion robustness

## Plain-language claim

A coherence-aware quaternionic representation may improve multicoil fusion
stability when channels disagree in phase/orientation-sensitive conditions.

## Why OEMs care

More stable multicoil fusion can help reduce reconstruction variability in
challenging scans and may improve confidence in downstream image quality.

## Technical mechanism being tested

The test evaluates whether QCSM-style state fusion better captures coupled
inter-coil behavior than complex-only magnitude fusion in controlled settings.

## Baseline comparison

- Baseline: standard inverse FFT plus RSS fusion.
- Candidate: QCSM/coherence-aware placeholder reconstruction path.

## Required code path

- `src/qsg_mri/coil_state.py`
- `src/qsg_mri/baselines.py`
- `src/qsg_mri/reconstruction.py`
- `src/qsg_mri/metrics.py`

## Required simulation

- `simulations/multicoil_fusion/run.py`
- Synthetic phantom with controlled coil phase disagreement.
- Paired outputs for baseline and candidate from the same input.

## Required metrics

- NMSE (relative to known phantom reference)
- PSNR
- Artifact energy
- Mean coherence defect

## Current evidence maturity

Concept defined; code scaffolded; synthetic simulation scaffolded.
No achieved benchmark result is claimed unless measured artifacts are present.

## Limitations

- Synthetic scenario only.
- Placeholder candidate implementation.
- Transferability to sequence-specific production workflows remains open.

## Next proof step

Generate reproducible `metrics.json` outputs from repeated synthetic runs, then
prepare offline replay on a small deidentified multicoil dataset against an OEM
internal baseline.

## Technical basis

Per-coil state model under evaluation:

\[
q_c(r) = A_c(r)\left[\cos \phi_c(r) + u_c(r)\sin \phi_c(r)\right]
\]
