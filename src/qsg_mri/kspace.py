import numpy as np


def ifft2c(kspace: np.ndarray) -> np.ndarray:
    """Run centered 2D inverse FFT used for MRI k-space processing.

    The input is shifted to move k-space center to the FFT origin, inverse
    transformed, then shifted back to center image-space coordinates.
    """
    return np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(kspace)))


def rss_combine(coil_images: np.ndarray, axis: int = 0) -> np.ndarray:
    """Root-sum-of-squares coil combination."""
    return np.sqrt(np.sum(np.abs(coil_images) ** 2, axis=axis))
