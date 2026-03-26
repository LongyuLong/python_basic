# numpy_exercise.py
import numpy as np
# Q1) 브로드캐스팅과 조건 연산
# 다음 두 배열이 있을 때,
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
# 두 배열을 브로드캐스팅하여 곱한 결과를 출력하시오.
print("--------- Q1 ---------")
# 그 결과에서 값이 30 이상인 요소만 골라 출력하시오.
c = a*b
print(type(np.where(c>=30)))        # 튜플 반환
print(np.where(c>=30))              # 배열 2개를 요소로 가진 튜플
print()
result = (np.where(c>=30))          # c가 30 이상인 인덱스 정보
print(result[0], result[1])
print(c[result[0], result[1]])      # Fancy indexing 개념?

# Q2) 다차원 배열 슬라이싱 및 재배열
#  - 3×4 크기의 배열을 만들고 (reshape 사용),  
#  - 2번째 행 전체 출력
#  - 1번째 열 전체 출력
#  - 배열을 (4, 3) 형태로 reshape
#  - reshape한 배열을 flatten() 함수를 사용하여 1차원 배열로 만들기
print()
print("--------- Q2 ---------")
a = np.array(range(1,13)).reshape(3,4)
print(a)
print()
print(a[1,:])       # 2번째 행 전체 출력
print()
print(a[:,0])       # 1번째 열 전체 출력
b = a.reshape(4,3)
print(b)
b = b.flatten()
print(b)

# Q3) 1부터 100까지의 수로 구성된 배열에서 3의 배수이면서 5의 배수가 아닌 값만 추출하시오.
# 그런 값들을 모두 제곱한 배열을 만들고 출력하시오.
print()
print("--------- Q3 ---------")
a = np.array(range(1,101))
print(a)
print()
b = np.where((a%3 == 0) & (a%5 != 0))
print(a[b[0]])

for i in range(len(b)):
    c = a[b[i]]**2

print(c)

# Q4) 다음과 같은 배열이 있다고 할 때,
arr = np.array([15, 22, 8, 19, 31, 4])
# 값이 10 이상이면 'High', 그렇지 않으면 'Low'라는 문자열 배열로 변환하시오.
# 값이 20 이상인 요소만 -1로 바꾼 새로운 배열을 만들어 출력하시오. (원본은 유지)
# 힌트: np.where(), np.copy()
print()
print("--------- Q4 ---------")
# np.where(arr >= 10, 'High', 'Low') 로 푸는게 더 합리적?
High_index = np.where(arr>=10)
High = arr[High_index[0]]
print(High)
Low_index = np.where(arr<10)
Low = arr[Low_index[0]]
print(Low)

New_index = np.where(arr>=20)
New = np.copy(arr)
New[New_index] = -1
print(New)


# Q5) 정규분포(평균 50, 표준편차 10)를 따르는 난수 1000개를 만들고, 상위 5% 값만 출력하세요.
# 힌트 :  np.random.normal(), np.percentile()
print()
print("--------- Q5 정규분포(평균 50, 표준편차 10)를 따르는 난수 1000개를 만들고, 상위 5% 값만 출력하세요. ---------")
arr = np.random.normal(50,10,1000)
five = np.percentile(arr,95)
print("상위 5% 값: ",five)