# pandas 문제 8)
from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
from markupsafe import escape
import numpy as np
import matplotlib
matplotlib.use('Agg')  # ← 반드시 추가. 화면 없이 렌더링하는 백엔드
import matplotlib.pyplot as plt

# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.
# Django 또는 Flask 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.

#    1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)
#        : 부서번호, 직원명 순으로 오름 차순 정렬 
app = Flask(__name__)

db_config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8mb4'
}

def get_connection():
    return pymysql.connect(**db_config)

@app.route("/")
def index():
    dept = request.args.get("dept","").strip()
    sql = """
            select j.jikwonno as 사번, j.jikwonname as 직원명, b.busername as 부서명, j.jikwonjik as 직급,
                    j.jikwonpay as 연봉, TIMESTAMPDIFF(YEAR, j.jikwonibsail, CURDATE()) as 근무년수,
                    j.jikwongen as 성별
            from jikwon j
            inner join buser b on j.busernum = b.buserno
        """
    params = []

    if dept:
        sql += " where busername like %s"       # 앞에 공백 있어야하는 이유?
        params.append(f"%{dept}%")

    sql += " order by buserno, jikwonname asc"  
    
    # SQL 실행
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql,params)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description ]      # .description: 컬럼 정보 얻기.

    df = pd.DataFrame(rows, columns=cols)
    # 직원정보 html로 전송
    if not df.empty:
        jikwondata = df[['사번','직원명','부서명','연봉','근무년수']].to_html(index=False)
    else:
        jikwondata = "직원 정보 없음"
    print(jikwondata)

#    2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.
    if not df.empty:
        stats_df = (
            df.groupby("직급")["연봉"]
            .agg(
                연봉합="sum",
                평균 = "mean"
            )
            .round(2)
            .reset_index()
            .sort_values(by='평균', ascending=False)
        )
        statsdata = stats_df.to_html(index=False)   # ← 여기 추가
    else:
        statsdata = "정보 없음"

#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
    if not df.empty:
        graph_df = (
                df.groupby("부서명")["연봉"]
                .agg(
                        연봉합="sum",
                        평균="mean"
                    )
                    .round(2)
                    .reset_index()
                    .sort_values(by='평균', ascending=False)
                )
        graph = graph_df.to_html(index=False)
        plt.bar(graph_df['부서명'],graph_df['연봉합'])
        plt.title('부서별 연봉합')
        plt.savefig('static/graph.png')
        plt.show()
        plt.close()
    else:
        graph = "정보없음"

#    4) 성별, 직급별 빈도표를 출력하시오.
    if not df.empty:
        gender_df = (
                df.groupby("성별")["직급"]
                .agg(
                        빈도="count"                        
                    )
                    .round(2)
                    .reset_index()
                    .sort_values(by='빈도', ascending=False)
                )
        gender = gender_df.to_html(index=False)
        plt.bar(gender_df['성별'],gender_df['빈도'])
        plt.title('성별, 직급별 빈도표')
        plt.savefig('static/graph_gender.png')
        plt.show()
        plt.close()
    else:
        gender = "정보없음"


#    5) 부서별 최고 연봉자 출력 : 부서명별로 가장 연봉이 높은 직원 1명씩 출력 
#        출력 항목: 부서명, 직원명, 연봉

#    6) 부서별 직원 비율 계산 : 전체 인원 대비 각 부서 인원 비율(%) 
#        비율 계산 (%)은 dept_ratio = (dept_count / total * 100).round(2)
#       결과를 DataFrame으로 출력
#       예: 총 인원: 30명
#            영업부 20%
#            총무부 30%
#            전산부 5%

    return render_template("index.html", dept=escape(dept), 
                        jikwondata=jikwondata, statsdata=statsdata,
                        graph=graph, gender=gender
                        )

if __name__ == '__main__':
    app.run(debug=True)
