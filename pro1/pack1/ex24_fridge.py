# 클래스의 포함 관계 연습 - 냉장고 객체에 음식 객체 담기

class Fridge:
    isOpened = False                                # 냉장고 문 개폐 여부에 대한 변수
    foods = []                                      # 음식 리스트

    def open(self):
        self.isOpened = True
        print("냉장고 문을 열기")

    def close(self):
        self.isOpened = False
        print("냉장고 문을 닫기")

    def foodslist(self):                            # 냉장고 문이 열렸을 때 음식 확인
        for f in self.foods:
            print(f' - {f.name} {f.expire_date}')
        print()

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f'냉장고에 {thing.name} 넣음')
            self.foodslist()
        else:
            print('냉장고 문이 닫혀있음')




class FoodData:
    def __init__(self, name, expire_date):
        self.name = name
        self.expire_date = expire_date
        
fobj = Fridge()

apple = FoodData('사과','2026-08-01')
# fobj.put(apple)
fobj.open()
fobj.put(apple)
# fobj.close()
cola = FoodData('콜라','2027-11-01')

# fobj.open()
fobj.put(cola)
fobj.close()





















