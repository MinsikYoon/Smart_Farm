import RPi.GPIO as GPIO
import time

led_R = 20
led_Y = 21
sensor = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_R,GPIO.OUT)
GPIO.setup(led_Y,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)

print("PIR Ready.......")
time.sleep(5)

try:
    while True:
        if GPIO.input(sensor) == 1:
            GPIO.output(led_Y=1)
            GPIO.output(led_R,0)
            print("Motion Detected")

        if GPIO.input(sensor) == 0:
            GPIO.output(led_Y=0)
            GPIO.output(led_R,1)
            print("Motion Detected")

except KeyboardInterrupt:
    print("STOP")
    GPIO.cleanup()