"""Simplified array geometry objects for ultrasound method research.

The geometry in this module is intentionally lightweight and is not a
manufacturer-specific probe model or medical device representation.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class LinearArrayGeometry:
    """Simplified linear-array geometry for synthetic research experiments.

    This class models a 2D x-z element layout with all elements at z=0.
    It is meant for algorithm prototyping and benchmark scaffolding only.
    """

    n_elements: int
    pitch_m: float
    center_frequency_hz: float | None = None
    metadata: dict | None = None

    def __post_init__(self) -> None:
        if self.n_elements <= 0:
            raise ValueError("n_elements must be positive.")
        if self.pitch_m <= 0:
            raise ValueError("pitch_m must be positive.")

    @property
    def center_index(self) -> float:
        """Fractional index of the lateral array center."""
        return 0.5 * (self.n_elements - 1)

    @property
    def aperture_m(self) -> float:
        """Active aperture length in meters."""
        return (self.n_elements - 1) * self.pitch_m

    @property
    def element_positions_m(self) -> np.ndarray:
        """Element x-z coordinates with shape (n_elements, 2), in meters."""
        x_m = (np.arange(self.n_elements, dtype=float) - self.center_index) * self.pitch_m
        z_m = np.zeros(self.n_elements, dtype=float)
        return np.stack([x_m, z_m], axis=1)
