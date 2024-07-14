import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
print("DISTANCE MEASUREMENT IN PROGRESS")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print("waiting for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO.input(ECHO) == 1:
            stop = time.time()

        check_time = stop -start
        distance = check_time *34300/2
        print("distance : %.1f cm"% distance)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup() 