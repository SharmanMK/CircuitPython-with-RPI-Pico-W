import time
import board
import digitalio
import pwmio
from adafruit_motor import motor

# Define Pin Variables
PWM_M1A = board.GP4  
PWM_M1B = board.GP5

# DC motor setup
# DC Motors generate electrical noise when running that can reset the microcontroller in extreme
# cases. A capacitor can be used to help prevent this.
pwm_1a = pwmio.PWMOut(PWM_M1A, frequency=10000)
pwm_1b = pwmio.PWMOut(PWM_M1B, frequency=10000)

motor = motor.DCMotor(pwm_1a, pwm_1b)

# Set motor speed to maximum
motor.throttle = 1.0

# Wait for 5 seconds
time.sleep(5)

# Turn off the motor
motor.throttle = 0.0
