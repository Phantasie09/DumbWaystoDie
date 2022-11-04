import numpy as np
from roadster import *
import matplotlib.pyplot as plt


def plot(name):
    distance_km, speed_kmph = load_route(f'{name}')
    position = np.linspace(0, max(distance_km), 100000)
    speed=velocity(position,'speed_anna')
    plt.plot(position, speed, '-', markersize = 1)
    plt.scatter(distance_km, speed_kmph, s = [3]*len(speed_kmph), marker = 'd', color = 'r')
    plt.xlabel(r'$v$ / km/h')
    plt.ylabel(r'$m$ / km')
    plt.title('Part 1b: Consumption data')
    plt.savefig(fname='plot 1b')
    plt.show()
    #plt.cla()
plot("speed_anna.npz")



