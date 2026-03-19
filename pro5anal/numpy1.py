# numpy1.py
# numpy의 ndarray는 단순한 배열이라기보다,
# 벡터/행렬 연산도 가능한 다차원 수치 데이터 구조다

import numpy as np

ss = ['tom', 'james', 'oscar', 1, True]
print(ss, ' ', type(ss))

ss2 = np.array(ss)
print(ss2, ' ', type(ss2))      # ndarray는 동일 타입만 취급한다면 문자열 숫자 불리언 저건?

li = list(range(1,10))
print(li)
print(li[0], ' ',id(li[0]))
#print(li*10)                    # li 값에 10을 곱한게 아니고 li 10개

for i in li:                    # 빅데이터에서 for문쓰면 느리다. 그럼?
    print(i*10, end = ' ')
print()
num_arr = np.array(li)
print(num_arr[0], ' ', num_arr[1],' ',id(num_arr[0]), id(num_arr[1]))
print(num_arr*10)               # 이건 10이곱해진다. python과 왜다른지 정리. 유연성은 떨어지나 좋다? 벡터화 연산이 가능하다.

print()
a = np.array([1,2,3.5], dtype='float32')
print(a, type(a))               # ndarray는 동일 타입만 취급
# 여러 타입의 자료가 입력되면 상위 타입으로 자동 변환. int -> float -> complex -> str

print("b = np.array([[1,2,3],[4,5,6]])")
b = np.array([[1,2,3],[4,5,6]])
print(b, b.shape, ' ', b[0, 0],' ', b[[0]])

print()
c = np.zeros((2,2))
print(c)
d = np.ones((2,2))
print(d)
e = np.eye(3)                   # 단위행렬
print(e)

print()
print(np.random.rand(5))        # 균등 분포?
print(np.random.randn(5))       # 정규 분포

np.random.seed(0)
print(np.random.randn(2,3))

print(list(range(0,10)))
print(np.arange(10))

print()
# 인덱싱/슬라이싱
a = np.array([1,2,3,4,5])
print(a, ' ', a[1])
print(a[1:4])
print(a[1:])
print(a[1:5:2])                 # a:b:c -> a부터 b까지 c 간격으로
print(a[-2:])
b = a
print(a[0], ' ', b[0])
b[0]=88
print(a[0], ' ', b[0])
c = np.copy(a)                  # 복사본 생성
print(a[0], ' ', c[0])
b[0]=33
print(a[0], ' ', c[0])          # 여기서만 33이 출력된다 근데왜





