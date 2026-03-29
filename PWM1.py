from machine import Pin, PWM
from time import sleep

LED = Pin(0,Pin.OUT)

pwm = PWM(LED)
pwm.freq(1000)

pwm.duty_u16(int(0.1*65535))

LED.on()