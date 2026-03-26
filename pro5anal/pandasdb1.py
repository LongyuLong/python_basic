# local db 연동 후 DataFrame에 자료 저장
import sqlite3

sql = "create table if not exists extab(product varchar(10), maker varchar(10), weight real, price integer)"

conn = sqlite3.connect(':memory:')
conn.execute(sql)
conn.commit()

data = [('mouse','samsung', 12.5, 5000),('keyboard','lg', 52.5,35000)]
isql = "insert into extab values(?,?,?,?)"
conn.executemany(isql, data)      # execute(sql, data) : 1개씩 / executemany(sql, data) : 여러개
data1 = ('pen','abc',5.0,1200)
conn.execute(isql, data1)
conn.commit()

cursor = conn.execute("select * from extab")        # db 읽어오기
rows = cursor.fetchall()
for a in rows :     
    print(a)        # extab의 값들 하나씩 출력

print('rows를 DataFrame에 저장 ---')
import pandas as pd

# 1)
df1 = pd.DataFrame(rows, columns=['product','maker','weight','price'])
print(df1)
print(df1.describe())
print()

# 2)
df2 = pd.read_sql("select * from extab", conn)
print(df2)
print(df2.describe())
print(pd.read_sql("select count(*) from extab", conn))      # 건수
print()

# DataFrame의 자료를 테이블에 저장(insert)
data = {
    'product':['연필','볼펜','지우개'],
    'maker':['모나미','제트스트림','아인'],
    'weight':[2.5, 3.7, 1.2],
    'price':(1200, 1800, 1000)      # 튜플도 가능
}
frame = pd.DataFrame(data)
print(frame)
print()

frame.to_sql('extab', conn, if_exists='append', index=False)
df3 = pd.read_sql("select * from extab", conn)
print(df3)

cursor.close()
conn.close()
