# ## python - 연습문제 : 클래스


# 2. 클래스의 상속 관계 연습문제 - 다형성

class ElecProduct:
    volume = 0

    def volumeControl(volume):
        pass


class ElecTv(ElecProduct):
    
    def volumeControl(self,volume):
        print(f"{volume}까지 볼륨 업/다운 스위치 조작")

class ElecRadio(ElecProduct):
    
    def volumeControl(self,volume):
        sori = volume
        print(f"{sori}까지 볼륨 다이얼 조작")                       # 굳이굳이 변수 변경해도 잘 돌아간다.

Elec = [ElecTv(), ElecRadio()]

for E in Elec:
    E.volumeControl(30)

# product = ElecProduct()
# tv = ElecTv()
# product = tv
# product.volumeControl(30)                                       # 이런식으로 해도되긴하는데 굳이 싶다

print("\n\n\n3번문제\n")

# 3. 다중 상속 연습문제

# 부모 Animal:  move()
# 자식 Dog: +name = "개" +move(), Cat: +name = "고양이" +move()
# 3세대 Wolf: pass / Dog, Cat 상속, Fox: +move(), +foxMethod()

class Animal:                                                       # Animal의 경우 추상 클래스로 취급할 수도 있다.
                                                                    
    def move(self):
        print("동물 공통")

class Dog(Animal):
    # Field
    name = "개"

    # Method
    def move(self):
        print("탁탁탁탁")

class Cat(Animal):
    name = "고양이"

    def move(self):
        print("음소거")

class Wolf(Dog, Cat):
    pass
    
class Fox(Cat, Dog):

    def move(self):
        print("살금살금")

    def foxMethod(self):
        print("여우 메소드")

animal = [Dog(), Cat(), Wolf(), Fox()]

for a in animal:
    print(a, a.move(), a.name)

fox = Fox()
fox.foxMethod()

# 4. 추상 클래스 연습문제
# Employee 에 Temporary, Regular 가 묶이고, Regular에 Salesman이 묶인다.
# Employee: irum=이름, nai=나이, abstract pay(), abstract data_print(), irumnai_print() // 
# ** 이름 나이 는 employee에만 만든다, 계산 또한 Employee의 pay에서만 수행한다. 
# Temporary: ilsu=일수, ildang=일당, 이름, 나이, 월급(일수*일당) 출력
# Salesman : sales = 실적, commission = 수수료율(0.25) // 

from abc import *
import math

class Employee(metaclass=ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def data_print(self):
        pass

    def irumnai_print(self):
        print('이름: '+ self.irum + ', 나이: ' + str(self.nai), end = ' ')

class Temporary(Employee):
    def __init__(self,irum,nai,ilsu,ildang):
        # self.irum = irum                                                          # 틀림    
        # self.nai = nai                                                            # 틀림
        Employee.__init__(self, irum, nai)                                          # 이게맞다
        self.ilsu = ilsu
        self.ildang = ildang
        # self.pay()                                                                # 틀림
        # self.data_print()

    def pay(self):
        return self.ilsu * self.ildang                                              
    def data_print(self):
        super().irumnai_print()
        print(', 월급: ' + str(self.pay()))

t=Temporary('홍길동',25,20,150000)


class Regular(Employee):
    def __init__(self,irum,nai,salary):
        Employee.__init__(self,irum,nai)
        self.salary = salary
        # self.pay()                                                                 
        # self.data_print()

    def pay(self):
        return self.salary 
        
    def data_print(self):
        super().irumnai_print()
        print(', 급여: ' + str(self.pay()))

r = Regular('한국인', 27, 3500000)



class Salesman(Regular):
    def __init__(self,irum,nai,salary,sales,commission):
        Employee.__init__(self,irum,nai)
        self.salary = salary
        self.sales = sales
        self.commission = commission

    def pay(self):
        return super().pay() + (self.sales * self.commission)

    def data_print(self):
        super().irumnai_print()
        print('수령액: ' + str(self.pay()))


s = Salesman('손오공',29,1200000, 5000000, 0.25)


print("\n--Temporary--")
t.data_print()
print("\n--Regular--")
r.data_print()  
print("\n--Salesman--")
s.data_print()








