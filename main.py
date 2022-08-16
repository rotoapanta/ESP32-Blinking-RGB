#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = main.py
__author__ = rotoapanta "Roberto Toapanta"
__copyright__ = "Copyright 2022, BitTech"
__credits__ = ["Roberto Toapanta, Giovanny Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__date__ = 16/8/22 10:58
__description__ = "This project is based on an ESP32-S2 general-purpose development board with
                    micropython that allows the rgb led to blink."
__information__ : 
"""

from machine import Pin
import neopixel
import time
 
pixels = neopixel.NeoPixel(Pin(18, Pin.OUT), 1)  # create output pin on GPIO18
while True:
    pixels[0] = (0xff, 0x00, 0x00)   # red color
    pixels.write()
    time.sleep(1)
    pixels[0] = (0x00, 0xff, 0x00)   # green color
    pixels.write()
    time.sleep(1)
    pixels[0] = (0x00, 0x00, 0xff)   # blue color
    pixels.write()
    time.sleep(1)
