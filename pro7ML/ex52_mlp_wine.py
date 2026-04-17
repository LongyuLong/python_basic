# MLP- wine dataset으로 다항분리

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # 표준화
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

data = load_wine()
x=data.data
y=data.target
print(x[:2], ' ', x.shape)          # (178, 13)
print(y[:2], ' ', np.unique(y))     # [0 1 2]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, stratify=y)

# 스케일링 (MLP - 스케일링 권장)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

# 모델 생성
model = MLPClassifier(
    hidden_layer_sizes=(20,10), # 은닉층 2개
    activation='relu',          # 활성화 함수
    solver='adam',              # 손실 최소화 함수 지정
    learning_rate_init=0.001,   # 학습률
    max_iter=500,                # 에폭 수
    random_state=42,            # 
    verbose=1                   # 학습 도중 로그 출력 여부
)
model.fit(x_train_scaled, y_train)
pred = model.predict(x_test_scaled)
print("accuracy score: ", accuracy_score(y_test, pred))
# accuracy score:  0.6666666666666666
print("classification_report: \n", classification_report(y_test, pred))
# classification_report:
#                precision    recall  f1-score   support

#            0       0.64      1.00      0.78        18
#            1       1.00      0.14      0.25        21
#            2       0.65      1.00      0.79        15

#     accuracy                           0.67        54
#    macro avg       0.77      0.71      0.61        54
# weighted avg       0.78      0.67      0.58        54

# 혼동행렬 시각화
cm = confusion_matrix(y_test, pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("confusion matrix")
plt.xlabel("predicted")
plt.ylabel("actual")
plt.show()

# train loss curve 시각화
plt.plot(model.loss_curve_)
plt.title("train loss curve")
plt.xlabel("iteration(epoch)")
plt.ylabel("loss")
plt.show()

# 참고: 미분이 MLP에서 어떻게 쓰이는가? 미분으로 오차를 줄여나감
# MLP구조: 입력 -> 신경망 -> 출력 후 오차 확인
# 예)   입력(x) -> 모델 -> 예측(y_hat) - 실제값(y) = 오차(Loss)
#       오차함수(Loss Function)는 Loss = (y - y_hat) 예측이 틀릴 수록 값이 커짐
#       미분은 이 오차를 어떻게 줄일 지, 오차가 줄어드는 방향으로 w(weight)를 갱신한다
# 학습과정:
# 1. 모델이 예측 -> 2. 오차 계산 -> 3. 미분(기울기 계산) -> 4. 가중치 w 갱신
# 5. (1~4) 과정 반복 - 역전파(back propergation)
# >> MLP



