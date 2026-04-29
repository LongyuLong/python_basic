# 모델 생성방법 3가지 수행
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np


# 공부 시간에 따른 성적 결과 예측
xdata=np.array([1,2,3,4,5], dtype=np.float32).reshape(-1,1)
ydata=np.array([15,32,39,55,60]).reshape(-1,1)

print("모델 생성 방법1 - Sequential API")
# model = Sequential()
# model.add(Input((1,)))  # (1,) 표현 해설
# model.add(Dense(units=4, activation='relu'))
# model.add(Dense(units=1, activation='linear'))
model = Sequential([
    Input((1,)),
    Dense(units=4, activation='relu'),
    Dense(units=1, activation='linear')
])

print(model.summary())
# Model: "sequential"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 4)                   │               8 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_1 (Dense)                      │ (None, 1)                   │               5 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 13 (52.00 B)
#  Trainable params: 13 (52.00 B)
#  Non-trainable params: 0 (0.00 B)
# None

opti = optimizers.SGD(learning_rate=0.001)
model.compile(loss='mse', optimizer=opti, metrics=["mse"])
history = model.fit(x=xdata, y=ydata, batch_size=1, epochs=100, verbose=2)
loss_metrics = model.evaluate(x=xdata, y=ydata)
print("loss metrics: ", loss_metrics)
# loss metrics:  [12.980427742004395, 12.980427742004395]

ypred = model.predict(xdata, verbose=0)

from sklearn.metrics import r2_score
print("설명력: ", r2_score(ydata, ypred))
print("실제값: ", ydata.ravel())
print("예측값: ", ypred.ravel())
# ravel() : 다차원 배열 1차원으로 펼치기
# 설명력:  0.9506372809410095
# 실제값:  [15 32 39 55 60]
# 예측값:  [16.767172 27.416592 38.06601  48.715427 59.36485 ]

import matplotlib.pyplot as plt
plt.scatter(xdata,ydata, color='r', marker='o', label='real')
plt.plot(xdata,ypred, 'b--', label='pred')
plt.show()

# mse 변화량 시각화
plt.plot(history.history['mse'], label='mse')
plt.xlabel("epochs")
plt.show()



