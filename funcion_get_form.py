
def _GET(request,args):
    ini=request.find('?')
    print (ini)
    final=request.find('HTTP')
    print(final)
    variables=(request[ini+1:final]).split('&')
    print("variables=",(request[ini+1:final]).split('&'))
    for m in variables:
        k,v= m.split('=')
        if k==args:
            print("var es",k,"valor es",v)
            return v
            break

request="GET /?var1=valor_var1&var2=valor_var2&var3=valor_var3 HTTP/1.1\r\n"
print(_GET(request,"Nom"))
