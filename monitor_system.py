import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import gate_control_functions as gc

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)# touch sensor input
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)# temp en hum sensor input

#warning flags
touchWarning = False
tempWarning = False
humidityWarning = False
windSpeedWarning = False

#treshholds
tempTreshold = 25
humTreshold = 25
windSpeedTreshold = 50

while True:#placeholder loop moet werkend worden gemaakt
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
        gc.open_gate()
