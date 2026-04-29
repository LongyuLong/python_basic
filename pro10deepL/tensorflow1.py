import tensorflow as tf

print(tf.__version__)   # 2.21.0
print("즉시 실행 모드: ", tf.executing_eagerly())   # True
print("GPU 사용 정보: ", tf.config.list_physical_devices("GPU"))

print("\nTensor: 텐서 플로우에서 데이터를 담는 기본 자료 구조")
# ndarray와 유사하지만 텐서플로에서 연산에 사용되도록 만들어진 객체

print(12, type(12))             # 파이썬 상수로 파이썬이 직접 계산
# 12 <class 'int'>
print(tf.constant(12))          # 0d 텐서(scalar)
# tf.Tensor(12, shape=(), dtype=int32)
print(tf.constant([12]))        # 1d 텐서(vector)
# tf.Tensor([12], shape=(1,), dtype=int32)
print(tf.constant([[12]]))      # 2d 텐서(matrix)
# tf.Tensor([[12]], shape=(1, 1), dtype=int32)
print(tf.constant([[12,1]]))
# tf.Tensor([[12  1]], shape=(1, 2), dtype=int32)
print(tf.rank(tf.constant([[12,1]])))
# tf.Tensor(2, shape=(), dtype=int32)   2차원?

tf.print(tf.constant(12))
# 텐서플로우 전용 출력함수

print()
import numpy as np
imsi = np.array([1, 2])     # 일반 수치 연산(CPU 연산이 기본, 자동 미분 불가)
a = tf.constant([1, 2])     # 딥러닝 연산(GPU 연산 가능, )
b = tf.constant([3, 4])
c = a + b # 텐서 요소값 더하기(열단위 연산)
tf.print(c)     # [4 6]

d = tf.constant([3])
e = c + d
tf.print(e)     # [7 9] Broadcast 연산

print("\nNumpy와 tensorslow 형변환 가능")
print(7)    # 7
print(tf.convert_to_tensor(7))  # tf.Tensor(7, shape=(), dtype=int32)
print(tf.constant(7).numpy())   # 7

arr = np.array([1, 2])  # ndarray type
tfarr = tf.add(arr, 5)  # 텐서 연산하면 텐서 타입으로 자동 형변환됨
print(tfarr)            # tf.Tensor([6 7], shape=(2,), dtype=int64)
print(np.add(tfarr, 2)) # [8 9]

print("\n---- 텐서플로 변수 선언 후 사용하기 ----")
# tf.Variable(): 텐서플로에서 값이 바뀔 수 있는 텐서를 만들 때 사용.
# ex. weight, bias ...
v1 = tf.Variable(1.0)
tf.print("v1: ", v1)
v2 = tf.Variable(tf.ones(2, ))     # 1으로 채워진 변수
tf.print("v2: ", v2)
v3 = tf.Variable(tf.zeros(2, ))    # 0으로 
tf.print("v3: ", v3)
# print의 출력
# v1:  <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>
# v2:  <tf.Variable 'Variable:0' shape=(2,) dtype=float32, numpy=array([1., 1.], dtype=float32)>
# v3:  <tf.Variable 'Variable:0' shape=(2,) dtype=float32, numpy=array([0., 0.], dtype=float32)>

# tf.print의 출력
# v1:  1
# v2:  [1 1]
# v3:  [0 0]

v1.assign(123)
tf.print("assigned v1: ", v1)     # 123
v2.assign([30, 40])
tf.print("assigned v2: ", v2)     # 123
print()

aa = tf.Variable(tf.zeros((2,1))) # 2행 1열에 모두 1을 기억
tf.print("aa: ", aa)        # aa:  [[0] [0]]

aa.assign(tf.ones((2,1)))   
tf.print("aa: ", aa)        # aa:  [[1] [1]]

aa.assign_add([[2], [3]])   # 더하기 치환
tf.print("aa: ", aa)        # aa:  [[3] [4]]

aa.assign_sub([[2], [3]])   # 빼기 치환
tf.print("aa: ", aa)        # aa:  [[1] [1]]

aa.assign(aa * [[2], [3]])# 곱하기 치환
tf.print("aa: ", aa)        # aa:  [[2] [3]]

aa.assign(aa / [[2], [3]])# 나누기 치환
tf.print("aa: ", aa)        # aa:  [[1] [1]]

print("\n난수 처리")
tf.print(tf.random.uniform([1], 0, 1)) # 균등 분포 난수 ([shape], 최소, 최대) 순
tf.print(tf.random.normal([3], 0, 1)) # 균등 분포 난수 ([shape], 최소, 표준편차) 순
tf.print(tf.random.normal([3], mean=0, stddev=1))   
# [-0.545560718 -0.251950055 -0.945179403]








