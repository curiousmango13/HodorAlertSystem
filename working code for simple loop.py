import machine
import time
from time import sleep

rw = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    #sleep(1)
    #print(str(rw.value()))
    
    time.sleep(0.9)
   
    
    if rw.value() == 1:
        print('Door Closed')
    if rw.value() == 0:
        print('Door Open')