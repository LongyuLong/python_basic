# 어딘가에서 필요한 부품. 핸들 클래스 작성

class PohamHandle:
    quantity = 0                        # 핸들의 회전량이라고 하자.

    def leftTurn(self, quentity):       # quentity 자리가 argument인데 여기서 a를 쓰든 quantity를 쓰든 상관없는거아닌가 아래쪽에서 통일만 시켜주면
        self.quantity = quentity
        return "좌회전"
    
    def rightTurn(self, quentity):
        self.quantity = quentity
        return "우회전"
    

