"""Coherence metrics for quaternionic coil states in controlled benchmarks.

Outputs from this module are research diagnostics and should not be interpreted
as clinical quality markers.
"""

from __future__ import annotations

import numpy as np


def coherence_score(qs: np.ndarray, weights: np.ndarray | None = None, eps: float = 1e-12) -> float:
    """Compute C_MRI for a local set of coil quaternion states.

    Args:
        qs: Quaternion states with shape (coils, 4).
        weights: Optional complex/real-like scalar weights with shape (coils,).

    Returns:
        Coherence score intended for reproducible candidate-method comparisons.
    """
    qs = np.asarray(qs, dtype=float)
    if qs.ndim != 2 or qs.shape[1] != 4:
        raise ValueError("qs must have shape (coils, 4).")
    if weights is None:
        alpha = np.ones(qs.shape[0], dtype=float)
    else:
        alpha = np.asarray(weights, dtype=float)
        if alpha.shape != (qs.shape[0],):
            raise ValueError("weights must have shape (coils,).")

    numerator = np.linalg.norm(np.sum(alpha[:, None] * qs, axis=0))
    denominator = float(np.sum(np.abs(alpha) * np.linalg.norm(qs, axis=1))) + eps
    return float(numerator / denominator)


def coherence_defect(qs: np.ndarray, weights: np.ndarray | None = None) -> float:
    """Return D_coh = 1 - C_MRI as a research defect diagnostic."""
    return float(1.0 - coherence_score(qs=qs, weights=weights))


def coherence_map_from_fixed_axis_coils(coil_images: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Compute per-pixel coherence map from fixed-axis complex coil images.

    For complex-valued coils interpreted as fixed-axis quaternion states, this map
    is equivalent to:
        abs(sum(coils)) / (sum(abs(coils)) + eps)
    """
    coil_images = np.asarray(coil_images, dtype=np.complex128)
    if coil_images.ndim != 3:
        raise ValueError("coil_images must have shape (coils, height, width).")

    coherent_sum = np.abs(np.sum(coil_images, axis=0))
    incoherent_sum = np.sum(np.abs(coil_images), axis=0)
    return coherent_sum / (incoherent_sum + eps)


def coherence_defect_map_from_fixed_axis_coils(coil_images: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Compute per-pixel coherence-defect map (1 - coherence map)."""
    return 1.0 - coherence_map_from_fixed_axis_coils(coil_images=coil_images, eps=eps)
