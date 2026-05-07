# EVIDENCE MAP

All ranges below are **research targets** for controlled synthetic/offline
evaluation. They are not reported as achieved results.

| Area | Hypothesis | Evidence type | Current status | Target metric | Limitations |
| --- | --- | --- | --- | --- | --- |
| Multicoil fusion | Quaternionic coil-state fusion can improve robustness when coil phase/orientation disagreement is elevated. | Synthetic multicoil phantom reconstruction with baseline vs QCSM outputs, error maps, and coherence maps. | Scaffolded | 5-15% relative error/coherence improvement target | Synthetic conditions may not transfer to all acquisition protocols. |
| Artifact coherence mapping | Coherence defect maps can highlight artifact-prone regions more directly than magnitude-only residuals. | Controlled artifact injection with pixel-level localization metrics and defect maps. | Scaffolded | 10-25% artifact-region detection improvement target | Mapping quality depends on artifact model realism and threshold policy. |
| Undersampling robustness | Coherence-aware fusion/regularization can reduce undersampling-related error concentration. | Undersampling masks on synthetic data with NMSE/PSNR comparisons. | Scaffolded | 5-12% relative NMSE reduction target | Does not cover all acceleration factors or parallel imaging settings. |
| Motion/orientation robustness | Quaternionic orientation-aware states can reduce ghosting/artifact sensitivity in motion perturbations. | Synthetic motion corruption replay with artifact-energy and ghosting proxies. | Scaffolded | 10-20% ghosting/artifact reduction target | Simplified motion simulators may not match full patient or sequence dynamics. |
