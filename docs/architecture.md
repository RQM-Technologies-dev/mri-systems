# Phase 1 Architecture

The current Phase 1 prototype follows a synthetic research pipeline:

Linear array geometry
-> point-scatterer phantom
-> pulse-echo RF simulation
-> baseline delay-and-sum beamforming
-> envelope/log compression
-> coherence and error metrics
-> future quaternionic/QSG comparison layer

Design goals:

- Keep implementation lightweight and testable.
- Use only NumPy for core numerical methods in this phase.
- Preserve research-only scope without clinical positioning.
