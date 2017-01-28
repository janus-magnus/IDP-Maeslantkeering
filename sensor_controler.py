import Adafruit_DHT
import RPi.GPIO as GPIO


# de sensor data moet constant ge-update worden


GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)# touch sensor input


def get_rawTempHum():
    global humidity, temperature
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)  # temp en hum sensor input


def get_humidity():
    global humidity
    get_rawTempHum()
    humidity = round(humidity, 2)
    return humidity

def get_temp():
    global temperature
    get_rawTempHum()
    temperature = round(temperature, 2)
    return temperature

def get_touch():
    return GPIO.input(36)


print(''+get_humidity() +' + ' + get_temp())
print(''+get_humidity() +' + ' + get_temp())
print(''+get_humidity() +' + ' + get_temp())