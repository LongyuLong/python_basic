# [two-sample t 검정 : 문제1] 
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.

# 수집된 자료 :  
blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red  = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

shapiro_blue = stats.shapiro(blue).pvalue
shapiro_red = stats.shapiro(red).pvalue
print("shapiro(blue): ",shapiro_blue)
print("shapiro(red): ",shapiro_red)
# 모두 0.5 이상이므로 정규성을 만족한다.

levene = stats.levene(blue, red).pvalue
print("Levene: ", levene)
# 0.439로 등분산성 만족

result = stats.ttest_ind(blue, red).pvalue
print(result)   # 0.0083 >> 귀무가설 기각. 매출액에 차이가 존재한다.

# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
# 수집된 자료 :  

male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]
np.random.seed(1)
rand_male = np.random.choice(male,15,replace=False)
rand_female = np.random.choice(female,15,replace=False)
# print(rand_female)

result2 = stats.ttest_ind(rand_male,rand_female).pvalue
print(result2)  # 0.3123 >> 귀무가설 채택. 차이가 없다?


# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
import pymysql
import sqlite3
import pandas as pd
from pandas import DataFrame
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
        select jikwonno,jikwonname,busername,jikwonpay
        from jikwon inner join buser on jikwon.busernum = buser.buserno
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    df1 = pd.DataFrame(rows, columns=['jikwonno','jikwonname','busername','jikwonpay'])
    # print(df1)
    account = df1[df1['busername'] == '총무부']
    sales = df1[df1['busername'] == '영업부']
    account = account.fillna(account.jikwonpay.mean())
    sales = sales.fillna(sales.jikwonpay.mean())
    
except Exception as e:
    print("처리 오류 : ", e)
finally :
    cursor.close()
    conn.close()

result3 = stats.ttest_ind(account['jikwonpay'],sales['jikwonpay']).pvalue
print(result3)  # pvalue 0.6524 이므로 귀무가설 채택


# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 수집된 자료 :  
mid_term = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

result4 = stats.ttest_rel(mid_term,final).pvalue
print(result4)  # 0.0234 이므로 귀무가설 기각. 학업능력이 변화했다

## 샘플이 30개가 안되는 경우 정규성, 등분산성 체크했어야했는데 안했다. 노트에 기록할것. ##









