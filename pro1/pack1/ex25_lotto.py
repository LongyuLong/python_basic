import random

class LottoBall:
    def __init__(self, num):
        self.num = num                                  # 입력된 num에 따라 각 객체가 고유의 num값을 갖는다

class LottoMachine:
    def __init__(self):
        self.ballList = []                              # set({})으로 주면 순서가 없어서 곤란?
        for i in range(1,46):
            self.ballList.append(LottoBall(i))          # 1-45까지 로또 볼 생성, 리스트에 추가 // LottoBall 클래스를 포함한다~

    def selectBalls(self):
        # for a in range(45):
        #     print(self.ballList[a].num, end = ' ')
        # print()
        # print('------------------------------')
        random.shuffle(self.ballList)                   # 번호 섞어주기    
        # for a in range(45):
        #     print(self.ballList[a].num, end = ' ')
        return self.ballList[0:6]

class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()                   # LottoUI가 가져와 쓰는거니까 포함관계, 불러올 때 class로서 불러오는게 아니라 
                                                        # 인스턴스(객체)로서 불러오도록 뒤에 () 필수

    def playLotto(self):
        input('로또를 시작하려면 엔터키를 누르세요')       # 아무거나 눌러도 상관없음
        selectedBalls = self.machine.selectBalls()
        for ball in selectedBalls:
            print("%d"%(ball.num))



if __name__=='__main__':
#     machine = LottoMachine()
#     print(machine.selectBalls()
    lot = LottoUI()
    lot.playLotto()