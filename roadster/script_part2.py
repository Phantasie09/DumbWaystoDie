import numpy as np
from roadster import *
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

elsa='speed_elsa.npz'
anna='speed_anna.npz'
def time_to_destination (x , route , n ):
    h = x/n
    position = np.linspace(0, x, n+1)
    speed = 1/velocity(position, route)
    t = trapezoid(speed,position)
    return h*(np.sum(speed) - (speed[0] + speed[-1])/2)


def total_consumption (x , route , n ):
    h = x/n
    position = np.linspace(0, x, n+1)
    mjamjam  = consumption(velocity(position, route))
    t = trapezoid(mjamjam ,position)
    return h*(np.sum(mjamjam ) - (mjamjam [0] + mjamjam [-1])/2)
  

def timekonverter(x): #WIth Inspiration of Concept INput in Sec
    if x // (365.2425*24*3600) < 1: # year
        if x//(24 * 3600)>1: #day
            days = x // (24 * 3600)
            hours = (x % (24 * 3600))/3600
            return [int(days),"days",int(hours),"hours"]
        else:
            if x // 3600 < 1:  # day
                sec=x % 60
                min= x // 60
                return[int(min),"min",int(sec),"seconds"]
            else:
                hours = x // 3600
                min = (x % 3600)/60
                return [int(hours), "hours", int(min), "min"]
    else:
        days= (x % (365.2425*24*3600))/(24*3600)
        years=x // (365.2425*24*3600)
        return [int(years),"years",int(days),"days"]

def call(name,n,x):
    user=(name.split("_")[1]).split(".")[0]
    print("User: "+user+", Numerations: "+str(n),", Distance:" +str(x))
    print("time:")
    zeit=time_to_destination(x, name, n) * 3600
    print(*timekonverter(zeit))
    print("Fuel:")
    fuel=(total_consumption(x, name, n) )
    print(fuel)
    return zeit,fuel
def main():
    fueldata=[]
    n=10
    for y in [50]:
        for i in range(1,11):
            fueldata.append(call(anna,n*i,y)[0])
    print(fueldata)

if __name__ == '__main__':
    main()
    
# 2c

x = 65
route = elsa
Routes = [anna, elsa]
N = [2**n for n in range(10, 25)]

for route in Routes:
    time = [time_to_destination(x, route, n) for n in N]
    Error = [abs(time[i]-time[i+1]) for i in range(len(time)-1)]
    plt.loglog(N[:-1], Error, label = f'Error: {route.split("_")[1].split(".")[0]}')

Power = [1, 2, 3]
for p in Power:
    Y = []
    for x in N[:-1]:
        Y.append(1/x**p)
    plt.loglog(N[:-1], Y, label = rf'$O(1/(n^{p}$)')    
                
plt.xlabel(r'$n$')
plt.ylabel('Error')
plt.legend()
plt.title('2(c) Convergence study:')
plt.grid(which="both")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    