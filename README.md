pi_light_show
=============

### Purpose
Automating the functionality of using a raspberry pi to control lights

### References
Great reference for more information on setting up / configuring your rPi and GPIO
 - [opensourceforu](https://opensourceforu.com/2017/07/introduction-raspberry-pi-gpio-programming-using-python/)


### IMPORTANT:
 - update lib/pinconfig.py with YOUR pin configuration from your RPi as it is used by:
 * lightlib.py
 * morselightlib.py
<br>
<br>Example crontab:
<br>#Christmas Lights 2017-12-19
<br>#on at 5pm
<br>0 17 * * * /home/pi/gitroot/pi_light_show/rob_example.py
<br>#kill script at 1AM
<br>0 1 * * * killall rob_example.py
<br>#ensure all off at 1:05AM
<br>5 1 * * * /home/pi/gitroot/pi_light_show/off.py

