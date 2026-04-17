# 계층적 군집분석
# 학생 10명의 시험점수 사용

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

students = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']
scores = np.array([76,95,65,85,60,92,55,88,83,72]).reshape(-1,1)
print("점수: ", scores)

linked = linkage(scores, method='ward')

# 시각화
plt.figure(figsize=(10,6))
dendrogram(linked, labels=students)
plt.title("student score")
plt.xlabel("students")
plt.axhline(y=25, color='red', linestyle="--",label='cut at 25')
plt.ylabel('distance')
plt.legend()
plt.grid(True)
plt.show()

# 군집 3개로 나누기
clusters = fcluster(linked, t=3, criterion='maxclust')
print("학생 자료 군집 결과")
for stu, cluster in zip(students, clusters):
    print(f"{stu}: cluster {cluster}")

# 군집별로 점수와 이름 확인
cluster_info = {}
for student, cluster, score in zip(students, clusters, scores.flatten()):
    if cluster not in cluster_info:          # ?
        cluster_info[cluster] = {"students":[], "scores":[]}      # 클러스터 인포에 등록한다 생각하면 이해됨
    cluster_info[cluster]["students"].append(student)
    cluster_info[cluster]["scores"].append(score)

print(cluster_info)
#  {np.int32(2): {'students': ['s1', 's10'], 'scores': [np.int64(76), np.int64(72)]}, 
#   np.int32(1): {'students': ['s2', 's4', 's6', 's8', 's9'], 'scores': [np.int64(95), np.int64(85), np.int64(92), np.int64(88), np.int64(83)]}, np.int32(3): {'students': ['s3', 's5', 's7'], 'scores': [np.int64(65), np.int64(60), np.int64(55)]}}


# 군집별로 평균 점수와 이름 확인
print('---- 군집별 평균 점수와 이름 확인 ----')
for cluster_id, info in sorted(cluster_info.items()):
    avg_score = np.mean(info["scores"])
    student_list = ", ".join(info["students"])  # 표현식 유의. 설명 보충필요
    print(f"cluster {cluster_id}: 평균 점수={avg_score:.2f}, 학생={student_list}")

# ---- 군집별 평균 점수와 이름 확인 ----
# cluster 1: 평균 점수=88.60, 학생=s2, s4, s6, s8, s9
# cluster 2: 평균 점수=74.00, 학생=s1, s10
# cluster 3: 평균 점수=60.00, 학생=s3, s5, s7

#
# 군집별 Scatter plot
x_positions = np.arange(len(students))
y_scores = scores.ravel()                   # ravel?
colors = {1:'red', 2:'blue', 3:'green'}
plt.figure(figsize=(10,6))

for i, (x,y,cluster) in enumerate(zip(x_positions, y_scores, clusters)):
    plt.scatter(x,y,color=colors[cluster], s=100)
    plt.text(x,y + 1.5, students[i], fontsize=12, ha="center")
plt.xticks(x_positions, students)
plt.xlabel("students")
plt.ylabel("scores")
plt.title("score cluster")
plt.grid(True)
plt.show()
# 성적 그룹 분석, 고객 등급분류, 사용자 행동 패턴등을 군집화할 수 있다.




