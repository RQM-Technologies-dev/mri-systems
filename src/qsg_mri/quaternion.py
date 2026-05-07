"""Quaternion primitives for quaternionic MRI research models."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Quaternion:
    """Minimal scalar-vector quaternion representation: q = w + xi + yj + zk."""

    w: float
    x: float
    y: float
    z: float

    def as_tuple(self) -> tuple[float, float, float, float]:
        return self.w, self.x, self.y, self.z

    def conjugate(self) -> "Quaternion":
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def norm_squared(self) -> float:
        return self.w**2 + self.x**2 + self.y**2 + self.z**2

    def norm(self) -> float:
        return float(np.sqrt(self.norm_squared()))

    def multiply(self, other: "Quaternion") -> "Quaternion":
        """Hamilton product."""
        w1, x1, y1, z1 = self.as_tuple()
        w2, x2, y2, z2 = other.as_tuple()
        return Quaternion(
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        )

    def normalize(self, eps: float = 1e-12) -> "Quaternion":
        n = self.norm()
        if n <= eps:
            raise ValueError("Cannot normalize near-zero quaternion.")
        return Quaternion(self.w / n, self.x / n, self.y / n, self.z / n)


IDENTITY = Quaternion(1.0, 0.0, 0.0, 0.0)


def normalize_axis(axis: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Normalize a 3D quaternion-imaginary axis; raises on near-zero input."""
    axis = np.asarray(axis, dtype=float)
    if axis.shape != (3,):
        raise ValueError("Axis must be shape (3,).")
    n = float(np.linalg.norm(axis))
    if n <= eps:
        raise ValueError("Axis must be non-zero for quaternionic lift.")
    return axis / n


def from_polar_state(amplitude: float, phase: float, axis: np.ndarray) -> Quaternion:
    """Construct q = A[cos(phi) + u sin(phi)] from amplitude, phase, and axis."""
    u = normalize_axis(axis)
    c = float(np.cos(phase))
    s = float(np.sin(phase))
    return Quaternion(amplitude * c, amplitude * s * u[0], amplitude * s * u[1], amplitude * s * u[2])
