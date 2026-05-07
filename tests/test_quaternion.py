import unittest

import numpy as np

from qsg_mri.quaternion import IDENTITY, fixed_axis_complex_state, multiply, norm


class QuaternionTests(unittest.TestCase):
    def test_quaternion_identity_multiplication(self):
        q = np.array([0.5, -1.0, 2.0, -3.0], dtype=float)
        self.assertTrue(np.allclose(multiply(IDENTITY, q), q))
        self.assertTrue(np.allclose(multiply(q, IDENTITY), q))

    def test_quaternion_norm(self):
        q = np.array([1.0, 2.0, 3.0, 4.0], dtype=float)
        self.assertAlmostEqual(norm(q), np.sqrt(30.0))

    def test_fixed_axis_complex_special_case(self):
        amplitude = 2.0
        phase = np.pi / 3
        q = fixed_axis_complex_state(amplitude=amplitude, phi=phase)
        self.assertTrue(np.allclose(q, np.array([amplitude * np.cos(phase), amplitude * np.sin(phase), 0.0, 0.0])))


if __name__ == "__main__":
    unittest.main()
