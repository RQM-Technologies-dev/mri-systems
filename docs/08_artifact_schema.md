# 08 - Artifact schema

This document defines the expected output artifacts for controlled simulation
runs. The goal is reproducible OEM engineering evaluation with machine-readable
evidence.

## Required output files

- `config_snapshot.json`
  - Resolved run configuration used to generate outputs.
  - Should include all effective parameters and resolved output directory.
- `metrics.json`
  - Machine-readable run metrics and run-state fields.
  - Should include `run_completed`, `synthetic_only`, `clinical_result`,
    `result_scope`, and `target_achieved`.
- `summary.md`
  - Human-readable run summary with methods, key metrics, relative changes, and
    interpretation guardrail text.

## Array artifacts (`.npy`)

- `phantom.npy` (where applicable)
  - Synthetic reference object used for controlled comparisons.
- `baseline_reconstruction.npy`
  - Baseline method reconstruction output.
- `candidate_reconstruction.npy`
  - Candidate method reconstruction output.
- `baseline_error_map.npy`
  - Absolute error map between baseline reconstruction and synthetic reference.
- `candidate_error_map.npy`
  - Absolute error map between candidate reconstruction and synthetic reference.
- `coherence_defect_map.npy`
  - Coherence-defect diagnostic map from candidate method output.
- `quaternion_components.npy`
  - Quaternion component channels from candidate method internals.

## Optional image artifacts

- Optional PNG files (for example `*_reconstruction.png`, `*_error_map.png`,
  `coherence_defect_map.png`) may be emitted for fast human review.
- PNG files are review aids only.
- `.npy` files are the machine-readable evidence artifacts and should be used
  for quantitative inspection and reproducibility.
