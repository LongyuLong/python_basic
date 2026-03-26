#  a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
#      - DataFrame의 자료를 파일로 저장
#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pymysql
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,    
    'charset':'utf8'
}
try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwonno,jikwonname,busername,jikwonpay,jikwonjik
        from jikwon inner join buser on jikwon.busernum = buser.buserno
    """
    cursor.execute(sql)
    rows = cursor.fetchall() 
    df1 = pd.DataFrame(rows, columns=['jikwonno','jikwonname','busername','jikwonpay','jikwonjik'])
    bn = df1.groupby('busername')['jikwonpay'].sum()
    print(bn)
    print("최대 연봉 : ", bn.max())
    print("최소 연봉 : ", bn.min())
    ctab = pd.crosstab(df1['busername'], df1['jikwonjik'])
    print(ctab)

    print()
    gsql = """
    select jikwonname, gogekno, gogekname, gogektel 
    from jikwon  
    left outer join gogek on jikwon.jikwonno = gogek.gogekdamsano
    order by jikwonname
    """
    cursor.execute(gsql)
    grow = cursor.fetchall()
    df2 = pd.DataFrame(grow, columns=['직원명', '고객번호', '고객명', '전화번호'])
    
    df2['고객번호'] = df2['고객번호'].fillna('담당 고객 X')
    df2['고객명'] = df2['고객명'].fillna('-')
    df2['전화번호'] = df2['전화번호'].fillna('-')
    print(df2)
#      - 연봉 상위 20% 직원 출력  : quantile()
#      - SQL로 1차 필터링 후 pandas로 분석 
#     - 조건: 연봉 상위 50% (df['연봉'].median() ) 만 가져오기  후 직급별 평균 연봉 출력
#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
except Exception as e:
    print("처리 오류 : ", e)
finally :
    cursor.close()
    conn.close()
#  b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pymysql
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,    
    'charset':'utf8'
}
try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwongen, jikwonpay, busername from jikwon
        inner join buser on jikwon.busernum = buser.buserno
    """
    cursor.execute(sql)
    jrow = cursor.fetchall()
    df12 = pd.DataFrame(jrow, columns=['성별','연봉','부서명'])
    df_table = df12.pivot_table(index='성별', values='연봉', aggfunc='mean')
    print(df_table)

    df_table.plot(kind='bar', color=['skyblue', 'pink'], legend=False, rot=0)
    plt.title('성별 연봉 평균')
    plt.xlabel('성별')
    plt.ylabel('평균 연봉')
    plt.show()
    tab = pd.crosstab(df12['부서명'], df12['성별'])
    print(tab)
except Exception as e:
    print("처리 오류 : ", e)
finally :
    cursor.close()
    conn.close()
#  c) 키보드로 사번, 직원명을 입력받아 로그인에 성공하면 console에 아래와 같이 출력하시오.
#       조건 :  try ~ except MySQLdb.OperationalError as e:      사용
#      사번  직원명  부서명   직급  부서전화  성별
#      ...
#      인원수 : * 명
#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
#     - Histogram (분포 비교) : 남/여 연봉 분포 비교    <== 그래프 출력
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8'
}

jikwonno_input = input("사번 입력: ")
jikwonname_input = input("직원명 입력: ")

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # 로그인 검증
    login_sql = """
        select jikwonno from jikwon
        where jikwonno = %s and jikwonname = %s
    """
    cursor.execute(login_sql, (jikwonno_input, jikwonname_input))
    login_row = cursor.fetchone()

    if login_row is None:
        print("로그인 실패: 사번 또는 직원명이 일치하지 않습니다.")
    else:
        print("로그인 성공!")

        # 전체 직원 정보 출력
        sql = """
            select j.jikwonno, j.jikwonname, b.busername, j.jikwonjik, b.busertel, j.jikwongen
            from jikwon j
            inner join buser b on j.busernum = b.buserno
            order by j.jikwonno
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['사번', '직원명', '부서명', '직급', '부서전화', '성별'])
        print(df.to_string(index=False))
        print(f"\n인원수 : {len(df)} 명")

        # 성별 연봉 분포 + 이상치 확인 (박스플롯)
        pay_sql = """
            select j.jikwongen, j.jikwonpay
            from jikwon j
        """
        cursor.execute(pay_sql)
        pay_rows = cursor.fetchall()
        df_pay = pd.DataFrame(pay_rows, columns=['성별', '연봉'])

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # 박스플롯 — 성별 연봉 분포 + 이상치
        df_pay.boxplot(column='연봉', by='성별', ax=axes[0])
        axes[0].set_title('성별 연봉 분포 및 이상치')
        axes[0].set_xlabel('성별')
        axes[0].set_ylabel('연봉')
        plt.suptitle('')  # 자동 생성되는 상위 제목 제거

        # 히스토그램 — 남/여 연봉 분포 비교
        male_pay = df_pay[df_pay['성별'] == '남']['연봉']
        female_pay = df_pay[df_pay['성별'] == '여']['연봉']
        axes[1].hist(male_pay, alpha=0.6, label='남', color='skyblue', bins=10)
        axes[1].hist(female_pay, alpha=0.6, label='여', color='pink', bins=10)
        axes[1].set_title('남/여 연봉 분포 비교')
        axes[1].set_xlabel('연봉')
        axes[1].set_ylabel('인원수')
        axes[1].legend()

        plt.tight_layout()
        plt.show()

except pymysql.MySQLError as e:
    print("처리 오류:", e)
finally:
    cursor.close()
    conn.close()




# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.

# Django(Flask) 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.
#    1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)
#        : 부서번호, 직원명 순으로 오름 차순 정렬 
#    2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.
#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
#    4) 성별, 직급별 빈도표를 출력하시오.


# Flask — DB 조회 결과를 브라우저로 출력

from flask import Flask, render_template_string
import pymysql
import pandas as pd

app = Flask(__name__)

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8'
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>직원 현황</title>
    <style>
        body { font-family: sans-serif; margin: 30px; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 30px; }
        th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: center; }
        th { background-color: #f2f2f2; }
        h2 { margin-top: 40px; }
    </style>
</head>
<body>
    <h1>직원 현황</h1>

    <h2>1) 직원 목록 (부서번호·직원명 오름차순)</h2>
    {{ df1 | safe }}

    <h2>2) 부서명별 연봉 합계 / 평균</h2>
    {{ df2 | safe }}

    <h2>3) 직급별 연봉 합계 / 평균</h2>
    {{ df3 | safe }}

    <h2>4) 성별·직급별 빈도표</h2>
    {{ df4 | safe }}
</body>
</html>
"""

@app.route('/')
def index():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        # 1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수 — 부서번호·직원명 오름차순
        sql1 = """
            select j.jikwonno, j.jikwonname, b.busername, j.jikwonjik,
                   j.jikwonpay, TIMESTAMPDIFF(YEAR, j.jikwonibsail, CURDATE()) as 근무년수
            from jikwon j
            inner join buser b on j.busernum = b.buserno
            order by j.busernum asc, j.jikwonname asc
        """
        cursor.execute(sql1)
        df1 = pd.DataFrame(cursor.fetchall(),
                           columns=['사번', '직원명', '부서명', '직급', '연봉', '근무년수'])

        # 2) 부서명별 연봉 합계·평균
        df2 = df1.groupby('부서명')['연봉'].agg(['sum', 'mean']).reset_index()
        df2.columns = ['부서명', '연봉합계', '연봉평균']
        df2['연봉평균'] = df2['연봉평균'].round(0)

        # 3) 직급별 연봉 합계·평균
        df3 = df1.groupby('직급')['연봉'].agg(['sum', 'mean']).reset_index()
        df3.columns = ['직급', '연봉합계', '연봉평균']
        df3['연봉평균'] = df3['연봉평균'].round(0)

        # 4) 성별·직급별 빈도표
        sql4 = """
            select j.jikwongen, j.jikwonjik
            from jikwon j
        """
        cursor.execute(sql4)
        df_gen = pd.DataFrame(cursor.fetchall(), columns=['성별', '직급'])
        df4 = pd.crosstab(df_gen['직급'], df_gen['성별'])

        return render_template_string(
            HTML_TEMPLATE,
            df1=df1.to_html(index=False, border=1),
            df2=df2.to_html(index=False, border=1),
            df3=df3.to_html(index=False, border=1),
            df4=df4.to_html(border=1)
        )

    except Exception as e:
        return f"<p>오류 발생: {e}</p>"
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)


