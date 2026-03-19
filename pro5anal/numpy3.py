#numpy3.py

# 배열에 행, 열 추가

import numpy as np

aa = np.eye(3)
print(aa)

bb = np.c_[aa, aa[2]]       # 2열과 동일한 열 추가
print(bb)

cc = np.r_[aa, [aa[2]]]
print(cc)


print('--append, insert, delete ---')
a = np.array([1,2,3])
print(a)
b = np.append(a, [4,5])
b = np.append(a, [4,5], axis=0) # 위와 동일표현. 근데 행 기준? 
print(b)

c = np.insert(a,0,[6,7])        # 0번째에 [6,7] 삽입
print(c)

d = np.delete(a,1)              # 1번째 성분 삭제
print(d)

print()
aa = np.arange(1,10).reshape(3,3)
print()
print(aa)
print()
print(np.insert(aa,1,99))               # axis를 안넣어주면 차원이 축소되고
print()
print(np.insert(aa,1,99, axis=0))       # 넣어주면 차원이 늘어나? 유지된다?
print(np.insert(aa,1,99, axis=1))       # axis=1 -> 열 기준 insert

print()
# 조건 연산 where(조건, 참, 거짓)
print('조건 연산 where(조건, 참, 거짓)')

x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
result = np.where(conditionData, x, y)      # 참이면 x, 거짓이면 y 출력
print(result)                               # [1 5 3]으로 나오는게 참거짓참이어서 x[0]y[1]x[2]로 나오는거같은데 정확한 설명필요

print()
aa = np.where(x>=2)
print(aa)           # (array([1,2]),) 인덱스
print(a[aa])
print()

# 배열 결합
print('배열 결합')
kbs = np.concatenate([x,y])
print(kbs)

# 배열 분할
print('배열 분할')
mbc, sbs = np.split(kbs,2)
print(mbc)
print(sbs)

print()
# 배열 좌우 분할

a = np.arange(1,17).reshape(4,4)
print(a)
print('배열 좌우 분할')
x1, x2 = np.hsplit(a,2)
print(x1)
print(x2)
print('배열 상하 분할')
x1, x2 = np.vsplit(a,2)
print(x1)
print(x2)

print('\n표본 추출(sampling) - 복원, 비복원')
li = np.array([1,2,3,4,5,6,7])
print(li)
print()
# 복원 추출
print("복원 추출")
for _ in range(5):
    print(li[np.random.randint(0,len(li) - 1)], end = ' ')

print()
print("비복원 추출")
# 비복원 추출
import random
print(random.sample(li.tolist(),5))   # random.sample() 함수는 List type 대상

print()
# choice
print(np.random.choice(range(1,46), 6))
print(np.random.choice(range(1,46), 6, replace=True))   # 복원
print(np.random.choice(range(1,46), 6, replace=False))  # 비복원



