# main.py

import numpy as np
import matplotlib.pyplot as plt
from dspmodule.dspmodule import calculate_zeros_poles_gain, calculate_frequency_response, linearfilter

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

# Example usage for zeros, poles, and gain
numerator_coeffs = ([1])  # Numerator coefficients of the transfer function
denominator_coeffs = [1, -0.6, 0.8]  # Denominator coefficients of the transfer function

# Calculate zeros, poles, and gain
zeros, poles, gain = calculate_zeros_poles_gain(numerator_coeffs, denominator_coeffs)

#print poles at,zeros at and the gain

print(" Zeros are at {}".format(zeros))
print(" Poles are at {}".format(poles))
print(" Gain is : {}".format(gain))

# Calculate frequency response
w, H = calculate_frequency_response(zeros, poles, gain)

# Apply the filter to the signal
y = linearfilter(numerator_coeffs, denominator_coeffs, x)

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
plt.xlabel("Time (s) ---->")
plt.ylabel("Amplitude")
plt.title("Original Signal")
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(t, y)  # Plotting the filtered signal
plt.xlabel("Time (s) ---->")
plt.ylabel("Amplitude")
plt.title("Filtered Signal")
plt.grid()

# Adjusting the layout for better visualization
plt.tight_layout()
plt.show()
