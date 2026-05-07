# Proof note: projection back to complex k-space

Measured data is complex \(y_c(k)\). Let quaternionic latent states produce a
candidate complex signal through projection operator \(\Pi\):

\[
\tilde z_c(r) = \Pi(q_c(r)) \in \mathbb{C}
\]

Forward model comparison remains:

\[
\tilde y_c(k) = \mathcal{F}\{\tilde z_c(r)\},\qquad
\min \sum_{c,k} |\tilde y_c(k)-y_c(k)|^2
\]

Thus quaternionic internal modeling does not replace measured complex fidelity;
it augments representation while preserving complex-domain data constraints.
