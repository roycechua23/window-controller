import dht
import machine
import time

#d = dht.DHT11(machine.Pin(0))
#d.measure()
#d.temperature() # eg. 23 (°C)
#d.humidity() # eg. 41 (% RH)
d = dht.DHT22(machine.Pin(0))
  while True:
  d.measure()
  d.temperature() # eg. 23.6 (°C)
  d.humidity() # eg. 41.3 (% RH)
  print(d.measure())
  time.sleep(0.5)
  
