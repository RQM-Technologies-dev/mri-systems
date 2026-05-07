"""medical_ultrasound_systems: research-only ultrasound software methods.

This package is intended for simulation and algorithm research workflows.
It does not provide clinical decision support or medical device functionality.
"""

from .beamforming import delay_and_sum_plane_wave, envelope_detect_fft, log_compress
from .coherence import channel_coherence_factor, coherence_score, quaternion_alignment_score
from .geometry import LinearArrayGeometry
from .metrics import correlation_coefficient, mse, normalized_cross_correlation, normalized_error, psnr
from .phantom import PointScatterer, PointScattererPhantom, random_point_phantom, single_point_phantom
from .pulse import gaussian_modulated_pulse, normalize_pulse
from .simulation import RFChannelData, simulate_pulse_echo_rf, synthetic_plane_wave

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "LinearArrayGeometry",
    "PointScatterer",
    "PointScattererPhantom",
    "random_point_phantom",
    "single_point_phantom",
    "gaussian_modulated_pulse",
    "normalize_pulse",
    "synthetic_plane_wave",
    "RFChannelData",
    "simulate_pulse_echo_rf",
    "delay_and_sum_plane_wave",
    "envelope_detect_fft",
    "log_compress",
    "coherence_score",
    "channel_coherence_factor",
    "quaternion_alignment_score",
    "mse",
    "normalized_error",
    "psnr",
    "correlation_coefficient",
    "normalized_cross_correlation",
]
