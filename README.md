pi_light_show
=============

#### Purpose
Automating the functionality of using a raspberry pi to control lights

#### References
References for more information on setting up / configuring your rPi and GPIO
    - Quick Intro to using python + rPi [opensourceforu](https://opensourceforu.com/2017/07/introduction-raspberry-pi-gpio-programming-using-python/)
    - [Wiring Pi](http://wiringpi.com)

#### IMPORTANT
update lib/pinconfig.py with YOUR pin configuration from your RPi as it is used by:
    - lightlib.py
    - morselightlib.py

#### Usage
Currently just writing a script that you create that pulls from the lib.
Future plans:
    - ./pi_light_show -text <path/to/file/with/triggers>
    - ./pi_light_show -playlist </path/to/music_file(s)>

#### Example crontab entry:
    #Christmas Lights 2017-12-19
    #on at 5pm
    0 17 * * * /home/pi/gitroot/pi_light_show/rob_example.py
    #kill script at 1AM
    0 1 * * * killall rob_example.py
    #ensure all off at 1:05AM
    5 1 * * * /home/pi/gitroot/pi_light_show/off.py
