# 연산자

v1 = 3
v1 = v2 = v3 = 5
print(v1, v2, v3)

print('출력1',end = ',#%') # 줄바꿈 대신 같은 줄에 이어서
print('출력2')
print('출력3')

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('값 할당 : packing 연산')
v1 = 1,2,3,4,5 # v1 = (1,2,3,4,5) 튜플로 작성한 것과 같다.
v1 = [1,2,3,4,5]
# *v1, v2 = [1,2,3,4,5] # packing인데 v1, v2* = [1,2,3,4,5]는 에러 발생
v1, *v2, v3 = [1,2,3,4,5] # 최소한의 성분을 제외하고 *를 붙인 원소에 몰아주기
print(v1,' ', v2, ' ', v3)

print(format(1.5678, '10.3f'))

abc = 123
print(f"abc의 값은{abc}이다")
print() # 빈줄 삽입
print('\n--------------- 본격적 연산 --------------') # \n, \b, \t(탭) ... 

print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 3 ** 3)
# A // B : 정수형 나누기(몫만 취함), A % B : 나누기 후 나머지 반환

print(divmod(5,3), ' ', 5 % 3) # divmod: 내장 함수로 몫과 나머지 표시.
print(3 + 4 * 5 + (2 + 3) / 2) # 소괄호가 1순위. "항을 구분하는 건 더하기 뿐"
result = 3 + 4 * 5 + (2 + 3) /2
#연산자 우선순위 / () -> ** -> 단항 -> 산술 연산자 -> 관계 연산자 -> 논리 연산자(not -> and -> or 순) -> =
print(result)

print(5 > 3, 5 == 3, 5 != 3)

print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3)) # 논리 연산자
print(True or False and False)                      # and가 or보다 연산 우선 순위가 높다 // True 반환
print(True and False or False)                      # False 반환

print(4+5)                  # 산술 연산 // 9 반환
print('4'+"5")              # 문자열 연산 // 45 반환
print("한국"+'만세')         # 한국만세
print("한국"*5 + '만세')     # 한국한국..한국만세

print('누적')
a = 10
a = a+1
a += 1                      # -=, +=, *=, /= 연산도 가능
print(f"a는 {a}") 
print(--a)                  # ++, -- 와 같은 증감 연산자는 없음
print(-a)                   # 부호 변경
print(a * -1)

# print(('1' + '1') + 1)            # TypeError 발생. 문자열 + 숫자 연산
print(int('1') + int('1') + 1)      # 3 반환    // int(문자열) -> 정수화
print(int('1') + float('1') + 1)    # 3.0 반환  // float(문자열) -> 상수화
print(str(1+1)+'1')                 # 21 반환 // 
print('boolen 처리: ', bool(True), bool(False))
print(bool(1), bool(12.3), bool('ok'), bool([12]))
print(bool(0), bool(0.0), bool(''), bool([]), bool(None)) # 전부 false. 데이터가 있어야 true 반환이 나오고, bool에서 0은 유효한 숫자로 보지 않음. 데이터가 없다 라고 보는 거

# r 선행문자
print('aa\tbb')
print('aa\nbb') 
print(r'aa\nbb') # r 선행 -> \n, \t 등의 기능 무시하고 문자열로 취급





