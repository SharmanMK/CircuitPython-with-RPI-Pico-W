#Import necessary Libraries 

import time
import board
import digitalio
import busio
from grove_lcd import Grove_LCD_I2C

LCD_ADDR = 0x3E
i2c = busio.I2C(scl=board.GP27, sda= board.GP26)
lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

lcd.home()
lcd.print("Hello World!")
time.sleep(5)
lcd.clear()