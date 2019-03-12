#librerias importadas
import network
import time
import socket
import machine

#metodo para hacer un request a un pagina web
#en este caso para un email es necesario definir 3 parametros
#val1-correo/val2-asunto/val3-mensaje
def http_get(site, port, reference, val1, val2, val3):
    address = socket.getaddrinfo(site, port)[0][-1]
    print('Connecting to ', site, '(', address, '):', port)
    s = socket.socket() 
    s.connect(address)
    values="{\"value1\":\""+val1+"\",\"value2\":\""+val2+"\",\"value3\":\""+val3+"\"}"
    message = "POST "+reference+" HTTP/1.1\r\n"+"Host: "+site+"\r\n"+"Content-Type: application/json\r\n"+"Content-Length: "+str(len(values))+"\r\n"+"\r\n"+values
    print('Sending: ', message)
    s.send(message)
    print(s.recv(500))
    s.close()

def ifttt_message(event, val1, val2, val3): #metodo para usar http_get rapidamente especificando el nombre del evento y las variables especificadas
    http_get('maker.ifttt.com', 80, '/trigger/' + event + '/with/key/"key cuenta ifttt"', val1, val2, val3)

#se conecta el microcontrolador a internet para el request a ifttt
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect("SSID", "PASSWORD")
print(nic.isconnected())
print(nic.ifconfig())

#se define el pin en el que se conecta el sensor de movimiento infrarrojo y el objeto
sens=machine.Pin(27, machine.Pin.IN)
#en el while true, cada vez que el sensor reciba un movimiento, este envia un correo
while True:
    if sens.value()==1:
        ifttt_message("nombreEspecificadoDelEvento", "correo","asunto", "mensaje")
