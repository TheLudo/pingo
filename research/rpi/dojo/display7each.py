#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pi Cobbler Numbering

                         3v3
bread | 25 23 21 ... 5 3 1 |
board | 26 24 22 ... 6 4 2 |
                     G 5 5v
                     N v 
                     D    
"""

import atexit
import time
import RPi.GPIO as GPIO

# make sure GPIO.cleanup is called when script exits
atexit.register(GPIO.cleanup)

# use physical pin numbering
GPIO.setmode(GPIO.BOARD)

#       A   B   C   D   E   F   G  dp
PINS = [11, 7, 16, 18, 22, 13, 15, 12]

for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)

for pin in PINS:
    GPIO.output(pin, 1)
    time.sleep(.5)
    GPIO.output(pin, 0)
