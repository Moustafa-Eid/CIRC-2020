# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:27:04 2020

@author: Aiman Hussaini
"""

import math

p1 = [12, 4]                                # Destination Point (latitude, longitude)
p2 = [9, 6]                                 # Dummy second point. I want to create this by taking our ref
                                            # and findHeading, then extrapolating it to any point on that line
ref = [0,0]                                 # Reference point, ie. Rover's current location
    
def findAngle(pointOne, pointTwo) :
    
    def vector(a, r) :                      # Returns difference between a point and reference point
        return [a[0] - r[0], a[1] - r[1]]
    
    point1 = vector(p1, ref)                # Points in relation to rover's current position. These
    point2 = vector(p2, ref)                # are the points we work with going forward
    
    def length(a) :                         # Accepts inputs for a point and reference point, returns the length
        return math.sqrt(a[0]**2 + a[1]**2) # Can likely be replaced by findDistance
    
    def dotprod(a, b) :                     # Returns dot product of two vectors (needed to find angle)    
        return a[0]*b[0] + a[1]*b[1]
    
    def angle(a, b) :                       # Finds angle between rover and destination point in radians
        cosAng = dotprod(a, b)/(length(a)*length(b))
        return math.acos(cosAng)
    
    def radToDeg(a) :                       # Converts angle to degrees
        return a*180/math.pi
    
    ang = radToDeg(angle(point1, point2))
    
    print("The angle in degrees is " + str(round(ang, 1)))      # Prints the angle to 1 decimal point
    return ang                                                  # Actual angle accuracy is much higher

print(findAngle(p1, p2))






# ok so what I'm thinking is to have a point that is our current gps location, 
# use that as a reference point (assuming it's (0,0) rn). We can use this reference point
# along with our heading to extrapolate a point somewhere further, then use that and our
# desired location to calculate angle. Then translate that angle to PWM code to make the wheels move and ta-da    