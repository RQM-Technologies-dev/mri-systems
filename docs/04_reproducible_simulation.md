# 04 - Reproducible simulation

Simulations are for offline, controlled engineering evaluation. They are
designed to answer "is this worth deeper OEM testing?" not to prove clinical
performance.

## Required artifacts per simulation

Every simulation run should emit a complete artifact set so results are
replayable and auditable:

- `input_config.yaml` or `config.yaml`
- `baseline_output` image/array
- `candidate_output` image/array
- `error_map`
- `coherence_defect_map` (where applicable)
- `metrics.json`
- `summary.md`

If an artifact is not applicable to a specific scenario, `summary.md` should
state why.

## Required `metrics.json` fields

Every scenario should record the following fields:

- `scenario_name`
- `baseline_method`
- `candidate_method`
- `nmse`
- `psnr` (where applicable)
- `artifact_energy` (where applicable)
- `coherence_score` (where applicable)
- `runtime_seconds` (if implemented)
- `notes`
- `achieved_result`

Guardrail:
- `achieved_result` must be `false` unless the file contains a real measured
  benchmark result from an actual run.

## Simulation execution expectations

For each scenario:

1. Use the same input/config for baseline and candidate paths.
2. Generate all required artifacts in a deterministic output structure.
3. Write machine-readable metrics and a short human-readable summary.
4. Keep claims as research targets unless measured outputs are present.

## How to read results

- Lower NMSE is better.
- Higher PSNR is usually better.
- Lower artifact energy is better.
- Coherence-defect maps are diagnostic research outputs, not clinical maps.
- A successful simulation is **not** proof of clinical performance; it is
  evidence about whether offline OEM testing is worthwhile.

## Repository implementation pattern

Each scenario folder typically includes:

- `run.py` for deterministic execution
- `config.yaml` (or equivalent input config)
- artifact-writing logic for outputs and metrics

This structure keeps baseline-vs-candidate comparisons repeatable across teams.
