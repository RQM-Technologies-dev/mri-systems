# 03 - Controlled proof

In this repository, "proof" means reproducible engineering evidence for a
software-only reconstruction candidate. It does **not** mean clinical proof.

This validation model is intentionally practical: code, tests, simulation
artifacts, and metrics carry the burden of evidence.

## What "controlled proof" means here

Controlled proof answers a narrow technical question:

- Can a QSG-MRI candidate be evaluated fairly against existing complex
  reconstruction workflows?
- Can the evaluation be repeated with the same inputs and settings?
- Can outputs be audited by engineering teams before any integration decision?

## Engineering validation ladder

### Level 0 - Mathematical compatibility

Goal: ensure the candidate does not break core MRI data assumptions.

- Standard complex MRI is preserved as a fixed-axis case.
- Measured complex k-space remains the data-fidelity target.
- Mathematical definitions remain in `THEORY.md` and `proofs/`; implementation
  docs stay operational.

Exit criterion:
- The bridge from complex representation to candidate state is specified and
  does not replace the underlying measured complex data model.

### Level 1 - Unit-test proof

Goal: verify core software behavior is correct and stable in isolation.

Coverage focus:
- quaternion operations
- fixed-axis complex bridge behavior
- k-space helper behavior
- coherence score behavior

Exit criterion:
- Unit tests for these components run deterministically and pass.

### Level 2 - Synthetic phantom proof

Goal: run baseline-vs-candidate reconstruction on controlled data and emit
auditable artifacts.

Expected outputs:
- baseline reconstruction
- QCSM/coherence-aware candidate output
- error map
- coherence-defect map (where applicable)
- `metrics.json`
- `summary.md`

Exit criterion:
- Artifacts are generated from a known phantom/config and can be replayed by
  another engineer.

### Level 3 - Controlled stress tests

Goal: evaluate failure behavior under realistic software stressors before any
external data replay.

Stress scenarios:
- coil disagreement
- undersampling
- synthetic motion
- artifact injection

Exit criterion:
- Baseline and candidate are compared side-by-side under each stress scenario
  with machine-readable metrics and diagnostics.

### Level 4 - Offline OEM replay

Goal: evaluate technical fit in an OEM engineering environment without scanner
control changes.

Scope:
- deidentified raw multicoil k-space replay
- comparison against OEM internal baseline
- runtime and integration complexity evaluation

Exit criterion:
- OEM team can decide whether further integration exploration is justified.

## Scope boundary

This ladder is an engineering validation ladder, not a clinical validation
framework. Success at any level supports technical evaluation decisions only.
