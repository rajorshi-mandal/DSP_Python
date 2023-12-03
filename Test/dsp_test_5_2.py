import numpy as np
import matplotlib.pyplot as plt

ix = 0
ih = 0

xn = np.random.rand(500)
hn = np.ones(21)/21

lx = xn.size
lh = hn.size

print("x[n] sequence length : {}".format(lx))
print("h[n] sequence length : {}".format(lh))

iy = ix + ih
ly = lx + lh - 1

y = np.zeros(ly)

for i in range(lx):
    for j in range(lh):
        y[i + j] += xn[i] * hn[j]

print("Input : {}".format(xn))
print("Impulse : {}".format(hn))
print("Output : {}".format(y))

nx = np.arange(ix, ix + lx)
nh = np.arange(ih, ih + lh)
ny = np.arange(iy, iy + ly)

plt.figure(figsize = (12,8))

plt.subplot(3,1,1)
plt.plot(nx,xn)
plt.xlim([min(ny) - 1, max(ny) + 1])
plt.ylim([-5,5])
plt.grid()

plt.subplot(3,1,2)
plt.stem(nh,hn)
plt.xlim([min(ny) - 1, max(ny) + 1])
#plt.ylim([-5,5])
plt.grid()

plt.subplot(3,1,3)
plt.plot(ny,y)
plt.xlim([min(ny) - 1, max(ny) + 1])
plt.ylim([-5,5])
plt.grid()

plt.tight_layout()
plt.show()
