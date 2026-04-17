# LogisticRegression(회귀 분류 모델) - 강수 예측해보기

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/weather.csv")
print(data.head(2), data.shape)
#          Date  MinTemp  MaxTemp  Rainfall  Sunshine  WindSpeed  Humidity  Pressure  Cloud  Temp RainToday RainTomorrow
# 0  2016-11-01      8.0     24.3       0.0       6.3         20        29    1015.0      7  23.6        No          Yes
# 1  2016-11-02     14.0     26.9       3.6       9.7         17        36    1008.4      3  25.7       Yes          Yes (366, 12)
data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis=1)
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':0})
print(data2.head(2), data2.shape)
#    MinTemp  MaxTemp  Rainfall  Sunshine  WindSpeed  Humidity  Pressure  Cloud  Temp  RainTomorrow
# 0      8.0     24.3       0.0       6.3         20        29    1015.0      7  23.6             1
# 1     14.0     26.9       3.6       9.7         17        36    1008.4      3  25.7             1 (366, 10)

# RainTomorrow: 종속변수(범주형, label, class), 나머지열: 독립변수(feature)

print("데이터 분리: Train data, Test data")
# 모델의 성능을 객관적으로 파악. 모델 학습과 검증에 사용된 자료가 같다면 과적합 발생
# 데이터 분리: Train data, Test data
# (256, 10) (110, 10)

train, test = train_test_split(data2, test_size=0.3, random_state=42)
print(train.shape, test.shape)
print(train.head(3))
#      MinTemp  MaxTemp  Rainfall  Sunshine  WindSpeed  Humidity  Pressure  Cloud  Temp  RainTomorrow
# 268     -2.0     11.3       0.2       5.9         19        50    1015.3      7  10.9             0
# 231      4.0     15.9       0.0       2.0          7        63    1019.7      7  14.8             1
# 157      5.9     21.8       0.0       9.3         11        35    1024.1      5  20.8             0


# 모델 생성
col_select = "+".join(train.columns.difference(["RainTomorrow"]))
print(col_select)
my_formula = 'RainTomorrow ~'  + col_select
model = smf.logit(formula=my_formula, data=train).fit()
print(model.summary())
print(model.params)
print()
print("예측값: ", np.rint(model.predict(test)[:5].values))
print("실제값: ", test["RainTomorrow"][:5].values)
# 예측값:  [0. 0. 0. 0. 0.]
# 실제값:  [0 0 0 0 0]

# 분류 정확도
conf_mat = model.pred_table()
print(conf_mat)
# [[197.   9.]
#  [ 21.  26.]]
print("훈련 정확도: ", (conf_mat[0][0] + conf_mat[1][1]) / len(train))
# 분류 정확도:  0.87109375
from sklearn.metrics import accuracy_score
pred = model.predict(test)
print("테스트 정확도: ", accuracy_score(test['RainTomorrow'], np.around(pred)))
# 분류 정확도:  0.8727272727272727

# 위에서는 train에 대한 혼동행렬로 정확도를 따졌고, 아래에서는 test에 대한 분류 정확도를 따졌는데
# 학습을 한게 아니니 분류모델의 학습/검증으로 생각하면 안되는건가? 분류 정확도라고 표현하니까 이상해보이는데

































