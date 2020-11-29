from tkinter import Tk
from tkinter.ttk import *
from tkinter import *
import Gabungan

temps = None

def pool():
    global temps
    
    try:
        val = str(round(Gabungan.temps(), 2))
        temps.set(val)
    except:
        pass
    
    root.after(500, pool)

# Creating tkinter window with fixed geometry
    
Raja = Tk()
Raja.geometry('550x300') 
Raja.title("New Thermal Devices")


temps = StringVar()

Suhu = Label(Raja, textvariable=temps, font='Calibri')
Suhu.pack()

Raja.bind("<i>", lambda event: Raja.attributes("-fullscreen", True))
Raja.bind("<o>", lambda event: Raja.attributes("-fullscreen", False))

Gabungan.init()
Raja.mainloop()
