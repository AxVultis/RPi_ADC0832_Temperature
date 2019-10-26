#!/usr/bin/env python
import ADC0832
import time
import math


def init():
    ADC0832.setup()


def loop():
    while True:
        analog_val = ADC0832.get_result()
        voltage = 5 * float(analog_val) / 255
        rt = 10000 * voltage / (5 - voltage)
        temp = 1 / (((math.log(rt / 10000)) / 3950) + (1 / (273.15 + 25)))
        temp = temp - 273.15
        print('temperature = %.2f C' % temp)
        time.sleep(0.2)


if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt:
        ADC0832.destroy()
        print('The end !')
