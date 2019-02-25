import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
import dht
esp.osdebug(None)
import gc
gc.collect()
ssid = 'RCWiFi'
password = 'R0yc3261523'
#mqtt_server = '192.168.254.122'
mqtt_server = '192.168.8.119'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub1 = b'esp8266/window1'
topic_pub = b'temperature'
last_message = 0
message_interval = 5

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass
print('Connection successful')
print(station.ifconfig())

# main program
from machine import Pin

d = dht.DHT22(Pin(0))
d1 = Pin(5, Pin.OUT)
d2 = Pin(4, Pin.OUT)
d3 = Pin(0, Pin.OUT)
d4 = Pin(2, Pin.OUT)

d5 = Pin(14, Pin.OUT)
d6 = Pin(12, Pin.OUT)
d7 = Pin(13, Pin.OUT)
d8 = Pin(15, Pin.OUT)

def closeWindow():
    for i in range(1000): 
        d1.on() 
        d5.on()
        time.sleep(0.0031); 
        d1.off()
        d5.off() 
        d2.on() 
        d6.on()
        time.sleep(0.0031); 
        d2.off() 
        d6.off()
        d3.on() 
        d7.on()
        time.sleep(0.0031); 
        d3.off() 
        d7.off()
        d4.on() 
        d8.on()
        i+=1
        time.sleep(0.0031); 
        d4.off()
        d8.off()

def openWindow():
    for i in range(1000): 
        d8.on() 
        d4.on()
        time.sleep(0.0031); 
        d8.off()
        d4.off() 
        d7.on() 
        d3.on()
        time.sleep(0.0031); 
        d7.off() 
        d3.off()
        d6.on() 
        d2.on()
        time.sleep(0.0031); 
        d6.off() 
        d2.off()
        d5.on() 
        d1.on()
        i+=1
        time.sleep(0.0031); 
        d5.off()
        d1.off()

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'esp8266/window1' and msg == b'1':
    openWindow()
  elif topic == b'esp8266/window1' and msg == b'0': 
    closeWindow()

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub1)
  print('Connected to %s MQTT broker, subscribed to %s' % (mqtt_server, topic_sub1))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    new_message = client.check_msg()
    if new_message != 'None':
      d.measure()
      t = d.temperature() 
      client.publish(topic_pub, b'%d' % t)
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()

