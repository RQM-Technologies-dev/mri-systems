# Proof note: quaternionic coil-state model

Per-coil local state:

\[
q_c(r) = A_c(r)\left[\cos\phi_c(r)+u_c(r)\sin\phi_c(r)\right]
\]

For unit \(u_c(r)\), this separates:

- amplitude \(A_c(r)\)
- phase \(\phi_c(r)\)
- orientation axis \(u_c(r)\)

The representation keeps phase information but can encode orientation/coherence
variation through axis changes across coils and space.

This note defines state structure only; it does not claim reconstruction
optimality.
