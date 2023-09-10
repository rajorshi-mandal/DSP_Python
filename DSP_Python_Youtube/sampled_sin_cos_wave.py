import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,1,0.008)
xn = np.sin(2*np.pi*1000*n)

#To plot the signal
plt.stem(n,xn)
plt.title('sampled sin wave')
plt.xlabel('------------>')
plt.ylabel('Amplitude')
plt.show()
