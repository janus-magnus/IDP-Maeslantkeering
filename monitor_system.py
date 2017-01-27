import time
import gate_control_functions as gc

#warning flags
touchWarning = False
tempWarning = False
humidityWarning = False
windSpeedWarning = False
rainWarning = False

#treshholds Oranje
tempTreshold = 25
humTreshold = 25
windSpeedTreshold = 50
rainTreshold = 10

#thresholds rood
tempTreshold = 30
humTreshold = 30
windSpeedTreshold = 60
rainTreshold = 15

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

def get_colour_code():
    # count de flags die op true staan en geeft een kleur code terug