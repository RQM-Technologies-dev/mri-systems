"""Minimal quaternion helpers for research-oriented signal representations."""

from __future__ import annotations

import numpy as np


def norm(q: np.ndarray) -> float:
    """Return Euclidean norm of quaternion-like vector."""
    q = np.asarray(q, dtype=float)
    return float(np.linalg.norm(q))


def normalize(q: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Normalize quaternion-like vector with epsilon safeguard."""
    q = np.asarray(q, dtype=float)
    q_norm = norm(q)
    if q_norm <= eps:
        return np.zeros_like(q)
    return q / q_norm


def conjugate(q: np.ndarray) -> np.ndarray:
    """Return quaternion conjugate for [w, x, y, z]."""
    q = np.asarray(q, dtype=float)
    if q.shape[-1] != 4:
        raise ValueError("q must have last dimension size 4.")
    result = np.array(q, copy=True)
    result[..., 1:] *= -1.0
    return result


def multiply(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    """Multiply two quaternions represented as [w, x, y, z]."""
    q1 = np.asarray(q1, dtype=float)
    q2 = np.asarray(q2, dtype=float)
    if q1.shape[-1] != 4 or q2.shape[-1] != 4:
        raise ValueError("q1 and q2 must have last dimension size 4.")

    w1, x1, y1, z1 = np.moveaxis(q1, -1, 0)
    w2, x2, y2, z2 = np.moveaxis(q2, -1, 0)
    return np.stack(
        [
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        ],
        axis=-1,
    )
