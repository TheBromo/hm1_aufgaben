import numpy as np

arr = np.array([[1, 0, 2], [0, 1, 0], [0.0001, 0, 0.0001]])
inv = np.linalg.inv(arr)
print(arr)
print(inv)
print(np.linalg.norm(arr, 1))
print(np.linalg.norm(inv, 1))
print(np.linalg.norm(arr, 1) * np.linalg.norm(inv, 1))
print(np.linalg.cond(arr))

print(2.e+04 + 1.e+04)

print("------------------")

print(np.linalg.norm(arr, np.inf))
print(np.linalg.norm(inv, np.inf))
print(np.linalg.norm(arr, np.inf) * np.linalg.norm(inv, np.inf))

b = np.array([1, 1, 1.7 * 10e-7])

r= np.linalg.solve(arr,b)
print(r)