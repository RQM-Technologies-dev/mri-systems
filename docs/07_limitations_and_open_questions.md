# 07 - Limitations and open questions

## Current limitations

- Current simulations are synthetic and simplified.
- Quaternionic fusion/reconstruction code is placeholder-level.
- Coherence metrics are research diagnostics, not validated clinical markers.
- Runtime and memory behavior are not yet optimized for production workflows.

## Open technical questions

- Which coil-state parameterizations are most stable across sequences?
- How should projection-back constraints be tuned against noise and artifacts?
- Which coherence-defect definitions best correlate with real artifact regimes?
- What regularization forms preserve detail while reducing instability?

## Evidence gaps

- External dataset diversity
- Sequence/protocol breadth
- Robustness under realistic motion and field perturbations
- Reproducibility across independent implementations

## Scope guardrails

No claims in this repository should be interpreted as clinical efficacy,
regulatory readiness, or scanner-control capability.
