# 단순선형회귀 모델 작성
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras.optimizers import SGD, RMSprop, Adam
import numpy as np

# feature, label을 2차원 형태로 입력하기 위함
xdata = np.array([1,2,3,4,5], dtype='float32').reshape(-1,1)
ydata = np.array([1,2.0,3.0,3.5,5.5]).reshape(-1,1)
print("상관계수: ", np.corrcoef(xdata.ravel(), ydata.ravel()))

model = Sequential()
model.add(Input((1,)))
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=1, activation='linear'))
print(model.summary())

model.compile(loss='mse', optimizer='SGD', metrics=["mse"])
# loss='mse': 회귀분석 모델에서는 Mean Squared Error 사용

model.fit(x=xdata, y=ydata, epochs=10, batch_size=1, verbose=1, shuffle=True)
# batch_size는 정수
# verbose=1:
# - 학습 과정을 출력한다.
# - 0: 출력 없음
# - 1: 진행바 형태 출력
# - 2: 한 epoch마다 결과 출력
# shuffle=True -- default값
loss_eval = model.evaluate(x=xdata,y=ydata)
print('loss_eval: ', loss_eval)
# loss_eval:  [0.11665954440832138, 0.11665954440832138]
pred = model.predict(xdata)
print("pred: ", pred.ravel())
print("real: ", ydata.ravel())
# pred:  [0.8730406 1.8722813 2.8715222 3.8707628 4.8700037]
# real:  [1.  2.  3.  3.5 5.5]

print("--- 결정계수(R2) ---")
from sklearn.metrics import r2_score
print("설명력: ", r2_score(ydata, pred))
# 설명력:  0.9237578583450347
import matplotlib.pyplot as plt
plt.scatter(xdata,ydata, color='r', marker='o', label='real')
plt.plot(xdata,pred, 'b--', label='pred')
plt.show()

# 새로운 값으로 예측
new_x = np.array([1.5, 5.7, -3.0]).reshape(-1,1)
new_pred = model.predict(new_x)
print("새 값 예측 결과: ", new_pred.ravel())
# 새 값 예측 결과:  [1.7973964 6.1197844 2.3525732]











