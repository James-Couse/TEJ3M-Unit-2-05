"""
Created by: James Couse
Created on: Nov 21 2023
This module rotates a servo back and forth.
"""

import time
import board
import pwmio
from adafruit_motor import servo

# Sets the output to Pin GP27 or A1
pwm = pwmio.PWMOut(board.A1, frequency=50)

# Creates a servo object, sets it to a variable name
ServoNumber1 = servo.Servo(pwm)

# Loops the servo between 0 and 180 degrees
while True:
    ServoNumber1 = 0
    time.sleep(2.0)
    ServoNumber1 = 180
    time.sleep(2.0)
    
    