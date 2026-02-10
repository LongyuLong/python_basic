# 매개 변수 유형

# 위치 매개 변수:   인수와 순서대로 대응
# 기본값 매개 변수: 매개 변수에 입력값이 없으면, 기본값 사용
# 키워드 매개 변수: 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개 변수:   인수의 개수가 동적인 경우

def showGugu(start, end=5):                                 # end = 5 이런 식으로 초기값을 주게되면, showGugu(2)로 실행해도 (2,5)로 받아들여진다.
    for dan in range(start, end + 1, 1):
        print(str(dan)+ '단 출력')
        for i in range(1,10):
            print(str(dan)+ "*" + \
                  str(i) + "=" + str(dan * i), end = ' ')
        print()

showGugu(2,3)
print()
showGugu(2)
print()
showGugu(start=7,end=9)
showGugu(end=7,start=9)                                     # 앞뒤 변수 위치가 달라졌지만 키워드 매개변수이므로 상관없다.
showGugu(7,end=9)                                           # 이건 되지만
# showGugu(start=7,9)                                       # 이건 안돼

print("------------가변 매개변수-----------")

def func1(*ar):                                                   # 여러 개의 인자를 tuple로 묶어서 받는다.      
    print(ar)
    for i in ar:
        print('밥 : '+ i)

func1('김밥',"볶음밥", "공기밥","라면")                      # 1개 이상 넣게되면 에러가 뜨지만 def func1(*ar)로 변경하면해결된다1
                                                            # tuple 일 때는 요소가 1개면 ('김밥', ) 으로 전달된다. 잊으면 안된대. 2개부터는 (a,b)식으로 전달되지만 하나는 (a,)

def func2(a,*ar):                                           #첫항만 a, 나머진 *ar로 취급됨    
# def func2(*a,ar):                                           # 이것도 안되고 (*ar, a) 도 안됨    
    print(a)
    print(ar)

func2('김밥','비빔밥')
func2('김밥','비빔밥','볶음밥','공기밥')


print()

def func3(w,h,**other):                                     # **로 표시하면 dict를 받는다
    print(f'몸무게: {w}, 키: {h}')
    print(f'기타: {other}')

func3(80,180,irum='신기루',nai=23)
# func3(80,180,{'irum':'신기루','nai':23})                    # 근데 진짜 dict 양식으로 만들어서 주면 오류남

print()
def func4(a,b,*c,**d):
    print(a,b)
    print(c)
    print(d)

func4(1,2)
func4(1,2,3,4,5)
func4(1,2,3,4,5,kbs=9,mbc=11)                               # 1,2가 a,b로 대응되고 나머지는 *c로, kbs=9,mbc=11와 같은 dict는 **d로

print()
# type hint: 함수의 인자와 반환값에 type을 적어 가독성 향상
def typeFunc(num:int, data:list[str]) -> dict[str, int]:    # int라고 써있지만 1.2를 넣더라도 오류는 안남. 강제성은 없다, 가독성 향상을 위한 장치
    print(num)                                                  
    print(data)
    result = {}
    for idx, item in enumerate(data, start = 1):            # enumerate: 
        print(f'idx:{idx}, item:{item}')
        result[item] = idx
    return result

rdata=typeFunc(1,['일','이','삼'])
print(rdata)

rdata = typeFunc("한개", [10,20,30])
print(rdata)





















































