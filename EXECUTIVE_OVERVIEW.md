# Executive Overview

## The upgrade in one sentence

MRI-systems tests whether quaternionic signal-state modeling can improve MRI
reconstruction software by treating phase, coil geometry, motion, and
multichannel coherence as one coupled representation.

## Why OEMs should care

- Small image-quality gains can matter in healthcare workflows.
- Better artifact tolerance and motion robustness can help reduce retakes.
- Reconstruction improvements can support throughput and product
  differentiation.
- Software-only offline evaluation lowers adoption risk.

## What remains unchanged

- Scanner hardware.
- Acquisition physics.
- Complex k-space input.
- Existing baseline reconstruction methods.

## What is new

- A quaternionic state layer in the reconstruction software stack.
- Coherence-aware fusion and diagnostics.
- Reproducible simulation framework for controlled benchmark comparisons.
- `qsg_mri` package components for testing and integration exploration.

## First evaluation target

Research target: test for 5-15% relative improvement in controlled
multicoil/coherence-sensitive reconstruction tasks.

## What this repo is not

- Not a clinical product.
- Not scanner control software.
- Not FDA-cleared.
- Not a claim of established superiority.
