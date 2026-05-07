# 02 - Better representation

Complex numbers capture magnitude and phase. Quaternions add a structured
orientation axis, which may better represent coupled phase/coherence behavior
across coils.

The proposed upgrade is a candidate representation layer in software, not a
hardware redesign. Measured complex k-space remains the input. Existing complex
reconstruction remains the baseline.

## Conceptual shift

- Complex-domain methods typically use one phase axis per local signal.
- Quaternionic state modeling introduces a local orientation axis that can encode
  richer multichannel coupling behavior.
- The goal is coherence-aware reconstruction and diagnostics under difficult
  conditions (coil disagreement, motion, undersampling, artifact structure).

## Mathematical form (for technical reviewers)

Standard complex local signal:

\[
z(r) = A(r)\exp(i \phi(r))
\]

Quaternionic local signal state:

\[
q(r) = A(r)\left[\cos \phi(r) + u(r)\sin \phi(r)\right]
\]

with \(u(r)\) as a local unit imaginary quaternion axis.

## Backward compatibility

- Complex MRI is the fixed-axis case (\(u(r)=i\)).
- Existing complex pipelines are therefore preserved as a special case.
- This allows controlled benchmark comparisons and practical integration testing.
