import time
import board
import neopixel

# Configure NeoPixel LED
pixel_pin = board.GP28
num_pixels = 1

# Initialize NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

# Define RGB color values
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

# Set RGB colors
colors = [red, green, blue, cyan, magenta, yellow, orange, purple, pink, white, black]

# Function to cycle through and display all colors
def colours():
    for color in colors:
        pixels.fill(color)
        time.sleep(1)

# Call the colours() function
colours()
