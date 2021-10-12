print('RUN: main.py')
import ConnectWifi
ConnectWifi.connect()
import machine
import network
import time
from umqtt.robust import MQTTClient
import os
import gc
import sys




# create a random MQTT clientID 
random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')

# connect to Adafruit IO MQTT broker using unsecure TCP (port 1883)
# 
# To use a secure connection (encrypted) with TLS: 
#   set MQTTClient initializer parameter to "ssl=True"
#   Caveat: a secure connection uses about 9k bytes of the heap
#         (about 1/4 of the micropython heap on the ESP8266 platform)
ADAFRUIT_IO_URL = b'io.adafruit.com' 
ADAFRUIT_USERNAME = b'YOUR ADAFRUIT USERNAME'
ADAFRUIT_IO_KEY = b'YOUR TOKEN'
ADAFRUIT_IO_FEEDNAME = b'HodorAlert'

client = MQTTClient(client_id=mqtt_client_id, 
                    server=ADAFRUIT_IO_URL, 
                    user=ADAFRUIT_USERNAME, 
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)
try:            
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

# publish free heap statistics to Adafruit IO using MQTT
#
# format of feed name:  
#   "ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME"
mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
PUBLISH_PERIOD_IN_SEC = 5

 
rw = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    #time.sleep(0.1)
    
    if rw.value() == 1:
        print('Checking')
        message = "OFF"
        #time.sleep(1)
    if rw.value() == 0:
        
       # while True:
        message = "ON"
        print('Door Open')
           # time.sleep(0.1)
        
    try:
                      
                client.publish(mqtt_feedname,  bytes(str(message), 'utf-8'), qos=0)  
                time.sleep(PUBLISH_PERIOD_IN_SEC)
    except KeyboardInterrupt:
                print('Ctrl-C pressed...exiting')
                
client.disconnect()
sys.exit()
