from machine import Pin
import time

r = Pin(13, Pin.IN, Pin.PULL_UP)
d = Pin(4, Pin.OUT)

while True:
  print(r.value())
  if r.value() == 0:
    d.on()
  else:
    d.off()
  time.sleep(1)
