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

    def test_metrics_are_finite_for_normal_arrays(self):
        ref = np.array([[0.1, 0.2], [0.3, 0.4]], dtype=float)
        est = np.array([[0.12, 0.18], [0.28, 0.43]], dtype=float)
        self.assertTrue(np.isfinite(nmse(ref, est)))
        self.assertTrue(np.isfinite(psnr(ref, est)))
        self.assertTrue(np.isfinite(artifact_energy(ref, est)))


if __name__ == "__main__":
    unittest.main()
