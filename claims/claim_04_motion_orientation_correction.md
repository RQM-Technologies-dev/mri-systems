# Claim 04: Motion/orientation robustness

## Plain-language claim

Orientation-aware quaternionic states may improve robustness to motion-driven
artifacts in controlled reconstruction scenarios.

## Why an OEM would care

Motion sensitivity is a practical source of retakes and quality variability.
Improved robustness can be valuable for throughput and user confidence.

## Mechanism being tested

The mechanism tests whether coherence-aware candidate reconstruction better
handles phase/orientation perturbations injected into multicoil k-space.

## Baseline comparison

- Baseline: standard complex reconstruction path (inverse FFT + RSS).
- Candidate: QCSM/coherence-aware placeholder path under same perturbation.

## Required simulation

- `simulations/motion_artifacts/run.py`
- Synthetic line-wise phase modulation and coil-wise random phase offsets.
- Paired baseline/candidate reconstructions with diagnostics.

## Metrics

- NMSE
- PSNR
- Artifact energy (ghosting/artifact proxy)
- Mean coherence defect

## Current status

Scaffolded research workflow. Target hypothesis only; no achieved result claim.

## Limitations

- Synthetic perturbation model does not represent full patient/sequence dynamics.
- Placeholder candidate implementation.
- No clinical validation is implied.

## Technical basis

Orientation-aware local axis terms are introduced in the quaternionic state
representation and evaluated for controlled robustness effects.
