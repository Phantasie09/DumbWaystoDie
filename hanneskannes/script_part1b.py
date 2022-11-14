import numpy as np
from roadster import *
import matplotlib.pyplot as plt

plt
def plot(name, n = 10000):
    plt.figure()
    distance_km, speed_kmph = load_route(f'{name}')
    position = np.linspace(0, max(distance_km), n)
    speed=velocity(position, name)
    plt.plot(position, speed, '-', markersize = 0.1, label = f'interpolation n = {n}')
    plt.scatter(distance_km, speed_kmph, s = [50]*len(speed_kmph), marker = '+', color = 'r', label = 'data')
    plt.xlabel(r'$distance$ / km')
    plt.ylabel(r'$speed$ / km/h')
    plt.title(f'Part 1b: Consumption data: {name}')
    plt.savefig(fname=f'plot 1b_{(name.split("_")[1]).split(".")[0]}')
    plt.legend()
    plt.show()
    #plt.close()
    #plt.cla()
plot("speed_anna.npz")
plot("speed_elsa.npz")



