# 실습
# 복부 수술 전 9명의 몸무게와 수술 후 몸무게 변화

baseline = [67.2, 71.5, 67.4, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

# 귀무: 복부 수술 전 몸무게와 복부 수술 후 몸무게의 변화는 없다

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

print(np.mean(baseline))
print(np.mean(follow_up))
print('평균의 차이: ', np.mean(baseline) - np.mean(follow_up))  # 6.91

plt.bar(np.arange(2),[np.mean(baseline), np.mean(follow_up)])
plt.title("수술 전/후 몸무게", fontdict={'fontsize':'12', 'fontweight':'bold'})
plt.ylabel("kg")
plt.xlim(0, 1)

result = stats.ttest_rel(baseline, follow_up)
print(result)   # statistic=3.3681, pvalue=0.0098, df=8
# pvalue=0.0098 < alpha=0.05 이므로 귀무가설 기각.. >> 수술 후 몸무게 변화 유의미하다


plt.show()








