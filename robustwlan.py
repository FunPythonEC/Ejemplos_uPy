import network
import time
import _thread    
def connwifithread(ssid, clave):
    nic = network.WLAN(network.STA_IF)
    try:
        nic.active(True)
    except Exception as e:
        print("No se pudo activar WiFi: "+str(e))

    if nic.active():
        print("WiFi activado")
        while True:
            if not nic.isconnected():
                try:
                    nic.connect(ssid, clave)
                except Exception as e:
                    print(e)
                time.sleep(3)
                if nic.isconnected():
                    print("Se ha conectado a la red")
                    print(nic.ifconfig())
            elif nic.isconnected():
                pass

    else:
        print("Intentar ejecutar el metodo connectwifi de nuevo")  
def connectwifi(nombre, clave):
    _thread.start_new_thread(connwifithread(nombre, clave), ())
