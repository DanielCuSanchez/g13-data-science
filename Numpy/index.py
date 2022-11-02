import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


print("Numpy 😀")

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[2][3])
print(a.ndim)
print(a.size)
print(a.shape)

arr = np.arange(50)
print(arr)

temp = arr.reshape(2,25)

print(temp)
print(temp[0][:2])
print(temp[(temp % 2 == 0) & (temp <= 20)])
print(arr.min())
print(arr.max())
print(arr.sum())
#print(temp[2].max(axis=0))

# ------------------------------------- #

plt.plot(temp[0], temp[1], 'ro')
plt.axis([0, 50, 0, 50])
plt.show()