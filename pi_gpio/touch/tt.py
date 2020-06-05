#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import Adafruit_DHT

from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

import RPi_I2C_driver

def clock(seg, seconds):
   
    now = datetime.now()
    seg.text = now.strftime("%Y.%m.%d")
    mylcd.lcd_display_string("LEO's ", 1)
    mylcd.lcd_display_string("   Raspberry Pi", 2)
    h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT11_GPIO_PIN)
    time.sleep(5)
    mylcd.lcd_clear()
    if h is not None and t is not None:
            print('TEMP={0:0.1f}C Hum={1:0.1f}%'.format(t, h))
            mylcd.lcd_display_string_pos("Temp = "+format(t)+ " C",1,0) # row 1, column 1
            mylcd.lcd_display_string_pos("Hum  = "+format(h)+" %",2,0) # row 1, column 1
    else:
            print('FAIL')
            
    #mylcd.backlight(0)
#    Display current time on device.
    interval = 0.5
    for i in range(int(seconds / interval)):

        now = datetime.now()
        seg.text = now.strftime("%H-%M-%S")

        # calculate blinking dot
        if i % 2 == 0:
            seg.text = now.strftime("%H-%M-%S")
        else:
            seg.text = now.strftime("%H %M %S")

        time.sleep(interval)
 

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 37 (GPIO26) as an input
buttonPin = 37
print ("Setup Pin 37")
GPIO.setup(buttonPin, GPIO.IN)
prev_input = 0

#max7219
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
seg = sevensegment(device)

#LCD
mylcd = RPi_I2C_driver.lcd()

#DHT11
DHT11_GPIO_PIN = 4


while True:
  #take a reading
  input = GPIO.input(buttonPin)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
    clock(seg, seconds=20)
    mylcd.lcd_clear()
    mylcd.backlight(0)
    seg.text = ""
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
