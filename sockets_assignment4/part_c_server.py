#!/usr/bin/env python3
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1", 7069))
s.listen(5)
c,a = s.accept()
counter = 0
while True:
    if counter == 0:
        c.send("System:\tHello, welcome to chatbot program. \nAre you importing messages from file? \nEnter only either \"yes\" or \"no\".".encode())
        counter += 1
    elif counter == 1:
        if data == "yes":
            c.send("System:\tImport file but currently not available. \nSystem:\tHello, are you male or female?".encode())
            counter += 1
        elif data == "no":
            c.send("System:\tHello, are you male or female?".encode())
            counter += 1
        else:
            c.send("System:\tPlease enter in the correct format ... \n".encode())
    elif counter == 2:
        if data == "female":
            c.send("System:\tHow excellent! Are you a CS major?".encode())
        elif data == "male":
            c.send("System:\tMe too. Are you CS major?".encode())
        else:
            c.send("System:\tGreat! Anyways, are you CS major?".encode())
        counter += 1
    elif counter == 3:
        if data == "no":
            c.send("System:\tToo bad. Anyway, what's an animal you like, and two you don't?".encode())
        elif data == "yes":
            c.send("System:\tExcellent, I am too. What's an animal you don't like, and two you don't?".encode())
        else:
            c.send("System:\tCool! By the way, what's an animal you like, and two you don't?".encode())
        counter += 1
    elif counter == 4:
        data1 = data.split(',')
        msg = "System:\t%s awesome, but i hate %s too. Bye for now." % (data1[0].strip(), data1[-1].strip())
        c.send(msg.encode())
        counter += 1
    else:
        c.send(''.encode())
    data = c.recv(1000).decode().strip()
c.close()
