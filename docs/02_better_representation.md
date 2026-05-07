# 02 - Better representation

Standard complex local signal model:

\[
z(r) = A(r)\exp(i \phi(r))
\]

Quaternionic local signal state:

\[
q(r) = A(r)\left[\cos \phi(r) + u(r)\sin \phi(r)\right]
\]

with:

- \(A(r)\): local magnitude
- \(\phi(r)\): local phase
- \(u(r)\): local unit imaginary quaternion axis
- \(q(r)\): local quaternionic resonance state

## Why lift to quaternionic state?

Complex numbers are well-suited for single-axis phase representation.
Quaternionic states are being tested for scenarios where phase, orientation,
coil geometry, motion, and multichannel coupling are jointly relevant.

## Fixed-axis bridge to standard MRI

The model must remain backward-compatible:

- Set \(u(r)=i\) and the quaternionic model reduces to the standard complex case.
- Existing complex MRI is therefore a fixed-axis special case, not discarded.

This compatibility is the basis for controlled comparison and OEM integration.
