# 일원분산분석으로 평균 차이 검정
# 강남구에 있는 GS 편의점 3개 지역 알바생의 급여에 대한 평균 차이 검정
# 요인: "GS편의점"

# 귀무: GS편의점 3개 지역 알바생의 급여에 대한 평균은 차이가 없다.

import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib

uri = "https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/group3.txt"
# 읽기1
# data = pd.read_csv(uri, header=None)
# print(data) # type: DataFrame

# 읽기2
data = np.genfromtxt(urllib.request.urlopen(uri),delimiter=",")
print(data, type(data)) # <class 'numpy.ndarray'>
print(data.shape)       # (22, 2)    

# 3개 집단의 월급 정보 얻기
gr1 = data[data[:,1]==1,0]
gr2 = data[data[:,1]==2,0]
gr3 = data[data[:,1]==3,0]
print(gr1, ' ', np.mean(gr1))
print(gr2, ' ', np.mean(gr2))
print(gr3, ' ', np.mean(gr3))

print()
# 정규성 확인
print(stats.shapiro(gr1).pvalue)    # 0.3337
print(stats.shapiro(gr2).pvalue)    # 0.6561
print(stats.shapiro(gr3).pvalue)    # 0.8325

# 등분산성확인
print(stats.levene(gr1,gr2,gr3).pvalue)     # 0.0458 // 0.05에 좀 모자라지만 대충 넘어가도 된다?          
print(stats.bartlett(gr1,gr2,gr3).pvalue)   # 0.3508 // 0.05보다 확실히 크다.

# 데이터 퍼짐 정도 시각화
# plt.boxplot([gr1,gr2,gr3], showmeans=True)
# plt.show()

# 일원분산분석 방법1: anova_lm()
df = pd.DataFrame(data=data,columns=['pay','group'])
print(df)
lmodel = ols('pay ~ C(group)', data=df).fit()   # C(group): group은 범
print(anova_lm(lmodel, type=1))
# P=0.0435 < alpha=0.05 이므로 귀무 기각

# 일원분산분석 방법2: f_oneway()
f_stat, p_val = stats.f_oneway(gr1,gr2,gr3)
print('f_stat: ',f_stat)    # f_stat: 3.7113
print('p_val: ',p_val)      # p_val:  0.0435
print()

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
print(tukResult)

# 시각화
tukResult.plot_simultaneous(xlabel="mean", ylabel="group")
plt.show()

# 참고
# anova_lm(): 정규성, 등분산성이 깨지면 p-value 신뢰 불가
# f_oneway(): 정규성이 깨지면 stats.kruskal(), 등분산성이 깨지면 welch ANOVA 사용




















