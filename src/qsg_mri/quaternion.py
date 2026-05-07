"""Quaternion utilities represented as NumPy arrays [w, x, y, z]."""

from __future__ import annotations

import numpy as np


QuaternionArray = np.ndarray
IDENTITY = np.array([1.0, 0.0, 0.0, 0.0], dtype=float)
FIXED_AXIS_I = np.array([1.0, 0.0, 0.0], dtype=float)


def as_quaternion(values: np.ndarray | list[float] | tuple[float, float, float, float]) -> QuaternionArray:
    """Return quaternion array with shape (4,) as [w, x, y, z]."""
    q = np.asarray(values, dtype=float)
    if q.shape != (4,):
        raise ValueError("Quaternion must have shape (4,) as [w, x, y, z].")
    return q


def conjugate(q: QuaternionArray) -> QuaternionArray:
    """Return quaternion conjugate [w, -x, -y, -z]."""
    q = as_quaternion(q)
    return np.array([q[0], -q[1], -q[2], -q[3]], dtype=float)


def norm(q: QuaternionArray) -> float:
    """Euclidean norm of quaternion components."""
    q = as_quaternion(q)
    return float(np.linalg.norm(q))


def normalize(q: QuaternionArray, eps: float = 1e-12) -> QuaternionArray:
    """Normalize quaternion to unit norm."""
    q = as_quaternion(q)
    qn = norm(q)
    if qn <= eps:
        raise ValueError("Cannot normalize near-zero quaternion.")
    return q / qn


def multiply(q1: QuaternionArray, q2: QuaternionArray) -> QuaternionArray:
    """Hamilton product of quaternions q1 and q2."""
    a = as_quaternion(q1)
    b = as_quaternion(q2)
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array(
        [
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        ],
        dtype=float,
    )


def _normalize_axis(axis: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    axis = np.asarray(axis, dtype=float)
    if axis.shape != (3,):
        raise ValueError("Axis must have shape (3,).")
    n = float(np.linalg.norm(axis))
    if n <= eps:
        raise ValueError("Axis must be non-zero.")
    return axis / n


def from_axis_angle(amplitude: float, phi: float, axis: np.ndarray) -> QuaternionArray:
    """Construct q = A[cos(phi) + u sin(phi)] for unit axis u."""
    u = _normalize_axis(axis)
    c = float(np.cos(phi))
    s = float(np.sin(phi))
    return np.array([amplitude * c, amplitude * s * u[0], amplitude * s * u[1], amplitude * s * u[2]], dtype=float)


def fixed_axis_complex_state(amplitude: float, phi: float) -> QuaternionArray:
    """Complex MRI special case with fixed axis u=i -> [A cos(phi), A sin(phi), 0, 0]."""
    return from_axis_angle(amplitude=amplitude, phi=phi, axis=FIXED_AXIS_I)


def quaternion_to_complex_fixed_axis(q: QuaternionArray) -> complex:
    """Project quaternion to complex value in fixed i-axis plane using (w + i*x)."""
    q = as_quaternion(q)
    return complex(float(q[0]), float(q[1]))
