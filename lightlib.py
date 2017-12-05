#!/usr/bin/python

import RPi.GPIO as GPIO
import random
import time
import pinconfig as cfg
# This is hard-coded so I don't have to pass it every time. A true lib would expect the pinList to be passed :)

pinList = cfg.pinList

# activate all our relays as OUT and turn the relay 'off'
def initialize():
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)    

# cleanup relays, sets them all to GPIO.IN
def cleanup():
    GPIO.cleanup()



# turn them all on/off
def all(opt):
    if opt == 'on':
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
    if opt == 'off':
        for i in pinList:
            GPIO.output(i, GPIO.HIGH)

# ok, randomize for sec=seconds with delay=delay between...
def allrando(sec, delay):
    t_end = time.time() + sec
    while time.time() < t_end:
        i = random.sample(pinList, 5)
        GPIO.output(i, GPIO.LOW)
        time.sleep(delay);
        GPIO.output(i, GPIO.HIGH)

# turn socket one on/off
def one(opt):
    if opt == 'on':
        GPIO.output(pinList[0], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[0], GPIO.HIGH)

# turn socket two on/off
def two(opt):
    if opt == 'on':
        GPIO.output(pinList[1], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[1], GPIO.HIGH)

# turn socket three on/off
def three(opt):
    if opt == 'on':
        GPIO.output(pinList[2], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[2], GPIO.HIGH)

# turn socket four on/off
def four(opt):
    if opt == 'on':
        GPIO.output(pinList[3], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[3], GPIO.HIGH)

# turn socket five on/off
def five(opt):
    if opt == 'on':
        GPIO.output(pinList[4], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[4], GPIO.HIGH)

# turn socket six on/off
def six(opt):
    if opt == 'on':
        GPIO.output(pinList[5], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[5], GPIO.HIGH)

# turn socket seven on/off
def seven(opt):
    if opt == 'on':
        GPIO.output(pinList[6], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[6], GPIO.HIGH)

# turn socket eight on/off
def eight(opt):
    if opt == 'on':
        GPIO.output(pinList[7], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[7], GPIO.HIGH)

# turn socket nine on/off
def nine(opt):
    if opt == 'on':
        GPIO.output(pinList[8], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[8], GPIO.HIGH)

# turn socket ten on/off
def ten(opt):
    if opt == 'on':
        GPIO.output(pinList[9], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[9], GPIO.HIGH)

# turn socket eleven on/off
def eleven(opt):
    if opt == 'on':
        GPIO.output(pinList[10], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[10], GPIO.HIGH)

# turn socket twelve on/off
def twelve(opt):
    if opt == 'on':
        GPIO.output(pinList[11], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[11], GPIO.HIGH)

# turn socket thirteen on/off
def thirteen(opt):
    if opt == 'on':
        GPIO.output(pinList[12], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[12], GPIO.HIGH)

# turn socket fourteen on/off
def fourteen(opt):
    if opt == 'on':
        GPIO.output(pinList[13], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[13], GPIO.HIGH)

# turn socket fifteen on/off
def fifteen(opt):
    if opt == 'on':
        GPIO.output(pinList[14], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[14], GPIO.HIGH)

# turn socket sixteen on/off
def sixteen(opt):
    if opt == 'on':
        GPIO.output(pinList[15], GPIO.LOW)
    if opt == 'off':
        GPIO.output(pinList[15], GPIO.HIGH)

