#!/usr/bin/env python3
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 7069))
for x in range(1,5):
    result = s.recv(512)
    print(result)


