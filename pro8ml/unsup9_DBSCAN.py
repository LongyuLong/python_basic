# [DBSCAN 알고리즘 개념]
# 1. 정의: '밀도 기반' 군집 분석 (Density-Based Spatial Clustering of Applications with Noise)
# 2. 핵심 아이디어: "점들이 밀집해 있는 곳은 하나의 군집으로 보고, 
#                  밀도가 희박한 곳은 '노이즈(이상치)'로 간주한다."
# 3. 주요 장점:
#    - 군집의 개수(K)를 미리 정할 필요가 없음.
#    - 원형이 아닌 불규칙한 모양(초승달 등)의 데이터도 잘 분리함.
# 4. 주요 파라미터:
#    - eps (epsilon): 이웃으로 간주할 최대 거리.
#    - min_samples: 하나의 군집을 형성하기 위한 최소 점의 개수.

import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

# 샘플 데이터 생성
x, y = make_moons(n_samples=200, noise=0.05, shuffle=True, random_state=0)
print(x[:5], x.shape)
# print(y)

# plt.scatter(x[:, 0], x[:, 1], c=y)
# plt.show()

print("KMeans로 군집 분류")
km = KMeans(n_clusters=2, init="k-means++", random_state=0)
pred1 = km.fit_predict(x)
print("km 예측 군집 id: ", pred1[:10])

# km 결과 시각화
def plotResult(x,pr):
    plt.scatter(x[pr==0, 0], x[pr==0, 1], c='blue', marker='o', s=40, label='cluster1')
    plt.scatter(x[pr==1, 0], x[pr==1, 1], c='red', marker='s', s=40, label='cluster2')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:,1], c='black', marker='+', s=40, label='centroid')
    plt.title('Clustering Result')
    plt.legend()
    plt.show()

# [KMeans 결과 해석]
# - KMeans는 무조건 데이터의 '중심'을 잡고 원형(구형)으로 군집을 형성함
# - 초승달 모양처럼 휜 데이터도 억지로 수직/수평으로 이등분하려는 경향이 있음 (거리 기반의 한계)
plotResult(x,pred1)
# 군집분류 결과 그림 정리할 때 추가하기

print("---- DBSCAN으로 군집 분류 ----")
db = DBSCAN(eps=0.2, min_samples=5, metric='euclidean')
# eps: 샘플 간 최대 거리, min_samples: 점에 대한 이웃 샘플 수
pred2 = db.fit_predict(x)
print("DBSCAN 군집 id: ", pred2[:10])
# DBSCAN 군집 id:  [0 1 1 0 1 1 0 1 0 1]

# [DBSCAN의 핵심 포인트]
# 1. Core Point(핵심점): 설정한 eps 내에 min_samples 이상의 이웃을 가진 점
# 2. Border Point(경계점): 핵심점의 이웃이지만 스스로는 핵심점이 아닌 점
# 3. Noise(노이즈): 어디에도 속하지 않는 점 (결과값에 -1로 표시됨)
print("군집 종류: ", set(pred2))
# 군집 종류:  {np.int64(0), np.int64(1)} << 이상치는 없음. 0과 1만 있으니까

# [DBSCAN 결과 시각화]
# - 데이터가 아무리 휘어있어도 점들이 밀접하게 '연결'되어 있다면 하나의 군집으로 인식함
# - 즉, '모양'에 구애받지 않고 실제 데이터가 모여 있는 '분포'를 정확히 찾아냄
plotResult(x,pred2)
# KMeans는 k개에 군집의 갯수를 맞추고, DBSCAN은 밀도에 의해 형태를 맞춘다.

# 군집분류 결과 그림 정리할 때 추가하기




