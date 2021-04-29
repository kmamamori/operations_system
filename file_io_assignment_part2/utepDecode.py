#!/usr/bin/python3
# utepDecode.py
# Nigel Ward, UTEP, April 2021

import sys
bufferSize = 512
key = b'uteputep'

# assumes that the position is just after the key
def  processUtep(occurrence):
    global expectedKeyCount, payloadLength
    if occurrence == 1:
        expectedKeyCount = int(f.read(3))  # a 3-digit number
        print('expectedKeyCount is %d' % expectedKeyCount)
        return
    elif occurrence == 2:
        payloadLength = int(f.read(3)) # a 3-digit number
        print('payloadLength is %d' % payloadLength)
        return 
    elif occurrence == expectedKeyCount - 1:
        print('the secret is `%s\' ' % f.read(payloadLength).decode())
        exit(0)
    else:
        return

def seekUtepInBuffer(buffer, f):   # side effect: changes the position 
    global key 
    bufferLen = len(buffer)
    for i in range(bufferLen - len(key)):
        if buffer[i] == key[0]:
            #print('found %c at %d starting %s ' %(buffer[i], i, buffer[i:i+len(key)]))
            if buffer[i:i+len(key)] == key:
                #print('spotted %s at %d ' % (key, i))
                f.seek(len(key) + i - bufferLen, 1)  # seek backwards
                #print('position is now ' + str(f.tell()))
                return True
    f.seek(-len(key), 1)  
    return False


if len(sys.argv) < 2:
    print("usage: utepDecode filename")
    exit(-1)
codeFile = sys.argv[1]
keysSeen = 0

with open(codeFile, 'rb') as f:
    #print('bufferSize is %d' % bufferSize)
    while(1):
        #print('refilling the buffer... ', end='')
        buffer = f.read(bufferSize)
        #print('read %d bytes' % len(buffer))
        if buffer == b'':  #  end of file
            exit(0) 
        if seekUtepInBuffer(buffer, f):
            keysSeen += 1
            processUtep(keysSeen)



"""
buffer = 512
key = b'uteputep'

f1 = open file
f2 = open file
i1 = 0
i2 = 0
f1_o = 0
f2_o = 0

do-while i1 is less than i2 = (i1<i2)
    if data1 = key
        f1_o ++
    if f1_o is -1
        pass
    elif f1_o is not 2
        data1 = f1.seek(-len(key), 1)
    else
        data1 = f1.seek(-3, 1)
        f1_o = -1

    if data2 = key
        f2_o ++
    if f2_o is -1
        pass
    elif f2_o is not 2
        data2 = f2.seek(len(key), 1)
    else
        if f1_o is 2 or f1_o is -1
            data2 = f2.seek(-data1, 1)
            return data2
do
    data1 = f1.seek(-len(key))
    data2 = f2.seek(len(key), 2)
    function(data1)
    function(data2)




"""

