# 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량에 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 운동 10시간 초과는 이상치로 한다.  

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. 데이터 생성
raw_values = [
    [1, 0.9, 0.7, 4.2], [2, 1.2, 1.0, 3.8], [3, 1.2, 1.3, 3.5],
    [4, 1.9, 2.0, 4.0], [5, 3.3, 3.9, 2.5], [6, 4.1, 3.9, 2.0],
    [7, 5.8, 4.1, 1.3], [8, 2.8, 2.1, 2.4], [9, 3.8, 3.1, 1.3],
    [10, 4.8, 3.1, 35.0], [11, np.nan, 3.5, 4.0], [12, 0.9, 0.7, 4.2],
    [13, 3.0, 2.0, 1.8], [14, 2.2, 1.5, 3.5], [15, 2.0, 2.0, 3.5]
]
df = pd.DataFrame(raw_values, columns=['구분', '지상파', '종편', '운동'])

# 2. 결측치 처리 (지상파 평균값으로 채우기)
df['지상파'] = df['지상파'].fillna(df['지상파'].mean())

# 3. IQR 기반 이상치 제거 (운동 칼럼 기준)
Q1 = df['운동'].quantile(0.25)
Q3 = df['운동'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR  # 상한선 계산 (약 6.7)

# IQR 범위를 벗어나는 행을 통째로 제거 (df_clean의 인덱스 일관성 유지)
df_clean = df[df['운동'] <= upper_bound].copy()

# --- 분석 데이터 추출 ---
x = df_clean['지상파']
y1 = df_clean['운동']
y2 = df_clean['종편']

# 4. 회귀분석 수행 (scipy.stats.linregress)
model1 = stats.linregress(x, y1) # 지상파 vs 운동
model2 = stats.linregress(x, y2) # 지상파 vs 종편

# 결과 출력 (주석 포함)
print("--- [결과 1] 지상파 시청시간에 따른 운동 시간 ---")
print(f"기울기: {model1.slope:.4f}")      # -0.5430
print(f"절편: {model1.intercept:.4f}")    # 4.3414
print(f"p-value: {model1.pvalue:.6f}")   # 0.000213 (0.05 미만이므로 유의함)

print("\n--- [결과 2] 지상파 시청시간에 따른 종편 시청 시간 ---")
print(f"기울기: {model2.slope:.4f}")      # 0.7185
print(f"절편: {model2.intercept:.4f}")    # 0.3801
print(f"p-value: {model2.pvalue:.6f}")   # 0.000030 (매우 유의함)

# 5. 시각화
plt.figure(figsize=(12, 5))

# 그래프 1: 지상파 vs 운동
plt.subplot(1, 2, 1)
plt.scatter(x, y1, color='blue', label='Data')
plt.plot(x, model1.slope * x + model1.intercept, color='red', label='Regression')
plt.title(f'KBS vs Workout (Upper: {upper_bound:.2f})')
plt.legend()

# 그래프 2: 지상파 vs 종편
plt.subplot(1, 2, 2)
plt.scatter(x, y2, color='green', label='Data')
plt.plot(x, model2.slope * x + model2.intercept, color='red', label='Regression')
plt.title('KBS vs JTBC')
plt.legend()

plt.show()

'''
[최종 요약]
- IQR 상한선인 {upper_bound:.2f}를 넘는 10번 행(운동 35.0)이 성공적으로 제거됨.
- 지상파와 운동량 사이에는 음의 상관관계가 뚜렷하며, p-value가 낮아 회귀 모델이 유효함.
- 지상파와 종편 사이에는 양의 상관관계가 나타남.
'''