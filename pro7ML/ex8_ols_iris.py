# 단순선형회귀 - iris dataset
# 상관관계가 약한 경우와 강한 경우로 회귀분석모델을 생성 후 비교

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head(3),type(iris))
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa <class 'pandas.core.frame.DataFrame'>
print(iris.iloc[:,0:4].corr())
#               sepal_length  sepal_width  petal_length  petal_width
# sepal_length      1.000000    -0.117570      0.871754     0.817941
# sepal_width      -0.117570     1.000000     -0.428440    -0.366126
# petal_length      0.871754    -0.428440      1.000000     0.962865
# petal_width       0.817941    -0.366126      0.962865     1.000000

print("\n연습1: 상관관계가 약한 변수를 사용. -0.117570")
result1 = smf.ols(formula='sepal_length ~ sepal_width',data=iris).fit()
print(result1.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:           sepal_length   R-squared:                       0.014
# Model:                            OLS   Adj. R-squared:                  0.007
# Method:                 Least Squares   F-statistic:                     2.074
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):              0.152
# Time:                        16:05:26   Log-Likelihood:                -183.00
# No. Observations:                 150   AIC:                             370.0
# Df Residuals:                     148   BIC:                             376.0
# Df Model:                           1
# Covariance Type:            nonrobust
# ===============================================================================
#                   coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------
# Intercept       6.5262      0.479     13.628      0.000       5.580       7.473
# sepal_width    -0.2234      0.155     -1.440      0.152      -0.530       0.083
# ==============================================================================
# Omnibus:                        4.389   Durbin-Watson:                   0.952
# Prob(Omnibus):                  0.111   Jarque-Bera (JB):                4.237
# Skew:                           0.360   Prob(JB):                        0.120
# Kurtosis:                       2.600   Cond. No.                         24.2
# ==============================================================================
print('R squared: ', result1.rsquared)
# R squared:  0.013822654141080859
print('p-value: ', result1.pvalues.iloc[1])
# p-value:  0.15189826071144905

# 시각화
plt.scatter(iris.sepal_width, iris.sepal_length)
plt.plot(iris.sepal_width, result1.predict(), color='r')

plt.show()


print("\n연습2: 상관관계가 강한 변수를 사용. 0.871754")
result2 = smf.ols(formula='sepal_length ~ petal_length',data=iris).fit()
print(result2.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:           sepal_length   R-squared:                       0.760
# Model:                            OLS   Adj. R-squared:                  0.758
# Method:                 Least Squares   F-statistic:                     468.6
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           1.04e-47
# Time:                        16:11:06   Log-Likelihood:                -77.020
# No. Observations:                 150   AIC:                             158.0
# Df Residuals:                     148   BIC:                             164.1
# Df Model:                           1
# Covariance Type:            nonrobust
# ================================================================================
#                    coef    std err          t      P>|t|      [0.025      0.975]
# --------------------------------------------------------------------------------
# Intercept        4.3066      0.078     54.939      0.000       4.152       4.462
# petal_length     0.4089      0.019     21.646      0.000       0.372       0.446
# ==============================================================================
# Omnibus:                        0.207   Durbin-Watson:                   1.867
# Prob(Omnibus):                  0.902   Jarque-Bera (JB):                0.346
# Skew:                           0.069   Prob(JB):                        0.841
# Kurtosis:                       2.809   Cond. No.                         10.3
# ==============================================================================
print('R squared: ', result2.rsquared)
# R squared:  0.7599546457725151
print('p-value: ', result2.pvalues.iloc[1])
# p-value:  1.0386674194497976e-47

# 시각화
plt.scatter(iris.petal_length, iris.sepal_length)
plt.plot(iris.petal_length, result2.predict(), color='b')
plt.show()


print("실제값: ",iris.sepal_length[:10].values)
# 실제값:  [5.1 4.9 4.7 4.6 5.  5.4 4.6 5.  4.4 4.9]
print("예측값: ",result2.predict()[:10])
# 예측값:  [4.8790946  4.8790946  4.83820238 4.91998683 4.8790946  5.00177129
#  4.8790946  4.91998683 4.8790946  4.91998683]

# 새로운 값으로 예측
new_data = pd.DataFrame({'petal_length':[1.1, 0.5, 6.0]})
y_pred = result2.predict(new_data)
print("예측결과: ", y_pred.values)
# 예측결과:  [4.75641792 4.51106455 6.76013708]


print("\n연습2: 독립변수를 복수로 사용 - 다중선형회귀")
# result3 = smf.ols(formula='sepal_length ~ petal_length + petal_width', data=iris).fit()
# print(result3.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:           sepal_length   R-squared:                       0.766
# Model:                            OLS   Adj. R-squared:                  0.763
# Method:                 Least Squares   F-statistic:                     241.0
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           4.00e-47
# Time:                        16:47:08   Log-Likelihood:                -75.023
# No. Observations:                 150   AIC:                             156.0
# Df Residuals:                     147   BIC:                             165.1
# Df Model:                           2
# Covariance Type:            nonrobust
# ================================================================================
#                    coef    std err          t      P>|t|      [0.025      0.975]
# --------------------------------------------------------------------------------
# Intercept        4.1906      0.097     43.181      0.000       3.999       4.382
# petal_length     0.5418      0.069      7.820      0.000       0.405       0.679
# petal_width     -0.3196      0.160     -1.992      0.048      -0.637      -0.002
# ==============================================================================
# Omnibus:                        0.383   Durbin-Watson:                   1.826
# Prob(Omnibus):                  0.826   Jarque-Bera (JB):                0.540
# Skew:                           0.060   Prob(JB):                        0.763
# Kurtosis:                       2.732   Cond. No.                         25.3
# ==============================================================================

column_select = "+".join(iris.columns.difference(['sepal_length','sepal_width','species']))
print(column_select)
result3 = smf.ols(formula='sepal_length ~ '+column_select, data=iris).fit()
print(result3.summary())
# petal_length+petal_width
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:           sepal_length   R-squared:                       0.766
# Model:                            OLS   Adj. R-squared:                  0.763
# Method:                 Least Squares   F-statistic:                     241.0
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           4.00e-47
# Time:                        16:50:52   Log-Likelihood:                -75.023
# No. Observations:                 150   AIC:                             156.0
# Df Residuals:                     147   BIC:                             165.1
# Df Model:                           2
# Covariance Type:            nonrobust
# ================================================================================
#                    coef    std err          t      P>|t|      [0.025      0.975]
# --------------------------------------------------------------------------------
# Intercept        4.1906      0.097     43.181      0.000       3.999       4.382
# petal_length     0.5418      0.069      7.820      0.000       0.405       0.679
# petal_width     -0.3196      0.160     -1.992      0.048      -0.637      -0.002
# ==============================================================================
# Omnibus:                        0.383   Durbin-Watson:                   1.826
# Prob(Omnibus):                  0.826   Jarque-Bera (JB):                0.540
# Skew:                           0.060   Prob(JB):                        0.763
# Kurtosis:                       2.732   Cond. No.                         25.3
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.





