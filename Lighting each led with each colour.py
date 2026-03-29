from machine import Pin
from time import sleep
from neopixel import NeoPixel

ring = NeoPixel(Pin(0),16)

colors = [(50,0,0), (0,50,0), (0,0,50), (30,30,0)]

orange = (50,5,0)
pink = (40,0,10)
turquoise = (0,20,30)
purple = (30,0,20)

index = 0
for cols in colors:
    ring[index] = cols
    ring.write()
    sleep(0.5)
    index = index + 1