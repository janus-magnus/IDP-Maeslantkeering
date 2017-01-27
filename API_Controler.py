from pyowm import *

W_API_key = '0292ef38878076e5a546762d1c2a5ff8'  # weather API key
owmAPI = OWM(W_API_key)
owm = owmAPI.weather_at_place('Utrecht,NL')
weather_ob = owm.get_weather()

'''def weather():
    owm = owmAPI.weather_at_place('Utrecht,NL')
    weather_ob = owm.get_weather()
    return weather_ob
'''
def get_rain():
    rain = weather_ob.get_rain()
    return rain

def get_wind():
    wind = weather_ob.get_wind()
    return wind

