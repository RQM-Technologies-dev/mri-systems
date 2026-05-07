import unittest

import numpy as np

from qsg_mri.coil_state import construct_coil_state, pack_two_complex_channels


class CoilStateTests(unittest.TestCase):
    def test_pack_two_complex_channels_into_quaternion_components(self):
        z1 = 1.0 + 2.0j
        z2 = -3.0 + 4.0j
        q = pack_two_complex_channels(z1, z2)
        self.assertTrue(np.allclose(q, np.array([1.0, 2.0, -3.0, 4.0])))

    def test_construct_coil_state_shape(self):
        q = construct_coil_state(amplitude=2.0, phase=np.pi / 4.0, axis=np.array([0.0, 1.0, 0.0]))
        self.assertEqual(q.shape, (4,))


if __name__ == "__main__":
    unittest.main()
