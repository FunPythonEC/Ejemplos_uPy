import neopixel
import network
from machine import Pin
from time import sleep
import socket

html="""<!DOCTYPE html>
<html>
<body>

<h2>Color Picker</h2>
<p>The <strong>input type="color"</strong> is used for input fields that should contain a color.</p>
<p>Depending on browser support:<br>A color picker can pop-up when you enter the input field.</p>

<form action="/action_page.php">
  Select your favorite color:
  <input type="color" name="favcolor" value="#ff0000">
  <input type="submit">
</form>

<p><b>Note:</b> type="color" is not supported in Internet Explorer 11 and earlier versions or Safari 9.1 and earlier versions.</p>

</body>
</html>"""

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32')
ap.config(authmode=3, password='123456789')
ap.ifconfig()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sleep(3)
s.bind(('', 80))
s.listen(5)


while True:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        print(request)
        try:
            print(_GET(request, "favcolor"))
            
        except Exception:
            print("fallo de nuevo")

        response = html
        conn.send(response)
        conn.close()
