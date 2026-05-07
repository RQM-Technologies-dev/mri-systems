# 01 - Problem

Standard MRI acquisition is complex-valued and phase-sensitive, but modern
reconstruction failure modes are not only complex-scalar problems.

Canonical per-coil measurement model:

\[
y_c(k) = \int_\Omega \rho(r) s_c(r) \exp(-i 2\pi k\cdot r) dr + \epsilon_c(k)
\]

where:

- \(y_c(k)\): measured k-space data for coil \(c\)
- \(k\): Fourier-space / spatial-frequency coordinate
- \(r\): image-space coordinate
- \(\rho(r)\): tissue magnetization image
- \(s_c(r)\): coil sensitivity map
- \(\epsilon_c(k)\): noise

Important interpretation note:

- \(k\) is **not** anatomical radius.
- \(k=0\) is low spatial frequency.
- larger \(|k|\) corresponds to finer spatial detail.

In practical software reconstruction, quality is affected by:

- multichannel receiver-coil interactions
- coil sensitivity mismatch
- phase disagreement
- field variation
- undersampling
- motion artifacts
- reconstruction instability
- local coherence loss

The repository treats these as coupled software reconstruction issues suitable
for controlled evidence building.
