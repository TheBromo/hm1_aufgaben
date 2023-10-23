import numpy as np

x = np.array([7,8,6,3,3/2,5,4,3/2])
y = np.array([8,5,6,2,7,3,4,1])

# c = [[-6, -12], [-13, 1], [-5, -4], [-1, 10], [14, -5], [-3, 9], [-2, 2], [14, 12]]

print(np.sort(x))
print(np.sort(y))


def empCov(arr1, arr2):
    mean1 = np.mean(arr1)
    mean2 = np.mean(arr2)
    sum = 0
    for i in range(len(arr1)):
        sum += (arr1[i] - mean1) * (arr2[i] - mean2)
    return np.sqrt((1 / len(arr1)) * sum)


def mean(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)


def cov(arr):
    mean = np.mean(arr)
    sum = 0
    for i in range(len(arr)):
        sum += (arr[i] - mean) ** 2
    return np.sqrt((1 / len(arr)) * sum)


sum = 0
mean_x = mean(x)
mean_y = mean(y)

for i in range(len(x)):
    sum += (x[i] - mean_x) * (y[i] - mean_y)

sxy = 1 / len(x) * sum

print(sxy)

#r = sxy / (sy * sx)

#print(r)

# sx 6.020797289396148
# sy 7.3875834268648966
