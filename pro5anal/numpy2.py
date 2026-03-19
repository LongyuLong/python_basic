# numpy2.py

# 배열연산
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float32)
# # x = np.array([[1.,2],[3,4]]) 하나라도 float이 들어가면(1.) 모두 float 된다.
# print(x, ' ', x.dtype)

# y = np.arange(5,9).reshape((2,2))       # 구조변경 1차원 -> 2차원~
# print(y)

# print()
# print(x + y)                    # 파이썬 연산자 - 느림
# print(np.add(x,y))              # 넘파이 함수(유니버셜 함수) - 빠름

# print(x-y)
# print(np.subtract(x,y))

# print(x*y)
# print(np.multiply(x,y))

# print(x/y)
# print(np.divide(x,y))

# print('\ndot은 numpy모듈의 함수나 배열객체의 인스턴트 메소드로 사용 가능')
# v = np.array([9,10])
# w = np.array([11,12])
# print(v*w)                      # 요소별 곱셈 9*11, 10*11

# # 벡터의 내적(행렬곱)
# print(v.dot(w))                 # 내적의결과는 스칼라
# print(np.dot(v,w))              # 9*11 + 10*12

print()
# 배열 계산 함수
print(x)
print(np.mean(x), ' ', np.var(x))
print(np.max(x), ' ', np.min(x))
print(np.argmax(x), ' ', np.argmin(x))  # index 반환
print(np.cumsum(x))                     # 누적 합
print(np.cumprod(x))                    # 누적 곱

print()
names1 = np.array(['tom', 'james', 'tom', 'oscar'])
names2 = np.array(['tom', 'page', 'john'])

print(np.unique(names1))                # 중복 제거
print(np.intersect1d(names1,names2))    # 교집합
print(np.intersect1d(names1,names2, assume_unique=True))    # 교집합 + 중복허용
print(np.union1d(names1,names2))        # 합집합 - 중복도 제거

print('\n전치(Transpose)')
print(x)
print(x.T)
print(x.transpose())
print(x.swapaxes(0,1))

print('\nBroadcasting: 크기가 다른 배열간의 연산 - 작은 배열을 여러번 반복해 큰 배열과 연산')
x = np.arange(1,10).reshape(3,3)
y = np.array([1,0,1])
print(x)
print(y)
# 두 배열의 차원이 다르지만 numpy가 연산을 가능하게 만든다
# 근데 어떻게?

print(x+y)

np.savetxt("my.txt",x)


