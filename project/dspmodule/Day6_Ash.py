# Day6
# Z - Transform and DFT

# Import necessary modules
import dsp_module_ayeshee as dsp
import numpy as np
import matplotlib.pyplot as plt

# Define the numerator and denominator coefficients for the transfer function
b = np.array([1])  # Numerator coefficients
a = np.array([1, -0.6, 0.8])  # Denominator coefficients

# Calculate poles, zeros, and gain of the transfer function
z, p, k = dsp.tf2polezero(b, a)

print(" Zeros are at {}".format(z))
print(" Poles are at {}".format(p))
print(" Gain is : {}".format(k))

# Calculate frequency response
w, H = dsp.polezero2freq_response(z, p, k)

# Define signal parameters
Fs = 16000
w1 = 1.25
w2 = 2.5
F1 = Fs * (w1 / (2 * np.pi))
F2 = Fs * (w2 / (2 * np.pi))

# Define time parameters for the signal
Td = 5e-3
t = np.arange(0, Td, 1 / Fs)

# Generate the signal with two sinusoids
x = 1 * np.sin(2 * np.pi * F1 * t) + 1 * np.sin(2 * np.pi * F2 * t)  # Creating the signal
# We are removing parts of signal with low gain; in this case, it is w2 where gain is low or attenuation

# Apply the filter to the signal
y = dsp.linearfilter(b, a, x)

# Plotting the frequency response, original signal, and filtered signal
plt.figure(figsize=(20, 4))
plt.subplot(2, 2, 1)
plt.plot(w, np.abs(H))  # Taking absolute value since complex values for frequency response
plt.xlabel("w (rad/sample) ---->")
plt.ylabel("|H(w)| ---->")
plt.title("Amplitude Plot")
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(w, np.unwrap(np.angle(H)))  # Fixing sudden phase changes like 360 + 15, similar to 360
plt.xlabel("w (rad/sample) ---->")
plt.ylabel("<H(w) ---->")
plt.title("Phase Plot")
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(t, x)  # Plotting the original signal

plt.subplot(2, 2, 4)
plt.plot(t, y)  # Plotting the filtered signal

# Adjusting the layout for better visualization
plt.tight_layout()
plt.show()
