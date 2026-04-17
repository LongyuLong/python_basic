# Kaggle의 Santander customer satisfaction dataset 사용
# santander 은행 고객만족 여부 분류 처리
# 클래스(label)명: target, 0: 만족, 1: 불만족

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from xgboost import plot_importance
from sklearn.model_selection import train_test_split

# pd.set_option('display.max_columns', None)

df = pd.read_csv("santander_train.csv", encoding='latin-1')
# print(df.head(2))     # column 수가 너무많아서 가독성 떨어짐
print(df.shape)     # (76020, 371)
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 76020 entries, 0 to 76019
# Columns: 371 entries, ID to TARGET
# dtypes: float64(111), int64(260)
# memory usage: 215.2 MB


# 전체 데이터에서 만족과 불만족의 비율 확인
print("-- 전체 데이터에서 만족과 불만족의 비율 확인 --")
print(df['TARGET'].value_counts())
# TARGET
# 0    73012
# 1     3008
print()
unsatisfied_cnt = df[df['TARGET']==1].TARGET.count()
total_cnt = df.TARGET.count()
print(f"불만족 비율: {(unsatisfied_cnt/total_cnt)*100}%")
# 불만족 비율: 3.9568534596158904%
print()

print(df.describe())        # column 수가 너무많아서 가독성 떨어짐 >> pd.set_option(..) 주석처리
#                   ID           var3         var15  ...  saldo_medio_var44_ult3         var38        TARGET
# count   76020.000000   76020.000000  76020.000000  ...            76020.000000  7.602000e+04  76020.000000
# mean    75964.050723   -1523.199277     33.212865  ...               56.614351  1.172358e+05      0.039569
# std     43781.947379   39033.462364     12.956486  ...             2852.579397  1.826646e+05      0.194945
# min         1.000000 *-999999.000000*    5.000000  ...                0.000000  5.163750e+03      0.000000
# 25%     38104.750000       2.000000     23.000000  ...                0.000000  6.787061e+04      0.000000
# 50%     76043.000000       2.000000     28.000000  ...                0.000000  1.064092e+05      0.000000
# 75%    113748.750000       2.000000     40.000000  ...                0.000000  1.187563e+05      0.000000
# max    151838.000000     238.000000    105.000000  ...           397884.300000  2.203474e+07      1.000000
print()

# df.describe()에서 확인된 outlier(-999999) 대체
print("-- df.describe()에서 확인된 outlier(-999999) 대체 --")
df['var3'].replace(-999999, 2, inplace=True)
df.drop('ID', axis=1, inplace=True)             # ID는 식별자이므로 제거
print(df.describe())
#                var3         var15  imp_ent_var16_ult1  ...  saldo_medio_var44_ult3         var38        TARGET
# count  76020.000000  76020.000000        76020.000000  ...            76020.000000  7.602000e+04  76020.000000
# mean       2.716483     33.212865           86.208265  ...               56.614351  1.172358e+05      0.039569
# std        9.447971     12.956486         1614.757313  ...             2852.579397  1.826646e+05      0.194945
# min        0.000000      5.000000            0.000000  ...                0.000000  5.163750e+03      0.000000
# 25%        2.000000     23.000000            0.000000  ...                0.000000  6.787061e+04      0.000000
# 50%        2.000000     28.000000            0.000000  ...                0.000000  1.064092e+05      0.000000
# 75%        2.000000     40.000000            0.000000  ...                0.000000  1.187563e+05      0.000000
# max      238.000000    105.000000       210000.000000  ...           397884.300000  2.203474e+07      1.000000

# feature / label 분리
print("-- feature / label 분리 --")
x_features = df.iloc[:, :-1]        # 마지막열만 제외
y_label = df.iloc[:,-1]
print("x_features shape: ", x_features.shape)
# x_features shape:  (76020, 369) -------(76020, 371)에서 2개 줄었다(ID, TARGET)

# train / test split
print("-- train / test split --")
x_train, x_test, y_train, y_test = train_test_split(x_features, y_label, test_size=0.2, random_state=0)
train_cnt = y_train.count()
test_cnt = y_test.count()
print(x_train.shape, x_test.shape)
# (60816, 369) (15204, 369)
print()
print('학습데이터 레이블 값 분포 비율: ', y_train.value_counts() / train_cnt)
# 학습데이터 레이블 값 분포 비율:  TARGET
# 0    0.960964
# 1    0.039036
print()
print('검증데이터 레이블 값 분포 비율: ', y_test.value_counts() / test_cnt)
# 검증데이터 레이블 값 분포 비율:  TARGET
# 0    0.9583
# 1    0.0417
print()

xgb_clf = XGBClassifier(n_estimators=5, random_state=12, eval_metric='auc')
xgb_clf.fit(x_train, y_train, eval_set=[(x_train, y_train), (x_test, y_test)])
xgb_roc_score = roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:,1])
# [0]     validation_0-auc:0.84292        validation_1-auc:0.82682
# [1]     validation_0-auc:0.85114        validation_1-auc:0.83389
# [2]     validation_0-auc:0.85699        validation_1-auc:0.83338
# [3]     validation_0-auc:0.86184        validation_1-auc:0.83388
# [4]     validation_0-auc:0.86530        validation_1-auc:0.83431
print(f"xgb_roc_score: {xgb_roc_score:.5f}")
# xgb_roc_score: 0.83431

pred = xgb_clf.predict(x_test)
print("예측값: ", pred[:5])
print("실제값: ", y_test[:5].values)
# 예측값:  [0 0 0 0 0]
# 실제값:  [0 0 0 0 0]
from sklearn import metrics
print("분류 정확도: ", metrics.accuracy_score(y_test, pred))    # 변수넣는거 아직도 잘 모르겠네
# 분류 정확도:  0.9583004472507235


# 최적 파라미터 구하기
params = {'max_depth':[5,7], 'min_child_weight':[1,3], 'colsample_bytree':[0.5,0.75]}
# max_depth: 트리 깊이 
# min_child_weight: 관측치 가중치합 최소(?)
# colsample_bytree: Feature 비율

grid_cv = GridSearchCV(xgb_clf, param_grid=params)
print(grid_cv)
# GridSearchCV(estimator=XGBClassifier(base_score=None, booster=None,
#                                      callbacks=None, colsample_bylevel=None,
#                                      colsample_bynode=None,
#                                      colsample_bytree=None, device=None,
#                                      early_stopping_rounds=None,
#                                      enable_categorical=False,
#                                      eval_metric='auc', feature_types=None,
#                                      feature_weights=None, gamma=None,
#                                      grow_policy=None, importance_type=None,
#                                      interaction_constraints=None,
#                                      learning_rate=None, max_bin=None,
#                                      max_cat_threshold=None,
#                                      max_cat_to_onehot=None,
#                                      max_delta_step=None, max_depth=None,
#                                      max_leaves=None, min_child_weight=None,
#                                      missing=nan, monotone_constraints=None,
#                                      multi_strategy=None, n_estimators=5,
#                                      n_jobs=None, num_parallel_tree=None, ...),
#              param_grid={'colsample_bytree': [0.5, 0.75], 'max_depth': [5, 7],
#                          'min_child_weight': [1, 3]})

grid_cv.fit(x_train, y_train, eval_set=[(x_test, y_test)])
print("grid_cv 최적 파라미터: ", grid_cv.best_params_)
# grid_cv 최적 파라미터:  {'colsample_bytree': 0.75, 'max_depth': 5, 'min_child_weight': 3}
xgb_roc_score = roc_auc_score(y_test, grid_cv.predict_proba(x_test)[:,1], average='macro')
# macro평균과 micro 평균의 개념정리필요
# 매크로는 클래스별 점수를 동등하게 평균내어 작은 클래스 성능을 중요시할 때(?)
# 마이크로는 전체 데이터의 개별 정답률을 기반으로 하여 데이터 불균형이 심할 때 사용
print(f'xgb_roc_score: {xgb_roc_score:.5f}')
# xgb_roc_score: 0.83825

# 위 파라미터로 모델 생성
print()
xgb_clf2 = XGBClassifier(n_estimator=5, random_state=12,
                        max_depth=5, min_child_weight=3, colsample_bytree=0.75)
xgb_clf2.fit(x_train, y_train, eval_set=[(x_train, y_train), (x_test, y_test)])
xgb_roc_score2 = roc_auc_score(y_test, xgb_clf2.predict_proba(x_test)[:,1])
print(f"xgb_roc_score2: {xgb_roc_score2:.5f}")
# xgb_roc_score2: 0.83783

pred2 = xgb_clf2.predict(x_test)    
print("예측값: ", pred2[:5])
print("실제값: ", y_test[:5].values)
# 예측값:  [0 0 0 0 0]
# 실제값:  [0 0 0 0 0]
from sklearn import metrics
print("분류 정확도: ", metrics.accuracy_score(y_test, pred2))    # 변수넣는거 아직도 잘 모르겠네
# 분류 정확도:  0.9575769534333071

# 중요 피처 시각화
fig, ax = plt.subplots(1,1, figsize=(10,8))
plot_importance(xgb_clf2, ax=ax, max_num_feature=20)
plt.show()







