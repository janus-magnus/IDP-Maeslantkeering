from tkinter import *
import API_Controler as ap
from datetime import datetime

last_tweet = ""
show_weather = 0

class ScreenFrame():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('510x510')
        self.root.title('Screen')
        self.root.columnconfigure(0, weight=3)
        self.root.rowconfigure(0,minsize=40,weight=3)
        #Voeg een label aan de bovenkant van het scherm toe.
        self.display_label_top = Label(text='place holder',
                                   fg='white',bg='#163c76',bd=1, relief=GROOVE, font='bold')
        self.display_label_top.grid(row=0,columnspan=2, sticky=W+E+N+S)
        self.get_weather()

        self.root.mainloop()


    def get_weather(self):
        '''haalt de weer informatie op en zet het in labels voor weergave'''
        weather_ob = ap.weather() #roep het weer API aan

       # dit zijn de functies die op de het weather_ob kan uitvoeren
        wind = weather_ob.get_wind()   # haalt windgegevens op
        humidity = weather_ob.get_humidity()  # haalt luchtvochtingheid op
        temp = weather_ob.get_temperature(unit='celsius') # haalt de temp op
        status = weather_ob.get_status() # haalt weer op e.g. rain, sun, cloudy

        #de tijd van laatste update omzetten naar gewenste notatie
        text_date = datetime.strftime(weather_ob.get_reference_time(timeformat='date'), "%a %e %b om %H:%M:%S")

        #Voeg de labels van het weerbericht toe met de info.
        self.weather_label = Label(text='API info:\n'+text_date, fg='#163c76',bg='#EEEEEE', bd=1, font=('normal', '14'))
        self.weather_label.grid(row=4, columnspan=2, sticky=E+W+N+S)

        self.weather_label = Label(text=status+"\t\t\tLuchtvochtigheid: "+str(humidity)+"%\nTemperatuur: "+str(temp['temp'])+"°C\tWindsnelheid: "+str(wind['speed'])+"km/u"
                                   ,anchor='n',fg='#163c76',bg='#EEEEEE',bd=1, font=('normal', '13'))
        self.weather_label.grid(row=5, columnspan=2, sticky=E+W+N+S)
sf = ScreenFrame()