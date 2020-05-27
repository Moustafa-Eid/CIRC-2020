# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:27:04 2020

@author: Aiman Hussaini
"""

import math

ref = (0,0)                                 # Reference point

unit = (1,0)


def vector(a, r) :                      
    """Returns difference between a point and reference point."""
    return [a[0] - r[0], a[1] - r[1]]

def length(a) :                        
    """Returns the length of the vector connecting cartesian point a and the origin (0, 0)."""
    return math.sqrt(a[0]**2 + a[1]**2) 

def dotprod(a, b) :                    
    """Returns dot product of two vectors (needed to find angle)."""    
    return a[0]*b[0] + a[1]*b[1]

def angle(a, b) :                       
    """Finds angle between rover and destination point in radians."""
    cosAng = dotprod(a, b)/(length(a)*length(b))
    return math.acos(cosAng)

def radToDeg(a) :                       
    """Converts angle from radians to degrees"""
    return a*180/math.pi

def findAngle(pointOne, pointTwo) :
    """Returns the angle between two points using the origin as a reference point."""
    point1 = vector(pointOne, ref)                
    point2 = vector(pointTwo, ref)                

    ang = radToDeg(angle(point1, point2))
    
    return ang

def find_angle(current, destination, heading) :
    """Returns the angle the rover must turn to face its destination point given current heading."""
    default = (1, 0)
    parallel_vector = (destination[0] - current[0], destination[1] - current[1])
    if destination[1] < current[1] :
        pv_angle = 360 - findAngle(parallel_vector, default)
    else : 
        pv_angle = findAngle(parallel_vector, default)
    turn_angle = pv_angle - heading/10
    return turn_angle
