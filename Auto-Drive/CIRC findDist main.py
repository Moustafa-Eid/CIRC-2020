#import findAngle
import findDistance
#import sendArduino
import socket
import math
import numpy as np
import serial
import pandas as pd
#import geopandas as gpdcd 
import matplotlib.pyplot as plt 
#import picket 

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




#sendArduino:
'''
NOTE:
==> figure out each message for each case,
 sent to determine power given to motors

==> also figure out python code that turns
 PWM signal on, to an arduino


message = "100200300400500600"
UDP_IP = "192.168.1.210"
UDP_PORT =8090
# template==> SendArduino(message,UDP_IP,UDP_PORT):

Sock = sendArduino.SendArduino(message,UDP_IP,UDP_PORT)[1]
SentSockVal = sendArduino.SendArduino(message,UDP_IP,UDP_PORT)[0]
print("The sent socket value is :" + str(SentSockVal)+ " and the socket is:" + str(Sock))
'''

'''

  
  REFERENCES:
  1. reading serial from a raspberry pi:
  i. https://pimylifeup.com/raspberry-pi-serial/
  ii. https://raspberrypi.stackexchange.com/questions/935/how-do-i-get-the-data-from-the-serial-port
  iii. https://www.instructables.com/id/Read-and-write-from-serial-port-with-Raspberry-Pi/
 ----------------------------------------------------------------
 '''
 




#------------------------- my own method #1: finding the shortest path: 
'''
     ser = serial.Serial('/dev/ttyACM0', 9600)#assigning to port 
    GPSdata=ser.readline()#assigning to variable

  if gps is set up uncomment ser and GPSdata change RoverGPSPos to GPSdata
'''

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


#-----------------------Adding the Radiation Aspect:

'''
    Psudocode:
    1. option 1: create a ranking system
    for most ideal/shortest method updated with fixed arbitrary Radiation values for now,
    (then sort the updated distances(updated means w/ radiation pts) from shortest to longest )
    
    2. option 2:  Add radiation locations, and tell rover to change path to move around it
 
'''
RadPt1 = [0,0]
RadPt2 = [2,32]

RadiationPts = []

RadiationPts.append(RadPt1)
RadiationPts.append(RadPt2)

RadArray = np.array([RadiationPts]) 

RadThreshold = 60

Radiation = [RadArray + [-RadThreshold,RadThreshold], RadArray + [ RadThreshold,RadThreshold], RadArray + [-RadThreshold,-RadThreshold], RadArray + [RadThreshold,-RadThreshold]] #template is: [TopLeft,TopRight,BottomLeft,BottomRight]
print("The radiation bounds are:" + str(Radiation) +"\n")

#------figure out how to apply this for all possibilities==> if pt is top right/left or bottom right/left of rover for example. -------?

#my own method:
'''
#if gps location is top right of rover:
#for count in range(0,len(GPSlocations_Lat)):
if (((np.any(Radiation[0][0] >= RoverGPSPos[0]) and (np.any(Radiation[0][0]<= GPSlocations_Lat ))) and ((np.any(Radiation[0][1] >= RoverGPSPos[1]) )and (np.any(Radiation[0][1]<= GPSlocations_Long ))))):
       hypDist = np.array(hypDist) + RadThreshold
       print("hyp values with radiation included are:" + str(hypDist))
'''
#trying to use picket library:




#trying to use geopandas library:


#other methods:
'''
from: 
1.
i. https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python
ii. https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

2.https://stackoverflow.com/questions/43892459/check-if-geo-point-is-inside-or-outside-of-polygon

3.https://automating-gis-processes.github.io/2017/lessons/L3/point-in-polygon.html

4. what is geofencing and other info: https://developer.tomtom.com/blog/decoded/what-geofencing
5. https://stackoverflow.com/questions/45570618/is-it-possible-to-fit-a-coordinate-to-a-street-in-osmnx

'''



# method from ref-2:


# method from ref-3:


#tangent method:(if geofence is tangent to hypDist(lat,and long portions)+Threshold):
RadThreshold2 = 15
i=0
for count in range(0,len(GPS_locations)):
    RADArray2 = abs(Radiation-abs(np.array([GPSlocations_Lat[count],GPSlocations_Long[count]])-np.array(RoverGPSPos)))
    print("The radiation pts are: \n" + str(RADArray2)+ "\n"+"\n [lat,long] units apart from rover path")
    
    if np.any(RADArray2 <=RadThreshold2):
        i = i+1
        print("# of occurance:" + str(i) + " , GPS location is near radiation area " + "  , The GPS cpprdinate where this occurs is GPS#" + str(count) + " and gps value of:"+str([GPSlocations_Lat[count],GPSlocations_Long[count]]) + '\n')
        #get index of gps pt thats close to radiation area:
       
        #RadIndex = np.where(np.array(RADArray2)<=RadThreshold2)

        #RadIndex = int("".join(map(str,RadIndex))) #from:https://www.geeksforgeeks.org/python-convert-a-list-of-multiple-integers-into-a-single-integer/

        
        #feed that into RADIATION array, then add some distance to hypDist: 
        
        hypDist = hypDist + RadThreshold + RadThreshold # adding Radiations, lat component("RadThreshold") and long component
        print("The adjusted distance for GPS# " + str(count) + "  is:" + str(hypDist)+"\n")
    else:
        print('GPS location is not near radiation area \n')

#-----------------------------------------------------------------------

print("The hypotenuse values (in sqrt(lat and long coordinates) ) are:" +str(hypDist))
MinHypVal = np.min(hypDist)
print("the smallest hyp value is:"+ str(MinHypVal))# or can use==> np.array(call array).min()
# below from : https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
MinHypIndex = np.where(np.array(hypDist)==MinHypVal)[0]
#x = [ n for n, z in enumerate(hypDist) if z== MinHypVal]
y = int("".join(map(str,MinHypIndex))) #from:https://www.geeksforgeeks.org/python-convert-a-list-of-multiple-integers-into-a-single-integer/

MinHypIndex=y 
print("method #1: The MinHypIndex is:"+str(MinHypIndex))

Angle = math.degrees(math.atan(GPS_locations[MinHypIndex][1]/GPS_locations[MinHypIndex][0]))

print("the angle the rover should turn is: " +  str(Angle)+ " degrees")

Dist2Location=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[MinHypIndex][0],GPS_locations[MinHypIndex][1])

print("The distance to the closest pt(in cm then m) are:"  + str(Dist2Location))

#----------------- note see if using geopy is faster than numpy ------------------?

'''
#Creating a distance array: 

Dist=[]
Dist1=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[0][0],GPS_locations[0][1])
Dist2=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[1][0],GPS_locations[1][1])
Dist3=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[2][0],GPS_locations[2][1])
Dist4=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[3][0],GPS_locations[3][1])
Dist5=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[4][0],GPS_locations[4][1])
Dist6=findDistance.FindDistance(RoverGPSPos[0],RoverGPSPos[1],GPS_locations[5][0],GPS_locations[5][1])
#appending:
Dist.append(Dist1)
Dist.append(Dist2)
Dist.append(Dist3)
Dist.append(Dist4)
Dist.append(Dist5)
Dist.append(Dist6)
print("All the distances from the rover to location 1,2,3,etc. (in cm then m) are: "+str(Dist))
'''


#---------------------------Geofencing:
'''
References:
geopy library: https://geopy.readthedocs.io/en/stable/#module-geopy.distance
1. my own method: (making another array adding a threshold to each GPS point)

2. picket library:
https://github.com/sam-drew/picket

NOTE: i could use geopandas library it would make things 1000% easier but
theres a problem with my anaconda environment 

'''
#my own method:
Threshold = 5
#the current GeoFence pt is at the pt where the shortest path is(ie the pt where the rover is currently headed towards): 

HeadedLocation = np.array([GPS_locations[MinHypIndex][0],GPS_locations[MinHypIndex][1]])
                          
CurrentGeoFencePts = [HeadedLocation + [-Threshold,Threshold], HeadedLocation + [ Threshold,Threshold], HeadedLocation + [-Threshold,-Threshold], HeadedLocation + [Threshold,-Threshold]] #template is: [TopLeft,TopRight,BottomLeft,BottomRight]

print("The geofence boundary for the current gps location is a square and is at the following points:" + str(CurrentGeoFencePts))

#

if ((RoverGPSPos[0]>= CurrentGeoFencePts[1][0] and RoverGPSPos[0] <=CurrentGeoFencePts[0][0]) and (RoverGPSPos[1] >=CurrentGeoFencePts[2][1] and RoverGPSPos[1]<=CurrentGeoFencePts[1][1] )):
    print("Rover shall stop")
    '''
    ------------INSERT COMMANDS TO MAKE ROVER DRIVE AROUND THE BORDER HERE:---------------------
    
    '''
    #optional==> deleting gps coordinates out of the array if rover reaches them( basically similar to a checklist):

else:
    print("Rover shall keep going") 


#using the above reference #2(picket library:


# ----------------------------------------------- Figuring out how often the rover is going to read the serial data/ how often are we going to send the serial data: 


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



#--------------------------my own method #2: using a node type method (further develop from method#1) 
'''
basically use method #2's idea but add more gps pts shortening the dist betw. each pt/node. Each pt or node
will be within the bounds of the end gps location goal (basically each small node paves a pathway fro the rover to go until end goal is reached) 
'''


#-------------------------method #3: using path finding algorithms/known node methods: 

