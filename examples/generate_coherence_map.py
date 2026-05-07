"""Generate a coherence-defect map from synthetic multicoil data."""

from __future__ import annotations

import numpy as np

from qsg_mri.phantoms import synthetic_multicoil_sensitivities, synthetic_phantom
from qsg_mri.reconstruction import qcsm_coherence_weighted_fusion


def main() -> None:
    size = 64
    coils = 6
    phantom = synthetic_phantom(size=size)
    sens = synthetic_multicoil_sensitivities(num_coils=coils, size=size)
    coil_images = sens * phantom[None, :, :]
    multicoil_kspace = np.fft.ifftshift(np.fft.fft2(np.fft.fftshift(coil_images, axes=(-2, -1)), axes=(-2, -1)), axes=(-2, -1))

    out = qcsm_coherence_weighted_fusion(multicoil_kspace)
    coherence_defect = out["coherence_defect"]
    print("coherence defect map shape:", coherence_defect.shape)
    print("coherence defect range:", float(np.min(coherence_defect)), float(np.max(coherence_defect)))


if __name__ == "__main__":
    main()
