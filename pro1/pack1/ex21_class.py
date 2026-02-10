kor = 100                           # 모듈의 전역 변수

def abc():
    kor = 0                         # 함수 내의 지역 변수
    print('모듈의 멤버 함수')

class My:
    kor = 80                        # My 멤버 변수(필드)

    def abc(self):                  # 메소드라고 표현하는게 self 자체인듯
        print('My 멤버 메소드')

    def show(self):
        kor = 77                    # 이 줄을 주석처리하면
        print(kor)                  # 여기서 100을 출력한다. >> 지역 변수가 없어지면 모듈멤버 100으로 간다. 80이 찍히려면 self.kor 사용
        print(self.kor)             # kor=77을 주석처리 안했을 때 이건 왜 80이 찍히냐
        self.abc()                  # my 멤버 메소드 출력
        abc()                       # 모듈의 멤버함수 출력

my = My()
my.show()

# print('-----------------')

# print(My.kor)
# tom = My()
# print(tom.kor)
# tom.kor = 88
# print(tom.kor)

# oscar = My()
# print(oscar.kor)



