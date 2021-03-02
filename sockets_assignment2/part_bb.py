import socket
if socket.ntohs(256) == 1:
    print("Little endian because socket.ntohs(256) =", socket.ntohs(256))
else:
    print("big endian because socket.ntohs(256) =", socket.ntohs(256))

if socket.htons(256) == 1:
    print("Little endian because socket.htons(256) =", socket.htons(256))
else:
    print("big endian because socket.htons(256) =", socket.htons(256))
