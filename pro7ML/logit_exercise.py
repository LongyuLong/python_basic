# [로지스틱 분류분석 문제1]
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.

# logit vs glm?+
# 토/일 만 남기고
import pandas as pd

# 1. 데이터 생성
data = [
    ['토',0,57], ['토',0,39], ['토',0,28], ['화',1,60], ['토',0,31], 
    ['월',1,42], ['토',1,54], ['토',1,65], ['토',0,45], ['토',0,37], 
    ['토',1,98], ['토',1,60], ['토',0,41], ['토',1,52], ['일',1,75], 
    ['월',1,45], ['화',0,46], ['수',0,39], ['목',1,70], ['금',1,44], 
    ['토',1,74], ['토',1,65], ['토',0,46], ['토',0,39], ['일',1,60], 
    ['토',1,44], ['일',0,30], ['토',0,34]
]

columns = ['요일', '외식유무', '소득수준']
df = pd.DataFrame(data, columns=columns)

# 2. 토/일 데이터만 필터링
rows = []
for i in range(len(df)):
    week = df.loc[i,'요일']
    if week == '토' or week == '일':
        rows.append(df.loc[i])
weekend = pd.DataFrame(rows)
# print(weekend)    # 토/일만 거르기 완료

# 소득수준에 따른 외식 빈도 영향이니까
# income = df['소득수준']
# rest = df['외식유무']

# logit
import statsmodels.formula.api as smf
import numpy as np
formula = '외식유무 ~ 소득수준'
result = smf.logit(formula=formula, data=weekend).fit()
print(result.summary())
#                            Logit Regression Results
# ==============================================================================
# Dep. Variable:                외식유무   No. Observations:                   21
# Model:                          Logit   Df Residuals:                       19
# Method:                           MLE   Df Model:                            1
# Date:                Tue, 07 Apr 2026   Pseudo R-squ.:                  0.6240
# Time:                        17:14:02   Log-Likelihood:                -5.4648
# converged:                       True   LL-Null:                       -14.532
# Covariance Type:            nonrobust   LLR p-value:                 2.058e-05
# ==============================================================================
#                  coef    std err          z      P>|z|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept    -11.8668      4.982     -2.382      0.017     -21.632      -2.102
# 소득수준        0.2375      0.100      2.366      0.018       0.041       0.434
# ==============================================================================

pred = result.predict(weekend)
# print(pred)
print('예측값: ', pred.values)              
print("예측값: ", np.around(pred.values))  
# 예측값:  [1. 0. 0. 0. 1. 1. 0. 0. 1. 1. 0. 1. 1. 1. 1. 0. 0. 1. 0. 0. 0.]

print("실제값: ", weekend['외식유무'].values)
# 실제값:  [0 0 0 0 1 1 0 0 1 1 0 1 1 1 1 0 0 1 1 0 0]
print('---- 수치에 대한 집계표(Confusion Matrix, 혼동행렬) 확인 ----')
conf_tab = result.pred_table()
print(conf_tab)

from sklearn.metrics import accuracy_score
print("분류 정확도: ", accuracy_score(weekend['외식유무'], np.around(pred)))
# 분류 정확도:  0.9047619047619048

a = int(input("소득 수준을 입력하세요: "))
input_data = pd.DataFrame({'소득수준': [a]})
pred_prob = result.predict(input_data)
print(pred_prob)

print("------- glm -------")
import statsmodels.api as sm

result2 = smf.glm(formula=formula, data=weekend, family=sm.families.Binomial()).fit()
print(result2.summary())
#                  Generalized Linear Model Regression Results
# ==============================================================================
# Dep. Variable:                외식유무   No. Observations:                   21
# Model:                            GLM   Df Residuals:                       19
# Model Family:                Binomial   Df Model:                            1
# Link Function:                  Logit   Scale:                          1.0000
# Method:                          IRLS   Log-Likelihood:                -5.4648
# Date:                Tue, 07 Apr 2026   Deviance:                       10.930
# Time:                        17:42:23   Pearson chi2:                     11.7
# No. Iterations:                     7   Pseudo R-squ. (CS):             0.5783
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          z      P>|z|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept    -11.8668      4.982     -2.382      0.017     -21.632      -2.102
# 소득수준        0.2375      0.100      2.366      0.018       0.041       0.434
# ==============================================================================

glm_pred = result2.predict(weekend)
print('glm 예측값: ', np.around(glm_pred.values))
print('glm 실제값: ', weekend['외식유무'].values)
# glm 예측값:  [1. 0. 0. 0. 1. 1. 0. 0. 1. 1. 0. 1. 1. 1. 1. 0. 0. 1. 0. 0. 0.]
# glm 실제값:  [0 0 0 0 1 1 0 0 1 1 0 1 1 1 1 0 0 1 1 0 0]
print('glm 모델 분류 정확도: ', accuracy_score(weekend['외식유무'], np.around(glm_pred)))
# glm 모델 분류 정확도:  0.9047619047619048
b = int(input("소득 수준을 입력하세요: "))
input_data2 = pd.DataFrame({'소득수준': [b]})
pred_prob2 = result2.predict(input_data2)
print(pred_prob2)
# 소득 수준을 입력하세요: 80
# 0    0.999203
# dtype: float64
