# 일회용 서버
from socket import *

# socket 객체 생성
serversock = socket(AF_INET, SOCK_STREAM)       # Address Family - AF_INET

# 소켓을 특정 객체와 바인딩
serversock.bind(('127.0.0.1', 8888))            # 자신의 IP 192.168.0.84를 사용해도 된다
serversock.listen(5)                            # client와 연결 정보수. 리스너 설정

print("서버 서비스 중..")

conn, addr = serversock.accept()                # 수동적으로 연결을 받아들임
print('client addr: ', addr)
print('from client message: ', conn.recv(1024).decode())

conn.close()
serversock.close()
