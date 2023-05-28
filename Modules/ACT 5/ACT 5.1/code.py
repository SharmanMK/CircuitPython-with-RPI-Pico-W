import time
import board
import adafruit_dht

dht11 = adafruit_dht.DHT11(board.GP7)

while True:
    try:
        temperature = dht11.temperature
        humidity = dht11.humidity
        
        print("Temperature: {:.2f} °C, Humidity: {:.2f} %RH ".format(temperature, humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht22.exit()
        raise error

    time.sleep(2.0)
