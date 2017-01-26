from pyowm import *

W_API_key = '0292ef38878076e5a546762d1c2a5ff8'  # weather API key
owmAPI = OWM(W_API_key)

def weather():
    '''haalt de weer gegevens op van openweathermap en return weather_ob'''
    owm = owmAPI.weather_at_place('Utrecht,NL')
    weather_ob = owm.get_weather()
    return weather_ob
