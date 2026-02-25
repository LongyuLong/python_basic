"""
문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)

직원번호 직원명 관리 고객 수

1 홍길동 3

2 한송이 1
"""

import MySQLdb
import pickle               # 아래 config가 노출되는 것을 막기위한 pickle 사용

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

"""
config = {                                          
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}
"""

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        sql = """
            select
            jikwonno as 직원번호, jikwonname as 직원명, count(*) as 관리고객수
            from jikwon
            inner join gogek on jikwonno = gogekdamsano
            group by jikwonno
            
            """
        cursor.execute(sql)
        data = cursor.fetchall()
        print("직원번호 직원명 관리고객수")
        for jikwonno, jikwonname, 관리고객수 in data:
                print(jikwonno, jikwonname, 관리고객수)
    except Exception as e:
        print('err: ',e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    chulbal()