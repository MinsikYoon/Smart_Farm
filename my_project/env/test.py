import RPi.GPIO as GPIO

Relay_Fan = 23   #팬
Relay_Water_Moter = 27   #펌프기
Relay_Huminity = 25  #가습기
Relay_LED = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_Fan,GPIO.OUT)
GPIO.setup(Relay_Water_Moter,GPIO.OUT)
GPIO.setup(Relay_Huminity,GPIO.OUT)
GPIO.setup(Relay_LED,GPIO.OUT)

#while True:
    # GPIO.output(Relay_Fan,1)
    #GPIO.output(Relay_Water_Moter,1)
    #GPIO.output(Relay_Huminity,1)
    # GPIO.output(Relay_LED,1)
    # time.sleep(3)

    # GPIO.output(Relay_Fan,0)
    #GPIO.output(Relay_Water_Moter,0)
    # GPIO.output(Relay_Huminity,0)
    # GPIO.output(Relay_LED,0)
    # time.sleep(3)

GPIO.cleanup()
# 

#     
    
#     
#     GPIO.cleanup()


