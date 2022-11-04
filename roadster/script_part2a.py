import numpy as np
from roadster import *
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid


def time_to_destination (x , route , n ):
    h = x/n
    position = np.linspace(0, x, n+1)
    speed = 1/velocity(position, route)
    t = trapezoid(speed,position)
    return h*(np.sum(speed) - (speed[0] + speed[-1])/2)
  

def timekonverter(x): #WIth Inspiration of Concept INput in Sec
    if x // (365.2425243600) < 1: # year
        if x//(24 * 3600)>1: #day
            days = x // (24 * 3600)
            hours = (x % (24 * 3600))/3600
            return [int(days),"days",int(hours),"hours"]
        else:
            hours=x // 3600
            seconds= x % 3600
            return[int(hours),"hours",int(seconds),"seconds"]
    else:
        days= (x % (365.2425243600))/(243600)
        years=x // (365.242524*3600)
        return [int(years),"years",int(days),"days"]

print(time_to_destination(30, 'speed_anna.npz', n = 10)*3600)
print(timekonverter(212223))
print(timekonverter( time_to_destination(30, 'speed_anna.npz', n = 10)*3600))