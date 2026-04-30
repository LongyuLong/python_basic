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

print("\n모델 생성 방법2 - Functional API")
# 유연한 구조: 입력자료로 여러 층을 공유하거나 다양한 종류의 입출력 모델 생성 가능
# 다중입력값 모델, 다중출력값 모델, 공유층 활용 모델, 데이터 흐름이 비순차적인 경우에도 효과적

from tensorflow.keras.models import Model
inputs = Input(shape=(1,))  # 입력 크기 지정
output1 = Dense(units=4, activation='relu')(inputs)         # 히든레이어
outputs = Dense(units=1, activation='linear')(output1)      # output1을 받아서 outputs 출력
# 히든에서는 relu, 마지막엔 linear

model2 = Model(inputs, outputs)
opti2 = optimizers.SGD(learning_rate=0.001)
model2.compile(loss='mse', optimizer=opti2, metrics=['mse'])
history2 = model2.fit(x=xdata, y=ydata, batch_size=1, epochs=100, verbose=0)
loss_metrics2 = model2.evaluate(x=xdata, y=ydata)
ypred2 = model2.predict(xdata, verbose=0)

print("loss_metrics2 :", loss_metrics2)
print('설명력 :', r2_score(ydata, ypred2))
print('실제값 :', ydata.ravel())
print('예측값 :', ypred2.ravel())
print()

# 모델 생성 방법2 - Functional API
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 70ms/step - loss: 15.8272 - mse: 15.8272
# loss_metrics2 : [15.827165603637695, 15.827165603637695]
# 설명력 : 0.9398115277290344
# 실제값 : [15 32 39 55 60]
# 예측값 : [16.538897 27.047184 37.55547  48.063755 58.57204 ]



# =======================================================
# 모델 생성방법3
# Sub classing 사용
#   - Model을 상속받아 직접 모델 생성
# =======================================================
print("\n모델 생성 방법3 - Sub Classing")

class MyModel(Model):       # Model을 상속받았고..
    def __init__(self):
        super(MyModel, self).__init__()
        self.d1 = Dense(units=4, activation='relu')
        self.d2 = Dense(units=1, activation='linear')

    # x: input 매개변수
    def call(self,x):       # Input 클래스 사용하지 않고 call 메소드의 input 매개 변수 이용
        x = self.d1(x)
        return self.d2(x)
    
model3 = MyModel()
opti3 = optimizers.SGD(learning_rate=0.001)
model3.compile(loss='mse', optimizer=opti3, metrics=['mse'])
history3 = model3.fit(x=xdata, y=ydata, batch_size=1, epochs=100, verbose=0)
loss_metrics3 = model3.evaluate(x=xdata, y=ydata)
ypred3 = model3.predict(xdata, verbose=0)

print("loss_metrics3 :", loss_metrics3)
print('설명력 :', r2_score(ydata, ypred3))
print('실제값 :', ydata.ravel())
print('예측값 :', ypred3.ravel())
print()

# 모델 생성 방법3 - Sub Classing
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 66ms/step - loss: 7.5989 - mse: 7.5989
# loss_metrics3 : [7.598912239074707, 7.598912239074707]
# 설명력 : 0.9711024165153503
# 실제값 : [15 32 39 55 60]
# 예측값 : [17.822048 29.068354 40.314663 51.560966 62.80727 ]

print("\n모델 생성 방법3 - 1: Custom Layer 층 사용")
from tensorflow.keras.layers import Layer

class MyLayer(Layer):
    def __init__(self, units=1, **kwargs):
        super(MyLayer, self).__init__(**kwargs)
        self.units = units

    def build(self, input_shape):       # 내부적으로 call() 호출               
        print(f'build: input_shape = {input_shape}')
        self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                initializer='random_normal', trainable=True)
        self.b = self.add_weight(shape=(self.units, ), initializer='zeros', trainable=True) 
        # 설정 위처럼하는 이유를 1도모르겠음

    # 위에서 call() 호출했으니까
    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b # y = wx + b

class MLP(Model):
    def __init__(self, **kwargs):
        super(MLP, self).__init__(**kwargs)
        self.linear1 = MyLayer(3)
        self.linear2 = MyLayer(1)

    def call(self, inputs):
        net = self.linear1(inputs)
        net = tf.nn.relu(net)
        return self.linear2(net)
        # 이게좋은방법인가

model4 = MLP()

opti4 = optimizers.SGD(learning_rate=0.001)
model4.compile(loss='mse', optimizer=opti4, metrics=['mse'])
history4 = model4.fit(x=xdata, y=ydata, batch_size=1, epochs=100, verbose=0)
loss_metrics4 = model4.evaluate(x=xdata, y=ydata)
ypred4 = model4.predict(xdata, verbose=0)

print("loss_metrics4 :", loss_metrics4)
print('설명력 :', r2_score(ydata, ypred4))
print('실제값 :', ydata.ravel())
print('예측값 :', ypred4.ravel())
print()

# 1회차 실행
# 모델 생성 방법3 - 1: Custom Layer 층 사용
# build: input_shape = (1, 1)
# build: input_shape = (1, 3)
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 73ms/step - loss: 481.2558 - mse: 481.2558
# loss_metrics4 : [481.2557678222656, 481.2557678222656]
# 설명력 : -0.8301481008529663
# 실제값 : [15 32 39 55 60]
# 예측값 : [25.425165 25.425165 25.425165 25.425165 25.425165]

# 2회차 실행
# 모델 생성 방법3 - 1: Custom Layer 층 사용
# build: input_shape = (1, 1)
# build: input_shape = (1, 3)
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 65ms/step - loss: 8.7884 - mse: 8.7884
# loss_metrics4 : [8.788378715515137, 8.788378715515137]
# 설명력 : 0.966579020023346
# 실제값 : [15 32 39 55 60]
# 예측값 : [18.105536 29.669687 41.23385  52.798    64.362144]



