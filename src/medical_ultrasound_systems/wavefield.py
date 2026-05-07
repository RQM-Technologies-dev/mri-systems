"""Wavefield helpers for lightweight ultrasound research simulations."""

from __future__ import annotations

import numpy as np


def plane_wave_travel_time(
    x_m: np.ndarray,
    z_m: np.ndarray,
    sound_speed_m_s: float = 1540.0,
    angle_rad: float = 0.0,
) -> np.ndarray:
    """Compute plane-wave travel time at x-z coordinates."""
    if sound_speed_m_s <= 0:
        raise ValueError("sound_speed_m_s must be positive.")
    x_m = np.asarray(x_m, dtype=float)
    z_m = np.asarray(z_m, dtype=float)
    return (x_m * np.sin(angle_rad) + z_m * np.cos(angle_rad)) / sound_speed_m_s
