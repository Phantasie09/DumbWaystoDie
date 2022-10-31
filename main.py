import numpy as np
from numba import *
import math
import matplotlib.pyplot as plt
import time

global v
global A


v = np.array([3, -1])
A = np.array([[2, -1], [-4, 8]])



# Press the green button in the gutter to run the script.

def Gauss():

    sigma = 0.5
    mu = 0.1

    x = np.arange(0, 1, 0.01)

    y = np.exp(-(x - mu) * 2 / (2 * sigma * 2)) / (sigma * np.sqrt(2 * np.pi))

    plt.plot(x, y)
    plt.grid()


def drucker():
    print(A[0, 1])
    print(A.shape)
    print(A.size)
    print(v + v)
    print(A * v)
    print(np.dot(v, v))
    print(v * v)
    print(np.linspace (0,100,5))
    print(np.arange(0,1,0.1))
    print(np.eye(3))

def main():
    Gauss()

if __name__ == '__main__':
    main()


