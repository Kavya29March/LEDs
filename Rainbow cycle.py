from machine import Pin
from time import sleep
from neopixel import NeoPixel

ring = NeoPixel(Pin(0),16)

colours = [(30,0,20), (30,0,20), (0,0,50), (0,0,50), (0,20,30), (0,20,30), (0,50,0), (0,50,0), (30,30,0), (30,30,0), (45,5,0), (45,5,0),
 (50,0,0), (50,0,0), (40,0,10), (40,0,10)]

off = (0,0,0)

#red = (50,0,0), green = (0,50,0), blue = (0,0,50), yellow = (30,30,0), orange = (45,5,0),
#pink = (40,0,10), turquoise = (0,20,30), purple = (30,0,20)



while True:
    index = 0
    
    for c in colours:
        ring[index] = c
        ring.write()
        sleep(0.2)
        index = index + 1
    for i in range(15,-1,-1):
        ring[i] = off
        sleep(0.2)
        ring.write()
    sleep(0.1)
    
    
        

    
    
    
    