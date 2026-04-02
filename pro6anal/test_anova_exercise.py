print("[ANOVA 예제 1]")
print("""빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.""")
# 수집된 자료 :  
# kind quantity
# (1, 64) (2, 72) (3, 68) (4, 77)(2, 56) (1, NaN) (3, 95) (4, 78) (2, 55) (1, 91) (2, 63)
# (3, 49) (4, 70) (1, 80) (2, 90) (1, 33) (1, 44) (3, 55) (4, 66) (2, 77)
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = {
    'kind': [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2],
    'quantity': [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
    }
df = pd.DataFrame(data)
df = df.fillna(df.mean())   # NaN을 평균값으로 채움 -- 근데 자동으로 quantity column의 평균으로 채워지는건가
# print(df)
# 기름 종류별로 분리
# df['kind'] == 1 부분은 "kind 컬럼의 값이 1인게 맞니?"라고 묻는 조건문이에요.
# 이걸 df[...] 대괄호 안에 넣으면, 조건이 참(True)인 행들만 남긴 새로운 표를 만듭니다
oil1 = df[df['kind']==1]['quantity']
oil2 = df[df['kind']==2]['quantity']
oil3 = df[df['kind']==3]['quantity']
oil4 = df[df['kind']==4]['quantity']
# 정규성, 등분산성 체크
print(stats.levene(oil1,oil2,oil3,oil4).pvalue)
# LeveneResult: 0.326
print(stats.shapiro(oil1).pvalue) # 0.868
print(stats.shapiro(oil2).pvalue) # 0.592
print(stats.shapiro(oil3).pvalue) # 0.486
print(stats.shapiro(oil4).pvalue) # 0.416
# 모두 정규성, 등분산성 만족함
print("--- f_oneway(oil1, oil2, oil3, oil4) ----")
print(stats.f_oneway(oil1, oil2, oil3, oil4).pvalue)    
# 0.848 -- 귀무 채택? 그럼 기름에 따라 빵에 흡수되는 양 차이없다?
# 귀무 채택인 경우 사후검정은 할필요없다~
print()
print()

print("""[ANOVA 예제 2]
DB에 저장된 buser와 jikwon 테이블을 이용하여 
총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 
만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.""")

import pymysql
import sqlite3

config = {
    'host':'127.0.0.1', 'user':'root',
    'password':'123', 'database':'test',
    'port':3306, 'charset':'utf8'
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
    junsan = df1[df1['busername'] == '전산부']
    manage = df1[df1['busername'] == '관리부']

    account = account['jikwonpay'].dropna()
    sales = sales['jikwonpay'].dropna()
    junsan = junsan['jikwonpay'].dropna()
    manage = manage['jikwonpay'].dropna()

    print("정규성 확인")
    print(stats.shapiro(account).pvalue)    # 0.026 -- 불만족
    print(stats.shapiro(sales).pvalue)      # 0.025 -- 불만족
    print(stats.shapiro(junsan).pvalue)     # 0.419
    print(stats.shapiro(manage).pvalue)     # 0.907

    print("등분산성 확인")
    print(stats.levene(account, sales, junsan, manage).pvalue)      # 0.798
    print(stats.bartlett(account, sales, junsan, manage).pvalue)    # 0.335
    
    print("---- f_oneway ----")
    f_stat, p_val = stats.f_oneway(account, sales, junsan, manage)
    print('f_stat: ',f_stat)    # f_stat: 0.412
    print('p_val: ',p_val)      # p_val:  0.745
    print()
    # pvalue 0.745니까 귀무 채택이네? 그럼 부서로 인한 연봉차이는 없다?

    # 사후 검정
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    # pairwise_tukeyhsd(endog=분석하고자 하는 수치 데이터(예: 연봉, 흡수량)가 담긴 하나의 긴 리스트나 배열,
    # groups=각 수치 데이터가 어떤 그룹(예: 부서명, 기름 종류)에 속하는지 알려주는 같은 길이의 리스트나 배열) 
    # [방법 1] 각 부서별로 나뉜 데이터를 수동으로 합치는 방식
    # 각 부서의 데이터 개수(len)만큼 부서명을 반복해서 이름표(buser)를 만듭니다.
    pay = np.concatenate([account, sales, junsan, manage])
    buser = ['총무부'] * len(account) + ['영업부'] * len(sales) + ['전산부'] * len(junsan) + ['관리부'] * len(manage)

    tukResult = pairwise_tukeyhsd(endog=pay, groups=buser)


    """
    # [방법 2] 데이터프레임(df1)을 활용해 한 번에 처리하는 방식 (추천)
    # 결측치를 제거한 전체 데이터프레임을 사용하면 이름표를 수동으로 만들 필요가 없습니다.
    df_clean = df1.dropna(subset=['jikwonpay'])

    tukResult = pairwise_tukeyhsd(endog=df_clean['jikwonpay'], 
                                    groups=df_clean['busername'])
    """

    # 결과 출력 및 시각화
    print(tukResult)
    tukResult.plot_simultaneous(xlabel="mean", ylabel="group")
    plt.show()

    
except Exception as e:
    print("처리 오류 : ", e)

finally :
    cursor.close()
    conn.close()

