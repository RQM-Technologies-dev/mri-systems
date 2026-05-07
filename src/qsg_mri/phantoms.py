"""Synthetic phantom generators for controlled reconstruction benchmarks.

These utilities create reproducible synthetic inputs for offline evaluation.
They are not patient-data tools.
"""

from __future__ import annotations

import numpy as np


def synthetic_phantom(size: int = 128) -> np.ndarray:
    """Generate deterministic synthetic reference image for metric comparisons."""
    yy, xx = np.meshgrid(np.linspace(-1.0, 1.0, size), np.linspace(-1.0, 1.0, size), indexing="ij")
    r = np.sqrt(xx**2 + yy**2)
    phantom = np.zeros((size, size), dtype=float)
    phantom[r < 0.75] = 0.3
    phantom[r < 0.5] = 0.7
    phantom[(xx + 0.2) ** 2 + (yy - 0.15) ** 2 < 0.08**2] = 1.0
    return phantom


def synthetic_multicoil_sensitivities(num_coils: int = 8, size: int = 128) -> np.ndarray:
    """Generate simplified multicoil sensitivities for controlled stress tests."""
    yy, xx = np.meshgrid(np.linspace(-1.0, 1.0, size), np.linspace(-1.0, 1.0, size), indexing="ij")
    angle = np.arctan2(yy, xx)
    radius = np.sqrt(xx**2 + yy**2)

    sensitivities = np.zeros((num_coils, size, size), dtype=np.complex128)
    for coil in range(num_coils):
        offset = 2.0 * np.pi * coil / max(num_coils, 1)
        magnitude = np.clip(1.0 - 0.35 * radius + 0.05 * np.cos(angle - offset), 0.1, None)
        phase = angle - offset
        sensitivities[coil] = magnitude * np.exp(1j * phase)

    norm = np.sqrt(np.sum(np.abs(sensitivities) ** 2, axis=0, keepdims=True)) + 1e-12
    return sensitivities / norm
