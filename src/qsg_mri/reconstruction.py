"""MRI reconstruction helpers.

This module is intentionally minimal and research-oriented. It supports
baseline-vs-candidate comparisons and research metric generation only.
It is not production-grade or clinically validated reconstruction software.
"""

from __future__ import annotations

import numpy as np

from .baselines import baseline_multicoil_from_kspace, inverse_fft2_centered
from .coherence import coherence_defect_map_from_fixed_axis_coils, coherence_map_from_fixed_axis_coils


def baseline_reconstruction(multicoil_kspace: np.ndarray) -> np.ndarray:
    """Baseline multicoil reconstruction used as controlled reference output."""
    return baseline_multicoil_from_kspace(multicoil_kspace)


def qcsm_coherence_weighted_fusion(multicoil_kspace: np.ndarray, eps: float = 1e-12) -> dict[str, np.ndarray]:
    """Run a first-pass coherence-weighted QCSM candidate reconstruction.

    This method is for synthetic/offline research use only, not clinically
    validated, and is designed to produce auditable baseline-vs-candidate
    artifacts.
    """
    multicoil_kspace = np.asarray(multicoil_kspace, dtype=np.complex128)
    if multicoil_kspace.ndim != 3:
        raise ValueError("multicoil_kspace must have shape (coils, height, width).")

    coil_images = np.stack([inverse_fft2_centered(k) for k in multicoil_kspace], axis=0)
    magnitude = np.abs(coil_images)
    phase = np.angle(coil_images)

    # Fixed-axis quaternionic components q_c = [mag*cos(phase), mag*sin(phase), 0, 0].
    q_real = magnitude * np.cos(phase)
    q_imag = magnitude * np.sin(phase)
    quaternion_components = np.stack(
        [
            np.mean(q_real, axis=0),
            np.mean(q_imag, axis=0),
            np.zeros_like(q_real[0]),
            np.zeros_like(q_real[0]),
        ],
        axis=0,
    )

    coherence_score_map = coherence_map_from_fixed_axis_coils(coil_images=coil_images, eps=eps)
    coherence_defect = coherence_defect_map_from_fixed_axis_coils(coil_images=coil_images, eps=eps)

    # Circular-mean phase reference from the complex sum across coils.
    reference_phase = np.angle(np.sum(coil_images, axis=0))
    phase_rotation = np.exp(1j * (reference_phase[None, :, :] - phase))
    aligned_coils = coil_images * phase_rotation

    # Magnitude and coherence-weighted fusion.
    weights = magnitude * (coherence_score_map[None, :, :] + eps)
    fused_complex = np.sum(weights * aligned_coils, axis=0) / (np.sum(weights, axis=0) + eps)
    reconstruction = np.abs(fused_complex)

    return {
        "reconstruction": reconstruction,
        "coherence_defect": coherence_defect,
        "quaternion_components": quaternion_components,
    }


qcsm_reconstruction_placeholder = qcsm_coherence_weighted_fusion
