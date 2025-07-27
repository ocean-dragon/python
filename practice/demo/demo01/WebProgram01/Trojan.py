from socket import *

s = socket()

s.connect(("127.0.0.1", 8899))

choice = s.recv(1024).decode()

print(choice)
