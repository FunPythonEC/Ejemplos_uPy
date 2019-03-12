import socket 
import machine
import network
import time
import robustwlan

def wificonfig():
    def _GET(request,args):
        ini=request.find('?')
        final=request.find('HTTP')
        variables=(request[ini+1:final]).split('&')
        for m in variables:
            k,v= m.split('=')
            if k==args:
                return v
                break
    #HTML to send to browsers
    html = """<!DOCTYPE html>
    <html>
    <head> <title>ESP CONFIG MENU</title> </head>
    <center><h2>Menu para configurar ESP</h2></center>

    <form>


      SSID:<br>
      <input type="text" name="ssid"><br>
      CLAVE:<br>
      <input type="text" name="clave"><br>
      <button name="confg" value="1" type="submit">Configurar</button>
    </form> 
    </html>
    """

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='ESP32')
    ap.config(authmode=3, password='123456789')
    ap.ifconfig()

    #Setup Socket WebServer
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(3)
    s.bind(('', 80))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        print(request)
        try:
            print(_GET(request, "confg"))
            print(_GET(request, "ssid"))
            print(_GET(request, "clave"))
            if _GET(request, "ssid")!="":
                txt="ssid="+str(_GET(request, "ssid"))+"\nclave="+str(_GET(request, "clave"))
                f = open('config.txt', 'w')
                f.write(txt)
                f.close()
                print("guardado")
            time.sleep(1)
            
        except Exception:
            print("fallo")

        response = html
        conn.send(response)
        conn.close()
def wificonnect():
    i=0
    for line in open('config.txt'):
        if i==0:
            ssid=line[5:len(line)-1]
        if i==1:
            clave=line[6:]
        i=i+1
    robustwlan.connectwifi(ssid,clave)
    
def confaccess(pin): 
    pinrev=machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
    print(pinrev.value())
    if pinrev.value()==1:
        wificonfig()
    else:
        wificonnect()
