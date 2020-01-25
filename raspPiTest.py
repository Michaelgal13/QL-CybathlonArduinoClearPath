import gpiozero as gp
from time import sleep

# pins 4 and 23

pin4=gp.DigitalOutputDevice(4,True, False,None)
pin4.on()