# pi_light_show
Automating the functionality of using a raspberry pi to control lights

IMPORTANT:
update the pinconfig.py with YOUR pin configuration from your RPi as it is used by:
<br>    lightlib.py
<br>    morselightlib.py
<p>
<p>Example crontab:
<p>#Christmas Lights 2017-12-19
<p>#on at 5pm
<p>0 17 * * * /home/pi/gitroot/pi_light_show/rob_example.py
<p>#kill script at 1AM
<p>0 1 * * * killall rob_example.py
<p>#ensure all off at 1:05AM
<p>5 1 * * * /home/pi/gitroot/pi_light_show/off.py

