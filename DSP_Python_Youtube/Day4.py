#For smapling of Continuous Time Signal
import numpy as np
import matplotlib.pyplot as plt

#parameters :
Fs = 16000
Td = 4e-3

A1 = 1.5
F1 = 650

#Define the time vector
t = np.arange(0,Td,1/Fs)

#Develop the signals :
sig1 = A1 * np.sin(2 * np.pi * F1 * t)

#Plotting Section:

#discrete plot:
plt.stem(t,sig1,markerfmt='C2o')


#continuous plot:
plt.plot(t,sig1,label = str(F1) + "Hz")


plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal Plot  F1 = {}".format(F1))


plt.legend()
plt.show()
