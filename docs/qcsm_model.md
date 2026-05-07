# Quaternionic Coil-State Model (QCSM)

Per-coil local state:

\[
q_c(r) = A_c(r)[\cos\phi_c(r) + u_c(r)\sin\phi_c(r)]
\]

QCSM reconstruction seeks a coherent quaternionic field while preserving agreement with measured **complex** k-space data through projection-back data-fidelity terms.

High-level objective:

\[
\hat q = \arg\min_q [\text{data fidelity} + \text{quaternionic regularity} + \text{coil-state coherence}]
\]
