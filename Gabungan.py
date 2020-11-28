import board
import busio as io
import RPi.GPIO as IO
import adafruit_mlx90614
import time

#import fungsi
#=============================================

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(14,IO.IN)
IO.setup(17,IO.OUT)

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)


#=============================================
while True:
    if(IO.input(14)==True): #object is far away
        print("0")
        time.sleep(1)
    if(IO.input(14)==False): #object is near
        IO.output(17, IO.LOW) #im using Buzzer for this
        #temp1 = mlx.ambient_temperature
        temp2 = mlx.object_temperature
        #print("room temperature : {} C".format(round(temp1, 3)))
        print(format(round(temp2, 3)))
        time.sleep(1)


