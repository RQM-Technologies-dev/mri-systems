import unittest

import numpy as np

from qsg_mri.kspace import ifft2c, is_high_spatial_frequency, rss_combine, spatial_frequency_radius


class KSpaceTests(unittest.TestCase):
    def test_ifft2c_shape(self):
        kspace = np.ones((8, 8), dtype=np.complex128)
        image = ifft2c(kspace)
        self.assertEqual(image.shape, (8, 8))

    def test_rss_combine(self):
        coils = np.array([[[3.0, 4.0]], [[4.0, 3.0]]], dtype=np.complex128)
        combined = rss_combine(coils, axis=0)
        self.assertTrue(np.allclose(combined, [[5.0, 5.0]]))

    def test_kspace_radius_is_frequency_not_anatomy(self):
        center = spatial_frequency_radius(0.0, 0.0)
        outer = spatial_frequency_radius(8.0, 6.0)
        self.assertEqual(center, 0.0)
        self.assertGreater(outer, center)
        self.assertTrue(is_high_spatial_frequency(8.0, 6.0, threshold=5.0))
        self.assertFalse(is_high_spatial_frequency(1.0, 1.0, threshold=5.0))


if __name__ == "__main__":
    unittest.main()
