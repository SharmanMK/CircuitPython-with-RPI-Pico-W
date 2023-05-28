import time
import board
import busio
import adafruit_dht
from grove_lcd import Grove_LCD_I2C

# DHT11 sensor pin
DHT_PIN = board.GP7

# LCD I2C address
LCD_ADDRESS = 0x3E

# Initialize I2C
i2c = busio.I2C(sda=board.GP26, scl=board.GP27)

# Initialize LCD
lcd = Grove_LCD_I2C(i2c, LCD_ADDRESS)

# Initialize DHT11 sensor
dht = adafruit_dht.DHT11(DHT_PIN)

# Main loop
while True:
    try:
        # Read temperature and humidity from DHT11 sensor
        temperature = dht.temperature
        humidity = dht.humidity

        # Clear LCD display
        lcd.clear()

        # Display temperature and humidity on LCD
        lcd.print("T/H: ")
        lcd.print(str(temperature) + "C / ")
        lcd.print(str(humidity) + "%")

    except RuntimeError as e:
        # Error occurred, display error message on LCD
        lcd.clear()
        lcd.print("Error: " + str(e))

    # Delay between readings
    time.sleep(2)
