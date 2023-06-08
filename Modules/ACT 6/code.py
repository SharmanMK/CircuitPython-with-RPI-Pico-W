import time
import board
import busio
import adafruit_dht
from digitalio import DigitalInOut, Direction, Pull
from grove_lcd import Grove_LCD_I2C
import neopixel
import pwmio
from adafruit_motor import motor as af_motor

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

# Motor pins
MOTOR_PIN_A_FWD = board.GP4
MOTOR_PIN_A_BWD = board.GP5

# Initialize DHT11 sensor
dht = adafruit_dht.DHT11(DHT_PIN)

# Initialize motor
pwm_a_fwd = pwmio.PWMOut(MOTOR_PIN_A_FWD, frequency=10000)
pwm_a_bwd = pwmio.PWMOut(MOTOR_PIN_A_BWD, frequency=10000)
motor1 = af_motor.DCMotor(pwm_a_fwd, pwm_a_bwd)

# NeoPixel
neopixel_pin = board.GP28
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Button pins
BUTTON_INC_PIN = board.GP22
BUTTON_DEC_PIN = board.GP20

# Initialize buttons
button_inc = DigitalInOut(BUTTON_INC_PIN)
button_inc.direction = Direction.INPUT
button_inc.pull = Pull.UP
button_inc_state = False

button_dec = DigitalInOut(BUTTON_DEC_PIN)
button_dec.direction = Direction.INPUT
button_dec.pull = Pull.UP
button_dec_state = False

# Motor speed
speed = 1.0

# Initialize motor state
motor_state = False

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
        lcd.print(str(temperature) + "*C")

        if temperature > 30:
            # Run the motor and set neopixel color to red
            if not motor_state:
                motor1.throttle = 1.0
                motor_state = True
                pixels.fill((255, 0, 0))  # Hot color (red)
        else:
            # Stop the motor and set neopixel color to blue
            if motor_state:
                motor1.throttle = 0
                motor_state = False
                pixels.fill((0, 0, 255)) # Cold color (blue)

        # Check if accelerate button is pressed
        if not button_inc.value:
            motor_state = True
            speed += 0.1
            if speed > 1.0:
                speed = 1.0

        # Check if decelerate button is pressed
        if not button_dec.value:
            motor_state = True
            speed -= 0.1
            if speed < 0.0:
                speed = 0.0

        # Update motor state
        if motor_state:
            motor1.throttle = speed
        else:
            motor1.throttle = 0

        time.sleep(0.05)

        # Display motor speed on LCD
        lcd.cursor_position(0, 1)
        lcd.print("Speed: {:.2f}".format(speed))

    except RuntimeError as e:
        # Error occurred, display error message on LCD
        lcd.clear()
        lcd.cursor_position(0, 0)
        lcd.print("DHT11 Error")
        print("Error:", e)

    # Delay between readings
    time.sleep(2)

