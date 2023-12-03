#Day 4

import numpy as np
import matplotlib.pyplot as plt

Fs = 16000
Td = 4e-3

A1 = 1.5
F1 = 650

A2 = 2.5
F2 = 820

t = np.arange(0, Td, 1/Fs)

sig1 = A1 * np.sin(2 * np.pi * F1 * t)
sig2 = A2 * np.sin(2 * np.pi * F2 * t)

try:
    with np.errstate(divide='raise', invalid='raise'):
        sig = sig1 / sig2
except (RuntimeWarning, Exception) as e:
    print(f"Error: {type(e).__name__} - {e}")
    sig = np.zeros_like(t)


plt.stem(t,sig1, markerfmt = 'C2o')
plt.stem(t,sig2, markerfmt = 'C4^')
plt.stem(t,sig, markerfmt = 'C6s')

plt.plot(t,sig1,label = str(F1) + "Hz")
plt.plot(t,sig2,label = str(F2) + "Hz")
plt.plot(t,sig,'b', linewidth = 3, label = "sig1 + sig2")


plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Division : F1 = {}, F2 = {}".format(F1, F2))

plt.legend()
plt.show()
