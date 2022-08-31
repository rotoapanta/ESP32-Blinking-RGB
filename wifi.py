# https://www.youtube.com/watch?v=2bpdLOoz828

from machine import Pin
import network
import time

p17 = Pin(17, Pin.OUT)
p16 = Pin(16, Pin.OUT)
p15 = Pin(15, Pin.OUT)

p17.off() 
p16.on() 
p15.on() 

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wifiList = wlan.scan()             # scan for access points

print('Redes disponibles-----------------------------------------------------------------')
for item in wifiList:
    print('Red:' + str(item[0]) + ' Canal :' + str(item[2]) + ' Señal: ' + str(item[3]) )
print('----------------------------------------------------------------------------------')


def wifiConncect():
    while not wlan.isconnected():
        print('Conectando...')
        time.sleep(1)
        print(wlan.status())
        if wlan.status() == 1001: 
            pass           
        else:            
            wlan.connect('LGRC', '2706@09rg') # connect to an AP
    p15.off()
    p17.on() 
    p16.on() 
    print('Conexión establecida!')

if not wlan.isconnected():      # check if the station is connected to an AP
    wifiConncect()
else:
    p15.off()
    p17.on() 
    p16.on() 
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

