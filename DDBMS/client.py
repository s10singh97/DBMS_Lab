import os
from socket import *
host = "172.21.4.55" # set to IP address of target computer
port = 13000
addr = (host, port)
addr1 = ("", 13001)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data.encode("utf-8"), addr)
    result, addr1 = UDPSock.recvfrom(1024)
    print(result)
    if data == "exit":
        break
UDPSock.close()