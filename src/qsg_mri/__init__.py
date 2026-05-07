"""qsg_mri: research package for controlled MRI reconstruction comparisons.

This package supports offline benchmark experiments and research metrics only.
It does not provide clinical validation or scanner-control functionality.
"""

from .baselines import baseline_multicoil_from_kspace, inverse_fft2_centered, root_sum_of_squares
from .coherence import coherence_defect, coherence_score
from .coil_state import construct_coil_state, multicoil_quaternionic_fusion, pack_two_complex_channels
from .kspace import centered_frequency_grid, kspace_radius
from .metrics import artifact_energy, nmse, psnr
from .phantoms import synthetic_multicoil_sensitivities, synthetic_phantom
from .quaternion import (
    IDENTITY,
    FIXED_AXIS_I,
    conjugate,
    fixed_axis_complex_state,
    from_axis_angle,
    multiply,
    norm,
    normalize,
)
from .reconstruction import baseline_reconstruction, qcsm_reconstruction_placeholder

__all__ = [
    "IDENTITY",
    "FIXED_AXIS_I",
    "conjugate",
    "norm",
    "normalize",
    "multiply",
    "from_axis_angle",
    "fixed_axis_complex_state",
    "kspace_radius",
    "centered_frequency_grid",
    "construct_coil_state",
    "pack_two_complex_channels",
    "multicoil_quaternionic_fusion",
    "coherence_score",
    "coherence_defect",
    "inverse_fft2_centered",
    "root_sum_of_squares",
    "baseline_multicoil_from_kspace",
    "baseline_reconstruction",
    "qcsm_reconstruction_placeholder",
    "synthetic_phantom",
    "synthetic_multicoil_sensitivities",
    "nmse",
    "psnr",
    "artifact_energy",
]
