# EVIDENCE MAP

This table separates proposed value from achieved evidence. Each row is a
testable hypothesis with a planned evidence path. Target ranges are research
goals, not reported results.

## Evidence maturity scale

- Concept defined
- Code scaffolded
- Unit tested
- Synthetic simulation runnable
- Metrics generated
- External/deidentified data tested
- OEM replay tested

## Current evidence table

| Area | Hypothesis | Evidence type | Evidence maturity | Target metric | Limitations |
| --- | --- | --- | --- | --- | --- |
| Multicoil fusion | Quaternionic coil-state fusion can improve robustness when coil phase/orientation disagreement is elevated. | Synthetic multicoil phantom reconstruction with baseline vs QCSM outputs, error maps, and coherence maps. | Concept defined; code scaffolded; synthetic simulation scaffolded | 5-15% relative error/coherence improvement target | Synthetic conditions may not transfer to all acquisition protocols. |
| Artifact coherence mapping | Coherence defect maps can highlight artifact-prone regions more directly than magnitude-only residuals. | Controlled artifact injection with pixel-level localization metrics and defect maps. | Concept defined; code scaffolded; synthetic simulation scaffolded | 10-25% artifact-region detection improvement target | Mapping quality depends on artifact model realism and threshold policy. |
| Undersampling robustness | Coherence-aware fusion/regularization can reduce undersampling-related error concentration. | Undersampling masks on synthetic data with NMSE/PSNR comparisons. | Concept defined; code scaffolded; synthetic simulation scaffolded | 5-12% relative NMSE reduction target | Does not cover all acceleration factors or parallel imaging settings. |
| Motion/orientation robustness | Quaternionic orientation-aware states can reduce ghosting/artifact sensitivity in motion perturbations. | Synthetic motion corruption replay with artifact-energy and ghosting proxies. | Concept defined; code scaffolded; synthetic simulation scaffolded | 10-20% ghosting/artifact reduction target | Simplified motion simulators may not match full patient or sequence dynamics. |

No row is marked as externally validated unless measured external or OEM replay
evidence is available.

## Synthetic metrics schema interpretation

For simulation artifacts, use the following semantics consistently:

- `run_completed` means the script produced output artifacts.
- `synthetic_only` means controlled synthetic data was used.
- `clinical_result` remains `false` for synthetic runs.
- `result_scope` should be `synthetic_controlled_engineering_run`.
- `target_achieved` is `true` only when measured outputs explicitly demonstrate
  a predeclared target was met.

Synthetic run completion is not clinical evidence and does not, by itself,
establish target achievement.
