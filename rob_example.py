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

#because I don't want to type " " every time i use on/off
on = "on"
off = "off"

def evens(st):
    ll.two(st)
    ll.four(st)
    ll.six(st)
    ll.eight(st)
    ll.ten(st)
    ll.twelve(st)
    ll.fourteen(st)
    ll.sixteen(st)

def odds(st):
    ll.one(st)
    ll.three(st)
    ll.five(st)
    ll.seven(st)
    ll.nine(st)
    ll.eleven(st)
    ll.thirteen(st)
    ll.fifteen(st)

try:
    while True:
        print "All On"
        ll.all(on)
        time.sleep(5)
        print "All off"
        ll.all(off)
        time.sleep(1)
        print "All Random"
        ll.allrando(15, 1, 7)
        for i in range(5):
            print "Odds on"
            odds(on)
            time.sleep(3)
            odds(off)
            print "Evens on"
            evens(on)
            time.sleep(3)
            evens(off)

except KeyboardInterrupt:
    print "Quitting"

ll.cleanup()
