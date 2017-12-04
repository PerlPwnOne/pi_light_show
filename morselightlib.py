#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# This is hard-coded so I don't have to pass it every time. A true lib would expect the pinList to be passed :)
pinList = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 21, 20]


def dot(socketnum, delay):
    GPIO.output(socketnum, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(socketnum, GPIO.HIGH)

def dash(socketnum, delay):
    GPIO.output(socketnum, GPIO.LOW)
    time.sleep(delay * 3)
    GPIO.output(socketnum, GPIO.HIGH)

def space(socketnum, delay):
    GPIO.output(socketnum, GPIO.HIGH)
    time.sleep(delay * 4) # space between words is 7, but we are already doing 3 after each letter


def morse_parse_string(socketnum, string, delay):
    socketnum = pinList[socketnum-1]
    for char in string:
        l = char.lower()
        print l
        if l == " ":
            space(socketnum, delay)
        if l == "a":
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "b":
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "c":
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "d":
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "e":
            dot(socketnum, delay)
        if l == "f":
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "g":
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "h":
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "i":
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "j":
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "k":
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "l":
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "m":
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "n":
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "o":
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "p":
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay
        if l == "q":
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "r":
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "s":
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
        if l == "t":
            dash(socketnum, delay)
        if l == "u":
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "v":
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "w":
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "x":
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "y":
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
        if l == "z":
            dash(socketnum, delay)
            time.sleep(delay)
            dash(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)
            time.sleep(delay)
            dot(socketnum, delay)

        time.sleep(delay *3) # 3 units of time between letters
