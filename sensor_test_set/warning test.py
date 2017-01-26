import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

humidity = round(humidity, 2)
temperature = round(temperature, 2)

GPIO.setup(36, GPIO.IN)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

touchWarning = False
tempWarning = False
humidityWarning = False

tempTreshold = 25
humTreshold = 25

while True:
    if GPIO.input(36)==1:
        touchWarning=True
        continue
    if humidity >= humTreshold:
        humidityWarning = True
        continue
    if temperature >= tempTreshold:
        tempWarning=True
        continue
    if touchWarning == True and tempWarning== True and humidityWarning == True:
        GPIO.output(12, 1)
        GPIO.output(11, 0)
        time.sleep(3)