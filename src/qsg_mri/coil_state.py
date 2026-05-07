"""Quaternionic Coil-State Model (QCSM) placeholders.

The scanner measures complex k-space data. These helpers define software-side
quaternionic state representations for reconstruction experiments.
"""

import numpy as np

from .quaternion import Quaternion, from_polar_state


def coil_state_from_magnitude_phase(amplitude: float, phase: float, axis: np.ndarray) -> Quaternion:
    """Build per-coil local quaternionic state q_c(r) = A_c[cos(phi_c)+u_c sin(phi_c)]."""
    return from_polar_state(amplitude=amplitude, phase=phase, axis=axis)


def project_to_complex(q: Quaternion) -> complex:
    """Project quaternion state back to fixed-axis complex plane (w + i x).

    This is a placeholder projection used to enforce complex-data fidelity.
    """
    return complex(q.w, q.x)
