import numpy as np


def strenge_s12_aufg1(f, a, b, n, y0, h):
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    # coefficient
    c = np.array([0, 0.5, 0.5, 1])
    a = np.array([
        [0, 0, 0],
        [0.5, 0, 0],
        [0, 0.5, 0],
        [0, 0, 1]])
    b = np.array([1 / 6, 1 / 3, 1 / 3, 1 / 6])

    for k in range(n):
        k1 = f(x[k] + c[0] * h, y[k])  # + h *a[0,0]
        k2 = f(x[k] + c[1] * h, y[k] + h * a[1, 0] * k1)
        k3 = f(x[k] + c[2] * h, y[k] + h * a[2, 0] * k1 + h * a[2, 1] * k2)
        k4 = f(x[k] + c[3] * h, y[k] + h * a[3, 0] * k1 + h * a[3, 1] * k2 + h * a[3, 2] * k3)
        y[k + 1] = y[k] + h * (b[0] * k1 + b[1] * k2 + b[2] * k3 + b[3] * k4)

    return x, y


f = lambda t, y: t ** 2 + 0.1 * y
print(strenge_s12_aufg1(f, -1.5, 1.5, 5, 0, (1.5 - -1.5) / 5))