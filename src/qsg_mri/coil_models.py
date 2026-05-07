import numpy as np


def normalize_sensitivities(sensitivities: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    denom = np.sqrt(np.sum(np.abs(sensitivities) ** 2, axis=0, keepdims=True))
    return sensitivities / (denom + eps)
