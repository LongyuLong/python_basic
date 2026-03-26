#pandas6.py

import pandas as pd

items = {
    'apple':{'count':10,'price':1500},
    'orange':{'count':5,'price':800}
}

df = pd.DataFrame(items)
print(df)

# DataFrame 저장
# 클립보드로 저장
df.to_clipboard()           # 메모장 등으로 확인
print(df.to_html())
print(df.to_json())

df.to_csv('result1.csv', sep=',')
df.to_csv('result1.csv', sep=',', index=False)
df.to_csv('result1.csv', sep=',', index=False, header=False)
print()

df2 = df.T
print(df2)
df2.to_csv('result4.csv', sep=',', index=False, encoding='utf-8-sig')

redata = pd.read_csv('result4.csv')
print(redata)

print('\n--------- 엑셀 관련 ---------')
df3 = pd.DataFrame({
    'name':['Alice','Bob','Oscar'],
    'age':[24,22,29],
    'city':['Seoul','Suwon','Incheon']
})
print(df3)

# 엑셀 파일 i/o
df3.to_excel('result.xlsx', index=False, sheet_name='work1')

# exdf = 

# df4 = 



















