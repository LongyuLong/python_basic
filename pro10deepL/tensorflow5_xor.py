import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras.optimizers import SGD, RMSprop, Adam

# 1) 데이터 수집 및 가공
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [1]])    # XOR 게이트

model = Sequential()
model.add(Input(shape=(2,)))    # 입력층
model.add(Dense(units=5, activation='relu')) # 은닉층
model.add(Dense(units=5, activation='relu')) # 은닉층
model.add(Dense(units=1, activation='sigmoid')) # 출력층
print(model.summary())  # 설계된 모델의 Layer, Parameter 수 확인
# Model: "sequential"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 1)                   │               3 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 3 (12.00 B)
#  Trainable params: 3 (12.00 B)
#  Non-trainable params: 0 (0.00 B)

# parameter 수: (입력 수 + 1) * 출력 수

model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.01), metrics=['accuracy'])
history = model.fit(x=x, y=y, epochs=50, batch_size=1, verbose=1)
loss_metrics = model.evaluate(x=x, y=y)
print('loss_metrics: ', loss_metrics)
print(history.history)
# log .... 생기고
# loss_metrics:  [0.38072648644447327, 0.75]
# {'accuracy': [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75], 
# 'loss': [0.6480703949928284, 0.5994418859481812, 0.5564282536506653, 0.5314331650733948, 0.5021571516990662, 0.48152726888656616, 0.45842546224594116, 0.43101397156715393, 0.4157625436782837, 0.3989664316177368]}

proba = model.predict(x=x, verbose = 0)
pred = (proba > 0.5).astype('int32')
print('예측 값 : ', pred)

import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label = "loss")
plt.plot(history.history['accuracy'], label = "accuracy")
plt.legend()
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()











