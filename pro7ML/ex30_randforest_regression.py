# RandomForest 는 분류, 회귀 모두 가능. sklearn모듈은 대개 그러하다.
# 캘리포니아 주택 가격 데이터로 회귀 분석
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.pipeline import Pipeline   # 전처리 + 모델을 하나로 묶어서 실행
from sklearn.compose import ColumnTransformer   # 칼럼별 전처리를 다르게 적용
from sklearn.impute import SimpleImputer    # 결측치 처리
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score

housing = fetch_california_housing(as_frame=True)
print(housing.DESCR)
pd.set_option('display.max_columns', )
print(housing.data[:2])
















