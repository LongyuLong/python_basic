#oop(object oriented promgraming) : 객체 중심 프로그래밍 가능 -> 새로운 타입 생성, 포함, 상속, 다형성 등을 구사
#class(설계도)로 인스턴스 해서 객체를 생성(별도의 이름 공간을 갖음)
#객체는 멤버필드(변수)와 메소드로 구성
#모듈의 멤버 : 변수, 명령문, 함수, 모듈, 클래스
#함수는 행위만 있고 클래스는 속성과 행위가 있으며 다형성이 있음


print('뭔가를 하다가 객체 만들기')

class TestClass:                    ##부모 없으면 그냥 :
    aa = 1                          ##멤버필드(변수). 현재 클래스 내에서 전역(속성)

    def __init__(self):             ##__init__ : 자동 호출 초기화 담당  특별 메소드(행위)
        print('생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당')

    def __del__(self):              ##특별 메소드(행위)
        print('소멸자 : 프로그램 종료시 자동 실행. 마무리 작업')


    def printMsg(self):             ##일반 메소드(클래스 내에 함수), 메소드는 반드시 argument가 있어야 한다(self) : 자기 자신을 의미함
        name = '한국인'               ##지역변수 : printMsg에서만 유효
        print(name)


print(TestClass)                    ##type이 TestClass타입
test = TestClass()                  ##객체를 생성한 것, 생성자 호출 프로그램이 끝날때 소멸자 호출(callback), 인스턴스 화
print('test객체의 멤버 aa',test.aa)

##method call
test.printMsg()                     ##1. Bound Method call              .찍으면 argument 넣은걸로 인정
TestClass.printMsg(test)            ##2. UnBound Method call            .객체 변수(test)가 없으니까 넣어줘야 함

print(type(1))
print(type(1.0))
print(type(test))                   ##새로운 type(TestClass)
print(id(test))                     
print(id(TestClass))                ##두개의 객체가 만들어진것

test2 = TestClass()                 ##두번째 객체 생성
print(id(test2))
