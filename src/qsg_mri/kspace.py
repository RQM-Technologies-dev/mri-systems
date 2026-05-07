"""k-space helpers for MRI reconstruction baselines.

Note: k-space coordinates are spatial-frequency coordinates, not anatomical radius.
"""

import numpy as np


def ifft2c(kspace: np.ndarray) -> np.ndarray:
    """Centered 2D inverse FFT (complex k-space -> image space)."""
    return np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(kspace)))


def rss_combine(coil_images: np.ndarray, axis: int = 0) -> np.ndarray:
    """Root-sum-of-squares coil combination."""
    return np.sqrt(np.sum(np.abs(coil_images) ** 2, axis=axis))


def spatial_frequency_radius(kx: float, ky: float) -> float:
    """Return |k| in Fourier space; larger values indicate finer spatial detail."""
    return float(np.hypot(kx, ky))


def is_high_spatial_frequency(kx: float, ky: float, threshold: float) -> bool:
    """Classify whether a k-space point is beyond a chosen high-frequency threshold."""
    return spatial_frequency_radius(kx, ky) >= threshold
