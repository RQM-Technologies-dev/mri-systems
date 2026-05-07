# ROADMAP

## 1) Problem framing and baseline lock

- Keep standard complex MRI forward model explicit.
- Standardize baseline reconstruction and metric definitions.
- Document why coherence failures matter for multicoil workflows.

## 2) Better representation implementation

- Implement quaternionic lift and fixed-axis complex special case in `qsg_mri`.
- Define coil-state representation and packing utilities.
- Preserve complex-data compatibility and projection path.

## 3) Controlled proof layer

- Publish proof notes for:
  - complex-as-fixed-axis equivalence
  - quaternionic coil-state model
  - projection back to complex k-space
  - coherence metric derivation
- Tie each proof to testable software functions.

## 4) Reproducible simulation harness

- Maintain simulation folders with deterministic configs.
- Produce baseline, quaternionic/coherence-aware output, maps, and metrics.
- Keep all demonstrations clearly synthetic unless otherwise documented.

## 5) Integration path for OEM workflows

- Add research plugin path on top of existing preprocessing.
- Keep scanner hardware unchanged.
- Validate offline on recorded multicoil k-space before any runtime integration.

## 6) Software package maturity

- Expand from placeholder QCSM functions to validated reconstruction blocks.
- Strengthen tests, reproducibility checks, and benchmark automation.
- Continue strict non-clinical, research-only scope unless separately validated.
