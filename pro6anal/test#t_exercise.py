print("[one-sample t 검정 : 문제1]")
# 영사기( 프로젝터 )에 사용되는 구형 백열전구의 수명은 250 시간이라고 알려졌다. 
# 한국 연구소에서 수명이 50 시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명 시간 관련 자료를 얻었다. 
# 한국 연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
# 수집된 자료 :  305 280 296 313 287 240 259 266 318 280 325 295 315 278
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import wilcoxon

data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
# 30개가 넘지 않으므로 정규성 검정 실시
print(stats.shapiro(data))
# ShapiroResult(statistic=0.966, pvalue=(0.8208) >> pvalue가 0.05보다 크므로 정규성 따른다.
result = stats.ttest_1samp(data, popmean=250)
print(result)
# TtestResult(statistic=6.0624, pvalue=4.0169e-05, df=13)
# >> pvalue 0.05보다 낮으므로 귀무가설 기각. 

print()
print("[one-sample t 검정 : 문제2]") 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. 
# A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 
# A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.  
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", ""),
#           null인 관찰값은 제거.
from pandas import DataFrame
data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/one_sample.csv")
# print(len(data2))
# print(data2)
time = data2.time.replace("     ", ""),
print(type(time[0]))
print(time[0].head())

time_numeric = pd.to_numeric(time[0], errors='coerce')
print(time)
filtered_time = time_numeric.dropna()
print("사용시간 평균: ", np.mean(filtered_time))        # 5.5568 시간

result = stats.ttest_1samp(filtered_time, popmean=5.2)
print(result)
# p-value 0.0001로 alpha 0.05보다 작으므로 귀무가설 기각?

print()
print("[one-sample t 검정 : 문제3]")
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오. (월별)

# pip install xlrd
data3 = pd.read_excel('2026.02_data.xls')

data4 = data3.iloc[0, 2:]    # 지역 데이터만 추출
data4 = pd.to_numeric(data4, errors='coerce')
data4 = data4.dropna()

print('표본 평균 미용 요금 :', data4.mean())
print('표본 크기 :', len(data4))

# 정규성 검정
result3 = stats.shapiro(data4)
print(result3)

# one-sample t-test
t_result3 = stats.ttest_1samp(data4, popmean=15000)
print(t_result3)
