""" 
Example for Pi Pico W. Blink the built-in LED
"""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP28)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(1)