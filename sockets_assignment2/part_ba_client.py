#!/usr/bin/env python3
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 7069))

while 1:
    data = s.recv(10000)
    data = int.from_bytes(data, byteorder="big")
    if data == 0:
        break
    print(data)
s.close()
