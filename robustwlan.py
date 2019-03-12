import network
import time
import _thread    
def connwifithread(ssid, clave):
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    while True:
        if not nic.isconnected():
            nic.connect(ssid, clave)
            print(nic.isconnected())
            print(nic.ifconfig())
        elif nic.isconnected():
            print(nic.isconnected())
            print(nic.ifconfig())
            pass 
        time.sleep(1)   
def connectwifi(nombre, clave):
    _thread.start_new_thread(connwifithread(nombre, clave), ())
