# Simulations

All simulations in this directory are synthetic controlled demonstrations for
research evidence generation. They are not clinical validation outputs.

Each simulation includes:

- `run.py`: runnable script with deterministic synthetic setup
- `config.yaml`: editable parameters
- output directory creation
- baseline reconstruction output
- quaternionic/coherence-aware placeholder output
- error map
- coherence defect map
- `metrics.json`
- `summary.md`

Run a simulation example:

```bash
python simulations/phantom_baseline/run.py
```
