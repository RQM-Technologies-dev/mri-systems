"""Baseline MRI reconstruction helpers."""

from __future__ import annotations

import numpy as np


def inverse_fft2_centered(kspace: np.ndarray) -> np.ndarray:
    """Centered inverse FFT for 2D k-space."""
    return np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(kspace)))


def root_sum_of_squares(coil_images: np.ndarray, axis: int = 0) -> np.ndarray:
    """Root-sum-of-squares multicoil magnitude fusion."""
    return np.sqrt(np.sum(np.abs(coil_images) ** 2, axis=axis))


def baseline_multicoil_from_kspace(multicoil_kspace: np.ndarray) -> np.ndarray:
    """Apply centered inverse FFT per coil and combine with RSS."""
    coil_images = np.stack([inverse_fft2_centered(k) for k in multicoil_kspace], axis=0)
    return root_sum_of_squares(coil_images, axis=0)
