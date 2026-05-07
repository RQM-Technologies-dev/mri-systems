"""Evaluation metrics for controlled MRI reconstruction experiments.

Metrics are for research comparison reporting and do not imply clinical
performance claims.
"""

from __future__ import annotations

import numpy as np


def nmse(reference: np.ndarray, estimate: np.ndarray, eps: float = 1e-12) -> float:
    """Normalized mean squared error for baseline-vs-candidate comparisons."""
    reference = np.asarray(reference, dtype=float)
    estimate = np.asarray(estimate, dtype=float)
    return float(np.linalg.norm(reference - estimate) ** 2 / (np.linalg.norm(reference) ** 2 + eps))


def psnr(reference: np.ndarray, estimate: np.ndarray, data_range: float | None = None, eps: float = 1e-12) -> float:
    """Peak signal-to-noise ratio for controlled benchmark reporting."""
    reference = np.asarray(reference, dtype=float)
    estimate = np.asarray(estimate, dtype=float)
    mse = float(np.mean((reference - estimate) ** 2))
    if mse <= eps:
        return float("inf")
    peak = float(np.max(reference) - np.min(reference)) if data_range is None else float(data_range)
    peak = max(peak, eps)
    return float(20.0 * np.log10(peak) - 10.0 * np.log10(mse))


def ssim_placeholder(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Placeholder SSIM function.

    A full SSIM implementation is intentionally omitted in this minimal package
    to avoid introducing unvalidated behavior.
    """
    raise NotImplementedError("SSIM is intentionally omitted in this minimal package.")


def artifact_energy(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Residual artifact energy (L2) for research-only artifact proxies."""
    reference = np.asarray(reference, dtype=float)
    estimate = np.asarray(estimate, dtype=float)
    residual = estimate - reference
    return float(np.sum(residual**2))
