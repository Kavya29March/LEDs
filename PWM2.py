from machine import Pin, PWM
from time import sleep

LED = Pin(0,Pin.OUT)
pwm = PWM(LED)
pwm.freq(1000)

while True:
    for x in range(0,65536,1000):
        pwm.duty_u16(x)
        sleep(0.1)

    for y in range(65535,-1,-1000):
        pwm.duty_u16(y)
        sleep(0.1)

    





