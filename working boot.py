import gc 
import webrepl
import network

# WiFi variables
ssid = "ATT7WXji9I"
pwd  = "pzjdhzsat6sf"

webrepl.start()
gc.collect()
sta_if = network.WLAN(network.STA_IF)
ap_if  = network.WLAN(network.AP_IF)
ap_if.active(False)
if not sta_if.isconnected():
  print('Connecting to WiFi...')
  sta_if.active(True)
  sta_if.connect(ssid, pwd)
  while not sta_if.isconnected():
   # pass$
    print('network config:', sta_if.ifconfig())

