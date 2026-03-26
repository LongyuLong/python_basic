# 고수준의 자료구조(시리즈, 데이터프레임)와 빠르고 쉬운 데이터 분석용 함수제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, SQL, 시각화 .. 등을 제공
# 데이터랭글링(Data Wrangling), 데이터 먼징(Data Munging)을 효율적으로 처리 가능
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# series: 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)을 갖는다
# obj = pd.Series([3, 7, -5, 4])
obj = pd.Series([3, 7, -5, '사'])       # 요소값은 object type. 어떤것이든 들어갈 수 있다.
# obj = pd.Series((3, 7, -5, 40))       # 튜플은 되지만
# obj = pd.Series({3, 7, -5, 4})        # set은 typeError발생. set type is unordered
print(obj)
print(type(obj))

obj2 = pd.Series([3, 7, -5, 4], index=['a','b','c','d'])
print(obj2)
print(obj2.sum(), ' ', np.sum(obj2), ' ', sum(obj2))
# pandas에서 numpy 가져다 쓸 수 있다?

print(obj2.std())
print(obj2.values)
print(obj2.index)
print(obj2['a'])        # 3 -- 인덱스 사용해서 출력

print(obj2[['a']])      # a  3 -- 인덱스, 값 같이 나옴. 왜?
print(obj2['a':'c'])

print(obj2[2])
print(obj2.iloc[2])

print(obj2[[2,1]])
print(obj2.iloc[[2,1]])

print('a' in obj2)      # 해당 인덱스가 있으니 True
print('k' in obj2)      # 해당 인덱스가 없으면 False

print('파이썬 dict 자료를 series 객체로 생성')
names = {'mouse':50000, 'keyboard':250000, 'monitor':1000000}
print(names)
obj3 = Series(names)
print(obj3, ' ',type(obj3))             
# Series에 dict 타입을 넣어주면 출력할때는 표처럼 정리되어서

obj3.index = ['마우스','키보드','모니터']
print(obj3, ' ', type(obj3))

obj3.name = "상품 가격"
print(obj3)

print('\n--------------DataFrame 객체-------------')
df = pd.DataFrame(obj3)
print(df, ' ', type(df))
#        상품 가격
# 마우스    50000
# 키보드   250000
# 모니터  1000000

data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':['역삼동', '신당동', '역삼동', '역삼동', '신사동'],
    'nai':[23,25,33,231,35]
}

frame = pd.DataFrame(data)

print(frame)                # 인덱스는 따로 설정하지 않으면 자동으로 0부터 부여
#   irum juso  nai
# 0  홍길동  역삼동   23
# 1  한국인  신당동   25
# 2  신기해  역삼동   33
# 3  공기밥  역삼동  231
# 4  한가해  신사동   35

print()
print(frame['irum'])
# print(frame.irum)   # 위와 같은 표현이긴하지만 객체의 멤버처럼 보여서 가독성 저하

print(type(frame['irum']))
print(DataFrame(data=data, columns=['juso','irum','nai']))  # 컬럼 순서 변경
# pd.DataFrame이 아니어도 되는데 왜그런건지 헷갈림

# NaN (결측치)
frame2 = pd.DataFrame(data, columns=['irum','nai','juso','tel'],
                    index=['a','b','c','d','e']
                    )
# tel 컬럼 추가했고 인덱스 a~e 부여
frame2["tel"] = '111-1111'  # tel 열 전체에 적용
print(frame2)
val = pd.Series(['222-2222','333-3333','444-4444'], index = ['b','c','e'])
print(val)                  # 인덱스 겹쳐도 되나본데?

frame2["tel"] = val
print(frame2)               # 222~444 전화번호 덮어쓰기

print()
print(frame2.T)
print()

print(frame2.values)        # 결과는 list 타입
print(frame2.values[0,2])   

frame3 = frame2.drop('d')   
frame3 = frame2.drop('d', axis=0)   # 행 삭제
print(frame3)

frame4 = frame2.drop('tel',axis=1)  # 열 삭제
print(frame4)

print('----------')
print(frame2)
print(frame2.sort_index(axis=0, ascending=False))       # 행 단위 정렬
print(frame2.sort_index(axis=1, ascending=True))

print(frame2.rank(axis=0))  # 컬럼별로 랭크매김

counts = frame2['juso'].value_counts()
print(counts)

# 문자열 자르기
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}

fr = pd.DataFrame(data)
print(fr)
print('---------------------')
result1 = Series([x.split()[0] for x in fr.juso])   # 잘라서 0번째
# x.split을 감싸는 괄호가 대괄호면 리스트, 소괄호면 튜플.관호가 없으면? 튜플
result2 = Series([x.split()[1] for x in fr.juso])   # 잘라서 1번째
print(result1)
print(result2)
print(result1.value_counts())










