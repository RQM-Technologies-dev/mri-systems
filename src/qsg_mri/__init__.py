"""qsg_mri: quaternion-native MRI reconstruction research primitives."""

from .coil_state import coil_state_from_magnitude_phase, project_to_complex
from .kspace import ifft2c, is_high_spatial_frequency, rss_combine, spatial_frequency_radius
from .metrics import artifact_energy, nmse, psnr
from .quaternion import IDENTITY, Quaternion, from_polar_state, normalize_axis

__all__ = [
    "Quaternion",
    "IDENTITY",
    "normalize_axis",
    "from_polar_state",
    "ifft2c",
    "rss_combine",
    "spatial_frequency_radius",
    "is_high_spatial_frequency",
    "coil_state_from_magnitude_phase",
    "project_to_complex",
    "nmse",
    "psnr",
    "artifact_energy",
]
