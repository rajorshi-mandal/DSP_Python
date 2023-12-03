import numpy as np
import matplotlib.pyplot as plt
import dspmodule as dsp
#Z-transform

b = np.array([1])
a = np.array([1, -0.6, 0.8])

z, p, k = dsp.tf2polezero(b, a)

print("zeros : {}".format(z))
print("poles : {}".format(z))
print("gain : {}".format(z))

w, H = dsp.polezero2freq_response(z, p, k)

Fs = 16000
w1 = 1.25
w2 = 2.5
F1 = Fs * (w1/ (2*np.pi))
F2 = Fs * (w1/ (2*np.pi))

Td = 5e-3
t = np.arange(0, Td, 1/Fs)

x = 1 * np.sin(2 * np.pi * F1 * t) + 1 * np.sin(2 * np.pi * F1 * t)

y = dsp.linearfilter(b,a, x)

plt.figure(figsize = (12,8))

plt.subplot(2,2,1)
plt.plot(w, np.abs(H))
plt.xlabel("W (rad/sample) ---->")
plt.ylabel("|H(W)|")
plt.title("Amplitude Plot")
plt.grid()

plt.subplot(2,2,2)
plt.plot(w, np.unwrap(np.angle(H)))
plt.xlabel("W ()rad/sample")
plt.ylabel("<|H(W)|")
plt.title("Phase Plot")
plt.grid()

plt.subplot(2,2,3)
plt.plot(t,x)

plt.subplot(2,2,4)
plt.plot(t,y)

plt.tight_layout()
plt.show()
