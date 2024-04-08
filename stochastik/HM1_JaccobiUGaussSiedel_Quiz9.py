import numpy as np

def calculateJaccobi(A, b, x0, k):
    d = np.diag(A)
    D = np.diag(d)
    LplusR = A - D
    Dinv = np.linalg.inv(D)
    B = -Dinv @ LplusR
    c = Dinv @ b
    for j in range(k):
        x0 = B @ x0 + c

    return x0


def calculateGaussSiedel(A, b, x0, k):
    d = np.diag(A)
    D = np.diag(d)
    R = np.triu(A) - D
    LD = A - R
    LDinv = np.linalg.inv(LD)
    B = -LDinv @ R
    c = LDinv @ b

    for j in range(k):
        x0 = B @ x0 + c
    return x0

A = np.array([[2, 1], [4, 5]])
b= np.array([14, 13])
x0 = np.array([0, 0])

print(calculateJaccobi(A, b, x0, 2))
print(calculateGaussSiedel(A, b, x0, 2))