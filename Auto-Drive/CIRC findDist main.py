#METHOD #1:
import findDistance
import socket
import math
import numpy as np
import serial

'''
-------psudocode==> alternate method ==> METHOD#2:----------
==> add possible encoder code/PID code
==> add python code that turns pwm signal on the arduino
==> look into actual legit path finding algorithms: but remember we are dealing with the real world so setup some sort of node systems like a dotted grid

1. GPS function:
 
Get the current GPS position of the rover and compare by subtracting 
this from the designated GPS location

==> create a double array to hold the designated GPS coordinates,and 
another array for the theoretical angle(w/ a heading==> so basically a compass) 
needed to go from designation starting pt to: 1 to 2 to 3,etc.
 
==> once 1st location is reached within a threshold cross out that location and compass value
 and either move on to the next location or move to the closest location.
 
--note, we dont have to erase it, 
though the thing to think about is: memory optimization vs less possibility for error/disorganization

2. Send Arduino function:

send the amount of power needed in bits to the pi which sends power to the motors 

==> look at how to use python code to turn on PWM signal on an arduino
==> look at how to determine exactly what numbers to send for motor power for each case 
( maybe by mapping/converting each sensors range to motor power range (-128 to +128)--?  )

3.. Compass Function:


where: '=/=' is does not equal

if (compass has N,S,E,W)
{
 
==> if (current compass reading =/= theoretical compass value for specific destination)  

use sendArduino function rotate the rover :


if (heading = theoretical heading
rotate by (Current Compass - theoretical Compass)

else if ( heading =/= theo heading)
rotate by abs(Current Compass - theoretical Compass) in the direction of theoretical heading
}

if (compass doesnt have N,S,E,W)
{
    
--add something here--
    
}
4. Computer Vision/AR code finding Function: 
==> look into glare,masking,etc. for object detection

--------------------------NOTE--------------------------------------------------------------
==> camera is 360 deg (a normal camera attached to a servo motor making it 360deg)
==> lidar can only detect shapes and distances, not colour like a normal camera would 
(so using opencv cannot occur, however==>one can run 2 programs to try and guess whats infront of it) 
----------------------------------------------------------------------------------------------
    if (object= detected):
        figure out object size: 
        ==>method 1: use openCV libraries
        ==> method 2: rotate rover left until object=/= detected then do this
        with the right side from this the width of the object could be determined.
         ==> method 3: if the competition released obstacle dimensions we could use this 
         for object avoidence


if camerea = 360 deg:
    method 1: 
    
         if object = infront of rover:
            ==> rotate until object in front view is gone and camera detects object 
             at rovers side
            ==> move forward until object not detected in side view anymore
            ==> rotate back until object can be seen again w/ a small threshhold to not hit 
            object, 
            ==> then move straight
    
    method 2:
        ==> set a limit as to how close an object should be to the rover then just maneuver around it
        accordingly
        
if camera =/= 360 deg:
    arduino send signal to motors to rotate rover until object=/= detected, then
    arduino makes motors move straight until objects cleared, then return rover to designated compass 
    orientation (now starting in front of object, as the new ref)
 -----------------------------------------------------------------------
                                REFERENCES-1:
------------------------------------------------------------------------                             
 1. reading serial from a raspberry pi:
  i. https://pimylifeup.com/raspberry-pi-serial/
  ii. https://raspberrypi.stackexchange.com/questions/935/how-do-i-get-the-data-from-the-serial-port
  iii. https://www.instructables.com/id/Read-and-write-from-serial-port-with-Raspberry-Pi/
 
 2. finding the shortest path:
 i. my own method
 ii.https://stackoverflow.com/questions/59230049/find-the-shortest-distance-between-sets-of-gps-coordinates-python
 iii. https://stackoverflow.com/questions/52051503/how-to-find-shortest-distance-of-a-location-from-a-route-python
 

    '''




'''
 ser = serial.Serial('/dev/ttyACM0', 9600)#assigning to port 
 GPSdata=ser.readline()#assigning to variable

  if gps is set up uncomment ser and GPSdata change Pt1 to GPSdata
'''





# my own method #1: finding the shortest path: 

# Rover gps position:
RoverGPSPos = [0,0]

#kerrHall = (43.657972, -79.378915)
# SLC = (43.657926, -79.377756)
GPS_locations =[]
GPS1 = [11,21]
GPS2 = [23,-4]
GPS3=[42,6]
GPS4=[90,83]
GPS5=[2,2]
GPS6=[11,-90]

'''
REFERENCES-3: to append onto a 2D arrays: 
1. https://thispointer.com/numpy-append-how-to-append-elements-at-the-end-of-a-numpy-array-in-python/
2. https://stackoverflow.com/questions/8183146/two-dimensional-array-in-python
3.https://stackoverflow.com/questions/50116416/appending-to-2-dimensional-array-in-python
4. https://stackoverflow.com/questions/9775297/append-a-numpy-array-to-a-numpy-array

''' 
#appending GPS locations , from ref 3, #3: 
GPS_locations.append(GPS1)
GPS_locations.append(GPS2)
GPS_locations.append(GPS3)
GPS_locations.append(GPS4)
GPS_locations.append(GPS5)
GPS_locations.append(GPS6)


GPS_Threshold = [1.5,3.3]# [lat,long]



'''
References-2: to select all elements in array:

1. https://www.geeksforgeeks.org/python-accessing-all-elements-at-given-list-of-indexes/
2. https://thispointer.com/find-max-value-its-index-in-numpy-array-numpy-amax/
3.getting 1st element of each sublist:  https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/

4. finding index of a val: 
i. https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
ii. https://www.geeksforgeeks.org/python-ways-to-find-indices-of-value-in-list/
iii.https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
'''

#getting lat and long of GPS locations: 
GPSlocations_Lat= [item[0] for item in GPS_locations] #from ref-2: #3.
GPSlocations_Long= [item[1] for item in GPS_locations]
# finding hypoteneuse:
# cant subtract a list from a list error solved by ==> https://stackoverflow.com/questions/26685679/typeerror-unsupported-operand-types-for-list-and-list

hypDist= np.sqrt(np.array(((np.array(GPSlocations_Lat)-RoverGPSPos[0])**2)) + np.array(((np.array(GPSlocations_Long)-RoverGPSPos[1])**2))) 
# cant use math.sqrt() for an array so use np.sqrt()
# below from: https://www.geeksforgeeks.org/numpy-sqrt-in-python/
print("The hypotenuse values (in sqrt(lat and long coordinates) ) are:" +str(hypDist))
MinHypVal = np.min(hypDist)
print("the smallest hyp value is:"+ str(MinHypVal))# or can use==> np.array(call array).min()
# below from : https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
MinHypIndex = np.where(np.array(hypDist)==MinHypVal)[0]
#x = [ n for n, z in enumerate(hypDist) if z== MinHypVal]
y = int("".join(map(str,MinHypIndex))) #from:https://www.geeksforgeeks.org/python-convert-a-list-of-multiple-integers-into-a-single-integer/

MinHypIndex=y 
print("method #1: The MinHypIndex is:"+str(MinHypIndex))

Dist2Location=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[MinHypIndex][0],GPS_locations[MinHypIndex][1],GPS_Threshold[0],GPS_Threshold[1])

print("The distance to the closest pt(in cm then m) are:"  + str(Dist2Location))

# my own method option #2: using the findDistance function inputting all gps coordinates, then find min dist:
'''Dist=[]
Dist1=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[0][0],GPS_locations[0][1],GPS_Threshold[0],GPS_Threshold[1])
Dist2=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[1][0],GPS_locations[1][1],GPS_Threshold[0],GPS_Threshold[1])
Dist3=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[2][0],GPS_locations[2][1],GPS_Threshold[0],GPS_Threshold[1])
Dist4=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[3][0],GPS_locations[3][1],GPS_Threshold[0],GPS_Threshold[1])
Dist5=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[4][0],GPS_locations[4][1],GPS_Threshold[0],GPS_Threshold[1])
Dist6=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[5][0],GPS_locations[5][1],GPS_Threshold[0],GPS_Threshold[1])
#appending:
Dist.append(Dist1)
Dist.append(Dist2)
Dist.append(Dist3)
Dist.append(Dist4)
Dist.append(Dist5)
Dist.append(Dist6)
print("my method #2: The distances (in cm then m) are: "+str(Dist))
#finding min val: 
minDistval = np.min(Dist)
print("method #2: the min dist (in m) is: " + str(minDistval))
'''
#optional==> deleting gps coordinates out of the array if rover reaches them( basically similar to a checklist):

# my own method #3: using a node type method (further develop from method#1) 
'''
basically use method #2's idea but add more gps pts shortening the dist betw. each pt/node. Each pt or node
will be within the bounds of the end gps location goal (basically each small node paves a pathway fro the rover to go until end goal is reached) 
'''


#method #4: using path finding algorithms/known node methods: 

