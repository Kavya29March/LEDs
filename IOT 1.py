from machine import Pin
from time import sleep
Red = Pin(0,Pin.OUT)
for i in range(10):
    Red.on()
    sleep(1)
    Red.off()
    sleep(1)

