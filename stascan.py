import network
import socket
import time
import ujson
import ubinascii
#with open('conf.json') as f:
    #data = ujson.load(f)

port=10086
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='593', authmode=network.AUTH_WPA_WPA2_PSK, password="12345678")

time.sleep(10)
a=ap.status('stations')
while True:
    for i in range(0,len(a)):
        print(a[i][0])
        print(ubinascii.hexlify(a[i][0]).decode())
