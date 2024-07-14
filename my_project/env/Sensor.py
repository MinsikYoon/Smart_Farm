import time
import adafruit_dht
import board
import RPi.GPIO as GPIO
import SmartFarm
import spidev

dhtDevice = adafruit_dht.DHT11(board.D17)   
light_sensor_channel = 0    
water_sensor_channel = 1
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def adafruit_dht_Sensor():
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {}*C    Humidity: {}% ".format(temperature_c, humidity))
        SmartFarm.Fan_Control(temperature_c)
        SmartFarm.Humidity_Control(humidity)
    except RuntimeError as error:
        print("runtime")
        pass
    except Exception as error:
        print("exception")
        pass

def Light_Channel(light_channel):
    r = spi.xfer2([1,8+light_channel <<4 ,0])
    data = ((r[1] & 3)<<8) +r[2]
    print(data)
    SmartFarm.LED_Control(data)

def Water_Channel(water_channel):
    val = spi.xfer2([1,(8+water_channel)<<4,0])
    data = ((val[1]&3 << 8 )+ val[2])
    print(data,"/",convertPercent(data),"%")
    SmartFarm.Water_Moter_Control(convertPercent(data))
def convertPercent(data):
    return 100.0-round(((data*100)/float(1023)),1)

while True:
    try:
        adafruit_dht_Sensor()
        Light_Channel(light_sensor_channel)
        print()
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break



