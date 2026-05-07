"""Coherence metrics for synthetic ultrasound channel-analysis research."""

from __future__ import annotations

import numpy as np


def coherence_score(states: np.ndarray, weights: np.ndarray | None = None, eps: float = 1e-12) -> float:
    """Compute a normalized coherence score for a set of channel states."""
    states = np.asarray(states)
    if states.ndim != 2:
        raise ValueError("states must have shape (channels, features).")

    if weights is None:
        alpha = np.ones(states.shape[0], dtype=float)
    else:
        alpha = np.asarray(weights, dtype=float)
        if alpha.shape != (states.shape[0],):
            raise ValueError("weights must have shape (channels,).")

    weighted_sum = np.sum(alpha[:, None] * states, axis=0)
    numerator = np.linalg.norm(weighted_sum)
    denominator = float(np.sum(np.abs(alpha) * np.linalg.norm(states, axis=1)) + eps)
    return float(np.clip(numerator / denominator, 0.0, 1.0))


def channel_coherence_factor(channel_values: np.ndarray, axis: int = 0) -> np.ndarray:
    """Compute conventional channel coherence factor.

    CF = |sum(x)|^2 / (N * sum(|x|^2) + eps)
    """
    channel_values = np.asarray(channel_values)
    if channel_values.size == 0:
        raise ValueError("channel_values must be non-empty.")

    n_channels = channel_values.shape[axis]
    if n_channels <= 0:
        raise ValueError("axis size must be positive.")

    eps = 1e-12
    coherent_power = np.abs(np.sum(channel_values, axis=axis)) ** 2
    incoherent_power = n_channels * np.sum(np.abs(channel_values) ** 2, axis=axis)
    cf = coherent_power / (incoherent_power + eps)
    return np.clip(cf, 0.0, 1.0)


def quaternion_alignment_score(reference: np.ndarray, observed: np.ndarray) -> float:
    """Domain-readable wrapper for coherence between reference and observed states."""
    reference = np.asarray(reference).ravel()
    observed = np.asarray(observed).ravel()
    if reference.shape != observed.shape:
        raise ValueError("reference and observed must have matching shapes.")
    if reference.size == 0:
        raise ValueError("reference and observed must be non-empty.")

    states = np.stack([reference, observed], axis=0)
    return coherence_score(states=states)
