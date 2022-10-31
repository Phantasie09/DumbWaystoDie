#!/usr/bin/env python3
import numpy as np
import roadster
import matplotlib.pyplot as plt

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)


plt.plot(speed_kmph, consumption_Whpkm)
plt.xlabel(r'$v$ / km/h')
plt.ylabel(r'$c$ / Wh/km')
