# pi_light_show
Automating the functionality of using a raspberry pi to control lights

IMPORTANT:
update the pinconfig.py with YOUR pin configuration from your RPi as it is used by:
    lightlib.py
    morselightlib.py
<p>
Example crontab:
#Christmas Lights 2017-12-19
#on at 5pm
0 17 * * * /home/pi/gitroot/pi_light_show/rob_example.py
#kill script at 1AM
0 1 * * * killall rob_example.py
#ensure all off at 1:05AM
5 1 * * * /home/pi/gitroot/pi_light_show/off.py

