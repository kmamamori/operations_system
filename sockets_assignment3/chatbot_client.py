#!/usr/bin/env python3
from socket import *
import sys
MLENGTH = 125
 
class MySocket:
 
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = sock
 
    def connect(self, host, port):
        self.sock.connect((host, port))
 
    def mysend(self, msg):
        self.sock.send(msg.encode('utf-8'))
 
    def myreceive(self):
        chunk = self.sock.recv(MLENGTH)
        chunk = chunk.strip()
        return chunk
 
    def myprepare(self,msg): # ensures that the message is of the right length
        while len(msg) < 100:
            msg = msg + ' '
        return msg
 
class ConsoleReader:
    def __init__(self):
        pass
    
    def get_next_line(self):
        return input()
 
class FileReader:
    def  __init__(self, filename):
        with open(filename) as f:
            content = f.readlines()
        self.file_lines = [x.strip() for x in content] 
 
    def get_next_line(self):
        return self.file_lines.pop(0)
 
def main():
    try:
        start_socket()
    except FileNotFoundError:
        print("File was not found")
 
def start_socket():
    s = MySocket()
    s.connect("localhost",7069)
    reader = get_reader()
    conversate(s, reader)
 
def get_reader():
    if len(sys.argv) == 1:
        return ConsoleReader()
    else:
        return FileReader(sys.argv[1])
 
def conversate(s, reader):
    response = s.myreceive()
    print(response.decode())
    while True:
        currentline = reader.get_next_line()
        currentline = s.myprepare(currentline)
        s.mysend(currentline)
        response = s.myreceive()
        print(response.decode())
main()
