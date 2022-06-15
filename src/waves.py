# src/waves.py

from typing import Callable

import numpy as np


def wave(frequency: int, amplitude: int = 1, phase: int = 0) -> Callable:
    """
    Returns a closure based on the wave_ function.

    Parameters:
        frequency: int
        amplitude: int
        phase: int

    Returns:
        Callable
    """
    def _wave(time: float) -> float:
        """
        Generates a pure sine wave with the given
        frequency, amplitude, and phase.

        Parameters:
            time: float

        Returns:
            float
        """
        return amplitude * np.sin(2 * np.pi * frequency * time + phase)
    return _wave
