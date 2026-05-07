import unittest

import numpy as np

from qsg_mri.reconstruction import baseline_reconstruction, qcsm_reconstruction_placeholder


class ReconstructionTests(unittest.TestCase):
    def test_baseline_reconstruction_shape(self):
        multicoil_kspace = np.ones((2, 8, 8), dtype=np.complex128)
        image = baseline_reconstruction(multicoil_kspace)
        self.assertEqual(image.shape, (8, 8))

    def test_qcsm_placeholder_outputs(self):
        multicoil_kspace = np.ones((3, 8, 8), dtype=np.complex128)
        out = qcsm_reconstruction_placeholder(multicoil_kspace)
        self.assertEqual(out["reconstruction"].shape, (8, 8))
        self.assertEqual(out["coherence_defect"].shape, (8, 8))
        self.assertEqual(out["quaternion_components"].shape, (4, 8, 8))


if __name__ == "__main__":
    unittest.main()
