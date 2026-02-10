# 상속 : 자원의 재활용을 목적으로 특정 클래스의 멤버
# 코드 재사용
# 확장성 : 기존 클래스 새 기능을 추가한 새로운 클래스 생성
# 구조적인 설계 가능 : 공통 개념은 부모 클래스, 구체적 내용은 자식 클래스에서 구현
# 다형성(같은 메서드 호출이라도 객체의 실제 타입에 따라 다른 결과를 내는 것) 구사 : 메소드 오버라이딩(부모 클래스에서 정의한 메서드를 **자식 클래스에서 같은 이름으로 다시 정의(재정의)**하는 것.)


class Animal:                               # 동물들이 가져야할 공통 속성과 행위 선언
    age = 1
    
    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print('움직이는 생물')



class Dog(Animal):                          # '상속'하려면 ()안에 부모 클래스를 넣는다.
    def __init__(self):
        print('Dog 생성자')

    def my(self):
        print("댕댕이라고 해요")

    # def move(self):
    #     print("여기도있음")

dog1 = Dog()
dog1.my()
dog1.move()                                 # 일단 dog1 내부에서 move찾고 없으면 부모 클래스로 올라가서 찾는다.
print()
print('age: ',dog1.age)                     # 상속받은 클래스 내부의 변수들도 불러다 쓸 수 있음
                                            # 부모: super(python문법) // 자식: 자손 파생 sub, child (??)
                                            # 클래스 간의 결합은 상속(강결합), 포함(약결합)의 경우가 있는데 상속은 다형성을 가능하게 한다 // 뭐가 더 좋은지는 모르겠고

dog2 = Dog()
dog2.my()
dog2.move()
print()

# class Horse:
#     pass
# horse1 = Horse
# horse1.                                   # 이렇게 작성하면 클래스는 형성돼있지만 . 을 찍었을 때 연관된게 안나온다. 하지만 괄호안에 animal이든 dog이든 부모 클래스 써주면 또 뜬다  

class Horse(Animal):
    pass
horse1 = Horse()
horse1.age




# from ex27_inheritance import Animal











