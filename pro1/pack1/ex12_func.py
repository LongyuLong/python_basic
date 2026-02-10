## 함수 장식자

# 기존 함수 코드를 고치지 않고 함수의 앞/뒤 동작을 추가하기
# 함수를 받아서 기능을 덧붙인 새함수로 바꿔치기하는 것
# meta 기능이 있다. 

def make2(fn):
    return lambda:"안녕" + fn()

def make1(fn):
    return lambda:"반가워" + fn()

def hello():
    return "홍길동"

hi = make2(make1(hello))                            # 장식자 없이 실행
print(hi())

@make2                                              # 장식자
@make1
def hello2():
    return "신기해"

print(hello2())

print('---------------')

def traceFunc(func):
    def wrapperFunc(a,b):
        r = func(a,b)
        print(f"함수명: {func.__name__} (a={a}, b={b} -> {r})")    # __name__은 자신이 종속된 함수/파일의 이름을 반환?
        return r                                                  #함수 반환값을 반환
    return wrapperFunc                                              # 함수 주소 반환 = 클로저


@traceFunc
def addFunc(a,b):
    return a + b

print(addFunc(10,20))


















