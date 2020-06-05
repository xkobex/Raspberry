import time
 
# Import the MCP4725 module.
import Adafruit_MCP4725
 
# Create a DAC instance.
#dac = Adafruit_MCP4725.MCP4725()
 
# Note you can change the I2C address from its default (0x62), and/or the I2C
# bus by passing in these optional parameters:
dac = Adafruit_MCP4725.MCP4725(address=0x60, busnum=0)
 
# Loop forever alternating through different voltage outputs.
print('Press Ctrl-C to quit...')
while True:
    for x in range(0,4097,150):
        
        print(x)
        dac.set_voltage(x)
        #lcd.cursor_pos = (0,0)
        print("DAC Value: " + str(x))
        voltage = x/4096.0*5.0
        print("\nAnalogVolt: %.2f" % voltage)
        time.sleep(2)
        #lcd.clear()