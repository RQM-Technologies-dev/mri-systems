import unittest

import numpy as np

from qsg_mri.reconstruction import baseline_multicoil_reconstruction, quaternionic_multicoil_fusion


class ReconstructionTests(unittest.TestCase):
    def test_baseline_multicoil_reconstruction_shape(self):
        multicoil_kspace = np.ones((2, 8, 8), dtype=np.complex128)
        image = baseline_multicoil_reconstruction(multicoil_kspace)
        self.assertEqual(image.shape, (8, 8))

    def test_quaternionic_multicoil_fusion_outputs(self):
        multicoil_kspace = np.ones((3, 8, 8), dtype=np.complex128)
        out = quaternionic_multicoil_fusion(multicoil_kspace)
        self.assertEqual(out["fused_image"].shape, (8, 8))
        self.assertEqual(out["phase_coherence"].shape, (8, 8))
        self.assertEqual(out["quaternion_components"].shape, (4, 8, 8))


if __name__ == "__main__":
    unittest.main()
