#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#GPIOの定義
SWITCH = 4
LED = 18

#GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

#スイッチの状態を監視し、スイッチONの間、LEDを点灯させる
GPIO.output(LED, GPIO.LOW)
try:
    while True:
        v = GPIO.input(SWITCH)
        if v == GPIO.HIGH:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
            
