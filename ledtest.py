#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#GPIOのセットアップ
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

#LEDを順番に光らせる
i=0
pin=[4, 17, 27]
while i<50:
	for p in pin:
		GPIO.output(p, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(p, GPIO.LOW)
	i += 1

GPIO.cleanup()

