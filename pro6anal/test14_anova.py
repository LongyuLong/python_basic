# 세 개 이상의 모집단에 대한 가설검정 – 분산분석
# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 요인
# 에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
# 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나눠진 각 집단 내의
# 분산으로 나누고, 요인에 의한 분산이 의미있는 크기를 가지는지 검정한다
# f값 = (집단 간 분석 / 집단 내 분석)

# 서로 독립인 세 집단의 평균 차이 검정
# 일원 분산 분석(One Way ANOVA)
# 실습) 세 가지 교육 방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기 시험을 실시
# three_sample.csv 사용
# 한 개의 요인: 교육 방법, 방법의 종류가 3가지(그룹이 3개)
# 독립변수(범주형)=교육방법, 종속변수(연속형)= 실기시험 평균 점수

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
# ols(Ordinary Least Square): 추정 및 검정, 회귀, 시계열 분석 등의...

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/three_sample.csv")
print(data.head(3), ' ', len(data))
print(data.describe())  # max 500으로 score에 이상치 존재확인

# 이상치(Outlier)를 시각화
import matplotlib.pyplot as plt
# plt.boxplot(data.score)
# plt.show()      # outlier 2개 확인

data = data.query("score<=100")
print(len(data))        # 80 -> 78개
print(data.describe())  # max 100으로 변화

# 교차표 (교육 방법 별 )
data2 = pd.crosstab(index=data['method'], columns='count')
data2.index=['방법1','방법2','방법3']
data2.columns=['교육생 수']
print(data2)

# 교차표 (교육방법 별 만족 건수)
data3 = pd.crosstab(data['method'], data['survey'])
data3.index = ['방법1','방법2','방법3']
data3.columns = ['만족', '불만족']
print(data3)

print("------------ ANOVA 검정 --------------")
import statsmodels.api as sm
lin_model = ols("data['score']~data['method']", data=data).fit()       # 회귀분석 모델 생성
result = sm.stats.anova_lm(lin_model, typ=1)
print(result)

#                  df(자유도)        sum_sq(제곱합)       mean_sq(제곱평균)   F(F값)        PR(>F)(p값)
# data['method']   1.0              27.980888           27.980888        0.122228      0.727597
# Residual        76.0              17398.134497        228.922822       NaN           NaN  
# 해석 : p-value 0.72759 > alapha 0.5 이므로 귀무가설 채택 

# 27.980888/228.922822 = 0.122228
# 제곱 평균을 나누면 F값이 나온다.

f_value = result.loc["data['method']","F"]
p_value = result.loc["data['method']","PR(>F)"]
print('f_value : ',f_value)
print('p_value : ',p_value)
# 사후분석(Post Hoc Analysis)하기
# 세가지 교육방법에 따른 시험 점수에 차이여부는 알려주지만
# 정확히 어느 그룹의 평균값이 의미가 있는지는 알려주지 않는다. 그룹간 평균 차이를 구체적으로 알려주지 않음
# 그러므로 그룹간의 관계를 보기 위해 구가적인 사후분석(Post Hoc Analysis)이 필요하다.

from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukResult = pairwise_tukeyhsd(endog=data['score'],groups=data['method'])
print(tukResult)

# Multiple Comparison of Means - Tukey HSD, FWER=0.05 
# ====================================================
# group1 group2 meandiff p-adj   lower   upper  reject
# ----------------------------------------------------
#      1      2   0.9725 0.9702 -8.9458 10.8909  False  : 유의미한 차이가 없으면 False
#      1      3   1.4904 0.9363 -8.8183  11.799  False  : 유의미한 차이가 있으면 True
#      2      3   0.5179 0.9918 -9.6125 10.6483  False
# ----------------------------------------------------

# Tukey HSD 결과 시각화
tukResult.plot_simultaneous(xlabel ='mean', ylabel='group')
plt.show()
# Tukey HSD : 원래 반복수가 동일하다는 가정하에 고안된 방법
# 집단간 평균 차이를 정밀하게 확인 가능
# 각 집단의 표본수의 차이가 크면 결과의 신뢰가 떨어짐









