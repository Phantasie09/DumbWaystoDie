import numpy as np
import matplotlib.pyplot as plt


P0 = [-10, 0.5]
#obere line
P1 = [-1.8, 1.5]
P2 = [-1.6, 3]
P3 = [-1.2, 2.8]
P4 = [0, 2.9]
#untere line
p1 = [-7, 0]
p2 = [-4, -1]
p3 = [-1.5, -3]
p4 = [0, -2.6]

#obere Linie
def f1(x):
    X = [P0[0], -4, P1[0]]
    Y = [P0[1], 2, P1[1]]
    a, b, c = np.polyfit(X, Y, 2)
    return a*x**2 + b*x + c

def f2(x):
    X = [P1[0], -1.7, P2[0]]
    Y = [P1[1], 2, P2[1]]
    a, b, c = np.polyfit(X, Y, 2)
    return a*x**2 + b*x + c

def f3(x):
    X = [P2[0], P3[0]]
    Y = [P2[1], P3[1]]
    a, b = np.polyfit(X, Y, 1)
    return a*x + b

def f4(x):
    X = [P3[0], 0, -P3[0]]
    Y = [P3[1], P4[1], P3[1]]
    a, b, c = np.polyfit(X, Y, 2)
    return a*x**2 + b*x + c

#untere Line

def f5(x):
    X = [P0[0], -8, p1[0]]
    Y = [P0[1], 0.4, p1[1]]
    a, b, c = np.polyfit(X, Y, 2)
    return a*x**2 + b*x + c

def f6(x):
    X = [p1[0], -8, p2[0]]
    Y = [p1[1], 0.4, p2[1]]
    a, b, c = np.polyfit(X, Y, 2)
    return a*x**2 + b*x + c


x1 = np.linspace(P0[0], P1[0], 100)
x2 = np.linspace(P1[0], P2[0], 100)
x3 = np.linspace(P2[0], P3[0], 100)
x4 = np.linspace(P3[0], P4[0], 100)
x5 = np.linspace(P0[0], p1[0], 100)

plt.plot(x1, f1(x1))
plt.plot(x2, f2(x2))
plt.plot(x3, f3(x3))
plt.plot(x4, f4(x4))
plt.plot(x5, f5(x5))


