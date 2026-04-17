"""
[Machine Learning] Support Vector Machine (SVM) 요약

1. 정의: 
    - 데이터를 분류하는 최적의 '결정 경계(Decision Boundary)'를 찾는 알고리즘.
    - 분류(SVC)와 회귀(SVR) 모두에 사용 가능.

2. 핵심 개념:
    - 서포트 벡터(Support Vector): 결정 경계와 가장 가까이 있는 데이터 포인트들.
    - 마진(Margin): 결정 경계와 서포트 벡터 사이의 거리. SVM의 목표는 이 마진을 '최대화'하는 것.
    - 초평면(Hyperplane): 데이터를 나누는 기준 (2차원에선 선, 3차원 이상에선 면).

3. 주요 파라미터 (Scikit-learn 기준):
    - C (규제): 
     * 클수록: 오차를 허용하지 않음 (오버피팅 위험)
     * 작을수록: 마진을 넓히고 오차를 허용 (일반화 성능 향상)
    - Kernel (커널): 
     * 'linear': 선형 분리
     * 'rbf' (기본값): 비선형 분리 (가우시안 커널)
     * 'poly': 다항식 커널
    - Gamma: 'rbf' 커널에서 하나의 데이터가 미치는 영향력의 범위 (클수록 복잡한 경계).

4. 장단점:
    - 장점: 고차원 데이터에서 효과적이며, 마진을 최대화하므로 일반화 능력이 좋음.
    - 단점: 데이터셋이 너무 크면 학습 시간이 오래 걸리고, Noise에 민감함.
"""

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='malgun gothic')
X, y = make_blobs(n_samples=50, centers=2, cluster_std=0.5, random_state=4)
y = 2 * y - 1

plt.scatter(X[y == -1, 0], X[y == -1, 1], marker='o', label="-1 클래스")
plt.scatter(X[y == +1, 0], X[y == +1, 1], marker='x', label="+1 클래스")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("학습용 데이터")
plt.show()

from sklearn.svm import SVC
model = SVC(kernel='linear', C=1.0).fit(X, y)  # tuning parameter  값을 변경해보자.
xmin = X[:, 0].min()
xmax = X[:, 0].max()
ymin = X[:, 1].min()
ymax = X[:, 1].max()
xx = np.linspace(xmin, xmax, 10)
yy = np.linspace(ymin, ymax, 10)
X1, X2 = np.meshgrid(xx, yy)
z = np.empty(X1.shape)

for (i, j), val in np.ndenumerate(X1):    # 배열 좌표와 값 쌍을 생성하는 반복기를 반환
    x1 = val
    x2 = X2[i, j]
    p = model.decision_function([[x1, x2]])
    z[i, j] = p[0]

plt.scatter(X[y == -1, 0], X[y == -1, 1], marker='o', label="-1 클래스")
plt.scatter(X[y == +1, 0], X[y == +1, 1], marker='x', label="+1 클래스")
plt.contour(X1, X2, z, levels=[-1, 0, 1], colors='k', linestyles=['dashed', 'solid', 'dashed'])
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=300, alpha=0.3)

x_new = [10, 2]
plt.scatter(x_new[0], x_new[1], marker='^', s=100)
plt.text(x_new[0] + 0.03, x_new[1] + 0.08, "테스트 데이터")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("SVM 예측 결과")
plt.show()

# Support Vectors 값 출력
print(model.support_vectors_)
# [[9.03715314 1.71813465]
#  [9.17124955 3.52485535]]







