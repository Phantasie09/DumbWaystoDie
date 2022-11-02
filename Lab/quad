from scipy . integrate import quad
import numpy as np
import math
from scipy . integrate import trapezoid

def f(x):
    return 4/(x**2+1)

xl=1
xr= math.inf

(I , err ) = quad (f , xl , xr )
print(I,err)
t= np.arange(0,1,0.2)
S=[0.2, 0.368, 0.381, 0.228, 0.049]

L = trapezoid (S , t )
print(L)




def h(m):
    g=lambda r: 4*math.pi*r*(1-r/m)**(1/6)
    xl=0
    xr=m
    (I , err ) = quad (g , xl , xr )
    return (I, err)

print("Tube")
print(h(6))

def kappa(g):
        x=np.arange(0,4.5,0.5)
        y=np.array([0.0, 1.2, 2.0, 1.4, 1.0, 1.5, 4.0, 4.1, 0.0])
        P = trapezoid (y*0.05 , x )
        return P
print("Soil")
print(kappa(5))