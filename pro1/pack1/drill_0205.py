# 커피 자판기 프로그램

# 입력 자료는 키보드로, 커피는 한잔에 200원 
# 100원 넣고 커피 요구 시 요금 부족 메세지 출력
# 400원 넣고 2잔 요구하면 두잔 출력
# 500원 넣고 1잔 요구하면 300원 반납

class Machine:
    cupcount = 0
    def __init__(self):
        
        CoinIn.insert(self)                             # 이 부분에서 CoinIn() 로 불러와야하는데
        
        self.cupcount=int(input("몇 잔을 원하세요"))            

        change = self.coin - self.cupcount * 200

        if change < 0:
            print("잔액이 부족합니다.")
        else:
            print(f'잔돈은 {change}원 입니다.')

        
    


class CoinIn:
    coin = 0
    # cupcount = 0
    def insert(self):
        self.coin = int(input("동전을 입력하세요"))
        # print(self.coin)

    # def cup(self):
    #     self.cupcount=int(input("몇 잔을 원하세요"))            
    #     # print(self.cupcount)

if __name__=='__main__':
    Machine()