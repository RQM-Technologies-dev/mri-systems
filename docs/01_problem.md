# 01 - Problem

MRI systems already acquire high-value complex multicoil data. The challenge is
not whether the scanner collects useful measurements, but how reliably software
reconstruction handles coupled failure modes across coils and time.

In practical workflows, coherence failures often appear as:

- coil disagreement in phase-sensitive regions
- sensitivity mismatch between channels
- motion-driven phase inconsistency
- undersampling artifacts concentrated in unstable regions
- local reconstruction instability that is hard to isolate with magnitude-only
  diagnostics

Many current pipelines address these with separate correction layers. That can
work well, but it can also make interactions between phase, geometry, motion,
and multichannel coherence harder to model as one problem.

This repository frames the issue as an engineering evaluation question:

1. Can a candidate representation layer better capture coupled coherence
   behavior?
2. Can that be tested in controlled benchmark settings with reproducible
   evidence artifacts?
3. Can teams evaluate integration feasibility without changing scanner hardware?

## Technical note

Standard per-coil measurement model:

\[
y_c(k) = \int_\Omega \rho(r) s_c(r) \exp(-i 2\pi k\cdot r) dr + \epsilon_c(k)
\]

where \(k\) is spatial-frequency coordinate (not anatomical radius), \(r\) is
image-space coordinate, \(\rho(r)\) is tissue magnetization, \(s_c(r)\) is coil
sensitivity, and \(\epsilon_c(k)\) is noise.
