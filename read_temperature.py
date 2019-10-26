#!/usr/bin/env python
import ADC0832
import time
import math


def init():
    ADC0832.setup()


def loop():
    while True:
        analogVal = ADC0832.getResult()
        # print analogVal
        Vr = 5 * float(analogVal) / 255
        # print Vr
        Rt = 10000 * Vr / (5 - Vr)
        # print Rt
        temp = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))
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
