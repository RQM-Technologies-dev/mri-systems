import numpy as np

from .kspace import ifft2c, rss_combine


def baseline_multicoil_reconstruction(multicoil_kspace: np.ndarray) -> np.ndarray:
    """Standard baseline: per-coil inverse FFT followed by RSS combination.

    Args:
        multicoil_kspace: Complex array with shape (coils, height, width).

    Returns:
        Magnitude image with shape (height, width).
    """
    coil_images = np.stack([ifft2c(c) for c in multicoil_kspace], axis=0)
    return rss_combine(coil_images, axis=0)


def quaternionic_multicoil_fusion(multicoil_kspace: np.ndarray) -> dict[str, np.ndarray]:
    """Compute a quaternion-inspired multicoil fusion representation.

    Args:
        multicoil_kspace: Complex array with shape (coils, height, width).

    Returns:
        Dictionary with:
          - fused_image: fused magnitude-like output, shape (height, width)
          - phase_coherence: phase coherence proxy, shape (height, width)
          - quaternion_components: stacked components [w, x, y, z], shape (4, height, width)
    """
    coil_images = np.stack([ifft2c(c) for c in multicoil_kspace], axis=0)
    mag = np.abs(coil_images)
    phase = np.angle(coil_images)

    magnitude_component = np.mean(mag, axis=0)
    phase_cos_component = np.mean(np.cos(phase), axis=0)
    phase_sin_component = np.mean(np.sin(phase), axis=0)
    phase_std_component = np.std(phase, axis=0)

    fused_image = np.sqrt(
        magnitude_component**2
        + phase_cos_component**2
        + phase_sin_component**2
        + phase_std_component**2
    )
    phase_coherence = np.sqrt(phase_cos_component**2 + phase_sin_component**2)
    return {
        "fused_image": fused_image,
        "phase_coherence": phase_coherence,
        "quaternion_components": np.stack(
            [
                magnitude_component,
                phase_cos_component,
                phase_sin_component,
                phase_std_component,
            ],
            axis=0,
        ),
    }
