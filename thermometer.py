#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import datetime as dt
import re

# GPIOの定義
LED = 18

# GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def get_temp(path):
        f = open(path,'r')
        data = f.readlines()
        f.close
        for str in data:
            temp = re.search('t=(?P<value>[0-9]{5})',str)
            if temp:
                r_value = temp.group('value')
        return(r_value)

if __name__ == '__main__':
    # 温度センサの情報
    tmeter_path = '/sys/bus/w1/devices/28-0000086d6a14/w1_slave'

    try:
        o_status = "Low"
        n_status = "Low"
        GPIO.output(LED,GPIO.LOW)
        while True:
            today = dt.datetime.now()
            # 温度計測
            t_value = get_temp(tmeter_path)
            if int(t_value) >= 27000:
                n_status = "High"
            else:
                n_status = "Low"
            # LED点灯/消灯判定                
            if o_status == n_status:
                pass
            else:
                if n_status == "High":
                    GPIO.output(LED,GPIO.HIGH)
                else:
                    GPIO.output(LED,GPIO.LOW)
                o_status = n_status
            # 処理結果出力
            print(today.strftime("%H:%M:%S"),t_value,o_status)
            time.sleep(0.5) 
    except:
        GPIO.cleanup()
