import unittest

import numpy as np

from qsg_mri.metrics import artifact_energy, nmse, psnr


class MetricsTests(unittest.TestCase):
    def test_nmse_zero_when_equal(self):
        ref = np.array([1.0, 2.0, 3.0])
        self.assertAlmostEqual(nmse(ref, ref), 0.0)

    def test_nmse_positive_when_different(self):
        ref = np.array([1.0, 2.0, 3.0])
        est = np.array([1.0, 1.0, 1.0])
        self.assertGreater(nmse(ref, est), 0.0)

    def test_psnr_infinite_when_equal(self):
        ref = np.array([1.0, 2.0, 3.0])
        self.assertEqual(psnr(ref, ref), float("inf"))

    def test_artifact_energy_positive(self):
        ref = np.zeros((2, 2))
        est = np.ones((2, 2))
        self.assertAlmostEqual(artifact_energy(ref, est), 4.0)


if __name__ == "__main__":
    unittest.main()
