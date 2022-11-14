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
            print(T - ttt)
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




def main():
    print(distance(0.5,anna))


if __name__ == '__main__':
    main()























