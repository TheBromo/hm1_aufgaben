
"""
Created on Fri Mar 26 12:03:41 2021

Höhere Mathematik 2, Serie 6, Aufgabe 3, Daten

@author: knaa
"""

import numpy as np
import matplotlib.pyplot as plt 

data=np.array([
    [1971, 2250.],
    [1972, 2500.],
    [1974, 5000.],
    [1978, 29000.],
    [1982, 120000.],
    [1985, 275000.],
    [1989, 1180000.],
    [1989, 1180000.],
    [1993, 3100000.],
    [1997, 7500000.],
    [1999, 24000000.],
    [2000, 42000000.],
    [2002, 220000000.],
    [2003, 410000000.],   
    ])

n= data.shape[0]
t_data = data[0:n,0]
n_data = data[0:n,1]
x_data = t_data-1970
y_data = np.log10(n_data)

def f1(x):
    return 1.

def f2(x):
    return x
m=2

A = np.zeros((n, m))
for i in range(0, n):
    A[i, 0:m ] = np.array([f1(x_data[i]),f2(x_data[i])])

Q, R = np.linalg.qr(A)
Q_T = np.transpose(Q)
lam = np.linalg.solve(R,Q_T@y_data)


def f(x, lam):
    return lam[0]*f1(x)+ lam[1]*f2(x)

x_plot = np.arange(0,32,0.1)
y_plot = f(x_plot, lam)
plt.figure(1)

plt.plot(x_plot, y_plot, marker='o', color='black', linestyle='')
plt.plot(x_plot, y_plot, color='red')
plt.grid()
plt.xlabel("jahre ab 1970")
plt.ylabel( 'Zehnerlogarithmus der Anzahl Chips pro Transistor')

x_extra= 2015 -1970
y_extra= f(x_extra, lam)
N_extra = 10**y_extra
print(N_extra)

