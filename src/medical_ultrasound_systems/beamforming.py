"""Baseline beamforming utilities for synthetic ultrasound research data."""

from __future__ import annotations

import numpy as np

from .simulation import RFChannelData


def delay_and_sum_plane_wave(
    rf: RFChannelData,
    x_grid_m: np.ndarray,
    z_grid_m: np.ndarray,
    sound_speed_m_s: float | None = None,
) -> np.ndarray:
    """Compute a simple plane-wave delay-and-sum image on an x-z grid."""
    x_grid_m = np.asarray(x_grid_m, dtype=float)
    z_grid_m = np.asarray(z_grid_m, dtype=float)
    if x_grid_m.ndim != 1 or z_grid_m.ndim != 1:
        raise ValueError("x_grid_m and z_grid_m must be 1D arrays.")

    c_m_s = rf.sound_speed_m_s if sound_speed_m_s is None else float(sound_speed_m_s)
    if c_m_s <= 0:
        raise ValueError("sound_speed_m_s must be positive.")

    element_x_m = rf.geometry.element_positions_m[:, 0]
    sample_rate_hz = rf.sample_rate_hz
    image = np.zeros((len(z_grid_m), len(x_grid_m)), dtype=float)

    for z_idx, z_m in enumerate(z_grid_m):
        tx_time_s = z_m / c_m_s
        for x_idx, x_m in enumerate(x_grid_m):
            rx_time_s = np.sqrt((x_m - element_x_m) ** 2 + z_m**2) / c_m_s
            total_time_s = tx_time_s + rx_time_s
            sample_idx = np.rint(total_time_s * sample_rate_hz).astype(int)

            valid = (sample_idx >= 0) & (sample_idx < rf.n_samples)
            if not np.any(valid):
                continue

            chan_idx = np.nonzero(valid)[0]
            image[z_idx, x_idx] = np.sum(rf.samples[chan_idx, sample_idx[valid]])

    return image


def envelope_detect_fft(signal: np.ndarray, axis: int = -1) -> np.ndarray:
    """Compute envelope magnitude via FFT-based analytic signal construction."""
    signal = np.asarray(signal)
    if np.iscomplexobj(signal):
        raise ValueError("envelope_detect_fft expects real-valued input.")

    axis = int(axis)
    ndim = signal.ndim
    if ndim == 0:
        raise ValueError("signal must have at least one dimension.")
    if axis < -ndim or axis >= ndim:
        raise ValueError("axis out of range.")
    if axis < 0:
        axis += ndim

    n = signal.shape[axis]
    if n == 0:
        return np.abs(signal.astype(np.complex128))

    h = np.zeros(n, dtype=float)
    if n % 2 == 0:
        h[0] = 1.0
        h[n // 2] = 1.0
        h[1 : n // 2] = 2.0
    else:
        h[0] = 1.0
        h[1 : (n + 1) // 2] = 2.0

    shape = [1] * ndim
    shape[axis] = n
    h = h.reshape(shape)

    spectrum = np.fft.fft(signal, axis=axis)
    analytic_signal = np.fft.ifft(spectrum * h, axis=axis)
    return np.abs(analytic_signal)


def log_compress(image: np.ndarray, dynamic_range_db: float = 60.0) -> np.ndarray:
    """Log-compress image magnitude and normalize output to [0, 1]."""
    if dynamic_range_db <= 0:
        raise ValueError("dynamic_range_db must be positive.")

    image = np.asarray(image, dtype=float)
    magnitude = np.abs(image)
    peak = float(np.max(magnitude)) if magnitude.size else 0.0
    eps = 1e-12
    if peak <= eps:
        return np.zeros_like(magnitude)

    db_image = 20.0 * np.log10(np.maximum(magnitude, eps) / peak)
    db_clipped = np.clip(db_image, -dynamic_range_db, 0.0)
    return (db_clipped + dynamic_range_db) / dynamic_range_db
