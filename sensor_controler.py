# import Adafruit_DHT
# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(36, GPIO.IN)# touch sensor input
humidity = 0
temperature = 0

def get_rawTempHum():
    global humidity, temperature
    # humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)  # temp en hum sensor input

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
    pass
    # return GPIO.input(36)

#get_rawTempHum()
#print 'temp = {0:0.1f}*C luchtvochtigheid = {1:0.1f}%'.format(temperature, humidity)
#print(''+str(get_humidity()) +' + ' + str(get_temp()))
