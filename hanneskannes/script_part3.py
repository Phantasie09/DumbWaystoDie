import numpy as np
from roadster import *
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

elsa = 'speed_elsa.npz'
anna = 'speed_anna.npz'

def time_to_destination (x , route , n ):
    h = x/n
    position = np.linspace(0, x, n+1)
    speed = 1/velocity(position, route)
    t = trapezoid(speed,position)
    return h*(np.sum(speed) - (speed[0] + speed[-1])/2)


def distance(T, route):
    strecke = load_route(route)[0]
    def _distance(T,min,max):
        ttt = time_to_destination(min+(max -min)/2, route, 1000)
        if 0<=T-ttt<=10**(-4):
            print("Timediff:",T - ttt)
            return (min+(max -min)/2)

        elif ttt < T:
            return _distance(T,min+(max -min)/2,max)
        else:
            return _distance(T,min,max-(max -min)/2 )

    if time_to_destination(max(strecke), route, 1000)<T:
        print("Stop",time_to_destination(max(strecke), route, 1000))
        return "out of border"
    else:
        return _distance(T,0 , max(strecke))


def total_consumption (x , route , n ):
    h = x/n
    position = np.linspace(0, x, n+1)
    mjamjam  = consumption(velocity(position, route))
    t = trapezoid(mjamjam ,position)
    return h*(np.sum(mjamjam ) - (mjamjam [0] + mjamjam [-1])/2)

def reach(C, route,n=1000):
    strecke = load_route(route)[0]
    def _reach(x):
        leakage=total_consumption(x, route, n)
        if 0<leakage-C< 10**(-4):
            print("Succes:",leakage)
            return x
        else:
            return _reach(x-(leakage-C)/consumption(velocity(x, route)))

    if total_consumption(max(strecke),route,n)<C:
        print("Stop",total_consumption(max(strecke), route, 1000))
        return "out of border"
    else:
        return _reach(0)









def main():
    #print(distance(0.5,anna))
    print(reach(10000, 'speed_anna'))

if __name__ == '__main__':
    main()























