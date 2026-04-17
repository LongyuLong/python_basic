# MLP(Multi-Layer Perceptron)란 지도학습에 사용되는 인공 신경망의 한 형태이다. 
# MLP는 일반적으로 최소 하나 이상의 비선형 은닉 계층을 포함하며, 
# 이러한 계층은 학습 데이터에서 복잡한 패턴을 추출하는 데 도움이 된다. 
# MLP는 주로 분류 및 회귀 문제에 적용되며, 그 학습 알고리즘으로 역전파가 주로 사용된다


# 실습1) 논리회로 분류
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
label = np.array([0, 0, 0, 1])  

# max_iter의 추천 횟수: 500~1000정도
ml = MLPClassifier(max_iter=500, hidden_layer_sizes=10, solver='adam',
                    learning_rate_init=0.01, verbose=1).fit(feature, label)  # max_iter(epoch, 학습횟수)
# print(ml)

pred = ml.predict(feature)
print("pred: ", pred)
print("accuracy: ", accuracy_score(label, pred))    # label=실제값, pred=예측값

print("-----------------------------------------")
# 실습2) 일반 자료로 분류

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

x, y = make_moons(n_samples=300, noise=0.2, random_state=42)

print(x[:2])
# [[ 0.80392642 -0.29140734]
#  [ 2.31443265 -0.12223813]]
print(y[:2])
# [1 1]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = MLPClassifier(hidden_layer_sizes=(10,10), solver='adam',
                    max_iter=1000, random_state=42, activation='relu')   # 히든레이어 10개씩 10개?
model.fit(x_train,y_train)
pred = model.predict(x_test)
print("accuracy: ",accuracy_score(y_test,pred))
# accuracy:  0.9666666666666667


