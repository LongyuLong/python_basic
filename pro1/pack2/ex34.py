print("---------파일 처리 ---------")

import os

try:
    print("---------파일 읽기")
    print(os.getcwd())                      # 자신의 로컬주소 반환 / C:\work\projects\pro1\pack2
    f1 = open(os.getcwd() + r"\ftext.txt", encoding='utf-8')  # 
    # f1 = open(r"C:\work\projects\pro1\pack2", encoding='utf-8')  # 절대경로로 써도 되지만 굳이
    # f1 = open("ftext.txt", encoding='utf-8')
    f1 = open("ftext.txt", mode='r', encoding='utf-8') # mode = 'r'(read), 'w'(write), 'a'(append), b ... 모드 언급 안하면 기본값은 읽기(r)
    print(f1)
    print(f1.read())
    f1.close()                                              # open 한 뒤에는 close 해줘야함

    print("---------파일 저장")
    f2 = open("ftext.txt", mode = 'w', encoding='utf-8')
    f2.write('내 친구들\n')
    f2.write('홍길동, 한국인')
    f2.close()
    print("----------파일 저장 성공")

    print("파일 내용 추가 ------")
    f3 = open("ftext2.txt",mode='a', encoding='utf-8')
    f3.write("\n사오정")
    f3.write("\n저팔계")
    f3.write("\n손오공")
    f3.close()
    print("----------내용 추가 성공")

    f4 = open("ftext2.txt", mode = 'r', encoding='utf-8')
    print(f4.read())
    f4.close()

except Exception as e:
    print('파일 처리 오류: ',e)





