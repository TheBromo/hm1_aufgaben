import numpy as np

def fixpunkt_iteration(B, c, x_0, max_iterations):
    x_k = x_0
    for _ in range(max_iterations):
        x_k = np.dot(B, x_k) + c
    return x_k


# Gegebene Werte
B = np.array([[0.4, 0.1], [0.2, 0.3]])
c = np.array([[0.5], [0.5]])
x_0 = np.array([[0], [1]])

# Berechnung der ersten Iterierten
x_1 = np.dot(B, x_0) + c
x_2 = np.dot(B, x_1) + c
x_3 = np.dot(B, x_2) + c
x_4 = np.dot(B, x_3) + c
# Berechnung der Norm von B und der Differenz x^(1) - x^(0) bezüglich der 1-Norm
B_norm_1 = np.linalg.norm(B, 1)
x_1_minus_x_0_norm_1 = np.linalg.norm(x_1 - x_0, 1)

# Berechnung der a-priori Abschätzung für n = 3
n = 4
apriori_abschaetzung = (B_norm_1**n / (1 - B_norm_1)) * x_1_minus_x_0_norm_1

print(x_1, B_norm_1, x_1_minus_x_0_norm_1, apriori_abschaetzung)