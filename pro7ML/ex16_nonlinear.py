# 회귀분석의 한 예로 scikit-learn 패키지에서 제공하는 주택가격을 예측하는 Dataset을 사용할 수 있다. 
# 이는 범죄율, 공기 오염도 등의 주거 환경 정보 등을 사용하여 70년대 미국 보스턴 시의 주택가격을 표시하고 있다.
# * 데이터 세트 특성 :
#     : 인스턴스 수 : 506
#     : 속성의 수 : 13 개의 숫자 / 범주 적 예측
#     : 중간 값 (속성 14)은 대개 대상입니다
#     : 속성 정보 (순서대로) :
# CRIM   자치시(town) 별 1인당 범죄율
# ZN 25,000   평방피트를 초과하는 거주지역의 비율
# INDUS   비소매상업지역이 점유하고 있는 토지의 비율
# CHAS   찰스강에 대한 더미변수(강의 경계에 위치한 경우는 1, 아니면 0)
# NOX   10ppm 당 농축 일산화질소
# RM   주택 1가구당 평균 방의 개수
# AGE   1940년 이전에 건축된 소유주택의 비율
# DIS   5개의 보스턴 직업센터까지의 접근성 지수
# RAD   방사형 도로까지의 접근성 지수
# TAX   10,000 달러 당 재산세율
# PTRATIO   자치시(town)별 학생/교사 비율
# B   1000(Bk-0.63)^2, 여기서 Bk는 자치시별 흑인의 비율을 말함.
# LSTAT   모집단의 하위계층의 비율(%)
# MEDV   본인 소유의 주택가격(중앙값) (단위: $1,000)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures # 다항식 특징 추가


df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/housing.data", 
                    header=None, sep=r'\s+')    # 정규표현식 ??
df.columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM',
        'AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
pd.set_option('display.max_columns', None)
print(df.head(2))
print(df.corr())
#              CRIM        ZN     INDUS      CHAS       NOX        RM       AGE  \
# CRIM     1.000000 -0.200469  0.406583 -0.055892  0.420972 -0.219247  0.352734
# ZN      -0.200469  1.000000 -0.533828 -0.042697 -0.516604  0.311991 -0.569537
# INDUS    0.406583 -0.533828  1.000000  0.062938  0.763651 -0.391676  0.644779
# CHAS    -0.055892 -0.042697  0.062938  1.000000  0.091203  0.091251  0.086518
# NOX      0.420972 -0.516604  0.763651  0.091203  1.000000 -0.302188  0.731470
# RM      -0.219247  0.311991 -0.391676  0.091251 -0.302188  1.000000 -0.240265
# AGE      0.352734 -0.569537  0.644779  0.086518  0.731470 -0.240265  1.000000
# DIS     -0.379670  0.664408 -0.708027 -0.099176 -0.769230  0.205246 -0.747881
# RAD      0.625505 -0.311948  0.595129 -0.007368  0.611441 -0.209847  0.456022
# TAX      0.582764 -0.314563  0.720760 -0.035587  0.668023 -0.292048  0.506456
# PTRATIO  0.289946 -0.391679  0.383248 -0.121515  0.188933 -0.355501  0.261515
# B       -0.385064  0.175520 -0.356977  0.048788 -0.380051  0.128069 -0.273534
# LSTAT    0.455621 -0.412995  0.603800 -0.053929  0.590879 -0.613808  0.602339
# MEDV    -0.388305  0.360445 -0.483725  0.175260 -0.427321  0.695360 -0.376955

#               DIS       RAD       TAX   PTRATIO         B     LSTAT      MEDV
# CRIM    -0.379670  0.625505  0.582764  0.289946 -0.385064  0.455621 -0.388305
# ZN       0.664408 -0.311948 -0.314563 -0.391679  0.175520 -0.412995  0.360445
# INDUS   -0.708027  0.595129  0.720760  0.383248 -0.356977  0.603800 -0.483725
# CHAS    -0.099176 -0.007368 -0.035587 -0.121515  0.048788 -0.053929  0.175260
# NOX     -0.769230  0.611441  0.668023  0.188933 -0.380051  0.590879 -0.427321
# RM       0.205246 -0.209847 -0.292048 -0.355501  0.128069 -0.613808  0.695360
# AGE     -0.747881  0.456022  0.506456  0.261515 -0.273534  0.602339 -0.376955
# DIS      1.000000 -0.494588 -0.534432 -0.232471  0.291512 -0.496996  0.249929
# RAD     -0.494588  1.000000  0.910228  0.464741 -0.444413  0.488676 -0.381626
# TAX     -0.534432  0.910228  1.000000  0.460853 -0.441808  0.543993 -0.468536
# PTRATIO -0.232471  0.464741  0.460853  1.000000 -0.177383  0.374044 -0.507787
# B        0.291512 -0.444413 -0.441808 -0.177383  1.000000 -0.366087  0.333461
# LSTAT   -0.496996  0.488676  0.543993  0.374044 -0.366087  1.000000 -0.737663
# MEDV     0.249929 -0.381626 -0.468536 -0.507787  0.333461 -0.737663  1.000000

x = df[['LSTAT']].values
y = df[['MEDV']].values
print(x[:3])
# [[4.98]
#  [9.14]
#  [4.03]]
print(y[:3])
# [[24. ]
#  [21.6]
#  [34.7]]

# 단항을 통한 선형모델
model = LinearRegression()

# 다항 특성
quad = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
x_quad = quad.fit_transform(x)
x_cubic = cubic.fit_transform(x)
# print(x_quad[:3])
# [[ 1.      4.98   24.8004]
#  [ 1.      9.14   83.5396]
#  [ 1.      4.03   16.2409]]
# print(x_cubic[:3])
# [[  1.         4.98      24.8004   123.505992]
#  [  1.         9.14      83.5396   763.551944]
#  [  1.         4.03      16.2409    65.450827]]

# 단순 회귀
model.fit(x,y)
x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]
y_lin_fit = model.predict(x_fit)
# print('y_lin_fit: ', y_lin_fit)

from sklearn.metrics import r2_score
model_r2 = r2_score(y, model.predict(x))
print("model_r2: ", model_r2)
# model_r2:  0.5441462975864797


# 2차
model.fit(x_quad,y) # 여기선 왜 x_quad를 쓰지. 아래 라인에서는 quad.fit_transform(x_fit)이고
y_quad_fit = model.predict(quad.fit_transform(x_fit))
quad_r2 = r2_score(y, model.predict(x_quad))
print("quad_r2: ", quad_r2)
# quad_r2:  0.6407168971636612


# 3차
model.fit(x_cubic,y) 
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
cubic_r2 = r2_score(y, model.predict(x_cubic))
print("cubic_r2: ", cubic_r2)
# cubic_r2:  0.6578476405895719

plt.scatter(x,y, label='초기 데이터')
plt.plot(x_fit, y_lin_fit, linestyle=':', label='linear fit(d=1), $R^2=%.2f$'%model_r2, c='b', lw=3)
plt.plot(x_fit, y_quad_fit, linestyle='-', label='quad fit(d=2), $R^2=%.2f$'%quad_r2, c='r', lw=3)
# x_fit으로 통일해주는 이유를 모르겠네. 당연한거같으면서도. quad로 피팅했는데 x_fit?
plt.plot(x_fit, y_cubic_fit, linestyle=':', label='cubic fit(d=3), $R^2=%.2f$'%cubic_r2, c='k', lw=3)
plt.legend()
plt.xlabel("하위 계층 비율")
plt.ylabel("주택 가격")
plt.show()




