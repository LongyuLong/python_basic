# 기본 자료형 : int, float, bool, complex
# 묶음 자료형 : str, list, tuple, set, dict

# 1) str: 문자열 묶음 자료형, 순서 존재, 수정 불가능
s = 'sequence'
print(s, id(s))                                             # sequence라는 단어에서 첫 글자인 s의 주소를 반환한다
print('길이: ',len(s))
print(s[0], s[2])
print('길이: ',s.find('e'), s.find('e',3), s.rfind('e'))    # s.find('e',3) e를 3번째 원소부터 찾아라

# -- 인덱싱, 슬라이싱
print(s[5])                             # 변수명[순서]. index는 0부터 출발
print(s[2:5])                           # 변수명[구간]. 각각 시작점과 끝점이며 반환값에 시작점과 끝점은 제외
print(s[:], ' ', s[0:len(s)], s[::1])   # s[::1] -> 1씩 증가
print(s[0:7:2])                         # 0~7인덱스를 2간격으로 (매트랩이랑 표기법 다름) 
print(s[-1], ' ', s[-4:-1:1])           # str은 순서가 있기 때문에 음수로 역순을 표시하더라도 잘 된다.

print(s, id(s))
s = 'bequence'                          # 수정이 아니고 변경
print(s, id(s))
s = 'sequenc'

# ------------------------------------------------------------------------------------------------------------------------------#

# 2) list: 다양한 종류의 자료 묶음형, 순서 존재, 수정 가능, 중복 가능
#          배열과 비슷하나 배열은 아님

a = [1, 2, 3]
print(a, a[0], a[0:2])                  # a[0:2] -> a의 0번째부터 2개
b = [10, a, 10, 20.5, True, '문자열']   # str, int, float, bool 모두 같이 들어갈 수 있음.
print(b, ' ', b[1], ' ', b[1][0])       # list 안에 list도 포함 가능.
print()
family = ['엄마','아빠','나','여동생']
print(id(family))
family.append('남동생')                 # 남동생 추가해도 id는 바뀌지않음. str과 다른부분
print(id(family))
print(family)
family.remove('나')                     # append, remove 통해서 추가/삭제 가능
family.insert(0,'할머니')               # 삽입
family.extend(['삼촌','고모','조카'])   # 추가
family += ['이모']                      # 추가

print(family)
print(family.index('아빠'))
print('엄마' in family, '나' in family)

del family[2]                           # del을 써야 list 내에서의 순서로 삭제 가능
print(family)

print()
kbs = ['123','34','234']
kbs.sort()                              # 문자열 정렬 
print(kbs)

mbc = [123,34,234]
mbc.sort(reverse=True)                  # 숫자열 정렬 (ascending sort)
print(mbc)

sbs = [123,34,234]
ytn_sorted = sorted(sbs)
ytn_sort = sbs.sort()
print(sbs)
print(ytn_sorted)
print(ytn_sort)

name = ['tom', 'james', 'oscar']        
name2 = name                            # = 로 연결하면 같은 객체 취급하는데
print(name, id(name))
print(name2, id(name2))

import copy
name3 = copy.deepcopy(name)             # deepcopy로 하면 다른 객체가 됨
print(name3, id(name3))

name[0] = '길동'
print(name)
print(name2)
print(name3)                            # 이미 위에서 복사했으니 여기선 영향없음

# -----------------------------------------------------------------------------------------------------------------------------#

# 3) tuple: list와 유사하나 읽기 전용으로 수정이 안됨

t = (1,2,3,4)                           # t=1,2,3,4로 적어도 똑같다
print(t, type(t))

k = (1)
print(k, type(k))                       # 괄호 안에 하나 밖에 없으면 integer취급한다. tuple로 취급하도록 하려면 (1,)로 작성해야함

print(t[0], ' ', t[0:2])
# t[0] = 77 ---------------------------> tuple은 수정이 불가하므로 TypeError 발생
# tuple 수정하고 싶으면 아래와 같이. tuple을 쓰면 연산 속도가 빨라져서 장점이 없진 않다.
imsi = list(t)
imsi[0] = 77
t = tuple(imsi)
print(t)

# --------------------------------------------------------------------------------------------------------------------------------

# 4) set: 수정 불가, 중복 불가 ex. 웹에서 크롤링해서 정보를 가져왔을 때 중복정보 날릴 때 좋다

ss = {1,2,1,3}
print(ss)
ss_2 = {3,4}
print(ss.union(ss_2))                   # 합집합
print(ss.intersection(ss_2))            # 교집합
print(ss-ss_2, ss | ss_2, ss & ss_2)    # 차집합, 합집합, 교집합
# print(ss[0]) -> TypeError 뜸. 순서란게 없으니까

ss.update({6,7})
print(ss)
ss.discard(7)
ss.remove(6)                            # discard, remove 모두 지우는거. discard는 있으면 지우고 없으면 스킵 // remove는 없으면 에러
print(ss)

li = ['aa','bb','cc','aa','aa']
print(li)
imsi = set(li)
li = list(imsi)
print(li)

#------------------------------------------------------------------------------------------------------------------------------------------

# 5) dict: 사전 자료형 {key: value} 형태 // key로 value를 찾고 인덱싱은 따로 없다 // 
# 방법 1
mydic = dict(k1=1, k2='ok', k3 = 123.4)
print(mydic, type(mydic))

# 방법 2
dic = {'파이썬':'뱀','자바':'커피','인사':'안녕'}
print(dic)
print(len(dic))
print(dic['자바'])                                     # print(dic['커피'])  ->  커피는 value. key가 아니므로 keyError 뜸
ff = dic.get('자바')                                   # 이렇게도 불러올수있다
print(ff)

dic['금요일'] = '와우'                                  # dict에 key를 추가하면서 value 지정
print(dic)
del dic['인사']
print(dic)
print(dic.keys())
print(dic.values())

#--------------------------------------------------------------------------------------------------------------------------------------------



