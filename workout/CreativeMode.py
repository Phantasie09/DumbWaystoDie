import numpy as np
from projekte import *
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid
import math

def Warm(h,b=1,a=0):
    points=np.arange(a,b+h,h)
    return h*(sum(f(points))-(f(points[0])+f(points[-1]))/2)
def f(x):
    return (x ** 2) * (math.e ** x)


def main():
    print(Warm(1/4))


if __name__ == '__main__':
    main()