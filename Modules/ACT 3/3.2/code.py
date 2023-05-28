import time
import board
import digitalio
import pwmio
from adafruit_motor import motor

# Define Pin Variables
PWM_M1A = board.GP4
PWM_M1B = board.GP5
BUTTON_ACCELERATE = board.GP22
BUTTON_DECELERATE = board.GP20

# DC motor setup
pwm_1a = pwmio.PWMOut(PWM_M1A, frequency=10000)
pwm_1b = pwmio.PWMOut(PWM_M1B, frequency=10000)

motor1 = motor.DCMotor(pwm_1a, pwm_1b)

# Button setup
button_accelerate = digitalio.DigitalInOut(BUTTON_ACCELERATE)
button_accelerate.direction = digitalio.Direction.INPUT
button_accelerate.pull = digitalio.Pull.UP

button_decelerate = digitalio.DigitalInOut(BUTTON_DECELERATE)
button_decelerate.direction = digitalio.Direction.INPUT
button_decelerate.pull = digitalio.Pull.UP

# Serial Monitor to monitor motor status
print("*** DC motor test ***")
speed = 0.5
motor_on = False

# Main loop
while True:
    # Check if accelerate button is pressed
    if not button_accelerate.value:
        motor_on = True
        speed += 0.01
        if speed > 1.0:
            speed = 1.0

    # Check if decelerate button is pressed
    if not button_decelerate.value:
        motor_on = True
        speed -= 0.01
        if speed < 0.0:
            speed = 0.0

    # Update motor state
    if motor_on:
        motor1.throttle = speed
        print("Motor speed: {:.2f}".format(speed))
    else:
        motor1.throttle = 0
        print("Motor is OFF")

    time.sleep(0.05)
