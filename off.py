#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
sys.path.append('./lib')
import random
import lightlib as ll
import pinconfig as cfg

GPIO.setmode(GPIO.BCM)

ll.initialize()

ll.cleanup()
