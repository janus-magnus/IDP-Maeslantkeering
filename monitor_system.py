import API_Controler as apc
import sensor_controler as sc

#treshholds Oranje
tempTresholdO = 15
humTresholdO = 35
windSpeedTresholdO = 20

#thresholds rood
tempTresholdR = 5
humTresholdR = 50
windSpeedTresholdR = 30

def define_threat_level():
    threatCount = 0

    if sc.get_touch()==1:
        threatCount+=2
    if sc.get_humidity() >= humTresholdO:
        threatCount+=1
    if sc.get_humidity() >= humTresholdR:
        threatCount+=1
    if sc.get_temp() <= tempTresholdO:
        threatCount += 1
    if sc.get_temp() <= tempTresholdR:
        threatCount += 1
    if apc.get_wind() >= windSpeedTresholdO:
        threatCount += 1
    if apc.get_wind() >= windSpeedTresholdR:
        threatCount += 1
    return threatCount

def get_threat_level():
    if define_threat_level()>=4:
        return 'Oranje'
    if define_threat_level()>=6:
        return 'Rood'
    else:
        return 'Groen'
