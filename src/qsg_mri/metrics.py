import numpy as np


def nmse(reference: np.ndarray, estimate: np.ndarray, eps: float = 1e-12) -> float:
    """Compute normalized mean squared error with epsilon-safe denominator."""
    num = np.linalg.norm(reference - estimate) ** 2
    den = np.linalg.norm(reference) ** 2 + eps
    return float(num / den)


def psnr(reference: np.ndarray, estimate: np.ndarray, data_range: float | None = None, eps: float = 1e-12) -> float:
    """Compute PSNR, using reference range if data_range is not provided.

    Returns infinity when the inputs are numerically identical.
    """
    mse = np.mean((reference - estimate) ** 2)
    if mse <= eps:
        return float("inf")
    peak = np.max(reference) - np.min(reference) if data_range is None else data_range
    peak = max(float(peak), eps)
    return float(20 * np.log10(peak) - 10 * np.log10(float(mse)))
