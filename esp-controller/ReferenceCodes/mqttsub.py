import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
ssid = 'rbc236'
password = 'royce236'
mqtt_server = '192.168.254.122'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub1 = b'esp8266/5'
topic_sub2 = b'esp8266/4'
topic_pub = b'hello'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass
print('Connection successful')
print(station.ifconfig())

# main program
from machine import Pin

d5 = Pin(5, Pin.OUT)
d4 = Pin(4, Pin.OUT)

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'esp8266/5' and msg == b'1':
    d5.on()
  elif topic == b'esp8266/5' and msg == b'0': 
    d5.off()
  elif topic == b'esp8266/4' and msg == b'1':
    d4.on()
  elif topic == b'esp8266/4' and msg == b'0':
    d4.off()

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub1)
  client.subscribe(topic_sub2)
  print('Connected to %s MQTT broker, subscribed to %s and %s topic' % (mqtt_server, topic_sub1, topic_sub2))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    new_message = client.check_msg()
    if new_message != 'None':
      client.publish(topic_pub, b'received')
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()

