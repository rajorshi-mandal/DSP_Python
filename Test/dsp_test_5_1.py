import numpy as np
import matplotlib.pyplot as plt

xn = np.array([1, -1, 2, -1, 3])
ix = -1
lx = xn.size

hn = np.array([1, -1, 1])
ih = -1
lh = hn.size

iy = ix + ih
ly = lx + lh - 1

yn = np.zeros(ly)

for i in range(lx):
    for j in range(lh):
        yn[i + j] = xn[i] * hn[j]

print("Input : ", xn)
print("Impulse : ", hn)
print("Output : ", yn)

nx = np.arange(ix, ix + lx)
nh = np.arange(ih, ih + lh)
ny = np.arange(iy, iy + ly)

#plt.figure(figsize=(12,8))

plt.subplot(3, 1, 1)
plt.stem(nx, xn, label = "Input")
plt.xlim(min(ny) - 1, max(ny) + 1)
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(nh, hn, label = "Impulse")
plt.xlim(min(ny) - 1, max(ny) + 1)
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(ny, yn, label = "Output")
plt.xlim(min(ny) - 1, max(ny) + 1)
plt.grid()

plt.legend()
plt.show()
