import matplotlib.pyplot as plt
import numpy as np
import strenge_s12_aufg1 as aufg1


def Aufg2b(f, a, b, n, y0, h):
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    # coefficient
    c = np.array([0, 0.25, 0.75, 0.5])
    a = np.array([
        [0, 0, 0],
        [0.5, 0.75, 0],
        [1, 0.5, 0],
        [0.5, 0.75, 1]])
    b = np.array([1 / 10, 4 / 10, 2 / 10, 3 / 10])

    for k in range(n):
        k1 = f(x[k] + c[0] * h, y[k])  # + h *a[0,0]
        k2 = f(x[k] + c[1] * h, y[k] + h * a[1, 0] * k1)
        k3 = f(x[k] + c[2] * h, y[k] + h * a[2, 0] * k1 + h * a[2, 1] * k2)
        k4 = f(x[k] + c[3] * h, y[k] + h * a[3, 0] * k1 + h * a[3, 1] * k2 + h * a[3, 2] * k3)
        y[k + 1] = y[k] + h * (b[0] * k1 + b[1] * k2 + b[2] * k3 + b[3] * k4)

    return x, y


yex = lambda t: t / 2 + 9 / (2 * t)
f = lambda t, y: 1 - y / t
y0 = 5
a = 1
b = 6
h = 0.01
n = int((b - a) / h)

t, yrk = aufg1.strenge_s12_aufg1(f, a, b, n, y0, 0.01)
t2, y2 = Aufg2b(f, a, b, n, y0, 0.01)

plt.plot(t, yrk, 'g', label='runge-kutta')
plt.plot(t2, y2, 'b:', label='rk-selber')
plt.plot(t, yex(t), 'r:', label='exakt')
plt.legend()
plt.show()