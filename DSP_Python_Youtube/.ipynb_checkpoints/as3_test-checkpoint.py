import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 8000
duration = 0.002  # in seconds
t_continuous = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
t_discrete = np.arange(0, duration, 1.0 / sampling_rate)

# Frequencies
freq1 = 1000  # 1000 Hz
freq2 = 7000  # 7000 Hz

# Generate continuous and discrete signals
signal1_continuous = np.sin(2 * np.pi * freq1 * t_continuous)
signal2_continuous = np.sin(2 * np.pi * freq2 * t_continuous)
dual_tone_signal_continuous = signal1_continuous + signal2_continuous

signal1_discrete = np.sin(2 * np.pi * freq1 * t_discrete)
signal2_discrete = np.sin(2 * np.pi * freq2 * t_discrete)
dual_tone_signal_discrete = signal1_discrete + signal2_discrete

# Plot the signals side by side
plt.figure(figsize=(15, 6))

# Continuous signal plot
plt.subplot(1, 2, 1)
plt.plot(t_continuous, dual_tone_signal_continuous)
plt.title('Continuous Dual Tone Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

# Discrete signal plot
plt.subplot(1, 2, 2)
plt.stem(t_discrete, dual_tone_signal_discrete, use_line_collection=True)
plt.title('Discrete Dual Tone Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()