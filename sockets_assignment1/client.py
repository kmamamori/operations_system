#!/usr/bin/env python3
from socket import *
import time
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 7069))
while 1:
    data = s.recv(10000).decode()
    print(data)
    if len(data) == 0:
        break
s.close()
