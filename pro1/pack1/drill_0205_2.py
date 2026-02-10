class Machine:
    
    def __init__(self):

        self.coin_in = CoinIn()
        self.coin_in.insert()
        self.calc()
        self.showData()

    def showData(self):
        
        if self.change < 0:
            print("잔액이 부족합니다.")
        else:
            print(f"{self.cupcount}잔이 나옵니다. 잔돈은 {self.change}원 입니다.")
        
    def calc(self):
        self.change = self.coin - self.cupcount*200

        

class CoinIn:
    coin = 0
    # cupcount = 0
    def insert(self):
        self.coin = int(input("동전을 입력하세요"))
        self.cupcount = int(input("몇 잔을 원하세요"))


if __name__=='__main__':
    Machine()