from tkinter import Tk
from tkinter.ttk import *
from tkinter import *
import Gabungan

Temps = None

def pool():
    global Temps
    
    try:
        val = round(Gabungan.Temps(), 2)
        Temps.set(val)
    except:
        pass
    
    root.after(500), pool()

# Creating tkinter window with fixed geometry
    
Raja = Tk()
Raja.geometry('550x300') 
Raja.title("New Thermal Devices")


temps = DoubleVar()

Suhu = Label(Raja, textvariable=Temps, font='Calibri')
Suhu.pack()

Raja.bind("<i>", lambda event: Raja.attributes("-fullscreen", True))
Raja.bind("<o>", lambda event: Raja.attributes("-fullscreen", False))

Gabungan.init()
Raja.mainloop()