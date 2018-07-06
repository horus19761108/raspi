#!/usr/bin/env python3

#----------#
# 暗くなったらLEDを点灯する
# ※分圧回路を使ってセンサを読む
#----------#

import wiringpi as pi, time

led_pin = 23 # LED
cds_pin = 17 # CDS
pi.wiringPiSetupGpio()
pi.pinMode( led_pin , 1 ) # led_pinをOutputに設定
pi.pinMode( cds_pin , 0 ) # cds_pinをInputに設定

while True:
	if ( pi.digitalRead(cds_pin) == 1 ): # 明るい時(CDSの抵抗が小さい時)
		pi.digitalWrite( led_pin, 0 ) # LEDが消灯
	else:
		pi.digitalWrite( led_pin, 1 ) # LEDが点灯

