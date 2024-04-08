import numpy as np 
import matplotlib.pyplot as plt 

x_data = np.arange(0,110,10)
y_data = np.arange([999.9, 999.7,998.2,995.7,988.1 , 983.2,977.8,971.8,965.3,958.4])


n = np.size(x_data)

def f1(x):
    return x**2
def f2(x):
    return x
def f3(x):
    return 1

m =3

# Matrix A
A = np.zeros((n, m))
for i in range(0, n):
    A[i, 0:m ] = np.array([f1(x_data[i]),f2(x_data[i]),f3(x_data[i])])

# Berechnung der Parameter durch Loesung der Normalgleichung
# mit und ohne QR-ZerLegung von A

A_T = np.transpose(A)
lam = np.linalg.solve(A_T@A,A_T@y_data)
print('Parameter ohne QR: \n', lam)
# Parameter ohne QR:
# [-3.567599e7e-e3 -6.96946387e-e2 1. eee544e6e+e31

Q, R = np.lina1g.qr(A)
Q_T = np.transpose(Q)
lam_qr = np.linalg. solve(R, Q_T@y_data)
print('Parameter mit ',lam_qr)

# Parameter mit QR:
# 193.5675990Ye-e3 -6.96946387+02 _ 1. ee954Ø6e+ø31
print( 'Differenzen der Parameterwerte ohne QR und mit', lam- lam_qr)
# Differenzen der Parameterwerte ohne QR und mit QR:
# [6.54858112e-17 1.013e7851e-14 3.41e6e513e-131

x_plot = np.arange(0, 101, 1)
y_plot = np.polyval(lam, x_plot)
y_plot_qr = np.polyval(lam_qr, x_plot)
plt.plot(x_data, y_data, marker='o', color='black', linestyle='',label= 'Daten' )
plt.plot(x_plot, y_plot, color=' red' ,linestyle='--',label='Norma1eng1eichung ohne QR')

plt.plot(x_plot, y_plot_qr, color='blue', linestyle='-.',label='Norma1eng1eichung mit QR')
plt.xlabel( 'Temperatur'); plt.ylabe1('Dichte'); plt.grid()
plt.legend()

print( 'Konditionszahl von AAT*A bez. 2-Norm: \n', np.linalg.cond(A_T@A,2))
print( 'Konditionszahl von R bez. 2-Norm: \n', np.linalg.cond(R, 2))

lam_poly = np.polyfit(x_data ,y_data, 2)
print( 'Differenzen der Parameterwerte ohne QR und' ,lam - lam_poly)
# Differenzen der Parameterwerte ohne QR und polyfit:
# 1-2.6454533ee-17 1.42941214e-14 -1.13686838e-121
print( 'Differenzen der Parameterwerte mit QR und' ,
lam_qr -lam_poly)

E =  np.linalg.norm(y_data - A@lam, 2)**2
E_qr =np.linalg.norm(y_data - A@lam_qr, 2)**2
E_poly =np.linalg.norm(y_data - A@lam_poly, 2)**2
