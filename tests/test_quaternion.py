import unittest

from qsg_mri.quaternion import Quaternion


class QuaternionTests(unittest.TestCase):
    def test_conjugate(self):
        q = Quaternion(1.0, 2.0, -3.0, 4.0)
        self.assertEqual(q.conjugate(), Quaternion(1.0, -2.0, 3.0, -4.0))

    def test_norm_squared(self):
        q = Quaternion(1.0, 2.0, 3.0, 4.0)
        self.assertEqual(q.norm_squared(), 30.0)

    def test_double_conjugate_returns_original(self):
        q = Quaternion(1.0, -2.0, 3.0, -4.0)
        self.assertEqual(q.conjugate().conjugate(), q)


if __name__ == "__main__":
    unittest.main()
