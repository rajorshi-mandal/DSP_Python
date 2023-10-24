# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import dspmodule as dsp

# Define filter parameters
tap = 25        # Number of taps
Fc = 1600       # Cutoff frequency in Hz
Fs = 8000       # Sampling rate in Hz
window_func = "boxcar"  # Window function for filter design

# Design the high-pass FIR filter
b, a = dsp.firdesign(tap, Fs, Fc, win=window_func, fir_type='highpass')

# Compute the frequency response
w, H = dsp.coeff2freq_response(b, a)

# Convert angular frequency to Hz
F = w * Fs / (2 * np.pi)

# Plot the impulse response
plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1)
plt.stem(b)
plt.ylabel('HPF IR')
plt.xlabel('Samples')

# Plot the magnitude response in dB
plt.subplot(3, 1, 2)
plt.plot(F, 20 * np.log10(np.abs(H)))
plt.grid()
plt.ylabel('|H(w)| in dB')
plt.xlabel('F in Hz')

# Plot the phase response in radians
plt.subplot(3, 1, 3)
plt.plot(F, np.unwrap(np.angle(H)))
plt.grid()
plt.ylabel('<H(w) in rad')
plt.xlabel('F in Hz')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
