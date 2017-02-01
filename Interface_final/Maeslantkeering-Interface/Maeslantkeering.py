import tkinter as tk
from Pass import Pass
from PassReset import PassReset
from Home import Home


class Maeslantkeering(tk.Tk):
    # Deze class is de kern van het programma. Dit is wat standaard Tkinter code om te zorgen dat we meerde frames kunnen ondersteuen.
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)
        container = tk.Frame(self)

        # Grid bevat alle frames
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Een dictionairy met alle frames
        self.frames = {}

        # Initialiseer alle Frames, hierdoor kunnen we er later door heen bladeren met de 'show_frame' functie
        for F in (Pass, PassReset, Home):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Geef aan dat de beginnende pagina de 'Pass_Frame moet zijn'
        frame = Pass(container, self)

        self.frames[Pass] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Pass)

        # Hier word de grote van het venster aangegeven, zowel als de naam en dat het niet verstelbaar mag zijn.
        self.geometry("265x410+1114+473")
        self.title("Maeslantkeering")
        self.resizable(0, 0)
        self.configure(background="#6d8bf3")

    with open ("password.txt", "r", encoding='utf-8') as f:
        passkey = f.read()
        f.close()

    # Deze functie verplaatst een frame (Pass_Frame of ActueleVertrekInformatie) naar de voorgrond. Zo lijkt het alsof je
    # navigeert door het programma.
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def setStation(self, stationNaam):
        self.station = stationNaam

    def toHome(self):
        self.minsize(width=666, height=666)
        self.maxsize(width=666, height=666)
        self.show_frame("Home")

    def toPassReset(self):
        self.minsize(width=265, height=410)
        self.maxsize(width=265, height=410)
        self.show_frame("PassReset")

app = Maeslantkeering()
app.mainloop()