from pyowm import *

W_API_key = '0292ef38878076e5a546762d1c2a5ff8'  # weather API key
owmAPI = OWM(W_API_key)
owm = owmAPI.weather_at_place('Utrecht,NL')
w = owm.get_weather()


def weather():
    owm = owmAPI.weather_at_place('Utrecht,NL')
    weather_ob = owm.get_weather()
    return weather_ob

def get_rain():# zou het volume van regen in de laatste 3 uur moeten weer geven maar blijft nu nog leeg geen idee waarom
    rain = w.get_rain()
    return rain

def get_wind():
    wind = w.get_wind()
    return wind['speed']


