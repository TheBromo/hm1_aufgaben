import numpy as np
import Strenge_S9_Aufg2 as s
import matplotlib.pyplot as plt

amount = 1000

dx_max = np.zeros(amount)
dx_obs = np.zeros(amount)

for i in range(amount):
    A = np.random.rand(100, 100)
    b = np.random.rand(100, 1)
    A_err = A + np.random.rand(100, 100) / 10e5
    b_err = b + np.random.rand(100, 1) / 10e5
    x, x_approx, dx_max[i], dx_obs[i] = s.Strenge_S9_Aufg2(A, A_err, b, b_err)

x = np.arange(0, amount)
plt.semilogy(range(0, amount), dx_max, label="dx_max", color="red",marker=".", linestyle="")
plt.semilogy(range(0, amount), dx_obs, color="blue", label="dx_obs",marker=".", linestyle="")
plt.semilogy(range(0, amount), dx_max / dx_obs, color="purple", label="dx_max/dx_obs",marker=".", linestyle="")
plt.legend(title='Graphen')
plt.grid()
plt.show()
