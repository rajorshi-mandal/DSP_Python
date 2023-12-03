import numpy as np
import matplotlib.pyplot as plt

#Parameters:
Fs = 8000
Td = 0.002

# A1 = 1.5
F1 = 1000

F2 = 7000

#Define the time vector
t = np.arange(0,Td,1/Fs)

#Define the signals :
sig1 = np.sin(2*np.pi*F1*t)
sig2 = np.sin(2*np.pi*F2*t)
sig3 = sig1+sig2

#Plotting Section :
# plt.stem(t,sig1,markerfmt='C2o')
# plt.stem(t,sig2,markerfmt='C4^')
plt.stem(t,sig3,markerfmt='C0s')

#Continuous plot :
# plt.plot(t,sig1,label = str(F1) + "Hz")
# plt.plot(t,sig2,label = str(F2) + "Hz")
plt.plot(t,sig3,'b',linewidth = 3,label = "sig1 + sig2")

plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal Plot F1 = {}, F2 = {}".format(F1,F2))

plt.legend()
plt.show()
