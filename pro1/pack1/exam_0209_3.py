# [문항3] 반복문 for를 사용 : 1 ~ 100 사이의 숫자 중 3의 배수 또는 4의 배수 이고 
# 7의 배수가 아닌 수를 출력하고 건수와 합도 출력하는 코드를 작성하시오


a = 0; b = 0; c = []

for i in range(0,100):
    a += 1
    if a % 3 == 0:
        continue
    elif a % 4 == 0:
        continue
    else:
        print(a, end = ' ')
        c.append(a)
        b += a
        

print("\n건수: ",len(c))
print("총합: ",b)

