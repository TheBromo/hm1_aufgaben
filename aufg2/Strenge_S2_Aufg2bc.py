import numpy as np
import matplotlib.pyplot as plt


## Aufgabe 2b
def g1(x):
    return x / (np.sin(1 + x) - np.sin(1))


x = np.linspace(-1e-14, 1e-14, 2001)
y1 = g1(x)

plt.figure(1)
plt.plot(x, y1, color="red")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend("g1(x)")


## Aufgabe 2c

def g2(x):
    return x / (2 * np.cos(1 + x / 2) * np.sin(x / 2))


y2 = g2(x)

plt.figure(2)
plt.plot(x, y2, color="blue")
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend("g2(x)")

plt.show()
