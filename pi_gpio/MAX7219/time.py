
import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

def clock(seg, seconds):

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

def main():
    # create seven segment device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)
    now = datetime.now()
    seg.text = now.strftime("%Y.%m.%d")
    time.sleep(5)

    # Digit futzing
    clock(seg, seconds=20)


if __name__ == '__main__':
    main()
