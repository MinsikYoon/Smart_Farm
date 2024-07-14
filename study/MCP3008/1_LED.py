import spidev
import time

delay = 0.5 #센서 측정 간격

#mcp3008 채널 설정
ldr_channel = 0


# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작(bus,device)
spi.open(0,0)

# SPI 통신 속도 설정
spi.max_speed_hz = 1000000


def readadc(adcnum):
    if adcnum > 7 or adcnum<0:
        return -1
    #xfer2 :SPI통신 전송 함수 r:buffer 저장값
    r = spi.xfer2([1,8+adcnum <<4 ,0])
    # 첫번째 ,2번째 저장값을 10bit 데이터로 합침
    data = ((r[1] & 3)<<8) +r[2]
    return data

while True:
    ldr_value = readadc(ldr_channel)
    print("LDR Value: %d"% ldr_value)
    time.sleep(delay)
