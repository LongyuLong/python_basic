# 원격 데이터베이스 연동 프로그래밍
# MariaDB : driver file 설치 후 사용
# pip install mysqlclient (완료)

import MySQLdb
"""
conn = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='test',
    port=3306                               # mariaDB 기본 포트값
    )

print(conn)
conn.close()
"""
# sangdata 자료 CRUD (Insert, Select, Update, Delete)
config = {                                          # dict 형식으로 정보 입력
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

def myFunc():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        # 자료 추가
#       isql = "insert into sangdata(code,sang,su,dan) values(5,'신상1',5,7800)"
#       cursor.execute(isql)
#       conn.commit()                                   # 원본자료에 추가. 다시 실행하면 오류 발생함.
#                                                       # primary키는 고유하기 때문에, commit 이후에는 쓸수 없음
        """
        isql = "insert into sangdata values(%s, %s, %s, %s)"
        # sql_data = (6,'신상2',11,5000)
        sql_data = 6,'신상2',11,5000    # 괄호 있어도 없어도 똑같다. 근데 5와 (5)는 다르다. 같으려면 5와 (5,)
        cursor.execute(isql, sql_data)
        conn.commit()
        """
        # 자료 수정
        """usql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
        sql_data = '물티슈',66,1000,5               # 위에서 선언한 usql와 순서 통일
        cursor.execute(usql, sql_data)
        conn.commit()"""
        """
        usql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
        sql_data = '콜라',77,1000,5               # 위에서 선언한 usql와 순서 통일
        cou = cursor.execute(usql, sql_data)
        print('수정 건수 : ', cou)
        conn.commit()
        """
        # 자료 삭제
        code = '6'
        #dsql = "delete from sangdata where code=" + code     # 문자열 더하기로 SQL 완성 <- 권장하지 않음
        #                                                     # secure coding 가이드라인 위배
        # 1안
        #dsql = "delete from sangdata where code=%s"
        #cursor.execute(dsql, (code,))                         # 튜플 형식 주의
        # 2안
        dsql = "delete from sangdata where code='{0}'".format(code)
        cou = cursor.execute(dsql)                     # 삭제 후 반환값 얻기(0 or 1이상)
        print('수정 건수 : ', cou)
        if cou != 0:
            print('삭제 성공')
        else:
            print('삭제 실패')
    
        conn.commit()


        # 자료 읽기
        sql = "select code, sang, su, dan from sangdata"
        cursor.execute(sql)
        
        for data in cursor.fetchall():
            #print(data)
            print('%s %s %s %s'%data)

        print()
        cursor.execute(sql)
        for r in cursor:
            print(r[0], r[1], r[2], r[3])

        print()
        cursor.execute(sql)
        for (code, sang, su, dan) in cursor:
            print(code, sang, su, dan)


    except Exception as e:
        print('err: ',e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    myFunc()