# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:56:55 2020

@author: Aiman Hussaini

Some Details:

This file simulates the rover's movement and prints it to the console.
It's given its current location (eventually will be taken from the gps module)
and its heading (read from the compass module).
Our compass module returns a 4-bit value, a number from 0-3599. Each
increment is equal to 0.1 degrees, so all angles = heading/10 
(eg. 1800 = 180 degrees from its original direction when powered on).
Eventually will read/write the heading to a text file when we have access to the module.
The program uses simple cartesian points for testing but can easily be
swapped out for more accurate gps coordinates.

Functions:
- Prints current location and heading
- Determines most efficient turn to face destination point
- Calculates distance to drive
- Updates location and writes to a text file
- Basic graph showing the rover's trajectory
"""
import math
import findAngle as ang
import matplotlib.pyplot as plt

f = open("Previous Locations.txt", "w+")

# TODO:
# Create a grid ui visualization that shows the rover's 
# movement

class Rover:
    heading = 0 # (read continuously from file)
    current_location = (0, 0)
    current_speed = 0 # Undecided Parameter
    distance_to_travel = 0 # Undecided Parameter
    # Add more parameters if necessary

    def __init__(self, loc, heading):
        self.current_location = loc
        self.heading = heading

    def move(self, destination) :
        print("Current Location: " + str(self.current_location))
        print("Current Heading: " + str(self.heading))
        a = ang.find_angle(self.current_location, destination, self.heading)
        # This next block of code just ensures the rover takes the most
        # efficient turn (eg. turns 90 degrees right instead of 270 degrees left)
        if abs(a) > 180 :
            while(a > 360) :
                a -= 360
            while(a < -360) :
                a += 360
            if -180 > a and a > -360 :
                a += 360
            if a > 180 and a < 360 :
                a = 360 - a
            angle = a
        else:
            angle = a
        print("Turning " + str(angle) + " degrees")   # Positive angle rotates left, negative rotates right
        new_heading = self.heading + round(angle*10)
        if new_heading < 0 : 
            self.heading = (3600 + new_heading)%3600
        else :
            self.heading = new_heading%3600
        print("Current Heading: " + str(self.heading))
        print("Moving " + str(ang.length((destination[0]-self.current_location[0], destination[1]-self.current_location[1]))) + " metres")
        self.current_location = destination
        print("New Location: " + str(self.current_location) + "\n")
        xloc.append(self.current_location[0])
        yloc.append(self.current_location[1])

rover = Rover((12, 9), 1200) # current position and heading
f.write(str(rover.current_location) + "\n")
xloc = [rover.current_location[0]]
yloc = [rover.current_location[1]]

coordinates = [(1, 16), (2, 2), (6, 9), (5, 9), (5, 10)]



for x in coordinates :
    rover.move(x)
    f.write(str(rover.current_location) + "\n")

f.close()

# PLOT/VISUALIZATION STARTS HERE

plt.plot(xloc, yloc)
plt.plot(xloc, yloc, 'ro')
plt.axis([0, 25, 0, 25])
plt.show()