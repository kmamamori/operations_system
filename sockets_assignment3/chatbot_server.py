# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:49:51 2021

@author: elisa
"""
from socket import *
import time
s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 7069))
s.listen(5)
while True:
    c,a = s.accept()
    print("Received connection from" , a)
    
    c.send(b"Hello, are you male or female?")
    sex = c.recv(128).decode()
    if sex.upper() == "MALE":
        c.send(b"Me too. Are you a CS major?")
    else:
        c.send(b"How excellent! Are you a CS major?")
    x = c.recv(128).decode()
    is_cs_major = x.upper()=="YES"
    if is_cs_major:
        c.send(b"Excellent, I am too. What's an animal you don't like, and two you do?")
    else:
        c.send(b"Too bad. Anyway, what's an animal you don't like, and two you do?")
    x = c.recv(128).decode()
    try:
        disliked_animal, liked_animal_1, liked_animal_2 = x.replace('and ', '').replace(', ', ',').split(",")
        c.send(("%s: awesome.  But I hate %s too.  Bye for now." % (liked_animal_2, disliked_animal)).encode())
    except ValueError:
        c.send(b"I asked for 3 animals! Oh well, goodbye.")
    c.close()