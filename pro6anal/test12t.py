# Paired Samples t-test(대응표본 t검정, 동일 집단 표본 t검정)

# 하나의 집단에 대해 독립변수를 적용하기 전과 후의 종속변수(평균)의 수준을 측정하고
# 이들의 차이가 통계적으로 유의미한지 분석하는 방법
# 동일한 관찰 대상으로 처리 이전과 이후를 1:1 대응시킨 검정 방법
# 집단 간 비교가 아니므로 등분산 가정을 할 필요는 없다
# ex. 광고 전후의 상품 선호도 측정, 투자 대비 상품 판매량 등등

# 실습1: 3강의실 학생들을 대상으로, 특강이 시험 점수에 영향을 주었는가?
# 귀무: 특강 효과 없음 # 대립: 특강 효과 있음

import numpy as np
import scipy.stats as stats

np.random.seed(123)
x1 = np.random.normal(75, 10, 100)
x2 = np.random.normal(80, 10, 100)

# 표본 수 30 넘지만, 정규성 확인(연습)
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(x1, kde=True)
sns.displot(x2, kde=True)

print(stats.shapiro(x1).pvalue) # 0.2749
print(stats.shapiro(x2).pvalue) # 0.1021

# 대응표본 t검정
print(stats.ttest_rel(x1,x2))
# statistic=-3.0031, pvalue=0.00338, df=99
# pvalue 0.0033 < alpha 0.05 이므로 귀무가설 기각 >> 특강은 효과가 있다

plt.show()


