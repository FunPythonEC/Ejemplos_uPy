import socket
try:
    import ussl as ssl
except:
    import ssl
    
IFTTT_HOST = 'maker.ifttt.com'
IFTTT_PORT = 443
SAFE_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.- '

def make_safe(string):
    r = []
    for c in string:
        if c in SAFE_CHARS:
            r.append(c)
        else:
            r.append('%%%x' % ord(c))
    return (''.join(r)).replace(' ', '+')

def trigger(event, key, value1='', value2='', value3=''):  
    path = '/trigger/%s/with/key/%s' % (make_safe(event), make_safe(key))  
    data =  '{'+value1+':"",'+value2+':"",'+value3+':""}'
             
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    s = ssl.wrap_socket(sock)
    s.connect(socket.getaddrinfo(IFTTT_HOST, IFTTT_PORT)[0][4])
    
    request = '%s %s HTTP/1.0\r\n' % ('POST', path)
    request += 'Host: %s\r\n' % IFTTT_HOST
    request += 'Content-Type: application/json\r\n'
    request += 'Content-Length: %s\r\n\r\n%s\r\n\r\n' % (len(data), data)
    
    s.send(request)
    response = ''
    while 1:
        recv = s.readline()
        if len(recv) == 0: break
        response += recv.decode()
    s.close()
    return response
