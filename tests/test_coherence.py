import unittest

import numpy as np

from qsg_mri.coherence import (
    coherence_defect,
    coherence_defect_map_from_fixed_axis_coils,
    coherence_map_from_fixed_axis_coils,
    coherence_score,
)


class CoherenceTests(unittest.TestCase):
    def test_coherence_score_near_one_for_aligned_states(self):
        qs = np.array([[1.0, 0.5, 0.0, 0.0], [2.0, 1.0, 0.0, 0.0]], dtype=float)
        self.assertGreater(coherence_score(qs), 0.999)

    def test_coherence_defect_increases_for_disagreeing_states(self):
        aligned = np.array([[1.0, 0.0, 0.0, 0.0], [0.8, 0.0, 0.0, 0.0]], dtype=float)
        disagreeing = np.array([[1.0, 0.0, 0.0, 0.0], [-1.0, 0.0, 0.0, 0.0]], dtype=float)
        self.assertGreater(coherence_defect(disagreeing), coherence_defect(aligned))

    def test_fixed_axis_coherence_map_is_near_one_for_aligned_coils(self):
        base = np.ones((16, 16), dtype=np.complex128)
        coils = np.stack([base, 2.0 * base, 0.5 * base], axis=0)
        cmap = coherence_map_from_fixed_axis_coils(coils)
        self.assertGreater(float(np.min(cmap)), 0.999)

    def test_fixed_axis_coherence_map_decreases_with_phase_disagreement(self):
        base = np.ones((16, 16), dtype=np.complex128)
        aligned = np.stack([base, base], axis=0)
        disagreeing = np.stack([base, -base], axis=0)
        aligned_mean = float(np.mean(coherence_map_from_fixed_axis_coils(aligned)))
        disagreeing_mean = float(np.mean(coherence_map_from_fixed_axis_coils(disagreeing)))
        self.assertGreater(aligned_mean, disagreeing_mean)

    def test_coherence_defect_map_matches_one_minus_coherence(self):
        base = np.ones((8, 8), dtype=np.complex128)
        coils = np.stack([base, 1j * base], axis=0)
        cmap = coherence_map_from_fixed_axis_coils(coils)
        dmap = coherence_defect_map_from_fixed_axis_coils(coils)
        self.assertTrue(np.allclose(dmap, 1.0 - cmap))


if __name__ == "__main__":
    unittest.main()
