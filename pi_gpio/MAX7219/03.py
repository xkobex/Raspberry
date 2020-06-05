#!/usr/bin/env python
 
import max7219.led as led
import time
 
device = led.sevensegment(cascaded=1)
for x in range(1, 100):
    device.write_number(deviceId=0, value=x)
    time.sleep(0.05)
