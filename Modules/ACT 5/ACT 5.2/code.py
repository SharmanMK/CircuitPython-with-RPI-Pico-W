import time
import board
import adafruit_dht
import neopixel

dht11 = adafruit_dht.DHT11(board.GP7)

# NeoPixel
neopixel_pin = board.GP28
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

while True:
    try:
        temperature = dht11.temperature
        humidity = dht11.humidity
        
        print("Temperature: {:.2f} °C, Humidity: {:.2f} %RH".format(temperature, humidity))

        # NeoPixel indication
        if temperature <= 29:
            pixels.fill((0, 0, 255))  # Cold color (blue)
        else:
            pixels.fill((255, 0, 0))  # Hot color (red)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht11.exit()
        raise error

    time.sleep(2.0)
