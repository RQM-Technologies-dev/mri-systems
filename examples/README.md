# Examples

These scripts are small, practical entry points for technical evaluation.

## `minimal_quaternionic_state.py`

Shows the representation step: how complex-valued inputs are lifted into a
minimal quaternionic state form for controlled testing.

## `compare_rss_vs_qcsm.py`

Shows baseline-vs-candidate structure:

- baseline path (standard complex reconstruction flow)
- candidate path (QCSM/coherence-aware flow)
- side-by-side comparison scaffolding

## `generate_coherence_map.py`

Shows diagnostic output generation, specifically a coherence-defect style map
that can be inspected alongside reconstruction error artifacts.
