import board
import digitalio
import busio
import time
from grove_lcd import Grove_LCD_I2C

# Button pins
BUTTON_MINUS = board.GP20
BUTTON_PLUS = board.GP22

# Button setup
button_minus = digitalio.DigitalInOut(BUTTON_MINUS)
button_minus.direction = digitalio.Direction.INPUT
button_minus.pull = digitalio.Pull.UP

button_plus = digitalio.DigitalInOut(BUTTON_PLUS)
button_plus.direction = digitalio.Direction.INPUT
button_plus.pull = digitalio.Pull.UP

# LCD setup
i2c = busio.I2C(board.GP27, board.GP26)
lcd = Grove_LCD_I2C(i2c, lcd_address=0x3E, cols=16, lines=2)

# Initial score
score = 0

# Display initial score on LCD
lcd.clear()
lcd.cursor_position(0, 0)
lcd.print("SCORE = {}".format(score))

# Button press variables
minus_button_pressed = False
plus_button_pressed = False

# Button press delay
button_press_delay = 0.5  # Adjust the delay as needed (in seconds)

# Main loop
while True:
    # Check if decrement button (B1) is pressed
    if not button_minus.value and not minus_button_pressed:
        score -= 1
        minus_button_pressed = True

        # Update LCD display
        lcd.cursor_position(7, 0)
        lcd.print("{:2d}".format(score))

        # Delay before allowing another button press
        time.sleep(button_press_delay)

    # Check if increment button (B2) is pressed
    if not button_plus.value and not plus_button_pressed:
        score += 1
        plus_button_pressed = True

        # Update LCD display
        lcd.cursor_position(7, 0)
        lcd.print("{:2d}".format(score))

        # Delay before allowing another button press
        time.sleep(button_press_delay)

    # Reset button press variables
    if button_minus.value:
        minus_button_pressed = False
    if button_plus.value:
        plus_button_pressed = False

    time.sleep(0.05)
