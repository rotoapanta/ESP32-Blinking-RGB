import network
import wifi_credentials
import ubinascii

def do_connect():
    wlan = network.WLAN(network.STA_IF) # create station interface
    wlan.active(True)       # activate the interface
    if not wlan.isconnected():# check if the station is connected to an AP
        print('connecting to network...')
        wlan.connect(wifi_credentials.ssid, wifi_credentials.password) # connect to an AP
        while not wlan.isconnected():
            pass
    print('MAC address', wlan.config('mac'))      # get the interface's MAC address
    print('Network config:', wlan.ifconfig())        # get the interface's IP/netmask/gw/DNS addresses    
    
    wlan_mac = wlan.config('mac')
    print('MAC address', ubinascii.hexlify(wlan_mac, ':').decode().upper())
    
    #hex_mac = hexlify(wlan_mac, ':').decode().upper()

do_connect();
