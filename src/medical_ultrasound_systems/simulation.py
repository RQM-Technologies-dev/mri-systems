"""Synthetic ultrasound simulation helpers for method development.

These utilities provide simplified research placeholders and are not acoustic
field solvers, hardware simulators, or clinical-performance estimators.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .geometry import LinearArrayGeometry
from .phantom import PointScattererPhantom
from .pulse import gaussian_modulated_pulse, normalize_pulse


def synthetic_plane_wave(
    x_m: np.ndarray,
    z_m: np.ndarray,
    time_s: float,
    frequency_hz: float = 5e6,
    sound_speed_m_s: float = 1540.0,
    angle_rad: float = 0.0,
) -> np.ndarray:
    """Return a simple synthetic plane-wave phase field sample."""
    if frequency_hz <= 0:
        raise ValueError("frequency_hz must be positive.")
    if sound_speed_m_s <= 0:
        raise ValueError("sound_speed_m_s must be positive.")

    x_m = np.asarray(x_m, dtype=float)
    z_m = np.asarray(z_m, dtype=float)
    travel_time_s = (x_m * np.sin(angle_rad) + z_m * np.cos(angle_rad)) / sound_speed_m_s
    phase = 2.0 * np.pi * frequency_hz * (time_s - travel_time_s)
    return np.cos(phase)


@dataclass
class RFChannelData:
    """RF channel data for research pulse-echo baseline experiments."""

    samples: np.ndarray
    sample_rate_hz: float
    geometry: LinearArrayGeometry
    sound_speed_m_s: float = 1540.0
    metadata: dict | None = None

    def __post_init__(self) -> None:
        self.samples = np.asarray(self.samples, dtype=float)
        if self.samples.ndim != 2:
            raise ValueError("samples must be a 2D array with shape (channels, samples).")
        if self.sample_rate_hz <= 0:
            raise ValueError("sample_rate_hz must be positive.")
        if self.sound_speed_m_s <= 0:
            raise ValueError("sound_speed_m_s must be positive.")
        if self.samples.shape[0] != self.geometry.n_elements:
            raise ValueError("Number of channels must match geometry.n_elements.")

    @property
    def n_channels(self) -> int:
        """Number of receive channels."""
        return self.samples.shape[0]

    @property
    def n_samples(self) -> int:
        """Number of temporal samples per channel."""
        return self.samples.shape[1]


def simulate_pulse_echo_rf(
    geometry: LinearArrayGeometry,
    phantom: PointScattererPhantom,
    sample_rate_hz: float = 40e6,
    center_frequency_hz: float = 5e6,
    duration_s: float = 80e-6,
    sound_speed_m_s: float = 1540.0,
) -> RFChannelData:
    """Simulate pulse-echo RF data using a simple plane-wave transmit model.

    Assumptions:
    - Plane-wave transmit approximation with transmit path length equal to depth.
    - Receive path uses geometric point-to-element distance.
    - Scatterer response uses nearest-sample pulse insertion.
    - Attenuation uses a safeguarded 1 / distance factor.
    """
    if sample_rate_hz <= 0:
        raise ValueError("sample_rate_hz must be positive.")
    if center_frequency_hz <= 0:
        raise ValueError("center_frequency_hz must be positive.")
    if duration_s <= 0:
        raise ValueError("duration_s must be positive.")
    if sound_speed_m_s <= 0:
        raise ValueError("sound_speed_m_s must be positive.")

    n_samples = int(np.ceil(duration_s * sample_rate_hz))
    channel_samples = np.zeros((geometry.n_elements, n_samples), dtype=float)
    element_x_m = geometry.element_positions_m[:, 0]

    _, pulse = gaussian_modulated_pulse(
        center_frequency_hz=center_frequency_hz,
        sample_rate_hz=sample_rate_hz,
    )
    pulse = normalize_pulse(pulse)
    pulse_center = len(pulse) // 2

    for scatterer in phantom.scatterers:
        transmit_path_m = float(scatterer.z_m)
        receive_path_m = np.sqrt((element_x_m - scatterer.x_m) ** 2 + scatterer.z_m**2)
        total_distance_m = transmit_path_m + receive_path_m
        total_time_s = total_distance_m / sound_speed_m_s
        center_indices = np.rint(total_time_s * sample_rate_hz).astype(int)

        attenuation = 1.0 / np.maximum(total_distance_m, 1e-6)
        channel_gain = scatterer.amplitude * attenuation

        for channel_idx in range(geometry.n_elements):
            start = center_indices[channel_idx] - pulse_center
            stop = start + len(pulse)

            src_start = 0
            src_stop = len(pulse)
            if start < 0:
                src_start = -start
                start = 0
            if stop > n_samples:
                src_stop -= stop - n_samples
                stop = n_samples
            if start >= stop or src_start >= src_stop:
                continue

            channel_samples[channel_idx, start:stop] += channel_gain[channel_idx] * pulse[src_start:src_stop]

    metadata = {
        "model": "simplified_plane_wave_pulse_echo",
        "assumptions": [
            "plane_wave_transmit_approximation",
            "nearest_sample_pulse_insertion",
            "inverse_distance_attenuation",
            "research_placeholder_not_acoustic_solver",
        ],
        "center_frequency_hz": center_frequency_hz,
        "duration_s": duration_s,
    }
    return RFChannelData(
        samples=channel_samples,
        sample_rate_hz=sample_rate_hz,
        geometry=geometry,
        sound_speed_m_s=sound_speed_m_s,
        metadata=metadata,
    )
