#!/usr/bin/env python3
from socket import *

#part A
s = socket(AF_INET, SOCK_STREAM)
s.connect(("nigelward.com", 80))
s.sendall(("GET /index.html HTTP/1.1\r\n" +
    "Host: nigelward.com\r\n" +
    "Accept: text/html\r\n" +
    "Connection: close\r\n\r\n").encode())
data = s.recv(1012).decode()
data = s.recv(16).decode()
print(data)
s.close()
