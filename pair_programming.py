import math

def pol_to_cartesian(r, theta):
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    
    return x, y
