import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)

while True:
    if GPIO.input(36)==1:
        print('yas, queen')
        break
    else:
        print(GPIO.input(36))
        time.sleep(1)