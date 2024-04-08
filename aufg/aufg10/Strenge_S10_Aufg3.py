import numpy as np


def Strenge_S10_Aufg3a(A, b, x0, tol, opt):
    d = np.diag(A)
    D = np.diag(d)
    LplusD = np.tril(A)
    L = LplusD - D
    RplusD = np.triu(A)
    R = RplusD - D
    if  opt == 'J':
        Dinv = np.linalg.inv(D)
        B = - Dinv @ (L + R)
        c = Dinv @ b
    if opt == 'Gs':
        LplusDinv = np.linalg.inv(LplusD)
        B = - LplusDinv @ R
        c = Dinv @ b

    Bnorm = np.linalg.norm(B, np.inf)

    if Bnorm >= 1:
        raise Exception("Konvergiert nicht")

    x1 = B@x0 + c
    n = 1

    n2 = np.log(tol* (1-Bnorm)/np.linalg.norm(x1-x0,np.inf))/np.log(Bnorm)

    while Bnorm/(1-Bnorm)*np.linalg.norm(x1 -x0, np.inf)>= tol:
        x0 = x1
        x1 = B@x0 +c
        n += 1
    return x1,  n ,n2


# xn, n, n2 = Strenge_S10_Aufg3a(A,b,x0,tol,opt)
