# SVM으로 XOR 연산 처리하기

x_data = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
        ]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

# feature, label 분리
# feature = []
# label = []
# for row in x_data:
#     p = row[0]  
#     q = row[1]  
#     r = row[2]  
#     feature.append([p,q])                      
#     label.append([r])                      

# print(feature)  # [[0, 0], [0, 1], [1, 0], [1, 1]]
# print(label)    # [[0], [0], [0], [0]]

x_df = pd.DataFrame(x_data)
feature = np.array(x_df.iloc[:, 0:2])
label = np.array(x_df.iloc[:,2])

print(feature)
# [[0 0]
#  [0 1]
#  [1 0]
#  [1 1]]
print(label)
# [0 0 0 0]

lmodel = LogisticRegression()   # 선형분류 모델
smodel = svm.SVC()              # 선형/비선형 모두 가능한 분류 모델

lmodel.fit(feature, label)
smodel.fit(feature, label)

pred1 = lmodel.predict(feature)
print("선형 모델(lmodel) 예측값: ", pred1)
pred2 = smodel.predict(feature)
print("선형/비선형 모델(smodel) 예측값: ", pred2)
print()

acc1 = metrics.accuracy_score(label, pred1)
print('선형 모델(lmodel) 분류 정확도: ', acc1)
# 선형 모델(lmodel) 분류 정확도:  0.5
acc2 = metrics.accuracy_score(label, pred2)
print('선형/비선형 모델(smodel) 분류 정확도: ', acc2)
# 선형/비선형 모델(smodel) 분류 정확도:  1.0


