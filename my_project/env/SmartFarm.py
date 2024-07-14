import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD

Relay_Fan = 23  
Relay_Huminity = 25 
Relay_LED = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_Fan,GPIO.OUT)
GPIO.setup(Relay_Huminity,GPIO.OUT)
GPIO.setup(Relay_LED,GPIO.OUT)

lcd = CharLCD(i2c_expander='PCF8574', address=0x26)

def Fan_Control(Temp):
    if Temp > 24:
        Fan_ON_OFF = 1
        Switch_ON_OFF = "ON"
        GPIO.output(Relay_Fan,Fan_ON_OFF)
    else:
        Fan_ON_OFF = 0
        Switch_ON_OFF = "OFF"
        GPIO.output(Relay_Fan,Fan_ON_OFF)
    lcd.clear()
    lcd.cursor_pos=(0,0)
    lcd.write_string("T: "+ str(Temp)+"C")
    lcd.cursor_pos=(1,0)
    lcd.write_string("Fan:"+Switch_ON_OFF)

def Humidity_Control(Humi):
    if Humi < 45:
        Humi_ON_OFF = 1
        Switch_ON_OFF = "ON"
        GPIO.output(Relay_Huminity,Humi_ON_OFF)
    else:
        Humi_ON_OFF = 0
        Switch_ON_OFF = "OFF"
        GPIO.output(Relay_Huminity,Humi_ON_OFF)
    lcd.cursor_pos=(0,8)
    lcd.write_string(" H: "+str(Humi)+"%")
    lcd.cursor_pos=(1,9)
    lcd.write_string("Hum:"+Switch_ON_OFF)

def LED_Control(Light):
    if Light < 100:
        LED_ON_OFF = 1
        GPIO.output(Relay_LED , LED_ON_OFF)
    else:
        LED_ON_OFF = 0
        GPIO.output(Relay_LED,LED_ON_OFF)

    
