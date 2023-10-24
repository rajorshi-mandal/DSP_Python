#Day9

import numpy as np
import matplotlib.pyplot as plt
import dspmodule as dsp

tap = 25
Fc = 2000
Fs = 8000
window_func = "boxcar"
b, a = dsp.firdesign(tap,Fs,Fc, win = window_func, fir_type = 'lowpass')
w,H = dsp.coeff2freq_response(b,a)
F = w * Fs/(2*np.pi)
plt.figure(figsize = (8,6))
plt.subplot(3,1,1)
plt.stem(b)
plt.ylabel('LPF IR')
plt.xlabel('Samples')
plt.subplot(3,1,2)
plt.plot(F,20*np.log10(np.abs(H)))
plt.grid()
plt.ylabel('|H(w)| in dB')

#plt.label('w rad/samples')
plt.subplot(3,1,3)
plt.plot(F,np.unwrap(np.angle(H)))
plt.grid()
plt.ylabel('<H(w) in rad')
#plt.xlabel('w rad/samples')
plt.xlabel('F in Hz')
plt.tight_layout()
plt.show()
