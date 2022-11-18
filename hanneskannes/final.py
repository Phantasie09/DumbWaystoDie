from time import strftime

import numpy as np
from route_nyc import *
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid



def nyc_route_traveler_tim ( t0 , h ):
    assert 0 <= t0 <= 24, "out of Range" #In Hours
    print("Start")
    time_h, distance_km, speed_kmph=[],[],[]
    def help_me(y,actT,end=60):
        speed = route_nyc(actT,y)[0][0]
        time_h.append(actT)
        distance_km.append(y)
        speed_kmph.append(speed)
        if y+ h*speed< end:
            return help_me(y+ h*speed,actT+h)
        else:
            last_step= (60-y)/speed
            time =actT+last_step
            time_h.append(time)
            distance_km.append(60)
            speed_kmph.append(speed)
            return np.array(time_h),np.array(distance_km),np.array(speed_kmph)
    return help_me(0,t0)



print("hi")
print(route_nyc(4,0)[0][0])

print(nyc_route_traveler_tim(4.00,0.05))
