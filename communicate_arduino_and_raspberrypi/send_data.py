# !/usr/bin/python

import serial

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)

while True:
    print(ser.readline())

############################################################################

# !/usr/bin/python
import serial
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)
""" Often the python program will read data from the serial port quicker than it can be received. 
The line I have added checks to see if there is and data first before trying to read it.
Note: in_waiting works with PySerial version 3.0 and greater. For older versions use ser.inWaiting()"""
while True:
    # if ser.in_waiting > 0:
    print(ser.readline())
