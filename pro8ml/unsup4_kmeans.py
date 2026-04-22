# [K-Means 알고리즘 개념]
# 1. 정의: 데이터를 K개의 군집(Cluster)으로 묶는 알고리즘으로, 각 군집의 '중심점(Centroid)'을 구함
# 2. 특징: 
#    - 비지도 학습(Label이 없는 데이터의 패턴을 찾음)
#    - 거리 기반 알고리즘 (일반적으로 유클리드 거리를 사용)
#    - 군집의 수(K)를 사용자가 직접 사전에 지정해야 함

# [알고리즘 작동 단계]
# Step 1. 초기화: 데이터 중 임의의 K개를 선택하여 각 군집의 초기 중심점으로 설정
# Step 2. 할당(Assignment): 모든 데이터를 가장 가까운 중심점에 배정하여 군집을 형성
# Step 3. 업데이트(Update): 각 군집에 속한 데이터들의 산술 평균을 계산하여 새로운 중심점 설정
# Step 4. 반복(Repeat): 중심점의 위치가 변하지 않을 때까지 Step 2, 3을 반복 수행

# 실습 1 - make_blobs 사용
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import koreanize_matplotlib

x, _ =make_blobs(n_samples=150, n_features=2, centers=3,
                cluster_std=0.5, shuffle=True, random_state=0)  # y값은 필요없음 -- 비지도이기때문에?

print(x[:3], ' ', x.shape)
# [[2.60509732 1.22529553]
#  [0.5323772  3.31338909]
#  [0.802314   4.38196181]]   (150, 2)

# 산점도
plt.scatter(x[:,0], x[:,1], c='gray', marker='o', s=50)
plt.grid(True)
plt.show()
# 정리할 때 그림넣기


# [K-Means 모델 생성 및 파라미터 설정]

# 1. 초기 중심점 설정 방법 선택
# - 'random': 무작위 선택. 중심점이 서로 가까워지면 성능이 저하될 위험 있음
# - 'k-means++': 첫 중심점 선택 후, 다음 중심점은 기존 점들과 '최대한 멀리' 떨어진 곳에서 선택 (수렴 속도 향상)
init_centroid = 'k-means++' 

km_model = KMeans(
    n_clusters=3,        # K: 형성할 군집의 개수 (IRIS 데이터의 경우 품종이 3개이므로 3 설정)
    init=init_centroid,  # 초기 중심점 설정 방식 ('k-means++' 또는 'random')
    n_init=10,           # 초기 중심점 위치를 다르게 하여 총 10번 실행 후, 가장 최적의 결과(오차 최소)를 선택
    random_state=0       # 실행 시마다 결과가 변하지 않도록 난수 발생 시드 고정
)

# [K-Means 알고리즘 내부 동작 원리 주석]
"""
작동 순서 (Iteration):
1. 할당(Assignment): 각 데이터 포인트를 가장 가까운 중심점(Centroid)에 배정
2. 이동(Update): 각 군집에 속한 데이터들의 평균 위치로 중심점을 새로 이동
3. 반복: 중심점의 위치가 변하지 않거나, 최대 반복 횟수에 도달할 때까지 1~2번 과정을 반복
"""

pred = km_model.fit_predict(x)  # 클러스터링으로 구분한 결과 예측?
print("pred: \n", pred)
# pred: 
# [1 2 2 2 1 2 2 1 0 2 1 0 0 2 2 0 0 1 0 1 2 1 2 2 0 1 1 2 0 1 0 0 0 0 2 1 1
#  1 2 2 0 0 2 1 1 1 0 2 0 2 1 2 2 1 1 0 2 1 0 2 0 0 0 0 2 0 2 1 2 2 2 1 1 2
#  1 2 2 0 0 2 1 1 2 2 1 1 1 0 0 1 1 2 1 2 1 2 0 0 1 1 1 1 0 1 1 2 0 2 2 2 0
#  2 1 0 2 0 2 2 0 0 2 1 2 2 1 1 0 1 0 0 0 0 1 0 0 0 2 0 1 0 2 2 1 1 0 0 0 0
#  1 1]

# 각 그룹별 보기. 0~2 그룹
# print(x[pred==0])
# print()
# print(x[pred==1])
# print()
# print(x[pred==2])

print("중심점: \n", km_model.cluster_centers_)
# 중심점:  
# [[-1.5947298   2.92236966]
#  [ 2.06521743  0.96137409]
#  [ 0.9329651   4.35420712]]

## 시각화 ##
plt.scatter(x[pred==0, 0], x[pred==0, 1], c='red', marker='o', s=50, label='cluster 1')    # x[pred==0, 0] 표현 설명 필요 클러스터 1~3 나누는 거 이해 잘 안됨
plt.scatter(x[pred==1, 0], x[pred==1, 1], c='green', marker='s', s=50, label='cluster 2')  
plt.scatter(x[pred==2, 0], x[pred==2, 1], c='blue', marker='v', s=50, label='cluster 3')   
plt.scatter(km_model.cluster_centers_[:,0],km_model.cluster_centers_[:,1], 
            color='black', marker='+', s=60, label="center") # 각 군집 중심점 표시
plt.legend()
plt.grid(True)
plt.show()
# 정리할 때 plot 넣기

# KMeans의 K값은? elbow or silhouette 기법을 이용해 k값 얻기
# 1) elbow
def elbow(x):
    sse = []
    for i in range(1,11):
        km = KMeans(n_clusters=i, init=init_centroid, random_state=0)
        km.fit(x)
        sse.append(km.inertia_)
    plt.plot(range(1,11), sse, marker='o')
    plt.xlabel("군집수")
    plt.ylabel("SSE")
    plt.show()
    # 정리할 때 그림넣기

elbow(x)

# 2) 실루엣(silhouette) 기법
'''
실루엣(silhouette) 기법
    클러스터링의 품질을 정량적으로 계산해 주는 방법이다.
    클러스터의 개수가 최적화되어 있으면 실루엣 계수의 값은 1에 가까운 값이 된다.
    실루엣 기법은 k-means 클러스터링 기법 이외에 다른 클러스터링에도 적용이 가능하다
'''
import numpy as np
from sklearn.metrics import silhouette_samples
from matplotlib import cm

# 데이터 X와 X를 임의의 클러스터 개수로 계산한 k-means 결과인 y_km을 인자로 받아 각 클러스터에 속하는 데이터의 실루엣 계수값을 수평 막대 그래프로 그려주는 함수를 작성함.
# y_km의 고유값을 멤버로 하는 numpy 배열을 cluster_labels에 저장. y_km의 고유값 개수는 클러스터의 개수와 동일함.

def plotSilhouette(x, pred):
    cluster_labels = np.unique(pred)
    n_clusters = cluster_labels.shape[0]   # 클러스터 개수를 n_clusters에 저장
    sil_val = silhouette_samples(x, pred, metric='euclidean')  # 실루엣 계수를 계산
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []

    for i, c in enumerate(cluster_labels):
        # 각 클러스터에 속하는 데이터들에 대한 실루엣 값을 수평 막대 그래프로 그려주기
        c_sil_value = sil_val[pred == c]
        c_sil_value.sort()
        y_ax_upper += len(c_sil_value)

        plt.barh(range(y_ax_lower, y_ax_upper), c_sil_value, height=1.0, edgecolor='none')
        yticks.append((y_ax_lower + y_ax_upper) / 2)
        y_ax_lower += len(c_sil_value)

    sil_avg = np.mean(sil_val)         # 평균 저장

    plt.axvline(sil_avg, color='red', linestyle='--')  # 계산된 실루엣 계수의 평균값을 빨간 점선으로 표시
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('클러스터')
    plt.xlabel('실루엣 개수')
    plt.show() 

'''
그래프를 보면 클러스터 1~3 에 속하는 데이터들의 실루엣 계수가 0으로 된 값이 아무것도 없으며, 실루엣 계수의 평균이 0.7 보다 크므로 잘 분류된 결과라 볼 수 있다.
'''
X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)
km = KMeans(n_clusters=3, random_state=0) 
y_km = km.fit_predict(X)

plotSilhouette(X, y_km)
# 정리할 때 그림 넣기


