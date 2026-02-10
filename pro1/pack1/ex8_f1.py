# function: 여러개의 수행문을 하나의 이름으로 묶은 실행 단위
# 함수 고유의 실행 공간을 갖음
# 자원의 재활용

#내장함수 일부체험

# # sum - 합
# print(sum({1,2,3}))

# # bin - 이진화
# print(bin(8))

# # eval - 문자열 수식 계산
# print(eval('4+5'))

# round - 반올림
# math.ceil 은 올림, math.floor 는 내림 << import math 이후 사용해야함

# b_list = [True, 1, False]
# print(all(b_list)) # ??
# print(any(b_list)) # ?

data1 = [10, 20, 30]
data2 = ['a','b']
for i in zip(data1,data2):
    print(i)




