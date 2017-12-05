#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import pygame
import random

GPIO.setmode(GPIO.BCM)

# Your GPIO pin configuration layout

pinList = [7, 8, 25, 24, 23, 2, 3, 4, 17, 27, 22, 10, 9, 14, 15, 18]

# loop through pins and set mode and state to 'HIGH' or off

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

#setup the pygame.music play for the main loop
 
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Carol_Of_The_Bells.mp3')
pygame.mixer.music.play()

# time to sleep between operations in the main loop

SleepTimeL = 2.5

# main loop

try:
    while True:
        i = random.sample([7, 8, 25, 24, 23, 2, 3, 4], 5)
        GPIO.output(i, GPIO.LOW)
        time.sleep(SleepTimeL);
        GPIO.output(i, GPIO.HIGH)

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
GPIO.cleanup()
