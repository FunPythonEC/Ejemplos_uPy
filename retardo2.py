import time

def mensaje(msj):
    print(msj)

def retardo(t):
    mseg=1000
    seg=0
    while (seg<t):    
        start = time.ticks_ms() # get millisecond counter
        while(time.ticks_diff(time.ticks_ms(),start)<mseg):
            pass       
        seg+=1
        mensaje(str(seg))
    #mensaje("listo")
    return(1)

retardo(10)