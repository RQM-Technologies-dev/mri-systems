import numpy as np

from .reconstruction import baseline_multicoil_reconstruction


def fft_rss_baseline(multicoil_kspace: np.ndarray) -> np.ndarray:
    return baseline_multicoil_reconstruction(multicoil_kspace)
