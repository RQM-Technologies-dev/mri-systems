# Claim 02: Artifact coherence mapping

## Plain-language claim

Coherence-defect maps may localize artifact-prone regions more clearly than
magnitude-only residual views in controlled reconstruction tests.

## Why an OEM would care

Better artifact localization can support operator confidence, workflow triage,
and faster debugging of problematic reconstruction behaviors.

## Mechanism being tested

The mechanism tests whether local multicoil disagreement metrics from
quaternionic states correlate with injected artifact regions.

## Baseline comparison

- Baseline: magnitude-domain residual/error analysis.
- Candidate: coherence-defect map analysis from QCSM-style outputs.

## Required simulation

- `simulations/artifact_localization/run.py`
- Controlled localized artifact injection.
- Artifact mask generation for analysis reference.

## Metrics

- Artifact-region detection proxy comparisons (baseline vs coherence-defect)
- NMSE and PSNR
- Artifact energy
- Mean coherence defect

## Current status

Scaffolded research workflow. Target hypothesis only; no achieved result claim.

## Limitations

- Artifact model is synthetic and simplified.
- Thresholding/decision policy is not finalized.
- Not validated as a clinical artifact detector.

## Technical basis

Coherence-defect quantity under evaluation:

\[
D_{coh}(r) = 1 - C_{MRI}(r)
\]
