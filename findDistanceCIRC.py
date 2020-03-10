from geopy import distance
import serial
#ser = serial.Serial('/dev/ttyACM0', 9600)#assigning to port 
#GPSdata=ser.readline()#assigning to variable
def FindDistance(lattitude,longitude,lattitude2,longitude2):
    #kerrHall = (43.657972, -79.378915)
    #SLC = (43.657926, -79.377756)
    Pt1 =(lattitude,longitude)
    Pt2 = (lattitude2,longitude2)
    print("distance from desired point 1 in meters then cm  ")
    Dist= [round( distance.distance(Pt1, Pt2).m),round((distance.distance(Pt1, Pt2).m)/100)]#gets distance (difference betw. pts)
    '''
    if gps is set up uncomment ser and GPSdata change Pt1 to GPSdata
    '''
    #print(distance.distance(GPSdata,SLC).km)
    print(Dist)
    return (Dist)
    
    
    #display GPS map:
    
FindDistance(90,-200,-90,300)
