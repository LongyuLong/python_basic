# 메소드 오버라이딩(재정의) // 메소드 : 클래스 안에 정의된 함수
# 부모에서 이미 정의된 메소드를, 자식 클래스에서 동일한 이름의 메소드를 재정의해 사용한 경우
# 부모 메소드의 기능을 대체하는 기능. 
# 목적: 동작의 구체화(공통 틀은 부모가, 실제 행동은 자식이) - 예: Animal.sound() → "소리낸다", Dog.sound() → "멍멍", Cat.sound() → "야옹
# 다형성(Polymorphism) 구현 - 같은 메소드이나 객체에 따라 다른 기능을 수행
# 확장 및 유지보수에 도움 - 부모 코드는 유지한 채 자식의 세부 동작만 변경이 가능하다.

class Parent:
    def printData(self):
        print("Parent의 printData")

class Child1(Parent):
    def abc():
        print("Child1 고유 메소드")
    
    def printData(self):                                        # 메소드 오버라이딩
        a = 5 + 6
        # ...
        print("Child1에서 printData 재정의")                    

class Child2(Parent):
    def abc():
        print("Child2 고유 메소드")
    
    def printData(self):                                        # 메소드 오버라이딩
        print("Child2에서 printData 재정의(override)")                    
        msg = "부모와 동일한 이름의 메소드지만 내용은 다르다"
        print(msg)

print("--Parent--")
p1 = Parent()
p1.printData()
print("--Child1--")
c1 = Child1()
c1.printData()
print("--Child2--")
c2 = Child2()
c2.printData()

print("\n\n---다형성---")                                       

par = Parent()                                                  # 아래처럼 해도 되지만 이와같이 하는게 권장사항이긴하다.
par = c1
par.printData()
print()
par = c2
par.printData()
print("--------------------------")

imsi = c1                                                       # 파이썬은 이렇게 해도 되는데, java에서는 안된다
imsi.printData()
imsi = c2
imsi.printData()












