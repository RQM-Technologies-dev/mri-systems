# Claim 01: Multicoil fusion robustness

## Plain-language claim

A coherence-aware quaternionic representation may improve multicoil fusion
stability when channels disagree in phase/orientation-sensitive conditions.

## Why an OEM would care

More stable multicoil fusion can help reduce reconstruction variability in
challenging scans and may improve confidence in downstream image quality.

## Mechanism being tested

The test evaluates whether QCSM-style state fusion better captures coupled
inter-coil behavior than complex-only magnitude fusion in controlled settings.

## Baseline comparison

- Baseline: standard inverse FFT plus RSS fusion.
- Candidate: QCSM/coherence-aware placeholder reconstruction path.

## Required simulation

- `simulations/multicoil_fusion/run.py`
- Synthetic phantom with controlled coil phase disagreement.
- Paired outputs for baseline and candidate from the same input.

## Metrics

- NMSE (relative to known phantom reference)
- PSNR
- Artifact energy
- Mean coherence defect

## Current status

Scaffolded research workflow. No achieved benchmark result is claimed.

## Limitations

- Synthetic scenario only.
- Placeholder candidate implementation.
- Transferability to sequence-specific production workflows remains open.

## Technical basis

Per-coil state model under evaluation:

\[
q_c(r) = A_c(r)\left[\cos \phi_c(r) + u_c(r)\sin \phi_c(r)\right]
\]
