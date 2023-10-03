import numpy as np

import matplotlib.pyplot as plt

xmin = 1.99
xmax = 2.01

step = (xmax - xmin) / 501.0
x = np.arange(xmin, xmax, step)


f1 = np.zeros(501)
pols = [1, -14, 84, -280, 560, -672, 448, -128]
pols.reverse()
n = np.size(pols) - 1

for i in range(n + 1):
    f1 += pols[i] * x ** i

f2 = np.zeros(501)

for i in range(1):
    f2 += (x - 2) ** 7

plt.plot(x, f1, color="red", label="f1")
plt.plot(x, f2, color="blue", label="f2")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
