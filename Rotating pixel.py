from machine import Pin
from time import sleep
from neopixel import NeoPixel

ring = NeoPixel(Pin(0),16)

colour = (0,20,30)
off = (0,0,0)

while True:
    for i in range(16):
        ring[i] = colour
        sleep(0.2)
        ring.write()
        ring[i] = off
        sleep(0.2)
        ring.write()
