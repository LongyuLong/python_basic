# pandas4.py

# DataFrame 재구조화 (열을 행으로, 행을 열로 이동)

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(6).reshape(2,3), index=['대전','서울'], 
                    columns=['2020','2021','2022'])
print(df)
print()

# stack, unstack
df_row = df.stack()     # 열을 행으로 변경
print(df_row)

df_col = df_row.unstack()   # 행을 열로 이동
print(df_col)

print('\n--------------- 범주화 ----------------')
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]                 # 구간 기준값
result_cut = pd.cut(price, cut)     # 연속형 데이터를 범주화
print(result_cut)
print(pd.value_counts(result_cut))

print()
datas = pd.Series(np.arange(1,1001))

print(datas.head())                 # head()를 통해서 앞에서부터 지정한 개수만 볼수 있다 기본값 5
print(datas.tail())
result_cut2 = pd.qcut(datas,3)
print(result_cut2)
print(pd.value_counts(result_cut2))

print('\n----------- agg 함수: 범주의 그룹별 연산 -----------')
group_col = datas.groupby(result_cut2)
print(group_col.agg(['count','mean','std','min']))

# agg 대신 사용자 함수 작성
def summaryFunc(gr):
    return {'count':gr.count(),
            'mean':gr.mean(),
            'std':gr.std(),
            'min':gr.min()
            }

print()
print(group_col.apply(summaryFunc).unstack())

print('\n------ merge: 데이터프레임 객체 병합')

df1 = pd.DataFrame({'data1':range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df2)
print()
print(pd.merge(df1,df2,on='key'))               # inner join(교집합) 정도
print()
print(pd.merge(df1,df2,on='key', how='inner'))      
print()
print(pd.merge(df1,df2,on='key', how='outer'))      
print()
print(pd.merge(df1,df2,on='key', how='left'))      
print()
print(pd.merge(df1,df2,on='key', how='right'))      

print()

# 공통 칼럼명이 없는 경우. df1 vs df3
df3 = pd.DataFrame({'key2':['a','b','d'], 'data2':range(3)})
print(df3)
print(df1)

print(pd.merge(df1, df3, left_on='key', right_on='key2'))       # inner join

print('--concat--')
print(pd.concat([df1,df3], axis=0))         # 행 단위
print(pd.concat([df1,df3], axis=1))         # 열 단위

print('\n\npivot_table: pivot과 groupby 명령의 중간적 성격')
# pivot: 데이터 열 중에서 두개의 열(key)을 사용해 데이터의 행렬을 재구성
data = {'city':['강남','강북','강남','강북'],
        'year':[2000, 2001, 2002, 2002],
        'pop':[3.3, 2.5, 3.0, 2.0]
        }
df = pd.DataFrame(data)
print(df)
print()
print(df.pivot(index='city',columns='year', values='pop'))
print()
print(df.set_index(['city','year']))        # set_index: 기존 행 인덱스 제거하고 첫번째 ..?
print()
print(df)
print(df.pivot_table(index=['city']))
print(df.pivot_table(index=['city'], aggfunc='mean'))
print(df.pivot_table(index=['city','year'], aggfunc=[len,'mean']))      #뭘하고있는건지모르겠네 자세히 설명해서 노션에 추가
print(df.pivot_table(values='pop',index=['city']))                      # aggfunc 기본값은 mean?
print(df.pivot_table(values='pop',index=['city'], aggfunc=len))

print()
print(df.pivot_table(values='pop',index=['year'], columns=['city']))
print(df.pivot_table(values='pop',index=['year'], columns=['city'], margins=True))
print(df.pivot_table(values='pop',index=['year'], columns=['city'], margins=True, fill_value=0))














