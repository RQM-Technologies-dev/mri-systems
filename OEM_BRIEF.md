# OEM Brief: Software-Only Quaternionic MRI Upgrade (Research Scope)

## The opportunity

MRI scanners already produce high-value complex multicoil k-space data, but
reconstruction quality can degrade when phase, coil geometry, orientation, and
motion effects interact. `qsg_mri` evaluates whether a quaternionic state model
improves coherence handling in those coupled conditions.

## What changes in the reconstruction stack

- Add a software-side quaternionic lift after standard preprocessing.
- Estimate coil-local quaternionic states and coherence scores.
- Fuse or regularize with coherence-aware logic.
- Project back to complex-domain data fidelity for measurement consistency.

## What does not change in the scanner

- No MRI hardware redesign.
- No sequence-control or scanner-control changes.
- Raw measured input remains complex multicoil k-space.
- Existing reconstruction baselines remain available as references.

## Initial target metrics (research targets, not achieved results)

- Multicoil fusion: evaluate 5-15% relative error/coherence improvement.
- Artifact localization: evaluate 10-25% improvement in artifact-region detection.
- Undersampling robustness: evaluate 5-12% relative NMSE reduction.
- Motion/orientation robustness: evaluate 10-20% ghosting/artifact reduction in
  controlled synthetic tests.

## Why this can be tested offline first

- Uses stored raw complex multicoil k-space.
- Can run as replay/offline reconstruction experiments.
- Produces paired outputs (baseline vs quaternionic/coherence-aware) and metrics.
- Keeps scanner-side acquisition unchanged during evidence generation.

## Why RQM Technologies is pursuing this

RQM Technologies is pursuing a software-first, evidence-driven path to determine
whether quaternionic state modeling can improve reconstruction robustness in
coherence-sensitive scenarios while preserving compatibility with standard MRI
data and workflows.
