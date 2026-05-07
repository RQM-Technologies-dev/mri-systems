"""Synthetic phantom baseline-vs-candidate evidence loop simulation."""

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


def _to_builtin(value: float | int | str) -> float | int | str:
    if isinstance(value, np.generic):
        return value.item()
    return value


def save_optional_pngs(output_dir: Path, arrays: dict[str, np.ndarray]) -> str:
    """Save PNG views when matplotlib is available."""
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return "PNG generation skipped (matplotlib unavailable)."

    for name, arr in arrays.items():
        image = np.asarray(arr, dtype=float)
        if np.allclose(image.max(), image.min()):
            image = np.zeros_like(image)
        plt.figure(figsize=(4, 4))
        cmap = "gray" if "error" not in name and "defect" not in name else "magma"
        plt.imshow(image, cmap=cmap)
        plt.colorbar(fraction=0.046, pad=0.04)
        plt.title(name.replace("_", " "))
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(output_dir / f"{name}.png", dpi=140)
        plt.close()
    return "PNG generation completed."


def main() -> None:
    started = time.perf_counter()
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
    candidate_output = qcsm_coherence_weighted_fusion(multicoil_kspace)
    candidate = candidate_output["reconstruction"]
    defect = candidate_output["coherence_defect"]
    coherence = 1.0 - defect

    baseline_error = np.abs(baseline - phantom)
    candidate_error = np.abs(candidate - phantom)
    runtime_seconds = float(time.perf_counter() - started)

    baseline_nmse = nmse(phantom, baseline)
    candidate_nmse = nmse(phantom, candidate)
    baseline_psnr = psnr(phantom, baseline)
    candidate_psnr = psnr(phantom, candidate)
    baseline_artifact = artifact_energy(phantom, baseline)
    candidate_artifact = artifact_energy(phantom, candidate)

    metrics = {
        "scenario_name": "phantom_baseline",
        "baseline_method": "rss_ifft2_centered",
        "candidate_method": "qcsm_coherence_weighted_fusion_first_pass",
        "synthetic_only": True,
        "achieved_result": True,
        "nmse": candidate_nmse,
        "psnr": candidate_psnr,
        "artifact_energy": candidate_artifact,
        "coherence_score": float(np.mean(coherence)),
        "runtime_seconds": runtime_seconds,
        "notes": (
            "Synthetic controlled engineering evidence only; not clinical evidence. "
            "This first-pass candidate is for offline comparison and auditability."
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
    }

    config_snapshot = {k: _to_builtin(v) for k, v in config.items()}
    config_snapshot["resolved_output_dir"] = str(output_dir)

    np.save(output_dir / "phantom.npy", phantom)
    np.save(output_dir / "baseline_reconstruction.npy", baseline)
    np.save(output_dir / "candidate_reconstruction.npy", candidate)
    np.save(output_dir / "qcsm_reconstruction.npy", candidate)
    np.save(output_dir / "baseline_error_map.npy", baseline_error)
    np.save(output_dir / "candidate_error_map.npy", candidate_error)
    np.save(output_dir / "error_map.npy", candidate_error)
    np.save(output_dir / "coherence_defect_map.npy", defect)
    np.save(output_dir / "quaternion_components.npy", candidate_output["quaternion_components"])
    (output_dir / "config_snapshot.json").write_text(json.dumps(config_snapshot, indent=2))
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))

    png_note = save_optional_pngs(
        output_dir=output_dir,
        arrays={
            "phantom": phantom,
            "baseline_reconstruction": baseline,
            "candidate_reconstruction": candidate,
            "baseline_error_map": baseline_error,
            "candidate_error_map": candidate_error,
            "coherence_defect_map": defect,
        },
    )

    (output_dir / "summary.md").write_text(
        "# Phantom baseline evidence summary\n\n"
        "## Scenario\n"
        "- Name: `phantom_baseline`\n"
        "- Synthetic only: `true`\n"
        "- Description: controlled phantom baseline-vs-candidate demonstration.\n\n"
        "## Input configuration\n"
        f"- seed: `{seed}`\n"
        f"- size: `{size}`\n"
        f"- coils: `{coils}`\n"
        f"- noise_std: `{noise_std}`\n\n"
        "## Methods\n"
        "- Baseline: `rss_ifft2_centered`\n"
        "- Candidate: `qcsm_coherence_weighted_fusion_first_pass`\n\n"
        "## Key metrics\n"
        "| Metric | Baseline | Candidate |\n"
        "|---|---:|---:|\n"
        f"| NMSE | {baseline_nmse:.6e} | {candidate_nmse:.6e} |\n"
        f"| PSNR | {baseline_psnr:.3f} | {candidate_psnr:.3f} |\n"
        f"| Artifact energy | {baseline_artifact:.6e} | {candidate_artifact:.6e} |\n\n"
        "## Relative changes\n"
        f"- NMSE change (% vs baseline): {metrics['relative_change']['nmse_percent']:.3f}\n"
        f"- Artifact energy change (% vs baseline): {metrics['relative_change']['artifact_energy_percent']:.3f}\n"
        f"- Mean coherence defect: {float(np.mean(defect)):.6f}\n"
        f"- Mean coherence score: {float(np.mean(coherence)):.6f}\n"
        f"- Runtime (s): {runtime_seconds:.6f}\n\n"
        "## Artifact list\n"
        "- `phantom.npy`\n"
        "- `baseline_reconstruction.npy`\n"
        "- `candidate_reconstruction.npy`\n"
        "- `baseline_error_map.npy`\n"
        "- `candidate_error_map.npy`\n"
        "- `coherence_defect_map.npy`\n"
        "- `quaternion_components.npy`\n"
        "- `metrics.json`\n"
        "- `config_snapshot.json`\n"
        f"- PNG note: {png_note}\n\n"
        "## Interpretation guardrail\n"
        "These outputs are controlled synthetic engineering artifacts. They are intended to decide whether "
        "deeper offline OEM replay is justified. They do not establish clinical performance.\n"
    )


if __name__ == "__main__":
    main()
