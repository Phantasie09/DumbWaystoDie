import numpy as np
from numba import *

import time

global v
global A


v = np.array([3, -1])
A = np.array([[2, -1], [-4, 8]])



# Press the green button in the gutter to run the script.

def drucker():
    print(A[0, 1])
    print(A.shape)
    print(A.size)
    print(v + v)
    print(A * v)
    print(np.dot(v, v))
    print(v * v)


def main():
    print(np.linspace (0,100,5))
    print(np.arange(0,1,0.1))
    print(np.eye(3))

if __name__ == '__main__':
    main()


