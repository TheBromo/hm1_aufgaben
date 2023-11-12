import numpy as np
import matplotlib.pyplot as plt

# eigene Lösung hat nicht  funktioniert, deshalb habe ich am ende die läsnug aus der besprechung übernommen

x_data = np.array([1997,1999,2006,2010])-1997
y_data =np.array([150,104,172,152])



A = np.array([[x_data[0]**3,x_data[0]**2,x_data[0],1],
              [x_data[1]**3,x_data[1]**2,x_data[1],1],
              [x_data[2]**3,x_data[2]**2,x_data[2],1],
              [x_data[3]**3,x_data[3]**2,x_data[3],1]])

b = y_data
c = np.linalg.solve(A,b)
print("c = ",c)

plt.figure(1)
plt.plot(x_data, y_data,color="red", marker = "o", linestyle = "", markersize="8")
x_plot = np.arange(0,15,0.1)
y_plot = np.polyval(c, x_plot)
plt.plot(x_plot, y_plot, color = "blue")
plt.grid()

# A

x_est = np.array([2003, 2004])-1997
y_est = np.polyval(c, x_est)

plt.figure(2)
plt.plot(x_data, y_data,color="red", marker = "o", linestyle = "", markersize="8")
plt.plot(x_est, y_est,color="red", marker = "o", linestyle = "", markersize="8")

x_plot = np.arange(0,15,0.1)
y_plot = np.polyval(c,x_plot)

plt.plot(x_plot, y_plot, color="blue")
plt.grid()
plt.ylim([0,200])

# B


c_new = np.polyfit(x_data, y_data,3)
print("cnew = ",c_new)

plt.figure(3)
plt.plot(x_data, y_data,color="red", marker = "o", linestyle = "", markersize="9")
x_new = x_plot
y_new = np.polyval(c_new,x_new)
plt.plot(x_new,y_new, color="purple")
plt.grid()
plt.ylim([0,200])