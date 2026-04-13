import RPi.GPIO as GPIO
import time

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("土壤湿润 ✅")
    else:
        print("土壤干燥 ⚠️ 需要浇水！")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
