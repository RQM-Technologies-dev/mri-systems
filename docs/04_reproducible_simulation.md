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
- `synthetic_only`
- `run_completed`
- `clinical_result`
- `result_scope`
- `target_achieved`
- `runtime_seconds` (if implemented)
- `notes`

Guardrail:
- `run_completed` means the script finished and produced output artifacts.
- `target_achieved` means a predeclared research target was actually met in
  measured outputs.
- `synthetic_only` should remain `true` for controlled synthetic demonstrations.
- `clinical_result` should remain `false` for synthetic runs.
- `result_scope` should be `synthetic_controlled_engineering_run` for these
  scenarios.
- Synthetic engineering outputs are not clinical outputs.
- Do not mark research targets as achieved unless measured artifacts explicitly
  demonstrate target attainment.

Recommended detail structure (in addition to required top-level fields):

```json
{
  "baseline": {
    "method": "rss_ifft2_centered",
    "nmse": 0.0,
    "psnr": 0.0,
    "artifact_energy": 0.0
  },
  "candidate": {
    "method": "qcsm_coherence_weighted_fusion_first_pass",
    "nmse": 0.0,
    "psnr": 0.0,
    "artifact_energy": 0.0,
    "mean_coherence_defect": 0.0,
    "mean_coherence_score": 0.0
  },
  "relative_change": {
    "nmse_percent": 0.0,
    "artifact_energy_percent": 0.0
  }
}
```

## Simulation execution expectations

For each scenario:

1. Use the same input/config for baseline and candidate paths.
2. Generate all required artifacts in a deterministic output structure.
3. Write machine-readable metrics and a short human-readable summary.
4. Keep claims as research targets unless measured outputs are present.
5. Do not treat synthetic metrics as clinical evidence.

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
