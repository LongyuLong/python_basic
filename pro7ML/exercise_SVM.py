
# [SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습

# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 
# 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 
# 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.     
# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ

# feature 칼럼 : 문자 데이터 칼럼은 제외
# label 칼럼 : AHD(중증 심장질환)

# 데이터 예)
# "","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
# "1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
# "2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"
# ...

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Heart.csv")
print(df)

# 1. 전처리: 첫 번째 의미 없는 인덱스 컬럼 삭제 및 결측치 제거
df = df.drop(df.columns[0], axis=1)
df = df.dropna() # Ca, Thal 등 결측치가 있는 행 제거

# 2. Feature, Label 분리(문자 데이터 컬럼 vs. AHD)
features = df.drop(['ChestPain', 'Thal', 'AHD'], axis=1)
label = df['AHD'].map({"Yes":0, "No":1})

print(features)
print(label)

# 3. 데이터 분할 (Train/Test)
train_x, test_x, train_y, test_y = train_test_split(
    features, label, test_size=0.3, random_state=42
)

# 4. 정규화 - 스케일러 사용해서
scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.transform(test_x)       # 왜 얘는 fit_transform이 아닌가?

# 5. SVM 모델 생성 및 학습
model = svm.SVC(C=1, kernel='rbf').fit(train_x, train_y)
print(model)

# 예측값, 실제값 확인
pred = model.predict(test_x)
print("예측값: ", pred[:5])
print("실제값: ", test_y[:5].values)
# 예측값:  [1 1 1 1 1]
# 실제값:  [1 0 1 0 1]

# 정확도 확인
score = metrics.accuracy_score(test_y, pred)
print("accuracy score: ", round(score,2))
# accuracy score:  0.54

cross_vali = model_selection.cross_val_score(model, features, label, cv=3)
print("3회 각각의 정확도: ", cross_vali)
print("평균 정확도: ", cross_vali.mean())
# 3회 각각의 정확도:  [0.54545455 0.53535354 0.53535354]
# 평균 정확도:  0.5387205387205388

new_data = features.iloc[[0]].copy()
print(new_data)
#    Age  Sex  RestBP  Chol  Fbs  RestECG  MaxHR  ExAng  Oldpeak  Slope   Ca
# 0   63    1     145   233    1        2    150      0      2.3      3  0.0
# >> 근데 이건 카피해온거니까 내용은 지워야니까 아래와 같이
new_data.iloc[0] = [55, 1, 140, 250, 0, 1, 155, 0, 1.5, 2, 0.0]
#    Age  Sex  RestBP  Chol  Fbs  RestECG  MaxHR  ExAng  Oldpeak  Slope   Ca
# 0   55    1     140   250    0        1    155      0      1.5      2  0.0
new_data_scaled = scaler.transform(new_data) # 학습 시 사용한 scaler로 변환
print(new_data_scaled)
# [[ 0.06026491  0.66143783  0.50030113  0.01770401 -0.43549417 -0.09262894
#    0.28542319 -0.72253638  0.43081583  0.6487686  -0.73240456]]
new_pred = model.predict(new_data_scaled)
print("새로운 값 예측 결과: ", new_pred)
# 새로운 값 예측 결과:  [1]


# 어떤 feature를 가지고 scatterplot 을 그릴건지 결정하기
# seaborn 사용
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier # RF 임포트

plot_df = pd.concat([features, label], axis=1)

# 1. 상관계수 기반 근거 (방법 1)
corr_val = plot_df.corr()['AHD'].abs().drop('AHD')

# 2. Random Forest 기반 변수 중요도 근거 (방법 3)
# RF 모델을 생성하여 데이터의 비선형적 기여도를 계산합니다.
rf = RandomForestClassifier(random_state=42)
rf.fit(features, label) 
rf_val = pd.Series(rf.feature_importances_, index=features.columns)

# 3. 두 수치를 결합하여 '종합 점수' 생성
summary = pd.DataFrame({'Correlation': corr_val, 'Importance': rf_val})
summary['Total_Score'] = summary['Correlation'] + summary['Importance']

# 종합 점수 기준 내림차순 정렬
summary_sorted = summary.sort_values(by='Total_Score', ascending=False)
print("--- 변수별 중요도 수치 근거 ---")
print(summary_sorted)

# 4. 상위 4개 변수만 추출하여 시각화 (합리적 선택)
top_4_features = summary_sorted.index[:4].tolist()
print(f"\n합리적으로 선택된 상위 변수: {top_4_features}")

# 5. 시각화 (선택된 변수만 pairplot)
sns.pairplot(plot_df[top_4_features + ['AHD']], hue='AHD', palette='RdBu', diag_kind='kde')
plt.show()


# -------------------------------------다른풀이
# import pandas as pd
# import numpy as np
# from sklearn import svm,metrics
# from sklearn.model_selection import train_test_split

# ''' 흉부외과 환자 303명을 관찰한 데이터다. 

# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 

# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 

# 임의의 값을 넣어 분류 결과를 확인하시오.     

# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ
# feature 칼럼 : 문자 데이터 칼럼은 제외

# label 칼럼 : AHD(중증 심장질환)'''

# df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Heart.csv')
# print(df.head(2))
# print(df.info())
# # "","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"



# # 칼럼 feature랑 label이랑 분리
# label = df.AHD
# feat=df.iloc[:,1:-1]
# # print(feat.head(2))
# # print(feat.shape)
# # print(label.shape)

# # pd.set_option('display.max_columns', None)  # 모든 컬럼 표시
# # pd.set_option('display.width', None)        # 너비 제한 해제
# # pd.set_option('display.max_colwidth', None) # 긴 값도 잘리지 않음

# # des=df.describe()
# # print(df['ChestPain'].unique())
# # print(df['Thal'].unique())

# feat.drop('ChestPain',axis=1,inplace=True)
# feat.drop('Thal',axis=1,inplace=True)
# print(feat.shape)

# print(label.unique())
# label=label.map({'No':0,'Yes':1})
# print(label.unique())


# # 정규화

# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# feat=scaler.fit_transform(feat)
# # print(pd.DataFrame(feat).describe())

# na= pd.DataFrame(feat)
# print(na.isna().sum())
# # Ca결측치 4개


# feat= pd.DataFrame(feat)
# feat.iloc[:,10]=feat.iloc[:,10].fillna(feat.iloc[:,10].mean())
# print(feat.isna().sum())


# # 데이터 나누기
# x_train,x_test,y_train,y_test=train_test_split(feat,label,test_size=0.2,random_state=12)
# print(x_train.shape, x_test.shape)


# smodel=svm.SVC(C=0.01, kernel='rbf').fit(x_train,y_train) 
# pred=smodel.predict(x_test)

# print('실제: ',y_test[:5])
# print('예측: ',pred[:5])

# score=metrics.accuracy_score(y_test,pred)
# print(f'총 갯수:{len(y_test)}, 오류수:{(y_test != pred).sum()}')

# print(f'분류 정확도 확인 :{score}')


"""
############ 이론 공부 ###################

특성공학기법: 좋은 성능을 내기 위해 입력 자료를 변형하거나 가공하는 방법
- 차원축소
1. feature selection: 변수선택
2. feature extraction: 차원축소(주성분분석-PCA)

- Scaling(정규화, 표준화)
- Transform(변형)
1. Binning(비닝): 연속적 자료를 구간으로 분류(연속형 -> 범주형)
2. Dummy: 범주형을 연속형으로 변환

- Feature Creation: 특성 생성


"""