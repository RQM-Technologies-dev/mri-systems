"""Coil-state construction helpers for QCSM benchmark comparisons.

Functions in this module are designed for controlled offline evaluation and
research metric generation. They are not clinical reconstruction claims.
"""

from __future__ import annotations

import numpy as np

from .quaternion import as_quaternion, fixed_axis_complex_state, from_axis_angle


def construct_coil_state(amplitude: float, phase: float, axis: np.ndarray) -> np.ndarray:
    """Construct per-coil quaternionic state used in testable comparisons."""
    return from_axis_angle(amplitude=amplitude, phi=phase, axis=axis)


def construct_coil_state_from_complex(z: complex) -> np.ndarray:
    """Lift complex scalar to fixed-axis state for compatibility checks."""
    return fixed_axis_complex_state(amplitude=abs(z), phi=float(np.angle(z)))


def pack_two_complex_channels(z1: complex, z2: complex) -> np.ndarray:
    """Pack two complex channels for controlled channel-coupling experiments."""
    return np.array([np.real(z1), np.imag(z1), np.real(z2), np.imag(z2)], dtype=float)


def multicoil_quaternionic_fusion(states: np.ndarray, weights: np.ndarray | None = None) -> np.ndarray:
    """Placeholder weighted fusion for quaternionic coil states.

    Args:
        states: Array with shape (coils, 4).
        weights: Optional per-coil weights with shape (coils,).

    Returns:
        Research-only fused state for baseline-vs-candidate comparisons.
    """
    states = np.asarray(states, dtype=float)
    if states.ndim != 2 or states.shape[1] != 4:
        raise ValueError("states must have shape (coils, 4).")
    if weights is None:
        w = np.ones(states.shape[0], dtype=float)
    else:
        w = np.asarray(weights, dtype=float)
        if w.shape != (states.shape[0],):
            raise ValueError("weights must have shape (coils,).")
    weighted = w[:, None] * states
    fused = np.sum(weighted, axis=0) / (np.sum(np.abs(w)) + 1e-12)
    return as_quaternion(fused)
