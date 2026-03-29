from machine import Pin
from time import sleep
from neopixel import NeoPixel

ring = NeoPixel(Pin(0),16)

red = (50,0,0)
green = (0,50,0)
blue = (0,0,50)
yellow = (30,30,0)
orange = (50,5,0)
white = (15,15,20)
turq = (0,20,30)
purple = (30,0,20)

while True:

    ring.fill(purple)
    ring.write()
    sleep(0.2)

    ring.fill(turq)
    ring.write()
    sleep(0.2)

    ring.fill(blue)
    ring.write()
    sleep(0.2)

    ring.fill(green)
    ring.write()
    sleep(0.2)

    ring.fill(yellow)
    ring.write()
    sleep(0.2)

    ring.fill(orange)
    ring.write()
    sleep(0.2)

    ring.fill(red)
    ring.write()
    sleep(0.2)

    ring.fill(white)
    ring.write()
    sleep(0.2)
   
