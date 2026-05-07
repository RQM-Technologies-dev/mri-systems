import unittest

import numpy as np

from qsg_mri.kspace import ifft2c, rss_combine


class KSpaceTests(unittest.TestCase):
    def test_ifft2c_shape(self):
        kspace = np.ones((8, 8), dtype=np.complex128)
        image = ifft2c(kspace)
        self.assertEqual(image.shape, (8, 8))

    def test_rss_combine(self):
        coils = np.array([[[3.0, 4.0]], [[4.0, 3.0]]], dtype=np.complex128)
        combined = rss_combine(coils, axis=0)
        self.assertTrue(np.allclose(combined, [[5.0, 5.0]]))


if __name__ == "__main__":
    unittest.main()
