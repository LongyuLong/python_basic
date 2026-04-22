# 계층적 군집분석: 데이터를 단계적으로 묶어 군집을 형성하는 알고리즘
# 거리가 가까운 데이터부터 계속 묶어가는 방식
# 군집 수를 미리 정하지 않아도됨. 구조는 덴드로그램으로 확인
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

iris = load_iris()
x = iris.data
y = iris.target
labels = iris.target_names

pd.set_option("display.max_columns", None)
df = pd.DataFrame(x, columns=iris.feature_names)
print(df.head(3))
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 0                5.1               3.5                1.4               0.2
# 1                4.9               3.0                1.4               0.2
# 2                4.7               3.2                1.3               0.2

# 스케일링 - 군집분석 시 권장
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# 계층적 군집
z = linkage(x_scaled, method='ward')

# 덴드로그램
plt.figure(figsize=(12,5))
dendrogram(z)
plt.title("IRIS 계층적 군집")
plt.xlabel("Sample")
plt.ylabel("Distance(Euclidean)")
plt.show()
# 정리 시 덴드로그램 이미지 삽입필요


# 덴드로그램 잘라서(?) 최대 3개 군집 만들기
clusters = fcluster(Z=z, t=3, criterion='maxclust')

df['cluster'] = clusters
print(df.head(3))
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \
# 0                5.1               3.5                1.4               0.2
# 1                4.9               3.0                1.4               0.2
# 2                4.7               3.2                1.3               0.2
#    cluster
# 0        1
# 1        1
# 2        1
print(df.tail(3))
#      sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \
# 147                6.5               3.0                5.2               2.0
# 148                6.2               3.4                5.4               2.3
# 149                5.9               3.0                5.1               1.8
#      cluster
# 147        3
# 148        3
# 149        3


# 2개 feature 시각화(산점도)
plt.figure(figsize=(6,5))
sns.scatterplot(x=x_scaled[:,0], y=x_scaled[:,1], hue=clusters, palette='Set1')
# hue=clusters:  군집결과에 따라 색을 다르게 표시
plt.title("IRIS 군집 결과")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
# 정리 시 scatter 이미지 삽입필요


print("실제 라벨: ", y[:10])
print("군집 결과: ", clusters[:10])
# 실제 라벨:  [0 0 0 0 0 0 0 0 0 0]
# 군집 결과:  [1 1 1 1 1 1 1 1 1 1]

print("\n----- 군집 결과 검증 -----")
print("교차 표 - 실제 라벨 vs 군집 결과")
ct = pd.crosstab(y, clusters)
print(ct)
# ----- 군집 결과 검증 -----
# 교차 표 - 실제 라벨 vs 군집 결과
# col_0   1   2   3
# row_0
# 0      49   1   0
# 1       0  27  23
# 2       0   2  48
# row0(실제라벨): 0-setosa, 1-versicolor, 2-virginica
# col_0(군집 결과): 1-cluster 1, 2-cluster 2, 3-cluster 3
# setosa는 완벽히 분리되었고, versicolor와 virginica는 일부 섞인 결과 보임

print("교차표 보조 설명: 각 실제 클래스가 가장 많이 속한 군집")
for i in range(ct.shape[0]):
    max_cluster = ct.iloc[i].idxmax()                 # ?
    print(f"실제 클래스 {i} -> 군집 {max_cluster} (갯수:{ct.iloc[i].max()})") # idxmax랑 무슨차이지
# 각 실제 클래스가 가장 많이 속한 군집
# 실제 클래스 0 -> 군집 1 (갯수:49)
# 실제 클래스 1 -> 군집 2 (갯수:27)
# 실제 클래스 2 -> 군집 3 (갯수:48)

# 정량적 평가: 군집 결과가 실제 정답과 얼마나 유사한지를 수치로 표현
from sklearn.metrics import adjusted_mutual_info_score, normalized_mutual_info_score   # 용도?
# AMI (Adjusted Mutual Info Score): 정보 이론 관점에서 두 군집 간의 상호 정보량을 측정
# 용도: 군집의 크기가 불균형할 때 ARI보다 좀 더 강점이 있으며, 정답과 예측값의 상관관계를 평가
ami = adjusted_mutual_info_score(y, clusters)       # 용도?
print(f"평가 지표: AMI - {ami:.4f}")
# 평가 지표: AMI - 0.6713
# [해석 기준 가이드]
# 1.0: 완벽하게 일치 (실제 정답과 군집 결과가 같음)
# 0.7 ~ 0.9: 매우 높은 수준의 군집화 (성능 우수)
# 0.4 ~ 0.6: 데이터의 특성을 어느 정도 잘 잡아낸 수준 (보통)
# 0.0 이하: 무작위로 그룹을 나눈 것보다 못하거나 무의미함 (모델 수정 필요)


# normalized_mutual_info_score: NMI(Normalized Mutual Information) - 상호 정보량 기반 평가
# 용도: 실제 정답과 예측 군집 사이의 정보 공유량을 0~1 사이로 정규화하여 측정
nmi = normalized_mutual_info_score(y, clusters)
print(f"평가 지표: NMI - {nmi:.4f}")
# 평가 지표: NMI - 0.6755
# [해석 기준]
# 1.0: 완벽한 일치 (예측이 정답과 완전히 동일함)
# 0.7 이상: 매우 우수한 군집화 결과
# 0.4 ~ 0.7: 준수한 성능, 데이터의 주요 특징을 잘 반영함
# 0.0: 두 그룹 간에 아무런 상관관계가 없음 (무작위 수준)

from sklearn.metrics import adjusted_rand_score

# adjusted_rand_score: ARI(Adjusted Rand Index) - 무작위 할당을 보정한 랜드 지수
# 용도: 두 데이터 쌍이 동일한 군집에 속하는지 여부를 바탕으로 정답과 예측의 유사도 측정
ari = adjusted_rand_score(y, clusters)
print(f"평가 지표: ARI - {ari:.4f}")
# 평가 지표: ARI - 0.6128 (예시 수치)

# ---------------------------------------------------------
# [종합 정리: 군집 평가 지표(Clustering Metrics) 비교]
# ---------------------------------------------------------
"""
1. ARI (Adjusted Rand Index) - "쌍(Pair) 중심"
    - 특징: '우연히' 군집이 맞을 확률을 수식에서 배제함. 0은 무작위 수준, 1은 완벽 일치.
    - 장점: 해석이 직관적이며 가장 엄격한 기준을 적용함.
    - 활용: 데이터 분포의 형태에 상관없이 전반적인 군집 성능을 평가할 때 가장 먼저 확인.

2. AMI (Adjusted Mutual Info) - "정보(Information) 중심"
    - 특징: 두 군집 간의 상호 정보량(Mutual Information)을 측정하고 우연성을 보정함.
    - 장점: 군집의 크기가 불균형할 때 ARI보다 더 안정적인 지표로 알려짐.
    - 활용: 군집 간 크기 차이가 많이 나거나 불균형한 데이터셋 평가에 적합.

3. NMI (Normalized Mutual Information) - "정규화 정보"
    - 특징: 상호 정보량을 0과 1 사이로 정규화함. (우연 보정 기능은 AMI보다 약함)
    - 장점: 계산이 비교적 단순하고 값이 항상 0~1 사이에 있어 비교가 용이함.
    - 활용: 결과가 항상 양수여야 하거나, 비교 대상 군집의 개수가 매우 많을 때 자주 사용.

* 결론: 보통 ARI를 기본 지표로 사용하되, AMI나 NMI를 보조적으로 함께 기재하여 결과의 신뢰도를 높임.
"""





