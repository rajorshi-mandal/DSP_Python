#import numpy and matplotlib library

import numpy as np
import matplotlib.pyplot as plt

#To define independent and dependent variable
t = np.arange(0,4,0.001)
xt = np.sin(2*np.pi*1*t)

#To plot the graph
plt.plot(t,xt)
plt.title('sin wave')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
