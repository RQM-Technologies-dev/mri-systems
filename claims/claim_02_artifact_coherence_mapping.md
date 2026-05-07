# Claim 02: Artifact coherence mapping

## Plain-language claim

Coherence-defect maps may localize artifact-prone regions more clearly than
magnitude-only residual views in controlled reconstruction tests.

## Why OEMs care

Better artifact localization can support operator confidence, workflow triage,
and faster debugging of problematic reconstruction behaviors.

## Technical mechanism being tested

The mechanism tests whether local multicoil disagreement metrics from
quaternionic states correlate with injected artifact regions.

## Baseline comparison

- Baseline: magnitude-domain residual/error analysis.
- Candidate: coherence-defect map analysis from QCSM-style outputs.

## Required code path

- `src/qsg_mri/coherence.py`
- `src/qsg_mri/reconstruction.py`
- `src/qsg_mri/metrics.py`

## Required simulation

- `simulations/artifact_localization/run.py`
- Controlled localized artifact injection.
- Artifact mask generation for analysis reference.

## Required metrics

- Artifact-region detection proxy comparisons (baseline vs coherence-defect)
- NMSE and PSNR
- Artifact energy
- Mean coherence defect

## Current evidence maturity

Concept defined; code scaffolded; synthetic simulation scaffolded.
Target hypothesis only; no achieved result claim without measured artifacts.

## Limitations

- Artifact model is synthetic and simplified.
- Thresholding/decision policy is not finalized.
- Not validated as a clinical artifact detector.

## Next proof step

Run repeatable artifact-injection sweeps with fixed configs and thresholds,
compare localization proxies against baseline residual maps, and prepare offline
deidentified replay for engineering-only review.

## Technical basis

Coherence-defect quantity under evaluation:

\[
D_{coh}(r) = 1 - C_{MRI}(r)
\]
