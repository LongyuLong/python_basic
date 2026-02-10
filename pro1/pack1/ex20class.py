class Car :
    handle = 1                                                  # 클래스 내부에서 사용할 공유 자원들
    speed = 0                                                   # 공유자원 ㅇㅇ

    def __init__(self, name, speed):
        self.name = name                                        ##현재 객체의 name에게 name(지역변수) 인자값 치환
        self.speed = speed                                      ##self가 밑에서는 car1임 그래서 car1.name에 'tom'이 들어가는 것

    def showData(self):
        km = '킬로미터'
        msg = '속도 : ' + str(self.speed) + km
        return msg
    
    def printHandle(self):
        return self.handle                                      # self.handle로 해서 1이 나온게 아니고 외부에서 handle값을 바꿨을 때 그 객체에 대한 handle값이 반환된다.

print(Car.handle)                                               ##원형(prototype) 클래스의 멤버 호출
car1 = Car('tom', 10)                                           ##생성자 호출 후 객체 생성
print('car1 객체 주소:',car1)
print('car1 : ',car1.name, ' ', car1.speed, car1.handle)        ##핸들이 __init__에 없음 그래서 핸들이 없는 놈임. 그럼 class내 전역으로 감 따라서 0
car1.color = "파랑"                                             # color같은건 없었지만?
print('car1.color = ',car1.color)                               # car1.color =  파랑 으로 나온다. >> 외부에서도 추가할 수 있다.


car2 = Car('john', 20)
print('car2 : ',car2.name, ' ', car2.speed, car2.handle)        # car1, car2에 입력된건 name과 speed 뿐이지만 handle에 대한 초기값은 기본적으로 내포하고있으므로 반환 가능하다
print('car2 객체 주소:',car2)
# print(Car.color, ' ', car2.color)                             # AttributeError: type object 'Car' has no attribute 'color'
                                                                # 각 개체에 고유 멤버를 추가할 수 있으나 다른 객체들에 영향을 끼치지 못함. (당연하지만;)

print(Car,car1,car2)                                            # <class '__main__.Car'> <__main__.Car object at 0x0000024F91A57230> <__main__.Car object at 0x0000024F91B911D0>
                                                                # 
print(id(Car), id(car1), id(car2))                              # 2540772427392 2540769210928 2540770496976 , 각자 다른 주소를 갖는다.
print(car1.__dict__)                                            # 클래스 객체 내부 살펴보는 법
print(car2.__dict__)

print('-------------메소드----------------')
print('car1 speed: ',car1.showData())                           # showData() 괄호 안에 아무것도 안넣었지만 car1이 알아서 들어간다(?). 그리고 car1.showData에 대해서 따로 정의하지도 않았지만 클래스 생성하면서 만들어지는듯?
print('car2 speed: ',car2.showData())                           # 클래스 정의하면서 showData(self)로 되어있으니 알아서 car1, car2에 따라 잘 가져온다

car1.speed = 80
car2.speed = 110
print('car1 speed: ',car1.showData())  
print('car2 speed: ',car2.showData())  

car1.handle = 2

print('car1 handle: ',car1.printHandle())                       # public, private 개념이 있는데, .을 찍었을 때 보이면 public 안보이면 private
print('car2 handle: ',car2.printHandle())




