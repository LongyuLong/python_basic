# [문항11] tom은 그림과 같은 모양의 *(별 문자)을 출력하고 싶어 한다.
# while문을 사용하여 tom이 원하는 별 모양을 출력하는 코드를 작성하시오.

# 조건 : 10행 10열 (배점:10)

# print('\n별 찍기 ------')

star = 1
while star <= 10:
    j=10
    msg = ""
    while j >= star:
        msg += "*"
        j -= 1
    print(str(msg).rjust(10))
    star += 1
