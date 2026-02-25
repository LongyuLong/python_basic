import sys
sys.stdout.reconfigure(encoding='utf-8')

ss = "파이썬 자료 출력"
# print(ss) 개발자가 자신의 터미널로 값 확인
ss2 = 123 + 5
# 클라이언트의 브라우저로 출력

print('Content-Type:text/html;charset=utf-8')
print()
print("<html><head><meta charset='UTF-8'></head><body>")
print("<b>안녕. 파이썬 모듈로 작성한 문서야</b><br/>")
print("파이썬 변수 ss의 값: %s"%(ss,))                  # 튜플 주의!
print("<br/>파이썬 변수 ss2의 값: %d"%(ss2,))           # 튜플 주의!, %s:string, %d:decimal 상관없긴함
print("</body></html>")
