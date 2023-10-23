import numpy as np
import matplotlib.pyplot as plt


def archimedes(x):
    return np.sqrt(2 - 2 * np.sqrt(1 - x ** 2 / 4))


def archimedes2(x):
    return np.sqrt(x ** 2 / (2 * (1 + np.sqrt(1 - (x ** 2 / 4)))))


iterations = 50
corner = 6
length = 1
res = np.zeros(iterations + 1)
res[0] = 6

for i in range(1, iterations + 1):
    corner = corner * 2
    length = archimedes(length)
    res[i] = length * corner

x = np.arange(0, iterations + 1)
plt.figure(1)
plt.plot(x, res, color="red")

corner = 6
length = 1
res2 = np.zeros(iterations + 1)
res2[0] = 6

for i in range(1, iterations + 1):
    corner = corner * 2
    length = archimedes2(length)
    res2[i] = length * corner

plt.figure(2)
plt.plot(x, res2, color="blue")
plt.show()
