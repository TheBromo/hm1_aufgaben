import matplotlib.pyplot as plt
import numpy as np
import decimal


def f(number):
    return number ** 3 + 2 * number ** 2 - 3 * number - 4


def f1(number):
    return 3 * number ** 2 + 4 * number - 3


def base_function(number):
    return (number ** 4) / 4 + (2 * number ** 3) / 3 - (3 * number ** 2) / 2 - (4 * number)


x = []
y = []

x1 = []
y1 = []

x2 = []
y2 = []

values = np.arange(-4, 4, 0.001)
for val in values:
    x.append(val)
    y.append(f(val))
    x1.append(val)
    y1.append(f1(val))
    x2.append(val)
    y2.append(base_function(val))

plt.plot(x, y, label="f(x)")
plt.plot(x1, y1, label="f'(x)")
plt.plot(x2, y2, label="F(x)")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(-5, 5)
plt.show()
