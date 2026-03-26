# * Pandas의 DataFrame 관련 연습문제 *
from pandas import DataFrame, Series
import numpy as np  
# pandas 문제 1)
print("1-a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. ")
df = DataFrame(np.random.randn(9, 4))
print(df)
print()
print("1-b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오")
df = DataFrame(np.random.randn(9, 4), columns=['No1','No2','No3','No4'])
print(df)
print()
print("1-c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용")
print(np.mean(df,axis=0))   # column 이니까 axis = 0

# pandas 문제 2)

#   numbers
# a 10
# b 20
# c 30
# d 40

print("2-a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.")
df1 = DataFrame({'numbers': [10,20,30,40]}, index=['a','b','c','d'])
print(df1)
print()

print("2-b) c row의 값을 가져오시오.")
ans = df1.loc['c']
print(ans)
print()

print("2-c) a, d row들의 값을 가져오시오.")
ans1 = [df1.loc['a'], df1.loc['d']]
print(ans1)
print()

print("2-d) numbers의 합을 구하시오.")
ans2 = df1.sum(axis=0)
print(ans2)
print()

print("2-e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.")
#   numbers
# a 100
# b 400
# c 900
# d 1600

sq = df1 ** 2
print(sq)
print()

print("2-f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.")
#   numbers floats
# a 10      1.5
# b 20      2.5
# c 30      3.5
# d 40      4.5
df1.insert(1,"floats",[1.5,2.5,3.5,4.5])
print(df1)
print()

print("2-g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.")
#   names
# d 길동
# a 오정
# b 팔계
# c 오공
names = Series(["길동","오정","팔계","오공"], index=['d','a','b','c'])
names = names.reindex(['a','b','c','d'])
df1.insert(2,"names",names)
print(df1)
print(df1.index)
print()
# pandas 문제 3)

print("3-1) 5 x 3 형태의 랜덤 정수형 DataFrame을 생성하시오. (범위: 1 이상 20 이하, 난수)")
df3 = DataFrame(np.random.randint(1, 21, (5, 3)))
print(df3)
print()

print("3-2) 생성된 DataFrame의 컬럼 이름을 A, B, C로 설정하고, 행 인덱스를 r1, r2, r3, r4, r5로 설정하시오.")
df3.columns=list('ABC')
df3.index=['r1','r2','r3','r4','r5']
print(df3)
print()

print("3-3) A 컬럼의 값이 10보다 큰 행만 출력하시오.")
print(df3[df3['A']>10]['A'])            # 중요.
print()

print("3-4) 새로 D라는 컬럼을 추가하여, A와 B의 합을 저장하시오.")
df3.insert(3,"D",df3['A']+df3['B'])
print(df3)
print()

print("3-5) 행 인덱스가 r3인 행을 제거하되, 원본 DataFrame이 실제로 바뀌도록 하시오.")
df3 = df3.drop('r3', axis=0)
print(df3)
print()

print("3-6) 아래와 같은 정보를 가진 새로운 행(r6)을 DataFrame 끝에 추가하시오.")
#          A     B    C     D
#   r6   15   10    2   (A+B)
a = 15
b = 10
c = 2
d = a+b
df3.loc['r6'] = [a,b,c,d]

print(df3)
print()

# pandas 문제 4)
# 다음과 같은 재고 정보를 가지고 있는 딕셔너리 data가 있다고 하자.
data = {
    'product': ['Mouse', 'Keyboard', 'Monitor', 'Laptop'],
    'price':   [12000,     25000,      150000,    900000],
    'stock':   [  10,         5,          2,          3 ]
}

print("4-1) 위 딕셔너리로부터 DataFrame을 생성하시오. 단, 행 인덱스는 p1, p2, p3, p4가 되도록 하시오.")
frame = DataFrame(data, index=['p1','p2','p3','p4'])
print(frame)
print()

print("4-2) price와 stock을 이용하여 'total'이라는 새로운 컬럼을 추가하고, 값은 'price x stock'이 되도록 하시오.")
frame.insert(3,"total",frame['price']*frame['stock'])
print(frame)
print()

print("4-3) 컬럼 이름을 다음과 같이 변경하시오. 원본 갱신")
print("product → 상품명,  price → 가격,  stock → 재고,  total → 총가격")
frame.columns=list(["상품명","가격","재고","총가격"])
print(frame)
print()

print("4-4) 재고(재고 컬럼)가 3 이하인 행의 정보를 추출하시오.")
ans4 = frame[frame["재고"]<=3]
print(ans4)
print()

print("4-5) 인덱스가 p2인 행을 추출하는 두 가지 방법(loc, iloc)을 코드로 작성하시오.")
loc = frame.loc['p2']
print("loc: ",loc)
print()
iloc = frame.loc['p2']
print("iloc: ",iloc)
print()

print("4-6) 인덱스가 p3인 행을 삭제한 뒤, 그 결과를 확인하시오.")
# (원본이 실제로 바뀌지 않도록, 즉 drop()의 기본 동작으로)
imsi = frame.drop('p3')
print(imsi)

print("4-7) 위 DataFrame에 아래와 같은 행(p5)을 추가하시오.")
#             상품명             가격     재고    총가격
#  p5       USB메모리    15000     10    가격*재고
a = "USB메모리"
b = 15000
c = 10
d = b*c
imsi.loc['p5'] = [a,b,c,d]
print(imsi)







