"""Point-scatterer phantom definitions for research-only ultrasound simulations."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class PointScatterer:
    """Single point-like scatterer for synthetic pulse-echo experiments."""

    x_m: float
    z_m: float
    amplitude: float = 1.0

    def __post_init__(self) -> None:
        if self.z_m <= 0:
            raise ValueError("Scatterer depth z_m must be positive.")


@dataclass
class PointScattererPhantom:
    """Container for point scatterers used in synthetic research scenes."""

    scatterers: list[PointScatterer]
    metadata: dict | None = None

    def __post_init__(self) -> None:
        for scatterer in self.scatterers:
            if scatterer.z_m <= 0:
                raise ValueError("All scatterers must have positive z_m.")

    @property
    def n_scatterers(self) -> int:
        """Number of scatterers in the phantom."""
        return len(self.scatterers)

    def as_array(self) -> np.ndarray:
        """Return scatterers as array with columns [x_m, z_m, amplitude]."""
        if not self.scatterers:
            return np.zeros((0, 3), dtype=float)
        return np.asarray(
            [[scatterer.x_m, scatterer.z_m, scatterer.amplitude] for scatterer in self.scatterers],
            dtype=float,
        )


def single_point_phantom(x_m: float = 0.0, z_m: float = 0.03, amplitude: float = 1.0) -> PointScattererPhantom:
    """Construct a single-point phantom for quick baseline checks."""
    return PointScattererPhantom(scatterers=[PointScatterer(x_m=x_m, z_m=z_m, amplitude=amplitude)])


def random_point_phantom(
    n_scatterers: int,
    x_range_m: tuple[float, float] = (-0.01, 0.01),
    z_range_m: tuple[float, float] = (0.015, 0.06),
    seed: int | None = None,
) -> PointScattererPhantom:
    """Generate a random point-scatterer phantom in the provided x/z bounds."""
    if n_scatterers <= 0:
        raise ValueError("n_scatterers must be positive.")
    if x_range_m[0] >= x_range_m[1]:
        raise ValueError("x_range_m must be an increasing interval.")
    if z_range_m[0] <= 0 or z_range_m[0] >= z_range_m[1]:
        raise ValueError("z_range_m must be positive and increasing.")

    rng = np.random.default_rng(seed)
    x_vals = rng.uniform(x_range_m[0], x_range_m[1], size=n_scatterers)
    z_vals = rng.uniform(z_range_m[0], z_range_m[1], size=n_scatterers)
    amplitudes = rng.uniform(0.5, 1.0, size=n_scatterers)

    scatterers = [
        PointScatterer(x_m=float(x_m), z_m=float(z_m), amplitude=float(amplitude))
        for x_m, z_m, amplitude in zip(x_vals, z_vals, amplitudes)
    ]
    return PointScattererPhantom(scatterers=scatterers, metadata={"seed": seed})
