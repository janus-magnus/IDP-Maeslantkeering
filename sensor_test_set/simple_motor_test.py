import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

while True:
    try:
        GPIO.output(12, True)
        GPIO.output(11, False)
        print('1')
        sleep(3)
        GPIO.output(11, True)
        GPIO.output(12, False)
        sleep(3)
    except(KeyboardInterrupt):
        GPIO.output(12, False)
        GPIO.output(11, False)
        quit()