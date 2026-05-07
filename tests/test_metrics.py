import unittest

import numpy as np

from qsg_mri.metrics import nmse, psnr


class MetricsTests(unittest.TestCase):
    def test_nmse_zero_when_equal(self):
        ref = np.array([1.0, 2.0, 3.0])
        self.assertAlmostEqual(nmse(ref, ref), 0.0)

    def test_psnr_infinite_when_equal(self):
        ref = np.array([1.0, 2.0, 3.0])
        self.assertEqual(psnr(ref, ref), float("inf"))


if __name__ == "__main__":
    unittest.main()
