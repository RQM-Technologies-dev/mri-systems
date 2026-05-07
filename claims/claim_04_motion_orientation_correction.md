# Claim 04: Motion/orientation robustness

## Plain-language claim

Orientation-aware quaternionic states may improve robustness to motion-driven
artifacts in controlled reconstruction scenarios.

## Why OEMs care

Motion sensitivity is a practical source of retakes and quality variability.
Improved robustness can be valuable for throughput and user confidence.

## Technical mechanism being tested

The mechanism tests whether coherence-aware candidate reconstruction better
handles phase/orientation perturbations injected into multicoil k-space.

## Baseline comparison

- Baseline: standard complex reconstruction path (inverse FFT + RSS).
- Candidate: QCSM/coherence-aware placeholder path under same perturbation.

## Required code path

- `src/qsg_mri/coil_state.py`
- `src/qsg_mri/coherence.py`
- `src/qsg_mri/reconstruction.py`
- `src/qsg_mri/metrics.py`

## Required simulation

- `simulations/motion_artifacts/run.py`
- Synthetic line-wise phase modulation and coil-wise random phase offsets.
- Paired baseline/candidate reconstructions with diagnostics.

## Required metrics

- NMSE
- PSNR
- Artifact energy (ghosting/artifact proxy)
- Mean coherence defect

## Current evidence maturity

Concept defined; code scaffolded; synthetic simulation scaffolded.
Target hypothesis only; no achieved result claim without measured artifacts.

## Limitations

- Synthetic perturbation model does not represent full patient/sequence dynamics.
- Placeholder candidate implementation.
- No clinical validation is implied.

## Next proof step

Run controlled motion perturbation sweeps with fixed seeds, compare ghosting
proxy and artifact-energy trends to baseline, and stage offline deidentified
replay against internal OEM reconstruction outputs.

## Technical basis

Orientation-aware local axis terms are introduced in the quaternionic state
representation and evaluated for controlled robustness effects.
