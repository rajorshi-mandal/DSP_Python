import numpy as np
import matplotlib.pyplot as plt
import dspmodule as dsp

window_flag = 0
N = 160
n = np.arange(0,N)

x = np.sin(np.pi * n/40) + 0.6 * np.cos(3 * np.pi * n/40) + 0.4 * np.sin(9 * np.pi * n/40)

N_dft = N

X = dsp.dft(x, N = N_dft, win = window_flag)
print("[=] {} point DFT successfully computed.".format(X.size))

x_hat = dsp.idft(X)
print("[=] {} point IDFT successfully computed.".format(x.size))

plt.figure(figsize = (20,4))
plt.subplot(1, 3, 1)
plt.plot(x, lw = 2, color = [0.8, 0.4, 0])
plt.title('Signal', fontsize = 14)
plt.xlabel('Samples', fontsize = 14)

plt.subplot(1, 3, 2)
plt.plot(np.abs(X), lw = 1, color = [0.8, 0, 0.5])
plt.title('Amplitude Spectrum', fontsize = 14)
plt.xlabel('Frequency bin', fontsize = 14)

plt.subplot(1, 3, 3)
plt.plot(x_hat.real, lw = 2, color = (0, 0.6, 0.7))
plt.title('IDFT Signal', fontsize = 14)
plt.xlabel('Samples', fontsize = 14)
plt.show()

