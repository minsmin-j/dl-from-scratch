import numpy as np


def relu(x):
    return np.maximum(0, x)

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
c = np.array([1, 2])
print(c.shape)