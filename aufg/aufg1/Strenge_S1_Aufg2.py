def strenge_s1_aufg2(a, xmin, xmax):
    import numpy as np

    # a = [a0, a1,...,an]
    # Koeffizientenvektoren
    # xmin,xmax Grenzenberreich

    step = (xmax - xmin) / 1000
    x = np.arange(xmin, xmax, step)
    n = np.size(a) - 1

    p = np.zeros(1000)
    for i in range(n + 1):
        p += a[i] * x ** i

    dp = np.zeros(1000)
    for i in range(n + 1):
        dp += a[i] * i * x ** (i - 1)

    pint = np.zeros(1000)
    for i in range(n + 1):
        pint += a[i] * i * x ** (i + 1) / (i + 1)

    # n grad polynom
    # np.zeros(1000)

    # x = [x0=xmin,x1,...,xm=xmax
    # Vektor x-Werte
    # p = [p(x0),p(x1),...,p(xm)]
    # funktionswerte
    # dp = [p'(x0),p'(x1),...,p'(xm)]
    # ableitungswerte
    # pint = [P(x0),P(x1),...,P(xm)]
    # Stammfunktionen

    return x, p, dp, pint
