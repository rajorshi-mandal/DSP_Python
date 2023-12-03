import numpy as np
import matplotlib.pyplot as plt
from  scipy import signal
from scipy.signal import firwin
from scipy.signal import freqz

def dft(signal, N=None, win=0):
    """
    Compute the Discrete Fourier Transform (DFT) of a signal.

    Parameters:
    signal (numpy.ndarray): Input signal (1-D numpy array).
    N (int or None): DFT point (optional). If None, N is set to the length of the signal.
    win (int): Window type (0 for rectangular, 1 for Bartlett, 2 for Hamming, 3 for Hann).

    Returns:
    numpy.ndarray: DFT spectrum (1-D numpy array).
    """
    # Check if N is provided, otherwise use the length of the signal
    if N is None:
        N = len(signal)

    # Generate the window based on the specified type
    window = generate_window(N, win)

    # Pad the signal with zeros to match the DFT point
    if len(signal) < N:
        signal = np.pad(signal, (0, N - len(signal)), 'constant')

    # Compute the DFT using FFT
    spectrum = np.fft.fft(signal * window, N)

    return spectrum

def idft(spectrum):
    """
    Compute the Inverse Discrete Fourier Transform (IDFT) of a spectrum.

    Parameters:
    spectrum (numpy.ndarray): Spectrum (1-D numpy array).

    Returns:
    numpy.ndarray: IDFT signal (1-D numpy array).
    """
    # Compute the IDFT using the inverse FFT
    signal = np.fft.ifft(spectrum)

    return signal

def generate_window(N, win_type):
    """
    Generate a window of a specified type and length.

    Parameters:
    N (int): Length of the window.
    win_type (int): Window type (0 for rectangular, 1 for Bartlett, 2 for Hamming, 3 for Hann).

    Returns:
    numpy.ndarray: Window (1-D numpy array).
    """
    if win_type == 0:  # Rectangular window
        window = np.ones(N)
    elif win_type == 1:  # Bartlett window
        window = np.bartlett(N)
    elif win_type == 2:  # Hamming window
        window = np.hamming(N)
    elif win_type == 3:  # Hann window
        window = np.hanning(N)
    else:  # Default to rectangular window
        window = np.ones(N)

    return window

def linearconv(x, h, mode=0, plotflag=False):
    """
    Perform linear convolution between input signal x and impulse response h.

    Parameters:
    x (numpy.ndarray): Input signal.
    h (numpy.ndarray): Impulse response.
    mode (int): Mode of convolution (0 for full, 1 for valid).
    plotflag (bool): Flag to indicate whether to plot the convolution result.

    Returns:
    numpy.ndarray: Convolution result.
    """
    # Compute the linear convolution
    conv_result = np.convolve(x, h, mode='full' if mode == 0 else 'valid')

    # Plot the convolution result if plotflag is True
    if plotflag:
        plt.plot(conv_result)
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')
        plt.title('Linear Convolution Result')
        plt.grid()
        plt.show()

    return conv_result


def circonv(x, h, plotflag=False):
    """
    Perform circular convolution between input signal x and impulse response h.

    Parameters:
    x (numpy.ndarray): Input signal.
    h (numpy.ndarray): Impulse response.
    plotflag (bool): Flag to indicate whether to plot the convolution result.

    Returns:
    numpy.ndarray: Convolution result.
    """
    # Compute the circular convolution using FFT
    X = np.fft.fft(x)
    H = np.fft.fft(h)
    conv_result = np.fft.ifft(X * H)

    # Plot the convolution result if plotflag is True
    if plotflag:
        plt.plot(conv_result.real)
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')
        plt.title('Circular Convolution Result')
        plt.grid()
        plt.show()

    return conv_result.real


def firdesign(tap, Fs, Fc, win="boxcar", fir_type='lowpass'):
    # Calculate the normalized cutoff frequency
    normalized_cutoff = Fc / (Fs / 2)
    
    # Design the FIR filter coefficients
    if fir_type == 'lowpass':
        b = firwin(tap, normalized_cutoff, window=win)
    elif fir_type == 'highpass':
        b = firwin(tap, normalized_cutoff, window=win, pass_zero=False)
    else:
        raise ValueError("Unsupported fir_type. Choose 'lowpass' or 'highpass'.")
    
    return b, [1.0]  # Return filter coefficients 'b' and 'a' (always [1.0] for FIR)




def coeff2freq_response(b, a):
    # Compute the frequency response
    w, H = freqz(b, a)
    
    return w, H

# dspmodule.py

def tf2polezero(b, a):
    """
    Convert transfer function coefficients to poles, zeros, and gain.

    Parameters:
    - b: Numerator coefficients of the transfer function.
    - a: Denominator coefficients of the transfer function.

    Returns:
    - z: Zeros of the transfer function.
    - p: Poles of the transfer function.
    - k: Gain of the transfer function.
    """
    z, p, k = signal.tf2zpk(b, a)   
    return z, p, k

def polezero2freq_response(z, p, k):
    """
    Convert poles, zeros, and gain to frequency response.

    Parameters:
    - z: Zeros of the transfer function.
    - p: Poles of the transfer function.
    - k: Gain of the transfer function.

    Returns:
    - w: Frequencies.
    - H: Frequency response.
    """
    w, H = signal.freqz_zpk(z, p, k)
    return w, H

def linearfilter(b, a, x):
    """
    Apply linear filtering to the input signal.

    Parameters:
    - b: Numerator coefficients of the filter.
    - a: Denominator coefficients of the filter.
    - x: Input signal.

    Returns:
    - y: Output signal after filtering.
    """
    y = signal.lfilter(b, a, x)
    return y

def butterorder(wp, wst, Ap, As, Fs):
    """
    Calculate the order and cutoff frequency for a Butterworth filter.

    Parameters:
    - wp: Passband edge frequency in rad/s.
    - wst: Stopband edge frequency in rad/s.
    - Ap: Maximum attenuation in the passband (dB).
    - As: Minimum attenuation in the stopband (dB).
    - Fs: Sampling frequency in Hz.

    Returns:
    - N: Order of the filter.
    - wc: Cutoff frequency in rad/s.
    """
    # Calculate the order using the approximation formula
    N = np.ceil((np.log10((10**(As / 10) - 1) / (10**(Ap / 10) - 1)) / (2 * np.log10(wst / wp))))
    
    # Calculate the cutoff frequency based on the provided specifications
    wc = min(wp / ((10**(Ap / 10) - 1)**(1 / (2 * N))), (Fs / 2) - 1e-9)

    return int(N), wc

def iirbutterdesign(N, wc, Fs, iir_type='lowpass'):
    """
    Design an IIR Butterworth filter.

    Parameters:
    - N: Order of the filter.
    - wc: Cutoff frequency in rad/s.
    - Fs: Sampling frequency in Hz.
    - iir_type: Type of the filter ('lowpass', 'highpass', 'bandpass', 'bandstop').

    Returns:
    - b: Numerator coefficients of the filter.
    - a: Denominator coefficients of the filter.
    """
    b, a = signal.butter(N, wc / (Fs / 2), btype=iir_type, analog=False)
    return b, a

# Additional utility functions if needed
# ...

# Example usage and testing
if __name__ == "__main__":
    # You can add some test cases or examples here
    pass
