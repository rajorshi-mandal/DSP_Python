#Day6
#Z - Transform and DFT

import dspmodule as dsp
import numpy as np
import matplotlib.pyplot as plt

b = np.array([1])
a = np.array([1,-0.6,0.8])

z,p,k = dsp.tf2polezero(b,a)

print(" Zeros are at {}".format(z))
print(" Poles are at {}".format(p))
print(" Gain is : {}".format(k))

w,H = dsp.polezero2freq_response(z, p, k)

Fs = 16000
w1 = 1.25
w2 = 2.5
F1 = Fs*(w1/(2*np.pi))
F2 = Fs*(w2/(2*np.pi))

Td = 5e-3
t = np.arange(0,Td,1/Fs) 
x = 1*np.sin(2*np.pi*F1*t) + 1*np.sin(2*np.pi*F2*t)  #creating the signal
#we are removing parts of signal with low gain in here it is w2 where gain is low or attenuation


y = dsp.linearfilter(b,a,x)

plt.figure(figsize = (20,4))
plt.subplot(2,2,1)
plt.plot(w,np.abs(H)) #taking absolute value since complex values for freq response
plt.xlabel("w (rad/sample) ---->")
plt.ylabel("|H(w)| ---->")
plt.title("Amplitude Plot")
plt.grid()

plt.subplot(2,2,3)
plt.plot(w,np.unwrap(np.angle(H)))  #for fixing sudden changes like 360 + 15 similar to 360
plt.xlabel("w (rad/sample) ---->")
plt.ylabel("<H(w) ---->")
plt.title("Phase Plot")
plt.grid()

plt.subplot(2,2,2)
plt.plot(t,x)

plt.subplot(2,2,4)
plt.plot(t,y)

#plt.subplots_adjust(left=0.1, bottom=0.09, right = 0.9, top=0.9, wspace=0.4,hspace=0.4)

plt.tight_layout()
plt.show()
