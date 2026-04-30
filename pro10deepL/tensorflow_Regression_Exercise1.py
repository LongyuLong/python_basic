import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

"""
data를 이용해 아버지 키로 아들의 키를 예측하는 회귀분석 모델을 작성하시오.
- train / test 분리
- Sequential api와 function api 를 사용해 모델을 만들어 보시오.
- train과 test의 mse를 시각화 하시오
- 새로운 아버지 키에 대한 자료로 아들의 키를 예측하시오.
"""

data = pd.read_csv("https://raw.githubusercontent.com/data-8/materials-fa17/refs/heads/master/lec/galton.csv")

print(data.head(2))
#   family  father  mother  midparentHeight  children  childNum  gender  childHeight
# 0      1    78.5    67.0            75.43         4         1    male         73.2
# 1      1    78.5    67.0            75.43         4         2  female         69.2

data = data[data["gender"] == "male"]
dad = data['father'].to_numpy(dtype=np.float32).reshape(-1, 1)
child = data["childHeight"].to_numpy(dtype=np.float32).reshape(-1, 1)

print("dad shape:", dad.shape)
print("child shape:", child.shape)

# test set은 학습 중 validation으로 쓰지 않고, 마지막 평가용 새로운 데이터처럼 사용
x_train, x_test, y_train, y_test = train_test_split(dad, child, shuffle=True,
                                                    test_size=0.3, random_state=123)

# 스케일링
# scaler는 train 데이터로만 학습하고, test 데이터에는 transform만 적용
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print("\n-- 모델 생성 방법1 - Sequential API --")

model1 = Sequential([
    Input((1, )),
    Dense(units=4, activation='relu'),
    Dense(units=1, activation='linear')
])

print(model1.summary())
opti1 = optimizers.Adam(learning_rate=0.01)
model1.compile(loss='mse', optimizer=opti1, metrics=["mse"])

# train 내부에서 validation_split=0.2로 validation 데이터 분리
history1 = model1.fit(x=x_train_scaled, y=y_train,
                        validation_split=0.2,
                        batch_size=8, epochs=30,
                        verbose=0, shuffle=True)

loss_metrics1_train = model1.evaluate(x=x_train_scaled, y=y_train, verbose=0)

print("train loss metrics1: ", loss_metrics1_train)

# test set을 새로운 데이터처럼 예측
pred1 = model1.predict(x_test_scaled, verbose=0)

print("설명력: ", r2_score(y_test, pred1))
print("실제값: ", y_test.ravel()[:10])
print("예측값: ", pred1.ravel()[:10])


# train / validation mse 시각화
plt.plot(history1.history['mse'], label='train mse')
plt.plot(history1.history['val_mse'], label='validation mse')
plt.xlabel("epochs")
plt.ylabel("mse")
plt.title("Sequential API - train / validation mse")
plt.legend()
plt.show()


# test set 실제값과 예측값 시각화
plt.scatter(x_test, y_test, color='r', marker='o', label='real')
plt.scatter(x_test, pred1, color='b', marker='x', label='pred')
plt.xlabel("father height")
plt.ylabel("son height")
plt.title("Sequential API prediction - test set")
plt.legend()
plt.show()


############################################
print("\n-- 모델 생성 방법2 - Function API --")
from tensorflow.keras.models import Model

# 입력층
inputs = Input(shape=(1, ), name="input_layer")

# 은닉층
hidden = Dense(units=4, activation='relu', name="HiddenLayer_1")(inputs)

# 출력층
outputs = Dense(units=1, activation="linear", name="OutputLayer")(hidden)

# 모델 생성
func_model = Model(inputs=inputs, outputs=outputs)

print(func_model.summary())

opti2 = optimizers.Adam(learning_rate=0.01)

func_model.compile(loss='mse', optimizer=opti2, metrics=["mse"])

# train 내부에서 validation_split=0.2로 validation 데이터 분리
# test set은 여기서 사용하지 않음
func_history = func_model.fit(x=x_train_scaled, y=y_train,
                                validation_split=0.2,
                                epochs=30, batch_size=8,
                                verbose=0, shuffle=True)

func_ev_train = func_model.evaluate(x=x_train_scaled, y=y_train, verbose=0)
func_ev_test = func_model.evaluate(x=x_test_scaled, y=y_test, verbose=0)

print("func train loss: ", func_ev_train)

# test set을 새로운 데이터처럼 예측
func_pred = func_model.predict(x_test_scaled, verbose=0)

print("설명력: ", r2_score(y_test, func_pred))
print("실제값: ", y_test.ravel()[:10])
print("예측값: ", func_pred.ravel()[:10])

# train / validation mse 시각화
plt.plot(func_history.history['mse'], label='train mse')
plt.plot(func_history.history['val_mse'], label='validation mse')
plt.xlabel("epochs")
plt.ylabel("mse")
plt.title("Function API - train / validation mse")
plt.legend()
plt.show()

# test set 실제값과 예측값 시각화
plt.scatter(x_test, y_test, color='r', marker='o', label='real')
plt.scatter(x_test, func_pred, color='b', marker='x', label='pred')
plt.xlabel("father height")
plt.ylabel("son height")
plt.title("Function API prediction - test set")
plt.legend()
plt.show()