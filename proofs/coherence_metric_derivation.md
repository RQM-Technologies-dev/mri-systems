# Proof note: coherence metric derivation

Given weighted local coil states \(q_c(r)\) and \(\alpha_c(r)\), define:

\[
C_{MRI}(r)=
\frac{\left\|\sum_c \alpha_c(r) q_c(r)\right\|}
{\sum_c |\alpha_c(r)|\|q_c(r)\|+\epsilon}
\]

By triangle inequality:

\[
\left\|\sum_c \alpha_c q_c\right\| \le \sum_c |\alpha_c|\|q_c\|
\]

so with \(\epsilon>0\), \(0 \le C_{MRI}(r) \le 1\) for finite states.

Define coherence defect:

\[
D_{coh}(r)=1-C_{MRI}(r)
\]

Then \(D_{coh}(r)\in[0,1]\), where higher values indicate greater local
orientation/state disagreement among coils.
