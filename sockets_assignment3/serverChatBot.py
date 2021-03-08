#!/usr/bin/env python3
from socket import *
import time
MLENGTH =125


def mysend(c,msg):
    totalsent = 0
    c.send(msg.encode('utf-8'))

def myreceive(c):

    chunk = c.recv(MLENGTH)
    chunk = chunk.decode()
    chunk = chunk.strip()
    return chunk

def myprepare(msg):
    while len(msg) < 100:
        msg = msg + ' '
    return msg
    
def start_conversation(c):
    response = ask_for_gender(c)
    response = ask_for_major(c, response)
    response = ask_for_favorite_animals(c, response)
    send_animal_response(c, response)
        
def ask_for_gender(c):
    message = myprepare("Hello, are you male or female?")
    mysend(c, message)
    answer = myreceive(c)
    return answer

def ask_for_major(c, answer):
    if answer == "female":
        message = myprepare("How excellent! are a CS major?")
    elif answer == "male":
        message = myprepare("Me too. Are you a CS major?")
    else:
        message = myprepare("really good! Are you a CS major?")
    mysend(c,message)
    answer = myreceive(c)
    return answer

def ask_for_favorite_animals(c, answer):
    if answer == "no":
        message = myprepare("too bad. Anyway, what's an animal you like, and two you don't?")
    elif answer == "yes":
        message = myprepare("Excellent, I am too. What's an animal you don't like, and two you do?")
    else:
        message = myprepare("Ok then, what's an animal you like and two you don't?")
    mysend(c, message)
    answer = myreceive(c)
    return answer

def send_animal_response(c, answer):
    answer_list = answer.split(" ")
    message = myprepare(answer_list[0] + " awesome, but I hate " + answer_list[-1])
    mysend(c,message)
    c.close()


s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 7069))
s.listen(5)
while True:
    c,a = s.accept()
    print("Received connection from" , a)
    start_conversation(c)

