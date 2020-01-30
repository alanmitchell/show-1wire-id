# show-1wire-id
Displays the ID of a Maxim 1-wire Sensor on a Rasperry Pi with OLED display.

Designed to work with the [Adafruit PiOLED 128x32 display](https://www.adafruit.com/product/3527).

To read the IDs from the 1-wire sensors, [digitemp](https://www.digitemp.com/) must be installed, and a 
1-wire master must be installed on a USB serial port.  Modify the digitemp command in the source code as
necessary to support the 1-wire master you are using.

On the Pi for proper operation of digitemp and other 1-wire programs, it is important to Blacklist the 
DS2490, DS9490r, and wire modules as described [here](https://www.raspberrypi.org/forums/viewtopic.php?t=27379).
