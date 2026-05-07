import numpy as np
import pytest

from medical_ultrasound_systems.beamforming import delay_and_sum_plane_wave, envelope_detect_fft, log_compress
from medical_ultrasound_systems.coherence import channel_coherence_factor
from medical_ultrasound_systems.geometry import LinearArrayGeometry
from medical_ultrasound_systems.metrics import correlation_coefficient, normalized_cross_correlation, psnr
from medical_ultrasound_systems.phantom import PointScatterer, PointScattererPhantom, single_point_phantom
from medical_ultrasound_systems.pulse import gaussian_modulated_pulse
from medical_ultrasound_systems.simulation import RFChannelData, simulate_pulse_echo_rf


def test_linear_array_geometry_centering_and_shape() -> None:
    geometry = LinearArrayGeometry(n_elements=4, pitch_m=0.001)
    pos = geometry.element_positions_m
    assert pos.shape == (4, 2)
    assert np.allclose(pos[:, 1], 0.0)
    assert np.isclose(np.mean(pos[:, 0]), 0.0)
    assert np.isclose(geometry.aperture_m, 0.003)


def test_point_scatterer_phantom_validation_and_array() -> None:
    phantom = PointScattererPhantom(scatterers=[PointScatterer(x_m=0.0, z_m=0.02, amplitude=0.8)])
    arr = phantom.as_array()
    assert phantom.n_scatterers == 1
    assert arr.shape == (1, 3)
    assert np.allclose(arr[0], [0.0, 0.02, 0.8])

    with pytest.raises(ValueError):
        PointScatterer(x_m=0.0, z_m=0.0)


def test_gaussian_modulated_pulse_shapes_and_finite_values() -> None:
    t, p = gaussian_modulated_pulse()
    assert t.ndim == 1
    assert p.ndim == 1
    assert t.shape == p.shape
    assert t.size > 5
    assert np.all(np.isfinite(t))
    assert np.all(np.isfinite(p))


def test_simulate_pulse_echo_rf_returns_rf_channel_data_shape() -> None:
    geometry = LinearArrayGeometry(n_elements=8, pitch_m=0.0003)
    phantom = single_point_phantom(z_m=0.03)
    rf = simulate_pulse_echo_rf(geometry=geometry, phantom=phantom, duration_s=40e-6)
    assert isinstance(rf, RFChannelData)
    assert rf.samples.shape[0] == geometry.n_elements
    assert rf.samples.shape[1] == int(np.ceil(40e-6 * rf.sample_rate_hz))


def test_delay_and_sum_plane_wave_returns_expected_shape() -> None:
    geometry = LinearArrayGeometry(n_elements=8, pitch_m=0.0003)
    phantom = single_point_phantom(z_m=0.03)
    rf = simulate_pulse_echo_rf(geometry=geometry, phantom=phantom, duration_s=40e-6)
    x_grid = np.linspace(-0.005, 0.005, 21)
    z_grid = np.linspace(0.01, 0.05, 31)
    image = delay_and_sum_plane_wave(rf=rf, x_grid_m=x_grid, z_grid_m=z_grid)
    assert image.shape == (len(z_grid), len(x_grid))


def test_channel_coherence_factor_is_one_for_identical_constants() -> None:
    channels = np.ones((8, 10), dtype=float)
    cf = channel_coherence_factor(channels, axis=0)
    assert np.allclose(cf, 1.0)


def test_envelope_detect_fft_nonnegative() -> None:
    signal = np.sin(np.linspace(0.0, 4.0 * np.pi, 200))
    env = envelope_detect_fft(signal)
    assert np.all(env >= 0.0)


def test_log_compress_clips_to_unit_interval() -> None:
    image = np.array([[0.0, 0.2], [1.0, 2.0]], dtype=float)
    compressed = log_compress(image, dynamic_range_db=40.0)
    assert np.all(compressed >= 0.0)
    assert np.all(compressed <= 1.0)


def test_psnr_correlation_and_ncc_sanity() -> None:
    reference = np.array([0.0, 1.0, 2.0, 3.0], dtype=float)
    estimate = np.array([0.0, 0.9, 2.1, 2.9], dtype=float)
    assert np.isfinite(psnr(reference, estimate))
    assert correlation_coefficient(reference, reference) > 0.999
    assert normalized_cross_correlation(reference, reference) > 0.999
