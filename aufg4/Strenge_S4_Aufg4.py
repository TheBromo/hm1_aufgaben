import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return (230 * x ** 4 + 18 * x ** 3 + 9 * x ** 2 - 9) / 221


def FAbleitung(x):
    return (920 * x ** 3 + 54 * x ** 2 + 18 * x) / 221


def iterate(a):
    for i in range(5):
        temp = F(a)
        print("{}. > F({}) = {}".format(i, a, temp))
        a = temp


# konvergiert
iterate(0)
# divergiert
iterate(1)

x = np.arange(-.5, .5, .01)

y = F(x)
plt.figure(1)
plt.plot(x, y), plt.xlabel("x"), plt.ylabel("F(x)"), plt.grid()

print("max Steigung: {}".format(FAbleitung(.5)))


# 3.a nicht gelöst von Lösungen genommen

# 3.b

x = np.arange(0, np.pi, .01)


def f1(x):
    return np.sin(x)


def f2(x):
    return x - 0.5 * np.pi


y1 = f1(x)
y2 = f2(x)

plt.figure(2)
plt.plot(x, y1),
plt.plot(x, y2),
plt.grid()
plt.show()


def G(x):
    return 1.0 / 2.0 * np.pi + np.sin(x)


a = 2.3

for i in range(15):
    temp = G(a)
    print("{}. > F({}) = {}".format(i, a, temp))
    a = temp
