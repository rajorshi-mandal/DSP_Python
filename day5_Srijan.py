#linear convolution
import numpy as np
import matplotlib.pyplot as plt
Ix=0
Ih=0
x= np.random.rand(500)
h=np.ones(21)/(21)
Lx=x.size
Lh=h.size
print("x[n] sequence length : {}". format (Lx))
print("h[n] sequence length : {}". format (Lh))
Iy=Ix+Ih
Ly=Lx+Lh-1

y=np.zeros(Ly)


for i in range (Lx):
    for j in range (Lh):
        y[i+j]+=x[i]*h[j]

print("Input sequence : {}". format(x))
print("IR sequence : {}". format(h))
print("output sequence : {}". format(y))

nx= np.arange (Ix,Ix+Lx)
nh= np.arange (Ih,Ih+Lh)
ny= np.arange (Iy,Iy+Ly)



plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(nx,x)
plt.xlim([min(ny)-1,max(ny)+1])
plt.ylim([-5,5])
plt.grid()


plt.subplot(3,1,2)
plt.stem(nh,h)
plt.xlim([min(ny)-1,max(ny)+1])
plt.grid()

plt.subplot(3,1,3)
plt.plot(ny,y)
plt.xlim([min(ny)-1,max(ny)+1])
plt.ylim([-5,5])
plt.grid()

plt.tight_layout()
plt.show()


#linear convolution
import numpy as np
import matplotlib.pyplot as plt
Ix=0
Ih=0
x= np.random.rand(500)
h=np.ones(21)/(21)
Lx=x.size
Lh=h.size
print("x[n] sequence length : {}". format (Lx))
print("h[n] sequence length : {}". format (Lh))
Iy=Ix+Ih
Ly=Lx+Lh-1

y=np.zeros(Ly)


for i in range (Lx):
    for j in range (Lh):
        y[i+j]+=x[i]*h[j]

print("Input sequence : {}". format(x))
print("IR sequence : {}". format(h))
print("output sequence : {}". format(y))

nx= np.arange (Ix,Ix+Lx)
nh= np.arange (Ih,Ih+Lh)
ny= np.arange (Iy,Iy+Ly)



plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(nx,x)
plt.xlim([min(ny)-1,max(ny)+1])
plt.ylim([-5,5])
plt.grid()


plt.subplot(3,1,2)
plt.stem(nh,h)
plt.xlim([min(ny)-1,max(ny)+1])
plt.grid()

plt.subplot(3,1,3)
plt.plot(ny,y)
plt.xlim([min(ny)-1,max(ny)+1])
plt.ylim([-5,5])
plt.grid()

plt.tight_layout()
plt.show()



























