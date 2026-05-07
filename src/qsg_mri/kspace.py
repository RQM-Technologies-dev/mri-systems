"""k-space helpers for MRI software-only evaluation workflows.

`k` is a spatial-frequency coordinate. It is not anatomical radius.
`k=0` corresponds to low spatial frequency content, and larger |k| corresponds
to finer spatial detail.

These utilities support controlled benchmark setup and analysis only.
"""

from __future__ import annotations

import numpy as np


def kspace_radius(kx: float, ky: float, kz: float | None = None) -> float:
    """Return Fourier-space radius |k| from k-space coordinates."""
    if kz is None:
        return float(np.sqrt(kx**2 + ky**2))
    return float(np.sqrt(kx**2 + ky**2 + kz**2))


def centered_frequency_grid(shape: tuple[int, ...]) -> tuple[np.ndarray, ...]:
    """Return centered frequency coordinate grids for the given shape."""
    axes = [np.fft.fftshift(np.fft.fftfreq(n)) for n in shape]
    return np.meshgrid(*axes, indexing="ij")
