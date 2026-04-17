# sklearn 제공 regressor 성능 비교
# pipeline + GridSearchCV + 교차검증 + 성능확인 + 시각화

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.datasets import load_diabetes  # 당뇨병데이터
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR     # Support Vector Regressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error

data = load_diabetes()

x = data.data
y = data.target
print(x[:2])
# [[ 0.03807591  0.05068012  0.06169621  0.02187239 -0.0442235  -0.03482076
#   -0.04340085 -0.00259226  0.01990749 -0.01764613]
#  [-0.00188202 -0.04464164 -0.05147406 -0.02632753 -0.00844872 -0.01916334
#    0.07441156 -0.03949338 -0.06833155 -0.09220405]]
print(y[:2])
# [151.  75.]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Pipeline + GridSearch
models = {
    "LinearRegression":{
        "pipeline":Pipeline([
            ("scaler", StandardScaler()),
            ("model", LinearRegression())
        ]),
        "params":{
            "model__fit_intercept":[True,False]
        }
    },
        "RandomForest":{
        "pipeline":Pipeline([
            ("model", RandomForestRegressor(random_state=42))
        ]),
        "params":{
            "model__n_estimators":[100, 200],
            "model__max_depth":[None, 5, 10],
            "model__min_samples_split":[2, 5]
        }
    },
        "XGBoost":{
        "pipeline":Pipeline([
            ("model", XGBRegressor(random_state=42, verbosity=0))   # verbosity ??
        ]),
        "params":{
            "model__n_estimators":[100, 200],
            "model__learning_rate":[0.01, 0.05],
            "model__min_samples_split":[3, 5]
        }
    },
        "SVR":{
        "pipeline":Pipeline([
            ("scaler", StandardScaler()),
            ("model", SVR())
        ]),
        "params":{
            "model__C":[0.1, 1, 10],
            "model__gamma":["scale", "auto"],
            "model__kernel":["rbf"]
        }
    },
            "KNN":{
        "pipeline":Pipeline([
            ("scaler", StandardScaler()),
            ("model", KNeighborsRegressor())
        ]),
        "params":{
            "model__n_neighbors":[3, 5, 7],
            "model__weights":["uniform", "distance"]
            }
    }
}

# GridSearchCV 실행
results = []
best_models = {}    
# dict로 잡아줘야 아래에서 best_models[name] = best_model 실행했을 때 Type Error 안뜬다


# 각 모델을 순서대로 반복 처리: Best모델 추출, 성능 저장
for name, config in models.items():
    print(f"{name} 튜닝 중 ..")
    grid = GridSearchCV(
        config["pipeline"],
        config["params"],
        cv = 5,
        scoring="r2",
        n_jobs=-1
    )
    grid.fit(x_train, y_train)
    
    best_model = grid.best_estimator_
    pred = best_model.predict(x_test)

    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)
    results.append([name, rmse, r2])

    best_models[name] = best_model
    print("Best params: ", grid.best_params_)
    print("r2 score: ", r2) # 설명력

# 최종 결과 DataFrame에 저장
df_results = pd.DataFrame(results, columns=["modelname", "rmse", "r2"])
df_results = df_results.sort_values("r2", ascending=False)
print("최종 성능 비교")
print(df_results)
# 최종 성능 비교
#                name       rmse        r2
# 3               SVR  51.791775  0.493713
# 1      RandomForest  53.482640  0.460115
# 0  LinearRegression  53.853446  0.452603
# 4               KNN  54.244609  0.444622
# 2           XGBoost  57.961648  0.365901

# 성능 비교를 위한 시각화
plt.figure(figsize=(12,5))

# R2
plt.subplot(1,2,1)
sns.barplot(x="modelname", y="r2", data=df_results)
plt.title("튜닝 모델 결정계수")
plt.xticks(rotation=30)
# RMSE
plt.subplot(1,2,2)
sns.barplot(x="modelname", y="rmse", data=df_results)
plt.title("튜닝 모델 RMSE")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Best model 예측 시각화
# 최고 모델 선택
best_modelname = df_results.iloc[0]["modelname"]
best_model = best_models[best_modelname]
pred = best_model.predict(x_test)

plt.figure(figsize=(6,6))
plt.scatter(y_test, pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title(f"최고 모델: {best_modelname}")
plt.xlabel("실제값")
plt.ylabel("예측값")
plt.show()




