import numpy as np
from matplotlib import pylab as plt


def relu(x):
    return np.maximum(0, x)

def leaky_relu(x):
    return np.maximum(0.2*x, x)

A = np.arange(-5.0, 5.0, 0.1)
y = leaky_relu(A)
plt.plot(A, y)
plt.show()