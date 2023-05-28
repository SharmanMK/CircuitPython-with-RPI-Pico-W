import time
import board
import busio
import adafruit_dht
import pwmio
from adafruit_motor import motor

# DHT11 sensor pin
DHT_PIN = board.GP7

# Motor pins
MOTOR_PIN_A_FWD = board.GP4
MOTOR_PIN_A_BWD = board.GP5

# Initialize DHT11 sensor
dht = adafruit_dht.DHT11(DHT_PIN)

# Initialize motor
pwm_a_fwd = pwmio.PWMOut(MOTOR_PIN_A_FWD, frequency=1000)
pwm_a_bwd = pwmio.PWMOut(MOTOR_PIN_A_BWD, frequency=1000)
motor_a = motor.DCMotor(pwm_a_fwd, pwm_a_bwd)

# Main loop
while True:
    try:
        # Read temperature from DHT11 sensor
        temperature = dht.temperature

        # Print temperature to shell monitor
        print("Temperature:", temperature, "°C")

        # Check if temperature exceeds 28 degrees Celsius
        if temperature > 29:
            # Run the motor at maximum speed
            motor_a.throttle = 1.0
        else:
            # Stop the motor
            motor_a.throttle = 0

    except RuntimeError as e:
        # Error occurred, print error message to shell monitor
        print("Error:", e)

    # Delay between readings
    time.sleep(2)
