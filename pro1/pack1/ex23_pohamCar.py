# 여러 개의 부품 객체를 조립해서 완성차를 만든다
# class의 포함 관계 사용 (자원의 재활용이 목적)
# 다른 클래스(객체,object)를 마치 자신의 멤버처럼 선언하고 사용할 수 있다
# class, 객체(object), instance 를 구분할 수 있어야함

from ex23_pohamHandle import PohamHandle

class PohamCar():
    turnShowMessage = "정지"

    def __init__(self, ownerName):
        # ownerName = ownerName 과 어떻게 다른지 설명가능해야함
        self.ownerName = ownerName
        self.handle = PohamHandle()             # 클래스의 포함관계 -- 이렇게 처리하면 PohamHandle이 PohamCar에 포함된다고 본다?
    
    def turnHandle(self, q):                    # pohamHandle에선 quentity지만 여기선 q
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q)            # 본래 argument가 2개(self, quentity)였으나 여기서 q 하나로 줄여도 되는이유?
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = "직진"


if __name__ == '__main__':                                  # 하단에서 PohamCar가 아닌 PohamHandle을 사용했다면 __name__ = 'ex23_pohamHandle'이 된다. 그럼 실행이 안되는거지. pohamCar가 이 모듈안에 있으니까 __name__이랑 __main__이랑 같은거고
    tom = PohamCar('Mr. Tom')
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은 ' +tom.turnShowMessage + ' ' + str(tom.handle.quantity)) # quantity는 정수형인데, print()내부에서 문자열과 숫자를 +로 연결하려면 숫자를 문자열로 변경해줘야함
    
    john = PohamCar('Mr. john')
    john.turnHandle(-30)
    print(john.ownerName + '의 회전량은 ' +john.turnShowMessage + ' ' + str(john.handle.quantity)) # quantity는 정수형인데, print()내부에서 문자열과 숫자를 +로 연결하려면 숫자를 문자열로 변경해줘야함
    














