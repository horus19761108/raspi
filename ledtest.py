#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#GPIOのセットアップ
GPIO.setmode(GPIO.BCM)		# GPIOモードのセット
GPIO.setup(4, GPIO.OUT)	 	# GPIO4を出力に使用(緑色LED用)
GPIO.setup(17, GPIO.OUT)	# GPIO17を出力に使用(黄色LED用)
GPIO.setup(27, GPIO.OUT)	# GPIO27を出力に使用(赤色LED用)

#LEDを順番に光らせる
i=0
pin=[4, 17, 27]	# GPIOのIDを配列にセット
while i<50:
	# 緑->黄色->赤の順にLEDを点灯させる
	for p in pin:
		GPIO.output(p, GPIO.HIGH)	# HIGHで電圧がかかる(LEDが光る)
		time.sleep(0.1)
		GPIO.output(p, GPIO.LOW)	# LOWで電圧がなくなる(LEDが消える)
	i += 1

GPIO.cleanup()	# 使ったGPIOの解放

