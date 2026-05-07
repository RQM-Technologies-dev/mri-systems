import unittest

import numpy as np

from qsg_mri.baselines import root_sum_of_squares
from qsg_mri.kspace import centered_frequency_grid, kspace_radius


class KSpaceTests(unittest.TestCase):
    def test_kspace_radius_is_frequency_not_anatomy(self):
        center = kspace_radius(0.0, 0.0)
        outer = kspace_radius(8.0, 6.0)
        self.assertEqual(center, 0.0)
        self.assertGreater(outer, center)

    def test_centered_frequency_grid_shape(self):
        kx, ky = centered_frequency_grid((8, 10))
        self.assertEqual(kx.shape, (8, 10))
        self.assertEqual(ky.shape, (8, 10))

    def test_rss_baseline_shape_behavior(self):
        coil_images = np.ones((4, 8, 8), dtype=np.complex128)
        rss = root_sum_of_squares(coil_images, axis=0)
        self.assertEqual(rss.shape, (8, 8))


if __name__ == "__main__":
    unittest.main()
