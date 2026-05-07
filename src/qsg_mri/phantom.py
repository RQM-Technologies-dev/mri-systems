import numpy as np


def circular_phantom(size: int = 64, radius_ratio: float = 0.35) -> np.ndarray:
    yy, xx = np.ogrid[:size, :size]
    cy = cx = (size - 1) / 2
    radius = size * radius_ratio
    mask = (yy - cy) ** 2 + (xx - cx) ** 2 <= radius**2
    phantom = np.zeros((size, size), dtype=float)
    phantom[mask] = 1.0
    return phantom
