# socket2_server.py

import socket
import sys

# host = '127.0.0.1'
host = ''                                                   # 알아서 자기 컴퓨터의 IP가 들어간다.
port = 7788

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((host,port))
    serversock.listen(5)
    print('서버(무한 루핑) 서비스 중..')

    while True:
        conn, addr = serversock.accept()
        print('client info: ', addr[0], ' ', addr[1])       
        print(conn.recv(1024).decode())                     # 수신 메세지 출력
        # 클라이언트에게 메세지 송신
        conn.send(('from server: ' + str(addr[1]) + '나도 반가워').encode('utf_8'))

except Exception as err:
    print('err: ',err)
    sys.exit                                                # 오류 발생하면 강제 종료
finally:
    serversock.close()
