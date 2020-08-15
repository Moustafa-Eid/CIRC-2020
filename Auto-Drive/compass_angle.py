#!/usr/bin/python3

import serial
import time

port = serial.Serial("dev/serial0", baudrate=19200,timeout=3.0)

while True:
    port.write("\r\nSay something:")
    rcv = port.read(10)
    port.write("\r\nYou sent:" +repr(rcv))