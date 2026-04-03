# 공분산과 상관계수
# 변수가 하나인 경우, 분산은 거리와 관련이 있다.
# 변수가 두개인 경우, 분산은 방향을 가진다.

import numpy as np
                                                    # 2번째 변수(배열)의 거동
print(np.cov(np.arange(1,6), np.arange(2,7)))       # 우상향
# [[2.5 2.5]
#  [2.5 2.5]]
print()
print(np.cov(np.arange(10,60,10), np.arange(2,7)))
# [[250.   25. ]
#  [ 25.    2.5]]
print()
print(np.cov(np.arange(100,600,100), np.arange(2,7)))
# [[2.5e+04 2.5e+02]
#  [2.5e+02 2.5e+00]]
print()
print(np.cov(np.arange(1,6), (3,3,3,3,3)))          # 상수함수(y=3)으로 변화없음
# [[2.5 0. ]
#  [0.  0. ]]
print()
print(np.cov(np.arange(1,6), np.arange(6,1,-1)))    # 우하향
# [[ 2.5 -2.5]
#  [-2.5  2.5]]

print()

x = [8,3,6,6,9,4,3,9,3,4]
print('x 평균: ', np.mean(x))
print('x 분산: ', np.var(x))
# x 평균:  5.5
# x 분산:  5.45
print()
y = [6,2,4,6,9,5,1,8,4,5]
print('y 평균: ', np.mean(y))
print('y 분산: ', np.var(y))
# y 평균:  5.0
# y 분산:  5.4

import matplotlib.pyplot as plt
# plt.plot(x,y,'o')
# plt.show()
# 우상향 개형 확인했음
print()
print("x,y의 공분산: ", np.cov(x,y))
# x,y의 공분산:  [[6.05555556 5.22222222] [5.22222222 6.        ]]
#             >> 5.22222 ---이게 결론?
print()

x2 = [80,30,60,60,90,40,30,90,30,40]
y2 = [60,20,40,60,90,50,10,80,40,50]
print('x2 평균: ', np.mean(x2))
print('x2 분산: ', np.var(x2))
# x2 평균:  55.0
# x2 분산:  545.0
print()
print('y2 평균: ', np.mean(y2))
print('y2 분산: ', np.var(y2))
# y2 평균:  50.0
# y2 분산:  540.0
print()
print("x2,y2의 공분산: ", np.cov(x2,y2))
# x2,y2의 공분산:  [[605.55555556 522.22222222]
#  [522.22222222 600.        ]]
print()
# plt.plot(x2,y2,'o')
# plt.show()
# x,y의 개형과 동일함을 확인
print()

# 두 데이터의 단위에 따라 공분산의 패턴이 일치하더라도, 공분산의 크기가 달라지므로
# 절대적 크기 판단이 어려움(의미 없음 이라고 해야되는거 아닌가?)
# 공분산을 표준화해서 -1 ~ 1 사이 구간으로 만들어 준 것이 상관계수 r 이다

print("x,y의 상관계수 r: ", np.corrcoef(x,y))
print()
print("x,y의 상관계수 r: ", np.corrcoef(x,y)[0, 1])
# x,y의 상관계수 r:  0.8663686463212855
print()
print("x2,y2의 상관계수 r: ", np.corrcoef(x2,y2)[0, 1])
# x2,y2의 상관계수 r:  0.8663686463212852
print()

m = [-3,-2,-1,0,1,2,3]
n = [9,4,1,0,1,4,9]
print(np.cov(m,n)[0,1])         # 0.0
print(np.corrcoef(m,n)[0,1])    # 0.0    
# 비선형 데이터의 경우 공분산, 상관계수는 의미
plt.plot(m,n,'o')
plt.show()





