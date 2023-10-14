import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.1, 1.3, 10e-7)

def h(x):
    return np.sqrt(100 * x ** 2 - 200 * x + 99)

y = h(x)

plt.figure(1)
plt.plot(x, y), plt.xlabel("x"), plt.ylabel("h(x)"), plt.grid()
plt.figure(2)
plt.semilogy(x, y), plt.xlabel("x"), plt.ylabel("h(x)"), plt.grid()

plt.show()


# Aufg c

