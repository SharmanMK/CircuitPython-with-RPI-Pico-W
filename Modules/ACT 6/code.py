import time
import board
import busio
import adafruit_dht
from digitalio import DigitalInOut, Direction, Pull
from grove_lcd import Grove_LCD_I2C
import neopixel

# DHT11 sensor pin
DHT_PIN = board.GP7

# Motor pins
MOTOR_PIN_A = board.GP4
MOTOR_PIN_B = board.GP5

# LCD I2C address
LCD_ADDRESS = 0x3E

# Initialize I2C
i2c = busio.I2C(sda=board.GP26, scl=board.GP27)

# Initialize LCD
lcd = Grove_LCD_I2C(i2c, LCD_ADDRESS)

# Initialize DHT11 sensor
dht = adafruit_dht.DHT11(DHT_PIN)

# Motor states
MOTOR_OFF = 0
MOTOR_ON = 1

# Initialize motor
motor_a = DigitalInOut(MOTOR_PIN_A)
motor_b = DigitalInOut(MOTOR_PIN_B)
motor_a.direction = Direction.OUTPUT
motor_b.direction = Direction.OUTPUT
motor_state = MOTOR_OFF

# NeoPixel
neopixel_pin = board.GP28
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

def toggle_motor():
    global motor_state
    motor_state = not motor_state
    if motor_state == MOTOR_ON:
        motor_a.value = True
        motor_b.value = False
        lcd.cursor_position(0, 1)
        lcd.print("Motor Stats: ON")
    else:
        motor_a.value = False
        motor_b.value = False
        lcd.cursor_position(0, 1)
        lcd.print("Motor Stats: OFF")

# Main loop
while True:
    try:
        # Read temperature from DHT11 sensor
        temperature = dht.temperature

        print("Temperature: {:.2f} °C".format(temperature))

        # Clear LCD display
        lcd.clear()

        # Display temperature on LCD
        lcd.cursor_position(0, 0)
        lcd.print("T: ")
        lcd.print(str(temperature) + "C")

        if temperature > 29:
            # Run the motor and set neopixel color to red
            pixels.fill((255, 0, 0))  # Hot color (red)
            toggle_motor()
        else:
            # Stop the motor and set neopixel color to blue
            pixels.fill((0, 0, 255))  # Cold color (blue)
            toggle_motor()

    except RuntimeError as e:
        # Error occurred, display error message on LCD
        lcd.clear()
        lcd.cursor_position(0, 0)
        lcd.print("DHT11 Error")
        print("Error:", e)

    # Delay between readings
    time.sleep(2)
