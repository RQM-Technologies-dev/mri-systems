# 05 - Integration path

This repository is organized around an OEM-friendly software evaluation model:

```text
Existing MRI scanner
  → raw complex multicoil k-space
  → standard preprocessing
  → QSG-MRI quaternionic lift
  → coherence-aware fusion/reconstruction/diagnostics
  → standard image output + optional coherence/artifact maps
```

## Offline evaluation mode

This is the default mode for technical assessment.

- Use stored raw complex multicoil k-space (or synthetic analogs).
- Run baseline and QSG-MRI candidate side-by-side.
- Do not modify scanner control or acquisition behavior.
- Do not use patient-facing deployment paths.

Purpose:
- Determine whether the candidate shows enough measurable value to justify
  deeper engineering work.

## Plugin mode

Future integration option for controlled OEM environments.

- QSG-MRI is exposed as an optional reconstruction plugin.
- Input: preprocessed complex multicoil k-space.
- Output: candidate reconstruction plus coherence diagnostics.
- Existing reconstruction remains available as fallback.

Purpose:
- Evaluate integration cost while preserving current reconstruction safety net.

## API mode

Future architecture option for internal tooling.

- A local/internal service exposes reconstruction or evaluation endpoints.
- Inputs: k-space arrays, coil metadata, configuration.
- Outputs: candidate reconstruction, metrics, diagnostic maps.

This describes potential software architecture, not a current clinical product.

## Decision gates

Before moving from offline evaluation to deeper integration, check:

1. Does it improve target metrics on controlled data?
2. Does it remain compatible with existing complex data assumptions?
3. Does it produce useful diagnostic maps for engineering analysis?
4. Is runtime acceptable for the intended evaluation or replay workflow?
5. Can it run offline before any integration with scanner-adjacent systems?
6. Does it avoid disruption to existing reconstruction workflow?

## Suggested adoption sequence

1. Run controlled simulation scenarios and collect artifacts.
2. Compare baseline vs candidate metrics and maps.
3. Replay a small deidentified dataset offline.
4. Evaluate runtime and integration complexity.
5. Decide whether plugin/API exploration is justified.
