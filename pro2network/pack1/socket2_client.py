# client 

from socket import *                       # = import socket

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 7788))    # 서버에서 listen 중, 능동적 연결 시도
clientsock.send('안녕 반가워'.encode(encoding='utf_8', errors='strict'))

print('수신 자료:', clientsock.recv(1024).decode())

clientsock.close()

