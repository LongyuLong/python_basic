# 회귀분석 문제 3)    
# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음) 
# Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import koreanize_matplotlib
import statsmodels.api

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Carseats.csv")

print(df.head(3), df.shape)
#    Sales  CompPrice  Income  Advertising  Population  Price ShelveLoc  Age  Education Urban   US
# 0   9.50        138      73           11         276    120       Bad   42         17   Yes  Yes
# 1  11.22        111      48           16         260     83      Good   65         10   Yes  Yes
# 2  10.06        113      35           10         269     80    Medium   59         12   Yes  Yes (400, 11)
print(df.info())
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   Sales        400 non-null    float64
#  1   CompPrice    400 non-null    int64
#  2   Income       400 non-null    int64
#  3   Advertising  400 non-null    int64
#  4   Population   400 non-null    int64
#  5   Price        400 non-null    int64
#  6   ShelveLoc    400 non-null    object
#  7   Age          400 non-null    int64
#  8   Education    400 non-null    int64
#  9   Urban        400 non-null    object
#  10  US           400 non-null    object
# >> object가 섞여있어서 df.corr()가 오류 발생하는거

df = df.drop([df.columns[6],df.columns[9],df.columns[10]], axis=1) # axis는 또 뭐임
print(df.corr())
#                 Sales  CompPrice    Income  Advertising  Population     Price       Age  Education
# Sales        1.000000   0.064079  0.151951     0.269507    0.050471 -0.444951 -0.231815  -0.051955
# CompPrice    0.064079   1.000000 -0.080653    -0.024199   -0.094707  0.584848 -0.100239   0.025197
# Income       0.151951  -0.080653  1.000000     0.058995   -0.007877 -0.056698 -0.004670  -0.056855
# Advertising  0.269507  -0.024199  0.058995     1.000000    0.265652  0.044537 -0.004557  -0.033594
# Population   0.050471  -0.094707 -0.007877     0.265652    1.000000 -0.012144 -0.042663  -0.106378
# Price       -0.444951   0.584848 -0.056698     0.044537   -0.012144  1.000000 -0.102177   0.011747
# Age         -0.231815  -0.100239 -0.004670    -0.004557   -0.042663 -0.102177  1.000000   0.006488
# Education   -0.051955   0.025197 -0.056855    -0.033594   -0.106378  0.011747  0.006488   1.000000
# >> sales 중심으로 분석할건데, 
print()

lm = smf.ols(formula='Sales ~ Income + Advertising + Price + Age', data = df).fit()
print(lm.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                  Sales   R-squared:                       0.371
# Model:                            OLS   Adj. R-squared:                  0.364
# Method:                 Least Squares   F-statistic:                     58.21
# Date:                Mon, 06 Apr 2026   Prob (F-statistic):           1.33e-38
# Time:                        12:10:43   Log-Likelihood:                -889.67
# No. Observations:                 400   AIC:                             1789.
# Df Residuals:                     395   BIC:                             1809.
# Df Model:                           4
# Covariance Type:            nonrobust
# ===============================================================================
#                   coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------
# Intercept      15.1829      0.777     19.542      0.000      13.656      16.710
# Income          0.0108      0.004      2.664      0.008       0.003       0.019
# Advertising     0.1203      0.017      7.078      0.000       0.087       0.154
# Price          -0.0573      0.005    -11.932      0.000      -0.067      -0.048
# Age            -0.0486      0.007     -6.956      0.000      -0.062      -0.035
# ==============================================================================
# Omnibus:                        3.285   Durbin-Watson:                   1.931
# Prob(Omnibus):                  0.194   Jarque-Bera (JB):                3.336
# Skew:                           0.218   Prob(JB):                        0.189
# Kurtosis:                       2.903   Cond. No.                     1.01e+03
# ==============================================================================
# >> Price와 Age는 독립변수?로서 약하다?

print("-- 선형회귀 모델의 적절성 조건 체크 후 모델 사용 --")
print(df.columns)
# Index(['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price',
#        'Age', 'Education'], dtype='object')
df_lm = df.iloc[:,[0, 2, 3, 5 ,6]]
print(df_lm.head(2))
# 잔차항구하기
fitted = lm.predict(df_lm)

residual = df_lm['Sales'] - fitted
print("residual: ",residual[:3])
print("잔차 평균: ", np.mean(residual))
# 잔차 평균:  -1.4122036873231992e-15
print()

print('잔차의 정규성: 잔차가 정규성을 따르는지 확인')
from scipy.stats import shapiro
import statsmodels.api as sm

stat, p = shapiro(residual)
print(f"통계량: {stat:.5f}, p-value:{p:.5f}")
# 통계량: 0.99492, p-value:0.21270
print("정규성 만족" if p > 0.05 else "정규성 불만족")
# 정규성 만족

# Q-Q plot으로 시각화
sm.qqplot(residual, line='s')
plt.title("Q-Q plot으로 정규성 만족 확인")
plt.show()
print()

print("선형성 검정: 독립변수의 변화에 종속변수도 변화하나 특정한 패턴이 있으면 안된다")
from statsmodels.stats.diagnostic import linear_reset
reset_result = linear_reset(lm, power=2, use_f=True)
print('reset_result 결과: ', reset_result.pvalue)
print("선형성 만족" if reset_result.pvalue > 0.05 else "선형성 위배")
# reset_result 결과:  0.1408583001141254
# 선형성 만족

#시각화
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='grey')
plt.show()
print()

print("등분산성 검정: 모든 x값에서 오차의 퍼짐이 유사해야 한다")
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, sm.add_constant(df_lm['Sales']))
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print(f"breuschpagan test 결과: 통계량={bp_stat}, p-value={bp_pvalue}")
# breuschpagan test 결과: 통계량=5.75781527234569, p-value=0.016415470734784027
print("등분산성 만족" if bp_pvalue > 0.05 else "등분산성 위배")
# 등분산성 위배
# 시각화는 선형성 시각화 참조(?)
print()

print("독립성 검정: 다중회귀 분석 시 독립변수의 값이 서로 관련되지 않아야한다.")
# 잔차가 자기상관(인접 관측치의 오차가 상관됨)이 있는지 확인
# Durbin-Watson: 잔차의 자기상관(Autocorrelation) 검정 지표.
# 잔차들이 서로 독립적인가? 시간흐름 데이터에서 중요(시계열)
# 값의 범위는 0~4이고 2이면 정상(자기상관 없음). < 2이면 양의 자기 상관, >2이면 ~
# model.summary()로 확인가능
import statsmodels.api as sm
print('Durbin-Watson: ', sm.stats.stattools.durbin_watson(residual))    # 잔차를 넣어준다
# Durbin-Watson:  1.9314981270829592 // 만족. >> 근데 왜 죄다 0.05만 넘으면 만족이고 왜 0.05인가?
# >> 2에 근사하므로 잔차의 자기상관은 없다.(?)

print()
print("다중공선성 검정: 다중회귀 분석 시, 독립변수 간에 강한 상관관계가 있어서는 안된다.")
# VIF(Variance Inflation Factor, 분산 인플레 요인, 분산 팽창 지수)
# : 값이 10을 넘으면 다중 공선성이 발생하는 변수라고 볼 수 있다.
from statsmodels.stats.outliers_influence import variance_inflation_factor
df_ind = df[['Income','Advertising','Price','Age']]   # 독립변수들
vifdf = pd.DataFrame()
vifdf['변수'] = df_ind.columns
vifdf['vif_value'] = [variance_inflation_factor(df_ind.values, i)
                        for i in range(df_ind.shape[1])]
print(vifdf)
# 10을 넘지 않았으므로 모두 만족
#             변수  vif_value
# 0       Income   5.971040
# 1  Advertising   1.993726
# 2        Price   9.979281
# 3          Age   8.267760

# 시각화
sns.barplot(x="변수", y="vif_value", data=vifdf)
plt.title("VIF")
plt.show()




# 유의한 모델이므로 생성된 모델을 파일로 저장하고 이를 재사용
# 방법1:
# import pickle
# with open('carseat.pkl','wb') as obj:   # 저장
#     pickle.dump(lm,obj)
# with open('carseat.pkl','rb') as obj:   # 읽기
#     mymodel = pickle.load(lm,obj)

# 방법2:pickle은 binary로 i/o해야하므로 번거롭다
import joblib
joblib.dump(lm, 'carseat.model')
mymodel = joblib.load('carseat.model')

print("새로운 값으로 Sales 예측")
new_df = pd.DataFrame({"Income":[35, 62],"Advertising":[3, 6],"Price":[105, 88],"Age":[32, 55]})

pred = mymodel.predict(new_df)
print("Sales 예측 결과: ", pred.values)












