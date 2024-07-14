import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
Relay_Water_Moter = 27

GPIO.setup(Relay_Water_Moter,GPIO.OUT)

GPIO.output(Relay_Water_Moter,1)
time.sleep(60)
GPIO.output(Relay_Water_Moter,0)
