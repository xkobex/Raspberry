


#!/usr/bin/env python
# File rpi_7219b.py
# http://www.bristolwatch.com/index.htm
# By Lewis Loflin - lewis@bvu.net
# Output time from system clock.
# http://www.bristolwatch.com/ele2/rpi_clock_max7219.htm

# Two bytes are shifted in first being address, second being data.
# Works the same as two 74165 SSRs in series or 16-bits.
# LD "pulseCS()" clocks 16-bit address/data into working registers.



# access to GPIO must be through root
import RPi.GPIO as GPIO
import time

LATCH = 11 # CS
CLK = 12
dataBit = 7 # DIN


GPIO.setup(LATCH, GPIO.OUT) # P0 
GPIO.setup(CLK, GPIO.OUT) # P1 
GPIO.setup(dataBit, GPIO.OUT) # P7


# Setup IO
GPIO.output(LATCH, 0)
GPIO.output(CLK, 0)


def pulseCLK():
    GPIO.output(CLK, 1)
    # time.sleep(.001) 
    GPIO.output(CLK, 0)
    return

def pulseCS():
    GPIO.output(LATCH, 1)
    # time.sleep(.001)
    GPIO.output(LATCH, 0)
    return
   
 

# shift byte into MAX7219
# MSB out first!
def ssrOut(value):
    for  x in range(0,8):
        temp = value & 0x80
        if temp == 0x80:
           GPIO.output(dataBit, 1) # data bit HIGH
        else:
           GPIO.output(dataBit, 0) # data bit LOW
        pulseCLK()
        value = value << 0x01 # shift left       
    return 



# initialize MAX7219 4 digits BCD
def initMAX7219():
    
    # set decode mode
    ssrOut(0x09) # address
    #	ssrOut(0x00); // no decode
    ssrOut(0xFF) # 4-bit BCD decode eight digits
    pulseCS();

    # set intensity
    ssrOut(0x0A) # address
    ssrOut(0x04) # 9/32
    pulseCS()

    # set scan limit 0-7
    ssrOut(0x0B); # address
    ssrOut(0x07) # 8 digits
    # ssrOut(0x03) # 4 digits
    pulseCS()


    # set for normal operation
    ssrOut(0x0C) # address
    # ssrOut(0x00); // Off
    ssrOut(0x01)  # On
    pulseCS()
	# clear to all 0s.
    for x in range(0,9):
        ssrOut(x)
        ssrOut(0)
        pulseCS()
    return


def writeMAX7219(data, location):
    ssrOut(location)
    ssrOut(data)
    pulseCS()
    return


def displayOff():
   # set for normal operation
    ssrOut(0x0C) # address
    ssrOut(0x00); # Off
    # ssrOut(0x01)  # On
    pulseCS()


def displayOn():
   # set for normal operation
    ssrOut(0x0C) # address
    # ssrOut(0x00); # Off
    ssrOut(0x01)  # On
    pulseCS()



initMAX7219()

# time returned as string
# But order is reversed relative to MAX7219.
str1 =  time.strftime("%H:%M:%S")
# str2 =  time.strftime("%d:%m:%Y")

print str1
# print len(str1) # 8

# x is digit position must be 1 to 8
# y is used for string pointer

while 1:
	y = 7
	for x in range(1, 9):
		if str1[y] == ":":
			# output "-"
			writeMAX7219(10, x)
			y = y - 1
			continue # back to if
		# convert y char to integer
		writeMAX7219(int(str1[y]), x)
		y = y - 1
	str1 =  time.strftime("%H:%M:%S")
	
	
	


print "Good by!"  
time.sleep(20)
displayOff()


exit
