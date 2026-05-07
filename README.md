# qsg_mri in MRI-systems

`qsg_mri` is research software for MRI reconstruction and medical imaging experiments.
It evaluates a software-only quaternionic upgrade path for multicoil complex MRI workflows.

This repository is:

- for MRI reconstruction and imaging research software
- not MRI hardware
- not a clinical diagnostic product
- not FDA-cleared medical-device software
- not a source of clinical claims

## What this repository does

The project tests whether Quaternionic Spectral Geometry (QSG-MRI) can improve
standard software reconstruction workflows by representing phase, coil geometry,
orientation, motion, and multichannel coherence in one state model.

Measured data remains standard complex multicoil k-space.

## Why MRI reconstruction is a coherence problem

MRI reconstruction starts from phase-sensitive complex measurements. A common
forward model for coil \(c\) is:

\[
y_c(k) = \int_\Omega \rho(r) s_c(r)\exp(-i 2\pi k\cdot r)\,dr + \epsilon_c(k)
\]

where \(k\) is a spatial-frequency coordinate (not anatomical radius), \(r\) is
image-space position, \(\rho\) is tissue magnetization, \(s_c\) is coil
sensitivity, and \(\epsilon_c\) is noise.

Modern reconstruction quality is affected by:

- multichannel coil disagreement
- sensitivity-map uncertainty
- undersampling and motion artifacts
- local coherence loss and instability

## What the quaternionic upgrade changes

Standard local complex signal:

\[
z(r) = A(r)\exp(i\phi(r))
\]

Quaternionic lift:

\[
q(r) = A(r)\left[\cos\phi(r) + u(r)\sin\phi(r)\right]
\]

with local unit axis \(u(r)\).  
Credibility bridge: standard complex MRI is the fixed-axis special case
\(u(r)=i\).

## Current status

- Mathematical notes and evidence map for OEM evaluation are included.
- Synthetic simulation scaffolds are runnable and produce reproducible artifacts.
- `qsg_mri` package provides baseline and placeholder quaternionic components.
- No benchmark claims are reported as achieved; all ranges are research targets.

## Quickstart

```bash
python -m pip install -e .
python -m pytest -q
python simulations/phantom_baseline/run.py
```

## Repository map

- `OEM_BRIEF.md`: decision-maker summary
- `THEORY.md`: MRI and quaternionic model definitions
- `EVIDENCE_MAP.md`: hypothesis-to-evidence tracking
- `claims/` + `proofs/`: explicit research claims and derivations
- `simulations/`: synthetic controlled demonstrations
- `src/qsg_mri/`: Python package
- `tests/`: unit tests for core behavior
- `docs/`: end-to-end technical narrative for OEM teams

## Safety and regulatory note

This repository is for research use only. It is not for diagnosis, patient care,
or scanner control. See `SAFETY_AND_REGULATORY.md` for full scope limits.
