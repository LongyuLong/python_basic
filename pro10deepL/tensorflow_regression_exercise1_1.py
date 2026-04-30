import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/data-8/materials-fa17/refs/heads/master/lec/galton.csv")
data = data[data["gender"] == "male"]

dad = data['father'].to_numpy(dtype=np.float32).reshape(-1, 1)
child = data["childHeight"].to_numpy(dtype=np.float32).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(dad, child, shuffle=True,
                                                    test_size=0.3, random_state=123)

# x, y 모두 스케일링
scaler_x = StandardScaler()
scaler_y = StandardScaler()

x_train_scaled = scaler_x.fit_transform(x_train)
x_test_scaled  = scaler_x.transform(x_test)

y_train_scaled = scaler_y.fit_transform(y_train)
y_test_scaled  = scaler_y.transform(y_test)


# ── Sequential API ──────────────────────────────────────────────
print("\n-- 모델 생성 방법1 - Sequential API --")

# 모델 생성 직전 seed 고정
tf.random.set_seed(42)
np.random.seed(42)

model1 = Sequential([
    Input((1,)),
    Dense(units=4, activation='relu'),
    Dense(units=1, activation='linear')
])

print(model1.summary())
model1.compile(loss='mse', optimizer=optimizers.Adam(learning_rate=0.01), metrics=["mse"])

history1 = model1.fit(x=x_train_scaled, y=y_train_scaled,
                    validation_data=(x_test_scaled, y_test_scaled),
                    batch_size=8, epochs=100,
                    verbose=0, shuffle=True)

# 예측 후 역변환
pred1 = scaler_y.inverse_transform(model1.predict(x_test_scaled, verbose=0))
print("설명력:", r2_score(y_test, pred1))

# train / test mse 시각화
plt.plot(history1.history['mse'], label='train mse')
plt.plot(history1.history['val_mse'], label='test mse')
plt.xlabel("epochs")
plt.ylabel("mse")
plt.title("Sequential API - train / test mse")
plt.legend()
plt.show()

# 실제값 / 예측값 시각화
plt.scatter(x_test, y_test, color='r', marker='o', label='real')
plt.scatter(x_test, pred1, color='b', marker='x', label='pred')
plt.xlabel("father height")
plt.ylabel("son height")
plt.title("Sequential API prediction - test set")
plt.legend()
plt.show()


# ── Functional API ──────────────────────────────────────────────
print("\n-- 모델 생성 방법2 - Functional API --")
from tensorflow.keras.models import Model

# 두 번째 모델 생성 직전에도 seed 재고정
tf.random.set_seed(42)
np.random.seed(42)

inputs  = Input(shape=(1,), name="input_layer")
hidden  = Dense(units=4, activation='relu', name="HiddenLayer_1")(inputs)
outputs = Dense(units=1, activation='linear', name="OutputLayer")(hidden)

func_model = Model(inputs=inputs, outputs=outputs)
print(func_model.summary())

func_model.compile(loss='mse', optimizer=optimizers.Adam(learning_rate=0.01), metrics=["mse"])

func_history = func_model.fit(x=x_train_scaled, y=y_train_scaled,
                            validation_data=(x_test_scaled, y_test_scaled),
                            epochs=100, batch_size=8,
                            verbose=0, shuffle=True)

# 예측 후 역변환
func_pred = scaler_y.inverse_transform(func_model.predict(x_test_scaled, verbose=0))
print("설명력:", r2_score(y_test, func_pred))

# train / test mse 시각화
plt.plot(func_history.history['mse'], label='train mse')
plt.plot(func_history.history['val_mse'], label='test mse')
plt.xlabel("epochs")
plt.ylabel("mse")
plt.title("Functional API - train / test mse")
plt.legend()
plt.show()

# 실제값 / 예측값 시각화
plt.scatter(x_test, y_test, color='r', marker='o', label='real')
plt.scatter(x_test, func_pred, color='b', marker='x', label='pred')
plt.xlabel("father height")
plt.ylabel("son height")
plt.title("Functional API prediction - test set")
plt.legend()
plt.show()


# ── 새로운 아버지 키 입력 → 예측 ────────────────────────────────
print("\n-- 새로운 아버지 키로 아들 키 예측 --")

new_dad_height = float(input("아버지 키를 입력하세요 (단위: inch): "))
new_dad = np.array([[new_dad_height]], dtype=np.float32)
new_dad_scaled = scaler_x.transform(new_dad)

# 예측 후 역변환
seq_result  = scaler_y.inverse_transform(model1.predict(new_dad_scaled, verbose=0))[0][0]
func_result = scaler_y.inverse_transform(func_model.predict(new_dad_scaled, verbose=0))[0][0]

print(f"[Sequential API]  예측 아들 키: {seq_result:.2f} inch")
print(f"[Functional API]  예측 아들 키: {func_result:.2f} inch")


# TensorBoard 실행 --------
# pip install tensorboard
from tensorflow.keras.callbacks import TensorBoard
import datetime
import os

# TensorBoard 로그 저장 경로
log_dir = os.path.join('logs', 'fit', datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))

tb = TensorBoard(
    log_dir=log_dir,
    histogram_freq=1,
    write_graph=True,
    write_images=False
)

func_model.fit(x_train_scaled, y_train_scaled, epochs=100,
            batch_size=32, verbose=2,
            validation_split=0.2,
            callbacks=[tb])

# 텐서보드 실행 후 결과는 브라우저로 확인
# 터미널 프로젝트에서 > tensorboard --logdir /logs/fit
# 웹서비스가 시작됨. 여기서 확인









