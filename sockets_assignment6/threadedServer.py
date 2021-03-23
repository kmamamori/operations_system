#!/usr/bin/env python3
from socket import *
import datetime, time, random
import _thread

def clientHandler(clientSocket, address, threadNumber):
    global cumulativeResponses
    myResponses = 0
    print("I'm a new thread, number %d" % threadNumber)
    print("  handling communications with " , address)
    for x in range(1,5):
        lck.acquire()
        oldCumulativeResponses = cumulativeResponses
        time.sleep(2)
        time1 = time.time()
        nowtime = datetime.datetime.now()
        toSendString = "hello from " + gethostname() + nowtime.strftime(" %A %I:%M")
        toSendBytes = toSendString.encode()
        clientSocket.send(toSendBytes)
        cumulativeResponses = oldCumulativeResponses + 1
        lck.release()
        myResponses = myResponses + 1
        print("Thread %d has done %d sends; all threads %d" %
              (threadNumber,myResponses, cumulativeResponses))
    clientSocket.close()
    _thread.exit()


##### main #####
nThreads = 0 
global cumulativeResponses
cumulativeResponses = 0
lck = _thread.allocate_lock()
s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 7069))
s.listen(5)
while True:
    nThreads = nThreads + 1
    c,a = s.accept()
    _thread.start_new_thread(clientHandler,(c,a, nThreads))




