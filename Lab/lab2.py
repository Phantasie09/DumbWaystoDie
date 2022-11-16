import math

import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt
def f(x,r_0=3,c=1.8):
    return 2*(1-x/r_0)**(1/6)-c

def zeichne( r_0, c):
    intervall=np.linspace(-100,100,1000)
    plt.plot(intervall, f(intervall,r_0,c), label='Hejda')
    plt.xlabel(r'$n$')
    plt.ylabel('Error')
    plt.legend()
    plt.title('2(c) Convergence study:')
    plt.grid(which="both")
    plt.show()
    return findsol(f,r_0,c)
def findsol(func,r_0,c):

   return brentq(func,-1000,1.8,args=(r_0,c))

def reaction(x,p=3,K=0.05):
    return x/(1-x)*math.sqrt(2*p/(2+x))-K

def findPArtner():
    intervall = np.linspace(-100, 100, 1000)
    plt.plot(intervall, reaction(intervall), label='Hejda')
    plt.xlabel(r'$n$')
    plt.ylabel('Error')
    plt.legend()
    plt.title('2(c) Convergence study:')
    plt.grid(which="both")
    plt.show()

    return brentq(reaction,-1.5,1000)
print(findPArtner())
#print(zeichne(3,4))