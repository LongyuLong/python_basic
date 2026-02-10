# a = 1
# while a <= 5:
#     print(a, end = ' ') ## 1 2 3 4 5 처럼 가로로 출력할 때 사용
#     a = a+1
# else:
#     print('완료')

# print()
# i = 1
# while i <= 3:
#     j=1
#     while j <= 4:
#         print("i="+str(i) + '/j=' + str(j))
#         j = j + 1
#     i = i + 1

# print('1 ~ 100 사이의 정수 중 3의 배수의 합 ---')
# su = 1; hap = 0
# while su <= 100:
#     # print(i)
#     if su % 3 == 0:
#         # print(i)
#         hap += su # hap = hap + i 랑 같긴한데 왼쪽 사용 권장
#     su += 1
# print('합은 ',hap)

# print()

# colors = ["빨강", "파랑", "노랑"]

# # print(colors[0])
# # print(colors[1])
# # print(colors[2])
# # num = 0
# # print(colors[num])
# num = 0
# while num < len(colors):
#     print(colors[num])
#     num += 1

# # 다중 while문

# print('\n별 찍기 ------')

# star = 1
# while star <= 10:
#     j=1
#     msg = ""
#     while j <= star:
#         msg += "*"
#         j += 1
#     print(msg)
#     star += 1

# print('if block 안에 while문----')

# import time
# sw = input('폭탄 스위치를 누를까요? [Y/N]')             # input.api 에서는 숫자를 입력하더라도 str로 취급된다
# # print("sw: ", sw)
# if sw == 'y' or 'Y':
#     count = 5
#     while 1 <= count:
#         print("%d초 남았습니다."%count)                # %d 일 때는 콤마 뒤에 변수넣는게 아니고 %변수
#         time.sleep(1)                                 # time.sleep(n) >> n초 후 다음 문장 실행
#         count -=1
#     print("폭발")

# elif sw == 'N' or 'n':
#     print("취소")
# else:
#     print("Y or N을 누르세요")

print("\ncontinue/break")

a = 0
while a < 10:
    a += 1
    if a == 3:                                          # continue: 아래 문을 무시하고 while로 이동
        continue
    if a == 5:
        continue
    # if a == 7:                                          # break: while문 탈출
    #     break
    print(a)
else:
    print('정상 종료')                                  # while문이 break 없이 종료되면 else로 이동. break로 종료되면 else 실행 안함.
print('while 수행 후 %d'%a)

print("\n키보드로 숫자를 입력 받아 홀수 짝수 확인하기(무한 반복) ---")
while True:                                             # True, 1, 100, -12.4, 'ok' >> 값이라는게 존재하면 True이므로 해당 while문은 무한 반복된다. >> break로 탈출
    mysu = int(input('확인할 숫자 입력(ex: 5): '))
    if mysu == 0:
        print("종료")
        break
    elif mysu % 2 == 0:
        print("%d는 짝수"%mysu)
    elif mysu % 2 == 1:
        print("%d는 홀수"%mysu)





print('end')