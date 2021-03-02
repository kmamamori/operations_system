#!/usr/bin/env python3
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1", 7069))
s.listen(5)

#data = s.send((256).to_bytes(2, byteorder = 'big'))

while True:
    c,a = s.accept()
#    data = c.htons(256)
    data = c.send(socket.ntohs(256))
    #data = c.send((256).to_bytes(2, byteorder = 'small'))
    c.close()
