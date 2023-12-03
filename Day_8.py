
import numpy as np
import matplotlib.pyplot as plt
import dspmodule as dsp

M = 256
L = 21
N = M + L - 1

#Input
Fs = 8000
F = 200
Tw = M/Fs
t = np.linspace(0,Tw,num = M)
x= 1.0*np.random.rand(M)
x += 1*np.sin(2*np.pi*F*t)

#Impulse response
h_org = np.ones(L)/L

#output via Lin-Con
y_lc = dsp.linearconv(x,h_org,mode = 0, plotflag = False)

#Zero padding
x = np.append(x,np.zeros(N - M)).reshape(-1)
h = np.append(h_org,np.zeros(N - L ))

#Compute CC
y = dsp.circonv(x,h,plotflag = False)
print("[=] CC completed")

plt.figure(figsize = (20,6))
plt.subplot(2,2,1)
plt.plot(x)
plt.ylabel('Input')
plt.grid()

plt.subplot(2,2,3)
n = list(range(0,h_org.size))
plt.stem(h_org,use_line_collection = True)
plt.ylabel('Impulse-Response')
plt.xticks(ticks = n)
plt.grid()
plt.subplot(2,2,2)
plt.plot(y, lw = 2)
plt.ylabel('CC - Output')
plt.grid()
plt.subplot(2,2,4)
plt.plot(y_lc, lw = 2)
plt.ylabel('LC - Output')
plt.grid()
plt.show()
