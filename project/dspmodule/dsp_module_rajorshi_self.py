# dspmodule.py

import numpy as np
from scipy.signal import freqz
from scipy.signal import lfilter


def calculate_zeros_poles_gain(numerator_coeffs, denominator_coeffs):
    """
    Calculate zeros, poles, and gain from numerator and denominator coefficients.

    Parameters:
    numerator_coeffs (array-like): Numerator coefficients of the transfer function.
    denominator_coeffs (array-like): Denominator coefficients of the transfer function.

    Returns:
    zeros (array): Zeros of the transfer function.
    poles (array): Poles of the transfer function.
    gain (float): Gain of the transfer function.
    """
    num = np.array(numerator_coeffs)
    den = np.array(denominator_coeffs)
    zeros, poles = np.roots(num), np.roots(den)
    gain = num[0] / den[0]
    return zeros, poles, gain

def calculate_frequency_response(zeros, poles, gain, num_points=512):
    """
    Calculate the frequency response (H) from zeros, poles, and gain.

    Parameters:
    zeros (array-like): Zeros of the transfer function.
    poles (array-like): Poles of the transfer function.
    gain (float): Gain of the transfer function.
    num_points (int, optional): Number of points for frequency response calculation.

    Returns:
    w (array): Digital frequencies (omega).
    H (array): Frequency response.
    """
    w, h = freqz(b=np.poly(zeros), a=np.poly(poles), worN=num_points)
    H = gain * h
    return w, H

def linearfilter(b, a, x):
    """
    Apply a linear filter to the input signal.

    Parameters:
    b (numpy.ndarray): Numerator coefficients of the filter.
    a (numpy.ndarray): Denominator coefficients of the filter.
    x (numpy.ndarray): Input signal.

    Returns:
    numpy.ndarray: Output signal.
    """
    b = np.atleast_1d(b)
    a = np.atleast_1d(a)
    x = np.array(x).flatten()
    y = lfilter(b, a, x)
    return y