# 오버라이딩: 결제 시스템

class Payment:
    def pay(self, amount):
        print(f'{amount}원 결제 처리')

# Payment의 자식은 결제를 pay()라는 동일 메소드를 이용하기를 기대한다.
# 동일한 인터페이스 구사

class Card(Payment):
    # Card만의 고유 멤버/메소드 ... 
    # 
    def pay(self, amount):
        print(f'{amount}원 카드 결제 승인 완료')

class Cash(Payment):

    def pay(self, amount):
        print(f'{amount}원 현금 결제 완료')

payments = [Card(), Cash()]                                         # 리스트의 요소로 Card 클래스, Cash 클래스의 객체 넣었다

for p in payments:
    p.pay(5000)                                                     # 같은 이름으로 실행, 다른 결과 출력. << 다형성











