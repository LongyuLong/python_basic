# 상속

class Person:
    say = '난 사람이야~~'
    nai = '20'
    __msg = '★ good: private member'                          # __변수 = private member. 현재 클래스 내부에서만 인식된다.

    def __init__(self, nai):                                # Person의 생성자는 2개. self는 자동으로 들어가고, nai는 입력해줘야함
        print('Person 생성자')
        self.nai = nai

    def printInfo(self):                                    # 접근 권한: public >> 클래스 외부에서도 호출 가능함을 의미
        print(f'나이: {self.nai}, 이야기: {self.say}')

    def helloMethod(self):
        print("안녕")
        print('hello: ', self.say, self.nai, self.__msg)    # self.__msg는 Person 클래스 내부에서만 사용되는 private member이므로 여기선 인식이 가능하다.
    
# print(Person.say, Person.nai)
# Person.printInfo()

per = Person('25')
per.printInfo()
per.helloMethod()

print("---------"*10)

class Employee(Person):
    subject = '근로자'
    say = '일하는 동물'                                      # 여기 say를 추가하면 Person에 있던 say: 사람이야~ 까지 안가고 여기서 출력
                                                            # hiding(shadowing)
    def __init__(self):
        print('Employee 생성자')

    def ePrintInfo(self):
        print(self.subject, self.say, self.nai)
        # print(self.__msg)                                   여기서 에러 발생하는데, __msg 는 private member이므로 자식 클래스라고 하더라도 가져다 쓸 수 없음
        print()
        self.helloMethod()                                  # Employee 내부에 helloMethod 없으니까 부모로 감
        print()
        self.printInfo()
        print(super().say)                                  # self.say로 하면 현재 클래스에서 가져오고, super().say로 가면 상위 클래스로 이동해서 say 찾는다
        super().printInfo()                                 # 따라서 일하는 동물 이 아니고 난 사람이야~ 가 출력된다.
                                                            # super()."부모의 멤버"
                                                            # 할아버지, 아빠, 나 로 구성된 클래스 계보? 에서 나 -> 할아버지로 가려면 super().super 따위같은거 없고 못함그냥

    def printInfo(self):                                    # 접근권한 : public
        print("Employee 클래스의 printInfo 호출됨")


emp = Employee()                                            # 인스턴스 생성  << 맞고
# print(emp.subject, emp.nai, emp.say)                      # 인스턴스 변수 프린트 << 틀림. 인스턴스 변수가 아니고 클래스 변수다. self.nai 처럼 만들어야 인스턴스변수다.
emp.ePrintInfo()

print("------"*10)

class Worker(Person):
    def __init__(self, nai):                                # 알아서 이렇게 만들어주긴하는데, 이해가 필요할듯? person을 부모로 지정한 이상 무조건 이렇게 써야하나?
        print('worker 생성자')                              # 자식 클래스에서 생성자를 새로 정의하면 부모 생성자가 자동 호출되지 않으므로, 부모의 초기화가 필요할 때는 super().__init__(...)로 직접 호출해야 합니다.
                                                            # 자식이 생성자를 정의하지 않으면 부모 생성자가 그대로 실행됩니다.
        super().__init__(nai)                               # 부모의 생성자 호출

    def wPrintInfo(self):
        print('Worker - wPrintInfo 처리')
        # self.printInfo()                                    굳이 이렇게 쓸 필요없음. 돌아가긴하겠지만
        super().printInfo()

pro = Worker('30')                                              # worker 역시 부모를 Person으로 하기 때문에 nai를 argument로 요구한다.
print(pro.say, pro.nai)
pro.wPrintInfo()

print('====='*10)

class Programmer(Worker):
    def __init__(self, nai):                                # Worker의 생성자를 불러왔는데, Person의 생성자와 형태가 같다. 하지만 Person이랑은 관련이 없다
        print('Programmer 생성자')
        # super().__init__(nai)                             # Bound call
        Worker.__init__(self, nai)                          # Unbound call

    def pPrintInfo(self):
        print("Programmer - pPrintInfo 처리하였음")

    def wPrintInfo(self):                                   # 부모 메소드와 동일 메소드 선언 // 굉장히 중요하다에요
        print("Programmer에서 Overriding")
    
wor = Worker('30')
print(wor.say, wor.say)
wor.wPrintInfo()

pro = Programmer(35)
print(pro.say, pro.nai)
pro.pPrintInfo()
pro.wPrintInfo()

print("\n\n클래스 타입 확인")
a = 3; print(type(a))
print(type(wor))
print(Person.__bases__)                                     # Person의 base. 부모를 확인한다. 모든 클래스의 super class는 object 이다. << 뭔말인지모르겟네
print(Employee.__bases__)
print(Worker.__bases__)
print(Programmer.__bases__)
