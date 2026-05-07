"""Synthetic undersampling robustness simulation."""

# ruff: noqa: E402

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from qsg_mri.metrics import artifact_energy, nmse, psnr
from qsg_mri.phantoms import synthetic_multicoil_sensitivities, synthetic_phantom
from qsg_mri.reconstruction import baseline_reconstruction, qcsm_coherence_weighted_fusion


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


def make_cartesian_mask(size: int, acceleration: int) -> np.ndarray:
    mask = np.zeros((size, size), dtype=float)
    mask[::acceleration, :] = 1.0
    center = size // 8
    start = size // 2 - center
    stop = size // 2 + center
    mask[start:stop, :] = 1.0
    return mask


def main() -> None:
    started = time.perf_counter()
    config = read_config(Path(__file__).with_name("config.yaml"))
    seed = int(config.get("seed", 17))
    size = int(config.get("size", 96))
    coils = int(config.get("coils", 8))
    acceleration = int(config.get("acceleration", 4))
    output_dir = Path(__file__).parent / str(config.get("output_dir", "outputs"))
    output_dir.mkdir(parents=True, exist_ok=True)

    np.random.default_rng(seed)  # reserved for future stochastic variants
    phantom = synthetic_phantom(size=size)
    sensitivities = synthetic_multicoil_sensitivities(num_coils=coils, size=size)
    coil_images = sensitivities * phantom[None, :, :]
    full_kspace = np.fft.ifftshift(
        np.fft.fft2(np.fft.fftshift(coil_images, axes=(-2, -1)), axes=(-2, -1)),
        axes=(-2, -1),
    )

    mask = make_cartesian_mask(size=size, acceleration=acceleration)
    multicoil_kspace = full_kspace * mask[None, :, :]
    baseline = baseline_reconstruction(multicoil_kspace)
    q_out = qcsm_coherence_weighted_fusion(multicoil_kspace)
    q_recon = q_out["reconstruction"]
    defect = q_out["coherence_defect"]
    coherence = 1.0 - defect
    error_map = np.abs(q_recon - phantom)

    baseline_nmse = nmse(phantom, baseline)
    candidate_nmse = nmse(phantom, q_recon)
    baseline_psnr = psnr(phantom, baseline)
    candidate_psnr = psnr(phantom, q_recon)
    baseline_artifact = artifact_energy(phantom, baseline)
    candidate_artifact = artifact_energy(phantom, q_recon)
    runtime_seconds = float(time.perf_counter() - started)

    metrics = {
        "scenario_name": "undersampling",
        "baseline_method": "rss_ifft2_centered",
        "candidate_method": "qcsm_coherence_weighted_fusion_first_pass",
        "synthetic_only": True,
        "run_completed": True,
        "clinical_result": False,
        "result_scope": "synthetic_controlled_engineering_run",
        "target_achieved": False,
        "nmse": candidate_nmse,
        "psnr": candidate_psnr,
        "artifact_energy": candidate_artifact,
        "coherence_score": float(np.mean(coherence)),
        "runtime_seconds": runtime_seconds,
        "notes": (
            "Synthetic controlled engineering evidence only; not clinical evidence. "
            "Undersampling stress test for baseline-vs-candidate comparison."
        ),
        "baseline": {
            "method": "rss_ifft2_centered",
            "nmse": baseline_nmse,
            "psnr": baseline_psnr,
            "artifact_energy": baseline_artifact,
        },
        "candidate": {
            "method": "qcsm_coherence_weighted_fusion_first_pass",
            "nmse": candidate_nmse,
            "psnr": candidate_psnr,
            "artifact_energy": candidate_artifact,
            "mean_coherence_defect": float(np.mean(defect)),
        },
        "relative_change": {
            "nmse_percent": float(100.0 * (candidate_nmse - baseline_nmse) / (abs(baseline_nmse) + 1e-12)),
            "artifact_energy_percent": float(
                100.0 * (candidate_artifact - baseline_artifact) / (abs(baseline_artifact) + 1e-12)
            ),
        },
        "acceleration": acceleration,
        "sampling_fraction": float(np.mean(mask)),
    }

    np.save(output_dir / "sampling_mask.npy", mask.astype(np.float32))
    np.save(output_dir / "baseline_reconstruction.npy", baseline)
    np.save(output_dir / "qcsm_reconstruction.npy", q_recon)
    np.save(output_dir / "error_map.npy", error_map)
    np.save(output_dir / "coherence_defect_map.npy", defect)
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))
    (output_dir / "summary.md").write_text(
        "# Undersampling summary\n\n"
        "- Data: synthetic phantom with Cartesian undersampling mask\n"
        "- Outputs include sampling mask and reconstruction comparisons\n"
        "- Note: controlled synthetic benchmark scaffold only\n"
    )


if __name__ == "__main__":
    main()
