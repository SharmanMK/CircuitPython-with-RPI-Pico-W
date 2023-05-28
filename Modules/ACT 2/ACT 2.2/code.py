import time
import board
import digitalio
import pwmio
from adafruit_motor import motor

# Define Pin Variables
PWM_M1A = board.GP4
PWM_M1B = board.GP5
BUTTON = board.GP21

# DC motor setup
pwm_1a = pwmio.PWMOut(PWM_M1A, frequency=10000)
pwm_1b = pwmio.PWMOut(PWM_M1B, frequency=10000)

motor1 = motor.DCMotor(pwm_1a, pwm_1b)

# Button setup
button = digitalio.DigitalInOut(BUTTON)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Serial Monitor to monitor motor status
print("*** DC motor test ***")
speed = 0
motor_on = False
prev_button_state = True

# Main loop
while True:
    button_state = button.value

    # Check if button state has changed
    if button_state != prev_button_state:
        if not button_state:  # Button is pressed
            motor_on = not motor_on  # Toggle motor state

            if motor_on:
                speed = 1
                print("Motor is ON")
            else:
                speed = 0
                print("Motor is OFF")

            motor1.throttle = speed

            # Debounce delay
            time.sleep(0.2)

    prev_button_state = button_state
