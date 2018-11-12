import socket

s = socket.socket()
host = socket.gethostname()
print(host)
port = 9077
s.connect((host, port))
print(s.recv(1024).decode("utf-8"))