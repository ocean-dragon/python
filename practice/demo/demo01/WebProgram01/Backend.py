from socket import *

# 创建套接字对象
S = socket()
# 将套接字对象绑定ip和端口
S.bind(("0.0.0.0", 8899))
# 开始监听socket
S.listen()
# 接收到请求后，获取已建立连接的socket对象
s, addr = S.accept()

print(s)

print("1. shutdown    2. restart")
choice = input("select your choice:")
s.send(choice.encode())
