# LogisticRegression(로지스틱 회귀분석)
# 선형결합을 로그오즈(logit())로 해석하고, 이를 시그모이드 함수를 통해 확률로 변환
# 이항분류(다항도 가능), 독립변수:연속형, 종속변수: 범주형
# LogisticRegression을 근거로 뉴럴네트워크의 뉴런에서 사용함

# mtcars dataset 사용
import statsmodels.api as sm

mtcarsdata = sm.datasets.get_rdataset('mtcars')
print(mtcarsdata.keys())
# dict_keys(['data', '__doc__', 'package', 'title', 'from_cache', 'raw_data'])
#                 mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
# rownames
# Mazda RX4      21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
# Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
# Datsun 710     22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
print()
print(mtcars.info())
# <class 'pandas.core.frame.DataFrame'>
# Index: 32 entries, Mazda RX4 to Volvo 142E
# Data columns (total 11 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   mpg     32 non-null     float64
#  1   cyl     32 non-null     int64
#  2   disp    32 non-null     float64
#  3   hp      32 non-null     int64
#  4   drat    32 non-null     float64
#  5   wt      32 non-null     float64
#  6   qsec    32 non-null     float64
#  7   vs      32 non-null     int64
#  8   am      32 non-null     int64
#  9   gear    32 non-null     int64
#  10  carb    32 non-null     int64
# dtypes: float64(5), int64(6)

# 연비와 마력수에 따른 변속기 분류
mtcar = mtcars.loc[:,['mpg','hp','am']]
print(mtcar.head())
#                     mpg   hp  am
# rownames
# Mazda RX4          21.0  110   1
# Mazda RX4 Wag      21.0  110   1
# Datsun 710         22.8   93   1
# Hornet 4 Drive     21.4  110   0
# Hornet Sportabout  18.7  175   0

print(mtcar['am'].unique())     # [1(수동) 0(자동)]
# [1 0]
# Optimization terminated successfully.
#          Current function value: 0.300509
#          Iterations 9

# 모델 작성 방법 1: logit()
import statsmodels.formula.api as smf
import numpy as np
formula = 'am ~ hp + mpg'       # '연속형 ~ 범주형 + ... '
result = smf.logit(formula=formula, data=mtcar).fit()
print(result.summary())
#                            Logit Regression Results
# ==============================================================================
# Dep. Variable:                     am   No. Observations:                   32
# Model:                          Logit   Df Residuals:                       29
# Method:                           MLE   Df Model:                            2
# Date:                Tue, 07 Apr 2026   Pseudo R-squ.:                  0.5551
# Time:                        15:45:57   Log-Likelihood:                -9.6163
# converged:                       True   LL-Null:                       -21.615
# Covariance Type:            nonrobust   LLR p-value:                 6.153e-06
# ==============================================================================
#                  coef    std err          z      P>|z|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept    -33.6052     15.077     -2.229      0.026     -63.156      -4.055
# hp             0.0550      0.027      2.045      0.041       0.002       0.108
# mpg            1.2596      0.567      2.220      0.026       0.147       2.372
# ==============================================================================
pred = result.predict(mtcar[:10])

print('예측값: ', pred.values)              # [0.25004729 0.25004729 0.55803435 0.35559974 0.39709691 0.00651918 0.10844152 0.63232168 0.58498645 0.06598365]   
print("예측값: ", np.around(pred.values))   # np.around = 0.5기준으로 
# 예측값:  [0. 0. 1. 0. 0. 0. 0. 1. 1. 0.]

print("실제값: ", mtcar['am'][:10].values)
# 실제값:  [1 1 1 0 0 0 0 0 0 0]

print()
print('---- 수치에 대한 집계표(Confusion Matrix, 혼동행렬) 확인 ----')
conf_tab = result.pred_table()
print(conf_tab)
# [[16.  3.]  TP FN
#  [ 3. 10.]] FP TN
# Recall : 전체 P 중 TP 비율
# Precision: TP+FP 중 TP 비율
# Accuracy: 

print("분류 정확도: ", (16+10) / len(mtcar))
print("분류 정확도: ", (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar))
# 분류 정확도:  0.8125
# 분류 정확도:  0.8125

# 모듈로 확인2 - accuracy_score 활용
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print("분류 정확도: ", accuracy_score(mtcar['am'], np.around(pred2)))
# 분류 정확도:  0.8125

print("----------모델 작성방법 2: glm()------------")

# 모델 작성방법 2: glm() -- 일반화된 선형모델
result2 = smf.glm(formula=formula, data=mtcar, family=sm.families.Binomial()).fit()
# Binomial: 이항 분포, Gaussian
print(result2.summary())
#                  Generalized Linear Model Regression Results
# ==============================================================================
# Dep. Variable:                     am   No. Observations:                   32
# Model:                            GLM   Df Residuals:                       29
# Model Family:                Binomial   Df Model:                            2
# Link Function:                  Logit   Scale:                          1.0000
# Method:                          IRLS   Log-Likelihood:                -9.6163
# Date:                Tue, 07 Apr 2026   Deviance:                       19.233
# Time:                        16:16:10   Pearson chi2:                     16.1
# No. Iterations:                     7   Pseudo R-squ. (CS):             0.5276
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          z      P>|z|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept    -33.6052     15.077     -2.229      0.026     -63.155      -4.055
# hp             0.0550      0.027      2.045      0.041       0.002       0.108
# mpg            1.2596      0.567      2.220      0.026       0.147       2.372
# ==============================================================================

glm_pred = result2.predict(mtcar[:10])
print('glm 예측값: ', np.around(glm_pred.values))
print('glm 실제값: ', mtcar['am'][:10].values)
# glm 예측값:  [0. 0. 1. 0. 0. 0. 0. 1. 1. 0.]
# glm 실제값:  [1 1 1 0 0 0 0 0 0 0]
glm_pred2 = result2.predict(mtcar)
print('glm 모델 분류 정확도: ', accuracy_score(mtcar['am'], np.around(glm_pred2)))
# glm 모델 분류 정확도:  0.8125

# logit()은 변환함수, glm()은 logit()을 포함한 전체 모델
import pandas as pd
print("---- 새로운 값으로 분류 ----")
newdf = pd.DataFrame()
newdf['mpg'] = [10, 30, 120, 200]
newdf['hp'] = [100, 110, 80, 130]
print(newdf)
#    mpg   hp
# 0   10  100
# 1   30  110
# 2  120   80
# 3  200  130
new_pred = result2.predict(newdf)
print("예측 결과: ", np.around(new_pred.values))
print("예측 결과: ", np.rint(new_pred.values))
# 예측 결과:  [0. 1. 1. 1.]
# 예측 결과:  [0. 1. 1. 1.]












