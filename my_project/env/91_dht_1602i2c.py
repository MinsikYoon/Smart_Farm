
# i2cdetect -y 1
# git clone https://github.com/eleparts/RPi_I2C_LCD_driver
# chmod 777  start.sh
# ./start.sh

import time
import board
import adafruit_dht
import RPi_I2C_driver
from datetime import datetime

mylcd = RPi_I2C_driver.lcd()

mydht11 = adafruit_dht.DHT11(board.D27)

while True:
    try:
        temperature = mydht11.temperature
        humidity = mydht11.humidity
        print( "temp=%0.1f*c  humi=%0.1f" %(temperature, humidity) )
        
        now = datetime.now()
        #current = now.strftime("%Y.%m.%d %H:%M")
        current = now.strftime("%y%b%d %H:%M:%S")
        mylcd.lcd_display_string("{}".format(current),1)
        mylcd.lcd_display_string("T:{0:.1f}C,' ',H:{1:.1f}%".format(temperature,humidity),2)
    
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2)
        continue    
    except KeyboardInterrupt:
        pass
    except Exception as error:
        mydht11.exit()
        raise error
    
    time.sleep(2)
        
