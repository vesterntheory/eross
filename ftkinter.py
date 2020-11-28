from tkinter import Tk
from tkinter.ttk import *
from tkinter import *
# Creating tkinter window with fixed geometry
    
Apps = Tk()
Apps.geometry('550x300') 
Apps.title("New Thermal Devices")


Apps.bind("<i>", lambda event: Apps.attributes("-fullscreen", True))
Apps.bind("<o>", lambda event: Apps.attributes("-fullscreen", False))
Apps.mainloop()