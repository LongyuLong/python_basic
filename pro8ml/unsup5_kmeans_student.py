# 비계층적 군집분석
# 학생 10명의 시험점수 사용

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.cluster import KMeans

students = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']
scores = np.array([76,95,65,85,60,92,55,88,83,72]).reshape(-1,1)
print("점수: ", scores)

# k=3
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)
km_clusters = kmeans.fit_predict(scores)
print(km_clusters)
# [2 0 1 2 1 0 1 0 2 2]

df = pd.DataFrame({
    'student':students,
    'score':scores.ravel(),
    'cluster':km_clusters
})

print(df)
#   student  score  cluster
# 0      s1     76        2
# 1      s2     95        0
# 2      s3     65        1
# 3      s4     85        2
# 4      s5     60        1
# 5      s6     92        0
# 6      s7     55        1
# 7      s8     88        0
# 8      s9     83        2
# 9     s10     72        2

print("\n군집별 평균 점수")
grouped = df.groupby('cluster')['score'].mean()
print(grouped)
# 군집별 평균 점수
# cluster
# 0    91.666667
# 1    60.000000
# 2    79.000000

## 시각화 ##    시각화 이하 코드 설명 필요
x_position = np.arange(len(students))
y_scores = scores.ravel()
colors = {0:'red', 1:'blue', 2:'green'}
plt.figure(figsize=(10,6))

# 학생별 군집 색으로 구분해 산점도 출력
for i, (x,y,cluster) in enumerate(zip(x_position, y_scores, km_clusters)):
    plt.scatter(x,y,color=colors[cluster])
    plt.text(x,y+1.5, students[i], fontsize=10, ha='center')

# 중심점
centers = kmeans.cluster_centers_
for center in centers:
    plt.scatter(len(students)//2, center[0], marker='X', c='black', s=200)

plt.xticks(x_position, students)
plt.xlabel("학생 명")
plt.ylabel("점수")
plt.grid(True)
plt.show()
# 정리할때 그림넣기








