import matplotlib.pyplot as plt
import numpy as np

'''INPUT'''
# Zu lösende Differentialgleichung
f = lambda x, y: x ** 2 / y
a = 0  # Untere Grenze
b = 1.4  # Obere Grenze
y0 = 2  # Anfangswert
h = 0.7  # Schrittweite
n = 10  # Anzahl Schritte
'''INPUT'''


def richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy):
    x = np.arange(xmin, xmax + hx, hx)
    y = np.arange(ymin, ymax + hy, hy)
    x, y = np.meshgrid(x, y)

    vx = np.ones_like(x)
    vy = f(x, y)
    v = np.sqrt(vx ** 2 + vy ** 2)
    vx = vx / v
    vy = vy / v
    plt.grid()
    plt.quiver(x, y, vx, vy, width=0.003, angles='xy')


def euler(f, a, b, n, y0):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for k in range(n):
        k1 = f(x[k], y[k])
        y[k + 1] = y[k] + h * k1

    return x, y


def mittelpunkt(f, a, b, n, y0):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for k in range(n):
        k1 = f(x[k], y[k])
        k2 = f(x[k] + h * 0.5, y[k] + 0.5 * h * k1)
        y[k + 1] = y[k] + h * k2
        print(f"k1: {k1}")
        print(f"k2: {k2}")
        print(f"x[{k + 1}]: {x[k + 1]}")
        print(f"z[:, {k + 1}]: {y[:, k + 1]}")

    return x, y


def mod_euler(f, a, b, n, y0):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for k in range(n):
        k1 = f(x[k], y[k])
        k2 = f(x[k] + h, y[k] + h * k1)
        y[k + 1] = y[k] + h * (k1 + k2) * 0.5

    return x, y


def strenge_s11_aufg3(f, a, b, n, y0):
    x, y_euler = euler(f, a, b, n, y0)
    x, y_modeuler = mod_euler(f, a, b, n, y0)
    x, y_mittelpunkt = mittelpunkt(f, a, b, n, y0)

    # Graphen zeichnen
    plt.plot(x, y_euler, label='Euler')
    plt.plot(x, y_modeuler, label='Modifiziertes Euler')
    plt.plot(x, y_mittelpunkt, label='Mittelpunkt')
    plt.legend()

    # Richtungsfeld zeichnen
    hx = (b - a) / n
    hy = hx
    richtungsfeld(f, a, b, 1.5, 2.5, hx, hy)

    plt.show()
    return x, y_euler, y_modeuler, y_mittelpunkt


strenge_s11_aufg3(f, a, b, n, y0)