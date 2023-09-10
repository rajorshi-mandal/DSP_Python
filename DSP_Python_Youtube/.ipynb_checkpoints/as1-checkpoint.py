import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(10, 4))

# Parameters
sampling_rate = 8000  # Hz
duration = 0.002  # seconds
frequency = 1000  # Hz

# Generate time values
t = np.linspace(0, duration, sampling_rate, False)

# Generate the single tone signal
signal = np.sin(2 * np.pi * frequency * t)

# Plot the continuous sinusoidal signal in the first subplot
ax1.plot(t, signal)
ax1.set_title('Continuous 1000 Hz Sinusoid')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.grid()

# Generate the sampled sinusoidal output for the second subplot
num_samples = 100  # Number of samples
sample_indices = np.arange(0, len(signal), len(signal) // num_samples)
sampled_signal = signal[sample_indices]

# Generate corresponding time values for the samples
sampled_t = t[sample_indices]

# Plot the sampled sinusoidal output in the second subplot
ax2.stem(sampled_t, sampled_signal, basefmt=" ", use_line_collection=True)
ax2.set_title('Sampled 1000 Hz Sinusoid')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')
ax2.grid()

plt.tight_layout()
plt.show()
