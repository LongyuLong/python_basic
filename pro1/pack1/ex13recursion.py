'''
카페 python 157번

구분                 for / while 반복문                    재귀(Recursion)            
기본 개념          조건이 참인 동안 반복 실행       함수가 자기 자신을 호출
제어 방식          반복 조건 + 증감식                  종료 조건(Base Case)
종료 시점          조건식이 거짓                         종료 조건 도달
메모리 사용       적음 (스택 증가 없음)               많음 (콜 스택 사용)                           <-이게 중요하다 재귀 장점
실행 흐름          한 함수 안에서 순차 진행          함수 호출 스택을 따라 깊어짐
성능                 일반적으로 빠름                      오버헤드 존재
가독성              반복 구조가 명확                     수학적/논리적 표현이 직관적
디버깅              비교적 쉬움                            스택 추적 필요
Stack Overflow  없음                                       가능                             
대표 사용          배열 순회, 카운트                     트리, 분할 정복
'''

##재귀함수 : 함수가 자기 자신을 호출 - 반복 처리
def countDown(n) :
    if n == 0 :                         ##빠져나올 구멍
        print('완료')
        # return
    else :
        print(n, end = ' ')
        countDown(n-1)                  ##재귀

countDown(5)
print('--------------1부 n까지 정수의 합-------------')
def totFunc(n) :
    if n == 0 :
        print('탈출')
        return 0
    return n + totFunc(n-1)             ##재귀



result = totFunc(5)                     #tot(5) -> 5 + tot(4) -> 4 + tot(3) -> 3 + tot(2) -> 2 + tot(1) -> 1 + tot(0) -> 탈출 ,,, 호출만 함 연산은 안함
print('result : ', result)              #                                       거슬러 올라가면서 연산 1 + 2 + 3 + 4 + 5



print('------5factorial(계승)--------')
def factFunc(a) :
    if a == 0 :
        return 1
    print(a)
    return a * factFunc(a-1)


result = factFunc(500)
print('result : ', result)
print('end')



####모듈을 여러개를 쓸 때에는 메인 모듈이 있다. 메인 모듈은 __main__이라고 해야 됨 응용 모듈들은 아님