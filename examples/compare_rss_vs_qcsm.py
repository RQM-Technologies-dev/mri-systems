"""Compare baseline RSS reconstruction against placeholder QCSM output."""

from __future__ import annotations

import numpy as np

from qsg_mri.phantoms import synthetic_multicoil_sensitivities, synthetic_phantom
from qsg_mri.reconstruction import baseline_reconstruction, qcsm_reconstruction_placeholder


def main() -> None:
    size = 64
    coils = 4
    phantom = synthetic_phantom(size=size)
    sens = synthetic_multicoil_sensitivities(num_coils=coils, size=size)
    coil_images = sens * phantom[None, :, :]
    multicoil_kspace = np.fft.ifftshift(np.fft.fft2(np.fft.fftshift(coil_images, axes=(-2, -1)), axes=(-2, -1)), axes=(-2, -1))

    baseline = baseline_reconstruction(multicoil_kspace)
    q_out = qcsm_reconstruction_placeholder(multicoil_kspace)

    print("baseline shape:", baseline.shape)
    print("qcsm shape:", q_out["reconstruction"].shape)
    print("coherence defect mean:", float(np.mean(q_out["coherence_defect"])))


if __name__ == "__main__":
    main()
