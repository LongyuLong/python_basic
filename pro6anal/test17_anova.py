# 이원분산분석: 요인 복수 - 각 요인의 레벨(그룹)도 복수
# 두 개의 요인에 대한 집단(독립변수) 각각이 종속 변수(평균)에 영향을 주는지 검정
# 주 효과: 독립변수들이 각각 독리적으로 종속 변수에 미치는 영향을 검정하는 것
# 상호작용효과(교호 작용): 독립 변수들이 서로 연관되어 종속변수에 미치는 영향을 검정하는것
# 하나의 독립변수가 종속변수에 미치는 영향이 다른 독립변수의 수준에 따라 달라지는 현상 (?)

# 실습1: 태아 수와 관측자 수가 태아의 머리둘레 평균에 영향을 주는가?
# 주효과 가설
# 귀무: 태아 수와 태아의 머리둘레 평균은 차이가 없다
# 대립: 있다
# 교호작용 가설
# 귀무: 교호작용 없다(태아수와 관측자 수는 관련이 없다)
# 대립: 있다

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3_2.txt")
print(data.head(3), data.shape)
print(data['태아수'].unique())
print(data['관측자수'].unique())

# data.boxplot(column='머리둘레', by="태아수")
# plt.show()
# data.boxplot(column='머리둘레', by="관측자수")
# plt.show()

# linreg = ols("머리둘레 ~ C(태아수) + C(관측자수)", data=data).fit()     # 교호작용 고려 X
#             df      sum_sq     mean_sq            F        PR(>F)
# C(태아수)     2.0  324.008889  162.004444  2023.182239  1.006291e-32
# C(관측자수)    3.0    1.198611    0.399537     4.989593  6.316641e-03
# Residual  30.0    2.402222    0.080074          NaN           NaN

linreg = ols("머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)", data=data).fit()
# # └ 교호작용 고려 O --> C(태아수):C(관측자수)
#                   df      sum_sq     mean_sq            F        PR(>F)
# C(태아수)           2.0  324.008889  162.004444  2113.101449  1.051039e-27
# C(관측자수)          3.0    1.198611    0.399537     5.211353  6.497055e-03
# C(태아수):C(관측자수)   6.0    0.562222    0.093704     1.222222  3.295509e-01
# Residual        24.0    1.840000    0.076667          NaN           NaN

# linreg = ols("머리둘레 ~ C(태아수) * C(관측자수)", data=data).fit()
#                       df      sum_sq      mean_sq          F           PR(>F)
# C(태아수)             2.0     324.008889   162.004444  2113.101449    1.051039e-27
# C(관측자수)           3.0     1.198611     0.399537     5.211353      6.497055e-03
# C(태아수):C(관측자수)  6.0     0.562222    0.093704     1.222222       3.295509e-01
# Residual              24.0    1.840000    0.076667          NaN           NaN

# 해석: 
# 태아수 -- PR은 0.05보다 작음 >> 귀무기각. 태아수와 태아의 머리둘레 평균은 차이가 있다
# 관측자수 -- 0.006으로 0.05보다 작음 >> 귀무 기각. 관측자 수와 태아의 머리둘레 평균은 차이가 있다
# 상호작용 -- 0.329로 0.05보다 큼 >> 귀무 채택. 교호작용이 없다.
# >> 태아수와 관측자 수는 각각 종속변수에 유의한 영향을 미친다.(?)
#    그러나 태아수와 관측자 수 간의 상호작용효과는 유의하지 않다.
#    주효과는 있으나 상호작용은 없다.

pd.set_option('display.max_columns',None)
result = anova_lm(linreg, type=2)
print(result)

print("------------------------")
# 실습2: poison과 treat가 독 퍼짐 시간의 평균에 영향을 주는가?
# 주효과 가설
# 귀무1: poison종류와 독 퍼짐 시간의 평균은 차이가 없다.
# 귀무2: treat(응급처치) 방법과 독 퍼짐 시간의 평균은 차이가 없다.
# 교호작용 가설
# 귀무(교호): poison 종류와 응급처치 방법은 관련이 없다.

data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/poison_treat.csv")
print(data2.head(3), data2.shape)
print(data2.groupby('poison').agg(len))
print(data2.groupby('treat').agg(len))
print(data2.groupby(['poison','treat']).agg(len))
# 요인별 레벨의 표본수는 4로 동일하다.(모든 집단 별 표본수 동일하므로 균형설계가 잘 되었다고 볼 수 있다.)
#         Unnamed: 0  time  treat
# poison
# 1               16    16     16
# 2               16    16     16
# 3               16    16     16
#        Unnamed: 0  time  poison
# treat
# A              12    12      12
# B              12    12      12
# C              12    12      12
# D              12    12      12
#               Unnamed: 0  time
# poison treat
# 1      A               4     4
#        B               4     4
#        C               4     4
#        D               4     4
# 2      A               4     4
#        B               4     4
#        C               4     4
#        D               4     4
# 3      A               4     4
#        B               4     4
#        C               4     4
#        D               4     4

result2 = ols("time ~ C(poison) * C(treat)", data=data2).fit()
print(anova_lm(result2))
#                       df    sum_sq   mean_sq          F        PR(>F)
# C(poison)            2.0  1.033013  0.516506  23.221737  3.331440e-07
# C(treat)             3.0  0.921206  0.307069  13.805582  3.777331e-06
# C(poison):C(treat)   6.0  0.250138  0.041690   1.874333  1.122506e-01
# Residual            36.0  0.800725  0.022242        NaN           NaN
# 해석: 
# Poison -- PR은 0.05보다 작음 >> 귀무기각. poison종류와 독 퍼짐 시간의 평균은 차이가 있다
# Treat -- 0.006으로 0.05보다 작음 >> 귀무 기각. treat(응급처치) 방법과 독 퍼짐 시간의 평균은 차이가 있다
# 상호작용 -- 0.329로 0.05보다 큼 >> 귀무 채택. 교호작용이 없다. poison종류와 treat 종류는 관련이 없다.
# 주효과는 있음, 상호 작용은 없음

# 사후 분석
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tkResult1 = pairwise_tukeyhsd(endog=data2.time, groups=data2.poison)
print("poison 사후분석\n",tkResult1)
tkResult1.plot_simultaneous(xlabel="mean of time", ylabel='poison')
# poison 사후분석
#  Multiple Comparison of Means - Tukey HSD, FWER=0.05 
# ====================================================
# group1 group2 meandiff p-adj   lower   upper  reject
# ----------------------------------------------------
#      1      2  -0.0731 0.5882 -0.2525  0.1063  False
#      1      3  -0.3412 0.0001 -0.5206 -0.1619   True
#      2      3  -0.2681 0.0021 -0.4475 -0.0887   True
# ----------------------------------------------------
tkResult2 = pairwise_tukeyhsd(endog=data2.time, groups=data2.treat)
print("treat 사후분석\n",tkResult2)
tkResult2.plot_simultaneous(xlabel="mean of time", ylabel='treat')
# treat 사후분석
#  Multiple Comparison of Means - Tukey HSD, FWER=0.05 
# ====================================================
# group1 group2 meandiff p-adj   lower   upper  reject
# ----------------------------------------------------
#      A      B   0.3625  0.001  0.1253  0.5997   True
#      A      C   0.0783 0.8143 -0.1589  0.3156  False
#      A      D     0.22 0.0778 -0.0172  0.4572  False
#      B      C  -0.2842 0.0132 -0.5214 -0.0469   True
#      B      D  -0.1425  0.387 -0.3797  0.0947  False
#      C      D   0.1417 0.3922 -0.0956  0.3789  False
# ----------------------------------------------------
plt.show()
plt.close()


