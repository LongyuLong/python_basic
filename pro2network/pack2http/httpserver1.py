# 단순한 HTTPServer 구축

from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 7777
handler = SimpleHTTPRequestHandler              # get 요청에 대해 문서를 읽어와 클라이언트로 전송하는 역할

# HTTP서버 객체 생성
serv = HTTPServer(('127.0.0.1', PORT), handler)             
print('웹 서비스 시작..')

serv.serve_forever()                            # 웹서비스 무한루핑
