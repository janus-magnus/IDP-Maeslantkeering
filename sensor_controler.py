import Adafruit_DHT
import RPi.GPIO as GPIO


# de sensor data moet constant ge-update worden


GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)# touch sensor input
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)# temp en hum sensor input
humidity = round(humidity, 2)
temperature = round(temperature, 2)

def get_humidity():
    return humidity

def get_temp():
    return temperature

def get_touch():
    return GPIO.input(36)