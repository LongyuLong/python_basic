"""
문2-1) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력

해당 직원이 근무하는 부서 내의 직원 전부를 직급별 오름차순우로 출력. 직급이 같으면 이름별 오름차순한다.

직원번호 입력 : _______
직원명 입력 : _______

직원번호 직원명 부서명 부서전화 직급 성별
1 홍길동 총무부 111-1111 이사 남
...

직원 수 :
"""

import MySQLdb

config = {                                          
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        jik_no = input('직원번호 입력: ')
        jik_name = input('직원명 입력: ')

        sql = """
            select
            jikwonno as 직원번호, jikwonname as 직원명,
            busername as 부서명, busertel as 부서전화,
            jikwonjik as 직급, jikwongen as 성별
            from jikwon
            inner join buser on busernum = buserno
            where jikwonno={0} and jikwonname='{1}'
        """.format(jik_no, jik_name)

        cursor.execute(sql)
        datas = cursor.fetchall()

        if len(datas) == 0:
            print("로그인 실패")
        else:
            sql2 = """
                select
                jikwonno as 직원번호, jikwonname as 직원명,
                busername as 부서명, busertel as 부서전화,
                jikwonjik as 직급, jikwongen as 성별
                from jikwon
                inner join buser on buserno = busernum
                where busername='{0}' order by jikwonjik, jikwonname 
                """.format(datas[0][2])
            # print(sql2)
            cursor.execute(sql2)
            datas2 = cursor.fetchall()
            # print(datas2)
            print("직원번호 직원명 부서명 부서전화 직급 성별")
            for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas2:
                
                print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)
            print("직원 수: "+str(len(datas2)))

            sql3 = """
                select
                gogekno as 고객번호, gogekname as 고객명, 
                gogektel as 고객전화, substring(date_format(now(),'%Y'),3,4)-substring(gogekjumin,1,2)+'100' as 고객나이
                from gogek
                inner join jikwon on jikwonno = gogekdamsano
                where jikwonno={0} and jikwonname='{1}'
                """.format(jik_no, jik_name)
            
            cursor.execute(sql3)
            datas3 = cursor.fetchall()
            # print(datas3)
            print("고객번호 고객명 고객전화 나이")
            for gogekno, gogekname, gogektel, 고객나이 in datas3:
                
                print(gogekno, gogekname, gogektel, 고객나이)
            print("관리 고객 수: "+str(len(datas3)))

    except Exception as e:
        print('err: ',e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    chulbal()