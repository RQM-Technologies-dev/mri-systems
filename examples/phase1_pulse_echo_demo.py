"""Phase 1 synthetic pulse-echo demo for research-only experimentation.

This script demonstrates the software-method pipeline without any clinical
claims, hardware assumptions, or diagnostic interpretation.
"""

from __future__ import annotations

import numpy as np

from medical_ultrasound_systems.beamforming import delay_and_sum_plane_wave, envelope_detect_fft, log_compress
from medical_ultrasound_systems.geometry import LinearArrayGeometry
from medical_ultrasound_systems.phantom import single_point_phantom
from medical_ultrasound_systems.simulation import simulate_pulse_echo_rf


def main() -> None:
    geometry = LinearArrayGeometry(n_elements=32, pitch_m=0.0003, center_frequency_hz=5e6)
    phantom = single_point_phantom(x_m=0.0, z_m=0.03, amplitude=1.0)

    rf = simulate_pulse_echo_rf(
        geometry=geometry,
        phantom=phantom,
        sample_rate_hz=40e6,
        center_frequency_hz=5e6,
        duration_s=80e-6,
    )

    x_grid_m = np.linspace(-0.01, 0.01, 96)
    z_grid_m = np.linspace(0.01, 0.06, 160)
    das_image = delay_and_sum_plane_wave(rf, x_grid_m=x_grid_m, z_grid_m=z_grid_m)

    envelope_image = envelope_detect_fft(das_image, axis=0)
    compressed = log_compress(envelope_image)

    max_idx = np.unravel_index(int(np.argmax(compressed)), compressed.shape)
    max_location = (float(x_grid_m[max_idx[1]]), float(z_grid_m[max_idx[0]]))

    print(f"RF shape: {rf.samples.shape}")
    print(f"Image shape: {compressed.shape}")
    print(f"Max image value: {float(np.max(compressed)):.6f}")
    print(f"Approximate max response location (x_m, z_m): {max_location}")


if __name__ == "__main__":
    main()
