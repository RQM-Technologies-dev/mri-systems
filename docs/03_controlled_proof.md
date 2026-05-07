# 03 - Controlled proof

In this repository, "proof" means reproducible engineering evidence for a
software-only upgrade path, not clinical validation.

The evidence model combines:

1. mathematical bridge definitions
2. code implementation in `src/qsg_mri/`
3. unit tests for core behavior
4. synthetic simulation scripts
5. metric outputs (`metrics.json`, maps, summaries)

## Proof obligations in engineering terms

1. Preserve compatibility with standard complex MRI.
2. Keep measured complex k-space as the data-fidelity target.
3. Show that quaternionic state construction and projection are implementable.
4. Generate controlled baseline-vs-candidate comparisons.
5. Produce auditable coherence-aware metrics and artifacts.

## Mathematical bridge (review layer)

Per-coil quaternionic state:

\[
q_c(r) = A_c(r)\left[\cos \phi_c(r) + u_c(r)\sin \phi_c(r)\right]
\]

Coherence score and defect:

\[
C_{MRI}(r) =
\frac{\left\|\sum_c \alpha_c(r) q_c(r)\right\|}
{\sum_c |\alpha_c(r)|\|q_c(r)\| + \epsilon}
\]

\[
D_{coh}(r) = 1 - C_{MRI}(r)
\]

These are used as research metrics in controlled benchmarks and should not be
interpreted as clinical outcome claims.
