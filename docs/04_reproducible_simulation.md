# 04 - Reproducible simulation

Simulations are designed for offline evaluation in controlled synthetic
conditions. They provide reproducible engineering evidence artifacts, not
clinical validation.

## What an engineer or manager should expect after a run

Each simulation is designed to generate:

- baseline image output
- QCSM/coherence-aware output
- error map
- coherence-defect map
- `metrics.json`
- `summary.md`

## Why this matters for evaluation

- Baseline and candidate outputs are produced from the same synthetic input.
- Metrics are machine-readable and can be compared across runs.
- Coherence-defect maps provide additional diagnostics beyond magnitude-only
  error views.
- The workflow supports controlled benchmark iteration before any external data
  replay.

## Repository implementation pattern

Each scenario folder includes:

- `run.py` for deterministic execution logic
- `config.yaml` for editable benchmark parameters
- output folder creation and artifact writing

Use these outputs as evidence scaffolds for technical decision-making, not as
claims of achieved clinical performance.
