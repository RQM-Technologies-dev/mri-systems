import numpy as np


def nmse(reference: np.ndarray, estimate: np.ndarray, eps: float = 1e-12) -> float:
    num = np.linalg.norm(reference - estimate) ** 2
    den = np.linalg.norm(reference) ** 2 + eps
    return float(num / den)


def psnr(reference: np.ndarray, estimate: np.ndarray, data_range: float | None = None, eps: float = 1e-12) -> float:
    mse = np.mean((reference - estimate) ** 2)
    if mse <= eps:
        return float("inf")
    peak = np.max(reference) - np.min(reference) if data_range is None else data_range
    peak = max(float(peak), eps)
    return float(20 * np.log10(peak) - 10 * np.log10(float(mse)))


def artifact_energy(reference: np.ndarray, estimate: np.ndarray) -> float:
    """L2 energy of residual artifacts."""
    residual = estimate - reference
    return float(np.sum(np.abs(residual) ** 2))
