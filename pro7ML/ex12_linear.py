# Linear Regression 클래스 사용

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression       # summary 기능 없음
from sklearn.metrics import r2_score,explained_variance_score,mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


# 데이터생성
sample_size = 100
np.random.seed(1)

x = np.random.normal(0,10,sample_size)
y = np.random.normal(0,10,sample_size) + x*30

print(x[:5])
print(y[:5])
# [ 16.24345364  -6.11756414  -5.28171752 -10.72968622   8.65407629]
# [ 482.83232345 -171.28184705 -154.41660926 -315.95480141  248.67317034]
print("상관계수: ", np.corrcoef(x,y)[0, 1])
# 상관계수:  0.9993935724865679
print()
# 독립변수 x를 정규화 하기 (0~1 사이 범위 내 자료로 변환)
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1,1))        # -1: 알아서
print(x[:5])
print(x_scaled[:5])
# [ 16.24345364  -6.11756414  -5.28171752 -10.72968622   8.65407629]
# [[0.87492405]
#  [0.37658554]
#  [0.39521325]
#  [0.27379961]
#  [0.70578689]]
print()

#시각화
# plt.scatter(x_scaled,y)
# plt.show()

model = LinearRegression().fit(x_scaled,y)
print("model: ", model)
print('회귀계수(slope): ', model.coef_)
print("회귀계수(Intercept=Bias): ", model.intercept_)
print("결정계수(R^2=rsquared): ", model.score(x_scaled,y))

y_pred = model.predict(x_scaled)    # 예측된 y값
print()
print("예측값: ", y_pred[:5])
print("실제값: ", y[:5])
# 예측값:  [ 490.32381062 -182.64057041 -157.48540955 -321.44435455  261.91825779]
# 실제값:  [ 482.83232345 -171.28184705 -154.41660926 -315.95480141  248.67317034]

# Cost = 실제값 - 예측값 >> 모델 설계 시 Cost 최소화..

# 모델 성능 확인함수 작성
def myRegScoreFunc(y_true, y_pred):
    # 결정 계수: 실제 관측값의 분산 대비 예측값의 부산을 계산하여 데이터 예측의 정확도 성능 측정(? 표현이 좀 이상한데)
    print(f"r^2_score(결정계수):                        {r2_score(y_true,y_pred)}")
    # 모델이 데이터의 분산을 얼마나 잘 설명하는지 나타내는 지표
    print(f"explained_variance_score(설명 분산 점수):   {explained_variance_score(y_true,y_pred)}")
    # 오차를 제곱해 평균 구함(오차가 커질수록 손실함수 값이 빠르게 증가함. 값이 작으면 모델 성능 우수)
    print(f"Mean_Squared_Error(MSE, 평균제곱근오차):    {mean_squared_error(y_true,y_pred)}")


myRegScoreFunc(y, y_pred) # 실제값, 예측값 입력
# r+^2_score(결정계수):                        0.9987875127274646
# explained_variance_score(설명 분산 점수):   0.9987875127274646
# Mean_Squared_Error(MSE, 평균제곱근오차):    86.14795101998747

print("---- 분산이 크게 다른 x,y값을 사용 ----")
x2 = np.random.normal(0,1, sample_size)
y2 = np.random.normal(0,1, sample_size) + x2 *30

print(x2[:5])
print(y2[:5])
print("상관계수: ", np.corrcoef(x2,y2)[0, 1])

x2_scaled = scaler.fit_transform(x2.reshape(-1,1))        # -1: 알아서
print(x2[:5])
print(x2_scaled[:5])
print()

#시각화
# plt.scatter(x_scaled,y)
# plt.show()

model2 = LinearRegression().fit(x2_scaled,y2)
print("model2: ", model2)
print('회귀계수(slope): ', model2.coef_)
print("회귀계수(Intercept=Bias): ", model2.intercept_)
print("결정계수(R^2=rsquared): ", model2.score(x2_scaled,y2))
# model2:  LinearRegression()
# 회귀계수(slope):  [156.98130724]
# 회귀계수(Intercept=Bias):  -83.65663146090387
# 결정계수(R^2=rsquared):  0.9987538556342392
# >> 분산이 너무 다른 데이터로 만든 모델은 의미 없다 . (?)



 











































