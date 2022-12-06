import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.sin(x)

xmin, xmax = 0, 7
n = 5


X = list(np.linspace(xmin, xmax, n*2+1))
Y = [f(x) for x in X]


def draw(X, Y):
    if len(X) != len(Y):
        print('not same size')
        return
    i = 0
    while i < len(X)-1:
        x = [X[i], X[i+1], X[i+2]]
        y = [Y[i], Y[i+1], Y[i+2]]
        a, b, c = np.polyfit(x, y, 2)
        def f (x, a, b, c):
            return a*x**2 + b*x + c
        XX = np.linspace(X[i], X[i+2])
        plt.plot(XX, f(XX, a, b, c))
        i += 2
        
print(X)

draw(X, Y)
x = np.arange(xmin, xmax, 0.001)
plt.plot(x, f(x), '--')
plt.plot(X, Y, marker = 'o', ls = '')

