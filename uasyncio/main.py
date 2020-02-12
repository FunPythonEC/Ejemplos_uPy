import api
import network

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect('SSID', 'PASS')
    while not sta_if.isconnected():
        pass

telegram = api.TelegramBot('734531224:AAHHILvDfwXVYSDKQ5QZYbbjOXewEx-z0WY')
def message_handler(message):
    print(message)
    if message[2] == '/start':
        telegram.send(message[0], 'qe')
    if message[2] == '/measure':
        telegram.send(message[0], 'Temperatura')

telegram.listen(message_handler)