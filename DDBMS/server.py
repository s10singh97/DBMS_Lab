import os
import sqlite3
from socket import *

conn = sqlite3.connect("testdb.db")

host = gethostname()
port = 13001
buf = 1024
addr = (host, port)
print(host)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
while True:
    data, addr = UDPSock.recvfrom(buf)
    print("Received message: " + data.decode("utf-8"))
    if data == "exit":
        break
    query = data.decode("utf-8")
    result = conn.execute(query)
    conn.execute("commit;")
    for row in result:
        print(row)
    # UDPSock.sendall(result.encode("utf-8"))
UDPSock.close()