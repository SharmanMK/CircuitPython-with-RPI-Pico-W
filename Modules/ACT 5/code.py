import board
import time
import busio
import digitalio
import adafruit_dht
import lcd
import i2c_pcf8574_interface

# DHT22
dht22 = adafruit_dht.DHT22(board.GP7)

# Serial LCD
i2c = busio.I2C(scl=board.GP27, sda=board.GP26)
address = 0x3E
i2c = i2c_pcf8574_interface.I2CPCF8574Interface(i2c, address)
display = lcd.LCD(i2c, num_rows=2, num_cols=16)
display.set_backlight(True)
display.set_display_enabled(True)

def read_dht22():
    try:
        temperature = dht22.temperature
        humidity = dht22.humidity
        
        print("Temperature: {:.2f} °C, Humidity: {:.2f} %RH ".format(temperature, humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        display.clear()
        display.set_cursor_pos(0, 0)
        display.print("DHT Sensor Not Found!")
    except Exception as error:
        dht22.exit()
        raise error
        display.clear()
        display.set_cursor_pos(0, 0)
        display.print("Error")
    
    return [temperature, humidity]

while True:
    datadht22 = read_dht22()
    print("Temperature: {:.2f} °C, Humidity: {:.2f} %RH ".format(datadht22[0], datadht22[1]))
    display.clear()
    display.set_cursor_pos(0, 0)
    display.print("Temp(C) = {:.2f}".format(datadht22[0]))
    display.set_cursor_pos(1, 0)
    display.print("Humi(%) = {:.2f}".format(datadht22[1]))
    time.sleep(2)
