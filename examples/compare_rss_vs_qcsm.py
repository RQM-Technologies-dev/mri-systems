"""Fast baseline-vs-candidate synthetic comparison demo."""

# ruff: noqa: E402

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from qsg_mri.metrics import artifact_energy, nmse, psnr
from qsg_mri.phantoms import synthetic_multicoil_sensitivities, synthetic_phantom
from qsg_mri.reconstruction import baseline_reconstruction, qcsm_coherence_weighted_fusion


def main() -> None:
    started = time.perf_counter()
    output_dir = REPO_ROOT / "examples" / "outputs" / "compare_rss_vs_qcsm"
    output_dir.mkdir(parents=True, exist_ok=True)

    size = 64
    coils = 4
    seed = 123
    noise_std = 0.01
    rng = np.random.default_rng(seed)

    phantom = synthetic_phantom(size=size)
    sens = synthetic_multicoil_sensitivities(num_coils=coils, size=size)
    coil_images = sens * phantom[None, :, :] + noise_std * (
        rng.standard_normal((coils, size, size)) + 1j * rng.standard_normal((coils, size, size))
    )
    multicoil_kspace = np.fft.ifftshift(
        np.fft.fft2(np.fft.fftshift(coil_images, axes=(-2, -1)), axes=(-2, -1)),
        axes=(-2, -1),
    )

    baseline = baseline_reconstruction(multicoil_kspace)
    q_out = qcsm_coherence_weighted_fusion(multicoil_kspace)
    candidate = q_out["reconstruction"]
    defect = q_out["coherence_defect"]
    runtime_seconds = float(time.perf_counter() - started)

    metrics = {
        "scenario_name": "examples_compare_rss_vs_qcsm",
        "baseline_method": "rss_ifft2_centered",
        "candidate_method": "qcsm_coherence_weighted_fusion_first_pass",
        "synthetic_only": True,
        "run_completed": True,
        "clinical_result": False,
        "result_scope": "synthetic_controlled_engineering_run",
        "target_achieved": False,
        "nmse": nmse(phantom, candidate),
        "psnr": psnr(phantom, candidate),
        "artifact_energy": artifact_energy(phantom, candidate),
        "coherence_score": float(np.mean(1.0 - defect)),
        "runtime_seconds": runtime_seconds,
        "notes": (
            "Synthetic controlled engineering evidence only; not clinical evidence. "
            "Quick package-level comparison demo."
        ),
        "baseline": {
            "method": "rss_ifft2_centered",
            "nmse": nmse(phantom, baseline),
            "psnr": psnr(phantom, baseline),
            "artifact_energy": artifact_energy(phantom, baseline),
        },
        "candidate": {
            "method": "qcsm_coherence_weighted_fusion_first_pass",
            "nmse": nmse(phantom, candidate),
            "psnr": psnr(phantom, candidate),
            "artifact_energy": artifact_energy(phantom, candidate),
            "mean_coherence_defect": float(np.mean(defect)),
        },
    }

    np.save(output_dir / "phantom.npy", phantom)
    np.save(output_dir / "baseline_reconstruction.npy", baseline)
    np.save(output_dir / "candidate_reconstruction.npy", candidate)
    np.save(output_dir / "baseline_error_map.npy", np.abs(baseline - phantom))
    np.save(output_dir / "candidate_error_map.npy", np.abs(candidate - phantom))
    np.save(output_dir / "coherence_defect_map.npy", defect)
    np.save(output_dir / "quaternion_components.npy", q_out["quaternion_components"])
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))

    print("Scenario: examples_compare_rss_vs_qcsm (synthetic only)")
    print("Baseline method:", metrics["baseline_method"])
    print("Candidate method:", metrics["candidate_method"])
    print("Baseline NMSE:", metrics["baseline"]["nmse"])
    print("Candidate NMSE:", metrics["candidate"]["nmse"])
    print("Baseline PSNR:", metrics["baseline"]["psnr"])
    print("Candidate PSNR:", metrics["candidate"]["psnr"])
    print("Mean coherence defect:", metrics["candidate"]["mean_coherence_defect"])
    print("Outputs:", output_dir)


if __name__ == "__main__":
    main()
