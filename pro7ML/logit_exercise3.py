# [로지스틱 분류분석 문제3]
# Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용
# 얘를 사용해도 됨   'testdata/advertisement.csv' 
# 참여 칼럼 : 
#    - Daily Time Spent on Site : 사이트 이용 시간 (분)
#    - Age : 나이,
#    - Area Income : 지역 소득,
#    - Daily Internet Usage :일별 인터넷 사용량(분),
#    - Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )
# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# 데이터 간 단위가 큰 경우 표준화 작업을 시도한다.
# 모델 성능 출력 : 정확도, 정밀도, 재현율, ROC 커브와 AUC 출력
# 새로운 데이터로 분류 작업을 진행해 본다.

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/advertisement.csv")

# print(data.head(1))
#    Daily Time Spent on Site / Age / Area Income / Daily Internet Usage / Ad Topic Line
#    City / Male / Country / Timestamp / Clicked on Ad
# train/test set 분리
x = data[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage']]
y = data['Clicked on Ad']
# print(x[:1])
#    Daily Time Spent on Site  Age  Area Income  Daily Internet Usage
# 0                     68.95   35      61833.9                256.09
# print(y[:3])
# 0    0
# 1    0
# 2    0

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
# print(x_train[:3], '\n------\n', x_test[:3], '\n------\n', y_train[:3], '\n------\n', y_test[:3])
#      Daily Time Spent on Site  Age  Area Income  Daily Internet Usage
# 541                     75.65   39     64021.55                247.90
# 440                     46.04   32     65499.93                147.92
# 482                     69.42   25     65791.17                213.38 
# ------
#       Daily Time Spent on Site  Age  Area Income  Daily Internet Usage
# 521                     63.26   29     54787.37                120.46
# 737                     71.23   52     41521.28                122.59
# 740                     43.63   38     61757.12                135.25
# ------
#  541    0
# 440    1
# 482    0
# Name: Clicked on Ad, dtype: int64
# ------
#  521    1
# 737    1
# 740    1
# Name: Clicked on Ad, dtype: int64

# Scaling (데이터 크기 표준화 - 최적화 과정에서 안정성, 수렴속도 향상, 과적합/과소적합 방지 등의 효과)
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

model = LogisticRegression(C=0.06, solver='lbfgs', random_state=1)
model.fit(x_train, y_train)

# 분류
y_pred = model.predict(x_test)
# print("예측값: ", y_pred[:10])
# # 예측값:  [1 1 1 1 0 0 0 1 0 1]
# print("실제값: \n", y_test[:10])
# 실제값: 
# 521    1
# 737    1
# 740    1
# 660    1
# 411    0
# 678    0
# 626    0
# 513    1
# 859    0
# 136    1
print(f"총 갯수: {len(y_test)}, 오류 수:{(y_test != y_pred).sum()}")
# 총 갯수: 300, 오류 수:12
print("--- 분류 정확도 확인 ---")
print(f"{accuracy_score(y_test, y_pred)}")
# --- 분류 정확도 확인 ---
# 0.96
print()
print("모델 성능 파악")
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))
# [[144   2]    TP  FN
#  [ 10 144]]   FP  TN
acc = (144 + 2) / 300       # TP + TN / 전체수  정확도
recall = 144 / (144 + 2)      # TP / (TP + FN)    재현율
precission = 144 / (144 + 10)  # TP / (TP + FP)    정밀도
specificity = 144 / (10 + 144)  # TN / (FP + TN)    특이도
fallout = 10 / (10 + 144)      # FP / (FP + TN)    위양성율

# print('acc : ', acc)                    # acc :  0.4866666666666667
# print('recall : ', recall)              # recall :  0.9863013698630136             
# print('precission : ', precission)      # precission :  0.935064935064935
# print('specificity : ', specificity)    # specificity :  0.935064935064935 
# print('fallout : ', fallout)            # fallout :  0.06493506493506493
# print('fallout : ', 1 - specificity)    # fallout :  0.06493506493506496 

from sklearn import metrics
import matplotlib.pyplot as plt
import koreanize_matplotlib

cl_rep = metrics.classification_report(y_test, y_pred)
print(cl_rep)       # 종합 보고서?
print()

fpr, tpr, thresholds = metrics.roc_curve(y_test, model.decision_function(x_test))
print('fpr : \n', fpr)
# fpr :  
# [0.         0.         0.         0.00684932 0.00684932 0.01369863
#  0.01369863 0.02054795 0.02054795 0.02739726 0.02739726 0.03424658
#  0.03424658 0.04109589 0.04109589 0.10273973 0.10273973 0.10958904
#  0.10958904 0.20547945 0.20547945 0.47260274 0.47260274 0.78082192
#  0.78082192 1.        ]
print('tpr : \n', tpr)
# tpr :  
# [0.         0.00649351 0.85714286 0.85714286 0.92207792 0.92207792
#  0.93506494 0.93506494 0.94155844 0.94155844 0.94805195 0.94805195
#  0.96103896 0.96103896 0.96753247 0.96753247 0.97402597 0.97402597
#  0.98051948 0.98051948 0.98701299 0.98701299 0.99350649 0.99350649
#  1.         1.        ]

# thresholds : 분류결정 임계값(결정함수값)
plt.plot(fpr, tpr, 'o-', label='LogisticRegression')
plt.plot([0, 1],[0, 1], 'k--', label='landom classifier line(AUC:0.5)')
plt.plot([fallout], [recall], 'ro', ms=6)   # 위양성률, 재현율 출력
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC Curve')
plt.legend()
plt.show()

print("AUC : ", metrics.auc(fpr, tpr))  # AUC :  0.9723999999999999 매우 성능이 우수한 모델
# AUC :  0.9875022238035938


x_test_new = [[40, 35, 62000, 100], [40, 30, 61000, 120], [80, 35, 63000, 260], 
                [50, 34, 56000, 210], [88, 25, 62000, 170], [80, 35, 62000, 230], 
                [60, 33, 66500, 150], [82, 15, 56000, 190], [80, 35, 60000, 210], 
                [70, 32, 69000, 160], [85, 32, 46000, 200], [80, 35, 56000, 220], 
                [80, 31, 61000, 180], [100, 39, 60000, 200], [80, 35, 65000, 100], 
            ]
y_test_new = [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
y_pred_new = model.predict(x_test_new)
print(f"총 갯수: {len(y_test_new)}, 오류 수:{(y_test_new != y_pred_new).sum()}")
# 총 갯수: 300, 오류 수:12
print("--- 분류 정확도 확인 ---")
print(f"{accuracy_score(y_test_new, y_pred_new)}")
# --- 분류 정확도 확인 ---
# 0.5333333333333333








