#!/usr/bin/env python3
from socket import *
import select
from datetime import datetime

s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 7069))
s.setblocking(False)
inputs = [s]
outputs = []
timer = 0
while 1:

    if inputs:
        timer += 1
        print("Client:\tat %s waiting for response, %d second has elapsed" % (datetime.now().strftime("%H:%M:%S"), timer))
    
    try:
        r, w, e = select.select(inputs, outputs, inputs, 1)
    except:
        print("Exiting...")
        break

    for s in w:
        i = input("Client:\t")
        data = s.send(i.encode())
        print("Client:\tsent to server at %s" % datetime.now().strftime("%H:%M:%S"))
        outputs.remove(s)
        inputs.append(s)
        
    for s in r:
        data = s.recv(10000).decode()
        if data == "e":
            s.close()
            break
        print("Client:\tserver replied at %s:" % datetime.now().strftime("%H:%M:%S"))
        print("%s" % data)
        inputs.remove(s)
        outputs.append(s)
        timer = 0
    
    for s in e:
        print(f'Non Blocking - error')
        inputs.remove(s)
        outputs.remove(s)
        break

s.close()
