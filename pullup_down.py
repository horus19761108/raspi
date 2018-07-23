#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

#繰り返して状態を確認
try:
	time.sleep(0.5)
	while True:
		if GPIO.input(4) == GPIO.HIGH:
			print("High")
		elif GPIO.input(4) == GPIO.LOW:
			print("Low")
		else:
			print("Error")
#CTRL+Cが押された時
except KeyboardInterrupt:
	GPIO.cleanup()
