# closure: Scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블럭,
# 내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조하기 ? 

def funcTimes(a,b):
    c = a*b                                                         # 함수 내에서 선언했으니까 c는 지역변수다.
    return c
print(funcTimes(2,3))
#  print(c)                                                         # c가 지역변수니까 프린트 해봣자 안나온다

kbs = funcTimes(2,3)
print(kbs)
kbs=funcTimes
print(kbs)
print(kbs(2,3))
print(id(kbs),id(funcTimes))
mbc = sbs = kbs
del funcTimes                                                       # 삭제
print(mbc(2,3))

## 클로저 : 자신이 태어난 환경(변수 등)을 기억하고 있는 함수
print('\n------클로저를 사용하지 않은 경우------')

def out():
    count = 0
    def inn():
        nonlocal count
        count +=1
        return count
    print(inn())

out()
out()

print('\n------클로저를 사용하는 경우------')


def outer():
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner                                                # 이게 클로저다. 내부 함수의 주소를 반환한다.

var1 = outer()                                                  # 내부 함수의 주소를 변수에 저장
print('var1 주소: ',var1)
print(var1())
print(var1())                                                   # 클로저를 사용하지 않았을 때는 1, 1로 출력됐으나 클로저를 사용했을 때는 1,2로 출력되었다.

myvar = var1()
print(myvar)
print()

var2 = outer()                                                  # 새로운 객체(새로운 inner 함수) 생성        
print(var2())                                                   # 같은 걸 쓰지만 별개다.
print(var2())

print(var1,var2)                                                # inner에 대한 주소를 받아서 출력하는데, 서로 주소가 다름.

print("수량 * 단가 * 세금 결과를 출력하는 함수 작성")

def outer2(tax):                                                # 여기서 선언한 변수 tax는 지역변수
    def inner2(su,dan):
        amount = su * dan * tax
        return amount
    return inner2                                               # 클로저.

# 1분기에는 su * dan 에 대한 tax=0.1 부과
q1 = outer2(0.1)                                                # inner2의 주소 기억
result1 = q1(5,50000)
print('result1: ',result1)
result2 = q1(2,10000)
print('result2: ',result2)

q2 = outer2(0.05)                                               #
result3 = q2(5,50000)
print('result3: ',result3)
result4 = q2(2,10000)
print('result4: ',result4)

print('\n일급 함수: 함수 안의 함수. 인자로 함수 전달하고 반환값도 함수')
def func1(a,b):
    return a+b

func2 = func1
print(func1(3,4))
print(func2(3,4))

print()

def func3(fu):
    def func4():
        print('나는 내부 함수야')
    func4()
    return fu                                                   # 반환값이 함수인데..fu 자리에 func1이 들어갔고..

mbc = func3(func1)
print(mbc(3,4))

print('\n축약함수(Lambda function): 이름이 없는 한 줄짜리 함수')

# 형식: lambda 매개 변수들 나열(...) :반환식   << return 없이 결과 반환

def hapFunc(x,y):
    return x+y
print(hapFunc(1,2))

# 람다로 표현
print((lambda x , y : x+y)(1,2))                               # 람다를 써서 코드 간소화..

gg = lambda x, y: x+y
print(gg(1,2))


kbs = lambda a, su=10: a+su                                    # 이쪽 놓쳤음     


# sbs(1,2,3,var1 = 4,var2 = 5)

li = [lambda a,b: a+b, lambda a,b: a*b]

print(li[0](3,4))
print(li[1](3,4))

print('\n다른 함수에서 람다 사용하기')
# filter(함수, 반복가능한 객체)
print(list(filter(lambda a: a<5, range(10))))
print(list(filter(lambda a: a%2, range(10))))

# 문) filter사용해서 1~100 사이의 정수 중 5의 배수이거나 7의 배수만 출력

print(list(filter(lambda a: a % 5==0 or a % 7==0, range(101))))







