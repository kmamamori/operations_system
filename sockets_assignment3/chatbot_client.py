#!/usr/bin/env python3
from socket import *
import sys
MLENGTH = 125

class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MLENGTH:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MLENGTH:
            chunk = self.sock.recv(min(MLENGTH - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

    def myprepare(self,msg):
        msg = 'X' +msg
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

#def send_message(message): 
#   totalsent = 0
#    while totalsent < MLENGTH:
#        sent = s.send(message[totalsent:])
#        if sent == 0:
#            raise RuntimeError("socket connection broken")
#        totalsent = totalsent + sent

#def recieve_message():
#    chunks = []
#    bytes_recd =0

 # probably here recieve the message length and then recieve the rest of the stuff
#    while bytes_recd <MLENGTH:
#        chunk = s.recv(min(MLENGTH-bytes_recd, 2048))
#        if chunk ==b'':
#            raise RuntimeError("socket connection broken")
#        chunks.append(chunk)
#        bytes_recd = bytes_recd +len(chunk)
#    return b''.join(chunks)

#def prepare_message(message):
#   message = 'X' +message
#    while len(message) < 100:
#        message = message + ' '
#    return message

def main():
    try:
        start_socket()
    except FileNotFoundError:
        print("File was not found")
    except IndexError:
        print("File has not enought lines to conversate")
    except BaseException:
        print("No valid arguments")

def start_socket():
    s = MySocket()
    s.connect("localhost",7069)
    reader = get_reader()
    conversate(s, reader)

def get_reader():
    if len(sys.argv) == 2:
        return ConsoleReader()
    
        return FileReader(sys.argv[1])    
    raise BaseException


def conversate(s, reader):
    while True:
        currentline = reader.get_next_line()
        currentline = s.myprepare(currentline)
        s.send_message(currentline)
        s.mysend(currentline)
        response = s.myreceive()
        print(response.decode)
    





main()