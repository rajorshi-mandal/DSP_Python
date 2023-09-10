from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Create figure with 2 subplots. 2 rows and 1 coloumn
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Sample rate of the periodic signal we will generate
Fs = 8000 

# Time duration of the signals
t = np.linspace(0, 10, Fs , False)  # 30 seconds

# Generate signal with 10 and 20 Hz frequency
sig1 = np.sin(2*np.pi*1000*t)
sig2 = np.sin(2*np.pi*7000*t)

# Plot the 1000Hz signal in first subplot using default color line
ax1.plot(t, sig1)
ax1.set_title('1000 Hz Sinusoid')
ax1.axis([0, 0.25, -1.5, 1.5])

# Plot the 7000Hz signal in second subplot using red color line
ax2.plot(t, sig2, 'r')
ax2.set_title('7000 Hz Sinusoid')
ax2.axis([0, 0.25, -1.5, 1.5])

plt.tight_layout()

plt.show()
