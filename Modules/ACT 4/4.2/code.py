import board
import busio
import time
from grove_lcd import Grove_LCD_I2C

# Initialize I2C bus
i2c = busio.I2C(scl=board.GP27, sda= board.GP26)

# Initialize LCD object
lcd = Grove_LCD_I2C(i2c, 0x3E)  # Replace 0x27 with your LCD address if different

# Clear LCD display
lcd.clear()

# Function to display message on LCD from shell input
def display_message():
    message = input("Enter a message to display: ")
    lcd.clear()
    lcd.print(message)

# Main loop
while True:
    display_message()
    time.sleep(2)
