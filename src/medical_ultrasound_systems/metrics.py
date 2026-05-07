"""Lightweight metrics for ultrasound method benchmarking workflows."""

from __future__ import annotations

import numpy as np


def mse(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Mean squared error between reference and estimate arrays."""
    reference = np.asarray(reference, dtype=float)
    estimate = np.asarray(estimate, dtype=float)
    return float(np.mean((reference - estimate) ** 2))


def normalized_error(reference: np.ndarray, estimate: np.ndarray, eps: float = 1e-12) -> float:
    """Normalized L2 error with epsilon safeguarding."""
    reference = np.asarray(reference, dtype=float)
    estimate = np.asarray(estimate, dtype=float)
    num = np.linalg.norm(reference - estimate)
    den = np.linalg.norm(reference)
    return float(num / (den + eps))


def psnr(reference: np.ndarray, estimate: np.ndarray, data_range: float | None = None, eps: float = 1e-12) -> float:
    """Peak signal-to-noise ratio in decibels."""
    reference = np.asarray(reference, dtype=float)
    estimate = np.asarray(estimate, dtype=float)

    mse_value = mse(reference, estimate)
    if mse_value <= eps:
        return float("inf")

    if data_range is None:
        peak = float(np.max(reference) - np.min(reference))
    else:
        peak = float(data_range)
    peak = max(peak, eps)
    return float(20.0 * np.log10(peak) - 10.0 * np.log10(mse_value))


def correlation_coefficient(a: np.ndarray, b: np.ndarray, eps: float = 1e-12) -> float:
    """Pearson-like correlation coefficient for flattened arrays."""
    a_flat = np.asarray(a, dtype=float).ravel()
    b_flat = np.asarray(b, dtype=float).ravel()
    if a_flat.shape != b_flat.shape:
        raise ValueError("a and b must have matching sizes.")

    a_centered = a_flat - np.mean(a_flat)
    b_centered = b_flat - np.mean(b_flat)
    numerator = float(np.sum(a_centered * b_centered))
    denominator = float(np.linalg.norm(a_centered) * np.linalg.norm(b_centered))
    return float(numerator / (denominator + eps))


def normalized_cross_correlation(a: np.ndarray, b: np.ndarray, eps: float = 1e-12) -> float:
    """Cosine-style normalized cross correlation for flattened arrays."""
    a_flat = np.asarray(a, dtype=float).ravel()
    b_flat = np.asarray(b, dtype=float).ravel()
    if a_flat.shape != b_flat.shape:
        raise ValueError("a and b must have matching sizes.")

    numerator = float(np.sum(a_flat * b_flat))
    denominator = float(np.linalg.norm(a_flat) * np.linalg.norm(b_flat))
    return float(numerator / (denominator + eps))
