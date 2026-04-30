# 다중선형회귀
# 조기종료 코드
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

datas = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/auto-mpg.csv',na_values='?')
print(datas.head(2))
print(datas.info())
del datas['car name']
datas = datas.dropna()
print(datas.isna().sum())

datas.drop(['cylinders', 'acceleration', 'model year','origin'],
            axis = 'columns', inplace=True)

print(datas.head(2))

# sns.pariplot(datas[['mpg', 'displacement', 'horsepower', 'weight']],
            # diag_kind = 'kde')
# plt.show()

# train / test split
train_dataset = datas.sample(frac=0.7, random_state=123)
print(train_dataset[:2], train_dataset.shape)
test_dataset = datas.drop(train_dataset.index)
print(test_dataset[:2], test_dataset.shape)

# 표준화: (요소값 - 평균) / 표준편차
train_stat = train_dataset.describe()
train_stat.pop("mpg")
print(train_stat)

train_stat = train_stat.transpose()     # 전치
print(train_stat)

def stdscal_func(x):
    return (x - train_stat["mean"]) / train_stat["std"]

print("표준화: (요소값 - 평균) / 표준편차 결과\n", stdscal_func(train_dataset[:3]))
#       displacement  horsepower  mpg    weight
# 222      0.599039    0.133053  NaN  1.247890
# 247     -1.042328   -0.881744  NaN -1.055604
# 136      0.992967    0.894151  NaN  1.341651

st_train_data = stdscal_func(train_dataset)
st_train_data = st_train_data.drop(['mpg'], axis='columns')

print(st_train_data[:3])
#      displacement  horsepower    weight
# 222      0.599039    0.133053  1.247890
# 247     -1.042328   -0.881744 -1.055604
# 136      0.992967    0.894151  1.341651

st_test_data = stdscal_func(test_dataset)
st_test_data = st_test_data.drop(['mpg'], axis='columns')
print(st_test_data[:3])

train_label = train_dataset.pop("mpg")
print(train_label[:3])
# 222    17.0
# 247    39.4
# 136    16.0

test_label = test_dataset.pop('mpg')
print(test_label[:3])

# model
def build_model():
    network = Sequential([
        Input(shape=(3,)),
        Dense(units=32, activation="relu"),
        Dense(units=16, activation="relu"),
        Dense(units=1, activation="linear")
    ])

    opti = tf.keras.optimizers.Adam(learning_rate=0.001)
    network.compile(optimizer=opti, loss="mean_squared_error",
                    metrics=['mean_squared_error', 'mean_absolute_error'])
    return network

model = build_model()
print(model.summary())
# Model: "sequential"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 32)                  │             128 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_1 (Dense)                      │ (None, 16)                  │             528 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ dense_2 (Dense)                      │ (None, 1)                   │              17 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 673 (2.63 KB)
#  Trainable params: 673 (2.63 KB)
#  Non-trainable params: 0 (0.00 B)
# None

EPOCHS = 5000

# 얼리스탑
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss", # 뭘 기준으로할지. loss, val_loss
    patience=5,        
    # baseline=0.01       # 최소한의 성능
    restore_best_weights=True   # 학습 도중 가장 성능이 좋은 epoch의 가중치를 취한다
    )   


history = model.fit(x=st_train_data, y=train_label, batch_size=32,
                    epochs=EPOCHS, verbose=2, validation_split=0.2,
                    callbacks = [early_stop]
                    )

df = pd.DataFrame(history.history)  # 왜 이렇게함?
print(df.head(3))
#          loss  mean_absolute_error  mean_squared_error    val_loss  val_mean_absolute_error  val_mean_squared_error
# 0  615.535522            23.336460          615.535522  595.221008                22.996567              595.221008
# 1  553.205505            21.827341          553.205505  525.640686                21.352312              525.640686
# 2  464.128571            19.371130          464.128571  404.464905                18.053181              404.464905
print(df.columns)
# Index(['loss', 'mean_absolute_error', 'mean_squared_error', 'val_loss',
#        'val_mean_absolute_error', 'val_mean_squared_error'],
#       dtype='object')

# 모델 학습 정보 시각화
def plt_history(df):
    hist = df
    hist["epoch"] = history.epoch

    plt.figure(figsize=(8, 14))
    plt.subplot(2, 1, 1)
    plt.xlabel("epoch")
    plt.ylabel("mae [mpg]")
    plt.plot(hist["epoch"], hist["mean_absolute_error"], label="train err")
    plt.plot(hist["epoch"], hist["val_mean_absolute_error"], label="validation err")
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.xlabel("epoch")
    plt.ylabel("mse [mpg]")
    plt.plot(hist["epoch"], hist["mean_squared_error"], label="train err")
    plt.plot(hist["epoch"], hist["val_mean_squared_error"], label="validation err")
    plt.legend()
    plt.show()


plt_history(df)

# 모델평가
from sklearn.metrics import r2_score
loss, mse, mae = model.evaluate(st_test_data, test_label)
print(f'loss: {loss:.4f}')
print(f'mse: {mse:.4f}')
print(f'mae: {mae:.4f}')
print("결정계수: ", r2_score(test_label, model.predict(st_test_data)))
# 4/4 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - loss: 15.4811 - mean_absolute_error: 3.1804 - mean_squared_error: 15.4811 
# loss: 15.4811
# mse: 15.4811
# mae: 3.1804
# 4/4 ━━━━━━━━━━━━━━━━━━━━ 0s 9ms/step 
# 결정계수:  0.7064471511720056

# 새로운 값으로 예측
new_data = pd.DataFrame({"displacement":[300, 400],
                        "horsepower":[120, 150],
                        "weight":[2000, 4000]
                        })

new_st_data = stdscal_func(new_data)
new_data_pred = model.predict(new_st_data).ravel()
print("새 값 예측결과: ", new_data_pred)
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 23ms/step
# 새 값 예측결과:  [19.39801  16.280685]

