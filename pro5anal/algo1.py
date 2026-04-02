# 알고리즘(Algorithm) 요약:
# 정의: 문제 해결이나 특정 목표를 달성하기 위한 단계별 절차나 규칙의 집합.
# 핵심 역할: 입력(Input)을 받아 정해진 로직을 거쳐 결과(Output)를 도출하는 '레시피' 역할.
# 성립 조건:
# 입력/출력: 0개 이상의 입력과 1개 이상의 출력 존재.
# 명확성: 각 단계는 모호하지 않고 실행 가능해야 함.
# 유한성: 반드시 작업이 끝나고 종료되어야 함.
# 효율성: 시간과 메모리를 최소한으로 사용해야 함.

# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += s+i

    return s

# print(sum_n(10))
# print(sum_n(100))

print('가우스의 합 공식 사용한 1 ~ n까지의 합')

def sum_n2(n):
    return n*(n+1) // 2

print(sum_n2(13))

# Big-O 표기법에 대한 설명 추가 필요

print("----- 최대값 구하기 -----")
def find_max(a):
    n = len(a)    
    maxv = a[0]
    for i in range(1,n):
        if a[i] > maxv:
            maxv = a[i]

    return maxv
d = [17, 92, 33, 58, 7, 32, 100]

print(find_max(d))

print('\n------- 최대 공약수 -------')
# ex) 4, 6의 경우: 모두 2로 나누어 떨어진다. GCD = 2

def gcd_func(a,b):
    i = min(a,b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        else:
            i -=1

print(gcd_func(4,6))

print('\n------- 최대 공약수 by 유클리드 -------')
def gcd_euclid(a,b):
    if b == 0:
        return a
    return gcd_euclid(b, a % b) # 좀 더 작은 값으로 재귀호출.

print(gcd_euclid(748, 34))
