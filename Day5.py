#Day 5
import numpy as np
import matplotlib.pyplot as plt

Ix = 0#4
Ih = 0#-1


#Linear Convolution
#x = np.array([1,0,-1,3,-2,2])
#h = np.array([1,-1,1])

x = np.random.rand(500)
h = np.ones(21)/21

Lx = x.size     #length of input response
Lh = h.size     #length of impulse response

print("x[n] sequence length : {}".format(Lx))
print("x[n] sequence length : {}".format(Lh))

Iy = Ix + Ih    #starting index of output response
Ly = Lx + Lh - 1  #length of output response

y = np.zeros(Ly) #initialising y array with zeros

for i in range(Lx):         #looping for creating output response y
    for j in range(Lh):
        y[i + j] += x[i]*h[j]

print("input sequence : {}".format(x))
print("IR sequence : {}".format(h))
print("Output sequence : {}".format(y))

nx = np.arange(Ix,Ix + Lx)      #bringing all the responses to equal sampling distance
nh = np.arange(Ih,Ih + Lh)
ny = np.arange(Iy,Iy + Ly)

plt.figure(figsize = (12,8))

plt.subplot(3,1,1)
plt.plot(nx,x)
plt.xlim([min(ny) - 1, max(ny) + 1])        #setting the limit for x-axis
plt.ylim([-5,5])
plt.grid()

plt.subplot(3,1,2)
plt.stem(nh,h)
plt.xlim([min(ny) - 1, max(ny) + 1])
plt.grid()

plt.subplot(3,1,3)
#plt.stem(ny,y)
plt.plot(ny,y)
plt.xlim([min(ny) - 1, max(ny) + 1])
plt.ylim([-5,5])
plt.grid()

plt.tight_layout()
plt.show()
