import cv2
import RPi.GPIO as GPIO
import time
import numpy as np

record_on = False
def button_callback(channel):
    global record_on
    record_on = not record_on
    print("button pressed")

button_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(button_pin,GPIO.RISING,callback = button_callback,bouncetime = 300)

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('Record.mp4',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('frame',frame)

        if record_on == True:
            out.write(frame)
    else:
        print('no frame')
        break
    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()