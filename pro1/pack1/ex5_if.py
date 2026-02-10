# 조건 판단문 if

var = 1

if var >= 3:

    print('큼')

else:

    print('작음')    

print()
money = 1000
age = 25
if money >= 500:
    item = '사과'
    if age <= 30:
        msg = "참 참"
    else:
        msg = "참 거짓"
else:
    item = '한라봉'
    if age >= 20:
        msg = "거짓 참"
    else:
        msg = "거짓 거짓"

print(f'중복 if 수행 후 결과 {item} {msg}')
print()
# data = input('점수:')                           # 이대로 받으면 str
# score = int(data)                               # str -> int
score = 77
if score >= 90:
    print('우수')
elif score >= 80:
    print('보통')
else:
    print('저조')

jum = 80
if 90 <= jum <= 100:
    print("A")
elif 80 <= jum <= 90:
    print("B")
else:
    print("C")

print('----------------')
names = ["홍길동", '신선해', '이기자']
if '홍길동' in names:
    print("친구 이름이야")
else:
    print("누구야")

if(count := len(names)) >= 5:                   # := -> 대입 표현식. if 문에서 = 를 쓸 때 사용한다.
    print(f"인원수가 {count}명이므로 단체 할인")
else:
    print("아깝다")

scores = [95, 88, 76, 92, 81]

if (avg := sum(scores) / len(scores)) >= 80:
    print(f"우수반: 평균 점수 {avg}")
print('----------------')
print("삼항 연산")

a = 'kbs'
b = 9 if a == 'kbs' else 11
print('b: ', b)

print('----------------')

a = 11
b = 'mbc' if a == 9 else 'kbs'
print('b: ', b)

a = 3
if a < 5:
    print(0)
elif a < 10:
    print(1)
else:
    print(2)



print('end')    



