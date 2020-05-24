
from geopy import distance

import serial




def FindDistance(lattitude,longitude,lattitude2,longitude2,LatThreshold,LongThreshold):
  Pt1 =[lattitude,longitude]
  Pt2 = [lattitude2+LatThreshold,longitude2+LongThreshold] #+[LatThreshold,LongThreshold] #add code that evaluates at +- threshold value---?
  Dist= [round( distance.distance(Pt1, Pt2).m),round((distance.distance(Pt1, Pt2).m)/100)]#gets distance (difference betw. pts)

  #print(distance.distance(GPSdata,SLC).km)
  return (Dist)

    

    
