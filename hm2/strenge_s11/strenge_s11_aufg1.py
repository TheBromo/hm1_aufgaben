import numpy as np
import matplotlib.pyplot as plt

'''INPUT'''
f = lambda t, y: t ** 2 + 0.1 * y

'''INPUT'''


def strenge_10_aufg1(f, xmin, xmax, ymin, ymax, hx, hy):
    x = np.arange(xmin, xmax, hx)
    y = np.arange(ymin, ymax, hy)
    [x, y] = np.meshgrid(x, y)

    vx = np.ones_like(x)
    vy = f(x, y)
    # ev. normieren
    v = np.sqrt(vx ** 2 + vy ** 2)
    vx = vx / v
    vy = vy / v

    plt.quiver(x, y, vx, vy, color='b', width=0.003, angles='xy')
    plt.grid()
    plt.show()


strenge_10_aufg1(f, -2.1, 2.1, -1.1, 2.6, 0.3, 0.3)
