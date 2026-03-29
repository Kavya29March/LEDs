from machine import Pin
from time import sleep
from neopixel import NeoPixel

ring = NeoPixel(Pin(0),16)

red = (50,0,0)
green = (0,50,0)
blue = (0,0,50)
yellow = (30,30,0)
orange = (50,5,0)
pink = (40,0,10)
turquoise = (0,20,30)
purple = (30,0,20)
white = (15,15,20)

ring[0] = purple
ring[1] = purple

ring[2] = blue
ring[3] = blue

ring[4] = turquoise
ring[5] = turquoise

ring[6] = green
ring[7] = green

ring[8] = yellow
ring[9] = yellow

ring[10] = orange
ring[11] = orange

ring[12] = red
ring[13] = red

ring[14] = pink
ring[15] = pink

ring.write()


    