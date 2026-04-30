import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/Advertising.csv")
print(data.head(3))
del data["no"]
print(data.head(3))
#    no     tv  radio  newspaper  sales
# 0   1  230.1   37.8       69.2   22.1
# 1   2   44.5   39.3       45.1   10.4
# 2   3   17.2   45.9       69.3    9.3
#       tv  radio  newspaper  sales
# 0  230.1   37.8       69.2   22.1
# 1   44.5   39.3       45.1   10.4
# 2   17.2   45.9       69.3    9.3

features = data[['tv', 'radio', 'newspaper']]
ldata = data.iloc[:,[3]]
print(features.head(3))
print(ldata[:2])
#       tv  radio  newspaper
# 0  230.1   37.8       69.2
# 1   44.5   39.3       45.1
# 2   17.2   45.9       69.3
#    sales
# 0   22.1
# 1   10.4

# feature 간 단위의 차이가 클 경우, 정규화/표준화 작업이 모델 성능에 도움된다
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler

# 정규화
scaler = MinMaxScaler(feature_range=(0,1))
fedata = scaler.fit_transform(features)
print(fedata[:3])

fedata = minmax_scale(features, axis=0, copy=True)  # 행 기준, 원본자료 보존
print(fedata[:3])

# train/test 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(fedata, ldata, shuffle=True,
                                                    test_size=0.3, random_state=123)
# 주의할 점: stratyfy는 회귀에서는 안줌..
print(x_train[:2], x_train.shape)
print(x_test[:2], x_test.shape)
# [[0.77578627 0.76209677 0.60598065]
#  [0.1481231  0.79233871 0.39401935]
#  [0.0557998  0.92540323 0.60686016]]
# [[0.77578627 0.76209677 0.60598065]
#  [0.1481231  0.79233871 0.39401935]
#  [0.0557998  0.92540323 0.60686016]]
# [[0.80858979 0.08266129 0.32189974]
#  [0.30334799 0.00604839 0.20140721]] (140, 3)
# [[0.67331755 0.0625     0.30167106]
#  [0.26885357 0.         0.07827617]] (60, 3)


# 전처리가 모두 끝난 경우, 모델 설계 및 실행

print()
# 전처리가 모두 끝난 경우 모델 설계 및 실행
model = Sequential()
model.add(Input(shape=(3, )))   # tv radio newspaper
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=1, activation='linear'))  # sales 하나니까?
# 마지막 레이어에서는 activation 생략해도 자동으로 linear로 설정된다

print(model.summary())
# Model: "sequential"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 16)                  │              64 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_1 (Dense)                      │ (None, 8)                   │             136 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_2 (Dense)                      │ (None, 1)                   │               9 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 209 (836.00 B)
#  Trainable params: 209 (836.00 B)
#  Non-trainable params: 0 (0.00 B)
# None

# pip install pydot << 케라스 모델구조 이미지파일로 저장
tf.keras.utils.plot_model(
    model,
    to_file = 'aaa.png',
    show_shapes=True,
    show_layer_names=True,
    show_dtype=True,
    show_layer_activations=True,
    dpi = 96
    )

model.compile(optimizer='adam', loss='mse', metrics=["mse"])

history = model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2, validation_split=0.2)

ev_loss = model.evaluate(x_test, y_test, verbose=0)
print('ev_loss: ', ev_loss)
# ev_loss:  [5.381180763244629, 5.381180763244629]

# history 값 확인
print('history: ', history.history)
print('history loss: ', history.history['loss'])
print('history mse: ', history.history['mse'])
print('history validation loss: ', history.history['val_loss']) # validation split이 있을 때
print('history validation mse: ', history.history['val_mse'])   # validation split이 있을 때

# loss 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['val_loss'], label='val_loss')
plt.plot(history.history['loss'], label='loss')
plt.legend()
plt.show()

from sklearn.metrics import r2_score
print("설명력: ", r2_score(y_test, model.predict(x_test)))
# 설명력:  0.6742448806762695

# predict
pred = model.predict(x_test[:5])
print("예측값: ", pred.ravel())
print("실제값: ", y_test[:5].values.ravel())
# 예측값:  [12.576224  8.033887 15.211267 10.598056 12.632567]
# 실제값:  [11.4  8.8 14.7 10.1 14.6]

print("\n--- Functional API를 이용한 방법 ---")
# 다중 입출력, 분기구조, 병합 구조 등 복잡한 신경망모델 작성 시 효과적
from tensorflow.keras.models import Model

# 입력층 정의
inputs = Input(shape=(3, ), name='input_layer')     # name은 텐서보드 등에 사용
# 은닉층 정의
x = Dense(units=16, activation='relu', name="HiddenLayer_1")(inputs)
x = Dense(units=8, activation='relu', name="HiddenLayer_2")(x)
# 출력층 정의
outputs = Dense(units=1, name="OutputLayer")(x)

# 모델 생성(입력과 출력을 연결)
func_model = Model(inputs=inputs, outputs=outputs)
print(func_model.summary())
# --- Functional API를 이용한 방법 ---
# Model: "functional_3"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ input_layer (InputLayer)             │ (None, 3)                   │               0 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ HiddenLayer 1 (Dense)                │ (None, 16)                  │              64 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ HiddenLayer 2 (Dense)                │ (None, 8)                   │             136 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ OutputLayer (Dense)                  │ (None, 1)                   │               9 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 209 (836.00 B)
#  Trainable params: 209 (836.00 B)
#  Non-trainable params: 0 (0.00 B)
# None

func_model.compile(optimizer='adam', loss='mse', metrics=["mse"])
func_history = func_model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2, validation_split=0.2)
func_ev_loss = func_model.evaluate(x_test, y_test, verbose=0)

print('func_ev_loss: ', func_ev_loss)
print("설명력: ", r2_score(y_test, func_model.predict(x_test)))
# func_ev_loss:  [8.906405448913574, 8.906405448913574]
# 2/2 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step
# 설명력:  0.6623133420944214









