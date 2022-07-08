


from machine import SPI,Pin         #从machine模块导入I2C、Pin子模块
from ssd1306 import SSD1306_SPI
from time    import sleep
import framebuf

spi = SPI(0, sck=Pin(2), mosi=Pin(3)) 
oled = SSD1306_SPI(128, 32, spi, res=Pin(0), dc=Pin(4), cs=Pin(1))
second=0
minute=22
hour  =11

while True:
    for i in range(1,5):
        a=i*32
        oled.text("stM32L031K6",  10, 0)
        print(a)
        oled.text(f"time {hour}:{minute} {second}",  0, 8)
        oled.text("temp:26.5'C",  0, 17)
        oled.rect(118,0,10,10,second%3)
        oled.fill_rect(0,28,a,5,1)
        oled.scroll(0,0)
        oled.show()
        sleep(1)
        oled.fill(0)
        oled.show()
        second+=1
        if   second==60:
             second=0
             minute+=1
        elif minute==60:
             minute=0
             hour+=1
        elif hour==24:
             hour=0
    
       
    
    
    
   
 
