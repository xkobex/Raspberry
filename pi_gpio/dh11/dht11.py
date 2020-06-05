import time
import Adafruit_DHT
 
GPIO_PIN = 4
 
try:
    print('Press Ctrl-C exit')
    while True:
        h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, GPIO_PIN)
        if h is not None and t is not None:
            print('TEMP={0:0.1f}C BB={1:0.1f}%'.format(t, h))
        else:
            print('FAIL')
        time.sleep(10)
except KeyboardInterrupt:
    print('EXIT')

