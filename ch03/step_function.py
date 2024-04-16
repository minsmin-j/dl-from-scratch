import numpy as np
from matplotlib import pylab as plt


def step(x):
    theta = 0
    return np.array(x>theta, dtype=np.int_)

X = np.arange(-5.0, 5.0, 0.1)
Y = step(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # y축의 범위 지정
plt.show()