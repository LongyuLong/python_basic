'''
    주식(stock)데이터로 다중선형회귀모델 작성
    전날 데이터로 다음날 종가(Close) 예측
'''
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras import optimizers
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.preprocessing import MinMaxScaler

# 배열 자료로 읽기
datas = np.loadtxt("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/stockdaily.csv", 
                delimiter=',',  # 구분자 ,
                skiprows=1      # 제목 빼기
                )
print(datas[:2], datas.shape) # (732, 5)

# feature
x_data = datas[:, 0:-1] # 'Close'제외 -Open,High,Low,Volume
print(x_data.shape)     # (732, 4)

# 정규화 scaler
scaler = MinMaxScaler(feature_range=(0, 1)) 
x_data = scaler.fit_transform(x_data)
print(x_data[:2])                             # [[0.97333581 0.97543152 1.         0.11112306]
# print(scaler.inverse_transform(x_data)[:2]) # [[8.28659973e+02 8.33450012e+02 8.28349976e+02 1.24770000e+06]

# label
y_data = datas[:, [-1]] # 'Close':종가
print(y_data[:2])
print()

'''
전날 데이터에 현재데이터(label)로 밀어넣기
오늘 x 데이터에 다음날 y값 넣기
'''
print(x_data[0], y_data[0])
print(x_data[1], y_data[1])

# x_data와 y_data를 한칸씩 어긋나게 맞추기 위한 전처리
x_data = np.delete(x_data, -1, axis=0)  # 마지막 데이터 삭제
y_data = np.delete(y_data, 0)           # 첫번째 데이터 삭제
print('x_data 마지막 삭제, y_data 첫번째 삭제')
print(x_data[0], y_data[0])
# x_data 마지막 삭제, y_data 첫번째 삭제
# [0.97333581 0.97543152 1.         0.11112306] 828.070007
print()

print('train / test split 없이 모델 작성')
model = Sequential()
model.add(Input(shape=(4,)))
model.add(Dense(units=1, activation='linear'))

model.compile(loss='mse', optimizer='sgd', metrics=['mse'])
model.fit(x_data, y_data, epochs=200, verbose=0)

print(f'evaluate result : {model.evaluate(x_data, y_data, verbose=0)}')
# [62.61282730102539, 62.61282730102539]

# 결정계수 확인하기
pred = model.predict(x_data)
print(f'train / test split 없이 설명력 확인 : {r2_score(y_data, pred)}')
# train / test split 없이 설명력 확인 : 0.9938512516479705 << 과적합 가능성 매우높다

# 시각화
plt.plot(y_data, 'orange', label='실제값')
plt.plot(pred, 'g--', label = '예측값')
plt.legend()
plt.show()

print()
print("train/test split 한 모델")
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.3, random_state=123, shuffle=False)

print(x_train.shape, x_test.shape)
# (511, 4) (220, 4)

print('train / test split 없이 모델 작성 -- 2')
model2 = Sequential()
model2.add(Input(shape=(4,)))
model2.add(Dense(units=1, activation='linear'))

model2.compile(loss='mse', optimizer='sgd', metrics=['mse'])
model2.fit(x_data, y_data, epochs=200, verbose=0, validation_split=0.15)

print(f'evaluate result : {model2.evaluate(x_data, y_data, verbose=0)}')
# evaluate result : [67.0099105834961, 67.0099105834961]
# 결정계수 확인하기
pred2 = model2.predict(x_data)
print(f'validation 추가 후 설명력 확인 : {r2_score(y_data, pred2)}')

# 시각화
plt.plot(y_data, 'b', label='실제값')
plt.plot(pred2, 'r--', label = '예측값')
plt.legend()
plt.show()

# 딥러닝의 이슈: 최적화와 일반화




