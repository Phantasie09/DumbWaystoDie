import numpy as np
from roadster import *
import matplotlib.pyplot as plt


def plot(name):
    distance_km, speed_kmph = load_route(f'{name}')
    position = np.linspace(0, max(distance_km), 1000)
    speed=velocity(position,'speed_anna')
    plt.plot(position, speed,'o' ,markersize=1)
    plt.xlabel(r'$v$ / km/h')
    plt.ylabel(r'$m$ / km')
    plt.title('Part 1b: Consumption data')
    plt.savefig(fname='plot 1b')
    plt.show()
    #plt.cla()
plot("speed_anna.npz")



