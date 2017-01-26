from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

def open_gate():#wordt aangepast op het fysieke model
    GPIO.output(12, True)
    GPIO.output(11, False)
    sleep(10)
    GPIO.output(12, False)
    GPIO.output(11, False)

def close_gate():#wordt aangepast op het fysieke model
    GPIO.output(12, False)
    GPIO.output(11, True)
    sleep(10)
    GPIO.output(12, False)
    GPIO.output(11, False)