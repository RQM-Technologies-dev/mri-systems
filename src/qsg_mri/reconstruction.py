"""MRI reconstruction helpers.

This module is intentionally minimal and research-oriented. It is not
production-grade MRI reconstruction software.
"""

from __future__ import annotations

import numpy as np

from .baselines import baseline_multicoil_from_kspace, inverse_fft2_centered
from .coherence import coherence_score


def baseline_reconstruction(multicoil_kspace: np.ndarray) -> np.ndarray:
    """Baseline multicoil reconstruction via inverse FFT + RSS."""
    return baseline_multicoil_from_kspace(multicoil_kspace)


def qcsm_reconstruction_placeholder(multicoil_kspace: np.ndarray) -> dict[str, np.ndarray]:
    """Placeholder QCSM-style fusion.

    The function builds per-pixel quaternionic states from magnitude and phase
    moments, then computes a coherence-defect map. This is a controlled research
    baseline and not a validated clinical reconstruction method.
    """
    coil_images = np.stack([inverse_fft2_centered(k) for k in multicoil_kspace], axis=0)
    mag = np.abs(coil_images)
    phase = np.angle(coil_images)

    q_components = np.stack(
        [
            np.mean(mag * np.cos(phase), axis=0),
            np.mean(mag * np.sin(phase), axis=0),
            np.std(mag, axis=0),
            np.std(phase, axis=0),
        ],
        axis=0,
    )
    fused = np.linalg.norm(q_components, axis=0)

    # Compute coherence at each voxel from fixed-axis per-coil states.
    coils, height, width = coil_images.shape
    defect = np.zeros((height, width), dtype=float)
    for iy in range(height):
        for ix in range(width):
            states = np.zeros((coils, 4), dtype=float)
            states[:, 0] = mag[:, iy, ix] * np.cos(phase[:, iy, ix])
            states[:, 1] = mag[:, iy, ix] * np.sin(phase[:, iy, ix])
            c_score = coherence_score(states)
            defect[iy, ix] = 1.0 - c_score

    return {
        "reconstruction": fused,
        "coherence_defect": defect,
        "quaternion_components": q_components,
    }
