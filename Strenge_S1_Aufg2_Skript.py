from Strenge_S1_Aufg2 import strenge_s1_aufg2
import matplotlib.pyplot as plt

pol = [-4., -3., 2., 1.]

x, p, dp, pint = strenge_s1_aufg2(pol, -4., 4.)

plt.plot(x, p)
plt.plot(x, dp)
plt.plot(x, pint)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-5., 5.)
plt.show()
