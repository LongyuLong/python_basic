# tf.constant(), tf.Variable(), autograph 기능

import tensorflow as tf
import numpy as np

node1 = tf.constant(3, dtype=tf.float32)
node2 = tf.constant(4.0)
print(node1)    # tf.Tensor(3.0, shape=(), dtype=float32)
print(node2)    # tf.Tensor(4.0, shape=(), dtype=float32)

adddata = tf.add(node1, node2)
print("adddata: ", adddata) 
# adddata:  tf.Tensor(7.0, shape=(), dtype=float32)

print()
node3 = tf.Variable(3, dtype=tf.float32)
node4 = tf.Variable(4.0)
print(node3)    # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=3.0>
print(node4)    # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=4.0>

imsi1 = tf.add(node3, node4)
print("imsi1(tf.add(node3, node4)): ", imsi1)
# imsi1(tf.add(node3, node4)):  tf.Tensor(7.0, shape=(), dtype=float32)

node4.assign_add(node3)     # 변수값에 더하기 후 치환
print(node4)    # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=7.0>

print()
a = tf.constant(5)
b = tf.constant(10)
# 조건 처리(tf.cond(조건, 함수1, 함수2))
result = tf.cond(a < b, lambda:tf.add(10,a), lambda:tf.square(a))
# result = tf.cond(a < b, tf.add(10,a), tf.square(a)) # 에러뜸
print("result: ", result)   # tf.Tensor(15, shape=(), dtype=int32)

# autograph 기능: 파이썬 코드를 텐서플로우 그래프(Graph) 코드로 자동변환
# 텐서플로우의 두가지 실행방법
# 1) Eager Execution: 파이썬 코드처럼 즉시 실행(기본)
# 2) Graph Execution: 별도 운영이 가능한 계산 그래프를 만들어 최적화 후 실행(텐서 처리에 효율적)

@tf.function    # Autograph가 개입함(텐서플로우 그래프 연산)
def calcFunc1(a,b): # 위 tf.cond()를 Autograph 사용한경우(?)
    if (a<b):
        return tf.add(10, a)
    else:
        return tf.square(a)
    
result2 = calcFunc1(a,b)
print("result2: ", result2)

# 참고:
# @tf.function 안에서 if, for, while, break, continue, return 등을 사용하면 Autograph가 관여


print("\n-- 반복문 처리 --")

@tf.function
def calcFunc2(n):
    hap = tf.constant(0)
    for i in tf.range(n):
        hap += i
    return hap

print("hap: ", calcFunc2(5))
# hap:  tf.Tensor(10, shape=(), dtype=int32)

print()
imsi = tf.constant(0)
su = tf.Variable(1)         # tf 변수는 @tf.function 밖에서 선언해야만함.

@tf.function
def calcFunc3():
    # imsi = tf.constant(0)
    global imsi # imsi << 로컬변수 아닌 글로벌
    # su = tf.Variable(1) << 에러발생 - Autograph에서는 구조가 고정적이어야한다.
    for _ in range(3):
        # imsi = imsi + su << 파이썬 연산자
        imsi = tf.add(imsi, su) # << 권장

    return imsi

print("imsi: ", calcFunc3())
# imsi:  tf.Tensor(3, shape=(), dtype=int32)

print("\n구구단 3단출력")
@tf.function
def calcFunc4(dan):
    for i in range(1,10):
        result = tf.multiply(dan, i)
        
        tf.print(dan, "*", i, "=", result)

calcFunc4(3)


