import os
import sqlite3
from socket import *
import pickle

conn = sqlite3.connect("testdb.db")

host = gethostname()
port = 13001    # For receiving requests from client
port2 = 13000   # For responding to user's request
buf = 1024
addr = (host, port)
addr2 = ('172.21.4.255', port2)
print(host)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock2 = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
# UDPSock2.bind(addr2)
print("Waiting to receive messages...")
while True:
    data, addr = UDPSock.recvfrom(buf)
    print("Received message: " + data.decode("utf-8"))
    if data == "exit":
        break
    query = data.decode("utf-8")
    b = query.split(" ")
    result = conn.execute(query)
    if b[0] == "select" or b[0] == "SELECT":
        a = []
        for x in result:
            for y in x:
                a.append(int(y))
        print(a)
        sending_data = pickle.dumps(a)
        UDPSock2.sendto(sending_data, addr2)
    else:
        conn.execute("commit;")
        UDPSock2.sendto(pickle.dumps("OK"), addr2)
UDPSock2.close()
UDPSock.close()