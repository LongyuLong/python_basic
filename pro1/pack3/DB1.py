# 개인용 Database : sqlite3
# https://www.sqlite.org
# 모바일 기기, 임베디드 시스템에서 주로 사용.

import sqlite3
print(sqlite3.sqlite_version)


# conn = sqlite3.connect('exam.db')
conn = sqlite3.connect(':memory:')          # RAM에만 db 저장, 휘발성


try:
    cur = conn.cursor();                    # SQL문 처리를 위한 cursor 객체 생성

    # 테이블 생성
    cur.execute("create table if not exists friends(name text, phone text, addr text)")

    # 자료 입력
    cur.execute("insert into friends values('홍길동', '222-2222', '서초1동')")
    
except Exception as e:
    print('err : ', e)
finally:
    pass
