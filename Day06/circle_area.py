# Garden area 
from math import pi
def circle_area(r):
    if type(r) not in [int,float]:
        raise TypeError("the radius must be a non-negative")
    if r<0:
        raise ValueError("the radius cannot be calculation")
    return pi*(r**2)