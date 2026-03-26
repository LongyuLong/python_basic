# pandas2.py

from pandas import Series, DataFrame

# Series의 재 색인(index 변경)
data = Series([1,3,2], index=(1,4,2))
print(data)
data2 = data.reindex((1,2,4))
print(data2)

print('\n재색인할 때 값 채워넣기')
data3 = data2.reindex([0,1,2,3,4,5])
print(data3)

print('\n재색인할 때 값 채워넣기')
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)
print(data3)

print()
# NaN 이전 값으로 채우기
data3 = data2.reindex([0,1,2,3,4,5], method='ffill')
print(data3)

data3 = data2.reindex([0,1,2,3,4,5], method='pad')
print(data3)
# 위 두방법 모두 0번 인덱스가 NaN -> 이전 값이 없어서.

# NaN 이후 값으로 채우기
data3 = data2.reindex([0,1,2,3,4,5], method='bfill')
print(data3)

data3 = data2.reindex([0,1,2,3,4,5], method='backfill')
print(data3)

import numpy as np
print('\nDataFrame: bool 처리')
df = DataFrame(np.arange(12).reshape(4,3),
                index=['1월','2월','3월','4월'],
                columns=['강남','강북','서초']
            )
print(df)
print("df['강남']")
print(df['강남'])
print("df['강남']>3")
print(df['강남']>3)
print("df[df['강남']>3]")
print(df[df['강남']>3])

print(df < 3)
df[df <3] = 0
print(df)
# 이쪽부분은 df 설명이랑 같이 해야될거같네. 헷갈려
print()

print('\n슬라이싱 관련 메소드: loc()-라벨 지원, iloc()-숫자 지원')
print(df.loc['3월',:])
print(df.loc[:'2월'])
print(df.loc[:'2월',['서초']])
print()

print(df.iloc[2])
print(df.iloc[2,:])
print(df.iloc[:3,2])    # :3 = 3행 미만이란 표현
print(df.iloc[:3,1:3])    # 1:3 = 1행 이상? 3행 미만이란 표현
print()










