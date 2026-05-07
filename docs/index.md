# Medical Ultrasound Systems Docs Index

This repository is a research-software prototype for ultrasound wavefield
analysis, simulation, and baseline benchmarking. It is not clinical software
and should not be used for diagnosis or treatment decisions.

## Phase 1 capability

Phase 1 introduces a lightweight, dependency-minimal synthetic pipeline:

- Linear array geometry (`LinearArrayGeometry`)
- Point-scatterer phantom generation (`PointScattererPhantom`)
- Pulse-echo RF channel simulation (`simulate_pulse_echo_rf`)
- RF channel container with metadata (`RFChannelData`)
- Baseline plane-wave delay-and-sum beamforming
- Envelope detection and log compression utilities
- Coherence metrics and baseline error metrics for controlled comparisons

This capability is intended for method research and benchmark scaffolding only.
