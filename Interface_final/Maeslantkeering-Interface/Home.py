import tkinter as tk
from tkinter import *

class Home(tk.Frame):
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

        self.welkomLabel = Label(self)
        self.welkomLabel.place(relx=0.27, rely=0.09, height=61, width=284)
        self.welkomLabel.configure(background="#a8b8ee")
        self.welkomLabel.configure(cursor="X_cursor")
        self.welkomLabel.configure(disabledforeground="#a3a3a3")
        tahoma = "-family Tahoma -size 12 -weight normal -slant roman " \
                 "-underline 0 -overstrike 0"
        self.welkomLabel.configure(font=self.tahoma)
        self.welkomLabel.configure(foreground="#000000")
        self.welkomLabel.configure(text='''Welkom, selecteer een optie:''')
        self.welkomLabel.configure(width=284)

        self.NetworkButton = Button(self)
        self.NetworkButton.place(relx=0.08, rely=0.33, height=74, width=217)
        self.NetworkButton.configure(activebackground="#d9d9d9")
        self.NetworkButton.configure(activeforeground="#000000")
        self.NetworkButton.configure(background="#d9d9d9")
        self.NetworkButton.configure(disabledforeground="#a3a3a3")
        self.NetworkButton.configure(foreground="#000000")
        self.NetworkButton.configure(highlightbackground="#d9d9d9")
        self.NetworkButton.configure(highlightcolor="black")
        self.NetworkButton.configure(pady="0")
        self.NetworkButton.configure(text='''Network''')
        self.NetworkButton.configure(width=217)

        self.manualButton = Button(self)
        self.manualButton.place(relx=0.55, rely=0.33, height=74, width=217)
        self.manualButton.configure(activebackground="#d9d9d9")
        self.manualButton.configure(activeforeground="#000000")
        self.manualButton.configure(background="#d9d9d9")
        self.manualButton.configure(disabledforeground="#a3a3a3")
        self.manualButton.configure(foreground="#000000")
        self.manualButton.configure(highlightbackground="#d9d9d9")
        self.manualButton.configure(highlightcolor="black")
        self.manualButton.configure(pady="0")
        self.manualButton.configure(text='''Manual''')

        self.autoButton = Button(self)
        self.autoButton.place(relx=0.08, rely=0.62, height=74, width=217)
        self.autoButton.configure(activebackground="#d9d9d9")
        self.autoButton.configure(activeforeground="#000000")
        self.autoButton.configure(background="#d9d9d9")
        self.autoButton.configure(disabledforeground="#a3a3a3")
        self.autoButton.configure(foreground="#000000")
        self.autoButton.configure(highlightbackground="#d9d9d9")
        self.autoButton.configure(highlightcolor="black")
        self.autoButton.configure(pady="0")
        self.autoButton.configure(text='''Auto''')

        self.changeButton = Button(self)
        self.changeButton.place(relx=0.55, rely=0.62, height=74, width=217)
        self.changeButton.configure(activebackground="#d9d9d9")
        self.changeButton.configure(activeforeground="#000000")
        self.changeButton.configure(background="#d9d9d9")
        self.changeButton.configure(disabledforeground="#a3a3a3")
        self.changeButton.configure(foreground="#000000")
        self.changeButton.configure(highlightbackground="#d9d9d9")
        self.changeButton.configure(highlightcolor="black")
        self.changeButton.configure(pady="0")
        self.changeButton.configure(text='''Verander passkey''')