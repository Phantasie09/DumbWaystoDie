import numpy as np
from scipy import interpolate
elsa='speed_elsa.npz'
anna='speed_anna.npz'

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    a1 = 546.8
    a2 = 50.31
    a3 = 0.2584
    a4 = 0.008210
    return a1/v+a2+a3*v+a4*v**2

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x, route, n):
    h = x/n
    position = np.linspace(0, x, n+1)
    speed = 1/velocity(position, route)
    #t = trapezoid(speed,position)
    return h*(np.sum(speed) - (speed[0] + speed[-1])/2)


### PART 2B ###
def total_consumption(x, route, n):
    h = x/n
    position = np.linspace(0, x, n+1)
    mjamjam  = consumption(velocity(position, route))
    #t = trapezoid(mjamjam ,position)
    return h*(np.sum(mjamjam ) - (mjamjam [0] + mjamjam [-1])/2)


### PART 3A ###
def distance(T, route,n=10**7):
    strecke = load_route(route)[0]
    def _distance(T,min,max):
        ttt = time_to_destination(min+(max -min)/2, route, n)
        if 0<=T-ttt<=10**(-10):
            print("Timediff:",T - ttt)
            return (min+(max -min)/2)

        elif ttt < T:
            return _distance(T,min+(max -min)/2,max)
        else:
            return _distance(T,min,max-(max -min)/2 )

    if time_to_destination(max(strecke), route, 1000)<T:
        print("Stop",time_to_destination(max(strecke), route, n))
        return max(strecke)
    else:
        return _distance(T,0 , max(strecke))



### PART 3B ###
def reach(C, route, n = 10**7):
    strecke = load_route(route)[0]
    def _reach(x):
        leakage=total_consumption(x, route, n)
        if 0<leakage-C< 10**(-10):
            print("Succes:",leakage)
            return x
        else:
            return _reach(x-(leakage-C)/consumption(velocity(x, route)))

    if total_consumption(max(strecke),route,n)<C:
        print("Stop",total_consumption(max(strecke), route, n))
        return max(strecke)
    else:
        return _reach(0)
    
