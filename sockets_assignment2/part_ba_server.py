#!/usr/bin/env python3
from socket import *
import time
s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1", 7069))
s.listen(5)

while True:
    c,a = s.accept()
    data = c.send((256).to_bytes(2, byteorder = 'big'))
    c.close()
