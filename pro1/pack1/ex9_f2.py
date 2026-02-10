## 사용자 정의 함수
"""
def 함수명(가인수, , , , ..):
    # ABCDEF..
    return 반환값           # 1개만 반환, return이 없으면 return None

함수명(실인수)              # 함수 호출
"""

def doFunc1():
    print('doFunc1 수행')

def doFunc2(name):
    print('name: ',name)
    # return None 이 원래 있어야하는데, 생략 가능하다.

def doFunc3(arg1, arg2):
    re = arg1 + arg2
    return re

def doFunc4(a1,a2):
    imsi = a1 + a2
    if imsi % 2 == 1:
        return
    else:
        return imsi

    
doFunc1()
print('함수 주소는 doFunc1', doFunc1)                        # <function doFunc1 at 0x000001E96D0EF920> 참조형이라서 반환으로 주소를 찍는다
print('함수 주소는 doFunc1', id(doFunc1))                    # 2146582001952
print(doFunc1())                                            # None -- 결과로 낼 게 없으면 none 반환 ㅇㅇ
imsi = doFunc1
imsi()                                                            # imsi = doFunc1 로 선언하고 나면 imsi()로 doFunc1 대체할 수 있음
print("------------------")
doFunc2("길동")                                              #

print("------------------")
doFunc3("대한", "민국")
print(doFunc3("대한", "민국"))
print(doFunc3(5,6))
result = doFunc3("5","6")
print(result)

print(doFunc4(3,4))
print(doFunc4(3,5))

print('----------------')
def triArea(a, b):
    c = 0.5 * a * b
    triAreaPrint(c)                                             # 여기서 호출하는데 syntax error 안뜸

def triAreaPrint(cc):                                           # 
    print('삼각형의 면적은 ', cc)

triArea(20,30)

def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else:
        return False

if passResult(20, 10):                                          # 반환값을 True, False 로 설정했을 때 if에서 True면 통과, False 면 Else측으로 간다.
    print('합격')
else:
    print('불합격')

print()
def swapFunc(a, b):
    return b, a                                                 # return (b,a)랑 동일한 표현임. 함수의 반환값은 한 덩어리여야함.

a = 10; b = 20
print(a, ' ', b)
print(swapFunc(a,b))

print()
def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('     내부 함수')
    funcInner()

funcTest()

#-------------------------------------------------------------------

# if 조건식 안에 함수 사용
def isOdd(para):
    return para % 2 == 1                                        # 홀수이면 True 반환

mydict = {x:x*x for x in range(11) if isOdd(x)}                 # isOdd가 True/False 반환하므로 if에서 True 반환 받았을 때만 dict에 추가된다.
print(mydict)


print('-----변수의 생존 범위(scope rule)-----')
# 변수가 저장되는 이름 공간은 변수가 어디서 선언되었는가에 따라 생존 시간이 다르다  << ?
# 전역 / 지역 변수

player = '전국대표'                                               # 전역변수(현재 모듈 어디서든 호출 가능)
name = '한국인'

def funcSoccer():                                                # 지역변수. (해당 함수 내에서만 호출 가능)           
    name = "홍길동"                 
    # player = "지역대표"                                         # 여길 주석처리하면 전역변수 player = 전국대표 를 가져와서 쓴다 // 지역변수가 없으면 전역변수를 찾는다
    city = "서울"
    print(f'이름은 {name}, 수준은 {player}, 소속은 {city}')

funcSoccer()

print(f'이름: {name}, 수준: {player}')
# print(f'지역: {city}')                                          # city는 funcSoccer 내에서 선언되었으므로 그 밖에서는 호출할 수 없음.


#-------------------------------------------------------------------



print()

a= 10; b= 20; c= 30
def Foo():
    a=7
    b=100
    def Bar():
        global c                                                # global로 변수 선언하면 모듈(파일) 단위의 멤버가 됨. a,b의 경우는 지역변수. c는 전역변수 
        nonlocal b                                              # nonlocal b : 가장 가까운 상위 함수의 변수까지 영향
        b=8
        print(f'Bar 수행 후 a:{a}, b:{b},c:{c}')
        c=9                                                     # c=9 선언하면 지역변수로 바뀌진 않지만 값은 변경 된다
        b=200
    Bar()
    print(f'Foo 수행 후 a:{a}, b:{b},c:{c}')

Foo()
print(f'함수 수행 후 a:{a}, b:{b},c:{c}')

#-------------------------------------------------------------------


print()

g = 1
def func():
    a = g
    # g = 2                                                       # 위에서 a=g를 하고 g=2를 다시 주면 에러가 난다 UnboundLocalError: cannot access local variable 'g' where it is not associated with a value
    return a                                                    # g=2를 a=g 위로 올리거나 g=2를 지우면 에러 사라짐.


print(func())

print()

g = 1
print('g: ',g)
def func():
    global g
    a = g
    g = 2
    return a
print(func())
print('g: ',g)

#-------------------------------------------------------------------






