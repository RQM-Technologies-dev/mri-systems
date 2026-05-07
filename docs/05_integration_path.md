# 05 - Integration path

This repository is organized around an OEM-friendly software integration model:

```text
Existing MRI scanner
  → raw complex multicoil k-space
  → standard preprocessing
  → QSG-MRI quaternionic lift
  → coherence-aware fusion/reconstruction/diagnostics
  → standard image output + optional coherence/artifact maps
```

## Practical integration points

- No scanner hardware replacement is required.
- Measured complex k-space remains the input.
- Existing complex-domain reconstruction stack remains compatible.
- Initial validation can run as offline replay evaluation.
- A plugin/API layer can be explored later if controlled benchmark outcomes are
  promising.

## Suggested adoption sequence

1. Run controlled benchmark scenarios in this repository.
2. Review baseline vs candidate metrics and diagnostics.
3. Replay deidentified multicoil data in an offline environment.
4. Define a narrow integration surface in an existing reconstruction workflow.
5. Evaluate runtime, maintainability, and product fit before expansion.
