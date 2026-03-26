# 연산

from pandas import Series, DataFrame
import numpy as np

s1 = Series([1,2,3], index=['a','b','c'])
s2 = Series([4,5,6,7], index=['a','b','c','d'])

print(s1)
print(s2)

print(s1+s2)        # 같은 index끼리만 연산, 불일치하면 NaN 반환(python 자체연산)
print(s1.add(s2))   # 결과는 똑같지만 numpy 함수 사용 예시

print(s1.mul(s2))

print()

df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('kbs'), 
                index=['서울', '대전', '부산'])
df2 = DataFrame(np.arange(12).reshape(4,3), columns=list('kbs'), 
                index=['서울', '대전', '제주','광주'])
print(df1)
print(df2)
print(df1+df2)
print(df1.add(df2,fill_value=0))    # NaN은 0으로 채워 연산하도록
# sub, mul, div 도 가능

print('---NaN 처리---')

df = DataFrame([[1.4, np.nan], [7, -4.5], [np.nan, np.nan],[0.5,-1]],
                columns=['one','two'])
print(df)
print()
print(df.isnull())
print()
print(df.notnull())
print()
print(df.dropna())
print()
print(df.dropna(how='any'))
print()
print(df.dropna(how='all'))
print()
print(df.dropna(subset=['one']))    # 특정 열(one)에 NaN 있는 행 삭제
print()
print(df.dropna(subset=['two']))    # 특정 열(two)에 NaN 있는 행 삭제
print()
print(df.dropna(axis='rows'))       # 
print()
print(df.dropna(axis='columns'))    # 

print()
print(df)
imsi = df.drop(1)   # 원본은 삭제 안됨. 삭제된 결과가 새로운 dataFrame으로 생성
print(imsi)
print(df)
print()
# df.drop(1, inplace=True)  # 원본 삭제됨

# 계산 관련 메서드
print(df.sum())         # 열의 합 - NaN은 연산에서 제외
print(df.sum(axis=0, skipna=True))   # NaN 연산제외옵션?
print(df.sum(axis=1))   # 행의 합
print(df.describe())    # 요약 통계량 출력. 유용할듯?

print()
words = Series(['봄','여름','가을','봄'])
print(words.describe()) # 숫자 데이터가 아니어도 통계량 나온다.









