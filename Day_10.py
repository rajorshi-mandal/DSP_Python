
#Day10

import numpy as np
import matplotlib.pyplot as plt
import dspmodule as dsp

epsilon = 1e-9
Fs = 8000
Fp = 1500
Fst = 3000
wp = 2*np.pi*Fp
wst = 2*np.pi*Fst
print('Passband and stopband edge frequency are {} Hs aand {} Hz'.format(Fp, Fst))
#Max attn (dB) is passband
Ap = 3

#Min attn (dB) is stopband
As = 10.0
N, wc = dsp.butterorder(wp, wst, Ap, As, Fs)
print("Order of filter : {}".format(N))
print("cutoff frequency : {:0.2f} Hz".format(wc/(2*np.pi)))
b, a = dsp.iirbutterdesign(N, wc, Fs ,iir_type = 'lowpass')
w, H = dsp.coeff2freq_response(b, a)
plt.figure(figsize = (6,4))

plt.subplot(2,1,1)
plt.plot(w* Fs/(2*np.pi), 20*np.log10(np.abs(H) + epsilon))
#plt.ylim([-20,1])
#plt.xlim([0,2000])
#plt.semilogx(w * Fs / (2*np.pi), 20*np.log10(np.abs(H) + epsilon))
plt.grid()
plt.ylabel('|H| in dB')
plt.xlabel('F Hz')
plt.subplot(2, 1, 2)
plt.plot(w * Fs/(2 * np.pi), np.unwrap(np.angle(H)))
# plt.semilogx(w * Fs / (2*np.pi),np.unwrap(np.angle(H)))
plt.grid()
plt.ylabel('<H in rad')
plt.xlabel('F Hz')
plt.tight_layout()
plt.show()
