import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

humidity = round(humidity, 2)
temperature = round(temperature, 2)

if humidity is not None and temperature is not None:
    print 'temp = {0:0.1f}*C luchtvochtigheid = {1:0.1f}%'.format(temperature, humidity)
    print('hey')
else:
    print('kan de sensor niet uitlezen')