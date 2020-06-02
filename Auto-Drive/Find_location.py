#!/usr/bin/python

import serial
import pynmea2
ser = serial.Serial('/dev/cu.usbmodem1421', baudrate=9600)
while 1:
     data = ser.readline()
     if (data.startswith("$GPGGA")):
         #pynmea2.parse(data)
         #print data
         msg = pynmea2.parse(data)
         #print repr(msg)
         print msg.lat
         print msg.lat_dir
         print msg.lon
         print msg.lon_dir
