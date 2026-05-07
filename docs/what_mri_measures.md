# What MRI Measures

MRI scanners acquire **complex-valued k-space measurements**. The coordinate \(k\) is a Fourier-space spatial-frequency coordinate, not an anatomical radius.

For coil \(c\):

\[
y_c(k) = \int_\Omega \rho(r) s_c(r)e^{-i2\pi k\cdot r}\,dr + \epsilon_c(k)
\]

Interpretation:

- center of k-space: low spatial frequencies (global contrast)
- outer k-space: high spatial frequencies (fine detail/edges)
- k-space direction: direction of spatial variation in image space
