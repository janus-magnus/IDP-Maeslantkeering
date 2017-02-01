import tkinter as tk
from tkinter import *
import hashlib

class Pass(tk.Frame):
    controller = None
    digitArray = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.geometry().format("265x410+1114+473")

        self._bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        self._fgcolor = '#000000'  # X11 color: 'black'
        self._compcolor = '#d9d9d9'  # X11 color: 'gray85'
        self._ana1color = '#d9d9d9'  # X11 color: 'gray85'
        self._ana2color = '#d9d9d9'  # X11 color: 'gray85'
        self.font3 = "-family System -size 10 -weight bold -slant " \
                     "roman -underline 0 -overstrike 0"


        self.configure(background="#a8b8ee")
        self.configure(cursor="X_cursor")

        self.Label1 = Label(self)
        self.Label1.place(relx=0.0, rely=0.07, height=61, width=264)
        self.Label1.configure(background="#a8b8ee")
        self.Label1.configure(cursor="X_cursor")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=self.font3)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Passkey fout, probeer het opnieuw.''')
        self.Label1.configure(fg="red")
        self.Label1.configure(width=264)


        self.Button2 = Button(self)
        self.Button2.place(relx=0.42, rely=0.29, height=44, width=47)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''2''')
        self.Button2.configure(command=lambda: self.addDigit(2))

        self.Button3 = Button(self)
        self.Button3.place(relx=0.68, rely=0.29, height=44, width=47)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''3''')
        self.Button3.configure(command=lambda: self.addDigit(3))

        self.Button4 = Button(self)
        self.Button4.place(relx=0.15, rely=0.44, height=44, width=47)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''4''')
        self.Button4.configure(command=lambda: self.addDigit(4))

        self.Button5 = Button(self)
        self.Button5.place(relx=0.68, rely=0.44, height=44, width=47)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''6''')
        self.Button5.configure(command=lambda: self.addDigit(6))

        self.Button6 = Button(self)
        self.Button6.place(relx=0.42, rely=0.44, height=44, width=47)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''5''')
        self.Button6.configure(command=lambda: self.addDigit(5))

        self.Button7 = Button(self)
        self.Button7.place(relx=0.15, rely=0.59, height=44, width=47)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''7''')
        self.Button7.configure(width=47)
        self.Button7.configure(command=lambda: self.addDigit(7))

        self.Button8 = Button(self)
        self.Button8.place(relx=0.42, rely=0.59, height=44, width=47)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''8''')
        self.Button8.configure(width=47)
        self.Button8.configure(command=lambda: self.addDigit(8))

        self.Button9 = Button(self)
        self.Button9.place(relx=0.68, rely=0.59, height=44, width=47)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''9''')
        self.Button9.configure(width=47)
        self.Button9.configure(command=lambda: self.addDigit(9))

        self.Button10 = Button(self)
        self.Button10.place(relx=0.42, rely=0.73, height=44, width=47)
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''0''')
        self.Button10.configure(width=47)
        self.Button10.configure(command=lambda: self.addDigit(0))

        self.Button12 = Button(self)
        self.Button12.place(relx=0.15, rely=0.29, height=44, width=47)
        self.Button12.configure(activebackground="#d9d9d9")
        self.Button12.configure(activeforeground="#000000")
        self.Button12.configure(background="#d9d9d9")
        self.Button12.configure(disabledforeground="#a3a3a3")
        self.Button12.configure(foreground="#000000")
        self.Button12.configure(highlightbackground="#d9d9d9")
        self.Button12.configure(highlightcolor="black")
        self.Button12.configure(pady="0")
        self.Button12.configure(text='''1''')
        self.Button12.configure(command=lambda: self.addDigit(1))

        self.Button1 = Button(self)
        self.Button1.place(relx=0.08, rely=0.88, height=34, width=227)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#57e72e")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Enter''')
        self.Button1.configure(width=227)
        self.Button1.configure(command=lambda: self.checkDigits())

    def addDigit(self, digit):
        self.digitArray.append(str(digit))

    def checkDigits(self):
        digitString = ''
        for x in range(0, 4):
            digit = self.digitArray[x]
            digitString = digitString + digit
        self.digitArray.clear()

        digitString = hashlib.md5(str.encode(digitString)).hexdigest()

        if (self.controller.passkey == digitString):
            self.controller.toHome()