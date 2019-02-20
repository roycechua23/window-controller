import machine
import time

d1 = machine.Pin(5, machine.Pin.OUT)
d2 = machine.Pin(4, machine.Pin.OUT)
d3 = machine.Pin(0, machine.Pin.OUT)
d4 = machine.Pin(2, machine.Pin.OUT)

for i in range(1000): 
  d1.on() 
  time.sleep(0.01); 
  d1.off() 
  d2.on() 
  time.sleep(0.01); 
  d2.off() 
  d3.on() 
  time.sleep(0.01); 
  d3.off() 
  d4.on() 
  i+=1
  time.sleep(0.01) 
  d4.off()
