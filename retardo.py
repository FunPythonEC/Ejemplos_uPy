import time

def mensaje(msj):
    print(msj)

start = time.ticks_ms() # get millisecond counter
while (time.ticks_diff(time.ticks_ms(),start)<3000):
    pass

mensaje("listo")

