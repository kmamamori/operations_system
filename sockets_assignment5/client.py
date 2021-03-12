#!/usr/bin/env python3
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 7069))
while 1:
    data = s.recv(10000)
    print(data.decode())
    message = input("Client:\t")
    s.send(message.encode())
    if message == "e":
        print("Exiting...")
        s.close()
        break
s.close()
