import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from grove_lcd import Grove_LCD_I2C

# GPIO pin assignments
BUTTON_PIN = board.GP21
MOTOR_PIN_A = board.GP4
MOTOR_PIN_B = board.GP5

# LCD I2C address
LCD_ADDRESS = 0x3E  # Replace with your LCD address if different

# Motor states
MOTOR_OFF = 0
MOTOR_ON = 1



# Motor speed
MOTOR_SPEED = 255  # Full speed

# Initialize I2C
i2c = busio.I2C(sda = board.GP26, scl = board.GP27)

# Initialize LCD
lcd = Grove_LCD_I2C(i2c, LCD_ADDRESS)


# Initialize motor
motor_a = DigitalInOut(MOTOR_PIN_A)
motor_b = DigitalInOut(MOTOR_PIN_B)
motor_a.direction = Direction.OUTPUT
motor_b.direction = Direction.OUTPUT
motor_state = MOTOR_OFF

# Helper functions
def toggle_motor():
    global motor_state
    motor_state = not motor_state
    if motor_state == MOTOR_ON:
        motor_a.value = True
        motor_b.value = False
        lcd.clear()
        lcd.print("Motor Stats: ON")
        lcd.cursor_position(0, 1)
        lcd.print("Motor Speed: {}".format(MOTOR_SPEED))
    else:
        motor_a.value = False
        motor_b.value = False
        lcd.clear()
        lcd.print("Motor Stats: OFF")

# Main loop
while True:
    current_time = time.monotonic()
    button_pressed = False

    # Check button state
    if not button.value:
        if not button_state:
            button_state = True
            last_press_time = current_time
    else:
        if button_state and (current_time - last_press_time >= DEBOUNCE_TIME):
            button_pressed = True
        button_state = False

    # Toggle motor if button is pressed
    if button_pressed:
        toggle_motor()

    # Delay to avoid button bouncing
    time.sleep(0.01)
