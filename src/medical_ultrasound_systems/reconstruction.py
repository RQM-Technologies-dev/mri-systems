"""Reconstruction placeholders for future ultrasound research extensions."""

from __future__ import annotations

import numpy as np


def baseline_reconstruction(image: np.ndarray) -> np.ndarray:
    """Return a pass-through baseline reconstruction placeholder."""
    return np.asarray(image, dtype=float)
