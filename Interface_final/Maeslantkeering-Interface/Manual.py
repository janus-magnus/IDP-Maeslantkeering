# alle GPIO inputs en dergelijk staan in comments omdat dit niet op de pi geschreven is
import tkinter as tk
from tkinter import *
#import gate_control_functions as gcf
import API_Controler as ac
from datetime import datetime
#from monitor_system import get_threat_level

class Manual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.geometry().format(600, 449)

        self._bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        self._fgcolor = '#000000'  # X11 color: 'black'
        self._compcolor = '#d9d9d9'  # X11 color: 'gray85'
        self._ana1color = '#d9d9d9'  # X11 color: 'gray85'
        self._ana2color = '#d9d9d9'  # X11 color: 'gray85'
        self.tahoma = "TkDefaultFont"

        self.configure(background="#a8b8ee")

        weather_ob = ac.weather()  # roep het weer API aan
        wind = weather_ob.get_wind()  # haalt windgegevens op
        humidity = weather_ob.get_humidity()  # haalt luchtvochtingheid op
        temp = weather_ob.get_temperature(unit='celsius')  # haalt de temp op
        status = weather_ob.get_status()  # haalt weer op e.g. rain, sun, cloudy
        text_date = datetime.strftime(weather_ob.get_reference_time(timeformat='date'), "%a %e %b om %H:%M:%S")

        self.timeLabel = Label(self)
        self.timeLabel.place(relx=0.27, rely=0.0, height=61, width=284)
        self.timeLabel.configure(background="#a8b8ee")
        self.timeLabel.configure(cursor="X_cursor")
        self.timeLabel.configure(disabledforeground="#a3a3a3")
        tahoma = "-family Tahoma -size 12 -weight normal -slant roman " \
                 "-underline 0 -overstrike 0"
        self.timeLabel.configure(font=self.tahoma)
        self.timeLabel.configure(foreground="#000000")
        self.timeLabel.configure(text=text_date)
        self.timeLabel.configure(width=284)

        self.threatLabel = Label(self)
        self.threatLabel.place(relx=0.27, rely=0.30, height=61, width=284)
        self.threatLabel.configure(background="#a8b8ee")
        self.threatLabel.configure(cursor="X_cursor")
        self.threatLabel.configure(disabledforeground="#a3a3a3")
        tahoma = "-family Tahoma -size 12 -weight normal -slant roman " \
                 "-underline 0 -overstrike 0"
        self.threatLabel.configure(font=self.tahoma)
        self.threatLabel.configure(foreground="#000000")
        #self.threatLabel.configure(text=get_threat_level())
        self.threatLabel.configure(text='placeholder voor code rood')
        self.threatLabel.configure(width=284)

        self.weatherLabel = Label(self)
        self.weatherLabel.place(relx=0.27, rely=0.15, height=61, width=284)
        self.weatherLabel.configure(background="#a8b8ee")
        self.weatherLabel.configure(cursor="X_cursor")
        self.weatherLabel.configure(disabledforeground="#a3a3a3")
        tahoma = "-family Tahoma -size 12 -weight normal -slant roman " \
                 "-underline 0 -overstrike 0"
        self.weatherLabel.configure(font=self.tahoma)
        self.weatherLabel.configure(foreground="#000000")
        self.weatherLabel.configure(text=status + "\t\t\tLuchtvochtigheid: " + str(humidity) + "%\nTemperatuur: " + str(
            temp['temp']) + "°C\tWindsnelheid: " + str(wind['speed']) + "km/u")
        self.weatherLabel.configure(width=284)


        self.openButton = Button(self)
        self.openButton.place(relx=0.08, rely=0.62, height=74, width=217)
        self.openButton.configure(activebackground="#d9d9d9")
        self.openButton.configure(activeforeground="#000000")
        self.openButton.configure(background="#d9d9d9")
        self.openButton.configure(disabledforeground="#a3a3a3")
        self.openButton.configure(foreground="#000000")
        self.openButton.configure(highlightbackground="#d9d9d9")
        self.openButton.configure(highlightcolor="black")
        self.openButton.configure(pady="0")
        self.openButton.configure(text='''Sluis Sluiten''')
        self.openButton.configure(command=lambda: self.open_gate())

        self.closeButton = Button(self)
        self.closeButton.place(relx=0.55, rely=0.62, height=74, width=217)
        self.closeButton.configure(activebackground="#d9d9d9")
        self.closeButton.configure(activeforeground="#000000")
        self.closeButton.configure(background="#d9d9d9")
        self.closeButton.configure(disabledforeground="#a3a3a3")
        self.closeButton.configure(foreground="#000000")
        self.closeButton.configure(highlightbackground="#d9d9d9")
        self.closeButton.configure(highlightcolor="black")
        self.closeButton.configure(pady="0")
        self.closeButton.configure(text='''Sluis Openen''')
        self.closeButton.configure(command=lambda: self.close_gate())


    def open_gate(self):
        #gcf.open_gate()
        print('sesame')

    def close_gate(self):
        #gcf.close_gate()
        print('''pool's closed''')
