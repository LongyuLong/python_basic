# 공분산 / 상관계수

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/drinking_water.csv")

print(data.head())
print(data.describe())
#                친밀도         적절성         만족도
# count     264.000000     264.000000     264.000000
# mean      2.928030       3.132576       3.094697
# std       0.970345       0.859657       0.828744
# min       1.000000       1.000000       1.000000
# 25%       2.000000       3.000000       3.000000
# 50%       3.000000       3.000000       3.000000
# 75%       4.000000       4.000000       4.000000
# max       5.000000       5.000000       5.000000

print("---- 표준편차 ----")
print(np.std(data.친밀도))  # 0.968505126935272
print(np.std(data.적절성))  # 0.8580277077642035
print(np.std(data.만족도))  # 0.8271724742228969

plt.hist([np.std(data.친밀도), np.std(data.적절성), np.std(data.만족도)])
# plt.show()

print("---- 공분산 by numpy ----")
print(np.cov(data.친밀도, data.적절성))  
print(np.cov(data.친밀도, data.만족도))
# [[0.94156873 0.41642182]
#  [0.41642182 0.73901083]]
# [[0.94156873 0.37566252]
#  [0.37566252 0.68681588]]
print()
print("---- 공분산 by pandas ----")
print(data.cov())
#           친밀도       적절성       만족도
# 친밀도  0.941569  0.416422  0.375663
# 적절성  0.416422  0.739011  0.546333
# 만족도  0.375663  0.546333  0.686816


print("---- 상관계수 by numpy ----")
print(np.corrcoef(data.친밀도, data.적절성))
print(np.corrcoef(data.친밀도, data.만족도))
# [[1.         0.49920861]
#  [0.49920861 1.        ]]
# [[1.         0.46714498]
#  [0.46714498 1.        ]]
print()
print("---- pearson 상관계수 ----\n",data.corr(method='pearson'))
#           친밀도       적절성       만족도
# 친밀도  1.000000  0.499209  0.467145
# 적절성  0.499209  1.000000  0.766853
# 만족도  0.467145  0.766853  1.000000
print()
print("---- kendall 상관계수 ----\n",data.corr(method='kendall'))
#        친밀도     적절성     만족도
# 친밀도  1.000000  0.466729  0.459353
# 적절성  0.466729  1.000000  0.703214
# 만족도  0.459353  0.703214  1.000000
print()
print("---- spearman 상관계수 ----\n",data.corr(method='spearman'))
#         친밀도    적절성     만족도
# 친밀도  1.000000  0.511078  0.501201
# 적절성  0.511078  1.000000  0.748510
# 만족도  0.501201  0.748510  1.000000
print()

print("----만족도에 따른 다른 특성 사이의 상관 관계----")
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))
# 만족도    1.000000
# 적절성    0.766853
# 친밀도    0.467145
# Name: 만족도, dtype: float64

# 시각화
data.plot(kind='scatter', x="만족도", y="적절성")
# plt.show()

from pandas.plotting import scatter_matrix
attr = ['친밀도','적절성','만족도']
scatter_matrix(data[attr], figsize=(10,6))
# plt.show()

import seaborn as sns
sns.heatmap(data.corr(), annot=True)
# plt.show()


# heatmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()

