# 클래스의 다중 상속 - 부모가 복수

class Tiger:

    data = "호랑이"

    def cry(self):
        print("호랑이: 어흥")

    def eat(self):
        print("호랑이는 고기를 좋아함")

class Lion:
    
    data = "사자"

    def cry(self):
        print("사자: 으르렁")

    def hobby(self):
        print("사자는 낮잠이 취미")


class Liger1(Tiger, Lion):                          # 다중 상속
    pass

a1 = Liger1()
print(a1.data)                                      # Tiger, Lion 양측에 data를 모두 선언해뒀는데 앞뒤 순서에 따라 우선시
a1.eat()
a1.cry()                                            # 위의 data와 마찬가지로 괄호 안의 순서에 따라 우선순위 결정
a1.hobby()

print('--------------------------')

def hobby():
    print('모듈의 멤버: 일반 함수')

class Liger2(Lion, Tiger):
    data = "라이거 만세"                             # 쉐도잉

    def play(self):
        print('라이거 고유 메소드입니다.')

    def hobby(self):                                # Lion의 메소드 오버라이딩
        print('라이거는 공원 걷기를 좋아함')

    def showData(self):
        self.hobby()
        super().hobby()
        hobby()                                     # 35행의 hobby() -> 모듈의 멤버인 일반 함수

        self.eat()
        super().eat()
        
        print(self.data + ' ' + super().data)



a2 = Liger2()
print()
print(a2.data)                                      
print()
a2.play()
print()
a2.hobby()                                            
print()
a2.showData()
a2.cry()


















