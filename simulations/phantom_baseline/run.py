"""Synthetic phantom baseline reconstruction simulation.

This script generates controlled synthetic multicoil data, runs baseline RSS and
placeholder QCSM reconstruction, and writes reproducible outputs for evidence
tracking.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from qsg_mri.metrics import artifact_energy, nmse, psnr
from qsg_mri.phantoms import synthetic_multicoil_sensitivities, synthetic_phantom
from qsg_mri.reconstruction import baseline_reconstruction, qcsm_reconstruction_placeholder


def read_config(path: Path) -> dict[str, float | int | str]:
    cfg: dict[str, float | int | str] = {}
    for line in path.read_text().splitlines():
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        key, value = [p.strip() for p in text.split(":", maxsplit=1)]
        if value.isdigit():
            cfg[key] = int(value)
        else:
            try:
                cfg[key] = float(value)
            except ValueError:
                cfg[key] = value
    return cfg


def main() -> None:
    config = read_config(Path(__file__).with_name("config.yaml"))
    seed = int(config.get("seed", 7))
    size = int(config.get("size", 64))
    coils = int(config.get("coils", 4))
    noise_std = float(config.get("noise_std", 0.01))
    output_dir = Path(__file__).parent / str(config.get("output_dir", "outputs"))
    output_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(seed)
    phantom = synthetic_phantom(size=size)
    sensitivities = synthetic_multicoil_sensitivities(num_coils=coils, size=size)
    coil_images = sensitivities * phantom[None, :, :]
    coil_images = coil_images + noise_std * (
        rng.standard_normal(coil_images.shape) + 1j * rng.standard_normal(coil_images.shape)
    )
    multicoil_kspace = np.fft.ifftshift(
        np.fft.fft2(np.fft.fftshift(coil_images, axes=(-2, -1)), axes=(-2, -1)),
        axes=(-2, -1),
    )

    baseline = baseline_reconstruction(multicoil_kspace)
    q_out = qcsm_reconstruction_placeholder(multicoil_kspace)
    q_recon = q_out["reconstruction"]
    defect = q_out["coherence_defect"]

    error_map = np.abs(q_recon - phantom)
    metrics = {
        "scenario": "phantom_baseline",
        "synthetic_only": True,
        "baseline_nmse": nmse(phantom, baseline),
        "qcsm_nmse": nmse(phantom, q_recon),
        "baseline_psnr": psnr(phantom, baseline),
        "qcsm_psnr": psnr(phantom, q_recon),
        "baseline_artifact_energy": artifact_energy(phantom, baseline),
        "qcsm_artifact_energy": artifact_energy(phantom, q_recon),
        "mean_coherence_defect": float(np.mean(defect)),
    }

    np.save(output_dir / "phantom.npy", phantom)
    np.save(output_dir / "baseline_reconstruction.npy", baseline)
    np.save(output_dir / "qcsm_reconstruction.npy", q_recon)
    np.save(output_dir / "error_map.npy", error_map)
    np.save(output_dir / "coherence_defect_map.npy", defect)
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))
    (output_dir / "summary.md").write_text(
        "# Phantom baseline summary\n\n"
        "- Data: synthetic controlled phantom\n"
        "- Outputs: baseline, qcsm placeholder, error map, coherence defect map\n"
        "- Note: research scaffold only; no clinical claims\n"
    )


if __name__ == "__main__":
    main()
