# ROADMAP

## Stage 0 (current): technical cleanup and canonicalization

- Align documentation to a single MRI-first framing
- Define Quaternionic Coil-State Model (QCSM)
- Keep explicit complex-data fidelity constraints
- Remove clinical/regulatory overclaim language

## Stage 1: baseline reproductions

- Inverse FFT + RSS baseline
- Sensitivity-informed baseline (SENSE-style where available)
- Reproducible scripts and dataset manifests

## Stage 2: QCSM MVP

- Quaternionic coil-state representation per coil
- Projection-back data-fidelity loops to measured complex k-space
- Initial ablations on phase/coherence-sensitive failure modes

## Stage 3: benchmark expansion

- Undersampling and motion-corruption stress tests
- Artifact-energy and phase-consistency analysis
- Runtime/memory profiling

## Stage 4: OEM-facing evidence package

- Reproducible benchmark reports
- Integration guidance for software-only reconstruction upgrade paths
- Scope-limited conclusions tied to tested datasets and protocols
