import spidev
import time
import SmartFarm
import RPi.GPIO as GPIO
delay = 0.5 #센서 측정 간격

GPIO.setmode(GPIO.BCM)

#mcp3008 채널 설정
light_sensor_channel = 0
water_sensor_channel = 1

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작(bus,device)
spi.open(0,0)

# SPI 통신 속도 설정
spi.max_speed_hz = 1000000


def read_light(light_channel):
    r = spi.xfer2([1,8+light_channel <<4 ,0])
    data = ((r[1] & 3)<<8) +r[2]
    print(data)
    SmartFarm.LED_Control(data)

def readChannel(water_channel):
    val = spi.xfer2([1,(8+water_channel)<<4,0])
    data = ((val[1]&3 << 8 )+ val[2])
    print(data,"/",convertPercent(data),"%")
    SmartFarm.Water_Moter_Control(convertPercent(data))
def convertPercent(data):
    return 100.0-round(((data*100)/float(1023)),1)



while True:
    try:
        read_light(light_sensor_channel)
        readChannel(water_sensor_channel)
        time.sleep(delay)

    except KeyboardInterrupt:
        GPIO.cleanup()
        break