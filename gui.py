import board
import busio as io
import RPi.GPIO as IO
import adafruit_mlx90614
import tkinter as tk
import threading


# Setup of GPIO's and sensors
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(14,IO.IN)
IO.setup(17,IO.OUT)
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)


def pool():
    global temps
    try:
        if(IO.input(14)==True): #object is far away
            print("0")
        if(IO.input(14)==False): #object is near
            IO.output(17, IO.LOW) #im using Buzzer for this
            #temp1 = mlx.ambient_temperature
            #print("room temperature : {} C".format(round(temp1, 3)))
        temp2 = mlx.object_temperature
        #print(format(round(temp2, 3)))
        val = round(temp2, 3)
        temps.set(val)
    except:
        pass
    Raja.after(1000, pool)


# Creating tkinter window with fixed geometry
Raja = tk.Tk()
Raja.geometry('550x300')
Raja.resizable(0, 0)
Raja.title("New Thermal Devices")

temps = tk.StringVar()
Suhu = tk.Label(Raja, textvariable=temps, font='Calibri')
Suhu.pack()

Raja.bind("<i>", lambda event: Raja.attributes("-fullscreen", True))
Raja.bind("<o>", lambda event: Raja.attributes("-fullscreen", False))

t = threading.Thread(target=pool)
t.start()

Raja.mainloop()
