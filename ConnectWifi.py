def connect():
    import network
    
    ssid = "YOUR SSID"
    password = "WI-FI PASSWORD"
    
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected() ==True:
        print("Already connected")
        return
    
    station.active(True)
    station.connect(ssid, password)
    
    while station.isconnected() == False:
        pass
    print("Connection successful")
    print(statio.ifconfig())