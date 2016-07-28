#!/usr/bin/python
import time

from gpio_96boards import GPIO

cnt = 0

GPIO_A = GPIO.gpio_id('GPIO_A')
pins = (
    (GPIO_A, 'in'),
)


def tilt(gpio):
    while True:
			pin_current = False
			pin_stat = gpio.digital_read(GPIO_A)
			#print "GPIO_A:%s" %pin_stat
			if pin_stat == 0:
				cnt += 1
			else:
				cnt = 0
			if cnt == 10:
				pin_current = not(pin_current)

			if pin_current:
				print "Push!"


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Blink LED on GPIO A (pin 23)')
    args = parser.parse_args()

    with GPIO(pins) as gpio:
        tilt(gpio)
