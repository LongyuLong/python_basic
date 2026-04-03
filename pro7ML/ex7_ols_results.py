# 단순 선형회귀: ols의 Regression

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/drinking_water.csv")

print(df.head(3))
print(df.corr())
#    친밀도  적절성  만족도
# 0    3    4    3
# 1    3    3    2
# 2    4    4    4
#           친밀도       적절성       만족도
# 친밀도  1.000000  0.499209  0.467145
# 적절성  0.499209  1.000000  0.766853
# 만족도  0.467145  0.766853  1.000000
model = smf.ols(formula="만족도 ~ 적절성", data = df).fit()

print(model.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                    만족도   R-squared:                       0.588
# Model:                            OLS   Adj. R-squared:                  0.586
# Method:                 Least Squares   F-statistic:                     374.0
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           2.24e-52
# Time:                        14:42:33   Log-Likelihood:                -207.44
# No. Observations:                 264   AIC:                             418.9
# Df Residuals:                     262   BIC:                             426.0
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      0.7789      0.124      6.273      0.000       0.534       1.023
# 적절성            0.7393      0.038     19.340      0.000       0.664       0.815
# ==============================================================================
# Omnibus:                       11.674   Durbin-Watson:                   2.185
# Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003
# Skew:                          -0.328   Prob(JB):                     0.000335
# Kurtosis:                       4.012   Cond. No.                         13.4
# ==============================================================================

print('parameters: ',model.params)
# parameters:  
# Intercept    0.778858
# 적절성          0.739276
print('R-squared: ',model.rsquared)
# R-squared:  0.5880630629464404
print('p-value: ',model.pvalues)
# p-value:
# Intercept    1.454388e-09
# 적절성          2.235345e-52
print('predict values: ',model.predict()[:5])
# predict values:  [3.73596305 2.99668687 3.73596305 2.25741069 2.25741069]
print("실제값: ",df.만족도[:5].values)

plt.scatter(df.적절성, df.만족도)
slope, intertcept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, slope * df.적절성 + intertcept, c='b')
plt.show()

