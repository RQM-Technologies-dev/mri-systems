import numpy as np

from .kspace import ifft2c, rss_combine


def baseline_multicoil_reconstruction(multicoil_kspace: np.ndarray) -> np.ndarray:
    coil_images = np.stack([ifft2c(c) for c in multicoil_kspace], axis=0)
    return rss_combine(coil_images, axis=0)


def quaternionic_multicoil_fusion(multicoil_kspace: np.ndarray) -> dict[str, np.ndarray]:
    coil_images = np.stack([ifft2c(c) for c in multicoil_kspace], axis=0)
    mag = np.abs(coil_images)
    phase = np.angle(coil_images)

    q_w = np.mean(mag, axis=0)
    q_x = np.mean(np.cos(phase), axis=0)
    q_y = np.mean(np.sin(phase), axis=0)
    q_z = np.std(phase, axis=0)

    fused_image = np.sqrt(q_w**2 + q_x**2 + q_y**2 + q_z**2)
    phase_coherence = np.sqrt(q_x**2 + q_y**2)
    return {
        "fused_image": fused_image,
        "phase_coherence": phase_coherence,
        "quaternion_components": np.stack([q_w, q_x, q_y, q_z], axis=0),
    }
