# KMeans : iris dataset 사용

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import (
    adjusted_rand_score,           # ARI: 무작위성을 보정한 정답(Label)과의 유사도 (-1 ~ 1)
    normalized_mutual_info_score,  # NMI: 정보 이론 기반의 정답 유사도 (0 ~ 1)
    silhouette_score               # 실루엣 계수: '정답 없이' 군집 자체의 밀집도와 분리도를 평가
)
from sklearn.decomposition import PCA # 4개의 특성(4차원)을 정보를 최대한 보존하며 2차원으로 압축 (시각화 목적)
# ---------------------------------------------------------
# [평가 지표 핵심 요약 주석]
# 1. ARI (Adjusted Rand Index): 
#    - 실제 정답이 있을 때 사용. 가장 엄격한 일치도 평가.
# 2. NMI (Normalized Mutual Info): 
#    - 실제 정답이 있을 때 사용. 군집 간의 상호 정보량 측정.
# 3. Silhouette Score:
#    - ★중요: 정답이 없을 때 사용 가능. 
#    - 1에 가까울수록 "내 그룹과는 가깝고 다른 그룹과는 멀다"는 의미 (품질 우수).
#    - 0.5 이상이면 군집화가 타당하다고 판단.
# ---------------------------------------------------------

iris = load_iris()
x = iris.data
y = iris.target
feature_names = iris.feature_names

df = pd.DataFrame(x, columns=feature_names)
print("iris data shape", x.shape)
# iris data shape (150, 4)

# 스케일링
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

print(x_scaled[:2])
# [[-0.90068117  1.01900435 -1.34022653 -1.3154443 ]
#  [-1.14301691 -0.13197948 -1.34022653 -1.3154443 ]]


# PCA - 주성분 분석
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scaled)
print("pca 설명 분산 비율: ", pca.explained_variance_ratio_)
# pca 설명 분산 비율:  [0.72962445 0.22850762] 비율의 의미는? 
# [해석 주석]
# - PC1(73%) + PC2(23%) = 약 96%의 정보 유지
# - 4차원에서 2차원으로 압축했으나 데이터 본연의 특징(분산)을 거의 대부분 보존함
# - 따라서 이 2차원 시각화는 원본 데이터를 충분히 대표한다고 판단할 수 있음

# KMeans 모델
k=3
kmeans = KMeans(
    n_clusters=k, 
    init='k-means++', 
    n_init=10,          # 초기 중심점 위치를 바꿔가며 10번 재시도하여 최적의 오차(Inertia) 선택
    random_state=42
)

clusters = kmeans.fit_predict(x_scaled)
df['cluster'] = clusters
print("클러스터 중심 값: ", kmeans.cluster_centers_)
# 클러스터 중심 값:  
# [[-0.05021989 -0.88337647  0.34773781  0.2815273 ]
#  [-1.01457897  0.85326268 -1.30498732 -1.25489349]
#  [ 1.13597027  0.08842168  0.99615451  1.01752612]]
## 시각화(PCA 기반, 4개의 열을 2차원 차트에 표현할 수 없으므로 차원 축소)

plt.figure(figsize=(6,5))
sns.scatterplot(x=x_pca[:,0], y=x_pca[:,1], hue=clusters, palette='Set1')
plt.title("KMeans Clustering")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

# 실제 라벨과 군집 비교(교차표)
ct = pd.crosstab(y,clusters)
print(ct)
# col_0   0   1   2     << 열: 군집번호(KMeans 결과)
# row_0
# 0       0  50   0     << setosa
# 1      39   0  11     << versicolor(?)
# 2      14   0  36     << verginica (?)
# 행: 실제라벨(iris)
# [교차표 최종 해석]
# Cluster 1 => 실제 Setosa (100% 일치)
# Cluster 0 => 실제 Versicolor (대부분 일치)
# Cluster 2 => 실제 Virginica (대부분 일치)
# ※ 주의: 군집 번호(0,1,2)는 실행 시마다 랜덤하게 부여되므로, 
# 숫자의 위치(좌표)보다 '한 행의 데이터가 특정 열에 얼마나 집중되었는지'가 중요함.

print("클래스 별 대표 군집")
for i in range(ct.shape[0]):
    max_cluster = ct.iloc[i].idxmax()
    print(f"실제 클래스 {i} -> 군집 {max_cluster}")
# 클래스 별 대표 군집
# 실제 클래스 0 -> 군집 1
# 실제 클래스 1 -> 군집 0
# 실제 클래스 2 -> 군집 2

print("--- 정량 평가 ---")
# ARI/NMI: '실제 정답(y)'과 얼마나 비슷한지 비교 (정답이 있을 때만 가능)
ari = adjusted_rand_score(y, clusters)
nmi = normalized_mutual_info_score(y, clusters)

# 실루엣: 정답 없이 '데이터의 거리(x_scaled)'만으로 군집 품질 평가
# 1에 가까울수록 군집화가 잘 된 것 (0.5 이상이면 우수)
silhouette = silhouette_score(x_scaled, clusters)

print(f"ARI: {ari:.4f}, NMI: {nmi:.4f}, silhouette: {silhouette:.4f}")
# --- 정량 평가 ---
# ARI: 0.6201, NMI: 0.6595, silhouette: 0.4599

# ---------------------------------------------------------
# [K 값 결정의 타당성 검증: 엘보우 기법(Elbow Method)]
# 목적: 군집 내 오차 제곱합(Inertia)을 확인하여 최적의 군집 개수(K)를 선정
inertia = []
k_range = range(1,10)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(x_scaled)
    # inertia_: 중심점에서 군집 내 데이터들 간의 거리 합 (작을수록 응집도가 높음)
    inertia.append(km.inertia_)

# [엘보우 그래프 시각화]
plt.figure(figsize=(6, 4))
plt.plot(k_range, inertia, marker='o', linestyle='--', color='b')
plt.title("최적의 K 찾기 (Elbow Method)")
plt.xlabel("군집 개수 (Number of Clusters)")
plt.ylabel("Inertia (SSE)")
plt.xticks(k_range)
plt.grid(True, alpha=0.3)
plt.show()

# [실제 vs 군집 결과 시각화 비교]
# 목적: PCA로 축소된 2차원 공간에서 실제 정답과 모델의 예측이 얼마나 일치하는지 육안으로 확인
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.scatterplot(x=x_pca[:,0], y=x_pca[:,1], hue=y, palette='Set1')
plt.title("실제 라벨 (Ground Truth)")

plt.subplot(1,2,2)
sns.scatterplot(x=x_pca[:,0], y=x_pca[:,1], hue=clusters, palette='Set1')
plt.title("KMeans 군집 결과 (Prediction)")
plt.show()

# ---------------------------------------------------------
# [군집 간 특성 차이 분석: ANOVA 검정]
# 목적: 형성된 군집들이 통계적으로 서로 '다른' 특성을 가진 집단인지 검증
# 귀무가설(H0): 모든 군집의 평균은 같다. (군집화가 의미 없음)
# 대립가설(H1): 적어도 한 군집의 평균은 다르다. (군집화가 유의미함)

# 클러스터별 평균 분석
pd.set_option('display.max_columns', None)
cluster_mean = df.groupby('cluster').mean()
print("클러스터 별 평균: \n", cluster_mean)
# 클러스터 별 평균:
# sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# cluster
# 0                 5.801887          2.673585           4.369811          1.413208
# 1                 5.006000          3.428000           1.462000          0.246000
# 2                 6.780851          3.095745           5.510638          1.972340

# 군집 3개: 군집 간 평균 차이 검정(ANOVA)
# 귀무: 군집 간 평균에 차이가 없다
from scipy.stats import f_oneway

for col in feature_names:   # 각 군집별 데이터 분리
    group0 = df[df['cluster']==0][col]
    group1 = df[df['cluster']==1][col]
    group2 = df[df['cluster']==2][col]
    # ANOVA 수행
    f_stat, p_val = f_oneway(group0, group1, group2)
    print(f"{col}: f-statistic: {f_stat:.4f}, p-value: {p_val:.4f}")
    # 해석
    if p_val >= 0.05:
        print("군집 간 평균에 차이가 없다(유의하지 않다)")
    else:
        print("군집 간 평균에 차이가 있다")
# sepal length (cm): f-statistic: 218.5710, p-value: 0.0000
# 군집 간 평균에 차이가 있다
# sepal width (cm): f-statistic: 79.9000, p-value: 0.0000
# 군집 간 평균에 차이가 있다
# petal length (cm): f-statistic: 860.6367, p-value: 0.0000
# 군집 간 평균에 차이가 있다
# petal width (cm): f-statistic: 525.6988, p-value: 0.0000
# 군집 간 평균에 차이가 있다
# >> KMeans가 꽃받침, 꽃잎 길이/너비를 제대로 군집분석했음을 알 수 있다.

# 사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# petal_length로 작업
feature = 'petal length (cm)'
tukey = pairwise_tukeyhsd(
    endog=df[feature], groups=df['cluster'], alpha=0.05
)
print("tukeyhsd 결과(petal_length에 대한): ", tukey)
# tukeyhsd 결과(petal_length에 대한):  
# Multiple Comparison of Means - Tukey HSD, FWER=0.05
# ===================================================
# group1 group2 meandiff p-adj  lower   upper  reject
# ---------------------------------------------------
#      0      1  -2.9078   0.0 -3.1405 -2.6751   True
#      0      2   1.1408   0.0  0.9043  1.3773   True
#      1      2   4.0486   0.0  3.8088  4.2884   True
# ---------------------------------------------------



# 사후 검정 시각화
tukey.plot_simultaneous(figsize=(6,4))
plt.title(f"tukeyhsd - {feature}")
plt.show()
# 정리할때 그림 넣기

# 군집별 boxplot
for col in feature_names:
    plt.figure(figsize=(5,3))
    sns.boxplot(x='cluster', y=col, data=df)
    plt.title(f'{col} by cluster')
    plt.show()

print() # 클러스터 평균분석 마지막열에 type 추가
cluster_mean['label'] = ["Type A", "Type B", "Type C"]
print(cluster_mean)
#          sepal length (cm)  sepal width (cm)  petal length (cm)  \
# cluster
# 0                 5.801887          2.673585           4.369811
# 1                 5.006000          3.428000           1.462000
# 2                 6.780851          3.095745           5.510638

#          petal width (cm)   label
# cluster
# 0                1.413208  Type A
# 1                0.246000  Type B
# 2                1.972340  Type C