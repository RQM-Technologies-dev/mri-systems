import unittest

import numpy as np

from qsg_mri.coherence import coherence_defect, coherence_score


class CoherenceTests(unittest.TestCase):
    def test_coherence_score_near_one_for_aligned_states(self):
        qs = np.array([[1.0, 0.5, 0.0, 0.0], [2.0, 1.0, 0.0, 0.0]], dtype=float)
        self.assertGreater(coherence_score(qs), 0.999)

    def test_coherence_defect_increases_for_disagreeing_states(self):
        aligned = np.array([[1.0, 0.0, 0.0, 0.0], [0.8, 0.0, 0.0, 0.0]], dtype=float)
        disagreeing = np.array([[1.0, 0.0, 0.0, 0.0], [-1.0, 0.0, 0.0, 0.0]], dtype=float)
        self.assertGreater(coherence_defect(disagreeing), coherence_defect(aligned))


if __name__ == "__main__":
    unittest.main()
