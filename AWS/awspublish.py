import machine
import network
import time
from umqtt.robust import MQTTClient

HOST = b'endpoint.iot.us-east-1.amazonaws.com' #el host debe ser reemplazado por uno propio
TOPIC = bytes('TopicName', 'utf-8')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSID","PASS")
time.sleep(4)

cert="/cert/cert.pem.crt"
key="/cert/private.pem.key"
root="/cert/root_ca.pem"

with open(cert, 'rb') as f:
    certf = f.read()
print(certf)

with open(key, 'rb') as f:
    keyf = f.read()
print(keyf)

with open(root, 'rb') as f:
    rootf = f.read()
print(rootf)

time.sleep(1)

conn = MQTTClient(client_id=TOPIC, server=HOST, port=8883, ssl=True, ssl_params={"cert":certf, "key":keyf})
conn.connect()

msg='mensaje'

while True:
  connection.publish(topic=TOPIC, msg=msg, qos=0)
  sleep(2)
