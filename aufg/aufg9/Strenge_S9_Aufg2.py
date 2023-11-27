import numpy as np

"""
Matrix A und Vektor b des linearen Gleichungssystems Ax = b, sowie die gestörte Matrix Ae und
Vektor eb des gestörten Gleichungssystems A˜xe = eb.
"""


def Strenge_S9_Aufg2(A, A_approx, b, b_approx):
    x = np.linalg.solve(A, b)
    x_approx = np.linalg.solve(A_approx, b_approx)

    conda = np.linalg.cond(A, np.inf)
    erra = err(A, A_approx)
    errb = err(b, b_approx)
    dx_obs = err(x, x_approx)

    if conda * erra < 1:
        dx_max = (conda / (1 - conda * erra)) * (erra + errb)
    else:
        dx_max = np.NAN

    return x, x_approx, dx_max, dx_obs


def err(val, val_err):
    return np.linalg.norm(val - val_err, np.inf) / np.linalg.norm(val, np.inf)


A = np.array([[20, 30, 10], [10, 17, 6], [2, 3, 2]])
b = np.array([5720, 3300, 836])
x = np.array([22, 88, 264])

A_approx = np.array([[20 - 0.1, 30 - 0.1, 10 - 0.1], [10 - 0.1, 17 - 0.1, 6 - 0.1], [2 - 0.1, 3 - 0.1, 2 - 0.1]])
b_approx = np.array([5720 + 100, 3300 + 100, 836 + 100])
x_approx = np.array([7.38, 58.77, 395.77])

print(Strenge_S9_Aufg2(A, A_approx, b, b_approx))
