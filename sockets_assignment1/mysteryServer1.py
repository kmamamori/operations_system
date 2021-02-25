#!/usr/bin/env python3
from socket import *
import datetime, time, random
s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 7069))
s.listen(5)
while True:
    c,a = s.accept()
#    print("Received connection from" , a)
    time1 = time.time()
    nowtime = datetime.datetime.now()
    toSendString = "hello from " + gethostname() + nowtime.strftime(" %A %I:%M")
    toSendBytes = toSendString.encode()
    c.send(toSendBytes)

    if random.random() > 0.5:
       time.sleep(1)
    time2 = time.time()
    interval = time2 - time1
    toSendString = " now after %.6f " % interval
    toSendBytes = toSendString.encode()
    c.send(toSendBytes)
    c.close()


