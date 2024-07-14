import spidev
import time

delay = 1

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def readChannel(channel):
    val = spi.xfer2([1,(8+channel)<<4,0])
    data = ((val[1]&3 << 8 )+ val[2])
    return data
def convertPercent(data):
    return 100.0-round(((data*100)/float(1023)),1)

try:
    while True:
        val = readChannel(1)
        if (val !=0):
            print(val,"/",convertPercent(val),"%")
        time.sleep(delay)

except KeyboardInterrupt:
    spi.close()
    print("keyboard interrupt")
