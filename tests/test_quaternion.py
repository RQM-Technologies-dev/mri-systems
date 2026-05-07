import unittest

import numpy as np

from qsg_mri.quaternion import IDENTITY, Quaternion, from_polar_state, normalize_axis


class QuaternionTests(unittest.TestCase):
    def test_norm(self):
        q = Quaternion(1.0, 2.0, 3.0, 4.0)
        self.assertAlmostEqual(q.norm(), np.sqrt(30.0))

    def test_multiplication_identity(self):
        q = Quaternion(0.5, -1.0, 2.0, -3.0)
        self.assertEqual(IDENTITY.multiply(q), q)
        self.assertEqual(q.multiply(IDENTITY), q)

    def test_unit_axis_validation(self):
        axis = normalize_axis(np.array([0.0, 3.0, 4.0]))
        self.assertTrue(np.allclose(axis, np.array([0.0, 0.6, 0.8])))
        with self.assertRaises(ValueError):
            normalize_axis(np.array([0.0, 0.0, 0.0]))

    def test_fixed_axis_complex_special_case(self):
        amplitude = 2.0
        phase = np.pi / 3
        q = from_polar_state(amplitude, phase, np.array([1.0, 0.0, 0.0]))
        self.assertAlmostEqual(q.w, amplitude * np.cos(phase))
        self.assertAlmostEqual(q.x, amplitude * np.sin(phase))
        self.assertAlmostEqual(q.y, 0.0)
        self.assertAlmostEqual(q.z, 0.0)


if __name__ == "__main__":
    unittest.main()
