# for문

# for i in [1,2,3,4,5]:                                   # 묶음형(list, tuple, dict, ..) 자료를 하나씩 처리. 
# for i in (1,2,3,4,5):
# for i in {1,2,3,4,5}:
#     print(i, end = ' ')

# print("\n\n분산과 표준 편차")                              # 예시는 모두 합이 25, 평균은 5
# # numbers = [1,3,5,7,9]
# # numbers = [3,4,5,6,7]
# numbers = [-3,4,5,7,12]
# total = 0
# for a in numbers:
#     total += a
# print(f"합은 {total}, 평균은 {total/len(numbers)}")
# avg = total/len(numbers)

# # 편차의 합
# hap = 0
# for i in numbers:
#     hap += (i-avg)**2 # **2 >> 제곱
# print(f"편차 제곱의 합: {hap}")

# # 분산
# vari = hap/len(numbers)
# print(f'분산: {vari}')

# #표준편차
# print(f'표준편차: {vari**0.5}')

# print()

# colors = ['r','g', 'b']
# for v in colors:
#     print(v, end = ' ')

# print("iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수")  # 반복 가능한 객체?
# iterator = iter(colors)
# for v in iterator:
#     print(v, end = ', ')
# print('\n')

# for idx, d in enumerate(colors):                                             # enumerate: 인덱스와 값을 반환 // 
#     print(idx, ' ', d)


# print('\n\n사전형 -- dict')
# datas = {'python':'만능언어','java':'웹용언어','MariaDB':'RDBMS(관계형데이터)'} # dict type
# for i in datas.items():
#     # print(i)
#     print(i[0], ' ~~ ', i[0])                                                # key만 나옴

# for k, v in datas.items():                                                   # key, value 다 나옴
#     print(k, ' ~~ ',v)

# for val in datas.values():                                                   # value만 나옴
#     print(val, end = ' ')

# print("------다중 for 문------")

# for n in [2,3]:
#     print('--{}단'.format(n))                                                   # 괄호안에 데이터 넣는 방법 많음
#     for i in [1,2,3,4,5,6,7,8,9]:
#         print('{} * {} = {}'.format(n,i,n*i))

# print('-- continue/break -- ')
# nums = [1,2,3,4,5]
# for i in nums:
#     if i == 2: continue
#     if i == 4: break
#     print(i, end = ' ')
# else:
#     print('정상 종료')

# print('\n\n정규 표현식 + for')

# str = """
# 서울지하철 2·3호선 교대역에서 만난 시민 강아무개(46)씨는 걱정스럽던 마음을 쓸어내리며 광역 버스를 내려 지하철역으로 향했다. 
# 가뜩이나 붐비는 월요일 출근길, 시민들은 밤새 내린 눈에 마음을 졸이며 출근길에 나섰다. 
# 전날 밤부터 이날 새벽까지 서울 지역에도 7cm 이상 눈이 쌓였다. 
# 전날 밤 발령된 대설 주의보는 이날 오전 4시를 기해 해제됐다.
# """

# import re
# str2 = re.sub(r'[^가-힣\s]','',str)                                             # 한글과 공백 이외의 문자는 공백 처리한다
# # print(str2)

# str3 = str2.split(' ')                                                          # 공백을 기준으로 문자열 분리
# # print(str3)

# cou = {}                                                                        # {}로 해놨으니 set 아니면 dict 가 된다
# for i in str3:
#     if i in cou:
#         cou[i] += 1                                                             # 같은 단어가 있으면 누적
#     else:
#         cou[i] = 1                                                              #최초 등장 단어인 경우 '단어':1

# print(cou)

# print("\n\n-------정규 표현식 연습------")

# for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234', '333&1234']:
#     if re.match(r'^\d{3}-\d{4}$', test_ss):                                              # []안에 ^가 있으면 부정(not)으로 사용. 그냥 쓰면 처음이란 의미. $는 마지막
#         print(test_ss, '전화번호 맞아요')
#     else:
#         print(test_ss, '전화번호 아니야')

# print('comprehension: 반복문 + 조건문 + 값 생성을 한 줄로 표현')

# a = [1,2,3,4,5,6,7,8,9,10]
# li = []
# for i in a:
#     if i % 2 == 0:
#         li.append(i)                                                              # 리스트로 만든다
# print(li)

# print(list(i for i in a if i % 2 == 0))                                           # 위 코드와 같은 문장. 

# # datas = [1,2,'a',True,3.0]                                                      
# datas = {1,2,'a',True, 3.0, 2,1,2,1,2,2}                                        # set은 중복허용 안하므로 결과값은 list를 사용했을 때와 다르지 않음
# li2 = [i * i for i in datas if type(i) == int]                                  # comprehension 방식으로 써야할 일이 있나
# print(li2)

# id_name = {1:'tom',2:'oscar'}
# name_id = {val:key for key, val in id_name.items()}                             # key value 맞바꾸기.
# print(name_id)


# print()
# print([1,2,3])
# print(*[1,2,3])                                                                 # * : unpack
# aa = [(1,2), (3,4), (5,6)]                                                      # list 안에 tuple
# for a, b in aa:                                                                 # aa가 tuple이고 자동으로 a,b가 자동으로 원소로 잡히는듯
#     print(a+b)

# print(*[a+b for a, b in aa], sep = ' ')                                        # 짧게 쓸 수 있는 장점은 있는듯 / end = ' ' 처럼 sep = '\n' 근데 sep이랑 end랑 아예 똑같은 기능인듯

# print('\n수열 생성: range')
# print(list(range(1,6)))                                                        # [1,2,3,4,5]로 반환. range(a,b) = a 이상 b 미만
# print(tuple(range(1,6,2)))                                                        # (1,3,5)로 반환. range(a,b,c) = a 이상 b 미만, 간격 c
# print(set(range(1,6,3)))

# for i in range(6):                                                              # 초기값 안주면 0 시작
#     print(i, end = ' ')


# for _ in range(6):                                                              # 꼭 i와 같은 변수가 필요한건 아님
#     print('반복')

# tot = 0
# for i in range(1,11):
#     tot += i
# print('tot: ', tot)                                                             # sum(range(1,11))해도되고

# for i in range(1,10):
#     print(f'2 * {i} = {2*i}')


## for문 예제

# Q1. 구구단 2~9단 출력 (단은 행단위 출력 -- end = ' ' 쓰면될듯)

for i in range(2,10):
    print()
    for a in range(1,10):
        print(f'{i}*{a}={a*i}', end = ' ')
    
print('\n\n')
# Q2. 주사위를 두번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력

for x in range(1,7):
    for y in range(1,7):
        dice = x+y
        if dice % 4 == 0:
            print(f'{y}+{x}={x+y}', end = ' ')

    




print('\nend')