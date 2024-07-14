import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 4

GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)

try:
    for i in range(0,10):
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
 
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()