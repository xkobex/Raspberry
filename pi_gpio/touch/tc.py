#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 37 (GPIO26) as an input
buttonPin = 37
print "Setup Pin 37"
GPIO.setup(buttonPin, GPIO.IN)
prev_input = 0
cmd = "python3.7 /home/pi/pi_gpio/MAX7219/time.py"
while True:
  #take a reading
  input = GPIO.input(buttonPin)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
    os.system(cmd)
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
