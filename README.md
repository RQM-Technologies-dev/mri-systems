# MRI-systems

## Software-only MRI reconstruction research for OEM evaluation

MRI-systems is a software-only upgrade path study for MRI reconstruction teams.
It tests whether a candidate quaternionic representation layer can improve
coherence-aware reconstruction in multicoil workflows while measured complex
k-space remains the input and existing hardware is unchanged.

## Why this matters

MRI systems already produce valuable complex multicoil data. In practice,
quality and stability often degrade when coil disagreement, phase instability,
undersampling, motion, and artifact structure are coupled. Even modest
reconstruction gains can matter in healthcare when they help reduce retakes,
improve confidence, and support scanner throughput. This repository is built for
offline evaluation first.

## What changes

- Existing scanner hardware is unchanged.
- Measured complex multicoil k-space remains the input.
- Standard preprocessing remains part of the workflow.
- QSG-MRI adds a candidate quaternionic representation layer in software.
- Outputs can include standard reconstructed images plus optional
  coherence/artifact maps for diagnostics.

## What OEM teams can evaluate

- Multicoil fusion behavior under coil disagreement.
- Artifact localization support from coherence-defect maps.
- Undersampling robustness in controlled benchmark settings.
- Motion/orientation robustness in synthetic stress tests.
- Runtime and integration feasibility in an existing stack.

## Current status

- Research prototype with synthetic simulations and reproducible artifacts.
- Simulation outputs may show measured synthetic results from controlled runs,
  but those results are not clinical evidence and do not establish target
  achievement unless explicitly stated.
- No clinical claims and no regulatory claims.
- No achieved benchmark claims are reported unless explicitly measured artifacts
  are included; target ranges are research targets.
- Python code, tests, and simulations carry the proof burden for engineering
  evaluation.

## Quickstart

```bash
python -m pip install -e .
python -m pytest -q
python simulations/phantom_baseline/run.py
```

## Repository guide

- `EXECUTIVE_OVERVIEW.md`: skimmable manager overview.
- `OEM_BRIEF.md`: decision-maker brief and evaluation path.
- `TECHNICAL_EVALUATION_GUIDE.md`: practical offline workflow for OEM engineers.
- `docs/`: narrative-first technical walkthrough.
- `docs/README.md` and `docs/08_artifact_schema.md`: doc navigation and artifact contract.
- `claims/`: testable product hypotheses and evidence plans.
- `examples/README.md`: practical script-level example guide.
- `simulations/`: reproducible controlled benchmark scripts.
- `src/qsg_mri/`: software package used to generate comparisons and metrics.
- `THEORY.md` and `proofs/`: mathematical foundation and detailed derivations.
- `EVIDENCE_MAP.md`: proposal-to-evidence tracking with research targets.

## Technical foundation (for technical reviewers)

Standard per-coil MRI measurement model:

\[
y_c(k) = \int_\Omega \rho(r) s_c(r)\exp(-i 2\pi k\cdot r)\,dr + \epsilon_c(k)
\]

with \(k\) as spatial-frequency coordinate, \(r\) as image-space coordinate,
\(\rho\) as tissue magnetization, \(s_c\) as coil sensitivity, and
\(\epsilon_c\) as noise.

Local complex and quaternionic representations:

\[
z(r) = A(r)\exp(i\phi(r))
\]

\[
q(r) = A(r)\left[\cos\phi(r) + u(r)\sin\phi(r)\right]
\]

where complex MRI is preserved as a fixed-axis special case (\(u(r)=i\)).

## Safety and regulatory note

This repository is research software only. It is not scanner-control software,
not a clinical product, and not FDA-cleared. See `SAFETY_AND_REGULATORY.md` for
scope limits.
