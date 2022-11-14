
import numpy as np
from roadster.roadster import *


### PART 3B ###
def reach(C, route):
    x = 1
    n = 1000
    def f(x):
        return C - total_consumption(x, route, n)
    def fdx(x):
        return consumption(velocity(x, route))
    print(f(x), fdx(x))
    while abs(f(x)) > 10e-4 and x < max(load_route(route)[0]):
        x = x - f(x)/fdx(x)
        print(x)
    return x
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')

print(reach(100000, 'speed_anna'))
    
    
