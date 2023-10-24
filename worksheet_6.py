import numpy as np
from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt

def firdesign(tap, Fs, Fc, win="boxcar", fir_type='lowpass'):
    # Calculate the normalized cutoff frequency
    normalized_cutoff = Fc / (Fs / 2)
    
    # Design the FIR filter coefficients
    if fir_type == 'lowpass':
        b = firwin(tap, normalized_cutoff, window=win)
    elif fir_type == 'highpass':
        b = firwin(tap, normalized_cutoff, window=win, pass_zero=False)
    else:
        raise ValueError("Unsupported fir_type. Choose 'lowpass' or 'highpass.")
    
    return b, [1.0]  # Return filter coefficients 'b' and 'a' (always [1.0] for FIR)

def coeff2freq_response(b, a):
    # Compute the frequency response
    w, H = freqz(b, a)
    
    return w, H

# Filter specifications
Fs = 8000  # Sampling rate
Fc_highpass = 2500  # Highpass cutoff frequency
stopband_low = 0  # Stopband low frequency
stopband_high = 1500  # Stopband high frequency
passband_low = 2500  # Passband low frequency
passband_high = 4000  # Passband high frequency
stopband_attenuation = 40  # Stopband attenuation in dB
passband_ripple = 0.1  # Passband ripple in dB
tap = 101  # Filter tap (filter length)

# Design the highpass FIR filter
b, a = firdesign(tap, Fs, Fc_highpass, win="hamming", fir_type='highpass')

# Compute the frequency response
w, H = coeff2freq_response(b, a)

# Plot the frequency response
plt.figure()
plt.plot(w, 20 * np.log10(np.abs(H)))
plt.title("Highpass FIR Filter Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.grid()
plt.show()
