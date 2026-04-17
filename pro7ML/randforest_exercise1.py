# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv 
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv
# Input variables (based on physicochemical tests):
#  1 - fixed acidity
#  2 - volatile acidity
#  3 - citric acid
#  4 - residual sugar
#  5 - chlorides
#  6 - free sulfur dioxide
#  7 - total sulfur dioxide
#  8 - density
#  9 - pH
#  10 - sulphates
#  11 - alcohol
#  Output variable (based on sensory data):
#  12 - quality (score between 0 and 10)

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.pipeline import Pipeline   # 전처리 + 모델을 하나로 묶어서 실행
from sklearn.compose import ColumnTransformer   # 칼럼별 전처리를 다르게 적용
from sklearn.impute import SimpleImputer    # 결측치 처리
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score

df = pd.DataFrame(pd.read_csv("winequality-red.csv"))
# print(df.head())
pd.set_option('display.max_columns', None)
print(df.info())
#  #   Column                Non-Null Count  Dtype
# ---  ------                --------------  -----
#  0   fixed acidity         1596 non-null   float64
#  1   volatile acidity      1596 non-null   float64
#  2   citric acid           1596 non-null   float64
#  3   residual sugar        1596 non-null   float64
#  4   chlorides             1596 non-null   float64
#  5   free sulfur dioxide   1596 non-null   float64
#  6   total sulfur dioxide  1596 non-null   float64
#  7   density               1596 non-null   float64
#  8   pH                    1596 non-null   float64
#  9   sulphates             1596 non-null   float64
#  10  alcohol               1596 non-null   float64
#  11  quality               1596 non-null   int64
# ** 결측치 없음

# target = Quality
x = df.drop('quality', axis=1)
y = df['quality']
# print(x)
#       free sulfur dioxide  total sulfur dioxide  density    pH  sulphates         alcohol 
# 0                    11.0                  34.0  0.99780  3.51       0.56         9.4
# 1                    25.0                  67.0  0.99680  3.20       0.68         9.8
# 2                    15.0                  54.0  0.99700  3.26       0.65         9.8
# 3                    17.0                  60.0  0.99800  3.16       0.58         9.8
# 4                    11.0                  34.0  0.99780  3.51       0.56         9.4
# ...                   ...                   ...      ...   ...        ...         ...
# 1591                 32.0                  44.0  0.99490  3.45       0.58        10.5
# 1592                 39.0                  51.0  0.99512  3.52       0.76        11.2
# 1593                 29.0                  40.0  0.99574  3.42       0.75        11.0
# 1594                 32.0                  44.0  0.99547  3.57       0.71        10.2
# 1595                 18.0                  42.0  0.99549  3.39       0.66        11.0

# print(y)
# 0       5
# 1       5
# 2       5
# 3       6
# 4       5
#        ..
# 1591    5
# 1592    6
# 1593    6
# 1594    5
# 1595    6
# Name: quality, Length: 1596, dtype: int64


# 컬럼 분리 : 숫자형, 범주형
num_cols = x.select_dtypes(include=['int64', 'float64']).columns # 숫자형 칼럼만 선택
cat_cols = x.select_dtypes(include=['category', 'object']).columns # 범주형 칼럼만 선택

# 전처리 파이프라인(숫자형)
num_pipeline = Pipeline([   # 처리 항목들을 연결해 연속적으로 실행
    ('scaler', StandardScaler())    # 표준화(평균 0, 표준편차 1)
])

# 전처리 파이프라인(범주형)
cat_pipeline = Pipeline([
    ('onehot', OneHotEncoder(handle_unknown='ignore'))      # 범주형 -> One-hot 인코딩
])

preprocesss = ColumnTransformer([
    ('num', num_pipeline, num_cols),    # 숫자형 컬럼에 num_pipeline 적용
    ('cat', cat_pipeline, cat_cols)     # 범주형 칼럼에 cat_pipeline 적용
])

# 전체 파이프라인(전처리 + 모델)
pipeline = Pipeline([
    ('prep', preprocesss),       # 전처리 단계
    ('model',RandomForestClassifier(random_state=12))   # 모델
])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12, stratify=y)
# stratify : 층화 유지 -- 클래스 비율 유지하면서 테스트셋을 쪼개기

model = RandomForestClassifier(n_estimators=100, random_state=12)

# 튜닝할 범위 설정
param_grid = {
    'model__n_estimators':[100, 200],    # 트리 갯수
    'model__max_depth':[5, 10, None],    # 트리의 깊이
    'model__class_weight':[None, 'balanced']  # 클래스 불균형 보정
}

cv= StratifiedKFold(n_splits=5, shuffle=True,random_state=12)

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv = cv,
    scoring='f1_macro',
    n_jobs=-1
)

# 학습
grid.fit(x_train, y_train)

# 최적 결과 출력
print('최적의 파라미터 : ', grid.best_params_)
print('F1-score(CV 기준) : ', grid.best_score_)

# 최적모델 + 예측
best_model = grid.best_estimator_

pred = grid.predict(x_test)

# 정확도, f1스코어 출력
final_acc = accuracy_score(y_test, pred)
final_f1 = f1_score(y_test, pred, average='macro') # macro 평균 사용

print("-" * 30)
print(f"최종 테스트 정확도 (Accuracy): {final_acc:.4f}")
print(f"최종 테스트 F1-Score (Macro) : {final_f1:.4f}")
print("-" * 30)

# 3. 상세 리포트 (클래스별 점수를 한눈에 확인)
print("\n[ 상세 분류 리포트 ]")
print(classification_report(y_test, pred))
