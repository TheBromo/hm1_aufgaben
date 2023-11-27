import sympy as sp

x = sp.symbols('x')
f_x = 1/10

# Berechne den Erwartungswert E(X)
E_X = sp.integrate(x * f_x, (x, 1, 11))

# Berechne den Erwartungswert E(X^2)
E_X2 = sp.integrate(x**2 * f_x, (x, 1, 11))

# Berechne die Varianz V(X) = E(X^2) - (E(X))^2
V_X = E_X2 - E_X**2

#E_X, E_X2, V_X

print(E_X)
print(E_X2)
print(V_X)