import numpy as np
import matplotlib.pyplot as plt

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
# Additional utility functions if needed
# ...

# Example usage and testing
if __name__ == "__main__":
    # You can add some test cases or examples here
    pass
