#!/usr/bin/env python3
"""Displays the 1-wire sensor ID on a Raspberry Pi OLED display.
Meant to only display the ID on one connected sensor.
"""
import subprocess
from glob import glob
import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Load a font
font = ImageFont.truetype('DejaVuSans.ttf', 17)

def text(line1, line2):
    # Clear display.
    oled.fill(0)
    oled.show()

    # Create blank image for drawing.
    image = Image.new('1', (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw the text
    draw.text((0, 0), line1, font=font, fill=255)
    draw.text((0, 16), line2, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()

def error_display():
    """What to display when no Master adapter is connected or
    no sensors are connected.
    """
    text('   No', 'Device')
    
while True:
    
    # Find all the FTDI serial ports.  We assume the adapter is on the
    # first one.
    ports = glob('/dev/serial/by-id/*FTDI*')

    try:
        proc = subprocess.run(
            f'/usr/bin/digitemp_DS9097U -i -s {ports[0]}', 
            check=True, 
            shell=True, 
            stdout=subprocess.PIPE, 
            universal_newlines=True,
            )
        output = proc.stdout
        if 'ROM #0' in output:
            # There is a sensor connected.  Read the ID from the last line.
            last = output.splitlines()[-1]
            s = last.split(':')[-1].strip()
            s = s[:-2]
            line1 = f'{s[:2]}.  {s[2:4]} {s[4:6]} {s[6:8]}'
            line2 = f'{s[8:10]} {s[10:12]} {s[12:14]}'
            text(line1, line2)
        else:
            error_display()
    except:
        error_display()

    time.sleep(1)
