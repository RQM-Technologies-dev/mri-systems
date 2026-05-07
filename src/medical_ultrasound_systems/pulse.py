"""Pulse models for synthetic ultrasound signal-processing research."""

from __future__ import annotations

import numpy as np


def gaussian_modulated_pulse(
    center_frequency_hz: float = 5e6,
    sample_rate_hz: float = 40e6,
    n_cycles: float = 2.5,
    fractional_bandwidth: float = 0.6,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate a real Gaussian-modulated cosine pulse.

    The implementation intentionally uses a simple analytic approximation:
    a Gaussian envelope with standard deviation derived from the requested
    fractional bandwidth multiplied by a cosine carrier.
    """
    if center_frequency_hz <= 0:
        raise ValueError("center_frequency_hz must be positive.")
    if sample_rate_hz <= 0:
        raise ValueError("sample_rate_hz must be positive.")
    if n_cycles <= 0:
        raise ValueError("n_cycles must be positive.")
    if fractional_bandwidth <= 0:
        raise ValueError("fractional_bandwidth must be positive.")

    sigma_t = np.sqrt(2.0 * np.log(2.0)) / (np.pi * fractional_bandwidth * center_frequency_hz)
    pulse_duration_s = n_cycles / center_frequency_hz
    half_span_s = 0.5 * max(pulse_duration_s, 6.0 * sigma_t)
    n_samples = int(np.ceil(2.0 * half_span_s * sample_rate_hz)) + 1

    time_s = (np.arange(n_samples, dtype=float) - 0.5 * (n_samples - 1)) / sample_rate_hz
    envelope = np.exp(-0.5 * (time_s / sigma_t) ** 2)
    carrier = np.cos(2.0 * np.pi * center_frequency_hz * time_s)
    pulse = envelope * carrier
    return time_s, pulse


def normalize_pulse(pulse: np.ndarray) -> np.ndarray:
    """Scale pulse amplitudes to unit peak magnitude."""
    pulse = np.asarray(pulse, dtype=float)
    peak = float(np.max(np.abs(pulse))) if pulse.size else 0.0
    if peak <= 1e-12:
        return np.zeros_like(pulse)
    return pulse / peak
