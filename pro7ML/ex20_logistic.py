# logisticRegression: 다항분류(softmax 함수 사용) - iris dataset

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
# LogisticRegression: 다중 클래스(label, 종속변수)를 지원하도록 일반화됨
# 이를 softmax regression 또는 multinormial logistic regression이라 함

iris = datasets.load_iris()
print(iris.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
print(iris.target)
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]
print(iris.data[:3])
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]]
print(np.corrcoef(iris.data[:,2], iris.data[:,3])[0,1])
# 0.9628654314027961

x = iris.data[:, [2,3]]
y = iris.target                 # target의 역할이 뭐지
print(x.shape, ' ', y.shape)    # (150, 2)
print(x[:3], y[:3], set(map(int,y)))

print('\ntrain/test split (7:3)')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# (105, 2) (45, 2) (105,) (45,)
print(x_train[:3], ' / ', x_test[:3], ' / ',y_train[:3], ' / ', y_test[:3])
# [[3.7 1. ]
#  [5.1 1.5]
#  [5.5 1.8]]  /  
# [[4.7 1.2]
#  [1.7 0.3]
#  [6.9 2.3]]  /  [1 2 2]  /  [1 0 2]

"""
# Scaling (데이터 크기 표준화 - 최적화 과정에서 안정성, 수렴속도 향상, 과적합/과소적합 방지 등의 효과)
sc = StandardScaler()
sc.fit(x_train)         # 독립변수(feature)만 표준화함
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

print(x_train[:3])
# [[ 0.11133528 -0.13368658]
#  [ 0.87373991  0.49296928]
#  [ 1.0915698   0.8689628 ]]
print(x_test[:3])
# [[ 0.65591001  0.11697576]
#  [-0.97781419 -1.01100479]
#  [ 1.85397443  1.49561866]]
# 스케일링 결과 원복
ori_x_train = sc.inverse_transform(x_train)
print(ori_x_train[:3])
# [[3.7 1. ]
#  [5.1 1.5]
#  [5.5 1.8]]

"""

print("---- 분류 모델 생성 ----")
# model = LogisticRegression(random_state=10)
model = LogisticRegression(C=0.1, solver='lbfgs', multi_class='multinomial', random_state=10)
# 모델에 패널티 적용1 --> C: L2 규제. 숫자값을 조정해가며 정확도 확인(? 설명 더 잘할수있을거같은데)
# C값이 작을수록 규제 강도가 높다.
# 모델에 패널티 적용2 --> solver='lbfgs', 
# multi_class='multinomial' softmax 지원(?) auto

print(model)
# LogisticRegression(random_state=0)
model.fit(x_train, y_train)

# 분류 예측
y_pred = model.predict(x_test)
print('예측값: ', y_pred)
# 예측값:  [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1
#  0 0 0 2 1 1 0 0]
print('실제값: ', y_test)
# 실제값:  [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1
#  0 0 0 2 1 1 0 0]

print(f"총 갯수: {len(y_test)}, 오류 수:{(y_test != y_pred).sum()}")
# 총 갯수: 45, 오류 수:0
print("--- 분류 정확도 확인 1 ---")
print(f"{accuracy_score(y_test, y_pred)}")
# 1.0

print("--- 분류 정확도 확인 2 ---")
con_mat = pd.crosstab(y_test, y_pred, rownames=["예측치"], colnames=["관측치"])
print(con_mat)
# 0    19   0   0
# 1     0  13   0
# 2     0   0  13
print((con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test))    # 0.977?
# 1.0

print("--- 분류 정확도 확인 3 ---")
print("test score: ", model.score(x_test, y_test))
print("train score: ", model.score(x_train, y_train))
# test score:  1.0
# train score:  0.9523809523809523

# 학습 후 검증된 모델 저장 후 읽기
import joblib                           # pickle보다 빠르고 대용량 지원
joblib.dump(model, 'logimodel.pkl')     
del model
read_model = joblib.load('logimodel.pkl')

# 이후부터 read_model 사용
print("-- 새로운 값으로 예측하기 --")

new_data = np.array([[5.5, 2.2], [0.6, 0.3], [1.1, 0.5]])
# 만약 표준화된 자료로 모델을 생성했다면 new_data도 표준화해야함
# ex) sc.fit(new_data)
# new_data = sc.transform(new_data)

new_pred = read_model.predict(new_data)
print("예측 결과: ", new_pred)
# 예측 결과:  [2 0 0]
print(read_model.predict_proba(new_data))           # _proba는 또 뭐여
# [[5.91889564e-03 2.52234609e-01 7.41846495e-01]
#  [9.43977276e-01 5.56278534e-02 3.94870164e-04]
#  [8.95173034e-01 1.03462250e-01 1.36471531e-03]]

# 시각화




























