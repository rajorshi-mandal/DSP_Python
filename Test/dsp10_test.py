import numpy as np
import matplotlib.pyplot as plt
import dspmodule as dsp

epsilon = 1e-9
Fs = 8000
Fp = 1500
Fst = 3000
Ap = 3
As = 10
wp = 2 * np.pi * Fp
ws = 2 * np.pi * Fst
N, wc = dsp.butterorder(wp, ws, Ap, As, Fs)

print("Order {} ".format(N))
print("cutoff freequency : {:0.2f}".format(wc / (2* np.pi)))


b, a = dsp.iirbutterdesign(N, wc, Fs, iir_type = 'lowpass')
w, H = dsp.coeff2freq_response(b, a)

plt.figure(figsize= (6, 4))

plt.subplot(2,1,1)
plt.plot(w * Fs /(2 *np.pi), 20 * np.log10(np.abs(H) + epsilon))
plt.ylabel("|H| in dB")
plt.xlabel("F Hz")
plt.grid()

plt.subplot(2,1,2)
plt.plot(w * Fs/(2*np.pi), np.unwrap(np.angle(H)))
plt.ylabel("<|H| in rad")
plt.xlabel("F Hz")

plt.tight_layout()
plt.show()
