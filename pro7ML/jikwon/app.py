# 회귀분석 문제 4) 
# 원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
# Django 또는 Flask로 작성한 웹에서 근무년수를 입력하면 예상 연봉이 나올 수 있도록 프로그래밍 하시오.
# LinearRegression 사용. Ajax 처리!!!      참고: Ajax 처리가 힘들면 그냥 submit()을 해도 됩니다.

from flask import Flask, render_template, request, jsonify
from sklearn.linear_model import LinearRegression
import statsmodels.api
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
import pymysql
import pandas as pd
import datetime

app = Flask(__name__)

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
        select jikwonjik, jikwonpay, jikwonibsail from jikwon
    """
    cursor.execute(sql)
    rows = cursor.fetchall() 
    df1 = pd.DataFrame(rows, columns=['jikwonjik', 'jikwonpay', 'jikwonibsail'])
    df1['jikwonibsail'] = pd.to_datetime(df1['jikwonibsail'])   # datetime으로 바꾸고
    today = pd.Timestamp.today()
    df1['year'] = (today - df1['jikwonibsail']).dt.days // 365  # dt.days >> 일수를 정수로 꺼내는 함수
    # print(df1['year'])
    x = df1['year'].values.reshape(-1,1)
    y = df1['jikwonpay']
    # print(x)
    # print(y)
    model = LinearRegression().fit(x,y)

    # print('slope: ', model.coef_)
    slope = model.coef_[0]
    intercept = model.intercept_
    # print('intercept: ', model.intercept_)
    # slope:  [539.35930003]
    # intercept:  -1005.5038103302268
    plt.scatter(x,y)
    plt.plot(x,model.coef_ * x + model.intercept_, c = 'r')
    plt.show()
    pred = model.predict(x)
    print("예측값: ", np.round(pred[:5],1))
    # 예측값:  [8163.6 7624.2 7624.2 5466.8 3309.4]
    print("실제값: ", y[:5])
    # 실제값:  0    9900
            # 1    8800
            # 2    7900
            # 3    4500
            # 4    3000
    print()

except Exception as e:
    print("처리 오류 : ", e)
finally :
    cursor.close()
    conn.close()

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/predict")
def predict():
    years = request.args.get("years", "")
    result = model.predict([[int(years)]])
    formula = f"pay = {round(slope,1)} * years + {round(intercept,1)}"
    group_avg = df1.groupby('jikwonjik')['jikwonpay'].mean().round(0)
    group_list = [{"jik": k, "pay": v} for k, v in group_avg.items()]
    return jsonify({"ok": True, "salary": round(result[0], 1), 
                    "r2":round(float(r2_score(y,pred)),4), 
                    "formula":formula, "jikavg":group_list})

if __name__ == "__main__":
    app.run(debug=True)