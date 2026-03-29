from machine import Pin
from time import sleep
Red = Pin(0, Pin.OUT)
Green = Pin(1, Pin.OUT)
while True:
    Red.on()
    sleep(4)
    Green.on()
    sleep(2)
    Red.off()
    Green.on()
    sleep(4)
    Green.off()


