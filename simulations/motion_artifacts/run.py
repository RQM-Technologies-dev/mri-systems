"""Synthetic motion/orientation artifact simulation."""

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


def main() -> None:
    started = time.perf_counter()
    config = read_config(Path(__file__).with_name("config.yaml"))
    seed = int(config.get("seed", 19))
    size = int(config.get("size", 96))
    coils = int(config.get("coils", 8))
    motion_strength = float(config.get("motion_strength", 1.2))
    output_dir = Path(__file__).parent / str(config.get("output_dir", "outputs"))
    output_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(seed)
    phantom = synthetic_phantom(size=size)
    sensitivities = synthetic_multicoil_sensitivities(num_coils=coils, size=size)
    coil_images = sensitivities * phantom[None, :, :]
    full_kspace = np.fft.ifftshift(
        np.fft.fft2(np.fft.fftshift(coil_images, axes=(-2, -1)), axes=(-2, -1)),
        axes=(-2, -1),
    )

    ky = np.linspace(-1.0, 1.0, size)
    line_phase = np.exp(1j * motion_strength * np.sin(2.0 * np.pi * ky))
    motion_profile = line_phase[None, :, None]
    random_coil_factor = np.exp(1j * rng.uniform(-0.25, 0.25, size=(coils, 1, 1)))
    multicoil_kspace = full_kspace * motion_profile * random_coil_factor

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
        "scenario_name": "motion_artifacts",
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
            "Motion-like phase modulation stress test for baseline-vs-candidate comparison."
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
        "motion_strength": motion_strength,
    }

    np.save(output_dir / "baseline_reconstruction.npy", baseline)
    np.save(output_dir / "qcsm_reconstruction.npy", q_recon)
    np.save(output_dir / "error_map.npy", error_map)
    np.save(output_dir / "coherence_defect_map.npy", defect)
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))
    (output_dir / "summary.md").write_text(
        "# Motion artifacts summary\n\n"
        "- Data: synthetic phantom with line-wise motion phase modulation\n"
        "- Outputs include baseline and first-pass coherence-aware candidate comparison\n"
        "- Note: controlled synthetic stress test only\n"
    )


if __name__ == "__main__":
    main()
