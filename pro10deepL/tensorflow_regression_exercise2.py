# 자전거 공유 시스템 분석용 데이터 train.csv를 이용하여 대여횟수에 영향을 주는 변수들을 골라 다중선형회귀분석 모델을 작성하시오.
# 모델 학습시에 발생하는 loss를 시각화하고 설명력을 출력하시오.
# 새로운 데이터를 input 함수를 사용해 키보드로 입력하여 대여횟수 예측결과를 콘솔로 출력하시오.
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
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/data/train.csv")

# 대여회수(count)에 영향주는거 찾기 -- 상관계수 분석
# print(data.head(3))
#               datetime  season  holiday  workingday  weather  temp   atemp  humidity  windspeed  casual  registered  count
# 0  2011-01-01 00:00:00       1        0           0        1  9.84  14.395        81        0.0       3          13     16
# 1  2011-01-01 01:00:00       1        0           0        1  9.02  13.635        80        0.0       8          32     40
# 2  2011-01-01 02:00:00       1        0           0        1  9.02  13.635        80        0.0       5          27     32

# ── 상관계수 분석 ──────────────────────────────────────────
# datetime → 시간 정보 추출 (시각/요일/월은 대여량에 유의미)
data['datetime'] = pd.to_datetime(data['datetime'])
data['hour']      = data['datetime'].dt.hour
data['dayofweek'] = data['datetime'].dt.dayofweek  # 0=월 ~ 6=일
data['month']     = data['datetime'].dt.month

# casual, registered는 count의 하위항목 → 누수 변수라 제거
df = data.drop(columns=['datetime', 'casual', 'registered'])

# 전체 상관행렬
corr_matrix = df.corr()

# count와의 상관계수만 추출 후 절댓값 내림차순 정렬
corr_with_count = corr_matrix['count'].drop('count').sort_values(key=abs, ascending=False)
print("=== count와의 상관계수 ===")
print(corr_with_count.round(3))

# 히트맵 시각화
plt.figure(figsize=(10, 8))
import seaborn as sns
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('상관계수 히트맵')
plt.tight_layout()
plt.show()

# count와 상관계수 막대그래프
plt.figure(figsize=(9, 5))
colors = ['tomato' if v > 0 else 'steelblue' for v in corr_with_count]
corr_with_count.plot(kind='bar', color=colors)
plt.axhline(0.3, color='red', linestyle='--', linewidth=0.8, label='|r|=0.3 기준선')
plt.axhline(-0.3, color='red', linestyle='--', linewidth=0.8)
plt.title('count와 각 변수의 상관계수')
plt.ylabel('Pearson r')
plt.legend()
plt.tight_layout()
plt.show()

# ── 두 브랜치 비교: 최소 vs 풀셋 ──────────────────────────
FEATURES = {
    '최소 (3변수)': ['hour', 'temp', 'humidity'],
    '풀셋 (6변수)': ['hour', 'temp', 'humidity', 'month', 'weather', 'windspeed'],
}

def build_model(n_features):
    model = Sequential([
        Input(shape=(n_features,)),
        Dense(units=1, activation="linear")
    ])
    model.compile(optimizer=optimizers.Adam(0.01), loss='mse')
    return model

results  = {}
histories = {}
models   = {}
scalers  = {}

for name, cols in FEATURES.items():
    X = df[cols].values
    y = df['count'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)

    es = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)

    model = build_model(len(cols))
    history = model.fit(X_train, y_train, epochs=500, batch_size=64,
                        validation_split=0.1, callbacks=[es], verbose=0)

    y_pred = model.predict(X_test).flatten()
    r2 = r2_score(y_test, y_pred)

    results[name]   = r2
    histories[name] = history
    models[name]    = model
    scalers[name]   = scaler
    print(f"[{name}]  R² = {r2:.4f}")

# ── Loss 비교 시각화 ──
fig, axes = plt.subplots(1, 2, figsize=(13, 4))
for ax, (name, history) in zip(axes, histories.items()):
    ax.plot(history.history['loss'],     label='train loss')
    ax.plot(history.history['val_loss'], label='val loss', linestyle='--')
    ax.set_title(f'{name}  R²={results[name]:.4f}')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('MSE Loss')
    ax.legend()
plt.suptitle('브랜치별 학습 Loss 비교')
plt.tight_layout()
plt.show()

# ── R² 막대 비교 ──
plt.figure(figsize=(6, 4))
bars = plt.bar(results.keys(), results.values(), color=['steelblue', 'tomato'], width=0.4)
for bar, r2 in zip(bars, results.values()):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                f'{r2:.4f}', ha='center', va='bottom', fontsize=11)
plt.ylim(0, 1)
plt.ylabel('R²')
plt.title('모델 설명력 비교 (R²)')
plt.tight_layout()
plt.show()
# ──────────────────────────────────────────────────────────

# ── 키보드 입력으로 대여횟수 예측 ─────────────────────────
# R²가 더 높은 모델을 자동 선택
best_name = max(results, key=results.get)
best_cols = FEATURES[best_name]
print(f"\n예측에 사용할 모델: {best_name}  (R²={results[best_name]:.4f})")
print("─" * 40)

# 변수별 입력 안내 메시지
PROMPTS = {
    'hour'     : '시간 (0~23): ',
    'temp'     : '기온 (°C, 예: 20.5): ',
    'humidity' : '습도 (%, 예: 60): ',
    'month'    : '월 (1~12): ',
    'weather'  : '날씨 (1=맑음 2=흐림 3=약한비/눈 4=강한비/눈): ',
    'windspeed': '풍속 (예: 10.0): ',
}

user_input = []
for col in best_cols:
    val = float(input(PROMPTS[col]))
    user_input.append(val)

X_new = np.array([user_input])
X_new_scaled = scalers[best_name].transform(X_new)
pred = models[best_name].predict(X_new_scaled, verbose=0)[0][0]

print(f"\n예측 자전거 대여횟수: {max(0, round(pred))} 대")
# ──────────────────────────────────────────────────────────

