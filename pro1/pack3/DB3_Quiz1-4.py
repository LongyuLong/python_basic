"""
문3) 성별 직원 현황 출력 : 성별(남/여) 단위로 직원 수와 평균 급여 출력

​

성별 직원수 평균급여

남 3 8500

여 2 7800

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
            jikwongen as 성별, count(*) as 직원수, avg(jikwonpay) as 평균급여
            from jikwon
            where jikwongen is not null group by jikwongen 
            """
        cursor.execute(sql)
        data = cursor.fetchall()
        print("성별 직원수 평균급여")
        for jikwongen, 직원수, 평균급여 in data:
                print(jikwongen, 직원수, round(평균급여))
    except Exception as e:
        print('err: ',e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    chulbal()