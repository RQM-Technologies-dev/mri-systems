from dataclasses import dataclass


@dataclass(frozen=True)
class Quaternion:
    w: float
    x: float
    y: float
    z: float

    def conjugate(self) -> "Quaternion":
        """Return the quaternion conjugate by negating i/j/k components."""
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def norm_squared(self) -> float:
        """Return squared magnitude: w^2 + x^2 + y^2 + z^2."""
        return self.w**2 + self.x**2 + self.y**2 + self.z**2

    def as_tuple(self) -> tuple[float, float, float, float]:
        return self.w, self.x, self.y, self.z
