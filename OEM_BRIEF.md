# OEM Brief: Software-Only Upgrade Path for MRI Reconstruction Teams

## What is the upgrade?

`MRI-systems` evaluates a candidate representation layer for reconstruction
software: quaternionic signal-state modeling (QSG-MRI). The core idea is to
treat coupled phase, coil geometry, motion/orientation effects, and multicoil
coherence as one coherence-aware reconstruction problem instead of separate
correction layers.

## Why is it software-only?

- Measured complex k-space remains the input.
- Existing hardware is unchanged.
- Existing acquisition physics is unchanged.
- Existing baseline reconstruction methods remain available for comparison.
- The upgrade is a software-side layer that can be tested in offline replay.

## Where could this improve existing suites?

- Multicoil fusion under coil disagreement.
- Artifact localization via coherence-defect outputs.
- Undersampling robustness in controlled benchmark tasks.
- Motion/orientation robustness in stress-test conditions.
- Optional diagnostics that accompany standard image output.

## How would an OEM test it offline?

1. Install and run the provided simulation scripts.
2. Produce baseline output and QCSM/coherence-aware output from the same
   synthetic input.
3. Review generated metrics (`metrics.json`), error maps, and coherence-defect
   maps.
4. Compare behavior across scenarios before considering data from
   deidentified raw multicoil studies.

## What are first measurable success criteria?

Research targets (not reported results):

- Multicoil fusion: 5-15% target relative improvement in controlled error or
  coherence metrics.
- Artifact localization: 10-25% target improvement in controlled artifact-region
  detection.
- Undersampling robustness: 5-12% target relative NMSE reduction.
- Motion/orientation robustness: 10-20% target ghosting/artifact proxy
  reduction.
- Integration feasibility: acceptable offline runtime and implementation
  complexity for plugin/API exploration.

## What is not being claimed?

- No claim of clinical superiority.
- No claim of regulatory readiness.
- No claim of scanner-control capability.
- No claim that quaternionic methods replace complex MRI pipelines.

## Evaluation path for an OEM

1. Run baseline synthetic simulations.
2. Compare RSS/standard baselines against QCSM outputs.
3. Inspect metrics and coherence maps.
4. Decide whether to test on deidentified raw multicoil data.
5. Explore plugin/API integration with an existing reconstruction workflow.
