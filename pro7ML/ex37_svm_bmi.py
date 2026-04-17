# BMI(Body Mass Index)는 체질량지수로, 몸무게(kg)를 키의 제곱으로 나눈 값을 뜻합니다. 
# 키와 몸무게로 체지방량을 추정하여 비만도를 간편하게 측정하는 지표로, 
# 보건소 등에서 비만 진단에 가장 널리 사용됩니다.
# 체중(kg) / {키(m)}^2
# ex. 170cm, 68kg --> 68 / (1.7)^2
"""
import random
random.seed(12)

def calc_bmiFunc(h, w):
    bmi = w / (h/100)**2
    if bmi < 18.5: return 'thin'
    if bmi < 25.0: return 'normal'
    return 'fat'

print(calc_bmiFunc(170,68))     # normal

fp = open('bmi.csv', mode='w')
fp.write('height,weight,label\n')     # 제목

# 무작위 데이터 생성
cnt = {'thin':0, 'normal':0, 'fat':0}
for i in range(50000):
    h = random.randint(150, 200)
    w = random.randint(35, 100)
    label = calc_bmiFunc(h, w)
    cnt[label] += 1
    fp.write('{0},{1},{2}\n'.format(h, w, label))

fp.close()
"""


# bmi data를 SVM으로 분류
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split # 모델 샘플링 추출 모듈
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import svm, metrics

df = pd.read_csv('bmi.csv')
print(df.head(2), df.shape)
print(df.info())
print()

label = df['label']
print(label[:2])
print()

w = df['weight'] / 100      # 정규화
print(w[:2].values)
print()

h = df['height'] / 200      # 정규화
print(h[:2].values)
print()

wh = pd.concat([w, h], axis=1)
print(wh.head(2))
#    weight  height
# 0    0.69    0.90
# 1    0.79    0.96
print()

# label은 dummy화
label = label.map({'thin':0, 'normal':1, 'fat':2})
print(label[:2])
# 0    1
# 1    1
print()

x_train, x_test, y_train, y_test = train_test_split(wh, label, test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape)      # (35000, 2) (15000, 2)

model = svm.SVC(C=0.01, kernel='rbf').fit(x_train, y_train)
print(model)    # SVC(C=0.01)

pred = model.predict(x_test)
print("예측값: ", pred[:10])
print("실제값: ", y_test[:10].values)
# 예측값:  [0 0 1 0 2 0 1 0 2 0]
# 실제값:  [0 0 1 0 2 0 1 0 2 0]

sc_score = metrics.accuracy_score(y_test, pred)
print('sc_score: ', sc_score)
# sc_score:  0.9654666666666667

# 교차 검증 모델
from sklearn import model_selection

cross_vali = model_selection.cross_val_score(model, wh, label, cv=3)  # 변수?
print("3회 각각의 정확도: ", cross_vali)
print("평균 정확도: ", cross_vali.mean())
# 3회 각각의 정확도:  [0.96940061 0.96586068 0.96681867]
# 평균 정확도:  0.9673599891736715

new_data = pd.DataFrame({'weight':[66, 88], 'height':[188, 160]})
new_data['weight'] = new_data['weight'] / 100
new_data['height'] = new_data['height'] / 200
print("***************확인용***************", new_data)


new_pred = model.predict(new_data)
print("새로운 값 예측 결과: ", new_pred)

# 시각화
df2 = pd.read_csv('bmi.csv', index_col=2)

def scatterFunc(lbl, color):
    b = df2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label = lbl)



scatterFunc('fat', 'red')
scatterFunc('normal', 'green')
scatterFunc('thin', 'blue')

plt.legend()
plt.show()



