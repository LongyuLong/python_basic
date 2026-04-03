# 선형회귀분석: mtcars dataset
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import koreanize_matplotlib
import statsmodels.api

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)
# mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb

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

# x: hp(마력수), y: mpg(연비)
print(mtcars.corr())
#            mpg       cyl      disp        hp      drat        wt      qsec        vs        am      gear      carb
# mpg   1.000000 -0.852162 -0.847551 -0.776168  0.681172 -0.867659  0.418684  0.664039  0.599832  0.480285 -0.550925
# cyl  -0.852162  1.000000  0.902033  0.832447 -0.699938  0.782496 -0.591242 -0.810812 -0.522607 -0.492687  0.526988
# disp -0.847551  0.902033  1.000000  0.790949 -0.710214  0.887980 -0.433698 -0.710416 -0.591227 -0.555569  0.394977
# hp   -0.776168  0.832447  0.790949  1.000000 -0.448759  0.658748 -0.708223 -0.723097 -0.243204 -0.125704  0.749812
# drat  0.681172 -0.699938 -0.710214 -0.448759  1.000000 -0.712441  0.091205  0.440278  0.712711  0.699610 -0.090790
# wt   -0.867659  0.782496  0.887980  0.658748 -0.712441  1.000000 -0.174716 -0.554916 -0.692495 -0.583287  0.427606
# qsec  0.418684 -0.591242 -0.433698 -0.708223  0.091205 -0.174716  1.000000  0.744535 -0.229861 -0.212682 -0.656249
# vs    0.664039 -0.810812 -0.710416 -0.723097  0.440278 -0.554916  0.744535  1.000000  0.168345  0.206023 -0.569607
# am    0.599832 -0.522607 -0.591227 -0.243204  0.712711 -0.692495 -0.229861  0.168345  1.000000  0.794059  0.057534
# gear  0.480285 -0.492687 -0.555569 -0.125704  0.699610 -0.583287 -0.212682  0.206023  0.794059  1.000000  0.274073
# carb -0.550925  0.526988  0.394977  0.749812 -0.090790  0.427606 -0.656249 -0.569607  0.057534  0.274073  1.000000

print(np.corrcoef(mtcars.hp, mtcars.mpg))
# [[ 1.         -0.77616837]
#  [-0.77616837  1.        ]]
print(np.corrcoef(mtcars.wt, mtcars.mpg))
# [[ 1.         -0.86765938]
#  [-0.86765938  1.        ]]

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel("마력수")
# plt.ylabel("연비")
# plt.show()
print("---- 단순선형회귀 ----")
result = smf.ols(formula='mpg ~ hp', data=mtcars).fit()
print(result.summary())

# yhat = -0.0682 * x + 30.0989
print("마력수 110에 대한 연비 예측값: ", -0.0682 * 110 + 30.0989)   # 22.5969
print("마력수 110에 대한 연비 예측값: ", result.predict(pd.DataFrame({'hp':[110]})).values)

print("\n---- 다중선형회귀 ----")
result2 = smf.ols(formula='mpg ~ hp + wt', data=mtcars).fit()
print(result2.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                    mpg   R-squared:                       0.827
# Model:                            OLS   Adj. R-squared:                  0.815
# Method:                 Least Squares   F-statistic:                     69.21
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           9.11e-12
# Time:                        17:12:27   Log-Likelihood:                -74.326
# No. Observations:                  32   AIC:                             154.7
# Df Residuals:                      29   BIC:                             159.0
# Df Model:                           2
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept     37.2273      1.599     23.285      0.000      33.957      40.497
# hp            -0.0318      0.009     -3.519      0.001      -0.050      -0.013
# wt            -3.8778      0.633     -6.129      0.000      -5.172      -2.584
# ==============================================================================
# Omnibus:                        5.303   Durbin-Watson:                   1.362
# Prob(Omnibus):                  0.071   Jarque-Bera (JB):                4.046
# Skew:                           0.855   Prob(JB):                        0.132
# Kurtosis:                       3.332   Cond. No.                         588.
# ==============================================================================

#                  coef
# hp            -0.0318
# wt            -3.8778
print("마력수 110 + 무게 5에 대한 연비 예측값: ", \
        (-0.0318 * 110) + (-3.8778 * 5) + 37.2273)  # 14.3403

print("마력수 110 + 무게 5에 대한 연비 예측값: ", \
        result2.predict(pd.DataFrame({'hp':[110], 'wt':[5]})).values)  # [14.34309224]

print("\n추정치 구하기 -- 차체무게를 입력해 연비 추정 --")
result3 = smf.ols(formula='mpg ~ wt', data=mtcars).fit()
print(result3.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                    mpg   R-squared:                       0.753
# Model:                            OLS   Adj. R-squared:                  0.745
# Method:                 Least Squares   F-statistic:                     91.38
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           1.29e-10
# Time:                        17:21:41   Log-Likelihood:                -80.015
# No. Observations:                  32   AIC:                             164.0
# Df Residuals:                      30   BIC:                             167.0
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept     37.2851      1.878     19.858      0.000      33.450      41.120
# wt            -5.3445      0.559     -9.559      0.000      -6.486      -4.203
# ==============================================================================
# Omnibus:                        2.988   Durbin-Watson:                   1.252
# Prob(Omnibus):                  0.225   Jarque-Bera (JB):                2.399
# Skew:                           0.668   Prob(JB):                        0.301
# Kurtosis:                       2.877   Cond. No.                         12.7
# ==============================================================================
print("결정계수: ", result3.rsquared)
# 결정계수:  0.7528327936582646
pred = result3.predict()
print("result3 연비 예측값: ", pred[:5])
# result3 연비 예측값:  [23.28261065 21.9197704  24.88595212 20.10265006 18.90014396]


# 새로운 차체 무게로 연비 추정
mtcars.wt = float(input('차체무게 입력: '))
new_pred = result3.predict(pd.DataFrame(mtcars.wt))
print(f"차체무게 {mtcars.wt[0]}일 때, 예상 연비는 {new_pred[0]}")
# 6입력 -- 차체무게 6.0일 때, 예상 연비는 5.218296731005971




