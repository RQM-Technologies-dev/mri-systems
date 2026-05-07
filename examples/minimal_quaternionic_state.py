"""Minimal example: construct a quaternionic MRI state from amplitude and phase."""

from __future__ import annotations

import numpy as np

from qsg_mri.quaternion import fixed_axis_complex_state, from_axis_angle


def main() -> None:
    q_general = from_axis_angle(amplitude=1.0, phi=np.pi / 4.0, axis=np.array([0.0, 1.0, 0.0]))
    q_fixed = fixed_axis_complex_state(amplitude=1.0, phi=np.pi / 4.0)
    print("general-axis quaternion:", q_general)
    print("fixed-axis quaternion:", q_fixed)


if __name__ == "__main__":
    main()
