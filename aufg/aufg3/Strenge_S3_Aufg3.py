# 1 + x, sqrt(x), x/10^9
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1e-3, 100, 1e-3)

def f(x):
    return 5*2**(-1/3)*x**(-2/3)

def g(x):
    return 1e5*(2*np.exp(1)**(-x/100))

def h(x):
    return (1e4/2**10)**x

res_f = f(x)
res_g = g(x)
res_h = h(x)

plt.figure(1)
plt.loglog(x, res_f),plt.xlabel("x"), plt.ylabel("f(x)"),plt.grid() 
plt.figure(2)
plt.semilogy(x, res_g),plt.xlabel("x"), plt.ylabel("g(x)"),plt.grid() 
plt.figure(3)
plt.semilogy(x, res_h),plt.xlabel("x"), plt.ylabel("h(x)"),plt.grid()

plt.show()