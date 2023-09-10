import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Parameters
frequency = 1000  # Frequency of the tone in Hz
duration = 1.0   # Duration of the tone in seconds
sampling_rate = 8000  # Sampling rate in Hz

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration), False)

# Generate the tone signal
tone_signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# Plot the signal
plt.plot(t, tone_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Synthesized Tone Signal')
plt.grid(True)
plt.show()

# Playback the signal
sd.play(tone_signal, sampling_rate)
sd.wait()

