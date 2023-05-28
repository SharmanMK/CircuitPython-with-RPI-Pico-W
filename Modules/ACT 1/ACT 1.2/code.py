import time
import board
import digitalio
import neopixel

# Button configuration
button_pin = board.GP20
button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Neopixel configuration
led_pin = board.GP28
num_leds = 1
pixels = neopixel.NeoPixel(led_pin, num_leds)

'''
COLOURS!!!
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
purple = (128, 0, 128)
pink = (255, 192, 203)
white = (255, 255, 255)
black = (0, 0, 0)
'''

# Main loop
while True:
    if not button.value:  # Button pressed
        pixels.fill((255, 0, 0))  # Set RGB LED to red
    else:
        pixels.fill((0, 0, 0))  # Turn off RGB LED
