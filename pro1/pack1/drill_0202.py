# Q1. 1~100사이 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고 합을 출력
print("\n\nQ1. 1~100사이 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고 합을 출력")
total_sum = 0

for i in range(1,101):
    if i % 3 == 0:
        k=i
        if k % 2 == 1:
            total_sum += k
            print(k, end = ' ')
            

print("sum: ", total_sum)

# Q2. 구구단 2~5단
print("\n\nQ2. 구구단 2~5단")
for x in range(2,6):
    print()
    for y in range(1,10):
        print(f'{x}*{y}={x*y}', end = ' ')


print("\n\nQ3. 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력") ##
total_sum = 0
positive = 0
negative = 0
for i in range(1,101):
    if i % 2 == 1:
        negative += -i
    elif i % 2 == 0:
        positive += i
total_sum = positive + negative
print("Total: ", total_sum)

print("\n\nQ4. -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력")     ## 복습
k = 0
for i in range(1,51):
    k += (2*i - 1)*(-1)**i
    
print("sum(k): ",k)

print("\n\nQ5. 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력") ## 복습
digit = []
for i in range(1,101):
    digit = [int(d) for d in str(i)]
    if sum(digit) >= 10:
        print("10 넘는 경우: ",i)

print("\n\nQ6. 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력 힌트: 언제 멈출지 미리 모름 → while 적합")
a = 0; n = 0
while a < 1000:
    n += 1
    a += n

print("누적 1000초과: ",n, "합: ",a)

print("\n\nQ7. 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동") ## 복습

for x in range(2,10):
    print()
    for y in range(1,10):
        if x*y <= 30:
            print(f'{x}*{y}={x*y}', end = ' ')


print("\n\nQ8. 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력 \n힌트: 이 문제는 반복이 두 단계다. 2부터 1000까지 하나씩 검사한다. 각 숫자마다 소수인지 확인한다.그래서 while 안에 while 구조가 필요하다.​") ## 복습
a=1; count = 0
while a < 1000:
    a += 1
    divider = 2
    sosu = True
    while divider < a:
        if a % divider == 0:
            sosu = False
            break
        divider += 1
    if sosu == True:
        print(a, end = ' ')
        count += 1
print(f"\n소수의 개수: ",count)

print("\n\nContinue Q1. 1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라") ## 복습

a = 0
while a < 50:
    a += 1
    if a % 3 == 0:
        continue
    print(a, end = " ")

print("\n\nContinue Q2. 1부터 100까지 출력하되 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력하라") ## 복습

a = 0; total = 0
while a < 100:
    a += 1
    if a % 4 == 0 or a % 6 == 0:
        continue
    elif a % 5 == 0:
        print(a, end = ' ')
        total += a
print("\n4와 6의 배수를 제외한 5의 배수의 합: ", total)







