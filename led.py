#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = led.py
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
from time import sleep

#El Pin del led es el 2 que corresponde al GPI17 Y 16

ledpin=17
ledpin2=16 
pin = Pin(ledpin, Pin.OUT)
pin2 = Pin(ledpin2, Pin.OUT)
while True:
  pin.value(1)
  pin2.off()
  sleep(1)
  pin.value(0)
  pin2.on()
  sleep(1)
