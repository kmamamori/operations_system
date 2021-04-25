#!/usr/bin/python3
# utepEncode.py
# Nigel Ward, UTEP, April 2021

import random, string, sys

def writeGarbage():
    global averageInterpolationSize
    alphabet = string.ascii_letters + ' 0123456789.,+=!@#$%^&*()-_|\?/><[]}{`\~|'
    sizeRatio = 0.1 + 1.8 * random.random()  # betwen 0.1 and 1.9
    for i in range(int(averageInterpolationSize * sizeRatio)):
            sys.stdout.write(random.choice(alphabet))

def printKey():
    sys.stdout.write('uteputep')


if len(sys.argv) < 4:
    print("usage: utepEncode secret keyCount interpolationSize")
    exit(-1)
secret = sys.argv[1]
keyCount = int(sys.argv[2])
averageInterpolationSize = int(sys.argv[3])

writeGarbage()
printKey()
sys.stdout.write('%03d' % keyCount)

writeGarbage()
printKey()
sys.stdout.write('%03d' % len(secret))

for i in range(keyCount - 4):
   writeGarbage()
   printKey()

writeGarbage()
printKey()
sys.stdout.write(secret)

writeGarbage()
printKey()
writeGarbage()

   
