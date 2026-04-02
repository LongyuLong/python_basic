# 어느 음식점의 매출 데이터와 기상청이 제공한 날씨 데이터를 활용하여
# 강수 여부에 따른 매출 변화 분석
# 두 집단: 강수량이 있을 때, 맑을 때

# 귀무: 어느 음식점의 매출 데이터는 강수 여부에 따라 매출액 평균 차이 없다.
# 대립: 어느 음식점의 매출 데이터는 강수 여부에 따라 매출액 평균 차이 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

pd.set_option("display.max_columns", None)
# 매출 데이터 읽기
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/tsales.csv",
                            dtype={'YMD':'object'}) # int -> object
print(sales_data.head(3))
#         YMD    AMT  CNT
# 0  20190514      0    1
# 1  20190519  18000    1
# 2  20190521  50000    4
print(sales_data.info())
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   YMD     328 non-null    int64
#  1   AMT     328 non-null    int64
#  2   CNT     328 non-null    int64

# 날씨 데이터 읽기
weather_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/tweather.csv")
print(weather_data.head(2)) # 328 * 3
#    stnId          tm  avgTa  minTa  maxTa  sumRn  maxWs  avgWs  ddMes
# 0    108  2018-06-01   23.8   17.5   30.2    0.0    4.3    1.9    0.0
# 1    108  2018-06-02   23.4   17.6   30.1    0.0    4.5    2.0    0.0
print(weather_data.info())  # 702 * 9
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   stnId   702 non-null    int64
#  1   tm      702 non-null    object
#  2   avgTa   702 non-null    float64
#  3   minTa   702 non-null    float64
#  4   maxTa   702 non-null    float64
#  5   sumRn   702 non-null    float64
#  6   maxWs   702 non-null    float64
#  7   avgWs   702 non-null    float64
#  8   ddMes   702 non-null    float64

print()
# sales: YMD 20190514, weather: tm 2018-06-01 병합을 위해 데이터 가공 필요
weather_data.tm = weather_data.tm.map(lambda x:x.replace("-",""))   # map, lambda 에 대해서는 설명필요
print(weather_data.head(2))

# YMD, tm를 merge
frame = sales_data.merge(weather_data, how="left", left_on='YMD', right_on="tm")
print(frame.columns)
# Index(['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn',
#        'maxWs', 'avgWs', 'ddMes'],
print(frame.head(), " ", len(frame))
#    avgWs  ddMes
# 0    1.6    0.0
# 1    1.2    0.0
# 2    2.9    0.0
# 3    2.4    0.0
# 4    1.7    0.0   328

data = frame.iloc[:,[0,1,7,8]]  # YMD, AMT, maxTa, sumRn
print(data.head())
#         YMD     AMT  maxTa  sumRn
# 0  20190514       0   26.9    0.0
# 1  20190519   18000   21.6   22.0
# 2  20190521   50000   23.8    0.0
# 3  20190522  125000   26.5    0.0
# 4  20190523  222500   29.2    0.0

print(data.maxTa.describe())
# plt.boxplot(data.maxTa)
# plt.show()

# 온도를 세 그룹으로 분리(int->범주형)
print(data.isnull().sum())
data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0,1,2])
print(data.head(3),' ',data["ta_gubun"].unique())
#         YMD    AMT  maxTa  sumRn ta_gubun
# 0  20190514      0   26.9    0.0        2
# 1  20190519  18000   21.6   22.0        1
# 2  20190521  50000   23.8    0.0        1   [2, 1, 0]
# Categories (3, int64): [0 < 1 < 2]

# 정규성, 등분산성
x1 = np.array(data[data.ta_gubun == 0].AMT)     # 이런 표현이 너무 안와닿는다;;
x2 = np.array(data[data.ta_gubun == 1].AMT)
x3 = np.array(data[data.ta_gubun == 2].AMT)
print(x1[:5])

print()
print(stats.levene(x1, x2, x3).pvalue)      # 0.03900   만족X
print(stats.bartlett(x1, x2, x3).pvalue)    # 0.00967
print()
print("정규성 체크")
print(stats.shapiro(x1).pvalue) # 0.2481924204382751    만족 --- 등분산성은 만족못하는
print(stats.shapiro(x2).pvalue) # 0.03882572120522948   불만족
print(stats.shapiro(x3).pvalue) # 0.3182989573650957    만족

# 온도별 매출액 평균
np.set_printoptions(suppress=True, precision=10)
spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())

print(np.mean(x1))  # 1032362.3188405797
print(np.mean(x2))  # 818106.8702290077
print(np.mean(x3))  # 553710.9375

group1 = x1
group2 = x2
group3 = x3

# plt.boxplot([group1, group2, group3], showmeans=3)
# plt.show()    개형 확인

print(stats.f_oneway(group1, group2, group3))
# F_onewayResult statistic=99.1908, pvalue=2.3607e-34
# 해석: pvalue < 0.05 이므로 귀무 기각 >> 온도에 따른 매출 차이가 있다~

# 정규성 깨지면 stats.kruskal() 사용, 등분산성이 깨지면 welch's ANOVA
print(stats.kruskal(group1, group2, group3))
# KruskalResult statistic=132.7022, pvalue=1.5278e-29
# 해석: pvalue < 0.05로 귀무기각 
print()
print("---- Welch's ANOVA ----")
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(dv="AMT", between='ta_gubun', data=data)) # 함수에 대한 설명 추가 필요
#      Source  ddof1     ddof2           F         p_unc       np2
# 0  ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038
# p_unc = 7.907e-35로 0.05보다 작으므로 귀무 기각

print()
# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['ta_gubun'], alpha=0.05)
print(tukResult)

#시각화
tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
